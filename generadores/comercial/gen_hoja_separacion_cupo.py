# -*- coding: utf-8 -*-
"""Hoja de separación de cupo: dos copias en una hoja carta (copia cliente / copia Heiiu), con línea de corte."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'NICHO_COLEGIOS', 'HOJA_SEPARACION_CUPO.pdf')
LOGO = os.path.join(ROOT, 'recursos', 'marca heiiu', 'logo_heiiu_sobre_naranja.png')
W, H = letter
M = 0.55 * inch

def linea(c, x, y, etiqueta, ancho):
    c.setFont('Helvetica', 9.5); c.drawString(x, y, etiqueta)
    tw = c.stringWidth(etiqueta, 'Helvetica', 9.5)
    c.setLineWidth(0.6); c.line(x + tw + 4, y - 2, x + ancho, y - 2)

def copia(c, top, titulo):
    x0, x1 = M, W - M
    c.drawImage(LOGO, x0, top - 0.55 * inch, width=0.9 * inch, height=0.5 * inch, preserveAspectRatio=True, mask='auto')
    c.setFont('Helvetica-Bold', 14); c.drawString(x0 + 1.05 * inch, top - 0.3 * inch, 'SEPARACIÓN DE CUPO')
    c.setFont('Helvetica-Bold', 9); c.setFillColor(colors.HexColor('#E54C09'))
    c.drawRightString(x1, top - 0.3 * inch, titulo); c.setFillColor(colors.black)
    y = top - 0.85 * inch; paso = 0.3 * inch; ancho = x1 - x0
    linea(c, x0, y, 'Estudiante:', ancho * 0.62); linea(c, x0 + ancho * 0.65, y, 'Grado:', ancho * 0.16); linea(c, x0 + ancho * 0.84, y, 'Edad:', ancho * 0.16); y -= paso
    linea(c, x0, y, 'Acudiente:', ancho * 0.62); linea(c, x0 + ancho * 0.65, y, 'Cédula:', ancho * 0.35); y -= paso
    linea(c, x0, y, 'Celular:', ancho * 0.40); linea(c, x0 + ancho * 0.43, y, 'Correo:', ancho * 0.57); y -= paso
    c.setFont('Helvetica', 9.5)
    c.drawString(x0, y, 'Programa:  Completo A1 → B2 (   )    Otro: ____________________        Jornada:  Mañana (   )    Noche (   )'); y -= paso
    linea(c, x0, y, 'Valor de la separación (mínimo $150.000):  $', ancho * 0.62); y -= paso * 1.15
    c.setFont('Helvetica', 8.6)
    texto = ('Se abona a la inicial y congela la beca del Fondo que se asigne en la cita, hasta el inicio del grupo. '
             'NO ES REEMBOLSABLE. Incluye el taller de bienvenida de 2 horas el martes 1 de diciembre (solo para quienes separan en esta visita). '
             'La cita con la familia se concreta a más tardar el miércoles 4 de noviembre.')
    t = c.beginText(x0, y); t.setFont('Helvetica', 8.6); t.setLeading(11)
    palabras = texto.split(); lin = ''
    for p in palabras:
        if c.stringWidth(lin + ' ' + p, 'Helvetica', 8.6) > ancho:
            t.textLine(lin); lin = p
        else:
            lin = (lin + ' ' + p).strip()
    t.textLine(lin); c.drawText(t)
    y -= 0.55 * inch
    linea(c, x0, y, 'Pago con el QR de pagos de Heiiu · Referencia:', ancho * 0.66); linea(c, x0 + ancho * 0.69, y, 'Fecha:', ancho * 0.31)
    # firmas con espacio amplio
    y -= 0.85 * inch
    c.setLineWidth(0.8)
    c.line(x0, y, x0 + ancho * 0.45, y); c.line(x0 + ancho * 0.55, y, x1, y)
    c.setFont('Helvetica', 9)
    c.drawString(x0, y - 12, 'Firma del acudiente'); c.drawString(x0 + ancho * 0.55, y - 12, 'Recibe (Heiiu)')
    c.drawString(x0, y - 24, 'C.C.'); c.drawString(x0 + ancho * 0.55, y - 24, 'Nombre')

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle('Separación de cupo · Heiiu')
copia(c, H - M, 'COPIA PARA LA FAMILIA')
c.setDash(4, 3); c.setLineWidth(0.5); c.line(M * 0.5, H / 2, W - M * 0.5, H / 2); c.setDash()
c.setFont('Helvetica', 7); c.drawCentredString(W / 2, H / 2 + 3, '✂  cortar aquí')
copia(c, H / 2 - M * 0.6, 'COPIA PARA HEIIU')
c.save()
print('OK', OUT, os.path.getsize(OUT))
