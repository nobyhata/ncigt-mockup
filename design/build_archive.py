import json,re,os,html,shutil
from bs4 import BeautifulSoup
from PIL import Image
C='/home/claude/crawl/'; S='/home/claude/site/'; M=S+'media/'
os.makedirs(M,exist_ok=True)
items=json.load(open(C+'items.json'))
def aname(u):
    u=u.split('?')[0].replace('http://','https://'); u=re.sub(r'-\d+x\d+(\.\w+)$',r'\1',u)
    return u.split('/wp-content/uploads/')[-1].replace('/','_')
done={}
def media(u):
    n=aname(u)
    if n in done: return done[n]
    src=C+'assets/'+n
    if not os.path.exists(src): done[n]=None; return None
    ext=os.path.splitext(n)[1].lower(); out=n
    if ext in ('.jpg','.jpeg','.png','.webp'):
        try:
            im=Image.open(src); im.load()
            if max(im.size)>1600: im.thumbnail((1600,1600))
            if ext=='.png' and im.mode in ('RGBA','LA','P') :
                im.save(M+out,optimize=True)
            else:
                out=os.path.splitext(n)[0]+'.jpg'; im.convert('RGB').save(M+out,quality=82,optimize=True)
        except Exception as e: shutil.copy(src,M+out)
    else: shutil.copy(src,M+out)
    done[n]='media/'+out; return done[n]
slug2={}
for it in items: slug2[it['slug']]=('page-' if it['kind']=='page' else 'news-')+it['slug']+'.html'
slug2['home']='index.html'
def local(href):
    if not href: return href
    h=href.replace('http://','https://')
    if '/wp-content/uploads/' in h: return media(h) or href
    m=re.match(r'https://(?:www\.)?ncigt\.org/?([^?#]*)(#.*)?$',h)
    if m:
        segs=[x for x in m.group(1).split('/') if x]
        anc=m.group(2) or ''
        if not segs: return 'index.html'
        if segs[-1] in slug2: return slug2[segs[-1]]+anc
        return href
    return href
KEEP={'a':['href','title'],'img':['src','alt','width','height'],'td':['colspan','rowspan'],'th':['colspan','rowspan'],'div':[]}
def clean(h):
    soup=BeautifulSoup(h,'html.parser')
    for y in soup.select('div.yt'):
        v,t=y['data-id'],y.get('data-title','Video')
        y.replace_with(BeautifulSoup(f'<div class="vid"><iframe src="https://www.youtube-nocookie.com/embed/{v}" title="{html.escape(t)}" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>','html.parser'))
    for t in soup.find_all(True):
        if t.name in('iframe',) : continue
        if t.name=='img':
            src=t.get('data-src') or t.get('src') or ''
            if t.get('srcset') and not src: src=t['srcset'].split(',')[-1].strip().split(' ')[0]
            t['src']=local(src); t['loading']='lazy'
        if t.name=='a': t['href']=local(t.get('href',''))
        keep=KEEP.get(t.name,[])
        if t.name=='div' and 'vid' in (t.get('class') or []): continue
        for a in list(t.attrs):
            if a not in keep and not (t.name=='img' and a=='loading'): del t[a]
    for t in soup.find_all(['div','span','section','font','center']):
        if t.name=='div' and t.get('class')==['vid']: continue
        t.unwrap()
    for t in soup.find_all(['p','li','h1','h2','h3','h4','h5']):
        if not t.get_text(strip=True) and not t.find(['img','iframe']): t.decompose()
    for t in soup.find_all('h1'): t.name='h2'
    out=str(soup)
    out=re.sub(r'(<br/?>\s*){3,}','<br><br>',out)
    return out
shell=open(S+'people.html').read()
head=shell[:shell.find('</header>')+9]; foot=shell[shell.find('<footer'):]
css='''<style>
.arc{max-width:900px;margin:0 auto;padding:48px 24px 80px;font-size:17px;line-height:1.7;color:#1F2B3D}
.arc h2{font-size:26px;margin:40px 0 12px;line-height:1.3}.arc h3{font-size:21px;margin:32px 0 10px}.arc h4,.arc h5{font-size:18px;margin:24px 0 8px}
.arc img{max-width:100%;height:auto;border-radius:10px;margin:12px 0;display:block}
.arc table{border-collapse:collapse;width:100%;font-size:15px;margin:16px 0;display:block;overflow-x:auto}.arc td,.arc th{border:1px solid #E3E8EF;padding:8px 10px;vertical-align:top}
.arc .vid{position:relative;aspect-ratio:16/9;margin:20px 0}.arc .vid iframe{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:12px}
.arc ul,.arc ol{padding-left:24px}.arc blockquote{border-left:4px solid #A8763E;margin:16px 0;padding:4px 16px;color:#3A4658}
.crumb{font-size:14px;color:#4A5668;margin-bottom:8px}.src{margin-top:48px;padding-top:16px;border-top:1px solid #E3E8EF;font-size:14px;color:#4A5668}
.hero-a{background:#0F1B2D;color:#fff}.hero-a div{max-width:900px;margin:0 auto;padding:48px 24px 36px}.hero-a h1{margin:0;font-size:36px;line-height:1.2;color:#fff}
</style>'''
head=head.replace('</head>',css+'</head>',1)
def page(title,crumb,body,desc,src=None,date=None):
    h=re.sub(r'<title>.*?</title>',f'<title>{html.escape(title)} · AT-NCIGT (draft)</title>',head,1)
    h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{html.escape(desc)}">',h,1)
    d=f'<p style="margin:10px 0 0;color:#C9D3E0;font-size:15px">{date}</p>' if date else ''
    s=f'<p class="src">Content carried over from <a href="{src}">{src}</a>.</p>' if src else ''
    return h+f'<main id="main"><section class="hero-a"><div><p class="crumb" style="color:#D9B98F">{crumb}</p><h1>{html.escape(title)}</h1>{d}</div></section><article class="arc">{body}{s}</article></main>\n'+foot
cap=lambda t:t if not t.isupper() else t.title().replace('And','and').replace('Of','of').replace('At','at').replace('Igt','IGT').replace('Trd','TR&D').replace('Imri','iMRI').replace('Amigo','AMIGO')
for it in items:
    body=clean(it['html'])
    if it['kind']=='post':
        if it['feat'] and media(it['feat']) and media(it['feat']) not in body: body=f'<img src="{media(it["feat"])}" alt="">'+body
        crumb='<a href="news.html" style="color:#D9B98F">News and seminars</a> · '+', '.join(c for c in it['cats'] if c)
        html_=page(it['title'],crumb,body,it['title'],it['link'],it['date'])
    else:
        html_=page(cap(it['title']),'<a href="sitemap.html" style="color:#D9B98F">All pages</a>',body,cap(it['title']),it['link'])
    if it['slug']=='home': fn='page-home.html'
    else: fn=slug2[it['slug']]
    open(S+fn,'w').write(html_)
json.dump({k:v for k,v in done.items() if v},open(C+'mediamap.json','w'))
# news index
posts=sorted([i for i in items if i['kind']=='post'],key=lambda i:i['date'],reverse=True)
groups={}
for p in posts:
    g='Seminars' if any(c and 'Seminar' in c for c in p['cats']) else 'News'
    groups.setdefault(g,[]).append(p)
b=''
for g in ('News','Seminars'):
    b+=f'<h2 id="{g.lower()}">{g} ({len(groups.get(g,[]))})</h2><ul>'
    for p in groups.get(g,[]):
        y=p['date'][:4] if p['date']>'1990' else ''
        b+=f'<li><a href="{slug2[p["slug"]]}">{html.escape(p["title"])}</a> <span style="color:#6B778A;font-size:14px">{y}</span></li>'
    b+='</ul>'
open(S+'news.html','w').write(page('News and seminars','<a href="sitemap.html" style="color:#D9B98F">All pages</a>',f'<p>Every news item and seminar posted on ncigt.org, newest first. <a href="#seminars">Jump to seminars</a>.</p>'+b,'News and seminars of AT-NCIGT'))
# sitemap following the old menu
menu=[('About',['home','history','team','collaborations','people']),('Research',['research','trd-1-imaging-cancer-heterogeneity','trd-2-deep-learning','trd-3-intraoperative-devices','neurosurgery-core','prostate-core','guidance-core','computation-core','robsai','fast-imaging-library','prostate-image-reporting-and-data-system-pi-rads']),
 ('AMIGO and clinical research',['amigo','amigoprocedures','clinical-trials','brain-tumor-resection','breast-cancer-surgery','mr-guided-prostate-biopsy','mri-guided-cryoablations-of-liver-and-kidney-tumors','gynecologic-hdr-brachytherapy','parathyroidectomy','video-assisted-thoracoscopic-surgeries-ivats','acs']),
 ('Events',['events','national-image-guided-therapy-workshops','past-igt-workshops','project-week','seminars','news','imri-2024','imri-symposium-2022']),
 ('Training and dissemination',['training-and-dissemination','training-in-image-guidance-precision-diagnosis-and-therapy','eligibility','application','trainees','visiting-scholars-program','online-lectures','software-and-tutorials']),('Publications',['publications'])]
byslug={i['slug']:i for i in items if i['kind']=='page'}
used=set(); b='<p>Every page from ncigt.org, carried over into the new design. News items and seminars are on <a href="news.html">News and seminars</a>.</p>'
for g,sl in menu:
    b+=f'<h2>{g}</h2><ul>'
    for s_ in sl:
        if s_ in byslug: used.add(s_); b+=f'<li><a href="{"page-home.html" if s_=="home" else slug2[s_]}">{html.escape(cap(byslug[s_]["title"]))}</a></li>'
    b+='</ul>'
rest=[s_ for s_ in byslug if s_ not in used]
if rest:
    b+='<h2>Other pages</h2><ul>'+''.join(f'<li><a href="{slug2[s_]}">{html.escape(cap(byslug[s_]["title"]))}</a></li>' for s_ in rest)+'</ul>'
b+=f'<h2>News and seminars</h2><ul><li><a href="news.html">All {len(posts)} news items and seminars</a></li></ul>'
open(S+'sitemap.html','w').write(page('All pages','<a href="index.html" style="color:#D9B98F">Home</a>',b,'All pages of AT-NCIGT'))
print('items',len(items),'media',len([v for v in done.values() if v]),'rest',rest)
