# -*- coding: utf-8 -*-
"""5 guiones de video pre-aprobados para la cerradora high ticket (canal propio, Arranque)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NARANJA = RGBColor(0xE5, 0x4C, 0x09)
GRIS = RGBColor(0x77, 0x77, 0x77)
CREMA = 'FFF8E7'

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.4); s.bottom_margin = Cm(1.2); s.left_margin = Cm(1.9); s.right_margin = Cm(1.9)
doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(10.5)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd'); el.set(qn('w:val'), 'clear'); el.set(qn('w:fill'), color)
    tcPr.append(el)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('5 GUIONES DE VIDEO — CERRADORA HIGH TICKET · ARRANQUE A1+A2'); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = NARANJA
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('PRE-APROBADOS POR GERENCIA · 30-45 segundos cada uno · Tu cara, tu estilo, tus palabras — el contenido de cada bloque se respeta'); r.font.size = Pt(9.5); r.font.color.rgb = GRIS
doc.add_paragraph()

def sec(txt):
    p = doc.add_paragraph(); r = p.add_run(txt); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = NARANJA
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)

def t(txt, bold=False):
    p = doc.add_paragraph(); r = p.add_run(txt); r.font.size = Pt(10.5); r.bold = bold
    p.paragraph_format.space_after = Pt(2)

def guion(txt):
    tab = doc.add_table(rows=1, cols=1); tab.style = 'Table Grid'
    c = tab.rows[0].cells[0]; shd(c, CREMA)
    for k, ln in enumerate(txt.split('\n')):
        p = c.paragraphs[0] if k == 0 else c.add_paragraph()
        r = p.add_run(ln); r.font.size = Pt(10.5)
    esp = doc.add_paragraph(); er = esp.add_run(''); er.font.size = Pt(3)
    esp.paragraph_format.space_after = Pt(0)

sec('GUION 1 — EL DIRECTO (precio y oferta, para pauta fría)')
guion('''GANCHO (3 seg): "En Bucaramanga hay una academia que te FIRMA en el contrato que aprendes inglés — o te devuelve la plata."
DESARROLLO: "Se llama Heiiu. Dos niveles completos de inglés, 200 horas presenciales, libros y certificados incluidos, por dos millones novecientos noventa. Y la garantía va POR ESCRITO — la única de la ciudad."
URGENCIA: "Son 20 cupos de lanzamiento y acaban de abrirse. La cohorte arranca el 5 de octubre."
CTA: "Escríbeme YA al WhatsApp del enlace y te cuento en 5 minutos si es para ti."''')

sec('GUION 2 — EL QUEMADO (para el que ya intentó y fracasó)')
guion('''GANCHO: "¿Cuántas veces has empezado inglés en tu vida? ¿Tres? ¿Cinco?"
DESARROLLO: "Déjame decirte algo que nadie te ha dicho: el problema nunca fuiste tú. Fue el método — años sentado copiando del tablero, con miedo a hablar. En Heiiu es al revés: hablas de pie desde el primer día. Y no te piden fe: te FIRMAN una garantía en el contrato — si cumples y no avanzas, te devuelven la plata."
HONESTIDAD: "No te voy a mentir: es exigente. Se entrena como un deporte. Por eso funciona."
CTA: "20 cupos de lanzamiento, arranca el 5 de octubre. Escríbeme al WhatsApp."''')

sec('GUION 3 — EL EMPRENDEDOR (el destino, no el inglés)')
guion('''GANCHO: "Esto no es un curso de inglés. Escucha bien lo que te entregan al final."
DESARROLLO: "En Heiiu, cuando terminas tus dos primeros niveles, sales con TU página web publicada con dominio propio, tu presentación en inglés, y tu primer mensaje de venta enviado a un cliente real en el exterior. Sales con un negocio montado que habla inglés."
PRUEBA: "Dos millones novecientos noventa los dos niveles completos, con garantía por escrito. Nadie más en la ciudad entrega eso."
CTA: "20 cupos. 5 de octubre. Escríbeme al WhatsApp y te muestro."''')

sec('GUION 4 — EL QUE SE QUIERE IR (Au Pair / trabajar afuera)')
guion('''GANCHO: "¿Te quieres ir a trabajar afuera pero el inglés te tiene frenado?"
DESARROLLO: "El requisito número uno de TODOS los programas — Au Pair, Work and Travel, los que sean — es el inglés conversacional. En Heiiu no solo lo aprendes: terminas con tu video de presentación en inglés, tu aplicación lista, y tu entrevista ENSAYADA y grabada. Llegas al programa con todo hecho."
PRUEBA: "Con garantía de aprendizaje por escrito y operadores verificados."
CTA: "La cohorte arranca el 5 de octubre — 20 cupos. Escríbeme al WhatsApp."''')

sec('GUION 5 — MODO DICIEMBRE (urgencia de fin de año)')
guion('''GANCHO: "Estamos en septiembre. ¿Otra vez vas a llegar a diciembre diciendo \\'el otro año sí aprendo inglés\\'?"
DESARROLLO: "Hagamos cuentas: si arrancas el 5 de octubre, para las fiestas ya llevas dos meses hablando — de pie, en clases presenciales, con tu avance medido desde el día uno. Y con una garantía FIRMADA en tu contrato: si cumples y no avanzas, te devuelven la plata. El riesgo no es tuyo."
URGENCIA: "20 cupos de lanzamiento a dos millones novecientos noventa. Cuando se acaben, el mismo programa vale más de tres millones y medio."
CTA: "Escríbeme YA al WhatsApp. Este año sí — pero empezando HOY."''')

sec('LAS REGLAS DE TODA PIEZA (innegociables — ya vienen cumplidas en estos 5)')
t('· PROHIBIDO decir: gratis, descuento, patrocinio, "fácil", "rápido", "bilingüe en X meses", promesas de empleo o visa.', bold=True)
t('· El contador se dice según la etapa REAL: con 0 vendidos = "acaban de abrirse los 20 cupos" · con ventas = "quedan N". Jamás inventar el número.')
t('· La garantía se cita EXACTA: "si cumples — asistencia, tareas, evaluaciones — y no avanzas, te devuelven el 100% del nivel. Por escrito."')
t('· Toda pieza NUEVA o modificada pasa por gerencia antes de publicarse. Estos 5 ya están aprobados: grábalos y publica.')
t('· Todos los enlaces van a TU WhatsApp con el mensaje prellenado acordado.')

doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Heiiu English Academy · material aprobado por gerencia · Sept 2026'); r.font.size = Pt(9); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\GUIONES_CERRADORA_ARRANQUE.docx'
doc.save(out); print('OK', out)
