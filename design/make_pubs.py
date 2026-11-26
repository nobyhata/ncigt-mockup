import json,re
D='https://doi.org/'
main=open('/home/claude/ncigt/project/Main.dc.html').read()
major=json.loads(re.search(r'major: (\[.*?\]),\ncollabs',main,re.S).group(1))
collabs=json.loads(re.search(r'collabs: (\[.*?\]),\ncycles',main,re.S).group(1))
major+= [
 dict(title='Clinical feasibility study of generative depth estimation to diagnose airway stenosis using 3D Slicer',venue='Int J Comput Assist Radiol Surg, May 2026',project='Robotic bronchoscopy',senior='Nobuhiko Hata',first='Artur Banach (BWH)',why='A public 3D Slicer tool that estimates airway narrowing from bronchoscopy video, tested on 30 patients; with Canon Medical Research USA and EPFL.',doi=D+'10.1007/s11548-026-03721-0'),
 dict(title='An in vivo platform to jointly monitor cellular and metabolic responses to chemotherapy (preprint)',venue='bioRxiv, Jun 2026',project='TR&D 2',senior='Oliver Jonas',first='Veronika Pister (MIT)',why='Combines microdevice drug testing with metabolic readouts in the same tumor.',doi=D+'10.64898/2026.06.25.734296')]
order={'Nov':11,'Oct':10,'Sep':9,'Aug':8,'Jul':7,'Jun':6,'May':5,'Apr':4,'Mar':3,'Feb':2,'Jan':1,'Dec':0}
def k(p):
    v=p['venue'].split(', ')[-1].split(' ')
    if len(v)==2: return (int(v[1]), order.get(v[0],0) + (12 if False else 0))
    return (int(v[0]),0)
major.sort(key=lambda p:(k(p)[0]*13+k(p)[1]),reverse=True)
collabs+= [
 dict(title='Toward autonomous robotic-assisted and microrobotic surgery',venue='Science Advances, Jul 2026',leadinst='Massachusetts Institute of Technology',first='Sungyun Yang (MIT)',partners='MIT; Johns Hopkins University; Vanderbilt University; Northwestern University; University of North Carolina; UC San Diego; Boston University; Boston Children’s Hospital; Activ Surgical (industry)',center='Nobuhiko Hata',doi=D+'10.1126/sciadv.aec4197'),
 dict(title='Implantable microdevices for in vivo assessment of chemotherapy response in patient-derived organoid orthotopic pancreatic cancer models',venue='Ann Surg, May 2026',leadinst='Cold Spring Harbor Laboratory',first='Oliver J. Standring (Cold Spring Harbor Laboratory)',partners='Cold Spring Harbor Laboratory; Northwell Health',center='Oliver Jonas',doi=D+'10.1097/SLA.0000000000007071'),
 dict(title='Real-time SLAM-based correction and 3D visualization for fluorescence lifetime imaging',venue='MICCAI, 2026',leadinst='Massachusetts Eye and Ear',first='Murali Krishnamoorthy (Mass Eye and Ear)',partners='Massachusetts Eye and Ear',center='Jagadeesan Jayender',doi=D+'10.1007/978-3-032-05141-7_47'),
 dict(title='Robot-assisted minimally invasive photoacoustic imaging for monitoring liver ablation using diffusing fiber illumination',venue='J Biomed Opt, 2026',leadinst='Worcester Polytechnic Institute',first='Shang Gao (WPI)',partners='Worcester Polytechnic Institute; MGH Wellman Center for Photomedicine',center='Sharath Bhagavatula, Oliver Jonas',doi=D+'10.1117/1.JBO.31.12.123302'),
 dict(title='Window of opportunity evaluation of blood-brain barrier permeability heterogeneity within and across high-grade glioma patients',venue='Neuro-Oncology, Jan 2026',leadinst='University of Minnesota',first='Ju-Hee Oh (University of Minnesota)',partners='University of Minnesota; Mayo Clinic',center='Nathalie Y. R. Agar',doi=D+'10.1093/neuonc/noaf204')]
collabs.sort(key=lambda p:(k(p)[0]*13+k(p)[1]),reverse=True)
inst=sorted({c['leadinst'] for c in collabs})
data={'major':major,'collabs':collabs,'nmajor':len(major),'ncollab':len(collabs),'ninst':len(inst),'insts':', '.join(inst)}
NAV=open('nav.html').read()
body=f'''<header style="border-bottom: 1px solid #E3E8EF">
<div style="max-width: 1200px; margin: 0 auto; padding: 18px 24px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px">
<a href="Main.dc.html" style="display: flex; align-items: center; gap: 12px; color: #0F1B2D">
<svg width="36" height="36" viewBox="0 0 36 36" aria-hidden="true"><circle cx="18" cy="18" r="16" fill="none" stroke="#0B5F86" stroke-width="2.5"></circle><circle cx="18" cy="18" r="6" fill="#A8763E"></circle><path d="M18 2v8M18 26v8M2 18h8M26 18h8" stroke="#0B5F86" stroke-width="2.5"></path></svg>
<span style="display: flex; flex-direction: column; line-height: 1.15"><strong style="font-family: 'Source Serif 4', Georgia, serif; font-size: 20px">AT-NCIGT</strong><span style="font-size: 12px; color: #4A5668">Advanced Technologies - National Center for Image Guided Therapy</span></span>
</a>
{NAV}
</div>
</header>
<section style="background: #0F1B2D; color: #FFFFFF"><div style="max-width: 1200px; margin: 0 auto; padding: 56px 24px 48px">
<p style="margin: 0 0 12px; font-size: 14px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; color: #D9B98F">Publications</p>
<h1 style="margin: 0 0 14px; font-size: 40px; line-height: 1.2">Research outcomes, past 12 months</h1>
<p style="margin: 0 0 24px; font-size: 18px; line-height: 1.6; color: #C9D3E0; max-width: 780px">Papers that acknowledge center support, published December 2025 to November 2026.</p>
<div style="display: flex; flex-wrap: wrap; gap: 32px">
<div><div style="font-family: 'Source Serif 4', Georgia, serif; font-size: 36px; font-weight: 600; color: #D9B98F">{{{{nmajor}}}}</div><div style="font-size: 14px; color: #C9D3E0">major achievements</div></div>
<div><div style="font-family: 'Source Serif 4', Georgia, serif; font-size: 36px; font-weight: 600; color: #D9B98F">{{{{ncollab}}}}</div><div style="font-size: 14px; color: #C9D3E0">collaborations</div></div>
<div><div style="font-family: 'Source Serif 4', Georgia, serif; font-size: 36px; font-weight: 600; color: #D9B98F">{{{{ninst}}}}</div><div style="font-size: 14px; color: #C9D3E0">partner institutions leading papers</div></div>
</div>
</div></section>

<section style="max-width: 1200px; margin: 0 auto; padding: 56px 24px 24px">
<h2 style="margin: 0 0 8px; font-size: 30px">Major achievements</h2>
<p style="margin: 0 0 24px; font-size: 16px; line-height: 1.6; color: #4A5668; max-width: 860px">Papers with a center investigator as senior author.</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 16px">
<sc-for list="{{{{major}}}}" as="p" hint-placeholder-count="6">
<article style="border: 1px solid #E3E8EF; border-left: 4px solid #0B5F86; border-radius: 0 12px 12px 0; padding: 18px 20px; display: flex; flex-direction: column; gap: 6px">
<span style="font-size: 13px; font-weight: 600; color: #8A5A2B">{{{{p.venue}}}} · {{{{p.project}}}}</span>
<a href="{{{{p.doi}}}}" style="color: #0F1B2D; font-family: 'Source Serif 4', Georgia, serif; font-size: 18px; font-weight: 600; line-height: 1.35">{{{{p.title}}}}</a>
<span style="font-size: 14px; color: #3A4658; line-height: 1.5">{{{{p.why}}}}</span>
<span style="font-size: 13px; color: #4A5668">Senior author: <strong>{{{{p.senior}}}}</strong> · First author: {{{{p.first}}}}</span>
</article>
</sc-for>
</div>
</section>

<section style="background: #F7F9FC; margin-top: 48px"><div style="max-width: 1200px; margin: 0 auto; padding: 56px 24px">
<h2 style="margin: 0 0 8px; font-size: 30px">Collaborations</h2>
<p style="margin: 0 0 24px; font-size: 16px; line-height: 1.6; color: #4A5668; max-width: 860px">Papers led by partner institutions and companies, with center investigators as co-authors. Lead institutions this year: {{{{insts}}}}.</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 16px">
<sc-for list="{{{{collabs}}}}" as="c" hint-placeholder-count="6">
<article style="background: #FFFFFF; border-radius: 12px; padding: 18px 20px; display: flex; flex-direction: column; gap: 6px">
<span style="font-size: 12px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; color: #8A5A2B">Led by {{{{c.leadinst}}}}</span>
<a href="{{{{c.doi}}}}" style="color: #0F1B2D; font-size: 16px; font-weight: 600; line-height: 1.4">{{{{c.title}}}}</a>
<span style="font-size: 13px; color: #4A5668">{{{{c.venue}}}} · First author: {{{{c.first}}}}</span>
<span style="font-size: 13px; color: #3A4658; line-height: 1.5"><strong>Partners:</strong> {{{{c.partners}}}}</span>
<span style="font-size: 13px; color: #0B5F86; font-weight: 600">Center co-authors: {{{{c.center}}}}</span>
</article>
</sc-for>
</div>
</div></section>

<section style="max-width: 1200px; margin: 0 auto; padding: 48px 24px 72px; display: flex; flex-wrap: wrap; gap: 24px">
<div style="flex: 999 1 480px; min-width: 0; background: #F6F1EA; border-radius: 14px; padding: 24px">
<h2 style="margin: 0 0 8px; font-size: 22px">Earlier publications</h2>
<p style="margin: 0 0 12px; font-size: 15px; line-height: 1.6; color: #3A4658">All papers acknowledging the center’s grants, from every funding cycle, are listed on PubMed.</p>
<a href="https://pubmed.ncbi.nlm.nih.gov/?term=P41+EB028741+OR+P41EB028741+OR+P41+EB015898+OR+P41EB015898&amp;sort=pubdate&amp;size=200" style="font-weight: 600">See all publications on PubMed →</a>
</div>
<div style="flex: 1 1 340px; min-width: 0; border: 1px solid #E3E8EF; border-radius: 14px; padding: 24px">
<h2 style="margin: 0 0 8px; font-size: 22px">Is your paper missing?</h2>
<p style="margin: 0 0 12px; font-size: 15px; line-height: 1.6; color: #3A4658">If your work used the center’s technology, data, equipment or staff, please acknowledge P41EB028741 and let us know, so we can feature it here.</p>
<a href="Main.dc.html#about" style="font-weight: 600">How to acknowledge the center →</a>
</div>
</section>
<footer style="background: #0F1B2D; color: #C9D3E0; font-size: 14px"><div style="max-width: 1200px; margin: 0 auto; padding: 36px 24px; line-height: 1.6"><strong style="color: #FFFFFF">Advanced Technologies - National Center for Image Guided Therapy (AT-NCIGT)</strong> · Brigham and Women's Hospital · Mass General Brigham · Harvard Medical School · Supported by NIBIB P41EB028741</div></footer>'''
doc='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Publications · AT-NCIGT</title>
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
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":3600}}'>
class Component extends DCLogic {
renderVals() {
return '''+json.dumps(data,ensure_ascii=False).replace("'","\\u0027")+''';
}
}
</script>
</body>
</html>
'''
open('/home/claude/ncigt/project/Publications.dc.html','w').write(doc)
print(len(major),len(collabs),inst)
