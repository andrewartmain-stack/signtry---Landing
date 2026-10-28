# SignTry landing site

Static HTML/CSS/JS marketing site for signtry.com (app: app.signtry.com).

## Rules
- More than 3 pages, new pages or research: send a short plan first and wait for a go-ahead.
- Don't read big files whole (`css/site.css`, the Semrush CSV, media). Use Grep or a script.
- Screenshots and web searches only when needed. Keep replies short. Commit only when asked.
- Only claim features that exist in the app. No fake testimonials, no fake logos.

## Pages
- `index.html` is hand-written. `pricing.html`, `guides.html`, `blog.html`, `privacy/terms/gdpr.html`, `features/`, `guides/`, `examples/` and `posts/` are **generated**: edit `tools/site/p_*.py`, not the HTML. Legal text lives in `tools/site/legal/`; blog posts in `tools/site/blog/` (add a post: its HTML body + an entry in `posts.json`).
- `free-email-signature-generator.html` is hand-written and self-contained (own CSS/JS); it loads only `css/chrome.css` for the shared navbar/footer.
- Shared navbar, footer and components: `tools/site/layout.py`. Styles: `css/site.css`. Scripts: `js/site.js`.

```bash
python tools/site/build.py       # rebuild generated pages
python tools/site/sync_index.py  # copy navbar/footer into index.html
python tools/site/check.py       # test, must exit 0
python tools/site/sitemap.py     # regenerate sitemap.xml after adding pages
```

## SEO
Keyword from `generate_email_signature_green_kd.csv` in the title (≤ 60 chars), H1 and first paragraph. Meta description ≤ 155 chars. Add new pages to `sitemap.xml`.

## Pricing
Subscription per signature, all features on every plan. Source of truth: `TIERS` in `tools/site/p_pricing.py`.

## Planned
Free builder under "Generate your free email signature": 2 templates, no photo, no save, no tracking.
