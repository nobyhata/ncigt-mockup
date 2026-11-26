"""Re-lay out the pages carried over from the old ncigt.org (page-*.html, news-*.html,
news.html, sitemap.html) for readability.

First run stores each page's original carried-over content in design/archive_src.json;
later runs always start from that stored source, so the script can be re-run safely.

    python3 design/restyle.py            # all carried-over pages
    python3 design/restyle.py page-x.html   # selected pages
"""
import re, os, sys, json, html, glob, copy
from bs4 import BeautifulSoup, NavigableString, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRCJSON = os.path.join(HERE, 'archive_src.json')
sys.path.insert(0, HERE)
import megamenu
import custom_pages

# ---------------------------------------------------------------- sources
def extract(doc):
    """title, crumb text, date, article html, source url from an original carried-over page"""
    m = re.search(r'<section class="hero-a"><div>(.*?)</div></section><article class="arc">(.*)</article></main>', doc, re.S)
    hero, art = m.group(1), m.group(2)
    title = html.unescape(re.search(r'<h1>(.*?)</h1>', hero, re.S).group(1))
    crumb = re.sub(r'<[^>]+>', '', re.search(r'<p class="crumb"[^>]*>(.*?)</p>', hero, re.S).group(1))
    dm = re.search(r'</h1><p[^>]*>(.*?)</p>', hero, re.S)
    date = dm.group(1) if dm else ''
    sm = re.search(r'<p class="src">Content carried over from <a href="([^"]+)">', art)
    src = sm.group(1) if sm else ''
    art = re.sub(r'<p class="src">.*?</p>\s*$', '', art, flags=re.S)
    return dict(title=title, crumb=html.unescape(crumb), date=date, body=art, src=src)

def load_sources(files):
    db = json.load(open(SRCJSON)) if os.path.exists(SRCJSON) else {}
    for f in files:
        if f in db: continue
        doc = open(os.path.join(ROOT, f), encoding='utf-8').read()
        if 'class="hx"' in doc:
            raise SystemExit(f'{f} is already restyled but has no stored source')
        db[f] = extract(doc)
    json.dump(db, open(SRCJSON, 'w'), ensure_ascii=False, indent=0, sort_keys=True)
    return db

# ---------------------------------------------------------------- where a page sits
OLDMENU = [('About', 'about.html', ['home', 'history', 'team', 'collaborations', 'people']),
 ('Research', 'index.html#research', ['research', 'trd-1-imaging-cancer-heterogeneity', 'trd-2-deep-learning', 'trd-3-intraoperative-devices', 'neurosurgery-core', 'prostate-core', 'guidance-core', 'computation-core', 'robsai', 'fast-imaging-library', 'prostate-image-reporting-and-data-system-pi-rads', 'publications']),
 ('AMIGO', 'clinical.html', ['amigo', 'amigoprocedures', 'clinical-trials', 'brain-tumor-resection', 'breast-cancer-surgery', 'mr-guided-prostate-biopsy', 'mri-guided-cryoablations-of-liver-and-kidney-tumors', 'gynecologic-hdr-brachytherapy', 'parathyroidectomy', 'video-assisted-thoracoscopic-surgeries-ivats', 'acs']),
 ('News & events', 'news.html', ['events', 'national-image-guided-therapy-workshops', 'past-igt-workshops', 'project-week', 'seminars', 'news', 'imri-2024', 'imri-symposium-2022']),
 ('Training', 'index.html#training', ['training-and-dissemination', 'training-in-image-guidance-precision-diagnosis-and-therapy', 'eligibility', 'application', 'trainees', 'visiting-scholars-program', 'online-lectures', 'software-and-tutorials'])]

def place(f):
    """(group label, group landing, note, related [(text, href, note)])"""
    for label, landing, sub, links in megamenu.MENU:
        for t, h, note in links:
            if h.split('#')[0] == f:
                return label, landing, note, [(a, b, c) for a, b, c in links if b.split('#')[0] != f]
    slug = f[5:-5] if f.startswith('page-') else ''
    for label, landing, slugs in OLDMENU:
        if slug in slugs:
            for L, land, sub, links in megamenu.MENU:
                if L == label:
                    return label, landing, '', links
    if f.startswith('news-'):
        for L, land, sub, links in megamenu.MENU:
            if L == 'News & events':
                return 'News & events', 'news.html', '', links
    return '', '', '', []

# ---------------------------------------------------------------- text helpers
SMALL = {'a', 'an', 'and', 'as', 'at', 'by', 'for', 'in', 'of', 'on', 'or', 'the', 'to', 'with', 'from', 'via'}
KEEPUP = {'IGT', 'MRI', 'MR', 'CT', 'PET', 'AMIGO', 'NCIGT', 'AT-NCIGT', 'NIH', 'NIBIB', 'NCI', 'BWH', 'HMS', 'MGB', 'TR&D', 'TRD',
          'T32', 'R25', 'US', 'USA', 'AI', 'AR', 'VR', 'iMRI', 'IVATS', 'iVATS', 'VATS', 'HDR', 'PI-RADS', 'TCIA', 'DICOM', 'FUS',
          'MD', 'PHD', 'PhD', 'II', 'III', 'IV', 'UK', 'MICCAI', 'ISMRM', 'RSNA', 'SPIE', 'ROS', 'ROS-MED', 'QIICR', 'NA-MIC', '3D',
          'MRGFUS', 'LITT', 'CAD', 'DBS', 'IMD', 'IR', 'OR', 'MS', 'COVID-19', 'PSMA', 'IDC', 'LMIC'}
def is_caps(t):
    letters = [c for c in t if c.isalpha()]
    return len(letters) >= 4 and sum(c.isupper() for c in letters) / len(letters) > 0.85

def smart_title(t):
    words = t.split()
    out = []
    for i, w in enumerate(words):
        core = re.sub(r'^[^\w&]+|[^\w&\-]+$', '', w)
        up = core.upper()
        fix = {'PHD': 'PhD', 'IMRI': 'iMRI', 'IVATS': 'iVATS'}
        if up in fix:
            out.append(w.replace(core, fix[up])); continue
        if up in KEEPUP or re.match(r'^[A-Z]?\d', core):
            out.append(w); continue
        lw = w.lower()
        if i and lw.strip('():,') in SMALL:
            out.append(lw)
        else:
            out.append(lw[:1].upper() + lw[1:] if lw else lw)
    return ' '.join(out)

def first_sentence(text, n=170):
    text = re.sub(r'\s+', ' ', text).strip()
    m = re.match(r'(.{40,%d}?[.!?])(\s|$)' % n, text)
    if m: return m.group(1)
    return (text[:n].rsplit(' ', 1)[0] + '…') if len(text) > n else text

# ---------------------------------------------------------------- body transforms
YT = re.compile(r'(youtube\.com|youtu\.be)')
def card_grid(soup, items, cls='cards'):
    g = soup.new_tag('div', attrs={'class': cls})
    for it in items: g.append(it)
    return g

def transform(body, f):
    soup = BeautifulSoup(body, 'html.parser')
    # drop accordion/tab residue
    for i in soup.find_all('i'):
        if not i.get_text(strip=True): i.decompose()
    for h in soup.find_all(['h2', 'h3', 'h4', 'h5']):
        a = h.find('a')
        if a and a.get('href', '').split('#')[-1:] and re.search(r'#[\w-]+$', a.get('href', '')) and h.get_text(strip=True) == a.get_text(strip=True):
            a.unwrap()
    for br in soup.find_all('br'):
        nxt = br.next_sibling
        while isinstance(nxt, NavigableString) and not nxt.strip(): nxt = nxt.next_sibling
        if br.parent is soup and (nxt is None or (isinstance(nxt, Tag) and nxt.name in ('h2', 'h3', 'h4', 'h5', 'table', 'ul', 'ol', 'figure', 'div'))):
            br.decompose()
    # runs of in-page anchor links (old tabs) -> remove; the TOC replaces them
    top_links = [a for a in soup.find_all('a', recursive=False) if re.search(r'#[\w-]+$', a.get('href', '')) and a.get_text(strip=True)]
    if len(top_links) >= 2:
        for a in top_links: a.decompose()
    # empty links pointing outside (e.g. ClinicalTrials.gov buttons)
    for a in soup.find_all('a'):
        if not a.get_text(strip=True) and not a.find('img'):
            h = a.get('href', '')
            if 'clinicaltrials.gov' in h:
                a.string = 'Study record on ClinicalTrials.gov →'; a['class'] = 'more'
            elif h.startswith('http'):
                a.string = 'Learn more →'; a['class'] = 'more'
            else:
                a.decompose()
        elif a.get_text(strip=True).lower() in ('read more', 'read more…', 'read more...'):
            a.string = 'Read more →'; a['class'] = 'more'
    # headings in capitals -> title case; h4/h5 -> h3; strong-only caps paragraphs -> h3
    for h in soup.find_all(['h2', 'h3', 'h4', 'h5']):
        t = h.get_text(' ', strip=True)
        if is_caps(t):
            for s in h.find_all(string=True):
                if s.strip(): s.replace_with(smart_title(str(s)))
        if h.name in ('h4', 'h5'): h.name = 'h3'
    for p in soup.find_all('p'):
        kids = [k for k in p.contents if not (isinstance(k, NavigableString) and not k.strip())]
        if len(kids) == 1 and isinstance(kids[0], Tag) and kids[0].name in ('strong', 'b') and len(kids[0].get_text()) < 90:
            t = kids[0].get_text(' ', strip=True)
            h = soup.new_tag('h3'); h.string = smart_title(t) if is_caps(t) else t
            p.replace_with(h)
    # tables: header row
    for tb in soup.find_all('table'):
        rows = tb.find_all('tr')
        if rows:
            cells = rows[0].find_all(['td', 'th'])
            if cells and all((c.find(['strong', 'b']) and c.get_text(strip=True) == c.find(['strong', 'b']).get_text(strip=True)) or not c.get_text(strip=True) for c in cells):
                for c in cells:
                    c.name = 'th'
                    for s in c.find_all(['strong', 'b']): s.unwrap()
                thead = soup.new_tag('thead'); rows[0].extract(); thead.append(rows[0]); tb.insert(0, thead)
        # drop columns that are empty in every row
        allrows = tb.find_all('tr')
        if allrows:
            ncol = max(len(r.find_all(['td', 'th'])) for r in allrows)
            for ci in reversed(range(ncol)):
                col = [r.find_all(['td', 'th'])[ci] for r in allrows if len(r.find_all(['td', 'th'])) > ci]
                body_cells = [c for c in col if c.name == 'td']
                if body_cells and not any(c.get_text(strip=True) for c in body_cells):
                    for c in col: c.decompose()
        wrap = soup.new_tag('div', attrs={'class': 'tbl'}); tb.wrap(wrap)
    # nested <article> lists (old post loops) -> cards
    for art in soup.find_all('article'):
        a = art.find('header').find('a') if art.find('header') else art.find('a')
        if not a: continue
        title = a.get_text(' ', strip=True); href = a.get('href', '')
        date = ''
        first = art.contents[0] if art.contents else None
        if isinstance(first, NavigableString): date = first.strip()
        dm = re.match(r'(\d{2})(\w{3}) (\d{2})', date)
        date = f'{dm.group(2)} {int(dm.group(1))}, 20{dm.group(3)}' if dm else date
        p = art.find('p'); ex = first_sentence(p.get_text(' ', strip=True), 200) if p else ''
        c = BeautifulSoup(f'<a class="card" href="{html.escape(href)}"><span class="kicker">{html.escape(date)}</span><strong>{html.escape(title)}</strong><span>{html.escape(ex)}</span></a>', 'html.parser')
        art.replace_with(c)
    runs = []
    for c in soup.find_all('a', class_='card'):
        if runs and c.previous_sibling is runs[-1][-1] or (runs and isinstance(c.previous_sibling, NavigableString) and not c.previous_sibling.strip() and c.previous_sibling.previous_sibling is runs[-1][-1]):
            runs[-1].append(c)
        else: runs.append([c])
    for r in runs:
        g = soup.new_tag('div', attrs={'class': 'cards'}); r[0].insert_before(g)
        for c in r: g.append(c.extract())
    # figure followed by a caption text node (online lectures) -> card grid
    figs = soup.find_all('figure', recursive=False)
    if len(figs) >= 3:
        items = []
        for fg in figs:
            cap = fg.next_sibling
            captxt = cap.strip() if isinstance(cap, NavigableString) else ''
            a = fg.find('a'); img = fg.find('img')
            href = a.get('href', '') if a else ''
            kind = 'Watch' if YT.search(href) else ('Slides' if href.endswith('.pdf') else 'Open')
            src = img.get('src', '') if img else ''
            name, _, rest = captxt.partition(':')
            items.append((fg, cap if captxt else None,
                f'<a class="card media" href="{html.escape(href)}"><img src="{html.escape(src)}" alt="" loading="lazy"><span class="kicker">{kind}</span><strong>{html.escape(name.strip() or captxt)}</strong><span>{html.escape(rest.strip())}</span></a>'))
        g = BeautifulSoup('<div class="cards three">' + ''.join(i[2] for i in items) + '</div>', 'html.parser')
        figs[0].insert_before(g)
        for fg, cap, _ in items:
            if cap is not None: cap.extract()
            fg.decompose()
    # images: runs of 2+ consecutive -> gallery; lone image inside text -> small float
    def is_img_node(n):
        if isinstance(n, NavigableString): return not n.strip()
        if n.name == 'img': return True
        if n.name in ('a', 'figure', 'p') and n.find('img') and not n.get_text(strip=True) and len(n.find_all('img')) == 1: return True
        return False
    def gather(parent):
        kids = list(parent.children); i = 0
        while i < len(kids):
            if isinstance(kids[i], Tag) and is_img_node(kids[i]):
                j = i; run = []
                while j < len(kids) and is_img_node(kids[j]):
                    if isinstance(kids[j], Tag): run.append(kids[j])
                    j += 1
                if len(run) >= 2:
                    seen = set(); g = soup.new_tag('div', attrs={'class': 'gallery'})
                    run[0].insert_before(g)
                    for r in run:
                        im = r if r.name == 'img' else r.find('img')
                        key = im.get('src')
                        r.extract()
                        if key in seen: continue
                        seen.add(key)
                        if r.name == 'img':
                            a = soup.new_tag('a', href=key); a.append(r); r = a
                        g.append(r)
                    kids = list(parent.children); i = kids.index(g) + 1; continue
                i = j
            else: i += 1
    gather(soup)
    for p in soup.find_all('p'):
        imgs = p.find_all('img', recursive=True)
        if len(imgs) == 1 and p.get_text(strip=True):
            im = imgs[0]
            w = int(im.get('width') or 0)
            im['class'] = 'side'
    # lone big images at top level -> figure
    for im in soup.find_all('img'):
        if im.find_parent(class_=['gallery', 'card']) or im.get('class') == ['side'] or 'side' in (im.get('class') or []): continue
        if not im.find_parent('figure'):
            fg = soup.new_tag('figure'); (im.parent if im.parent.name == 'a' else im).wrap(fg)
    # multiple consecutive videos -> 2 column grid
    vids = soup.find_all('div', class_='vid')
    for v in vids:
        if v.parent and 'vgrid' in (v.parent.get('class') or []): continue
        run = [v]; n = v.next_sibling
        while n is not None and ((isinstance(n, NavigableString) and not n.strip()) or (isinstance(n, Tag) and 'vid' in (n.get('class') or []))):
            if isinstance(n, Tag): run.append(n)
            n = n.next_sibling
        if len(run) >= 2:
            g = soup.new_tag('div', attrs={'class': 'vgrid'}); v.insert_before(g)
            for r in run: g.append(r.extract())
    for a in soup.find_all('a', class_='more'):
        n = a.next_sibling
        while isinstance(n, NavigableString) and not n.strip(): n = n.next_sibling
        while isinstance(n, Tag) and n.name == 'a' and 'more' in (n.get('class') or []) and n.get_text() == a.get_text():
            nn = n.next_sibling; n.decompose(); n = nn
            while isinstance(n, NavigableString) and not n.strip(): n = n.next_sibling
    out = str(soup)
    out = re.sub(r'(<br/?>\s*){2,}', '<br/>', out)
    out = re.sub(r'\n{3,}', '\n\n', out)
    return out

def add_ids(body):
    soup = BeautifulSoup(body, 'html.parser'); toc = []; used = set()
    for h in soup.find_all(['h2']):
        t = h.get_text(' ', strip=True)
        if not t: continue
        hid = h.get('id') or re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:48] or 'section'
        base = hid; k = 2
        while hid in used: hid = f'{base}-{k}'; k += 1
        used.add(hid); h['id'] = hid; toc.append((t, hid))
    return str(soup), toc

# ---------------------------------------------------------------- page shell
CSS = '''<style id="arc2">
.hx{background:#0F1B2D;color:#fff}.hx .w{max-width:1160px;margin:0 auto;padding:40px 24px 36px}
.hx .crumb{margin:0 0 12px;font-size:14px;font-weight:600;color:#D9B98F}.hx .crumb a{color:#D9B98F}.hx .crumb span{opacity:.6;margin:0 8px}
.hx h1{margin:0;font-size:38px;line-height:1.18;color:#fff;max-width:900px}
.hx .lede{margin:12px 0 0;font-size:18px;line-height:1.55;color:#C9D3E0;max-width:820px}
.hx .meta{margin:14px 0 0;display:flex;flex-wrap:wrap;gap:8px}.hx .chip{background:#1A2A42;color:#D9B98F;border-radius:999px;padding:4px 12px;font-size:13px;font-weight:600}
.lay{max-width:1160px;margin:0 auto;padding:40px 24px 24px;display:grid;grid-template-columns:220px minmax(0,1fr);gap:48px;align-items:start}
.lay.one{grid-template-columns:minmax(0,1fr)}
.toc{position:sticky;top:20px;font-size:14px;border-left:3px solid #E3E8EF;padding:4px 0 4px 16px}
.toc strong{display:block;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#8A5A2B;margin-bottom:8px}
.toc a{display:block;color:#3A4658;padding:5px 0;line-height:1.35}.toc a:hover{color:#0B5F86}
.arc{max-width:780px;font-size:17px;line-height:1.72;color:#1F2B3D;min-width:0}
.lay.one .arc{max-width:820px;margin:0 auto}
.arc>p:first-child,.arc>.lead{font-size:19px;line-height:1.65;color:#0F1B2D}
.arc h2{font-size:27px;margin:44px 0 14px;line-height:1.25;padding-top:8px;scroll-margin-top:16px}
.arc h2:first-child,.arc>*:first-child{margin-top:0}
.arc h3{font-size:20px;margin:30px 0 8px;line-height:1.35}
.arc p{margin:0 0 16px}.arc ul,.arc ol{padding-left:22px;margin:0 0 18px}.arc li{margin:4px 0}
.arc figure{margin:20px 0}.arc figure img,.arc>img{width:100%;height:auto;max-height:460px;object-fit:cover;border-radius:12px;display:block}
.arc img.side{float:right;width:200px;max-width:40%;height:auto;margin:4px 0 12px 24px;border-radius:10px}
.arc::after{content:"";display:block;clear:both}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;margin:20px 0}
.gallery a{display:block}.gallery img{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;border-radius:10px;display:block;margin:0}
.tbl{overflow-x:auto;margin:16px 0 24px;border:1px solid #E3E8EF;border-radius:12px}
.arc table{border-collapse:collapse;width:100%;font-size:15px;line-height:1.45}
.arc th{background:#F3F6FA;text-align:left;font-weight:600;color:#0F1B2D;padding:10px 14px;border-bottom:1px solid #E3E8EF;white-space:nowrap}
.arc td{padding:9px 14px;border-bottom:1px solid #EEF1F5;vertical-align:top}.arc tr:last-child td{border-bottom:0}
.arc tbody tr:nth-child(even) td{background:#FAFBFD}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;margin:18px 0 28px}
.cards.three{grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}
.card{display:flex;flex-direction:column;gap:6px;border:1px solid #E3E8EF;border-radius:12px;padding:16px 18px;color:#0F1B2D;text-decoration:none;line-height:1.45;background:#fff}
.card:hover{border-color:#0B5F86;box-shadow:0 6px 18px rgba(15,27,45,.08);text-decoration:none}
.card strong{font-family:'Source Serif 4',Georgia,serif;font-size:17px;line-height:1.3}
.card span{font-size:14px;color:#4A5668}.card .kicker{font-size:12px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:#8A5A2B}
.card.media{padding:0 0 14px;overflow:hidden}.card.media img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;margin:0 0 6px;border-radius:0}
.card.media .kicker,.card.media strong,.card.media span{padding:0 16px}
.arc a.more{display:inline-block;font-weight:600;font-size:15px;margin:0 0 18px}
.arc .vid{position:relative;aspect-ratio:16/9;margin:20px 0}.arc .vid iframe{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:12px}
.vgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;margin:20px 0}.vgrid .vid{margin:0}
.arc blockquote{border-left:4px solid #A8763E;margin:16px 0;padding:4px 16px;color:#3A4658}
.box{background:#F3F6FA;border-radius:14px;padding:20px 22px;margin:20px 0}
.src{margin-top:40px;padding-top:14px;border-top:1px solid #E3E8EF;font-size:13px;color:#6B778A}
.rel{max-width:1160px;margin:0 auto;padding:8px 24px 64px}.rel .in{border-top:1px solid #E3E8EF;padding-top:28px}
.rel h2{font-size:20px;margin:0 0 14px}.rel .cards{margin:0}
@media (max-width:900px){.lay{grid-template-columns:minmax(0,1fr);gap:20px}.toc{position:static;border-left:0;padding:0;display:flex;flex-wrap:wrap;gap:6px 14px}.toc strong{width:100%}.hx h1{font-size:30px}.arc img.side{float:none;width:100%;max-width:100%;margin:12px 0}}
</style>
'''

def shell_parts(doc):
    head = doc[:doc.index('<main id="main">')]
    foot = doc[doc.index('</main>') + len('</main>'):]
    head = re.sub(r'<style>\n?\.arc\{max-width:900px.*?</style>', '', head, flags=re.S)
    head = re.sub(r'<style id="arc2">.*?</style>\n?', '', head, flags=re.S)
    head = head.replace('</head>', CSS + '</head>', 1)
    return head, foot

def build(f, s):
    label, landing, note, related = place(f)
    is_news = f.startswith('news-')
    custom = custom_pages.render(f, s)
    if custom:
        body, lede = custom
    else:
        body = transform(s['body'], f); lede = note
    body, toc = add_ids(body)
    if not lede and not is_news:
        txt = BeautifulSoup(body, 'html.parser').find('p')
        lede = ''
    title = s['title']
    if is_caps(title): title = smart_title(title)
    crumbs = ['<a href="index.html">Home</a>']
    if is_news:
        crumbs.append('<a href="news.html">News and seminars</a>')
    elif label:
        crumbs.append(f'<a href="{landing}">{html.escape(label)}</a>')
    meta = ''
    if is_news:
        chips = []
        if s['date'] and s['date'] > '1990':
            y, mo, d = s['date'][:10].split('-')
            months = 'January February March April May June July August September October November December'.split()
            chips.append(f'{months[int(mo)-1]} {int(d)}, {y}')
        cat = s['crumb'].split('·')[-1].strip()
        if cat and cat.lower() != 'news and seminars': chips.extend(smart_title(c.strip()) for c in cat.split(',') if c.strip())
        meta = '<div class="meta">' + ''.join(f'<span class="chip">{html.escape(c)}</span>' for c in chips) + '</div>'
    hero = (f'<section class="hx"><div class="w"><p class="crumb">' + '<span>›</span>'.join(crumbs) + '</p>'
            f'<h1>{html.escape(title)}</h1>' + (f'<p class="lede">{html.escape(lede)}</p>' if lede else '') + meta + '</div></section>')
    use_toc = len(toc) >= 3 and not is_news
    tochtml = ('<nav class="toc" aria-label="On this page"><strong>On this page</strong>' + ''.join(f'<a href="#{i}">{html.escape(t)}</a>' for t, i in toc) + '</nav>') if use_toc else ''
    src = f'<p class="src">Carried over from the previous NCIGT website: <a href="{s["src"]}">{s["src"]}</a></p>' if s['src'] else ''
    lay = f'<div class="lay{"" if use_toc else " one"}">{tochtml}<article class="arc">{body}{src}</article></div>'
    rel = ''
    if is_news:
        rel_items = [('All news and seminars', 'news.html', 'Every item, newest first'), ('Research seminars', 'page-seminars.html', 'The Ferenc Jolesz Research Seminar Series'), ('Events', 'page-events.html', 'Meetings and workshops')]
        heading = 'More news'
    else:
        rel_items = related; heading = f'More in {label}' if label else ''
    if rel_items and heading:
        rel = ('<section class="rel"><div class="in"><h2>' + html.escape(heading) + '</h2><div class="cards">' +
               ''.join(f'<a class="card" href="{h}"><strong>{html.escape(t)}</strong>' + (f'<span>{html.escape(n)}</span>' if n else '') + '</a>' for t, h, n in rel_items[:6]) +
               '</div></div></section>')
    return f'<main id="main">{hero}{lay}{rel}</main>'

def main(argv):
    files = argv or sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, 'page-*.html')) + glob.glob(os.path.join(ROOT, 'news-*.html'))) + ['news.html', 'sitemap.html']
    db = load_sources(files)
    for f in files:
        path = os.path.join(ROOT, f)
        doc = open(path, encoding='utf-8').read()
        head, foot = shell_parts(doc)
        page = head + build(f, db[f]) + foot
        if is_caps(db[f]['title']):
            page = re.sub(r'<title>.*?·', f'<title>{html.escape(smart_title(db[f]["title"]))} ·', page, count=1)
        open(path, 'w', encoding='utf-8').write(page)
    print('restyled', len(files))

if __name__ == '__main__':
    main(sys.argv[1:])
