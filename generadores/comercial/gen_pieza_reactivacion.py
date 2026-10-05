# -*- coding: utf-8 -*-
"""Pieza de reactivacion de leads para LaHaus (horizontal). Version corta: titular + pregunta + garantia + boton.
Fondo: foto real si existe `recursos/comercial/plataforma LaHaus/fondo_reactivacion.jpg` (con capa oscura); si no, fondo de marca.
Salida: recursos/comercial/plataforma LaHaus/PIEZA_REACTIVACION_HEIIU.png"""
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
    # recorte a 1600x840 cubriendo
    r = max(W / img.width, H / img.height); img = img.resize((int(img.width * r) + 1, int(img.height * r) + 1))
    x = (img.width - W) // 2; y = (img.height - H) // 2; img = img.crop((x, y, x + W, y + H))
    # capa oscura con degradado: mas oscura a la izquierda (texto), mas foto a la derecha
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(overlay)
    for i in range(W):
        a = int(235 - 110 * (i / W))  # 235 -> 125
        od.line([(i, 0), (i, H)], fill=(48, 39, 28, a))
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
else:
    img = Image.new('RGB', (W, H), BG)
    # fondo de marca: circulos suaves en naranja y amarillo, muy tenues
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    ld.ellipse([980, -260, 1900, 660], fill=(229, 76, 9, 46))
    ld.ellipse([1180, 300, 1760, 880], fill=(251, 201, 0, 34))
    ld.ellipse([-320, 520, 420, 1260], fill=(229, 76, 9, 26))
    layer = layer.filter(ImageFilter.GaussianBlur(70))
    img = Image.alpha_composite(img.convert('RGBA'), layer).convert('RGB')

d = ImageDraw.Draw(img)

# logo
try:
    logo = Image.open(r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\marca heiiu\logo_heiiu_sobre_naranja.png').convert('RGBA')
    lh = 86; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    pad = Image.new('RGBA', (lw + 36, lh + 24), NAR + (255,)); pad.paste(logo, (18, 12), logo)
    img.paste(pad, (72, 56), pad)
except Exception:
    d.text((72, 60), 'heiiu', font=font('calibrib.ttf', 54), fill=AMAR)

# etiqueta
d.text((72, 268), 'YA DISTE EL PRIMER PASO', font=font('calibrib.ttf', 26), fill=AMAR)
d.rectangle([72, 308, 182, 313], fill=NAR)
# titular
d.text((72, 340), 'Nos escribiste', font=font('calibrib.ttf', 96), fill=CREMA)
d.text((72, 446), 'por el inglés.', font=font('calibrib.ttf', 96), fill=CREMA)
# pregunta
d.text((72, 572), '¿Sigue siendo una meta para ti?', font=font('georgiai.ttf', 46), fill=AMAR)
# garantia
d.text((72, 644), 'Garantía de aprendizaje firmada.', font=font('calibri.ttf', 30), fill=GRIS)
# boton
bx, by, bw, bh = 72, 706, 470, 70
d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14, fill=AMAR)
d.text((bx + 34, by + 17), 'Responde este mensaje  →', font=font('calibrib.ttf', 30), fill=BG)
# pie
d.text((W - 72 - 330, 790), 'heiiu  ·  @heiiu_english', font=font('calibri.ttf', 24), fill=GRIS)

out = os.path.join(BASE, 'PIEZA_REACTIVACION_HEIIU.png')
try:
    img.save(out, optimize=True); print('OK', out)
except OSError:
    out2 = os.path.join(BASE, 'PIEZA_REACTIVACION_HEIIU_v2.png'); img.save(out2, optimize=True); print('ABIERTA -> guardada como', out2)
