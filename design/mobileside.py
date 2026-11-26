"""On narrow screens, fold the section menu and 'On this page' into one closed
'Browse this section' control so the page content starts near the top."""
import re, sys, glob, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CSS = ('<style id="mside">.sdet>summary{display:none}.sdet>nav+nav{margin-top:22px}'
       '@media (max-width:900px){.sdet{border:1px solid #E3E8EF;border-radius:10px;padding:0 14px}'
       '.sdet>summary{display:block;cursor:pointer;padding:12px 0;font-weight:600;font-size:15px;color:#0B5F86;list-style:none}'
       '.sdet>summary::-webkit-details-marker{display:none}.sdet>summary::after{content:" \\25BE"}.sdet[open]>summary::after{content:" \\25B4"}'
       '.sdet[open]{padding-bottom:14px}.side .toc{display:none}.side{margin:0!important}}</style>')
JS = ('<script id="msidejs">(function(){var w=window.matchMedia("(min-width: 901px)");'
      'function s(){document.querySelectorAll("details.sdet").forEach(function(d){d.open=w.matches;});}'
      's();w.addEventListener?w.addEventListener("change",s):w.addListener(s);})();</script>')
n = 0
for f in glob.glob(os.path.join(ROOT, '*.html')):
    s = open(f, encoding='utf-8').read()
    if '<aside class="side">' not in s or 'class="sdet"' in s: continue
    s = re.sub(r'<aside class="side">(.*?)</aside>',
               lambda m: '<aside class="side"><details class="sdet" open><summary>Browse this section</summary>' + m.group(1) + '</details></aside>',
               s, count=1, flags=re.S)
    s = s.replace('</head>', CSS + '</head>', 1).replace('</body>', JS + '</body>', 1)
    open(f, 'w', encoding='utf-8').write(s); n += 1
print('folded side menu on', n, 'pages')
