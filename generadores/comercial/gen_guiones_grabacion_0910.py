# -*- coding: utf-8 -*-
"""Guiones para la jornada de grabacion del 09/10/2026: venden el SERVICIO (garantia, coach, acompañamiento, fecha de llegada).
Salida: recursos/comercial/campañas/GUIONES_GRABACION_2026-10-09.docx"""
import re
from docx import Document
from docx.shared import Pt, RGBColor

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(60); s.top_margin = s.bottom_margin = Pt(50)

def h(t, size=13, before=10):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAR
def para(t, size=10.5, color=None, italic=False, after=4):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        r = p.add_run(part[2:-2] if part.startswith('**') else part); r.bold = part.startswith('**'); r.italic = italic; r.font.size = Pt(size)
        if color: r.font.color.rgb = color
def guion(num, titulo, prioridad, vende, quien, dura, escena, texto, pantalla, cta, nota=None, gancho=None, codigo=None, prellenado=None, corto=None):
    h(f'GUION {num} — {titulo}   [{prioridad}]' + (f'   · anuncio {codigo}' if codigo else ''), 12.5, 14)
    if prellenado: para(f'**Mensaje prellenado del botón de WhatsApp:** "{prellenado}"', after=2)
    if gancho: para(f'**GANCHO (segundos 0-2, lo que para el dedo):** {gancho}', after=2)
    para(f'**Qué vende:** {vende}', after=2)
    para(f'**Quién habla:** {quien}   ·   **Duración:** {dura}', after=2)
    para(f'**Qué se ve:** {escena}', after=4)
    para('**Texto (se dice tal cual, con subtítulos):**', after=1)
    for linea in texto: para('"' + linea + '"', italic=True, after=2)
    para(f'**Texto en pantalla:** {pantalla}', after=2)
    para(f'**Cierre:** {cta}', after=2)
    if corto: para('**VERSIÓN DE 15 SEGUNDOS (se corta en edición del mismo material; no se graba aparte):** ' + corto, after=2)
    if nota: para('Nota: ' + nota, size=9.5, color=GRIS)

p = d.add_paragraph(); r = p.add_run('GUIONES — JORNADA DE GRABACIÓN 09/10/2026'); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = NAR
para('Venden el SERVICIO, no el producto: garantía por escrito, profesor que entrena (mentor), acompañamiento diario, y un plan con fecha de llegada. Reglas del calendario: gancho de destino, sin precio ni nombre del programa, nunca "fácil", "rápido" ni "gratis"; caras de profes, estudiantes con cláusula de imagen y coordinación; nunca gerencia. Verticales (9:16), 20-30 segundos, subtítulos grandes. Cada guion abre con un GANCHO de 2 segundos (imagen + texto grande) que es lo que detiene el dedo; la clase, el profe o el contrato son la prueba que viene después. Cierre siempre a WhatsApp. GRUPO DISPONIBLE EL 09/10: un grupo de B1/B2 de 5 estudiantes; 3 de ellos empezaron de cero (A1) en Heiiu (no hay video de entrada de ellos; la prueba es su confesión con el dato real y su inglés de hoy): son los protagonistas de los guiones 2 y 6.', color=GRIS, size=9.5, after=8)

h('PLAN DE LA JORNADA (para grabar sin la gerente presente)', 12)
for t in ['**Fecha y lugar:** jueves 09/10/2026, sede Heiiu, el salón de clase. **Grupo:** el B1/B2 que tiene clase ese día, con su profe. **Hora:** Isaac coordina su llegada con la profe; las tomas con el salón vacío se hacen antes de la clase y las de Jacqueline después.',
          '**Quién manda en el set: LA PROFE.** Ella dirige la clase y las escenas con la HOJA DE LA PROFE (página siguiente); el que graba (Isaac) sigue esa hoja y se encarga de que se vea y se oiga bien (encuadre, audio, dos ángulos); coordinación (Jacqueline) consigue permisos y datos antes de la clase y graba sus dos piezas después. Si algo no sale como está escrito, se graba la versión más cercana y se anota; no se inventa otra escena.',
          '**Equipo:** celular o cámara en vertical (9:16, 1080x1920), micrófono de solapa o el celular a menos de 1,5 m del que habla, luz natural o del salón (sin aro de luz: se ve a anuncio). Un segundo celular para grabar la simulación desde otro ángulo.',
          '**Permisos:** todos los estudiantes tienen firmada la autorización de imagen en su contrato de matrícula. La profe les pregunta si están contentos con la clase y les pide ayuda: "parte de mi trabajo es grabar contenido"; si alguien dice voluntariamente que no quiere salir, queda fuera de plano. Coordinación le confirma a cada uno de los 3 que empezaron de cero cuántos meses lleva desde su PRIMERA CLASE (no desde la matrícula: a veces el grupo arrancó hasta dos meses después), para "hace ___ meses". Sin nombres de estudiantes en pantalla.',
          '**Orden cronológico del día:** (1) antes de la clase, con el salón vacío: guion 3 "Siete meses" (profe + tablero), guion 4 "La vacante" (profe), tomas de la fachada y la recepción; (2) durante la clase, con el grupo: guion 7 "La corrección del día" al abrir (usa el error paper real), guion 2 "Esto es una clase" (simulación de entrevista o reclamo, 10 minutos de pie), guion 5 "El pasaporte" (simulación de entrevista con familia/empleador, 10 minutos), guion 1 "Llegué sin una palabra" (cada uno de los 3 que empezó de cero: la frase en español con su dato real + 10 s en inglés); (3) después de la clase: guion 1 "Te acompañamos" (Jacqueline con el anexo de garantía impreso), guion 7 "El año después del colegio" (Jacqueline en recepción) y guion 8 "El Pacto" (profe, 5 minutos, a solas). Se graban los 9; ninguno es opcional. Total estimado: 3 horas.',
          '**Qué se entrega (al WhatsApp de gerencia, enviados como DOCUMENTO, no como video, para que WhatsApp no los comprima; tanda 1 el lunes 12/10 y tanda 2 el miércoles 14/10, ver "Qué se edita primero"):** por cada guion, dos archivos: versión completa (20-30 s) y versión de 15 s (gancho + frase fuerte + cierre). Nombre del archivo = código del anuncio + duración: V1_VIDEODEHOY_30s.mp4, V1_VIDEODEHOY_15s.mp4, etc. (los códigos están en cada guion). Formato 9:16, 1080x1920, MP4. Subtítulos grandes, palabra por palabra, dentro de la zona segura de Reels (ni en el 14% superior ni en el 35% inferior). Colores de marca: naranja #E54C09 y amarillo #FBC900 para los textos en pantalla (el amarillo nunca como texto sobre blanco). Logo de Heiiu solo en el último segundo. Sin música encima de la voz en los guiones 1, 6 y 8; en los demás, música baja o ninguna. Además, el material en bruto completo en una subcarpeta BRUTO (sirve para cortar otros ganchos sin volver a grabar).',
          '**Lo que NO se graba ni se edita (reglas fijas):** precio, nombres de programas ("Arranque", "A1 intensivo"), "fácil", "gratis", "descuento", "rápido" sin número, "garantizado en X meses", "consigue trabajo", "visa", "profesores nativos", días de la semana. Si el profe lo dice, se repite la toma.']:
    para(t, after=3)

d.add_page_break()
h('HOJA DE LA PROFE — SECUENCIA DE LA CLASE CON CÁMARA (35-40 min de clase)', 12.5)
para('Tú diriges. La cámara te sigue. La clase ocurre igual que siempre: las dos simulaciones son tu Bloque 3 y la corrección es tu error paper. Habla normal, corrige en voz alta como siempre, no mires a la cámara salvo cuando diga "A CÁMARA".', color=GRIS, size=9.5, after=6)
HOJA_PROFE = ['**Al empezar la clase (antes de prender la cámara):** pregúntales si están contentos con la clase. Cuando digan que sí: "Parte de mi trabajo es grabar contenido de la academia, y hoy me ayudarían mucho: la clase de simulación se graba. Es la misma clase de siempre, con cámara." Con ánimo, como algo normal. Si alguien dice voluntariamente que no quiere salir, lo ubicas fuera de plano y participa desde ahí como observador; no se discute ni se insiste. (Todos tienen firmada la autorización de imagen en su contrato.)',
          '**Dentro de la clase todo va en inglés** (es un grupo B2): escenario, preguntas, instrucciones y correcciones. Solo las frases marcadas A CÁMARA se dicen en español: son para el anuncio.',
          '**ANTES de la clase, salón vacío (10 min, cuando Isaac llegue):**',
          '  1. Escribe en el tablero un "5 AÑOS" grande y táchalo. A CÁMARA: "El Marco Común Europeo calcula entre quinientas y seiscientas horas de clase para llegar a B2. Si estudias dos horas por semana, son cinco años. Aquí: cuatro horas al día, siete meses. O si trabajas, dos horas cada noche: catorce. No es fácil. Es rápido porque es intenso." Mientras hablas, escribe "575 h", "7 meses" y "14 meses". CIERRE: "Pregúntanos qué fecha te queda. Escríbenos." (2 tomas.)',
          '  2. Sentada en el borde del escritorio, A CÁMARA, seria: "Hay vacantes que dicen inglés intermedio. Ese renglón deja a mucha gente sin poder aplicar. El inglés no te da el puesto. Pero sin inglés, ese puesto ni se abre. Aquí la entrevista se ensaya en clase, pregunta por pregunta, hasta que se contesta sin pensar." CIERRE: "Cuéntanos para qué necesitas el inglés y te decimos por dónde empezar. Escríbenos." (2 tomas.)',
          '**EN LA CLASE (la cámara graba estos 35-40 minutos; después sigue tu clase normal y se acabó la jornada):**',
          '  3. Minuto 0-7 · Corrección del día. Si el grupo tiene error paper, usa el error más repetido. Si no, usa UNO de estos tres, típicos de hispanohablantes (elige el que más oyes en el grupo): (a) "I am agree" → "I agree"; (b) "It depends of the company" → "It depends on the company"; (c) "People is waiting" → "People are waiting". Con el grupo de pie: escribe la frase con el error y pregunta "Can anyone tell me why this is wrong?"; deja que uno lo explique; táchala, escribe la correcta y di "Repeat". Todos la repiten dos veces; pide a uno de los 3 que empezó de cero que la use en una frase propia. Tu voz en inglés es corta (el contenido va escrito en el tablero; lo que se ve es la corrección). CIERRE, A CÁMARA, en español: "Mándanos un audio con tu propia frase usando esto, y te la corregimos."',
          '  4. Minuto 7-19 · Simulación 1, entrevista de trabajo. ESCENARIO (lo dices en inglés y lo escribes en el tablero): "A company in Bucaramanga is hiring a bilingual customer service assistant. Today is the interview." Las 3 preguntas, en el tablero: "Tell me about yourself." / "Why should we hire you?" / "Tell me about a problem you solved at work." ROLES: 1 candidato (empieza el más seguro del grupo, no el más tímido), 1 entrevistador (lee las preguntas del tablero), los otros 3 son observadores de pie con su error paper: anotan UNA cosa que el candidato hizo bien y UN error que oyeron. ROTACIÓN: cada 4 minutos cambia candidato y entrevistador; en 12 minutos pasan los 5 (3 candidatos). CORRECCIÓN EN CÁMARA: corrige lo seguro y visible (volumen, mirar al entrevistador, repetir la frase completa, pronunciación de una palabra): "Again. Louder. Look at her, not at me." La gramática la corriges después, fuera de cámara, con lo que anotaron los observadores. PÁNICO: si alguien se bloquea, el entrevistador repite la pregunta más despacio y el candidato contesta con una sola frase; eso también sirve. Al terminar, A CÁMARA: "Aquí nadie copia del tablero. Desde la primera clase hablas, te equivocas, te corregimos y lo vuelves a decir. Así se entrena un idioma." CIERRE: "¿Quieres ver una clase así por dentro? Escríbenos."',
          '  5. Minuto 19-29 · Simulación 2, entrevista de Au Pair (solo Au Pair: es el programa donde la familia sí entrevista en inglés antes de elegir). ESCENARIO en el tablero, en inglés: "A family in the United States is interviewing their Au Pair candidate by video call." ROLES: el hombre del grupo hace de papá de la familia (lee las preguntas del tablero), las mujeres son las candidatas, una a la vez, 3 minutos cada una; las que no están en turno observan y anotan. Preguntas en el tablero: "Tell me about yourself." / "Why do you want to live with a family abroad?" / "What would you do if the child refuses to eat?" Misma corrección que en la simulación 1. Al terminar, A CÁMARA: "En Au Pair, la familia te entrevista en inglés antes de elegirte. Sin esa entrevista, no hay familia. Aquí la ensayamos hasta que la contestas sin pensar." CIERRE: "Cuéntanos a dónde quieres ir y te decimos qué nivel te pide. Escríbenos."',
          '  6. Minuto 29-37 · Los 3 que empezaron de cero en Heiiu, uno por uno, de pie frente a la cámara: (a) en español, una frase: "Llegué el primer día sin hablar una palabra de inglés. Hace ___ meses." (cada uno dice su dato real); (b) luego 10 segundos hablando en inglés de algo suyo (su trabajo, su plan). Después tú, A CÁMARA: "Esto no pasa por venir a clase a copiar. Pasa porque desde el primer día hablan, se equivocan, los corregimos y lo vuelven a decir. Eso es lo que compras aquí." CIERRE: "¿Quieres llegar ahí? Escríbenos." TOMA 2 DEL CIERRE (5 segundos más, se graba adicional): "Mándanos un audio de 30 segundos y te decimos tu nivel."',
          '  7. Se apaga la cámara. Sigues tu clase normal (Bloque 4, ticket de salida, tarea). La grabación en clase terminó.',
          '**8. Después de la clase (5 min, a solas):** muy cerca de la cámara, hablando bajo: "Te voy a decir lo que no te prometemos: que sea fácil, ni que te guste todos los días. Vas a tener clases pesadas y días de no querer venir. Lo que sí te prometemos: que hablas desde el primer día, que te corrigen todos los días, y que si cumples y no avanzas, te devolvemos la plata. Te lo entregamos firmado. Si buscas que sea divertido, no somos tu academia. Si buscas hablar inglés, sí." CIERRE: "Si vas en serio, escríbenos."',
          '**Reglas mientras la cámara está prendida:** no digas precio, ni "Arranque", ni "fácil", ni "gratis", ni "rápido" sin el número, ni "garantizado en siete meses", ni "consigue trabajo", ni nombres de estudiantes. Si se te sale, repites la toma; no pasa nada.',
          '**Si algo falla:** si uno de los 3 "de cero" no quiere salir, el paso 6 se hace con los que sí. Si alguien se bloquea, una sola frase basta. Si una toma sale mal, se repite. Todo queda grabado hoy.',
]
for t in HOJA_PROFE:
    para(t, after=3)
d.add_page_break()

h('QUÉ SE EDITA PRIMERO Y CUÁNDO SE ENTREGA', 12)
para('Salen 11 videos en dos duraciones = 22 archivos. Se editan en dos tandas:', after=3)
tb = d.add_table(rows=1, cols=3); tb.style = 'Table Grid'
for jj, tt in enumerate(['#', 'TANDA 1 — los 9 primeros (versión de 30 s) · entrega lunes 12/10', 'Archivo']):
    rr = tb.rows[0].cells[jj].paragraphs[0].add_run(tt); rr.bold = True; rr.font.size = Pt(9)
for fila in [['1', 'Llegué sin una palabra — el MEJOR de los 3 estudiantes (el que hable más claro en inglés)', 'V1_VIDEODEHOY_A_30s.mp4'],
             ['2', 'Esto es una clase', 'V2_CLASE_30s.mp4'],
             ['3', 'Siete meses', 'V3_575H_30s.mp4'],
             ['4', 'La vacante', 'V4_VACANTE_30s.mp4'],
             ['5', 'El pasaporte (Au Pair)', 'V5_PASAPORTE_30s.mp4'],
             ['6', 'Te acompañamos', 'V6_GARANTIA_30s.mp4'],
             ['7', 'El Pacto', 'V7_NOESFACIL_30s.mp4'],
             ['8', 'El año después del colegio', 'V8_PADRES_30s.mp4'],
             ['9', 'La corrección del día', 'V9_CORRECCION_30s.mp4']]:
    cells = tb.add_row().cells
    for jj, v in enumerate(fila):
        rr = cells[jj].paragraphs[0].add_run(v); rr.font.size = Pt(9)
para('TANDA 2 — los 13 restantes · entrega miércoles 14/10: las 9 versiones de 15 s (V1_A_15s … V9_15s) + los otros 2 estudiantes de "Llegué sin una palabra" en 30 s y 15 s (V1_VIDEODEHOY_B_30s, V1_VIDEODEHOY_B_15s, V1_VIDEODEHOY_C_30s, V1_VIDEODEHOY_C_15s).', after=3)
para('Las variantes con el cierre "Mándanos un audio" NO se editan hasta que gerencia lo autorice.', size=9.5, color=GRIS, after=8)

h('ORDEN DE GRABACIÓN (prioridad)', 12)
for t in ['1. GUION 6 "Llegué sin una palabra" (los 3 que empezaron de cero: confesión + inglés de hoy) y GUION 2 "Esto es una clase": estudiantes reales hablando. Es la prueba que más convierte en compras caras (investigación 08/10) y lo que ningún avatar ni competidor puede mostrar.',
          '2. GUION 4 "Siete meses": velocidad con número (575 h, 7 meses). Ningún competidor publica sus horas.',
          '3. GUION 3 "La vacante": el destino #1 de la base.',
          '4. GUION 1 "Te acompañamos": la garantía va DESPUÉS del precio (bot, cita, retargeting), no como gancho de alcance. Se graba igual.',
          '5. GUION 8 "El pasaporte": el destino de irse (Au Pair / Work and Travel / Europa), la conversación más barata.',
          '6. GUION 9 "La corrección del día": 10 minutos, el único que da algo antes de pedir (reciprocidad).',
          '7. GUION 5 "El Pacto" (filtro, poco volumen) y GUION 7 "El año después del colegio". Se graban los 9; el orden es de prioridad por si algo falla, no una lista opcional.']:
    para(t, after=2)

guion(1, 'TE ACOMPAÑAMOS (Y TE LO FIRMAMOS)', 'PRIORITARIO', 'La motivación que falla y el acompañamiento que la sostiene (el profe como mentor), cerrado con la garantía por escrito. OJO: siempre "única academia PRESENCIAL de Bucaramanga" (las plataformas online E4CC y EF sí tienen garantía escrita).',
      'Coordinación (Jacqueline), de pie, con el ANEXO DE GARANTÍA impreso en la mano (el documento que se firma con la matrícula; la garantía no está en el contrato de 24 cláusulas). Fondo: la recepción o un aula vacía con el tablero.', '25-30 s',
      'Plano medio. En la última frase, muestra el anexo a cámara y señala la garantía con el dedo. Cierre sobre la hoja, legible.',
      ['Tienes las ganas de aprender inglés. Pero a veces te falla la motivación. Eso no solo pasa con el inglés: pasa con todo.',
       'Por eso aquí no solo te enseñamos. Te acompañamos: tu profe es tu mentor. Te corrige, te pide cuentas y no te suelta.',
       'Es un trabajo en equipo: tú pones tu parte y, si no aprendes, te devolvemos el cien por ciento del nivel. Te lo entregamos firmado.'],
      '"Las ganas no bastan" · "Tu profe es tu mentor" · "Garantía de aprendizaje por escrito · única academia presencial de Bucaramanga que la firma"',
      '"Escríbenos y te mostramos cómo lo hacemos, antes de decidir algo fácil que no te lleve a los resultados que necesitas." Botón: WhatsApp.',
      'El anexo real se ve legible en el plano final. Sin cifras de precio en cuadro. Esta pieza se usa en retargeting (quien ya vio otro anuncio o preguntó precio).',
      gancho='Jacqueline a cámara, sin papel todavía: "Tienes las ganas. Pero a veces te falla la motivación." Texto grande: "Las ganas no bastan."',
      corto='0-3 s Jacqueline: "Tienes las ganas. Pero a veces te falla la motivación." (texto: "Las ganas no bastan") → 3-11 s: "Aquí tu profe es tu mentor: te corrige, te pide cuentas y no te suelta. Tú pones tu parte y, si no aprendes, te devolvemos el nivel." (levanta el anexo) → 11-15 s cierre: "Escríbenos."',
      codigo='V6_GARANTIA', prellenado='Hola, vi el video del acompañamiento (V6). ¿Me muestran la garantía?')

guion(2, 'ESTO ES UNA CLASE', 'PRIORITARIO', 'El método visto: estudiantes hablando desde la primera clase, el profesor como mentor, no como conferencista.',
      'Nadie a cámara: se graba la simulación real del grupo B2, toda en inglés: entrevista de trabajo (escenario en el tablero: "A company in Bucaramanga is hiring a bilingual customer service assistant"; 3 preguntas en el tablero; 1 candidato, 1 entrevistador, 3 observadores de pie; rotan cada 4 minutos). La profe corrige en vivo lo visible (volumen, mirada, repetir la frase completa, pronunciación). Al final, la profe dice UNA frase a cámara. Todo esto está en la hoja de la profe; Isaac solo graba.', '25-30 s',
      'Cámara desde atrás del grupo, luego desde el lado; se ve el tablero con la Frase del Día. Audio ambiente real. Corte final: profe a cámara.',
      ['(ambiente: estudiantes hablando en inglés, el profe corrige: "Again. Louder. Look at her, not at me.")',
       'Profe a cámara: Aquí nadie copia del tablero. Desde la primera clase hablas, te equivocas, te corregimos y lo vuelves a decir. Así se entrena un idioma.'],
      '"Empezó de cero en Heiiu" (solo sobre los 3 que sí) · "Clase de B1, 7:00 PM" (nivel y hora reales) · "Hablas desde el primer día"',
      '"¿Quieres ver una clase así por dentro? Escríbenos." Botón: WhatsApp. VARIANTE DE CIERRE (grabar también): "Mándanos un audio de 30 segundos y te decimos tu nivel." (misma condición que el guion 6).',
      'Autorización de imagen: en el contrato de matrícula; grupo avisado ese día por la profe. Sin nombres en pantalla. Nunca poner cuánto tiempo lleva si no es el dato real del estudiante.',
      gancho='Segundo 0: el estudiante de pie, a mitad de una frase en inglés, con el profe diciendo "Again. Louder." Texto grande: "Empezó de cero aquí. Escúchalo." (Nunca ganchos que le atribuyan una carencia al que mira: política de Meta.)',
      corto='0-3 s estudiante a mitad de frase + profe "Again. Louder." (texto: "Empezó de cero aquí. Escúchalo.") → 3-10 s la misma frase dicha bien + 3 s más de simulación → 10-15 s profe a cámara: "Aquí nadie copia del tablero. Hablas, te equivocas, te corregimos." + "Escríbenos."',
      codigo='V2_CLASE', prellenado='Hola, vi el video de la clase (V2). Quiero ver una por dentro.')

guion(3, 'LA VACANTE', 'PRIORITARIO', 'El destino #1 de la base: trabajo. Sin prometer empleo: el inglés quita la excusa.',
      'Un profe (Tomás o Juan Diego), a cámara, en el aula, sentado en el borde del escritorio. Tono directo, sin sonrisa de comercial.', '20 s',
      'Abre con 1 segundo de la fachada y el texto "Aquí, en Bucaramanga" (lo que Open English, Platzi y E4CC no pueden decir). Plano medio fijo. Al final, corte a 2 segundos de una simulación de entrevista de trabajo en clase.',
      ['Hay vacantes que dicen "inglés intermedio". Ese renglón deja a mucha gente sin poder aplicar.',
       'El inglés no te da el puesto. Pero sin inglés, ese puesto ni se abre.',
       'Aquí la entrevista se ensaya en clase, pregunta por pregunta, hasta que se contesta sin pensar.'],
      '"Aquí, en Bucaramanga" · "La vacante decía: inglés intermedio" · "Entrenamos la entrevista en clase"',
      '"Cuéntanos para qué necesitas el inglés y te decimos por dónde empezar. Escríbenos." Botón: WhatsApp. VARIANTE DE CIERRE: "Mándanos un audio de 30 segundos y te decimos tu nivel." (misma condición que el guion 6).',
      'Nunca "consigue trabajo" ni "aplica a vacantes". Es preparación, no empleo.',
      gancho='Texto grande sobre el profe mirando a cámara en silencio 1 segundo: "La vacante decía: inglés intermedio." (En tercera persona, no "tú no sabes": política de atributos personales de Meta.)',
      corto='0-3 s fachada + texto "La vacante decía: inglés intermedio." → 3-10 s profe: "El inglés no te da el puesto. Pero sin inglés, ese puesto ni se abre." → 10-15 s 2 s de entrevista en clase + "Cuéntanos para qué necesitas el inglés. Escríbenos."',
      codigo='V4_VACANTE', prellenado='Hola, vi el video de la vacante (V4). Necesito el inglés para el trabajo.')

guion(4, 'SIETE MESES', 'PRIORITARIO', 'Velocidad con número: el Marco Común Europeo estima 500-600 h guiadas para B2 (rango; varía por academia); Heiiu son 575 h en 7 meses (4 h/día) o 14 (2 h/noche). Es el único "rápido" verificable del mercado; los demás no publican horas.',
      'Profe a cámara, con el tablero detrás donde escribe (de verdad, en el momento) "575 h" y "7 meses".', '25 s',
      'Plano medio; el profe se voltea y escribe en el tablero mientras habla; vuelve a cámara.',
      ['El Marco Común Europeo calcula entre quinientas y seiscientas horas de clase para llegar a B2.',
       'Si estudias dos horas por semana, son cinco años. Aquí: cuatro horas al día, siete meses. O si trabajas, dos horas cada noche: catorce.',
       'No es fácil. Es rápido porque es intenso.'],
      '"B2 = 500-600 h (Marco Común Europeo)" · "2 h/semana = 5 años" · "Aquí: 7 meses · noche: 14" · al final: "Garantía por escrito"',
      '"Pregúntanos qué fecha te queda. Escríbenos." Botón: WhatsApp.',
      'Las dos jornadas van en la misma pieza (4 h/día = 7 meses; 2 h/noche = 14 meses) para no dejar por fuera al nocturno. Sin precio.',
      gancho='El profe escribe en el tablero un "5 AÑOS" grande y lo tacha. Texto: "Lo que tarda el inglés a 2 horas por semana." Política: "7 meses" es descripción del programa; jamás "garantizado que hablas en 7 meses".',
      corto='0-3 s la profe tacha "5 AÑOS" en el tablero → 3-11 s: "Si estudias dos horas por semana, son cinco años. Aquí: cuatro horas al día, siete meses." (escribe "7 meses") → 11-15 s: "No es fácil. Es intenso. Pregúntanos qué fecha te queda."',
      codigo='V3_575H', prellenado='Hola, vi el video de los 7 meses (V3). ¿Qué jornada me sirve?')

guion(5, 'EL PACTO', 'SE GRABA', 'La venta honesta: qué prometemos y qué no. Atrae al que va en serio y espanta al que busca "fácil" (y eso baja los leads que no contestan).',
      'Profe (Angie o Cristian) a cámara, en el aula, muy cerca, hablando bajo.', '25-30 s',
      'Plano cerrado, fijo. Sin música. Subtítulos palabra por palabra.',
      ['Te voy a decir lo que no te prometemos: que sea fácil, ni que te guste todos los días. Vas a tener clases pesadas y días de no querer venir.',
       'Lo que sí te prometemos: que hablas desde el primer día, que te corrigen todos los días, y que si cumples y no avanzas, te devolvemos la plata. Te lo entregamos firmado.',
       'Si buscas que sea divertido, no somos tu academia. Si buscas hablar inglés, sí.'],
      '"Lo que NO te prometemos" → "Lo que SÍ te firmamos"',
      '"Si vas en serio, escríbenos." Botón: WhatsApp.',
      'Es la pieza que más filtra: menos conversaciones, mejores. Medir costo por CITA, no por lead.',
      gancho='Profe muy cerca, bajo: "No te voy a decir que es fácil." Texto grande: "Lo que NO te prometemos".',
      corto='0-3 s profe muy cerca: "No te voy a decir que es fácil." → 3-11 s: "Si buscas que sea divertido, no somos tu academia. Si buscas hablar inglés, sí." → 11-15 s: "Si vas en serio, escríbenos."',
      codigo='V7_NOESFACIL', prellenado='Hola, vi el video de lo que no prometen (V7). Voy en serio.')

guion(6, 'LLEGUÉ SIN UNA PALABRA', 'PRIORITARIO', 'Prueba real: tres estudiantes que entraron a Heiiu sin hablar inglés y hoy hablan. Confesión en español + 10 s en inglés. (No hay video de entrada de este grupo; la prueba es su palabra con el dato real y su inglés de hoy.)',
      'Cada uno de los 3 que empezó de cero en Heiiu, de pie frente a la cámara, en el salón: (a) en español: "Llegué el primer día sin hablar una palabra de inglés. Hace ___ meses." (dato real de cada uno); (b) 10 segundos en inglés sobre algo suyo. Luego la profe a cámara. Son 3 piezas (una por estudiante) con la misma estructura.', '25-30 s',
      'Plano medio fijo del estudiante. Texto grande con su frase en español mientras la dice; corte a él hablando en inglés con el texto "Hoy". Luego la profe a cámara.',
      ['Estudiante, en español: "Llegué el primer día sin hablar una palabra de inglés. Hace ___ meses." (luego 10 s en inglés)',
       'Profe: Esto no pasa por venir a clase a copiar. Pasa porque desde el primer día hablan, se equivocan, los corregimos y lo vuelven a decir.',
       'Eso es lo que compras aquí.'],
      '"Llegó sin una palabra de inglés" · "Hace ___ meses" (dato real) · "Hoy"',
      '"¿Quieres llegar ahí? Escríbenos." Botón: WhatsApp. TOMA 2 DEL CIERRE (se graba adicional, 5 s de la profe): "Mándanos un audio de 30 segundos y te decimos tu nivel." Solo se publica si el agente recibe audios y alguien los responde en menos de 24 h; si no, "te decimos tu nivel en la cita".',
      'Grabar a los 3: tres piezas distintas con el mismo guion (Meta premia caras y conceptos distintos). Si uno no quiere salir, se hace con los que sí.',
      gancho='Segundo 0: el estudiante a cámara, en español: "Llegué el primer día sin hablar una palabra de inglés." (formato CONFESIÓN, top 5 de ganchos por tasa de acierto en Motion 2026). Corte seco a él hablando en inglés. En pantalla el dato exacto: "Hace ___ meses" (de la ficha del estudiante; sin dato real no se publica).',
      corto='0-4 s estudiante en español: "Llegué el primer día sin hablar una palabra de inglés. Hace ___ meses." → 4-11 s el mismo estudiante hablando en inglés (texto: "Hoy") → 11-15 s profe: "¿Quieres llegar ahí? Escríbenos." Se arma una versión de 15 s por cada uno de los 3 estudiantes.',
      codigo='V1_VIDEODEHOY', prellenado='Hola, vi el video del antes y después (V1). Quiero saber más.')

guion(7, 'EL AÑO DESPUÉS DEL COLEGIO', 'SE GRABA (padres de jóvenes de 17-20 años)', 'Padres de jóvenes que ya salieron del colegio y no han entrado a la universidad (no saben qué estudiar o todavía no alcanza la plata): ese año resuelve el inglés. Más la constancia que se entrena aquí.',
      'Coordinación (Jacqueline) a cámara, en la recepción, hablando a un papá o mamá. Si hay un padre voluntario, mejor él.', '25-30 s',
      'Plano medio fijo; corte de 3 segundos a jóvenes del grupo en clase (de espaldas o con autorización).',
      ['Su hijo ya salió del colegio y todavía no ha entrado a la universidad. No sabe qué estudiar, o todavía no alcanza la plata.',
       'Ese año no tiene que perderse: puede ser el año en que resuelve el inglés, y llega a la universidad o a su primer trabajo con eso listo.',
       'Y algo que los papás nos agradecen más que el inglés: aquí se entrena constancia. Asistencia, tareas, cumplir. Y cumplir no es solo para aprender inglés: es para la vida.',
       'En un mundo con inteligencia artificial, el que se sabe comunicar y cumple es el que avanza. Su hijo se lo va a agradecer. En la tarde, en la noche o los sábados.'],
      '"Salió del colegio. ¿Y ahora qué?" · "El año en que resuelve el inglés" · "Tarde · noche · sábados"',
      '"Pregúntenos qué horario le sirve. Escríbanos." Botón: WhatsApp.',
      'Nada de Saber 11 ni de niños de colegio: el público son los que ya salieron. Sin precio.',
      gancho='Texto grande sobre jóvenes en clase: "Salió del colegio. ¿Y ahora qué?"',
      corto='0-3 s texto sobre jóvenes en clase: "Salió del colegio. ¿Y ahora qué?" → 3-11 s Jacqueline: "Ese año no tiene que perderse: puede ser el año en que resuelve el inglés." → 11-15 s: "Pregúntenos qué horario le sirve. Escríbanos."',
      codigo='V8_PADRES', prellenado='Hola, vi el video del año después del colegio (V8). Es para mi hijo/a.')

guion(8, 'EL PASAPORTE', 'PRIORITARIO (destino: irse)', 'El destino #2 de la base: Au Pair (solo Au Pair: es el programa donde la familia sí entrevista en inglés antes de elegir; Work and Travel y Europa no siempre exigen inglés, así que no se afirman). Sin prometer familia, visa ni empleo.',
      'Simulación real del grupo B1/B2: una familia de Estados Unidos entrevista por videollamada a su candidata a Au Pair. El hombre del grupo hace de papá de la familia (lee las preguntas del tablero); las mujeres son las candidatas, una a la vez. Luego la profe a cámara.', '25-30 s',
      'Abre con 1 segundo de la fachada y el texto "Aquí, en Bucaramanga". Dos segundos de la entrevista en inglés; 8 segundos más de la simulación; profe a cámara; cierre.',
      ['(simulación: "Tell me about yourself. Why do you want to live with a family abroad? What would you do if the child refuses to eat?")',
       'Profe: En Au Pair, la familia te entrevista en inglés antes de elegirte. Sin esa entrevista, no hay familia.',
       'Aquí la ensayamos hasta que la contestas sin pensar.'],
      '"No somos agencia. Te preparamos para la entrevista" · "El inglés es el pasaporte"',
      '"Cuéntanos a dónde quieres ir y te decimos qué nivel te pide. Escríbenos." Botón: WhatsApp.',
      'Prohibido: "te conseguimos la familia / la visa / el empleo", nombres de agencias, países con salario prometido, y afirmar que Work and Travel o Europa exigen inglés (no siempre). Es preparación para la entrevista, no colocación. Prueba la hipótesis destino "irse" contra destino "trabajo aquí" (guion 3).',
      gancho='Estudiante a cámara, en inglés, respondiendo "Tell me about yourself". Texto grande: "La familia te entrevista en inglés antes de elegirte." Texto del anuncio (no del video), primera línea obligatoria: "No somos agencia: te preparamos en inglés para la entrevista de Au Pair. El trámite lo haces con la agencia que elijas."',
      corto='0-3 s candidata respondiendo "Tell me about yourself" (texto: "La familia te entrevista en inglés antes de elegirte.") → 3-11 s profe: "Sin esa entrevista, no hay familia. Aquí la ensayamos hasta que la contestas sin pensar." → 11-15 s: "Cuéntanos a dónde quieres ir. Escríbenos."',
      codigo='V5_PASAPORTE', prellenado='Hola, quiero prepararme en inglés para Au Pair / irme (V5).')

guion(9, 'LA CORRECCIÓN DEL DÍA', 'PRIORITARIO (10 minutos; el único que da algo antes de pedir)', 'Reciprocidad + valor primero: el único formato tutorial del set. Muestra cómo se corrige en Heiiu y regala una corrección real.',
      'La profe en el tablero con el grupo B1/B2 de pie. El error sale del error paper del grupo si existe; si no, uno de los tres típicos de hispanohablantes que trae la hoja de la profe ("I am agree" → "I agree"; "depends of" → "depends on"; "people is" → "people are"). La voz de la profe en inglés es mínima: el contenido va escrito.', '15-20 s',
      'Segundos 0-2: el profe escribe el error real en el tablero. Segundos 2-8: lo tacha y escribe la forma correcta; debajo queda la Frase del Día. Segundos 8-14: los estudiantes la repiten de pie; uno de los que empezó de cero la usa en una frase propia. Cierre del profe a cámara.',
      ['(profe escribe el error, lo tacha, escribe la forma correcta y la dice en voz alta)',
       'Profe (en inglés): "Can anyone tell me why this is wrong?" → lo tacha, escribe la correcta → "Repeat."',
       'Profe a cámara, en español: Mándanos un audio con tu propia frase usando esto, y te la corregimos.'],
      '"El error que más oigo en clase" · la forma correcta en el tablero · "Así se corrige en Heiiu"',
      '"Mándanos un audio con tu propia frase usando esto, y te la corregimos." Botón: WhatsApp. (Si el agente no recibe audios: "Escríbenos y te decimos tu nivel en la cita".)',
      'Sin la palabra "gratis". El acento de la profe no es tema: la pieza muestra la corrección escrita, no una clase de pronunciación. Es la pieza que prueba la hipótesis de dar valor primero (Freedman y Fraser 1966).',
      gancho='Segundo 0: el marcador escribiendo el error en el tablero. Texto grande: "El error que más oigo en clase."',
      corto='0-3 s el marcador escribiendo el error (texto: "El error que más oigo en clase") → 3-10 s lo tacha, escribe la forma correcta, el grupo repite → 10-15 s profe: "Mándanos un audio con tu propia frase usando esto, y te la corregimos."',
      codigo='V9_CORRECCION', prellenado='Hola, vi la corrección del día (V9). Aquí va mi audio.')

h('CHECKLIST DEL DÍA DE GRABACIÓN', 12)
for t in ['• Vertical 9:16, subtítulos grandes desde el primer segundo, sin música encima de la voz en los guiones 1, 5 y 6. Texto y subtítulos dentro de la ZONA SEGURA de Reels (ni en el 14% superior ni en el 35% inferior de la pantalla); audio siempre (Meta: video 9:16 con audio y texto en zona segura = 34,5% menos costo por resultado que imágenes).',
          '• DATOS A CONFIRMAR ANTES DE PUBLICAR (no se inventan): meses reales desde la PRIMERA CLASE (no desde la matrícula) de cada uno de los 3 que empezaron de cero (guiones 2 y 6); que el agente de WhatsApp recibe audios y alguien los responde en menos de 24 h (cierres de reciprocidad).',
          '• Cada video lleva su código de anuncio (V1-V9) y su mensaje prellenado (están en cada guion): el editor nombra el archivo con el código.',
          '• La autorización de imagen está en el contrato de matrícula que todos firmaron; la profe lo plantea como ayuda a su trabajo y quien diga voluntariamente que no, queda fuera de plano. Sin nombres en pantalla.',
          '• Prohibido en pantalla y en voz: precio, "Arranque", "A1 intensivo", "descuento", "gratis", "fácil", "rápido" sin número, "bilingüe", "consigue trabajo", "duplica tu salario", "profesores nativos", "única academia con garantía" sin la palabra PRESENCIAL (las online E4CC y EF la tienen), fecha de inicio de cohorte.',
          '• Cierre de todos: botón de WhatsApp (los anuncios nuevos van a clic-a-WhatsApp para que el agente los reciba; los de formulario llevan la pregunta de motivo).',
          '• Grabar cada guion completo (2 tomas). La versión de 15 segundos NO se graba aparte: se corta en edición siguiendo la línea "VERSIÓN DE 15 SEGUNDOS" de cada guion.',
          '• Tomas de apoyo (10 minutos): estudiantes de pie en simulación, el tablero con la Frase del Día, el anexo de garantía en primer plano, la fachada y la recepción.',
          '• Qué se mide del 15 al 31/10 por pieza: costo por conversación, costo por cita atendida, citas por pieza. La que gane se queda; la que no, se apaga.']:
    para(t, after=2)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\campañas\GUIONES_GRABACION_2026-10-09.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')

# ---- Hoja aparte para la profe (sin investigación ni notas internas) ----
d2 = Document(); d2.styles['Normal'].font.name = 'Calibri'; d2.styles['Normal'].font.size = Pt(10.5)
for sec in d2.sections: sec.left_margin = sec.right_margin = Pt(60); sec.top_margin = sec.bottom_margin = Pt(50)
pp = d2.add_paragraph(); rr = pp.add_run('HOJA DE LA PROFE — CLASE CON CÁMARA · 09/10/2026'); rr.bold = True; rr.font.size = Pt(14); rr.font.color.rgb = NAR
pp = d2.add_paragraph(); rr = pp.add_run('Tú diriges. La cámara te sigue. La clase ocurre igual que siempre: las dos simulaciones son tu Bloque 3 y la corrección es tu error paper. Habla normal, corrige en voz alta como siempre, no mires a la cámara salvo cuando diga "A CÁMARA". Son 35-40 minutos de clase; el resto sigue normal.'); rr.font.size = Pt(9.5); rr.font.color.rgb = GRIS
pp = d2.add_paragraph(); rr = pp.add_run('Quien graba: Isaac.   Coordinación (fechas de matrícula de los 3): Jacqueline.'); rr.font.size = Pt(10)
for t in HOJA_PROFE:
    pp = d2.add_paragraph(); pp.paragraph_format.space_after = Pt(3)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        rr = pp.add_run(part[2:-2] if part.startswith('**') else part); rr.bold = part.startswith('**'); rr.font.size = Pt(10)
out2 = out.replace('GUIONES_GRABACION_2026-10-09.docx', 'HOJA_PROFE_GRABACION_2026-10-09.docx')
try: d2.save(out2); print('OK', out2)
except PermissionError: d2.save(out2.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')

# ---- Hoja aparte para coordinación ----
d3 = Document(); d3.styles['Normal'].font.name = 'Calibri'; d3.styles['Normal'].font.size = Pt(10.5)
for sec in d3.sections: sec.left_margin = sec.right_margin = Pt(60); sec.top_margin = sec.bottom_margin = Pt(50)
pp = d3.add_paragraph(); rr = pp.add_run('HOJA DE COORDINACIÓN — GRABACIÓN 09/10/2026'); rr.bold = True; rr.font.size = Pt(14); rr.font.color.rgb = NAR
HOJA_COORD = [
 '**Antes de la clase, un solo dato:** dile a cada uno de los 3 estudiantes que empezaron de cero en Heiiu cuántos meses llevan desde su PRIMERA CLASE (no desde la fecha de matrícula: a veces el grupo arrancó hasta dos meses después). Primer día del A1 para cada uno. En cámara cada uno dice "Llegué el primer día sin hablar una palabra de inglés. Hace ___ meses": es para que digan el número exacto.',
 '**Tener listo:** el ANEXO DE GARANTÍA HEIIU DE APRENDIZAJE impreso (recursos/comercial/productos/ANEXO_GARANTIA_HEIIU.pdf), 2 copias, con la firma de la academia. Sin precios a la vista.',
 '  1. "Te acompañamos" (duración: 25 a 30 segundos), de pie, primero sin el papel: "Tienes las ganas de aprender inglés. Pero a veces te falla la motivación. Eso no solo pasa con el inglés: pasa con todo. Por eso aquí no solo te enseñamos. Te acompañamos: tu profe es tu mentor. Te corrige, te pide cuentas y no te suelta." Y ahí levantas el anexo a cámara, señalando la garantía: "Es un trabajo en equipo: tú pones tu parte y, si no aprendes, te devolvemos el cien por ciento del nivel. Te lo entregamos firmado." Cierre: "Escríbenos y te mostramos cómo lo hacemos, antes de decidir algo fácil que no te lleve a los resultados que necesitas." La cámara termina sobre la hoja. Dos tomas.',
 '  2. "El año después del colegio" (duración: 25 a 30 segundos), en la recepción, como hablándole a un papá o una mamá: "Su hijo ya salió del colegio y todavía no ha entrado a la universidad. No sabe qué estudiar, o todavía no alcanza la plata. Ese año no tiene que perderse: puede ser el año en que resuelve el inglés, y llega a la universidad o a su primer trabajo con eso listo. Y algo que los papás nos agradecen más que el inglés: aquí se entrena constancia. Asistencia, tareas, cumplir. Y cumplir no es solo para aprender inglés: es para la vida. En un mundo con inteligencia artificial, el que se sabe comunicar y cumple es el que avanza. Su hijo se lo va a agradecer. En la tarde, en la noche o los sábados." Cierre: "Pregúntenos qué horario le sirve. Escríbanos." Dos tomas.',
 '**Con la cámara prendida NO se dice:** precio, "Arranque", "fácil", "gratis", "descuento", "rápido", "garantizado en siete meses", "consigue trabajo", "profesores nativos", ni nombres de estudiantes. Si se te sale, se repite la toma.',
]
for t in HOJA_COORD:
    pp = d3.add_paragraph(); pp.paragraph_format.space_after = Pt(3)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        rr = pp.add_run(part[2:-2] if part.startswith('**') else part); rr.bold = part.startswith('**'); rr.font.size = Pt(10)
out3 = out.replace('GUIONES_GRABACION_2026-10-09.docx', 'HOJA_COORDINACION_GRABACION_2026-10-09.docx')
try: d3.save(out3); print('OK', out3)
except PermissionError: d3.save(out3.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
