"""Builds every content page from pages_content.py in one shared template.
render(f, src) returns (body_html, lede) or None when the page has no rewritten content."""
import re, html
from bs4 import BeautifulSoup
import pages_content as PC

def esc(s): return html.escape(s, quote=True)

def banner(spec, note=''):
    if spec:
        src, alt = spec
        return f'<figure class="banner"><img src="{esc(src)}" alt="{esc(alt)}" loading="lazy"><figcaption>{esc(alt)}</figcaption></figure>'
    return f'<figure class="banner ph" aria-label="Picture to come"><span>[{esc(note or "Photo to come")}]</span></figure>'

# ---- data blocks kept from the previous website, rebuilt in the shared card/table style
def trials(src):
    soup = BeautifulSoup(src['body'], 'html.parser')
    out, group, cards = [], None, []
    def flush():
        if cards: out.append(f'<h3>{group}</h3><div class="cards">' + ''.join(cards) + '</div>')
    for el in soup.find_all(['h2', 'h4']):
        if el.name == 'h2':
            flush(); group = el.get_text(strip=True); cards = []; continue
        title = el.get_text(' ', strip=True).title().replace('Mri', 'MRI').replace('Amigo', 'AMIGO').replace('Rqnestin34.5V.2', 'rQNestin34.5v.2').replace('In Situ', 'in Situ').replace(' Of ', ' of ').replace(' For ', ' for ').replace(' In ', ' in ').replace(' And ', ' and ').replace(' With ', ' with ').replace('Pet/Ct', 'PET/CT').replace('(Vats)', '(VATS)')
        p = el.find_next('p'); txt = p.get_text(' ', strip=True) if p else ''
        a = el.find_next('a', href=re.compile('clinicaltrials.gov'))
        link = f'<a class="more" href="{esc(a["href"])}">ClinicalTrials.gov record →</a>' if a and a.find_previous(['h4']) is el else ''
        s1 = re.match(r'(.+?[.!?])(\s|$)', txt); txt = s1.group(1) if s1 else txt
        cards.append(f'<div class="card"><strong>{esc(title)}</strong><span>{esc(txt)}</span>{link}</div>')
    flush()
    return ''.join(out)

def from_transform(src, f, keep):
    import restyle
    body = restyle.transform(src['body'], f)
    soup = BeautifulSoup(body, 'html.parser')
    return ''.join(str(x) for x in soup.select(keep))

def lectures(src): return from_transform(src, 'page-online-lectures.html', 'div.cards')
def seminars(src): return from_transform(src, 'page-seminars.html', 'div.cards')

def trainees(src):
    import restyle
    soup = BeautifulSoup(restyle.transform(src['body'], 'page-trainees.html'), 'html.parser')
    out = []
    for h in soup.find_all(['h2', 'h3']):
        tbl = h.find_next('div', class_='tbl')
        if tbl:
            n = len(tbl.find_all('tr')) - 1
            out.append(f'<h3>{esc(h.get_text(" ", strip=True))} <span class="count">{n}</span></h3>{tbl}')
    return ''.join(out)

def workshops(src, full=False):
    soup = BeautifulSoup(src['body'], 'html.parser'); rows = []; seen = set()
    for h in soup.find_all('h2'):
        t = re.sub(r'\s+', ' ', h.get_text(' ', strip=True))
        m = re.search(r'(\d+)\s*(?:th|st|nd|rd)', t)
        if not m or 'Workshop' not in t or m.group(1) in seen: continue
        seen.add(m.group(1))
        p = h.find_next('p'); txt = p.get_text(' ', strip=True) if p else ''
        yr = re.search(r'(19|20)\d\d', t) or re.search(r'\b(19|20)\d\d\b', txt)
        sents = re.findall(r'[^.!?]+[.!?]', txt)
        summ = ' '.join(sents[:2 if full else 1]).strip()
        rows.append((int(m.group(1)), yr.group(0) if yr else '', summ))
    rows.sort(reverse=True)
    return ('<div class="tbl"><table><thead><tr><th>Edition</th><th>Year</th><th>Summary</th></tr></thead><tbody>' +
            ''.join(f'<tr><td>{n}{"th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")}</td><td>{y}</td><td>{esc(s)}</td></tr>' for n, y, s in rows) + '</tbody></table></div>')

DATA = {'trials': trials, 'lectures': lectures, 'seminars': seminars, 'trainees': trainees,
        'workshops': lambda s: workshops(s), 'workshops_full': lambda s: workshops(s, True)}

def render(f, src):
    p = PC.PAGES.get(f)
    if not p: return None
    parts = [banner(p.get('banner'), p.get('banner_note', ''))]
    parts.append(f'<p class="lead">{p["lead"]}</p>')
    parts.append('<section class="glance"><h2>At a glance</h2><dl>' +
                 ''.join(f'<div><dt>{esc(k)}</dt><dd>{v}</dd></div>' for k, v in p['glance']) + '</dl></section>')
    for h, body in p.get('sections', []):
        parts.append(f'<h2>{esc(h)}</h2>{body}')
    if p.get('data'):
        h, key = p['data']
        if f == 'page-seminars.html' or f == 'page-past-igt-workshops.html' or f == 'page-national-image-guided-therapy-workshops.html':
            pass
        src_page = src
        if key in ('workshops', 'workshops_full') and f != 'page-past-igt-workshops.html':
            import json, os
            db = json.load(open(os.path.join(os.path.dirname(__file__), 'archive_src.json')))
            src_page = db['page-past-igt-workshops.html']
        parts.append(f'<h2>{esc(h)}</h2>' + DATA[key](src_page))
    links = ''.join(f'<a class="card" href="{esc(hh)}"><strong>{esc(t)}</strong></a>' for t, hh in p.get('links', []))
    parts.append(f'<section class="next"><h2>Contact and links</h2><p><strong>Contact:</strong> {p["contact"]}</p>' +
                 (f'<div class="cards">{links}</div>' if links else '') + '</section>')
    return ''.join(parts), ''
