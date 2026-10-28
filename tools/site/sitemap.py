"""Regenerate sitemap.xml from every public page in the repo."""
import os, glob, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SITE = 'https://signtry.com/'
TODAY = datetime.date.today().isoformat()
os.chdir(ROOT)

PRIORITY = {'index.html': 1.0, 'pricing.html': 0.9, 'free-email-signature-generator.html': 0.9,
            'guides.html': 0.8, 'blog.html': 0.7, 'privacy.html': 0.3, 'terms.html': 0.3, 'gdpr.html': 0.3}
FOLDERS = {'features': 0.9, 'guides': 0.8, 'examples': 0.8, 'posts': 0.6}

pages = [(f, PRIORITY[f]) for f in PRIORITY if os.path.exists(f)]
for folder, pr in FOLDERS.items():
    pages += [(f.replace(os.sep, '/'), pr) for f in sorted(glob.glob(f'{folder}/*.html'))]

out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for f, pr in pages:
    loc = SITE if f == 'index.html' else SITE + f
    out.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{pr:.1f}</priority>\n  </url>')
out.append('</urlset>\n')
open('sitemap.xml', 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print(f'sitemap.xml: {len(pages)} URLs')
