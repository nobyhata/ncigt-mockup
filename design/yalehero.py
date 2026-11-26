"""Yale-style page tops: a light title area, and where the page has a banner
photo, the photo runs full width with the title on a white card over it."""
import re, glob, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CSS = ('<style id="yh-css">'
 '.hx{background:#FFFFFF;color:#0F1B2D;border-bottom:1px solid #E3E8EF}'
 '.hx .w{padding:36px 24px 28px}'
 '.hx .crumb,.hx .crumb a{color:#0B5F86;font-size:12px;letter-spacing:1.5px;text-transform:uppercase}'
 '.hx h1{color:#0F1B2D;font-family:"Source Serif 4",Georgia,serif;font-weight:500;font-size:44px}'
 '.hx .lede{color:#3A4658}.hx .chip{background:#EEF3F8;color:#0B5F86}'
 '.hx.yh{position:relative;border:0;padding:0;background:#FFFFFF}'
 '.hx.yh .yh-img{display:block;width:100%;height:clamp(260px,42vw,520px);object-fit:cover}'
 '.hx.yh .w{position:relative;max-width:1160px;margin:-120px auto 0;padding:0 24px}'
 '.hx.yh .yh-card{background:#FFFFFF;max-width:720px;padding:28px 32px 26px;box-shadow:0 10px 30px rgba(15,27,45,.12)}'
 '.hx.yh + .lay{padding-top:32px}'
 '@media (max-width:760px){.hx h1{font-size:32px}.hx.yh .w{margin-top:-60px;padding:0 12px}.hx.yh .yh-card{padding:20px}}'
 '</style>')
n = m = 0
for f in glob.glob(os.path.join(ROOT, '*.html')):
    s = open(f, encoding='utf-8').read()
    if '<section class="hx">' not in s: continue
    s = re.sub(r'<style id="yh-css">.*?</style>', '', s, flags=re.S)
    fig = re.search(r'<figure class="banner"><img([^>]*)/?>(?:<figcaption>.*?</figcaption>)?</figure>', s, re.S)
    if fig:
        img = fig.group(1)
        src = re.search(r'src="([^"]+)"', img).group(1)
        alt = re.search(r'alt="([^"]*)"', img); alt = alt.group(1) if alt else ''
        s = s.replace(fig.group(0), '', 1)
        s = re.sub(r'<section class="hx"><div class="w">(.*?)</div></section>',
                   lambda mm: f'<section class="hx yh"><img class="yh-img" src="{src}" alt="{alt}"><div class="w"><div class="yh-card">{mm.group(1)}</div></div></section>',
                   s, count=1, flags=re.S)
        m += 1
    s = s.replace('</head>', CSS + '</head>', 1)
    open(f, 'w', encoding='utf-8').write(s); n += 1
print('page tops restyled on', n, 'pages;', m, 'with a full-width photo')
