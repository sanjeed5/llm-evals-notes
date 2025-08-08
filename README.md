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
- Refresh all URLs from `urls.txt`:
  ```sh
  uv run scripts/scrape.py refresh
  ```
- Flags:
  - `--force` overwrite even if content hash unchanged
  - `--timeout <seconds>` per-request timeout

## File structure
- `urls.txt`: canonical list of URLs (one per line)
- `content/`: scraped Markdown files (`{slug}.md`)
- `data/catalog.json`: catalog of docs
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

## Notes
- Idempotent: re-running without `--force` skips writes when `hash` matches.
- On errors, retries with exponential backoff (3 attempts) and logs to `logs/scrape.log`.