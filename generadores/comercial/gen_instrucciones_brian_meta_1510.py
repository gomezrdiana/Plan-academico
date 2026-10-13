# -*- coding: utf-8 -*-
"""Instrucciones para el trafficker: estructura Meta 15-31/10/2026 basada en la investigacion del 08/10.
Salida: recursos/comercial/campañas/INSTRUCCIONES_META_TRAFFICKER_2026-10-15.docx"""
import re
from docx import Document
from docx.shared import Pt, RGBColor

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(60); s.top_margin = s.bottom_margin = Pt(50)

def h(t, size=13, before=10):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAR
def para(t, size=10.5, color=None, after=4):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        r = p.add_run(part[2:-2] if part.startswith('**') else part); r.bold = part.startswith('**'); r.font.size = Pt(size)
        if color: r.font.color.rgb = color
def tabla(rows):
    tb = d.add_table(rows=1, cols=len(rows[0])); tb.style = 'Table Grid'
    for j, t in enumerate(rows[0]):
        r = tb.rows[0].cells[j].paragraphs[0].add_run(t); r.bold = True; r.font.size = Pt(9)
    for fila in rows[1:]:
        cells = tb.add_row().cells
        for j, v in enumerate(fila):
            r = cells[j].paragraphs[0].add_run(v); r.font.size = Pt(9); r.bold = (j == 0)
    d.add_paragraph().paragraph_format.space_after = Pt(2)

p = d.add_paragraph(); r = p.add_run('META ADS — ESTRUCTURA 15 AL 31 DE OCTUBRE 2026'); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = NAR
para('Para el trafficker. Basado en documentación oficial de Meta y evidencia publicada (investigación interna 08/10/2026). Presupuesto total: $70.000/día. Objetivo del periodo: saber cuál de los 8 videos nuevos trae citas más baratas, y dejar de perder leads de formulario que no contestan.', color=GRIS, size=9.5, after=8)

h('1. Campañas (tres, no más)')
tabla([
 ['Campaña', 'Objetivo y destino', 'Conjunto (uno solo)', '$/día', 'Anuncios'],
 ['HEIIU_CTWA_BGA_1510', 'Clientes potenciales → Apps de mensajería → WhatsApp. Meta de rendimiento: "Clientes potenciales" si aparece en la cuenta; si no, "Conversaciones". NUNCA Tráfico.', 'CTWA_BGA_ADV: Bucaramanga + radio que cubra el área metropolitana (Floridablanca, Girón, Piedecuesta), 18-45, Advantage+ audiencia, Advantage+ ubicaciones.', '$45.000 (hasta el 21/10 puede subir a $55.000 tomando del control)', 'Los 8 videos, UN anuncio por video. Nombres: V1_VIDEODEHOY, V2_CLASE, V3_575H, V4_VACANTE, V5_PASAPORTE, V6_GARANTIA, V7_NOESFACIL, V8_PADRES.'],
 ['HEIIU_FORM_CONTROL_1510', 'Clientes potenciales → Formulario instantáneo tipo "MAYOR INTENCIÓN" (no "más volumen").', 'Misma segmentación.', '$15.000', 'Los 2-3 videos que mejor gancho tengan del 15 al 18/10.'],
 ['HEIIU_RTG_GARANTIA_2210', 'Clientes potenciales → WhatsApp.', 'Audiencia: vieron el 50% de cualquier video (30 días) + interactuaron con IG/FB (30 días). Excluir lista de inscritos y de citas agendadas. Solo si la audiencia pasa de ~1.000 personas.', '$10.000 desde el 22/10', 'V6_GARANTIA y V7_NOESFACIL.'],
])
para('Por qué un solo conjunto con 8 anuncios y no un conjunto por video: Meta necesita ~50 eventos de optimización por semana por conjunto para salir de la fase de aprendizaje; con este presupuesto, ocho conjuntos no aprenden nunca. La lectura por video se hace a nivel de anuncio (desglose por anuncio) y con el código del mensaje prellenado.', size=9.5, color=GRIS)

h('2. Cada anuncio de WhatsApp lleva su mensaje prellenado con código')
para('El mensaje que el lead envía al tocar el botón es distinto por anuncio y lleva el código entre paréntesis. Es la única forma de saber qué video trajo cada cita sin desarrollador. Ejemplos:')
for t in ['V1_VIDEODEHOY → "Hola, vi el video del antes y después (V1). Quiero saber más."',
          'V3_575H → "Hola, vi el video de los 7 meses (V3). ¿Qué jornada me sirve?"',
          'V5_PASAPORTE → "Hola, quiero prepararme en inglés para Au Pair / irme (V5)."',
          'V6_GARANTIA → "Hola, vi el video de la garantía (V6). ¿Me muestran el contrato?"']:
    para('• ' + t, after=2)
para('Nada de precio ni de "quiero información" en el prellenado: el agente necesita un motivo para arrancar la conversación.', size=9.5, color=GRIS)
h('2-bis. Los 9 anuncios: código, archivo y mensaje prellenado (tabla completa)')
tabla([
 ['Código (nombre del anuncio)', 'Guion', 'Archivo 30 s', 'Mensaje prellenado del botón de WhatsApp'],
 ['V1_VIDEODEHOY', 'Llegué Sin Una Palabra', 'V1_VIDEODEHOY_A_30s.mp4', 'Hola, vi el video del antes y después (V1). Quiero saber más.'],
 ['V2_CLASE', 'Esto Es Una Clase', 'V2_CLASE_30s.mp4', 'Hola, vi el video de la clase (V2). Quiero ver una por dentro.'],
 ['V3_575H', 'Siete Meses', 'V3_575H_30s.mp4', 'Hola, vi el video de los 7 meses (V3). ¿Qué jornada me sirve?'],
 ['V4_VACANTE', 'La Vacante', 'V4_VACANTE_30s.mp4', 'Hola, vi el video de la vacante (V4). Necesito el inglés para el trabajo.'],
 ['V5_PASAPORTE', 'El Pasaporte', 'V5_PASAPORTE_30s.mp4', 'Hola, quiero prepararme en inglés para Au Pair / irme (V5).'],
 ['V6_GARANTIA', 'Te Acompañamos (Y Te Lo Firmamos)', 'V6_GARANTIA_30s.mp4', 'Hola, vi el video del acompañamiento (V6). ¿Me muestran la garantía?'],
 ['V7_NOESFACIL', 'El Pacto', 'V7_NOESFACIL_30s.mp4', 'Hola, vi el video de lo que no prometen (V7). Voy en serio.'],
 ['V8_PADRES', 'El Año Después Del Colegio', 'V8_PADRES_30s.mp4', 'Hola, vi el video del año después del colegio (V8). Es para mi hijo/a.'],
 ['V9_CORRECCION', 'La Corrección Del Día', 'V9_CORRECCION_30s.mp4', 'Hola, vi la corrección del día (V9). Aquí va mi audio.'],
])
para('Recibidos a 13/10: V1 (A), V3 y V4 (y V6, que se regraba por un cambio de palabra). El resto llega el miércoles 14. Si el jueves no están los 9, se lanza con los que haya y los que falten entran en el corte del 22/10.', 9.5, GRIS)

h('3. Formularios actuales')
for t in ['• "Au Pair" ya quedó pausada el 08/10 (dato: de 7 citas por LaHaus, 4 vinieron de Curso Inglés, 2 de base de datos y 1 de Au Pair). "Curso Inglés" sigue al aire hasta que la campaña de WhatsApp esté activa el 15/10; ese día se pausa y la reemplaza el control con formulario "mayor intención".',
          '• El control nuevo (HEIIU_FORM_CONTROL_1510) se crea con tipo "MAYOR INTENCIÓN" (pantalla de confirmación de datos). Activar verificación del teléfono por SMS si está disponible en Colombia. Teléfono SIN autorrelleno.',
          '• Pantalla de introducción: "Te escribirá nuestro asistente por WhatsApp en menos de 5 minutos. Responde para agendar tu videollamada de 20 minutos."',
          '• Preguntas (máximo 6, todas de opción múltiple PERSONALIZADAS, no las autollenadas de Meta): ¿Para qué necesitas el inglés? (trabajo / irme del país / estudio / mi hijo) · ¿Para cuándo quieres empezar? (este mes / en 1-2 meses / solo averiguando) · ¿Puedes asistir presencial en Bucaramanga? (sí / no) · ¿Estás dispuesto(a) a grabar un video corto en inglés todos los días como parte del entrenamiento? (sí, me le mido / prefiero algo más suave) · ¿Cómo prefieres invertir en tu formación? (de contado / inicial y cuotas / solo si es gratis) · Nombre y WhatsApp (el teléfono SIN autorrelleno).',
          '• Las dos preguntas nuevas (video diario y forma de pago) son las mismas que hace el asistente de WhatsApp; sirven para que la asesora priorice: "me le mido" + "contado / cuotas" = llamada en 5 minutos; "más suave" o "solo si es gratis" = no se agenda (se le responde con cortesía).',
          '• Pantalla final con el botón "Chatear en WhatsApp" (función nueva de Meta): el lead llega ya escribiendo.']:
    para(t, after=2)

h('4. Au Pair')
for t in ['• La campaña separada de Au Pair ya está pausada (08/10): a $20.000/día no salía de aprendizaje, 1 cita en 8 días y 3 de cada 5 leads creían que era una agencia de empleo. Esos $20.000/día quedan reservados para el 15/10.',
          '• Vuelve como UN anuncio (V5_PASAPORTE) dentro del conjunto de WhatsApp. Primera línea del texto del anuncio: "No somos agencia: te preparamos en inglés para la entrevista de Au Pair o de trabajo en el exterior. El trámite lo haces con la agencia que elijas."',
          '• Prohibido por política de Meta (resultados irreales): prometer empleo, visa, familia anfitriona o salario. Solo preparación.',
          '• La categoría especial "Empleo" no es obligatoria para audiencia en Colombia; no marcarla.']:
    para(t, after=2)

h('5. Reglas de los videos (política de Meta y nuestras)')
for t in ['• 9:16, audio y texto dentro de la zona segura de Reels (Meta reporta 34,5% menos costo por resultado que imágenes en Reels).',
          '• "7 meses / 575 horas" se dice como descripción del programa. NUNCA "garantizado que hablas en 7 meses". La garantía siempre "por escrito, con condiciones".',
          '• Nunca atribuir carencias a la persona en el texto ("¿No sabes inglés?", "¿Te congelas?"): política de atributos personales + ya no funcionó.',
          '• Sin precio, sin "descuento/gratis/fácil", sin "profesores nativos", sin nombre del programa.']:
    para(t, after=2)

h('6. Medición y cortes')
for t in ['• Hoja diaria (coordinación comercial): fecha · código V# · conversación sí/no · cita agendada · cita atendida. Costo por cita de un video = gasto de ese anuncio (desglose por anuncio) ÷ citas con su código.',
          '• Lectura temprana de creativos (tienen más volumen que las citas): tasa de gancho = reproducciones de 3 s ÷ impresiones · reproducciones completas (ThruPlay) · CTR · costo por conversación iniciada.',
          '• Primer corte: 22/10. Cierre: 31/10. No se apaga un video antes del 22 y no se declara ganador ninguno con menos de 5 citas.',
          '• No editar el conjunto a diario (cada edición reinicia el aprendizaje). Cambios solo en los cortes.',
          '• Preguntar a LaHaus por escrito: (a) ¿guardan el identificador del anuncio (ctwa_clid / source_id) que llega en el primer mensaje? (b) ¿envían a Meta el evento de "cliente potencial" por la API de conversiones de mensajería? Si (a) es sí, pueden exportar las citas con el anuncio de origen y el código sobra.']:
    para(t, after=2)

h('7. Qué hacer con el lead que no contesta (evidencia: HBR 2011, MIT 2007)')
for t in ['• Contactar en la primera hora da 7 veces más probabilidad de calificar que una hora después, y 60 veces más que al día siguiente. Llamar en 5 minutos frente a 30 multiplica por 100 el contacto.',
          '• Minuto 0-1: mensaje del agente. Antes de 5 minutos: LLAMADA humana (si el agente llama, que llame primero; si no, la asesora). Si no contesta, nota de voz de 15 segundos.',
          '• Días 1-7: hasta 6 intentos alternando llamada y WhatsApp en horarios distintos. Texto con contenido solo después de haber hablado.',
          '• Día 7: mensaje de cierre y pasa a la lista de retargeting.',
          '• Indicador semanal: minutos hasta el primer contacto (meta ≤ 5) y % de contacto por fuente (formulario vs. WhatsApp).']:
    para(t, after=2)

h('8. Lo que NO se hace')
for t in ['Objetivo Tráfico para WhatsApp · un conjunto por video · formulario "más volumen" con autorrelleno · prometer empleo/visa/"garantizado en X meses" · retargeting con menos de ~1.000 personas · comparar costo por lead con benchmarks de EE. UU. o de blogs sin muestra (el nuestro es ~$10.800 por lead de formulario) · declarar ganador con menos de 5 citas · videos con avatares de IA (sin evidencia y contra la prueba real).']:
    para(t, after=2)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\campañas\INSTRUCCIONES_META_TRAFFICKER_2026-10-15.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
