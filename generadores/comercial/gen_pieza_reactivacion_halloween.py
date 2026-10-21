# -*- coding: utf-8 -*-
"""Dos piezas de reactivacion de octubre (gancho de temporada) para la plantilla de LaHaus, misma base visual de
gen_pieza_reactivacion.py. Prueba A/B de mensaje, mitad y mitad:
  A = "Lo que deberia darte miedo es perder la oportunidad" (consecuencia / destino)
  B = "Que no te de miedo hablar ingles" (angulo propuesto por LaHaus)
Etiqueta de temporada: ESTE HALLOWEEN. Sin programa ni precio.
Salida: recursos/comercial/plataforma LaHaus/PIEZA_REACTIVACION_OCTUBRE_A_HEIIU.png y _B_"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1600, 840
BG = (48, 39, 28); CREMA = (255, 248, 231); AMAR = (251, 201, 0); NAR = (229, 76, 9); GRIS = (210, 200, 185)
F = 'C:/Windows/Fonts/'
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus'
LOGO = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\marca heiiu\logo_heiiu_sobre_naranja.png'
def font(name, size): return ImageFont.truetype(F + name, size)

PIEZAS = {
    'A': dict(titular=['Lo que debería', 'darte miedo es', 'perder la oportunidad.'], tsize=78,
              bajada=['La entrevista, el viaje o el cliente', 'llegan igual, con o sin inglés.']),
    'B': dict(titular=['Que no te dé miedo', 'hablar inglés.'], tsize=92,
              bajada=['Aquí se habla desde la primera clase,', 'con un profesor al lado que te corrige.']),
}

def fondo():
    foto = os.path.join(BASE, 'fondo_reactivacion.jpg')
    if os.path.exists(foto):
        img = Image.open(foto).convert('RGB')
        img = img.crop((int(img.width * 0.18), 0, img.width, int(img.height * 0.56)))
        r = max(W / img.width, H / img.height); img = img.resize((int(img.width * r) + 1, int(img.height * r) + 1))
        x = (img.width - W) // 2; y = (img.height - H) // 2; img = img.crop((x, y, x + W, y + H))
        overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(overlay)
        for i in range(W):
            od.line([(i, 0), (i, H)], fill=(40, 30, 22, int(246 - 100 * (i / W))))
        img = img.filter(ImageFilter.GaussianBlur(5))
        return Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    return Image.new('RGB', (W, H), BG)

def pieza(key, cfg):
    img = fondo(); d = ImageDraw.Draw(img)
    logo = Image.open(LOGO).convert('RGBA'); lh = 130; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
    pad = Image.new('RGBA', (lw + 44, lh + 30), NAR + (255,)); pad.paste(logo, (22, 15), logo)
    sh = Image.new('RGBA', (pad.width + 24, pad.height + 24), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle([12, 12, sh.width - 12, sh.height - 12], radius=10, fill=(0, 0, 0, 120)); sh = sh.filter(ImageFilter.GaussianBlur(10))
    img.paste(sh, (72 - 12, 56 - 6), sh); img.paste(pad, (72, 56), pad)

    # guiño de temporada: murcielagos dibujados con tiza, sutiles
    HALF = [(0,-22),(7,-36),(11,-20),(30,-27),(60,-32),(100,-30),(97,-20),(84,2),(72,-7),(58,8),(44,-2),(30,12),(16,4),(8,17),(0,21)]
    BAT = HALF + [(-x, y) for x, y in reversed(HALF[:-1])]
    bl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(bl)
    for (bx0, by0, sc, al, rot) in [(640, 130, 0.95, 165, -8), (790, 70, 0.6, 130, 10), (560, 215, 0.42, 110, -14), (1440, 150, 0.7, 140, 12), (1300, 225, 0.4, 100, -6)]:
        import math
        cr, sr = math.cos(math.radians(rot)), math.sin(math.radians(rot))
        pts = [(bx0 + (x * cr - y * sr) * sc, by0 + (x * sr + y * cr) * sc) for x, y in BAT]
        bd.polygon(pts, fill=(255, 248, 231, al))
    bl = bl.filter(ImageFilter.GaussianBlur(1.2))
    img = Image.alpha_composite(img.convert('RGBA'), bl).convert('RGB'); d = ImageDraw.Draw(img)
    d.text((72, 262), 'ESTE HALLOWEEN', font=font('calibrib.ttf', 26), fill=AMAR)
    d.rectangle([72, 302, 182, 307], fill=NAR)
    ts = cfg['tsize']; y = 326
    def linea(x, y, line, fnt, base, hi_font, hi_size):
        # dibuja la linea; la palabra "ingles" va en amarillo, mas grande y en otra letra, alineada a la misma base
        yb = y + fnt.getmetrics()[0]
        for w in line.split(' '):
            if w.startswith('inglés'):
                f2 = font(hi_font, hi_size); d.text((x, yb), w, font=f2, fill=AMAR, anchor='ls'); x += d.textlength(w, font=f2) + d.textlength(' ', font=fnt)
            else:
                d.text((x, yb), w, font=fnt, fill=base, anchor='ls'); x += d.textlength(w + ' ', font=fnt)
    for line in cfg['titular']:
        if 'inglés' in line: y += 10
        linea(72, y, line, font('calibrib.ttf', ts), CREMA, 'georgiab.ttf', int(ts * 1.22)); y += int(ts * 1.08)
    y += 14
    for line in cfg['bajada']:
        linea(72, y, line, font('georgiai.ttf', 38), AMAR, 'calibrib.ttf', 52); y += 46
    d.text((72, 696), 'Presencial en Bucaramanga · única academia con garantía de aprendizaje por escrito', font=font('calibri.ttf', 24), fill=GRIS)
    bx, by, bw, bh = 72, 736, 400, 64
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14, fill=AMAR)
    d.text((bx + 34, by + 15), 'Quiero mi fecha  →', font=font('calibrib.ttf', 30), fill=BG)

    cards = [('UN TRABAJO', 'la vacante que hoy\npasas de largo'), ('UN VIAJE', 'pasar inmigración con\ntus propias respuestas'),
             ('UN ESTUDIO', 'la beca o el posgrado\nsin ese requisito'), ('UN NEGOCIO', 'clientes de afuera\nsin traductor')]
    cw, ch, gap = 250, 160, 20
    x0 = W - 72 - (2 * cw + gap); y0 = 330
    cl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(cl)
    for i, _ in enumerate(cards):
        cx = x0 + (i % 2) * (cw + gap); cy = y0 + (i // 2) * (ch + gap)
        cd.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=18, fill=(48, 39, 28, 175), outline=(140, 118, 88, 200), width=2)
    img = Image.alpha_composite(img.convert('RGBA'), cl).convert('RGB'); d = ImageDraw.Draw(img)
    for i, (tit, sub) in enumerate(cards):
        cx = x0 + (i % 2) * (cw + gap); cy = y0 + (i // 2) * (ch + gap)
        d.rectangle([cx + 22, cy + 22, cx + 70, cy + 26], fill=NAR)
        d.text((cx + 22, cy + 40), tit, font=font('calibrib.ttf', 25), fill=AMAR)
        d.multiline_text((cx + 22, cy + 82), sub, font=font('calibri.ttf', 22), fill=CREMA, spacing=6)
    d.text((x0, y0 - 40), 'LO QUE NOS DIJISTE QUE QUERÍAS', font=font('calibrib.ttf', 20), fill=GRIS)

    ix, iy, isz = W - 72 - 300, 784, 30
    d.rounded_rectangle([ix, iy, ix + isz, iy + isz], radius=9, outline=AMAR, width=3)
    d.ellipse([ix + 8, iy + 8, ix + isz - 8, iy + isz - 8], outline=AMAR, width=3)
    d.ellipse([ix + isz - 10, iy + 5, ix + isz - 5, iy + 10], fill=AMAR)
    fh = font('calibrib.ttf', 28); bb = d.textbbox((0, 0), '@heiiu_english', font=fh)
    d.text((ix + isz + 12, iy + (isz - (bb[3] - bb[1])) // 2 - bb[1]), '@heiiu_english', font=fh, fill=AMAR)

    out = os.path.join(BASE, 'PIEZA_REACTIVACION_OCTUBRE_%s_HEIIU.png' % key)
    try:
        img.save(out, optimize=True); print('OK', out)
    except OSError:
        out2 = out.replace('.png', '_v2.png'); img.save(out2, optimize=True); print('ABIERTA -> guardada como', out2)

for k, c in PIEZAS.items(): pieza(k, c)
