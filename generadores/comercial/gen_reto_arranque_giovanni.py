# -*- coding: utf-8 -*-
"""RETO DE ARRANQUE de 15 días para el candidato 3 de alianzas (Giovanni): prueba real pagada por prestación de servicios
antes del contrato laboral. Meta: 10 inscritos pagados o $30M en caja al 3/11/2026, lo que llegue primero; bono $1M si llega. 1 página.
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
    s.top_margin = Cm(0.6); s.bottom_margin = Cm(0.4); s.left_margin = Cm(1.3); s.right_margin = Cm(1.3)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(8)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NAR
def t(txt, size=8, color=None, after=0, bold=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def bullets(items, size=8):
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
r = p.add_run('Heiiu · Miércoles 21 de octubre al martes 3 de noviembre de 2026 · Para: Giovanni García León'); r.font.size = Pt(9.5); r.font.color.rgb = GRIS

caja('Meta: 10 personas inscritas y pagadas, o $30.000.000 en caja de Heiiu, lo que llegue primero, al cierre del martes 3 de noviembre, traídas por ti: empresas, referidos o conocidos, de cualquier programa (completo, parcial, Arranque, plan empresa o inglés para empresarios). Cada persona queda registrada en tu planilla antes de pagar. Inscrito pagado = pagó de contado, o pagó la inicial de su plan de pagos y firmó el contrato con coordinación. Caja = dinero verificado en la cuenta de Heiiu. Lo ideal es de contado.', size=9.5)

sec('0. Lo que vendemos (El Pacto)')
t('No vendemos inglés fácil ni rápido. Vendemos un entrenamiento exigente, con video diario, puntualidad y horas de práctica real, y un destino concreto: el trabajo, el viaje o el estudio que esa persona necesita. El cliente firma sabiendo a qué se compromete. Quien no quiera entrenar así, no es nuestro estudiante, y es mejor que lo sepa en la charla, no en la clase 5.')

sec('1. Qué es')
t('Del miércoles 21 de octubre al martes 3 de noviembre: trabajo real por prestación de servicios, antes de un contrato laboral (9 días hábiles; el 2 de noviembre es festivo). Tú organizas tu agenda; la meta se mide en caja.')

sec('2. Cómo se consigue')
bullets([
 'Empresas de 40 a 150 empleados donde el dueño o el gerente decide en la reunión (compras y multinacionales no firman en dos semanas). Reunión con el decisor y charla de 20 minutos con sus empleados.',
 'Tú abres la puerta, presentas y cierras con la hoja de precios de Heiiu. El pago entra a la cuenta de Heiiu, de contado idealmente; el estudiante firma el contrato con coordinación en la sede, y pagaré solo si va a cuotas.',
 'La oferta es la que entrega Heiiu en la inducción: sin precios, descuentos, horarios ni condiciones distintas.'])

sec('3. Ritmo mínimo')
bullets([
 'Días 1 y 2: 15 empresas contactadas con el decisor (nombre y cargo en la planilla).',
 'Primera semana: 8 reuniones con decisor y 3 charlas autorizadas para la segunda semana.',
 'Segunda semana: charlas, citas e inscripciones. Cierre el martes 3 de noviembre a las 6:00 p. m.'])

sec('4. Seguimiento')
bullets([
 'Todos los días a las 8:30 a. m., 15 minutos con gerencia (lunes en la sede, el resto por llamada): rutina del día, dudas, sugerencias, recomendaciones e indicadores si los hay. Toda empresa se registra en la planilla antes de la primera reunión; planilla al día es condición para liquidar.'])

sec('5. Qué pone Heiiu')
t('Inducción el miércoles 21 de 8:00 a 10:00 a. m. en la sede; propuesta ejecutiva, hoja de precios y mensaje de contacto; planilla; coordinación para contratos y pagos; material de marca. Transporte y celular son tuyos.')

sec('6. Qué recibes')
t('Honorarios de $1.000.000 por el reto, contra cuenta de cobro el 3 de noviembre, más el 10% de lo que haya entrado a caja hasta esa fecha por tus inscritos: honorarios y comisión se pagan pase lo que pase con la meta. Y si llegas a la meta (10 inscritos o $30.000.000 en caja), un bono adicional de $1.000.000 de contado. Si la academia te entrega a alguien ya avanzado para que lo cierres, te pagan comisión, pero no cuenta para los 10. Con los 10 inscritos pagados, así queda:', after=2)
tb = doc.add_table(rows=1, cols=4); tb.style = 'Table Grid'
for i, h in enumerate(['Los 10 inscritos', 'Entra a caja', 'Comisión 10%', 'Total para ti (honorarios + bono + comisión)']):
    c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
for fila in [
 ('10 cupos pagados por la empresa ($4.350.000 c/u)', '$43.500.000', '$4.350.000', '$6.350.000'),
 ('10 cupos del programa completo pagados por los empleados ($4.782.800 c/u)', '$47.828.000', '$4.782.800', '$6.782.800'),
 ('10 Arranques pagados en su totalidad ($2.990.000 c/u)', '$29.900.000', '$2.990.000', '$4.990.000')]:
    row = tb.add_row().cells
    for i, txt in enumerate(fila):
        row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
        r = row[i].paragraphs[0].add_run(txt); r.font.size = Pt(9.5); r.bold = (i == 3)
for row in tb.rows:
    row.cells[0].width = Cm(8.6); row.cells[1].width = Cm(3.0); row.cells[2].width = Cm(2.9); row.cells[3].width = Cm(2.9)
t('Si un inscrito paga inicial y cuotas, al 3 de noviembre se liquida el 10% de la inicial; el 10% de cada cuota se paga cuando entra.', size=9, color=GRIS, after=2)

sec('7. Después del 3 de noviembre')
t('Con el resultado del reto en la mano, el 4 de noviembre nos sentamos a hablar de cómo seguimos. El reto no obliga a ninguna de las dos partes a nada más que lo escrito aquí.')

sec('8. Si aceptas hoy: de aquí al miércoles')
bullets([
 'Martes 20: lista de 15 empresas de 40 a 150 empleados con nombre y cargo del dueño o gerente, en el formato que te enviamos.',
 'Martes 20: mensaje de contacto (escrito por ti con los criterios del kit) a los 15. Meta: 5 reuniones agendadas para esta semana.',
 'Antes del lunes: leer la propuesta y los escenarios que ya tienes. Miércoles 21, 8:00 a. m. en la sede: inducción de 2 horas y a las 10:00 a la calle.'])

sec('9. Reglas')
t('Información de Heiiu (precios, materiales, bases) confidencial y solo para este reto. Empresas y contactos registrados quedan en la base de Heiiu. Comisión solo sobre dinero efectivamente recibido.', size=8)

t('Confirmas respondiendo "acepto" a este mensaje hoy lunes 19 de octubre antes de las 6:00 p. m. Con este reto te llega el kit completo de trabajo; con tu "acepto" te enviamos el formato y los documentos para que arranques hoy mismo con la lista de empresas.', size=10.5, bold=True, after=0)

out = BASE + r'\Giovanni Garcia\RETO_ARRANQUE_15_DIAS_GIOVANNI.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
