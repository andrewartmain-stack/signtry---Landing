from layout import *
from p_guides import article_page, answer, h2, SIGNTRY_BOX


def sig(label, name, title, org=None, lines=(), color='#0b5cff', initials=None, photo=None, links=(), tagline=None):
    av = ''
    if photo:
        av = f'<img class="av" src="../images/people/{photo}" alt="" loading="lazy">'
    elif initials:
        av = f'<span class="ini" style="background:{color}">{initials}</span>'
    org_html = f'<div class="org">{org}</div>' if org else ''
    lines_html = ''.join(f'<div>{l}</div>' for l in lines)
    links_html = f'<div class="ln">{" · ".join(links)}</div>' if links else ''
    tag_html = f'<div class="tagline">{tagline}</div>' if tagline else ''
    return f'''<div class="sigx"><span class="lbl">{label}</span><div class="row2">{av}<div><b>{name}</b><div class="ttl">{title}</div>{org_html}<div class="bar" style="background:{color}"></div>{lines_html}{links_html}{tag_html}</div></div></div>'''


def plain(label, text):
    return f'<div class="sigx"><span class="lbl">{label}</span><div class="plain">{text.strip()}</div></div>'


def grid(*cards):
    return '<div class="sigs">' + ''.join(cards) + '</div>'


# ---------------------------------------------------------------- Student
STUDENT = dict(
    path='examples/college-student-email-signature.html', crumb='College student email signature', mins=6,
    title='College Student Email Signature: 10 Examples & Template',
    desc='College student email signature examples for undergrads, grad students and PhD candidates. What to include, what to leave out, and templates you can copy.',
    h1='College student email signature examples',
    lead='A good college student email signature tells professors, recruiters and internship managers exactly who you are: your name, your major, your university and your graduation year. Below are 10 examples for undergraduates, graduate students and PhD candidates that you can copy.',
    image='images/people/job-seeker.jpg', cta_h='Make your student email signature in 2 minutes',
)
STUDENT['article'] = f"""                {answer('<strong>Quick answer:</strong> A college student email signature should include your <strong>full name</strong>, <strong>degree and major</strong>, <strong>university</strong>, <strong>expected graduation year</strong>, and <strong>one way to reach you</strong>, plus a LinkedIn or portfolio link if you are job hunting. Keep it to four or five lines.')}
                {toc([('include', 'What to include'), ('undergrad', 'Undergraduate examples'), ('grad', 'Graduate and PhD examples'), ('job', 'Examples for internships and job hunting'), ('avoid', 'What to leave out'), ('template', 'Copy-and-paste template')])}
                {h2('include', 'What to include in a student email signature')}
                {table(['Element', 'Example', 'Include?'], [
    ['Full name', 'Maya Johnson', 'Always'],
    ['Pronouns', '(she/her)', 'Optional'],
    ['Degree and major', 'B.A. Psychology', 'Always'],
    ['University', 'University of Michigan', 'Always'],
    ['Expected graduation', 'Class of 2027', 'Always'],
    ['Phone or email', '(555) 012-3456', 'One is enough'],
    ['LinkedIn or portfolio', 'linkedin.com/in/mayaj', 'When job hunting'],
    ['Clubs, honors, GPA', 'Dean’s List', 'Only if relevant']])}
                {h2('undergrad', 'Undergraduate student email signature examples')}
                <p>These work for emailing professors, advisors and campus offices. Simple is best: your professor wants to know which class you are in, not your Instagram.</p>
                {grid(
    plain('Basic college student', '''<b>Maya Johnson</b>
B.A. Psychology, Class of 2027
University of Michigan
mjohnson@umich.edu'''),
    plain('Student with pronouns', '''<b>Daniel Kim</b> (he/him)
B.S. Computer Science | Class of 2026
Georgia Institute of Technology
(555) 014-2290'''),
    plain('Student leader', '''<b>Priya Patel</b>
B.B.A. Marketing, Class of 2026
President, Marketing Association
Indiana University, Kelley School of Business'''),
    plain('Student athlete', '''<b>Marcus Lee</b>
B.S. Kinesiology, Class of 2027
Men’s Soccer, NCAA Division I
University of North Carolina'''))}
                {h2('grad', 'Graduate student and PhD email signature examples')}
                <p>Graduate students often email other researchers, conference organizers and journals, so add your lab or department and a link to your research.</p>
                {grid(
    plain('Graduate student (master’s)', '''<b>Sofia Ramirez</b>
M.S. Candidate, Environmental Engineering
Stanford University
sramirez@stanford.edu'''),
    plain('PhD candidate', '''<b>Ethan Brooks</b>
PhD Candidate, Department of History
Harvard University
ethanbrooks.com · Google Scholar'''),
    plain('Teaching assistant', '''<b>Nora Weiss</b>
Graduate Teaching Assistant, ECON 101
Ph.D. Student, Economics
University of Texas at Austin
Office hours: Tue 2–4 pm, Room 3.112'''),
    plain('Research assistant', '''<b>Jordan Davis</b>
Research Assistant, Human-Computer Interaction Lab
M.S. Information Science, Cornell University
linkedin.com/in/jordandavis'''))}
                {h2('job', 'Student email signatures for internships and job hunting')}
                <p>When you email recruiters, your signature becomes a mini business card. A photo, a LinkedIn link and a portfolio help them remember you.</p>
                {grid(
    sig('Internship applicant', 'Maya Johnson', 'B.A. Psychology, Class of 2027', 'University of Michigan', ['(555) 012-3456'], '#0b5cff', photo='job-seeker.jpg', links=['LinkedIn', 'Portfolio']),
    sig('Recent graduate', 'Daniel Kim', 'B.S. Computer Science, 2026', 'Georgia Tech', ['dkim.dev@gmail.com'], '#1aa89f', initials='DK', links=['GitHub', 'LinkedIn']))}
                {callout('Use your university email address when you write to professors and campus offices. It looks more professional and is less likely to land in spam.')}
                {h2('avoid', 'What to leave out of a student email signature')}
                <ul>
                    <li><strong>Quotes and song lyrics.</strong> Save them for your personal email.</li>
                    <li><strong>Every club you have joined.</strong> Pick one role that matters for the person you are writing to.</li>
                    <li><strong>Large images.</strong> They load slowly and often arrive as attachments.</li>
                    <li><strong>Your GPA,</strong> unless you are applying for jobs and it is strong.</li>
                    <li><strong>Personal social media,</strong> unless it is part of your work, such as a design Instagram.</li>
                </ul>
                {h2('template', 'College student email signature template')}
                <p>Copy this and replace the brackets:</p>
                {plain('Template', '''<b>[First name] [Last name]</b> ([pronouns])
[Degree] [Major], Class of [Year]
[University name]
[Phone or email] | [LinkedIn or portfolio]''')}
                <p>Want it with a photo and clickable LinkedIn icon? Make it in SignTry in two minutes, then add it to <a href="../posts/how-to-create-an-email-signature-in-gmail.html">Gmail</a> or <a href="../guides/how-to-create-an-email-signature-in-outlook.html">Outlook</a>.</p>"""
STUDENT['faqs'] = [
    ('What should a college student put in their email signature?', 'Your full name, degree and major, university, expected graduation year and one way to contact you. Add LinkedIn or a portfolio when job hunting.'),
    ('Should students put pronouns in their email signature?', 'It is optional and increasingly common at universities. If you include them, put them in brackets next to your name.'),
    ('How should a PhD student sign emails?', 'Use “PhD Candidate” (after passing qualifying exams) or “PhD Student”, followed by your department and university, plus a link to your research profile.'),
    ('Should I include my GPA in my email signature?', 'Usually not. Only consider it when applying for internships or jobs, and only if it is strong.'),
    ('Do I need an email signature to email a professor?', 'It is not required, but it helps: your professor instantly sees your name, course and year without having to look you up.'),
]
STUDENT['related'] = [('Examples', 'Teacher email signature examples', 'examples/teacher-email-signature.html'),
                      ('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html'),
                      ('Guide', 'How to make an email signature in Outlook', 'guides/how-to-create-an-email-signature-in-outlook.html')]

# ---------------------------------------------------------------- Teacher
TEACHER = dict(
    path='examples/teacher-email-signature.html', crumb='Teacher email signature', mins=5,
    title='Teacher Email Signature: 8 Examples for Parents & Staff',
    desc='Teacher email signature examples for elementary, middle and high school teachers, special education and substitutes, with what to include for emails to parents.',
    h1='Teacher email signature examples',
    lead='A clear teacher email signature saves parents time: they see your name, grade or subject, school and the best way to reach you, without digging through old emails. Here are 8 teacher email signature examples to copy, plus what to include and what to avoid.',
    image='images/people/healthcare.jpg', cta_h='Make your teacher email signature in 2 minutes',
)
TEACHER['article'] = f"""                {answer('<strong>Quick answer:</strong> A teacher email signature should include your <strong>name</strong> (as students call you, such as “Ms. Rivera”), your <strong>grade or subject</strong>, your <strong>school</strong>, a <strong>phone number or extension</strong>, and when you are available, such as <strong>office hours</strong>. Add a link to your class page if you have one.')}
                {toc([('include', 'What to include'), ('examples', 'Teacher email signature examples'), ('parents', 'Tips for emailing parents'), ('template', 'Template')])}
                {h2('include', 'What to include in a teacher email signature')}
                <ul>
                    <li><strong>Your name</strong> the way families know you: “Ms. Rivera” or “Mr. Thompson”, with your full name if you like.</li>
                    <li><strong>Grade level or subject,</strong> such as “3rd Grade” or “AP Biology”.</li>
                    <li><strong>School name,</strong> and district if you write to families across several schools.</li>
                    <li><strong>Phone and extension,</strong> or a note that email is the best way to reach you.</li>
                    <li><strong>Availability:</strong> office hours or when you reply to email.</li>
                    <li><strong>Class website</strong> or learning platform link.</li>
                    <li><strong>Pronouns,</strong> optional.</li>
                </ul>
                {callout('Many schools and districts have rules for staff email signatures, for example no personal social media or quotes. Check your school’s guidelines before you add anything beyond the basics.')}
                {h2('examples', 'Teacher email signature examples')}
                {grid(
    plain('Elementary school teacher', '''<b>Ms. Ana Rivera</b>
3rd Grade Teacher, Room 14
Lincoln Elementary School
(555) 013-4400 ext. 214
I reply to emails within one school day.'''),
    plain('High school subject teacher', '''<b>Mr. David Thompson</b>
AP Biology &amp; Environmental Science
Westfield High School
Office hours: Mon &amp; Wed, 3:00–3:45 pm
Class page: westfieldhs.org/thompson'''),
    plain('Middle school teacher', '''<b>Mrs. Keisha Brown</b> (she/her)
7th Grade English Language Arts
Roosevelt Middle School
kbrown@rooseveltms.org'''),
    plain('Special education teacher', '''<b>Mr. Luis Ortega</b>
Special Education Teacher, Grades 4–5
Oak Park Elementary School
(555) 011-2280 · Best reached by email'''),
    plain('Substitute teacher', '''<b>Emily Carter</b>
Substitute Teacher
Springfield Public Schools
(555) 019-7765'''),
    plain('ESL teacher', '''<b>Ms. Hana Sato</b>
English as a Second Language (ESL) Teacher
Maple Grove High School
Hablo español · 日本語も話せます'''),
    sig('Teacher with photo', 'Ms. Ana Rivera', '3rd Grade Teacher', 'Lincoln Elementary School', ['(555) 013-4400 ext. 214'], '#1aa89f', initials='AR', links=['Class page', 'Book a conference']),
    sig('School counselor', 'Jordan Hughes', 'School Counselor, Grades 9–12', 'Westfield High School', ['(555) 014-8800 ext. 120'], '#7b5cf0', initials='JH', links=['Schedule a meeting']))}
                {h2('parents', 'Tips for teacher emails to parents')}
                <ol>
                    <li><strong>Set expectations.</strong> A line such as “I reply within one school day” prevents follow-up emails.</li>
                    <li><strong>Make booking easy.</strong> A “Book a conference” link saves a long back-and-forth.</li>
                    <li><strong>List languages you speak,</strong> so families know they can write in their own.</li>
                    <li><strong>Keep it short.</strong> Parents read your emails on their phones.</li>
                </ol>
                {h2('template', 'Teacher email signature template')}
                {plain('Template', '''<b>[Ms./Mr./Mx.] [Full name]</b>
[Grade or subject] Teacher
[School name]
[Phone] ext. [number] · [Office hours]
[Class website]''')}
                <p>Want the whole staff to match? Generate signatures for every teacher from one spreadsheet with <a href="../features/email-signature-management.html">SignTry for teams</a>.</p>"""
TEACHER['faqs'] = [
    ('What should a teacher put in their email signature?', 'Your name as students know you, grade or subject, school, a phone number or extension, and your availability such as office hours. A class website link is a helpful extra.'),
    ('Should teachers include a quote in their email signature?', 'Usually not in emails to parents and staff. Many districts discourage quotes in staff signatures, so check your school’s guidelines.'),
    ('Can a whole school use the same signature design?', 'Yes. With SignTry you design one signature and generate one for every staff member from a CSV, each with their own name and subject.'),
    ('Should I include my personal phone number?', 'No. Use your school phone and extension, or say that email is the best way to reach you.'),
]
TEACHER['related'] = [('Examples', 'College student email signature examples', 'examples/college-student-email-signature.html'),
                      ('Feature', 'Signatures for a whole team from a CSV', 'features/email-signature-management.html'),
                      ('Examples', 'Professional email signature examples', 'examples/email-signature-examples.html')]

# ---------------------------------------------------------------- Real estate
REALESTATE = dict(
    path='examples/real-estate-email-signature.html', crumb='Real estate email signature', mins=6,
    title='Real Estate Email Signature: Examples for Realtors & Brokers',
    desc='Real estate email signature examples for realtors, brokers, property managers and teams. What to include, from license number to listings link, with templates.',
    h1='Real estate email signature examples for agents and brokers',
    lead='Your real estate email signature works like a business card on every email you send to buyers, sellers and other agents. These realtor email signature examples show what to include, from your headshot and brokerage to your license number and listings link.',
    image='images/people/real-estate.jpg', cta_h='Make your real estate email signature in 2 minutes',
)
REALESTATE['article'] = f"""                {answer('<strong>Quick answer:</strong> A real estate email signature should include your <strong>headshot</strong>, <strong>name and title</strong>, <strong>brokerage name and logo</strong>, <strong>license number</strong> where required, <strong>phone</strong>, and a link to your <strong>listings or booking page</strong>. Social icons for Instagram and Facebook are a bonus.')}
                {toc([('include', 'What to include'), ('examples', 'Realtor email signature examples'), ('teams', 'Signatures for brokerages and teams'), ('compliance', 'License numbers and compliance')])}
                {h2('include', 'What to include in a realtor email signature')}
                {table(['Element', 'Why it matters'], [
    ['Professional headshot', 'Clients choose people. A friendly photo builds trust before you meet.'],
    ['Name, title, designations', 'For example REALTOR®, Broker, CRS or ABR.'],
    ['Brokerage name and logo', 'Often required, and it adds credibility.'],
    ['License number', 'Required in many states. See compliance below.'],
    ['Mobile phone', 'Buyers call; make it one tap on a phone.'],
    ['Listings or booking link', 'Turns every email into a showing request.'],
    ['Instagram, Facebook, YouTube', 'Where your property photos and tours live.']])}
                {h2('examples', 'Real estate email signature examples')}
                {grid(
    sig('Real estate agent', 'Lauren Mitchell', 'REALTOR® | Buyer’s Agent', 'Sunrise Realty Group', ['(555) 014-2290', 'License #01234567'], '#0b5cff', photo='real-estate.jpg', links=['View my listings', 'Instagram', 'Book a showing']),
    sig('Broker / owner', 'Robert Hayes', 'Principal Broker, CRS', 'Hayes &amp; Co. Real Estate', ['(555) 018-7700', 'Broker License #00987654'], '#061b31', photo='legal-finance.jpg', links=['Website', 'LinkedIn']),
    sig('Team lead', 'Priya Patel', 'Team Lead, The Patel Team', 'Sunrise Realty Group', ['(555) 012-5500'], '#1aa89f', initials='PP', links=['Our listings', 'Client reviews'], tagline='Helping 120+ families find home in Austin'),
    sig('Property manager', 'Ethan Brooks', 'Property Manager', 'Sunrise Realty Group', ['(555) 011-6612', 'Maintenance requests: portal link'], '#7b5cf0', initials='EB', links=['Tenant portal']),
    plain('Luxury agent (minimal)', '''<b>Sophia Laurent</b>
Luxury Property Specialist
Laurent Estates | Beverly Hills
(555) 019-0001 · laurentestates.com'''),
    plain('Licensed insurance agent', '''<b>Michael Chen</b>
Licensed Life &amp; Health Insurance Agent
Chen Insurance Partners
License #0H12345 · (555) 016-3311'''))}
                {h2('teams', 'Email signatures for brokerages and real estate teams')}
                <p>When every agent designs their own signature, your brokerage ends up with a dozen logos and outdated phone numbers. With SignTry, you pick one real estate template, upload a spreadsheet of your agents, and every agent gets a matching signature with their own photo, license number and phone. A 50-agent brokerage pays $39 a month on yearly billing. <a href="../features/email-signature-management.html">See how team signatures work</a>.</p>
                {fig('../', 'media/stills/team-generation-88.jpg', 'Matching real estate email signatures for a brokerage team', 'One template, a signature for every agent.')}
                {h2('compliance', 'License numbers and compliance')}
                <p>Advertising rules for real estate are set by each state, and many count email as advertising. Common requirements include showing your <strong>brokerage name</strong> and, in some states, your <strong>license number</strong>. Rules vary, so check your state real estate commission and your broker’s policy. If you are a member of the National Association of REALTORS®, use the REALTOR® trademark correctly, in capitals with the ® symbol.</p>
                {callout('Not sure what your state requires? Ask your managing broker. They review marketing materials regularly and can confirm in a minute.')}"""
REALESTATE['faqs'] = [
    ('What should a realtor put in their email signature?', 'A headshot, your name and title, brokerage name and logo, license number where required, mobile phone, and a link to your listings or booking page.'),
    ('Do I need my license number in my email signature?', 'It depends on your state. Many states treat email as advertising and require the brokerage name, and some require the license number. Check your state real estate commission.'),
    ('Should real estate agents include a photo in their email signature?', 'Yes. A professional headshot helps clients recognize and trust you, and it is standard in real estate.'),
    ('How can a brokerage give all agents the same signature?', 'Design one signature in SignTry, then upload a CSV of your agents to generate a matching signature for each one.'),
]
REALESTATE['related'] = [('Feature', 'Team signatures from a CSV', 'features/email-signature-management.html'),
                         ('Feature', 'Real estate email signature templates', 'features/email-signature-templates.html'),
                         ('Guide', 'Social media icons for email signatures', 'guides/social-media-icons-for-email-signature.html')]

# ---------------------------------------------------------------- General examples
EXAMPLES = dict(
    path='examples/email-signature-examples.html', crumb='Email signature examples', mins=7,
    title='Email Signature Examples: 14 Professional Signatures to Copy',
    desc='14 professional email signature examples for business, personal and company email, plus signature block examples for sales, healthcare and more.',
    h1='Email signature examples: 14 professional signatures to copy',
    lead='Looking for email signature examples? Here are 14 professional, personal and company email signature examples, from simple signature blocks to designed signatures with a photo and logo. Each one shows what to include and why it works.',
    image='images/people/sales.jpg', cta_h='Turn any of these examples into your signature',
)
EXAMPLES['article'] = f"""                {answer('<strong>Quick answer:</strong> A professional email signature includes your <strong>name</strong>, <strong>job title</strong>, <strong>company</strong>, <strong>one or two contact details</strong> and <strong>one link</strong>, such as your website or a booking page. A photo or logo is optional but makes it memorable.')}
                {toc([('block', 'Email signature block examples'), ('business', 'Business and company examples'), ('personal', 'Personal email signature examples'), ('industry', 'Examples by industry'), ('rules', '5 rules every good signature follows')])}
                {h2('block', 'Email signature block examples')}
                <p>An email signature block is the few lines of text at the end of an email that identify you. Plain-text blocks are perfect for replies, internal email and anywhere images might not load.</p>
                {grid(
    plain('Simple professional block', '''<b>Jordan Davis</b>
Marketing Director, Northstar Studio
(555) 014-2810 | northstar.co'''),
    plain('Block with pronouns', '''<b>Alex Morgan</b> (they/them)
Senior Product Designer
Brightline Software
alex@brightline.io'''),
    plain('Short reply signature', '''<b>Jamie</b>
Jamie Lee · Account Manager · Acme Inc.'''),
    plain('Block with a call to action', '''<b>Sam Kim</b>
Client Success Lead, Harbor Analytics
(555) 016-4410
Book a 15-minute call: harbor.io/sam'''))}
                {h2('business', 'Business and company email signature examples')}
                <p>Company email signatures add a logo, brand color and the same layout for everyone, so every email looks like it comes from one business.</p>
                {grid(
    sig('Corporate', 'Jordan Davis', 'Marketing Director', 'Northstar Studio', ['jordan@northstar.co', '(555) 014-2810'], '#0b5cff', photo='freelancer.jpg', links=['Website', 'LinkedIn']),
    sig('Sales', 'Marcus Lee', 'Account Executive', 'Harbor Analytics', ['(555) 012-1180'], '#e5484d', photo='sales.jpg', links=['Book a demo', 'LinkedIn']),
    sig('CEO / founder', 'Sofia Ramirez', 'Founder &amp; CEO', 'Brightline Software', ['sofia@brightline.io'], '#7b5cf0', initials='SR', links=['brightline.io', 'LinkedIn', 'X']),
    sig('Consultant', 'Robert Hayes', 'Independent Strategy Consultant', None, ['(555) 018-7700'], '#061b31', photo='legal-finance.jpg', links=['Case studies', 'Book a call'], tagline='Helping B2B teams grow since 2014'))}
                {h2('personal', 'Personal email signature examples')}
                <p>Personal email signatures are for freelancers, side projects and job seekers. Lead with your name and what you do, and link to your best work.</p>
                {grid(
    sig('Freelancer', 'Maya Johnson', 'Freelance Brand Designer', None, ['hello@mayajohnson.design'], '#ec4899', photo='job-seeker.jpg', links=['Portfolio', 'Dribbble', 'Instagram']),
    plain('Job seeker', '''<b>Daniel Kim</b>
Data Analyst | Open to new roles
linkedin.com/in/danielkim · (555) 014-2290'''))}
                {h2('industry', 'Email signature examples by industry')}
                {grid(
    sig('Healthcare', 'Dr. Elena Novak, MD', 'Family Medicine Physician', 'Riverside Family Clinic', ['(555) 010-2200'], '#1aa89f', photo='healthcare.jpg', links=['Book an appointment']),
    sig('Marketing agency', 'Priya Patel', 'Head of Growth', 'Loop &amp; Co. Agency', ['priya@loopco.agency'], '#f59e0b', photo='marketing.jpg', links=['Our work', 'Instagram', 'LinkedIn']),
    plain('Legal', '''<b>Michael Chen</b>, Esq.
Partner, Chen &amp; Walsh LLP
(555) 016-3311 · chenwalsh.com
This email may contain confidential information.'''),
    plain('Nonprofit', '''<b>Emily Carter</b>
Volunteer Coordinator, Green City Alliance
(555) 019-7765
Join our next cleanup: greencity.org/volunteer'''))}
                <p>More by profession: <a href="real-estate-email-signature.html">real estate</a>, <a href="teacher-email-signature.html">teachers</a> and <a href="college-student-email-signature.html">students</a>.</p>
                {h2('rules', '5 rules every good email signature follows')}
                <ol>
                    <li><strong>Name first, biggest.</strong> Everything else supports it.</li>
                    <li><strong>Four or five lines.</strong> If it scrolls, it is too long.</li>
                    <li><strong>One call to action.</strong> A booking link beats five social icons.</li>
                    <li><strong>One accent color,</strong> taken from your logo.</li>
                    <li><strong>Under 600px wide,</strong> so it fits on a phone. See our <a href="../guides/email-signature-size.html">size guide</a>.</li>
                </ol>
                <p>To create any of these, pick a matching <a href="../features/email-signature-templates.html">email signature template</a>, add your details and copy it into your inbox.</p>"""
EXAMPLES['faqs'] = [
    ('What is an email signature block?', 'The few lines of text at the end of an email that identify the sender: usually name, job title, company and contact details.'),
    ('What should a professional email signature include?', 'Your name, job title, company, one or two contact details and one link. A photo or logo is optional.'),
    ('What is a good personal email signature?', 'Your name, what you do, and a link to your best work or LinkedIn. Keep it to two or three lines.'),
    ('Should I put a quote in my email signature?', 'In business email, usually not. A short tagline about what you do is more useful than a quote.'),
    ('How do I make all company email signatures match?', 'Pick one template and generate signatures for everyone from a spreadsheet with <a href="../features/email-signature-management.html">SignTry for teams</a>.'),
]
EXAMPLES['related'] = [('Feature', 'Email signature templates', 'features/email-signature-templates.html'),
                       ('Examples', 'Real estate email signature examples', 'examples/real-estate-email-signature.html'),
                       ('Guide', 'Email signature size and dimensions', 'guides/email-signature-size.html')]


def build():
    hub = ('Guides &amp; examples', 'guides.html')
    return [article_page(a, 'Examples', hub) for a in (STUDENT, TEACHER, REALESTATE, EXAMPLES)]
