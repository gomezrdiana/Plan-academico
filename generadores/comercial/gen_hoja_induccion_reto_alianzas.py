# -*- coding: utf-8 -*-
"""Hoja de gerencia para la inducción de 2 horas (miércoles 21/10/2026, 8:00-10:00) del ejecutivo de alianzas que arranca
el reto de 15 días. Por rol, 1 página: checklist previo + 10 bloques con minutos + cierre.
Salida (git): recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/HOJA_INDUCCION_RETO_ALIANZAS.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial'
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(0.8); s.bottom_margin = Cm(0.6); s.left_margin = Cm(1.4); s.right_margin = Cm(1.4)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(9)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NAR
def t(txt, size=9, color=None, after=1, bold=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def bullets(items, size=9):
    for x in items:
        p = doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); r = p.add_run(x); r.font.size = Pt(size)
def caja(txt, size=9):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(txt); r.font.size = Pt(size); r.italic = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('INDUCCIÓN DEL RETO DE 15 DÍAS — 2 HORAS'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(4)
r = p.add_run('Miércoles 21 de octubre de 2026 · 8:00 a 10:00 a. m. · Sede · Hoja de gerencia · Él habla más que tú: en cada bloque él explica y tú corriges'); r.font.size = Pt(8.5); r.font.color.rgb = GRIS

sec('Antes de las 8:00 (checklist)')
bullets([
 'Número de cuenta de Heiiu para pagos, escrito en un papel para él. Confirmado con coordinación quién recibe pagos, expide recibos y firma contratos, y que le pide RUT y documento vigente para la cuenta de cobro del 3/11.',
 'Impresos: el kit (6 págs.), 10 hojas INTERESADOS, el flyer "Dos caminos", 3 copias de la Orden Plan Empresa, 3 del Convenio y 5 de la Carta de postulación.',
 'Llamada a la referencia de su último empleo hecha, o programada para hoy antes de las 8:00. Si no está hecha, él no sale a hablar en nombre de la academia hasta que esté.',
 'El Excel FORMATO_15_EMPRESAS_RETO abierto en el computador de la sede y enviado a su celular.'])

sec('Los 10 bloques')
tb = doc.add_table(rows=1, cols=3); tb.style = 'Table Grid'
for i, h in enumerate(['Hora', 'Bloque', 'Qué pasa y qué se verifica']):
    c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(8.5); r.font.color.rgb = BLANCO
filas = [
 ('8:00', '1. El reto en sus palabras', 'Él te dice la meta, la fecha, qué cuenta como inscrito pagado, qué recibe, y que el 4 de noviembre se habla con el resultado en la mano. Si se equivoca en algo, se corrige ahí. 2 minutos para que te diga qué dudas le dejó la lectura.'),
 ('8:10', '2. Lo que vendemos', 'Él lee El Pacto en voz alta, como lo diría en una charla. Luego explica las 4 diferencias (garantía con condiciones, mentor y grupo selectivo, Módulo de Graduación, virtudes). Tú corriges palabras: nunca fácil, rápido, nativos, descuento.'),
 ('8:25', '3. Precios', 'Con la hoja de precios del kit delante, él te presenta las 4 opciones como si fueras una empleada. Verificas: plan empresa desde 3 cupos y sus tramos; beca de alianza contado y cuotas; Arranque máximo 2 pagos; inglés para empresarios $70.000/h mín. 30 h. Y la respuesta a "¿por qué no descuento?".'),
 ('8:40', '4. La plata y el proceso', 'Le entregas la cuenta. Él repite: todo entra a Heiiu, efectivo a la sede el mismo día, contrato en la sede con coordinación, pagaré solo si hay cuotas, cédula en la sede y no por chat. Qué cuenta y qué no para los 10; los avanzados que le entregue la academia comisionan pero no cuentan.'),
 ('8:50', '5. Los documentos', 'Orden Plan Empresa (quién la firma, cuándo queda en firme, cambio de persona solo antes del inicio), Convenio (12 meses, sin costo, se firma con fecha de charla), Carta de postulación (una por colaborador, sin carta no hay beca), flyer. Él te dice cuál usa en cada caso.'),
 ('9:00', '6. La planilla', 'Abre el Excel y mete ahí, en vivo, las empresas que trae con nombre y cargo del decisor. Regla: toda empresa registrada antes de la primera reunión. Le muestras el reporte diario de 3 líneas y la hoja INTERESADOS. Meta del jueves: 15 empresas.'),
 ('9:15', '7. Su mensaje al gerente', 'Lo escribe él ahí mismo para una de sus empresas. Tú lo lees como gerente con los 6 criterios del kit. Se ajusta y se manda en vivo antes de salir.'),
 ('9:25', '8. Simulación de 5 minutos', 'Tú eres la dueña de una empresa de 60 empleados; él hace la reunión de 10 minutos en 5. Dos correcciones máximo, no diez. Si le sobra tiempo, 3 minutos de charla a empleados.'),
 ('9:35', '9. Reglas innegociables', 'Él lee las 9 reglas del kit. Preguntas. Se cierra con la de menores de 12 y la de que él no firma por Heiiu.'),
 ('9:45', '10. Cierre y rutina', 'Todos los días 8:30, 15 minutos por llamada: rutina, dudas, sugerencias, recomendaciones, indicadores si hay. Cortes: jueves 22 (15 empresas), martes 27 (8 reuniones, 3 charlas), martes 3/11 6:00 p. m. Un solo canal de WhatsApp contigo. A las 10:00, a la calle.'),
]
for a, b, c3 in filas:
    row = tb.add_row().cells
    for i, txt in enumerate((a, b, c3)):
        row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
        r = row[i].paragraphs[0].add_run(txt); r.font.size = Pt(8.5); r.bold = (i < 2)
for row in tb.rows:
    row.cells[0].width = Cm(1.2); row.cells[1].width = Cm(3.6); row.cells[2].width = Cm(13.4)
doc.add_paragraph().paragraph_format.space_after = Pt(0)

sec('Lo que no se hace en la inducción')
t('No se le muestra el esquema ni el nombre de ningún otro ejecutivo. No se le dan precios ni condiciones que no estén en el kit. No se le promete ningún contrato: el 4 de noviembre se habla con el resultado en la mano. No se alarga: a las 10:00 sale, aunque falte algo; lo que falte se resuelve a las 8:30 del jueves.', size=9)
caja('Al terminar, 3 líneas a tu socio: 1) sabe explicar precios y Pacto sin ayuda: sí / no. 2) cuántas empresas con decisor metió en la planilla. 3) su mensaje al gerente: lo mandarías tú: sí / no. El martes o miércoles él le hace las 5 preguntas de números con datos reales.')

out = BASE + r'\HOJA_INDUCCION_RETO_ALIANZAS.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
