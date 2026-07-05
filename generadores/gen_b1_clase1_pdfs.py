#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""
B1 MASTERY - Clase 1
Genera 4 PDFs blanco y negro listos para imprimir:
- B1_Clase1_GRAMMAR_GUIA.pdf (multi-pagina)
- B1_Clase1_CONV_GUIA.pdf (multi-pagina)
- B1_Clase1_GRAMMAR_REPORTE.pdf (1 hoja, no editable, para escribir a mano)
- B1_Clase1_CONV_REPORTE.pdf (1 hoja, no editable, para escribir a mano)
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import black, white, HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, PageBreak)
from reportlab.pdfgen import canvas
import os, re

GRAY = HexColor('#555555')
LIGHT = HexColor('#e8e8e8')
DARKBOX = HexColor('#1a1a1a')
w, h = letter

styles = getSampleStyleSheet()
for n, fs, ld, f, c, sb, sa in [
    ('T1', 16, 19, 'Helvetica-Bold', black, 0, 3),
    ('Sub', 8.5, 10.5, 'Helvetica-Oblique', GRAY, 0, 5),
    ('SH', 11, 13, 'Helvetica-Bold', black, 8, 3),
    ('AT', 9, 11, 'Helvetica-Bold', black, 6, 2),
    ('B', 8, 10.5, 'Helvetica', black, 0, 2),
    ('BB', 8, 10.5, 'Helvetica-Bold', black, 0, 2),
    ('BI', 7.5, 9.5, 'Helvetica-Oblique', GRAY, 0, 1.5),
    ('SM', 7, 9, 'Helvetica', GRAY, 0, 1),
    ('TC', 7.5, 9.5, 'Helvetica', black, 0, 0),
    ('TCB', 7.5, 9.5, 'Helvetica-Bold', black, 0, 0),
    ('TH', 7.5, 9.5, 'Helvetica-Bold', white, 0, 0),
    ('Box', 7.5, 9.5, 'Helvetica', black, 0, 1),
]:
    if n not in styles.byName:
        styles.add(ParagraphStyle(n, parent=styles['Normal'], fontSize=fs,
            leading=ld, fontName=f, textColor=c, spaceBefore=sb, spaceAfter=sa))

def box_bw(text, border_thick=1.0):
    t = Table([[Paragraph(text, styles['Box'])]], colWidths=[7.2 * inch])
    t.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), border_thick, black),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    return t

def gray_box(text):
    """Caja con fondo gris claro para destacar."""
    t = Table([[Paragraph(text, styles['Box'])]], colWidths=[7.2 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT),
        ('BOX', (0, 0), (-1, -1), 0.5, black),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    return t

# =========================================================================
# GUIA - GRAMMAR & WRITING
# =========================================================================
def build_grammar_guide():
    out = 'B1/B1_Clase1_GRAMMAR_GUIA.pdf'
    doc = SimpleDocTemplate(out, pagesize=letter,
        topMargin=0.45*inch, bottomMargin=0.4*inch,
        leftMargin=0.5*inch, rightMargin=0.5*inch)
    s = []

    s.append(Paragraph('B1 MASTERY - CLASE 1 - BLOQUE 1: GRAMMAR &amp; WRITING', styles['T1']))
    s.append(Paragraph('Sesion 1 de 44 | Duracion 1h50min (8:00-9:50) | Profesor: __________________ | Fecha: ___/___/___ | Presentes: ___/16',
        styles['Sub']))

    s.append(box_bw(
        '<b>PRINCIPIOS DE ESTE BLOQUE:</b> En Bloque 1 los estudiantes ESCRIBEN. Aqui se hace la parte escrita del proyecto. '
        'Aqui se revisa el cuaderno de GoldList. Aqui se permite espanol brevemente para desbloquear. La precision importa, '
        'la accountability importa. Pero la energia no se baja: ninguna actividad dura mas de 20 min.', 1.0))
    s.append(Spacer(1, 4))

    s.append(box_bw(
        '<b>CORRECCION:</b> Di: "No." Luego: "Listen." + version correcta lento + el estudiante repite 2 veces. NO expliques POR QUE. '
        '<b>ERROR PAPER:</b> Hoja en blanco + lapicero durante cada actividad oral. Anota cada error. '
        '<b>SI UNA ACTIVIDAD SE PASA, CORTALA.</b> Di "Tiempo" y pasa a la siguiente.', 1.0))
    s.append(Spacer(1, 4))

    s.append(box_bw(
        '<b>NO NEGOCIABLE:</b> VATS, GoldList, autochequeo y socializacion de tarea SIEMPRE. '
        'NO comuniques info sobre evaluaciones/midterms/finales - eso lo hace coordinacion. '
        '<b>SIGUE LA GUIA AL PIE.</b> No improvises, no agregues contenido fuera de lo planificado.', 1.5))
    s.append(Spacer(1, 6))

    # ESTRUCTURA
    s.append(Paragraph('ESTRUCTURA DEL BLOQUE', styles['SH']))
    header = [Paragraph('<b>#</b>', styles['TH']), Paragraph('<b>Tiempo</b>', styles['TH']),
              Paragraph('<b>Bloque</b>', styles['TH']), Paragraph('<b>Min</b>', styles['TH'])]
    rows = [header]
    for i, (t, b, m) in enumerate([
        ('00:00-00:07', 'VATS - Prudencia', '7'),
        ('00:07-00:25', 'Carta a Mi Yo del Futuro (especial Clase 1)', '18'),
        ('00:25-00:50', 'Speaking Circle - diagnostico encubierto', '25'),
        ('00:50-01:00', 'GoldList Notebook entrega + 5 frases', '10'),
        ('01:00-01:20', 'Diagnostico Present Perfect vs Past Simple', '20'),
        ('01:20-01:35', 'Writing - "My English Story"', '15'),
        ('01:35-01:45', 'Error Paper introduccion', '10'),
        ('01:45-01:50', 'Tarea + Wrap', '5'),
    ], 1):
        rows.append([Paragraph(str(i), styles['TC']), Paragraph(t, styles['TC']),
                     Paragraph(b, styles['TC']), Paragraph(m, styles['TC'])])
    t = Table(rows, colWidths=[0.3*inch, 1.0*inch, 5.5*inch, 0.4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARKBOX),
        ('GRID', (0, 0), (-1, -1), 0.4, black),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    s.append(t)

    # ACTIVIDADES
    activities = [
        ('1. VATS - PRUDENCIA (00:00-00:07, 7 min)', [
            '<b>Esta semana toda la academia trabaja PRUDENCIA. La virtud rota cada semana - Prudencia, Templanza, Justicia, Fortaleza.</b>',
            'Escribe en el tablero: <b>PRUDENCIA</b> - "Es mas prudente practicar 30 min cada dia, o 3 horas un solo dia a la semana?"',
            '<b>V - Virtud (1 min):</b> Lee la pregunta. Di: "PRUDENCIA es la habilidad de pensar antes de actuar y elegir lo bueno a largo plazo, no solo lo que se siente bien ahora."',
            '<b>A - Activar (30 seg):</b> "Piensen en silencio. NO hablen todavia."',
            '<b>T - Talk en parejas (2 min):</b> "Parejas. Discutan. Pueden usar espanol pero traten AL MENOS UNA frase en ingles. Ejemplo: I think 30 minutes every day is better."',
            '<b>S - Share (2.5 min):</b> 3 estudiantes comparten. Celebra cualquier intento en ingles.',
            '<b>Cierre (1 min):</b> "Esta semana es PRUDENCIA. La van a ver en cada clase. Hoy van a tomar UNA decision prudente: comprometerse con un horario realista de practica."',
            ('SmallNote', 'El VATS es el ritual diario de Heiiu. NUNCA se salta. Si el bloque va tarde, recortas otra cosa, no esto.'),
        ]),
        ('2. CARTA A MI YO DEL FUTURO (00:07-00:25, 18 min)', [
            '<b>** MOMENTO ESPECIAL. Es emocional, no academico. Hazlo con calma y seriedad.</b>',
            'Di: "Antes de empezar el contenido del nivel, vamos a hacer algo especial que solo se hace UNA vez en todo el journey de B1. Van a escribir una carta a su YO DEL FUTURO - al que va a estar aqui cuando se graduen."',
            '<b>Explicar (2 min):</b> "Escriban una carta en ESPANOL. Dirijanla a ustedes mismos del futuro - dentro de 9 semanas. Por que empezaste B1? Que suenas lograr al final? Que te da miedo? Que quieres que tu yo del futuro recuerde?"',
            '<b>Adicion B1:</b> "Al final, escriban UNA SOLA frase en ingles. Una promesa, un sueno, una declaracion."',
            '<b>Escribir (12 min):</b> Pon musica suave. Camina en silencio. NO leas - es privado. Si alguien dice "no se que escribir": "Escribele lo que quieres que tu yo futuro sepa."',
            '<b>Sellar (3 min):</b> Entrega un sobre a cada uno. "Doblen. Metan en el sobre. Escriban su nombre afuera. Sellen." Recoge los 16 sobres.',
            '<b>Compromiso (1 min):</b> "Estos sobres se quedan en la academia. El dia que terminen B1, los abren y leen. Es un contrato emocional con ustedes mismos."',
            ('SmallNote', 'ENTREGABLE: 16 sobres sellados a coordinacion HOY. Los guardan en archivo seguro hasta final del nivel.'),
            ('SmallNote', 'Algunos se van a emocionar. Eso es bueno. Crea un ancla emocional con el programa.'),
        ]),
        ('3. SPEAKING CIRCLE - DIAGNOSTICO ENCUBIERTO (00:25-00:50, 25 min)', [
            '<b>OBJETIVO REAL (NO se le dice al estudiante):</b> Diagnosticar nivel de cada uno. Llamalo "conocernos."',
            '<b>Setup (2 min):</b> "Quiero conocerlos. Cada persona dice 4 cosas: (1) nombre, (2) de donde es, (3) por que esta aqui, (4) un talento secreto. Empieza [Catalina o Miguel - anchor]."',
            '<b>Orden estrategico:</b> Anchors PRIMERO (modelan), luego A2 graduados, luego catch-up, luego nuevos.',
            '<b>Round (22 min):</b> ~80 seg por estudiante x 16 = 22 min.',
            '<b>MIENTRAS HABLAN, TU HACES (silencioso):</b> Lleva lista del cohorte. Marca: nivel oral aparente (Alto/Medio/Bajo). Anota 1 error escuchado. Anota fortalezas (vocab, fluidez, pronunciacion).',
            '<b>Reglas:</b> NO corrijas durante esta actividad. Si alguien se traba, di "Take your time. You can use one Spanish word if you need." Aplaude cuando termina cada uno.',
            '<b>Cierre (1 min):</b> "Gracias. Ya se un poco de cada uno."',
            ('SmallNote', 'REPORTE: Las observaciones de este Speaking Circle van al reporte AL FINAL del bloque. Coordinacion las usa para personalizar.'),
        ]),
        ('4. GOLDLIST NOTEBOOK (00:50-01:00, 10 min)', [
            '<b>Setup (3 min):</b> "Cada uno recibe un cuaderno especial - su GoldList Notebook. NO es para tareas. NO es para gramatica. Es solo para una cosa: GoldList."',
            'Reparte los 16 cuadernos.',
            '<b>Explicar (3 min):</b> "El cuaderno se queda en la academia. Cada lunes reciben 5 frases del profesor. Las escriben asi: izquierda = ingles, derecha = traduccion. 25 frases por mes. NO las van a estudiar. NO van a memorizar. El profesor las usa naturalmente. Por absorcion aprenderan. Cada 14 dias revisamos y destilamos las que ya saben."',
            '<b>Primeras 5 frases (4 min):</b> Conectan con PRUDENCIA. Di una a una en ingles, repiten, escriben:',
            '1. <i>I plan ahead before I act.</i> - Yo planeo antes de actuar.',
            '2. <i>Slow and steady wins the race.</i> - Lento pero seguro gana la carrera.',
            '3. <i>I think twice before I speak.</i> - Pienso dos veces antes de hablar.',
            '4. <i>Discipline is freedom.</i> - La disciplina es libertad.',
            '5. <i>Small steps every day beat big steps once.</i> - Pequenos pasos diarios son mejores que un paso grande de vez en cuando.',
            ('SmallNote', 'Las 5 frases conectan con PRUDENCIA a proposito. La virtud esta en su vocabulario sin que se den cuenta. Recoge los cuadernos al final del bloque.'),
        ]),
        ('5. DIAGNOSTICO PRESENT PERFECT vs PAST SIMPLE (01:00-01:20, 20 min)', [
            '<b>Por que esta gramatica:</b> Es la bisagra A2-B1. Si la dominan, listos para B1. Si no, hay que reforzar.',
            '<b>Setup (1 min):</b> "Voy a escribir 5 oraciones. Algunas estan bien, otras tienen errores. Diran cual y POR QUE."',
            'Escribe en el tablero:',
            '1. <i>I have lived in Bucaramanga for 10 years.</i>',
            '2. <i>Yesterday I have gone to the supermarket.</i>',
            '3. <i>She has finished her homework already.</i>',
            '4. <i>I have seen that movie last week.</i>',
            '5. <i>They have been friends since 2015.</i>',
            '<b>Discusion guiada (12 min):</b> Una a una. ANTES de dar respuesta, deja que 2-3 estudiantes opinen. Anchors van SEGUNDO (no monopolicen). Solo cuando hay consenso o silencio, das la respuesta:',
            '1: OK (accion que continua) | 2: MAL - <i>Yesterday I went</i> (tiempo especifico = past simple) | 3: OK (already con perfect) | 4: MAL - <i>I saw that movie last week</i> (tiempo especifico) | 5: OK (since + estado continuo)',
            '<b>Regla en el tablero (3 min):</b> Tiempo especifico (yesterday, last week, in 2020) = PAST SIMPLE. Sin tiempo especifico, o for/since/already/yet/ever = PRESENT PERFECT.',
            '<b>Challenge tier para anchors (4 min):</b> Mientras el resto copia la regla, di a Catalina/Miguel/Sofia: "3 oraciones mas, en su cuaderno propio. Una con just, una con never, una con for. Pasenmelas en 2 min."',
            ('SmallNote', 'Si la mitad de la clase no entiende ni la regla simple, el martes se vuelve a tratar. Si la mayoria entiende, el martes se avanza.'),
        ]),
        ('6. WRITING - "MY ENGLISH STORY" (01:20-01:35, 15 min)', [
            '<b>Setup (2 min):</b> "Ahora vamos a escribir. En el cuaderno propio (NO el de GoldList). 5 a 7 oraciones sobre My English Story. Pueden incluir: cuando empezaron, que los motivo, momento mas dificil, que quieren lograr en B1. USEN present perfect Y past simple. Por lo menos UNA de cada uno."',
            '<b>Escribir (10 min):</b> Silencio total. Camina en silencio. Si alguien se traba: "Empieza con I started learning English when... o I have been studying for..."',
            '<b>Recoleccion (3 min):</b> "Pongan su nombre arriba. Levanten la mano cuando terminen."',
            '<b>Anchors:</b> Catalina, Miguel, Sofia: pideles 8-10 oraciones. <b>Catch-up:</b> 3 oraciones esta bien. NO presionar.',
            ('SmallNote', 'ENTREGABLE: Recoger 16 escritos. PRIMERA materia prima del proyecto My Story My Goals. La proxima clase se devuelven con feedback.'),
        ]),
        ('7. ERROR PAPER - INTRODUCCION (01:35-01:45, 10 min)', [
            '<b>Setup (3 min):</b> "Durante el Speaking Circle anote errores que escuche. NO digo de quien. Vamos a corregirlos juntos. Esto se llama Error Paper, va a pasar en cada clase."',
            'Escribe en el tablero 4-5 errores reales que anotaste. Ejemplos tipicos:',
            '<i>"I have lived here since 10 years"</i> (debe ser FOR 10 years)',
            '<i>"Yesterday I have eaten pizza"</i> (past simple, no perfect)',
            '<i>"He don\'t speak English"</i> (doesn\'t)',
            '<i>"I am living here from 2020"</i> (since 2020)',
            '<b>Correccion colectiva (5 min):</b> Pregunta: "Que esta mal en #1?" Anchors van SEGUNDO. Cuando alguien dice la version correcta: "Yes. Repeat 2x. Everyone repeats."',
            '<b>Cierre (2 min):</b> "Yo NUNCA voy a decir quien hizo cada error. Es anonimo. Si tienen miedo de hablar porque pueden equivocarse, recuerden: el error de hoy es la correccion de manana."',
            ('SmallNote', 'NUNCA cobres errores personalmente delante del grupo. Anonimo siempre.'),
        ]),
        ('8. TAREA + WRAP (01:45-01:50, 5 min)', [
            '<b>Tarea para manana (escribe en tablero):</b>',
            '1. <b>Escuchar:</b> Video corto en YouTube en ingles (3-5 min). Apuntar 5 palabras NUEVAS en su cuaderno.',
            '2. <b>Escribir:</b> Respuesta corta (3 oraciones) a "What is one prudent decision I will make this week about my English?"',
            '3. <b>GoldList:</b> No hacer nada con el cuaderno - se queda en la academia.',
            '<b>Cierre:</b> "Manana es Bloque 2 - solo conversacion, solo ingles. Despues de break vienen al Bloque 2 con [profesor 2]. Disfruten ese bloque, es muy diferente."',
            '"Recuerden: PRUDENCIA esta semana. Una pequena decision prudente cada dia = gran cambio en B1."',
            'Recoge los cuadernos de GoldList.',
        ]),
    ]

    for title, lines in activities:
        s.append(Paragraph(title, styles['AT']))
        for line in lines:
            if isinstance(line, tuple) and line[0] == 'SmallNote':
                s.append(Paragraph(f'> {line[1]}', styles['BI']))
            else:
                s.append(Paragraph(line, styles['B']))

    s.append(Spacer(1, 6))
    s.append(Paragraph('ENTREGABLES PARA COORDINACION (al final del bloque)', styles['SH']))
    for item in [
        '[ ] 16 sobres sellados de "Carta a Mi Yo del Futuro"',
        '[ ] 16 escritos "My English Story"',
        '[ ] 16 cuadernos de GoldList con las primeras 5 frases',
        '[ ] Reporte lleno (formato impreso) con observaciones del Speaking Circle',
        '[ ] Lista de quienes NO entregaron tarea (si aplica - primera clase, todos arrancan limpio)',
    ]:
        s.append(Paragraph(item, styles['B']))

    s.append(Spacer(1, 6))
    s.append(gray_box(
        '<b>REGLA DE ORO PARA ESTE BLOQUE:</b> El estudiante debe terminar este bloque sintiendo que '
        '(1) lo conocen, (2) hay un sistema serio, (3) la escritura importa, (4) el cuaderno de GoldList es nuevo y especial, '
        '(5) hay una virtud que va a vivir esta semana. NO debe sentir que esto es "repaso" o "regreso a A2."'))

    doc.build(s)
    with open(out, 'rb') as f:
        pages = len(re.findall(rb'/Type\s*/Page[^s]', f.read()))
    print(f'OK: {out} - {pages} pag')


# =========================================================================
# GUIA - CONVERSACIONAL
# =========================================================================
def build_conv_guide():
    out = 'B1/B1_Clase1_CONV_GUIA.pdf'
    doc = SimpleDocTemplate(out, pagesize=letter,
        topMargin=0.45*inch, bottomMargin=0.4*inch,
        leftMargin=0.5*inch, rightMargin=0.5*inch)
    s = []

    s.append(Paragraph('B1 MASTERY - CLASE 1 - BLOQUE 2: CONVERSACIONAL', styles['T1']))
    s.append(Paragraph('Sesion 1 de 44 | Duracion 1h50min (10:10-12:00) | Profesor: __________________ | Fecha: ___/___/___ | Presentes: ___/16',
        styles['Sub']))

    s.append(box_bw(
        '<b>PRINCIPIOS DE ESTE BLOQUE:</b> En Bloque 2 se HABLA. Solo ingles (English-only). NO libros. NO espanol (excepto desbloqueo extremo). '
        'Aqui ocurren presentaciones, debates, juegos, simulaciones. La precision NO es el foco - la fluidez y el riesgo lo son. '
        'El profesor corrige pero NO explica gramatica. Si preguntan "why": "Ask in Block 1 tomorrow."', 1.0))
    s.append(Spacer(1, 4))

    s.append(box_bw(
        '<b>CORRECCION:</b> Di: "No." Luego: "Listen." + version correcta + el estudiante repite 2 veces. NO expliques POR QUE. '
        '<b>ERROR PAPER:</b> Hoja en blanco + lapicero. Anota cada error. '
        '<b>SI UNA ACTIVIDAD SE PASA, CORTALA.</b> Di "Tiempo" y pasa.', 1.0))
    s.append(Spacer(1, 4))

    s.append(box_bw(
        '<b>NO NEGOCIABLE:</b> VATS, English Points, autochequeo y socializacion de tarea SIEMPRE. '
        'NO comuniques info sobre evaluaciones - eso lo hace coordinacion. <b>SIGUE LA GUIA AL PIE.</b>', 1.5))
    s.append(Spacer(1, 6))

    s.append(gray_box(
        '<b>REGLA DE ORO PARA ESTE BLOQUE - ESCRIBE EN EL TABLERO AL ENTRAR:</b><br/>'
        'THIS BLOCK: ENGLISH ONLY<br/>'
        '- If you don\'t know a word, describe it<br/>'
        '- If you don\'t know how to say it, use simpler English<br/>'
        '- If you really need Spanish: say "May I use Spanish?" in English first<br/><br/>'
        '<b>ENGLISH POINTS:</b> Empiezan en 0. Anota en tablero. Cada uso de espanol sin permiso = -1 al grupo. '
        'Cada anchor que ayuda a nuevo en ingles = +2 al grupo. Si terminan con &gt;=10 puntos, "win" - aplauso celebratorio.'))
    s.append(Spacer(1, 6))

    # ESTRUCTURA
    s.append(Paragraph('ESTRUCTURA DEL BLOQUE', styles['SH']))
    header = [Paragraph('<b>#</b>', styles['TH']), Paragraph('<b>Tiempo</b>', styles['TH']),
              Paragraph('<b>Bloque</b>', styles['TH']), Paragraph('<b>Min</b>', styles['TH'])]
    rows = [header]
    for i, (t, b, m) in enumerate([
        ('00:00-00:07', 'VATS RECONNECT - oral, English-only', '7'),
        ('00:07-00:20', 'Icebreaker - "If you... stand up"', '13'),
        ('00:20-00:40', 'Hot Topic - debate corto en parejas', '20'),
        ('00:40-01:00', 'TBLT - "Design Your Perfect English Week"', '20'),
        ('01:00-01:20', 'Anuncio Proyecto - "MY STORY, MY GOALS"', '20'),
        ('01:20-01:35', 'Juego - Two Truths and a Lie', '15'),
        ('01:35-01:45', 'Error Paper LIVE - correccion oral', '10'),
        ('01:45-01:50', 'Exit Ticket + Tarea', '5'),
    ], 1):
        rows.append([Paragraph(str(i), styles['TC']), Paragraph(t, styles['TC']),
                     Paragraph(b, styles['TC']), Paragraph(m, styles['TC'])])
    t = Table(rows, colWidths=[0.3*inch, 1.0*inch, 5.5*inch, 0.4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARKBOX),
        ('GRID', (0, 0), (-1, -1), 0.4, black),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    s.append(t)

    activities = [
        ('1. VATS RECONNECT - ORAL, ENGLISH-ONLY (00:00-00:07, 7 min)', [
            '<b>Setup (1 min):</b> Entra al salon con energia. Di in English: "Welcome back. Block 1 is over. This is Block 2. Different rules. ENGLISH ONLY."',
            '<b>Reconectar con la virtud (5 min):</b> Escribe en tablero: "PRUDENCE - the strength to think before acting. This week, I will make ONE prudent decision about my English."',
            'Di: "In Block 1 you talked about PRUDENCIA. Now we say it in English: PRUDENCE. Same idea. This week, every decision you make about your English: be prudent."',
            '<b>T - Talk (3 min):</b> "Pairs. Tell your partner ONE prudent decision YOU will make THIS WEEK about your English. Real, specific, small. English only." Si alguien dice "I will study more": "More specific. When? How long? Where?"',
            '<b>S - Share (1 min):</b> 2 estudiantes comparten su decision.',
            ('SmallNote', 'Aqui es donde el VATS deja de ser teorico y se vuelve compromiso oral. El estudiante DICE en voz alta. Eso lo hace mas real.'),
        ]),
        ('2. ICEBREAKER - "IF YOU... STAND UP" (00:07-00:20, 13 min)', [
            '<b>OBJETIVO:</b> Romper hielo, conocerse, mover el cuerpo, escuchar ingles rapido.',
            '<b>Setup (2 min):</b> "Everybody stand up. Push your chair back. Make space. I will say sentences starting with IF YOU... If true for YOU, you STAY standing. If not, you SIT DOWN."',
            '<b>Demostracion (1 min):</b> "If you have eaten breakfast today, stay standing." Aplaude. "If you didn\'t sleep well last night, sit down."',
            '<b>Round 1 - Datos basicos (4 min):</b> Una por una, deja 5 seg entre cada una:',
            '- "If you have a pet at home, stay standing."',
            '- "If you have lived in another city in Colombia, stay standing."',
            '- "If you have traveled outside Colombia, stay standing."',
            '- "If you have studied English for more than 2 years, stay standing."',
            '- "If you have worked in a job that uses English, stay standing."',
            '<b>Round 2 - Mas profundo (4 min):</b>',
            '- "If you can cook a complete meal, stay standing."',
            '- "If you have ever performed in front of an audience, stay standing."',
            '- "If you read books in English, stay standing."',
            '- "If you have a goal to live or work abroad, stay standing."',
            '- "If you are nervous about speaking English in this class, stay standing."',
            '<b>Cierre (2 min):</b> "Sit down. Look around. We have a diverse group. Different stories, different goals. THAT is what makes a good class."',
            ('SmallNote', 'Para el catch-up student: si se siente perdido, no lo senales. Di al grupo: "Anchor next to a new student - help if needed. In English."'),
        ]),
        ('3. HOT TOPIC - "WHAT IS HARD ABOUT LEARNING ENGLISH?" (00:20-00:40, 20 min)', [
            '<b>Setup (2 min):</b> "What is the HARDEST thing about learning English for YOU? Personally?" Escribe en tablero: "HOT TOPIC: What is hard about learning English?"',
            '<b>Pairs discussion (10 min):</b> "Pairs. Anchor + non-anchor. Discuss for 8 minutes. ENGLISH ONLY. If you don\'t know a word, describe it."',
            '<b>Empareja activamente:</b> Catalina+Catch-up | Miguel+nuevo | Sofia+A2 graduado | Daniela+ alguien | Alejandro+alguien. Numero impar = grupo de 3 con anchor.',
            '<b>Mientras caminan, tu haces 4 cosas:</b> (1) Anota errores en Error Paper. (2) Asigna English Points cuando anchor ayuda. (3) Espanol sin permiso = -1 grupo. (4) Si alguien callado: "What did your partner say?" - fuerzalo a producir.',
            '<b>Share whole group (8 min):</b> "Stop. ONE thing your PARTNER said about what\'s hard. Not what YOU said - what your partner said." Esto fuerza que escucharon. ~30 seg por pareja.',
            ('SmallNote', 'NO es para corregir gramatica. Es para que produzcan, escuchen, se conecten. Anota errores en silencio. Los abordas en Error Paper Live al final.'),
        ]),
        ('4. TBLT - "DESIGN YOUR PERFECT ENGLISH WEEK" (00:40-01:00, 20 min)', [
            '<b>OBJETIVO:</b> Tarea comunicativa real con producto medible. Conecta con PRUDENCIA - planificar bien la semana.',
            '<b>Setup (2 min):</b> "Now we plan. Each pair will design THE PERFECT ENGLISH WEEK. 7 days. From Monday to Sunday. What will you do EACH day to improve your English?"',
            '<b>Reglas en el tablero:</b> 7 actividades (una por dia) | Al menos 3 formatos diferentes (speaking/listening/reading/writing) | Realista - deben poder hacerlo | Cada dia: minimo 30 minutos | Ultima actividad domingo: REVIEW the week',
            '<b>Trabajar (12 min):</b> Mismas parejas del Hot Topic. "12 minutes. Make a clear plan. Use a piece of paper. 7 days, 7 activities."',
            '<b>Camina y escucha. Asigna English Points por:</b> vocabulario rico, frases en present perfect bien usadas (acaban de aprenderlo), anchor ayudando.',
            '<b>Presentar (6 min):</b> Cada pareja: 30 segundos. UNA persona habla. "ONE person from each pair presents. The OTHER will go in the next activity." Esto entrena Public Speaking en pequenas dosis (la soft skill destacada).',
        ]),
        ('5. PROYECTO ANUNCIO - "MY STORY, MY GOALS" (01:00-01:20, 20 min)', [
            '<b>Por que este momento:</b> Los estudiantes deben saber DESDE LA CLASE 1 que hay proyecto largo, midterm, final. Da estructura emocional al journey.',
            '<b>Anuncio (3 min):</b> Escribe en tablero: "PROJECT: MY STORY, MY GOALS. Sessions 1-22: collect material, build draft, practice. Session 22: MIDTERM (5 min each). Sessions 23-43: refine. Session 44: FINAL (7-10 min each)."',
            'Di: "From day one, you are building toward your Midterm in week 4 and your Final in week 9. Every Block 1 you write a piece. Every Block 2 you practice presenting. Today: first piece."',
            '<b>Brainstorm (10 min):</b> "Take 10 minutes. Alone. Pencil on paper. Answer 4 questions: (1) WHO am I? 3 things - not name and age - REAL things. (2) WHAT is my English STORY? when started, why, key moments. (3) WHAT is my BIGGEST GOAL with English? (4) WHAT do I want my future self to know about this moment?"',
            '<b>Compartir parcial (5 min):</b> "Pairs. Read your answer to question 4 to your partner. Just question 4."',
            '<b>Anchors (Catalina/Miguel/Sofia):</b> usen vocabulary B2-tier, estructuras complejas. <b>Catch-up:</b> minimo 1 oracion por pregunta.',
            '<b>Cierre (2 min):</b> "This paper goes home with you tonight. Tomorrow in Block 1, you will use it to write the FIRST page of your project. Don\'t lose it."',
            ('SmallNote', 'Block 1 manana usa este papel como insumo. Coordina con el otro profesor.'),
        ]),
        ('6. JUEGO - TWO TRUTHS AND A LIE (01:20-01:35, 15 min)', [
            '<b>OBJETIVO:</b> Rebajar la energia formal, conocerse mejor, producir oraciones complejas, divertirse.',
            '<b>Setup (2 min):</b> "Game time. Each person says 3 sentences about themselves. Two TRUE, one LIE. The group guesses which is the lie. Realistic - not from Mars. We catch your lie = we win. We don\'t = you win."',
            '<b>Demostracion (1 min):</b> Modela tu primero. Que el grupo adivine. Hazlo divertido.',
            '<b>Round (12 min):</b> ~45 seg por estudiante x 16 = 12 min. Cada uno dice sus 3 oraciones. Grupo vota mano alzada: "Who thinks #1 is the lie? #2? #3?" Estudiante revela. Aplauso.',
            '<b>Reglas extra:</b> 3 oraciones con verbos diferentes (no las 3 con "I have"). Anchors: usen present perfect en al menos 1 (acaban de aprenderlo). Catch-up: 2 oraciones esta bien.',
            '<b>Para anchors:</b> despues del round normal, exigir UNA oracion extra usando tiempo complejo (past perfect, future perfect, conditional).',
            ('SmallNote', 'Anota en silencio errores en tu Error Paper. Va a haberlos. Los corriges en el siguiente bloque.'),
        ]),
        ('7. ERROR PAPER LIVE - CORRECCION ORAL (01:35-01:45, 10 min)', [
            '<b>Setup (1 min):</b> "I heard everything you said today. I wrote down 5 errors. Anonymous - I won\'t say who. We will fix them together."',
            'Escribe en tablero los 5 errores reales que anotaste. Ejemplos tipicos en Clase 1 B1:',
            '<i>"I have studied English since 5 years"</i> -&gt; since FIVE YEARS AGO o FOR 5 years',
            '<i>"Yesterday I have gone to the gym"</i> -&gt; past simple',
            '<i>"He don\'t like coffee"</i> -&gt; doesn\'t',
            '<i>"I\'m boring"</i> -&gt; BORED (different meaning)',
            '<i>"My english is no very good"</i> -&gt; not very good',
            '<b>Correccion colectiva (8 min):</b> "What\'s wrong with #1?" Espera. Deja silencio. Si nadie responde: "Hint: it\'s about TIME." Cuando alguien dice la correccion: "YES. Repeat 2x. Everyone repeats 2x." Anchors van segundo (no monopolicen).',
            '<b>Cierre (1 min):</b> "These mistakes are normal. They are the road. The student who makes the mistake today is the student who fixes it tomorrow. Tomorrow you will hear me say No. Listen. Yesterday I WENT to the gym. That\'s the correction. Repeat. Move on. No shame, just learning."',
            ('SmallNote', 'ESTE es el ritual de correccion de Heiiu. Profesor 2 (corrector) lo hace cada clase. Profesor 1 (gramatica) lo hace en Bloque 1 con la lista que le pasa Profesor 2.'),
        ]),
        ('8. EXIT TICKET + TAREA (01:45-01:50, 5 min)', [
            '<b>English Points final (1 min):</b> Cuenta los puntos del grupo en el tablero. Si &gt;=10, celebracion (aplauso 10 seg). Si &lt;10, "Tomorrow we do better. The goal is 15."',
            '<b>Tarea para manana (2 min):</b>',
            '1. <b>Block 1 prep:</b> Bring your "MY STORY, MY GOALS" brainstorm paper. Tomorrow you write the first page of the project.',
            '2. <b>Listening:</b> Watch a 2-3 min video in English. Note 3 phrases you like.',
            '3. <b>Reflection in English:</b> Write 2 sentences (English) about today\'s class. What was new? What surprised you?',
            '<b>Exit Ticket (2 min):</b> Reparte papelito. Cada estudiante escribe: una palabra en ingles que define como se sintio hoy + una pregunta (espanol o ingles). Recoge los 16. Lee esta noche. Comparte temas comunes con coordinacion.',
        ]),
    ]

    for title, lines in activities:
        s.append(Paragraph(title, styles['AT']))
        for line in lines:
            if isinstance(line, tuple) and line[0] == 'SmallNote':
                s.append(Paragraph(f'> {line[1]}', styles['BI']))
            else:
                s.append(Paragraph(line, styles['B']))

    s.append(Spacer(1, 6))
    s.append(Paragraph('ENTREGABLES PARA COORDINACION (al final del bloque)', styles['SH']))
    for item in [
        '[ ] Reporte lleno (formato impreso) con observaciones del bloque',
        '[ ] Lista de errores recurrentes para el Error Paper de manana (Bloque 1)',
        '[ ] 16 Exit Tickets con palabra+pregunta de cada estudiante',
        '[ ] Notas sobre dinamica de parejas (que emparejamientos funcionaron)',
        '[ ] English Points totales del bloque',
    ]:
        s.append(Paragraph(item, styles['B']))

    s.append(Spacer(1, 6))
    s.append(gray_box(
        '<b>REGLA DE ORO PARA ESTE BLOQUE:</b> El estudiante debe terminar este bloque sintiendo que '
        '(1) hablo mucho ingles, (2) no fue reganado, (3) los errores se corrigen sin verguenza, '
        '(4) hay un proyecto grande por delante, (5) la clase es divertida y activa, no aburrida y sentada.'))

    doc.build(s)
    with open(out, 'rb') as f:
        pages = len(re.findall(rb'/Type\s*/Page[^s]', f.read()))
    print(f'OK: {out} - {pages} pag')


# =========================================================================
# REPORTE - 1 HOJA, B&W, NO EDITABLE (para imprimir y llenar a mano)
# =========================================================================
def build_report_bw(block_name, blocks_list, observations, output_path, sesion=1):
    """Reporte en 1 hoja, blanco y negro, lineas en blanco para escribir."""
    c = canvas.Canvas(output_path, pagesize=letter)
    margin_l = 0.5 * inch
    margin_r = 0.5 * inch
    page_w = w - margin_l - margin_r
    y = h - 0.4 * inch

    # HEADER
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(margin_l, y, f'B1 MASTERY - REPORTE BLOQUE {block_name} - SESION {sesion}')
    y -= 12
    c.setFont('Helvetica-Oblique', 7.5)
    c.setFillColor(GRAY)
    c.drawString(margin_l, y, 'Confidencial - Entregar a coordinacion al final del bloque - Imprimir y llenar a mano')
    y -= 14

    # METADATA ROW
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l, y, 'Profesor:')
    c.line(margin_l + 50, y - 1, margin_l + 230, y - 1)
    c.drawString(margin_l + 245, y, 'Fecha:')
    c.line(margin_l + 280, y - 1, margin_l + 380, y - 1)
    c.drawString(margin_l + 395, y, 'Presentes:')
    c.line(margin_l + 450, y - 1, margin_l + 490, y - 1)
    c.setFont('Helvetica', 8)
    c.drawString(margin_l + 495, y, '/16')
    y -= 14

    # CHECKLIST DE BLOQUE - 2 columnas
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'CHECKLIST DE BLOQUE - Marca lo que SI ocurrio')
    y -= 16

    c.setFillColor(black)
    c.setFont('Helvetica', 7.5)
    checklist = [
        'VATS al inicio (5-7 min) Prudencia',
        '80% estudiantes hablaron',
        'Todas actividades completadas',
        'Movimiento o cambio de formato',
        'Ninguna actividad &gt;20 min',
        'Error paper anonimo',
        'Tarea revisada (si aplica)',
        'Exit ticket / autochequeo cierre',
    ]
    col_w = page_w / 2
    for i, item in enumerate(checklist):
        col = i % 2
        row = i // 2
        x_pos = margin_l + col * col_w + 4
        # Empty checkbox
        c.rect(x_pos, y - row * 11 - 1, 8, 8, stroke=1, fill=0)
        c.drawString(x_pos + 12, y - row * 11, item)
    y -= (len(checklist) // 2) * 11 + 4

    # BLOQUES DE LA SESION
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'BLOQUES DE LA SESION - Marca cada uno realizado')
    y -= 16

    c.setFillColor(black)
    c.setFont('Helvetica', 7)
    for tiempo, titulo in blocks_list:
        c.rect(margin_l + 4, y - 1, 8, 8, stroke=1, fill=0)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(margin_l + 16, y, tiempo)
        c.setFont('Helvetica', 7)
        c.drawString(margin_l + 70, y, titulo)
        y -= 10
    y -= 4

    # OBSERVACIONES
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'OBSERVACIONES CLAVE - Llenar al final')
    y -= 14

    c.setFillColor(black)
    for title, prompt in observations:
        c.setFont('Helvetica-Bold', 7.5)
        c.drawString(margin_l + 2, y, title + ':')
        c.setFont('Helvetica-Oblique', 6.5)
        c.setFillColor(GRAY)
        c.drawString(margin_l + 2 + c.stringWidth(title + ':', 'Helvetica-Bold', 7.5) + 4, y, prompt)
        c.setFillColor(black)
        y -= 9
        # 2 lines
        for _ in range(2):
            c.line(margin_l + 4, y, margin_l + page_w - 4, y)
            y -= 11
        y -= 1

    # ESTUDIANTES DESTACADOS
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'ESTUDIANTES DESTACADOS HOY (bien o mal) - Solo los que requieren mencion')
    y -= 14

    c.setFillColor(black)
    c.setFont('Helvetica', 7)
    for i in range(1, 5):
        c.drawString(margin_l + 2, y, f'{i}.')
        c.drawString(margin_l + 12, y, 'Nombre:')
        c.line(margin_l + 45, y - 1, margin_l + 175, y - 1)
        c.drawString(margin_l + 180, y, 'Obs:')
        c.line(margin_l + 200, y - 1, margin_l + page_w - 4, y - 1)
        y -= 12

    # AUSENCIAS / TAREA / PASE
    y -= 2
    c.setFont('Helvetica-Bold', 7.5)
    c.drawString(margin_l + 2, y, 'Ausentes:')
    c.line(margin_l + 50, y - 1, margin_l + page_w - 4, y - 1)
    y -= 12

    c.drawString(margin_l + 2, y, 'No hicieron tarea:')
    c.line(margin_l + 90, y - 1, margin_l + page_w - 4, y - 1)
    y -= 14

    # PASE PARA OTRO PROFESOR
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'PASE PARA EL OTRO PROFESOR (lo que necesita saber el otro bloque)')
    y -= 14
    c.setFillColor(black)
    for _ in range(2):
        c.line(margin_l + 4, y, margin_l + page_w - 4, y)
        y -= 12
    y -= 4

    # FIRMA
    c.setFont('Helvetica', 7.5)
    c.drawString(margin_l + 2, y, 'Firma profesor:')
    c.line(margin_l + 75, y - 1, margin_l + 300, y - 1)
    c.drawString(margin_l + 320, y, 'Recibido coordinacion:')
    c.line(margin_l + 425, y - 1, margin_l + page_w - 4, y - 1)

    c.save()
    with open(output_path, 'rb') as f:
        pages = len(re.findall(rb'/Type\s*/Page[^s]', f.read()))
    print(f'OK: {output_path} - {pages} pag')


if __name__ == '__main__':
    os.makedirs('B1', exist_ok=True)
    os.makedirs('B1/reportes', exist_ok=True)

    # GUIAS
    build_grammar_guide()
    build_conv_guide()

    # REPORTES
    grammar_blocks = [
        ('00:00-00:07', 'VATS Prudencia'),
        ('00:07-00:25', 'Carta a Mi Yo del Futuro'),
        ('00:25-00:50', 'Speaking Circle (diagnostico)'),
        ('00:50-01:00', 'GoldList Notebook + 5 frases'),
        ('01:00-01:20', 'Diagnostico Present Perfect'),
        ('01:20-01:35', 'Writing My English Story'),
        ('01:35-01:45', 'Error Paper introduccion'),
        ('01:45-01:50', 'Tarea + Wrap'),
    ]
    grammar_obs = [
        ('Speaking Circle - quienes destacan ALTO',
         'Nombres + por que (fluidez, vocab, pron)'),
        ('Speaking Circle - quienes mas DEBILES',
         'Nombres + observacion para catch-up'),
        ('Diagnostico gramatical', 'Mayoria si / mayoria no / mitad?'),
        ('Errores recurrentes (3-5)',
         'Pasalos al profesor de Bloque 2'),
    ]
    build_report_bw('GRAMMAR & WRITING', grammar_blocks, grammar_obs,
                    'B1/reportes/B1_Clase1_GRAMMAR_REPORTE.pdf')

    conv_blocks = [
        ('00:00-00:07', 'VATS reconnect oral'),
        ('00:07-00:20', 'Icebreaker If You Stand Up'),
        ('00:20-00:40', 'Hot Topic - What is hard about English'),
        ('00:40-01:00', 'TBLT Design Your Perfect English Week'),
        ('01:00-01:20', 'Anuncio Proyecto MY STORY MY GOALS'),
        ('01:20-01:35', 'Juego Two Truths and a Lie'),
        ('01:35-01:45', 'Error Paper Live'),
        ('01:45-01:50', 'Exit Ticket + Tarea'),
    ]
    conv_obs = [
        ('English-Only - Como funciono?',
         'Cuanto espanol? Quienes se cayeron? English Points totales'),
        ('Public Speaking - quien se destaco',
         'En TBLT y Two Truths'),
        ('Anuncio Proyecto - reaccion',
         'Entusiasmo / resistencia / ansiedad'),
        ('Errores orales recurrentes (3-5)',
         'Pasalos al profesor de Bloque 1 manana'),
    ]
    build_report_bw('CONVERSACIONAL', conv_blocks, conv_obs,
                    'B1/reportes/B1_Clase1_CONV_REPORTE.pdf')

    print('\nListo. 4 PDFs en B&W para imprimir.')
