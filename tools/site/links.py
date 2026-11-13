"""Internal linking map: one place that decides the "Related" block of every generated page.

Pages are grouped into topic clusters (install guides, design, writing and fun, examples, features).
Each page links to 6 pages: mostly its own cluster, plus one or two bridges to a neighbouring
cluster, so every page gets contextual links in and out. Paths keep .html; page() cleans URLs.
"""

PAGES = {
    # install guides
    'guides/how-to-create-an-email-signature-in-outlook.html': ('Guide', 'How to make an email signature in Outlook'),
    'guides/how-to-create-an-email-template-in-outlook.html': ('Guide', 'How to create an email template in Outlook'),
    'posts/how-to-create-an-email-signature-in-gmail.html': ('Guide', 'How to create an email signature in Gmail'),
    'guides/how-to-change-email-signature-on-iphone.html': ('Guide', 'How to change your email signature on iPhone'),
    'guides/how-to-change-signature-in-yahoo-mail.html': ('Guide', 'How to change your signature in Yahoo Mail'),
    # design
    'guides/email-signature-size.html': ('Guide', 'Email signature size: the right dimensions'),
    'guides/social-media-icons-for-email-signature.html': ('Guide', 'Social media icons for your email signature'),
    'guides/email-signature-fonts.html': ('Guide', 'The best fonts for email signatures'),
    # writing and fun
    'guides/funny-email-sign-offs.html': ('Guide', 'Funny email sign-offs: 70+ ideas'),
    'examples/funny-email-signatures.html': ('Examples', 'Funny email signatures and quotes'),
    'examples/holiday-email-signature.html': ('Examples', 'Christmas and holiday email signatures'),
    # examples
    'examples/email-signature-examples.html': ('Examples', 'Email signature examples: 14 to copy'),
    'examples/college-student-email-signature.html': ('Examples', 'College student email signature examples'),
    'examples/teacher-email-signature.html': ('Examples', 'Teacher email signature examples'),
    'examples/real-estate-email-signature.html': ('Examples', 'Real estate email signature examples'),
    # features and tools
    'features/email-signature-templates.html': ('Feature', 'Email signature templates for every industry'),
    'features/email-signature-generator.html': ('Feature', 'Email signature generator with logo and photo'),
    'features/email-signature-management.html': ('Feature', 'Team signatures from a CSV'),
    'features/email-signature-analytics.html': ('Feature', 'Signature analytics: see which links get clicked'),
    'features/html-email-signature.html': ('Feature', 'HTML email signatures for every inbox'),
    'free-email-signature-generator.html': ('Tool', 'Free email signature generator'),
    'pricing.html': ('Pricing', 'Pay per signature, not per seat'),
}

_OUTLOOK = 'guides/how-to-create-an-email-signature-in-outlook.html'
_TEMPLATE = 'guides/how-to-create-an-email-template-in-outlook.html'
_GMAIL = 'posts/how-to-create-an-email-signature-in-gmail.html'
_IPHONE = 'guides/how-to-change-email-signature-on-iphone.html'
_YAHOO = 'guides/how-to-change-signature-in-yahoo-mail.html'
_SIZE = 'guides/email-signature-size.html'
_ICONS = 'guides/social-media-icons-for-email-signature.html'
_FONTS = 'guides/email-signature-fonts.html'
_SIGNOFFS = 'guides/funny-email-sign-offs.html'
_FUNNY = 'examples/funny-email-signatures.html'
_HOLIDAY = 'examples/holiday-email-signature.html'
_EXAMPLES = 'examples/email-signature-examples.html'
_STUDENT = 'examples/college-student-email-signature.html'
_TEACHER = 'examples/teacher-email-signature.html'
_REALTY = 'examples/real-estate-email-signature.html'
_F_TPL = 'features/email-signature-templates.html'
_F_GEN = 'features/email-signature-generator.html'
_F_TEAM = 'features/email-signature-management.html'
_F_STATS = 'features/email-signature-analytics.html'
_F_HTML = 'features/html-email-signature.html'
_FREE = 'free-email-signature-generator.html'
_PRICING = 'pricing.html'

RELATED = {
    _OUTLOOK: [_TEMPLATE, _GMAIL, _IPHONE, _YAHOO, _SIZE, _F_HTML],
    _TEMPLATE: [_OUTLOOK, _GMAIL, _IPHONE, _F_TEAM, _F_TPL, _EXAMPLES],
    _GMAIL: [_OUTLOOK, _TEMPLATE, _IPHONE, _YAHOO, _SIZE, _F_HTML],
    _IPHONE: [_OUTLOOK, _GMAIL, _YAHOO, _F_HTML, _SIZE, _FONTS],
    _YAHOO: [_OUTLOOK, _GMAIL, _IPHONE, _EXAMPLES, _SIZE, _F_HTML],
    _SIZE: [_ICONS, _FONTS, _F_GEN, _EXAMPLES, _OUTLOOK, _F_TPL],
    _ICONS: [_SIZE, _FONTS, _F_STATS, _EXAMPLES, _REALTY, _F_GEN],
    _FONTS: [_SIZE, _ICONS, _F_GEN, _EXAMPLES, _SIGNOFFS, _F_TPL],
    _SIGNOFFS: [_FUNNY, _HOLIDAY, _EXAMPLES, _FONTS, _FREE, _GMAIL],
    _FUNNY: [_SIGNOFFS, _HOLIDAY, _EXAMPLES, _STUDENT, _FREE, _F_TPL],
    _HOLIDAY: [_FUNNY, _SIGNOFFS, _SIZE, _F_TEAM, _EXAMPLES, _FONTS],
    _EXAMPLES: [_F_TPL, _REALTY, _STUDENT, _TEACHER, _SIZE, _FONTS],
    _STUDENT: [_TEACHER, _EXAMPLES, _OUTLOOK, _GMAIL, _FONTS, _FREE],
    _TEACHER: [_STUDENT, _F_TEAM, _EXAMPLES, _GMAIL, _OUTLOOK, _FONTS],
    _REALTY: [_F_TEAM, _F_TPL, _ICONS, _EXAMPLES, _F_STATS, _SIZE],
    _F_TPL: [_EXAMPLES, _F_GEN, _SIZE, _REALTY, _FONTS, _F_HTML],
    _F_GEN: [_F_TPL, _OUTLOOK, _ICONS, _SIZE, _FONTS, _FREE],
    _F_TEAM: [_PRICING, _EXAMPLES, _REALTY, _F_STATS, _TEACHER, _TEMPLATE],
    _F_STATS: [_F_GEN, _EXAMPLES, _PRICING, _ICONS, _F_TEAM, _REALTY],
    _F_HTML: [_OUTLOOK, _IPHONE, _YAHOO, _GMAIL, _SIZE, _F_GEN],
}


def related(path, fallback=()):
    """Related items (kind, title, path) for a page, or the page's own list if it isn't mapped."""
    if path not in RELATED:
        return list(fallback)
    return [(*PAGES[u], u) for u in RELATED[path]]
