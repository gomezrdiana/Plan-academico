# -*- coding: utf-8 -*-
"""Pieza de reactivacion de leads para LaHaus (imagen horizontal que acompana el mensaje de WhatsApp). Estilo de los carruseles IG Heiiu.
Salida: recursos/comercial/plataforma LaHaus/PIEZA_REACTIVACION_HEIIU.png"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 840
BG = (48, 39, 28); CREMA = (255, 248, 231); AMAR = (251, 201, 0); NAR = (229, 76, 9); GRIS = (200, 190, 175); CARD = (62, 51, 37)
F = 'C:/Windows/Fonts/'
def font(name, size): return ImageFont.truetype(F + name, size)

img = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(img)

# logo
try:
    logo = Image.open(r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\marca heiiu\logo_heiiu_sobre_naranja.png').convert('RGBA')
    lh = 86; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    pad = Image.new('RGBA', (lw + 36, lh + 24), NAR + (255,)); pad.paste(logo, (18, 12), logo)
    img.paste(pad, (72, 56), pad)
except Exception as e:
    d.text((72, 60), 'heiiu', font=font('calibrib.ttf', 54), fill=AMAR)

# eyebrow + linea
d.text((72, 212), 'YA DISTE EL PRIMER PASO', font=font('calibrib.ttf', 26), fill=AMAR, spacing=4)
d.rectangle([72, 252, 182, 257], fill=NAR)

# titular
d.text((72, 290), 'Nos escribiste', font=font('calibrib.ttf', 86), fill=CREMA)
d.text((72, 384), 'por el inglés.', font=font('calibrib.ttf', 86), fill=CREMA)
# subtitulo
d.text((72, 500), '¿Sigue siendo una meta para ti?', font=font('georgiai.ttf', 44), fill=AMAR)
# prueba
d.text((72, 572), 'Desde 2012 en Bucaramanga. Entrenamiento presencial con', font=font('calibri.ttf', 29), fill=GRIS)
d.text((72, 608), 'garantía de aprendizaje por escrito en el contrato.', font=font('calibri.ttf', 29), fill=GRIS)
# boton
bx, by, bw, bh = 72, 672, 470, 70
d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14, fill=AMAR)
d.text((bx + 34, by + 17), 'Responde este mensaje  →', font=font('calibrib.ttf', 30), fill=(48, 39, 28))
# pie
d.text((72, 772), 'heiiu  ·  @heiiu_english  ·  Carrera 27 # 48-49, Sotomayor, segundo piso', font=font('calibri.ttf', 24), fill=GRIS)

# tarjetas de motivo (lado derecho)
cards = [('UN TRABAJO', 'la vacante que hoy\npasas de largo'), ('UN VIAJE', 'pasar inmigración con\ntus propias respuestas'), ('UN ESTUDIO', 'la beca o el posgrado\nsin ese requisito'), ('UN NEGOCIO', 'clientes de afuera\nsin traductor')]
cw, ch, gap = 300, 215, 24
x0 = W - 72 - (2 * cw + gap); y0 = 262
for i, (tit, sub) in enumerate(cards):
    cx = x0 + (i % 2) * (cw + gap); cy = y0 + (i // 2) * (ch + gap)
    d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=22, fill=CARD, outline=(90, 76, 58), width=2)
    d.rectangle([cx + 28, cy + 30, cx + 88, cy + 35], fill=NAR)
    d.text((cx + 28, cy + 56), tit, font=font('calibrib.ttf', 32), fill=AMAR)
    d.multiline_text((cx + 28, cy + 110), sub, font=font('calibri.ttf', 27), fill=CREMA, spacing=8)
d.text((x0, y0 - 44), 'LO QUE NOS DIJISTE QUE QUERÍAS', font=font('calibrib.ttf', 22), fill=GRIS)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus\PIEZA_REACTIVACION_HEIIU.png'
img.save(out, optimize=True); print('OK', out)
