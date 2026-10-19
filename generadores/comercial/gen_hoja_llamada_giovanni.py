# -*- coding: utf-8 -*-
"""Hoja de la llamada de 15 minutos con el candidato 3 de alianzas (Giovanni): al grano, reto de 15 días.
Salida (fuera de git): Candidatos/Giovanni Garcia/HOJA_LLAMADA_GIOVANNI.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\Giovanni Garcia'
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(0.9); s.bottom_margin = Cm(0.7); s.left_margin = Cm(1.5); s.right_margin = Cm(1.5)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(9.5)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def t(txt, size=9.5, color=None, after=2, bold=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def caja(txt, size=9.5):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(txt); r.font.size = Pt(size); r.italic = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
def anota(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2); p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run('Anota: '); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = GRIS
    r = p.add_run(txt); r.font.size = Pt(9); r.font.color.rgb = GRIS
def bullets(items, size=9.5):
    for x in items:
        p = doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); r = p.add_run(x); r.font.size = Pt(size)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('GIOVANNI — LLAMADA DE 15 MINUTOS: EL RETO'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Uso interno de gerencia · Antes de llamar: sus respuestas a las 5 preguntas, con números. Sin números, no hay llamada.'); r.font.size = Pt(9); r.font.color.rgb = GRIS
anota('Sus 5 respuestas, una línea cada una: 1) ventas 12 meses y clientes ______  2) ticket y contactos por cierre ______  3) reuniones con dueños al mes ______  4) por qué salió de TNK y qué ha hecho ______  5) expectativa mes 1 / mes 6 ______')

t('1. Abres tú, 1 minuto:', bold=True, after=1)
caja('"Giovanni, te voy a ir al grano. La academia necesita vender ya, y yo no tengo tiempo para un proceso de selección de tres semanas. La única forma de saber si esto funciona es trabajando. Te propongo un reto de 15 días. Te lo cuento completo y me dices si lo tomas."')
t('2. Su experiencia, 4 minutos, una sola pregunta:', bold=True, after=1)
caja('"Antes, cuéntame TNK en cuatro minutos: cómo abrías un cliente nuevo, quién decidía la compra, cuánto tardabas de la primera visita a la primera orden, y por qué saliste en septiembre."')
anota('abría: ______________  decidía: ______________  ciclo: ______ semanas  salida: ______________.   Si dice "mucho" o "casi siempre", pides el número. Puente: "Aquí vendes lo mismo que allá, la decisión de un dueño, pero sin marca detrás y sin producto físico: lo que vendes es un resultado con garantía por escrito. Por eso el reto se mide en caja y no en visitas."')
t('3. El Pacto, 1 minuto:', bold=True, after=1)
caja('"No vendemos inglés fácil ni rápido. Vendemos un entrenamiento exigente, con video diario y trabajo fuera de clase, y un destino: el trabajo, el viaje o el estudio que esa persona necesita. El cliente firma sabiendo a qué se compromete. Eso es lo que vas a decir en las empresas."')
t('4. El reto, de corrido, 3 minutos:', bold=True, after=1)
bullets([
 'Miércoles 21 de octubre a martes 3 de noviembre, por prestación de servicios. Nueve días hábiles, el 2 es festivo.',
 'Meta: 10 inscritos pagados o $30 millones en caja, lo que llegue primero. Traídos por él: empresas, referidos o conocidos, de cualquier programa. Registrados en su planilla antes de pagar.',
 'Empresas de dueño, 40 a 150 empleados: talleres, almacenes, distribuidoras, industria. Él abre, presenta y cierra; el pago entra a Heiiu y coordinación firma el contrato.',
 'Un millón de honorarios más el 10% de la caja, pase lo que pase con la meta; bono de un millón si llega. 15 minutos con gerencia todos los días a las 8:30.',
 'El 4 de noviembre, con el resultado en la mano, hablamos de cómo seguimos. El reto no obliga a nada más.'])
t('5. La plata, una frase:', bold=True, after=1)
caja('"Si logras la meta te vas con entre 5 y 7 millones por 15 días: un millón de honorarios, un millón de bono y el 10% de caja."')
t('6. Las dos preguntas que decides con él:', bold=True, after=1)
caja('"¿Estás libre de tiempo completo desde el miércoles, o tienes algo en curso?"   Se acepta "libre". No se acepta "manejo las dos cosas".')
caja('"¿Con qué cinco empresas arrancas el martes? Nombre del dueño o gerente. Pueden ser tus clientes de TNK o de distribución, lo que tenga 40 empleados o más."')
anota('1 __________ 2 __________ 3 __________ 4 __________ 5 __________.   Sin cinco con persona puede aceptar igual, pero ya sabes qué esperar el miércoles.')
t('7. Cierre, 1 minuto:', bold=True, after=1)
caja('"¿Lo tomas? Te mando el reto y el kit por escrito al colgar; me respondes acepto hoy, y con eso te llega el formato y los documentos. El martes armas tu lista y mandas tus mensajes; miércoles 8:00 en la sede, dos horas y a la calle."')
t('Si pide más fijo: "El fijo se habla el 4 de noviembre con el resultado." Si pide una semana de inducción: "Son dos horas y yo contigo todos los días a las 8:30." Si pregunta si hay más gente: "Hay otro comercial en otro sector. Tu lista es tuya." No se dice "estás contratado". No se menciona a nadie más. Las referencias de su hoja de vida (supervisor en TNK y ejecutivo regional) se llaman el martes, antes de la inducción.', size=9, color=GRIS, after=0)

out = BASE + r'\HOJA_LLAMADA_GIOVANNI.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
