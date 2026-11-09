# -*- coding: utf-8 -*-
"""Certificado de la semana del vacacional de ninos (7 a 12). Una hoja carta horizontal por semana (A, B, C, D)
mas una en blanco. Coordinacion imprime la de la semana y escribe a mano el nombre del nino, las frases que
dicta el profesor el viernes y la fecha. Salida: recursos/comercial/productos/VACACIONAL_KIDS/CERTIFICADOS/."""
import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'VACACIONAL_KIDS', 'CERTIFICADOS')
LOGO = os.path.join(ROOT, 'recursos', 'marca heiiu', 'logo_heiiu_transparente.png')
os.makedirs(OUT, exist_ok=True)

pdfmetrics.registerFont(TTFont('Rounded', 'C:/Windows/Fonts/ARLRDBD.TTF'))
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialB', 'C:/Windows/Fonts/arialbd.ttf'))

NARANJA = colors.HexColor('#E54C09'); NARANJA_LOGO = colors.HexColor('#FF4A00'); AMARILLO = colors.HexColor('#FBC900')
CREMA = colors.HexColor('#FFF8E7'); TINTA = colors.HexColor('#2A1A12'); GRIS = colors.HexColor('#9C8E82')

SEMANAS = {
    'A': ('23 al 27 de noviembre de 2026', ['This is me', 'My family at breakfast', 'The lost dog', 'The toy store', "I'm sick!"]),
    'B': ('30 de noviembre al 4 de diciembre de 2026', ['My day', 'At the zoo', 'The airport', 'The birthday party', 'The show']),
    'C': ('7 al 11 de diciembre de 2026', ['My house', "What's the weather like?", 'The big game', "Let's cook!", 'When I grow up']),
    'D': ('14 al 18 de diciembre de 2026', ['How do I get there?', 'A day on the farm', 'How do you feel?', 'At the hotel', 'Talent show']),
    'EN_BLANCO': ('____ al ____ de ______________ de 20____', ['', '', '', '', '']),
}

def certificado(path, fecha, escenas):
    W, H = landscape(letter); M = 1.4 * cm
    c = canvas.Canvas(path, pagesize=(W, H)); c.setTitle('Certificado · Vacaciones en inglés')
    # marco crema y borde naranja
    c.setFillColor(CREMA); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setStrokeColor(NARANJA); c.setLineWidth(3); c.rect(M, M, W - 2 * M, H - 2 * M, stroke=1, fill=0)
    # banda del logo
    bh = 2.6 * cm
    c.setFillColor(NARANJA_LOGO); c.rect(M, H - M - bh, W - 2 * M, bh, stroke=0, fill=1)
    from reportlab.lib.utils import ImageReader
    logo = ImageReader(LOGO); lw0, lh0 = logo.getSize(); lh = bh * 0.62; lw = lw0 * lh / lh0
    c.drawImage(logo, (W - lw) / 2, H - M - bh + (bh - lh) / 2, lw, lh, mask='auto')
    y = H - M - bh - 1.3 * cm
    c.setFillColor(TINTA); c.setFont('Rounded', 30); c.drawCentredString(W / 2, y, 'CERTIFICADO DE VACACIONES EN INGLÉS')
    y -= 0.9 * cm
    c.setFont('Arial', 12); c.setFillColor(GRIS); c.drawCentredString(W / 2, y, 'Semana del ' + fecha + ' · Sede Heiiu, Bucaramanga')
    # nombre
    y -= 1.6 * cm
    c.setFillColor(TINTA); c.setFont('Arial', 13); c.drawCentredString(W / 2, y, 'Este certificado es de')
    y -= 1.5 * cm
    c.setStrokeColor(TINTA); c.setLineWidth(1); c.line(W / 2 - 9 * cm, y, W / 2 + 9 * cm, y)
    y -= 1.1 * cm
    c.setFont('ArialB', 13); c.drawCentredString(W / 2, y, 'que esta semana habló en inglés todas las mañanas y presentó el show del viernes.')
    # dos columnas: escenas y frases
    y -= 1.2 * cm
    colw = (W - 2 * M - 3 * cm) / 2; x1 = M + 1.5 * cm; x2 = x1 + colw + 1.5 * cm; top = y
    c.setFillColor(AMARILLO); c.rect(x1, top - 0.75 * cm, colw, 0.75 * cm, stroke=0, fill=1); c.rect(x2, top - 0.75 * cm, colw, 0.75 * cm, stroke=0, fill=1)
    c.setFillColor(TINTA); c.setFont('Rounded', 13)
    c.drawString(x1 + 0.3 * cm, top - 0.52 * cm, 'Las escenas de la semana'); c.drawString(x2 + 0.3 * cm, top - 0.52 * cm, 'Frases que ya dice solo')
    yy = top - 1.6 * cm
    for i, e in enumerate(escenas):
        c.setFont('Arial', 13); c.drawString(x1 + 0.3 * cm, yy, '%d.  %s' % (i + 1, e))
        if not e:
            c.setLineWidth(0.6); c.line(x1 + 1.2 * cm, yy - 0.1 * cm, x1 + colw - 0.3 * cm, yy - 0.1 * cm)
        yy -= 0.95 * cm
    yy = top - 1.6 * cm
    for i in range(3):
        c.setLineWidth(0.6); c.line(x2 + 0.3 * cm, yy - 0.1 * cm, x2 + colw - 0.3 * cm, yy - 0.1 * cm); yy -= 1.3 * cm
    c.setFont('Arial', 11); c.drawCentredString(x2 + colw / 2, yy - 0.2 * cm, 'Bucaramanga, ____ de ______________ de 20____')
    # firmas
    yf = M + 2.0 * cm
    for xx, rol in [(W * 0.28, 'Profesor'), (W * 0.72, 'Coordinación')]:
        c.setLineWidth(0.8); c.line(xx - 4 * cm, yf, xx + 4 * cm, yf)
        c.setFont('Arial', 10); c.drawCentredString(xx, yf - 0.5 * cm, rol)
    c.setFont('Arial', 8); c.setFillColor(GRIS)
    c.drawCentredString(W / 2, M + 0.5 * cm, 'Heiiu · Global Teacher S.A.S. · Línea 317 717 3641 · Este certificado reconoce la participación en la semana; no certifica un nivel de inglés.')
    c.save()

if __name__ == '__main__':
    for k, (fecha, escenas) in SEMANAS.items():
        p = os.path.join(OUT, 'CERTIFICADO_SEMANA_%s.pdf' % k)
        certificado(p, fecha, escenas); print('OK', p, os.path.getsize(p))
