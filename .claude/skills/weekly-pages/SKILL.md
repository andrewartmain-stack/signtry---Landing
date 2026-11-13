---
name: weekly-pages
description: Weekly SEO content run for signtry.com. "/weekly-pages plan" proposes the next 5 pages from docs/content-plan.md, "/weekly-pages" writes them on a content branch with links, build and checks, "/weekly-pages publish" merges, pushes and lists URLs for Google Search Console.
---

# Weekly pages (SignTry)

Goal: 5 new pages a week that each deserve to rank. Quality beats the count: if a topic can't be
done well (no real substance, feature doesn't exist), say so and propose a replacement.
Follow `CLAUDE.md` (only claim features that exist, no fake testimonials) and the
`write-content` skill rules (anti-slop list, no invented numbers, quick answer first).
Reply to the owner in the language they write in, short.

Week id = ISO year + week, e.g. `2026-w47`. Branch = `content/2026-w47`.

## `/weekly-pages plan`

1. Read `docs/content-plan.md`. Rows with Status `todo` are candidates.
2. If fewer than 5 `todo` rows: analyse `generate_email_signature_green_kd.csv` with a short Python
   script (never read it whole), group keywords by intent, drop topics already covered by
   `tools/site/links.py` PAGES, and append new rows (cluster volume, main keywords, type).
3. Pick 5: highest cluster volume first, but keep a mix of guides/examples, and prefer topics that
   strengthen an existing cluster (Outlook, Gmail, design, examples).
4. Show a table: # · title · URL · type · main keyword (vol/KD) · 1-line angle. Wait for OK or swaps.
5. On OK: set those rows to `planned 2026-wNN`.

## `/weekly-pages` (write)

1. `git switch -c content/<week>` from an up-to-date `main`.
2. For each planned page, one at a time:
   - Read the top 5 Google results (WebSearch + fetch) and note format, gaps, PAA questions.
     Verify every product-specific step against official docs (Microsoft, Google, Apple...).
   - Write it as a dict in the matching generator: guides → `tools/site/p_guides.py`
     (`article_page`), examples → `tools/site/p_examples.py`. Use the house blocks: `answer()`,
     `toc()`, `h2()`, `steps()`, `table()`, `callout()`, `fig()`, `faqs`. Title ≤ 60, meta ≤ 155,
     keyword in title, H1 and lead.
   - Images: product stills from `media/stills/` where they fit, or a schematic SVG in
     `images/guides/` labelled "Illustration". Never fake screenshots of other products.
   - Links: add the page to `PAGES` and `RELATED` in `tools/site/links.py` (6 related), to
     `GUIDES`/`EXAMPLES` in `tools/site/build.py`, and add one in-text link to it from 1–2
     existing related pages. Source paths keep `.html`; `clean_urls()` handles output.
3. Run `python tools/site/build.py && python tools/site/sync_index.py && python tools/site/sitemap.py && python tools/site/check.py` (must exit 0).
4. Visual check: `python -m http.server 8765` in the repo, screenshot each new page at 390px and
   1440px with Playwright (installed in `C:/Users/andre/Desktop/websites-organizer/node_modules/@playwright/test`),
   confirm no horizontal scroll and no console errors. Stop the server afterwards.
5. Commit on the branch: `content: <week> — <5 short titles>`.
6. Report: the 5 URLs, word count each, and a "please verify" list (any fact you could not
   confirm from an official source). Push the branch only if the owner wants a Vercel preview.

## `/weekly-pages publish`

1. Only after the owner says the pages are OK. Merge the branch into `main` (fast-forward),
   rerun `sitemap.py` + `check.py`, commit if the sitemap changed, `git push origin main`.
2. Wait until each new URL returns 200 on https://signtry.com (curl), check its canonical.
3. Set the rows in `docs/content-plan.md` to `published YYYY-MM-DD`, commit and push.
4. Give the owner the list for Google Search Console → URL Inspection → Request indexing
   (one URL at a time, ~10 per day limit). No sitemap resubmission needed.
