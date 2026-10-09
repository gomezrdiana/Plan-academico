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
def guion(num, titulo, prioridad, vende, quien, dura, escena, texto, pantalla, cta, nota=None, gancho=None):
    h(f'GUION {num} — {titulo}   [{prioridad}]', 12.5, 14)
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

h('ORDEN DE GRABACIÓN (prioridad)', 12)
for t in ['1. GUION 6 "El video de hoy" (los 3 que empezaron de cero: día 1 vs. hoy) y GUION 2 "Esto es una clase": estudiantes reales hablando. Es la prueba que más convierte en compras caras (investigación 08/10) y lo que ningún avatar ni competidor puede mostrar.',
          '2. GUION 4 "Siete meses": velocidad con número (575 h, 7 meses). Ningún competidor publica sus horas.',
          '3. GUION 3 "La vacante": el destino #1 de la base.',
          '4. GUION 1 "Te lo firmamos": la garantía va DESPUÉS del precio (bot, cita, retargeting), no como gancho de alcance. Se graba igual.',
          '5. Si hay tiempo: GUION 5 "El Pacto" (filtro, poco volumen), GUION 7 "Su hijo a los 18".']:
    para(t, after=2)

guion(1, 'TE LO FIRMAMOS', 'PRIORITARIO', 'La garantía por escrito, legible y fácil de cobrar. OJO: siempre "única academia PRESENCIAL de Bucaramanga" (las plataformas online E4CC y EF sí tienen garantía escrita; Wall Street ya no opera en la ciudad). Y la nuestra cabe en 3 líneas.',
      'Coordinación (Jacqueline), de pie, con el contrato impreso en la mano. Fondo: la recepción o un aula vacía con el tablero.', '20-25 s',
      'Plano medio. Al decir "aquí", muestra la hoja a cámara y señala la cláusula con el dedo. Al final, la firma de la academia en la hoja.',
      ['Todas las academias te prometen que vas a aprender inglés. Nosotros te lo firmamos.',
       'Aquí, en tu contrato, dice: si cumples con tu asistencia, tus tareas y tus evaluaciones, y no avanzas, te devolvemos el cien por ciento del nivel.',
       'No te pedimos que nos creas. Te pedimos que leas.'],
      '"GARANTÍA DE APRENDIZAJE POR ESCRITO" · "Única academia presencial de Bucaramanga que la firma · sin letra pequeña"',
      '"Escríbenos y te mostramos el contrato antes de que decidas." Botón: WhatsApp.',
      'Que el contrato real se vea legible en el plano cerrado (cláusula de garantía). Sin cifras de precio en cuadro. Esta pieza se usa en retargeting (quien ya vio otro anuncio o preguntó precio): ahí es donde la garantía decide.',
      gancho='Jacqueline levanta el contrato a cámara. Texto grande: "Si no aprendes, te devolvemos el 100%. Firmado."')

guion(2, 'ESTO ES UNA CLASE', 'PRIORITARIO', 'El método visto: estudiantes hablando desde la primera clase, el profesor como coach, no como conferencista.',
      'Nadie a cámara: se graba la simulación real del grupo B1/B2 (entrevista de trabajo o reclamo a un proveedor), estudiantes de pie; protagonista uno de los 3 que empezó de cero en Heiiu. Voz del profe corrigiendo en vivo. Al final, el profe dice UNA frase a cámara.', '25-30 s',
      'Cámara desde atrás del grupo, luego desde el lado; se ve el tablero con la Frase del Día. Audio ambiente real. Corte final: profe a cámara.',
      ['(ambiente: estudiantes hablando en inglés, el profe corrige: "Again. Louder. Look at her, not at me.")',
       'Profe a cámara: Aquí nadie copia del tablero. Desde la primera clase hablas, te equivocas, te corregimos y lo vuelves a decir. Así se entrena un idioma.'],
      '"Empezó de cero en Heiiu" (solo sobre los 3 que sí) · "Clase de B1, 7:00 PM" (nivel y hora reales) · "Hablas desde el primer día"',
      '"¿Quieres ver una clase así por dentro? Escríbenos." Botón: WhatsApp.',
      'Solo estudiantes con cláusula de imagen firmada y avisados ese día. Sin nombres en pantalla. Nunca poner cuánto tiempo lleva si no es el dato real del estudiante.',
      gancho='Segundo 0: el estudiante de pie, a mitad de una frase en inglés, con el profe diciendo "Again. Louder." Texto grande: "Empezó de cero aquí. Escúchalo." Alternativa: "¿Cuánto llevas en: estoy aprendiendo inglés?"')

guion(3, 'LA VACANTE', 'PRIORITARIO', 'El destino #1 de la base: trabajo. Sin prometer empleo: el inglés quita la excusa.',
      'Un profe (Tomás o Juan Diego), a cámara, en el aula, sentado en el borde del escritorio. Tono directo, sin sonrisa de comercial.', '20 s',
      'Plano medio fijo. Al final, corte a 2 segundos de una simulación de entrevista de trabajo en clase.',
      ['¿Cuántas vacantes has dejado pasar porque decían "inglés intermedio"?',
       'El inglés no te da el puesto. Te quita la excusa que hoy te lo cierra.',
       'Aquí entrenamos esa entrevista hasta que la haces sin pensar.'],
      '"La vacante que hoy pasas de largo" · "Entrenamos la entrevista en clase"',
      '"Cuéntanos para qué necesitas el inglés y te decimos por dónde empezar. Escríbenos." Botón: WhatsApp.',
      'Nunca "consigue trabajo" ni "aplica a vacantes". Es preparación, no empleo.',
      gancho='Texto grande sobre el profe mirando a cámara en silencio 1 segundo: "Decía: inglés intermedio. Y la cerraste."')

guion(4, 'SIETE MESES', 'PRIORITARIO', 'Velocidad con número: 575 h (estándar Cambridge para B2) en 7 meses. Es el único "rápido" verificable del mercado; los demás dicen "2x" o "10 meses" sin publicar horas.',
      'Profe a cámara, con el tablero detrás donde escribe (de verdad, en el momento) "575 h" y "7 meses".', '25 s',
      'Plano medio; el profe se voltea y escribe en el tablero mientras habla; vuelve a cámara.',
      ['Llegar a B2 son unas quinientas setenta y cinco horas de clase. En cualquier academia.',
       'A dos horas por semana, eso son cinco años. Aquí son cuatro horas al día, de lunes a viernes: siete meses.',
       'No es fácil. Es rápido porque es intenso. Y te lo firmamos.'],
      '"B2 = 575 horas" · "2 h/semana = 5 años" · "Aquí: 7 meses"',
      '"Pregúntanos qué fecha te queda. Escríbenos." Botón: WhatsApp.',
      'El "7 meses" aplica al súper intensivo de 4 h; en la noche son ~14 meses: no mezclar. Sin precio. Versión nocturna del cierre: "dos horas cada noche, catorce meses".',
      gancho='El profe escribe en el tablero un "5 AÑOS" grande y lo tacha. Texto: "Lo que tarda el inglés a 2 horas por semana."')

guion(5, 'EL PACTO', 'ALTERNO', 'La venta honesta: qué prometemos y qué no. Atrae al que va en serio y espanta al que busca "fácil" (y eso baja los leads que no contestan).',
      'Profe (Angie o Cristian) a cámara, en el aula, muy cerca, hablando bajo.', '25-30 s',
      'Plano cerrado, fijo. Sin música. Subtítulos palabra por palabra.',
      ['Te voy a decir lo que no te prometemos: que sea fácil, que sea rápido, o que te guste todos los días. Vas a tener clases pesadas y días de no querer venir.',
       'Lo que sí te prometemos: que hablas desde el primer día, que alguien revisa tu práctica todos los días, y que si cumples y no avanzas, te devolvemos la plata. Por escrito.',
       'Si buscas que sea divertido, no somos tu academia. Si buscas hablar inglés, sí.'],
      '"Lo que NO te prometemos" → "Lo que SÍ te firmamos"',
      '"Si vas en serio, escríbenos." Botón: WhatsApp.',
      'Es la pieza que más filtra: menos conversaciones, mejores. Medir costo por CITA, no por lead.',
      gancho='Profe muy cerca, bajo: "No te voy a decir que es fácil." Texto grande: "Lo que NO te prometemos".')

guion(6, 'EL VIDEO DE HOY', 'PRIORITARIO', 'El acompañamiento diario: cada estudiante graba un video corto todos los días y el profe le dice qué mejorar. Antes y después real.',
      'Uno de los 3 estudiantes del grupo que empezó de cero en Heiiu (cláusula de imagen + autorización escrita para usar sus dos videos): 5 segundos de su video de entrada en A1 (día 1) y 5 segundos hablando hoy en B1 (grabado mañana o de su portafolio reciente). Luego el profe a cámara.', '25-30 s',
      'Pantalla partida o corte seco: "Día 1" / "Hoy" (con el dato real: "hace ___ meses", se llena con la fecha de matrícula del estudiante). Luego el profe, con el celular en la mano, mostrando (sin que se lea el nombre) el chat donde manda la corrección.',
      ['(video día 1 en A1, 5 s) (video de hoy en B1, 5 s)',
       'Profe: Esto no pasa solo por venir a clase. Pasa porque todos los días graba un minuto, me lo manda, y yo le digo exactamente qué corregir. Al día siguiente, otra vez.',
       'Un profesor que te acompaña todos los días. Eso es lo que compras aquí.'],
      '"Día 1" · "Hoy (hace ___ meses)" · "Un video al día. Un profesor que lo revisa."',
      '"¿Quieres que te acompañen así? Escríbenos." Botón: WhatsApp.',
      'Solo con autorización escrita del estudiante para usar sus dos videos. Si se puede, grabar los 3 (tres piezas distintas con el mismo guion: Meta premia conceptos y caras distintas).',
      gancho='Segundo 0: su video de entrada, nervioso, sin poder terminar la frase. Texto grande: "Día 1." Corte seco al de hoy hablando de corrido: "Hoy."')

guion(7, 'SU HIJO A LOS 18', 'ALTERNO (para el grupo de la tarde y el sabatino)', 'Padres: el inglés resuelto antes de la universidad, y la disciplina que se entrena aquí.',
      'Coordinación (Jacqueline) a cámara, en la recepción, hablando a un papá o mamá. Si hay un padre voluntario con cláusula, mejor él.', '25 s',
      'Plano medio fijo; corte de 3 segundos a jóvenes de 15-17 en clase (de espaldas o con autorización).',
      ['Imagínese a su hijo a los dieciocho con el inglés resuelto: la universidad o la beca sin ese requisito pendiente.',
       'Y algo que los papás nos agradecen más que el inglés: aquí se entrena constancia. Un video al día, asistencia, tareas. Lo que aprende de cumplir le sirve para todo.',
       'Desde los doce años, en la tarde, en la noche o los sábados.'],
      '"Desde los 12 años" · "Tarde · noche · sábados" · "Garantía por escrito"',
      '"Pregúntenos qué horario le sirve a su hijo. Escríbanos." Botón: WhatsApp.',
      'El grupo de la tarde está "en apertura": el anuncio no promete horario fijo; el agente captura la franja.',
      gancho='Texto grande sobre jóvenes en clase: "A los 18, con el inglés resuelto."')

h('CHECKLIST DEL DÍA DE GRABACIÓN', 12)
for t in ['• Vertical 9:16, subtítulos grandes desde el primer segundo, sin música encima de la voz en los guiones 1, 5 y 6.',
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
