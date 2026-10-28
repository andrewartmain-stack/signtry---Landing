import os, json
from layout import *

HERE = os.path.join(os.path.dirname(__file__), 'legal')


def build():
    meta = json.load(open(os.path.join(HERE, 'meta.json'), encoding='utf-8'))
    out = []
    for name, m in meta.items():
        path = name + '.html'
        content = open(os.path.join(HERE, name + '.html'), encoding='utf-8').read()
        body = f'''    <header class="hero page-hero">
        <div class="wrap">
            {crumbs_html('./', [('Home', ''), (m['h1'], path)])}
            <h1>{m['h1']}</h1>
            <p class="lead">{m['lead']}</p>
            <p class="alt" style="margin-top:0">{m['updated']}</p>
        </div>
    </header>

    <section class="plain">
        <div class="wrap">
            <article class="prose legal">
{content}
            </article>
        </div>
    </section>'''
        schema = [crumbs_schema([('Home', ''), (m['h1'], path)])]
        out.append((path, page(path, m['title'], m['desc'], body, schema)))
    return out
