import json,re
NAV='''<nav aria-label="Main" style="display: flex; flex-wrap: wrap; gap: 4px 20px; font-size: 15px; font-weight: 500">
<a href="Main.dc.html#research" style="color: #0F1B2D">Research</a>
<a href="People.dc.html" style="color: #0F1B2D">People</a>
<a href="Main.dc.html#clinical" style="color: #0F1B2D">AMIGO</a>
<a href="Publications.dc.html" style="color: #0F1B2D">Publications</a>
<a href="Main.dc.html#resources" style="color: #0F1B2D">Resources</a>
<a href="Main.dc.html#training" style="color: #0F1B2D">Training</a>
<a href="Industry.dc.html" style="color: #0F1B2D">Industry</a>
<a href="Main.dc.html#partner" style="color: #0F1B2D">Partner with us</a>
<a href="news.html" style="color: #0F1B2D">News</a>
<a href="Main.dc.html#about" style="color: #0F1B2D">About</a>
</nav>'''
open('/home/claude/build/nav.html','w').write(NAV)
P='portraits/'
def card(name, role, focus='', photo='', link='', linktext=''):
    return {'name':name,'role':role,'focus':focus,'photo':P+photo+'.jpg' if photo else '','nophoto':not photo,'link':link,'linktext':linktext,'haslink':bool(link)}
leaders=[card('Clare M. Tempany','Contact PI · Administration Core','Prostate MRI and image-guided therapy','clare-m-tempany'),card('Nobuhiko Hata','Multiple PI · Administration Core','Robotic navigation and image-guided interventions','nobuhiko-hata')]
current=[card('Stephan E. Maier','TR&D 1 lead','Quantitative diffusion MRI','stephan-e-maier','TRD1.dc.html','TR&D 1'),
card('Carl-Fredrik Westin','TR&D 1 · Training and Dissemination lead','Diffusion MRI methods','carl-fredrik-westin','TRD1.dc.html','TR&D 1'),
card('William M. Wells III','TR&D 1 co-investigator','Image registration and multimodal learning','william-m-wells-iii','TRD1.dc.html','TR&D 1'),
card('Daniel Paech','TR&D 1 investigator','Quantitative CEST MRI of tumor chemistry','daniel-paech','TRD1.dc.html','TR&D 1'),
card('Oliver Jonas','TR&D 2 lead','Implantable microdevices','oliver-jonas','TRD2.dc.html','TR&D 2'),
card('Sharath Bhagavatula','TR&D 2 investigator','Interventional radiology','sharath-bhagavatula','TRD2.dc.html','TR&D 2'),
card('[First name] Akgul','TR&D 2 co-investigator','[Research focus]','','TRD2.dc.html','TR&D 2'),
card('Junichi Tokuda','TR&D 3 lead','MRI-guided robotic interventions','junichi-tokuda','TRD3.dc.html','TR&D 3'),
card('Jagadeesan Jayender','TR&D 3 investigator','Surgical navigation and computer vision','jagadeesan-jayender','TRD3.dc.html','TR&D 3'),
card('Haoyin Zhou','TR&D 3 co-investigator','Trackerless navigation for minimally invasive surgery','haoyin-zhou','TRD3.dc.html','TR&D 3')]
past=[card(n,'Investigator, 2021–2026 cycle',f,p) for n,f,p in [('Nathalie Y. R. Agar','Mass spectrometry imaging (TRD 1 lead)','nathalie-y-r-agar'),('Tina Kapur','Training and Dissemination (core lead)','tina-kapur'),('Alexandra J. Golby','Image-guided neurosurgery; AMIGO clinical director','alexandra-j-golby'),('Sarah F. Frisken','Image analysis for brain tumor surgery','sarah-f-frisken'),('Ron Kikinis','Open-source medical image computing','ron-kikinis'),("Lauren J. O\u2019Donnell",'Diffusion MRI tractography','lauren-j-odonnell'),('Fiona M. Fennessy','Quantitative prostate MRI','fiona-m-fennessy'),('Kemal Tuncali','MRI-guided interventions','kemal-tuncali')]]
inv=[('Oliver Jonas','Implantable microdevices for measuring drug response','oliver-jonas','TRD2'),
("Lauren J. O’Donnell",'Diffusion MRI tractography and white-matter analysis','lauren-j-odonnell',''),
('Nobuhiko Hata','Robotic navigation for bronchoscopy and prostate interventions','nobuhiko-hata','TRD3'),
('Junichi Tokuda','MRI-guided robotic prostate interventions','junichi-tokuda','TRD3'),
('Jagadeesan Jayender','Surgical navigation and computer vision','jagadeesan-jayender','TRD3'),
('Stephan E. Maier','Quantitative diffusion MRI','stephan-e-maier','TRD1'),
('Fiona M. Fennessy','Quantitative prostate MRI','fiona-m-fennessy','TRD1'),
('Sarah F. Frisken','Image analysis for brain tumor surgery','sarah-f-frisken',''),
('Nathalie Y. R. Agar','Mass spectrometry imaging','nathalie-y-r-agar','TRD2'),
('Clare M. Tempany','Prostate MRI and image-guided therapy','clare-m-tempany','TRD1'),
('Alexandra J. Golby','Image-guided neurosurgery','alexandra-j-golby',''),
('Ron Kikinis','Open-source medical image computing','ron-kikinis',''),
('Tina Kapur','Neurosurgical imaging data and machine learning','tina-kapur',''),
('William M. Wells III','Image registration and multimodal learning','william-m-wells-iii',''),
('Carl-Fredrik Westin','Diffusion MRI methods','carl-fredrik-westin','TRD1'),
('Pedro Moreira','Image-guided prostate cryoablation and robotics','pedro-moreira','TRD3')]
investigators=[card(n,'Investigator',f,p,(t+'.dc.html') if t else '',('TR&D '+t[-1]) if t else '') for n,f,p,t in inv]
clin=[('Kemal Tuncali','MRI-guided interventions','kemal-tuncali'),('Sharath Bhagavatula','Interventional radiology','sharath-bhagavatula'),('Adam Kibel','Urologic oncology',''),('Patrick Wen','Neuro-oncology',''),('Jong Woo Lee','Neurology',''),('Eva Gombos','Breast imaging',''),('Scott Swanson','Thoracic surgery',''),('C. Eduardo Corrales','Otology and skull base surgery',''),('Paul Shyn','Interventional radiology','')]
clinicians=[card(n,'Clinical investigator',f,p) for n,f,p in clin]
labs=[('Jonas Lab','TRD2',[('Sebastian Ahn','sebastian-ahn'),('Simon Chow','simon-chow'),('Christine Dominas','christine-dominas'),('Guigen Liu','guigen-liu'),('Nellie Maloney','nellie-maloney'),('Samantha Martin','samantha-martin'),('Sajanlal Panikkanvalappil','sajanlal-panikkanvalappil'),('Fanni Santa','fanni-santa'),('Vincenzo Tarallo','vincenzo-tarallo')]),
('Agar Lab','TRD2',[('Gerard Baquer','gerard-baquer'),('Sankha (Bobby) Basu','sankha-bobby-basu'),('Clément Bodineau','clement-bodineau'),('Julia Bonney','julia-bonney'),('Kaitlyn Bootz','kaitlyn-bootz'),('Aaron Bowen','aaron-bowen'),('Jamie Brett','jamie-brett'),('Aanchalika Chauhan','aanchalika-chauhan'),('Jennifer Gantchev','jennifer-gantchev'),('Christelle Guillermier','christelle-guillermier'),('Songhua Hu','songhua-hu'),('Jaimie Lee','jaimie-lee'),('Zongyu Li','zongyu-li'),('C. Zoë Linke','c-zoe-linke'),('Camilla Martinez','camilla-martinez'),('Jacob Myers','jacob-myers'),('Atticus Scovel','atticus-scovel')]),
('Tokuda Lab','TRD3',[('Mariana Bernardes','mariana-bernardes'),('Ruofeng Wei','ruofeng-wei')])]
labgroups=[{'lab':l,'page':t+'.dc.html','proj':'TR&D '+t[-1],'people':[{'name':n,'photo':P+f+'.jpg'} for n,f in ppl]} for l,t,ppl in labs]
collab=[{'name':n,'photo':P+f+'.jpg','role':r} for n,f,r in [('Iulian Iordachita','iulian-iordachita','Research Professor'),('Axel Krieger','axel-krieger','Assistant Professor'),('Gregory Fischer','gregory-fischer','Professor'),('Simon Leonard','simon-leonard','Assistant Research Professor'),('Tamas Ungi','tamas-ungi','Assistant Professor'),('Ehud Schmidt','ehud-schmidt','Associate Professor'),('Robert Cormack','robert-cormack','Associate Professor of Radiation Oncology'),('Mark Fuge','mark-fuge','Associate Professor'),('Yue Chen','yue-chen','Assistant Professor'),('Gregory Ekchian','gregory-ekchian','CEO')]]
data={'leaders':leaders,'current':current,'past':past,
 'rising':[{'name':'Pedro Moreira, PhD','role':'Instructor in Radiology, Brigham and Women’s Hospital and Harvard Medical School','open':'collaborations, invited talks, faculty positions','photo':'portraits/pedro-moreira.jpg','nophoto':False},{'name':'[Name]','role':'[Instructor in Radiology]','open':'collaborations, invited talks, faculty positions','photo':'','nophoto':True},{'name':'[Name]','role':'[Senior research fellow]','open':'collaborations, faculty positions','photo':'','nophoto':True}]}
CARD='''<article style="background: #FFFFFF; border: 1px solid #E3E8EF; border-radius: 14px; padding: 20px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 4px">
<sc-if value="{{c.photo}}" hint-placeholder-val="{{ true }}"><img src="{{c.photo}}" alt="{{c.name}}" style="width: 104px; height: 104px; border-radius: 50%; object-fit: cover; margin-bottom: 8px"></sc-if>
<sc-if value="{{c.nophoto}}" hint-placeholder-val="{{ false }}"><div role="img" aria-label="Portrait to come" style="width: 104px; height: 104px; border-radius: 50%; background: #EEF1F5; border: 1px dashed #B8C3D1; margin-bottom: 8px"></div></sc-if>
<h3 style="margin: 0; font-size: 18px">{{c.name}}</h3>
<span style="font-size: 13px; font-weight: 600; color: #8A5A2B">{{c.role}}</span>
<span style="font-size: 14px; line-height: 1.45; color: #4A5668">{{c.focus}}</span>
<sc-if value="{{c.haslink}}" hint-placeholder-val="{{ false }}"><a href="{{c.link}}" style="font-size: 14px; font-weight: 600; margin-top: 4px">{{c.linktext}} project →</a></sc-if>
</article>'''
def grid(lst): return '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 18px">\n<sc-for list="{{'+lst+'}}" as="c" hint-placeholder-count="4">\n'+CARD+'\n</sc-for>\n</div>'
def sec(title, intro, inner, bg=''):
    b=f' style="background: {bg}"' if bg else ''
    return f'''<section{b}><div style="max-width: 1200px; margin: 0 auto; padding: 56px 24px 24px">
<h2 style="margin: 0 0 8px; font-size: 28px">{title}</h2>
<p style="margin: 0 0 24px; font-size: 16px; line-height: 1.6; color: #4A5668; max-width: 820px">{intro}</p>
{inner}
</div></section>
'''
body = f'''<header style="border-bottom: 1px solid #E3E8EF">
<div style="max-width: 1200px; margin: 0 auto; padding: 18px 24px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px">
<a href="Main.dc.html" style="display: flex; align-items: center; gap: 12px; color: #0F1B2D">
<svg width="36" height="36" viewBox="0 0 36 36" aria-hidden="true"><circle cx="18" cy="18" r="16" fill="none" stroke="#0B5F86" stroke-width="2.5"></circle><circle cx="18" cy="18" r="6" fill="#A8763E"></circle><path d="M18 2v8M18 26v8M2 18h8M26 18h8" stroke="#0B5F86" stroke-width="2.5"></path></svg>
<span style="display: flex; flex-direction: column; line-height: 1.15"><strong style="font-family: 'Source Serif 4', Georgia, serif; font-size: 20px">AT-NCIGT</strong><span style="font-size: 12px; color: #4A5668">Advanced Technologies - National Center for Image Guided Therapy</span></span>
</a>
{NAV}
</div>
</header>
<section style="background: #0F1B2D; color: #FFFFFF"><div style="max-width: 1200px; margin: 0 auto; padding: 56px 24px 48px">
<p style="margin: 0 0 12px; font-size: 14px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; color: #D9B98F">People</p>
<h1 style="margin: 0 0 14px; font-size: 40px; line-height: 1.2">The people of AT-NCIGT</h1>
<p style="margin: 0; font-size: 18px; line-height: 1.6; color: #C9D3E0; max-width: 760px">Investigators, clinicians, scientists, students and collaborators who carry out the center's research. Reach out to any of them to collaborate, invite a talk or join a lab.</p>
</div></section>
''' + sec('Leadership','Principal investigators of the center.',grid('leaders')) \
  + sec('Center investigators','Investigators funded in the current cycle (2P41EB028741, 2026–2031), including clinician-scientists. Follow a link to see their project.',grid('current'),'#F7F9FC') \
  + sec('Rising investigators','Early-career faculty and senior fellows ready for their next step. They welcome conversations about collaborations, invited talks and career opportunities.','''<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px">
<sc-for list="{{rising}}" as="r" hint-placeholder-count="3"><article style="background: #FFFFFF; border-radius: 12px; padding: 18px; display: flex; gap: 12px; align-items: center"><sc-if value="{{r.photo}}" hint-placeholder-val="{{ false }}"><img src="{{r.photo}}" alt="{{r.name}}" style="flex: 0 0 64px; width: 64px; height: 64px; border-radius: 50%; object-fit: cover"></sc-if><sc-if value="{{r.nophoto}}" hint-placeholder-val="{{ true }}"><div role="img" aria-label="Portrait to come" style="flex: 0 0 64px; height: 64px; border-radius: 50%; background: #EEF1F5; border: 1px dashed #B8C3D1"></div></sc-if><div><strong>{{r.name}}</strong><div style="font-size: 13px; color: #4A5668">{{r.role}}</div><div style="font-size: 12px; font-weight: 600; color: #8A5A2B; margin-top: 2px">Open to: {{r.open}}</div></div></article></sc-for>
</div>''','#F6F1EA') \
      + sec('Investigators of past funding cycles','We gratefully acknowledge the investigators of the 2021–2026 cycle (P41EB028741-01 to -05) and of earlier NCIGT cycles (P41EB015898), whose work is the foundation of the center today.',grid('past'),'#F7F9FC') \
  + sec('External Advisory Committee','Leaders in the field who review the center’s progress and advise its leadership.','<p style="margin: 0; font-size: 15px; color: #4A5668">[Committee members and chair]</p>') \
  + '''<section style="max-width: 1200px; margin: 0 auto; padding: 40px 24px 72px"><div style="background: #0B5F86; color: #FFFFFF; border-radius: 16px; padding: 28px; display: flex; flex-wrap: wrap; gap: 16px 28px; align-items: center; justify-content: space-between"><div style="flex: 999 1 420px"><h2 style="margin: 0 0 6px; font-size: 24px; color: #FFFFFF">Join us</h2><p style="margin: 0; font-size: 15px; line-height: 1.6; color: #E2EEF4">Open positions in center labs, visiting appointments and training opportunities.</p></div><a href="Main.dc.html#training" style="background: #FFFFFF; color: #0B5F86; padding: 13px 20px; border-radius: 8px; font-weight: 600">Open positions →</a></div></section>
<footer style="background: #0F1B2D; color: #C9D3E0; font-size: 14px"><div style="max-width: 1200px; margin: 0 auto; padding: 36px 24px; line-height: 1.6"><strong style="color: #FFFFFF">Advanced Technologies - National Center for Image Guided Therapy (AT-NCIGT)</strong> · Brigham and Women's Hospital · Mass General Brigham · Harvard Medical School · Supported by NIBIB P41EB028741</div></footer>'''
doc='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>People · AT-NCIGT</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;background:#FFFFFF}
a{color:#0B5F86;text-decoration:none}a:hover{color:#08405A;text-decoration:underline}
h1,h2,h3{font-family:'Source Serif 4',Georgia,serif;font-weight:600}
</style>
</helmet>
<div style="font-family: Inter, system-ui, sans-serif; color: #0F1B2D; background: #FFFFFF">
'''+body+'''
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":4200}}'>
class Component extends DCLogic {
renderVals() {
return '''+json.dumps(data,ensure_ascii=False).replace("'","\\u0027")+''';
}
}
</script>
</body>
</html>
'''
open('/home/claude/ncigt/project/People.dc.html','w').write(doc)
print(len(doc))
