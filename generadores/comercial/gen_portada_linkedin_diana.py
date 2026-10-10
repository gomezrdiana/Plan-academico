# -*- coding: utf-8 -*-
"""Portada de LinkedIn (1584x396) para el perfil de Diana — estilo ejecutivo Heiiu, 'Estamos contratando'.
Ojo: en el perfil, la foto tapa la esquina inferior izquierda (≈ x 0-560, y 200-396): no poner texto ahí.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/LINKEDIN DIANA GOMEZ/PORTADA_LINKEDIN_DIANA.png"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
NAR = (229, 76, 9); AMAR = (251, 201, 0); CREMA = (255, 248, 231); FONDO = (24, 21, 18); GRIS = (180, 170, 160)
F = 'C:/Windows/Fonts/'
def font(n, s): return ImageFont.truetype(F + n, s)
W, H = 1584, 396

im = Image.new('RGB', (W, H), FONDO)
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
g.ellipse([W - 700, -350, W + 250, 450], fill=NAR + (130,))
g.ellipse([200, 150, 900, 700], fill=NAR + (40,))
glow = glow.filter(ImageFilter.GaussianBlur(120))
im = Image.alpha_composite(im.convert('RGBA'), glow); d = ImageDraw.Draw(im)

X = 600  # todo el texto a la derecha de la zona de la foto
d.text((X, 70), 'HEIIU ENGLISH ACADEMY · BUCARAMANGA', font=font('calibrib.ttf', 26), fill=AMAR)
d.text((X, 108), 'Formamos personas a través del inglés', font=font('calibrib.ttf', 58), fill=(255, 255, 255))
d.text((X, 182), 'Garantía de aprendizaje por escrito · Triple certificación ICONTEC · Desde 2012', font=font('calibri.ttf', 28), fill=GRIS)
d.line([X, 240, X + 110, 240], fill=AMAR, width=4)
# sello contratando
d.rounded_rectangle([X, 268, X + 520, 330], radius=31, fill=AMAR)
d.text((X + 260, 299), 'ESTAMOS CONTRATANDO · Alianzas B2B', font=font('calibrib.ttf', 28), fill=FONDO, anchor='mm')
d.text((X + 545, 299), 'citasheiiu@gmail.com', font=font('calibri.ttf', 28), fill=CREMA, anchor='lm')

# logo arriba a la derecha
try:
    logo = Image.open(os.path.join(BASE, r'recursos\marca heiiu\logo_heiiu_sobre_naranja.png')).convert('RGBA')
    lh = 58; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    im.paste(logo, (W - lw - 40, 22), logo)
except Exception:
    pass

out = os.path.join(BASE, r'recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\PORTADA_LINKEDIN_DIANA.png')
im = im.convert('RGB')
try: im.save(out); print('OK', out)
except (PermissionError, OSError): im.save(out.replace('.png', '_v2.png')); print('ABIERTO -> _v2')
