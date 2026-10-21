# -*- coding: utf-8 -*-
"""Pieza de reactivacion de octubre (gancho de temporada) para la plantilla de LaHaus. Misma base visual de
gen_pieza_reactivacion.py (fondo de tablero oscuro, logo, tarjetas de motivo). Titular: el miedo no es al ingles,
es a lo que llega sin el; etiqueta con la urgencia real (ultimo grupo del ano, noviembre). Sin programa ni precio.
Salida: recursos/comercial/plataforma LaHaus/PIEZA_REACTIVACION_OCTUBRE_HEIIU.png"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1600, 840
BG = (48, 39, 28); CREMA = (255, 248, 231); AMAR = (251, 201, 0); NAR = (229, 76, 9); GRIS = (210, 200, 185)
F = 'C:/Windows/Fonts/'
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus'
def font(name, size): return ImageFont.truetype(F + name, size)

foto = os.path.join(BASE, 'fondo_reactivacion.jpg')
if os.path.exists(foto):
    img = Image.open(foto).convert('RGB')
    img = img.crop((int(img.width * 0.18), 0, img.width, int(img.height * 0.56)))
    r = max(W / img.width, H / img.height); img = img.resize((int(img.width * r) + 1, int(img.height * r) + 1))
    x = (img.width - W) // 2; y = (img.height - H) // 2; img = img.crop((x, y, x + W, y + H))
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(overlay)
    for i in range(W):
        a = int(246 - 100 * (i / W))
        od.line([(i, 0), (i, H)], fill=(40, 30, 22, a))
    img = img.filter(ImageFilter.GaussianBlur(5))
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
else:
    img = Image.new('RGB', (W, H), BG)

d = ImageDraw.Draw(img)

# logo
logo = Image.open(r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\marca heiiu\logo_heiiu_sobre_naranja.png').convert('RGBA')
lh = 130; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
pad = Image.new('RGBA', (lw + 44, lh + 30), NAR + (255,)); pad.paste(logo, (22, 15), logo)
sh = Image.new('RGBA', (pad.width + 24, pad.height + 24), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
sd.rounded_rectangle([12, 12, sh.width - 12, sh.height - 12], radius=10, fill=(0, 0, 0, 120)); sh = sh.filter(ImageFilter.GaussianBlur(10))
img.paste(sh, (72 - 12, 56 - 6), sh); img.paste(pad, (72, 56), pad)

# etiqueta (urgencia real)
d.text((72, 262), 'ÚLTIMO GRUPO DEL AÑO: NOVIEMBRE', font=font('calibrib.ttf', 26), fill=AMAR)
d.rectangle([72, 302, 182, 307], fill=NAR)
# titular
d.text((72, 330), 'Lo que da miedo', font=font('calibrib.ttf', 92), fill=CREMA)
d.text((72, 430), 'no es el inglés.', font=font('calibrib.ttf', 92), fill=CREMA)
# bajada
d.text((72, 548), 'Es la entrevista, el viaje o el cliente', font=font('georgiai.ttf', 40), fill=AMAR)
d.text((72, 596), 'que llegan sin él.', font=font('georgiai.ttf', 40), fill=AMAR)
# garantia
d.text((72, 660), 'Presencial en Bucaramanga. Única academia con garantía', font=font('calibri.ttf', 26), fill=GRIS)
d.text((72, 690), 'de aprendizaje por escrito.', font=font('calibri.ttf', 26), fill=GRIS)
# boton
bx, by, bw, bh = 72, 736, 400, 64
d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14, fill=AMAR)
d.text((bx + 34, by + 15), 'Quiero mi fecha  →', font=font('calibrib.ttf', 30), fill=BG)

# tarjetas de motivo (derecha)
cards = [('UN TRABAJO', 'la vacante que hoy\npasas de largo'), ('UN VIAJE', 'pasar inmigración con\ntus propias respuestas'),
         ('UN ESTUDIO', 'la beca o el posgrado\nsin ese requisito'), ('UN NEGOCIO', 'clientes de afuera\nsin traductor')]
cw, ch, gap = 250, 160, 20
x0 = W - 72 - (2 * cw + gap); y0 = 330
cl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(cl)
for i, (tit, sub) in enumerate(cards):
    cx = x0 + (i % 2) * (cw + gap); cy = y0 + (i // 2) * (ch + gap)
    cd.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=18, fill=(48, 39, 28, 175), outline=(140, 118, 88, 200), width=2)
img = Image.alpha_composite(img.convert('RGBA'), cl).convert('RGB'); d = ImageDraw.Draw(img)
for i, (tit, sub) in enumerate(cards):
    cx = x0 + (i % 2) * (cw + gap); cy = y0 + (i // 2) * (ch + gap)
    d.rectangle([cx + 22, cy + 22, cx + 70, cy + 26], fill=NAR)
    d.text((cx + 22, cy + 40), tit, font=font('calibrib.ttf', 25), fill=AMAR)
    d.multiline_text((cx + 22, cy + 82), sub, font=font('calibri.ttf', 22), fill=CREMA, spacing=6)
d.text((x0, y0 - 40), 'LO QUE NOS DIJISTE QUE QUERÍAS', font=font('calibrib.ttf', 20), fill=GRIS)

# pie: instagram
ix, iy, isz = W - 72 - 300, 784, 30
d.rounded_rectangle([ix, iy, ix + isz, iy + isz], radius=9, outline=AMAR, width=3)
d.ellipse([ix + 8, iy + 8, ix + isz - 8, iy + isz - 8], outline=AMAR, width=3)
d.ellipse([ix + isz - 10, iy + 5, ix + isz - 5, iy + 10], fill=AMAR)
fh = font('calibrib.ttf', 28); bb = d.textbbox((0, 0), '@heiiu_english', font=fh)
d.text((ix + isz + 12, iy + (isz - (bb[3] - bb[1])) // 2 - bb[1]), '@heiiu_english', font=fh, fill=AMAR)

out = os.path.join(BASE, 'PIEZA_REACTIVACION_OCTUBRE_HEIIU.png')
try:
    img.save(out, optimize=True); print('OK', out)
except OSError:
    out2 = out.replace('.png', '_v2.png'); img.save(out2, optimize=True); print('ABIERTA -> guardada como', out2)
