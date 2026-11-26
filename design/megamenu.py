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

CSS = """<style id="mm-css">
.ym-btn{display:inline-flex;align-items:center;gap:10px;background:#0F1B2D;color:#FFFFFF;border:0;border-radius:2px;padding:12px 18px;font:600 13px Inter,system-ui,sans-serif;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer}
.ym-btn:hover,.ym-btn:focus-visible{background:#0B5F86}
.ym-bars{display:inline-block;width:18px;height:12px;position:relative;border-top:2px solid currentColor;border-bottom:2px solid currentColor}
.ym-bars::after{content:"";position:absolute;left:0;right:0;top:3px;border-top:2px solid currentColor}
.ym{position:fixed;inset:0;z-index:1000;background:#0F1B2D;color:#FFFFFF;overflow:auto;display:none}
.ym.open{display:block}
.ym-top{max-width:1200px;margin:0 auto;padding:18px 24px;display:flex;justify-content:space-between;align-items:center}
.ym-top .ym-logo{font-family:'Source Serif 4',Georgia,serif;font-size:24px;font-weight:600;color:#FFFFFF;text-decoration:none}
.ym-close{background:#0B5F86}
.ym-body{max-width:1200px;margin:0 auto;padding:8px 24px 64px}
.ym-sec{border-top:1px solid rgba(255,255,255,.18);display:grid;grid-template-columns:minmax(220px,320px) 1fr;gap:8px 40px;padding:18px 0}
.ym-sec>a{font-family:'Source Serif 4',Georgia,serif;font-size:28px;font-weight:500;color:#FFFFFF;text-decoration:none;line-height:1.2}
.ym-sec>a:hover{color:#D9B98F}
.ym-sub{display:flex;flex-wrap:wrap;gap:6px 22px;align-content:center;list-style:none;margin:0;padding:0}
.ym-sub a{color:#C9D3E0;text-decoration:none;font-size:13px;font-weight:600;letter-spacing:1px;text-transform:uppercase}
.ym-sub a:hover{color:#FFFFFF;text-decoration:underline}
@media (max-width:760px){.ym-sec{grid-template-columns:1fr}.ym-sec>a{font-size:24px}.ym-btn{padding:10px 14px}}
body.ym-lock{overflow:hidden}
</style>
<script id="mm-js">document.addEventListener("DOMContentLoaded",function(){var o=document.getElementById("ym"),b=document.getElementById("ym-open"),c=document.getElementById("ym-close");if(!o||!b)return;
function op(){o.classList.add("open");document.body.classList.add("ym-lock");b.setAttribute("aria-expanded","true");c.focus();}
function cl(){o.classList.remove("open");document.body.classList.remove("ym-lock");b.setAttribute("aria-expanded","false");b.focus();}
b.addEventListener("click",op);c.addEventListener("click",cl);document.addEventListener("keydown",function(e){if(e.key==="Escape"&&o.classList.contains("open"))cl();});
o.addEventListener("click",function(e){if(e.target.tagName==="A")cl();});});</script>
"""

def build_nav():
    e = lambda s: html.escape(s, quote=True)
    out = ['<nav aria-label="Main" class="mm">',
           '<button type="button" class="ym-btn" id="ym-open" aria-expanded="false" aria-controls="ym"><span class="ym-bars" aria-hidden="true"></span>Menu</button>',
           '<div class="ym" id="ym" role="dialog" aria-modal="true" aria-label="Site menu"><div class="ym-top"><a class="ym-logo" href="index.html">AT-NCIGT</a>',
           '<button type="button" class="ym-btn ym-close" id="ym-close">✕ Close</button></div><div class="ym-body">']
    for label, href, sub, links in MENU:
        out.append(f'<div class="ym-sec"><a href="{e(href)}">{e(label)}</a><ul class="ym-sub">')
        seen=set()
        for t, h, note in links:
            if h == href or t in seen: continue
            seen.add(t)
            out.append(f'<li><a href="{e(h)}">{e(t)}</a></li>')
        out.append('</ul></div>')
    out.append('</div></div></nav>')
    return '\n'.join(out)

NAV = build_nav()

def apply(doc):
    if not re.search(r'<nav aria-label="Main"', doc):
        return doc
    doc = re.sub(r'<nav aria-label="Main".*?</nav>', lambda m: NAV, doc, count=1, flags=re.S)
    doc = re.sub(r'<style id="mm-css">.*?</style>\n?', '', doc, flags=re.S)
    doc = re.sub(r'<script id="mm-js">.*?</script>\n?', '', doc, flags=re.S)
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
