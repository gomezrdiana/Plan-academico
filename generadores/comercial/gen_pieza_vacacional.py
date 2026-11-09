# -*- coding: utf-8 -*-
"""Pieza de imagen del vacacional de ninos (7 a 12) para WhatsApp e Instagram.
Salidas en recursos/comercial/productos/VACACIONAL_KIDS/:
 - PIEZA_VACACIONAL_HISTORIA.png (1080x1920, historias)
 - PIEZA_VACACIONAL_CUADRADA.png (1080x1080, feed y WhatsApp)
Textos editables en CONFIG."""
import os, io
import qrcode
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'VACACIONAL_KIDS')
LOGO = os.path.join(ROOT, 'recursos', 'marca heiiu', 'logo_heiiu_transparente.png')

CONFIG = dict(
    whatsapp='573177173641', whatsapp_visible='317 717 3641',
    mensaje_qr='Hola, quiero información de Vacaciones en inglés para mi hijo. Código: VACACIONAL',
    titulo='VACACIONES EN INGLÉS', edades='Niños de 7 a 12 años',
    cuerpo='Mañanas de 8 a 12 en la sede, todo en inglés: historias, juegos y una misión cada día.',
    promesa='Cada viernes recibes el video de tu hijo hablando inglés.',
    semanas_titulo='Semanas de lunes a viernes:',
    semanas=['23 al 27 de noviembre', '30 de noviembre al 4 de diciembre', '7 al 11 de diciembre', '14 al 18 de diciembre'],
    precio='$290.000 la semana  o  $490.000 dos semanas',
    sede='Sede Heiiu · Barrio Sotomayor, Bucaramanga',
)

NARANJA = (229, 76, 9); NARANJA_LOGO = (255, 74, 0); AMARILLO = (251, 201, 0); CREMA = (255, 248, 231); TINTA = (42, 26, 18); BLANCO = (255, 255, 255)
F_ROUND = 'C:/Windows/Fonts/ARLRDBD.TTF'; F_AR = 'C:/Windows/Fonts/arial.ttf'; F_ARB = 'C:/Windows/Fonts/arialbd.ttf'

def font(path, size):
    return ImageFont.truetype(path, size)

def qr_img(px):
    url = 'https://wa.me/%s?text=%s' % (CONFIG['whatsapp'], CONFIG['mensaje_qr'].replace(' ', '%20'))
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=1)
    q.add_data(url); q.make(fit=True)
    return q.make_image(fill_color='#2A1A12', back_color='white').convert('RGB').resize((px, px), Image.NEAREST)

def wrap(draw, text, fnt, maxw):
    words = text.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=fnt) > maxw and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    if cur: lines.append(cur)
    return lines

def par(draw, W, y, text, fnt, maxw, leading, fill=TINTA, center=True, x=None):
    for ln in wrap(draw, text, fnt, maxw):
        if center:
            draw.text((W / 2, y), ln, font=fnt, fill=fill, anchor='ma')
        else:
            draw.text((x, y), ln, font=fnt, fill=fill, anchor='la')
        y += leading
    return y

def banda_logo(im, W, bh):
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, bh], fill=NARANJA_LOGO)
    logo = Image.open(LOGO).convert('RGBA')
    lw = int(W * 0.42); lh = int(logo.height * lw / logo.width)
    if lh > bh * 0.7:
        lh = int(bh * 0.7); lw = int(logo.width * lh / logo.height)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    im.paste(logo, ((W - lw) // 2, (bh - lh) // 2), logo)

def historia():
    W, H = 1080, 1920
    im = Image.new('RGB', (W, H), CREMA); d = ImageDraw.Draw(im)
    bh = 260; banda_logo(im, W, bh)
    # franja amarilla con el titulo
    y = bh + 40
    d.rectangle([0, y, W, y + 150], fill=AMARILLO)
    d.text((W / 2, y + 75), CONFIG['titulo'], font=font(F_ROUND, 78), fill=TINTA, anchor='mm')
    y += 150 + 50
    d.text((W / 2, y), CONFIG['edades'], font=font(F_ROUND, 60), fill=NARANJA, anchor='ma'); y += 110
    y = par(d, W, y, CONFIG['cuerpo'], font(F_AR, 40), W - 160, 54); y += 36
    # caja oscura con la promesa
    lines = wrap(d, CONFIG['promesa'], font(F_ROUND, 46), W - 220)
    ch = 60 + 62 * len(lines)
    d.rounded_rectangle([70, y, W - 70, y + ch], radius=28, fill=TINTA)
    yy = y + 30
    for ln in lines:
        d.text((W / 2, yy), ln, font=font(F_ROUND, 46), fill=CREMA, anchor='ma'); yy += 62
    y += ch + 50
    # semanas
    d.text((W / 2, y), CONFIG['semanas_titulo'], font=font(F_ARB, 38), fill=TINTA, anchor='ma'); y += 60
    for s in CONFIG['semanas']:
        d.text((W / 2, y), s, font=font(F_AR, 40), fill=TINTA, anchor='ma'); y += 54
    y += 30
    # precio
    d.rectangle([0, y, W, y + 110], fill=AMARILLO)
    d.text((W / 2, y + 55), CONFIG['precio'], font=font(F_ROUND, 42), fill=TINTA, anchor='mm'); y += 110 + 50
    # QR + numero
    q = qr_img(300); im.paste(q, (90, y))
    d.text((430, y + 40), 'Escribe por WhatsApp', font=font(F_ARB, 38), fill=TINTA, anchor='la')
    d.text((430, y + 100), CONFIG['whatsapp_visible'], font=font(F_ROUND, 74), fill=NARANJA, anchor='la')
    d.text((430, y + 200), 'o escanea el código', font=font(F_AR, 34), fill=TINTA, anchor='la')
    # pie
    d.text((W / 2, H - 70), CONFIG['sede'], font=font(F_AR, 32), fill=TINTA, anchor='ma')
    return im

def cuadrada():
    W, H = 1080, 1080
    im = Image.new('RGB', (W, H), CREMA); d = ImageDraw.Draw(im)
    bh = 170; banda_logo(im, W, bh)
    y = bh + 24
    d.rectangle([0, y, W, y + 110], fill=AMARILLO)
    d.text((W / 2, y + 55), CONFIG['titulo'], font=font(F_ROUND, 62), fill=TINTA, anchor='mm'); y += 110 + 26
    d.text((W / 2, y), CONFIG['edades'], font=font(F_ROUND, 46), fill=NARANJA, anchor='ma'); y += 70
    y = par(d, W, y, CONFIG['cuerpo'], font(F_AR, 32), W - 140, 42); y += 20
    lines = wrap(d, CONFIG['promesa'], font(F_ROUND, 36), W - 200)
    ch = 40 + 48 * len(lines)
    d.rounded_rectangle([60, y, W - 60, y + ch], radius=22, fill=TINTA)
    yy = y + 20
    for ln in lines:
        d.text((W / 2, yy), ln, font=font(F_ROUND, 36), fill=CREMA, anchor='ma'); yy += 48
    y += ch + 26
    sem = ' · '.join(['23-27 nov', '30 nov-4 dic', '7-11 dic', '14-18 dic'])
    d.text((W / 2, y), 'Semanas de lunes a viernes: ' + sem, font=font(F_AR, 29), fill=TINTA, anchor='ma'); y += 50
    d.rectangle([0, y, W, y + 80], fill=AMARILLO)
    d.text((W / 2, y + 40), CONFIG['precio'], font=font(F_ROUND, 34), fill=TINTA, anchor='mm'); y += 80 + 24
    q = qr_img(200); im.paste(q, (90, y))
    d.text((320, y + 20), 'Escribe por WhatsApp', font=font(F_ARB, 30), fill=TINTA, anchor='la')
    d.text((320, y + 64), CONFIG['whatsapp_visible'], font=font(F_ROUND, 60), fill=NARANJA, anchor='la')
    d.text((320, y + 146), CONFIG['sede'], font=font(F_AR, 26), fill=TINTA, anchor='la')
    return im

if __name__ == '__main__':
    for name, fn in [('PIEZA_VACACIONAL_HISTORIA.png', historia), ('PIEZA_VACACIONAL_CUADRADA.png', cuadrada)]:
        p = os.path.join(OUT, name); fn().save(p, optimize=True); print('OK', p, os.path.getsize(p))
