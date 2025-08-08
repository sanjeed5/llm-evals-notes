## Objective
Create a curated, context-rich knowledge base of LLM evaluation resources so an AI (via Cursor or other tools) can reason about evals and answer questions over this corpus. Ultimately expose the corpus via the Model Context Protocol (MCP) so other agents can connect to it.

## Workflow
- **Maintain URL list**: Keep a canonical list of relevant links.
- **Ingest to Markdown**: When a new URL is added, scrape it to `.md` and store it in the repo.
- **Expose via MCP**: Publish the corpus through MCP so external agents can access it easily.