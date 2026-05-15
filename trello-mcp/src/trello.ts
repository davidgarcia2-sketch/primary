const TRELLO_API = "https://api.trello.com/1";

export type TrelloCredentials = {
  key: string;
  token: string;
};

function appendAuth(
  url: URL,
  { key, token }: TrelloCredentials,
  extra?: Record<string, string | undefined>,
): void {
  url.searchParams.set("key", key);
  url.searchParams.set("token", token);
  if (extra) {
    for (const [k, v] of Object.entries(extra)) {
      if (v !== undefined && v !== "") url.searchParams.set(k, v);
    }
  }
}

export async function trelloGet<T>(
  creds: TrelloCredentials,
  path: string,
  query?: Record<string, string | undefined>,
): Promise<T> {
  const url = new URL(`${TRELLO_API}/${path.replace(/^\//, "")}`);
  appendAuth(url, creds, query);
  const res = await fetch(url);
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Trello ${res.status}: ${body || res.statusText}`);
  }
  return (await res.json()) as T;
}

export async function trelloPostJson<T>(
  creds: TrelloCredentials,
  path: string,
  body: Record<string, unknown>,
  query?: Record<string, string | undefined>,
): Promise<T> {
  const url = new URL(`${TRELLO_API}/${path.replace(/^\//, "")}`);
  appendAuth(url, creds, query);
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Trello ${res.status}: ${text || res.statusText}`);
  }
  return (await res.json()) as T;
}

export async function trelloPostForm<T>(
  creds: TrelloCredentials,
  path: string,
  fields: Record<string, string>,
  query?: Record<string, string | undefined>,
): Promise<T> {
  const url = new URL(`${TRELLO_API}/${path.replace(/^\//, "")}`);
  appendAuth(url, creds, query);
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams(fields),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Trello ${res.status}: ${text || res.statusText}`);
  }
  return (await res.json()) as T;
}

export async function trelloPutJson<T>(
  creds: TrelloCredentials,
  path: string,
  body: Record<string, unknown>,
  query?: Record<string, string | undefined>,
): Promise<T> {
  const url = new URL(`${TRELLO_API}/${path.replace(/^\//, "")}`);
  appendAuth(url, creds, query);
  const res = await fetch(url, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Trello ${res.status}: ${text || res.statusText}`);
  }
  return (await res.json()) as T;
}

export async function trelloDelete(
  creds: TrelloCredentials,
  path: string,
  query?: Record<string, string | undefined>,
): Promise<void> {
  const url = new URL(`${TRELLO_API}/${path.replace(/^\//, "")}`);
  appendAuth(url, creds, query);
  const res = await fetch(url, { method: "DELETE" });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Trello ${res.status}: ${text || res.statusText}`);
  }
}
