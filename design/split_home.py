"""One-time restructure: shorten the home page (Main.dc.html) and move detail
into four section pages (Clinical, Partner, Resources, About .dc.html).
Each home section keeps its summary and ends with a row of prominent links.
"""
import re

SRC = 'Main.dc.html'
orig = open(SRC, encoding='utf-8').read()

head, rest = orig.split('</header>', 1)
head += '</header>'
mid, foot = rest.split('<footer', 1)
foot = '<footer' + foot

secs = re.findall(r'<section\b.*?</section>', mid, re.S)
def key(s):
    m = re.search(r'<section[^>]*\bid="([^"]+)"', s) or re.search(r'aria-labelledby="([^"]+)"', s)
    return m.group(1)
S = {key(s): s for s in secs}
order = [key(s) for s in secs]
assert order == ['top', 'research', 'clinical', 'resources', 'training', 'industry', 'partner',
                 'partner-research', 'community', 'shared', 'events', 'about', 'history', 'contact'], order

def linkrow(links, dark=False):
    c = '#FFFFFF' if dark else '#0B5F86'
    bc = '#D9B98F' if dark else '#0B5F86'
    items = ''.join(f'<a href="{h}" style="display: inline-block; border: 1.5px solid {bc}; color: {c}; padding: 10px 16px; border-radius: 8px; font-weight: 600; font-size: 15px; text-decoration: none">{t} →</a>' for t, h in links)
    return f'<div style="margin-top: 28px; display: flex; flex-wrap: wrap; gap: 10px">{items}</div>\n'

def cut(s, start_pat, end_pat, repl='', include_end=True):
    i = s.index(start_pat)
    j = s.index(end_pat, i) + (len(end_pat) if include_end else 0)
    return s[:i] + repl + s[j:]

# ---------- new home sections ----------
research = S['research']
research = cut(research, '<h3 style="margin: 56px 0 8px; font-size: 26px">Latest major achievements</h3>', '</section>',
               linkrow([('Latest publications', 'Publications.dc.html'), ('TR&amp;D 1', 'TRD1.dc.html'),
                        ('TR&amp;D 2', 'TRD2.dc.html'), ('TR&amp;D 3', 'TRD3.dc.html'),
                        ('Collaborative and service projects', 'Partner.dc.html#partner-research')]) + '</section>')

clinical = S['clinical']
clinical = cut(clinical, '<h3 style="margin: 0 0 16px; font-size: 22px; color: #FFFFFF">Clinical studies using the center</h3>',
               '</sc-for>\n</div>\n',
               linkrow([('Clinical studies using the center', 'Clinical.dc.html#studies'), ('About AMIGO', 'page-amigo.html'),
                        ('Procedures in AMIGO', 'page-amigoprocedures.html'), ('Clinical trials', 'page-clinical-trials.html')], dark=True))
clinical = clinical.replace('<div style="background: #F6F1EA; border-radius: 16px; padding: 32px; display: flex; flex-wrap: wrap; gap: 32px; align-items: center; margin-bottom: 32px">',
                            '<div style="background: #F6F1EA; border-radius: 16px; padding: 32px; display: flex; flex-wrap: wrap; gap: 32px; align-items: center">')

resources = S['resources'].replace('</section>', linkrow([('All equipment, software and data', 'Resources.dc.html'),
    ('Recently shared software and data', 'Resources.dc.html#shared'), ('Software and tutorials', 'page-software-and-tutorials.html'),
    ('Online lectures', 'page-online-lectures.html')]) + '</section>')

training = S['training']
training = cut(training, '<div style="margin-top: 24px; display: flex; flex-wrap: wrap; gap: 20px">', '</section>',
               linkrow([('Trainees and alumni', 'page-trainees.html'), ('T32 training program', 'page-training-in-image-guidance-precision-diagnosis-and-therapy.html'),
                        ('Postdoctoral and visiting scholars', 'page-visiting-scholars-program.html'), ('Project Week hackathons', 'page-project-week.html'),
                        ('Online lectures', 'page-online-lectures.html')]) + '</section>')
training = training.replace('grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px">\n<sc-for list="{{alumni}}"',
                            'grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px">\n<sc-for list="{{alumni}}"')

partner = S['partner']
partner = cut(partner, '<h3 style="margin: 0 0 14px; font-size: 22px">Where your work could connect</h3>', '</section>',
              linkrow([('How to partner with us', 'Partner.dc.html'), ('Where your work could connect', 'Partner.dc.html#connect'),
                       ('Current collaborative and service projects', 'Partner.dc.html#partner-research'),
                       ('Working with industry', 'Industry.dc.html')]) + '</section>')
partner = partner.replace('gap: 16px; margin-bottom: 32px">\n<sc-for list="{{steps}}"', 'gap: 16px">\n<sc-for list="{{steps}}"', 1)

community = S['community'].replace('<sc-for list="{{wins}}" as="w" hint-placeholder-count="6">', '<sc-for list="{{wins3}}" as="w" hint-placeholder-count="3">')
community = cut(community, '<div style="margin-top: 24px; background: #FFFFFF; border-radius: 12px; padding: 18px 22px;', '</div>\n</div>\n</section>',
                linkrow([('All news', 'news.html'), ('Research seminars', 'page-seminars.html'), ('Events', 'page-events.html')]) + '</div>\n</section>')

about = S['about'].replace('<a href="page-history.html">History of the center →</a>', '<a href="About.dc.html#history">History of the center →</a>')
about = cut(about, '<div style="margin-top: 20px; background: #F6F1EA; border-radius: 14px; padding: 22px 24px">', '</section>',
            linkrow([('About the center', 'About.dc.html'), ('History of the center', 'About.dc.html#history'),
                     ('Acknowledging the center', 'About.dc.html#acknowledge'), ('Leadership and organization', 'page-team.html')]) + '</section>')

home = [S['top'], research, clinical, resources, training, S['industry'], partner, community, S['events'], about, S['contact']]

# ---------- section pages ----------
def hero(title, sub):
    return (f'<section id="top" style="background: #0F1B2D; color: #FFFFFF">\n<div style="max-width: 1200px; margin: 0 auto; padding: 48px 24px 44px">\n'
            f'<p style="margin: 0 0 10px; font-size: 14px; font-weight: 600"><a href="Main.dc.html" style="color: #D9B98F">Home</a></p>\n'
            f'<h1 style="margin: 0 0 10px; font-size: 40px; line-height: 1.15; color: #FFFFFF">{title}</h1>\n'
            f'<p style="margin: 0; font-size: 18px; line-height: 1.6; color: #C9D3E0; max-width: 820px">{sub}</p>\n</div>\n</section>\n')

def fix_anchors(body):
    ids = set(re.findall(r'\bid="([^"]+)"', body))
    return re.sub(r'href="#([^"]+)"', lambda m: m.group(0) if m.group(1) in ids else f'href="Main.dc.html#{m.group(1)}"', body)

def page(title_tag, h1, sub, sections):
    body = hero(h1, sub) + '\n'.join(sections)
    h = head.replace('<title>NCIGT homepage</title>', f'<title>{title_tag}</title>').replace('<a href="#top"', '<a href="Main.dc.html"', 1)
    return fix_anchors(h + '\n' + body + '\n' + foot)

clin_full = S['clinical'].replace('margin-top: 56px', 'margin-top: 0').replace(
    '<h3 style="margin: 0 0 16px; font-size: 22px; color: #FFFFFF">Clinical studies using the center</h3>',
    '<h3 id="studies" style="margin: 0 0 16px; font-size: 22px; color: #FFFFFF">Clinical studies using the center</h3>')
part_full = S['partner'].replace('<h3 style="margin: 0 0 14px; font-size: 22px">Where your work could connect</h3>',
                                 '<h3 id="connect" style="margin: 0 0 14px; font-size: 22px">Where your work could connect</h3>')
about_full = S['about'].replace('<div style="margin-top: 20px; background: #F6F1EA; border-radius: 14px; padding: 22px 24px">',
                                '<div id="acknowledge" style="margin-top: 20px; background: #F6F1EA; border-radius: 14px; padding: 22px 24px">').replace(
                                '<a href="page-history.html">History of the center →</a>', '<a href="#history">History of the center →</a>')

pages = {
    'Clinical.dc.html': page('AMIGO and clinical research', 'AMIGO and clinical research',
        'The AMIGO suite and the clinical studies that use the center’s imaging, guidance and analysis resources.', [clin_full]),
    'Partner.dc.html': page('Partner with us', 'Partner with the center',
        'How to start working with us, where your work could connect, and the collaborative and service projects under way.',
        [part_full, S['partner-research'], S['industry']]),
    'Resources.dc.html': page('Resources', 'Resources for collaborators',
        'Equipment, tools, software and data that center investigators share with collaborators.', [S['resources'], S['shared']]),
    'About.dc.html': page('About the center', 'About the center',
        'Our home at Mass General Brigham, how to acknowledge the center, and its history through NIH funding cycles.', [about_full, S['history'], S['contact']]),
}

new_main = head + '\n' + '\n\n'.join(home) + '\n\n' + foot
new_main = new_main.replace('renderVals() {\nreturn {', 'renderVals() {\nconst d = {', 1)
i = new_main.rindex('};\n}\n}\n</script>')
new_main = new_main[:i] + '};\nd.wins3 = d.wins.slice(0, 3);\nreturn d;\n}\n}\n</script>' + new_main[i + len('};\n}\n}\n</script>'):]
open(SRC, 'w', encoding='utf-8').write(new_main)
for f, t in pages.items():
    open(f, 'w', encoding='utf-8').write(t)
print('done')
