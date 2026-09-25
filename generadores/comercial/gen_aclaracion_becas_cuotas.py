# -*- coding: utf-8 -*-
"""Una hoja: aclaracion a la seccion 3 del Kit de Venta (becas, cuotas y modalidades). Se envia aparte, sin reenviar el kit."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NARANJA = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0); s.left_margin = Cm(1.6); s.right_margin = Cm(1.6)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)

def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NARANJA

def t(txt, bold=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(txt); r.font.size = Pt(10); r.bold = bold

def tabla(filas, anchos):
    tb = doc.add_table(rows=len(filas), cols=len(filas[0])); tb.style = 'Table Grid'
    for i, fila in enumerate(filas):
        for j, v in enumerate(fila):
            c = tb.cell(i, j); c.width = Cm(anchos[j]); c.paragraphs[0].paragraph_format.space_after = Pt(0)
            r = c.paragraphs[0].add_run(v); r.font.size = Pt(9.5)
            if i == 0: r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); shd(c, 'E54C09')
            elif j == 0: r.bold = True; shd(c, 'FFF8E7')

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('ACLARACIÓN AL KIT DE VENTA — BECAS, CUOTAS Y MODALIDADES'); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = NARANJA
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Complemento a la sección 3 del Kit · Una página · Septiembre 2026'); r.font.size = Pt(9); r.font.color.rgb = GRIS

t('La sección 3 del Kit mezcla tres cosas que en realidad son independientes. Separadas quedan así:')

sec('1. LA BECA DEPENDE DE QUIÉN ES Y QUÉ COMPRA — LA MODALIDAD NO CAMBIA LA BECA')
t('· QUIÉN es define la columna: Transformación (estrato 1-2 con soporte, O afiliado a Cajasan con carné o certificado vigente, sin importar estrato), General (todos los demás), Ejecutivo (paga su empresa).')
t('· QUÉ compra y CÓMO paga define la fila: paquete completo, A2 a B2, B1 a B2 o solo B2 — y si es contado o cuotas.')
t('· Ejemplo: estrato 3 que compra el programa completo a cuotas → General, fila completo, cuotas → 25,6% sobre $8.696.000 = $6.469.824.')
t('Intensivo o súper intensivo, la beca es la misma. Se busca la celda en la tabla en pesos y se dice el número. No se calcula.', bold=True)

sec('2. LA MODALIDAD SOLO CAMBIA UNA COSA: EL MÁXIMO DE CUOTAS')
t('Regla: el estudiante termina de pagar antes de terminar el programa. Por eso el súper intensivo, que dura la mitad, admite la mitad de cuotas.')
tabla([
    ['Paquete', 'Intensivo (10 h/semana)', 'Súper intensivo (20 h/semana)'],
    ['Completo A1 a B2', '~14 meses → máximo 11 cuotas', '~7 meses → máximo 5 cuotas'],
    ['A2 a B2', '~12 meses → máximo 11', '~6 meses → máximo 5'],
    ['B1 a B2', '~9 meses → máximo 8', '~4 meses → máximo 3'],
    ['Solo B2', '~5 meses → máximo 4', 'prácticamente de contado'],
    ['ARRANQUE (sin beca)', '~5 meses → máximo 4', '~2,5 meses → máximo 2'],
], [5.0, 6.0, 6.0])
t('Menos cuotas que el máximo SIEMPRE se puede, y el cliente paga menos interés. Más cuotas que el máximo, nunca.', bold=True)
t('· Las tablas en pesos del Kit van SIN interés: son el precio base. El interés del 1,9% mensual sobre saldo solo existe con crédito directo de Heiiu, y ya está sumado en la tabla de "cuota tipo" (inicial 20% + máximo de cuotas).')
t('· Si el cliente pide otra inicial u otro número de cuotas (por ejemplo 9 en vez de 11), el número sale del MOTOR_CUOTAS_FONDO_2026.xlsx, nunca de memoria. Ejemplo General completo: 11 cuotas de $525.855 · 9 cuotas de $631.100 · 6 cuotas de $920.909, siempre con inicial de $1.293.965.')
t('· Cesantías, crédito de un tercero o tarjeta = CONTADO para nosotros: beca de contado y sin interés nuestro. Por tarjeta no se cobra ningún recargo.')
t('· Al cliente se le da el plan completo: inicial + número de cuotas + valor de cada cuota. Nunca solo la cuota.')

sec('3. EL SABATINO ES OTRO PRODUCTO')
t('Solo se vende por nivel suelto (A1 $1.596.000 · A2 $1.915.000 · B1 $2.842.000 · B2 $2.343.000), SIN beca del Fondo. El precio depende de la forma de pago: contado 20% menos · cuotas 10% menos más interés · afiliado Cajasan 30% menos. Se dice "precio de contado", nunca "descuento".')

sec('EL CAMINO EN LA LLAMADA — 3 PASOS')
t('1. ¿Es sabatino o nivel suelto? → precio del nivel, sin Fondo. Fin.', bold=True)
t('2. Si es paquete: ¿quién es? → columna. ¿Qué paquete y contado o cuotas? → fila. Esa celda es su beca.', bold=True)
t('3. Si paga a cuotas: ¿intensivo o súper intensivo? → máximo de cuotas. La cuota exacta la da el motor.', bold=True)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(6)
r = p.add_run('Esta hoja complementa el Kit de Venta; si algo aquí y el Kit no coinciden, manda esta hoja.'); r.font.size = Pt(8.5); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\ACLARACION_BECAS_CUOTAS.docx'
doc.save(out); print('OK', out)
