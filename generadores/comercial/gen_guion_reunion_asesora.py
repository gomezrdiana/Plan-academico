# -*- coding: utf-8 -*-
"""Guion de la reunion (videollamada) gerencia-asesora comercial · 15-sep-2026.
Documento interno de gerencia — no se comparte."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NARANJA = RGBColor(0xE5, 0x4C, 0x09)
GRIS = RGBColor(0x77, 0x77, 0x77)
CREMA = 'FFF8E7'
NARANJA_HEX = 'E54C09'

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(10)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd'); el.set(qn('w:val'), 'clear'); el.set(qn('w:fill'), color)
    tcPr.append(el)

def sec(txt):
    p = doc.add_paragraph(); r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NARANJA
    p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(2)

def t(txt, bold=False):
    p = doc.add_paragraph(); r = p.add_run(txt); r.font.size = Pt(10); r.bold = bold
    p.paragraph_format.space_after = Pt(2)

def frase(txt):
    tab = doc.add_table(rows=1, cols=1); tab.style = 'Table Grid'
    c = tab.rows[0].cells[0]; shd(c, CREMA)
    p = c.paragraphs[0]; r = p.add_run(txt); r.italic = True; r.font.size = Pt(10)
    esp = doc.add_paragraph(); er = esp.add_run(''); er.font.size = Pt(2)
    esp.paragraph_format.space_after = Pt(0)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('GUION DE REUNIÓN — GERENCIA · ASESORA COMERCIAL'); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = NARANJA
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Videollamada · 15 de septiembre de 2026 · USO INTERNO DE GERENCIA — no se comparte · Duración objetivo: 15-20 min'); r.font.size = Pt(8.5); r.font.color.rgb = GRIS

sec('ANTES DE LA LLAMADA (checklist)')
t('□ Nombres y teléfonos de las 2 citas del bot de hoy (Dani y Yenmi) — pedidos al operador del bot.')
t('□ Rescate ya enviado a las 2 plantadas desde la línea de la academia (reagendar en 24h).')
t('□ Andrea Flórez (contado, octubre) y Yareinis (test hecho, A2) asignadas para cierre HOY a primera hora.')
t('□ PDFs a la mano para enviar en la llamada: contrato de prestación comercial + anexo económico asesora + acuerdo de actividad.')
t('□ Su archivo abierto (el que envió ayer): hoja Registro, hoja Informe Diario del 12, hoja Seguimientos.')

sec('OBJETIVO DE LA REUNIÓN (uno solo)')
t('Que salga de la llamada UNA de dos: (a) firmada y ejecutando el sprint esta semana, o (b) fuera hoy, en paz, pagando lo causado. NO es una reunión para desahogo ni para renegociar el rol.', bold=True)

sec('SECUENCIA — 6 PASOS EN ESTE ORDEN')
t('1. ABRIR CON SU PLANILLA, no con reclamos: "Compárteme pantalla con tu planilla de hoy." Lo que haya ahí es la conversación.')
t('2. RECONOCER LO JUSTO (30 segundos, le quita el escudo): hay gestión real del 7 al 12 — 15 contactos, 4 interesados. Y lo de las citas que no bajaron al calendario fue falla del sistema y ella avisó: "bien por avisar, ya se está corrigiendo".')
t('3. LOS HECHOS (sin adjetivos, todos salen de SU archivo):')
t('     · Hoy lunes, día 1 del sprint: cero filas. Ni un contacto nuevo.')
t('     · Su propio seguimiento de las 9:15 AM (Daniela) — agendado por ella misma — sin ejecutar.')
t('     · El informe enviado ayer es el del viernes 12, presentado como si fuera del día. Con 4 interesados en la mesa, cero cierres.')
t('4. EL RECLAMO DE FONDO (la frase completa, sin suavizar):')
frase('"Te contratamos por lo que nos dijiste que sabías hacer: generar tus propios leads. En dos semanas tu gestión ha sido solo los leads que el bot te entrega — ese trabajo no me lo tienes que hacer tú, y no me da para pagarlo. El sprint que te envié ES el trabajo por el que se te contrató: prospección tuya, 40 contactos, reporte diario en formato — no video, formato. Hoy firmamos el contrato y los entregables, y el viernes revisamos tus números. Si ese trabajo no es el que quieres hacer, me lo dices hoy y quedamos en paz."')
t('5. EL AJUSTE OPERATIVO: los leads y citas del bot pasan a cierre directo con la casa desde hoy. Su frente: prospección (6 canales del sprint). El auxilio del período se paga contra cumplimiento del acuerdo de entregables.')
t('6. EL PAPEL Y LA FECHA: "Te envío ahora contrato + anexo económico + acuerdo de entregables. Se firman HOY. Viernes 19, 10:30 AM, revisión con la planilla — ahí se decide continuidad con números, no con opiniones." Si dice "lo pienso", esa ES su respuesta: se agradece y se termina hoy.')

doc.add_paragraph()
sec('SI SE DEFIENDE — LAS 3 RESPUESTAS PREPARADAS')
t('DEFENSA 1: "No sabía el producto, me lo cambiaste el sábado." → CONCEDER EL PASADO Y QUEDARSE CON LA SEMANA:', bold=True)
frase('"Tienes razón: el producto final quedó listo el sábado. Por eso NO te estoy midiendo las dos semanas pasadas — te estoy midiendo ESTA semana, que arranca contigo teniendo todo: kit, precios, mensajes redactados, planilla. Hoy fue el día 1… y fue cero."')
t('DEFENSA 2: "No podía hacer más sin la información." → LA ACTIVIDAD NO DEPENDÍA DEL PRODUCTO:', bold=True)
frase('"Prospectar no necesita lista de precios: contactar, agendar y llenar la planilla se hace con \'te cuento todo en la asesoría\'. Lo único que dependía del producto era el cierre — y no llegaste a ningún cierre. Lo que falta no es información: es actividad."')
t('DEFENSA 3: "No sabía cómo reportar / la planilla me llegó tarde." → SU PROPIO FORMATO LA RESPONDE:', bold=True)
frase('"Tu propio archivo tiene un formato de informe diario que tú misma construiste — y está bien hecho. Ayer no me mandaste ni ese ni el mío con los datos del día: me mandaste el del viernes. Y las llamadas de ayer no necesitaban ningún archivo. Eso no fue falta de información."')

sec('LAS DOS SALIDAS (ambas sirven — la decisión la toma su reacción)')
t('A) FIRMA HOY → corre la semana bajo reglas escritas. Viernes 19: deciden los números de la planilla contra los mínimos del acuerdo. Sin nueva reunión intermedia.')
t('B) NO FIRMA (o "lo pienso") → terminación hoy: se agradece, se paga lo causado, se pide devolución del material (kit, planilla, accesos) y las claves/bases quedan con la casa. Sin contrato vigente no hay nada que romper.')
t('REGLA DE ORO DE LA LLAMADA: no debatir causas ni personalidades. Cada desvío se responde igual: "eso lo resuelve la planilla del viernes". Quien se sale del guion pierde.', bold=True)

doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Heiiu English Academy · Gerencia · Documento interno — Septiembre 2026'); r.font.size = Pt(8.5); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\GUION_REUNION_ASESORA_15SEP.docx'
doc.save(out); print('OK', out)
