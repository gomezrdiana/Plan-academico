# -*- coding: utf-8 -*-
"""Hoja de 1 página: escenarios de ingreso con sobrecumplimiento (acelerador) — Ejecutivo(a) Senior de Alianzas.
Reglas = PROPUESTA_EJECUTIVA_ALIANZAS (metas trimestrales, básicos de etapa, acelerador marginal 10/15/20% por trimestre).
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/ESCENARIOS_INGRESO_ALIANZAS.pdf"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

F = 'C:/Windows/Fonts/'
pdfmetrics.registerFont(TTFont('Cal', F + 'calibri.ttf')); pdfmetrics.registerFont(TTFont('CalB', F + 'calibrib.ttf'))
NAR = colors.HexColor('#E54C09'); CREMA = colors.HexColor('#FFF8E7'); CAFE = colors.HexColor('#30271C'); GRIS = colors.HexColor('#6B6B6B'); LINEA = colors.HexColor('#E6DCCB'); AMAR = colors.HexColor('#FBC900')
st = {
 'kicker': ParagraphStyle('k', fontName='CalB', fontSize=10, textColor=GRIS, leading=13),
 'h1': ParagraphStyle('h1', fontName='CalB', fontSize=22, textColor=NAR, leading=26, spaceAfter=4),
 'p': ParagraphStyle('p', fontName='Cal', fontSize=10.5, textColor=CAFE, leading=14, spaceAfter=6),
 'h2': ParagraphStyle('h2', fontName='CalB', fontSize=13, textColor=NAR, leading=16, spaceBefore=8, spaceAfter=4),
 'tc': ParagraphStyle('tc', fontName='Cal', fontSize=9.5, textColor=CAFE, leading=12, alignment=1),
 'tcl': ParagraphStyle('tcl', fontName='CalB', fontSize=9.5, textColor=CAFE, leading=12),
 'th': ParagraphStyle('th', fontName='CalB', fontSize=9.5, textColor=colors.white, leading=12, alignment=1),
 'big': ParagraphStyle('big', fontName='CalB', fontSize=22, textColor=NAR, leading=26, alignment=1),
 'bigl': ParagraphStyle('bigl', fontName='Cal', fontSize=9.5, textColor=GRIS, leading=12, alignment=1),
 'note': ParagraphStyle('n', fontName='Cal', fontSize=8.8, textColor=GRIS, leading=11.3, spaceAfter=3),
}
P = lambda t, s='p': Paragraph(t, st[s])
m = lambda v: f'${v:,.0f}'.replace(',', '.')
mm = lambda v: ('$%.1fM' % (v / 1e6)).replace('.', ',')


def comision(meta, ventas):
    """Acelerador marginal: 10% hasta la meta, 15% del 100% al 130%, 20% sobre el 130%."""
    t1, t2 = meta, 1.3 * meta
    return 0.10 * min(ventas, t1) + 0.15 * max(0, min(ventas, t2) - t1) + 0.20 * max(0, ventas - t2)


ETAPAS = [('Meses 1-3', 30_000_000, 2_000_000), ('Meses 4-6', 48_000_000, 2_000_000), ('Meses 10-12', 78_000_000, 2_550_000), ('Meses 22-24', 108_000_000, 2_850_000)]
NIV = [1.0, 1.3, 1.5]
CUPO = 4_782_800

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\ESCENARIOS_INGRESO_ALIANZAS.pdf'
doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.6 * cm, bottomMargin=1.6 * cm, title='Escenarios de ingreso · Ejecutivo(a) Senior de Alianzas')
W = letter[0] - 4 * cm
E = [P('HEIIU ENGLISH ACADEMY · EJECUTIVO(A) SENIOR DE ALIANZAS EMPRESARIALES', 'kicker'),
     P('Cuando se supera la meta', 'h1'),
     P('La propuesta muestra el ingreso cumpliendo la meta. Esta hoja muestra lo que pasa cuando se supera: la comisión sube al <b>15%</b> sobre lo vendido entre el 100% y el 130% de la meta, y al <b>20%</b> sobre lo que pase del 130%. <b>No hay techo.</b> Está pensada para quien ya llega con relaciones comerciales y resultados comprobados.')]

top = [(mm(ETAPAS[-1][2] + comision(ETAPAS[-1][1], 1.5 * ETAPAS[-1][1])), 'al mes en el año 2 vendiendo el 150% de la meta'),
       (mm(ETAPAS[2][2] + comision(ETAPAS[2][1], 1.3 * ETAPAS[2][1])), 'al mes en el primer año (meses 10-12) con el 130%'),
       ('20%', 'de comisión sobre lo que pase del 130% de la meta')]
cards = Table([[Table([[P(v, 'big')], [P(l, 'bigl')]], colWidths=[5.3 * cm]) for v, l in top]], colWidths=[W / 3] * 3)
cards.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), CREMA), ('INNERGRID', (0, 0), (-1, -1), 6, colors.white), ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
E += [Spacer(1, 4), cards, P('Ingreso mensual por escenario (básico + comisión)', 'h2')]

rows = [[P(c, 'th') for c in ['Etapa', 'Meta mensual', 'Cumpliendo la meta (100%)', 'Superándola al 130%', 'Superándola al 150%']]]
for lab, meta, bas in ETAPAS:
    r = [P(lab, 'tcl'), P(m(meta), 'tc')]
    for k in NIV:
        v = meta * k
        r.append(P('<b>%s</b><br/><font size=8 color="#6B6B6B">ventas %s/mes ≈ %d programas</font>' % (m(bas + comision(meta, v)), mm(v), round(v / CUPO)), 'tc'))
    rows.append(r)
t = Table(rows, colWidths=[2.6 * cm, 2.7 * cm] + [(W - 5.3 * cm) / 3] * 3)
t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, LINEA), ('BACKGROUND', (0, 0), (-1, 0), NAR), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                       ('BACKGROUND', (3, 1), (4, -1), CREMA), ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]))
E.append(t)

E += [P('Y la cartera se suma', 'h2'),
      P('Cada estudiante que llega por una empresa aliada genera el <b>6%</b> de sus pagos durante 12 meses desde la firma de su matrícula, y el 3% del mes 13 al 24. Con 30 estudiantes de las alianzas pagando cuotas de ' + m(450_000) + ', son <b>' + m(810_000) + ' más cada mes</b>, aparte de lo que muestra la tabla.'),
      P('Cómo se lee esta hoja', 'h2'),
      P('• La meta y el acelerador se miden <b>por trimestre</b>; la tabla muestra el promedio mensual. • El acelerador aplica en los trimestres con al menos <b>2 empresas nuevas</b> firmadas con inicial pagada. • La comisión se paga sobre lo <b>recaudado</b>: si la empresa paga a cuotas, se liquida a medida que paga; la tabla supone pagos de contado. • Básico: mínimo vigente + auxilio de transporte en los meses 1-6 (' + m(2_000_000) + ' en 2026); + ' + m(550_000) + ' en los meses 7-12 y + ' + m(850_000) + ' en el año 2, cuando se cumple la meta en 2 de los 3 últimos trimestres. • Programas calculados a tarifa corporativa (' + m(CUPO) + '). • Valores de 2026.', 'note'),
      P('Son escenarios ilustrativos según las reglas de la propuesta, no un ingreso garantizado. Las condiciones definitivas quedan en el contrato laboral y su anexo de compensación y metas.', 'note')]


def pie(c, d):
    c.saveState(); c.setFillColor(NAR); c.rect(0, letter[1] - 0.5 * cm, letter[0], 0.5 * cm, fill=1, stroke=0)
    c.setFillColor(AMAR); c.rect(0, letter[1] - 0.5 * cm, 4 * cm, 0.5 * cm, fill=1, stroke=0)
    c.setFont('Cal', 8.5); c.setFillColor(GRIS)
    c.drawString(2 * cm, 1.0 * cm, 'Heiiu English Academy · Escenarios de ingreso · Ejecutivo(a) Senior de Alianzas Empresariales · confidencial · octubre 2026')
    c.restoreState()


try:
    doc.build(E, onFirstPage=pie, onLaterPages=pie); print('OK', out)
except PermissionError:
    doc.filename = out.replace('.pdf', '_v2.pdf'); doc.build(E, onFirstPage=pie, onLaterPages=pie); print('ABIERTO -> _v2')
