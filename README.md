# Berlin Notebook — World Health Summit 2026

A record of the World Health Summit (Berlin, 12–14 October 2026) from three
delegates: an interactive map of how the sessions connect, five themes, and a
browsable archive of all thirteen sessions with the notes taken in the room.

Live: https://sasaigoli05.github.io/whs-berlin-2026/

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | The page source. No `<!doctype>` or `<head>` — those are supplied by the Claude artifact platform. |
| `build.py` | Wraps `index.html` into a standalone page in `docs/`. |
| `docs/` | What GitHub Pages serves (Settings → Pages → main / docs). Generated — don't edit by hand. |

## Editing

Edit `index.html`, then:

```
python3 build.py
git commit -am "..." && git push
```

Pages redeploys from `docs/` on every push to `main`. The page carries `noindex`, so it stays out of
search results while remaining readable to anyone with the link.
