from layout import *
from p_guides import article_page, answer, h2, SIGNTRY_BOX
from p_examples import sig, plain, grid


def lines(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


GEN_LINK = '<a href="../free-email-signature-generator.html">free email signature generator</a>'

# ---------------------------------------------------------------- Funny sign-offs
SIGNOFFS = dict(
    path='guides/funny-email-sign-offs.html', crumb='Funny email sign-offs', mins=6,
    title='Funny Email Sign-Offs: 70+ Unhinged & Work-Safe Ideas',
    desc='Funny email sign-offs for every mood: unhinged, silly, Gen Z and work-safe ideas to end your emails with a smile, plus when to keep it professional.',
    h1='Funny email sign-offs: 70+ unhinged, silly and work-safe ideas',
    lead='Funny email sign-offs are the quickest way to make an email feel human. Here are more than 70 of them, from work-safe and witty to properly unhinged, plus a simple rule for when a joke works and when “Best regards” is still the right call.',
    image='media/stills/install-signature-35.jpg',
)
SIGNOFFS['article'] = f"""                {answer('<strong>Quick answer:</strong> A funny email sign-off works best with <strong>colleagues you already know</strong>, in <strong>casual threads</strong>, and when it matches the tone of the email. Keep it to one short line, and keep your normal signature with your name and contact details underneath it.')}
                {toc([('work', 'Funny sign-offs that are safe for work'), ('unhinged', 'Unhinged email sign-offs'), ('silly', 'Silly and weird sign-offs'), ('genz', 'Gen Z email sign-offs'), ('situations', 'Sign-offs for specific situations'), ('when', 'When to use a funny sign-off'), ('classic', 'Professional sign-offs for everything else')])}
                {h2('work', 'Funny email sign-offs that are safe for work')}
                <p>These get a smile without making HR nervous. Good for teammates, friendly clients and Friday emails.</p>
                {lines(['Fueled by coffee and good intentions,', 'Sent from my desk, which misses me on weekends,', 'May your inbox be lighter than mine,', 'Running on caffeine and optimism,', 'Yours in spreadsheets,', 'Looking forward to your reply (and lunch),', 'Talk soon, unless this becomes a meeting,', 'With minimal typos,', 'Thanks in advance (and in arrears),', 'Cheers to fewer meetings,', 'Warmly, and slightly over-caffeinated,', 'Have a great weekend. You earned it,'])}
                {h2('unhinged', 'Unhinged email sign-offs')}
                <p>For the group chat energy you bring to work. Use these only with people who already share your sense of humor.</p>
                {lines(['Per my last email, and the one before that,', 'Sent from the void,', 'Holding it together with tape and hope,', 'This email will self-destruct in 5 business days,', 'Thriving (allegedly),', 'Respectfully, I need a nap,', 'Chaotically yours,', 'Living the dream (it is a weird dream),', 'Hope this email finds you before my next one does,', 'Signing off before I make it weird,', 'Sent with 14 browser tabs open,', 'Love and deadlines,'])}
                {callout('“Per my last email” is famously passive-aggressive. It is funny between friends, but it can sting with a client who genuinely missed something.')}
                {h2('silly', 'Silly and weird email sign-offs')}
                {lines(['Stay hydrated,', 'Live long and prosper,', 'May the force be with your inbox,', 'Keep calm and reply all (please don’t),', 'Yours until the Wi-Fi drops,', 'Sent by a human, probably,', 'Toodle-oo,', 'Over and out,', 'Catch you on the flip side,', 'Peace, love and pivot tables,', 'Bye for now, crocodile,', 'Warm regards and lukewarm coffee,'])}
                {h2('genz', 'Gen Z email sign-offs')}
                <p>Short, lowercase and a bit ironic. Perfect for internal threads with a younger team; skip them for formal emails.</p>
                {lines(['ok bye,', 'slay,', 'no thoughts, just vibes,', 'it is what it is,', 'lmk!,', 'ttyl,', 'live laugh leave me on read,', 'sending good energy,', 'this is a sign (off),', 'xoxo, gossip girl,'])}
                {h2('situations', 'Funny sign-offs for specific situations')}
                {table(['Situation', 'Sign-off'], [
    ['Monday morning', '“Sent with the enthusiasm of a Monday,”'],
    ['Friday afternoon', '“Mentally already on the weekend,”'],
    ['Chasing a reply', '“Gently bumping this to the top of your inbox,”'],
    ['After a long thread', '“Thank you for coming to my TED talk,”'],
    ['Deadline day', '“Typing at the speed of panic,”'],
    ['Before a holiday', '“Out of office in spirit since Tuesday,”'],
    ['Saying thanks', '“You are a legend. That is all,”']])}
                {h2('when', 'When to use a funny email sign-off')}
                <ul>
                    <li><strong>Yes:</strong> colleagues you know well, casual internal threads, creative industries, newsletters with a playful brand voice.</li>
                    <li><strong>Maybe:</strong> long-term clients who joke with you first.</li>
                    <li><strong>No:</strong> first contact, job applications, complaints, legal or financial topics, bad news, and anyone senior you have not met.</li>
                </ul>
                <p>A good test: would you say the same line out loud to this person? If not, keep it professional.</p>
                {h2('classic', 'Professional sign-offs for everything else')}
                <p>When in doubt, these never go wrong: <strong>Best regards</strong>, <strong>Kind regards</strong>, <strong>Best</strong>, <strong>Thanks</strong>, <strong>Thank you</strong>, <strong>Many thanks</strong>, <strong>Warm regards</strong> and <strong>Sincerely</strong> for formal letters. Put your sign-off on its own line, then your name, then your email signature.</p>
                <h2>Make the rest of your signature just as memorable</h2>
                <p>A great sign-off deserves a signature to match. Use our {GEN_LINK} to add your photo, title and links in two minutes, or browse <a href="../examples/funny-email-signatures.html">funny email signature examples</a>.</p>"""
SIGNOFFS['faqs'] = [
    ('Is it professional to use a funny email sign-off?', 'It can be, with people you know well and in casual threads. For first contact, job applications, complaints or formal topics, use a standard sign-off such as “Best regards”.'),
    ('What is an unhinged email sign-off?', 'A deliberately chaotic or over-honest closing line, such as “Thriving (allegedly)” or “Sent from the void”. They are popular on social media and best kept for close colleagues.'),
    ('What is a good funny sign-off for work?', 'Something light and harmless, such as “Fueled by coffee and good intentions” or “May your inbox be lighter than mine”.'),
    ('Should my sign-off go in my email signature?', 'Usually not. Type the sign-off yourself so you can match it to each email, and keep your signature for your name, title and contact details.'),
]
SIGNOFFS['related'] = [('Examples', 'Funny email signatures and quotes', 'examples/funny-email-signatures.html'),
                       ('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html'),
                       ('Tool', 'Free email signature generator', 'free-email-signature-generator.html')]

# ---------------------------------------------------------------- Fonts
FONTS = dict(
    path='guides/email-signature-fonts.html', crumb='Email signature fonts', mins=6,
    title='Best Font for Email Signature: 12 Safe Picks (2026)',
    desc='The best font for an email signature: 12 web-safe fonts that look right in Gmail, Outlook and Apple Mail, ideal sizes, and handwritten signature fonts.',
    h1='The best fonts for email signatures',
    lead='The best font for an email signature is one that every recipient actually sees. Below are 12 web-safe fonts that display correctly in Gmail, Outlook and Apple Mail, the right sizes to use, and how to get a handwritten signature font without it breaking.',
    image='media/stills/personalize-70.jpg',
)
FONT_ROWS = [
    ['Arial', 'Sans-serif', 'Clean, neutral, readable everywhere. The safest choice.'],
    ['Helvetica', 'Sans-serif', 'Classic and modern. Falls back to Arial on Windows.'],
    ['Verdana', 'Sans-serif', 'Wide letters, very readable at small sizes.'],
    ['Tahoma', 'Sans-serif', 'Compact version of Verdana. Good for long titles.'],
    ['Trebuchet MS', 'Sans-serif', 'A little personality without losing readability.'],
    ['Calibri', 'Sans-serif', 'Outlook’s default. Not installed on every Mac.'],
    ['Segoe UI', 'Sans-serif', 'Windows system font. Use with an Arial fallback.'],
    ['Georgia', 'Serif', 'Elegant and readable on screens. Great for law and finance.'],
    ['Times New Roman', 'Serif', 'Traditional and formal. Can look dated.'],
    ['Garamond', 'Serif', 'Refined, bookish look. Available in Gmail.'],
    ['Palatino', 'Serif', 'Warm serif for a classic feel. Mac and Windows have versions.'],
    ['Courier New', 'Monospace', 'Typewriter style. Only for a deliberately techy look.'],
]
FONTS['article'] = f"""                {answer('<strong>Quick answer:</strong> Use a <strong>web-safe font</strong> such as <strong>Arial, Helvetica, Verdana, Georgia or Tahoma</strong>, at <strong>14–16px for your name</strong> and <strong>12–14px for everything else</strong>. Custom fonts, including handwritten signature fonts, usually fall back to a default in Gmail and Outlook, so add those as an image instead.')}
                {toc([('safe', '12 best fonts for email signatures'), ('why', 'Why web-safe fonts matter'), ('size', 'Font size and style'), ('gmail', 'Fonts available in Gmail'), ('handwritten', 'Signature fonts that look handwritten'), ('pairs', 'Font pairings that work')])}
                {h2('safe', '12 best fonts for email signatures')}
                {table(['Font', 'Style', 'Why use it'], [[f'<span style="font-family:{r[0]},sans-serif;font-size:17px">{r[0]}</span>', r[1], r[2]] for r in FONT_ROWS])}
                {h2('why', 'Why web-safe fonts matter in email signatures')}
                <p>Email apps do not download fonts the way websites do. If you use a font the recipient does not have installed, their email app quietly swaps it for a default, often Times New Roman, and your carefully designed signature looks broken. Web-safe fonts are installed on almost every computer and phone, so everyone sees what you see.</p>
                <p>Apple Mail and the iPhone can show some web fonts; Gmail and Outlook on Windows generally cannot. Always set a fallback, for example <code>font-family: Helvetica, Arial, sans-serif</code>.</p>
                {h2('size', 'The best font size and style for an email signature')}
                <ul>
                    <li><strong>Name:</strong> 14–16px, bold.</li>
                    <li><strong>Title, company and contact details:</strong> 12–14px, regular.</li>
                    <li><strong>Disclaimers:</strong> 10–11px, gray.</li>
                    <li><strong>One font, two weights.</strong> Bold for your name, regular for the rest. Two fonts at most.</li>
                    <li><strong>Dark gray or your brand color</strong> for text, not pure black, for a softer look.</li>
                </ul>
                <p>More sizing advice is in our <a href="email-signature-size.html">email signature size guide</a>.</p>
                {h2('gmail', 'Fonts available in Gmail signatures')}
                <p>The Gmail signature editor offers a fixed list: Sans Serif, Serif, Fixed Width, Wide, Narrow, Comic Sans MS, Garamond, Georgia, Tahoma, Trebuchet MS and Verdana. Stick to these and your Gmail signature will look the same for everyone. See our <a href="../posts/how-to-create-an-email-signature-in-gmail.html">Gmail signature guide</a> to set it up.</p>
                {h2('handwritten', 'Signature fonts that look handwritten')}
                <p>Searching for a font that looks like a signature? Script fonts such as Great Vibes, Dancing Script, Allura or Sacramento (all free on Google Fonts) look like real handwriting. The catch: they are not installed on your recipients' devices, so typed in a script font, your signature will show as plain text.</p>
                <p>The fix is to use the handwriting as an <strong>image</strong>. SignTry does this for you: turn on <strong>Add a handwritten signature</strong> in the Branding step and it is generated from your name, readable on light and dark backgrounds, and hosted so it shows up in every inbox.</p>
                {fig('../', 'media/stills/personalize-70.jpg', 'Email signature with a handwritten signature under the name', 'A handwritten signature added as an image, so it looks the same in every inbox.')}
                {h2('pairs', 'Font pairings that work in email signatures')}
                {table(['Name', 'Details', 'Feels'], [
    ['Georgia bold', 'Arial', 'Professional and trustworthy (legal, finance)'],
    ['Helvetica bold', 'Helvetica', 'Modern and clean (tech, startups)'],
    ['Trebuchet MS bold', 'Verdana', 'Friendly and approachable (education, healthcare)'],
    ['Palatino bold', 'Georgia', 'Elegant (real estate, hospitality)']])}
                <h2>Get the fonts right automatically</h2>
                {SIGNTRY_BOX}"""
FONTS['faqs'] = [
    ('What is the best font for an email signature?', 'Arial, Helvetica, Verdana, Georgia and Tahoma are the safest choices because they are installed on almost every device and display the same in Gmail, Outlook and Apple Mail.'),
    ('What font size should an email signature be?', 'Use 14–16px for your name and 12–14px for your title and contact details. Disclaimers can be 10–11px.'),
    ('Can I use a custom or Google font in my email signature?', 'Only Apple Mail reliably shows web fonts. Gmail and Outlook replace them with a default, so always set a web-safe fallback such as Arial.'),
    ('What font looks like a real signature?', 'Script fonts such as Great Vibes, Dancing Script, Allura and Sacramento look handwritten. Add them as an image, or use SignTry’s handwritten signature option, so they display everywhere.'),
    ('Is Calibri a good font for email signatures?', 'Calibri looks good in Outlook on Windows, but it is not installed on every Mac or phone. Add Arial as a fallback.'),
]
FONTS['related'] = [('Guide', 'Email signature size and dimensions', 'guides/email-signature-size.html'),
                    ('Feature', 'Email signature generator with handwritten signature', 'features/email-signature-generator.html'),
                    ('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html')]

# ---------------------------------------------------------------- Funny signatures / quotes
FUNNY = dict(
    path='examples/funny-email-signatures.html', crumb='Funny email signatures', mins=5,
    title='Funny Email Signatures & Quotes: 40+ Examples to Copy',
    desc='Funny email signatures and email signature quotes you can copy: humorous taglines, witty one-liners and quotes for work, plus how to keep them professional.',
    h1='Funny email signatures and email signature quotes',
    lead='A funny email signature or a well-chosen quote gives your emails personality and makes people remember you. Here are more than 40 humorous email signatures, witty taglines and quotes you can copy, plus how to use them without looking unprofessional.',
    image='images/people/freelancer.jpg', cta_h='Build a signature with personality',
)
FUNNY['article'] = f"""                {answer('<strong>Quick answer:</strong> Add humor as <strong>one short tagline</strong> under your contact details, in a smaller, lighter font. Keep your name, title and contact information first, and use a funny email signature only for casual or internal email.')}
                {toc([('examples', 'Funny email signature examples'), ('taglines', 'Humorous taglines to copy'), ('jobs', 'Funny signatures by job'), ('quotes', 'Email signature quotes'), ('rules', 'How to keep it professional')])}
                {h2('examples', 'Funny email signature examples')}
                {grid(
    sig('Marketer', 'Priya Patel', 'Head of Growth', 'Loop &amp; Co. Agency', ['priya@loopco.agency'], '#f59e0b', photo='marketing.jpg', links=['Our work', 'LinkedIn'], tagline='Professional overthinker of subject lines'),
    sig('Developer', 'Daniel Kim', 'Senior Software Engineer', 'Brightline Software', ['daniel@brightline.io'], '#0b5cff', initials='DK', links=['GitHub'], tagline='It works on my machine'),
    plain('Accountant', '''<b>Michael Chen</b>, CPA
Chen &amp; Walsh Accounting
(555) 016-3311
<i>I count on you. Literally.</i>'''),
    plain('Teacher', '''<b>Ms. Ana Rivera</b>
3rd Grade Teacher, Lincoln Elementary
<i>Powered by coffee and gold stars</i>'''))}
                {h2('taglines', 'Humorous email signature taglines to copy')}
                {lines(['Sent from my phone, so please excuse my thumbs.', 'Replying at the speed of coffee.', 'Professional email writer. Amateur everything else.', 'Inbox zero is a myth, but I believe.', 'Please consider the environment before printing this email. Or anything, really.', 'I promise this could not have been a meeting.', 'Currently fluent in sarcasm and Excel.', 'Out of office in spirit since 2019.', 'Will work for snacks.', 'Ask me about my spreadsheets. Actually, please don’t.', 'This signature is longer than my attention span.', 'Hand-crafted with 100% organic keystrokes.'])}
                {h2('jobs', 'Funny email signatures by job')}
                {table(['Job', 'Tagline'], [
    ['Developer', '“There are 10 kinds of people: those who understand binary and those who don’t.”'],
    ['Designer', '“Yes, I can make the logo bigger.”'],
    ['Marketer', '“Turning coffee into conversions.”'],
    ['Sales', '“Always be closing (this email, at least).”'],
    ['HR', '“Your friendly neighborhood policy reminder.”'],
    ['Project manager', '“Professional herder of cats and calendars.”'],
    ['Teacher', '“I survived another day of “but why?””'],
    ['Accountant', '“Making cents of it all.”'],
    ['Real estate agent', '“I know a place. Actually, several.”']])}
                {h2('quotes', 'Email signature quotes')}
                <p>A short quote can say what you stand for. Choose one that is accurately attributed and relevant to your work:</p>
                {lines(['“The best way to predict the future is to invent it.” — Alan Kay', '“Stay hungry, stay foolish.” — Steve Jobs, quoting the Whole Earth Catalog', '“The only way to do great work is to love what you do.” — Steve Jobs', '“Talk is cheap. Show me the code.” — Linus Torvalds', '“Premature optimization is the root of all evil.” — Donald Knuth', '“Make it work, make it right, make it fast.” — Kent Beck'])}
                {callout('Many quotes online are misattributed, for example most “Einstein” and “Mark Twain” quotes. If you are not sure who said it, use it without a name or pick a different line.')}
                {h2('rules', 'How to keep a funny email signature professional')}
                <ol>
                    <li><strong>Information first.</strong> Name, title and contact details come before the joke.</li>
                    <li><strong>One line only.</strong> A tagline, not a stand-up set.</li>
                    <li><strong>Make it smaller and lighter</strong> than the rest of your signature.</li>
                    <li><strong>Avoid politics, religion and anything about other people.</strong></li>
                    <li><strong>Keep a second, serious signature</strong> for clients and formal email.</li>
                </ol>
                <p>Looking for funny closing lines instead? See <a href="../guides/funny-email-sign-offs.html">70+ funny email sign-offs</a>. To build your signature with a tagline, try our {GEN_LINK}.</p>"""
FUNNY['faqs'] = [
    ('Is a funny email signature unprofessional?', 'Not if it is short, harmless and comes after your contact details. Keep a serious version for clients, job applications and formal emails.'),
    ('Where should a quote go in an email signature?', 'At the bottom, after your name and contact details, in a smaller and lighter font than the rest of the signature.'),
    ('What is a good funny email signature for work?', 'A short, self-deprecating tagline about your job, such as “Replying at the speed of coffee” or “Professional overthinker of subject lines”.'),
    ('Should I put a quote in my email signature?', 'Only if it is short, relevant to your work and correctly attributed. Many popular quotes are misattributed, so double-check the source.'),
]
FUNNY['related'] = [('Guide', 'Funny email sign-offs: 70+ ideas', 'guides/funny-email-sign-offs.html'),
                    ('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html'),
                    ('Tool', 'Free email signature generator', 'free-email-signature-generator.html')]

# ---------------------------------------------------------------- Holiday
HOLIDAY = dict(
    path='examples/holiday-email-signature.html', crumb='Holiday email signature', mins=5,
    title='Christmas & Holiday Email Signature Ideas (2026)',
    desc='Christmas, holiday and Thanksgiving email signature ideas: greetings, banners and examples to copy, plus office-closure notes and when to switch back.',
    h1='Christmas and holiday email signature ideas',
    lead='A Christmas or holiday email signature is a small, festive touch on every email you send in December. Below are holiday and Thanksgiving email signature examples, greetings you can copy, banner ideas, and how to announce office closures without anyone missing it.',
    image='images/people/strip-wide.jpg', cta_h='Add a holiday touch to your signature',
)
HOLIDAY['article'] = f"""                {answer('<strong>Quick answer:</strong> Add <strong>one short seasonal greeting</strong> (for example “Wishing you a happy holiday season”) and, if needed, your <strong>office closure dates</strong> under your normal signature. Use an inclusive greeting for clients, keep any banner under 600×150px, and switch back to your usual signature in early January.')}
                {toc([('greetings', 'Holiday greetings to copy'), ('examples', 'Christmas email signature examples'), ('thanksgiving', 'Thanksgiving email signature'), ('closures', 'Office closure notes'), ('banners', 'Holiday banners and images'), ('timing', 'When to add and remove it')])}
                {h2('greetings', 'Holiday email signature greetings to copy')}
                <h3>Inclusive greetings (best for clients)</h3>
                {lines(['Wishing you a happy holiday season and a wonderful new year.', 'Warm wishes for the holidays and a bright 2027.', 'Season’s greetings from all of us at [Company].', 'Thank you for a great year. Happy holidays!', 'Wishing you peace and joy this holiday season.'])}
                <h3>Merry Christmas greetings</h3>
                {lines(['Merry Christmas and a happy new year!', 'Wishing you a merry Christmas and a joyful new year.', 'Merry Christmas from the [Company] team.', 'Have a cozy Christmas and a great start to the new year.'])}
                <h3>Fun holiday lines</h3>
                {lines(['Currently powered by cookies and hot chocolate.', 'Replying between gingerbread batches.', 'My inbox is on the nice list. Is yours?', 'Out of office, in a holiday sweater.'])}
                {h2('examples', 'Christmas email signature examples')}
                {grid(
    sig('Classic Christmas', 'Jordan Davis', 'Marketing Director', 'Northstar Studio', ['(555) 014-2810'], '#c0262d', photo='freelancer.jpg', links=['Website'], tagline='Merry Christmas and a happy new year! 🎄'),
    sig('Inclusive holiday', 'Sofia Ramirez', 'Founder &amp; CEO', 'Brightline Software', ['sofia@brightline.io'], '#16a34a', initials='SR', links=['brightline.io'], tagline='Wishing you a happy holiday season ❄️'),
    plain('Office closure', '''<b>Robert Hayes</b>
Principal Broker, Hayes &amp; Co. Real Estate
(555) 018-7700
<i>Our office is closed Dec 24 – Jan 1. Happy holidays!</i>'''),
    plain('Minimal', '''<b>Emily Carter</b>
Volunteer Coordinator, Green City Alliance
<i>Season’s greetings and thank you for an amazing year.</i>'''))}
                {h2('thanksgiving', 'Thanksgiving email signature ideas')}
                {lines(['Happy Thanksgiving! Grateful for clients like you.', 'Wishing you a Thanksgiving full of good food and great company.', 'Thankful for your partnership this year.', 'Out for Thanksgiving, back Monday with leftovers.'])}
                {h2('closures', 'How to announce office closures in your signature')}
                <p>Your signature is seen on every email, so it is the perfect place for holiday hours. Keep it to one line with exact dates, and point to a backup contact for urgent requests:</p>
                {plain('Closure line', '''<i>We are closed Dec 24 – Jan 1. For urgent help, email support@company.com.</i>''')}
                <p>Pair it with an out-of-office auto-reply for the days you are actually away.</p>
                {h2('banners', 'Holiday banners and images for email signatures')}
                <ul>
                    <li><strong>Size:</strong> up to 600×150px displayed, uploaded at 2× for sharp screens. See our <a href="../guides/email-signature-size.html">size guide</a>.</li>
                    <li><strong>Animated GIFs</strong> are fun, but classic Outlook for Windows shows only the first frame, so make sure that frame works on its own.</li>
                    <li><strong>Host the image</strong> instead of attaching it, or it may show as an attachment.</li>
                    <li><strong>Emoji</strong> such as 🎄 ❄️ 🎁 are the lightest way to add color, and they work in every modern email app.</li>
                </ul>
                {h2('timing', 'When to add and remove your holiday signature')}
                <p>Switch to your holiday signature in early December (or the week before Thanksgiving) and back to your normal one in the first week of January. In SignTry, keep your holiday version as a second signature and copy whichever one fits the season; for teams, update everyone at once by <a href="../features/email-signature-management.html">generating from a CSV</a>.</p>
                <p>Ready to make yours? Start with our {GEN_LINK}.</p>"""
HOLIDAY['faqs'] = [
    ('What should I put in my Christmas email signature?', 'Your normal signature plus one short greeting, such as “Merry Christmas and a happy new year!”, and your office closure dates if they apply.'),
    ('Should I say Merry Christmas or Happy Holidays in a work email?', 'For clients and mixed audiences, “Happy holidays” or “Season’s greetings” is the safer, inclusive choice. Use “Merry Christmas” with people you know celebrate it.'),
    ('Can I add a GIF to my holiday email signature?', 'Yes, but classic Outlook for Windows shows only the first frame, so choose a GIF whose first frame looks good on its own.'),
    ('When should I remove my holiday email signature?', 'In the first week of January, or the day after the holiday it mentions.'),
    ('What is a good Thanksgiving email signature?', 'A short line of thanks, such as “Happy Thanksgiving! Grateful for clients like you,” under your usual signature.'),
]
HOLIDAY['related'] = [('Guide', 'Email signature size and dimensions', 'guides/email-signature-size.html'),
                      ('Examples', 'Funny email signatures and quotes', 'examples/funny-email-signatures.html'),
                      ('Feature', 'Team signatures from a CSV', 'features/email-signature-management.html')]


def build():
    hub = ('Guides &amp; examples', 'guides.html')
    return [article_page(SIGNOFFS), article_page(FONTS), article_page(FUNNY, 'Examples', hub), article_page(HOLIDAY, 'Examples', hub)]
