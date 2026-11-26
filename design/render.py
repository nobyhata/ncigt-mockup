import re, json, subprocess, html, sys
def data_of(src):
    js = re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>', src, re.S).group(1)
    prog = "class DCLogic{constructor(){this.props={};this.state={}}setState(){}};" + js + ";console.log(JSON.stringify(new Component().renderVals()))"
    return json.loads(subprocess.run(['node','-e',prog],capture_output=True,text=True,check=True).stdout)
def get(ctx, path):
    v = ctx
    for k in path.split('.'):
        v = v[k]
    return v
def fill(t, ctx):
    def rep(m):
        v = get(ctx, m.group(1).strip())
        return html.escape(str(v), quote=True)
    return re.sub(r'\{\{\s*([\w.$]+)\s*\}\}', rep, t)
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
            out.append(fill(inner, ctx))
        return ''.join(out)
    body = re.sub(r'<sc-for list="\{\{\s*([\w.]+)\s*\}\}" as="(\w+)"[^>]*>(.*?)</sc-for>', loop, body, flags=re.S)
    body = fill(body, data)
    for a,b in page_links.items(): body = body.replace(a,b)
    title = re.search(r'<title>(.*?)</title>', src).group(1)
    return title, helmet, body
banner = '<div role="note" style="background:#FFF4D6;color:#5A4300;font:600 14px/1.4 Inter,system-ui,sans-serif;padding:10px 16px;text-align:center;border-bottom:1px solid #E8D49A">Draft mockup for internal review — not the official NCIGT website. Bracketed items and grey circles are placeholders.</div>'
extra_css = '''
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:16px}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}}
a:focus-visible{outline:3px solid #A8763E;outline-offset:2px}
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
links = {'href="Industry.dc.html"':'href="industry.html"','href="Main.dc.html"':'href="index.html"'}
for srcf, outf, ptitle in [('/home/claude/ncigt/project/Main.dc.html','/home/claude/site/index.html','NCIGT (draft mockup)'),('/home/claude/ncigt/project/Industry.dc.html','/home/claude/site/industry.html','Working with industry · NCIGT (draft)')]:
    title, helmet, body = render(open(srcf).read(), links)
    helmet = helmet.replace('<link rel="preconnect" href="https://fonts.googleapis.com">','')
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{ptitle}</title>
{helmet.replace('<style>','<style>'+extra_css,1)}
</head>
<body>
{banner}
{body}
</body>
</html>
'''
    assert '{{' not in doc and 'sc-for' not in doc, srcf
    open(outf,'w').write(doc)
    print(outf, len(doc))
