# -*- coding: utf-8 -*-
"""Auditoria de conversaciones del agente LaHaus 03-06/10/2026: mensaje a JP + anexo con 6 conversaciones; y lista de rescates para Paula."""
import re
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus'
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); ROJO = RGBColor(0xB0, 0x00, 0x00)

def newdoc():
    d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
    for s in d.sections: s.left_margin = s.right_margin = Pt(60); s.top_margin = s.bottom_margin = Pt(50)
    return d

def para(d, txt, bold=False, size=10.5, color=None, after=6, italic=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', txt):
        if not part: continue
        r = p.add_run(part[2:-2] if part.startswith('**') else part)
        r.bold = bold or part.startswith('**'); r.italic = italic; r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    return p

def h(d, txt, size=13):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAR

# ------------------------------------------------------------------ DOC 1: mensaje + anexo
d = newdoc()
h(d, 'AUDITORÍA DEL AGENTE — CONVERSACIONES 3 AL 6 DE OCTUBRE DE 2026', 14)
para(d, 'Para: Juan Pablo (LaHaus) · De: Heiiu English Academy · 06/10/2026', color=GRIS, size=9.5, after=10)

h(d, 'MENSAJE (copiar y pegar)')
msg = [
 'Juan Pablo, buenos días. Revisé siete conversaciones del agente del 3 al 6 de octubre (van completas en el anexo, con la línea exacta donde se perdió cada una). Las siete se pierden en el mismo punto: el agente perfila bien, pero al final da precio y pregunta "¿decides tú o consultas?" en vez de agendar, y cuando el lead dice "no" cierra sin rescate. Dos cosas son urgentes hoy y diez son ajustes para esta semana.',
 '**URGENTE 1 — Fecha vencida.** El agente dice "¿Te queda bien si las clases empiezan el 5 de octubre?" (y "la cohorte que inicia este 5 de octubre") en cinco de las seis conversaciones, incluidas las de hoy 6 de octubre. Acordamos que el agente no maneja fechas de inicio. Quitar hoy. También sigue "el Arranque de octubre" en el saludo: sin mes.',
 '**URGENTE 2 — Cero citas presenciales.** El agente está ofreciendo "pasar por la sede" y "Asesoría Personalizada en la sede". Hoy no hay asesora física en la academia: si un lead llega, no hay quien lo atienda. Desde ya el agente ofrece únicamente videollamada o llamada. Presencial solo cuando el calendario tenga franjas marcadas como presenciales (hoy, ninguna). Y necesito la lista de todas las citas agendadas desde el 30/09 con modalidad, para convertir hoy las presenciales a videollamada.',
 '**Los diez ajustes:**',
 '1. Cierre de la perfilación = cita. Después de la jornada, el agente propone dos franjas (videollamada o llamada). El precio solo si lo piden, y siempre seguido de la cita. Hoy el agente termina en precio + "¿decides tú o consultas?" y se queda esperando.',
 '2. Una pregunta a la vez. Si el lead no contesta, el seguimiento repite la misma pregunta; no lanza la siguiente. En tres casos mandó dos o tres preguntas distintas seguidas y el lead respondió "no entiendo la pregunta".',
 '3. Franjas estables. Un solo par de opciones por conversación hasta que respondan. A Yasmin le ofreció tres menús distintos de horario en dos horas (3:00/11:00; 4:00/10:00; 3:30 video/4:00 sede/4:15 llamada).',
 '4. Nivel intermedio (A2, B1, TOEFL, IELTS) → prueba de nivel + asesoría para plan B1-B2. Nunca el Arranque A1+A2. Si el lead dice "ya hice la prueba", no se le vuelve a mandar el EF SET.',
 '5. Precio con contexto: "el programa completo tiene becas del Fondo del 32% al 45% según tu perfil y planes de cuotas; el valor exacto sale en la asesoría". Nunca abrir con $8.696.000. Y si el lead calcula una mensualidad (Yasmin dividió $2.990.000 entre 5 meses), el agente la corrige: la cuota tiene inicial y mensualidades; no es el valor dividido en meses; y ofrece la cita.',
 '6. Sin promesas. "Te deja lista para ganarte la plaza", "la dejamos lista para la entrevista": fuera. El módulo Pasaporte se describe, no se promete.',
 '7. Rescate humano. Cualquier "no por ahora", "no tengo el dinero", "me queda alta la cuota", "yo te confirmo", "gracias" dispara notificación a Paula (copia a Diana) y el agente NO cierra la conversación. En las siete hubo siete despedidas y cero rescates.',
 '8. Ruta ejecutiva. Nivel B2, "personalizado" o "ejecutivo": sin precios de programa, sin Arranque, sin EF SET; el agente ofrece dos franjas de llamada con la dirección académica. Hoy una lead de reactivación con B2 que pidió personalizado se fue sin que le ofrecieran una sola hora.',
 '9. Familias: dos o más personas (mamá e hijo, pareja) = cita con humano de inmediato. Nunca precio de lista por persona ni "aplicarían los valores estándar": en la asesoría se evalúa la beca del Fondo de cada uno y un plan de cuotas conjunto.',
 '10. Horario o edad que el agente no tenga configurado (por ejemplo tarde entre semana, o menor de 17 que no puede el sábado) nunca se responde con "no se puede". El agente captura la franja que le sirve al lead ("¿qué franja entre 1:30 y 6:00 pm te sirve?") y notifica a coordinación. Hoy una mamá con hijo de 15 que solo podían entre semana en la tarde recibió "tu hijo no podría estudiar en ese horario", y la academia tiene salones libres en la tarde.',
 'Y cuando el lead manda varias preguntas seguidas, el agente responde en UN solo mensaje: hoy mandó cinco mensajes en dos minutos a la misma persona.',
 'Dos notas más: el correo se pide al confirmar la cita, no en mitad de la perfilación (hoy salió antes de la jornada en dos chats). Y la reactivación funciona: dos respuestas en menos de 20 minutos esta mañana; el cuello está en los últimos tres mensajes de cada conversación.',
 'Y un dato que necesito desde ya, no para el 15: citas por fuente (formulario, WhatsApp y reactivación) y tasa de respuesta de cada grupo, de lo que va desde el 30/09. Con eso decidimos esta misma semana dónde va el presupuesto. ¿Me lo pasas hoy, y me confirmas cuándo quedan aplicados los dos urgentes y los diez ajustes?',
]
for m in msg: para(d, m)

d.add_page_break()
h(d, 'ANEXO — LAS SIETE CONVERSACIONES Y DÓNDE SE PERDIÓ CADA UNA', 13)

convs = [
 ('1. YARHI — 03-04/10 · Curso Inglés (formulario) · trabajo y viajes · básico · noche',
  'Se perdió en: precio del Arranque sin pedirlo + pregunta de decisor en el mismo mensaje; ninguna oferta de cita; al "no, muchas gracias" el agente cierra sin rescate.',
  """[Agente 03/10 19:58] Hola! Soy Louissiana, de Heiiu English Academy en Bucaramanga. Gracias por escribirnos. Vi que te interesó el Arranque de octubre. Para decirte si es el programa que te sirve, cuéntame: ¿para qué necesitas el inglés, un trabajo, un viaje, un estudio, un negocio…?
[Lead 19:58] Trabajo y viajes
[Agente 19:59] Qué bueno Yarhi Gómez. El inglés te quita la excusa que hoy te cierra vacantes y te permite viajar entendiendo todo desde que llegas al aeropuerto. ¿El curso es para ti o para alguien más?
[Lead 20:11] Para mí
[Agente 20:11] Anotado Yarhi. Como de hoy qué tanto inglés tienes, ¿empiezas desde cero o ya entiendes algo?
[Lead 04/10 06:39] Algo básico
[Agente 06:40] Listo ¿qué jornada te queda mejor: la mañana de 8:00 a 12:00 o la noche de 6:30 a 8:30 PM?
[Lead 06:48] Noche
[Agente 06:49] Para tu meta de trabajo y viajes te cuento cómo funciona la escalera en Heiiu. Primero el programa completo A1 a B2 de 575 horas con becas del fondo según tu perfil y refuerzo pro. Como segunda opción el Arranque A1 y A2 de 200 horas por un precio de lanzamiento de $2.990.000. ¿La decisión la tomas tú o la consultas con alguien más?   ← AQUÍ: precio sin pedirlo + decisor; sin cita
[Lead 13:36] No, muchas gracias por la información
[Agente] Con gusto Yarhi. Quedo atenta por si retomas el proceso más adelante. Buen día.   ← cierre sin rescate"""),
 ('2. ADRIANA — 04-05/10 · Au Pair (formulario) · mamá, hija de 18 que ya habla inglés',
  'Se perdió en: tres preguntas apiladas sin esperar respuesta; promesa; primer número $8.696.000; "las clases empiezan el 5 de octubre"; salta de precio a "empezar clases" sin cita; al "no contamos con ese dinero" cierra sin ofrecer Fondo ni cuotas.',
  """[Agente 04/10 21:10] Hola! Soy Louissiana… Vi que llegaste por lo de Au Pair. Para orientarte bien, cuéntame: ¿para cuándo tienes pensado viajar?
[Lead 21:12] Hola....solo quisiera mas información....por el momento
[Agente 21:13] Claro Adriana. Para darte la información que realmente te sirve cuéntame ¿cuál es tu meta principal con el inglés: un trabajo, un viaje, un estudio o un negocio?
[Agente 05/10 09:11] Adriana, para enviarte la información más acertada… ¿el programa de inglés sería para ti o para alguien más?   ← segunda pregunta sin respuesta a la primera
[Agente 09:46] Adriana, para orientarte sobre tu proceso de Au Pair… ¿Qué tanto inglés sientes que dominas hoy?   ← tercera pregunta apilada
[Lead 09:58] Sería para mí hija....ella habla inglés, tiene 18 años
[Agente 09:58] Qué bien Adriana. Imagínate a tu hija pasando su entrevista con la familia en Estados Unidos con total seguridad. Con el módulo Pasaporte la dejamos lista para que se gane esa plaza ✈️. ¿Qué horario le queda mejor…?   ← promesa
[Agente 10:33] Adriana, para definir el mejor plan para tu hija, ¿tú misma tomas la decisión…?
[Lead 10:36] Con mi esposo..... pero queremos saber cuánto dinero se necesita presupuestar para esto
[Agente 10:37] …el programa completo A1 a B2 de 575 horas vale $8.696.000 y se evalúa una Beca del Fondo en la asesoría. El Arranque A1+A2 de 200 horas tiene un precio de lanzamiento de $2.990.000. Por cierto ¿son afiliados a Cajasan?   ← abre con precio de lista
[Lead 10:41] No ..no somos afiliados
[Agente 10:42] Listo Adriana. Como ella ya tiene bases lo primero es definir su nivel exacto para el programa. ¿Te queda bien si las clases empiezan el 5 de octubre en las dos jornadas?   ← fecha; sin cita
[Lead 10:44] No....nos toca esperar.... porque no contamos con ese dinero.. de todas formas gracias por la información...
[Agente] Listo sin problema. Aquí estaremos cuando lo necesiten para retomar. Que estés muy bien.   ← cierre sin Fondo/cuotas ni rescate"""),
 ('3. GEMA — 05/10 · Curso Inglés (formulario) · TOEFL B2 · ya tiene B1/A2 · noche',
  'Se perdió en: le empuja el Arranque A1+A2 a alguien con B1; repite la jornada dos veces y mete el decisor antes de respuesta ("no entiendo la pregunta"); precio sin pedirlo; el humano entra 1h40 después y tampoco agenda.',
  """[Agente 05/10 05:57] Hola! Soy Louissiana… Vi que te interesó el Arranque de octubre… ¿para qué necesitas el inglés…?
[Lead 06:01] Trabajo
[Agente 06:02] Imagínate en la vacante que hoy pasas de largo porque pide inglés… ¿En qué área trabajas o qué proyecto tienes en mente? 📈
[Lead 06:36] Quiero certificarme en toefl como b2
[Agente 06:37] Gema un nivel B2 es el punto donde ya te mueves con total seguridad en cualquier entrevista de trabajo. ¿El programa lo buscas para ti o para alguien más?
[Lead 06:37] Para mi
[Agente 06:37] ¿Hoy qué tanto inglés tienes? ¿Empiezas desde cero o ya entiendes algo?
[Lead 06:38] B1 o como mínimo A2. No he hecho pruebas recientes
[Agente 06:39] Tener esas bases te ayuda a avanzar más rápido al B2. ¿Qué horario te queda mejor…?
[Agente 09:14] Gema, para validar disponibilidad en el Arranque y que logres ese B2… ¿te queda mejor la jornada de la mañana… o la de la noche…? 💼   ← repite + Arranque a una B1
[Agente 09:46] Gema, para alcanzar ese nivel B2… ¿tomas la decisión de iniciar el programa por tu cuenta o lo consultas con alguien más?   ← tercera pregunta sin respuesta
[Lead 10:15] En la noche me queda mejor. No entiendo la pregunta sobre la decisión de entrar la programa
[Agente 10:17] Gema la pregunta es solo para saber si quieres que alguien más se conecte a la asesoría… Te cuento del programa completo A1 a B2: son 575 horas presenciales con garantía por escrito y una beca del fondo… También tienes el Arranque A1+A2 por $2.990.000 COP. ¿Eres afiliada a Cajasan?   ← precio sin pedirlo; sin cita
[Lead 11:56] Nooo, estoy en comfenalco
[Humano 12:03] para darte información más detallada teniendo en cuenta que ya has estudiado inglés… te puedo indicar que prueba gratuita puedes hacer para validar el nivel de ingles. y así podemos avanzar / te parece ?   ← 1h40 después; sin franja"""),
 ('4. YASMIN — 05/10 · Curso Inglés (formulario) · viaje · desde cero · noche · decide ella',
  'Se perdió en: precio del Arranque sin pedirlo; tres menús de franjas distintos en dos horas; "las clases empiezan hoy 5 de octubre"; la lead calcula $2.990.000 ÷ 5 = $589.000 y nadie corrige que la cuota no es el valor dividido en meses; cierre sin rescate.',
  """[Agente 05/10 12:29] Hola! Soy Louissiana… Vi que te interesó el Arranque de octubre…
[Lead 12:29] Un viaje
[Agente 12:30] Qué bueno Yasmin. Imagínate llegando al aeropuerto… Para eso está el módulo Pasaporte que te deja lista. Por cierto ¿el curso es para ti o para alguien más?   ← promesa
[Lead 12:31] Para mí
[Agente 12:31] …¿hoy qué tanto inglés tienes?
[Lead 12:33] Desde cero
[Agente 12:34] Como empiezas desde cero no necesitas prueba. Respecto a tu tiempo ¿qué horario te queda mejor…?
[Lead 12:36] Noche
[Agente 12:37] Perfecto Yasmin. El programa completo va de A1 a B2… También tienes el Arranque A1+A2 por $2.990.000 COP que es ideal para tu viaje. ¿La decisión la tomas tú o la consultas con alguien más?   ← precio sin pedirlo
[Agente 13:11] Yasmin, para que empieces clases el 12 de octubre… ¿te queda mejor agendar tu asesoría mañana a las 3:00 pm o el miércoles a las 11:00 am? ✈️   ← franjas 1
[Agente 13:45] Yasmin, para terminar de organizar tu perfil, ¿eres afiliada a Cajasan?
[Agente 14:35] Yasmin, si aseguras tu cupo en el Arranque A1+A2 el mismo día de tu Asesoría Personalizada, los libros van incluidos. ¿Te sirve pasar por la sede mañana a las 4:00 pm o el miércoles a las 10:00 am?   ← franjas 2 (distintas) + "en la sede"
[Lead 15:01] Cuantos meses dura el curso, mensualmente pagaría cuánto?
[Agente 15:02] El Arranque dura unos 5 meses en la noche y el programa completo cerca de 14 meses. El plan de cuotas exacto se define en la asesoría… ¿Me confirmas si la decisión la tomas tú o la consultas con alguien más?
[Lead 15:03] No estoy afiliado a caja san, la desicion la tomo yo. Catorce meses A1 y A2
[Agente 15:03] Yasmin los 14 meses son para el programa completo hasta B2. El Arranque A1+A2 dura solo 5 meses en la noche. ¿Te queda bien si las clases empiezan hoy 5 de octubre en las dos jornadas?   ← fecha
[Lead 15:05] Cuántos días ala semana
[Agente 15:06] Son 5 días a la semana de lunes a viernes. Tengo videollamada mañana a las 3:30 pm, o si prefieres en la sede tengo a las 4:00 pm o una llamada a las 4:15 pm. ¿Cuál te queda mejor? 🗓️   ← franjas 3
[Lead 15:08] Me quedaría muy alto los pagos con mensualidad de 589mil no alcanzo, agradezco mucho su atención   ← cálculo propio; nadie lo corrige
[Agente 15:09] Sin problema. Si más adelante retomas la búsqueda aquí estaré. Que estés muy bien.   ← cierre sin rescate"""),
 ('5. CLAUDIA — 06/10 · REACTIVACIÓN · trabajo · nivel B2 con prueba hecha · noche · pide PERSONALIZADO · decide ella',
  'Se perdió en: ignora "ya realicé la prueba" y manda el EF SET; jornada dos veces; a una B2 le recita el programa A1-B2 y el Arranque; pide el correo en vez de franja; "¿las clases empiezan el 5 de octubre?" (hoy 6); "pasamos a agendar" sin dar hora. Perfil de personalizado ejecutivo perdido.',
  """[Agente 06/10 08:34] Hola Claudia, soy Louissiana… Hace unas semanas nos escribiste por el inglés y queremos retomar. ¿Sigue siendo una meta para ti?…
[Lead 08:52] Buen día / Si señora, estoy revisando para iniciar mis estudios
[Agente 08:52] Qué bueno Claudia ¿qué te gustaría estudiar o en qué área buscas especializarte con el inglés?
[Lead 08:53] Si por trabajo
[Agente 08:53] Imagínate en esa próxima reunión… ¿El curso es para ti o para alguien más?
[Lead 08:53] Para mi
[Agente 08:54] …¿hoy qué tanto inglés tienes?
[Lead 08:54] Empiezo B2 / Ya realice la prueba
[Agente 08:54] Para ubicarte mejor en ese nivel antes de la cita haces la prueba internacional gratuita en efset.org/ef-set-50…   ← no escuchó "ya hice la prueba"
[Agente 08:55] Listo Claudia. ¿Qué jornada te queda mejor para estudiar…?   ← jornada repetida
[Lead 08:59] Noche
[Agente 08:59] …El programa completo de A1 a B2 tiene 575 horas… el valor de $8.696.000 baja bastante en la asesoría. El Arranque A1+A2 está en $2.990.000 COP. Para dejar tu registro al día ¿me compartes tu correo?   ← programa A1-B2 y Arranque a una B2; pide correo, no franja
[Lead 09:03] Yo lo haría personalizado
[Agente 09:04] Manejamos paquetes desde 30 horas con el horario totalmente a tu medida y el valor exacto lo cotizamos en la asesoría. ¿La decisión de iniciar la tomas tú o la consultas con alguien más?   ← debió ofrecer franja con dirección
[Lead 09:25] Yo
[Agente 09:27] Perfecto Claudia. ¿Te queda bien si las clases empiezan el 5 de octubre en las dos jornadas? Pasamos a agendar tu asesoría para que asegures tu cupo.   ← fecha vencida; "agendar" sin hora
[Lead 09:28] Por ahora no / Yo te confirmo
[Agente] Dale Claudia. Quedo pendiente de tu mensaje cuando quieras retomar. Que estés muy bien.   ← cierre sin rescate"""),
 ('6. JERSON — 06/10 · REACTIVACIÓN · profesional en sistemas · básico · preguntó presencial/virtual · "necesito consultar" · ABIERTA',
  'Riesgos: pide el correo antes de la jornada y de la cita; nunca obtiene la jornada; "la cohorte que inicia este 5 de octubre"; ofrece Asesoría Personalizada EN LA SEDE (mañana 11:00 o jueves 9:00) y no hay asesora en la sede; franjas de mañana a alguien que trabaja y preguntó por virtual.',
  """[Agente 06/10 08:28] Hola Jerson, soy Louissiana… Hace unas semanas nos escribiste por el inglés y queremos retomar…
[Lead 08:30] Hola, si señora, cuentame cuales son tus planes, horarios y valores, gracias
[Agente 08:31] Jerson claro te comparto todo. Para darte el plan y el valor exacto necesito saber primero tu meta… ¿Qué proyecto específico tienes en mente con el inglés?
[Lead 08:33] Es para complementar mi perfil ya que pues soy profesional en sistemas, quiero también dominar el ingles
[Agente 08:33] Para alguien en sistemas el inglés no es un lujo… ¿El curso sería para ti o para alguien más?
[Lead 08:33] Solo para mi
[Agente 08:34] …¿hoy qué tanto inglés tienes?
[Lead 08:39] Basico, lo que enseñan en la universidad
[Agente 08:39] Listo con ese nivel podemos avanzar rápido… Para dejar tu registro al día ¿me compartes tu correo? 📈   ← correo antes de jornada y cita
[Lead 09:00] jerson0493@gmail.com
[Agente 09:01] Gracias ya actualizo tu correo… ¿qué jornada te queda mejor…?
[Lead 09:02] Son presenciales o virtuales ?
[Agente 09:03] Somos 100% presenciales en nuestra sede de Sotomayor… ¿qué jornada te queda mejor…?
[Agente 09:36] Jerson, para cuando revisemos los detalles del programa en tu Asesoría Personalizada, ¿la decisión de iniciar la tomas tú solo o la consultas con alguien más?   ← salta sin jornada
[Lead 09:39] Necesito consultar
[Agente 09:39] Entiendo perfectamente. Es mejor que las personas que deciden escuchen la información juntas… nuestro curso completo va de A1 a B2… el Arranque A1+A2… precio de lanzamiento de $2.990.000 COP para la cohorte que inicia este 5 de octubre. ¿Te queda bien si las clases empiezan el 5 de octubre en las dos jornadas?   ← precio sin pedirlo + fecha vencida
[Agente 09:39] Jerson, para que tú y la persona con quien vas a consultar tengan su Asesoría Personalizada en la sede, ¿les queda mejor venir mañana a las 11:00 am o el jueves a las 9:00 am?   ← EN LA SEDE, sin asesora; franjas de mañana"""), ('7. ALEXANDRA — 06/10 · REACTIVACIÓN · viaje · ella + hijo de 15 · solo pueden entre semana en la TARDE · Comfenalco',
  'Se perdió en: ráfaga de cinco mensajes en dos minutos; precio de lista y, al "ese valor x2 se sale de mi presupuesto", responde "aplicarían los valores estándar"; "¿las clases empiezan el 5 de octubre?"; y al final cierra una puerta que no existe: "tu hijo no podría estudiar en ese horario", cuando la academia tiene salones libres en la tarde. Eran dos matrículas.',
  """[Agente 06/10 08:22] Hola Alexandra, soy Louissiana… Hace unas semanas nos escribiste por el inglés y queremos retomar…
[Lead 08:22] (respuesta automática de fuera de oficina con firma: Guía Profesional de Turismo…)
[Agente 08:23] Listo Alexandra Martínez Arias ya registro tu correo… ¿tu enfoque con el inglés es para el área de turismo o para otra meta?
[Lead 08:26] Para viajar
[Agente 08:26] Qué bien Alexandra. Imagínate llegando al aeropuerto… ¿El curso es para ti o para alguien más?
[Lead 08:59] Para mi y para mí hijo / De 15 años
[Agente 08:59] Qué buen plan hacerlo en familia. ¿Qué edad tiene tu hijo?   ← ya lo había dicho
[Agente 09:00] Súper. Como tu hijo tiene 15 años aplicaría para la modalidad sabatina. Respecto a ti ¿hoy qué tanto inglés tienes?…
[Lead 09:00] Tengo varias inquietudes / 1.- cuánto dura / 2.- cuál es el horario / 3.- es virtual o es presencial / Nosotros iniciamos desde lo básico / Cuanto es el valor
[Agente 09:00-09:02] (CINCO mensajes seguidos: dudas; duración; "programa ideal es el completo… Arranque $2.990.000… ¿ustedes toman las decisiones?"; jornadas; presencial)   ← ráfaga
[Agente 09:02] El programa completo A1 a B2 cuesta $8.696.000 COP con una beca del fondo… El Arranque A1+A2 está en $2.990.000 COP. ¿Eres afiliada a Cajasan?   ← precio de lista sin pedirlo
[Lead 09:02] No podemos en la mañana. Mi hijo sale del colegio a la 1:30 p.m
[Agente 09:03] Para tu hijo lo ideal es el programa de los sábados de 8:00 a 12:00… Para ti la jornada de la noche… ¿tú tomas la decisión sola…? 📈
[Lead 09:03] No. A comfenalco / Ese valor X2. Se sale de mi presupuesto
[Agente 09:03] Entiendo. En ese caso aplicarían los valores estándar que te comenté. ¿Tú misma tomas la decisión…?   ← familia de dos: debió pasar a humano
[Agente 09:03] Es una inversión importante para la familia Alexandra. Mira que el Arranque sale a menos de $15.000 la hora…
[Agente 09:04] Te entiendo perfectamente. Justamente en la asesoría evaluamos el perfil de ambos… ¿Te queda bien si las clases empiezan el 5 de octubre en las dos jornadas?   ← fecha vencida; sin franja de cita
[Lead 09:04] Muchas gracias por la información / Definitivamente desisto / No vamos a tomar el programa
[Agente 09:05] Sin problema Alexandra. Si más adelante retoman la búsqueda aquí estaremos…   ← cierre sin rescate
[Lead 09:06] El horario tampoco me favorece porque la idea es que mi hijo y yo quedemos en el mismo horario; el sábado en la mañana mi hijo tiene natación y en la tarde scout; solo tendríamos disponibles entre semana en la tarde
[Agente] Te hablo de frente Alexandra para menores de 17 años solo manejamos la modalidad de los sábados… tu hijo no podría estudiar en ese horario. Si más adelante se les libera el sábado me avisas…   ← puerta cerrada que no existe: hay salones en la tarde"""),
]
for tit, diag, texto in convs:
    h(d, tit, 11.5)
    para(d, diag, color=ROJO, size=9.5)
    for line in texto.split('\n'):
        p = d.add_paragraph(); p.paragraph_format.space_after = Pt(1)
        if '←' in line:
            a, b = line.split('←', 1); r = p.add_run(a); r.font.size = Pt(9); r2 = p.add_run('← ' + b.strip()); r2.font.size = Pt(9); r2.bold = True; r2.font.color.rgb = ROJO
        else:
            r = p.add_run(line); r.font.size = Pt(9)
            if line.startswith('[Lead'): r.bold = True

out1 = BASE + r'\AUDITORIA_AGENTE_CONVERSACIONES_2026-10-06.docx'
try: d.save(out1); print('OK', out1)
except PermissionError: print('ABIERTO, no regenerado:', out1)

# ------------------------------------------------------------------ DOC 2: rescates de hoy
d = newdoc()
h(d, 'RESCATES — para enviar el martes 7/10 en la mañana (13 leads)', 14)
para(d, 'Trece leads que el agente dejó ir entre el 3 y el 6 de octubre. Orden: primero los seis con teléfono (Ivonne, Vanessa, Leine, Isa, Richard, Nathaly), que son los más calientes; después los siete del fin de semana, cuyo número se toma del encabezado de la conversación en LaHaus. Franjas escritas para enviar el martes 7 en la mañana; si se envían otro día, ajustar "hoy/mañana". PASO 0 EN CADA RESCATE: antes de escribir, PAUSAR EL AGENTE en esa conversación en la plataforma (botón del agente de IA); si no, el agente sigue preguntando mientras la asesora propone la cita. BARRIDOS: a las 12 y a las 6, abrir primero el filtro de "contacto humano" de la plataforma (ahí quedan los que pidieron asesor y nadie ve) y luego revisar conversaciones cerradas o sin respuesta en 24 h con precio, cuotas, "por ahora no", "gracias" o "lo pienso"; un solo mensaje (pregunta + cuotas + dos franjas) y anotar quién, cuándo y qué respondió. Todos siguen calientes. Los teléfonos están en el encabezado de cada conversación en LaHaus. Regla: un solo mensaje, una sola propuesta (Fondo + cuotas + cita por videollamada o llamada), dos franjas. Si no responde en 2 horas, llamada. Nada presencial: no hay asesora en la sede.', color=GRIS, size=9.5, after=10)
resc = [
 ('MARÍA EUGENIA — Yarhi · Tel: ______________ (tomar de LaHaus) · trabajo y viajes, básico, noche', 'Hola Yarhi, soy María Eugenia de Heiiu. Vi que la noche te sirve y que buscas el inglés para trabajo y viajes. El valor que te dio la asistente es el de lista; con tu perfil hay beca del Fondo y plan de cuotas con inicial y mensualidades. ¿Te muestro el plan real en 20 minutos por videollamada hoy a las 6:00 pm o mañana a las 10:00 am?'),
 ('MARÍA EUGENIA — Adriana · Tel: ______________ (tomar de LaHaus) · mamá; hija de 18 que ya habla inglés', 'Hola Adriana, soy María Eugenia de Heiiu. Como tu hija ya tiene inglés, no le sirve empezar desde cero: le mando la prueba de nivel gratuita en línea y con el resultado les propongo un plan B1 a B2 con beca del Fondo según perfil y cuotas, para que presupuesten con el número real y no con el de lista. ¿Les queda bien una videollamada hoy a las 6:30 pm o mañana a las 11:00 am? Pueden entrar tú, tu esposo y ella.'),
 ('MARÍA EUGENIA — Gema · Tel: ______________ (tomar de LaHaus) · TOEFL B2, tiene B1, noche, Comfenalco', 'Hola Gema, soy María Eugenia de Heiiu. Para tu meta de TOEFL B2 el camino no es el Arranque: es un plan B1 a B2 en la noche. Te mando la prueba de nivel gratuita (efset.org/ef-set-50) y con tu resultado armamos el plan y la beca del Fondo según tu perfil. ¿Videollamada hoy a las 7:00 pm o mañana a las 12:00?'),
 ('MARÍA EUGENIA — Yasmin · Tel: ______________ (tomar de LaHaus) · viaje, desde cero, noche, decide ella', 'Hola Yasmin, soy María Eugenia de Heiiu. Vi que calculaste la mensualidad en $589.000; ese no es el número: la cuota se arma con una inicial y mensualidades más bajas, y con tu perfil hay beca del Fondo. ¿Te muestro el plan real en 20 minutos por videollamada hoy a las 6:00 pm o mañana a las 10:30 am?'),
 ('MARÍA EUGENIA — Jerson Gómez · Tel: +57 317 376 1839 · sistemas, básico, "necesito consultar"; el agente le ofreció SEDE mañana 11:00 / jueves 9:00', 'Hola Jerson, soy María Eugenia de Heiiu. Como trabajas, te propongo la asesoría por videollamada para que entre también la persona con quien consultas sin desplazarse: hoy a las 6:30 pm o mañana a las 7:30 am. ¿Cuál les sirve? Te mando el enlace a este número. (Si ya eligió "mañana 11 en la sede": confirmarle que será por videollamada a esa misma hora.)'),
 ('MARÍA EUGENIA — Alexandra Martínez · Tel: ______________ (tomar de LaHaus) · viaje · ella + hijo de 15 · solo tarde entre semana', 'Hola Alexandra, soy María Eugenia de Heiiu. Leí tu conversación y te corrijo dos cosas: sí tenemos salones entre semana en la tarde y estamos abriendo grupo en esa franja, así que tú y tu hijo pueden estudiar juntos; y el valor para dos personas de la misma familia no es el de lista por dos: en la asesoría evaluamos la beca del Fondo para cada uno y un plan de cuotas conjunto. ¿Qué franja entre 1:30 y 6:00 pm les sirve a los dos? Y te propongo 20 minutos por videollamada hoy a las 6:30 o mañana a las 10 para armarles el plan.'),
 ('MARÍA EUGENIA — Isa Durango · Tel: 313 809 9965 · reactivación · noche · dijo "sí señora" a empezar y "yo iría" a la sede · nunca recibió hora confirmada', 'Hola Isa, soy María Eugenia de Heiiu. Vi que quieres empezar y que la noche te sirve. Te confirmo tu asesoría de hoy a la 1:00 pm, por videollamada para que no tengas que desplazarte (la sede la conoces el primer día de clase). Te mando el enlace a este número 10 minutos antes. Si prefieres a las 3:30, también puedo. ¿Cuál te queda mejor?'),
 ('MARÍA EUGENIA — Nathaly Nayitg · Tel: 320 397 2471 · formulario · estudiar fisioterapia afuera · desde cero · sin responder desde las 9:26 am → LLAMADA', 'Guion de llamada: "Nathaly, buenas tardes, soy María Eugenia de Heiiu, la asistente te escribió esta mañana por lo del inglés para estudiar fisioterapia afuera. Te llamo solo para dejarte agendada la asesoría virtual de 20 minutos: ¿te sirve hoy a las 10:30 o a las 3:30? Ahí te explico el programa completo y la beca según tu perfil." Si no contesta: WhatsApp con las mismas dos franjas y segunda llamada mañana miércoles a las 9.'),
 ('MARÍA EUGENIA — Leine Vargas · Tel: 301 438 8172 · reactivación · viaje · desde cero · noche · preguntó precio y mensualidad TRES veces', 'Hola Leine, soy María Eugenia de Heiiu. Vi que preguntaste la mensualidad y la asistente no te la dio; te la doy yo. La cuota se arma con una inicial y mensualidades según la beca del Fondo que te corresponda, y es bastante menos de lo que sale dividiendo el valor en meses. En 20 minutos te muestro tu número exacto para la noche: ¿hoy a las 11:00 o a las 4:30 por videollamada?'),
 ('MARÍA EUGENIA — Richard López (papá; hija de 16, estudia en las mañanas → sabatino o noche) · Tel: 316 483 7953 · preguntó "¿cuánto mensual?" → LLAMADA', 'Guion de llamada: "Richard, buenas tardes, soy María Eugenia de Heiiu. La asistente no te dio la mensualidad para tu hija y te la doy yo: puede estudiar los sábados de 8 a 12, un nivel a la vez, o en la noche de 6:30 a 8:30 entre semana; ambas con inicial y cuotas. ¿Te queda bien 20 minutos por videollamada hoy a las 10 o a las 4 para mostrarte el número exacto y dejarle el cupo?"'),
 ('MARÍA EUGENIA — Vanessa Castro · Tel: 315 705 2306 · formulario 5/10 + reactivación 6/10 (le reiniciaron el flujo) · noche · desde cero · preguntó precio y cómo se paga · WhatsApp y, si no responde en 30 min, LLAMADA', 'Hola Vanessa, soy María Eugenia de Heiiu. Vi que quieres la noche, empiezas desde cero y preguntaste cómo se paga: te lo explico yo en 20 minutos con tu plan de cuotas (inicial más mensualidades, según la beca del Fondo que te corresponda). Por videollamada, para que no te desplaces: ¿hoy a las 11:00 o a las 4:30?'),
 ('MARÍA EUGENIA — Ivonne (TRES personas: ella, esposo e hija de 25 que llega en 30 días) · Tel: 317 375 7435 · no puede los jueves · está fuera de la ciudad esta semana · dijo que iría a la sede → LLAMADA', 'Guion de llamada: "Ivonne, buenas tardes, soy María Eugenia de Heiiu. Vi que quieren estudiar los tres, que tu hija llega en un mes y que los jueves no puedes. Para que no tengan que esperar a que vuelvas a la ciudad, les propongo la asesoría por videollamada esta semana, los tres si quieren: ¿hoy a las 6:30 pm o el jueves a las 10 am? Ahí les armo el plan para los tres con la beca del Fondo de cada uno y las cuotas, y les dejo los cupos apartados para cuando llegue tu hija."'),
 ('DIANA — Claudia · Tel: ______________ (tomar de LaHaus; hay 7 Claudias en la lista de reactivación) · B2 con prueba, trabajo, noche, PERSONALIZADO, decide ella', 'Claudia, buenos días, soy Diana Gómez, directora de Heiiu. Vi que ya tienes un B2 y buscas un plan personalizado por trabajo, en la noche. Eso lo diseño yo directamente con la persona: 20 minutos para entender qué necesitas lograr y en cuánto tiempo, y te propongo el plan. ¿Hoy a las 6:30 pm o mañana a las 8:00 am?'),
]
for tit, m in resc:
    h(d, tit, 11); para(d, m, after=10)
para(d, 'Regla de esta semana: cada mañana a las 8:00, Diana revisa en LaHaus las citas del día y confirma por WhatsApp a cada lead la modalidad (videollamada o llamada) con el enlace. Ninguna cita queda "en la sede".', bold=True, size=10)
out2 = BASE + r'\RESCATES_LEADS_2026-10-06.docx'
try: d.save(out2); print('OK', out2)
except PermissionError: d.save(out2.replace('.docx','_v2.docx')); print('ABIERTO -> _v2', out2)
