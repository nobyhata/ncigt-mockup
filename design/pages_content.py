"""Rewritten content for every carried-over content page, in one shared template.

Each page has the same parts, in the same order:
  banner   one picture (src, alt) or None for a placeholder, shown in the same 21:9 frame
  lead     two or three sentences: what this is and who it is for
  glance   3-4 "At a glance" facts (label, value html)
  sections 2-3 short sections (heading, html)
  data     optional (heading, key) — a list or table kept from the previous website
  contact  who to contact (html)
  links    2-4 related links (text, href)
Text in [brackets] is a placeholder to be filled in.
"""

AMIGO_CONTACT = 'Clare Tempany, MD, and Alexandra Golby, MD, co-medical directors of AMIGO [verify current directors]'

PAGES = {

# ------------------------------------------------------------------ AMIGO
'page-amigo.html': dict(
  banner=('media/2025_05_AMIGO-team2025-e1747954294868.jpg', 'The AMIGO team in the suite, 2025'),
  lead='The Advanced Multimodality Image Guided Operating (AMIGO) suite is where the center tests its technology in patients. Three connected procedure rooms let surgeons, radiologists, physicists and engineers image, navigate and treat without moving the patient out of the suite.',
  glance=[('Opened', '2011'), ('Size', '5,700 sq ft, three sterile rooms'), ('Imaging', '3T wide-bore MRI, PET/CT, X-ray angiography, 3D ultrasound'), ('Role', 'Clinical test bed of AT-NCIGT')],
  sections=[
    ('Three rooms, one procedure', '<p>The <strong>MRI room</strong> has a 3 tesla, 70 cm wide-bore scanner on ceiling rails that can move to a draped patient on the operating table. The <strong>operating room</strong> in the middle has surgical navigation, a near-infrared surgical microscope, a ceiling-mounted angiographic C-arm and 3D ultrasound. The <strong>PET/CT room</strong> uses short half-life tracers from the hospital cyclotron to show tumor before treatment and confirm its removal after.</p>'),
    ('What is done here', '<ul><li>Brain tumor resection and laser ablation</li><li>Breast-conserving surgery with intraoperative MRI</li><li>MRI-guided prostate biopsy and cryoablation</li><li>Gynecologic brachytherapy</li><li>Thoracic, spine, skull base, endoscopic and laparoscopic surgery</li></ul>'),
    ('For researchers', '<p>Fridays are reserved for technical research, with no clinical cases. New projects pass a scientific review, an engineering and safety review and a dry run before the first patient.</p>'),
  ],
  contact=AMIGO_CONTACT,
  links=[('Procedures in AMIGO', 'page-amigoprocedures.html'), ('Clinical trials', 'page-clinical-trials.html'), ('A review of the first year of AMIGO (PDF)', 'media/2022_12_2013.03_amigo_first_yr.pdf'), ('Image-guided therapy research at the Brigham', 'page-history.html')]),

'page-amigoprocedures.html': dict(
  banner=('media/2026_01_AMIGO-PROCEDURES-SLIDE12312025.jpg', 'Procedures performed in AMIGO through December 2025'),
  lead='Many procedures in AMIGO are part of clinical trials. This page summarizes the types and numbers of procedures performed in the suite.',
  glance=[('Data through', 'December 31, 2025'), ('Procedure types', 'Neurosurgery, breast, prostate, gynecologic, thoracic, interventional radiology'), ('Total procedures', '[number]')],
  sections=[
    ('Procedures by type', '<p>The figure above shows procedures by clinical area. [Replace with a short table: procedure type, number of cases, first year performed.]</p>'),
    ('Procedures in clinical trials', '<p>Studies that are recruiting or have completed are listed on <a href="page-clinical-trials.html">Clinical trials</a>.</p>'),
  ],
  contact=AMIGO_CONTACT,
  links=[('Clinical trials', 'page-clinical-trials.html'), ('About the AMIGO suite', 'page-amigo.html')]),

'page-clinical-trials.html': dict(
  banner=None, banner_note='Photo: a procedure in the AMIGO MRI room',
  lead='Clinical studies that use the AMIGO suite and center technology. Each study links to its record on ClinicalTrials.gov, where eligibility and contacts are kept current.',
  glance=[('Recruiting or active', '5 studies'), ('Completed', '[number] studies'), ('Areas', 'Prostate, brain, head, neck and spine, lung, liver, breast')],
  sections=[],
  data=('Studies', 'trials'),
  contact='The study contact listed on each ClinicalTrials.gov record. ' + AMIGO_CONTACT,
  links=[('Procedures in AMIGO', 'page-amigoprocedures.html'), ('About the AMIGO suite', 'page-amigo.html')]),

'page-brain-tumor-resection.html': dict(
  banner=('media/2023_01_330px-neuroflow5b-e1675109723927.jpg', 'Navigation view during brain tumor surgery in AMIGO'),
  lead='For tumors that look like normal brain during surgery, such as low-grade gliomas, AMIGO lets the team bring preoperative maps, electrical mapping and new ultrasound, MRI, CT and PET images together in one operation.',
  glance=[('Who benefits', 'Patients whose tumor is hard to tell from brain'), ('Imaging used', 'Ultrasound, 3T MRI, tractography, navigation'), ('Clinical lead', 'Alexandra Golby, MD')],
  sections=[
    ('How a case runs', '<ol><li><strong>Plan and open.</strong> Navigation guides a small craniotomy over the tumor.</li><li><strong>Orient.</strong> Ultrasound shows the tumor and major vessels; electrical stimulation maps critical cortex when needed.</li><li><strong>Remove.</strong> Navigation and tractography guide resection around white matter tracts.</li><li><strong>Check.</strong> The 3T MRI moves into the room to show any remaining tumor, which can be removed in the same operation.</li><li><strong>Close and confirm.</strong> A final MRI sets a new baseline, and motor function is tested on waking.</li></ol>'),
    ('Why it matters', '<p>Removing more tumor improves progression-free and overall survival, and sparing critical areas preserves function. Intraoperative MRI lets the surgeon see both before the operation ends.</p>'),
  ],
  contact='Alexandra Golby, MD, Department of Neurosurgery',
  links=[('About the AMIGO suite', 'page-amigo.html'), ('Clinical trials', 'page-clinical-trials.html'), ('Neurosurgery Core (earlier cycle)', 'page-neurosurgery-core.html')]),

'page-breast-cancer-surgery.html': dict(
  banner=('media/2023_01_breastmrimoving.png', 'Supine breast MRI in the AMIGO operating room'),
  lead='In the United States 15 to 40 percent of women who have breast-conserving surgery need a second operation because cancer is found at the edge of the removed tissue. In AMIGO, we test whether MRI and mass spectrometry during surgery can find remaining cancer before the operation ends.',
  glance=[('Problem', 'Re-excision after lumpectomy (15–40%)'), ('Approach', 'Supine MRI before and after resection; mass spectrometry of tissue'), ('Clinical trial', '<a href="https://clinicaltrials.gov/ct2/show/NCT02335671">NCT02335671</a>')],
  sections=[
    ('How a case runs', '<ol><li><strong>Image.</strong> With the patient asleep on the operating table, a contrast MRI maps the tumor and any satellite lesions.</li><li><strong>Operate.</strong> The surgeon removes the tumor and sentinel lymph nodes; the cavity is filled with saline.</li><li><strong>Check.</strong> A second MRI looks for enhancement around the cavity that could be residual cancer.</li><li><strong>Act.</strong> If suspicious tissue is seen, it is removed in the same operation.</li></ol>'),
    ('Goal', '<p>Clear margins at the first operation, fewer repeat surgeries, and no delay to follow-on treatment.</p>'),
  ],
  contact='Study contact: Stephen (Dan) DeSantis, <a href="mailto:Stephen_Desantis@DFCI.HARVARD.EDU">Stephen_Desantis@DFCI.HARVARD.EDU</a> [verify]',
  links=[('Clinical trial record', 'https://clinicaltrials.gov/ct2/show/NCT02335671'), ('Interim analysis of intraoperative mass spectrometry (PubMed)', 'https://pubmed.ncbi.nlm.nih.gov/34504095/'), ('About the AMIGO suite', 'page-amigo.html')]),

'page-mr-guided-prostate-biopsy.html': dict(
  banner=('media/2023_01_320px-prostate-flow2-1.jpg', 'MRI-guided prostate biopsy setup in the wide-bore 3T MRI'),
  lead='We biopsy the prostate through the perineum inside the wide-bore 3T MRI in AMIGO. The program serves men with rising PSA after negative ultrasound-guided biopsies and men with suspected recurrence, and the same setup is used for focal cryoablation.',
  glance=[('Scanner', '3T wide-bore (70 cm) MRI'), ('Software', '<a href="https://github.com/SlicerProstate/SliceTracker">SliceTracker</a> in 3D Slicer'), ('Also used for', 'MRI-guided focal cryoablation'), ('Clinical lead', 'Kemal Tuncali, MD [verify]')],
  sections=[
    ('How a case runs', '<ol><li><strong>Plan.</strong> A radiologist marks suspicious targets on the diagnostic MRI.</li><li><strong>Register.</strong> A calibration frame on the needle-guide template is imaged so 3D Slicer knows where every template hole is.</li><li><strong>Target.</strong> 3D Slicer picks the best hole and insertion depth for each target.</li><li><strong>Sample.</strong> The needle is inserted, its position confirmed on MRI and the core taken.</li></ol>'),
    ('Why the wide bore matters', '<p>The patient stays in the scanner while needles or cryoprobes are placed, so the plan made at the start lines up with every later image without re-registration.</p>'),
  ],
  contact='Kemal Tuncali, MD, and Junichi Tokuda, PhD [verify]',
  links=[('SliceTracker software', 'https://github.com/SlicerProstate/SliceTracker'), ('Open-source platform for in-bore MRI-guided biopsy (PubMed)', 'https://pubmed.ncbi.nlm.nih.gov/31135342/'), ('Clinical trials', 'page-clinical-trials.html')]),

'page-mri-guided-cryoablations-of-liver-and-kidney-tumors.html': dict(
  banner=('media/2023_01_cryo4a.jpg', 'Iceball around a tumor on MRI during cryoablation'),
  lead='Cryoablation destroys tumors by freezing them through needles placed in the skin. Under MRI the iceball is clearly visible, so the team can see that it covers the tumor and spares nearby organs.',
  glance=[('Treats', 'Kidney, liver, bone, lung, adrenal and prostate tumors'), ('Probes', '17-gauge argon cryoprobes'), ('Protocol', 'Freeze 15 min, thaw 10 min, freeze 15 min'), ('Margin goal', '5–10 mm around the tumor')],
  sections=[
    ('How a case runs', '<ol><li><strong>Plan.</strong> An MRI shows the tumor; the number and position of probes are chosen.</li><li><strong>Target.</strong> Probes are placed about 1.5 cm apart and checked on MRI before freezing.</li><li><strong>Monitor.</strong> The iceball appears dark on MRI and is watched until it covers the tumor plus margin.</li><li><strong>Survey.</strong> A final MRI confirms coverage and checks for complications.</li></ol>'),
    ('Why MRI', '<p>MRI shows the iceball edge during freezing, which is especially useful when the tumor sits next to bowel, nerves or other critical structures.</p>'),
  ],
  contact='[Interventional radiology contact]',
  links=[('MRI-guided prostate biopsy and cryoablation', 'page-mr-guided-prostate-biopsy.html'), ('Clinical trials', 'page-clinical-trials.html')]),

'page-gynecologic-hdr-brachytherapy.html': dict(
  banner=('media/2023_01_300px-insertedneedlemodel-e1675187676426.jpg', 'Model of brachytherapy catheters placed in a gynecologic tumor'),
  lead='For large gynecologic tumors, MRI in AMIGO guides the placement of radiation catheters directly into the tumor and away from healthy tissue, so each part of the tumor receives the right dose.',
  glance=[('Treats', 'Large cervical and other gynecologic tumors'), ('Imaging used', 'MRI, ultrasound, PET/CT'), ('Collaboration', 'Radiology and Radiation Oncology')],
  sections=[
    ('How a case runs', '<ol><li><strong>Assess.</strong> The patient is examined under anesthesia and an applicator is placed with ultrasound guidance.</li><li><strong>Place catheters.</strong> Needles are inserted through a template into the tumor.</li><li><strong>Check.</strong> MRI shows each needle relative to the tumor and organs; needles are adjusted as needed.</li><li><strong>Plan the dose.</strong> The final images are used for the radiation plan.</li></ol>'),
    ('Research', '<p>Biopsies taken during imaging allow imaging and pathology to be compared, with the goal of longer disease-free intervals and fewer long-term side effects.</p>'),
  ],
  contact='[Radiation oncology contact]',
  links=[('Gynecologic brachytherapy in AMIGO (talk, PDF)', 'media/2022_12_2012novembergynebrachy-in-amigo-mj.pdf'), ('About the AMIGO suite', 'page-amigo.html')]),

'page-parathyroidectomy.html': dict(
  banner=('media/2023_01_300px-parathyroid1-1.jpg', 'Navigation model of a parathyroid adenoma'),
  lead='Finding a parathyroid gland can be hard even for experienced surgeons, especially in repeat operations. In AMIGO the surgeon follows a navigation model of the gland and can check during the operation how much has been removed.',
  glance=[('Treats', 'Parathyroid adenomas; nerve mapping in thyroid surgery'), ('Imaging used', 'Preoperative sestamibi and ultrasound, intraoperative navigation'), ('Status', 'Clinical research')],
  sections=[
    ('The problem', '<p>Preoperative ultrasound and sestamibi scans are not always reliable, and there has been no imaging during surgery to find the gland.</p>'),
    ('What AMIGO adds', '<p>Navigation compares the planned model with the actual dissection, giving real-time feedback on location and completeness of resection. We have also mapped the recurrent laryngeal nerve, which controls the voice, ahead of thyroid surgery.</p>'),
  ],
  contact='[Endocrine surgery contact]',
  links=[('About the AMIGO suite', 'page-amigo.html'), ('Clinical trials', 'page-clinical-trials.html')]),

'page-video-assisted-thoracoscopic-surgeries-ivats.html': dict(
  banner=('media/2023_01_ivats1c.jpg', 'C-arm CT image used to mark a small lung nodule'),
  lead='Small lung nodules found on CT screening are hard to feel during surgery, which can mean removing more lung than needed. In AMIGO we mark the nodule with fiducials under C-arm CT just before thoracoscopic surgery, so the surgeon can remove it precisely.',
  glance=[('Treats', 'Small lung nodules that may be early cancer'), ('Imaging used', 'Intraoperative fluoroscopy and C-arm CT'), ('Benefit', 'Less normal lung removed, clear margins')],
  sections=[
    ('How a case runs', '<ol><li><strong>Mark.</strong> With the patient in the operating room, C-arm CT guides placement of fiducials around the nodule.</li><li><strong>Remove.</strong> The surgeon uses the fiducials to remove the nodule thoracoscopically.</li><li><strong>Confirm.</strong> Imaging and pathology confirm the nodule was removed with margin.</li></ol>'),
    ('Why it matters', '<p>Low-dose CT screening finds many more small nodules. A precise, safe way to remove them could benefit many patients as hybrid operating rooms become more common.</p>'),
  ],
  contact='[Thoracic surgery contact]',
  links=[('About the AMIGO suite', 'page-amigo.html'), ('Clinical trials', 'page-clinical-trials.html')]),

# ------------------------------------------------------------------ Research (earlier cycles)
'page-research.html': dict(
  banner=None, banner_note='Image: the center’s funding cycles on a timeline',
  lead='How the center’s research has been organized across its NIH funding cycles, from the four projects of 2015–2020 to the three projects of 2026–2030.',
  glance=[('2015–2020', 'Four TR&D projects: Prostate, Neurosurgery, Computation, Guidance'), ('2020–2025', 'Three TR&D projects: Imaging cancer heterogeneity, Deep learning, Intraoperative devices'), ('2026–2030', 'Three TR&D projects: High-fidelity MRI, Multiscale tumor analysis, Data-driven IGT')],
  sections=[
    ('2015–2020', '<p>Four projects. Prostate built molecular profiling and imaging markers to guide biopsy and focal therapy. Neurosurgery developed mass spectrometry and fMRI with diffusion tractography for surgical decisions. Computation built multimodal registration and motion compensation. Guidance built instrument and tumor tracking for moving, deforming organs.</p>'),
    ('2020–2025', '<p>Three projects. TR&amp;D 1 characterized tumors at macroscopic, microscopic and molecular scales. TR&amp;D 2 developed weakly supervised deep learning for brain, lung and prostate procedures and data curation tools. TR&amp;D 3 delivered devices through 3D Slicer and OpenIGTLink, including prostate needle guidance, lung navigation and implantable microdevices.</p>'),
    ('2026–2030', '<p>The current cycle: <a href="trd1.html">high-fidelity MRI</a>, <a href="trd2.html">implantable microdevices and multiscale tumor analysis</a>, and <a href="trd3.html">enabling technologies for data-driven image-guided therapy</a>.</p>'),
  ],
  contact='Center leadership, see <a href="people.html">People</a>',
  links=[('Current research', 'research.html'), ('History of the center', 'about.html#history')]),

'page-neurosurgery-core.html': dict(
  banner=None, banner_note='Image: tractography and tumor model for neurosurgical planning',
  lead='A project of the 2015–2020 cycle. It built tools to help neurosurgeons decide what to remove and what to preserve in brain tumor surgery.',
  glance=[('Cycle', '2015–2020'), ('Investigators', 'Alexandra Golby, MD; Nathalie Agar, PhD; Lauren O’Donnell, PhD'), ('Methods', 'Diffusion MRI, functional MRI, mass spectrometry')],
  sections=[
    ('Aims', '<ul><li>Map critical brain function for each patient by modeling functional and structural MRI together.</li><li>Define tumor margins during surgery with mass spectrometry as a molecular test.</li></ul>'),
    ('Where it went', '<p>This work continued in the 2020–2025 projects on imaging cancer heterogeneity and deep learning.</p>'),
  ],
  contact='Alexandra Golby, MD', links=[('Research overview by cycle', 'page-research.html'), ('Brain tumor resection in AMIGO', 'page-brain-tumor-resection.html')]),

'page-prostate-core.html': dict(
  banner=None, banner_note='Image: multiparametric prostate MRI with biopsy targets',
  lead='A project of the 2015–2020 cycle. It aimed to predict how aggressive a prostate cancer is and to sample it better at biopsy.',
  glance=[('Cycle', '2015–2020'), ('Investigators', 'Kemal Tuncali, MD; Fiona Fennessy, MD, PhD; Junichi Tokuda, PhD; Andriy Fedorov, PhD'), ('Methods', 'Multiparametric and hypoxia MRI, MRI-targeted biopsy, molecular pathology')],
  sections=[
    ('Aims', '<ul><li>Validate new imaging biomarkers against molecular and routine pathology.</li><li>Build a diagnostic platform to detect, characterize and grade prostate cancer for active surveillance and focal therapy.</li></ul>'),
    ('Where it went', '<p>The MRI-targeted biopsy platform is in clinical use in AMIGO, and the imaging work continues in TR&amp;D 1.</p>'),
  ],
  contact='Kemal Tuncali, MD', links=[('MRI-guided prostate biopsy', 'page-mr-guided-prostate-biopsy.html'), ('PI-RADS', 'page-prostate-image-reporting-and-data-system-pi-rads.html')]),

'page-guidance-core.html': dict(
  banner=None, banner_note='Image: electromagnetic and MRI tracking of instruments',
  lead='A project of the 2015–2020 cycle. It developed ways to guide therapy accurately in organs that move and deform during a procedure.',
  glance=[('Cycle', '2015–2020'), ('Investigators', 'Nobuhiko Hata, PhD; Jayender Jagadeesan, PhD; Junichi Tokuda, PhD'), ('Methods', 'Wireless electromagnetic sensors, MRI-tracked catheters, deformation models')],
  sections=[
    ('Aims', '<ul><li>An integrated navigation system to track the tumor and the instrument despite tissue deformation.</li><li>Miniature MRI tracking coils in needles and catheters for faster, more accurate placement.</li></ul>'),
    ('Where it went', '<p>This work continued in TR&amp;D 3, intraoperative devices, and in today’s data-driven image-guided therapy project.</p>'),
  ],
  contact='Nobuhiko Hata, PhD', links=[('Research overview by cycle', 'page-research.html'), ('TR&D 3 today', 'trd3.html')]),

'page-computation-core.html': dict(
  banner=None, banner_note='Image: multimodal image registration',
  lead='A project of the 2015–2020 cycle. It built image registration and motion-compensation methods that the other projects relied on.',
  glance=[('Cycle', '2015–2020'), ('Investigators', 'William Wells, PhD; Bruno Madore, PhD'), ('Methods', 'Multimodal registration, motion compensation hardware')],
  sections=[
    ('Aims', '<ul><li>Register preoperative and intraoperative images of different types.</li><li>Compensate for patient motion to improve tumor localization and functional mapping.</li></ul>'),
    ('Where it went', '<p>The registration work continued in TR&amp;D 2, deep learning, in 2020–2025.</p>'),
  ],
  contact='William Wells, PhD', links=[('Research overview by cycle', 'page-research.html'), ('Fast Imaging Library', 'page-fast-imaging-library.html')]),

'page-prostate-image-reporting-and-data-system-pi-rads.html': dict(
  banner=None, banner_note='Image: PI-RADS scoring on prostate MRI',
  lead='PI-RADS is a scoring system for reading and reporting prostate MRI consistently. The center has used it clinically and studied how to improve it.',
  glance=[('Version', 'PI-RADS v2 (2015) and later'), ('At BWH', 'All prostate MRI follows PI-RADS'), ('Related project', 'Prostate Core, 2015–2020')],
  sections=[
    ('What PI-RADS does', '<p>Multiparametric prostate MRI combines T2-weighted, diffusion-weighted and contrast-enhanced images. PI-RADS gives a common way to score and report what they show.</p>'),
    ('Our work', '<ul><li>Clinical evidence for evaluating and refining PI-RADS.</li><li>Using PI-RADS in the evaluation protocol for MRI-targeted biopsy.</li></ul>'),
  ],
  contact='Fiona Fennessy, MD, PhD [verify]', links=[('Prostate Core', 'page-prostate-core.html'), ('MRI-guided prostate biopsy', 'page-mr-guided-prostate-biopsy.html')]),

# ------------------------------------------------------------------ Resources
'page-fast-imaging-library.html': dict(
  banner=None, banner_note='Image: accelerated MRI reconstruction',
  lead='A C and Matlab library for reconstructing accelerated MRI data, with a reference manual and demos.',
  glance=[('Latest version', '2.2, January 19, 2015'), ('Platforms', 'Windows, macOS, Linux'), ('Languages', 'C and Matlab (MEX)'), ('Support', 'ncigt-imaging-toolkit at bwh.harvard.edu')],
  sections=[
    ('What it does', '<ul><li>UNFOLD</li><li>Parallel imaging: SENSE, variable-density SENSE, regularized SPACE RIP, GRAPPA, GROG</li><li>Homodyne partial-Fourier processing, gradient nonlinearity correction (gradwarp), Nyquist ghost correction</li></ul>'),
    ('Where it is used', '<p>Reconstruction of EPI data in z-shimmed functional imaging at BWH; earlier, temperature monitoring and prostate biopsy tracking in the center.</p>'),
    ('Download version 2.2', '<div class="tbl"><table><thead><tr><th>Platform</th><th>Package</th></tr></thead><tbody><tr><td>Windows 64-bit</td><td><a href="media/2023_01_ncigt_fil_v2.2_20150119_mswin64.zip">library</a> · <a href="media/2023_01_ncigt_fil_v2.2_20150119_mswin64_mex.zip">MEX files</a></td></tr><tr><td>macOS 64-bit</td><td><a href="media/2023_01_ncigt_fil_v2.2_20150119_darwin_x64.zip">library</a></td></tr><tr><td>Linux 64-bit</td><td><a href="media/2023_01_ncigt_fil_v2.2_20150119_x64_0.zip">library</a></td></tr><tr><td>Linux 32-bit</td><td><a href="media/2023_01_ncigt_fil_v2.2_20150119_x32.zip">library</a></td></tr></tbody></table></div><p>Read the <a href="http://projects.iq.harvard.edu/files/ncigt/files/ncigt_fil_license.txt?m=1437067676">license</a> before use. Version 2.0 (2014) is available on request.</p>'),
  ],
  contact='ncigt-imaging-toolkit at bwh.harvard.edu', links=[('Software and tutorials', 'resources.html#software'), ('Computation Core (earlier cycle)', 'page-computation-core.html')]),

'page-online-lectures.html': dict(
  banner=None, banner_note='Image: a lecture in the Ferenc Jolesz seminar series',
  lead='Free recordings and slides of talks by center investigators and seminar speakers, from 2014 to today.',
  glance=[('Lectures', '50, from 2014 to 2026'), ('Series', 'Ferenc Jolesz Research Seminars, invited keynotes, lecture series'), ('Also on', '<a href="https://www.youtube.com/@bwhncigt">NCIGT YouTube channel</a>')],
  sections=[],
  data=('All lectures', 'lectures'),
  contact='Marianna Jakab, webmaster [verify]', links=[('Research seminars', 'page-seminars.html'), ('NCIGT YouTube channel', 'https://www.youtube.com/@bwhncigt')]),

# ------------------------------------------------------------------ Training
'page-trainees.html': dict(
  banner=None, banner_note='Photo: center trainees in the AMIGO suite',
  lead='Over more than two decades the center has trained clinicians and scientists in image-guided therapy. This roster lists current trainees and where our graduates are now.',
  glance=[('Graduated since 2001', '358'), ('Training now', '13'), ('Programs', 'NCIGT, AT-NCIGT, T32 and R25')],
  sections=[],
  data=('Roster', 'trainees'),
  contact='Marianna Jakab, who keeps trainee records [verify]', links=[('Where training with us can lead', 'index.html#training'), ('T32 training program', 'page-training-in-image-guidance-precision-diagnosis-and-therapy.html'), ('Postdoctoral and visiting scholars', 'page-visiting-scholars-program.html')]),

'page-visiting-scholars-program.html': dict(
  banner=None, banner_note='Photo: visiting scholars with center investigators',
  lead='Clinicians and scientists from other institutions can join a center laboratory for research training, from a few months to two years.',
  glance=[('Who', 'Physicians, engineers and scientists, students to faculty'), ('Length', '[3 months to 2 years]'), ('Funding', '[Self-funded or sponsored by the home institution]'), ('Apply', '<a href="http://goo.gl/M8oiE2">Online form</a>')],
  sections=[
    ('What you do here', '<p>[Work on a project in a center laboratory, attend lab meetings and the Ferenc Jolesz Research Seminars, and observe procedures in the AMIGO suite.]</p>'),
    ('How to apply', '<ol><li>Fill out the <a href="http://goo.gl/M8oiE2">visiting scholar form</a>.</li><li>[We match you with an investigator whose work fits your interests.]</li><li>[The host investigator arranges the appointment with the hospital.]</li></ol>'),
  ],
  contact='[Visiting scholars contact]', links=[('Trainees and alumni', 'page-trainees.html'), ('T32 training program', 'page-training-in-image-guidance-precision-diagnosis-and-therapy.html')]),

'page-training-in-image-guidance-precision-diagnosis-and-therapy.html': dict(
  banner=None, banner_note='Photo: T32 fellows with their mentors',
  lead='An NIH-funded two-year postdoctoral program at Brigham and Women’s Hospital and Harvard Medical School that trains MD and PhD investigators at the meeting point of medicine and technology.',
  glance=[('Grant', 'T32EB025823 (NIBIB)'), ('Positions', 'Four postdoctoral fellows, two years each'), ('Co-directors', 'Lauren O’Donnell, PhD; Fiona Fennessy, MD, PhD'), ('Applications', 'Rolling')],
  sections=[
    ('The program', '<p>Each fellow has a technical and a clinical mentor and works on research spanning engineering, computer science, imaging, AI, multiomics, surgical robotics and targeted therapeutics, with career development toward an independent research career. Krisztina Fischer, MD, PhD, is Director of Education.</p>'),
    ('Research themes', '<ol><li>Multiomics for IGT: radiomics, pathomics, metabolomics</li><li>Advanced MR and computational image science</li><li>Microdevices and surgical robotics</li><li>Targeted brain therapeutics</li><li>Machine learning for robust sensing and imaging</li><li>Cross-scale biomarker integration</li></ol>'),
    ('Eligibility', '<p>An MD, PhD or equivalent doctorate; MD applicants must have completed residency. Under NIH rules, fellows must be U.S. citizens, noncitizen nationals or permanent residents when appointed. Pay follows BWH postdoctoral guidelines.</p>'),
    ('How to apply', '<p>Email Lauren O’Donnell, PhD, at <a href="mailto:odonnell@bwh.harvard.edu">odonnell@bwh.harvard.edu</a> with your CV; a statement of your career goals and how the program fits them; your research interests and possible mentors; three references; and confirmation of citizenship or permanent residency. Selected applicants are invited to interview.</p>'),
  ],
  contact='Lauren O’Donnell, PhD, <a href="mailto:odonnell@bwh.harvard.edu">odonnell@bwh.harvard.edu</a>', links=[('Trainees and alumni', 'page-trainees.html'), ('Postdoctoral and visiting scholars', 'page-visiting-scholars-program.html')]),

'page-training-and-dissemination.html': dict(
  banner=None, banner_note='Photo: a hands-on workshop at Project Week',
  lead='The core that shares the center’s technology: it trains clinicians and researchers, and it informs the wider community through workshops, Project Week, seminars and online material.',
  glance=[('Lead', 'Carl-Fredrik Westin, PhD'), ('Members', 'Clare Tempany, MD; Nobuhiko Hata, PhD'), ('Mandate', 'NIBIB requires P41 centers to train and disseminate')],
  sections=[
    ('Training', '<ul><li><a href="page-training-in-image-guidance-precision-diagnosis-and-therapy.html">T32 training program</a></li><li><a href="page-trainees.html">Trainees and alumni</a></li><li><a href="page-visiting-scholars-program.html">Postdoctoral and visiting scholars</a></li><li><a href="page-online-lectures.html">Online lectures</a> and <a href="resources.html#software">software tutorials</a></li></ul>'),
    ('Dissemination', '<ul><li><a href="page-national-image-guided-therapy-workshops.html">National IGT Workshops</a></li><li><a href="page-project-week.html">Project Week</a></li><li><a href="page-seminars.html">Research seminars</a></li></ul>'),
  ],
  contact='Carl-Fredrik Westin, PhD', links=[('Training', 'training.html'), ('News & events', 'news.html')]),

# ------------------------------------------------------------------ Partner
'page-collaborations.html': dict(
  banner=None, banner_note='Image: map of collaborating institutions',
  lead='Collaborations with NIH-funded researchers bring the center’s technology to new clinical problems, from radiation therapy and brain tumors to abdominal surgery and focused ultrasound.',
  glance=[('Who', 'NIH-funded research groups, local to international'), ('How', 'Collaborative and service projects'), ('Current list', '<a href="https://docs.google.com/spreadsheets/d/164wpD66JnQGLkx3Zu1zDsLv5Z-OPmU94tEH8X0hBaKI">Spreadsheet</a>')],
  sections=[
    ('How we choose', '<ul><li>A match with our skills, resources and expertise</li><li>NIH-funded projects</li><li>Projects that lead to clinical translation</li><li>Projects from academic institutions and from U.S. regions under-represented in NIH funding</li></ul>'),
    ('How to start', '<p>Submit the <a href="http://docs.google.com/forms/d/1Wg2Uv5YAkJjEmqjgeGzPtQoS7_AaFJdsjMWFeg-KKZs/viewform">collaboration application form</a>, or see <a href="partner.html">Partner with us</a> for the three steps from a first conversation to a formal project.</p>'),
  ],
  contact='The center, see <a href="about.html#contact">Contact</a>', links=[('Partner with us', 'partner.html'), ('Collaborative and service projects', 'partner.html#partner-research'), ('Working with industry', 'industry.html')]),

# ------------------------------------------------------------------ News & events
'page-seminars.html': dict(
  banner=('media/2023_01_ferencjolesz-e1717450291199.jpg', 'Ferenc Jolesz, MD'),
  lead='A monthly seminar series of the Department of Radiology with speakers from Harvard Medical School and beyond on topics related to image-guided therapy. It honors Ferenc Jolesz, MD, who founded the image-guided therapy program at Brigham and Women’s Hospital.',
  glance=[('When', 'First Monday of the month [time]'), ('Where', '[Room], Brigham and Women’s Hospital, and Zoom'), ('Open to', 'Everyone; no registration')],
  sections=[('Upcoming', '<p>[Next seminar: speaker, title, date.]</p>')],
  data=('Past seminars', 'seminars'),
  contact='[Seminar organizer]', links=[('Online lectures', 'page-online-lectures.html'), ('News and seminars', 'news.html')]),

'page-national-image-guided-therapy-workshops.html': dict(
  banner=('media/2023_01_ncigtwscomposite.jpg', 'Scenes from National IGT Workshops'),
  lead='A national workshop series, organized by the center with NIH, on the needs and opportunities in image-guided interventions. Each workshop has a single track of invited and submitted talks and a poster session.',
  glance=[('Editions', '12, most recently 2022'), ('Latest', '289 registrants, including 29 NIH staff and 48 from industry'), ('Next', '13th workshop [date]')],
  sections=[('Format', '<p>Plenary lectures by leaders in the field, oral presentations selected from abstracts, and fellow and postdoc presentations.</p>')],
  data=('Past workshops', 'workshops'),
  contact='[Workshop organizer]', links=[('Programs of past workshops', 'page-past-igt-workshops.html'), ('iMRI Symposium', 'page-imri-2024.html')]),

'page-past-igt-workshops.html': dict(
  banner=('media/2023_01_map_of_the_10th_ncigt_workshop_2018-geographic_distribution_of_attendees-mj100918.png', 'Where attendees of the 10th workshop came from'),
  lead='Summaries of earlier National Image Guided Therapy Workshops.',
  glance=[('Editions', '12'), ('Most recent', '12th, May 19, 2022, virtual'), ('Format', 'Plenaries, oral talks, posters')],
  sections=[],
  data=('Workshops', 'workshops_full'),
  contact='[Workshop organizer]', links=[('National IGT Workshops', 'page-national-image-guided-therapy-workshops.html')]),

'page-imri-2024.html': dict(
  banner=('media/2023_11_Save-the-Date-iMRI24-Final.png', 'Save the date for iMRI 2024'),
  lead='The 14th Interventional MRI Symposium on the use of MRI to plan, control and monitor surgical and radiological interventions. The series is co-organized by the Brigham and endorsed by ISMRM and ESMRMB.',
  glance=[('Dates', 'October 17–18, 2024'), ('Place', 'Graduate Hotel, Annapolis, Maryland'), ('Host', 'Johns Hopkins, with Leipzig, Brigham and Women’s and Emory'), ('Next', '15th symposium, October 8–9, 2026, Boston')],
  sections=[
    ('Topics', '<p>Interventional MRI systems and hybrid designs, instrumentation, pulse sequences, visualization, navigation, robotics, MR thermometry and thermal ablation, MR-guided biopsy, molecular imaging, cellular therapies and targeted drug delivery.</p>'),
    ('Organizers', '<p>Local chairs Clifford Weiss and Dara Kraitchman (Johns Hopkins), with Thomas Kahn (Leipzig), Clare Tempany (Harvard Medical School) and Jonathan Lewin (Emory).</p>'),
  ],
  contact='<a href="mailto:cweiss@jhmi.edu">cweiss@jhmi.edu</a> or <a href="mailto:dkraitc1@jhmi.edu">dkraitc1@jhmi.edu</a>', links=[('iMRI 2026 website', 'https://imri2026.org'), ('iMRI Symposium 2022', 'page-imri-symposium-2022.html')]),

'page-imri-symposium-2022.html': dict(
  banner=('media/2023_01_mri_2022_first_announcement.jpg', 'First announcement of iMRI 2022'),
  lead='The 13th Interventional MRI Symposium, held in Leipzig, Germany, the first since Boston in 2018.',
  glance=[('Edition', '13th'), ('Place', 'Leipzig, Germany'), ('Organizers', 'Leipzig University Hospital, Brigham and Women’s Hospital, Johns Hopkins'), ('Endorsed by', 'ISMRM and ESMRMB')],
  sections=[('About', '<p>Technical and clinical sessions with invited lectures and submitted papers, in cooperation with Hannover Medical School, the University of Magdeburg and Emory Healthcare, and supported by the center.</p>')],
  contact='[Organizer]', links=[('iMRI Symposium 2024', 'page-imri-2024.html')]),

'page-project-week.html': dict(
  banner=('media/2024_08_PW40-scaled-e1722871057686.jpg', 'Participants at Project Week 40'),
  lead='A twice-yearly, week-long hackathon where 80 to 120 people work together on open-source medical imaging software. The focus is making progress on projects, not reporting on them.',
  glance=[('How often', 'Twice a year, January and June'), ('Size', '80–120 participants'), ('Endorsed by', 'MICCAI, since 2014'), ('Next', 'Project Week 46, January 25–29, 2027, Gran Canaria')],
  sections=[
    ('How it works', '<p>Everyone arrives with a project: some work on the platform, some on algorithms, some apply tools to their own research. The week opens with project introductions, mixes working sessions with breakout topics such as image-guided therapy, and closes with each team reporting what it achieved.</p>'),
    ('Who takes part', '<p>Funded projects including NAC, AT-NCIGT, QIICR, SlicerIGT and OpenIGTLink use Project Week to meet and collaborate. It is open to all and paid for by attendee fees.</p>'),
  ],
  contact='[Project Week contact]', links=[('Project Week website', 'https://projectweek.na-mic.org/'), ('Software and tutorials', 'resources.html#software')]),

'page-robsai.html': dict(
  banner=None, banner_note='Image: robotics and imaging at the point of care',
  lead='A MICCAI 2023 workshop on robotics, AI and imaging for surgical guidance at the point of care, organized by center investigators.',
  glance=[('Date', 'October 8, 2023, virtual, at MICCAI'), ('Organizers', 'Laura Brattain, Jayender Jagadeesan, Tina Kapur'), ('Papers', 'Peer reviewed, 8 pages')],
  sections=[('Topics', '<ul><li>Robotics, AI and imaging for surgical guidance</li><li>Image-guided navigation and visualization</li><li>Machine learning for therapy guidance and decisions</li><li>New sensors for point-of-care guidance</li><li>Clinical translation and evaluation</li></ul>')],
  contact='Jayender Jagadeesan, PhD', links=[('Meetings we organize', 'news.html'), ('TR&D 3', 'trd3.html')]),

# ------------------------------------------------------------------ About
'page-history.html': dict(
  banner=('media/2025_02_History.jpg', 'Timeline of image-guided therapy research at the Brigham'),
  lead='Image-guided therapy at Brigham and Women’s Hospital grew from the first interventional MRI in the early 1990s into the NCIGT, the AMIGO suite and today’s AT-NCIGT.',
  glance=[('Founder', 'Ferenc A. Jolesz, MD (1946–2014)'), ('NCIGT', 'NIH P41EB015898'), ('AT-NCIGT', 'NIH P41EB028741, 2021 onward'), ('AMIGO', 'Opened 2011')],
  sections=[
    ('Milestones', '<p>[A short timeline taken from the figure above: first open-configuration interventional MRI; MR-guided focused ultrasound; founding of NCIGT; opening of AMIGO; AT-NCIGT.]</p>'),
    ('Funding cycles', '<p>See <a href="about.html#history">History of the center</a> for each NIH funding cycle and its leaders.</p>'),
  ],
  contact='The center, see <a href="about.html#contact">Contact</a>', links=[('History of the center', 'about.html#history'), ('Research overview by cycle', 'page-research.html')]),
}

# carried-over pages that duplicate newer pages: replaced by a pointer
REDIRECTS = {
  'page-home.html': ('index.html', 'Home'),
  'page-news.html': ('news.html', 'News and seminars'),
  'page-events.html': ('news.html', 'News & events'),
  'page-people.html': ('people.html', 'People'),
  'page-team.html': ('people.html', 'People'),
  'page-software-and-tutorials.html': ('resources.html#software', 'Resources: software, tutorials and data'),
  'page-publications.html': ('publications.html', 'Publications'),
  'page-acs.html': ('page-seminars.html', 'Research seminars'),
  'page-trd-1-imaging-cancer-heterogeneity.html': ('trd1.html', 'TR&D 1'),
  'page-trd-2-deep-learning.html': ('trd2.html', 'TR&D 2'),
  'page-trd-3-intraoperative-devices.html': ('trd3.html', 'TR&D 3'),
  'page-eligibility.html': ('page-training-in-image-guidance-precision-diagnosis-and-therapy.html#eligibility', 'T32 training program: eligibility'),
  'page-application.html': ('page-training-in-image-guidance-precision-diagnosis-and-therapy.html#how-to-apply', 'T32 training program: how to apply'),
}
