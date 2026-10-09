# Salesforce Web-to-Lead test site

Static test page that embeds a Salesforce Web-to-Lead form for org `00D1N000001BsY8`.

## Run locally

```bash
# any static server works; for example:
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

## Form behavior

- Posts to `https://webto.salesforce.com/servlet/servlet.WebToLead`
- On success, Salesforce redirects to `http://therealreal.com` (`retURL`)
- To test without creating live leads, uncomment the `debug` / `debugEmail` hidden inputs in `index.html`
