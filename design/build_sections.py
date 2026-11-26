"""Builds the section structure from sitetree.py:
- research.html and training.html (section landing pages that did not exist)
- sitemap.html (all pages, section by section)
- an "In this section" index on every section landing page (apply(doc, file))

    python3 design/build_sections.py      # after restyle.py; render.py also calls apply()
"""
import os, re, sys, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import sitetree

def cards(items):
    out = []
    for f, t, n, ch in items:
        sub = ''.join(f'<span class="chl">↳ {html.escape(c[1])}</span>' for c in ch)
        out.append(f'<a class="card" href="{f}"><strong>{html.escape(t)}</strong><span>{html.escape(n)}</span>{sub}</a>')
    return '<div class="cards">' + ''.join(out) + '</div>'

def index_block(sec, heading='In this section'):
    b = [f'<section class="secidx" aria-label="{html.escape(sec["label"])}: {heading}"><div class="w"><h2>{heading}</h2>']
    for gt, items in sec['groups']:
        if gt: b.append(f'<h3>{html.escape(gt)}</h3>')
        b.append(cards(items))
    b.append('</div></section>')
    return ''.join(b)

CSS = '''<style id="secidx-css">
.secidx{background:#F7F9FC;border-top:1px solid #E3E8EF}.secidx .w{max-width:1200px;margin:0 auto;padding:48px 24px 56px}
.secidx h2{font-family:'Source Serif 4',Georgia,serif;font-size:26px;margin:0 0 6px}.secidx h3{font-size:13px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#8A5A2B;margin:24px 0 10px}
.secidx .cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.secidx .card{display:flex;flex-direction:column;gap:6px;border:1px solid #E3E8EF;border-radius:12px;padding:16px 18px;background:#fff;color:#0F1B2D;text-decoration:none;line-height:1.45}
.secidx .card:hover{border-color:#0B5F86;box-shadow:0 6px 18px rgba(15,27,45,.08);text-decoration:none}
.secidx .card strong{font-family:'Source Serif 4',Georgia,serif;font-size:17px;line-height:1.3}.secidx .card span{font-size:14px;color:#4A5668}
.secidx .card .chl{font-size:13px;color:#0B5F86}
</style>
'''

def apply(doc, f):
    """add the section index to a section landing page"""
    sec = next((s for s in sitetree.SECTIONS if s['landing'] == f), None)
    if not sec or not any(items for _, items in sec['groups']): return doc
    doc = re.sub(r'<section class="secidx".*?</section>', '', doc, flags=re.S)
    doc = re.sub(r'<style id="secidx-css">.*?</style>\n?', '', doc, flags=re.S)
    doc = doc.replace('</head>', CSS + '</head>', 1)
    blk = index_block(sec)
    if f == 'news.html':   # long list page: index goes right under the title
        return re.sub(r'(<section class="hx">.*?</section>)', lambda m: m.group(1) + blk, doc, count=1, flags=re.S)
    return doc.replace('<footer', blk + '\n<footer', 1)

def shell():
    sys.path.insert(0, HERE); import restyle
    doc = open(os.path.join(ROOT, 'page-team.html'), encoding='utf-8').read()
    return restyle.shell_parts(doc)

def page(head, foot, title, lede, crumbs, body, desc):
    h = re.sub(r'<title>.*?</title>', f'<title>{html.escape(title)} · AT-NCIGT (draft)</title>', head, count=1)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(desc)}">', h, count=1)
    hero = (f'<section class="hx"><div class="w"><p class="crumb">' + '<span>›</span>'.join(crumbs) + f'</p><h1>{html.escape(title)}</h1>'
            f'<p class="lede">{html.escape(lede)}</p></div></section>')
    return h + f'<main id="main">{hero}{body}</main>' + foot

def main():
    head, foot = shell()
    head = head.replace('</head>', CSS + '</head>', 1)
    home = '<a href="index.html">Home</a>'
    # site map
    b = ['<div class="lay one"><article class="arc"><p>Every page of the site, section by section. News items are listed on <a href="news.html">News and seminars</a>.</p>']
    for sec in sitetree.SECTIONS:
        b.append(f'<h2><a href="{sec["landing"]}">{html.escape(sec["label"])}</a></h2><p>{html.escape(sec["blurb"])}</p>')
        for gt, items in sec['groups']:
            if gt: b.append(f'<h3>{html.escape(gt)}</h3>')
            b.append('<ul>' + ''.join(f'<li><a href="{f}">{html.escape(t)}</a> — {html.escape(n)}' +
                     ('<ul>' + ''.join(f'<li><a href="{c[0]}">{html.escape(c[1])}</a> — {html.escape(c[2])}</li>' for c in ch) + '</ul>' if ch else '') + '</li>'
                     for f, t, n, ch in items) + '</ul>')
    b.append('</article></div>')
    about = next(s for s in sitetree.SECTIONS if s['key'] == 'about')
    open(os.path.join(ROOT, 'sitemap.html'), 'w', encoding='utf-8').write(
        page(head, foot, 'All pages', 'The complete site, section by section.', [home, '<a href="about.html">About</a>'], ''.join(b), 'All pages of AT-NCIGT'))
    n = 0
    for sec in sitetree.SECTIONS:
        if sec['key'] in ('research', 'amigo', 'resources', 'training', 'partner', 'about'): continue
        p = os.path.join(ROOT, sec['landing'])
        d = open(p, encoding='utf-8').read(); d2 = apply(d, sec['landing'])
        if d2 != d: open(p, 'w', encoding='utf-8').write(d2); n += 1
    print('sitemap built; section index added to', n)

if __name__ == '__main__':
    main()
