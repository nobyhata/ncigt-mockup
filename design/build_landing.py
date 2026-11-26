"""Section landing pages (research, clinical, resources, training, partner, about) in the same
template as every content page: banner, lead, At a glance, sections, contact and links, with the
section's side navigation. Data comes from Main.dc.html, the single source the home page also uses;
the home page shows only a short summary of each section and links here.

    python3 design/build_landing.py
"""
import os, re, sys, html, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import sitetree, restyle

def esc(s): return html.escape(str(s), quote=True)

def main_data():
    src = open(os.path.join(HERE, 'render.py')).read()
    ns = {}; exec(src[:src.index('links = {')], ns)
    return ns['data_of'](open(os.path.join(HERE, 'Main.dc.html'), encoding='utf-8').read())

def link(h):
    return {'TRD1.dc.html': 'trd1.html', 'TRD2.dc.html': 'trd2.html', 'TRD3.dc.html': 'trd3.html'}.get(h, h)

def banner(src, alt, ph=None):
    if src:
        return f'<figure class="banner"><img src="{esc(src)}" alt="{esc(alt)}" loading="lazy"><figcaption>{esc(alt)}</figcaption></figure>'
    return f'<figure class="banner ph" aria-label="Picture to come"><span>[{esc(ph)}]</span></figure>'

def glance(rows):
    return '<section class="glance"><h2>At a glance</h2><dl>' + ''.join(f'<div><dt>{esc(k)}</dt><dd>{v}</dd></div>' for k, v in rows) + '</dl></section>'

def cards(items):
    """items: (kicker, title, text, href or '')"""
    out = []
    for k, t, x, h in items:
        tag, attr = ('a', f' href="{esc(h)}"') if h else ('div', '')
        out.append(f'<{tag} class="card"{attr}>' + (f'<span class="kicker">{esc(k)}</span>' if k else '') + f'<strong>{esc(t)}</strong>' + (f'<span>{esc(x)}</span>' if x else '') + f'</{tag}>')
    return '<div class="cards">' + ''.join(out) + '</div>'

def pages_block(sec):
    out = []
    for gt, items in sec['groups']:
        if not items: continue
        if gt: out.append(f'<h3>{esc(gt)}</h3>')
        out.append(cards([('', it[1], it[2], it[0]) for it in items]))
    return ('<h2>Pages in this section</h2>' + ''.join(out)) if out else ''

def nextblock(contact, links):
    return ('<section class="next"><h2>Contact and links</h2><p><strong>Contact:</strong> ' + contact + '</p>' +
            cards([('', t, '', h) for t, h in links]) + '</section>')

def build(d):
    P = {}
    trd_cards = [(t['tag'], t['title'], t['problem'] + ' Project lead: ' + t['lead'] + '.', link(t['page'])) for t in d['trds']]
    # ---------------- Research
    P['research'] = dict(
        banner=banner(d['trds'][0]['fig'], d['trds'][0]['figcap']),
        lead='The center’s research is organized into three technology research and development (TR&amp;D) projects. Each takes a clinical problem from new technology to testing in patients, and each works with collaborating teams who use and shape that technology.',
        glance=[('Funding cycle', '2026–2030, NIH NIBIB 2P41EB028741'), ('Projects', '3 TR&amp;D projects'), ('Clinical test bed', '<a href="clinical.html">AMIGO suite</a>'), ('Publications', '<a href="publications.html">Past 12 months</a>')],
        body=[('Projects', cards(trd_cards)),
              ('Latest results', cards([(m['venue'] + ' · ' + m['project'], m['title'], m['why'], m['doi']) for m in d['major'][:4]]) + '<p><a class="more" href="publications.html">All publications, past 12 months →</a></p>')],
        contact='The project leads named above, or the center through <a href="about.html#contact">Contact</a>',
        links=[('Partner with us', 'partner.html'), ('Research by funding cycle', 'page-research.html')])
    # ---------------- AMIGO
    P['amigo'] = dict(
        banner=banner('media/2022_12_amigo-mriroom.jpg', 'The MRI room of the AMIGO suite'),
        lead='The Advanced Multimodality Image Guided Operating (AMIGO) suite combines MRI, PET/CT and X-ray imaging with a fully equipped operating room, so imaging, navigation and robotics research can take place during clinical procedures. Clinical investigators across Brigham and Women’s Hospital use it and the center’s resources in their own studies.',
        glance=[('Opened', '2011'), ('Rooms', 'MRI, operating room, PET/CT'), ('Research time', 'Fridays reserved for technical research'), ('Clinical areas', str(len(d['clinical'])) + ' areas with active studies')],
        body=[('Clinical studies using the center', cards([('', c['field'], c['what'] + ' ' + c['people'], '') for c in d['clinical']]))],
        contact='Alexandra Golby, MD, clinical director and co-medical director [verify current directors]',
        links=[('About the AMIGO suite', 'page-amigo.html'), ('Clinical trials', 'page-clinical-trials.html')])
    # ---------------- Resources
    sw = [('Software', '3D Slicer', 'The open platform behind our navigation tools', 'http://download.slicer.org/'),
          ('Software', 'OpenIGTLink', 'Connects devices in the operating room', 'http://openigtlink.org/'),
          ('Software', 'ROS for Medical Robotics (ROS-MED)', 'Robot software for image-guided interventions', 'https://rosmed.github.io/'),
          ('Software', 'TCIA Browser', 'Load Cancer Imaging Archive data into 3D Slicer', 'https://github.com/QIICR/TCIABrowser'),
          ('Tutorials', 'SlicerIGT tutorials', 'Building navigation systems with 3D Slicer', 'http://www.slicerigt.org/wp/user-tutorial/'),
          ('Tutorials', 'All 3D Slicer tutorials', 'From basic use to development', 'https://training.slicer.org/'),
          ('Tutorials', 'Perk Tutor', 'Training platform for image-guided interventions', 'http://perktutor.github.io/index.html'),
          ('Tutorials', 'Video playlists and demos', 'Recorded demonstrations', 'http://www.youtube.com/channel/UC11x1iQ7ydSIFYw4L6wveXg/playlists'),
          ('Data', 'Prostate MR Image Database', 'Prostate MRI for research', 'http://prostatemrimagedatabase.com/Database/index.html'),
          ('Data', 'ReMIND', 'Brain resection multimodal imaging, on TCIA', 'https://www.cancerimagingarchive.net/collection/remind/'),
          ('Data', 'Surgical Navigation and Robotics Laboratory data', 'Datasets and open-source software', 'https://snr.spl.harvard.edu/data/')]
    P['resources'] = dict(
        banner=banner(None, '', 'Photo: equipment in a center laboratory'),
        lead='Equipment, software, tutorials and data that the center shares. Equipment is available to collaborators through the investigator who runs it; software and data are open to everyone.',
        glance=[('Equipment', str(len(d['equip'])) + ' shared facilities'), ('Software', 'Open source, built on 3D Slicer'), ('Data', 'Prostate MRI, ReMIND brain resection'), ('Lectures', '<a href="page-online-lectures.html">50 recorded talks</a>')],
        body=[('Equipment and tools', cards([('Contact: ' + e['who'], e['name'], e['what'], '') for e in d['equip']])),
              ('Recently shared', cards([(h['kind'], h['name'], h['what'], '') for h in d['shared']])),
              ('Software, tutorials and data', cards(sw))],
        contact='The investigator named on each piece of equipment; for software, the project leads',
        links=[('Fast Imaging Library', 'page-fast-imaging-library.html'), ('Online lectures', 'page-online-lectures.html')])
    # ---------------- Training
    P['training'] = dict(
        banner=banner(None, '', 'Photo: trainees in the AMIGO suite'),
        lead='Clinical and technical trainees work alongside center investigators on real clinical problems. Many go on to independent careers in academic medicine, engineering and industry.',
        glance=[('Graduated since 2001', '<a href="page-trainees.html">358</a>'), ('Training now', '13'), ('Postdoctoral program', '<a href="page-training-in-image-guidance-precision-diagnosis-and-therapy.html">NIH T32, four positions</a>'), ('Visiting scholars', '<a href="page-visiting-scholars-program.html">Apply online</a>')],
        body=[('Where training with us can lead', cards([(a['path'], a['name'], a['story'], a['grant']) for a in d['alumni']]))],
        contact='Lauren O’Donnell, PhD, for the T32 program; Marianna Jakab for trainee records [verify]',
        links=[('Trainees and alumni', 'page-trainees.html'), ('Project Week hackathons', 'page-project-week.html')])
    # ---------------- Partner
    P['partner'] = dict(
        banner=banner(None, '', 'Photo: center investigators with a partner team'),
        lead='We work with research groups at many sites through collaborative and service projects. In this cycle we especially welcome partnerships that connect with our three projects, but any part of our methods, tools or technology can be a starting point.',
        glance=[('Who', 'Academic groups and companies'), ('Formal projects', 'Collaborative or service project, for groups with active funded research'), ('Industry', 'NIH SBIR and STTR experience'), ('Start', '<a href="page-collaborations.html">Collaboration form</a>')],
        body=[('How to start', cards([('Step ' + s['n'], s['title'], s['text'], '') for s in d['steps']])),
              ('Where your work could connect', cards([(t['tag'], t['title'], 'Talk to ' + t['lead'] + '.', link(t['page'])) for t in d['trds']])),
              ('Two kinds of formal project', cards([('', 'Collaborative project', 'Your research question needs technology that does not yet exist. Your needs help shape our development, with co-authored papers, shared data, letters of support and possible studies in AMIGO.', ''),
                                                     ('', 'Service project', 'You use software, methods, equipment or data the center has already developed, with training and support from center staff.', '')])),
              ('Work enabled through our projects', cards([(p['type'] + ' · ' + p['venue'], p['title'], 'Led by ' + p['lead'], p['doi']) for p in d['partners']])),
              ('Industry', '<p>Center investigators help companies define needs with our clinicians, prototype with clinical equipment, test from phantom to patient and gather data for regulatory review. For example, fifteen years of work with center investigators led to a 2026 SBIR Phase II award to AiM Medical Robotics, with the Brigham as clinical partner. See <a href="industry.html">Working with industry</a>.</p>')],
        contact='The center through <a href="about.html#contact">Contact</a>, or a project lead directly',
        links=[('Collaborations', 'page-collaborations.html'), ('Working with industry', 'industry.html')])
    # ---------------- About
    P['about'] = dict(
        banner=banner('media/2025_02_History.jpg', 'Image-guided therapy research at the Brigham, a timeline'),
        lead='Advanced Technologies – National Center for Image Guided Therapy is an NIH NIBIB P41 national resource center at Brigham and Women’s Hospital and Harvard Medical School. Its work depends on the clinical expertise, research infrastructure and patients of Mass General Brigham.',
        glance=[('Funded by', 'NIH NIBIB, P41EB028741'), ('Since', '2005 as NCIGT'), ('Principal investigators', 'Clare Tempany, MD; Nobuhiko Hata, PhD'), ('Home', 'Department of Radiology, Brigham and Women’s Hospital')],
        body=[('History of the center', cards([(c['years'] + ' · ' + c['grant'], c['name'], c['people'].replace('\n', '; '), '') for c in d['cycles']])),
              ('Acknowledging the center', '<p>If the center’s technology, data, equipment or staff contributed to your work, please include this sentence in your acknowledgments:</p><blockquote>This work was supported in part by the Advanced Technologies - National Center for Image Guided Therapy (AT-NCIGT), funded by the National Institute of Biomedical Imaging and Bioengineering of the National Institutes of Health under award P41EB028741.</blockquote>')],
        contact='Tell us what you would like to talk about, and we will connect you with the right person. [Center email]',
        links=[('People', 'people.html'), ('IGT research at the Brigham', 'page-history.html'), ('All pages', 'sitemap.html')])
    return P

def main():
    d = main_data()
    shell_doc = open(os.path.join(ROOT, 'page-amigo.html'), encoding='utf-8').read()
    head, foot = restyle.shell_parts(shell_doc)
    P = build(d)
    for sec in sitetree.SECTIONS:
        p = P.get(sec['key'])
        if not p: continue
        f = sec['landing']
        body = p['banner'] + f'<p class="lead">{p["lead"]}</p>' + glance(p['glance'])
        IDS = {'Clinical studies using the center': 'studies', 'Where your work could connect': 'connect', 'Work enabled through our projects': 'partner-research',
               'Recently shared': 'shared', 'Software, tutorials and data': 'software', 'History of the center': 'history', 'Acknowledging the center': 'acknowledge',
               'Contact': 'contact', 'Equipment and tools': 'equipment', 'Projects': 'projects', 'How to start': 'start'}
        for h, b in p['body']:
            hid = f' id="{IDS[h]}"' if h in IDS else ''
            body += f'<h2{hid}>{esc(h)}</h2>{b}'
        body += pages_block(sec)
        body += nextblock(p['contact'], p['links'])
        body, toc = restyle.add_ids(body)
        snav = restyle.section_nav(f, sec)
        tochtml = '<nav class="toc" aria-label="On this page"><strong>On this page</strong>' + ''.join(f'<a href="#{i}">{esc(t)}</a>' for t, i in toc) + '</nav>'
        hero = (f'<section class="hx"><div class="w"><p class="crumb"><a href="index.html">Home</a></p><h1>{esc(sec["label"])}</h1>'
                f'<p class="lede">{esc(sec["blurb"])}</p></div></section>')
        main_html = f'<main id="main">{hero}<div class="lay"><aside class="side">{snav}{tochtml}</aside><article class="arc">{body}</article></div></main>'
        h = re.sub(r'<title>.*?</title>', f'<title>{esc(sec["label"])} · AT-NCIGT (draft)</title>', head, count=1)
        h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(sec["blurb"])}">', h, count=1)
        open(os.path.join(ROOT, f), 'w', encoding='utf-8').write(h + main_html + foot)
        print('built', f)

if __name__ == '__main__':
    main()
