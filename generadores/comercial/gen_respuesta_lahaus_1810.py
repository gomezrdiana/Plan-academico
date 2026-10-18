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
p('ANTES DE ENVIAR, gerencia completa o confirma: (a) los dos números o apodos del punto 4; (b) la regla de edad del punto 6 (está escrita como quedó en la base del 6/10: desde 12 en cualquier jornada con acudiente); (c) si la jornada de la tarde se ofrece como "en apertura"; (d) el estado de la campaña Curso Inglés 13/10 en el punto 2.', True, GRIS, 9.5)

MSG = """Hola Jaider, gracias por el informe del 13: está claro y se nota el trabajo. Confirmo lo aplicado y respondo lo que nos pediste, en el mismo orden, más cuatro puntos nuevos.

1. SALUDO (sección 01). No cambiamos el saludo. Se mantiene el vigente: "Hola, gracias por escribirnos. Soy el asistente de Heiiu. Para orientarte bien, ¿para qué necesitas el inglés?" Razones: una sola pregunta, la motivación primero y sin superlativos (no decimos "la mejor metodología" de nada). Con esto, por favor actualicen también la confirmación de cita: solo menciona el enlace cuando la cita es por videollamada.

2. SALUDOS POR FLUJO (sección 07). Hoy hay dos flujos activos y uno pausado:
   a) Clic a WhatsApp, campaña HEIIU_CTWA_BGA_1510 (anuncios V1_VIDEODEHOY, V3_575H, V4_VACANTE). El lead llega con un mensaje prellenado que trae el código del video entre paréntesis. Saludo: "Hola, gracias por escribirnos por el video. Soy el asistente de Heiiu. Para orientarte bien, ¿para qué necesitas el inglés?" Si el prellenado ya trae el motivo (por ejemplo V4: "Necesito el inglés para..."), el agente omite el paso 1, pide el nombre y sigue con el paso 2.
   b) Formulario, campaña HEIIU_FORM_CONTROL_1510. El formulario trae el motivo (trabajo / irme del país / estudio / mi hijo). Saludo: "Hola, [nombre]. Gracias por dejarnos tus datos. Soy el asistente de Heiiu. Vi que el inglés es para [motivo del formulario]; para orientarte bien, ¿es para ti o para alguien más?" Si el motivo no se puede leer, usa el saludo del punto 1.
   c) Reactivación: sin saludo nuevo; no habrá reactivaciones hasta nuevo aviso.
   Campañas pausadas: Au Pair 25/08 y Curso Inglés 30/09. Curso Inglés 13/10: [CONFIRMAR: pausada / activa; si sigue activa usa el saludo a)]. En ningún saludo aparece "Arranque de octubre" ni el nombre de un programa.

3. FILTROS DE AGENDA (sección 03). No pedimos cambios: con Modalidad (llamada, virtual, presencial) y Estado nos basta. Solo confirmen que el mensaje al lead dice "por llamada de WhatsApp a este mismo número" o, si es video, trae el enlace.

4. CASOS (sección 08). Jerson (317 376 1839) y Henry (318 561 8222) ya los tienen; esperamos la respuesta el miércoles 21. Los otros dos:
   • Lead del 7/10 que dijo "quiero reforzar lo que ya sé": [NÚMERO O APODO DE WHATSAPP].
   • María Eugenia (7/10, 12:34 pm): [NÚMERO O APODO DE WHATSAPP].

5. HORARIO LEGAL (sección 12). No hemos detectado contactos fuera de horario. Si vemos uno, enviamos el número ese mismo día.

Puntos nuevos:

6. EDAD Y JORNADAS (pasos 2 y 4 del flujo). Dos ajustes de configuración:
   • Paso 2: la edad mínima es 12 años en cualquier jornada. De 12 a 17, el acudiente asiste a la asesoría y firma, y entre semana se exige el compromiso de trabajo diario fuera de clase. Menores de 12: no se agenda. Hoy el agente dice "entre semana desde 17", y eso no es así.
   • Paso 4: además de mañana (8:00 a 12:00) y noche (6:30 a 8:30 p. m.), existe la jornada de la tarde en apertura: si el lead solo puede en la tarde, el agente registra la franja que le sirve y agenda igual la asesoría. No se le dice que no.

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
