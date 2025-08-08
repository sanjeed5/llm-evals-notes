#!/usr/bin/env python3
import argparse
import hashlib
import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from slugify import slugify
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
DATA_DIR = ROOT / "data"
LOGS_DIR = ROOT / "logs"
URLS_FILE = ROOT / "urls.txt"
CATALOG_FILE = DATA_DIR / "catalog.json"

DEFAULT_TIMEOUT_SECONDS = 60


@dataclass
class ScrapeResult:
    title: str
    source_url: str
    source_domain: str
    status_code: Optional[int]
    markdown: str


def configure_logging() -> None:
    """
    Configure logging to output messages to both the console and a log file in the logs directory.
    """
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOGS_DIR / "scrape.log"),
        ],
    )


def read_env() -> None:
    # Load .env if present so FIRECRAWL_API_KEY can be set locally
    """
    Loads environment variables from a `.env` file located at the project root, enabling local configuration such as the Firecrawl API key.
    """
    load_dotenv(ROOT / ".env")


def load_urls() -> List[str]:
    """
    Load and return a list of URLs from the `urls.txt` file.
    
    Returns:
        List of non-empty, stripped URLs. Returns an empty list if the file does not exist.
    """
    if not URLS_FILE.exists():
        return []
    with URLS_FILE.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def save_urls(urls: List[str]) -> None:
    """
    Write a sorted, deduplicated list of URLs to the `urls.txt` file.
    
    Parameters:
        urls (List[str]): List of URLs to save.
    """
    lines = "\n".join(sorted(set(urls))) + "\n" if urls else ""
    URLS_FILE.write_text(lines, encoding="utf-8")


def normalize_url(url: str) -> str:
    """
    Normalize a URL by enforcing HTTPS scheme, lowercasing scheme and domain, removing default ports, fragments, redundant slashes, trailing slashes (except for root), and index.html/htm suffixes.
    
    Parameters:
        url (str): The URL to normalize.
    
    Returns:
        str: The normalized URL.
    """
    url = url.strip()
    if not url:
        return url
    if not re.match(r"^https?://", url, flags=re.IGNORECASE):
        url = f"https://{url}"
    parts = urlsplit(url)
    scheme = parts.scheme.lower() or "https"
    netloc = parts.netloc.lower()
    # drop default ports
    if netloc.endswith(":80") and scheme == "http":
        netloc = netloc[:-3]
    if netloc.endswith(":443") and scheme == "https":
        netloc = netloc[:-4]
    # remove fragment
    path = parts.path or "/"
    # collapse multiple slashes in path
    path = re.sub(r"/{2,}", "/", path)
    # remove index.html/htm at end
    path = re.sub(r"/(index\.html?|index\.htm)$", "/", path, flags=re.IGNORECASE)
    # remove trailing slash except for root
    if path != "/":
        path = path.rstrip("/")
    query = parts.query
    return urlunsplit((scheme, netloc, path, query, ""))


def compute_hash(markdown: str) -> str:
    """
    Compute the SHA-256 hash of a Markdown string.
    
    Parameters:
        markdown (str): The Markdown content to hash.
    
    Returns:
        str: The hexadecimal SHA-256 hash of the input Markdown.
    """
    return hashlib.sha256(markdown.encode("utf-8")).hexdigest()


def ensure_catalog() -> Dict[str, Dict]:
    """
    Ensures the catalog file exists and returns its contents as a dictionary.
    
    If the catalog file is missing or contains invalid JSON, returns a new catalog dictionary with an empty "items" list.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if CATALOG_FILE.exists():
        try:
            return json.loads(CATALOG_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            logging.warning("catalog.json is invalid JSON; starting fresh")
    return {"items": []}


def write_catalog(catalog: Dict[str, Dict]) -> None:
    """
    Write the catalog dictionary to the catalog JSON file in the data directory as pretty-printed UTF-8 JSON.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CATALOG_FILE.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def safe_slug(text: str, fallback: str) -> str:
    """
    Generate a URL-safe slug from the given text, using a fallback or a hash if necessary.
    
    If `text` is empty or produces an empty slug, the function uses the `fallback` string. If both result in an empty slug, a SHA-1 hash of the fallback is used (truncated to 10 characters).
    
    Parameters:
        text (str): The primary string to slugify.
        fallback (str): The fallback string to use if `text` is empty or cannot be slugified.
    
    Returns:
        str: A URL-safe slug derived from `text`, `fallback`, or a hash of `fallback`.
    """
    base = slugify(text) if text else slugify(fallback)
    return base or slugify(fallback) or hashlib.sha1(fallback.encode()).hexdigest()[:10]


def extract_domain(url: str) -> str:
    """
    Extracts and returns the domain portion from a given URL string.
    
    Parameters:
        url (str): The URL from which to extract the domain.
    
    Returns:
        str: The domain name extracted from the URL.
    """
    return re.sub(r"^https?://([^/]+).*$", r"\1", url)


def generate_slug(title: str, url: str, content_hash: Optional[str] = None) -> str:
    """
    Generate a filename slug based on the URL's domain and the provided title or last path segment.
    
    If the title is empty, uses the last segment of the URL path or the domain. Falls back to a SHA-1 hash if no slug can be generated. Optionally accepts a content hash for collision avoidance, but does not append it unless needed elsewhere.
    
    Parameters:
        title (str): The page title to use for slug generation.
        url (str): The source URL for extracting the domain and path.
        content_hash (Optional[str]): Optional content hash for collision avoidance.
    
    Returns:
        str: A slug suitable for use as a filename.
    """
    domain = extract_domain(url)
    title_slug = slugify(title) if title else ""
    # derive from last path segment if title empty
    path = urlsplit(url).path or "/"
    last_seg = path.rstrip("/").split("/")[-1] if path != "/" else domain
    base_slug = title_slug or slugify(last_seg) or slugify(domain)
    slug = slugify(f"{domain}-{base_slug}")
    if not slug:
        slug = hashlib.sha1((domain + base_slug).encode()).hexdigest()[:10]
    # Optionally append short hash for collision avoidance
    if content_hash:
        short = content_hash[:6]
        slug = f"{slug}"
        # only add short suffix later if needed upon collision
    return slug


def frontmatter_yaml(meta: Dict[str, str]) -> str:
    """
    Generate a YAML frontmatter string from a metadata dictionary.
    
    Parameters:
        meta (Dict[str, str]): Metadata to include in the YAML frontmatter.
    
    Returns:
        str: A string containing the YAML frontmatter delimited by '---' lines.
    """
    import yaml  # local import to keep import list tidy

    return "---\n" + yaml.safe_dump(meta, sort_keys=False).strip() + "\n---\n\n"


def scrape_once(app: FirecrawlApp, url: str, timeout: int) -> ScrapeResult:
    # Firecrawl SDK (>=2.x) returns a ScrapeResponse pydantic model with attributes
    """
    Scrapes a single URL using the Firecrawl API and returns the result as a ScrapeResult.
    
    Attempts to extract Markdown content, title, source URL, HTTP status code, and domain from the response. Falls back to metadata or input values if necessary.
    
    Parameters:
        url (str): The URL to scrape.
        timeout (int): Timeout in seconds for the scrape operation.
    
    Returns:
        ScrapeResult: An object containing the scraped Markdown, title, source URL, domain, and status code.
    """
    timeout_ms = int(timeout * 1000) if timeout else None
    resp = app.scrape_url(url, formats=["markdown"], timeout=timeout_ms)

    # Primary content
    markdown = getattr(resp, "markdown", None) or ""

    # Metadata/title/url
    title_attr = getattr(resp, "title", None) or ""
    metadata = getattr(resp, "metadata", {}) or {}
    title = (title_attr or (metadata.get("title") if isinstance(metadata, dict) else "") or "").strip()

    # Prefer response.url, then metadata.sourceURL, else the input url
    resp_url = getattr(resp, "url", None)
    source_url_meta = resp_url or (metadata.get("sourceURL") if isinstance(metadata, dict) else None) or url

    # Best-effort status code if present in metadata
    status_code = None
    if isinstance(metadata, dict):
        status_code = metadata.get("statusCode") or metadata.get("status_code")
        try:
            status_code = int(status_code) if status_code is not None else None
        except Exception:
            status_code = None

    if not title:
        # Fallback: derive from domain/path
        path_part = re.sub(r"^https?://", "", source_url_meta).rstrip("/")
        title = path_part

    domain = extract_domain(source_url_meta)
    return ScrapeResult(
        title=title,
        source_url=source_url_meta,
        source_domain=domain,
        status_code=status_code,
        markdown=markdown,
    )


def write_markdown_file(slug: str, result: ScrapeResult, content_hash: str) -> Path:
    """
    Write a Markdown file with YAML frontmatter and scraped content to the content directory.
    
    Parameters:
    	slug (str): The filename slug for the Markdown file.
    	result (ScrapeResult): The result of the scrape operation containing metadata and Markdown content.
    	content_hash (str): The SHA-256 hash of the Markdown content.
    
    Returns:
    	Path: The path to the written Markdown file.
    """
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    meta = {
        "title": result.title,
        "source_url": result.source_url,
        "source_domain": result.source_domain,
        "date_fetched": datetime.now(timezone.utc).isoformat(),
        "hash": content_hash,
    }
    fm = frontmatter_yaml(meta)
    path = CONTENT_DIR / f"{slug}.md"
    path.write_text(fm + result.markdown, encoding="utf-8")
    return path


def upsert_catalog_item(catalog: Dict[str, Dict], *, title: str, path: Path, url: str, content_hash: str) -> None:
    """
    Insert or update an item in the catalog's "items" list with the given title, relative file path, URL, content hash, and fetch timestamp.
    
    If an item with the same URL or file path exists, its metadata is updated; otherwise, a new item is appended.
    """
    items: List[Dict] = catalog.setdefault("items", [])
    # find by url if present; else by path
    existing = next((it for it in items if it.get("url") == url or it.get("path") == str(path)), None)
    try:
        rel_path = path.relative_to(ROOT)
    except Exception:
        rel_path = path
    record = {
        "title": title,
        "path": str(rel_path),
        "url": url,
        "hash": content_hash,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }
    if existing:
        existing.update(record)
    else:
        items.append(record)


def refresh_all(urls: List[str], *, force: bool, timeout: int) -> None:
    """
    Scrapes and updates Markdown files for a list of URLs, maintaining idempotency and catalog consistency.
    
    For each URL, normalizes and fetches content using the Firecrawl API with retries and exponential backoff. Skips writing files if content is unchanged unless forced. Handles slug generation and collision avoidance, writes Markdown files with metadata, and updates the catalog JSON. Logs progress and errors. Requires the FIRECRAWL_API_KEY environment variable.
    """
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        logging.error("FIRECRAWL_API_KEY is not set. Provide it via environment or .env file.")
        sys.exit(1)
    app = FirecrawlApp(api_key=api_key)

    catalog = ensure_catalog()

    for raw_url in urls:
        url = normalize_url(raw_url)
        try:
            logging.info("Fetching %s", url)
            # simple retries with exponential backoff
            last_exc: Optional[Exception] = None
            result: Optional[ScrapeResult] = None
            for attempt in range(1, 4):
                try:
                    result = scrape_once(app, url, timeout)
                    break
                except Exception as exc:  # noqa: BLE001
                    last_exc = exc
                    backoff = 2 ** (attempt - 1)
                    logging.warning("Attempt %d failed for %s: %s. Retrying in %ss", attempt, url, exc, backoff)
                    time.sleep(backoff)
            if result is None:
                raise last_exc or RuntimeError("Unknown error during scrape")
            if not result.markdown:
                logging.warning("No markdown returned for %s; skipping", url)
                continue

            # determine slug — preserve existing from catalog if present
            existing_item = None
            for it in catalog.get("items", []):
                if it.get("url") == url and it.get("path"):
                    existing_item = it
                    break
            if existing_item:
                existing_path = Path(existing_item["path"]).name
                slug = existing_path[:-3] if existing_path.endswith(".md") else existing_path
            else:
                # compute content hash first for potential collision suffix
                tentative_hash = compute_hash(result.markdown)
                slug = generate_slug(result.title, url, content_hash=tentative_hash)

            # idempotency via hash
            new_hash = compute_hash(result.markdown)
            md_path = CONTENT_DIR / f"{slug}.md"
            # if path exists but content changed and slug collision risk, append short hash
            if md_path.exists():
                existing_text = md_path.read_text(encoding="utf-8")
                m0 = re.search(r"^---[\s\S]*?\nhash:\s*([0-9a-f]{64})\n[\s\S]*?---\n", existing_text)
                if not m0 or (m0 and m0.group(1) != new_hash):
                    md_path = CONTENT_DIR / f"{slug}-{new_hash[:6]}.md"

            if md_path.exists() and not force:
                # parse existing hash from frontmatter
                existing_text = md_path.read_text(encoding="utf-8")
                m = re.search(r"^---[\s\S]*?\nhash:\s*([0-9a-f]{64})\n[\s\S]*?---\n", existing_text)
                if m:
                    old_hash = m.group(1)
                    if old_hash == new_hash:
                        logging.info("Unchanged: %s (slug=%s)", url, slug)
                        upsert_catalog_item(catalog, title=result.title, path=md_path, url=url, content_hash=new_hash)
                        continue

            path = write_markdown_file(slug if md_path.stem == slug else md_path.stem, result, new_hash)
            upsert_catalog_item(catalog, title=result.title, path=path, url=url, content_hash=new_hash)
            logging.info("Wrote %s", path)
        except Exception as exc:  # noqa: BLE001
            logging.exception("Failed to fetch %s: %s", url, exc)

    write_catalog(catalog)


def cmd_add(url: str, *, force: bool, timeout: int) -> None:
    """
    Adds a URL to the list if not already present, saves the updated list, and scrapes the URL into a Markdown file.
    
    Parameters:
        url (str): The URL to add and scrape.
        force (bool): If True, forces re-scraping even if content is unchanged.
        timeout (int): Timeout in seconds for the scraping operation.
    """
    urls = load_urls()
    url = normalize_url(url)
    if url not in urls:
        urls.append(url)
        save_urls(urls)
        logging.info("Added URL: %s", url)
    else:
        logging.info("URL already present: %s", url)
    refresh_all([url], force=force, timeout=timeout)


def cmd_refresh(*, force: bool, timeout: int) -> None:
    """
    Refreshes all URLs in the list by scraping their content and updating Markdown files and the catalog.
    
    Normalizes and deduplicates URLs from `urls.txt`, saves changes if needed, and invokes the scraping process for each URL with the specified options.
    """
    urls = load_urls()
    if not urls:
        logging.info("No URLs in urls.txt")
        return
    # Normalize and dedupe urls.txt on refresh
    normalized = sorted({normalize_url(u) for u in urls if u.strip()})
    if normalized != urls:
        save_urls(normalized)
        logging.info("Normalized and deduped urls.txt (%d → %d)", len(urls), len(normalized))
    refresh_all(normalized, force=force, timeout=timeout)


def build_parser() -> argparse.ArgumentParser:
    """
    Builds and returns the command-line argument parser for the scraping tool.
    
    The parser supports two subcommands:
    - `add`: Adds a URL to the list and fetches its content.
    - `refresh`: Fetches content for all URLs in the list.
    
    Returns:
        argparse.ArgumentParser: The configured argument parser for the CLI.
    """
    parser = argparse.ArgumentParser(description="Scrape URLs to Markdown using Firecrawl")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a URL to urls.txt and fetch once")
    p_add.add_argument("url", help="URL to add and fetch")
    p_add.add_argument("--force", action="store_true", help="Ignore cache and overwrite if unchanged")
    p_add.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS, help="Per-request timeout seconds")

    p_refresh = sub.add_parser("refresh", help="Fetch all URLs from urls.txt")
    p_refresh.add_argument("--force", action="store_true", help="Ignore cache and overwrite if unchanged")
    p_refresh.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS, help="Per-request timeout seconds")

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """
    Entry point for the command-line tool, handling argument parsing and dispatching to the appropriate command.
    
    Parameters:
        argv (Optional[List[str]]): List of command-line arguments to parse. If None, uses sys.argv.
    
    Returns:
        int: Exit code (0 for success).
    """
    configure_logging()
    read_env()

    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        cmd_add(args.url, force=args.force, timeout=args.timeout)
    elif args.command == "refresh":
        cmd_refresh(force=args.force, timeout=args.timeout)
    else:
        parser.error("Unknown command")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())