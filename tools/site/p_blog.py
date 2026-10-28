import os, json
from layout import *

HERE = os.path.join(os.path.dirname(__file__), 'blog')

# Guides and examples also appear on the blog index, so readers find them from /blog.html
MORE = [
    ('Writing', 'Funny email sign-offs: 70+ unhinged and work-safe ideas', 'guides/funny-email-sign-offs.html', 'images/people/sales.jpg', 'From work-safe and witty to properly unhinged, plus when to keep it professional.'),
    ('Design', 'The best fonts for email signatures', 'guides/email-signature-fonts.html', 'media/stills/personalize-70.jpg', '12 web-safe fonts that look right in every inbox, and how to add a handwritten signature.'),
    ('Examples', 'Funny email signatures and quotes', 'examples/funny-email-signatures.html', 'images/people/freelancer.jpg', 'Humorous taglines, job-specific one-liners and quotes you can copy.'),
    ('Seasonal', 'Christmas and holiday email signature ideas', 'examples/holiday-email-signature.html', 'images/people/strip-wide.jpg', 'Greetings, banners and office-closure notes for the holiday season.'),
    ('Guides', 'How to make an email signature in Outlook', 'guides/how-to-create-an-email-signature-in-outlook.html', 'media/stills/install-signature-35.jpg', 'Step by step for new Outlook, classic Outlook, Outlook on the web, Mac and mobile.'),
    ('Guides', 'How to change your email signature on iPhone', 'guides/how-to-change-email-signature-on-iphone.html', 'media/stills/personalize-70.jpg', 'Replace “Sent from my iPhone” and add an HTML signature to Apple Mail.'),
    ('Guides', 'How to change your signature in Yahoo Mail', 'guides/how-to-change-signature-in-yahoo-mail.html', 'media/stills/template-35.jpg', 'Add or change your Yahoo Mail signature on desktop and in the app.'),
    ('Design', 'Email signature size: the right dimensions', 'guides/email-signature-size.html', 'media/stills/personalize-35.jpg', 'Exact pixel sizes for your photo, logo, banner and social icons.'),
    ('Design', 'Social media icons for your email signature', 'guides/social-media-icons-for-email-signature.html', 'media/stills/template-70.jpg', 'Which icons to include, the right size, and how to add them.'),
    ('Examples', 'Email signature examples: 14 to copy', 'examples/email-signature-examples.html', 'images/people/sales.jpg', 'Professional, personal and company signature examples you can copy.'),
    ('Examples', 'College student email signature examples', 'examples/college-student-email-signature.html', 'images/people/job-seeker.jpg', 'Examples for undergrads, grad students and PhD candidates.'),
    ('Examples', 'Teacher email signature examples', 'examples/teacher-email-signature.html', 'images/people/strip-meeting.jpg', 'Eight examples for emails to parents and staff.'),
    ('Examples', 'Real estate email signature examples', 'examples/real-estate-email-signature.html', 'images/people/real-estate.jpg', 'What realtors and brokers should include, from headshot to license number.'),
]


def card(p, kind, title, url, img, text, meta=''):
    m = f'<small class="bmeta">{meta}</small>' if meta else ''
    return (f'<a class="bcard" href="{p}{url}"><img src="{p}{img}" alt="" loading="lazy" width="640" height="400">'
            f'<span class="bbody"><span class="tag">{kind}</span><b>{title}</b><span class="bex">{text}</span>{m}</span></a>')


def posts():
    return json.load(open(os.path.join(HERE, 'posts.json'), encoding='utf-8'))


def blog_index(ps):
    p, path = './', 'blog.html'
    title = 'SignTry Blog: Email Signature Tips, Guides and Examples'
    desc = 'Email signature tips, how-to guides for Gmail, Outlook, iPhone and Yahoo, and examples for every profession from the SignTry team.'
    cards = [card(p, x['category'], x['h1'], f"posts/{x['slug']}.html", x['image'], x['excerpt'], f"{x['date']} · {x['mins']} min read") for x in ps]
    cards += [card(p, k, t, u, i, d) for k, t, u, i, d in MORE]
    body = f'''    <header class="hero page-hero">
        <div class="wrap">
            {crumbs_html(p, [('Home', ''), ('Blog', path)])}
            <span class="tag">Blog</span>
            <h1>SignTry blog</h1>
            <p class="lead">Practical email signature tips, step-by-step guides for every email app, and examples you can copy for your job.</p>
        </div>
    </header>

    <section class="plain">
        <div class="wrap">
            <div class="bgrid">{''.join(cards)}</div>
        </div>
    </section>

{cta_band(p)}'''
    schema = [crumbs_schema([('Home', ''), ('Blog', path)]),
              {'@context': 'https://schema.org', '@type': 'Blog', 'name': 'SignTry Blog', 'url': SITE + '/' + path, 'description': desc}]
    return path, page(path, title, desc, body, schema)


def post_page(x, ps):
    path, p = f"posts/{x['slug']}.html", '../'
    content = open(os.path.join(HERE, x['slug'] + '.html'), encoding='utf-8').read()
    trail = [('Home', ''), ('Blog', 'blog.html'), (x['h1'], path)]
    others = [o for o in ps if o['slug'] != x['slug']]
    related = [('Blog', o['h1'], f"posts/{o['slug']}.html") for o in others][:1] + [
        ('Guide', 'How to make an email signature in Outlook', 'guides/how-to-create-an-email-signature-in-outlook.html'),
        ('Feature', 'Free email signature generator', 'free-email-signature-generator.html')]
    body = f'''    <header class="hero page-hero">
        <div class="wrap">
            {crumbs_html(p, [('Home', ''), ('Blog', 'blog.html'), (x['category'], path)])}
            <span class="tag">{x['category']}</span>
            <h1>{x['h1']}</h1>
            <div class="author"><img src="{p}images/avatar.jpg" alt="{x['author']}" width="44" height="44"><span><b>{x['author']}</b>{x['role']} · {x['date']} · {x['mins']} min read</span></div>
        </div>
    </header>

    <section class="plain">
        <div class="wrap">
            <article class="prose post">
                <figure><div class="media-frame"><img src="{p}{x['image']}" alt="{x['h1']}" width="1000" height="500"></div></figure>
{content}
            </article>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-head"><h2>Keep reading</h2></div>
            {related_html(p, related)}
        </div>
    </section>

{cta_band(p)}'''
    schema = [crumbs_schema([(n.replace('&amp;', '&'), u) for n, u in trail]), {
        '@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': x['h1'], 'description': x['desc'],
        'image': SITE + '/' + x['image'], 'datePublished': x['date'], 'dateModified': x['date'],
        'author': {'@type': 'Person', 'name': x['author']},
        'publisher': {'@type': 'Organization', 'name': 'SignTry', 'logo': {'@type': 'ImageObject', 'url': SITE + '/images/logo-full.png'}},
        'mainEntityOfPage': SITE + '/' + path}]
    return path, page(path, x['title'], x['desc'], body, schema, og_image=x['image'])


def build():
    ps = posts()
    return [blog_index(ps)] + [post_page(x, ps) for x in ps]
