"""Stage 1 fix: hero demo must not blank the hero copy or zoom/crop the phone.

The cinematic phase (html.demo-cinema + .hero.cinema + phone.cinema + --cinema-dx)
hid the hero copy for ~28s and left a shifted, cropped phone on screen, so the
landing page looked broken. The scene overlays stay; the hero-wide "cinema"
state goes away.
"""
import io, sys

P = 'scripts/hero-demo.js'
s = io.open(P, encoding='utf-8').read()
orig = s

reps = [
    # (a) cinema start: drop html-level class + stage cinema
    ('document.documentElement.classList.add("demo-cinema"),phone.classList.add("glare-still"),'
     'stageEl&&stageEl.classList.add("cinema"),',
     'phone.classList.add("glare-still"),'),
    # (b) drop the horizontal shift + hero/phone cinema classes
    ('var heroRect=heroSec?heroSec.getBoundingClientRect():null,'
     'stageRect=stageEl?stageEl.getBoundingClientRect():null;'
     'if(heroRect&&stageRect){var dx=Math.round(heroRect.left+heroRect.width/2-'
     '(stageRect.left+stageRect.width/2));phone.style.setProperty("--cinema-dx",dx+"px")}'
     'phone.classList.add("cinema"),phone.classList.remove("idle"),'
     'heroSec&&heroSec.classList.add("cinema"),',
     'phone.classList.remove("idle"),heroSec&&heroSec.classList.remove("cinema"),'),
    # (c) scene overlay mounts without the cinema-mode backdrop class
    ('rlStage.classList.add("on","cinema"),rlStage.innerHTML="";var card=',
     'rlStage.classList.add("on"),rlStage.innerHTML="";var card='),
]

# (d) replace the whole finale() body with a state-cleaning version.
#     The exact source text is extracted from the file (minified, easy to typo).
def extract_fn(src, name):
    i = src.find('function ' + name + '()')
    if i < 0:
        raise SystemExit('function %s not found' % name)
    j = src.find('{', i)
    depth, k = 0, j
    while k < len(src):
        if src[k] == '{':
            depth += 1
        elif src[k] == '}':
            depth -= 1
            if depth == 0:
                return i, k + 1, src[i:k + 1]
        k += 1
    raise SystemExit('unbalanced function %s' % name)

_fi, _fj, OLD_FINALE = extract_fn(s, 'finale')

NEW_FINALE = ('function finale(){phone.classList.remove("glare-still"),chanLayer.classList.remove("on"),'
              'iosLayer.classList.remove("on","launch"),botLayer.classList.remove("on"),explorerOn(!1),'
              'dropGlow.classList.remove("on"),fxCursor.classList.remove("on","holding"),'
              'rlStage.classList.remove("on","cinema","finale","written","hero-back"),rlStage.innerHTML="",'
              'phone.classList.remove("cinema","finale","cine-hide","cine-restore"),'
              'document.documentElement.classList.remove("demo-cinema"),'
              'heroSec&&heroSec.classList.remove("cinema","hero-back"),'
              'stageEl&&stageEl.classList.remove("cinema"),'
              'phone.style.removeProperty("--cinema-dx"),finaleHead(!1),'
              'later(function(){phone.classList.add("idle");'
              'var rp=document.querySelector(".hero-copy .hero-replay");rp&&(rp.hidden=!1)},900)}')

# finale first (positions were measured on the original text)
s = s[:_fi] + NEW_FINALE + s[_fj:]

for old, new in reps:
    if old not in s:
        print('MISS:', old[:80])
        sys.exit(1)
    if s.count(old) != 1:
        print('AMBIGUOUS x%d:' % s.count(old), old[:80])
        sys.exit(1)
    s = s.replace(old, new)

io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('[ok] patched %s (%d -> %d bytes)' % (P, len(orig), len(s)))
