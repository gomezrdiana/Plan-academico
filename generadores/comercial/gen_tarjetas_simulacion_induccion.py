# -*- coding: utf-8 -*-
"""Tarjetas de simulación para la inducción del Gerente de Alianzas (gerencia actúa de decisor): dos reuniones de 10 min
y una charla de 5 min. Por rol. Salida (git): recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/TARJETAS_SIMULACION_INDUCCION_ALIANZAS.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\TARJETAS_SIMULACION_INDUCCION_ALIANZAS.docx'
d = Document()
for s in d.sections:
    s.top_margin = Cm(0.9); s.bottom_margin = Cm(0.7); s.left_margin = Cm(1.3); s.right_margin = Cm(1.3)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAR
def t(txt, size=9.5, color=None, after=2, bold=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def caja(txt, size=9.5):
    tb = d.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(txt); r.font.size = Pt(size); r.italic = True
    d.add_paragraph().paragraph_format.space_after = Pt(0)
def bullets(items, size=9.5):
    for x in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); r = p.add_run(x); r.font.size = Pt(size)

p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('TARJETAS DE SIMULACIÓN — INDUCCIÓN DEL GERENTE DE ALIANZAS'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(5)
r = p.add_run('Gerencia actúa de decisor. Él lleva la reunión de 6 pasos del kit. Hoja de gerencia, no se le entrega. Las respuestas son la idea que debe decir con sus palabras, no un guion. Dos correcciones por simulación, al final, no en medio.'); r.font.size = Pt(8.5); r.font.color.rgb = GRIS

def par(dice, responde, mira):
    tb = d.add_table(rows=1, cols=3); tb.style = 'Table Grid'
    for k, (txt, bold, fill) in enumerate([(dice, True, 'FFF8E7'), (responde, False, None), (mira, False, None)]):
        c = tb.rows[0].cells[k]; c.paragraphs[0].paragraph_format.space_after = Pt(0)
        if fill: shd(c, fill)
        r = c.paragraphs[0].add_run(txt); r.font.size = Pt(8.5); r.bold = bold
        if k == 2: r.font.color.rgb = GRIS
    for row in tb.rows:
        for k, w in enumerate([4.0, 10.2, 3.8]): row.cells[k].width = Cm(w)
def enc():
    tb = d.add_table(rows=1, cols=3); tb.style = 'Table Grid'
    for k, h in enumerate(['Tú dices', 'Lo que él debería responder (la idea, con sus palabras)', 'Marca si']):
        c = tb.rows[0].cells[k]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(8.5); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for row in tb.rows:
        for k, w in enumerate([4.0, 10.2, 3.8]): row.cells[k].width = Cm(w)

sec('Simulación 1 · Gerente de una clínica de 80 empleados (10 minutos)')
t('Quién eres: gerente general, ocupada, le diste 10 minutos. Tu interés real: retener personal asistencial y verte bien con la junta. No sabes nada de la academia.', size=9)
enc()
par('Apertura fría: "Tengo diez minutos. ¿Esto me va a costar plata?"',
    '"Depende de lo que usted quiera: si quiere formar a su equipo, la empresa invierte; si prefiere no tocar presupuesto, la alianza no le cuesta nada. Antes de eso, un minuto de quiénes somos." Y la causa: academia santandereana e independiente; formar a la gente de Santander a través del inglés, con disciplina y valores, y demostrar que las empresas locales ganan con resultados que se pueden mostrar. Luego: "¿A usted qué le importa más: formar a su equipo o premiarlo?"',
    'No arrancó con precios ni con "academia de inglés". Dijo la causa en una frase y preguntó formar o premiar.')
par('Cuando mencione la alianza sin costo: "¿Y entonces ustedes qué ganan?"',
    '"Estudiantes. Llegan con una carta de su empresa, entran al programa completo con la beca más alta del Fondo y pagan directo a la academia. Usted gana un beneficio para su gente sin costo, becas con el nombre de la clínica y un reporte de asistencia y cumplimiento de sus becados. Usted no gestiona ni recibe un peso."',
    'Lo dijo sin rodeos: ganamos alumnos. No dijo "nómina", "gratis" ni "patrocinio".')
par('Cuando mencione el plan empresa: "Ya tuvimos un convenio con una academia y nadie terminó el curso."',
    '"Por eso nuestra garantía es por escrito: si la persona cumple asistencia, tareas y evaluaciones y no avanza, se le devuelve el 100% del nivel. Y por eso el grupo es selectivo: antes de pagar, cada persona escucha El Pacto y acepta entrenar así, con video diario y un profesor que es mentor y le pide cuentas. A usted le llega el reporte de asistencia y cumplimiento de sus becados." Sin nombrar a la otra academia.',
    'Respondió con garantía, Pacto y reporte de asistencia. No ofreció descuento ni habló mal de la otra academia.')
par('Cuando mencione la garantía: "¿Garantía de qué? ¿Me devuelven la plata a mí o al empleado?"',
    '"A quien pagó. Si la clínica pagó los cupos, a la clínica; si el colaborador pagó con la beca de la alianza, a él. Las condiciones las firma el estudiante en su contrato: hasta 20% de faltas por nivel, tareas al 90% y todas las evaluaciones. Retracto de ley 5 días hábiles; después no hay devolución por retiro, solo por garantía."',
    'Dijo las condiciones (asistencia, tareas, evaluaciones) y a quién se devuelve. No prometió "si no aprende, plata de vuelta" a secas.')
par('Cuando pida la charla: "Mis turnos son rotativos; no puedo sacar a nadie 20 minutos."',
    '"La hacemos en dos charlas de 15 minutos, una por turno, el día que usted diga; o en el cambio de turno. Y para su gente de turnos rotativos le digo de frente: el programa es de horario fijo; a quien no pueda cumplirlo no se lo vendo, porque la asistencia es parte de la garantía."',
    'Ofreció una charla por turno con fecha. Dijo que a turnos rotativos no se les vende sin horario fijo.')
par('Cierre: "Mándeme la propuesta por correo y lo pensamos." (No cedas.)',
    '"Se la mando hoy. Y para que no se quede en el correo, dejemos ya la charla: ¿martes a las 7 o jueves a las 2? Si después de la charla no le sirve, no firma nada." Y silencio. Si insistes: "Firmamos el convenio, que no le cuesta nada ni la obliga, y la charla es la prueba."',
    'Propuso dos fechas y se calló. No se fue con "le mando la propuesta" sin fecha.')
caja('Corrección típica: se va a los precios antes de que preguntes, o abre con "somos una academia de inglés". Al final: "Me diste el precio antes de saber si yo quería formar o premiar. Pregunta primero."')

sec('Simulación 2 · Directora de una fundación (10 minutos)')
t('Quién eres: directora de una fundación con 120 beneficiarios jóvenes y 15 empleados. Te importa la causa social, no tienes presupuesto y desconfías de "convenios" que son publicidad disfrazada.', size=9)
enc()
par('Apertura: "Nosotros no tenemos presupuesto para esto."',
    '"No lo necesita. Lo que le propongo no le cuesta a la fundación: un beneficio de formación para su equipo y para sus beneficiarios mayores de 12, con becas con el nombre de la fundación y garantía por escrito. Le cuento quiénes somos en un minuto." La causa, y luego: "¿Quién le importa más hoy: su equipo o sus beneficiarios?"',
    'No se asustó con "sin presupuesto". Dijo "sin costo para la fundación" y la causa.')
par('Cuando hable de becas con el nombre de la fundación: "¿Cuántas becas y de cuánto? ¿Es beca o es descuento?"',
    '"Es beca, no descuento. El programa vale $8.696.000; las becas las otorga el Fondo de Becas de la academia según el perfil y con soportes, y la alianza con la fundación da la columna más alta: el completo a $4.782.800 de contado. Además la fundación elige 3 becas con su nombre por trimestre, que suben a 5 si todos sus becados cumplen, con certificado a nombre de la fundación. No se suman becas: se aplica la mejor."',
    'Explicó beca y descuento (el Fondo, el perfil, los soportes) y las 3 becas con nombre. No inventó cupos gratis.')
par('Cuando hable de los jóvenes: "Mis muchachos no tienen 4 millones. ¿Qué les ofrecen a ellos?"',
    '"Para quien empieza, el Arranque: A1 y A2, 200 horas, con Módulo de Graduación, $2.990.000 en máximo dos pagos. Para los de 12 a 17, por lo general el sabatino. Y si la fundación quiere becar a alguno con recursos de un donante, eso lo agendo con gerencia." No promete nada más.',
    'Dio el Arranque y el sabatino. Lo que no está en el kit lo mandó a gerencia, sin prometer.')
par('Cuando hable de la empresa aliada: "¿Puedo poner esto en mi informe a los donantes?"',
    '"Sí: la fundación queda como aliada de la academia, con el convenio firmado y los certificados de las becas con su nombre. Lo que no le puedo dar son notas ni datos de los estudiantes: solo el reporte de asistencia y cumplimiento de sus becados."',
    'Dijo sí con límites: convenio y certificados sí; notas y datos personales no.')
par('Cierre: "¿Y qué me toca hacer a mí?"',
    '"Tres cosas: firmar el convenio de 12 meses, que no tiene costo ni obligaciones económicas; nombrar un contacto que emita las cartas de postulación; y darme 20 minutos con su gente. La fundación no recibe ni gestiona pagos. ¿La charla la hacemos el martes o el jueves?"',
    'Dijo las tres cosas del convenio y pidió la charla con fecha. No dijo que él firma por Heiiu.')
caja('Corrección típica: promete cosas para los jóvenes que no existen (cupos gratis, precios especiales). Al final: "Lo que no está en el kit se agenda con gerencia; no se promete."')

sec('Charla de 5 minutos a empleados (tú eres la sala: tres empleados en uno)')
enc()
par('A los 30 segundos: "¿Cuánto vale?"',
    '"Ya te doy los números; primero te cuento cómo es esto, para que decidas con todo claro." Y El Pacto completo en voz alta. Luego: completo $8.696.000 de lista; con la beca de la alianza $4.782.800 de contado o $5.565.440 en cuotas; Arranque $2.990.000 solo si el completo no le alcanza. "No manejamos descuentos: el precio es el precio."',
    'El Pacto antes del precio. Las opciones en orden. Dijo "beca", nunca "descuento".')
par('"¿Es virtual?"',
    '"En grupo somos presenciales. Virtual solo las clases personalizadas por videollamada, desde 30 horas, que arma gerencia contigo."',
    'No prometió grupo virtual.')
par('"¿Y si no aprendo?"',
    'La garantía con su texto: "Si cumples (asistencia, tareas y evaluaciones) y no avanzas, te devolvemos el 100% del nivel. Por escrito, en el contrato."',
    'Dijo las condiciones junto con la garantía.')
par('"¿Hay clase de prueba?"',
    '"No manejamos clase de prueba: una clase suelta no te muestra si vas a aprender; lo que te lo garantiza es el contrato." Y cierra: "Hoy te doy tu número exacto, pagas a la cuenta de Heiiu y firmas en la sede con coordinación. Los primeros que se matriculan definen el horario." Pasa la hoja de interesados: nombre, celular, motivo, jornada.',
    'Dijo no a la prueba sin disculparse. Cerró con cómo inscribirse hoy y pasó la hoja.')

sec('Cierre de las simulaciones (2 minutos)')
t('Dos correcciones en total, no más, y una cosa que hizo bien dicha con el mismo peso. Luego: "A las 4 lo haces de verdad, con los 18."', size=9, after=0)

try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
