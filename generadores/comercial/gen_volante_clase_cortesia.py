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
LOGO = os.path.join(ROOT, 'recursos', 'marca heiiu', 'logo_heiiu_transparente.png')
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

NARANJA = colors.HexColor('#E54C09'); NARANJA_LOGO = colors.Color(255/255, 74/255, 0/255); AMARILLO = colors.HexColor('#FBC900')
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
    c.setFillColor(CREMA); c.rect(0, 0, W, H, stroke=0, fill=1)
    # banda naranja con logo grande
    bh = 1.5 * inch
    c.setFillColor(NARANJA_LOGO); c.rect(0, H - bh, W, bh, stroke=0, fill=1)
    c.drawImage(LOGO, (W - 2.4 * inch) / 2, H - bh + 0.25 * inch, width=2.4 * inch, height=1.0 * inch, preserveAspectRatio=True, mask='auto')
    # GRATIS enorme en amarillo
    y = H - bh - 0.18 * inch
    c.setFillColor(AMARILLO); c.rect(0, y - 1.05 * inch, W, 1.1 * inch, stroke=0, fill=1)
    c.setFont('Rounded', 64); c.setFillColor(TINTA); c.drawCentredString(W / 2, y - 0.8 * inch, 'GRATIS')
    # titular
    y -= 1.65 * inch
    c.setFont('Rounded', 40); c.setFillColor(NARANJA)
    c.drawCentredString(W / 2, y, 'CLASE DE'); y -= 0.55 * inch
    c.drawCentredString(W / 2, y, 'CORTESÍA'); y -= 0.48 * inch
    c.setFont('Rounded', 15); c.setFillColor(TINTA)
    c.drawCentredString(W / 2, y, 'Habla inglés desde el primer día,'); y -= 0.26 * inch
    c.drawCentredString(W / 2, y, 'sin importar tu nivel.'); y -= 0.34 * inch
    # caja oscura: una sola frase
    c.setFillColor(TINTA); c.roundRect(M, y - 0.62 * inch, W - 2 * M, 0.72 * inch, 10, stroke=0, fill=1)
    c.setFont('Rounded', 16); c.setFillColor(AMARILLO)
    c.drawCentredString(W / 2, y - 0.42 * inch, 'Te entrenamos para llegar a tu destino.')
    y -= 0.85 * inch
    # QR grande + número
    qs = 1.75 * inch
    c.setFillColor(BLANCO); c.roundRect(M, y - qs - 0.3 * inch, W - 2 * M, qs + 0.3 * inch, 10, stroke=0, fill=1)
    c.drawImage(qr_image(), M + 0.15 * inch, y - qs - 0.15 * inch, width=qs, height=qs)
    tx = M + qs + 0.3 * inch
    c.setFont('Rounded', 17); c.setFillColor(TINTA)
    c.drawString(tx, y - 0.5 * inch, 'Agenda tu'); c.drawString(tx, y - 0.78 * inch, 'clase por'); c.drawString(tx, y - 1.06 * inch, 'WhatsApp')
    c.setFont('Rounded', 19); c.setFillColor(NARANJA); c.drawString(tx, y - 1.5 * inch, CONFIG['whatsapp_visible'])
    c.setFont('Arial', 9.5); c.setFillColor(TINTA); c.drawString(tx, y - 1.78 * inch, 'Cupos por horario')
    y -= qs + 0.5 * inch
    # pie
    c.setFont('ArialB', 10); c.setFillColor(TINTA); c.drawCentredString(W / 2, y, CONFIG['sede']); y -= 0.18 * inch
    c.setFont('Arial', 9.5); c.drawCentredString(W / 2, y, 'Garantía de aprendizaje por escrito.')
    c.setFillColor(AMARILLO); c.rect(0, 0, W, 0.22 * inch, stroke=0, fill=1)
    c.restoreState()

def volante_v2(c, ox=0, oy=0):
    """Versión 2 (texto propuesto por los críticos): pregunta en inglés como título."""
    c.saveState(); c.translate(ox, oy)
    M = 0.35 * inch
    c.setFillColor(CREMA); c.rect(0, 0, W, H, stroke=0, fill=1)
    bh = 1.5 * inch
    c.setFillColor(NARANJA_LOGO); c.rect(0, H - bh, W, bh, stroke=0, fill=1)
    c.drawImage(LOGO, (W - 2.4 * inch) / 2, H - bh + 0.25 * inch, width=2.4 * inch, height=1.0 * inch, preserveAspectRatio=True, mask='auto')
    # pregunta en inglés, grande
    y = H - bh - 0.75 * inch
    c.setFont('Rounded', 38); c.setFillColor(NARANJA)
    c.drawCentredString(W / 2, y, 'Stuck with'); y -= 0.55 * inch
    c.drawCentredString(W / 2, y, 'your English?'); y -= 0.45 * inch
    # franja amarilla: invitación
    c.setFillColor(AMARILLO); c.rect(0, y - 0.72 * inch, W, 0.92 * inch, stroke=0, fill=1)
    c.setFont('Rounded', 17); c.setFillColor(TINTA)
    c.drawCentredString(W / 2, y - 0.22 * inch, '¡Prepárate para una clase'); c.drawCentredString(W / 2, y - 0.52 * inch, 'de cortesía con nosotros!')
    y -= 1.05 * inch
    # caja oscura: promesa
    c.setFillColor(TINTA); c.roundRect(M, y - 0.85 * inch, W - 2 * M, 0.95 * inch, 10, stroke=0, fill=1)
    c.setFont('Rounded', 16); c.setFillColor(AMARILLO)
    c.drawCentredString(W / 2, y - 0.38 * inch, 'Habla desde el primer encuentro'); c.drawCentredString(W / 2, y - 0.68 * inch, 'y aprende haciendo.')
    y -= 1.1 * inch
    # QR grande + número
    qs = 1.75 * inch
    c.setFillColor(BLANCO); c.roundRect(M, y - qs - 0.3 * inch, W - 2 * M, qs + 0.3 * inch, 10, stroke=0, fill=1)
    c.drawImage(qr_image(), M + 0.15 * inch, y - qs - 0.15 * inch, width=qs, height=qs)
    tx = M + qs + 0.3 * inch
    c.setFont('Rounded', 17); c.setFillColor(TINTA)
    c.drawString(tx, y - 0.5 * inch, 'Agenda tu'); c.drawString(tx, y - 0.78 * inch, 'clase por'); c.drawString(tx, y - 1.06 * inch, 'WhatsApp')
    c.setFont('Rounded', 19); c.setFillColor(NARANJA); c.drawString(tx, y - 1.5 * inch, CONFIG['whatsapp_visible'])
    c.setFont('Arial', 9.5); c.setFillColor(TINTA); c.drawString(tx, y - 1.78 * inch, 'Cupos por horario')
    y -= qs + 0.5 * inch
    c.setFont('ArialB', 10); c.setFillColor(TINTA); c.drawCentredString(W / 2, y, CONFIG['sede']); y -= 0.18 * inch
    c.setFont('Arial', 9.5); c.drawCentredString(W / 2, y, 'Garantía de aprendizaje por escrito.')
    c.setFillColor(AMARILLO); c.rect(0, 0, W, 0.22 * inch, stroke=0, fill=1)
    c.restoreState()

def salidas(fn, sufijo):
    p1 = os.path.join(OUT, 'VOLANTE_CLASE_CORTESIA%s.pdf' % sufijo)
    c = canvas.Canvas(p1, pagesize=(W, H)); c.setTitle('Clase de cortesía · Heiiu'); fn(c); c.save()
    p2 = os.path.join(OUT, 'VOLANTE_CLASE_CORTESIA%s_2xCARTA.pdf' % sufijo)
    c = canvas.Canvas(p2, pagesize=letter); c.setTitle('Clase de cortesía · Heiiu (2 por hoja)')
    fn(c, 0, 0.5 * inch); fn(c, W, 0.5 * inch)
    c.setDash(4, 3); c.setStrokeColor(colors.grey); c.line(W, 0.2 * inch, W, letter[1] - 0.2 * inch); c.save()
    import fitz
    d = fitz.open(p1); pix = d[0].get_pixmap(dpi=200); p3 = os.path.join(OUT, 'VOLANTE_CLASE_CORTESIA%s.png' % sufijo); pix.save(p3)
    for p in (p1, p2, p3): print('OK', p, os.path.getsize(p))

salidas(volante, '')
salidas(volante_v2, '_V2')
