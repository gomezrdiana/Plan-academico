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
    s.top_margin = Cm(0.9); s.bottom_margin = Cm(0.7); s.left_margin = Cm(1.5); s.right_margin = Cm(1.5)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(9.5)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR
def t(txt, size=9.5, color=None, after=2, bold=False, indent=0):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after); p.paragraph_format.left_indent = Cm(indent)
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
        p = doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(1); r = p.add_run(x); r.font.size = Pt(size)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('JHEAN — REUNIÓN: NÚMEROS Y RETO DE 15 DÍAS'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('40 min · Uso interno de gerencia · Llevas: esta hoja, su HV, sus respuestas del 16/10 y el documento del reto (no se entrega en la reunión, se envía después)'); r.font.size = Pt(9); r.font.color.rgb = GRIS

sec('VERSIÓN AL GRANO — 20 minutos (usa solo esta página; lo demás es respaldo)')
t('1. Abres tú, 1 minuto, sin preámbulo:', bold=True, after=1)
caja('"Jhean, te voy a ir al grano. La academia necesita vender ya, y yo no tengo tiempo para un proceso de selección de tres semanas. La única forma de saber si esto funciona es trabajando. Te propongo un reto de 15 días. Te lo cuento completo y me dices si lo tomas."')
t('1b. Su experiencia, 5 minutos, una sola pregunta (para que se sienta escuchado y te sirva de puente):', bold=True, after=1)
caja('"Antes de contarte el reto, cuéntame Tiresia en cinco minutos: cómo conseguías la primera reunión, quién firmaba y cuánto duraba hasta la firma."')
anota('reunión: ______________  firmaba: ______________  ciclo: ______ semanas.   Si dice "mucho" o "casi siempre", pides el número. Puente al reto: "Aquí es lo mismo pero al revés: el ticket es 20 veces más chico y el ciclo tiene que ser de días, no de meses. Por eso el reto se mide en caja y no en reuniones."')
t('2. El Pacto, 1 minuto:', bold=True, after=1)
caja('"No vendemos inglés fácil ni rápido. Vendemos un entrenamiento exigente, con video diario y puntualidad, y un destino: el trabajo, el viaje o el estudio que esa persona necesita. El cliente firma sabiendo a qué se compromete. Quien no quiera entrenar así no es nuestro estudiante, y es mejor que lo sepa en la charla, no en la clase 5. Eso es lo que vas a decir en las empresas."')
t('3. El reto, de corrido, 3 minutos (no pausas hasta terminar):', bold=True, after=1)
bullets([
 'Lunes 20 de octubre a martes 3 de noviembre, por prestación de servicios. Diez días hábiles, el 2 es festivo.',
 'Meta: 10 inscritos con inicial pagada, por empresas, al menos 5 de una misma empresa.',
 'Empresas de dueño, 40 a 150 empleados, donde el que decide está en la reunión. Tú abres, das una charla de 20 minutos a su gente y cierras. El pago entra a Heiiu y coordinación firma el contrato.',
 'Un millón de honorarios más el 10% de la caja que entre hasta el 3 de noviembre. 15 minutos conmigo todos los días a las 8:00.',
 'El 4 de noviembre: 10 o más, contrato laboral con la meta a tu ritmo. 5 a 9, contrato con el esquema normal. Menos de 5, hasta ahí.'])
t('4. La plata, una frase:', bold=True, after=1)
caja('"Si logras los 10 te vas con entre 4 y 6 millones por 15 días. Pediste de 4 a 8 al mes. Aquí está."')
t('5. Las dos preguntas que sí haces, 3 minutos:', bold=True, after=1)
caja('"Y ahora, las consultorías y la fotografía: ¿se cierran o siguen? Esto es tiempo completo."   Se acepta "fin de semana". No se acepta "manejo las dos".')
caja('"¿Con qué cinco empresas arrancas mañana? Nombre del dueño o gerente."')
anota('1 __________ 2 __________ 3 __________ 4 __________ 5 __________.   Sin cinco con persona puede aceptar igual, pero ya sabes qué esperar el lunes.')
t('6. Cierre, 1 minuto:', bold=True, after=1)
caja('"¿Lo tomas? Te mando el reto por escrito al salir, me respondes acepto hoy, y esta noche te llega el kit, el formato y los documentos. Lunes 8:00 en la sede, dos horas y a la calle."')
t('Si pide más fijo: "El fijo sube el 4 de noviembre con el contrato." Si pide una semana de inducción: "Son dos horas y yo contigo todos los días a las 8:00." Si pregunta si hay más gente: "Hay otro ejecutivo en otro sector. Tu lista es tuya." No se dice "estás contratado". No se menciona a nadie más. Lo de Tiresia se lo pregunta Carlos el martes.', size=9.5, color=GRIS, after=0)
doc.add_page_break()

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
t('Balance: pasó el filtro (respondió en horas, con cifras y sin adornos). Lo que falta probar hoy: que el ciclo corto y el ticket pequeño de Heiiu le sirven, que está de tiempo completo, y que lo de Aprende Institute tiene una explicación con fechas y una persona a quien llamar.', size=9.5, after=4)
caja('Regla de la reunión: una sola pregunta abierta al principio, el reto dicho una vez y sin negociar, y SIN contrato laboral hoy. Sale con el reto por escrito. La referencia (Francy Ferro, Tiresia) se llama antes del lunes; Carlos lo entrevista dentro de la primera semana del reto.', size=9.5)

sec('1. Una sola pregunta (10 min)')
caja('"Cuéntame Tiresia de principio a fin: cómo conseguías la primera reunión, cuánto duraba de la primera llamada a la firma, quién firmaba, y cuánto de esos $600 millones entró a caja mientras estabas."')
t('Lo dejas hablar. Solo interrumpes para pedir un número cuando diga "mucho", "bastante" o "casi siempre".', size=9.5, color=GRIS)
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
t('Primero el dato, en una frase: "El programa completo vale $8.696.000; el empleado de una empresa aliada lo paga a $4.782.800 de contado o $5.565.440 en cuotas, y si la empresa paga los cupos, $4.782.800 cada uno ($4.350.000 de 8 en adelante). El Arranque, $2.990.000, solo si no le alcanza. Vendemos a empresas de 40 a 150 empleados donde el que decide es el dueño o el gerente."', size=9.5, after=2)
caja('"Para hacer $30 millones al mes: ¿cuántos cupos son, en cuántas empresas, cuántas reuniones necesitas y a cuántos decisores tienes que contactar?"')
anota('cupos ______  empresas ______  reuniones ______  contactos ______.   Referencia: 6-7 cupos · 2-3 empresas · 12 reuniones · 40 contactos. Él viene de 300-400 contactos para una venta; si calcula bien, verá que aquí sobra ritmo y falta cierre.')
caja('"De tu red de Tiresia, ¿quiénes tienen 40 empleados o más y te recibirían la semana que entres? Dame tres nombres con empresa y cargo."')
anota('1 __________ 2 __________ 3 __________.   Mala señal: empresas sin persona, o solo gerentes de sistemas (compraban ERP, no deciden formación).')

sec('4. El reto, dicho una vez y sin negociar (8 min)')
t('Antes del reto, El Pacto en un minuto: "No vendemos inglés fácil ni rápido. Vendemos un entrenamiento exigente, con video diario y puntualidad, y un destino: el trabajo, el viaje o el estudio que esa persona necesita. El cliente firma sabiendo a qué se compromete. Quien no quiera entrenar así no es nuestro estudiante, y es mejor que lo sepa en la charla, no en la clase 5. Eso es lo que vas a decir en las empresas."', size=9.5, after=3)
t('El reto no es el contrato. Es la prueba real, pagada, antes del contrato. Se dice completo, de corrido, y luego se pregunta.', size=9.5, color=GRIS, after=2)
bullets([
 'Del lunes 20 de octubre al martes 3 de noviembre (10 días hábiles; el 2 es festivo), por prestación de servicios, no contrato laboral.',
 'Meta única: 10 inscritos con inicial pagada, vía empresas, al 3 de noviembre. Al menos 5 de una misma empresa.',
 'Dónde: empresas de dueño, 40 a 150 empleados, donde el que decide está en la reunión y autoriza una charla de 20 minutos con su gente. Nada de compras ni multinacionales: no firman en dos semanas.',
 'Qué recibe: $1.000.000 de honorarios por el reto (cuenta de cobro el 3/11) más 10% de la caja que entre hasta esa fecha de los inscritos que él trajo.',
 'La plata en una frase: "Si logras los 10 te vas con entre 4 y 6 millones por 15 días: un millón de honorarios más el 10% de caja. Pediste de 4 a 8 al mes. Aquí está." (10 cupos pagados por la empresa: $5.350.000 · 10 completos pagados por empleados: $5.782.800 · 10 Arranques: $3.990.000).',
 'Qué pasa el 4 de noviembre: 10 o más = contrato laboral (básico $2M más prestaciones, piso $3,5M por indicadores, 10% de caja sin tope) con la meta puesta a su propio ritmo: noviembre 10 inscritos, diciembre 12, enero 15. "La meta de tu contrato va a ser lo que hagas en el reto, nunca menos." 5 a 9 = el mismo contrato con los indicadores estándar del cargo. Menos de 5 = se paga el reto y termina. El contrato es indefinido con periodo de prueba de 2 meses; eso se dice si pregunta, no se adelanta.',
 'Qué pone Heiiu: inducción de 2 horas el lunes, propuesta y oferta a empleados cerradas (él no inventa precios), hoja de precios y mensaje de contacto, planilla, coordinación para contratos y pagos, 15 minutos diarios a las 8:00 con gerencia. No hay asesora: él presenta y cierra.',
 'Ritmo mínimo: 15 empresas con decisor contactadas en los primeros 2 días, 8 reuniones con decisor la primera semana, 3 charlas autorizadas para la segunda.'])
caja('"¿Con qué empresas arrancas el lunes? Dame cinco, con nombre del dueño o gerente, que te reciban esta semana."')
anota('1 __________ 2 __________ 3 __________ 4 __________ 5 __________.   Esta es la respuesta que decide. Si no tiene cinco con persona, el reto no arranca el lunes: se le da hasta el miércoles para mandar la lista y arranca el jueves.')
caja('"¿Lo tomas?" Si pide más honorarios: "El fijo sube el 4 de noviembre con el contrato. Lo que sube en el reto es la comisión." Si pide que la meta sea en reuniones: no, la meta es caja. Si pide una semana de inducción: "Son dos horas el lunes y yo contigo 15 minutos todos los días a las 8:00; lo demás se aprende en la calle." Si pregunta si hay más gente vendiendo: "Hay otro ejecutivo de alianzas en otro sector. Tu lista es tuya." Nada más sobre eso.', size=9.5)

sec('5. Cierre (2 min)')
caja('"Te mando hoy el reto por escrito en una página. Me respondes acepto hoy mismo, y con eso te llega el formato y el mensaje de contacto para que mañana empieces con la lista de 15 empresas. El lunes a las 8:00 en la sede, inducción de 2 horas y a la calle. Antes del lunes hablo con tu referencia de Tiresia."')
t('No se dice "estás contratado", "cuenta con eso" ni "bienvenido". No se le muestra ni se le describe el esquema del otro ejecutivo: ni piso, ni comisión, ni fecha.', size=9.5)

sec('Después de la reunión: 5 líneas a Carlos')
t('1) Tiresia: ciclo, quién firmaba y cuánto entró a caja; cuadra con "$600M": sí / no.  2) Aprende Institute y fotografía: explicación con fechas: sí / no; tiempo completo: sí / no.  3) Heiiu en vivo: su embudo se acerca a 6-7 cupos / 2-3 empresas / 12 reuniones / 40 contactos: sí / no.  4) Las cinco empresas con persona para el lunes: sí / no.  5) Tomó el reto: sí / no, y tu veto en una frase.', size=9.5)
t('Orden: hoy el reto por escrito → sábado llamada a Francy Ferro → lunes 8:00 inducción → martes o miércoles Carlos le hace las 5 preguntas (ya con datos reales del reto) → 3/11 corte → 4/11 contrato o fin.', size=9.5, bold=True, after=0)

out = BASE + r'\Jhean Cardenas\HOJA_LLAMADA_JHEAN_TIRESIA.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
