"""The site's hierarchy: every page belongs to exactly one section (and optionally a parent page).

Used by restyle.py (breadcrumbs, section side navigation) and build_sections.py
(section landing pages, site map). The top menu (megamenu.py) may also link a page
from a second tab, but its breadcrumb always follows this tree.

Item: (file, title, one-line note, children)
"""
SECTIONS = [
  dict(key='research', label='Research', landing='research.html',
       blurb='Three technology research and development (TR&D) projects, their publications, and the research of earlier funding cycles.',
       groups=[
         ('Current projects', [
           ('trd1.html', 'TR&D 1: Imaging cancer heterogeneity', 'Advanced diffusion and CEST MRI', []),
           ('trd2.html', 'TR&D 2: Implantable microdevices', 'Testing drugs inside the tumor', []),
           ('trd3.html', 'TR&D 3: Enabling technologies', 'Robotic guidance and AR navigation', []),
         ]),
         ('Results', [
           ('publications.html', 'Publications', 'Major achievements and collaborations, past 12 months', []),
         ]),
         ('Earlier funding cycles', [
           ('page-research.html', 'Research by funding cycle', 'How the research was organized, 2015 to today', []),
           ('page-neurosurgery-core.html', 'Neurosurgery Core', 'NCIGT core, earlier cycle', []),
           ('page-prostate-core.html', 'Prostate Core', 'NCIGT core, earlier cycle', []),
           ('page-guidance-core.html', 'Guidance Core', 'NCIGT core, earlier cycle', []),
           ('page-computation-core.html', 'Computation Core', 'NCIGT core, earlier cycle', []),
           ('page-prostate-image-reporting-and-data-system-pi-rads.html', 'PI-RADS', 'Prostate Image Reporting and Data System', []),
         ]),
       ]),
  dict(key='people', label='People', landing='people.html',
       blurb='The investigators, staff and advisors of the center.',
       groups=[
       ]),
  dict(key='amigo', label='AMIGO', landing='clinical.html',
       blurb='The AMIGO suite and the clinical research that uses it.',
       groups=[
         ('The suite', [
           ('page-amigo.html', 'About the AMIGO suite', 'MRI, PET/CT and X-ray in one procedure suite', []),
           ('page-amigoprocedures.html', 'Procedures in AMIGO', 'Procedures that are part of clinical trials', []),
           ('page-clinical-trials.html', 'Clinical trials', 'Current and completed studies', []),
         ]),
         ('Clinical programs', [
           ('page-brain-tumor-resection.html', 'Brain tumor resection', 'Intraoperative MRI for neurosurgery', []),
           ('page-breast-cancer-surgery.html', 'Breast cancer surgery', 'Supine MRI for breast-conserving surgery', []),
           ('page-mr-guided-prostate-biopsy.html', 'MRI-guided prostate biopsy', 'Transperineal biopsy in the wide-bore 3T MRI', []),
           ('page-mri-guided-cryoablations-of-liver-and-kidney-tumors.html', 'MRI-guided cryoablation of liver and kidney tumors', 'Freezing tumors under MRI guidance', []),
           ('page-gynecologic-hdr-brachytherapy.html', 'Gynecologic HDR brachytherapy', 'Image-guided radiation for large tumors', []),
           ('page-parathyroidectomy.html', 'Parathyroidectomy', 'Locating parathyroid glands during surgery', []),
           ('page-video-assisted-thoracoscopic-surgeries-ivats.html', 'Image-guided thoracoscopic surgery (iVATS)', 'Removing small lung nodules', []),
         ]),
       ]),
  dict(key='resources', label='Resources', landing='resources.html',
       blurb='Software, data, equipment and recorded lectures that the center shares.',
       groups=[
         (None, [
           ('page-fast-imaging-library.html', 'Fast Imaging Library', 'Reconstruction code for accelerated MRI', []),
           ('page-online-lectures.html', 'Online lectures', 'Free recorded talks and seminars', []),
         ]),
       ]),
  dict(key='training', label='Training', landing='training.html',
       blurb='Training at the center, the people it has trained, and where they went.',
       groups=[
         (None, [
           ('page-trainees.html', 'Trainees and alumni', 'Our roster since 2001 and where alumni went', []),
           ('page-visiting-scholars-program.html', 'Postdoctoral and visiting scholars', 'Train with us for months or years', []),
           ('page-training-in-image-guidance-precision-diagnosis-and-therapy.html', 'T32 training program', 'Image Guidance, Precision Diagnosis and Therapy', []),
           ('page-training-and-dissemination.html', 'Training and dissemination core', 'Who leads training and dissemination', []),
         ]),
       ]),
  dict(key='partner', label='Partner with us', landing='partner.html',
       blurb='How to work with the center, from a first conversation to a formal project.',
       groups=[
         (None, [
           ('industry.html', 'Working with industry', 'From a clinical need to a device ready for patients', []),
           ('page-collaborations.html', 'Collaborations', 'Current and past NIH-funded collaborations', []),
         ]),
       ]),
  dict(key='news', label='News & events', landing='news.html',
       blurb='News, seminars and the meetings the center organizes.',
       groups=[
         ('Seminars', [
           ('page-seminars.html', 'Research seminars', 'The Ferenc Jolesz Research Seminar Series', []),
         ]),
         ('Meetings we organize', [
           ('page-national-image-guided-therapy-workshops.html', 'National IGT Workshops', 'Our national image-guided therapy workshop series', [
             ('page-past-igt-workshops.html', 'Past workshops', 'Programs of earlier workshops', []),
           ]),
           ('page-imri-2024.html', 'iMRI Symposium 2024', 'The interventional MRI meeting we co-organize', []),
           ('page-imri-symposium-2022.html', 'iMRI Symposium 2022', 'The previous edition', []),
           ('page-project-week.html', 'Project Week', 'Twice-yearly open-source hackathon', []),
           ('page-robsai.html', 'RobsAI workshop, MICCAI 2023', 'Robotics, AI and imaging for point-of-care surgical guidance', []),
         ]),
       ]),
  dict(key='about', label='About', landing='about.html',
       blurb='The center, its home at Mass General Brigham, and its history.',
       groups=[
         (None, [
           ('page-history.html', 'Image-guided therapy research at the Brigham', 'How image-guided therapy began here', []),
           ('sitemap.html', 'All pages', 'The complete site, section by section', []),
         ]),
       ]),
]
HIDDEN = set()   # empty page on the previous website

def walk():
    """yield (section, group_title, item, parent_item) for every page in the tree"""
    for sec in SECTIONS:
        for gt, items in sec['groups']:
            for it in items:
                yield sec, gt, it, None
                for ch in it[3]:
                    yield sec, gt, ch, it

def lookup(f):
    for sec, gt, it, parent in walk():
        if it[0] == f:
            return sec, gt, it, parent
    for sec in SECTIONS:
        if sec['landing'] == f:
            return sec, None, None, None
    return None
