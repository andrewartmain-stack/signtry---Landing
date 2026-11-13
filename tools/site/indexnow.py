"""Tell Bing, Yandex and other IndexNow engines about new or changed pages. Run AFTER the deploy is live.

    python tools/site/indexnow.py                 # pages changed in the last commit
    python tools/site/indexnow.py --since HEAD~5  # pages changed since a git ref
    python tools/site/indexnow.py --all           # every URL in sitemap.xml
    python tools/site/indexnow.py --dry-run ...   # print the URLs, send nothing

Google does not use IndexNow; it finds pages through internal links and sitemap.xml.
The key file (<KEY>.txt) must be live at the site root, or the engines reject the request.
"""
import json, os, re, subprocess, sys, urllib.request, urllib.error

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HOST = 'signtry.com'
KEY = '3856bd4e9f175b0d8c4f8ab406e24c5b'
ENDPOINT = 'https://api.indexnow.org/indexnow'
PUBLIC = re.compile(r'^(index|pricing|guides|blog|free-email-signature-generator|privacy|terms|gdpr)\.html$|^(features|guides|examples|posts)/[^/]+\.html$')

os.chdir(ROOT)
args = sys.argv[1:]
dry = '--dry-run' in args


def to_url(f):
    return f'https://{HOST}/' + ('' if f == 'index.html' else f[:-len('.html')])


if '--all' in args:
    urls = re.findall(r'<loc>(.*?)</loc>', open('sitemap.xml', encoding='utf-8').read())
else:
    ref = args[args.index('--since') + 1] if '--since' in args else 'HEAD~1'
    changed = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=AM', ref, 'HEAD'],
                             capture_output=True, text=True, check=True).stdout.split()
    urls = [to_url(f) for f in changed if PUBLIC.match(f)]

if not urls:
    sys.exit('No public pages to submit.')
print(f'{len(urls)} URL(s):', *urls, sep='\n  ')
if dry:
    sys.exit(0)

body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'https://{HOST}/{KEY}.txt', 'urlList': urls[:10000]}).encode()
req = urllib.request.Request(ENDPOINT, data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print('IndexNow:', r.status, '(200/202 = accepted)')
except urllib.error.HTTPError as e:
    sys.exit(f'IndexNow error {e.code}: {e.read().decode(errors="ignore")[:300]}  (403 = key file not live yet)')
