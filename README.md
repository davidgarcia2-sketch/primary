# Salesforce Web-to-Lead test site

Static test page that embeds a Salesforce Web-to-Lead form for org `00D1N000001BsY8`.

## Shareable URL (GitHub Pages)

After this branch is merged to `main`, enable Pages once:

1. Repo **Settings → Pages**
2. Source: **GitHub Actions**
3. Site URL will be: `https://davidgarcia2-sketch.github.io/primary/`

You can also run the **Deploy GitHub Pages** workflow manually from the Actions tab.

## Run locally

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

## Form behavior

- Posts to `https://webto.salesforce.com/servlet/servlet.WebToLead`
- On success, Salesforce redirects to `http://therealreal.com` (`retURL`)
- To test without creating live leads, uncomment the `debug` / `debugEmail` hidden inputs in `index.html`
