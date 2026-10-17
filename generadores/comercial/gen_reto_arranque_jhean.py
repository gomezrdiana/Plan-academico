# -*- coding: utf-8 -*-
"""RETO DE ARRANQUE de 15 días para el candidato 2 de alianzas (Jhean): prueba real pagada por prestación de servicios
antes del contrato laboral. Meta única: 10 inscritos con inicial pagada vía empresas al 3/11/2026. 1 página.
Se envía por escrito después de la reunión (ver gen_hoja_reunion_jhean.py, bloque 4).
Salida (fuera de git): Candidatos/RETO_ARRANQUE_15_DIAS_JHEAN.docx (+ PDF vía Word COM)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos'
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(0.9); s.bottom_margin = Cm(0.7); s.left_margin = Cm(1.6); s.right_margin = Cm(1.6)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(9.5)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NAR
def t(txt, size=9.5, color=None, after=2, bold=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def bullets(items, size=9.5):
    for x in items:
        p = doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); r = p.add_run(x); r.font.size = Pt(size)
def caja(txt, size=10.5):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(txt); r.font.size = Pt(size); r.bold = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('RETO DE ARRANQUE — ALIANZAS EMPRESARIALES'); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Heiiu · Lunes 20 de octubre al martes 3 de noviembre de 2026 · Para: Jhean Cárdenas'); r.font.size = Pt(9.5); r.font.color.rgb = GRIS

caja('Meta única: 10 personas inscritas con inicial pagada en caja de Heiiu al cierre del martes 3 de noviembre, llegadas a través de empresas. Al menos 5 de una misma empresa. Cuenta solo lo que esté pagado a esa fecha.')

sec('1. Qué es')
t('Quince días de trabajo real por prestación de servicios, antes de un contrato laboral. Diez días hábiles (el 2 de noviembre es festivo). Tú organizas tu agenda; la meta es una sola y se mide en caja.')

sec('2. Cómo se consigue')
bullets([
 'Empresas de 40 a 150 empleados donde el dueño o el gerente decide en la reunión. Nada de áreas de compras ni multinacionales: no firman en dos semanas.',
 'Reunión con el decisor y autorización de una charla de 20 minutos con sus empleados, en la empresa.',
 'En cada charla va una asesora de Heiiu: ella toma los interesados, agenda y cierra. Tú abres la puerta y presentas; la inscripción la hace Heiiu.',
 'La oferta para los empleados es la que entrega Heiiu en la inducción. No se prometen precios, descuentos, horarios ni condiciones distintas.'])

sec('3. Ritmo mínimo')
bullets([
 'Días 1 y 2: 15 empresas contactadas con el decisor (nombre y cargo en la planilla).',
 'Primera semana: 8 reuniones con decisor y 3 charlas autorizadas para la segunda semana.',
 'Segunda semana: charlas, citas e inscripciones. Cierre el martes 3 de noviembre a las 6:00 p. m.'])

sec('4. Seguimiento')
bullets([
 'Todos los días a las 8:00 a. m., 15 minutos con gerencia (lunes en la sede, los demás días por llamada): qué hiciste ayer frente al plan y qué empresas tienes hoy.',
 'Toda empresa se registra en la planilla de Heiiu antes de la primera reunión. La planilla al día es condición para liquidar.'])

sec('5. Qué pone Heiiu')
t('Inducción el lunes 20 de 8:00 a 10:00 a. m. en la sede; propuesta ejecutiva y oferta a empleados; planilla; una asesora para cada charla y cada cierre; material de marca. Transporte y celular son tuyos.')

sec('6. Qué recibes')
t('Honorarios de $1.000.000 por el reto, contra cuenta de cobro el 3 de noviembre, más el 10% de lo que haya entrado a caja hasta esa fecha por los inscritos de tus empresas. Con los 10 inscritos pagados, así queda:', after=2)
tb = doc.add_table(rows=1, cols=4); tb.style = 'Table Grid'
for i, h in enumerate(['Los 10 inscritos', 'Entra a caja', 'Comisión 10%', 'Total para ti']):
    c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
for fila in [
 ('10 cupos pagados por la empresa ($4.350.000 c/u)', '$43.500.000', '$4.350.000', '$5.350.000'),
 ('10 cupos del programa completo pagados por los empleados ($4.782.800 c/u)', '$47.828.000', '$4.782.800', '$5.782.800'),
 ('10 Arranques pagados en su totalidad ($2.990.000 c/u)', '$29.900.000', '$2.990.000', '$3.990.000')]:
    row = tb.add_row().cells
    for i, txt in enumerate(fila):
        row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
        r = row[i].paragraphs[0].add_run(txt); r.font.size = Pt(9.5); r.bold = (i == 3)
for row in tb.rows:
    row.cells[0].width = Cm(8.6); row.cells[1].width = Cm(3.0); row.cells[2].width = Cm(2.9); row.cells[3].width = Cm(2.9)
t('Si un inscrito paga inicial y cuotas, al 3 de noviembre se liquida el 10% de la inicial; el 10% de cada cuota se paga cuando entra.', size=9, color=GRIS, after=2)

sec('7. El 4 de noviembre')
bullets([
 '10 inscritos o más: contrato laboral (básico $2.000.000 más prestaciones, ingreso mínimo de $3.500.000 los meses 1 a 3 por indicadores, comisión del 10% sobre caja, acelerador sobre meta), con el mínimo del mes 1 garantizado.',
 '5 a 9 inscritos: contrato laboral con el mismo esquema, sin la garantía del mes 1.',
 'Menos de 5: el reto termina; se pagan los honorarios y la comisión de lo que haya entrado.'])

sec('8. Reglas')
t('La información de Heiiu (precios, materiales, bases de datos) es confidencial y se usa solo para este reto. Las empresas y contactos registrados quedan en la base de Heiiu. El nombre de Heiiu se usa únicamente para lo acordado aquí. La comisión se paga solo sobre dinero efectivamente recibido.', size=9.5)

t('Confirmas respondiendo "acepto" a este mensaje antes del domingo 19 de octubre a las 6:00 p. m. Nos vemos el lunes a las 8:00 a. m. en la sede.', size=10.5, bold=True, after=0)

out = BASE + r'\RETO_ARRANQUE_15_DIAS_JHEAN.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
