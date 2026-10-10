# -*- coding: utf-8 -*-
"""Pieza gráfica 1080x1350 (LinkedIn / Instagram) — vacante Ejecutivo(a) Senior de Alianzas Empresariales. Cifras como protagonistas.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PIEZA_VACANTE_ALIANZAS.png"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
NAR = (229, 76, 9); AMAR = (251, 201, 0); CREMA = (255, 248, 231); CAFE = (48, 39, 28); BLANCO = (255, 255, 255)
F = 'C:/Windows/Fonts/'
def font(n, s): return ImageFont.truetype(F + n, s)
W, H = 1080, 1350
im = Image.new('RGB', (W, H), CREMA); d = ImageDraw.Draw(im)

# ---- bloque superior naranja ----
TOP = 560
d.rectangle([0, 0, W, TOP], fill=NAR)
d.rectangle([0, 0, 300, 20], fill=AMAR)
try:
    logo = Image.open(os.path.join(BASE, r'recursos\marca heiiu\logo_heiiu_sobre_naranja.png')).convert('RGBA')
    lh = 92; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    im.paste(logo, (64, 56), logo)
except Exception:
    d.text((64, 60), 'Heiiu', font=font('calibrib.ttf', 80), fill=BLANCO)
# sello contratación inmediata
d.rounded_rectangle([W - 400, 66, W - 64, 140], radius=37, fill=AMAR)
d.text((W - 232, 103), 'CONTRATACIÓN INMEDIATA', font=font('calibrib.ttf', 28), fill=CAFE, anchor='mm')

d.text((64, 200), 'BUSCAMOS', font=font('calibrib.ttf', 44), fill=AMAR)
d.text((64, 250), 'EJECUTIVO(A) SENIOR', font=font('calibrib.ttf', 92), fill=BLANCO)
d.text((64, 350), 'DE ALIANZAS EMPRESARIALES', font=font('calibrib.ttf', 62), fill=BLANCO)
d.rounded_rectangle([64, 448, 64 + 560, 510], radius=31, fill=BLANCO)
d.text((64 + 280, 479), 'Mínimo 5 años de experiencia B2B', font=font('calibrib.ttf', 32), fill=NAR, anchor='mm')

# ---- tarjetas de cifras (2x2) ----
cards = [('$3.5M', 'garantizados al mes\nlos 3 primeros meses'),
         ('10%', 'de lo que paga\ncada empresa'),
         ('6%', 'mensual por cada\nestudiante de tus alianzas'),
         ('SIN TECHO', 'comisiones +\naumentos por resultados')]
cw, ch, gx, gy = 456, 250, 40, 34
x0, y0 = 64, TOP + 50
for i, (num, lab) in enumerate(cards):
    x = x0 + (i % 2) * (cw + gx); y = y0 + (i // 2) * (ch + gy)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=24, fill=BLANCO)
    d.rectangle([x, y, x + 12, y + ch], fill=NAR)
    size = 104 if len(num) <= 5 else 76
    d.text((x + cw // 2 + 6, y + 88), num, font=font('calibrib.ttf', size), fill=NAR, anchor='mm')
    d.multiline_text((x + cw // 2 + 6, y + 182), lab, font=font('calibri.ttf', 30), fill=CAFE, anchor='mm', align='center', spacing=6)

# ---- pie ----
FY = H - 190
d.rectangle([0, FY, W, H], fill=CAFE)
d.text((W // 2, FY + 58), 'Contrato laboral + prestaciones · Bucaramanga', font=font('calibrib.ttf', 34), fill=AMAR, anchor='mm')
d.text((W // 2, FY + 118), 'Hoja de vida + audio de 1 min → citasheiiu@gmail.com · asunto "Alianzas Heiiu"', font=font('calibri.ttf', 30), fill=BLANCO, anchor='mm')
d.rectangle([W - 300, H - 20, W, H], fill=AMAR)

out = os.path.join(BASE, r'recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PIEZA_VACANTE_ALIANZAS.png')
try: im.save(out); print('OK', out)
except (PermissionError, OSError): im.save(out.replace('.png', '_v2.png')); print('ABIERTO -> _v2')
