# LLM Evals Notes (MVP)

## Objective

The objective of this repo is to collect good evals (LLM evals) related resources and have them in context so that an AI (I) can easily think about evals and ask questions about evals on this knowledge base using Cursor or any other AI tools. Also maybe later, convert it into an MCP (Model Context Protocol) so that other agents can also connect to this content easily.

Curate URLs about LLM evaluation, scrape to clean Markdown with metadata, and maintain a simple catalog. 

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

## CI: Submit a URL via urls.txt
- This repo includes a GitHub Action that runs the scraper automatically when `urls.txt` changes on the `main` branch.
- How to submit a URL:
  - Edit `urls.txt` on `main` (commit directly or merge a PR) and add a single URL per line.
  - Once pushed to `main`, the action will:
    - Set up Python 3.12 with `uv`
    - Run `uv run scripts/scrape.py refresh`
    - Open a PR with updates to `content/**` and `data/catalog.json` (if any changes)
- Manual trigger: You can also run the workflow via the Actions tab (workflow_dispatch).
- Secrets: The action uses the repository secret `FIRECRAWL_API_KEY`.

### PR behavior and forks
- The workflow is configured to run only on pushes to `main` (plus manual dispatch).
- PRs (including from forks) that modify `urls.txt` do not automatically run the scrape; the scrape happens after the change lands on `main` or when triggered manually.

## Behavior (scraping & overwrite)
- On refresh, previously scraped URLs are skipped by default to save credits. Use `--force` to re-scrape.
- When content changes, the existing `content/{slug}.md` is overwritten (no hash suffix in filename). Git history tracks changes.

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
  