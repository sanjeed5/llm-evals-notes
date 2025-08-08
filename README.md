# LLM Evals Notes (MVP)

Curate URLs about LLM evaluation, scrape to clean Markdown with metadata, and maintain a simple catalog. Later: expose via MCP.

## Quickstart

1) Install uv (one-time)
- Linux/macOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Then: `source $HOME/.local/bin/env`

2) Install deps
- `uv sync`

3) Configure API key
- Copy `.env.example` to `.env` and set `FIRECRAWL_API_KEY`.

4) Run commands
- Add and fetch a single URL:
  ```sh
  uv run scripts/scrape.py add https://example.com/article
  ```
- Refresh all URLs from `urls.txt` (also normalizes and dedupes them):
  ```sh
  uv run scripts/scrape.py refresh
  ```
- Flags:
  - `--force` overwrite even if content hash unchanged
  - `--timeout <seconds>` per-request timeout (converted to ms for the SDK)

## File structure
- `urls.txt`: canonical list of URLs (one per line)
- `content/`: scraped Markdown files (`{slug}.md`)
- `data/catalog.json`: catalog of docs (paths are repo-relative)
- `logs/scrape.log`: scrape log
- `scripts/scrape.py`: CLI

## Markdown frontmatter
Each `content/{slug}.md` starts with YAML:
```yaml
---
# human-friendly title
title: ...
# original URL and domain
source_url: ...
source_domain: ...
# ISO timestamp
date_fetched: ...
# SHA256 of markdown body
hash: ...
---
```

## Behavior
- Idempotent writes via content hash: re-running without `--force` skips when `hash` matches.
- Retries with exponential backoff (3 attempts) on transient errors; logs to `logs/scrape.log`.
- URL normalization on refresh and add: ensures https scheme, drops fragments, removes default ports, collapses slashes, strips `index.html`, trims trailing slashes (except root); writes back normalized, deduped `urls.txt`.
- Catalog entries use repo-relative `path` values.

## Slug naming and collisions
- Slugs are prefixed with the root domain to reduce cross-site title collisions, e.g. `hamel-dev-your-ai-product-needs-evals-hamel-s-blog`.
- Existing slugs in the catalog are preserved to avoid churn.
- If a slug file exists but content changes (true collision), a short `-<hash6>` suffix is appended to the filename.