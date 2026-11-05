# -*- coding: utf-8 -*-
"""Volante: clase de cortesía gratis en la sede. Salidas:
 - VOLANTE_CLASE_CORTESIA.pdf  (media carta, 1 volante)
 - VOLANTE_CLASE_CORTESIA_2xCARTA.pdf (dos por hoja carta, para imprimir y cortar)
 - VOLANTE_CLASE_CORTESIA.png  (para WhatsApp / redes)
Datos editables abajo en CONFIG."""
import os, io
import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'campanas', 'VOLANTE_CLASE_CORTESIA')
LOGO = os.path.join(ROOT, 'recursos', 'marca heiiu', 'logo_heiiu_sobre_naranja.png')
os.makedirs(OUT, exist_ok=True)

CONFIG = dict(
    whatsapp='573177173641',
    whatsapp_visible='317 717 3641',
    mensaje_qr='Hola, quiero agendar mi clase de cortesía gratis. Código: VOLANTE',
    sede='Sede Heiiu · Barrio Sotomayor, Bucaramanga',
)

pdfmetrics.registerFont(TTFont('Rounded', 'C:/Windows/Fonts/ARLRDBD.TTF'))
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialB', 'C:/Windows/Fonts/arialbd.ttf'))

NARANJA = colors.HexColor('#E54C09'); AMARILLO = colors.HexColor('#FBC900')
CREMA = colors.HexColor('#FFF8E7'); TINTA = colors.HexColor('#2A1A12'); BLANCO = colors.white
W, H = 5.5 * inch, 8.5 * inch

def qr_image():
    url = 'https://wa.me/%s?text=%s' % (CONFIG['whatsapp'], CONFIG['mensaje_qr'].replace(' ', '%20'))
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=1)
    q.add_data(url); q.make(fit=True)
    im = q.make_image(fill_color='#2A1A12', back_color='white').convert('RGB')
    b = io.BytesIO(); im.save(b, format='PNG'); b.seek(0)
    return ImageReader(b)

def wrap(c, text, font, size, maxw):
    words = text.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if c.stringWidth(t, font, size) > maxw and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    if cur: lines.append(cur)
    return lines

def draw_par(c, x, y, text, font, size, maxw, leading, color=TINTA, align='left'):
    c.setFont(font, size); c.setFillColor(color)
    for ln in wrap(c, text, font, size, maxw):
        if align == 'center': c.drawCentredString(x + maxw / 2, y, ln)
        else: c.drawString(x, y, ln)
        y -= leading
    return y

def volante(c, ox=0, oy=0):
    c.saveState(); c.translate(ox, oy)
    M = 0.35 * inch
    # fondo crema
    c.setFillColor(CREMA); c.rect(0, 0, W, H, stroke=0, fill=1)
    # banda naranja superior con logo
    bh = 1.25 * inch
    c.setFillColor(NARANJA); c.rect(0, H - bh, W, bh, stroke=0, fill=1)
    c.drawImage(LOGO, M, H - bh + 0.28 * inch, width=1.55 * inch, height=0.72 * inch, preserveAspectRatio=True, mask='auto')
    c.setFont('Rounded', 10); c.setFillColor(BLANCO)
    c.drawRightString(W - M, H - bh + 0.72 * inch, 'INGLÉS PRESENCIAL')
    c.drawRightString(W - M, H - bh + 0.50 * inch, 'BUCARAMANGA')
    # etiqueta GRATIS
    y = H - bh - 0.5 * inch
    c.setFillColor(AMARILLO); c.roundRect(M, y - 0.08 * inch, 1.05 * inch, 0.34 * inch, 5, stroke=0, fill=1)
    c.setFont('Rounded', 13); c.setFillColor(TINTA); c.drawString(M + 0.12 * inch, y, 'GRATIS')
    # titular
    y -= 0.5 * inch
    c.setFont('Rounded', 30); c.setFillColor(NARANJA)
    c.drawString(M, y, 'CLASE DE'); y -= 0.42 * inch
    c.drawString(M, y, 'CORTESÍA'); y -= 0.34 * inch
    y = draw_par(c, M, y, 'Ven a vivir una clase real en nuestra sede. Sin costo y sin compromiso.', 'Arial', 11.5, W - 2 * M, 15)
    # mensaje destino
    y -= 0.12 * inch
    c.setFillColor(TINTA); c.roundRect(M, y - 0.72 * inch, W - 2 * M, 0.8 * inch, 8, stroke=0, fill=1)
    draw_par(c, M + 0.15 * inch, y - 0.27 * inch, 'Te entrenamos para llegar a tu destino: la entrevista, el viaje, el negocio, el cargo que pide inglés.', 'Rounded', 12, W - 2 * M - 0.3 * inch, 16, color=AMARILLO)
    y -= 1.0 * inch
    # qué vas a vivir
    c.setFont('Rounded', 12.5); c.setFillColor(NARANJA); c.drawString(M, y, 'En tu clase de cortesía:'); y -= 0.26 * inch
    items = ['Hablas inglés desde el primer minuto, con un profesor que te corrige en vivo.',
             'Conoces cómo entrenamos todos los días y qué destino puedes alcanzar.',
             'Te explicamos la garantía de aprendizaje por escrito: si cumples tu parte y no avanzas en inglés, te devolvemos el 100% del nivel.']
    for it in items:
        c.setFillColor(NARANJA); c.circle(M + 0.07 * inch, y + 0.04 * inch, 0.045 * inch, stroke=0, fill=1)
        y = draw_par(c, M + 0.25 * inch, y, it, 'Arial', 10.5, W - 2 * M - 0.25 * inch, 13.5) - 0.07 * inch
    # bloque QR + CTA
    y -= 0.05 * inch
    qh = 1.5 * inch
    c.setFillColor(BLANCO); c.roundRect(M, y - qh, W - 2 * M, qh, 8, stroke=0, fill=1)
    c.drawImage(qr_image(), M + 0.12 * inch, y - qh + 0.12 * inch, width=qh - 0.24 * inch, height=qh - 0.24 * inch)
    tx = M + qh + 0.05 * inch; tw = W - M - tx - 0.1 * inch
    c.setFont('Rounded', 13); c.setFillColor(TINTA); c.drawString(tx, y - 0.38 * inch, 'Agenda tu clase')
    c.drawString(tx, y - 0.62 * inch, 'por WhatsApp')
    c.setFont('Rounded', 15); c.setFillColor(NARANJA); c.drawString(tx, y - 0.95 * inch, CONFIG['whatsapp_visible'])
    draw_par(c, tx, y - 1.2 * inch, 'Escanea el código o escríbenos. Cupos por horario.', 'Arial', 9, tw, 11)
    y -= qh + 0.2 * inch
    # pie
    c.setFont('ArialB', 9); c.setFillColor(TINTA); c.drawCentredString(W / 2, y, CONFIG['sede']); y -= 0.17 * inch
    c.setFont('Arial', 8.5); c.drawCentredString(W / 2, y, 'Para jóvenes y adultos. Afiliados a Cajasan: condiciones especiales con carné o certificado vigente.')
    # franja amarilla inferior
    c.setFillColor(AMARILLO); c.rect(0, 0, W, 0.22 * inch, stroke=0, fill=1)
    c.restoreState()

# 1) media carta
p1 = os.path.join(OUT, 'VOLANTE_CLASE_CORTESIA.pdf')
c = canvas.Canvas(p1, pagesize=(W, H)); c.setTitle('Clase de cortesía · Heiiu'); volante(c); c.save()
# 2) dos por hoja carta (vertical, lado a lado)
p2 = os.path.join(OUT, 'VOLANTE_CLASE_CORTESIA_2xCARTA.pdf')
c = canvas.Canvas(p2, pagesize=letter); c.setTitle('Clase de cortesía · Heiiu (2 por hoja)')
volante(c, 0, 0.5 * inch); volante(c, W, 0.5 * inch)
c.setDash(4, 3); c.setStrokeColor(colors.grey); c.line(W, 0.2 * inch, W, letter[1] - 0.2 * inch); c.save()
# 3) PNG para WhatsApp
import fitz
d = fitz.open(p1); pix = d[0].get_pixmap(dpi=200); p3 = os.path.join(OUT, 'VOLANTE_CLASE_CORTESIA.png'); pix.save(p3)
for p in (p1, p2, p3): print('OK', p, os.path.getsize(p))
