#!/usr/bin/env python
"""One brand mark for every declared icon.

favicon.svg was a green plane glyph while favicon.ico / favicon-*-.png / the
webmanifest icons carried the calendar brand mark, so browsers (tab vs
bookmark vs pinned tab vs PWA install) drew different logos for the same site.
Regenerate the whole raster/ICO/SVG set from brand-logo.png.
"""
import base64, io, os
from PIL import Image

SRC = 'brand-logo.png'
img = Image.open(SRC).convert('RGBA')

PNGS = {'favicon-16.png': 16, 'favicon-32.png': 32, 'icon-48.png': 48,
        'icon-96.png': 96, 'icon-192.png': 192, 'icon-512.png': 512,
        'apple-touch-icon.png': 180}

for out, size in PNGS.items():
    img.resize((size, size), Image.LANCZOS).save(out, 'PNG', optimize=True)
    print('[png ]', out, size)

img.resize((48, 48), Image.LANCZOS).save('favicon.ico', format='ICO',
                                         sizes=[(16, 16), (32, 32), (48, 48)])
print('[ico ] favicon.ico 16/32/48')

buf = io.BytesIO()
img.resize((128, 128), Image.LANCZOS).save(buf, 'PNG', optimize=True)
b64 = base64.b64encode(buf.getvalue()).decode('ascii')
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" '
       'width="128" height="128">\n'
       '  <image width="128" height="128" '
       'href="data:image/png;base64,' + b64 + '"/>\n</svg>\n')
io.open('favicon.svg', 'w', encoding='utf-8', newline='\n').write(svg)
print('[svg ] favicon.svg (embedded brand mark)')
