import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import *
import p_pricing, p_features, p_guides, p_examples, p_legal, p_blog, p_batch2

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

HUB_PATH = 'guides.html'
GUIDES = [('Outlook', 'How to make an email signature in Outlook', 'guides/how-to-create-an-email-signature-in-outlook.html'),
          ('Gmail', 'How to create an email signature in Gmail', 'posts/how-to-create-an-email-signature-in-gmail.html'),
          ('iPhone &amp; Mac', 'How to change your email signature on iPhone', 'guides/how-to-change-email-signature-on-iphone.html'),
          ('Yahoo Mail', 'How to change your signature in Yahoo Mail', 'guides/how-to-change-signature-in-yahoo-mail.html'),
          ('Design', 'Email signature size: the right dimensions', 'guides/email-signature-size.html'),
          ('Design', 'Social media icons for your email signature', 'guides/social-media-icons-for-email-signature.html'),
          ('Design', 'The best fonts for email signatures', 'guides/email-signature-fonts.html'),
          ('Writing', 'Funny email sign-offs: 70+ ideas', 'guides/funny-email-sign-offs.html')]
EXAMPLES = [('Examples', 'Email signature examples: 14 to copy', 'examples/email-signature-examples.html'),
            ('Students', 'College student email signature examples', 'examples/college-student-email-signature.html'),
            ('Teachers', 'Teacher email signature examples', 'examples/teacher-email-signature.html'),
            ('Real estate', 'Real estate email signature examples', 'examples/real-estate-email-signature.html'),
            ('Humor', 'Funny email signatures and quotes', 'examples/funny-email-signatures.html'),
            ('Seasonal', 'Christmas and holiday email signatures', 'examples/holiday-email-signature.html')]
FEATS = [('Feature', t, u) for u, _, _, _, t, _ in FEATURES]


def hub():
    p = './'
    title = 'Email Signature Guides, Examples & Help Center | SignTry'
    desc = 'Free email signature guides for Outlook, Gmail, iPhone and Yahoo Mail, plus email signature examples for students, teachers, real estate agents and businesses.'
    body = f'''    <header class="hero page-hero">
        <div class="wrap">
            {crumbs_html(p, [('Home', ''), ('Guides &amp; examples', HUB_PATH)])}
            <span class="tag">Help center</span>
            <h1>Email signature guides and examples</h1>
            <p class="lead">Everything you need to create, install and improve your email signature: step-by-step email signature guides for every email app, plus examples you can copy for your job.</p>
        </div>
    </header>

    <section class="plain">
        <div class="wrap">
            <div class="sec-head"><h2>Install guides</h2><p class="sub">Add your signature to the email app you use.</p></div>
            {related_html(p, GUIDES)}
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-head"><h2>Email signature examples</h2><p class="sub">Real layouts, ready to copy.</p></div>
            {related_html(p, EXAMPLES)}
        </div>
    </section>

    <section class="plain">
        <div class="wrap">
            <div class="sec-head"><h2>Product features</h2><p class="sub">What SignTry does for you.</p></div>
            {related_html(p, FEATS)}
        </div>
    </section>

{cta_band(p)}'''
    schema = [crumbs_schema([('Home', ''), ('Guides & examples', HUB_PATH)]),
              {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': title, 'description': desc, 'url': SITE + '/' + HUB_PATH}]
    return HUB_PATH, page(HUB_PATH, title, desc, body, schema)


pages = [p_pricing.build(), hub()] + p_features.build() + p_guides.build() + p_examples.build() + p_legal.build() + p_blog.build() + p_batch2.build()
for path, html_ in pages:
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8', newline='\n').write(html_)
    print(path, len(html_))
