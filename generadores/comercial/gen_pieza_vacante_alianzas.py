# -*- coding: utf-8 -*-
"""Pieza gráfica 1080x1350 (LinkedIn / Instagram) — vacante Ejecutivo(a) de Alianzas Empresariales.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PIEZA_VACANTE_ALIANZAS.png"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
NAR = (229, 76, 9); AMAR = (251, 201, 0); CREMA = (255, 248, 231); CAFE = (48, 39, 28); BLANCO = (255, 255, 255)
F = 'C:/Windows/Fonts/'
def font(n, s): return ImageFont.truetype(F + n, s)
W, H = 1080, 1350
im = Image.new('RGB', (W, H), CREMA); d = ImageDraw.Draw(im)

# franja superior naranja con logo
d.rectangle([0, 0, W, 210], fill=NAR)
d.rectangle([0, 0, 260, 18], fill=AMAR)
try:
    logo = Image.open(os.path.join(BASE, r'recursos\marca heiiu\logo_heiiu_sobre_naranja.png')).convert('RGBA')
    lh = 110; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    im.paste(logo, (70, 60), logo)
except Exception as e:
    d.text((70, 70), 'Heiiu', font=font('calibrib.ttf', 90), fill=BLANCO)
d.text((W - 70, 105), 'CONTRATACIÓN\nINMEDIATA', font=font('calibrib.ttf', 40), fill=BLANCO, anchor='rm', align='right')

def wrap(text, fnt, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=fnt) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

y = 270
d.text((70, y), 'BUSCAMOS', font=font('calibrib.ttf', 52), fill=CAFE); y += 70
for line in wrap('EJECUTIVO(A) DE ALIANZAS EMPRESARIALES', font('calibrib.ttf', 84), W - 140):
    d.text((70, y), line, font=font('calibrib.ttf', 84), fill=NAR); y += 92
y += 18
for line in wrap('Abre las puertas de las empresas, colegios y fundaciones de Bucaramanga al inglés.', font('georgiai.ttf', 40), W - 140):
    d.text((70, y), line, font=font('georgiai.ttf', 40), fill=CAFE); y += 52
y += 34

items = ['Contrato laboral + prestaciones',
         '$3.500.000 garantizados los 3 primeros meses',
         '10% de lo que paga cada empresa + cartera mensual',
         'Comisiones sin techo · Bucaramanga']
for it in items:
    d.rounded_rectangle([70, y, W - 70, y + 92], radius=18, fill=BLANCO)
    d.ellipse([100, y + 30, 132, y + 62], fill=NAR)
    d.text((158, y + 46), it, font=font('calibrib.ttf', 38), fill=CAFE, anchor='lm')
    y += 112

# cierre
d.rectangle([0, H - 210, W, H], fill=NAR)
d.text((W // 2, H - 150), 'Aplica con tu hoja de vida + un audio de 1 minuto', font=font('calibrib.ttf', 40), fill=BLANCO, anchor='mm')
d.text((W // 2, H - 92), 'citasheiiu@gmail.com · asunto "Alianzas Heiiu"', font=font('calibri.ttf', 38), fill=BLANCO, anchor='mm')
d.rectangle([W - 260, H - 18, W, H], fill=AMAR)

out = os.path.join(BASE, r'recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PIEZA_VACANTE_ALIANZAS.png')
try: im.save(out); print('OK', out)
except PermissionError: im.save(out.replace('.png', '_v2.png')); print('ABIERTO -> _v2')
