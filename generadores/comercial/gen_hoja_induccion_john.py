# -*- coding: utf-8 -*-
"""Hoja de gerencia para la inducción de día y medio del Gerente de Alianzas (John): martes 20/10 completo y miércoles 21
en la mañana. Base: kit de arranque (secciones 1-11), anexo de compensación, tablero de alianzas y su lista de prospectos.
Salida (fuera de git): Candidatos/John Hinestroza/HOJA_INDUCCION_JOHN_2026-10-20.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza'
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
def tabla(filas, anchos):
    tb = doc.add_table(rows=1, cols=3); tb.style = 'Table Grid'
    for i, h in enumerate(['Hora', 'Bloque', 'Qué pasa y qué se verifica']):
        c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(8.5); r.font.color.rgb = BLANCO
    for a, b, c3 in filas:
        row = tb.add_row().cells
        for i, txt in enumerate((a, b, c3)):
            row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
            r = row[i].paragraphs[0].add_run(txt); r.font.size = Pt(8.5); r.bold = (i < 2)
    for row in tb.rows:
        for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('INDUCCIÓN DEL GERENTE DE ALIANZAS — DÍA Y MEDIO'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(4)
r = p.add_run('Martes 20 de octubre (8:00 a 5:30) y miércoles 21 (8:45 a 12:00) · Sede · Hoja de gerencia · Él habla más que tú: en cada bloque él explica y tú corriges'); r.font.size = Pt(8.5); r.font.color.rgb = GRIS

sec('Hoy lunes, antes de mañana (checklist)')
bullets([
 'Contrato y anexo del abogado o contador listos para firmar a las 8:00. Si no llegan hoy, se firma el miércoles y se le dice en una línea; la inducción arranca igual.',
 'Exámenes de ingreso hechos hoy con la orden firmada. Coordinación avisada: nómina en cuenta del banco de la academia (abrirla esta semana), documentos a más tardar el miércoles 6 pm, RUT.',
 'Impresos: kit de arranque (secciones 1 a 11; la 12 y la 13 son del reto y no aplican), su anexo, 3 órdenes plan empresa, 3 convenios, 5 cartas de postulación, flyer "Dos caminos", 10 hojas de interesados.',
 'Tablero de alianzas (TABLERO_ALIANZAS.xlsx) compartido en Drive con él y contigo; su lista de prospectos (PROSPECTOS EMPRESAS + 40 EMPLEADOS.xlsx) a la mano para cargarla.',
 'Número de cuenta de Heiiu para pagos, en un papel. Decidido: cuántos contactos de la base de la academia le entregas el miércoles (sugerido: 20, los más recientes sin cita).'])

sec('Martes 20')
tabla([
 ('8:00', '1. Firma y bienvenida', 'Contrato, anexo y cédula. Un solo canal de WhatsApp contigo. Le entregas el kit y el anexo impresos.'),
 ('8:30', '2. La oferta en sus palabras', 'Él te dice: cargo, garantía y sus indicadores (40 / 12 / 2 firmas), comisión sobre recaudo, acelerador, los dos cortes (día 30 una venta o alianza activada; día 45 $30 millones en caja), territorio y regla de atribución. Lo que diga mal se corrige ahí.'),
 ('9:15', '3. Lo que vendemos', 'Él lee El Pacto en voz alta como en una charla. Luego explica las 4 diferencias: garantía con condiciones, mentor y grupo selectivo, Módulo de Graduación, virtudes. Correcciones de vocabulario: nunca fácil, rápido, nativos, descuento, nombres de competidores.'),
 ('10:00', '4. Precios y plata', 'Con la hoja de precios del kit, él te presenta las 4 opciones (plan empresa por tramos desde 3 cupos, beca de alianza contado y cuotas, Arranque máximo 2 pagos, inglés para empresarios). "¿Por qué beca y no descuento?". Todo entra a Heiiu; efectivo a la sede el mismo día; contrato con coordinación; cédula en la sede.'),
 ('10:45', '5. Documentos', 'Orden plan empresa (quién firma, cuándo queda en firme, cambio de persona solo antes del inicio), convenio (12 meses, sin costo, se firma con fecha de charla), carta de postulación (una por colaborador), flyer. Él dice cuál usa en cada caso. Él no firma por Heiiu.'),
 ('11:30', '6. Tablero y su lista', 'Abre el tablero y carga en vivo su lista de prospectos: empresa, sector, decisor con nombre y cargo, celular, estado. Regla: toda empresa registrada antes de la primera reunión; la empresa es de quien la registra primero, 60 días. Meta de la semana: 15 contactadas con decisor.'),
 ('12:30', 'Almuerzo', ''),
 ('2:00', '7. Su mensaje al gerente', 'Lo escribe él para tres empresas de su lista (una clínica, una fundación, una caja). Tú lo lees como gerente con los 6 criterios del kit (no abrir con "academia de inglés" ni con quién paga; un pedido de 15 minutos; sin precios; "sin costo para la empresa"; dos opciones de hora). Se ajusta y se manda en vivo.'),
 ('3:00', '8. Simulaciones', 'Dos reuniones de 10 minutos: tú eres la gerente de una clínica de 80 empleados y luego la directora de una fundación. Él lleva la reunión de 6 pasos con plan empresa primero. Dos correcciones por simulación, no diez. Luego 5 minutos de charla a empleados.'),
 ('4:00', '9. Llamadas reales', 'Diez llamadas a su lista para agendar reuniones de esta semana, contigo al lado. Objetivo del día: 3 reuniones agendadas en el tablero.'),
 ('5:00', '10. Cierre del día', 'Él te presenta el reporte: contactados, reuniones agendadas, qué faltó. Reglas innegociables leídas por él. Mañana 8:45 presencial.'),
], [1.2, 3.4, 13.6])

sec('Miércoles 21')
tabla([
 ('8:45', '1. Primer seguimiento', 'Lo presenta él, 15 minutos: resultados de ayer frente al plan y empresas de hoy. Así va a ser todos los días.'),
 ('9:00', '2. Base de la academia', 'Le entregas los contactos asignados con el guion de cierre en cita y las reglas del agente (precio solo con beca, cita por llamada, sin descuentos). Primeras 5 llamadas contigo al lado; luego solo. Estas ventas cuentan completas para los cortes de la prueba.'),
 ('10:30', '3. Acompañamiento', 'Si ya tiene una reunión agendada, van juntos; si no, llamadas a empresas de su lista hasta tener 2 reuniones más para el jueves y el viernes.'),
 ('12:00', 'A la calle', 'Viernes 24, 8:45, presencial: cierre de la primera semana con el tablero.'),
], [1.2, 3.4, 13.6])

sec('Lo que no se hace')
t('No se le muestra el esquema ni el nombre del otro comercial. No se le dan precios ni condiciones que no estén en el kit y en el anexo. No se alarga la inducción: lo que falte se resuelve en los seguimientos de las 8:45.', size=9)

out = BASE + r'\HOJA_INDUCCION_JOHN_2026-10-20.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
