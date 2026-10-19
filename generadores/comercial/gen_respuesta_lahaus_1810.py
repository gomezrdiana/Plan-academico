# -*- coding: utf-8 -*-
"""Respuesta a LaHaus 18/10/2026 al informe "Respuestas y ajustes a tus solicitudes del 13 de octubre" (15 págs) y al
folleto de reintentos. Un solo mensaje + notas internas de qué llenar antes de enviar.
Salida: recursos/comercial/plataforma LaHaus/RESPUESTA_LAHAUS_2026-10-18.docx"""
from docx import Document
from docx.shared import Pt, RGBColor

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(54)

def p(t, bold=False, color=None, size=10.5):
    x = d.add_paragraph(); r = x.add_run(t); r.bold = bool(bold); r.font.size = Pt(size); x.paragraph_format.space_after = Pt(4)
    if color is not None: r.font.color.rgb = color

p('RESPUESTA A LAHAUS — 18/10/2026', True, NAR, 14)
p('Responde al informe "Respuestas y ajustes a tus solicitudes del 13 de octubre" y al folleto del nuevo sistema de reintentos. Enviar como un solo mensaje por el grupo de WhatsApp o por correo.', False, GRIS, 9.5)
p('Decisiones de gerencia 19/10 ya incorporadas: edad (sábados desde 12, entre semana desde 17, excepción solo en la asesoría), tarde (solo en la cita), campaña 13/10 apagada y nueva del 19/10 activa, casos sin número buscados por frase y hora.', True, GRIS, 9.5)

MSG = """Hola Jaider, gracias por el informe del 13: está claro y se nota el trabajo. Confirmo lo aplicado y respondo lo que nos pediste, en el mismo orden, más cuatro puntos nuevos.

1. SALUDO (sección 01). No cambiamos el saludo. Se mantiene el vigente: "Hola, gracias por escribirnos. Soy el asistente de Heiiu. Para orientarte bien, ¿para qué necesitas el inglés?" Razones: una sola pregunta, la motivación primero y sin superlativos (no decimos "la mejor metodología" de nada). Con esto, por favor actualicen también la confirmación de cita: solo menciona el enlace cuando la cita es por videollamada.

2. SALUDOS POR FLUJO (sección 07). Hoy hay un solo flujo activo:
   a) Clic a WhatsApp: la campaña nueva que entró el 19 de octubre (reemplaza a la del 15, que quedó pausada). Los videos entran con un mensaje prellenado que trae el código del video entre paréntesis (V1, V3, V4). Saludo: "Hola, gracias por escribirnos por el video. Soy el asistente de Heiiu. Para orientarte bien, ¿para qué necesitas el inglés?" Si el prellenado ya trae el motivo (por ejemplo V4: "Necesito el inglés para..."), el agente omite el paso 1, pide el nombre y sigue con el paso 2.
   b) Formulario: por ahora no hay campañas de formulario activas. Cuando volvamos a prender una, el saludo será: "Hola, [nombre]. Gracias por dejarnos tus datos. Soy el asistente de Heiiu. Vi que el inglés es para [motivo del formulario]; para orientarte bien, ¿es para ti o para alguien más?" Les avisamos antes de activarla.
   c) Reactivación: sin saludo nuevo; no habrá reactivaciones hasta nuevo aviso.
   Campañas pausadas: Au Pair 25/08, Curso Inglés 30/09, Curso Inglés 13/10, el formulario de control 1510 y la de clic a WhatsApp del 15/10. En ningún saludo aparece "Arranque de octubre" ni el nombre de un programa.

3. FILTROS DE AGENDA (sección 03). No pedimos cambios: con Modalidad (llamada, virtual, presencial) y Estado nos basta. Solo confirmen que el mensaje al lead dice "por llamada de WhatsApp a este mismo número" o, si es video, trae el enlace.

4. CASOS (sección 08). Jerson (317 376 1839) y Henry (318 561 8222) ya los tienen; esperamos la respuesta el miércoles 21. De los otros dos no tenemos el número, pero ustedes tienen todas las conversaciones del 7 de octubre y se pueden buscar por frase y hora:
   • El lead que escribió "quiero reforzar lo que ya sé" el 7/10, y el agente le repitió la pregunta de nivel.
   • La conversación del 7/10 a las 12:34 pm en la que nuestra asesora escribió "déjame que la asesora te escriba hoy" y el agente siguió escribiendo después.
   Si no aparecen con esos datos, nos dicen y los buscamos conversación por conversación.

5. HORARIO LEGAL (sección 12). No hemos detectado contactos fuera de horario. Si vemos uno, enviamos el número ese mismo día.

Puntos nuevos:

6. EDAD Y JORNADAS (pasos 2 y 4 del flujo). Dos precisiones de configuración:
   • Paso 2: se mantiene "sábados desde 12 años; entre semana desde 17". Pero si un padre pide entre semana para un hijo de 12 a 16, el agente no dice que no: responde "es una opción que se revisa con el acudiente en la asesoría" y agenda. Menores de 12: no se agenda.
   • Paso 4: el agente sigue ofreciendo solo mañana (8:00 a 12:00) y noche (6:30 a 8:30 p. m.). Si el lead dice que solo puede en la tarde, no se descalifica: "eso lo revisas con la asesora en la cita" y agenda igual. La tarde no se ofrece como opción por iniciativa del agente.

7. REGLA DE ANTICIPACIÓN PARA AGENDAR (punto 16 del informe del 9/10). Sí queremos cambiarla: de 24 horas a 4 horas, dentro del horario de atención. Con 24 horas perdemos al que quiere la asesoría mañana temprano.

8. AUDIO Y CADENCIA. El paso de audio se mantiene hasta el corte del 31 de octubre; ahí lo evaluamos con datos, no antes. Para la revisión de cadencia del 30 de octubre nuestra propuesta sigue siendo día 0, 1, 3 y 7, repitiendo la misma pregunta pendiente, y los disparadores de aviso a la asesora que sí sean posibles. Propongo esa revisión el viernes 30 a las 10:00 a. m.

9. REPORTES. Tres cosas:
   a) Una demostración de SAMI de 15 minutos esta semana, para que saquemos nosotros mismos el informe por fuente y por número de toque.
   b) Mientras tanto, por favor envíen el informe del 1 al 17 de octubre: cuántos escribieron, agendaron, asistieron y quedaron en rescate, separados por fuente (formulario, clic a WhatsApp, reactivación).
   c) ¿Están llegando conversaciones de la campaña "CM_Campaña Interacción_10/10/26"? Meta reporta 84 conversaciones iniciadas desde el 10/10 y necesitamos saber si caen en el agente o en otra bandeja.

Gracias. Si les sirve, la reunión de seguimiento la hacemos el jueves 22 a las 10:00 a. m., ya con la respuesta de los casos del 21.

Diana Gómez
Gerente General, Heiiu English Academy"""
for line in MSG.split('\n'):
    p(line, size=10.5)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus\RESPUESTA_LAHAUS_2026-10-18.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
