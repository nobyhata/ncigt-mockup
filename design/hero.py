V='FKmVNp5UrBw'
def apply(doc):
    doc=doc.replace('<section id="top" style="background: #0F1B2D; color: #FFFFFF">',f'''<section id="top" style="position: relative; overflow: hidden; background: #0F1B2D url(https://i.ytimg.com/vi/{V}/maxresdefault.jpg) center / cover no-repeat; color: #FFFFFF; min-height: 640px; display: flex; align-items: center">
<div id="herovid" aria-hidden="true" style="position: absolute; inset: 0; pointer-events: none"></div>
<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(10,19,33,0.92) 0%, rgba(10,19,33,0.78) 45%, rgba(10,19,33,0.45) 100%)"></div>
<button id="vidtoggle" type="button" style="position: absolute; right: 20px; bottom: 20px; z-index: 3; background: rgba(15,27,45,0.7); color: #FFFFFF; border: 1px solid rgba(255,255,255,0.5); border-radius: 999px; padding: 8px 14px; font: 600 13px Inter, sans-serif; cursor: pointer">Pause video</button>
<p style="position: absolute; left: 24px; bottom: 16px; z-index: 3; margin: 0; font-size: 12px; color: #C9D3E0">Video: Mass General Brigham Image-Guided Therapy, filmed in the AMIGO suite. <a href="https://www.youtube.com/watch?v={V}" style="color: #D9B98F">Watch with sound →</a></p>''',1)
    doc=doc.replace('<div style="max-width: 1200px; margin: 0 auto; padding: 80px 24px 72px; display: flex; flex-wrap: wrap; gap: 48px; align-items: center">','<div style="position: relative; z-index: 2; width: 100%; max-width: 1200px; margin: 0 auto; padding: 96px 24px 104px; display: flex; flex-wrap: wrap; gap: 48px; align-items: center">',1)
    js=('<style>#herovid iframe{position:absolute;top:50%;left:50%;width:max(100%,177.78vh);height:max(100%,56.25vw);transform:translate(-50%,-50%);border:0}</style>\n'
     '<script>(function(){var V="'+V+'",box=document.getElementById("herovid"),btn=document.getElementById("vidtoggle");'
     'var reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;'
     'function start(){box.innerHTML=\'<iframe title="AMIGO video (background, muted)" tabindex="-1" src="https://www.youtube-nocookie.com/embed/\'+V+\'?autoplay=1&mute=1&loop=1&playlist=\'+V+\'&controls=0&modestbranding=1&playsinline=1&rel=0&disablekb=1" allow="autoplay; encrypted-media"></iframe>\';btn.textContent="Pause video";}'
     'function stop(){box.innerHTML="";btn.textContent="Play video";}'
     'if(reduce){stop();}else{start();}btn.addEventListener("click",function(){box.innerHTML?stop():start();});})();</script>\n</body>')
    return doc.replace('</body>',js,1)
