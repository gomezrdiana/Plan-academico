# -*- coding: utf-8 -*-
"""Pieza gráfica 1080x1350 — vacante Ejecutivo(a) Senior de Alianzas Empresariales. Estilo ejecutivo (fondo oscuro, curva de ingreso).
Cifras de la propuesta: ingreso mensual cumpliendo la meta, pagos de contado; sin acelerador ni cartera.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PIEZA_VACANTE_ALIANZAS.png"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
NAR = (229, 76, 9); AMAR = (251, 201, 0); CREMA = (255, 248, 231); FONDO = (24, 21, 18); GRIS = (170, 160, 150); BLANCO = (255, 255, 255)
F = 'C:/Windows/Fonts/'
def font(n, s): return ImageFont.truetype(F + n, s)
W, H = 1080, 1350

im = Image.new('RGB', (W, H), FONDO)
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
g.ellipse([W - 620, -380, W + 380, 520], fill=NAR + (110,))
g.ellipse([-420, H - 520, 380, H + 300], fill=NAR + (60,))
glow = glow.filter(ImageFilter.GaussianBlur(160))
im = Image.alpha_composite(im.convert('RGBA'), glow)
d = ImageDraw.Draw(im)

M = 72
try:
    logo = Image.open(os.path.join(BASE, r'recursos\marca heiiu\logo_heiiu_sobre_naranja.png')).convert('RGBA')
    lh = 74; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    im.paste(logo, (M, 62), logo)
except Exception:
    d.text((M, 64), 'Heiiu', font=font('calibrib.ttf', 64), fill=BLANCO)
d.rounded_rectangle([W - M - 330, 72, W - M, 128], radius=28, outline=AMAR, width=3)
d.text((W - M - 165, 100), 'CONTRATACIÓN INMEDIATA', font=font('calibrib.ttf', 24), fill=AMAR, anchor='mm')

def spaced(x, y, text, fnt, fill, sp=6):
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill); x += d.textlength(ch, font=fnt) + sp
spaced(M, 200, 'BUSCAMOS', font('calibrib.ttf', 30), AMAR, 8)
d.text((M, 240), 'Ejecutivo(a) Senior', font=font('calibrib.ttf', 96), fill=BLANCO)
d.text((M, 344), 'de Alianzas Empresariales', font=font('calibrib.ttf', 70), fill=NAR)
d.text((M, 436), 'Mínimo 5 años de experiencia B2B  ·  Bucaramanga', font=font('calibri.ttf', 34), fill=GRIS)
d.line([M, 506, M + 120, 506], fill=AMAR, width=5)

d.text((M, 540), 'Tu ingreso puede llegar a', font=font('calibri.ttf', 40), fill=CREMA)
d.text((M - 4, 588), '$13,6M', font=font('calibrib.ttf', 168), fill=AMAR)
x_mes = M + d.textlength('$13,6M', font=font('calibrib.ttf', 168)) + 22
d.text((x_mes, 640), 'al mes', font=font('calibrib.ttf', 48), fill=BLANCO)
d.text((x_mes, 700), 'comisiones sin techo', font=font('calibri.ttf', 34), fill=GRIS)

pts_v = [('Meses 1-3', '$5M', 5.0), ('Meses 4-6', '$6,8M', 6.8), ('Meses 7-12', '$10,3M', 10.35), ('Año 2', '$13,6M', 13.65)]
cx0, cx1 = M + 70, W - M - 70; cy_base = 1110; ch = 230; vmin, vmax = 3.5, 13.65
xs = [cx0 + i * (cx1 - cx0) / 3 for i in range(4)]
ys = [cy_base - (v - vmin) / (vmax - vmin) * ch - 20 for _, _, v in pts_v]
area = Image.new('RGBA', (W, H), (0, 0, 0, 0)); a = ImageDraw.Draw(area)
a.polygon([(xs[0], cy_base)] + list(zip(xs, ys)) + [(xs[-1], cy_base)], fill=NAR + (70,))
im = Image.alpha_composite(im, area); d = ImageDraw.Draw(im)
d.line([(cx0 - 40, cy_base), (cx1 + 40, cy_base)], fill=(80, 72, 64), width=2)
d.line(list(zip(xs, ys)), fill=NAR, width=7, joint='curve')
for i, ((lab, val, v), x, y) in enumerate(zip(pts_v, xs, ys)):
    r = 14 if i < 3 else 18
    d.ellipse([x - r, y - r, x + r, y + r], fill=AMAR if i == 3 else NAR, outline=FONDO, width=4)
    d.text((x, y - 44), val, font=font('calibrib.ttf', 40 if i < 3 else 46), fill=BLANCO if i < 3 else AMAR, anchor='mm')
    d.text((x, cy_base + 32), lab, font=font('calibri.ttf', 28), fill=GRIS, anchor='mm')
d.text((W // 2, cy_base + 76), 'Ingreso mensual cumpliendo la meta · mínimo garantizado de $3,5M los 3 primeros meses', font=font('calibri.ttf', 24), fill=GRIS, anchor='mm')

d.line([M, 1218, W - M, 1218], fill=(70, 62, 55), width=1)
d.text((W // 2, 1250), 'Contrato laboral  ·  Licencia desde 2012  ·  Triple certificación ICONTEC  ·  Convenio Cajasan', font=font('calibri.ttf', 26), fill=GRIS, anchor='mm')
d.text((W // 2, 1300), 'Hoja de vida + audio de 1 min  →  citasheiiu@gmail.com  ·  asunto "Alianzas Heiiu"', font=font('calibrib.ttf', 30), fill=CREMA, anchor='mm')

out = os.path.join(BASE, r'recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PIEZA_VACANTE_ALIANZAS.png')
im = im.convert('RGB')
try: im.save(out); print('OK', out)
except (PermissionError, OSError): im.save(out.replace('.png', '_v2.png')); print('ABIERTO -> _v2')
