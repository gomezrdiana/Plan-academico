# -*- coding: utf-8 -*-
"""Hoja de control de gerencia (1 pagina carta): numeros del dia (reunion 8:30), reporte de las 5 pm
del Gerente de Alianzas y lista de cuentas de la semana. Se imprime una por semana."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'estrategia comercial', 'HOJA_CONTROL_GERENCIA_SEMANAL.pdf')
W, H = letter; M = 1.5 * cm
NARANJA = colors.HexColor('#E54C09'); CREMA = colors.HexColor('#FFF8E7'); TINTA = colors.HexColor('#2A1A12'); GRIS = colors.HexColor('#C9BFB3')

def tabla(c, x, y, cols, widths, rows, rh, header_h=0.75 * cm, fs=7.8):
    """Dibuja tabla con encabezado; rows = lista de textos de la primera columna. Devuelve y final."""
    tw = sum(widths)
    c.setFillColor(CREMA); c.rect(x, y - header_h, tw, header_h, stroke=0, fill=1)
    c.setStrokeColor(NARANJA); c.setLineWidth(0.8); c.line(x, y - header_h, x + tw, y - header_h)
    c.setFillColor(TINTA); c.setFont('Helvetica-Bold', fs)
    cx = x
    for col, w in zip(cols, widths):
        lines = col.split('\n')
        for k, ln in enumerate(lines):
            c.drawCentredString(cx + w / 2, y - 0.28 * cm - k * (fs + 1.5), ln)
        cx += w
    c.setStrokeColor(GRIS); c.setLineWidth(0.4)
    yy = y - header_h
    for r in rows:
        c.setFont('Helvetica', 8.6); c.setFillColor(TINTA)
        c.drawString(x + 0.12 * cm, yy - rh + 0.3 * cm, r)
        yy -= rh
        c.line(x, yy, x + tw, yy)
    cx = x
    for w in widths[:-1]:
        cx += w; c.line(cx, y, cx, yy)
    c.rect(x, yy, tw, y - yy, stroke=1, fill=0)
    return yy

c = canvas.Canvas(OUT, pagesize=letter); c.setTitle('Hoja de control de gerencia · semana')
# titulo
c.setFillColor(NARANJA); c.setFont('Helvetica-Bold', 14); c.drawString(M, H - M - 0.2 * cm, 'HOJA DE CONTROL DE GERENCIA · SEMANA DEL ________ AL ________')
c.setFillColor(TINTA); c.setFont('Helvetica', 8.8)
c.drawString(M, H - M - 0.85 * cm, 'Se llena en la reunión de las 8:30 (10 minutos, la dirige gerencia) con los números del día anterior. Una fila por día. Se guarda; es el registro.')

# Tabla 1: numeros del dia
y = H - M - 1.6 * cm
c.setFont('Helvetica-Bold', 10.5); c.drawString(M, y, '1. Números del día (reunión de las 8:30)'); y -= 0.3 * cm
cols = ['Día', 'Leads\nnuevos', 'Citas\nagendadas', 'Citas\nasistidas', 'Separaciones\npagadas', 'Matrículas\n(inicial)', 'Visitas de\nalianzas', 'Reporte 5 pm\nllegó (sí/no)', 'Nota / incumplimiento']
aw = W - 2 * M
widths = [aw * p for p in (0.085, 0.07, 0.085, 0.085, 0.105, 0.105, 0.085, 0.1, 0.28)]
y = tabla(c, M, y, cols, widths, ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'TOTAL SEMANA'], 0.72 * cm)

# Reporte 5 pm: formato
y -= 0.55 * cm
c.setFont('Helvetica-Bold', 10.5); c.drawString(M, y, '2. Reporte de las 5:00 pm del Gerente de Alianzas (4 líneas por WhatsApp)'); y -= 0.45 * cm
c.setFont('Helvetica', 8.8)
for ln in ['1) Visitas hechas y resultado    2) Citas agendadas    3) Separaciones o pagos recibidos    4) Plan de mañana',
           'Si a las 5:15 no ha llegado, gerencia llama y toma las 4 líneas por teléfono; se anota "no" en la columna de la tabla 1.']:
    c.drawString(M, y, ln); y -= 0.42 * cm

# Tabla 3: cuentas de la semana
y -= 0.3 * cm
c.setFont('Helvetica-Bold', 10.5); c.drawString(M, y, '3. Lista de cuentas de la semana (lunes se arma, jueves se revisa; 30 minutos, no se cancela)'); y -= 0.3 * cm
cols3 = ['#', 'Cuenta', 'Contacto (cargo)', 'Producto', 'Fecha\nvisita', 'Siguiente paso', 'Fecha\ncompromiso', 'Jueves:\navanzó']
widths3 = [aw * p for p in (0.035, 0.235, 0.14, 0.11, 0.08, 0.2, 0.1, 0.1)]
y = tabla(c, M, y, cols3, widths3, [str(i) for i in range(1, 11)], 0.62 * cm)

# Cortes
y -= 0.55 * cm
c.setFont('Helvetica-Bold', 10.5); c.drawString(M, y, '4. Cortes'); y -= 0.45 * cm
c.setFont('Helvetica', 8.8)
for ln in ['18 de noviembre: separaciones de colegios ____ / meta ____    ·    propuestas de salud firmadas ____ / meta ____',
           '30 de noviembre: matrículas ____ / 10    ·    cupos de salud ____ / 12    ·    niños vacacional ____ / 16    ·    separaciones colegios ____ / 10']:
    c.drawString(M, y, ln); y -= 0.45 * cm

c.setFont('Helvetica-Oblique', 7.8); c.setFillColor(colors.HexColor('#6B5B4E'))
c.drawString(M, M - 0.2 * cm, 'Documento interno de gerencia. Las metas del 30 de noviembre son las de la estrategia de noviembre de 2026.')
c.save(); print('OK', OUT, os.path.getsize(OUT))
