# -*- coding: utf-8 -*-
"""Hoja de la PRIMERA llamada de gerencia con Jhean (candidato Ejecutivo de Alianzas, 2º en línea).
Él ya respondió por escrito las 5 preguntas de números (16/10). La llamada contrasta esas cifras con una sola
pregunta abierta, cubre lo que no está en la HV, hace el embudo de Heiiu en vivo, dice los términos una vez
y cierra con la tarea. Sin oferta. 30 min por llamada. 2 págs.
Salida (fuera de git): Candidatos/HOJA_LLAMADA_JHEAN_TIRESIA.docx (+ PDF vía Word COM)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos'
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0); s.left_margin = Cm(1.7); s.right_margin = Cm(1.7)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(7); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR
def t(txt, size=10, color=None, after=3, bold=False, indent=0):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after); p.paragraph_format.left_indent = Cm(indent)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def caja(txt, size=10.5):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(txt); r.font.size = Pt(size); r.italic = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
def anota(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2); p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run('Anota: '); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = GRIS
    r = p.add_run(txt); r.font.size = Pt(9.5); r.font.color.rgb = GRIS
def bullets(items, size=10):
    for x in items:
        p = doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(1); r = p.add_run(x); r.font.size = Pt(size)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('JHEAN — PRIMERA LLAMADA (sus números ya llegaron por escrito)'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Llamada · 30 min · Uso interno de gerencia · Llevas: esta hoja, su HV y sus respuestas del 16/10'); r.font.size = Pt(9); r.font.color.rgb = GRIS

sec('Lo que respondió el 16/10, leído contra lo que pedimos')
tb = doc.add_table(rows=1, cols=3); tb.style = 'Table Grid'
hdr = ['Pregunta', 'Lo que dijo', 'Lectura']
for i, h in enumerate(hdr):
    c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
filas = [
 ('1. Ventas 12 meses y nº contratos', '$600M en contratos (ERP, 36-48 meses). No dio el número de contratos.', 'Con ticket $75-100M son 6 a 8 contratos al año: menos de uno al mes. Ciclo largo, ticket 20 veces el nuestro.'),
 ('2. Ticket y contactos por cierre', 'Ticket $75-100M. 15-20 empresas en frío al día "para obtener una oportunidad".', '300-400 contactos al mes. Disciplina de frío real. Contactos por cierre: ~500. Aquí necesita 40 al mes para 2 firmas.'),
 ('3. Reuniones con gerentes y origen', '10-15 al mes (virtual, visitas, viajes). Frío, algunos referidos; marketing no funcionó.', 'Cumple las 12 reuniones del mes 1 sin cambiar su ritmo. Verificar que eran con quien decide.'),
 ('4. Por qué salió y qué ha hecho', 'Tiempos de pago de comisiones. 3 meses de "break" y proyectos personales; Aprende Institute (no está en la HV) "no continuaron con el grupo"; hoy consultorías + fotografía.', 'Dos cosas que no están en la HV: Aprende Institute y la fotografía. Se preguntan hoy. Lo de comisiones importa: aquí se pagan mes vencido sobre caja.'),
 ('5. Expectativa mes 1 y mes 6', '$4M a $8M entre fijo y variable. No separó mes 1 de mes 6.', 'Cabe en el esquema (piso $3,5M + comisión). Hoy se le pregunta el mes en que pasa el piso.'),
]
for a, b, c3 in filas:
    row = tb.add_row().cells
    for i, txt in enumerate((a, b, c3)):
        row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
        r = row[i].paragraphs[0].add_run(txt); r.font.size = Pt(8.5); r.bold = (i == 0)
for row in tb.rows:
    row.cells[0].width = Cm(3.6); row.cells[1].width = Cm(6.6); row.cells[2].width = Cm(7.4)
doc.add_paragraph().paragraph_format.space_after = Pt(0)
t('Balance: pasó el filtro (respondió en horas, con cifras y sin adornos). Lo que falta probar hoy: que el ciclo corto y el ticket pequeño de Heiiu le sirven, que está de tiempo completo, y que lo de Aprende Institute tiene una explicación con fechas y una persona a quien llamar.', size=10, after=4)
caja('Regla de la llamada: una sola pregunta abierta al principio, los términos dichos una vez, y SIN oferta. Sale con la tarea. Carlos y la referencia (Francy Ferro, Tiresia) van después de la tarea.', size=10)

sec('1. Una sola pregunta (10 min)')
caja('"Cuéntame Tiresia de principio a fin: cómo conseguías la primera reunión, cuánto duraba de la primera llamada a la firma, quién firmaba, y cuánto de esos $600 millones entró a caja mientras estabas."')
t('Lo dejas hablar. Solo interrumpes para pedir un número cuando diga "mucho", "bastante" o "casi siempre".', size=10, color=GRIS)
anota('ciclo (semanas) ______  quién firmaba (cargo) ______  caja de los $600M $______  cuántos contratos ______.   Mala señal: no sabe cuánto entró a caja, o el que firmaba no era con quien él hablaba (entonces vendía a técnicos, no a gerentes).')
caja('Comisiones: "Dijiste que saliste por los tiempos de pago de las comisiones. ¿Cada cuánto las pagaban y sobre qué: lo firmado o lo cobrado?"')
anota('______________.   Aquí se le dice de una: "Nosotros pagamos mes vencido sobre lo que entra a caja. Si eso no te sirve, mejor saberlo hoy."')

sec('2. Lo que no está en la hoja de vida (5 min)')
caja('"Mencionaste Aprende Institute. ¿Cuándo fue, qué cargo, cuánto duró y a quién puedo llamar allá?"')
anota('fechas ______  cargo ______  duración ______  contacto ______.   Mala señal: no da fechas o no quiere que llamen.')
caja('"Las consultorías y el proyecto de fotografía: si entras aquí, ¿se cierran o siguen? Este cargo es de tiempo completo, con seguimiento diario."')
anota('______________.   Se acepta "la fotografía es fin de semana". No se acepta "manejo las dos cosas".')
caja('"¿Desde qué fecha podrías empezar?"')
anota('fecha ______.')

sec('3. Heiiu en vivo (10 min)')
t('Primero el dato, en una frase: "El cupo vale $4.782.800 por persona, nivel completo. Vendemos a empresas de 40 o más empleados, y el que decide es gerente, gerente de talento humano o dueño."', size=10, after=2)
caja('"Para hacer $30 millones al mes: ¿cuántos cupos son, en cuántas empresas, cuántas reuniones necesitas y a cuántos decisores tienes que contactar?"')
anota('cupos ______  empresas ______  reuniones ______  contactos ______.   Referencia: 6-7 cupos · 2-3 empresas · 12 reuniones · 40 contactos. Él viene de 300-400 contactos para una venta; si calcula bien, verá que aquí sobra ritmo y falta cierre.')
caja('"De tu red de Tiresia, ¿quiénes tienen 40 empleados o más y te recibirían la semana que entres? Dame tres nombres con empresa y cargo."')
anota('1 __________ 2 __________ 3 __________.   Mala señal: empresas sin persona, o solo gerentes de sistemas (compraban ERP, no deciden formación).')

sec('4. Los términos, dichos una vez (5 min)')
t('No se negocia nada hoy. Se dicen y se pasa a la pregunta de plata.', size=10, color=GRIS, after=2)
bullets([
 'Contrato laboral desde el día uno. Básico $2.000.000 más prestaciones.',
 'Ingreso mínimo de $3.500.000 los meses 1 a 3, en cada mes en que cumpla los indicadores: mes 1 = 40 empresas contactadas con quien decide, 12 reuniones, 2 firmas; mes 2 = 4 firmas acumuladas y 2 activaciones; mes 3 = 6 firmas acumuladas y 3 activaciones.',
 'Comisión del 10% sobre lo que entra a caja, no sobre lo firmado; se liquida mes vencido. Acelerador del 15% y 20% sobre la meta trimestral, sin tope. Más 6% de los pagos de cada estudiante de sus alianzas durante 12 meses.',
 'Meta $30 millones al mes en el primer trimestre, medida en ventas firmadas con inicial pagada.',
 'Dos días fijos en la sede, con planilla. Los otros días en campo. Seguimiento diario de 15 minutos a hora fija y planeación los lunes de 30 minutos, las dos las presenta él.',
 'Sin equipo a cargo. El equipo de asesoría apoya activaciones y matricula a los interesados que él genere, pero no le reporta.'])
caja('"Dijiste entre $4 y $8 millones. Con este esquema: ¿en qué mes calculas que tu comisión pasa el piso de $3,5 millones? Y si en el mes 4 no lo ha hecho, ¿qué haces?"')
anota('mes ______  respuesta al mes 4: ______________.   Lo que sirve: un número y una razón ("mes 3, con dos empresas de 5 cupos ya son $4,8M"). Mala señal: "no hay problema" sin cálculo, o pedir fijo de $4M.')
caja('Si pide más fijo: "El esquema es este para todo el mundo. Lo que sube aquí es la comisión, y sube sin tope."', size=10)

sec('5. Cierre: la tarea (2 min)')
caja('"Gracias. Te mando hoy por escrito una tarea corta, con fecha. Con eso y una llamada a tu referencia de Tiresia te digo cómo seguimos."')
t('Tarea (misma de los demás, se envía por WhatsApp al colgar, vence a las 48 horas): cinco empresas de 40 o más empleados con nombre y cargo del decisor; el mensaje con el que los contactaría, máximo 120 palabras; y su plan de las dos primeras semanas, día por día. No se dice "estás contratado", "cuenta con eso" ni "bienvenido". No se menciona ningún otro candidato.', size=10)

sec('Después de la llamada: 5 líneas a Carlos')
t('1) Tiresia: ciclo, quién firmaba y cuánto entró a caja; cuadra con "$600M": sí / no.  2) Aprende Institute y fotografía: explicación con fechas: sí / no; tiempo completo: sí / no.  3) Heiiu en vivo: su embudo se acerca a 6-7 cupos / 2-3 empresas / 12 reuniones / 40 contactos: sí / no; nombres con cargo: ______.  4) Plata: mes en que dice que pasa el piso y qué hace si no.  5) Tu veto: sí / no, y por qué en una frase.', size=10)
t('Orden después: tarea (48 h) → llamada a Francy Ferro (Tiresia) → entrevista de 5 preguntas de Carlos → oferta por escrito. Nada se promete antes.', size=10, bold=True, after=0)

out = BASE + r'\HOJA_LLAMADA_JHEAN_TIRESIA.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
