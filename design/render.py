import re, json, subprocess, html, sys
def data_of(src):
    js = re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>', src, re.S).group(1)
    prog = "class DCLogic{constructor(){this.props={};this.state={}}setState(){}};" + js + ";console.log(JSON.stringify(new Component().renderVals()))"
    return json.loads(subprocess.run(['node','-e',prog],capture_output=True,text=True,check=True).stdout)
def get(ctx, path):
    if path in ('true','false'): return path=='true'
    v = ctx
    for k in path.split('.'):
        v = v[k]
    return v
def fill(t, ctx):
    def rep(m):
        v = get(ctx, m.group(1).strip())
        return html.escape(str(v), quote=True)
    return re.sub(r'\{\{\s*([\w.$]+)\s*\}\}', rep, t)
def resolve_if(t):
    def f(m):
        v=m.group(1).strip()
        return m.group(2) if v not in ('', 'False', 'false', '0', 'None') else ''
    prev=None
    while prev!=t:
        prev=t; t=re.sub(r'<sc-if value="([^"]*)"[^>]*>((?:(?!<sc-if).)*?)</sc-if>', f, t, flags=re.S)
    return t
def render(src, page_links):
    data = data_of(src)
    body = re.search(r'<x-dc>(.*?)</x-dc>', src, re.S).group(1)
    helmet = re.search(r'<helmet>(.*?)</helmet>', body, re.S).group(1)
    body = re.sub(r'<helmet>.*?</helmet>', '', body, flags=re.S)
    def loop(m):
        lst, var, inner = m.group(1), m.group(2), m.group(3)
        out=[]
        for item in get(data, lst):
            ctx = dict(data); ctx[var] = item
            out.append(resolve_if(fill(inner, ctx)))
        return ''.join(out)
    body = re.sub(r'<sc-for list="\{\{\s*([\w.]+)\s*\}\}" as="(\w+)"[^>]*>(.*?)</sc-for>', loop, body, flags=re.S)
    body = resolve_if(fill(body, data))
    for a,b in page_links.items(): body = body.replace(a,b)
    title = re.search(r'<title>(.*?)</title>', src).group(1)
    return title, helmet, body
skip = '<a href="#content" class="skip">Skip to content</a>'
banner = '<div role="note" style="background:#FFF4D6;color:#5A4300;font:600 14px/1.4 Inter,system-ui,sans-serif;padding:10px 16px;text-align:center;border-bottom:1px solid #E8D49A">Draft mockup for internal review — not the official AT-NCIGT website. Bracketed items and grey circles are placeholders.</div>'
extra_css = '''
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:16px}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #A8763E;outline-offset:2px}
.skip{position:absolute;left:-9999px;top:8px;background:#0F1B2D;color:#fff;padding:10px 14px;border-radius:6px;z-index:10}.skip:focus{left:8px}
img{max-width:100%}
@media (max-width: 760px){
 [style*="repeat(3, minmax(0, 1fr))"]{grid-template-columns:minmax(0,1fr)!important}
 [style*="repeat(4, minmax(0, 1fr))"]{grid-template-columns:repeat(2,minmax(0,1fr))!important}
 [style*="repeat(auto-fit, minmax(340px"],[style*="repeat(auto-fit, minmax(320px"]{grid-template-columns:minmax(0,1fr)!important}
 h1{font-size:32px!important}
 h2{font-size:26px!important}
 [style*="padding: 40px"],[style*="padding: 36px"],[style*="padding: 32px;"]{padding:22px!important}
}
'''
links = {'href="Industry.dc.html"':'href="industry.html"','href="Main.dc.html"':'href="index.html"','href="TRD1.dc.html"':'href="trd1.html"','href="TRD2.dc.html"':'href="trd2.html"','href="TRD3.dc.html"':'href="trd3.html"'}
P='/home/claude/ncigt/project/'
pages=[('Main','index','AT-NCIGT · Advanced Technologies - National Center for Image Guided Therapy (draft)','Advanced Technologies - National Center for Image Guided Therapy (AT-NCIGT) at Brigham and Women\'s Hospital: imaging, microdevices, robotics and navigation research for image-guided therapy.'),
('Industry','industry','Working with industry · AT-NCIGT (draft)','How AT-NCIGT partners with companies, from clinical needs to patient studies and regulatory data.'),
('TRD1','trd1','TR&D 1: Imaging cancer heterogeneity · AT-NCIGT (draft)','AT-NCIGT TR&D 1: advanced diffusion and CEST MRI at 3T and 7T.'),
('TRD2','trd2','TR&D 2: Implantable microdevices · AT-NCIGT (draft)','AT-NCIGT TR&D 2: implantable microdevices that measure drug response inside tumors.'),
('TRD3','trd3','TR&D 3: Enabling technologies for data-driven interventions · AT-NCIGT (draft)','AT-NCIGT TR&D 3: robotic needle guidance and augmented-reality navigation.')]
import re as _re
ld='<script type="application/ld+json">{"@context":"https://schema.org","@type":"ResearchOrganization","name":"Advanced Technologies - National Center for Image Guided Therapy","alternateName":"AT-NCIGT","parentOrganization":{"@type":"Hospital","name":"Brigham and Women\'s Hospital"},"funder":{"@type":"GovernmentOrganization","name":"National Institute of Biomedical Imaging and Bioengineering"}}</script>'
for src, out, ptitle, desc in pages:
    title, helmet, body = render(open(P+src+'.dc.html').read(), links)
    helmet = helmet.replace('<link rel="preconnect" href="https://fonts.googleapis.com">','')
    body = _re.sub(r'<svg width="36" height="36" viewBox="0 0 36 36" aria-hidden="true">.*?</svg>','<img src="ncigt-logo.png" alt="AT-NCIGT logo" width="52" height="52" style="display:block">',body,count=1,flags=_re.S)
    body = body.replace('</header>','</header>\n<div id="content"></div>',1)
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" href="ncigt-logo.png">
<title>{html.escape(ptitle)}</title>
{ld if src=='Main' else ''}
{helmet.replace('<style>','<style>'+extra_css,1)}
</head>
<body>
{skip}
{banner}
{body}
</body>
</html>
'''
    assert '{{' not in doc and 'sc-for' not in doc and '.dc.html' not in doc, src
    open('/home/claude/site/'+out+'.html','w').write(doc)
    print(out, len(doc))
