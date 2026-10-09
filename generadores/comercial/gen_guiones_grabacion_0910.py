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
def guion(num, titulo, prioridad, vende, quien, dura, escena, texto, pantalla, cta, nota=None, gancho=None, codigo=None, prellenado=None):
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
    if nota: para('Nota: ' + nota, size=9.5, color=GRIS)

p = d.add_paragraph(); r = p.add_run('GUIONES — JORNADA DE GRABACIÓN 09/10/2026'); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = NAR
para('Venden el SERVICIO, no el producto: garantía por escrito, profesor que entrena (coach), acompañamiento diario, y un plan con fecha de llegada. Reglas del calendario: gancho de destino, sin precio ni nombre del programa, nunca "fácil", "rápido" ni "gratis"; caras de profes, estudiantes con cláusula de imagen y coordinación; nunca gerencia. Verticales (9:16), 20-30 segundos, subtítulos grandes. Cada guion abre con un GANCHO de 2 segundos (imagen + texto grande) que es lo que detiene el dedo; la clase, el profe o el contrato son la prueba que viene después. Cierre siempre a WhatsApp. GRUPO DISPONIBLE EL 09/10: un grupo de B1/B2 de 5 estudiantes; 3 de ellos empezaron de cero (A1) en Heiiu y tienen video de entrada en el portafolio: son los protagonistas de los guiones 2 y 6.', color=GRIS, size=9.5, after=8)

h('PLAN DE LA JORNADA (para grabar sin la gerente presente)', 12)
for t in ['**Fecha y lugar:** jueves 09/10/2026, sede Heiiu. **Hora de llegada del equipo:** 45 minutos antes de la clase. **Hora de la clase del grupo B1/B2:** ______ (llenar). **Profe:** ______ (llenar). **Salón:** ______ (llenar).',
          '**Quién manda en el set: LA PROFE.** Ella dirige la clase y las escenas con la HOJA DE LA PROFE (página siguiente); el que graba (Isaac) sigue esa hoja y se encarga de que se vea y se oiga bien (encuadre, audio, dos ángulos); coordinación (Jacqueline) consigue permisos y datos antes de la clase y graba sus dos piezas después. Si algo no sale como está escrito, se graba la versión más cercana y se anota; no se inventa otra escena.',
          '**Equipo:** celular o cámara en vertical (9:16, 1080x1920), micrófono de solapa o el celular a menos de 1,5 m del que habla, luz natural o del salón (sin aro de luz: se ve a anuncio). Un segundo celular para grabar la simulación desde otro ángulo.',
          '**Permisos (ANTES de encender la cámara):** cláusula de imagen firmada por cada estudiante que aparezca; autorización escrita de los 3 que empezaron de cero para usar su video de entrada y el de hoy; fecha de matrícula de cada uno (para los "___ meses · ___ horas" en pantalla). Quien no firme no sale en cámara: se le ubica fuera de plano. Sin nombres de estudiantes en pantalla.',
          '**Orden cronológico del día:** (1) antes de la clase, con el salón vacío: guion 3 "Siete meses" (profe + tablero), guion 4 "La vacante" (profe), tomas de la fachada y la recepción; (2) durante la clase, con el grupo: guion 7 "La corrección del día" al abrir (usa el error paper real), guion 2 "Esto es una clase" (simulación de entrevista o reclamo, 10 minutos de pie), guion 5 "El pasaporte" (simulación de entrevista con familia/empleador, 10 minutos), guion 1 "El video de hoy" (cada uno de los 3 que empezó de cero: 5 s hablando en inglés + 3 s de la confesión en español); (3) después de la clase: guion 6 "Te lo firmamos" (Jacqueline con el contrato impreso), guion 9 "Su hijo a los 18" (Jacqueline en recepción) y, si queda tiempo, guion 8 "El Pacto" (profe). Total estimado: 3 horas.',
          '**Qué entrega Isaac (lunes 12/10, a la carpeta ______ (llenar), y aviso a Brian, que monta la pauta el 15):** por cada guion, dos archivos: versión completa (20-30 s) y versión de 15 s (gancho + frase fuerte + cierre). Nombre del archivo = código del anuncio + duración: V1_VIDEODEHOY_30s.mp4, V1_VIDEODEHOY_15s.mp4, etc. (los códigos están en cada guion). Formato 9:16, 1080x1920, MP4. Subtítulos grandes, palabra por palabra, dentro de la zona segura de Reels (ni en el 14% superior ni en el 35% inferior). Colores de marca: naranja #E54C09 y amarillo #FBC900 para los textos en pantalla (el amarillo nunca como texto sobre blanco). Logo de Heiiu solo en el último segundo. Sin música encima de la voz en los guiones 1, 6 y 8; en los demás, música baja o ninguna. Además, el material en bruto completo en una subcarpeta BRUTO (sirve para cortar otros ganchos sin volver a grabar).',
          '**Lo que NO se graba ni se edita (reglas fijas):** precio, nombres de programas ("Arranque", "A1 intensivo"), "fácil", "gratis", "descuento", "rápido" sin número, "garantizado en X meses", "consigue trabajo", "visa", "profesores nativos", días de la semana. Si el profe lo dice, se repite la toma.']:
    para(t, after=3)

d.add_page_break()
h('HOJA DE LA PROFE — SECUENCIA DE LA CLASE CON CÁMARA (35-40 min de clase)', 12.5)
para('Tú diriges. La cámara te sigue. La clase ocurre igual que siempre: las dos simulaciones son tu Bloque 3 y la corrección es tu error paper. Habla normal, corrige en voz alta como siempre, no mires a la cámara salvo cuando diga "A CÁMARA".', color=GRIS, size=9.5, after=6)
HOJA_PROFE = ['**20 min ANTES de la clase, salón vacío (10 min):**',
          '  1. Escribe en el tablero un "5 AÑOS" grande y táchalo. A CÁMARA: "Llegar a B2 son unas quinientas setenta y cinco horas de clase. En cualquier academia. A dos horas por semana, eso son cinco años. Aquí son cuatro horas al día, de lunes a viernes: siete meses. No es fácil. Es rápido porque es intenso. Lo que firmamos: si cumples y no avanzas, te devolvemos el nivel." Mientras hablas, escribe "575 h" y "7 meses". (2 tomas.)',
          '  2. Sentada en el borde del escritorio, A CÁMARA, seria: "Hay vacantes que dicen inglés intermedio. Ese renglón deja a mucha gente por fuera. El inglés no da el puesto. Quita el requisito que lo cierra. En clase ensayamos esa pregunta: Tell me about yourself. Hasta que se contesta sin pensar." (2 tomas.)',
          '**EN LA CLASE:**',
          '  3. Minuto 0-7 · Corrección del día: con el grupo de pie, escribe en el tablero el error más repetido del error paper de la semana (real). Dilo, táchalo, escribe la forma correcta y di: "This is the mistake I hear the most. This is how we fix it. Repeat." Todos la repiten dos veces; pide a uno de los 3 que empezó de cero que la use en una frase propia. Al final, A CÁMARA, en español: "Mándanos un audio diciéndola y te la corregimos."',
          '  4. Minuto 7-19 · Simulación 1, entrevista de trabajo: un estudiante es el candidato (uno de los 3 que empezó de cero), otro el entrevistador, los demás observan de pie y anotan. Preguntas: "Tell me about yourself", "Why should we hire you?", "Describe a problem you solved." Corrige en voz alta, en el momento: "Again. Louder. Look at her, not at me." Rota el candidato cada 4 minutos. Al terminar, A CÁMARA: "Aquí nadie copia del tablero. Desde la primera clase hablas, te equivocas, te corregimos y lo vuelves a decir. Así se entrena un idioma."',
          '  5. Minuto 19-29 · Simulación 2, entrevista con una familia o un empleador del exterior: "Tell me about yourself. Why do you want to live with a family abroad? What would you do if the child refuses to eat?" Mismo formato. Al terminar, A CÁMARA: "Au Pair, Work and Travel, Europa: ninguno te recibe por querer irte. Te reciben porque pasas la entrevista. Y la entrevista es en inglés. Sin la entrevista en inglés, el proceso se detiene ahí. Aquí la ensayamos hasta que la contestas sin pensar."',
          '  6. Minuto 29-37 · Los 3 que empezaron de cero, uno por uno, de pie frente a la cámara: (a) 10 segundos hablando en inglés de algo suyo (su trabajo, su plan); (b) luego en español, 3 segundos: "Mi video del día 1 me da vergüenza. Mírenlo." Después tú, A CÁMARA: "Esto no pasa solo por venir a clase. Pasa porque todos los días graba un minuto, me lo manda, y yo le digo exactamente qué corregir. Al día siguiente, otra vez. Un profesor que te acompaña todos los días. Eso es lo que compras aquí." Y la variante de cierre: "Mándanos un audio de 30 segundos y te decimos tu nivel."',
          '  7. El resto de la clase sigue normal (Bloque 4, ticket de salida, tarea). La cámara se apaga.',
          '**Si sobra tiempo al final (opcional, 5 min, a solas):** muy cerca de la cámara, hablando bajo: "Te voy a decir lo que no te prometemos: que sea fácil, ni que te guste todos los días. Vas a tener clases pesadas y días de no querer venir. Lo que sí te prometemos: que hablas desde el primer día, que alguien revisa tu práctica todos los días, y que si cumples y no avanzas, te devolvemos la plata. Por escrito. Si buscas que sea divertido, no somos tu academia. Si buscas hablar inglés, sí."',
          '**Reglas mientras la cámara está prendida:** no digas precio, ni "Arranque", ni "fácil", ni "gratis", ni "rápido" sin el número, ni "garantizado en siete meses", ni "consigue trabajo", ni nombres de estudiantes. Si se te sale, repites la toma; no pasa nada.',
          '**Antes de empezar, confirma con Jacqueline:** cláusulas firmadas de los que salen en cámara, autorización de los 3 para usar su video de entrada, y quién NO firmó (lo ubicas fuera de plano).',
          '**PLAN B SI LOS ESTUDIANTES NO COOPERAN:** (1) No firman: quedan fuera de plano; mínimo 2 firmados para las simulaciones y 1 de los 3 "de cero" para el día 1 vs. hoy; se confirma ANTES de la clase. (2) Firman pero les da pena: cámara en trípode al fondo, no en la cara; los primeros 5 minutos de la simulación no se graban; tú corriges como siempre y lo encuadras como lo que es: la clase de simulación de siempre, que en Heiiu se graba para el portafolio; cada uno recibe su clip editado para él (LinkedIn, familia). (3) Se traban o hablan mal: no importa; la pieza vende el entrenamiento, no la fluidez; el momento "Again. Louder." ES el anuncio; lo que no sirve es gente callada. (4) Nadie coopera: se graba todo lo que no necesita estudiantes (pasos 1 y 2 de esta hoja, la corrección del día tú sola en el tablero, El Pacto, y las piezas de Jacqueline) y las de estudiantes se reprograman la semana siguiente con otro grupo, avisando con dos días para las cláusulas. Nunca se paga a un estudiante por salir ni se presiona al que dijo que no.']
for t in HOJA_PROFE:
    para(t, after=3)
d.add_page_break()

h('QUÉ VAMOS A LOGRAR CON ESTOS VIDEOS', 12)
para('Una sola pregunta: ¿qué hace que un desconocido en Bucaramanga pida cita por una academia que no vende fácil? Cada pieza es una hipótesis distinta; del 15 al 31/10 corren con el mismo presupuesto, cada una en su propio conjunto de anuncios, y se miden tres números por pieza: costo por conversación, costo por cita atendida y citas. La que gane se queda con la pauta de noviembre y define el mensaje de todo (agente, flyers, asesoras); las demás se apagan.', after=4)
tb = d.add_table(rows=1, cols=3); tb.style = 'Table Grid'
for j, t in enumerate(['Pieza', 'Hipótesis que prueba', 'Gana si…']):
    c = tb.rows[0].cells[j]; r = c.paragraphs[0].add_run(t); r.bold = True; r.font.size = Pt(9)
for fila in [
 ['6 "El video de hoy" + 2 "Esto es una clase"', 'PRUEBA: ver gente real hablando convierte más que cualquier promesa (lo que dice el cliente que compró en otra parte: "no me importa la garantía si veo que los que muestran hablan").', 'Menor costo por cita de todas.'],
 ['4 "Siete meses"', 'VELOCIDAD CON NÚMERO: "7 meses, 575 horas" compite con el "rápido" de Open English y E4CC sin mentir; nadie más publica horas.', 'Costo por cita igual o menor que las de prueba, y leads que ya no preguntan "¿cuánto dura?".'],
 ['3 "La vacante"', 'DESTINO TRABAJO AQUÍ: el gancho de empleo trae las conversaciones más baratas (dato propio: destino cuesta la mitad que producto).', 'Más conversaciones baratas, aunque conviertan menos a cita.'],
 ['8 "El pasaporte"', 'DESTINO IRSE (Au Pair, Work and Travel, Europa): la conversación más barata de la base, sin confundirse con agencia de empleo.', 'Conversaciones baratas que SÍ contestan al agente (hoy 3 de 5 creen que es una agencia).'],
 ['1 "Te lo firmamos"', 'GARANTÍA COMO CIERRE, no como gancho: en retargeting (quien ya vio otra pieza o preguntó precio) sube la tasa de cita. Es donde está la rotura real: 284 preguntaron precio, 21 agendaron.', 'Entre los que ya preguntaron precio, más citas que sin ella.'],
 ['5 "El Pacto"', 'FILTRO: decir "no es fácil" trae menos leads pero más citas atendidas (menos "no contesta").', 'Menos leads, mayor % que contesta y asiste a la cita.'],
 ['7 "Su hijo a los 18"', 'PADRES: abre el grupo de la tarde y el sabatino con un comprador distinto (el acudiente).', 'Citas con acudiente para la franja 1:30-6:00.'],
]:
    row = tb.add_row().cells
    for j, v in enumerate(fila):
        r = row[j].paragraphs[0].add_run(v); r.font.size = Pt(9); r.bold = (j == 0)
para('Cómo se lee (investigación Meta 08/10): con ~75 conversaciones en 17 días, el costo por cita por video no va a ser estadísticamente sólido; la lectura temprana se hace con tasa de gancho (vistas de 3 s ÷ impresiones), reproducción completa, CTR y costo por conversación. Ningún video se declara ganador con menos de 5 citas, y ninguno se apaga antes del corte del 22/10.', size=9.5, color=GRIS, after=2)
para('Lo que NO se prueba porque ya se sabe que no diferencia: "fácil", "gratis", descuento, nombre del programa, miedo ("¿te congelas?"), profesores nativos.', size=9.5, color=GRIS, after=8)

h('ORDEN DE GRABACIÓN (prioridad)', 12)
for t in ['1. GUION 6 "El video de hoy" (los 3 que empezaron de cero: día 1 vs. hoy) y GUION 2 "Esto es una clase": estudiantes reales hablando. Es la prueba que más convierte en compras caras (investigación 08/10) y lo que ningún avatar ni competidor puede mostrar.',
          '2. GUION 4 "Siete meses": velocidad con número (575 h, 7 meses). Ningún competidor publica sus horas.',
          '3. GUION 3 "La vacante": el destino #1 de la base.',
          '4. GUION 1 "Te lo firmamos": la garantía va DESPUÉS del precio (bot, cita, retargeting), no como gancho de alcance. Se graba igual.',
          '5. GUION 8 "El pasaporte": el destino de irse (Au Pair / Work and Travel / Europa), la conversación más barata.',
          '6. GUION 9 "La corrección del día": 10 minutos, el único que da algo antes de pedir (reciprocidad).',
          '7. Si hay tiempo: GUION 5 "El Pacto" (filtro, poco volumen), GUION 7 "Su hijo a los 18".']:
    para(t, after=2)

guion(1, 'TE LO FIRMAMOS', 'PRIORITARIO', 'La garantía por escrito, legible y fácil de cobrar. OJO: siempre "única academia PRESENCIAL de Bucaramanga" (las plataformas online E4CC y EF sí tienen garantía escrita; Wall Street ya no opera en la ciudad). Y la nuestra cabe en 3 líneas.',
      'Coordinación (Jacqueline), de pie, con el contrato impreso en la mano. Fondo: la recepción o un aula vacía con el tablero.', '20-25 s',
      'Plano medio. Al decir "aquí", muestra la hoja a cámara y señala la cláusula con el dedo. Al final, la firma de la academia en la hoja.',
      ['Todas las academias te prometen que vas a aprender inglés. Nosotros te lo firmamos.',
       'Aquí, en tu contrato, dice: si cumples con tu asistencia, tus tareas y tus evaluaciones, y no avanzas, te devolvemos el cien por ciento del nivel.',
       'Si cumples y no avanzas, el que pierde plata somos nosotros. No te pedimos que nos creas: te pedimos que leas.'],
      '"GARANTÍA DE APRENDIZAJE POR ESCRITO" · "Única academia presencial de Bucaramanga que la firma · sin letra pequeña"',
      '"Escríbenos y te mostramos el contrato antes de que decidas." Botón: WhatsApp.',
      'Que el contrato real se vea legible en el plano cerrado (cláusula de garantía). Sin cifras de precio en cuadro. Esta pieza se usa en retargeting (quien ya vio otro anuncio o preguntó precio): ahí es donde la garantía decide.',
      gancho='Jacqueline levanta el contrato a cámara. Texto grande: "Si cumples y no avanzas, te devolvemos el 100%. Firmado."',
      codigo='V6_GARANTIA', prellenado='Hola, vi el video de la garantía (V6). ¿Me muestran el contrato?')

guion(2, 'ESTO ES UNA CLASE', 'PRIORITARIO', 'El método visto: estudiantes hablando desde la primera clase, el profesor como coach, no como conferencista.',
      'Nadie a cámara: se graba la simulación real del grupo B1/B2 (entrevista de trabajo o reclamo a un proveedor), estudiantes de pie; protagonista uno de los 3 que empezó de cero en Heiiu. Voz del profe corrigiendo en vivo. Al final, el profe dice UNA frase a cámara.', '25-30 s',
      'Cámara desde atrás del grupo, luego desde el lado; se ve el tablero con la Frase del Día. Audio ambiente real. Corte final: profe a cámara.',
      ['(ambiente: estudiantes hablando en inglés, el profe corrige: "Again. Louder. Look at her, not at me.")',
       'Profe a cámara: Aquí nadie copia del tablero. Desde la primera clase hablas, te equivocas, te corregimos y lo vuelves a decir. Así se entrena un idioma.'],
      '"Empezó de cero en Heiiu" (solo sobre los 3 que sí) · "Clase de B1, 7:00 PM" (nivel y hora reales) · "Hablas desde el primer día"',
      '"¿Quieres ver una clase así por dentro? Escríbenos." Botón: WhatsApp. VARIANTE DE CIERRE (grabar también): "Mándanos un audio de 30 segundos y te decimos tu nivel." (misma condición que el guion 6).',
      'Solo estudiantes con cláusula de imagen firmada y avisados ese día. Sin nombres en pantalla. Nunca poner cuánto tiempo lleva si no es el dato real del estudiante.',
      gancho='Segundo 0: el estudiante de pie, a mitad de una frase en inglés, con el profe diciendo "Again. Louder." Texto grande: "Empezó de cero aquí. Escúchalo." (Nunca ganchos que le atribuyan una carencia al que mira: política de Meta.)',
      codigo='V2_CLASE', prellenado='Hola, vi el video de la clase (V2). Quiero ver una por dentro.')

guion(3, 'LA VACANTE', 'PRIORITARIO', 'El destino #1 de la base: trabajo. Sin prometer empleo: el inglés quita la excusa.',
      'Un profe (Tomás o Juan Diego), a cámara, en el aula, sentado en el borde del escritorio. Tono directo, sin sonrisa de comercial.', '20 s',
      'Abre con 1 segundo de la fachada y el texto "Aquí, en Bucaramanga" (lo que Open English, Platzi y E4CC no pueden decir). Plano medio fijo. Al final, corte a 2 segundos de una simulación de entrevista de trabajo en clase.',
      ['Hay vacantes que dicen "inglés intermedio". Ese renglón deja a mucha gente por fuera.',
       'El inglés no da el puesto. Quita el requisito que lo cierra.',
       'En clase ensayamos esa pregunta: "Tell me about yourself". Hasta que se contesta sin pensar.'],
      '"Aquí, en Bucaramanga" · "La vacante decía: inglés intermedio" · "Entrenamos la entrevista en clase"',
      '"Cuéntanos para qué necesitas el inglés y te decimos por dónde empezar. Escríbenos." Botón: WhatsApp. VARIANTE DE CIERRE: "Mándanos un audio de 30 segundos y te decimos tu nivel." (misma condición que el guion 6).',
      'Nunca "consigue trabajo" ni "aplica a vacantes". Es preparación, no empleo.',
      gancho='Texto grande sobre el profe mirando a cámara en silencio 1 segundo: "La vacante decía: inglés intermedio." (En tercera persona, no "tú no sabes": política de atributos personales de Meta.)',
      codigo='V4_VACANTE', prellenado='Hola, vi el video de la vacante (V4). Necesito el inglés para el trabajo.')

guion(4, 'SIETE MESES', 'PRIORITARIO', 'Velocidad con número: 575 h (estándar Cambridge para B2) en 7 meses. Es el único "rápido" verificable del mercado; los demás dicen "2x" o "10 meses" sin publicar horas.',
      'Profe a cámara, con el tablero detrás donde escribe (de verdad, en el momento) "575 h" y "7 meses".', '25 s',
      'Plano medio; el profe se voltea y escribe en el tablero mientras habla; vuelve a cámara.',
      ['Llegar a B2 son unas quinientas setenta y cinco horas de clase. En cualquier academia.',
       'A dos horas por semana, eso son cinco años. Aquí son cuatro horas al día, de lunes a viernes: siete meses.',
       'No es fácil. Es rápido porque es intenso.',
       'Lo que firmamos: si cumples y no avanzas, te devolvemos el nivel.'],
      '"B2 = 575 horas" · "2 h/semana = 5 años" · "Aquí: 7 meses"',
      '"Pregúntanos qué fecha te queda. Escríbenos." Botón: WhatsApp.',
      'El "7 meses" aplica al súper intensivo de 4 h; en la noche son ~14 meses: no mezclar. Sin precio. Versión nocturna del cierre: "dos horas cada noche, catorce meses".',
      gancho='El profe escribe en el tablero un "5 AÑOS" grande y lo tacha. Texto: "Lo que tarda el inglés a 2 horas por semana." Política: "7 meses" es descripción del programa; jamás "garantizado que hablas en 7 meses".',
      codigo='V3_575H', prellenado='Hola, vi el video de los 7 meses (V3). ¿Qué jornada me sirve?')

guion(5, 'EL PACTO', 'ALTERNO', 'La venta honesta: qué prometemos y qué no. Atrae al que va en serio y espanta al que busca "fácil" (y eso baja los leads que no contestan).',
      'Profe (Angie o Cristian) a cámara, en el aula, muy cerca, hablando bajo.', '25-30 s',
      'Plano cerrado, fijo. Sin música. Subtítulos palabra por palabra.',
      ['Te voy a decir lo que no te prometemos: que sea fácil, ni que te guste todos los días. Vas a tener clases pesadas y días de no querer venir.',
       'Lo que sí te prometemos: que hablas desde el primer día, que alguien revisa tu práctica todos los días, y que si cumples y no avanzas, te devolvemos la plata. Por escrito.',
       'Si buscas que sea divertido, no somos tu academia. Si buscas hablar inglés, sí.'],
      '"Lo que NO te prometemos" → "Lo que SÍ te firmamos"',
      '"Si vas en serio, escríbenos." Botón: WhatsApp.',
      'Es la pieza que más filtra: menos conversaciones, mejores. Medir costo por CITA, no por lead.',
      gancho='Profe muy cerca, bajo: "No te voy a decir que es fácil." Texto grande: "Lo que NO te prometemos".',
      codigo='V7_NOESFACIL', prellenado='Hola, vi el video de lo que no prometen (V7). Voy en serio.')

guion(6, 'EL VIDEO DE HOY', 'PRIORITARIO', 'El acompañamiento diario: cada estudiante graba un video corto todos los días y el profe le dice qué mejorar. Antes y después real.',
      'Uno de los 3 estudiantes del grupo que empezó de cero en Heiiu (cláusula de imagen + autorización escrita para usar sus dos videos): 5 segundos de su video de entrada en A1 (día 1) y 5 segundos hablando hoy en B1 (grabado mañana o de su portafolio reciente). Luego el profe a cámara.', '25-30 s',
      'Pantalla partida o corte seco: "Día 1" / "Hoy" (con el dato real: "hace ___ meses", se llena con la fecha de matrícula del estudiante). Luego el profe, con el celular en la mano, mostrando (sin que se lea el nombre) el chat donde manda la corrección.',
      ['(video día 1 en A1, 5 s) (video de hoy en B1, 5 s)',
       'Profe: Esto no pasa solo por venir a clase. Pasa porque todos los días graba un minuto, me lo manda, y yo le digo exactamente qué corregir. Al día siguiente, otra vez.',
       'Un profesor que te acompaña todos los días. Eso es lo que compras aquí.'],
      '"Día 1" · "Hoy: ___ meses, ___ horas de clase" (datos reales de la ficha) · "Un video al día. Un profesor que lo revisa."',
      '"¿Quieres que te acompañen así? Escríbenos." Botón: WhatsApp. VARIANTE DE CIERRE (grabar también, 5 s del profe): "Mándanos un audio de 30 segundos y te decimos tu nivel." Solo se publica si el agente recibe audios y alguien los responde en menos de 24 h; si no, "te decimos tu nivel en la cita".',
      'Solo con autorización escrita del estudiante para usar sus dos videos. Si se puede, grabar los 3 (tres piezas distintas con el mismo guion: Meta premia conceptos y caras distintas).',
      gancho='Segundo 0: su video de entrada, nervioso, sin poder terminar la frase. Texto grande: "Día 1." Corte seco al de hoy hablando de corrido: "Hoy." VERSIÓN B (formato CONFESIÓN, top 5 de ganchos por tasa de acierto en Motion 2026): el mismo estudiante a cámara, en español, 3 segundos: "Mi video del día 1 me da vergüenza. Mírenlo." → corte a su video de entrada → corte a él hoy en inglés. En pantalla los datos exactos: "___ meses · ___ horas de clase" (de la ficha del estudiante; el antes/después vago ya no convence).',
      codigo='V1_VIDEODEHOY', prellenado='Hola, vi el video del antes y después (V1). Quiero saber más.')

guion(7, 'SU HIJO A LOS 18', 'ALTERNO (para el grupo de la tarde y el sabatino)', 'Padres: el inglés resuelto antes de la universidad, y la disciplina que se entrena aquí.',
      'Coordinación (Jacqueline) a cámara, en la recepción, hablando a un papá o mamá. Si hay un padre voluntario con cláusula, mejor él.', '25 s',
      'Plano medio fijo; corte de 3 segundos a jóvenes de 15-17 en clase (de espaldas o con autorización).',
      ['En grado once, el Saber 11 ya le evalúa inglés. Imagínese a su hijo a los dieciocho con eso resuelto: la universidad o la beca sin ese requisito pendiente.',
       'Y algo que los papás nos agradecen más que el inglés: aquí se entrena constancia. Un video al día, asistencia, tareas. Lo que aprende de cumplir le sirve para todo.',
       'Desde los doce años, en la tarde, en la noche o los sábados.'],
      '"Desde los 12 años" · "Tarde · noche · sábados" · "Garantía por escrito"',
      '"Pregúntenos qué horario le sirve a su hijo. Escríbanos." Botón: WhatsApp.',
      'El grupo de la tarde está "en apertura": el anuncio no promete horario fijo; el agente captura la franja.',
      gancho='Texto grande sobre jóvenes en clase: "A los 18, con el inglés resuelto."',
      codigo='V8_PADRES', prellenado='Hola, vi el video para padres (V8). Es para mi hijo/a.')

guion(8, 'EL PASAPORTE', 'PRIORITARIO (destino: irse)', 'El destino #2 de la base: Au Pair, Work and Travel, Europa. Sin prometer familia, visa ni empleo: la entrevista es en inglés y aquí se ensaya.',
      'Simulación real del grupo B1/B2: entrevista con una familia o un empleador del exterior, un estudiante responde, otro hace de entrevistador. Luego un profe a cámara.', '25-30 s',
      'Abre con 1 segundo de la fachada y el texto "Aquí, en Bucaramanga". Dos segundos de la entrevista en inglés; 8 segundos más de la simulación; profe a cámara; cierre.',
      ['(simulación: "Tell me about yourself. Why do you want to live with a family abroad?")',
       'Profe: Au Pair, Work and Travel, Europa: ninguno te recibe por querer irte. Te reciben porque pasas la entrevista. Y la entrevista es en inglés.',
       'Sin la entrevista en inglés, el proceso se detiene ahí. Aquí la ensayamos hasta que la contestas sin pensar.'],
      '"No somos agencia. Te preparamos para la entrevista" · "El inglés es el pasaporte"',
      '"Cuéntanos a dónde quieres ir y te decimos qué nivel te pide. Escríbenos." Botón: WhatsApp.',
      'Prohibido: "te conseguimos la familia / la visa / el empleo", nombres de agencias, países con salario prometido. Es preparación para la entrevista, no colocación. Prueba la hipótesis destino "irse" contra destino "trabajo aquí" (guion 3).',
      gancho='Estudiante a cámara, en inglés, respondiendo "Tell me about yourself". Texto grande: "La familia te entrevista en inglés antes de elegirte." Texto del anuncio (no del video), primera línea obligatoria: "No somos agencia: te preparamos en inglés para la entrevista de Au Pair o de trabajo en el exterior. El trámite lo haces con la agencia que elijas."',
      codigo='V5_PASAPORTE', prellenado='Hola, quiero prepararme en inglés para Au Pair / irme (V5).')

guion(9, 'LA CORRECCIÓN DEL DÍA', 'PRIORITARIO (10 minutos; el único que da algo antes de pedir)', 'Reciprocidad + valor primero: el único formato tutorial del set. Muestra cómo se corrige en Heiiu y regala una corrección real.',
      'El profe en el tablero con el grupo B1/B2 de pie. El error sale del ERROR PAPER real del grupo (anónimo); no se inventa.', '15-20 s',
      'Segundos 0-2: el profe escribe el error real en el tablero. Segundos 2-8: lo tacha y escribe la forma correcta; debajo queda la Frase del Día. Segundos 8-14: los estudiantes la repiten de pie; uno de los que empezó de cero la usa en una frase propia. Cierre del profe a cámara.',
      ['(profe escribe el error, lo tacha, escribe la forma correcta y la dice en voz alta)',
       'Profe: Este es el error que más oigo. Así se corrige. Repeat.',
       'Profe a cámara: Mándanos un audio diciéndola y te la corregimos.'],
      '"El error que más oigo en clase" · la forma correcta en el tablero · "Así se corrige en Heiiu"',
      '"Mándanos un audio diciéndola y te la corregimos." Botón: WhatsApp. (Si el agente no recibe audios: "Escríbenos y te decimos tu nivel en la cita".)',
      'Sin la palabra "gratis". Es la pieza que prueba la hipótesis de dar valor primero (Freedman y Fraser 1966: un pedido pequeño sube la aceptación del grande).',
      gancho='Segundo 0: el marcador escribiendo el error en el tablero. Texto grande: "El error que más oigo en clase."',
      codigo='V9_CORRECCION', prellenado='Hola, vi la corrección del día (V9). Aquí va mi audio.')

h('CHECKLIST DEL DÍA DE GRABACIÓN', 12)
for t in ['• Vertical 9:16, subtítulos grandes desde el primer segundo, sin música encima de la voz en los guiones 1, 5 y 6. Texto y subtítulos dentro de la ZONA SEGURA de Reels (ni en el 14% superior ni en el 35% inferior de la pantalla); audio siempre (Meta: video 9:16 con audio y texto en zona segura = 34,5% menos costo por resultado que imágenes).',
          '• DATOS A CONFIRMAR ANTES DE PUBLICAR (no se inventan): meses y horas reales de cada uno de los 3 estudiantes que empezaron de cero (guiones 2, 4, 6); que el agente de WhatsApp recibe audios y alguien los responde en menos de 24 h (cierres de reciprocidad); el error real del error paper (guion 9).',
          '• Cada video lleva su código de anuncio (V1-V9) y su mensaje prellenado (están en cada guion): el editor nombra el archivo con el código.',
          '• Cláusula de imagen firmada por cada estudiante que aparezca; avisarles antes de la clase. Sin nombres en pantalla.',
          '• Prohibido en pantalla y en voz: precio, "Arranque", "A1 intensivo", "descuento", "gratis", "fácil", "rápido" sin número, "bilingüe", "consigue trabajo", "duplica tu salario", "profesores nativos", "única academia con garantía" sin la palabra PRESENCIAL (las online E4CC y EF la tienen), fecha de inicio de cohorte.',
          '• Cierre de todos: botón de WhatsApp (los anuncios nuevos van a clic-a-WhatsApp para que el agente los reciba; los de formulario llevan la pregunta de motivo).',
          '• Grabar cada guion dos veces: una completa y una de 15 segundos (solo la frase fuerte + cierre) para pruebas.',
          '• Tomas de apoyo (10 minutos): estudiantes de pie en simulación, el tablero con la Frase del Día, el contrato de garantía en primer plano, la fachada y la recepción.',
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
pp = d2.add_paragraph(); rr = pp.add_run('Hora de la clase: ________   Salón: ________   Quien graba: ________   Coordinación (permisos y datos): Jacqueline'); rr.font.size = Pt(10)
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
 '**ANTES DE LA CLASE (tu parte más importante):** (1) Cláusula de imagen firmada por cada estudiante del grupo B1/B2 que vaya a salir en cámara; quien no firme se ubica fuera de plano y se le avisa a la profe. (2) Autorización escrita de los 3 estudiantes que empezaron de cero en Heiiu para usar su video de entrada (día 1) y el de hoy. (3) Fecha de matrícula de esos 3 (para poner en pantalla "___ meses · ___ horas de clase"): se la entregas al que graba por escrito. (4) Avisar al grupo al llegar: "hoy la clase de simulación se graba; es la misma clase de siempre, con cámara; cada uno recibe su clip".',
 '**Tener listo:** el contrato de matrícula real impreso (2 copias), abierto en la cláusula de la garantía de aprendizaje, con la firma de la academia. Sin precios a la vista en el cuadro.',
 '**DESPUÉS DE LA CLASE, tus dos piezas (15 min, a cámara, de pie):**',
 '  1. "Te lo firmamos" (20-25 s). Levantas el contrato a cámara y, señalando la cláusula con el dedo, dices: "Todas las academias te prometen que vas a aprender inglés. Nosotros te lo firmamos. Aquí, en tu contrato, dice: si cumples con tu asistencia, tus tareas y tus evaluaciones, y no avanzas, te devolvemos el cien por ciento del nivel. Si cumples y no avanzas, el que pierde plata somos nosotros. No te pedimos que nos creas: te pedimos que leas." Al final, la cámara cierra sobre la cláusula, que debe leerse. Dos tomas.',
 '  2. "Su hijo a los 18" (25 s), en la recepción, como hablándole a un papá o una mamá: "En grado once, el Saber 11 ya le evalúa inglés. Imagínese a su hijo a los dieciocho con eso resuelto: la universidad o la beca sin ese requisito pendiente. Y algo que los papás nos agradecen más que el inglés: aquí se entrena constancia. Un video al día, asistencia, tareas. Lo que aprende de cumplir le sirve para todo. Desde los doce años, en la tarde, en la noche o los sábados." Dos tomas.',
 '**Con la cámara prendida NO se dice:** precio, "Arranque", "fácil", "gratis", "descuento", "rápido", "garantizado en siete meses", "consigue trabajo", "profesores nativos", ni nombres de estudiantes. Si se te sale, se repite la toma.',
 '**Al terminar:** le confirmas al que graba que tiene las fechas de matrícula de los 3 y la lista de quién firmó, y se lo reportas a gerencia por WhatsApp en una línea: "Grabación hecha: X estudiantes firmaron, piezas grabadas: ___".',
]
for t in HOJA_COORD:
    pp = d3.add_paragraph(); pp.paragraph_format.space_after = Pt(3)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        rr = pp.add_run(part[2:-2] if part.startswith('**') else part); rr.bold = part.startswith('**'); rr.font.size = Pt(10)
out3 = out.replace('GUIONES_GRABACION_2026-10-09.docx', 'HOJA_COORDINACION_GRABACION_2026-10-09.docx')
try: d3.save(out3); print('OK', out3)
except PermissionError: d3.save(out3.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
