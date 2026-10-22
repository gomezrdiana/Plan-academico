# -*- coding: utf-8 -*-
"""Bosquejo de la pieza del programa de referidos para asesores de cajas de compensacion y cooperativas aliadas
(bono recargable de $200.000 por matricula). Reemplaza la propuesta en azul del gerente de alianzas:
marca Heiiu (naranja + amarillo + crema), sin logos de terceros, sin "en efectivo", con codigo, con el paso
de la matricula pagada y con la vigencia del piloto. Vertical 1080x1620 (WhatsApp / impresion media carta).
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PIEZA_REFERIDOS_ASESORAS_BOSQUEJO.png
        + copia en la carpeta del gerente de alianzas (plan referidos/)."""
import os, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1730
NAR = (229, 76, 9); AMAR = (251, 201, 0); CREMA = (255, 248, 231); OSC = (48, 39, 28); GRIS = (110, 100, 88); BLANCO = (255, 255, 255)
F = 'C:/Windows/Fonts/'
ROOT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
LOGO = ROOT + r'\recursos\marca heiiu\logo_heiiu_sobre_naranja.png'
OUT = ROOT + r'\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PIEZA_REFERIDOS_ASESORAS_BOSQUEJO.png'
COPIA = ROOT + r'\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza\plan referidos\PIEZA_REFERIDOS_ASESORAS_BOSQUEJO.png'
def font(name, size): return ImageFont.truetype(F + name, size)

def wrap(d, txt, fnt, maxw):
    out, cur = [], ''
    for w in txt.split(' '):
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=fnt) <= maxw: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out

def parrafo(d, x, y, txt, fnt, fill, maxw, lh=None, align='left'):
    lh = lh or int(fnt.size * 1.28)
    for ln in wrap(d, txt, fnt, maxw):
        xx = x if align == 'left' else x + (maxw - d.textlength(ln, font=fnt)) / 2
        d.text((xx, y), ln, font=fnt, fill=fill); y += lh
    return y

img = Image.new('RGB', (W, H), CREMA); d = ImageDraw.Draw(img)

# ---- banda superior naranja con el logo (el logo viene sobre naranja)
logo = Image.open(LOGO).convert('RGB'); band_col = logo.getpixel((3, 3))
BAND = 222
d.rectangle([0, 0, W, BAND], fill=band_col)
lh_ = 150; lw_ = int(logo.width * lh_ / logo.height); logo = logo.resize((lw_, lh_), Image.LANCZOS)
img.paste(logo, (60, 26))
# etiqueta del programa, a la derecha del logo
tag = 'PROGRAMA DE REFERIDOS · CAJAS Y COOPERATIVAS ALIADAS'
ft = font('calibrib.ttf', 22)
d.text((60, 182), tag, font=ft, fill=CREMA)

# ---- titular
y = BAND + 46
d.rectangle([60, y, 170, y + 6], fill=NAR); y += 28
f_t = font('calibrib.ttf', 74)
d.text((60, y), 'Tu recomendación', font=f_t, fill=OSC); y += 76
d.text((60, y), 'también cuenta.', font=f_t, fill=OSC); y += 92
f_b = font('georgiai.ttf', 33)
y = parrafo(d, 60, y, 'Si eres asesor o asesora de una caja de compensación o cooperativa aliada de Heiiu, '
            'recibes un bono por cada afiliado que se matricule con tu código.', f_b, GRIS, W - 120, lh=44)

# ---- panel oscuro con el bono
y += 28
px0, py0, px1, py1 = 60, y, W - 60, y + 280
sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
sd.rounded_rectangle([px0 + 6, py0 + 14, px1 + 6, py1 + 14], radius=28, fill=(0, 0, 0, 70)); sh = sh.filter(ImageFilter.GaussianBlur(12))
img = Image.alpha_composite(img.convert('RGBA'), sh).convert('RGB'); d = ImageDraw.Draw(img)
d.rounded_rectangle([px0, py0, px1, py1], radius=28, fill=OSC)
d.text((px0 + 48, py0 + 40), 'POR CADA MATRÍCULA, RECARGAMOS TU BONO CON', font=font('calibrib.ttf', 26), fill=CREMA)
f_n = font('georgiab.ttf', 118)
d.text((px0 + 44, py0 + 86), '$200.000', font=f_n, fill=AMAR)
d.text((px0 + 48, py0 + 218), 'en tu tarjeta recargable, a tu nombre', font=font('calibri.ttf', 30), fill=CREMA)
# sello lateral
cx, cy, r = px1 - 120, py0 + 140, 84
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=NAR)
d.text((cx, cy - 28), 'PILOTO', font=font('calibrib.ttf', 26), fill=CREMA, anchor='mm')
d.text((cx, cy + 2), 'hasta el', font=font('calibri.ttf', 22), fill=CREMA, anchor='mm')
d.text((cx, cy + 34), '31 ene 2027', font=font('calibrib.ttf', 26), fill=CREMA, anchor='mm')
y = py1 + 48

# ---- como funciona: 4 pasos
d.text((60, y), '¿Cómo funciona?', font=font('calibrib.ttf', 44), fill=OSC); y += 70
pasos = [
    ('Comparte', 'Le cuentas a tu afiliado que puede estudiar inglés en Heiiu y le das tu código de asesor.'),
    ('Se matricula', 'Firma el contrato, paga la cuota inicial y entrega tu código en la matrícula.'),
    ('Entra el pago', 'Pasan los cinco días de retracto y Heiiu recibe el pago de la entidad o del estudiante.'),
    ('Recargamos tu bono', 'Ese mes cargamos $200.000 a tu tarjeta. Sin cuentas de cobro ni papeles.'),
]
cw, gap = (W - 120 - 3 * 18) // 4, 18
ch = 272
for i, (tit, sub) in enumerate(pasos):
    cx0 = 60 + i * (cw + gap)
    d.rounded_rectangle([cx0, y, cx0 + cw, y + ch], radius=20, fill=BLANCO, outline=(232, 220, 200), width=2)
    d.ellipse([cx0 + 20, y + 20, cx0 + 68, y + 68], fill=NAR)
    d.text((cx0 + 44, y + 44), str(i + 1), font=font('calibrib.ttf', 28), fill=CREMA, anchor='mm')
    yy = y + 84
    for ln in wrap(d, tit, font('calibrib.ttf', 27), cw - 40):
        d.text((cx0 + 20, yy), ln, font=font('calibrib.ttf', 27), fill=NAR); yy += 32
    yy += 6
    parrafo(d, cx0 + 20, yy, sub, font('calibri.ttf', 22), OSC, cw - 40, lh=27)
y += ch + 30

# ---- caja amarilla: programa de cupos (opcional, si se aprueba)
d.rounded_rectangle([60, y, W - 60, y + 112], radius=20, fill=AMAR)
d.text((92, y + 20), 'Y SI LLEGAS A DOS MATRÍCULAS EN EL TRIMESTRE', font=font('calibrib.ttf', 25), fill=OSC)
d.text((92, y + 56), 'un nivel de inglés en Heiiu para ti o para un familiar, además del bono.', font=font('georgiai.ttf', 29), fill=OSC)
y += 112 + 30

# ---- condiciones en letra pequeña
cond = ('Condiciones: el bono se causa por matrícula con contrato firmado, cuota inicial pagada y los cinco días de retracto cumplidos, '
        'una vez Heiiu recibe el pago. Un código por asesor; sin código no hay bono. Bono nominativo, entregado en tarjeta recargable; '
        'no se paga en efectivo. Programa piloto vigente hasta el 31 de enero de 2027 e informado a la dirección de cada oficina.')
y = parrafo(d, 60, y, cond, font('calibri.ttf', 19), GRIS, W - 120, lh=24)

# ---- pie
fy = H - 120
d.rectangle([0, fy, W, H], fill=NAR)
d.text((60, fy + 26), 'Tu contacto en Heiiu: gerente de alianzas', font=font('calibrib.ttf', 26), fill=CREMA)
d.text((60, fy + 64), 'ger.alianzas@heiiu.com  ·  [celular del gerente de alianzas]', font=font('calibri.ttf', 24), fill=CREMA)
d.text((W - 60, fy + 26), 'Presencial en Bucaramanga', font=font('calibrib.ttf', 24), fill=AMAR, anchor='ra')
d.text((W - 60, fy + 64), 'Garantía de aprendizaje por escrito', font=font('calibri.ttf', 22), fill=CREMA, anchor='ra')

os.makedirs(os.path.dirname(COPIA), exist_ok=True)
for p in (OUT, COPIA):
    try: img.save(p, optimize=True); print('OK', p)
    except OSError: p2 = p.replace('.png', '_v2.png'); img.save(p2, optimize=True); print('ABIERTA ->', p2)
