# -*- coding: utf-8 -*-
"""Hoja de la PRIMERA llamada de gerencia con Jhean (candidato Ejecutivo de Alianzas, 2º en línea).
Él ya respondió por escrito las 5 preguntas de números (16/10). La llamada contrasta esas cifras con una sola
pregunta abierta, cubre lo que no está en la HV, hace el embudo de Heiiu en vivo, dice los términos una vez
y cierra con la tarea. Sin oferta. 30 min por llamada. 2 págs.
Versión 17/10 tarde: el cierre ya no es la tarea sino el RETO DE ARRANQUE de 15 días (10 inscritos al 3/11), ver gen_reto_arranque_jhean.py.
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
r = p.add_run('JHEAN — REUNIÓN: NÚMEROS Y RETO DE 15 DÍAS'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('40 min · Uso interno de gerencia · Llevas: esta hoja, su HV, sus respuestas del 16/10 y el documento del reto (no se entrega en la reunión, se envía después)'); r.font.size = Pt(9); r.font.color.rgb = GRIS

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
caja('Regla de la reunión: una sola pregunta abierta al principio, el reto dicho una vez y sin negociar, y SIN contrato laboral hoy. Sale con el reto por escrito. La referencia (Francy Ferro, Tiresia) se llama antes del lunes; Carlos lo entrevista dentro de la primera semana del reto.', size=10)

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

sec('4. El reto, dicho una vez y sin negociar (8 min)')
t('No es el contrato. Es la prueba real, pagada, antes del contrato. Se dice completo y luego se pregunta.', size=10, color=GRIS, after=2)
bullets([
 'Del lunes 20 de octubre al martes 3 de noviembre (10 días hábiles; el 2 es festivo), por prestación de servicios, no contrato laboral.',
 'Meta única: 10 inscritos con inicial pagada, vía empresas, al 3 de noviembre. Al menos 5 de una misma empresa.',
 'Dónde: empresas de dueño, 40 a 150 empleados, donde el que decide está en la reunión y autoriza una charla de 20 minutos con su gente. Nada de compras ni multinacionales: no firman en dos semanas.',
 'Qué recibe: $1.000.000 de honorarios por el reto (cuenta de cobro el 3/11) más 10% de la caja que entre hasta esa fecha de los inscritos que él trajo.',
 'Qué pasa el 4 de noviembre: 10 o más = contrato laboral con el piso del mes 1 garantizado. 5 a 9 = contrato laboral con el esquema estándar (básico $2M, piso $3,5M por indicadores, 10% de caja). Menos de 5 = se paga el reto y termina.',
 'Qué pone Heiiu: inducción de 2 horas el lunes, propuesta y oferta a empleados cerradas (él no inventa precios), hoja de precios y mensaje de contacto, planilla, coordinación para contratos y pagos, 15 minutos diarios a las 8:00 con gerencia. No hay asesora: él presenta y cierra.',
 'Ritmo mínimo: 15 empresas con decisor contactadas en los primeros 2 días, 8 reuniones con decisor la primera semana, 3 charlas autorizadas para la segunda.'])
caja('"¿Con qué empresas arrancas el lunes? Dame cinco, con nombre del dueño o gerente, que te reciban esta semana."')
anota('1 __________ 2 __________ 3 __________ 4 __________ 5 __________.   Esta es la respuesta que decide. Si no tiene cinco con persona, el reto no arranca el lunes: se le da hasta el miércoles para mandar la lista y arranca el jueves.')
caja('"¿Lo tomas?" Si pide más honorarios: "El fijo sube el 4 de noviembre con el contrato. Lo que sube en el reto es la comisión." Si pide que la meta sea en reuniones y no en inscritos: no. La meta es caja, porque es lo que necesita la academia.', size=10)

sec('5. Cierre (2 min)')
caja('"Te mando hoy el reto por escrito en una página. Me respondes acepto hoy mismo, y con eso te llega el formato y el mensaje de contacto para que mañana empieces con la lista de 15 empresas. El lunes a las 8:00 en la sede, inducción de 2 horas y a la calle. Antes del lunes hablo con tu referencia de Tiresia."')
t('No se dice "estás contratado", "cuenta con eso" ni "bienvenido". No se menciona ningún otro candidato. No se le muestra el esquema de John ni se le dice que hay otro proceso.', size=10)

sec('Después de la reunión: 5 líneas a Carlos')
t('1) Tiresia: ciclo, quién firmaba y cuánto entró a caja; cuadra con "$600M": sí / no.  2) Aprende Institute y fotografía: explicación con fechas: sí / no; tiempo completo: sí / no.  3) Heiiu en vivo: su embudo se acerca a 6-7 cupos / 2-3 empresas / 12 reuniones / 40 contactos: sí / no.  4) Las cinco empresas con persona para el lunes: sí / no.  5) Tomó el reto: sí / no, y tu veto en una frase.', size=10)
t('Orden: hoy el reto por escrito → sábado llamada a Francy Ferro → lunes 8:00 inducción → martes o miércoles Carlos le hace las 5 preguntas (ya con datos reales del reto) → 3/11 corte → 4/11 contrato o fin.', size=10, bold=True, after=0)

out = BASE + r'\HOJA_LLAMADA_JHEAN_TIRESIA.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
