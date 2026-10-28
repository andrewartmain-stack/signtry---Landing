import json, html, re

SITE = 'https://signtry.com'
SIGNUP = 'https://app.signtry.com/signup'
LOGIN = 'https://app.signtry.com/login'
TODAY = '2026-10-28'

ICONS = {
    'chev': '<path d="m6 9 6 6 6-6"/>',
    'layout': '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18M9 21V9"/>',
    'pen': '<path d="M12 20h9"/><path d="M16.38 3.62a1 1 0 0 1 3 3L7.37 18.64a2 2 0 0 1-.86.5l-2.87.84a.5.5 0 0 1-.62-.62l.84-2.87a2 2 0 0 1 .5-.86z"/>',
    'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    'chart': '<path d="M3 3v18h18"/><path d="M18 17V9M13 17V5M8 17v-3"/>',
    'mailcheck': '<path d="M22 13V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h8"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/><path d="m16 19 2 2 4-4"/>',
    'book': '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    'compass': '<circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-2.12 6.36-6.36 2.12 2.12-6.36z"/>',
    'mail': '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    'buoy': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="m4.93 4.93 4.24 4.24M14.83 9.17l4.24-4.24M14.83 14.83l4.24 4.24M9.17 14.83l-4.24 4.24"/>',
    'spark': '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/><path d="M20 3v4M22 5h-4"/>',
    'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>',
    'check': '<path d="M20 6 9 17l-5-5"/>',
    'image': '<rect width="18" height="18" x="3" y="3" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.09-3.09a2 2 0 0 0-2.82 0L6 21"/>',
    'link': '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    'badge': '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m9 12 2 2 4-4"/>',
    'table': '<path d="M12 3v18"/><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18M3 15h18"/>',
    'palette': '<circle cx="13.5" cy="6.5" r=".5"/><circle cx="17.5" cy="10.5" r=".5"/><circle cx="8.5" cy="7.5" r=".5"/><circle cx="6.5" cy="12.5" r=".5"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.93 0 1.65-.75 1.65-1.69 0-.44-.18-.84-.44-1.13-.29-.29-.44-.65-.44-1.13a1.64 1.64 0 0 1 1.67-1.67h2c3.05 0 5.55-2.5 5.55-5.55C21.97 6.01 17.46 2 12 2z"/>',
    'phone': '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    'code': '<path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/>',
    'cloud': '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
    'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    'shield': '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    'info': '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    'cal': '<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    'grad': '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    'home': '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    'brief': '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    'apple': '<path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06Z"/><path d="M10 2c1 .5 2 2 2 5"/>',
    'ruler': '<path d="M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.41 2.41 0 0 1 0-3.4l2.6-2.6a2.41 2.41 0 0 1 3.4 0Z"/><path d="m14.5 12.5 2-2M11.5 9.5l2-2M8.5 6.5l2-2M17.5 15.5l2-2"/>',
    'share': '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.59 13.51 6.83 3.98M15.41 6.51l-6.82 3.98"/>',
}


def ic(name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24">{ICONS[name]}</svg>'


GOOGLE_G = '''<svg viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>'''

MAIL_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="#0b5cff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'

GEN_ICON = '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gen-grad)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><defs><linearGradient id="gen-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b5cff"/><stop offset="1" stop-color="#b14bf4"/></linearGradient></defs><path d="M12 20h9"/><path d="M16.38 3.62a1 1 0 0 1 3 3L7.37 18.64a2 2 0 0 1-.86.5l-2.87.84a.5.5 0 0 1-.62-.62l.84-2.87a2 2 0 0 1 .5-.86z"/><path d="M5 3v4M3 5h4"/></svg>'''

FEATURES = [
    ('features/email-signature-templates.html', 'layout', '#e6efff', '#0b5cff', 'Email signature templates', 'Professional layouts for every industry'),
    ('features/email-signature-generator.html', 'pen', '#efe9ff', '#7b5cf0', 'Email signature generator', 'Add your photo, logo, links and colors'),
    ('features/email-signature-management.html', 'users', '#ddf7f5', '#1aa89f', 'Team signatures from a CSV', 'One brand across every inbox'),
    ('features/email-signature-analytics.html', 'chart', '#fff1e3', '#d9730d', 'Signature analytics', 'See which links get clicked'),
    ('features/html-email-signature.html', 'mailcheck', '#f2f8dc', '#5d7a0a', 'Works in every inbox', 'HTML signatures for Gmail, Outlook and more'),
]

RESOURCES = [
    ('blog.html', 'book', '#e6efff', '#0b5cff', 'Blog', 'Tips for better email and personal branding'),
    ('guides.html', 'buoy', '#f2f8dc', '#5d7a0a', 'Guides &amp; examples', 'Install guides and signature examples'),
    ('index.html#individuals', 'users', '#efe9ff', '#7b5cf0', 'About Us', 'Who we are and why we built SignTry'),
    ('mailto:support@signtry.com', 'mail', '#ddf7f5', '#1aa89f', 'Contact Us', 'Talk to a real person on our team'),
]


def href(p, url):
    return url if url.startswith(('http', 'mailto:', '#')) else p + url


def menu_items(p, items):
    out = []
    for url, icon, bg, fg, title, desc in items:
        out.append(f'<a href="{href(p, url)}"><span class="ic" style="background:{bg};color:{fg}">{ic(icon)}</span>'
                   f'<span><b>{title}</b><small>{desc}</small></span></a>')
    return '\n                        '.join(out)


def nav(p):
    return f'''    <nav class="site-nav">
        <div class="wrap">
            <a class="logo" href="{p}index.html" aria-label="SignTry home"><img src="{p}images/logo-full.png" alt="signtry" width="134" height="42"></a>
            <div class="links" id="links">
                <div class="dd">
                    <button type="button" aria-expanded="false" aria-haspopup="true">Features {ic('chev')}</button>
                    <div class="menu wide">
                        {menu_items(p, FEATURES)}
                    </div>
                </div>
                <a href="{p}pricing.html">Pricing</a>
                <div class="dd">
                    <button type="button" aria-expanded="false" aria-haspopup="true">Resources {ic('chev')}</button>
                    <div class="menu">
                        {menu_items(p, RESOURCES)}
                    </div>
                </div>
                <a class="gen" href="{p}free-email-signature-generator.html">{ic('spark')}Generate your free email signature <em>Free</em></a>
            </div>
            <div class="nr"><a class="btn" href="{LOGIN}">Log in</a><a class="btn dark" href="{SIGNUP}">Sign up</a></div>
            <button class="burger" id="burger" type="button" aria-label="Open menu" aria-controls="links" aria-expanded="false">{ic('menu')}</button>
        </div>
    </nav>'''


FOOTER_COLS = [
    ('Product', [('Free email signature generator', 'free-email-signature-generator.html'), ('Pricing', 'pricing.html'), ('Email signature templates', 'features/email-signature-templates.html'),
                 ('Email signature generator', 'features/email-signature-generator.html'),
                 ('Team signatures', 'features/email-signature-management.html'),
                 ('Signature analytics', 'features/email-signature-analytics.html'),
                 ('HTML email signatures', 'features/html-email-signature.html')]),
    ('Guides', [('Outlook email signature', 'guides/how-to-create-an-email-signature-in-outlook.html'),
                ('iPhone email signature', 'guides/how-to-change-email-signature-on-iphone.html'),
                ('Yahoo Mail signature', 'guides/how-to-change-signature-in-yahoo-mail.html'),
                ('Gmail signature', 'posts/how-to-create-an-email-signature-in-gmail.html'),
                ('Email signature size', 'guides/email-signature-size.html'),
                ('Social media icons', 'guides/social-media-icons-for-email-signature.html'),
                ('Email signature fonts', 'guides/email-signature-fonts.html'),
                ('Funny email sign-offs', 'guides/funny-email-sign-offs.html')]),
    ('Examples', [('Email signature examples', 'examples/email-signature-examples.html'),
                  ('Student email signature', 'examples/college-student-email-signature.html'),
                  ('Teacher email signature', 'examples/teacher-email-signature.html'),
                  ('Real estate email signature', 'examples/real-estate-email-signature.html'),
                  ('Funny email signatures', 'examples/funny-email-signatures.html'),
                  ('Holiday email signatures', 'examples/holiday-email-signature.html'),
                  ('All guides &amp; examples', 'guides.html')]),
    ('Company', [('Blog', 'blog.html'), ('Contact support', 'mailto:support@signtry.com'), ('Log in', LOGIN),
                 ('Privacy', 'privacy.html'), ('Terms', 'terms.html'), ('GDPR', 'gdpr.html')]),
]


def footer(p):
    cols = ''
    for h, links in FOOTER_COLS:
        lis = ''.join(f'\n                        <li><a href="{href(p, u)}">{t}</a></li>' for t, u in links)
        cols += f'''
                <div>
                    <h4>{h}</h4>
                    <ul>{lis}
                    </ul>
                </div>'''
    return f'''    <footer class="site-footer">
        <div class="wrap">
            <div class="top">
                <h3>Make every email count.</h3>{cols}
            </div>
            <div class="logo" style="margin-top:56px"><img src="{p}images/logo-full-light.png" alt="signtry"></div>
            <div class="bot"><span>Works with: Gmail · Outlook · Apple Mail · Yahoo Mail · and more</span><span>Questions? <a href="mailto:support@signtry.com">support@signtry.com</a></span></div>
            <div class="bot" style="margin-top:16px;border:0;padding:0"><span>© <span id="year">2026</span> SignTry</span><span><a href="{p}privacy.html">Privacy</a> · <a href="{p}terms.html">Terms</a> · <a href="{p}gdpr.html">GDPR</a></span></div>
        </div>
    </footer>'''


def head(p, path, title, desc, schema, og_image='media/demo.jpg'):
    url = SITE + '/' + path
    ld = '\n'.join(f'    <script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
    return f'''<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8QDTQTXQ2M"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
        gtag('js', new Date());
        gtag('config', 'G-8QDTQTXQ2M');
    </script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="theme-color" content="#061b31">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="SignTry">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{SITE}/{og_image}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="icon" href="{p}favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="{p}images/favicon-32.png">
    <link rel="apple-touch-icon" href="{p}images/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{p}css/site.css">
{ld}
</head>
'''


def crumbs_schema(trail):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + '/' + u} for i, (n, u) in enumerate(trail)]}


def faq_schema(faqs):
    strip = lambda s: re.sub(r'<[^>]+>', '', s)
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in faqs]}


def article_schema(path, title, desc, image):
    return {'@context': 'https://schema.org', '@type': 'Article', 'headline': title, 'description': desc,
            'image': SITE + '/' + image, 'datePublished': TODAY, 'dateModified': TODAY,
            'author': {'@type': 'Organization', 'name': 'SignTry', 'url': SITE + '/'},
            'publisher': {'@type': 'Organization', 'name': 'SignTry', 'logo': {'@type': 'ImageObject', 'url': SITE + '/images/logo-full.png'}},
            'mainEntityOfPage': SITE + '/' + path}


def crumbs_html(p, trail):
    parts = []
    for i, (n, u) in enumerate(trail):
        parts.append(n if i == len(trail) - 1 else f'<a href="{href(p, u if u else "index.html")}">{n}</a>')
    return '<div class="crumbs">' + ' / '.join(parts) + '</div>'


def cta_buttons(p, second=('Generate your first email signature free', 'free-email-signature-generator.html')):
    return f'''<div class="cta">
                <a class="btn sso" href="{SIGNUP}"><span class="ic">{MAIL_ICON}</span>Sign up with email</a>
                <a class="btn sso" href="{href(p, second[1])}"><span class="ic">{GEN_ICON}</span>{second[0]}</a>
            </div>
            <p class="alt">No credit card required</p>'''


def faq_html(faqs):
    items = ''.join(f'''
                    <details{' open' if i == 0 else ''}>
                        <summary>{q}</summary>
                        <p>{a}</p>
                    </details>''' for i, (q, a) in enumerate(faqs))
    return f'<div class="acc faq-wrap">{items}\n                </div>'


def related_html(p, items):
    return '<div class="related">' + ''.join(
        f'<a href="{href(p, u)}"><small>{k}</small><b>{t}</b></a>' for k, t, u in items) + '</div>'


def page(path, title, desc, body, schema, og_image='media/demo.jpg', extra_script=''):
    depth = path.count('/')
    p = '../' * depth if depth else './'
    body = body.replace('{P}', p)
    return (head(p, path, title, desc, schema, og_image) + '\n<body>\n' + nav(p) + '\n\n' + body + '\n\n' + footer(p) +
            f'\n\n    <script src="{p}js/site.js"></script>\n{extra_script}</body>\n\n</html>\n')


def video(p, name, label, still=None):
    poster = f'{p}media/{name}.jpg'
    return f'<video src="{p}media/{name}.mp4" poster="{poster}" muted loop playsinline preload="none" aria-label="{label}"></video>'


def fig(p, src, alt, cap=''):
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure><div class="media-frame"><img src="{p}{src}" alt="{alt}" loading="lazy" width="1400" height="875"></div>{c}</figure>'


def callout(text):
    return f'<div class="callout">{ic("info")}<p>{text}</p></div>'


def steps(items):
    return '<ol class="steps">' + ''.join(f'<li>{s}</li>' for s in items) + '</ol>'


def table(head_, rows, us_row=None):
    th = ''.join(f'<th>{h}</th>' for h in head_)
    trs = ''
    for i, r in enumerate(rows):
        cls = ' class="us"' if us_row is not None and i == us_row else ''
        trs += f'<tr{cls}>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return f'<div class="tbl-wrap"><table class="tbl"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def toc(items):
    return '<div class="toc" role="navigation" aria-label="On this page"><b>On this page</b><ol>' + ''.join(
        f'<li><a href="#{a}">{t}</a></li>' for a, t in items) + '</ol></div>'


def fgrid(items):
    return '<div class="fgrid">' + ''.join(
        f'<div class="fcard"><span class="fi">{ic(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in items) + '</div>'


def cta_band(p, h='Create your email signature in 2 minutes', sub='Pick a template, add your details and copy it into your inbox. Free to start, no credit card required.'):
    return f'''    <section class="cta-band">
        <div class="wrap">
            <h2>{h}</h2>
            <p class="sub">{sub}</p>
            {cta_buttons(p)}
        </div>
    </section>'''
