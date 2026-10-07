# -*- coding: utf-8 -*-
"""Pieza 'Precios 2026' para la asesora (rediseño de la lámina vieja): escalera de niveles, precio de lista,
becas del Fondo, Cajasan, programas. Salida: recursos/comercial/INDUCCION_COMERCIAL/PRECIOS_2026_HEIIU.png"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1600, 900
CREMA = (255, 248, 231); NAR = (229, 76, 9); AMAR = (251, 201, 0); CAFE = (48, 39, 28); GRIS = (120, 110, 100); BLANCO = (255, 255, 255)
F = 'C:/Windows/Fonts/'
def font(n, s): return ImageFont.truetype(F + n, s)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'

img = Image.new('RGB', (W, H), CREMA)
d = ImageDraw.Draw(img)
# acentos diagonales de marca (como la lámina original), suaves
acc = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ad = ImageDraw.Draw(acc)
ad.polygon([(0, 0), (140, 0), (0, 420)], fill=NAR + (255,))
ad.polygon([(0, 0), (60, 0), (0, 200)], fill=AMAR + (255,))
ad.polygon([(W, H), (W - 120, H), (W, H - 330)], fill=AMAR + (255,))
ad.polygon([(W, H), (W - 50, H), (W, H - 150)], fill=NAR + (255,))
img = Image.alpha_composite(img.convert('RGBA'), acc).convert('RGB'); d = ImageDraw.Draw(img)

# logo
try:
    logo = Image.open(os.path.join(BASE, r'recursos\marca heiiu\logo_heiiu_sobre_naranja.png')).convert('RGBA')
    lh = 96; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    pad = Image.new('RGBA', (lw + 36, lh + 24), NAR + (255,)); pad.paste(logo, (18, 12), logo)
    img.paste(pad, (150, 40), pad)
except Exception:
    d.text((150, 50), 'heiiu', font=font('calibrib.ttf', 60), fill=NAR)

# título
d.text((W // 2, 60), 'PRECIOS 2026', font=font('calibrib.ttf', 54), fill=CAFE, anchor='mt')
d.text((W // 2 + 40, 122), 'Programa completo A1 → B2 · 575 horas presenciales · garantía por escrito', font=font('calibri.ttf', 24), fill=GRIS, anchor='mt')

# escalera de niveles
niveles = [('A1', '90 h', '$1.596.000', (160, 150, 140)), ('A2', '110 h', '$1.915.000', (200, 110, 70)), ('B1', '175 h', '$2.842.000', (236, 110, 40)), ('B2', '200 h', '$2.343.000', NAR)]
x0, base_y, bw, gap = 150, 640, 225, 24
step = 62
for i, (nv, hrs, pr, col) in enumerate(niveles):
    x = x0 + i * (bw + gap); top = base_y - 210 - i * step
    d.rounded_rectangle([x, top, x + bw, base_y], radius=14, fill=col)
    d.text((x + bw // 2, top + 18), nv, font=font('calibrib.ttf', 64), fill=BLANCO, anchor='mt')
    d.text((x + bw // 2, top + 96), hrs, font=font('calibri.ttf', 28), fill=(255, 240, 225), anchor='mt')
    d.text((x + bw // 2, base_y - 40), pr, font=font('calibrib.ttf', 30), fill=BLANCO, anchor='mt')
# línea base y total de lista
d.line([(x0, base_y + 2), (x0 + 4 * bw + 3 * gap, base_y + 2)], fill=CAFE, width=3)
d.text((x0, base_y + 14), 'Nivel suelto: sin beca.', font=font('calibri.ttf', 26), fill=GRIS)
d.text((x0 + 300, base_y + 14), 'Programa completo de lista:', font=font('calibri.ttf', 26), fill=GRIS)
d.text((x0 + 612, base_y + 9), '$8.696.000', font=font('calibrib.ttf', 34), fill=CAFE)

# tarjeta becas del Fondo
cx, cy, cw, ch = 1150, 190, 380, 300
d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=20, fill=NAR)
d.text((cx + cw // 2, cy + 22), 'BECAS DEL FONDO', font=font('calibrib.ttf', 30), fill=AMAR, anchor='mt')
d.text((cx + cw // 2, cy + 62), 'según el perfil del estudiante', font=font('calibri.ttf', 22), fill=BLANCO, anchor='mt')
d.text((cx + cw // 2, cy + 104), 'del 32% al 45%', font=font('calibrib.ttf', 46), fill=BLANCO, anchor='mt')
d.text((cx + cw // 2, cy + 168), 'Programa completo, de contado', font=font('calibri.ttf', 21), fill=(255, 230, 210), anchor='mt')
d.text((cx + cw // 2, cy + 196), 'desde $4.782.800', font=font('calibrib.ttf', 34), fill=AMAR, anchor='mt')
d.text((cx + cw // 2, cy + 246), 'Se evalúa con soportes en la asesoría.', font=font('calibri.ttf', 19), fill=(255, 230, 210), anchor='mt')
d.text((cx + cw // 2, cy + 270), 'Libros incluidos si separas el mismo día.', font=font('calibri.ttf', 19), fill=(255, 230, 210), anchor='mt')

# tarjeta Cajasan / financiación
cy2 = cy + ch + 24; ch2 = 170
d.rounded_rectangle([cx, cy2, cx + cw, cy2 + ch2], radius=20, fill=BLANCO, outline=NAR, width=3)
d.text((cx + 22, cy2 + 18), 'CONVENIO CAJASAN', font=font('calibrib.ttf', 26), fill=NAR)
d.text((cx + 22, cy2 + 54), 'Afiliados: condiciones especiales', font=font('calibri.ttf', 22), fill=CAFE)
d.text((cx + 22, cy2 + 90), 'Crédito por nómina: Cajasan (0,8%)', font=font('calibri.ttf', 20), fill=GRIS)
d.text((cx + 22, cy2 + 118), 'y Comultrasan (1,8%). Aprobación rápida.', font=font('calibri.ttf', 20), fill=GRIS)

# programas (abajo izquierda)
py = 712
d.text((x0, py), 'PROGRAMAS', font=font('calibrib.ttf', 26), fill=NAR)
progs = ['Súper intensivo 4 h · L-V 8:00 a 12:00', 'Intensivo 2 h · L-V 6:30 a 8:30 pm', 'Tarde entre semana · en apertura', 'Sabatino 4 h · 8:00 a 12:00 · un nivel a la vez', 'Clases personalizadas · desde 30 h']
for i, t in enumerate(progs):
    cxp = x0 + (i % 2) * 500; cyp = py + 38 + (i // 2) * 32
    d.ellipse([cxp, cyp + 9, cxp + 10, cyp + 19], fill=AMAR, outline=NAR)
    d.text((cxp + 20, cyp), t, font=font('calibri.ttf', 22), fill=CAFE)

# pie
d.text((x0, H - 46), 'Formas de pago: contado · cuotas con inicial y mensualidades · cesantías · crédito banco o cooperativa', font=font('calibri.ttf', 21), fill=GRIS)
d.text((W - 190, H - 46), 'Heiiu English Academy · Bucaramanga', font=font('calibri.ttf', 21), fill=GRIS, anchor='rt')

out = os.path.join(BASE, r'recursos\comercial\INDUCCION_COMERCIAL\PRECIOS_2026_HEIIU.png')
try: img.save(out, optimize=True); print('OK', out)
except OSError: img.save(out.replace('.png', '_v2.png'), optimize=True); print('ABIERTA -> _v2')
