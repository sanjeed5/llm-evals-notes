# MVP TODO — LLM Evals Notes (Firecrawl + uv)

Goal: Collect LLM evals URLs, scrape to clean Markdown with metadata, and maintain a simple catalog. MCP later.

## Phase 0 — Decisions
- [x] Scraper: Firecrawl SDK (Python)
- [x] Env/packaging: uv
- [x] Scope now: URLs → Markdown in `content/` + `data/catalog.json`

## Phase 1 — Project setup
- [x] Create folders: `content/`, `data/`, `scripts/`, `logs/`
- [x] Add `urls.txt` (one URL per line)
- [x] Initialize Python project with uv
  - [x] `uv init --package llm_evals_notes`
  - [x] `uv add firecrawl-py python-slugify pyyaml requests`
- [x] Secrets
  - [x] Create `.env.example` with `FIRECRAWL_API_KEY=`
  - [x] Read `FIRECRAWL_API_KEY` from env in code

## Phase 2 — Scraper (Firecrawl)
- [x] Implement `scripts/scrape.py` CLI:
  - [x] `add <url>`: append to `urls.txt` (dedupe) and fetch once
  - [x] `refresh`: iterate all URLs in `urls.txt` and fetch
  - [x] Flags: `--force` (ignore cache), `--timeout`
- [x] For each URL:
  - [x] Use Firecrawl `scrape_url` with `formats=['markdown']`
  - [x] Extract `title`, `sourceURL`, `statusCode` from metadata
  - [x] Generate slug from title, prefixed with root domain to avoid collisions
  - [x] Compute content hash (e.g., SHA256 of markdown)
  - [x] Write `content/{slug}.md` with YAML frontmatter: title, source_url, source_domain, date_fetched, hash
  - [x] Update `data/catalog.json`: title, path, url, hash, fetched_at
  - [x] Idempotent: if hash unchanged and not `--force`, skip write
- [x] Errors & logs
  - [x] Retries/backoff and sensible timeouts
  - [x] Log failures to `logs/scrape.log`

## Phase 3 — Developer UX
- [x] `README.md` with quickstart
  - [x] `uv run scripts/scrape.py add <url>`
  - [x] `uv run scripts/scrape.py refresh`
- [x] Document file structure and frontmatter
- [x] Add `.gitignore` for `.venv/`, `__pycache__/`, `logs/`

## Optional (after MVP)
- [x] URL normalization/deduping for `urls.txt`

## Later
- [ ] Minimal MCP server exposing `list_docs`, `get_doc`, `search`

## Phase 4 — CI (Scrape on urls.txt changes)
- [x] Trigger
  - [x] Run on push when only `urls.txt` changes
  - [x] Allow manual dispatch
- [x] Runtime
  - [x] Use Python `3.12` (respect `.python-version`)
  - [x] Use `uv` for dependency install and run
- [x] Execution
  - [x] Run `uv sync --frozen`
  - [x] Run `uv run scripts/scrape.py refresh` with `FIRECRAWL_API_KEY` from GitHub Actions secrets
- [x] Output handling
  - [x] Open a PR with any changes in `content/**` and `data/catalog.json`
  - [x] Use a dedicated CI branch per run, auto-delete after merge
  - [x] Do not include `logs/` or unrelated files in the PR
- [x] Permissions & safety
  - [x] `contents: write`, `pull-requests: write`
  - [x] Concurrency to avoid overlapping runs per ref
  - [x] No schedule for now

## Phase 5 — Cost & overwrite behavior
- [x] Skip re-scraping previously scraped URLs during refresh unless `--force` is provided (saves Firecrawl credits)
- [x] Overwrite existing `content/{slug}.md` instead of creating hash-suffixed files when content changes

### Acceptance criteria (CI)
- [x] A push that changes `urls.txt` triggers the workflow
- [x] If scraping produces changes, a PR is created with only `content/**` and `data/catalog.json`
- [x] If nothing changes, no PR is opened
- [x] Workflow uses Python 3.12 and `uv` and reads `FIRECRAWL_API_KEY` from repo secrets

## Acceptance criteria
- [x] `uv run scripts/scrape.py refresh` creates Markdown files in `content/` with frontmatter
- [x] `data/catalog.json` lists docs with path, url, title, hash, fetched_at
- [x] Re-running without `--force` skips unchanged content via hash
- [x] Adding a URL via `add` updates files and catalog

## Reference
- Firecrawl Quickstart and SDK: https://docs.firecrawl.dev/introduction
