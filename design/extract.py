import json,glob,re,html,os
from bs4 import BeautifulSoup, Comment
C='/home/claude/crawl/'
pages=json.load(open(C+'pages-1.json')); posts=sum([json.load(open(f)) for f in sorted(glob.glob(C+'posts-*.json'))],[])
cats={c['id']:html.unescape(c['name']) for c in json.load(open(C+'categories-1.json'))}
items=[]
for kind,lst in (('page',pages),('post',posts)):
    for p in lst:
        s=open(f"{C}live/{kind}-{p['id']}.html",errors='ignore').read()
        soup=BeautifulSoup(s,'html.parser')
        node=soup.select_one('.single-page-content' if kind=='page' else '.single-blog-content') or soup.select_one('main')
        title=html.unescape(p['title']['rendered'])
        if kind=='post':
            h=soup.select_one('.single-post-title'); title=h.get_text(' ',strip=True) if h else title
            fm=soup.select_one('.single-blog-media img, .single-media img')
            feat=fm.get('src') if fm else None
        else: feat=None
        for t in node.find_all(['style','script','noscript','form','iframe']):
            if t.name=='iframe' and 'youtube' in (t.get('src') or ''):
                vid=re.search(r'embed/([\w-]{11})',t['src']).group(1)
                nt=soup.new_tag('div'); nt['class']='yt'; nt['data-id']=vid; nt['data-title']=t.get('title','Video'); t.replace_with(nt); continue
            t.decompose()
        for c in node.find_all(string=lambda x:isinstance(x,Comment)): c.extract()
        items.append(dict(kind=kind,id=p['id'],slug=p['slug'],link=p['link'],title=title,date=p['date'][:10],
            cats=[cats.get(c) for c in p.get('categories',[])],parent=p.get('parent',0),feat=feat,html=str(node)))
json.dump(items,open(C+'items.json','w'))
imgs=set()
for it in items:
    for u in re.findall(r'(?:src|href|srcset)="([^"]+)"',it['html']):
        for v in u.split(','):
            v=v.strip().split(' ')[0]
            if 'ncigt.org/wp-content/uploads/' in v: imgs.add(v)
    if it['feat']: imgs.add(it['feat'])
open(C+'assets.txt','w').write('\n'.join(sorted(imgs)))
from collections import Counter
print(len(items),len(imgs),Counter(os.path.splitext(i)[1].lower() for i in imgs))
