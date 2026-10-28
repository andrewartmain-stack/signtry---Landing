from layout import *

PATH = 'pricing.html'
TITLE = 'Email Signature Pricing: Pay Per Signature | SignTry'
DESC = 'Simple email signature pricing: pay only for the signatures you need. From $3 a month for one signature, $1 per signature for teams. Analytics and CSV included.'

TIERS = [  # count, yearly per month, monthly per month
    (1, 3, 4), (5, 7, 10), (10, 10, 14), (25, 22, 29), (50, 39, 52), (100, 69, 92), (250, 149, 199)]

FAQS = [
    ('How does SignTry email signature pricing work?',
     'You pay for the number of email signatures you need, not for features. One signature is $3 a month (billed yearly). Team plans start at 5 signatures for $7 a month and get cheaper per signature as you add more, down to $0.60 per signature at 250.'),
    ('What counts as one signature?',
     'One signature is one finished design for one person, for example “Jane Cooper, Head of Sales”. You can edit it as often as you like without using another signature. A teammate with their own name and details is a second signature.'),
    ('Is there a free plan?',
     'You can sign up and start building your signature with no credit card. When you are ready to use it, pick a plan for 1 signature or for your whole team.'),
    ('Do I need a plan for every person on my team?',
     'No. Pick the size that covers everyone, for example 25 signatures for a 22-person team. There are no seat minimums, so a 4-person team can buy 5 signatures instead of paying for 10 seats.'),
    ('Can I change the number of signatures later?',
     'Yes. You can move to a bigger or smaller plan at any time from Billing in your dashboard.'),
    ('What is the difference between monthly and yearly billing?',
     'The features are identical. Yearly billing costs about 25% less than paying month to month. Both can be cancelled, and you keep access until the end of the period you paid for.'),
    ('Are analytics and CSV import really included in every team plan?',
     'Yes. Link-click analytics, bulk generation from a CSV, verified badges, every template and hosted images are included from the 5-signature plan up. We do not lock features behind higher tiers.'),
    ('Which payment methods do you accept?',
     'All major credit and debit cards through Stripe. Teams that need an invoice for 500 or more signatures can <a href="mailto:support@signtry.com?subject=Volume%20pricing">contact us</a>.'),
]


def calc():
    btns = ''
    for n, _, _ in TIERS:
        on = ' class="on"' if n == 10 else ''
        btns += f'<button type="button" data-n="{n}"{on}><b>{n}</b><small>{"signature" if n == 1 else "signatures"}</small></button>'
    btns += '<button type="button" data-n="500"><b>500+</b><small>signatures</small></button>'
    return f'''<div class="calc" id="calc">
                <div class="calc-top">
                    <h2>How many signatures do you need?</h2>
                    <div class="bill" role="group" aria-label="Billing period"><button type="button" class="on" data-b="y">Yearly <em>Save 25%</em></button><button type="button" data-b="m">Monthly</button></div>
                </div>
                <div class="counts" role="group" aria-label="Number of signatures">{btns}</div>
                <div class="calc-out">
                    <div>
                        <div class="big-price" id="price">$10<span> / month</span></div>
                        <div class="per" id="per"><b>$1.00</b> per signature · $120 billed yearly</div>
                        <span class="save" id="save">You save $48 a year with yearly billing</span>
                        <div><a class="btn dark" id="buy" href="{SIGNUP}">Get 10 signatures</a></div>
                    </div>
                    <ul class="incl" id="incl"></ul>
                </div>
            </div>'''


SCRIPT = '''    <script>
        (function () {
            var T = { 1: [3, 4], 5: [7, 10], 10: [10, 14], 25: [22, 29], 50: [39, 52], 100: [69, 92], 250: [149, 199] };
            var TEAM = ['Every template, for every industry', 'Generate the whole team from a CSV', 'Link-click analytics dashboard', 'Verified badges, photos, logos and banners', 'Booking buttons and social icons', 'Hosted images that load in every inbox', 'Works in Gmail, Outlook, Apple Mail, Yahoo and more'];
            var BIG = ['Everything in team plans', 'Volume price per signature', 'Invoice billing', 'Help importing your team', 'Priority support'];
            var n = 10, b = 'y';
            var $ = function (id) { return document.getElementById(id) };
            function money(v) { return '$' + (v % 1 ? v.toFixed(2) : v) }
            function list(a) { $('incl').innerHTML = a.map(function (x) { return '<li>' + x + '</li>' }).join('') }
            function render() {
                document.querySelectorAll('.counts button').forEach(function (x) { x.classList.toggle('on', +x.dataset.n === n) });
                document.querySelectorAll('.bill button').forEach(function (x) { x.classList.toggle('on', x.dataset.b === b) });
                document.querySelector('.bill').style.visibility = n === 500 ? 'hidden' : 'visible';
                var buy = $('buy'), save = $('save');
                if (n === 500) {
                    $('price').innerHTML = 'Custom';
                    $('per').innerHTML = '<b>Volume pricing</b> for 500+ signatures';
                    save.hidden = true;
                    buy.textContent = 'Talk to us'; buy.href = 'mailto:support@signtry.com?subject=SignTry%20for%20500%2B%20signatures';
                    list(BIG); return;
                }
                var y = T[n][0], m = T[n][1], v = b === 'y' ? y : m;
                $('price').innerHTML = money(v) + '<span> / month</span>';
                $('per').innerHTML = '<b>' + money(v / n) + '</b> per signature · ' + (b === 'y' ? money(y * 12) + ' billed yearly' : 'billed monthly');
                save.hidden = false;
                save.textContent = b === 'y' ? 'You save ' + money((m - y) * 12) + ' a year with yearly billing' : 'Switch to yearly and save ' + money((m - y) * 12);
                buy.textContent = n === 1 ? 'Get my signature' : 'Get ' + n + ' signatures'; buy.href = 'https://app.signtry.com/signup';
                list(TEAM);
            }
            document.querySelectorAll('.counts button').forEach(function (x) { x.onclick = function () { n = +x.dataset.n; render() } });
            document.querySelectorAll('.bill button').forEach(function (x) { x.onclick = function () { b = x.dataset.b; render() } });
            render();
        })();
    </script>
'''


def build():
    p = './'
    rows = []
    who = {1: 'Freelancers, job seekers, founders', 5: 'Small teams and partners', 10: 'Growing teams', 25: 'Agencies and offices', 50: 'Sales and real estate teams',
           100: 'Multi-office companies', 250: 'Large organizations'}
    for n, y, m in TIERS:
        rows.append([f'<strong>{n}</strong>', f'${y} / month', f'${m} / month', f'${y / n:.2f}', who[n]])
    rows.append(['<strong>500+</strong>', 'Custom', 'Custom', 'Volume pricing', '<a href="mailto:support@signtry.com?subject=Volume%20pricing">Talk to us</a>'])
    tier_table = table(['Signatures', 'Billed yearly', 'Billed monthly', 'Per signature (yearly)', 'Best for'], rows)

    cmp1 = table(['Tool', 'One person', 'Billing'], [
        ['<strong>SignTry</strong>', '<strong>$3 / month ($36 a year)</strong>', 'Billed yearly'],
        ['MySignature', 'about $6 / month ($72 a year)', 'Billed yearly'],
        ['WiseStamp', 'about $9 / month (Pro+)', 'Billed yearly'],
        ['Newoldstamp', 'Not available (5-signature minimum)', '—'],
        ['Exclaimer', 'Not available (10-user minimum)', '—'],
    ], us_row=0)
    cmp10 = table(['Tool', '10 people, per month', 'Analytics included?', 'Minimum'], [
        ['<strong>SignTry</strong>', '<strong>$10</strong>', '<strong>Yes, every plan</strong>', 'None'],
        ['Exclaimer', '$9 to $17.50 ($0.90 to $1.75 per user)', 'Depends on plan', '10 users'],
        ['Newoldstamp', 'about $18 ($219 a year)', 'Depends on plan', '5 signatures'],
        ['MySignature', '$24 to $34 ($2.40 to $3.40 per user)', 'Higher plan', '5 users'],
        ['WiseStamp', '$29 to $59 ($19 to $49 base + $1 per user)', 'From the $49 Grow plan', '3 seats'],
    ], us_row=0)
    cmp50 = table(['Tool', '50 people, per month', 'Per person'], [
        ['<strong>SignTry</strong>', '<strong>$39</strong>', '<strong>$0.78</strong>'],
        ['Exclaimer', '$45 to $87.50', '$0.90 to $1.75'],
        ['Newoldstamp', 'about $67 ($799 a year)', 'about $1.33'],
        ['WiseStamp', '$69 to $99', '$1.38 to $1.98'],
        ['MySignature', '$120 to $170', '$2.40 to $3.40'],
    ], us_row=0)

    wins = [
        ('No seat minimums', 'You buy the signatures you need, starting at 5. Other tools round you up to 5, 10 or more paid seats.',
         '<strong>Example:</strong> a 4-person design studio pays $7 a month on SignTry. With a 10-user minimum it would pay for 6 people who do not exist.'),
        ('Every feature on every team plan', 'Analytics, CSV import, verified badges and every template are included from the smallest plan. No “upgrade to unlock”.',
         '<strong>Example:</strong> to see link clicks on WiseStamp you need the Grow plan at $49 a month plus $1 per user. On SignTry, 10 people with analytics cost $10 a month.'),
        ('Half the price if it is just you', 'One signature costs $3 a month on yearly billing, with the same templates and analytics as team plans.',
         '<strong>Example:</strong> an individual plan at $6 a month costs $72 a year. SignTry costs $36 a year.'),
        ('A whole team in one click', 'Upload a spreadsheet and SignTry creates a personal signature for every row, with names, titles, photos and phone numbers filled in.',
         '<strong>Example:</strong> a 40-agent brokerage uploads one CSV and gets 40 on-brand signatures in under a minute. <a href="features/email-signature-management.html">See how it works</a>.'),
        ('The price drops as you grow', 'Your price per signature falls from $1.40 to $0.60 as your team grows, and you can change size at any time.',
         '<strong>Example:</strong> 250 signatures cost $149 a month, which is $0.60 each.'),
        ('Works where your team already emails', 'Signatures work in Gmail, Outlook, Apple Mail, Yahoo Mail and other email apps, with images hosted for you.',
         '<strong>Example:</strong> half your team on Outlook and half on Gmail? Same signature, same look. <a href="features/html-email-signature.html">See supported apps</a>.'),
    ]
    wins_html = '<div class="wins">' + ''.join(f'<div class="win"><h3>{t}</h3><p>{d}</p><div class="ex">{e}</div></div>' for t, d, e in wins) + '</div>'

    body = f'''    <header class="hero page-hero">
        <div class="wrap">
            {crumbs_html(p, [('Home', ''), ('Pricing', PATH)])}
            <span class="tag">Pricing</span>
            <h1>Email signature pricing that grows with you</h1>
            <p class="lead">SignTry email signature pricing is simple: you pay only for the number of signatures you need. One signature is $3 a month. Teams start at $7 a month for 5 signatures, with every feature included.</p>
            {calc()}
        </div>
    </header>

    <section class="plain">
        <div class="wrap">
            <div class="sec-head">
                <h2>Every plan, side by side</h2>
                <p class="sub">Same features at every size. The only thing that changes is how many signatures you get, and the more you need, the less each one costs.</p>
            </div>
            <div style="max-width:960px;margin:40px auto 0">{tier_table}
                <p class="note">Prices in USD, excluding taxes. Yearly plans are billed once a year; the monthly price shown is the yearly total divided by 12.</p>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-head">
                <h2>Everything is included in every team plan</h2>
                <p class="sub">No feature tiers. A 5-signature plan gets the same tools as a 250-signature plan.</p>
            </div>
            {fgrid([
        ('layout', 'All templates', 'Layouts for real estate, healthcare, legal, sales, students and more. <a href="features/email-signature-templates.html">Browse templates</a>.'),
        ('table', 'Generate from a CSV', 'Create a signature for every person on your team from one spreadsheet.'),
        ('chart', 'Link-click analytics', 'See clicks per month, per link and per signature.'),
        ('badge', 'Verified badges', 'Add a blue check next to your name for a little extra credibility.'),
        ('image', 'Photos, logos and banners', 'Cropped and hosted for you, so they show up in every inbox.'),
        ('cal', 'Booking buttons', 'Add “Book a call” or any call-to-action button with one click.'),
        ('share', 'Social icons', 'LinkedIn, Instagram, Facebook, WhatsApp and more.'),
        ('mailcheck', 'Every email app', 'Gmail, Outlook, Apple Mail, Yahoo Mail and more, with step-by-step install guides.'),
        ('clock', 'Unlimited edits', 'Change titles, phone numbers or colors whenever you like, at no extra cost.'),
    ])}
        </div>
    </section>

    <section class="plain">
        <div class="wrap">
            <div class="sec-head">
                <h2>How SignTry compares</h2>
                <p class="sub">We looked at what the best-known email signature tools charge and priced SignTry below them, with no feature tiers and no minimums.</p>
            </div>
            <div class="prose" style="max-width:960px;margin-top:40px">
                <h3>For one person</h3>
                {cmp1}
                <h3>For a team of 10</h3>
                {cmp10}
                <h3>For a team of 50</h3>
                {cmp50}
                <p class="note">Competitor prices are list prices billed yearly, taken from their public pricing pages and independent review sites in October 2026. Pricing changes often and some tools only quote on request, so check each vendor for current figures. All trademarks belong to their owners.</p>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-head">
                <h2>Why teams switch to SignTry</h2>
                <p class="sub">Cheaper is nice. Here is what you get on top.</p>
            </div>
            {wins_html}
        </div>
    </section>

    <section class="plain">
        <div class="wrap">
            <div class="sec-head">
                <h2>Pricing questions</h2>
            </div>
            {faq_html(FAQS)}
        </div>
    </section>

{cta_band(p, 'Start with one signature. Grow into more.', 'Sign up in seconds, no credit card required. Pay only for the signatures you need.')}'''

    schema = [crumbs_schema([('Home', ''), ('Pricing', PATH)]), faq_schema(FAQS), {
        '@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': 'SignTry',
        'applicationCategory': 'BusinessApplication', 'operatingSystem': 'Web', 'url': SITE + '/',
        'offers': [
            {'@type': 'Offer', 'name': f'{n} signature' + ('' if n == 1 else 's'), 'price': str(y * 12), 'priceCurrency': 'USD',
             'priceSpecification': {'@type': 'UnitPriceSpecification', 'price': str(y * 12), 'priceCurrency': 'USD', 'unitText': 'YEAR'}}
            for n, y, _ in TIERS]}]
    return PATH, page(PATH, TITLE, DESC, body, schema, extra_script=SCRIPT)
