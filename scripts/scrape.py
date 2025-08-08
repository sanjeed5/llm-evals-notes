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
    load_dotenv(ROOT / ".env")


def load_urls() -> List[str]:
    if not URLS_FILE.exists():
        return []
    with URLS_FILE.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def save_urls(urls: List[str]) -> None:
    lines = "\n".join(sorted(set(urls))) + "\n" if urls else ""
    URLS_FILE.write_text(lines, encoding="utf-8")


def normalize_url(url: str) -> str:
    url = url.strip()
    if not re.match(r"^https?://", url):
        url = f"https://{url}"
    # strip anchors and trailing slashes duplication
    url = re.sub(r"#.*$", "", url)
    url = re.sub(r"/{2,}$", "/", url)
    return url


def compute_hash(markdown: str) -> str:
    return hashlib.sha256(markdown.encode("utf-8")).hexdigest()


def ensure_catalog() -> Dict[str, Dict]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if CATALOG_FILE.exists():
        try:
            return json.loads(CATALOG_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            logging.warning("catalog.json is invalid JSON; starting fresh")
    return {"items": []}


def write_catalog(catalog: Dict[str, Dict]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CATALOG_FILE.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def safe_slug(text: str, fallback: str) -> str:
    base = slugify(text) if text else slugify(fallback)
    return base or slugify(fallback) or hashlib.sha1(fallback.encode()).hexdigest()[:10]


def extract_domain(url: str) -> str:
    return re.sub(r"^https?://([^/]+).*$", r"\1", url)


def frontmatter_yaml(meta: Dict[str, str]) -> str:
    import yaml  # local import to keep import list tidy

    return "---\n" + yaml.safe_dump(meta, sort_keys=False).strip() + "\n---\n\n"


def scrape_once(app: FirecrawlApp, url: str, timeout: int) -> ScrapeResult:
    # Firecrawl docs: scrape_url(url, formats=["markdown"]) returns dict with 'content' and 'metadata'
    resp = app.scrape_url(url, formats=["markdown"])  # type: ignore[arg-type]
    # Possible shapes have evolved; handle common variants
    markdown = resp.get("content") or resp.get("markdown") or ""
    metadata = resp.get("metadata") or {}
    title = metadata.get("title") or metadata.get("metadata", {}).get("title") or ""
    status_code = metadata.get("statusCode") or metadata.get("status_code")
    source_url_meta = metadata.get("sourceURL") or url
    if not title:
        # Fallback: derive from domain/path
        path_part = re.sub(r"^https?://", "", url).rstrip("/")
        title = path_part
    domain = extract_domain(source_url_meta)
    return ScrapeResult(
        title=title.strip(),
        source_url=source_url_meta,
        source_domain=domain,
        status_code=int(status_code) if status_code is not None else None,
        markdown=markdown,
    )


def write_markdown_file(slug: str, result: ScrapeResult, content_hash: str) -> Path:
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
    items: List[Dict] = catalog.setdefault("items", [])
    # find by url if present; else by path
    existing = next((it for it in items if it.get("url") == url or it.get("path") == str(path)), None)
    record = {
        "title": title,
        "path": str(path),
        "url": url,
        "hash": content_hash,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }
    if existing:
        existing.update(record)
    else:
        items.append(record)


def refresh_all(urls: List[str], *, force: bool, timeout: int) -> None:
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

            # determine slug
            fallback = extract_domain(url) + "/" + re.sub(r"[^a-zA-Z0-9]+", "-", url.split("/", 3)[-1]).strip("-")
            slug = safe_slug(result.title, fallback=fallback)

            # idempotency via hash
            new_hash = compute_hash(result.markdown)
            md_path = CONTENT_DIR / f"{slug}.md"
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

            path = write_markdown_file(slug, result, new_hash)
            upsert_catalog_item(catalog, title=result.title, path=path, url=url, content_hash=new_hash)
            logging.info("Wrote %s", path)
        except Exception as exc:  # noqa: BLE001
            logging.exception("Failed to fetch %s: %s", url, exc)

    write_catalog(catalog)


def cmd_add(url: str, *, force: bool, timeout: int) -> None:
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
    urls = load_urls()
    if not urls:
        logging.info("No URLs in urls.txt")
        return
    refresh_all(urls, force=force, timeout=timeout)


def build_parser() -> argparse.ArgumentParser:
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