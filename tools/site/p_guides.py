from layout import *
from links import related


def article_page(a, kind='Guide', hub=('Guides &amp; examples', 'guides.html')):
    path = a['path']
    p = '../'
    trail = [('Home', ''), (hub[0], hub[1]), (a['crumb'], path)]
    img = a.get('image', 'media/demo.jpg')
    body = f'''    <header class="hero page-hero">
        <div class="wrap">
            {crumbs_html(p, trail)}
            <span class="tag">{kind}</span>
            <h1>{a['h1']}</h1>
            <p class="lead">{a['lead']}</p>
            <p class="alt" style="margin-top:0">Updated October 28, 2026 · {a['mins']} min read · By the SignTry team</p>
        </div>
    </header>

    <section class="plain">
        <div class="wrap">
            <article class="prose">
{a['article']}
            </article>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-head"><h2>Frequently asked questions</h2></div>
            {faq_html(a['faqs'])}
        </div>
    </section>

    <section class="plain">
        <div class="wrap">
            <div class="sec-head"><h2>Related guides</h2></div>
            {related_html(p, related(path, a['related']))}
        </div>
    </section>

{cta_band(p, a.get('cta_h', 'Skip the formatting. Get a signature that just works.'), a.get('cta_sub', 'Build a professional email signature in 2 minutes, then paste it into Outlook, Gmail, Apple Mail or Yahoo. No credit card required.'))}'''
    schema = [crumbs_schema([(re.sub('&amp;', '&', n), u) for n, u in trail]),
              article_schema(path, a['h1'], a['desc'], img), faq_schema(a['faqs'])]
    return path, page(path, a['title'], a['desc'], body.replace('{P}', p), schema, og_image=img)


def answer(text):
    return f'<div class="answer"><p>{text}</p></div>'


def h2(id_, t):
    return f'<h2 id="{id_}">{t}</h2>'


SIGNTRY_BOX = '''<p>Writing a signature by hand in a settings box is fiddly: no photo cropping, no layout, and it looks different in every app. With <a href="../features/email-signature-generator.html">SignTry's free email signature generator</a> you pick a template, fill in your details, click <strong>Copy</strong> and paste it into the signature box above. Your photo and logo are hosted for you, so they show up for every recipient.</p>'''


# ---------------------------------------------------------------- Outlook
OUTLOOK = dict(
    path='guides/how-to-create-an-email-signature-in-outlook.html', crumb='Outlook email signature', mins=7,
    title='How to Make an Email Signature in Outlook (2026 Guide)',
    desc='How to make an email signature in Outlook step by step: new and classic Outlook, Outlook on the web, Mac and mobile. Plus how to edit it and add a logo.',
    h1='How to make an email signature in Outlook',
    lead='Here is how to make an email signature in Outlook in under two minutes, whichever version you use: new Outlook for Windows, classic Outlook, Outlook on the web, Outlook for Mac or the Outlook mobile app. You will also learn how to change, edit and add a logo to your Outlook signature.',
)
OUTLOOK['article'] = f'''                {answer('<strong>Quick answer:</strong> In new Outlook and Outlook on the web, go to <strong>Settings → Account → Signatures</strong>, select <strong>+ New signature</strong>, type or paste your signature, choose it as the default for new messages and replies, then click <strong>Save</strong>. In classic Outlook for Windows, go to <strong>File → Options → Mail → Signatures → New</strong>.')}
                {toc([('which', 'Which Outlook do I have?'), ('new', 'New Outlook and Outlook on the web'), ('classic', 'Classic Outlook for Windows'), ('mac', 'Outlook for Mac'), ('mobile', 'Outlook on iPhone and Android'), ('change', 'How to change or edit your Outlook signature'), ('image', 'How to add a logo or image'), ('fix', 'Signature not showing? Fixes')])}
                {h2('which', 'Which Outlook do I have?')}
                <p>Microsoft currently ships several versions of Outlook, and the signature settings are in a different place in each one:</p>
                {table(['If you see…', 'You are using', 'Jump to'], [
    ['A <strong>New Outlook</strong> toggle at the top right, and a gear icon for settings', 'New Outlook for Windows', '<a href="#new">Steps</a>'],
    ['Outlook in a browser at outlook.com or outlook.office.com', 'Outlook on the web (Microsoft 365 or Outlook.com)', '<a href="#new">Steps</a>'],
    ['A <strong>File</strong> tab in the ribbon', 'Classic Outlook for Windows', '<a href="#classic">Steps</a>'],
    ['An <strong>Outlook</strong> menu in the Mac menu bar', 'Outlook for Mac', '<a href="#mac">Steps</a>'],
    ['The app on your phone', 'Outlook for iOS or Android', '<a href="#mobile">Steps</a>']])}
                {h2('new', 'How to create an email signature in new Outlook and Outlook on the web')}
                <p>New Outlook for Windows, Outlook on the web and Outlook.com share the same settings, and in Microsoft 365 your signature can follow you between them.</p>
                {steps(['Select the <strong>Settings</strong> gear icon at the top right.', 'Go to <strong>Account → Signatures</strong>.', 'Select <strong>+ New signature</strong> and give it a name, such as “Work”.', 'Type your signature in the editor, or paste one you made in SignTry. Use the toolbar for bold, colors, links and images.', 'Under <strong>Select default signatures</strong>, choose it for <strong>new messages</strong> and for <strong>replies and forwards</strong>.', 'Select <strong>Save</strong>.'])}
                {callout('If you have more than one email account in Outlook, pick the right account at the top of the Signatures page before you choose the defaults.')}
                {h2('classic', 'How to create an email signature in classic Outlook for Windows')}
                {steps(['Select <strong>File → Options → Mail</strong>.', 'Select <strong>Signatures…</strong>.', 'On the <strong>E-mail Signature</strong> tab, select <strong>New</strong>, type a name and select <strong>OK</strong>.', 'Type or paste your signature in the <strong>Edit signature</strong> box.', 'Under <strong>Choose default signature</strong>, pick the email account and set the signature for <strong>New messages</strong> and <strong>Replies/forwards</strong>.', 'Select <strong>OK</strong>.'])}
                <p>Shortcut: when you are writing an email, select <strong>Message → Signature → Signatures…</strong> to open the same window.</p>
                {h2('mac', 'How to create an email signature in Outlook for Mac')}
                {steps(['Open Outlook and choose <strong>Outlook → Settings</strong> in the menu bar.', 'Select <strong>Signatures</strong>.', 'Select <strong>+</strong>, name the signature and type or paste it in the editor.', 'Save, then under <strong>Default signatures</strong> choose it for new messages and replies for each account.'])}
                {h2('mobile', 'How to add a signature in Outlook on iPhone and Android')}
                {steps(['Open the Outlook app and tap your profile picture at the top left.', 'Tap the <strong>Settings</strong> gear.', 'Tap <strong>Signature</strong>.', 'Replace the default text with your signature. Turn on <strong>Per account signature</strong> if you want a different one for each account.'])}
                <p>The mobile app keeps signatures simple. Text and links work well; logos and complex layouts are best set up on desktop or web. Mobile and desktop signatures are separate, so set up both.</p>
                {h2('change', 'How to change or edit your email signature in Outlook')}
                <p>To change it later, go back to the same Signatures page, select the signature, edit it and save. Our step-by-step guide on <a href="how-to-change-email-signature-in-outlook.html">how to change your email signature in Outlook</a> covers every version and what to do when the old signature keeps appearing.</p>
                <p>Sending the same email again and again? Save it once and reuse it: here is <a href="how-to-create-an-email-template-in-outlook.html">how to create an email template in Outlook</a>. Keep your signature out of the template, and Outlook adds the current one every time.</p>
                {h2('image', 'How to add a logo or image to your Outlook signature')}
                <p>In the signature editor, place your cursor where the image should go and use the <strong>image</strong> button in the toolbar (classic Outlook has an <strong>Insert Picture</strong> icon). Keep images small: a logo around 150–200 pixels wide and a headshot around 100 pixels square look sharp without making emails heavy. Our <a href="email-signature-size.html">email signature size guide</a> has exact dimensions.</p>
                <p>Images inserted from your computer are embedded in every email, and some recipients see them as attachments. Signatures made in SignTry use hosted images instead, which display more reliably.</p>
                {h2('fix', 'Outlook signature not showing? Common fixes')}
                <ul>
                    <li><strong>No default is set.</strong> Choose the signature for new messages and for replies; they are separate settings.</li>
                    <li><strong>Wrong account.</strong> Each account has its own defaults. Check you set it on the account you send from.</li>
                    <li><strong>Different device.</strong> Classic Outlook stores signatures on the computer, so a signature made on your laptop will not appear on your desktop. Set it up on each device, or use new Outlook or the web where signatures can roam.</li>
                    <li><strong>Plain text emails.</strong> If you send in plain text format, formatting and images are removed. Switch to HTML format.</li>
                </ul>
                <h2>Make a professional Outlook signature in 2 minutes</h2>
                {SIGNTRY_BOX}'''
OUTLOOK['faqs'] = [
    ('How do I change my email signature in Outlook?', 'In new Outlook or Outlook on the web, go to Settings, Account, Signatures, select your signature, edit it and click Save. In classic Outlook, go to File, Options, Mail, Signatures, select the signature and edit it in the Edit signature box.'),
    ('How do I create a signature in Outlook 365?', 'Outlook in Microsoft 365 uses the new Outlook settings: Settings, Account, Signatures, then + New signature. Type or paste your signature, set your defaults and click Save.'),
    ('Why is my signature not showing in Outlook?', 'Usually because no default signature is set for new messages or for replies, or it is set on a different account. In classic Outlook, signatures are also stored per computer.'),
    ('Can I have more than one signature in Outlook?', 'Yes. Create as many as you like, for example a full one for new emails and a short one for replies, and choose a default for each.'),
    ('What size should my Outlook signature image be?', 'A logo around 150–200 pixels wide and a headshot around 100 pixels square work well. Keep the whole signature under 600 pixels wide. See our <a href="email-signature-size.html">email signature size guide</a>.'),
]
OUTLOOK['related'] = [('Guide', 'How to change your email signature on iPhone', 'guides/how-to-change-email-signature-on-iphone.html'),
                      ('Guide', 'How to create an email signature in Gmail', 'posts/how-to-create-an-email-signature-in-gmail.html'),
                      ('Guide', 'Email signature size: the right dimensions', 'guides/email-signature-size.html')]

# ---------------------------------------------------------------- iPhone / Apple Mail
IPHONE = dict(
    path='guides/how-to-change-email-signature-on-iphone.html', crumb='iPhone email signature', mins=6,
    title='How to Change Your Email Signature on iPhone (and Mac Mail)',
    desc='How to change your email signature on iPhone, step by step. Remove “Sent from my iPhone”, keep formatting, and add an HTML signature to Apple Mail on Mac.',
    h1='How to change your email signature on iPhone',
    lead='You can change your email signature on iPhone in about 30 seconds and finally replace “Sent from my iPhone”. This guide covers the iPhone Mail app, Outlook and Gmail on iPhone, and how to add an HTML signature to Apple Mail on a Mac.',
)
IPHONE['article'] = f'''                {answer('<strong>Quick answer:</strong> Open <strong>Settings → Apps → Mail → Signature</strong> (on iOS 17 and earlier: <strong>Settings → Mail → Signature</strong>), delete “Sent from my iPhone”, and type or paste your new signature. It saves automatically.')}
                {toc([('iphone', 'Change your iPhone Mail signature'), ('format', 'Keep formatting when you paste'), ('apps', 'Outlook and Gmail on iPhone'), ('mac', 'Add a signature in Apple Mail on Mac'), ('html', 'Add an HTML signature to Apple Mail')])}
                {h2('iphone', 'How to change your email signature on iPhone Mail')}
                {steps(['Open the <strong>Settings</strong> app.', 'Scroll down and tap <strong>Apps</strong>, then <strong>Mail</strong>. (On iOS 17 or earlier, tap <strong>Mail</strong> directly.)', 'Scroll to <strong>Composing</strong> and tap <strong>Signature</strong>.', 'Choose <strong>All Accounts</strong> for one signature everywhere, or <strong>Per Account</strong> for a different one on each email address.', 'Delete “Sent from my iPhone” and type or paste your signature. There is no save button; it saves as you type.'])}
                <p>The same steps work on iPad, where the default text is “Sent from my iPad”.</p>
                {h2('format', 'How to keep bold text, colors and links')}
                <p>Select text in the signature box and tap <strong>B<em>I</em><u>U</u></strong> in the menu to make it bold, italic or underlined. To use a designed signature, open it on your iPhone (for example, email it to yourself), copy it, and paste it into the Signature field.</p>
                {callout('Lost the formatting after pasting? <strong>Shake your iPhone</strong> right away and tap <strong>Undo</strong>. iOS often strips styles in a second step, and undoing that step brings your colors and layout back.')}
                <p>Images in iPhone signatures are hit and miss: some recipients see them as attachments. A signature with hosted images, like the ones <a href="../features/email-signature-generator.html">SignTry generates</a>, avoids this.</p>
                {h2('apps', 'How to change your signature in Outlook and Gmail on iPhone')}
                <p>If you use the Outlook or Gmail app instead of Apple Mail, the signature lives inside that app:</p>
                {table(['App', 'Where to find the signature'], [
    ['Outlook for iPhone', 'Tap your profile picture → Settings gear → <strong>Signature</strong>'],
    ['Gmail for iPhone', 'Tap the menu → <strong>Settings</strong> → your account → <strong>Signature settings</strong> → turn on <strong>Mobile signature</strong>'],
    ['Yahoo Mail for iPhone', 'Tap your profile icon → <strong>Settings</strong> → <strong>Signature</strong>. See our <a href="how-to-change-signature-in-yahoo-mail.html">Yahoo Mail guide</a>']])}
                {h2('mac', 'How to add a signature in Apple Mail on Mac')}
                {steps(['Open <strong>Mail</strong> and choose <strong>Mail → Settings</strong> (called Preferences on older macOS).', 'Click <strong>Signatures</strong>.', 'Select an account in the left column and click <strong>+</strong>.', 'Name the signature and type or paste it on the right.', 'Uncheck <strong>Always match my default message font</strong> to keep your own fonts and colors.', 'Use the <strong>Choose Signature</strong> menu to make it the default for that account.'])}
                {h2('html', 'How to add an HTML signature to Apple Mail')}
                <p>Pasting a designed signature into the Signatures window works for most people. If yours loses its layout, you can install the HTML directly:</p>
                {steps(['Create a placeholder signature in <strong>Mail → Settings → Signatures</strong> and quit Mail.', 'In Finder, choose <strong>Go → Go to Folder</strong> and open <code>~/Library/Mail/</code>, then the newest <code>V</code> folder (for example <code>V10</code>), then <code>MailData/Signatures</code>.', 'Open the newest <code>.mailsignature</code> file in TextEdit, keep the header lines at the top, and replace everything below them with your signature HTML.', 'Save, then select the file, choose <strong>File → Get Info</strong> and tick <strong>Locked</strong> so Mail does not overwrite it.', 'Reopen Mail. Your HTML signature appears in the Signatures window.'])}
                <p>Every SignTry signature has an HTML code button for exactly this. <a href="../features/html-email-signature.html">Learn more about HTML email signatures</a>.</p>
                <h2>Get a signature worth putting on your iPhone</h2>
                {SIGNTRY_BOX}'''
IPHONE['faqs'] = [
    ('How do I remove “Sent from my iPhone”?', 'Go to Settings, Apps, Mail, Signature (or Settings, Mail, Signature on older iOS) and delete the text. Leave it empty for no signature, or type your own.'),
    ('Why did my iPhone signature lose its formatting?', 'iOS sometimes strips styles after you paste. Shake your iPhone straight after pasting and tap Undo to restore the formatting.'),
    ('Can I have a different signature for each email account on iPhone?', 'Yes. In the Signature settings, choose Per Account and enter a signature under each address.'),
    ('Can I add a logo to my iPhone email signature?', 'You can paste a signature that contains a logo, but embedded images often arrive as attachments. Signatures with hosted images, like SignTry signatures, display more reliably.'),
    ('Does my iPhone signature sync to my Mac?', 'No. iPhone Mail and Mac Mail signatures are set separately, so add your signature on each device.'),
]
IPHONE['related'] = [('Guide', 'How to make an email signature in Outlook', 'guides/how-to-create-an-email-signature-in-outlook.html'),
                     ('Feature', 'HTML email signatures for every inbox', 'features/html-email-signature.html'),
                     ('Guide', 'How to change your signature in Yahoo Mail', 'guides/how-to-change-signature-in-yahoo-mail.html')]

# ---------------------------------------------------------------- Yahoo
YAHOO = dict(
    path='guides/how-to-change-signature-in-yahoo-mail.html', crumb='Yahoo Mail signature', mins=4,
    title='How to Change Your Signature in Yahoo Mail (Desktop & App)',
    desc='How to add or change your signature in Yahoo Mail on desktop and in the Yahoo Mail app, step by step, plus how to add links, images and a professional design.',
    h1='How to change your signature in Yahoo Mail',
    lead='Here is how to change your signature in Yahoo Mail, or add one for the first time, on a computer and in the Yahoo Mail app. It takes about a minute, and you can add formatting, links and images on desktop.',
)
YAHOO['article'] = f'''                {answer('<strong>Quick answer:</strong> On a computer, click the <strong>Settings</strong> gear → <strong>More Settings</strong> → <strong>Writing email</strong>, turn on the <strong>Signature</strong> switch for your address, and type or paste your signature. Changes save automatically.')}
                {toc([('desktop', 'Change your signature on a computer'), ('app', 'Change your signature in the Yahoo Mail app'), ('design', 'Add links, images and formatting'), ('fix', 'Troubleshooting')])}
                {h2('desktop', 'How to add a signature in Yahoo Mail on a computer')}
                {steps(['Sign in to Yahoo Mail in your browser.', 'Click the <strong>Settings</strong> gear icon at the top right.', 'Click <strong>More Settings</strong>.', 'Select <strong>Writing email</strong>.', 'Under <strong>Signature</strong>, turn on the switch next to the email address you want.', 'Type or paste your signature in the box. It is saved automatically; click <strong>Back to Inbox</strong> when you are done.'])}
                <p>To change your signature later, follow the same steps and edit the text in the box. To remove it, turn the switch off.</p>
                {h2('app', 'How to change your signature in the Yahoo Mail app')}
                {steps(['Open the Yahoo Mail app on iPhone or Android.', 'Tap your profile icon or the menu, then <strong>Settings</strong>.', 'Tap <strong>Signature</strong>.', 'Turn the signature on for your account and edit the text. The default is “Sent from Yahoo Mail for iPhone” or “…for Android”.'])}
                <p>The app signature is separate from the desktop one and is mostly plain text, so keep it short: your name, title and one link.</p>
                {h2('design', 'How to add links, images and formatting')}
                <p>The desktop signature box has a small toolbar for bold, italics, colors and links. To add an image, the most reliable way is to paste a signature whose images are hosted online. Images copied from your computer may not show for every recipient.</p>
                <p>For a polished look, build your signature in <a href="../features/email-signature-generator.html">SignTry</a>, click <strong>Copy</strong>, and paste it straight into the Yahoo signature box. Photos, logos and social icons come along. Need icons? See <a href="social-media-icons-for-email-signature.html">social media icons for email signatures</a>.</p>
                {h2('fix', 'Yahoo signature not showing?')}
                <ul>
                    <li><strong>The switch is off.</strong> Each address in Writing email has its own on/off switch.</li>
                    <li><strong>You are on the app.</strong> The app uses its own signature setting; set it there too.</li>
                    <li><strong>Pasted as plain text.</strong> Paste with Ctrl+V or Cmd+V, not “paste as plain text”, to keep formatting.</li>
                </ul>
                <h2>Make a Yahoo signature that stands out</h2>
                {SIGNTRY_BOX}'''
YAHOO['faqs'] = [
    ('How do I change my signature in Yahoo Mail?', 'Click the Settings gear, More Settings, Writing email, then edit the text in the Signature box for your address. Changes save automatically.'),
    ('How do I add a signature in Yahoo Mail on my phone?', 'In the Yahoo Mail app, tap your profile icon or menu, then Settings, Signature, and turn it on for your account.'),
    ('Can I add a picture to my Yahoo Mail signature?', 'Yes, on desktop. Paste a signature with hosted images for the most reliable result; images from your computer may not show for everyone.'),
    ('How do I remove “Sent from Yahoo Mail for iPhone”?', 'In the app, go to Settings, Signature, and either edit the text or turn the signature off.'),
]
YAHOO['related'] = [('Guide', 'How to change your email signature on iPhone', 'guides/how-to-change-email-signature-on-iphone.html'),
                    ('Guide', 'How to make an email signature in Outlook', 'guides/how-to-create-an-email-signature-in-outlook.html'),
                    ('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html')]

# ---------------------------------------------------------------- Size
SIZE = dict(
    path='guides/email-signature-size.html', crumb='Email signature size', mins=5,
    title='Email Signature Size: Dimensions for Images, Logos & Photos',
    desc='The right email signature size: overall dimensions plus logo, photo, banner and icon sizes in pixels, and the formats that work in Gmail and Outlook.',
    h1='Email signature size: the right dimensions for every part',
    lead='The ideal email signature size is no more than 600 pixels wide and roughly 100 to 200 pixels tall. Below are the exact dimensions for your photo, logo, banner and social icons, plus the file sizes and formats that display reliably in every inbox.',
    image='media/stills/personalize-70.jpg',
)
SIZE['article'] = f'''                {answer('<strong>Quick answer:</strong> Keep your email signature <strong>under 600px wide</strong> and about <strong>100–200px tall</strong>. Use a <strong>headshot around 80–120px</strong> square, a <strong>logo 30–60px tall</strong> and up to 200px wide, a <strong>banner up to 600×150px</strong>, and <strong>social icons 16–24px</strong>. Upload images at twice the display size so they look sharp on high-resolution screens.')}
                {toc([('chart', 'Email signature size chart'), ('overall', 'Overall signature dimensions'), ('photo', 'Photo size'), ('logo', 'Logo size'), ('banner', 'Banner size'), ('files', 'File size and formats'), ('text', 'Font size and length')])}
                {h2('chart', 'Email signature size chart')}
                {table(['Element', 'Display size', 'Upload at (2×)', 'Best format'], [
    ['Whole signature', 'Up to 600px wide, 100–200px tall', '—', '—'],
    ['Headshot photo', '80–120px square', '160–240px square', 'JPG'],
    ['Company logo', '30–60px tall, up to 200px wide', '60–120px tall', 'PNG (transparent)'],
    ['Banner', 'Up to 600×150px', 'Up to 1200×300px', 'JPG or PNG'],
    ['Social media icons', '16–24px', '32–48px', 'PNG'],
    ['Call-to-action button', 'About 120–180×32px', '2× display size', 'HTML button or PNG']])}
                {h2('overall', 'Overall email signature dimensions')}
                <p>Most email apps show messages in a column 600 to 800 pixels wide, and phones are narrower still. A signature up to <strong>600px wide</strong> fits everywhere without wrapping. Aim for <strong>100–200px tall</strong>: enough for a photo, four lines of text and a row of icons. Anything taller starts to feel like an advert.</p>
                {h2('photo', 'Email signature photo size')}
                <p>Display your headshot at <strong>80–120px square</strong>. Upload it at <strong>twice that size</strong> (for example 240×240px) so it stays crisp on Retina and high-DPI screens. Use a square crop with your face centered; SignTry crops it around your face automatically and lets you choose square, rounded or circle shapes.</p>
                {h2('logo', 'Email signature logo size')}
                <p>A logo <strong>30–60px tall</strong> and no wider than <strong>200px</strong> is easy to recognize without overpowering your name. SignTry shows logos about 28px tall next to your details. Use a <strong>transparent PNG</strong> so it looks right on light and dark themes, and trim any empty space around it before uploading.</p>
                {h2('banner', 'Email signature banner size')}
                <p>Banners promote an event, offer or new product under your signature. Keep them at most <strong>600px wide and 150px tall</strong>; 600×100px is a common choice. Put the message in the image itself in large text, since many people only glance at it.</p>
                {h2('files', 'File size and image formats')}
                <ul>
                    <li><strong>Keep each image under about 100KB</strong>, and the whole signature light, so emails load fast on mobile data.</li>
                    <li><strong>Use JPG for photos</strong> and <strong>PNG for logos and icons</strong>.</li>
                    <li><strong>Avoid SVG.</strong> Gmail and Outlook do not display SVG images in emails.</li>
                    <li><strong>Animated GIFs:</strong> classic Outlook for Windows shows only the first frame, so make sure it works as a still image.</li>
                    <li><strong>Host your images.</strong> Images embedded in the email often show up as attachments. SignTry hosts them for you.</li>
                </ul>
                {h2('text', 'Font size and signature length')}
                <p>Use <strong>14–16px</strong> for your name and <strong>12–14px</strong> for everything else, in a web-safe font like Arial, Helvetica, Verdana or Georgia. Our list of the <a href="email-signature-fonts.html">best fonts for email signatures</a> shows 12 safe picks. Keep the text to four or five lines. Gmail also limits signatures to <strong>10,000 characters</strong>, which a signature with lots of formatting can hit; if Gmail says your signature is too long, simplify it or use hosted images.</p>
                {fig('../', 'media/stills/personalize-70.jpg', 'Email signature preview with a correctly sized photo, name and handwritten signature', 'A well-proportioned signature: square photo, short text, one accent color.')}
                <h2>Get the sizes right automatically</h2>
                <p>SignTry resizes, crops and hosts every image for you, so your signature is the right size in every inbox without you opening an image editor. <a href="../features/email-signature-generator.html">Try the free email signature generator</a>.</p>'''
SIZE['faqs'] = [
    ('What is the best size for an email signature?', 'No more than 600 pixels wide and about 100–200 pixels tall, with four or five lines of text.'),
    ('What size should my email signature photo be?', 'Display it at 80–120 pixels square and upload it at twice that size, for example 240×240 pixels.'),
    ('What size should a logo be in an email signature?', 'About 30–60 pixels tall and up to 200 pixels wide. Use a transparent PNG.'),
    ('What is the best image size for an Outlook email signature?', 'The same as other apps: keep the whole signature under 600 pixels wide, logos up to 200 pixels wide and photos around 100 pixels square. Avoid SVG images, which Outlook does not show.'),
    ('Why is my email signature too long for Gmail?', 'Gmail allows up to 10,000 characters, including hidden formatting code. Simplify the layout or use hosted images instead of embedded ones.'),
]
SIZE['related'] = [('Guide', 'Social media icons for email signatures', 'guides/social-media-icons-for-email-signature.html'),
                   ('Feature', 'Email signature generator with logo and photo', 'features/email-signature-generator.html'),
                   ('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html')]

# ---------------------------------------------------------------- Social icons
SOC = ['linkedin', 'instagram', 'facebook', 'x', 'youtube', 'tiktok', 'whatsapp', 'github', 'behance', 'dribbble', 'pinterest', 'calendly']
SOC_NAMES = {'linkedin': 'LinkedIn', 'instagram': 'Instagram', 'facebook': 'Facebook', 'x': 'X (Twitter)', 'youtube': 'YouTube', 'tiktok': 'TikTok',
             'whatsapp': 'WhatsApp', 'github': 'GitHub', 'behance': 'Behance', 'dribbble': 'Dribbble', 'pinterest': 'Pinterest', 'calendly': 'Calendly'}
icon_grid = '<div class="provs" style="grid-template-columns:repeat(auto-fill,minmax(110px,1fr));margin:24px 0 32px">' + ''.join(
    f'<div class="prov"><img src="../images/social/{s}.svg" alt="{SOC_NAMES[s]} icon" width="40" height="40" loading="lazy" style="width:40px;height:40px">{SOC_NAMES[s]}</div>' for s in SOC) + '</div>'
SOCIAL = dict(
    path='guides/social-media-icons-for-email-signature.html', crumb='Social media icons', mins=5,
    title='Social Media Icons for Email Signature: Which, Size & How',
    desc='Social media icons for your email signature: which networks to include, the right icon size and colors, and how to add them in Gmail and Outlook.',
    h1='Social media icons for your email signature',
    lead='Social media icons for your email signature turn every email into a path to your LinkedIn, Instagram or portfolio. This guide covers which icons to include for your job, the right size and style, and how to add them in Gmail, Outlook and SignTry.',
)
SOCIAL['article'] = f'''                {answer('<strong>Quick answer:</strong> Add <strong>two to four</strong> social media icons that are relevant to your work, at <strong>16–24px</strong>, in your brand color or each network’s official color. Link each icon to your profile, not the network’s homepage, and use hosted PNG images, since Gmail and Outlook do not display SVG.')}
                {toc([('which', 'Which icons to include'), ('size', 'Icon size and style'), ('signtry', 'Add icons in SignTry'), ('manual', 'Add icons manually in Gmail or Outlook'), ('rules', 'Brand rules to follow')])}
                {icon_grid}
                {h2('which', 'Which social media icons should you include?')}
                <p>More icons is not better. Pick the profiles a contact would actually want to visit:</p>
                {table(['Your role', 'Icons to include'], [
    ['Sales, recruiting, consulting', 'LinkedIn, plus a booking link such as Calendly'],
    ['Real estate agents', 'Instagram, Facebook, LinkedIn, YouTube for property tours'],
    ['Designers and creatives', 'Behance or Dribbble, Instagram, LinkedIn'],
    ['Developers', 'GitHub, LinkedIn, X'],
    ['Creators and marketers', 'Instagram, TikTok, YouTube'],
    ['Local businesses', 'Facebook, Instagram, WhatsApp'],
    ['Students and job seekers', 'LinkedIn, plus a portfolio or GitHub if relevant']])}
                {callout('Only link profiles you keep up to date and professional. An empty or personal profile does more harm than no icon at all.')}
                {h2('size', 'The right size and style for social icons')}
                <ul>
                    <li><strong>Size:</strong> 16–24px is standard; 20px is a safe default. Upload at 2× (40px) for sharp results on Retina screens.</li>
                    <li><strong>Spacing:</strong> leave 6–10px between icons so they are easy to tap on a phone.</li>
                    <li><strong>Color:</strong> use official brand colors, or make every icon one color that matches your signature.</li>
                    <li><strong>Format:</strong> PNG, hosted online. SVG and icon fonts do not show in Gmail or Outlook.</li>
                    <li><strong>Alt text:</strong> add “LinkedIn”, “Instagram” and so on, so people with images turned off still know where the link goes.</li>
                </ul>
                <p>More sizing tips are in our <a href="email-signature-size.html">email signature size guide</a>.</p>
                <p>Not sure which icons earn their place? With <a href="../features/email-signature-analytics.html">signature analytics</a> you can see which links in your signature people actually click, then drop the ones nobody uses.</p>
                {h2('signtry', 'How to add social media icons in SignTry')}
                {steps(['Open the <a href="../features/email-signature-generator.html">email signature generator</a> and pick a template.', 'In the <strong>Links</strong> step, paste the URL of each profile you want to show.', 'Fine-tune colors and sizes in the <strong>Style</strong> step.', 'Save and click <strong>Copy</strong>. The icons are hosted and linked for you, and clicks show up in your <a href="../features/email-signature-analytics.html">signature analytics</a>.'])}
                {h2('manual', 'How to add social icons manually in Gmail or Outlook')}
                {steps(['Download each icon as a PNG, about 40×40px, and upload it somewhere public, such as your website.', 'Open your signature settings (<a href="../posts/how-to-create-an-email-signature-in-gmail.html">Gmail</a> or <a href="how-to-create-an-email-signature-in-outlook.html">Outlook</a>).', 'Click the image button in the signature editor and insert the icon by its URL.', 'Select the icon, click the link button, and paste your profile URL.', 'Repeat for each icon, then save.'])}
                <p>It works, but it is slow and the icons often end up different sizes. A generator does it in one step.</p>
                {h2('rules', 'Brand rules for social media logos')}
                <p>Networks are strict about how their logos are used. Use the official icon unchanged: do not stretch it, rotate it, add effects or redraw it. You can usually show it in the network's color, or in a single solid color such as black, white or your brand color. The icons on this page are the official brand marks.</p>
                <h2>Add your icons in two minutes</h2>
                {SIGNTRY_BOX}'''
SOCIAL['faqs'] = [
    ('What size should social media icons be in an email signature?', '16–24 pixels, with 20 pixels a safe default. Upload them at twice the size so they look sharp on high-resolution screens.'),
    ('How many social media icons should I put in my email signature?', 'Two to four. Choose the profiles that matter for your work and keep them up to date.'),
    ('Why are my social media icons not showing?', 'Usually because they are SVG files or embedded images. Use hosted PNG images, which display in Gmail, Outlook and Apple Mail.'),
    ('Where can I get free social media icons for my email signature?', 'Use each network’s official brand assets, or a generator like SignTry that adds correctly sized, hosted icons for you.'),
    ('Should social icons be in color or black and white?', 'Either works. Official colors are recognizable; a single color matching your brand looks more refined. Do not change the shape of the logos.'),
]
SOCIAL['related'] = [('Guide', 'Email signature size and dimensions', 'guides/email-signature-size.html'),
                     ('Feature', 'Signature analytics: see which links get clicked', 'features/email-signature-analytics.html'),
                     ('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html')]


# ---------------------------------------------------------------- Outlook email templates
TEMPLATE = dict(
    path='guides/how-to-create-an-email-template-in-outlook.html', crumb='Outlook email template', mins=8,
    title='How to Create an Email Template in Outlook (2026 Guide)',
    desc='How to create an email template in Outlook: new and classic Outlook, Outlook on the web and Mac. Save, use, edit and share templates step by step.',
    h1='How to create an email template in Outlook',
    lead='Here is how to create an email template in Outlook so you write an email once and reuse it forever, whichever version you use: new Outlook for Windows, classic Outlook, Outlook on the web or Outlook for Mac. You will also learn how to edit, move and share your templates.',
)
_MS = 'https://support.microsoft.com/en-us/outlook/create-email-templates-in-outlook'
_TPL_DIR = r'C:\<wbr>Users\<wbr>&lt;your username&gt;\<wbr>AppData\<wbr>Roaming\<wbr>Microsoft\<wbr>Templates'  # <wbr> lets it wrap on phones
TEMPLATE['article'] = f'''                {answer('<strong>Quick answer:</strong> In new Outlook and Outlook on the web, open a new message, then select <strong>Mail template → Save email as template</strong> on the Message ribbon. In classic Outlook for Windows, select <strong>File → Save As</strong> and choose <strong>Outlook Template (*.oft)</strong>. On a Mac, use <strong>File → Save As Template</strong>.')}
                {toc([('which', 'Which Outlook do you have?'), ('types', 'Mail templates vs My Templates'), ('new', 'New Outlook and Outlook on the web'), ('classic', 'Classic Outlook for Windows'), ('mac', 'Outlook for Mac'), ('edit', 'How to edit a template'), ('move', 'Move templates to new Outlook'), ('share', 'Share templates with your team'), ('signature', 'Keep your signature out of the template'), ('mistakes', 'Common mistakes')])}
                <p>Outlook now has two different template features, four versions of the app, and menus that moved in the last year. Plenty of guides still describe buttons that no longer exist, so start by checking which Outlook is in front of you.</p>
                {h2('which', 'Which Outlook do you have?')}
                {table(['If you see…', 'You are using', 'Jump to'], [
    ['No <strong>File</strong> tab, and a ribbon that looks like the web version', 'New Outlook for Windows', '<a href="#new">Steps</a>'],
    ['Outlook in a browser at outlook.office.com or outlook.live.com', 'Outlook on the web', '<a href="#new">Steps</a>'],
    ['A <strong>File</strong> tab at the far left of the ribbon', 'Classic Outlook for Windows', '<a href="#classic">Steps</a>'],
    ['An <strong>Outlook</strong> menu in the Mac menu bar', 'Outlook for Mac', '<a href="#mac">Steps</a>']])}
                {h2('types', 'Mail templates vs My Templates: pick the right one')}
                <p>New Outlook and Outlook on the web give you two options. <a href="{_MS}" rel="noopener">Microsoft separates them clearly</a>; most guides don't.</p>
                {table(['', 'Mail templates', 'My Templates add-in'], [
    ['What it saves', 'The whole email: recipients, subject, body and attachments', 'Short text snippets only'],
    ['Formatting', 'Rich formatting, images and tables', 'Plain text with basic styling'],
    ['Best for', 'Complete emails you send the same way every time', 'Reusable phrases you drop into replies']])}
                <p>The rule of thumb: if you normally copy an old email and change two words, you want a <strong>Mail template</strong>. If you keep typing the same paragraph about your refund policy, you want <strong>My Templates</strong>. Both need a qualifying Microsoft 365 subscription, so on a free Outlook.com account some of these options may not appear.</p>
                {h2('new', 'How to create an email template in new Outlook and Outlook on the web')}
                <h3>Save a full email as a Mail template</h3>
                {steps(['On the <strong>Home</strong> ribbon, select <strong>New → Mail</strong>.', 'Write the email exactly as you want to reuse it. Add the subject, any attachments, and recipients only if they never change.', 'On the <strong>Message</strong> ribbon, select <strong>Mail template → Save email as template</strong>.', 'Type a name for the template and select <strong>Save</strong>.'])}
                {fig('../', 'images/guides/outlook-save-email-as-template.svg', 'Illustration of saving an email as a template in new Outlook: Message tab, Mail template, Save email as template, then name and save', 'Illustration of the menu path in new Outlook and Outlook on the web.')}
                <p>To see everything you have saved, open <strong>Settings → Mail → Templates</strong>. Templates are listed by account, and a template you save in new Outlook also shows up in Outlook on the web for the same mailbox.</p>
                {callout('Watch the recipients. Mail templates save whatever is in To, Cc and Bcc. Save a template while a colleague is still in Cc and every email you send from it copies them too. Clear the recipient fields before saving unless they truly never change.')}
                <h3>Save a text snippet with My Templates</h3>
                {steps(['Select <strong>New → Mail</strong>.', 'On the <strong>Message</strong> tab, select <strong>My Templates</strong>. A side panel opens.', 'Select <strong>+Template</strong>.', 'Enter a title, then type the snippet text in the field below it.', 'Select <strong>Save</strong>. To insert it later, open the same panel while writing and click the snippet.'])}
                <p>Don't see <strong>My Templates</strong> at all? Your organization has probably switched add-ins off. That is an admin setting, so ask IT. Mail templates still work without it.</p>
                <h3>Use a template you have saved</h3>
                {steps(['On the <strong>Home</strong> ribbon, select <strong>New → Mail from template</strong>.', 'Pick the template from the list. It opens as a normal draft.', 'Change the recipients, subject or body as needed, then select <strong>Send</strong>.'])}
                {h2('classic', 'How to create an email template in classic Outlook for Windows')}
                <p>Classic Outlook saves templates as <code>.oft</code> files on your computer rather than in your mailbox.</p>
                {steps(['On the <strong>Home</strong> tab, select <strong>New Email</strong> (shortcut: <strong>Ctrl + Shift + M</strong>).', 'Write the message you want to reuse.', 'In the message window, select <strong>File → Save As</strong>.', 'In the <strong>Save as type</strong> list, choose <strong>Outlook Template (*.oft)</strong>.', 'Name the file and select <strong>Save</strong>.'])}
                {fig('../', 'images/guides/outlook-classic-save-as-oft.svg', 'Illustration of the classic Outlook Save As dialog with Outlook Template (*.oft) selected as the file type', 'Illustration of the Save As dialog in classic Outlook.')}
                <p>Outlook saves it to <code>{_TPL_DIR}</code> by default. Remember that path: you will need it if you move to new Outlook or a new computer.</p>
                <h3>Open a template in classic Outlook</h3>
                {steps(['Select <strong>New Items → More Items → Choose Form</strong>.', 'In the <strong>Look In</strong> list, select <strong>User Templates in File System</strong>.', 'Pick your template and select <strong>Open</strong>.'])}
                <p>Four clicks deep, every single time. If you send the same email several times a day, pin the Templates folder in File Explorer and double-click the <code>.oft</code> file instead. It opens the same draft.</p>
                {h2('mac', 'How to create an email template in Outlook for Mac')}
                {steps(['Open the email you want to reuse, or write a new one.', 'Select <strong>File → Save As Template</strong>.', 'Give it a name, such as “Monthly status update”, and add a tag if you like.', 'Choose where to save it and select <strong>Save</strong>.'])}
                <p>To use it, select <strong>File → New → Mail From Template</strong> and pick the file. Mac templates end in <code>.emltpl</code>, not <code>.oft</code>, so the two are not interchangeable. Microsoft says the built-in Mac controls need a Microsoft 365 subscription and Outlook for Mac 15.35 or later, and the My Templates add-in on Mac only works with Exchange accounts.</p>
                {h2('edit', 'How to edit an Outlook email template')}
                <p>This trips up nearly everyone: <strong>changing a draft you opened from a template does not change the template.</strong> If you select Save, Outlook creates a draft of that message and leaves the template untouched.</p>
                <ul>
                    <li><strong>New Outlook and the web:</strong> open the template, make your changes, and save it again with <strong>Mail template → Save email as template</strong> under the same name. Then delete the old version in <strong>Settings → Mail → Templates</strong>.</li>
                    <li><strong>Classic Outlook:</strong> open the <code>.oft</code>, edit it, then <strong>File → Save As → Outlook Template</strong> with the same file name to overwrite it.</li>
                    <li><strong>My Templates:</strong> open the panel and select <strong>Edit</strong> on the snippet.</li>
                </ul>
                {h2('move', 'How to move classic templates to new Outlook')}
                <p>Switching from classic to new Outlook does not bring your <code>.oft</code> files along. Import them yourself:</p>
                {steps(['In new Outlook, open <strong>Settings → Mail → Templates</strong>.', 'Select <strong>Add → Add OFT</strong>.', f'Select <strong>Choose</strong> and browse to <code>{_TPL_DIR}</code>.', 'Select the files (you can pick several at once) and select <strong>Add</strong>.'])}
                {fig('../', 'images/guides/outlook-settings-templates.svg', 'Illustration of new Outlook settings: Mail, Templates, the Add OFT option and a Save as OFT button next to each template', 'Illustration of Settings → Mail → Templates in new Outlook.')}
                <p>It works in reverse too: <strong>Save as OFT</strong> next to any saved template downloads a copy to your computer.</p>
                {h2('share', 'How to share Outlook email templates with your team')}
                <p>Outlook has no shared template library for regular mailboxes. You have two practical options:</p>
                <ul>
                    <li><strong>Forward as OFT.</strong> In new Outlook, open the draft and select <strong>Forward as OFT</strong> on the Message tab. Outlook attaches the template to a new email, and your colleague imports it with <strong>Add → Add OFT</strong>.</li>
                    <li><strong>Use a shared mailbox.</strong> My Templates snippets created in a shared mailbox can be visible to everyone with access, but only if the mailbox is added as a full account in new Outlook, or opened in a separate tab with <strong>Open another mailbox</strong> in Outlook on the web. Open it any other way and the templates stay private to you.</li>
                </ul>
                <p>Either way, shared files drift: six people, six slightly different versions of the “pricing follow-up” within a month. If the wording matters, keep one master copy and re-share it whenever it changes. The same goes for signatures, which is why teams use <a href="../features/email-signature-management.html">team email signatures from one CSV</a> instead of asking everyone to copy a file.</p>
                {h2('signature', 'Keep your email signature out of the template')}
                <p>A template is the body of the email. Your signature should stay separate.</p>
                {fig('../', 'images/guides/outlook-template-vs-signature.svg', 'Illustration of an email made from a template: the reusable body comes from the template and the signature is added by Outlook', 'The template holds the body; Outlook adds the signature.')}
                <p>Paste your signature into a template and two things happen. If Outlook adds your signature automatically, you can end up with your sign-off twice. And every template freezes your signature as it was on the day you saved it: change your job title, phone number or logo, and you are editing every template one by one.</p>
                <p>Set up your signature once in Outlook and let Outlook attach it. Our guide on <a href="how-to-create-an-email-signature-in-outlook.html">how to make an email signature in Outlook</a> covers every version, including adding a logo that does not turn into an attachment. If you would rather skip the signature editor, the <a href="../free-email-signature-generator.html">free email signature generator</a> builds an HTML signature you can paste straight in.</p>
                {h2('mistakes', 'Common mistakes to avoid')}
                <ul>
                    <li><strong>Leaving placeholders in.</strong> Write them in capitals and brackets, like <code>[FIRST NAME]</code> or <code>[DATE]</code>. They are ugly on purpose, so you can't miss them before you hit Send.</li>
                    <li><strong>Using My Templates for a formatted email.</strong> It stores plain text with basic styling. Tables and images belong in a Mail template.</li>
                    <li><strong>Saving outdated attachments.</strong> A Mail template keeps the file from the day you saved it. Update the template when the price list changes, or attach the file fresh each time.</li>
                    <li><strong>Vague names.</strong> “Template 3” means nothing in six weeks. Name templates by situation: “Quote follow-up, day 7” or “New client welcome”.</li>
                </ul>'''
TEMPLATE['faqs'] = [
    ('Where are Outlook templates stored?', 'In classic Outlook for Windows, .oft files are saved in C:\\Users\\your username\\AppData\\Roaming\\Microsoft\\Templates. In new Outlook and Outlook on the web, Mail templates live in your mailbox under Settings, Mail, Templates, and My Templates snippets are saved to your primary mailbox.'),
    ('Why can’t I find “Save as Outlook Template” in new Outlook?', 'New Outlook does not use File, Save As for templates. Use Mail template, Save email as template on the Message ribbon. If you need an .oft file, save the template first, then select Save as OFT in Settings, Mail, Templates.'),
    ('Why is My Templates missing in Outlook?', 'Usually your organization has disabled Outlook add-ins. Ask your IT admin to enable it. Mail templates do not depend on the add-in, so you can use those in the meantime.'),
    ('Can a template include a subject line?', 'Yes. A Mail template in new Outlook or on the web, or an .oft file in classic Outlook, saves the subject. A My Templates snippet does not, because it only stores body text.'),
    ('Can I use Outlook templates on my phone?', 'Microsoft’s template instructions cover Outlook for Windows, Mac and the web. Create and manage your templates on desktop or in a browser.'),
]
TEMPLATE['related'] = []


# ---------------------------------------------------------------- Change / edit Outlook signature
CHANGE = dict(
    path='guides/how-to-change-email-signature-in-outlook.html', crumb='Change Outlook signature', mins=7,
    title='How to Change Your Email Signature in Outlook (2026)',
    desc='How to change or edit your email signature in Outlook: new and classic Outlook, web, Mac and mobile, plus fixes when the old signature keeps showing up.',
    h1='How to change your email signature in Outlook',
    lead='Changing your email signature in Outlook takes under a minute once you know where the setting lives, and it lives somewhere different in every version. Here is how to change or edit your signature in new Outlook, classic Outlook, Outlook on the web, Outlook for Mac and the mobile app, and what to do when the old one refuses to go away.',
)
_MS_SIG = 'https://support.microsoft.com/en-us/office/create-an-email-signature-31fb24f9-e698-4789-b92a-f0e777f774ca'
CHANGE['article'] = f'''                {answer('<strong>Quick answer:</strong> In new Outlook and Outlook on the web, select <strong>Settings → Accounts → Signatures</strong>, click the edit button next to your signature, make your changes and select <strong>Save</strong>. In classic Outlook for Windows, go to <strong>File → Options → Mail → Signatures</strong>, pick the signature, edit it in the <strong>Edit signature</strong> box and select <strong>OK</strong>.')}
                {toc([('where', 'Where the signature setting lives'), ('new', 'New Outlook and Outlook on the web'), ('classic', 'Classic Outlook for Windows'), ('mac', 'Outlook for Mac'), ('mobile', 'iPhone and Android'), ('default', 'Change which signature is used'), ('one', 'Change it for one email only'), ('old', 'Old signature still showing?')])}
                {h2('where', 'Where the signature setting lives in each Outlook')}
                <p>Most “I can't find it” moments come from following steps written for a different Outlook. Check this table first:</p>
                {table(['You use', 'Go to', 'Steps'], [
    ['New Outlook for Windows (gear icon top right, no File tab)', '<strong>Settings → Accounts → Signatures</strong>', '<a href="#new">Steps</a>'],
    ['Outlook on the web or Outlook.com', '<strong>Settings → Accounts → Signatures</strong>', '<a href="#new">Steps</a>'],
    ['Classic Outlook for Windows (File tab in the ribbon)', '<strong>File → Options → Mail → Signatures</strong>', '<a href="#classic">Steps</a>'],
    ['Outlook for Mac', '<strong>Outlook → Settings → Signatures</strong>', '<a href="#mac">Steps</a>'],
    ['Outlook app on iPhone or Android', 'Profile picture → Settings gear → <strong>Signature</strong>', '<a href="#mobile">Steps</a>']])}
                {h2('new', 'How to change your signature in new Outlook and Outlook on the web')}
                <p>New Outlook for Windows, Outlook on the web and Outlook.com share the same settings page, so these steps work in all three.</p>
                {steps(['Select the <strong>Settings</strong> gear at the top right.', 'Go to <strong>Accounts → Signatures</strong>.', 'If you have more than one email account, pick the right one at the top of the page.', 'Select the <strong>edit</strong> (pencil) button next to the signature you want to change.', 'Change the text, links or image in the editor, then select <strong>Save</strong>.'])}
                <p>To replace a signature completely, it is often faster to paste a new one over the old text than to edit line by line. A signature built in the <a href="../free-email-signature-generator.html">free email signature generator</a> pastes in with its layout, photo and links intact.</p>
                {callout('Using both Outlook on the web and the Outlook desktop app with a personal Microsoft account? Microsoft notes you may need to set up the signature in both, so check each one after you change it.')}
                {h2('classic', 'How to change your signature in classic Outlook for Windows')}
                {steps(['Select <strong>File → Options → Mail</strong>.', 'Select <strong>Signatures…</strong>.', 'Under <strong>Select signature to edit</strong>, click the signature you want to change.', 'Make your changes in the <strong>Edit signature</strong> box. Use the image button to swap a logo or photo.', 'Select <strong>Save</strong>, then <strong>OK</strong>.'])}
                <p>Shortcut: while writing an email, select <strong>Message → Signature → Signatures…</strong> to open the same window without leaving the draft.</p>
                <p>Classic Outlook can store signatures on the computer itself. If you use Outlook on two PCs, a change on one may not appear on the other, so open the Signatures window on each machine and check.</p>
                {h2('mac', 'How to change your signature in Outlook for Mac')}
                {steps(['Open Outlook and choose <strong>Outlook → Settings</strong> in the menu bar.', 'Select <strong>Signatures</strong>.', 'Pick the signature in the list and edit it on the right.', 'Close the window. Outlook for Mac saves the change automatically.'])}
                <p>Under <strong>Default signatures</strong> in the same window you choose which signature each account uses for new messages and for replies.</p>
                {h2('mobile', 'How to change your signature in the Outlook app on iPhone and Android')}
                {steps(['Open the Outlook app and tap your profile picture at the top left.', 'Tap the <strong>Settings</strong> gear.', 'Tap <strong>Signature</strong> (in some versions it sits under <strong>Mail</strong>).', 'Edit the text. Turn on <strong>Per account signature</strong> if each address needs its own.'])}
                <p>The app keeps its own signature, separate from desktop and web, and it is built for plain text and links. If your phone still says “Get Outlook for iOS”, this is where you replace it. Using Apple Mail instead? See <a href="how-to-change-email-signature-on-iphone.html">how to change your email signature on iPhone</a>.</p>
                {h2('default', 'How to change which signature Outlook uses')}
                <p>Sometimes the signature is fine and Outlook simply picks the wrong one. New messages and replies are separate settings:</p>
                <ul>
                    <li><strong>New Outlook and the web:</strong> on <strong>Settings → Accounts → Signatures</strong>, set <strong>For new messages</strong> and <strong>For replies and forwards</strong>, then select <strong>Save</strong>.</li>
                    <li><strong>Classic Outlook:</strong> in the Signatures window, under <strong>Choose default signature</strong>, pick the account and set <strong>New messages</strong> and <strong>Replies/forwards</strong>.</li>
                </ul>
                <p>A common setup is a full signature for new emails and a two-line version for replies, so a long thread doesn't repeat your logo twenty times.</p>
                {h2('one', 'How to change your signature for one email only')}
                <p>No need to touch the settings for a one-off. Open the draft, select <strong>Signature</strong> on the <strong>Message</strong> (or <strong>Insert</strong>) tab and pick a different saved signature. Outlook swaps it in that email only. If you send the same email often, save it as a template too: here is <a href="how-to-create-an-email-template-in-outlook.html">how to create an email template in Outlook</a>.</p>
                {h2('old', 'Changed your signature but the old one still shows up?')}
                <p>You saved the change, sent a test, and there it is: last year's job title. These are the usual causes, roughly in order of how often they bite:</p>
                <ul>
                    <li><strong>You edited a different account.</strong> Each account has its own signatures and defaults. Check the account at the top of the Signatures page matches the one in your <strong>From</strong> field.</li>
                    <li><strong>The draft was already open.</strong> Outlook adds the signature when the message is created. Close the draft and start a new one.</li>
                    <li><strong>Another device or app still has the old one.</strong> The mobile app, Outlook for Mac and classic Outlook on a second PC can each keep their own copy. Microsoft's roaming signatures store signatures in the mailbox for Microsoft 365 and Outlook.com accounts in recent Outlook for Windows builds; POP, IMAP and on-premises Exchange accounts do not roam.</li>
                    <li><strong>Your company adds the signature.</strong> If IT adds signatures on the mail server, recipients see that one no matter what you set in Outlook, and you won't see it in Sent Items. Ask IT to update it.</li>
                    <li><strong>You are looking at an old thread.</strong> Earlier replies keep the signature they were sent with. Only new messages get the new one.</li>
                </ul>
                <p>If images break after the change, check their size and format in our <a href="email-signature-size.html">email signature size guide</a>.</p>
                <h2>Change it once, for everyone</h2>
                <p>Editing one signature is quick. Editing fifteen, one laptop at a time, is how teams end up with three versions of the company phone number. With <a href="../features/email-signature-management.html">team signatures from a CSV</a>, you update the design once and everyone gets a matching signature to paste into Outlook. New to Outlook signatures altogether? Start with <a href="how-to-create-an-email-signature-in-outlook.html">how to make an email signature in Outlook</a>.</p>'''
CHANGE['faqs'] = [
    ('How do I edit my signature in Outlook?', 'In new Outlook or Outlook on the web, select Settings, Accounts, Signatures, click the edit button next to the signature and select Save when you are done. In classic Outlook, go to File, Options, Mail, Signatures, select the signature and edit it in the Edit signature box.'),
    ('Why won’t my new signature show up in Outlook?', 'Usually the change was made on a different account, the draft was opened before the change, or another device still uses its own copy. If your company adds signatures on the mail server, only IT can change what recipients see.'),
    ('How do I change my signature in Outlook 365?', 'Outlook in Microsoft 365 uses the new Outlook settings: Settings, Accounts, Signatures. Edit the signature, set it as the default for new messages and replies, and select Save.'),
    ('Can I use a different signature for replies?', 'Yes. Set one signature for new messages and another, usually shorter, for replies and forwards. Both settings are on the same Signatures page.'),
    ('How do I change my Outlook signature on my phone?', 'In the Outlook app, tap your profile picture, the Settings gear and then Signature. The app signature is separate from the desktop and web signature, so change it there too.'),
]
CHANGE['related'] = []


def build():
    return [article_page(a) for a in (OUTLOOK, TEMPLATE, CHANGE, IPHONE, YAHOO, SIZE, SOCIAL)]
