import json
TPL = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>__TITLE__ · NCIGT</title>
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

<header style="border-bottom: 1px solid #E3E8EF">
<div style="max-width: 1200px; margin: 0 auto; padding: 18px 24px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px">
<a href="Main.dc.html" style="display: flex; align-items: center; gap: 12px; color: #0F1B2D">
<svg width="36" height="36" viewBox="0 0 36 36" aria-hidden="true"><circle cx="18" cy="18" r="16" fill="none" stroke="#0B5F86" stroke-width="2.5"></circle><circle cx="18" cy="18" r="6" fill="#A8763E"></circle><path d="M18 2v8M18 26v8M2 18h8M26 18h8" stroke="#0B5F86" stroke-width="2.5"></path></svg>
<span style="display: flex; flex-direction: column; line-height: 1.15"><strong style="font-family: 'Source Serif 4', Georgia, serif; font-size: 20px">NCIGT</strong><span style="font-size: 12px; color: #4A5668">National Center for Image Guided Therapy</span></span>
</a>
<nav aria-label="Main" style="display: flex; flex-wrap: wrap; gap: 4px 20px; font-size: 15px; font-weight: 500">
<a href="Main.dc.html#research" style="color: #0F1B2D">Research</a>
<a href="People.dc.html" style="color: #0F1B2D">People</a>
<a href="Main.dc.html#clinical" style="color: #0F1B2D">AMIGO</a>
<a href="Publications.dc.html" style="color: #0F1B2D">Publications</a>
<a href="Main.dc.html#resources" style="color: #0F1B2D">Resources</a>
<a href="Main.dc.html#training" style="color: #0F1B2D">Training</a>
<a href="Industry.dc.html" style="color: #0F1B2D">Industry</a>
<a href="Main.dc.html#partner" style="color: #0F1B2D">Partner with us</a>
<a href="Main.dc.html#community" style="color: #0F1B2D">News</a>
<a href="Main.dc.html#about" style="color: #0F1B2D">About</a>
</nav>
</div>
</header>

<section style="background: #0F1B2D; color: #FFFFFF">
<div style="max-width: 1200px; margin: 0 auto; padding: 64px 24px 56px; display: flex; flex-wrap: wrap; gap: 40px; align-items: center">
<div style="flex: 999 1 520px; min-width: 0">
<p style="margin: 0 0 14px; font-size: 14px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; color: #D9B98F">{{tag}} · Technology research and development</p>
<h1 style="margin: 0 0 16px; font-size: 42px; line-height: 1.2">{{title}}</h1>
<p style="margin: 0 0 24px; font-size: 18px; line-height: 1.6; color: #C9D3E0; max-width: 680px">{{goal}}</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px">
<a href="#team" style="background: #FFFFFF; color: #0F1B2D; padding: 13px 20px; border-radius: 8px; font-weight: 600; text-decoration: none">Meet the team</a>
<a href="#work-with" style="border: 1.5px solid #FFFFFF; color: #FFFFFF; padding: 12px 20px; border-radius: 8px; font-weight: 600; text-decoration: none">Work with this project</a>
</div>
</div>
<div role="img" aria-label="Placeholder for a research figure from this project" style="flex: 1 1 340px; min-width: 0; aspect-ratio: 4 / 3; border-radius: 14px; background: #1C2C44; border: 1px dashed #4A5E7A; display: flex; align-items: center; justify-content: center; text-align: center; padding: 20px; color: #9FB0C6; font-size: 15px">[Key figure from {{figure}}]</div>
</div>
</section>

<section style="max-width: 1200px; margin: 0 auto; padding: 64px 24px 24px; display: flex; flex-wrap: wrap; gap: 40px">
<div style="flex: 999 1 520px; min-width: 0">
<h2 style="margin: 0 0 12px; font-size: 28px">The clinical problem</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.65; color: #3A4658">{{problem}}</p>
</div>
<div style="flex: 1 1 340px; min-width: 0; background: #F3F6FA; border-radius: 14px; padding: 24px">
<h2 style="margin: 0 0 12px; font-size: 22px">What we are developing</h2>
<ul style="margin: 0; padding-left: 20px; font-size: 15px; line-height: 1.7">
<sc-for list="{{aims}}" as="a" hint-placeholder-count="3"><li>{{a.t}}</li></sc-for>
</ul>
</div>
</section>

<section style="max-width: 1200px; margin: 0 auto; padding: 56px 24px 24px">
<h2 style="margin: 0 0 8px; font-size: 28px">Research highlights</h2>
<p style="margin: 0 0 24px; font-size: 16px; line-height: 1.6; color: #4A5668">Publications from the past 12 months by this project and its collaborators.</p>
<figure style="margin: 0 0 28px; display: flex; flex-wrap: wrap; gap: 0; border: 1px solid #E3E8EF; border-radius: 16px; overflow: hidden; background: #FFFFFF">
<a href="{{feat.doi}}" style="flex: 999 1 520px; min-width: 0; background: #0F1B2D; display: block"><img src="{{feat.fig}}" alt="{{feat.alt}}" style="display: block; width: 100%; height: 100%; max-height: 460px; object-fit: contain; background: #FFFFFF"></a>
<figcaption style="flex: 1 1 300px; min-width: 0; padding: 24px; display: flex; flex-direction: column; gap: 8px">
<span style="font-size: 12px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; color: #0B5F86">Latest paper</span>
<a href="{{feat.doi}}" style="color: #0F1B2D; font-family: 'Source Serif 4', Georgia, serif; font-size: 20px; font-weight: 600; line-height: 1.3">{{feat.title}}</a>
<span style="font-size: 14px; color: #4A5668">{{feat.cite}}</span>
<span style="font-size: 15px; line-height: 1.55; color: #3A4658">{{feat.what}}</span>
<span style="margin-top: auto; font-size: 12px; color: #6B778A">{{feat.credit}}</span>
</figcaption>
</figure>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 16px">
<sc-for list="{{papers}}" as="p" hint-placeholder-count="4">
<article style="border: 1px solid #E3E8EF; border-radius: 12px; padding: 20px; display: flex; flex-direction: column; gap: 6px">
<span style="font-size: 13px; font-weight: 600; color: #8A5A2B">{{p.venue}}</span>
<h3 style="margin: 0; font-size: 18px; line-height: 1.35"><a href="{{p.doi}}" style="color: #0F1B2D">{{p.title}}</a></h3>
<span style="font-size: 14px; color: #4A5668">{{p.authors}}</span>
</article>
</sc-for>
</div>
</section>

<section id="team" style="background: #F6F1EA; margin-top: 56px">
<div style="max-width: 1200px; margin: 0 auto; padding: 64px 24px">
<p style="margin: 0 0 8px; font-size: 14px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; color: #8A5A2B">The people behind this project</p>
<h2 style="margin: 0 0 24px; font-size: 32px">Meet the team</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px">
<sc-for list="{{team}}" as="m" hint-placeholder-count="4">
<article style="background: #FFFFFF; border-radius: 14px; padding: 24px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 6px">
<sc-if value="{{m.photo}}" hint-placeholder-val="{{ true }}"><img src="{{m.photo}}" alt="{{m.name}}" style="width: 112px; height: 112px; border-radius: 50%; object-fit: cover; margin-bottom: 8px"></sc-if>
<sc-if value="{{m.nophoto}}" hint-placeholder-val="{{ false }}"><div role="img" aria-label="Portrait to come" style="width: 112px; height: 112px; border-radius: 50%; background: #EEF1F5; border: 1px dashed #B8C3D1; margin-bottom: 8px"></div></sc-if>
<h3 style="margin: 0; font-size: 19px">{{m.name}}</h3>
<span style="font-size: 13px; font-weight: 600; color: #8A5A2B">{{m.role}}</span>
<span style="font-size: 14px; line-height: 1.5; color: #4A5668">{{m.focus}}</span>
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 6px 14px; margin-top: 8px; font-size: 14px; font-weight: 600"><a href="#work-with">Collaborate</a><a href="#work-with">Invite to speak</a><a href="#work-with">Join the lab</a></div>
</article>
</sc-for>
</div>
<div style="margin-top: 24px; background: #FFFFFF; border-radius: 14px; padding: 22px">
<strong style="font-family: 'Source Serif 4', Georgia, serif; font-size: 19px">Rising investigators on this project</strong>
<p style="margin: 6px 0 14px; font-size: 15px; line-height: 1.55; color: #3A4658">Early-career faculty and fellows ready for their next step. They welcome collaborations, invited talks and career opportunities.</p>
<div style="display: flex; flex-wrap: wrap; gap: 16px">
<sc-for list="{{rising}}" as="r" hint-placeholder-count="2">
<div style="display: flex; gap: 12px; align-items: center; flex: 1 1 260px">
<sc-if value="{{r.photo}}" hint-placeholder-val="{{ false }}"><img src="{{r.photo}}" alt="{{r.name}}" style="flex: 0 0 56px; width: 56px; height: 56px; border-radius: 50%; object-fit: cover"></sc-if>
<sc-if value="{{r.nophoto}}" hint-placeholder-val="{{ true }}"><div role="img" aria-label="Placeholder for portrait" style="flex: 0 0 56px; height: 56px; border-radius: 50%; background: #EEF1F5; border: 1px dashed #B8C3D1"></div></sc-if>
<div><strong style="font-size: 16px">{{r.name}}</strong><div style="font-size: 13px; color: #4A5668">{{r.role}}</div></div>
</div>
</sc-for>
</div>
</div>
<sc-if value="{{hasMembers}}" hint-placeholder-val="{{ true }}">
<h3 style="margin: 40px 0 6px; font-size: 22px">Lab members</h3>
<p style="margin: 0 0 18px; font-size: 15px; color: #3A4658">Scientists, fellows and students in the project's laboratories.</p>
<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 18px">
<sc-for list="{{members}}" as="u" hint-placeholder-count="8">
<div style="text-align: center"><img src="{{u.photo}}" alt="{{u.name}}" style="width: 88px; height: 88px; border-radius: 50%; object-fit: cover"><div style="font-size: 14px; font-weight: 600; margin-top: 6px; line-height: 1.3">{{u.name}}</div><div style="font-size: 12px; color: #6B5640">{{u.lab}}</div></div>
</sc-for>
</div>
</sc-if>
<sc-if value="{{hasCollab}}" hint-placeholder-val="{{ true }}">
<h3 style="margin: 40px 0 6px; font-size: 22px">Collaborators</h3>
<p style="margin: 0 0 18px; font-size: 15px; color: #3A4658">Investigators at other institutions and companies who work with this project.</p>
<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 18px">
<sc-for list="{{collab}}" as="u" hint-placeholder-count="6">
<div style="text-align: center"><img src="{{u.photo}}" alt="{{u.name}}" style="width: 88px; height: 88px; border-radius: 50%; object-fit: cover"><div style="font-size: 14px; font-weight: 600; margin-top: 6px; line-height: 1.3">{{u.name}}</div><div style="font-size: 12px; color: #6B5640">{{u.role}}</div></div>
</sc-for>
</div>
</sc-if>
</div>
</section>

<section style="max-width: 1200px; margin: 0 auto; padding: 64px 24px 24px; display: flex; flex-wrap: wrap; gap: 32px">
<div style="flex: 999 1 520px; min-width: 0">
<h2 style="margin: 0 0 8px; font-size: 26px">Partner projects</h2>
<p style="margin: 0 0 18px; font-size: 15px; line-height: 1.6; color: #4A5668">Collaborative and service projects whose questions drive this project's development or who use its technology.</p>
<sc-for list="{{partners}}" as="x" hint-placeholder-count="3">
<div style="display: flex; gap: 14px; align-items: center; padding: 14px 0; border-top: 1px solid #E3E8EF">
<div role="img" aria-label="Placeholder for portrait" style="flex: 0 0 52px; height: 52px; border-radius: 50%; background: #EEF1F5; border: 1px dashed #B8C3D1"></div>
<div style="min-width: 0"><div style="font-size: 12px; font-weight: 600; color: #8A5A2B">{{x.type}}</div><strong style="font-size: 16px">{{x.lead}}</strong><div style="font-size: 14px; color: #4A5668; line-height: 1.45">{{x.what}}</div></div>
</div>
</sc-for>
</div>
<div style="flex: 1 1 340px; min-width: 0">
<h2 style="margin: 0 0 8px; font-size: 26px">Resources</h2>
<p style="margin: 0 0 18px; font-size: 15px; line-height: 1.6; color: #4A5668">Equipment and tools available to collaborators through this project.</p>
<sc-for list="{{equip}}" as="e" hint-placeholder-count="3">
<div style="padding: 14px 0; border-top: 1px solid #E3E8EF"><strong style="font-size: 16px">{{e.name}}</strong><div style="font-size: 14px; color: #4A5668; line-height: 1.45; margin-top: 2px">{{e.what}}</div></div>
</sc-for>
</div>
</section>

<section id="work-with" style="max-width: 1200px; margin: 0 auto; padding: 56px 24px 80px">
<div style="background: #0B5F86; color: #FFFFFF; border-radius: 18px; padding: 36px; display: flex; flex-wrap: wrap; gap: 24px 32px; align-items: center; justify-content: space-between">
<div style="flex: 999 1 480px; min-width: 0">
<h2 style="margin: 0 0 8px; font-size: 26px; color: #FFFFFF">Work with this project</h2>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: #E2EEF4">Any part of this project's methods, tools or data can be a starting point. Talk to the project lead, or contact the center and we will connect you.</p>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px">
<a href="#work-with" style="background: #FFFFFF; color: #0B5F86; padding: 13px 20px; border-radius: 8px; font-weight: 600">Talk to {{lead}}</a>
<a href="Main.dc.html" style="border: 1.5px solid #FFFFFF; color: #FFFFFF; padding: 12px 20px; border-radius: 8px; font-weight: 600">Contact the center</a>
</div>
</div>
</section>

<footer style="background: #0F1B2D; color: #C9D3E0; font-size: 14px">
<div style="max-width: 1200px; margin: 0 auto; padding: 36px 24px; line-height: 1.6"><strong style="color: #FFFFFF">National Center for Image Guided Therapy</strong> · Brigham and Women's Hospital · Mass General Brigham · Harvard Medical School · Supported by NIBIB P41EB028741</div>
</footer>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":3600}}'>
class Component extends DCLogic {
renderVals() {
return __DATA__;
}
}
</script>
</body>
</html>
'''
D = 'https://doi.org/'
pages = {
'TRD1': dict(tag='TR&D 1', title='Imaging cancer heterogeneity', figure='a diffusion or CEST MRI study',
 goal='Advanced MRI at 3T and 7T that reveals the structure and chemistry of tumors in more detail, to guide where and how to treat.',
 problem='Tumors are not uniform. Regions that look alike on standard MRI can differ in cell density, microstructure and metabolism, and those differences affect diagnosis, targeting and response to treatment. Measuring them noninvasively, with methods that are reproducible across scanners, would let clinicians aim biopsies and therapy at the parts of a tumor that matter most.',
 aims=[{'t':'Sub-millimeter diffusion MRI for tissue microstructure'},{'t':'Quantitative chemical exchange saturation transfer (CEST) imaging'},{'t':'Methods for 3T clinical scanners, 7T and high-performance gradient systems'},{'t':'Reproducible quantitative measures for prostate and brain tumors'}],
 papers=[
  {'title':'Unveiling neuronal microstructure in the human brain in vivo with time-dependent radial diffusivity in a head-only high-performance gradient 3T MRI system','authors':'Zhu A, … Maier SE, … Westin CF, … Li H (led by GE HealthCare)','venue':'Hum Brain Mapp, Nov 2026','doi':D+'10.1002/hbm.70664'},
  {'title':'Optimization of diffusion MRI with consideration of the signal decay in biological tissues','authors':'Kuczera S, Maier SE','venue':'Magn Reson Med, Jul 2026','doi':D+'10.1002/mrm.70346'}],
 team=[{'name':'Stephan E. Maier','role':'Project lead','focus':'Quantitative diffusion MRI'},
  {'name':'Carl-Fredrik Westin','role':'Investigator','focus':'Diffusion MRI methods'},
  {'name':'William M. Wells III','role':'Co-investigator','focus':'Image registration and multimodal learning'},
  {'name':'Daniel Paech','role':'Investigator','focus':'Quantitative CEST MRI of tumor chemistry'},
  {'name':'Florian Kroh','role':'Postdoctoral fellow','focus':'CEST MRI'},
  {'name':'Arthur Chakwizira','role':'Investigator','focus':'Diffusion MRI methods'}],
 rising=[{'name':'[Name]','role':'[Instructor in Radiology]'},{'name':'[Name]','role':'[Research fellow]'}],
 partners=[{'type':'Collaborative project','lead':'Vikas Gulani, University of Michigan','what':'Multicenter repeatability of MR fingerprinting in prostate tissue'},
  {'type':'Service project','lead':'Peter LaViolette, Medical College of Wisconsin','what':'Multi-site concordance of diffusion-weighted imaging in prostate cancer'},
  {'type':'[Partner type]','lead':'[Current partner]','what':'[One line on the project]'}],
 equip=[{'name':'High-performance gradient MRI (MAGNUS)','what':'Ultra-high-performance gradients for advanced diffusion imaging.'},{'name':'7T and 3T research MRI','what':'Quantitative and CEST imaging protocols.'},{'name':'Analysis software','what':'Diffusion and quantitative MRI processing tools.'}],
 lead='Stephan Maier'),
'TRD2': dict(tag='TR&D 2', title='Implantable microdevices', figure='a microdevice implantation study',
 goal='Tiny devices placed in a tumor that test many drugs at once inside the patient, so treatment can be chosen by how that tumor actually responds.',
 problem='Patients with the same cancer type often respond very differently to the same drug, and today most treatment choices are made without testing them on the patient’s own tumor. Microdevices that release minute doses of many drugs into different regions of a tumor, then are removed with the surrounding tissue, can show which drugs work before a full course of systemic therapy begins.',
 aims=[{'t':'Microdevices that measure drug efficacy in situ'},{'t':'Image-guided implantation and retrieval, including MRI-guided placement'},{'t':'Multi-omic readout of local drug response'},{'t':'Machine learning that links response patterns to imaging biomarkers'}],
 papers=[
  {'title':'A spatially resolved implantable microdevice for multiplexed in situ screening of engineered cellular therapies in solid tumors','authors':'Panikkanvalappil SR, … Bhagavatula SK, Jonas O','venue':'Science Advances, Aug 2026','doi':D+'10.1126/sciadv.aee6195'},
  {'title':'Implantable microdevices for in vivo assessment of chemotherapy response in patient-derived organoid orthotopic pancreatic cancer models','authors':'Standring OJ, … Jonas O, … Weiss MJ','venue':'Ann Surg, May 2026','doi':D+'10.1097/SLA.0000000000007071'},
  {'title':'Development and pre-clinical feasibility of a catheter-based platform for interventional phase-0 drug response measurements','authors':'Bhagavatula SK, … Jonas O','venue':'Ann Biomed Eng, Mar 2026','doi':D+'10.1007/s10439-026-04113-w'}],
 team=[{'name':'Oliver Jonas','role':'Project lead','focus':'Implantable microdevices'},
  {'name':'Sharath Bhagavatula','role':'Investigator','focus':'Interventional radiology'},
  {'name':'Nobuhiko Hata','role':'Investigator','focus':'Image-guided device placement'},
  {'name':'[First name] Akgul','role':'Co-investigator','focus':'[Research focus]'}],
 rising=[{'name':'Guigen Liu, PhD','role':'NIBIB K25 awardee: 4D microimaging of implanted microdevices','photo':'portraits/guigen-liu.jpg'},{'name':'[Name]','role':'[Research fellow]'}],
 partners=[{'type':'Partner site','lead':'University of California, San Francisco','what':'Enrolling patients in the three-day microdevice implantation study'},
  {'type':'Collaborative project','lead':'Jann Sarkaria, Mayo Clinic','what':'Drug delivery and response in glioblastoma models'},
  {'type':'[Partner type]','lead':'[Current partner]','what':'[One line on the project]'}],
 equip=[{'name':'Microdevice fabrication and implantation','what':'Device design, loading and image-guided placement.'},{'name':'Mass spectrometry imaging','what':'Spatially resolved measurement of drugs and metabolites in tissue.'},{'name':'The AMIGO suite','what':'MRI-guided implantation during clinical procedures.'}],
 lead='Oliver Jonas'),
'TRD3': dict(tag='TR&D 3', title='Enabling technologies for data-driven interventions', figure='a robotic or navigated procedure',
 goal='Robotic needle guidance and augmented-reality navigation that help physicians reach small targets precisely, across MRI, CT, ultrasound and endoscopy.',
 problem='Many procedures depend on placing a needle or instrument exactly on a small target that moves or deforms, while the physician watches images that are not perfectly aligned with the patient. Needles bend, organs shift and anatomy differs from the preoperative scan. Robots that correct their path from imaging data, and navigation that tracks the anatomy as it moves, can make these procedures more accurate and more consistent.',
 aims=[{'t':'Robotic needle guidance with path correction for needle deflection'},{'t':'Augmented-reality and trackerless navigation for open and endoscopic surgery'},{'t':'AI-based prediction to plan and monitor ablation'},{'t':'Clinical evaluation in the AMIGO suite and procedure rooms'}],
 papers=[
  {'title':'Multimodal cross-attention fusion of B-mode ultrasound and strain elastography for tumor segmentation in robotics-assisted surgery','authors':'Abkhofte S, Naidu AS, Patel RV, Jagadeesan J','venue':'IEEE Trans Med Robot Bionics, May 2026','doi':D+'10.1109/tmrb.2026.3681001'},
  {'title':'Clinical validation of a novel robotic device for MR-guided prostate biopsy: initial patient experience','authors':'Moreira P, … Park J, Tokuda J','venue':'J Med Robot Res, Mar 2026','doi':D+'10.1142/s2424905x26500042'},
  {'title':'AI-assisted cryo-dose estimation and tissue injury modeling in MRI-guided prostate cryoablation','authors':'Moreira P, … Tempany C, Tuncali K, Tokuda J','venue':'Phys Med Biol, Mar 2026','doi':D+'10.1088/1361-6560/ae4847'},
  {'title':'Machine learning model for fast prediction and uncertainty quantification of needle deflection during prostate biopsy','authors':'Hoffman N, … Tokuda J, Moreira P, Fuge M (led by University of Maryland)','venue':'Med Phys, Feb 2026','doi':D+'10.1002/mp.70314'}],
 team=[{'name':'Junichi Tokuda','role':'Project lead','focus':'MRI-guided robotic interventions'},
  {'name':'Jagadeesan Jayender','role':'Investigator','focus':'Surgical navigation and computer vision'},
  {'name':'Nobuhiko Hata','role':'Investigator','focus':'Robotic navigation for bronchoscopy and prostate interventions'},
  {'name':'Haoyin Zhou','role':'Co-investigator','focus':'Trackerless navigation for minimally invasive surgery'},
  {'name':'Mariana Bernardes','role':'Investigator','focus':'MRI-guided robotic needle placement'}],
 rising=[{'name':'Pedro Moreira, PhD','role':'Instructor in Radiology, BWH and HMS','photo':'portraits/pedro-moreira.jpg'},{'name':'[Name]','role':'[Research fellow]'}],
 partners=[{'type':'Service project','lead':'Jesung Park, Physical Sciences Inc.','what':'Robotic template for MRI-guided prostate biopsy and cryoablation'},
  {'type':'Collaborative project','lead':'Haichong Zhang, Worcester Polytechnic Institute','what':'Robot-assisted photoacoustic imaging for monitoring liver ablation'},
  {'type':'[Partner type]','lead':'[Current partner]','what':'[One line on the project]'}],
 equip=[{'name':'MRI-guided robotics','what':'MRI-compatible needle-guidance robots and shape-sensing needles.'},{'name':'Robotic navigation and bronchoscopy','what':'Continuum robots and vision-based navigation.'},{'name':'Surgical vision and augmented reality','what':'Stereo endoscopy, 3D reconstruction and AR navigation.'},{'name':'The AMIGO suite','what':'Robotic and navigated procedures under MRI, PET/CT and X-ray.'}],
 lead='Junichi Tokuda'),
}
P='portraits/'
def ph(n): return P+n+'.jpg'
photos={'Mariana Bernardes':'mariana-bernardes','Carl-Fredrik Westin':'carl-fredrik-westin','Daniel Paech':'daniel-paech','Haoyin Zhou':'haoyin-zhou','Stephan E. Maier':'stephan-e-maier','Fiona M. Fennessy':'fiona-m-fennessy','Clare M. Tempany':'clare-m-tempany','Oliver Jonas':'oliver-jonas','Sharath Bhagavatula':'sharath-bhagavatula','Nathalie Y. R. Agar':'nathalie-y-r-agar','Junichi Tokuda':'junichi-tokuda','Nobuhiko Hata':'nobuhiko-hata','Jagadeesan Jayender':'jagadeesan-jayender','Pedro Moreira':'pedro-moreira','Kemal Tuncali':'kemal-tuncali'}
jonas=[('Sebastian Ahn','sebastian-ahn'),('Simon Chow','simon-chow'),('Christine Dominas','christine-dominas'),('Guigen Liu','guigen-liu'),('Nellie Maloney','nellie-maloney'),('Samantha Martin','samantha-martin'),('Sajanlal Panikkanvalappil','sajanlal-panikkanvalappil'),('Fanni Santa','fanni-santa'),('Vincenzo Tarallo','vincenzo-tarallo')]
agar=[('Gerard Baquer','gerard-baquer'),('Sankha (Bobby) Basu','sankha-bobby-basu'),('Clément Bodineau','clement-bodineau'),('Julia Bonney','julia-bonney'),('Kaitlyn Bootz','kaitlyn-bootz'),('Aaron Bowen','aaron-bowen'),('Jamie Brett','jamie-brett'),('Aanchalika Chauhan','aanchalika-chauhan'),('Jennifer Gantchev','jennifer-gantchev'),('Christelle Guillermier','christelle-guillermier'),('Songhua Hu','songhua-hu'),('Jaimie Lee','jaimie-lee'),('Zongyu Li','zongyu-li'),('C. Zoë Linke','c-zoe-linke'),('Camilla Martinez','camilla-martinez'),('Jacob Myers','jacob-myers'),('Atticus Scovel','atticus-scovel')]
tokuda=[('Mariana Bernardes','mariana-bernardes'),('Ruofeng Wei','ruofeng-wei')]
collab3=[('Iulian Iordachita','iulian-iordachita','Research Professor'),('Axel Krieger','axel-krieger','Assistant Professor'),('Gregory Fischer','gregory-fischer','Professor'),('Simon Leonard','simon-leonard','Assistant Research Professor'),('Tamas Ungi','tamas-ungi','Assistant Professor'),('Ehud Schmidt','ehud-schmidt','Associate Professor'),('Robert Cormack','robert-cormack','Associate Professor of Radiation Oncology'),('Mark Fuge','mark-fuge','Associate Professor'),('Yue Chen','yue-chen','Assistant Professor'),('Gregory Ekchian','gregory-ekchian','CEO')]

FEAT={
'TRD1':{'fig':'media/figs/trd1-hbm2026-fig2-full.jpg','alt':'Diffusion MRI maps of the human brain in axial, sagittal and coronal planes','title':'Unveiling neuronal microstructure in the human brain in vivo with time-dependent radial diffusivity in a head-only high-performance gradient 3T MRI system','cite':'Zhu A, … Maier SE, … Westin CF, … Li H. Hum Brain Mapp, Nov 2026','what':'Oscillating-gradient diffusion MRI on a high-performance gradient scanner reveals how radial diffusivity changes with diffusion time across white matter.','credit':'Figure 2 of the paper, CC BY 4.0.','doi':'https://doi.org/10.1002/hbm.70664'},
'TRD2':{'fig':'media/figs/trd2-sciadv2026-fig2-full.jpg','alt':'Design drawings, imaging and fluorescence microscopy of an implantable microdevice releasing cells','title':'A spatially resolved implantable microdevice for multiplexed in situ screening of engineered cellular therapies in solid tumors','cite':'Panikkanvalappil SR, … Jonas O. Sci Adv, Aug 2026','what':'The microdevice platform extended from drugs to engineered cell therapies, screened side by side inside solid tumors.','credit':'Figure 2 of the paper, CC BY-NC 4.0.','doi':'https://doi.org/10.1126/sciadv.aee6195'},
'TRD3':{'fig':'media/figs/trd3-medphys2026-fig7-full.jpg','alt':'Predicted needle deflection with confidence bands on segmented prostate MRI and on the MRI slice','title':'Machine learning model for fast prediction and uncertainty quantification of needle deflection during prostate biopsy','cite':'Hoffman N, Al-Zogbi L, Krieger A, Tokuda J, Moreira P, Fuge M. Med Phys, Feb 2026','what':'A neural network predicts how a biopsy needle will bend, with confidence bands, fast enough for planning during the procedure.','credit':'Figure 7 of the paper, CC BY 4.0.','doi':'https://doi.org/10.1002/mp.70314'}}
for k in FEAT: pages[k]['feat']=FEAT[k]
for k,v in pages.items():
    for m in v['team']:
        f=photos.get(m['name']); m['photo']=ph(f) if f else ''; m['nophoto']= not f
    for r in v.get('rising',[]):
        r.setdefault('photo',''); r['nophoto']=not r['photo']
    v['members']=[]; v['collab']=[]
    if False:
        v['members']=[{'name':n,'photo':ph(f),'lab':'Jonas Lab'} for n,f in jonas]+[{'name':n,'photo':ph(f),'lab':'Agar Lab'} for n,f in agar]
    if False:
        v['members']=[{'name':n,'photo':ph(f),'lab':'Tokuda Lab'} for n,f in tokuda]
        v['collab']=[{'name':n,'photo':ph(f),'role':r} for n,f,r in collab3]
    v['hasMembers']=bool(v['members']); v['hasCollab']=bool(v['collab'])
for k,v in pages.items():
    s = TPL.replace('__TITLE__', v['title']).replace('__DATA__', json.dumps(v, ensure_ascii=False, indent=0))
    open(f'/home/claude/ncigt/project/{k}.dc.html','w').write(s)
    print(k, len(s))
