import os, re, json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(ROOT)
VOID = {'img', 'br', 'meta', 'link', 'input', 'source', 'path', 'circle', 'rect', 'stop', 'hr', 'polyline', 'line'}


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st = []; s.err = []; s.refs = []; s.ids = set(); s.h1 = 0; s.ld = []; s._ld = False
    def handle_starttag(s, t, a):
        a = dict(a)
        if t not in VOID: s.st.append(t)
        if t == 'h1': s.h1 += 1
        if 'id' in a: s.ids.add(a['id'])
        for k in ('href', 'src', 'poster'):
            if a.get(k): s.refs.append(a[k])
        s._ld = t == 'script' and a.get('type') == 'application/ld+json'
    def handle_data(s, d):
        if s._ld: s.ld.append(d)
    def handle_endtag(s, t):
        s._ld = False
        if t in VOID: return
        if s.st and s.st[-1] == t: s.st.pop()
        else: s.err.append((t, s.getpos()))


files = ['index.html', 'free-email-signature-generator.html', 'pricing.html', 'guides.html', 'privacy.html', 'terms.html', 'gdpr.html', 'blog.html'] + glob.glob('posts/*.html') + glob.glob('features/*.html') + glob.glob('guides/*.html') + glob.glob('examples/*.html')
parsed = {}
for f in files:
    f = f.replace(os.sep, '/')
    src = open(f, encoding='utf-8').read()
    p = P(); p.feed(src); parsed[f] = p
    t = re.search(r'<title>(.*?)</title>', src, re.S).group(1)
    d = re.search(r'<meta\s+name="description"\s+content="(.*?)"', src, re.S).group(1)
    probs = []
    if p.err or p.st: probs.append(f'tags {p.err[:3]} {p.st[:3]}')
    if p.h1 != 1: probs.append(f'h1={p.h1}')
    if len(t) > 65: probs.append(f'title {len(t)}')
    if len(d) > 160: probs.append(f'desc {len(d)}')
    for j in p.ld:
        try: json.loads(j)
        except Exception as e: probs.append('ld ' + str(e))
    print(f'{f:62} t{len(t):3} d{len(d):3} ' + ('; '.join(probs) or 'ok'))

bad = []
for f, p in parsed.items():
    base = os.path.dirname(f)
    for r in p.refs:
        u = urlparse(r)
        if u.scheme or r.startswith('mailto:'): continue
        path, frag = u.path, u.fragment
        target = os.path.normpath(os.path.join(base, path)) if path else f
        if path and not os.path.exists(target): bad.append((f, r)); continue
        if frag:
            tp = parsed.get(target.replace(os.sep, '/'))
            if tp and frag not in tp.ids: bad.append((f, r + ' (missing anchor)'))
print('broken refs:', bad or 'none')
fails = [f for f, p in parsed.items() if p.err or p.st or p.h1 != 1]
sys.exit(1 if bad or fails else 0)
