# Content plan (from generate_email_signature_green_kd.csv, Nov 2026)

Volumes are monthly US searches summed over the keyword cluster. KD ≤ 29 for everything in the CSV.
Weekly run: `/weekly-pages plan` → `/weekly-pages` → `/weekly-pages publish` (5 pages a week).
Status: `todo` → `planned 2026-wNN` → `published YYYY-MM-DD`. Check Search Console "Pages" monthly: <80% of new pages indexed → slow down.

| # | Page | Type | Main keywords (volume / KD) | Cluster vol | Status |
|---|---|---|---|---|---|
| 1 | How to change or edit your email signature in Outlook | new guide | how to edit signature in outlook 4,400/29 · how to change your email signature in outlook 2,400/28 · how do i change my email signature in outlook 1,900/28 | ~35,700 | todo |
| 2 | Refresh: How to create an email signature in Outlook (+ Outlook 365 section) | update existing | how to create email signature in outlook 3,600/23 · how to create signature in outlook 365 1,300/17 | ~7,000 | todo |
| 3 | Email signature block: examples and how to add one | new guide | email signature block examples 1,300/27 · signature blocks 720/26 · how to add a signature block in outlook 590/19 | ~6,500 | todo |
| 4 | Animated GIF email signature | new guide | signature gif 880/17 · animated email signature 320/24 · animated gif signature 260/8 | ~3,950 | todo |
| 5 | Email signature quotes and captions | new examples | email signature quotes 480/19 · email signature captions 480/21 · quotes for email signature 320/26 | ~3,570 | todo |
| 6 | Business and sales email signature examples | new examples | company email signature examples 480/28 · sales email signature 390/16 · business email signature examples 320/21 | ~3,400 | todo |
| 7 | How to add a logo to your email signature | new guide | how to add logo to email signature 210/9 · how to add logo to gmail signature 210/28 | ~2,770 | todo |
| 8 | PhD, academic and medical student email signatures | new examples | phd email signature example 1,300/27 · medical student email signature 260/20 · phd student email signature 170/17 | ~2,600 | todo |
| 9 | Pronouns in your email signature | new guide | how to add pronouns to email signature 320/24 · pronouns email signature 210/23 | ~1,650 | todo |
| 10 | Lawyer and attorney email signature examples | new examples | lawyer email signature 210/7 · attorney email signature 170/8 · law firm email signature 70/5 | ~740 | todo |

Notes
- #1 overlaps the "change or edit" section of the Outlook guide: when #1 ships, shorten that section to two lines and link to #1.
- #4 and #7: only describe SignTry features that exist in the app (CLAUDE.md rule).
- Skipped: brand searches (hubspot email signature), PDF/Word signatures (not our product), "signature" alone.
- Every new page: add to `PAGES` and `RELATED` in `tools/site/links.py`, to `GUIDES`/`EXAMPLES` in `build.py`, then build → sync_index → sitemap → check.
