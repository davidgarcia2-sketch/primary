# Trello MCP server

stdio MCP server that wraps common [Trello REST API](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/) operations. Use it from Cursor or any MCP client that supports process-based servers.

## Credentials

1. Open [Trello Power-Ups admin](https://trello.com/power-ups/admin), select or create a Power-Up, and copy the **API key**.
2. Generate a **token** from the same screen (Trello will prompt you to authorize scopes).

Set environment variables wherever you configure the server:

- `TRELLO_API_KEY` — public API key  
- `TRELLO_API_TOKEN` — secret token (treat like a password)

## Install and build

```bash
cd trello-mcp
npm install
npm run build
```

## Run

```bash
cd trello-mcp
TRELLO_API_KEY=... TRELLO_API_TOKEN=... node dist/index.js
```

## Cursor configuration

Add to your MCP settings (merge into your existing `mcpServers` object):

```json
"trello": {
  "command": "node",
  "args": ["/absolute/path/to/repo/trello-mcp/dist/index.js"],
  "env": {
    "TRELLO_API_KEY": "your_key",
    "TRELLO_API_TOKEN": "your_token"
  }
}
```

Use the real absolute path to `dist/index.js` on your machine.

## Tools

| Tool | Purpose |
|------|---------|
| `trello_list_boards` | Boards for the current member |
| `trello_get_board` | Board details by ID |
| `trello_list_lists` | Lists on a board |
| `trello_list_cards` | Cards on a list |
| `trello_get_card` | Card by ID |
| `trello_create_card` | Create a card on a list |
| `trello_update_card` | Patch a card (including `idList` to move) |
| `trello_add_comment` | Comment on a card |
| `trello_search` | `/1/search` across models |
| `trello_archive_card` | Set `closed: true` |
| `trello_delete_card` | Permanent delete |

## Security

Keep `TRELLO_API_TOKEN` out of source control. Prefer OS keychain, a secrets manager, or Cursor env blocks that are not committed.
