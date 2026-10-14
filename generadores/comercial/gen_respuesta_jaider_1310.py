# -*- coding: utf-8 -*-
"""Respuesta a Jaider (LaHaus) 13/10/2026 v2: flujo de perfilación con precalificación (El Pacto + forma de pago),
precio solo cuando lo piden, despedidas, puntaje 0-10 y preguntas nuevas. Base: INVESTIGACION_PRECALIFICACION_LEADS_2026-10-13.md §6.
Salida: recursos/comercial/plataforma LaHaus/RESPUESTA_JAIDER_2026-10-13.docx"""
from docx import Document
from docx.shared import Pt, RGBColor

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(54)

def p(t, bold=False, color=None, size=10.5):
    x = d.add_paragraph(); r = x.add_run(t); r.bold = bool(bold); r.font.size = Pt(size); x.paragraph_format.space_after = Pt(4)
    if color is not None: r.font.color.rgb = color

p('RESPUESTA A JAIDER (LAHAUS) — 13/10/2026 (v3 final, con precalificación)', True, NAR, 14)
p('Responde a: Informe de respuestas al feedback (16 puntos) + Informe de leads 29/09-08/10. Base: INVESTIGACION_PRECALIFICACION_LEADS_2026-10-13.md §6. Enviar como un solo mensaje.', False, GRIS, 9.5)

MSG = """Hola Jaider, gracias por los dos informes; están muy claros. Te respondo lo pendiente de nuestro lado y te dejo preguntas nuevas.

1. FLUJO DE PERFILACIÓN Y PRECIOS (punto 1). Decidido: el paso "programa y precio" se reemplaza por dos pasos de calificación, y la cita va al final. El flujo queda así (una pregunta por mensaje; si ya respondió, se salta):
   1) MOTIVO (saludo vigente): "Hola, gracias por escribirnos. Soy el asistente de Heiiu. Para orientarte bien, ¿para qué necesitas el inglés?"
   2) PARA QUIÉN: "¿El curso es para ti o para alguien más?" (si es para otro adulto: lo ideal es que esa persona hable directamente o venga a la asesoría).
   3) NIVEL + EXPERIENCIA: "¿Hoy qué tanto inglés tienes? ¿Empiezas desde cero o ya estudiaste antes?" Si ya estudió: "¿Y qué pasó esa vez? ¿Por qué lo dejaste?"
   4) PRESENCIAL + JORNADA: "Las clases son presenciales en Bucaramanga. ¿Qué jornada te queda mejor: mañana de 8:00 a 12:00 o noche de 6:30 a 8:30 PM?"
   5) EL PACTO (nuevo): "Antes de agendarte te cuento cómo es, para que decidas con todo claro. Nuestro objetivo es que salgas hablando inglés; si no se logra, algo está mal: o tú dejaste de entrenar, o nosotros no estamos cumpliendo. Esto es un entrenamiento en equipo, como un gimnasio o aprender a nadar: desde el primer día hablas, tu profesor identifica dónde puedes mejorar y lo repetimos hasta que sale. Por eso grabas un video corto todos los días, y tu profesor te lo devuelve con una mejora. A cambio, la garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel. ¿Te le mides a ese ritmo?" Si duda ("¿todos los días?"): "Son unos minutos al día, y tu profesor te responde cada uno. Es la parte que más te hace avanzar. ¿Te le mides?"
   6) FORMA DE PAGO (nuevo): "Para que la asesora te lleve el plan que te sirve: ¿cómo prefieres invertir: de contado (sirven cesantías, tarjeta o crédito de tu banco) o con una inicial y cuotas mensuales?" Si dice cuotas: "Los planes arrancan con una inicial del 20% y cuotas mensuales según tu beca. ¿Algo así te cabe en el presupuesto?" Si dice "algo más bajo" o "no sé si me alcanza": "Tenemos opciones más livianas: entradas con una inicial desde $600.000 y cuotas, o un nivel suelto los sábados. La asesora te muestra cuál te cuadra." (sin decir el total del Arranque; ese lo da la asesora con el plan completo)
   7) CITA + DECISOR: "Te agendo 20 a 30 minutos con la asesora para definir tu plan y tu beca: ¿[franja 1] o [franja 2]? Si alguien más decide contigo, me dices y lo incluimos." Confirmación del agente con todo: "Listo, te queda agendada: [día, hora, enlace o dirección]. Para dejarla firme, respóndeme con el día y la hora de tu asesoría." (también para las citas agendadas por voz; si no responde, la cita queda "por confirmar" y el recordatorio del día anterior se la vuelve a pedir).
   Nunca se preguntan ingresos, salario, deudas ni reportes, y no se consultan centrales. El agente no dice ningún valor de cuota.
   PRECIO: el agente no dice totales por iniciativa propia. Si el lead PREGUNTA precio, se responde a la primera, una sola vez: "Te doy la referencia: el programa completo A1 a B2 es de $8.696.000 de lista, y con la beca del Fondo (hasta el 45% según tu perfil) baja bastante. Se paga de contado o con una inicial del 20% y cuotas mensuales. Pero más que el dinero, que lo cuadramos, lo que buscamos es que estés dispuesto a entrenarte con nosotros. Tu número exacto te lo da la asesora en 20 minutos: ¿[franja 1] o [franja 2]?" Si pregunta precio por segunda vez, no se repiten cifras: "Eso depende de tu beca y de cómo quieras pagar; la asesora te lo cierra en la cita" y se ofrecen las franjas.
   DESPEDIDAS (mensaje final, sin reintentos después; el lead queda marcado "frío" y la asesora decide si lo llama):
   - "No tengo el dinero ahora" (una sola vez): "Hay opciones con inicial y cuotas, y con cesantías o crédito de tu banco. ¿Quieres que la asesora te muestre cómo puedes entrenarte con nosotros con menos esfuerzo económico?" Sí → cita (tibio). No → "Perfecto. Cuando sea tu momento, me escribes por aquí y te agendo."
   - "Solo si es gratis": "Te entiendo. Nuestros programas tienen costo, con becas y cuotas, porque incluyen profesor, garantía y certificado. Si quieres, te aviso cuando abramos becas o entradas más cortas: ¿te escribo por aquí?" (solo con su sí se guarda para campañas).
   - Rechaza el Pacto ("busco algo más suave"): "Te agradezco la sinceridad. Este programa es exigente a propósito, y prefiero decírtelo ahora a que lo descubras en la segunda semana. Si más adelante quieres entrenarte con propósito, ¡escríbenos!"
   PUNTAJE 0-10 que el agente marca en el panel (2/1/0 por criterio): presencial en la jornada · capacidad en la escalera · motivo con destino · disposición a la mentoría · quién decide. Si el lead agendó, no se le llama: queda con su confirmación y el recordatorio. El puntaje ordena a los que NO agendaron: caliente 8-10 → la alerta llega a la asesora y ella le escribe en menos de 15 minutos (en horario legal) con la llamada anunciada; tibio 5-7 → ese mismo día; frío 0-4 o con tope → no se contacta, la asesora decide si lo revisa. Necesitamos los campos presencial_ok, pago_preferido, pacto_ok, motivo_destino, decisor, audio_recibido y el puntaje con su etiqueta en la alerta, y que su definición actual de "lead caliente" se reemplace por esta.

2. SALUDOS POR CAMPAÑA (punto 7). "Au Pair" está pausada desde el 8. "Curso Inglés" como formulario se pausó el 13 y ese anuncio pasó a WhatsApp ese mismo día. Mañana 14 entran en esa campaña 3 anuncios nuevos, cada uno con un mensaje prellenado que trae un código entre paréntesis (V1, V3 y V4; los demás, V2 y V5 a V9, entran el 22). Les compartimos el enlace apenas estén montados. El saludo es uno solo, genérico, que reconoce ese mensaje y no menciona "Arranque de octubre" ni programas: el del paso 1. También desde el 14 entra un formulario nuevo (mayor intención) cuyo lead llega escribiendo por el botón de WhatsApp; mismo saludo.

3. CASOS DE LOS PUNTOS 9, 10 Y 15. Están en el panel por nombre y fecha: Henry (6/10, 8:16 pm: precios $9.560.000 y $3.150.000, que no existen), lead del 7/10 "quiero reforzar lo que ya sé" (pregunta repetida), María Eugenia (7/10, 12:34 pm: el agente siguió después de "déjame que la asesora te escriba"), Jerson (6/10: pausado 10:11, activo 10:46) y la llamada sin perfilar del punto 15. Si necesitan el número sí o sí, lo sacamos; dinos de dónde lo toman ustedes para no duplicar.

Preguntas nuevas:

4. ENTREGA DEL PRIMER MENSAJE. A los leads de pauta les llega el primer mensaje en el 80,4% de los casos, contra 91,2% en la base reactivada. ¿Cuál es la causa (plantilla, ventana de 24 horas, número no válido) y qué proponen para cerrarla esta semana?

5. IDENTIFICADOR DEL ANUNCIO. (a) ¿Guardan el identificador del anuncio (ctwa_clid / source_id) que llega en el primer mensaje? (b) ¿Envían a Meta el evento de "cliente potencial" por la API de conversiones de mensajería? Si (a) es sí, ¿pueden exportar las citas con el anuncio de origen?

6. AUDIOS. ¿El agente recibe notas de voz, las transcribe y las deja en el panel? Si sí, agregamos un paso opcional de audio de 30 segundos antes de la cita.

7. CADENCIA Y HORARIO (Ley 2300 de 2023). Mensajes y llamadas comerciales solo de lunes a viernes 7:00 a.m.-7:00 p.m. y sábados 8:00 a.m.-3:00 p.m., nunca domingos ni festivos; y no más de un contacto al día por iniciativa de la empresa. Pedimos: (a) apagar las llamadas de voz de la IA en frío (505 llamadas en el último informe dieron 2 citas y las 2 faltaron); (b) que nada salga por iniciativa del agente (reintentos, plantillas, llamadas, blasts) fuera de ese horario: fuera de horario el agente solo responde lo que el lead escriba; (c) máximo 1 contacto por iniciativa nuestra al día por lead: día 0, día 1, día 3 y día 7 (despedida y silencio); (d) recordatorios de cita a las 6:30 p.m. del día anterior y 1 hora antes solo si cae en horario legal, y quitar la anticipación mínima de 24 h para agendar; (e) aviso inmediato a la asesora con cinco disparadores: pide una persona, segunda pregunta de precio o pregunta por la mensualidad, dice "no por ahora / lo pienso", es familia o ruta ejecutiva, o se queda callado 15 minutos después de dar el motivo sin agendar; (f) el primer contacto humano será una "llamada anunciada" por la misma línea de WhatsApp ("¿te llamo ahora 5 minutos? te marco desde el 3xx…"): ¿pueden habilitar llamadas de WhatsApp desde la línea de Heiiu? La cadencia completa la está revisando nuestro abogado; esto es lo que ya no admite discusión.

8. REACTIVACIÓN (BLAST). El del 6 de octubre metió 489 leads y produjo 2 citas; un lead de pauta responde 4,2 veces más y agenda 3,7 veces más. Hasta nuevo aviso no se hacen reactivaciones sin aprobación por escrito de gerencia, y necesito que confirmen cómo se factura ese blast.

9. INFORME SEMANAL por etiqueta (caliente/tibio/frío) y por grupo A/B (último dígito del teléfono: par = solo bot, impar = bot + llamada anunciada): leads, citas, asistencia y matrícula (ese dato lo pasa la asesora). Y los envíos fallidos del primer mensaje a leads de pauta por código de error (131049, 131026) y por origen (formulario vs. clic a WhatsApp). Corte de evaluación: 31 de octubre.

Lo demás (plantillas de nombre y correo, recordatorios a 12 h y 1 h, "fecha de cohorte") quedó bien. Lo que la plataforma no permite lo compensamos con la llamada anunciada de la asesora. Revisamos números el 15 con los anuncios nuevos al aire. Gracias."""
p(MSG)

OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus\RESPUESTA_JAIDER_2026-10-13.docx'
try: d.save(OUT); print('OK')
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
