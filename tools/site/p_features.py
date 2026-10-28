from layout import *


def feature_page(f):
    path = f['path']
    p = '../'
    trail = [('Home', ''), ('Features', path), (f['crumb'], path)]
    trail_html = crumbs_html(p, [('Home', ''), (f['crumb'], path)])
    body = f'''    <header class="hero page-hero">
        <div class="wrap">
            {trail_html}
            <span class="tag">{f['tag']}</span>
            <h1>{f['h1']}</h1>
            <p class="lead">{f['lead']}</p>
            {cta_buttons(p)}
            <div class="stage-sm">
                <div class="media-frame">{video(p, f['video'], f['video_label'])}</div>
            </div>
        </div>
    </header>

    <section class="plain">
        <div class="wrap">
            <article class="prose">
{f['article']}
            </article>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-head">
                <h2>{f['grid_title']}</h2>
                <p class="sub">{f['grid_sub']}</p>
            </div>
            {fgrid(f['grid'])}
        </div>
    </section>

    <section class="plain">
        <div class="wrap">
            <div class="sec-head"><h2>Frequently asked questions</h2></div>
            {faq_html(f['faqs'])}
            <div class="sec-head" style="margin-top:96px"><h2>Keep exploring</h2></div>
            {related_html(p, f['related'])}
        </div>
    </section>

{cta_band(p, f.get('cta_h', 'Create your email signature in 2 minutes'))}'''
    still = f'media/stills/{f["stills"][0]}' if f.get('stills') else f'media/{f["video"]}.jpg'
    schema = [crumbs_schema([('Home', ''), (f['crumb'], path)]), faq_schema(f['faqs']),
              {'@context': 'https://schema.org', '@type': 'WebPage', 'name': f['title'], 'description': f['desc'],
               'url': SITE + '/' + path, 'primaryImageOfPage': SITE + '/' + still}]
    return path, page(path, f['title'], f['desc'], body.replace('{P}', p), schema, og_image=still)


TEMPLATES = dict(
    path='features/email-signature-templates.html', crumb='Email signature templates', tag='Templates',
    title='Email Signature Templates for Every Industry | SignTry',
    desc='Professional email signature templates for real estate, healthcare, legal, sales, marketing and students. Pick one, add your details, and use it in any inbox.',
    h1='Email signature templates for every industry',
    lead='Pick from professional email signature templates made for real estate agents, doctors, lawyers, sales teams, freelancers and students. Every template works in Gmail, Outlook, Apple Mail and Yahoo Mail, and you can switch layouts at any time.',
    video='template', video_label='Browsing and picking an email signature template in SignTry',
    stills=['template-35.jpg'],
    article='''                {toc}
                <h2 id="pick">Find the right template in seconds</h2>
                <p>Most email signature templates look the same. Ours are grouped by the kind of work you do, so you start from a layout that already fits your industry instead of a blank page. Filter by industry, then by layout:</p>
                <ul>
                    <li><strong>Industries:</strong> General, Real estate, Marketing &amp; agencies, Doctors &amp; healthcare, Freelancers, Legal &amp; finance, and Sales &amp; corporate.</li>
                    <li><strong>Layouts:</strong> side by side (photo next to your details) or stacked (details above or below the photo).</li>
                </ul>
                <p>Click a template and the live preview on the right shows it inside a real email, with your own name and details as soon as you type them.</p>
                {fig1}
                <h2 id="industries">Templates by industry</h2>
                <p>Every profession needs slightly different things in a signature. Here is what each template group puts first:</p>
                {tbl}
                <p>Want to see finished designs first? Browse our <a href="../examples/email-signature-examples.html">email signature examples</a>, or jump straight to <a href="../examples/real-estate-email-signature.html">real estate</a>, <a href="../examples/teacher-email-signature.html">teacher</a> and <a href="../examples/college-student-email-signature.html">student</a> examples.</p>
                <h2 id="good">What makes a good email signature template</h2>
                <p>A good template does three things: it tells people who you are, how to reach you, and what to do next. Everything else is decoration. When you pick one, check that it:</p>
                <ol>
                    <li><strong>Leads with your name.</strong> It should be the biggest, boldest line.</li>
                    <li><strong>Keeps contact details to two or three lines.</strong> Phone, email and website are usually enough.</li>
                    <li><strong>Uses one accent color.</strong> Match it to your logo or brand.</li>
                    <li><strong>Has room for one call to action,</strong> such as “Book a call” or a link to your listings.</li>
                    <li><strong>Stays under about 600 pixels wide,</strong> so it never wraps on a phone. Read more in our <a href="../guides/email-signature-size.html">email signature size guide</a>.</li>
                </ol>
                {callout}
                <h2 id="switch">Change your template whenever you like</h2>
                <p>Your details are saved separately from the design, so switching templates never means retyping anything. Try a stacked layout for a week, then switch back to side by side. Your phone number, photo and links come along with you.</p>''',
    grid_title='Every template includes', grid_sub='All of this comes with every template, on every plan.',
    grid=[('image', 'Photo and logo', 'Square photos are cropped around your face automatically.'),
          ('badge', 'Verified badge', 'A blue check next to your name, if you want one.'),
          ('pen', 'Handwritten signature', 'Generated from your name and readable on light and dark backgrounds.'),
          ('share', 'Social icons', 'LinkedIn, Facebook, Instagram, WhatsApp, your website and more.'),
          ('cal', 'Call-to-action button', 'Add “Book a call” or any link you want people to click.'),
          ('mailcheck', 'Every email app', 'Tested in Gmail, Outlook, Apple Mail and Yahoo Mail.')],
    faqs=[('Are the email signature templates free?', 'You can sign up and try every template with no credit card. Templates are included with every plan, from 1 signature at $3 a month. See <a href="../pricing.html">pricing</a>.'),
          ('Will the template look the same in Outlook and Gmail?', 'Yes. Templates are made for email apps and images are hosted for you, so the design holds up in Gmail, Outlook, Apple Mail and Yahoo Mail on desktop and mobile.'),
          ('Can I use a template for my whole team?', 'Yes. Pick a template once, then <a href="email-signature-management.html">generate signatures for everyone from a CSV</a>. Each person gets their own name, title and photo in the same design.'),
          ('Can I change the colors and fonts?', 'Yes. In the Style step you can set colors, text styles and the size and shape of your photo: square, rounded, soft or circle.'),
          ('Do you have templates for students?', 'Yes. The General and Freelancers groups work well for students and job seekers. See our <a href="../examples/college-student-email-signature.html">college student email signature examples</a> for ideas.')],
    related=[('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html'),
             ('Feature', 'Free email signature generator', 'features/email-signature-generator.html'),
             ('Guide', 'What size should an email signature be?', 'guides/email-signature-size.html')],
)

GENERATOR = dict(
    path='features/email-signature-generator.html', crumb='Email signature generator', tag='Generator',
    title='Free Email Signature Generator with Logo & Photo | SignTry',
    desc='Free email signature generator: add your photo, logo, social icons and a booking button, then copy your signature into Gmail, Outlook or Apple Mail.',
    h1='Free email signature generator',
    lead='Our free email signature generator turns your name, photo and logo into a polished, clickable signature in about two minutes. Six short steps, a live preview the whole way, and nothing to install.',
    video='personalize', video_label='Filling in details in the SignTry email signature generator',
    stills=['personalize-35.jpg', 'personalize-70.jpg'],
    article='''                {toc}
                <h2 id="steps">How to create an email signature in 6 steps</h2>
                <p>The SignTry email signature generator walks you through six short steps. The preview updates as you type, and nothing is saved until the last step, so you can experiment freely.</p>
                {steps}
                {fig1}
                <h2 id="logo">How to add a logo to your email signature</h2>
                <p>Adding a logo is the fastest way to make a signature look official. In the <strong>Branding</strong> step, turn on <strong>Company logo</strong> and upload your file. Your logo is shown about 28 pixels tall, which is large enough to recognize and small enough not to dominate the email.</p>
                <ul>
                    <li><strong>Use a transparent PNG.</strong> It looks clean on both light and dark email themes.</li>
                    <li><strong>Crop away empty space</strong> around the logo before you upload it.</li>
                    <li><strong>Use the horizontal version</strong> of your logo if you have one. Wide logos read better at small sizes.</li>
                </ul>
                <p>Logos, banners and photos are optimized and hosted when you save, so they actually appear in Gmail, Outlook, Apple Mail and Yahoo instead of turning into attachments.</p>
                <h2 id="photo">Add a photo people will remember</h2>
                <p>A headshot makes your emails feel personal and helps people put a face to the name. Upload any photo; a square one works best, and SignTry crops it around your face automatically. In the Style step, choose its size and shape: square, rounded, soft or circle.</p>
                {fig2}
                <h2 id="links">Social icons, links and a booking button</h2>
                <p>Turn your signature into the most-clicked link in your emails. Add icons for LinkedIn, Facebook, Instagram, WhatsApp and your website, plus a button such as <strong>Book a call</strong> that sends people straight to your calendar. Every link can be tracked with <a href="email-signature-analytics.html">signature analytics</a>.</p>
                <p>Not sure which icons to include? Read our guide to <a href="../guides/social-media-icons-for-email-signature.html">social media icons for email signatures</a>.</p>
                {callout}''',
    grid_title='What you can add to your signature', grid_sub='Leave any field empty and it is simply left out of the design.',
    grid=[('users', 'Name, title, company', 'Only your first name is required. Everything else is optional.'),
          ('image', 'Photo', 'Cropped around your face automatically.'),
          ('brief', 'Company logo', 'Shown about 28px tall. Transparent PNGs look best.'),
          ('pen', 'Handwritten signature', 'Generated from your name, readable on light and dark backgrounds.'),
          ('badge', 'Verified badge', 'A small blue check next to your name.'),
          ('cal', 'Booking button', 'Send people to your calendar, store or portfolio.')],
    faqs=[('Is the email signature generator really free?', 'You can sign up and build your signature with no credit card. To keep using it, choose a plan: 1 signature is $3 a month on yearly billing, and team plans start at 5 signatures. See <a href="../pricing.html">pricing</a>.'),
          ('How do I add my logo to my email signature?', 'In the Branding step, turn on Company logo and upload a PNG or JPG. A transparent PNG with no empty space around it looks best. SignTry hosts the image so it shows up in every email app.'),
          ('Can I add a handwritten signature?', 'Yes. Turn on “Add a handwritten signature” in the Branding step and SignTry generates one from your name, readable on both light and dark backgrounds.'),
          ('Which email apps does the generator work with?', 'Gmail, Outlook, Apple Mail, Yahoo Mail and most other email apps. See <a href="html-email-signature.html">how installation works</a>.'),
          ('Do I need any design skills?', 'No. Pick a template, fill in your details and the layout, spacing and colors are handled for you.')],
    related=[('Feature', 'Email signature templates', 'features/email-signature-templates.html'),
             ('Guide', 'How to create an email signature in Outlook', 'guides/how-to-create-an-email-signature-in-outlook.html'),
             ('Guide', 'Social media icons for email signatures', 'guides/social-media-icons-for-email-signature.html')],
)

MANAGEMENT = dict(
    path='features/email-signature-management.html', crumb='Team email signatures', tag='Teams',
    title='Email Signature Management for Teams: Bulk from CSV | SignTry',
    desc='Email signature management for teams: upload a CSV and create on-brand company email signatures for everyone in one click, then copy and track them.',
    h1='Email signature management for your whole team',
    lead='SignTry makes email signature management simple: upload one spreadsheet and get a personal, on-brand company email signature for every person on your team in one click. Then manage, copy and track them all from one dashboard.',
    video='team-generation', video_label='Generating six team email signatures from a CSV file in SignTry',
    stills=['team-generation-50.jpg', 'team-generation-88.jpg'],
    cta_h='Give your whole team the same polished signature',
    article='''                {toc}
                <h2 id="why">Why company email signatures need managing</h2>
                <p>Without a system, every employee designs their own signature. You end up with five versions of the logo, outdated job titles and phone numbers nobody answers. Consistent company email signatures make every email look like it comes from the same business, and they turn thousands of everyday emails into brand impressions.</p>
                <h2 id="csv">Generate everyone's signature from a CSV</h2>
                <p>Design the signature once, then let the spreadsheet do the rest:</p>
                {steps}
                {fig1}
                {callout}
                <h2 id="library">Manage every signature in one library</h2>
                <p>Every signature you create lands in <strong>My signatures</strong>. Search by name, email or title, and for each person you can:</p>
                <ul>
                    <li><strong>Copy</strong> the signature, ready to paste into Gmail, Outlook or Apple Mail.</li>
                    <li><strong>Get the HTML code</strong> if you deploy signatures yourself.</li>
                    <li><strong>See analytics</strong> for the links in that signature.</li>
                    <li><strong>Delete</strong> signatures for people who leave.</li>
                </ul>
                {fig2}
                <h2 id="workspace">Google Workspace and Microsoft 365 teams</h2>
                <p>SignTry works for teams on Google Workspace, Microsoft 365 or a mix of both. Each signature is HTML made for email apps, with hosted images, so it looks the same whether a colleague uses Gmail, Outlook on Windows, Outlook on Mac or Apple Mail. Share each person's signature with them and they paste it in. Our <a href="../guides/how-to-create-an-email-signature-in-outlook.html">Outlook guide</a> and <a href="../posts/how-to-create-an-email-signature-in-gmail.html">Gmail guide</a> walk them through it.</p>
                <h2 id="price">Priced per signature, not per seat</h2>
                <p>Most email signature management platforms charge per user with a minimum number of seats. SignTry charges for the number of signatures you need, from 5 up to 250 and beyond, with every feature included. A 25-person team pays $22 a month on yearly billing. <a href="../pricing.html">Compare plans</a>.</p>''',
    grid_title='Built for teams of every size', grid_sub='From a 5-person agency to a 250-agent brokerage.',
    grid=[('table', 'CSV import', 'One row per person. Only the first name is required.'),
          ('image', 'Photos from the CSV', 'Match file names or use photo URLs.'),
          ('palette', 'One brand', 'Template, colors, logo and banner set once for everyone.'),
          ('code', 'Copy or export HTML', 'Paste into any email app or deploy it yourself.'),
          ('chart', 'Analytics per person', 'See which signatures and links get clicked.'),
          ('shield', 'No seat minimums', 'Pay for the signatures you need, nothing more.')],
    faqs=[('What is email signature management?', 'Email signature management means creating, updating and controlling the email signatures used across a company from one place, so every employee has a consistent, on-brand signature with correct details.'),
          ('What should my CSV file contain?', 'One row per person. Only the first name is required. Add columns for last name, job title, email, phone and photo as needed. Download the CSV template inside SignTry to start with the right column names.'),
          ('How do I add photos for everyone?', 'Either upload the photo files and put each file name (for example <code>jane.jpg</code>) in the photo column, or put an https link to the photo in that column. Rows without a photo still get a signature.'),
          ('Does it work with Google Workspace and Microsoft 365?', 'Yes. Signatures are standard HTML with hosted images, so they work in Gmail, Outlook and Apple Mail for both Google Workspace and Microsoft 365 accounts.'),
          ('How much does it cost for a team?', 'Team plans start at $7 a month for 5 signatures on yearly billing and go down to $0.60 per signature at 250. All features are included. See <a href="../pricing.html">pricing</a>.')],
    related=[('Pricing', 'Pay per signature, not per seat', 'pricing.html'),
             ('Examples', 'Company email signature examples', 'examples/email-signature-examples.html'),
             ('Examples', 'Real estate email signatures', 'examples/real-estate-email-signature.html')],
)

ANALYTICS = dict(
    path='features/email-signature-analytics.html', crumb='Email signature analytics', tag='Analytics',
    title='Email Signature Analytics & Link Click Tracking | SignTry',
    desc='Email signature analytics that show which links get clicked: per month, per day, per link and per signature, plus a monthly goal. In every team plan.',
    h1='Email signature analytics that show what gets clicked',
    lead='SignTry email signature analytics track every click on the links in your signature, from your website and LinkedIn to your “Book a call” button. See what works, set a monthly goal, and turn your sign-off into a lead source.',
    video='analytics', video_label='SignTry email signature analytics dashboard with link clicks per month',
    stills=['analytics-70.jpg'],
    cta_h='Find out what your signature is really worth',
    article='''                {toc}
                <h2 id="what">What email signature analytics measure</h2>
                <p>Your signature goes out in every email you send, often hundreds a week. Email signature tracking shows whether anyone acts on it. The SignTry dashboard counts <strong>link clicks</strong> on every link in your signature and breaks them down so you can see what is working.</p>
                {tbl}
                {fig1}
                <h2 id="use">How to use your signature data</h2>
                <ol>
                    <li><strong>Move your best link first.</strong> If “Book a call” gets three times the clicks of your website, make it the button.</li>
                    <li><strong>Test one change at a time.</strong> Swap your banner or call to action, then compare next month's clicks.</li>
                    <li><strong>Compare people on your team.</strong> Filter by signature to see which layouts and titles get the most engagement.</li>
                    <li><strong>Set a monthly goal.</strong> The goal tracker shows your progress, for example 238 of 325 clicks.</li>
                </ol>
                {callout}
                <h2 id="included">Included in every team plan</h2>
                <p>Many tools only unlock email signature analytics on their most expensive plans. With SignTry, analytics are part of every team plan from 5 signatures up. <a href="../pricing.html">See pricing</a>.</p>''',
    grid_title='Everything in the dashboard', grid_sub='Clicks are counted in UTC, so teams in different time zones see the same numbers.',
    grid=[('chart', 'Clicks per month', 'Spot trends across the last six months.'),
          ('cal', 'Last 7 days', 'See which days your signature works hardest.'),
          ('link', 'Clicks by link', 'Website, LinkedIn, booking button and more.'),
          ('target', 'Monthly goal', 'Set a target and track your progress.'),
          ('users', 'Per signature', 'Filter the dashboard by person.'),
          ('mailcheck', 'Works in every inbox', 'Tracked links work in Gmail, Outlook, Apple Mail and Yahoo.')],
    faqs=[('What does email signature tracking measure?', 'SignTry counts clicks on the links in your signature, such as your website, social profiles and booking button, and shows them per month, per day, per link and per signature.'),
          ('Can I set a click goal?', 'Yes. Set a monthly goal on the dashboard and a progress bar shows how close you are, for example 238 of 325 clicks.'),
          ('Can I see analytics for each person on my team?', 'Yes. Pick a signature from the menu at the top of the dashboard to see that person’s clicks, or view the totals for everyone.'),
          ('Are analytics included in every plan?', 'Analytics are included in every team plan, from 5 signatures up. See <a href="../pricing.html">pricing</a>.'),
          ('Which time zone are clicks counted in?', 'Clicks are counted in UTC so every team member sees the same numbers.')],
    related=[('Feature', 'Free email signature generator', 'features/email-signature-generator.html'),
             ('Examples', 'Sales and business signature examples', 'examples/email-signature-examples.html'),
             ('Pricing', 'Analytics on every team plan', 'pricing.html')],
)

HTML_SIG = dict(
    path='features/html-email-signature.html', crumb='HTML email signatures', tag='Works everywhere',
    title='HTML Email Signature for Gmail, Outlook & Apple Mail | SignTry',
    desc='Create an HTML email signature that looks right in Gmail, Outlook, Apple Mail and Yahoo Mail. Hosted images, mobile-friendly layout and copy-paste install.',
    h1='HTML email signatures that work in every inbox',
    lead='SignTry builds your HTML email signature for email apps, with hosted images, so it looks the same in Gmail, Outlook, Apple Mail and Yahoo Mail, on desktop and on phones. Copy it in one click; no code required.',
    video='install-signature', video_label='Pasting an HTML email signature into a Gmail message',
    stills=['install-signature-35.jpg'],
    cta_h='Get a signature that works in every inbox',
    article='''                {toc}
                <h2 id="why">Why HTML email signatures break, and how we fix it</h2>
                <p>Email apps are not web browsers. Outlook on Windows uses Microsoft Word to display email, Gmail strips many styles, and some apps block images by default. A signature that looks fine in a web page can arrive broken. SignTry is built around those limits:</p>
                <ul>
                    <li><strong>Email-safe layout.</strong> Every template is made to hold up in Gmail, Outlook, Apple Mail and Yahoo Mail.</li>
                    <li><strong>Hosted images.</strong> Photos and logos are optimized and hosted when you save, so they load instead of arriving as attachments.</li>
                    <li><strong>Mobile check.</strong> Switch the live preview to phone view before you save.</li>
                </ul>
                {fig1}
                <h2 id="install">How to add your HTML email signature</h2>
                <p>Click <strong>Copy</strong> on your signature, then paste it into your email app's signature settings. Here is where to find them:</p>
                {tbl}
                {callout}
                <h2 id="code">Need the raw HTML code?</h2>
                <p>Each signature in your library has a code button that gives you the HTML. Use it to deploy signatures through your own tools or to paste into apps that only accept HTML, such as Apple Mail on a Mac or some CRM and help desk tools.</p>''',
    grid_title='Tested in the apps your team uses', grid_sub='One signature, the same look everywhere.',
    grid=[('mail', 'Gmail and Google Workspace', 'Web, Android and iPhone apps.'),
          ('mailcheck', 'Outlook and Microsoft 365', 'New Outlook, classic Outlook, Outlook on the web and Mac.'),
          ('apple', 'Apple Mail', 'iPhone, iPad and Mac.'),
          ('mail', 'Yahoo Mail', 'Desktop and mobile.'),
          ('cloud', 'Hosted images', 'No attachments, no broken image icons.'),
          ('phone', 'Mobile-friendly', 'Preview the phone layout before you save.')],
    faqs=[('What is an HTML email signature?', 'An HTML email signature is a signature built with HTML code, so it can include formatting, a photo, a logo, colored text and clickable links and icons, instead of plain text only.'),
          ('How do I add an HTML signature to Gmail?', 'Copy your signature in SignTry, then in Gmail open Settings, See all settings, General, Signature, create a new signature and paste it. Our <a href="../posts/how-to-create-an-email-signature-in-gmail.html">Gmail signature guide</a> has screenshots.'),
          ('How do I add an HTML signature to Apple Mail?', 'On a Mac, open Mail, Settings, Signatures, add a new signature and paste. On iPhone, go to Settings, Apps, Mail, Signature and paste. See our <a href="../guides/how-to-change-email-signature-on-iphone.html">iPhone and Apple Mail guide</a>.'),
          ('Why do my signature images show as attachments?', 'That happens when images are embedded in the email. SignTry hosts your images online and links to them, which is the most reliable way to make them display.'),
          ('Will my signature work in Outlook?', 'Yes. SignTry signatures are built with Outlook-safe HTML. Follow our <a href="../guides/how-to-create-an-email-signature-in-outlook.html">Outlook email signature guide</a> to install it.')],
    related=[('Guide', 'How to create an email signature in Outlook', 'guides/how-to-create-an-email-signature-in-outlook.html'),
             ('Guide', 'How to change your email signature on iPhone', 'guides/how-to-change-email-signature-on-iphone.html'),
             ('Guide', 'How to change your signature in Yahoo Mail', 'guides/how-to-change-signature-in-yahoo-mail.html')],
)


def fill():
    p = '../'
    TEMPLATES['article'] = TEMPLATES['article'].format(
        toc=toc([('pick', 'Find the right template'), ('industries', 'Templates by industry'), ('good', 'What makes a good template'), ('switch', 'Change templates any time')]),
        fig1=fig(p, 'media/stills/template-35.jpg', 'Choosing a side-by-side email signature template in SignTry', 'Selecting a template. The live preview updates right away.'),
        tbl=table(['Template group', 'What it highlights'], [
            ['Real estate', 'Headshot, brokerage logo, license number, listings link'],
            ['Doctors &amp; healthcare', 'Credentials, practice name, appointment booking link'],
            ['Legal &amp; finance', 'Firm name, title, office address, compliance note'],
            ['Sales &amp; corporate', 'Direct line, booking button, company logo'],
            ['Marketing &amp; agencies', 'Brand colors, banner, portfolio and social links'],
            ['Freelancers', 'Photo, portfolio, rates or booking page'],
            ['General', 'Clean layouts for anyone, including students and job seekers']]),
        callout=callout('Tip: the simplest template is often the most professional. If you are unsure, pick a side-by-side layout with your photo, name, title and one link.'))
    GENERATOR['article'] = GENERATOR['article'].format(
        toc=toc([('steps', 'Create an email signature in 6 steps'), ('logo', 'Add a logo'), ('photo', 'Add a photo'), ('links', 'Social icons and links')]),
        steps=steps(['<strong>Template.</strong> Pick a layout by industry and style: side by side or stacked.',
                     '<strong>Details.</strong> Your name, job title, company, email and phone. Only your first name is required; empty fields are left out.',
                     '<strong>Branding.</strong> Add a company logo, a banner, a verified badge and a handwritten signature.',
                     '<strong>Links.</strong> Social icons, your website and a call-to-action button.',
                     '<strong>Style.</strong> Colors, text and the size and shape of your photo.',
                     '<strong>Save.</strong> Save it for yourself, or create one for every person on your team from a CSV.']),
        fig1=fig(p, 'media/stills/personalize-35.jpg', 'Entering name, job title and company in the SignTry email signature generator', 'The Details step. Only your first name is required.'),
        fig2=fig(p, 'media/stills/personalize-70.jpg', 'Live preview of an email signature with photo and handwritten signature', 'Your photo and handwritten signature in the live preview.'),
        callout=callout('Ready to use it? Follow our step-by-step guides for <a href="../guides/how-to-create-an-email-signature-in-outlook.html">Outlook</a>, <a href="../posts/how-to-create-an-email-signature-in-gmail.html">Gmail</a>, <a href="../guides/how-to-change-email-signature-on-iphone.html">iPhone and Apple Mail</a> and <a href="../guides/how-to-change-signature-in-yahoo-mail.html">Yahoo Mail</a>.'))
    MANAGEMENT['article'] = MANAGEMENT['article'].format(
        toc=toc([('why', 'Why company signatures need managing'), ('csv', 'Generate signatures from a CSV'), ('library', 'Manage every signature'), ('workspace', 'Google Workspace and Microsoft 365'), ('price', 'Pricing for teams')]),
        steps=steps(['<strong>Design once.</strong> Pick a template and set your logo, colors, banner and links.',
                     '<strong>Choose “For my team”</strong> in the last step and download the CSV template.',
                     '<strong>Fill in the spreadsheet</strong> in Excel, Google Sheets or Numbers: one row per person. Only the first name is required.',
                     '<strong>Add photos (optional).</strong> Upload image files and put the file name in the photo column (for example <code>jane.jpg</code>), or paste an https link.',
                     '<strong>Upload and review.</strong> SignTry shows every row with its email, title and photo status.',
                     '<strong>Click Generate.</strong> Every signature is created at once, ready to copy.']),
        fig1=fig(p, 'media/stills/team-generation-50.jpg', 'Six team members imported from a CSV, ready to generate email signatures', 'Reviewing the imported team before generating signatures.'),
        fig2=fig(p, 'media/stills/team-generation-88.jpg', 'Library of generated company email signatures with copy, code and analytics buttons', 'Every generated signature, ready to copy, export or track.'),
        callout=callout('Tip: start with a test file of two or three people to check the layout, then upload the full team.'))
    ANALYTICS['article'] = ANALYTICS['article'].format(
        toc=toc([('what', 'What email signature analytics measure'), ('use', 'How to use your signature data'), ('included', 'Included in every team plan')]),
        tbl=table(['Report', 'What it tells you'], [
            ['This month, last month, all time', 'Total clicks, with the change versus last month'],
            ['Clicks per month', 'A six-month trend so you can spot growth or drop-offs'],
            ['Clicks in the last 7 days', 'Which weekdays your signature gets the most attention'],
            ['Clicks by link', 'How each link performs: website, LinkedIn, booking button and more'],
            ['Monthly goal', 'Your progress toward a click target you set']]),
        fig1=fig(p, 'media/stills/analytics-70.jpg', 'Email signature analytics bar chart showing link clicks per month', 'Clicks per month, with details on hover.'),
        callout=callout('A booking button is usually the most-clicked link in a signature. If you sell anything, add one and watch the “Clicks by link” report.'))
    HTML_SIG['article'] = HTML_SIG['article'].format(
        toc=toc([('why', 'Why HTML signatures break'), ('install', 'How to add your HTML signature'), ('code', 'Get the raw HTML code')]),
        fig1=fig(p, 'media/stills/install-signature-35.jpg', 'Writing a new email in Gmail before inserting an HTML email signature', 'Your signature, ready to use in Gmail.'),
        tbl=table(['Email app', 'Where to paste your signature', 'Guide'], [
            ['Gmail', 'Settings → See all settings → General → Signature', '<a href="../posts/how-to-create-an-email-signature-in-gmail.html">Gmail guide</a>'],
            ['Outlook (new and web)', 'Settings → Account → Signatures', '<a href="../guides/how-to-create-an-email-signature-in-outlook.html">Outlook guide</a>'],
            ['Outlook (classic, Windows)', 'File → Options → Mail → Signatures', '<a href="../guides/how-to-create-an-email-signature-in-outlook.html#classic">Classic Outlook</a>'],
            ['Apple Mail (Mac)', 'Mail → Settings → Signatures', '<a href="../guides/how-to-change-email-signature-on-iphone.html#mac">Apple Mail guide</a>'],
            ['iPhone and iPad', 'Settings → Apps → Mail → Signature', '<a href="../guides/how-to-change-email-signature-on-iphone.html">iPhone guide</a>'],
            ['Yahoo Mail', 'Settings → More Settings → Writing email → Signature', '<a href="../guides/how-to-change-signature-in-yahoo-mail.html">Yahoo guide</a>']]),
        callout=callout('Paste with <strong>Ctrl+V</strong> (or <strong>Cmd+V</strong> on Mac), not “paste as plain text”, or the formatting and images will be lost.'))


def build():
    fill()
    return [feature_page(f) for f in (TEMPLATES, GENERATOR, MANAGEMENT, ANALYTICS, HTML_SIG)]
