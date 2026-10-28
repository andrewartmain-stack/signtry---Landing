"""Copy the shared navbar and footer from layout.py into the hand-written pages."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import nav, footer

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
for name in ('index.html', 'free-email-signature-generator.html'):
    f = os.path.join(ROOT, name)
    s = open(f, encoding='utf-8').read()
    s = re.sub(r'    <nav( class="site-nav")?>.*?</nav>', lambda m: nav('./'), s, count=1, flags=re.S)
    s = re.sub(r'    <footer( class="site-footer")?>.*?</footer>', lambda m: footer('./'), s, count=1, flags=re.S)
    open(f, 'w', encoding='utf-8', newline='\n').write(s)
    print(name + ': navbar and footer synced')
