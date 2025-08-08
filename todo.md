# MVP TODO — LLM Evals Notes (Firecrawl + uv)

Goal: Collect LLM evals URLs, scrape to clean Markdown with metadata, and maintain a simple catalog. MCP later.

## Phase 0 — Decisions
- [x] Scraper: Firecrawl SDK (Python)
- [x] Env/packaging: uv
- [x] Scope now: URLs → Markdown in `content/` + `data/catalog.json`

## Phase 1 — Project setup
- [ ] Create folders: `content/`, `data/`, `scripts/`, `logs/`
- [ ] Add `urls.txt` (one URL per line)
- [ ] Initialize Python project with uv
  - [x] `uv init --package llm_evals_notes`
  - [ ] `uv add firecrawl-py python-slugify pyyaml requests`
- [ ] Secrets
  - [ ] Create `.env.example` with `FIRECRAWL_API_KEY=`
  - [ ] Read `FIRECRAWL_API_KEY` from env in code

## Phase 2 — Scraper (Firecrawl)
- [ ] Implement `scripts/scrape.py` CLI:
  - [ ] `add <url>`: append to `urls.txt` (dedupe) and fetch once
  - [ ] `refresh`: iterate all URLs in `urls.txt` and fetch
  - [ ] Flags: `--force` (ignore cache), `--timeout`
- [ ] For each URL:
  - [ ] Use Firecrawl `scrape_url` with `formats=['markdown']`
  - [ ] Extract `title`, `sourceURL`, `statusCode` from metadata
  - [ ] Generate slug from title or domain+path
  - [ ] Compute content hash (e.g., SHA256 of markdown)
  - [ ] Write `content/{slug}.md` with YAML frontmatter: title, source_url, source_domain, date_fetched, hash
  - [ ] Update `data/catalog.json`: title, path, url, hash, fetched_at
  - [ ] Idempotent: if hash unchanged and not `--force`, skip write
- [ ] Errors & logs
  - [ ] Retries/backoff and sensible timeouts
  - [ ] Log failures to `logs/scrape.log`

## Phase 3 — Developer UX
- [ ] `README.md` with quickstart
  - [ ] `uv run scripts/scrape.py add <url>`
  - [ ] `uv run scripts/scrape.py refresh`
- [ ] Document file structure and frontmatter
- [ ] Add `.gitignore` for `.venv/`, `__pycache__/`, `logs/`

## Optional (after MVP)
- [ ] Naive search command over titles/content
- [ ] `data/summary.md` linking all docs
- [ ] URL normalization/deduping for `urls.txt`

## Later
- [ ] Minimal MCP server exposing `list_docs`, `get_doc`, `search`
- [ ] CI to auto-refresh on `urls.txt` changes

## Acceptance criteria
- [ ] `uv run scripts/scrape.py refresh` creates Markdown files in `content/` with frontmatter
- [ ] `data/catalog.json` lists docs with path, url, title, hash, fetched_at
- [ ] Re-running without `--force` skips unchanged content via hash
- [ ] Adding a URL via `add` updates files and catalog

## Reference
- Firecrawl Quickstart and SDK: https://docs.firecrawl.dev/introduction
