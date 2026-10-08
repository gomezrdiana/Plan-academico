# -*- coding: utf-8 -*-
"""Ocho ajustes de configuracion del agente LaHaus para Jaider (07/10/2026), con el lead de ejemplo de cada uno.
Salida: recursos/comercial/plataforma LaHaus/AJUSTES_CONFIGURACION_JAIDER_2026-10-07.docx"""
import re
from docx import Document
from docx.shared import Pt, RGBColor

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(60); s.top_margin = s.bottom_margin = Pt(50)

def para(txt, size=10.5, color=None, after=6, italic=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', txt):
        if not part: continue
        r = p.add_run(part[2:-2] if part.startswith('**') else part); r.bold = part.startswith('**'); r.italic = italic; r.font.size = Pt(size)
        if color: r.font.color.rgb = color

p = d.add_paragraph(); r = p.add_run('AJUSTES DE CONFIGURACIÓN DEL AGENTE — PARA JAIDER (LAHAUS)'); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = NAR
para('Heiiu English Academy · 07/10/2026 · Son cambios de configuración (preguntas, agendamiento, reintentos, notificaciones), no del documento de conocimiento, que ya fue recargado por nosotros. Cada punto trae el lead real donde se vio el fallo (conversaciones del 3 al 6 de octubre).', color=GRIS, size=9.5, after=10)

p = d.add_paragraph(); r = p.add_run('MENSAJE (copiar y pegar)'); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = NAR
para('Jaider, gracias por la reunión. Te dejo por escrito los trece ajustes de configuración, cada uno con el lead donde lo vimos, para que me confirmes fecha de cada uno:')

items = [
 ('1. Orden de las preguntas: motivo → para quién → nivel → jornada → CITA.',
  'El decisor ("¿decides tú o consultas?") va dentro de la oferta de cita, no antes. El precio no es un paso del flujo. Y la secuencia debe poder interrumpirse: si el cliente objeta ("es muy caro") o pregunta precio, el agente responde la objeción y ofrece la cita, no sigue con la siguiente pregunta de la lista.',
  'Yarhi (4/10): después de la jornada recibió precio + decisor y se fue sin que le ofrecieran cita. Jaime Pérez (6/10, 7:53 pm): decisor antes de la cita, ya con la base nueva. Henry (6/10, 8:09 pm): igual. Fernanda (7/10, 7:22 pm): soltó los dos precios sin que los pidiera y preguntó el decisor por segunda vez, en tres mensajes en el mismo minuto. Tilcia (6/10): abrió con "es muy caro el semestre" y el agente arrancó la lista completa (meta, para quién, nivel, jornada, decisor, Cajasan, correo, "¿otro obstáculo?"); ella contestó dos monosílabos y se fue.'),
 ('2. Franjas de cita = horas concretas del calendario (videollamada o llamada).',
  'Nunca las jornadas de clase ("mañana 8-12 / noche 6:30-8:30") como si fueran la cita; nunca "fecha de corte" ni "siguiente cohorte". Un solo par de franjas hasta que el cliente responda; no se cambian.',
  'Jaime Pérez y Henry (6/10): "Estos serían los horarios para la siguiente fecha de corte: MAÑANA 8-12 o NOCHE 6:30-8:30". Yasmin (5/10): tres menús de franjas distintos en dos horas (3:00/11:00 → 4:00/10:00 → 3:30 video/4:00 sede/4:15 llamada). Isa Durango (6/10): 1:00/1:30/jueves 9:00 y luego 3:30/jueves 10:30.'),
 ('3. En estado "Agendando" no se hacen preguntas nuevas de perfilación.',
  'Una vez ofrecidas las franjas, el agente solo confirma la cita.',
  'Isa Durango (6/10, 12:01 pm): ya en Agendando le preguntó "¿qué te gustaría más: entender películas o viajar?".'),
 ('4. Los reintentos repiten la MISMA pregunta pendiente; nunca avanzan el flujo.',
  'Cadencia única y escrita para lead nuevo: 10 min, 1 h, 4 h, mañana siguiente, tarde siguiente (hoy varía de un lead a otro: a unos cada 5 minutos, a otros cada 35). Reactivación: máximo 2 en 48 horas y 1 a los 7 días. Cuando el cliente responde, el contador se reinicia.',
  'D🪐z (6/10): sin respuesta desde las 8:33, recibió cuatro preguntas distintas en 70 minutos (nombre → para quién → nivel → jornada). Adriana (5/10): tres preguntas apiladas. Gema (5/10): dos distintas y respondió "no entiendo la pregunta". Vanessa (5-6/10): cuatro seguidas. Fernanda (7/10): callada de 2:22 a 7:21 pm y recibió decisor, Cajasan y "¿quieres conocer cuál programa?", tres preguntas distintas; su "No señora" fue a la tercera.'),
 ('5. Notificaciones a María Eugenia (copia a Diana), y confirmar que le llegan.',
  'Disparadores: segunda pregunta de precio; cualquier pregunta de mensualidad; "quiero hablar con una persona"; y cierres como "no por ahora", "no tengo el dinero", "me queda alta la cuota", "gracias por la información", "yo te confirmo". El agente responde una línea y no cierra la conversación.',
  'Leine (6/10) preguntó el precio tres veces y la mensualidad; Richard (6/10) "¿cuánto hay que pagar mensual?"; Yasmin (5/10) "no alcanzo"; Claudia (6/10) "por ahora no"; Adriana (5/10) "no contamos con ese dinero". Catorce despedidas en 14 conversaciones y ninguna notificación visible. El agente escribió "¿prefieres que un asesor te contacte?" a Richard e Isa: ¿esa frase dispara algo y a quién?'),
 ('6. La reactivación excluye leads con conversación en los últimos 30 días o en estado activo/agendando.',
  'El mensaje masivo no debe caer sobre una conversación en curso.',
  'Vanessa: entró por formulario el 5/10 a las 5:45 pm, contestó "Noche" el 6/10 a las 7:46 am y a las 8:22 le llegó el mensaje de reactivación, que reinició toda la perfilación desde cero.'),
 ('7. Saludo por campaña.',
  '"Vi que te interesó el Arranque A1+A2" sin mes; a los leads de la campaña Curso Inglés, saludo genérico; Au Pair empieza con "¿el programa es para ti o para alguien más?".',
  'Henry y Jaime Pérez (6/10) y Fernanda (7/10, 1:45 pm) siguieron recibiendo "el Arranque de octubre". Adriana (4/10): llegó por Au Pair, el agente asumió que viajaba ella y era la mamá de una joven de 18.'),
 ('8. Reporte desde el 30/09: citas y tasa de respuesta por fuente (formulario, WhatsApp, reactivación) y por número de toque.',
  'Con eso decidimos esta semana dónde va el presupuesto y si el toque 4 y 5 generan citas o solo respuestas.',
  'Datos: en 9 días Meta entregó 59 leads de formulario y 19 conversaciones de WhatsApp; la reactivación tuvo tres respuestas en menos de 20 minutos el 6/10 (Claudia, Jerson, Alexandra).'),
 ('9. Las preguntas de perfilación se dan por respondidas cuando el cliente ya las contestó por su cuenta.',
  'Si el cliente dice algo que responde una pregunta que aún no se le ha hecho, el agente no la hace. Si la plataforma obliga a "hacer" cada pregunta, el agente sigue preguntando lo que ya sabe.',
  'Lead del 7/10: escribió "quiero reforzar lo que ya sé" (es para él y tiene nivel) y el agente le preguntó "¿el curso es para ti o para alguien más?".'),
 ('10. La línea de rescate es un estado de entrega: notificación a la asesora y el agente se detiene.',
  'Cuando el agente responde "Te entiendo. Déjame que la asesora te escriba hoy…", no debe seguir con más preguntas ni ofertas hasta que la asesora actúe o el cliente escriba.',
  'María Eugenia (lead, 7/10 12:34 pm): dijo la línea de rescate y después mandó cinco mensajes más en seis horas (correo, Arranque, Cajasan, "¿te gustaría saber…?").'),
 ('11. Plantillas: el correo no puede pedirse con "para dejar tu registro al día"; el nombre se pide como primer nombre, no "nombre completo"; y la confirmación de una cita por llamada o videollamada no puede decir "¡Nos vemos!" ni "Te esperamos".',
  'La frase del correo está prohibida desde el 30/09 y no está en nuestro documento: vive en la plantilla de la plataforma; el correo se pide solo al confirmar la cita, con su razón real. La plantilla del nombre pregunta "¿cuál es tu nombre completo?" y luego el agente usa el nombre completo en cada mensaje; debe ser solo el primer nombre.',
  'María Eugenia (lead, 7/10 12:28 pm) y varios más esta semana. Laura (6/10): "¿cuál es tu nombre completo?" y después "Laura Alejandra Guarin" en tres mensajes. Vanesa Celis (7/10): cita por LLAMADA confirmada con "¡Nos vemos!" y "Te esperamos".'),
 ('12. Agrupar los mensajes que el cliente manda en ráfaga y responder una sola vez.',
  'Muchos clientes escriben en fragmentos (tres o cuatro mensajes en el mismo minuto). El agente debería esperar 20-30 segundos y responder a todo junto; hoy contesta cada fragmento por separado y repite preguntas.',
  'Sandra (7/10, 5:15-5:18 pm): fragmentos "Un viaje" / "Mi hija va a estudiar…" / "Quiero saber q costo tiene"; el agente mandó dos respuestas por minuto y preguntó la jornada tres veces. (Aun así agendó: viernes 9/10 11:00 am.)'),
 ('13. Recordatorios de cita: dos como máximo, y ninguno antes de 12 horas después de agendar.',
  'Uno la noche anterior a las 7:00 pm (solo si la cita se agendó antes de ese día) y uno 60 minutos antes, con el enlace de la videollamada o "te llamamos a este número". Si la cita se agenda hoy para mañana, solo el de los 60 minutos.',
  'Vanesa Celis (7/10): agendó a las 2:38 pm para el jueves 4:30 pm y a las 4:32 pm le llegó "tu asesor tiene todo listo… ¿todo bien de tu parte?", dos horas después de decir "ok" dos veces.'),
]
for tit, regla, ej in items:
    para('**' + tit + '**', after=1)
    para(regla, after=1)
    para('Ejemplo: ' + ej, size=9.5, color=GRIS, italic=True, after=8)

para('**Bug de envío:** a Tilcia (6/10, 3:10 pm) le llegó el mismo mensaje dos veces en el mismo minuto.')
para('**Pregunta aparte:** anoche el agente dio precios que no existen: a Henry (6/10, 8:16 pm) le dijo "$9.560.000" y "$3.150.000"; los únicos valores son $8.696.000 y $2.990.000. ¿De dónde salieron? Necesito saber si el modelo rellena cuando no tiene el dato, porque ya volvimos a cargar los dos precios con la instrucción de cuándo decirlos.')
para('Gracias. Quedo atenta a las fechas.', after=12)

p = d.add_paragraph(); r = p.add_run('Nota interna: las 14 conversaciones completas están en AUDITORIA_AGENTE_CONVERSACIONES_2026-10-06.docx (misma carpeta).'); r.italic = True; r.font.size = Pt(9); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus\AJUSTES_CONFIGURACION_JAIDER_2026-10-07.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
