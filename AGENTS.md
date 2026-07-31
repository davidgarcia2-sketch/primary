# AGENTS.md

## Cursor Cloud specific instructions

- As of this writing, the `main` branch of this repository is effectively empty: it contains only `README.md` (whose contents are the single word `primary`). There is no application code, no package manager manifest (`package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, etc.), no services, no database, no build system, and no lint/test configuration.
- There is therefore nothing to install, build, lint, test, or run end-to-end on `main`. The environment update/startup script is intentionally a no-op until real project code lands.
- Real/experimental work lives only on unmerged `cursor/*` feature branches (e.g. sprint-retrospective and weekly-status reporting artifacts, and an experimental TypeScript Trello MCP server under `trello-mcp/` on `cursor/trello-mcp-server-91b2`). These are not part of the `main` checkout and are not a single coherent, runnable product.
- When actual project code is added to `main`, update this section and the environment update script accordingly (add the dependency-install command for the chosen package manager, plus notes on how to run/lint/test the service).
