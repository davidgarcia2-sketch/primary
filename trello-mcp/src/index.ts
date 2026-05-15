#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import type { TrelloCredentials } from "./trello.js";
import {
  trelloDelete,
  trelloGet,
  trelloPostForm,
  trelloPostJson,
  trelloPutJson,
} from "./trello.js";

function requireEnv(name: string): string {
  const v = process.env[name];
  if (!v?.trim()) {
    throw new Error(
      `Missing ${name}. Set TRELLO_API_KEY and TRELLO_API_TOKEN (see trello-mcp/README.md).`,
    );
  }
  return v.trim();
}

function creds(): TrelloCredentials {
  return {
    key: requireEnv("TRELLO_API_KEY"),
    token: requireEnv("TRELLO_API_TOKEN"),
  };
}

function jsonText(data: unknown): { content: Array<{ type: "text"; text: string }> } {
  return {
    content: [{ type: "text", text: JSON.stringify(data, null, 2) }],
  };
}

const tools = [
  {
    name: "trello_list_boards",
    description:
      "List boards for the authenticated member. Optional filters: filter=all|open|closed|members|organization|public|starred|unpinned.",
    inputSchema: {
      type: "object",
      properties: {
        filter: {
          type: "string",
          description: "Board filter (default: open).",
        },
      },
    },
  },
  {
    name: "trello_get_board",
    description: "Get a single board by ID.",
    inputSchema: {
      type: "object",
      properties: {
        boardId: { type: "string", description: "Short Trello board ID." },
      },
      required: ["boardId"],
    },
  },
  {
    name: "trello_list_lists",
    description: "List lists on a board.",
    inputSchema: {
      type: "object",
      properties: {
        boardId: { type: "string", description: "Board ID." },
        filter: {
          type: "string",
          description: "List filter: all|open|closed (default: open).",
        },
      },
      required: ["boardId"],
    },
  },
  {
    name: "trello_list_cards",
    description: "List cards on a list.",
    inputSchema: {
      type: "object",
      properties: {
        listId: { type: "string", description: "List ID." },
        filter: {
          type: "string",
          description: "Card filter: all|open|closed|visible (default: open).",
        },
      },
      required: ["listId"],
    },
  },
  {
    name: "trello_get_card",
    description: "Get a card by ID.",
    inputSchema: {
      type: "object",
      properties: {
        cardId: { type: "string", description: "Card ID." },
      },
      required: ["cardId"],
    },
  },
  {
    name: "trello_create_card",
    description: "Create a new card on a list.",
    inputSchema: {
      type: "object",
      properties: {
        listId: { type: "string", description: "Target list ID." },
        name: { type: "string", description: "Card title." },
        desc: { type: "string", description: "Optional description (markdown)." },
        due: {
          type: "string",
          description: "Optional ISO 8601 due date.",
        },
        pos: {
          type: "string",
          description: "Position: top, bottom, or a number string.",
        },
      },
      required: ["listId", "name"],
    },
  },
  {
    name: "trello_update_card",
    description:
      "Update a card (partial). Common fields: name, desc, due (ISO or null to clear), idList to move, closed (boolean), pos.",
    inputSchema: {
      type: "object",
      properties: {
        cardId: { type: "string", description: "Card ID." },
        updates: {
          type: "object",
          description: "Fields to merge onto the card (Trello card JSON shape).",
          additionalProperties: true,
        },
      },
      required: ["cardId", "updates"],
    },
  },
  {
    name: "trello_add_comment",
    description: "Add a comment to a card.",
    inputSchema: {
      type: "object",
      properties: {
        cardId: { type: "string", description: "Card ID." },
        text: { type: "string", description: "Comment text." },
      },
      required: ["cardId", "text"],
    },
  },
  {
    name: "trello_search",
    description: "Search boards, cards, and members (Trello /1/search).",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Search query string." },
        modelTypes: {
          type: "string",
          description:
            "Comma-separated: actions,boards,cards,members,organizations (default: cards,boards).",
        },
        boardIds: {
          type: "string",
          description: "Optional comma-separated board IDs to scope search.",
        },
        cardLimit: {
          type: "string",
          description: "Max cards to return (string for schema simplicity).",
        },
      },
      required: ["query"],
    },
  },
  {
    name: "trello_archive_card",
    description: "Archive (close) a card.",
    inputSchema: {
      type: "object",
      properties: {
        cardId: { type: "string", description: "Card ID." },
      },
      required: ["cardId"],
    },
  },
  {
    name: "trello_delete_card",
    description: "Permanently delete a card (destructive).",
    inputSchema: {
      type: "object",
      properties: {
        cardId: { type: "string", description: "Card ID." },
      },
      required: ["cardId"],
    },
  },
] as const;

async function main(): Promise<void> {
  requireEnv("TRELLO_API_KEY");
  requireEnv("TRELLO_API_TOKEN");

  const server = new Server(
    { name: "trello-mcp", version: "1.0.0" },
    { capabilities: { tools: {} } },
  );

  server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: [...tools] }));

  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const c = creds();
    const args = (request.params.arguments ?? {}) as Record<string, unknown>;

    try {
      switch (request.params.name) {
        case "trello_list_boards": {
          const filter =
            typeof args.filter === "string" && args.filter ? args.filter : "open";
          const data = await trelloGet(c, "members/me/boards", { filter });
          return jsonText(data);
        }
        case "trello_get_board": {
          const boardId = String(args.boardId ?? "");
          const data = await trelloGet(c, `boards/${encodeURIComponent(boardId)}`);
          return jsonText(data);
        }
        case "trello_list_lists": {
          const boardId = String(args.boardId ?? "");
          const filter =
            typeof args.filter === "string" && args.filter ? args.filter : "open";
          const data = await trelloGet(c, `boards/${encodeURIComponent(boardId)}/lists`, {
            filter,
          });
          return jsonText(data);
        }
        case "trello_list_cards": {
          const listId = String(args.listId ?? "");
          const filter =
            typeof args.filter === "string" && args.filter ? args.filter : "open";
          const data = await trelloGet(c, `lists/${encodeURIComponent(listId)}/cards`, {
            filter,
          });
          return jsonText(data);
        }
        case "trello_get_card": {
          const cardId = String(args.cardId ?? "");
          const data = await trelloGet(c, `cards/${encodeURIComponent(cardId)}`);
          return jsonText(data);
        }
        case "trello_create_card": {
          const listId = String(args.listId ?? "");
          const name = String(args.name ?? "");
          const body: Record<string, unknown> = { idList: listId, name };
          if (typeof args.desc === "string") body.desc = args.desc;
          if (typeof args.due === "string" && args.due) body.due = args.due;
          if (typeof args.pos === "string" && args.pos) body.pos = args.pos;
          const data = await trelloPostJson(c, "cards", body);
          return jsonText(data);
        }
        case "trello_update_card": {
          const cardId = String(args.cardId ?? "");
          const updates = args.updates;
          if (!updates || typeof updates !== "object" || Array.isArray(updates)) {
            throw new Error("updates must be a JSON object");
          }
          const data = await trelloPutJson(
            c,
            `cards/${encodeURIComponent(cardId)}`,
            updates as Record<string, unknown>,
          );
          return jsonText(data);
        }
        case "trello_add_comment": {
          const cardId = String(args.cardId ?? "");
          const text = String(args.text ?? "");
          const data = await trelloPostForm(
            c,
            `cards/${encodeURIComponent(cardId)}/actions/comments`,
            { text },
          );
          return jsonText(data);
        }
        case "trello_search": {
          const query = String(args.query ?? "");
          const modelTypes =
            typeof args.modelTypes === "string" && args.modelTypes
              ? args.modelTypes
              : "cards,boards";
          const q: Record<string, string | undefined> = {
            query,
            modelTypes,
          };
          if (typeof args.boardIds === "string" && args.boardIds) {
            q.idBoards = args.boardIds;
          }
          if (typeof args.cardLimit === "string" && args.cardLimit) {
            q.cards_limit = args.cardLimit;
          }
          const data = await trelloGet(c, "search", q);
          return jsonText(data);
        }
        case "trello_archive_card": {
          const cardId = String(args.cardId ?? "");
          const data = await trelloPutJson(c, `cards/${encodeURIComponent(cardId)}`, {
            closed: true,
          });
          return jsonText(data);
        }
        case "trello_delete_card": {
          const cardId = String(args.cardId ?? "");
          await trelloDelete(c, `cards/${encodeURIComponent(cardId)}`);
          return jsonText({ ok: true, cardId });
        }
        default:
          throw new Error(`Unknown tool: ${request.params.name}`);
      }
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      return {
        content: [{ type: "text", text: message }],
        isError: true,
      };
    }
  });

  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
