"""Hover drop-down main menu for the AT-NCIGT mockup.

apply(doc) replaces the <nav aria-label="Main"> block of a published page with
the drop-down menu and adds its CSS once. Idempotent: running it again on a page
that already has the menu rewrites the menu to the current MENU definition.

Run on the published pages:  python3 design/megamenu.py *.html
render.py calls apply() on every page it builds.
"""
import re, sys, html

# (label, landing link, short line under the panel title, [(link text, href, note)])
MENU = [
    ('Research', 'research.html', 'Three technology research and development projects', [
        ('TR&D 1: Imaging cancer heterogeneity', 'trd1.html', 'Advanced diffusion and CEST MRI'),
        ('TR&D 2: Implantable microdevices', 'trd2.html', 'Testing drugs inside the tumor'),
        ('TR&D 3: Enabling technologies', 'trd3.html', 'Robotic guidance and AR navigation'),
        ('Publications', 'publications.html', 'Major achievements and collaborations'),
        ('Collaborations', 'page-collaborations.html', 'NIH-funded researchers using center technology'),
    ]),
    ('People', 'people.html', 'Investigators, trainees and advisors', [
        ('Leadership and investigators', 'people.html', 'Who leads and carries out the research'),
        ('Trainees and alumni', 'page-trainees.html', 'Current trainees and where graduates are now'),
    ]),
    ('AMIGO', 'clinical.html', 'Clinical research in the AMIGO suite', [
        ('About the AMIGO suite', 'page-amigo.html', 'MRI, PET/CT and X-ray in one procedure suite'),
        ('Procedures in AMIGO', 'page-amigoprocedures.html', 'Procedures that are part of clinical trials'),
        ('Clinical trials', 'page-clinical-trials.html', 'Current studies, such as MRI-guided prostate biopsy'),
        ('Clinical studies with the center', 'clinical.html#studies', 'Prostate, brain, breast, thoracic and more'),
    ]),
    ('Resources', 'resources.html', 'Tools and equipment open to collaborators', [
        ('Equipment and tools', 'resources.html', 'Imaging, robotics and devices you can use'),
        ('Software, tutorials and data', 'resources.html#software', '3D Slicer, OpenIGTLink, datasets and more'),
        ('Fast Imaging Library', 'page-fast-imaging-library.html', 'Reconstruction code for accelerated MRI'),
        ('Online lectures', 'page-online-lectures.html', 'Free recorded talks and seminars'),
    ]),
    ('Training', 'training.html', 'Where training with us can lead', [
        ('Trainees and alumni', 'page-trainees.html', 'Our roster since 2001 and where alumni went'),
        ('Postdoctoral and visiting scholars', 'page-visiting-scholars-program.html', 'Train with us for months or years'),
        ('T32 training program', 'page-training-in-image-guidance-precision-diagnosis-and-therapy.html', 'Image Guidance, Precision Diagnosis and Therapy'),
        ('Project Week hackathons', 'page-project-week.html', 'Hands-on open-source programming weeks'),
        ('Research seminars', 'page-seminars.html', 'The Ferenc Jolesz Research Seminar Series'),
    ]),
    ('Partner with us', 'partner.html', 'Collaborate with the center', [
        ('How to partner with us', 'partner.html', 'Three steps from a conversation to a project'),
        ('Collaborative and service projects', 'partner.html#partner-research', 'Formal projects under way with the center'),
        ('Working with industry', 'industry.html', 'From a clinical need to a device ready for patients'),
        ('Collaborations', 'page-collaborations.html', 'Current and past NIH-funded collaborations'),
    ]),
    ('News & events', 'news.html', 'News, seminars and meetings', [
        ('News and seminars', 'news.html', 'Awards, papers, grants and talks'),
        ('iMRI Symposium', 'page-imri-2024.html', 'The interventional MRI meeting we co-organize'),
        ('National IGT Workshops', 'page-national-image-guided-therapy-workshops.html', 'Our national image-guided therapy workshop series'),
        ('Project Week', 'page-project-week.html', 'Twice-yearly open-source hackathon'),
    ]),
    ('About', 'about.html', 'The center and its history', [
        ('About the center', 'about.html', 'Our home at Mass General Brigham'),
        ('History of the center', 'about.html#history', 'NIH funding cycles since the NCIGT'),
        ('IGT research at the Brigham', 'page-history.html', 'How image-guided therapy began here'),
        ('Contact', 'about.html#contact', 'Reach the right person for your question'),
        ('All pages', 'sitemap.html', 'A full index of the site'),
    ]),
]

CSS = '''<style id="mm-css">
.mm{display:flex;flex-wrap:wrap;gap:4px 4px;font-size:15px;font-weight:500;position:relative;z-index:50}
.mm-item{position:relative}
.mm-top{display:inline-flex;align-items:center;gap:5px;padding:8px 10px;border-radius:6px;color:#0F1B2D;text-decoration:none}
.mm-top::after{content:"";width:6px;height:6px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-2px);opacity:.6}
.mm-item:hover .mm-top,.mm-item:focus-within .mm-top{background:#F3F6FA;color:#0B5F86}
.mm-panel{display:none;position:absolute;top:100%;left:0;padding-top:8px;min-width:300px}
.mm-item.mm-right .mm-panel{left:auto;right:0}
.mm-item:hover .mm-panel,.mm-item:focus-within .mm-panel{display:block}
.mm-box{background:#FFFFFF;border:1px solid #E3E8EF;border-top:3px solid #0B5F86;border-radius:10px;box-shadow:0 12px 32px rgba(15,27,45,.16);padding:18px 20px}
.mm-head{display:block;font-family:'Source Serif 4',Georgia,serif;font-size:18px;font-weight:600;color:#0F1B2D;text-decoration:none}
.mm-head:hover{color:#0B5F86}
.mm-sub{font-size:13px;color:#4A5668;margin:2px 0 12px;font-weight:400}
.mm-list{list-style:none;margin:0;padding:12px 0 0;border-top:1px solid #E3E8EF;display:flex;flex-direction:column;gap:2px}
.mm-list a{display:block;padding:7px 8px;margin:0 -8px;border-radius:6px;color:#0F1B2D;text-decoration:none;font-size:15px;font-weight:600}
.mm-list a:hover,.mm-list a:focus{background:#F3F6FA;color:#0B5F86}
.mm-list small{display:block;font-size:12.5px;font-weight:400;color:#4A5668;margin-top:1px}
@media (max-width:760px){.mm-panel{display:none!important}.mm-top{padding:6px 8px}.mm-top::after{display:none}}
</style>
'''

def build_nav():
    e = lambda s: html.escape(s, quote=True)
    out = ['<nav aria-label="Main" class="mm">']
    n = len(MENU)
    for i, (label, href, sub, links) in enumerate(MENU):
        cls = 'mm-item mm-right' if i >= n - 2 else 'mm-item'
        out.append(f'<div class="{cls}"><a class="mm-top" href="{e(href)}" aria-haspopup="true">{e(label)}</a>')
        out.append(f'<div class="mm-panel"><div class="mm-box"><a class="mm-head" href="{e(href)}">{e(label)} →</a><div class="mm-sub">{e(sub)}</div><ul class="mm-list">')
        for t, h, note in links:
            out.append(f'<li><a href="{e(h)}">{e(t)}' + (f'<small>{e(note)}</small>' if note else '') + '</a></li>')
        out.append('</ul></div></div></div>')
    out.append('</nav>')
    return '\n'.join(out)

NAV = build_nav()

def apply(doc):
    if not re.search(r'<nav aria-label="Main"', doc):
        return doc
    doc = re.sub(r'<nav aria-label="Main".*?</nav>', lambda m: NAV, doc, count=1, flags=re.S)
    doc = re.sub(r'<style id="mm-css">.*?</style>\n?', '', doc, flags=re.S)
    doc = doc.replace('</head>', CSS + '</head>', 1)
    return doc

if __name__ == '__main__':
    changed = 0
    for f in sys.argv[1:]:
        s = open(f, encoding='utf-8').read()
        t = apply(s)
        if t != s:
            open(f, 'w', encoding='utf-8').write(t); changed += 1
    print('updated', changed, 'of', len(sys.argv) - 1)
