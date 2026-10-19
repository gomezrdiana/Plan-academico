# -*- coding: utf-8 -*-
"""Hoja del viernes para el ANALISTA DE INDICADORES (rol): 30 min con el Gerente de Alianzas leyendo el tablero.
5 indicadores por semana contra meta, 3 preguntas, 2 fechas de corte, y el embudo del lunes en 3 líneas.
Salida (git): recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/TABLERO_VIERNES_ALIANZAS.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\TABLERO_VIERNES_ALIANZAS.docx'
d = Document()
for s in d.sections:
    s.top_margin = Cm(1.0); s.bottom_margin = Cm(0.8); s.left_margin = Cm(1.5); s.right_margin = Cm(1.5)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9.5)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAR
def t(txt, size=9.5, color=None, after=2, bold=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def bullets(items, size=9.5):
    for x in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); r = p.add_run(x); r.font.size = Pt(size)
def tabla(hdr, filas, anchos, size=9):
    tb = d.add_table(rows=1, cols=len(hdr)); tb.style = 'Table Grid'
    for i, h in enumerate(hdr):
        c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = BLANCO
    for f in filas:
        row = tb.add_row().cells
        for i, txt in enumerate(f):
            row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
            r = row[i].paragraphs[0].add_run(txt); r.font.size = Pt(size); r.bold = (i == 0)
    for row in tb.rows:
        for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    d.add_paragraph().paragraph_format.space_after = Pt(0)

p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('TABLERO DE LOS VIERNES — ALIANZAS EMPRESARIALES'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(5)
r = p.add_run('Para el analista de indicadores · Viernes 8:45 a. m., 30 minutos, presencial · El Gerente de Alianzas presenta, el analista lee y anota · Gerencia decide'); r.font.size = Pt(8.5); r.font.color.rgb = GRIS

sec('1. Los cinco indicadores (del tablero de alianzas, semana cerrada el jueves)')
tabla(['Indicador', 'Meta semanal', 'Meta mes 1', 'Sem 1\n24/10', 'Sem 2\n31/10', 'Sem 3\n7/11', 'Sem 4\n14/11', 'Sem 5\n21/11', 'Sem 6\n28/11'], [
 ('1. Empresas contactadas con quien decide', '10', '40', '', '', '', '', '', ''),
 ('2. Reuniones con decisor hechas', '3', '12', '', '', '', '', '', ''),
 ('3. Alianzas firmadas / activadas', '', '2 firmas', '', '', '', '', '', ''),
 ('4. Inscritos con inicial pagada y caja ($) por canal', '', '', '', '', '', '', '', ''),
 ('5. Base de la academia: llamados / agendados / asistidos / separados', '', '', '', '', '', '', '', ''),
], [5.4, 1.7, 1.6, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5], size=8.5)
t('Se llena con lo que está registrado en el tablero, no con lo que se cuenta de palabra. Lo que no está en el tablero no existe.', size=8.5, color=GRIS)

sec('2. Las tres preguntas (siempre las mismas, en este orden)')
bullets([
 '"¿Qué número de la semana quedó por debajo de la meta y por qué?" Se anota la razón en una línea; no se discute.',
 '"¿Qué cierra la próxima semana?" Empresas con reunión agendada y fecha, y qué inscripciones están a un paso de pagar.',
 '"¿Qué necesitas de gerencia?" Una cosa, con fecha. Se anota y gerencia responde el lunes.'])

sec('3. Las dos fechas que no se mueven')
tabla(['Corte', 'Fecha', 'Qué tiene que haber', 'Qué pasa si no'], [
 ('Día 30', 'Miércoles 18 de noviembre', 'Al menos una venta firmada con pago inicial recibido, o una alianza activada', 'El cargo no continúa (periodo de prueba)'),
 ('Día 45', 'Jueves 3 de diciembre', '$30.000.000 recibidos en caja (contado e iniciales), por cualquier canal', 'El cargo no continúa (periodo de prueba)'),
], [2.0, 3.6, 6.6, 5.0], size=8.5)
t('El viernes anterior a cada corte (13 de noviembre y 27 de noviembre) el analista escribe en la hoja, con el número del tablero: "va a cumplir / no va a cumplir". Gerencia decide con ese papel delante.', size=9)

sec('4. El lunes: embudo de la semana en tres líneas (lo manda el analista a gerencia)')
bullets([
 'Pauta: gasto de la semana, leads, conversaciones (export de Meta o dato del trafficker).',
 'Citas: agendadas, asistidas, separaciones, matrículas (panel de LaHaus y coordinación).',
 'Alianzas: los cinco indicadores de arriba en una línea.'])
t('Regla: dato que no llegó se escribe "SIN DATO"; nunca se estima.', size=8.5, color=GRIS, after=0)

try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
