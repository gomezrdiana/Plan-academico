# -*- coding: utf-8 -*-
"""Pieza gráfica 1080x1350 — vacante Ejecutivo(a) Senior de Alianzas Empresariales.
Protagonista: el ingreso mensual alcanzable (cifras de la propuesta, con meta y pagos de contado; sin acelerador ni cartera).
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PIEZA_VACANTE_ALIANZAS.png"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
NAR = (229, 76, 9); AMAR = (251, 201, 0); CREMA = (255, 248, 231); CAFE = (48, 39, 28); BLANCO = (255, 255, 255); NAR2 = (240, 140, 90)
F = 'C:/Windows/Fonts/'
def font(n, s): return ImageFont.truetype(F + n, s)
W, H = 1080, 1350
im = Image.new('RGB', (W, H), CREMA); d = ImageDraw.Draw(im)

# ---- cabecera ----
TOP = 470
d.rectangle([0, 0, W, TOP], fill=NAR)
d.rectangle([0, 0, 300, 20], fill=AMAR)
try:
    logo = Image.open(os.path.join(BASE, r'recursos\marca heiiu\logo_heiiu_sobre_naranja.png')).convert('RGBA')
    lh = 88; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    im.paste(logo, (64, 54), logo)
except Exception:
    d.text((64, 60), 'Heiiu', font=font('calibrib.ttf', 80), fill=BLANCO)
d.rounded_rectangle([W - 400, 64, W - 64, 136], radius=36, fill=AMAR)
d.text((W - 232, 100), 'CONTRATACIÓN INMEDIATA', font=font('calibrib.ttf', 28), fill=CAFE, anchor='mm')
d.text((64, 185), 'BUSCAMOS', font=font('calibrib.ttf', 42), fill=AMAR)
d.text((64, 232), 'EJECUTIVO(A) SENIOR', font=font('calibrib.ttf', 90), fill=BLANCO)
d.text((64, 330), 'DE ALIANZAS EMPRESARIALES', font=font('calibrib.ttf', 60), fill=BLANCO)
d.text((64, 410), 'Mínimo 5 años de experiencia B2B · Bucaramanga', font=font('calibri.ttf', 34), fill=CREMA)

# ---- cifra protagonista ----
d.text((W // 2, TOP + 62), 'TU INGRESO PUEDE LLEGAR A', font=font('calibrib.ttf', 36), fill=CAFE, anchor='mm')
d.text((W // 2, TOP + 168), '$13,6 MILLONES', font=font('calibrib.ttf', 118), fill=NAR, anchor='mm')
d.text((W // 2, TOP + 258), 'AL MES  ·  y las comisiones no tienen techo', font=font('calibrib.ttf', 36), fill=CAFE, anchor='mm')

# ---- escalera de ingresos (barras crecientes) ----
etapas = [('Meses 1-3', '$3,5M', 'garantizados', 3.5), ('Meses 4-6', '$6,8M', '', 6.8), ('Meses 7-12', '$10,3M', '', 10.35), ('Año 2', '$13,6M', '', 13.65)]
base_y = H - 230; maxh = 270; bw = 190; gap = (W - 128 - 4 * bw) // 3
for i, (lab, val, sub, v) in enumerate(etapas):
    x = 64 + i * (bw + gap); h = int(maxh * v / 13.65)
    color = NAR if i == 3 else NAR2
    d.rounded_rectangle([x, base_y - h, x + bw, base_y], radius=16, fill=color)
    d.text((x + bw // 2, base_y - h - 34), val, font=font('calibrib.ttf', 42), fill=CAFE, anchor='mm')
    if sub: d.text((x + bw // 2, base_y - h + 30), sub, font=font('calibrib.ttf', 24), fill=BLANCO, anchor='mm')
    d.text((x + bw // 2, base_y + 28), lab, font=font('calibrib.ttf', 28), fill=CAFE, anchor='mm')
d.text((W // 2, base_y + 66), 'Ingreso mensual cumpliendo la meta · contrato laboral + prestaciones', font=font('calibri.ttf', 26), fill=CAFE, anchor='mm')

# ---- pie ----
FY = H - 120
d.rectangle([0, FY, W, H], fill=CAFE)
d.text((W // 2, FY + 42), 'Hoja de vida + audio de 1 minuto', font=font('calibrib.ttf', 32), fill=AMAR, anchor='mm')
d.text((W // 2, FY + 86), 'citasheiiu@gmail.com · asunto "Alianzas Heiiu"', font=font('calibri.ttf', 32), fill=BLANCO, anchor='mm')
d.rectangle([W - 300, H - 18, W, H], fill=AMAR)

out = os.path.join(BASE, r'recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PIEZA_VACANTE_ALIANZAS.png')
try: im.save(out); print('OK', out)
except (PermissionError, OSError): im.save(out.replace('.png', '_v2.png')); print('ABIERTO -> _v2')
