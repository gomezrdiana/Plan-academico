#!/usr/bin/env python3
"""Generate class guide PDFs (up to 4 pages) + separate 1-page report sheets."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
import os

DARK = HexColor('#1a1a2e')
ACCENT = HexColor('#e94560')
GRAY = HexColor('#555555')
LIGHT_BG = HexColor('#f0f0f0')
WHITE = white
WARN_BG = HexColor('#fff3cd')
WARN_BORDER = HexColor('#ffc107')
GREEN_BG = HexColor('#d4edda')
GREEN_BORDER = HexColor('#28a745')


def get_styles():
    styles = getSampleStyleSheet()
    defs = [
        ('Title2', 'Normal', 14, 16, 'Helvetica-Bold', DARK, 0, 3),
        ('Subtitle', 'Normal', 8.5, 10.5, 'Helvetica', GRAY, 0, 5),
        ('SectionHead', 'Normal', 9, 11, 'Helvetica-Bold', ACCENT, 6, 2),
        ('ActivityTime', 'Normal', 8.5, 10.5, 'Helvetica-Bold', DARK, 6, 1.5),
        ('Body2', 'Normal', 8, 10, 'Helvetica', black, 0, 2),
        ('BodyBold', 'Normal', 8, 10, 'Helvetica-Bold', black, 0, 2),
        ('SmallNote', 'Normal', 7, 9, 'Helvetica-Oblique', GRAY, 0, 1.5),
        ('RulesBox', 'Normal', 7.5, 9.5, 'Helvetica', black, 0, 1),
        ('TableCell', 'Normal', 7.5, 9.5, 'Helvetica', black, 0, 0),
        ('TableHeader', 'Normal', 7.5, 9.5, 'Helvetica-Bold', white, 0, 0),
        ('ReportTitle', 'Normal', 14, 16, 'Helvetica-Bold', DARK, 0, 2),
        ('ReportSub', 'Normal', 8, 10, 'Helvetica', GRAY, 0, 3),
        ('ReportBody', 'Normal', 8, 10, 'Helvetica', black, 0, 2),
        ('ReportBold', 'Normal', 8, 10, 'Helvetica-Bold', black, 0, 2),
        ('ReportCell', 'Normal', 7, 9, 'Helvetica', black, 0, 0),
        ('ReportHeader', 'Normal', 7, 9, 'Helvetica-Bold', white, 0, 0),
        ('ReportSmall', 'Normal', 6.5, 8, 'Helvetica-Oblique', GRAY, 0, 1),
    ]
    for name, parent, fs, ld, font, color, sb, sa in defs:
        if name not in styles.byName:
            styles.add(ParagraphStyle(name, parent=styles[parent],
                fontSize=fs, leading=ld, fontName=font, textColor=color,
                spaceBefore=sb, spaceAfter=sa))
    return styles


def box(text, styles, bg=WARN_BG, border=WARN_BORDER):
    t = Table([[Paragraph(text, styles['RulesBox'])]], colWidths=[7.2 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('BOX', (0, 0), (-1, -1), 0.5, border),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


# ===================== GUIDE PDF (up to 4 pages) =====================

def build_guide(filename, title, subtitle, activities, styles, special_note=None, is_reinforcement=False):
    doc = SimpleDocTemplate(filename, pagesize=letter,
        topMargin=0.45 * inch, bottomMargin=0.4 * inch,
        leftMargin=0.5 * inch, rightMargin=0.5 * inch)

    story = []
    story.append(Paragraph(title, styles['Title2']))
    story.append(Paragraph(subtitle, styles['Subtitle']))

    story.append(box(
        '<b>CORRECCIÓN:</b> Di: "No." Luego di: "Listen." + di la versión correcta lento + el estudiante la repite 2 veces. No expliques POR QUÉ está mal. Solo modela lo correcto. '
        '<b>PAPEL DE ERRORES OBLIGATORIO:</b> Lleva hoja en blanco + lapicero durante CADA actividad oral. Anota CADA error. Entregar con guía a coordinación. '
        '<b>SI UNA ACTIVIDAD SE PASA DEL TIEMPO, CÓRTALA.</b> Di: "Tiempo." y pasa a la siguiente.',
        styles))

    if not is_reinforcement:
        story.append(Spacer(1, 2))
        story.append(box(
            '<b>NO NEGOCIABLE:</b> El GoldList, el autochequeo y la socialización de tarea se hacen SIEMPRE. Nunca se saltan. '
            '<b>NO comuniques información sobre evaluaciones, midterms, proyectos finales ni calificaciones</b> — eso lo comunica coordinación. '
            '<b>SIGUE LA GUÍA AL PIE DE LA LETRA.</b> No improvises actividades, no enseñes contenido que no está en esta guía, no agregues vocabulario fuera de lo planificado.',
            styles, HexColor('#f8d7da'), HexColor('#dc3545')))

    story.append(Spacer(1, 3))

    if special_note:
        story.append(box(special_note, styles, GREEN_BG, GREEN_BORDER))
        story.append(Spacer(1, 3))

    for act in activities:
        time_str, act_title = act['time'], act['title']
        story.append(Paragraph(f'<b>{time_str} | {act_title}</b>', styles['ActivityTime']))
        for line in act['lines']:
            if isinstance(line, tuple):
                tag, text = line
                story.append(Paragraph(text, styles[tag]))
            else:
                story.append(Paragraph(line, styles['Body2']))

    doc.build(story)
    print(f"  OK GUIA: {filename}")


# ===================== REPORT PDF (1 page) =====================

def build_report(filename, title, subtitle, activities_checklist, deliverables, selfeval, styles):
    doc = SimpleDocTemplate(filename, pagesize=letter,
        topMargin=0.45 * inch, bottomMargin=0.4 * inch,
        leftMargin=0.5 * inch, rightMargin=0.5 * inch)

    story = []
    story.append(Paragraph(f'REPORTE — {title}', styles['ReportTitle']))
    story.append(Paragraph(subtitle, styles['ReportSub']))

    story.append(Paragraph(
        'Profesor: ___________________________ | Clase: ___ | Fecha: ___/___/___ | Ausentes: ___________________________',
        styles['ReportBody']))
    story.append(Spacer(1, 4))

    # Activities checklist
    story.append(Paragraph('<b>ACTIVIDADES (en orden — marque las completadas)</b>', styles['ReportBold']))
    act_header = [Paragraph('#', styles['ReportHeader']),
                  Paragraph('Actividad', styles['ReportHeader']),
                  Paragraph('Tiempo', styles['ReportHeader']),
                  Paragraph('OK', styles['ReportHeader'])]
    act_data = [act_header]
    for i, (act_name, act_time) in enumerate(activities_checklist, 1):
        act_data.append([
            Paragraph(str(i), styles['ReportCell']),
            Paragraph(act_name, styles['ReportCell']),
            Paragraph(act_time, styles['ReportCell']),
            ''])
    act_table = Table(act_data, colWidths=[0.25 * inch, 4.55 * inch, 0.8 * inch, 0.4 * inch])
    act_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('GRID', (0, 0), (-1, -1), 0.3, GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(act_table)
    story.append(Spacer(1, 3))

    # Deliverables
    story.append(Paragraph('<b>ENTREGABLES</b>', styles['ReportBold']))
    header = [Paragraph('Entregable', styles['ReportHeader']),
              Paragraph('Sí/No', styles['ReportHeader']),
              Paragraph('Notas', styles['ReportHeader'])]
    data = [header]
    for item in deliverables:
        data.append([Paragraph(item, styles['ReportCell']), '', ''])
    t = Table(data, colWidths=[4.5 * inch, 0.5 * inch, 2.0 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('GRID', (0, 0), (-1, -1), 0.3, GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))

    # Self-eval
    story.append(Paragraph('<b>AUTOEVALUACIÓN DEL PROFESOR</b>', styles['ReportBold']))
    header2 = [Paragraph('#', styles['ReportHeader']),
               Paragraph('Criterio', styles['ReportHeader']),
               Paragraph('S/N', styles['ReportHeader']),
               Paragraph('Evidencia / Notas', styles['ReportHeader'])]
    data2 = [header2]
    for i, c in enumerate(selfeval, 1):
        data2.append([
            Paragraph(str(i), styles['ReportCell']),
            Paragraph(c, styles['ReportCell']), '', ''])
    t2 = Table(data2, colWidths=[0.25 * inch, 3.5 * inch, 0.4 * inch, 2.85 * inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('GRID', (0, 0), (-1, -1), 0.3, GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t2)
    story.append(Spacer(1, 4))

    # Activities not completed
    story.append(Paragraph(
        '<b>Actividades no completadas:</b> Si alguna actividad no tiene check, justifica aquí:',
        styles['ReportBody']))
    story.append(Paragraph(
        '____________________________________________________________________________________________________________',
        styles['ReportBody']))
    story.append(Spacer(1, 6))

    # Student at risk
    story.append(Paragraph(
        '<b>Estudiante en riesgo:</b> __________________________________________ '
        '<b>Nota:</b> __________________________________________',
        styles['ReportBody']))
    story.append(Spacer(1, 4))

    # Signatures
    story.append(Paragraph(
        'Firma del profesor: _________________________ '
        'Firma coordinación: _________________________ '
        'Fecha: ___/___/___',
        styles['ReportBody']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        'Reportes incompletos o justificaciones faltantes por actividades omitidas = incumplimiento documentado. '
        '3 incumplimientos = revisión de contrato.',
        styles['ReportSmall']))

    doc.build(story)
    print(f"  OK REPORTE: {filename}")


def build_report_v2(filename, title, subtitle, activities_checklist, deliverables, selfeval, styles):
    """Reporte simplificado v2 — UNA SOLA HOJA (feedback profesores 2026-04-29):
    - Presentes: ___/___ (denominador en blanco)
    - Tarea, Errores Libro, Material Redes, Estudiantes en Riesgo: 1 línea cada uno
    - Autoevaluación compacta
    """
    doc = SimpleDocTemplate(filename, pagesize=letter,
        topMargin=0.3 * inch, bottomMargin=0.3 * inch,
        leftMargin=0.4 * inch, rightMargin=0.4 * inch)

    story = []
    story.append(Paragraph(f'REPORTE — {title}', styles['ReportTitle']))
    story.append(Paragraph(subtitle, styles['ReportSub']))

    # Header con Presentes variable
    story.append(Paragraph(
        'Profesor: ____________________ | Fecha: ___/___/___ | '
        'Presentes: ___/___ | Ausentes: ____________________',
        styles['ReportBody']))
    story.append(Spacer(1, 3))

    # Activities checklist
    story.append(Paragraph('<b>ACTIVIDADES (en orden — marque las completadas)</b>', styles['ReportBold']))
    act_header = [Paragraph('#', styles['ReportHeader']),
                  Paragraph('Actividad', styles['ReportHeader']),
                  Paragraph('Tiempo', styles['ReportHeader']),
                  Paragraph('OK', styles['ReportHeader'])]
    act_data = [act_header]
    for i, (act_name, act_time) in enumerate(activities_checklist, 1):
        act_data.append([
            Paragraph(str(i), styles['ReportCell']),
            Paragraph(act_name, styles['ReportCell']),
            Paragraph(act_time, styles['ReportCell']),
            ''])
    act_table = Table(act_data, colWidths=[0.25 * inch, 4.55 * inch, 0.8 * inch, 0.4 * inch])
    act_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('GRID', (0, 0), (-1, -1), 0.3, GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(act_table)
    story.append(Spacer(1, 3))

    # Entregables compacto
    story.append(Paragraph('<b>ENTREGABLES</b>', styles['ReportBold']))
    header = [Paragraph('Entregable', styles['ReportHeader']),
              Paragraph('Sí/No', styles['ReportHeader'])]
    data = [header]
    for item in deliverables:
        data.append([Paragraph(item, styles['ReportCell']), ''])
    t = Table(data, colWidths=[6.7 * inch, 0.6 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('GRID', (0, 0), (-1, -1), 0.3, GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t)
    story.append(Spacer(1, 3))

    # TAREA - 1 línea con la regla
    story.append(Paragraph(
        '<b>TAREA</b>  <i>Regla: si no la hicieron en casa, la recuperan en clase.</i>',
        styles['ReportBold']))
    story.append(Paragraph(
        'No entregaron en casa: __________________________  |  '
        'Recuperaron en clase: Sí ____ / No ____  |  '
        'No cumplieron (alertar coord): __________________  |  '
        'Total cumplió: ___/___',
        styles['ReportBody']))
    story.append(Spacer(1, 3))

    # ERRORES / INCONSISTENCIAS - 2 líneas (libro + guía)
    story.append(Paragraph(
        '<b>ERRORES E INCONSISTENCIAS DETECTADAS HOY</b>  <i>(deja en blanco si no encontraste — '
        'pero búscalas: erratas del libro, frases mal contadas en GoldList, tiempos que no suman, '
        'instrucciones contradictorias en la guía, etc.)</i>',
        styles['ReportBold']))
    story.append(Paragraph(
        'En el LIBRO (página/módulo/error): _________________________________________________',
        styles['ReportBody']))
    story.append(Paragraph(
        'En la GUÍA (qué decía / qué debería decir): _________________________________________',
        styles['ReportBody']))
    story.append(Spacer(1, 3))

    # MATERIAL REDES - 2 líneas (con justificación obligatoria si no grabó)
    story.append(Paragraph(
        '<b>MATERIAL PARA REDES HEIIU</b>  Grabó hoy: Sí ___ / No ___  |  '
        'Tipo: _____________  |  Descripción: __________________________  |  '
        'Enviado coord: Sí ___ / No ___',
        styles['ReportBody']))
    story.append(Paragraph(
        '<b>Si NO grabó, ¿por qué? (obligatorio)</b>: '
        '_____________________________________________________________________________',
        styles['ReportBody']))
    story.append(Spacer(1, 3))

    # ESTUDIANTES EN RIESGO - 1 línea
    story.append(Paragraph(
        '<b>ESTUDIANTE(S) EN RIESGO (alertar coord)</b>: ____________________  '
        '|  Razón: ________________________________________________________________',
        styles['ReportBody']))
    story.append(Spacer(1, 4))

    # AUTOEVALUACIÓN compacta (sin Notas, solo S/N)
    story.append(Paragraph('<b>AUTOEVALUACIÓN DEL PROFESOR</b>', styles['ReportBold']))
    header2 = [Paragraph('#', styles['ReportHeader']),
               Paragraph('Criterio', styles['ReportHeader']),
               Paragraph('S/N', styles['ReportHeader'])]
    data2 = [header2]
    for i, c in enumerate(selfeval, 1):
        data2.append([
            Paragraph(str(i), styles['ReportCell']),
            Paragraph(c, styles['ReportCell']), ''])
    t2 = Table(data2, colWidths=[0.25 * inch, 6.65 * inch, 0.4 * inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('GRID', (0, 0), (-1, -1), 0.3, GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t2)
    story.append(Spacer(1, 3))

    # Firmas compactas
    story.append(Paragraph(
        'Firma profesor: ____________________  |  '
        'Firma coord: ____________________  |  '
        'Fecha: ___/___/___',
        styles['ReportBody']))

    doc.build(story)
    print(f"  OK REPORTE v2: {filename}")


# ===================== DATA =====================

def main():
    S = get_styles()
    D = os.path.dirname(os.path.abspath(__file__))

    # ==============================================================
    # A1 CLASE 1 — GUÍA
    # ==============================================================
    build_guide(
        os.path.join(D, 'A1_Clase1_GUIA.pdf'),
        'HEIIU A1 | Clase 1 de 45 | SOLO PARA EL PROFESOR',
        'Módulo 0: Pronunciación en Inglés — 8 Trucos para Sonar Más Claro | Profesor: ___________ | Fecha: ___/___/___ | Presentes: ___/16',
        [
            {'time': '00:00–00:12', 'title': 'ROMPEHIELO: CADENA DE NOMBRES + UNA PALABRA EN INGLÉS (12 min)', 'lines': [
                '<b>Qué es:</b> Un juego en cadena donde cada estudiante dice su nombre + una palabra en inglés que ya sepa. La cadena crece — cada persona repite todos los nombres y palabras anteriores antes de agregar los suyos. Esto construye comunidad, reduce la ansiedad y revela qué inglés ya traen.',
                'Di: "Bienvenidos a Heiiu. Hoy empieza todo. Vamos a hacer un juego. Cada persona dice su nombre y UNA palabra en inglés que ya sepa. Cualquier palabra. No importa si la pronuncian mal — eso lo arreglamos hoy."',
                'Tú empiezas: "My name is [tu nombre]. My word is... hello." Señala al Estudiante 1.',
                '<b>Regla de la cadena:</b> Cada estudiante repite el nombre y la palabra de la persona ANTERIOR, luego agrega los suyos. Si alguien no recuerda, la clase le ayuda. Al final, el Estudiante 16 intenta recordar todos — la clase lo anima.',
                'Después de la cadena, di: "Levanten la mano si su palabra tenía una de estas letras: T-H, V, R, o CH." Di: "Hoy van a aprender a pronunciar esas letras mucho mejor. Esas palabras que acaban de decir — al final de la clase, van a sonar COMPLETAMENTE diferente."',
                ('SmallNote', 'Escribe TODAS las palabras en el tablero. Las vas a usar después en el Shadowing y el GoldList. Usa el contenido que los propios estudiantes generaron.'),
            ]},
            {'time': '00:12–00:17', 'title': 'REGLAS DEL SALÓN + INTRO GOLDLIST (5 min)', 'lines': [
                'Di: "Tres reglas. Solo tres." Escribe en el tablero:',
                '<b>1. CELULAR BOCA ABAJO</b> — "El celular boca abajo. Siempre. Si lo necesito para una actividad, yo les digo."',
                '<b>2. USTEDES HABLAN 80% — YO HABLO 20%</b> — "Ustedes hablan el 80% del tiempo. Yo soy guía, no conferencista."',
                '<b>3. ERRORES = APRENDIZAJE</b> — "Los errores no son malos. Son la forma más rápida de aprender. Aquí NADIE se burla de nadie."',
                '<b>GoldList (1 min):</b> Muestra un cuaderno. Di: "Esto es el GoldList. Cada clase, ustedes escriben palabras nuevas aquí. NO estudian las palabras — solo las escriben. Su cerebro las aprende solo. La neurociencia lo respalda. Al final de cada clase, escribimos juntos."',
            ]},
            {'time': '00:17–00:37', 'title': 'LIBRO: MÓDULO 0 — 8 TRUCOS DE PRONUNCIACIÓN (20 min)', 'lines': [
                'Di: "Abran su libro A1 en el Módulo 0 — Pronunciación. Lean los 8 trucos con su compañero. Tienen 8 minutos."',
                '<b>Primeros 8 min:</b> Leen en parejas. Camina por el salón. Si alguien se ve perdido, señálale las explicaciones en español del libro.',
                '<b>Siguientes 12 min — PRÁCTICA TRUCO POR TRUCO.</b> Di: "Cierren el libro. Vamos truco por truco. Escuchen. Repitan." Di la versión INCORRECTA primero, luego la correcta. Exagera la diferencia. Repiten 3 veces.',
                '<b>Truco 1 — "i" suena como "e":</b> Kick. Did. Kid. Lid. Exagera: "Kick" con la "i" española vs "Kick" correcta.',
                '<b>Truco 2 — Consonantes finales fuertes:</b> Card. Hard. Rock. Talk. Pon tu mano frente a tu boca: "Si no sienten aire, no lo están haciendo bien."',
                '<b>Truco 3 — Sonido "th":</b> "Miren mi lengua." Saca la lengua 5mm. Sopla aire. The. This. Think. Three. Si dicen "de" en vez de "the": "No. Listen. THE." Repiten 3 veces. Camina verificando que TODOS saquen la lengua.',
                '<b>Truco 4 — "a" con sonrisa:</b> "Sonrían. Ahora digan: Fan." Hat. Bat. Contraste: Fun vs Fan. Hut vs Hat. But vs Bat.',
                '<b>Truco 5 — "y" = "i" + vocal:</b> Yes. Yeah. Yard. Yesterday. Error común: "Jes" en vez de "Yes." Modela mal, luego bien.',
                '<b>Truco 6 — "v" con vibración:</b> "Pongan los dedos en su garganta. Digan very. ¿Sienten la vibración? Eso es la v. Ahora digan berry. Diferente." Very. Love. Live. Vote. Repiten 5 veces.',
                '<b>Truco 7 — "r" sin tocar el paladar:</b> "Doblen la lengua hacia ATRÁS. No toquen el techo de la boca." River. Rome. Reading. El más difícil para colombianos. Camina revisando las lenguas.',
                '<b>Truco 8 — "ch" = tsh:</b> "Como un estornudo: ¡Achoo!" Choose. Shoes. Teacher. T-shirt.',
                ('SmallNote', 'Máx 2 min por sonido difícil. Avanza. El Shadowing más adelante usa un video de YouTube con hablante nativo — ahí se refuerza. Tu trabajo aquí es ENERGÍA y REPETICIÓN, no perfección.'),
            ]},
            {'time': '00:37–00:57', 'title': 'HISTORIA INTERACTIVA: EL LOCO VIAJE DE RICARDO A NUEVA YORK (20 min)', 'lines': [
                '<b>Qué es:</b> Cuentas una historia absurda llena de palabras con pronunciación difícil. Los estudiantes escuchan, repiten frases clave, responden preguntas y ACTÚAN las escenas.',
                '<b>ANTES DE EMPEZAR:</b> Escribe en el tablero: THINK — THREE — VERY — RIVER — YARD — CHOOSE — SHOES — HARD — YES — THE. Señala cada una y haz que la clase las diga dos veces.',
                '<b>Cuenta la historia LENTO. Pausa después de cada sección:</b>',
                '"There is a man. His name is Ricardo. Ricardo lives in a very, VERY big yard." — Pregunta: "Is the yard small?" Clase: "No!" "Say it: A very big yard." Repiten.',
                '"One day, Ricardo THINKS about a trip to New York." — "Does Ricardo think about Bogotá?" "No!" "Say: Ricardo THINKS about New York." Revisa el TH en "thinks."',
                '"Ricardo needs THREE things." — Muestra 3 dedos. "How many?" "Three!" Revisa TH. Si está mal: "No. Listen. THREE." Lengua afuera. Repiten.',
                '"First — shoes. Ricardo needs to CHOOSE his shoes. He CHOOSES the red ones." — Actúalo: finge elegir zapatos. "Stand up. YOU are Ricardo. CHOOSE your shoes." Todos fingen escoger. "Say: I choose the red shoes." Revisa el sonido CH.',
                '"Second — a card. A HARD card. A very HARD credit card." — "Say: A very hard card." Revisa la D final — ¿es fuerte?',
                '"Third — courage. His friend says: YES, YES, you can do this!" — Parejas: "Say: YES, you can do this!" Revisa el sonido Y.',
                '"Ricardo arrives in New York. He walks to THE river. THE beautiful river." — "Say: THE river." Revisa TH.',
                '"But oh no! Ricardo falls in THE river! The water is very, VERY cold!" — Actúalo: finge caer. "Stand up! Fall in the river!" Caídas dramáticas. "Say: The water is very cold!" Revisa la V en "very."',
                '"A man says: THINK! THINK before you swim! Ricardo THINKS. He swims to the yard." — "Say: Think before you swim." Revisión final de TH.',
                '<b>Últimos 5 min:</b> Di: "En parejas, cuéntense la historia. Usen las palabras del tablero. Tienen 3 minutos." Camina escuchando. Últimos 2 min: 2-3 estudiantes dicen una frase. Corrige solo pronunciación.',
                ('SmallNote', 'La historia es absurda A PROPÓSITO. Absurdo = memorable. Van a recordar very, think, three, choose, shoes, river, yard, the, hard, yes porque Ricardo se cayó en un río.'),
            ]},
            {'time': '00:57–01:12', 'title': 'SIMULACIÓN: TU PRIMERA CONVERSACIÓN EN INGLÉS — HOTEL CHECK-IN (15 min)', 'lines': [
                '<b>Qué es:</b> Los estudiantes simulan llegar a un hotel en un país de habla inglesa. Tienen un objetivo concreto (registrarse), no es un ejercicio de gramática.',
                '<b>Escribe en el tablero:</b> Receptionist: "Hello! Welcome. What is your name?" / You: "Hello. My name is ___." / Receptionist: "Very good. Room three or room five?" / You: "Room three, please." / Receptionist: "Here is your card. Have a very nice day!" / You: "Thank you very much!"',
                '<b>Modelar (2 min):</b> Tú eres el recepcionista. Escoge un estudiante. Haz la conversación. Exagera la pronunciación de: "Hello" (H fuerte), "Very" (v no b), "Three" (th), "Thank you" (th), "Card" (D fuerte).',
                '<b>Parejas (8 min):</b> Uno es recepcionista, el otro huésped. Practican. Camina escuchando: Very → vibración de V, no B. Three → lengua afuera para TH. Thank you → lengua afuera. Card → D final fuerte. Si está mal: "No. Listen." + modelo + repiten. Cambian roles a los 4 min.',
                '<b>Presentar (5 min):</b> 3 parejas al frente. La clase escucha. Después de cada pareja: "¿Dijeron very correctamente? ¿Escucharon el TH en three?" Pulgar arriba o abajo. Si es abajo, la pareja lo intenta de nuevo. Aplaude después de cada pareja.',
                ('SmallNote', 'Esta es su PRIMERA actividad basada en tareas. Mantenla simple, solidaria y celebratoria. Necesitan sentir que HICIERON algo en inglés hoy.'),
            ]},
            {'time': '01:12–01:24', 'title': 'SHADOWING 5 PASOS: PRONUNCIACIÓN (12 min)', 'lines': [
                '<b>DURANTE UNA ACTIVIDAD ANTERIOR:</b> Busca en YouTube: "English pronunciation practice sentences slow" o "TH V R sounds English native speaker." Escoge un clip corto (máximo 60 segundos) de un hablante nativo pronunciando palabras o frases claramente. Envía el link al grupo de WhatsApp.',
                '<b>PASO 1 — ESCUCHAR (2 min):</b> Di: "Abran el video que envié al WhatsApp. Solo escuchen. No repitan. No lean. Solo ESCUCHEN los sonidos." Boca cerrada. Manos en el escritorio.',
                '<b>PASO 2 — CON TEXTO (3 min):</b> Di: "Otra vez. Subtítulos encendidos. Repitan INMEDIATAMENTE después del hablante. Imiten sus sonidos exactamente."',
                '<b>PASO 3 — SIN TEXTO (3 min):</b> Di: "Otra vez. Subtítulos APAGADOS. Pantalla boca abajo después de darle play."',
                '<b>PASO 4 — OJOS CERRADOS (2 min):</b> Di: "Una vez más. Cierren los ojos. Máxima concentración. Solo escuchen y repitan."',
                '<b>PASO 5 — SHADOWING EN PAREJAS (2 min):</b> Di: "Celulares ABAJO. Parejas. Repitan lo que escucharon de memoria. Una persona dice una frase, la otra repite. Luego cambian."',
            ]},
            {'time': '01:24–01:39', 'title': 'OLIMPIADAS DEL SONIDO: MAPA BOCA + CONSTRUIR + COMPETIR (15 min)', 'lines': [
                '<b>Paso 1 — Mapa de la Boca (3 min):</b> Dibuja una vista lateral simple de una boca en el tablero: lengua, dientes, labios, garganta. Señala y explica:',
                '"TH — la lengua va ENTRE los dientes." (Dibuja la lengua entre los dientes.) "Ningún sonido del español hace esto." / "V — los dientes de ARRIBA tocan el labio de ABAJO. Sientan la vibración." / "R — la lengua se dobla hacia ATRÁS. NO toca nada." Di: "Esto es ciencia. Su boca es una máquina. Hoy la están reprogramando."',
                '<b>Paso 2 — Construir y Nombrar (5 min):</b> Di: "Usen CUALQUIER COSA de su escritorio — lapiceros, borradores, cuadernos — y construyan algo. Tienen 2 minutos." Después: "Pónganle nombre usando un truco de pronunciación. Ejemplo: This is my very hard car (con V y D correctas)." Cada estudiante presenta en 10-15 seg. Corrige en vivo.',
                '<b>Paso 3 — Olimpiadas del Sonido (7 min):</b> 4 equipos de 4. Escribe en el tablero:',
                'R1 TH: "Those three things are there" (equipo más rápido con pronunciación correcta) / R2 V: "Viviana lives in Latvia and loves volleyball" (un estudiante por equipo) / R3 R: "Ralph and Randy really rocked the boat" (todo el equipo al unísono) / R4 CH: "I choose my shoes and change my chaps" (relevo — uno a la vez). 1 punto por ronda. Puntajes en tablero. Equipo perdedor hace ronda bonus.',
            ]},
            {'time': '01:39–01:47', 'title': 'REFLEXIÓN: DIARIO DE PRONUNCIACIÓN + VOTACIÓN (8 min)', 'lines': [
                '<b>Empatizar (2 min):</b> Di: "¿Por qué están aquí? Escriban UNA frase en español: Estoy aquí porque ___. Tienen 1 minuto." Después: "Ahora debajo escriban en inglés — solo intenten — I am here because ___." Camina. Ayuda con una palabra cada uno si es necesario.',
                '<b>Diario de Pronunciación (3 min):</b> Di: "Abran una página nueva. Escriban arriba: MY PRONUNCIATION JOURNAL." Escribe en el tablero los 8 trucos con ejemplo: 1."i"=kick 2.endings=card 3.th=think 4.a=hat 5.y=yes 6.v=very 7.r=river 8.ch=choose. Di: "Marquen con check los que ya les salen bien y con X los que necesitan practicar."',
                '<b>Votación (3 min):</b> Di: "¿Cuál fue el sonido MÁS DIFÍCIL hoy? Voten." TH — levantan la mano. V — levantan. R — levantan. Cuenta votos. Escribe el ganador. Di: "En la tarea van a practicar ESE sonido 10 veces."',
            ]},
            {'time': '01:47–01:52', 'title': 'GRABO BASELINE: TU PRIMERA GRABACIÓN (5 min)', 'lines': [
                '<b>ESTE ES EL PRIMER GRABO. Es un baseline — va a sonar terrible. ESE ES EL PUNTO.</b>',
                'Di: "Van a grabar su primer video en inglés. Van a cerrar los ojos. Sin notas. Sin leer. Solo su voz."',
                'Escribe en el tablero: GRABO BASELINE — OJOS CERRADOS — 30 SEGUNDOS. Di: 1) Tu nombre: "My name is ___." 2) Tres palabras de hoy con pronunciación correcta. 3) Una frase de la historia: "Ricardo thinks about New York."',
                'Di: "Todos al mismo tiempo. Saquen el celular. Temporizador en 30 segundos. Cierren los ojos. Cuando yo diga GO, todos graban. GO." Camina en silencio. 30 segundos.',
                'Di: "Stop. Envíen el video por WhatsApp AHORA MISMO. Etiquétenlo: GRABO BASELINE — [su nombre]."',
                '<b>PROFESOR:</b> Envía TODOS los videos a coordinación EL MISMO DÍA. Estos son los baselines del Día 1. En 4 semanas graban de nuevo y comparan.',
                ('SmallNote', 'Va a ser incómodo. Algunos se ríen. Algunos apenas hablan. ESE ES EL PUNTO. Celebra: "Acaban de hablar inglés con los ojos cerrados en su PRIMER DÍA. Eso requiere agallas."'),
            ]},
            {'time': '01:52–02:00', 'title': 'GOLDLIST + AUTOCHEQUEO + TAREA + CIERRE (8 min)', 'lines': [
                '<b>GoldList (3 min):</b> Di: "Abran su cuaderno de GoldList. Escriban la fecha de hoy. Ahora escriban estas 10 palabras — solo ESCRÍBANLAS. No las estudien. No las repitan. Solo escríbanlas." Dicta lento: think, three, very, river, yard, choose, shoes, hard, yes, the. Di: "Cierren el cuaderno. No las miren de nuevo hasta que yo les diga."',
                '<b>Autochequeo (3 min):</b> Entrega la hoja de autochequeo (Módulo 0). Di: "Llenen CADA casilla honestamente." RECOGE cada hoja. REVISA: ¿hay campos en blanco que deberían estar llenos? Devuélvela: "Llena esto AHORA." No se aceptan hojas incompletas. Envía a coordinación HOY.',
                '<b>Tarea (2 min):</b> Escribe en el tablero: TAREA — CLASE 2. 1) Practica los 3 sonidos más difíciles para TI (los que marcaste con X en tu Diario de Pronunciación). Di cada palabra de ejemplo 10 veces EN VOZ ALTA. No mentalmente — EN VOZ ALTA. 2) Mira tu video GRABO BASELINE. Escúchate. Escribe 2 sonidos que necesitas mejorar. 3) Grábate diciendo estas 3 frases (envía por WhatsApp ANTES de la próxima clase): "Those three things are there on their throne." / "I live in Latvia with Viviana, but I would love to leave." / "I choose my shoes and change my chaps." Etiqueta: TAREA 1 — [Tu Nombre].',
                'Di: "¿Preguntas? Nos vemos mañana. You did great today."',
                ('SmallNote', 'DESPUÉS DE QUE SE VAYAN: Envía la tarea como mensaje al grupo de WhatsApp. Copia la tarea EXACTAMENTE como está arriba. Si no está en el grupo, no pasó. TAREA DEL PROFESOR: Practica SH vs CH, TH, V vs B en YouTube. Habla con Greg — pídele que diga los 8 sonidos para ti.'),
            ]},
        ],
        S,
        special_note='<b>⚠ ESTA ES LA CLASE 1.</b> Los estudiantes no saben NADA de inglés. Están nerviosos. Tu energía y calidez en los primeros 15 minutos determinan si vuelven. Sonríe. Usa sus nombres. Usa el español como PUENTE — pero cambia al inglés en cuanto puedan manejarlo. Cada palabra que digan en inglés hoy es una victoria.'
    )

    # A1 CLASE 1 — REPORTE
    build_report(
        os.path.join(D, 'A1_Clase1_REPORTE.pdf'),
        'A1 | Clase 1 de 45',
        'Módulo 0: Pronunciación en Inglés — 8 Trucos para Sonar Más Claro',
        [
            ('Rompehielo: Cadena de nombres', '12 min'),
            ('Reglas del salón + Intro GoldList', '5 min'),
            ('Libro: Módulo 0 — 8 trucos de pronunciación', '20 min'),
            ('Historia interactiva: Ricardo en Nueva York', '20 min'),
            ('Simulación: Hotel check-in', '15 min'),
            ('Shadowing 5 pasos', '12 min'),
            ('Olimpiadas del sonido', '15 min'),
            ('Reflexión: Diario de pronunciación + Votación', '8 min'),
            ('GRABO baseline', '5 min'),
            ('GoldList', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Videos GRABO baseline ojos cerrados (todos)',
            'Hojas de autochequeo completadas (Módulo 0)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores escritos)',
            'Mi celular estaba boca abajo',
            'Creé un ambiente cálido y solidario en el Día 1',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'TODOS los videos GRABO baseline enviados a coord.',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # ==============================================================
    # A1 CLASE 2 — GUÍA
    # ==============================================================
    build_guide(
        os.path.join(D, 'A1_Clase2_GUIA.pdf'),
        'HEIIU A1 | Clase 2 de 45 | SOLO PARA EL PROFESOR',
        'Módulo 2: What Can You Play? — Pronombres Sujetos + "What" | Profesor: ___________ | Fecha: ___/___/___ | Presentes: ___/16',
        [
            {'time': '00:00–00:05', 'title': 'VATS: VIRTUD DE LA SEMANA — PRUDENCIA (5 min)', 'lines': [
                '<b>Qué es:</b> Ritual diario de valores. Escribe en el tablero: PRUDENCIA — "¿Es inteligente practicar un poco todos los días, o mucho un solo día?"',
                '<b>V — Virtud (1 min):</b> Lee la pregunta. Señala el tablero.',
                '<b>A — Activar (30 seg):</b> Di: "Piensen en silencio."',
                '<b>T — Talk en parejas (2 min):</b> Di: "Parejas. Discutan — pueden usar español, pero intenten decir al menos UNA frase en inglés." Ejemplo: "I think... every day."',
                '<b>S — Share (1.5 min):</b> 2 estudiantes comparten. Celebra cualquier intento en inglés.',
                ('SmallNote', 'Es la primera vez que hacen VATS. Mantenlo simple. La meta es que entiendan el ritual: pregunta → silencio → parejas → compartir. Cada clase se repite.'),
            ]},
            {'time': '00:05–00:15', 'title': 'CARTA A MI YO DEL FUTURO (10 min)', 'lines': [
                '<b>⚠ MOMENTO ESPECIAL. Este es un momento emocional, no académico. Hazlo con calma y seriedad.</b>',
                'Di: "Antes de empezar la clase de hoy, vamos a hacer algo especial. Van a escribir una carta a su YO DEL FUTURO — al que va a estar aquí cuando se gradúen de Heiiu."',
                '<b>Explicar (1 min):</b> Di: "Escriban una carta en ESPAÑOL. Escríbanle a ustedes mismos del futuro. Díganle: ¿por qué empezaron a estudiar inglés? ¿Qué sueñan lograr? ¿Qué les da miedo? ¿Qué quieren que su yo del futuro sepa? Esta carta la vamos a SELLAR en un sobre. Nadie la va a leer. La van a abrir el día de su graduación."',
                '<b>Escribir (7 min):</b> Di: "Tienen 7 minutos. Escriban." Pon música tranquila si quieres. Camina en silencio. NO leas lo que escriben — es privado. Si alguien dice "no sé qué escribir": "Escríbele a tu yo del futuro lo que quieres que sepa. ¿Por qué estás aquí hoy?"',
                '<b>Sellar (2 min):</b> Entrega un sobre a cada estudiante. Di: "Doblen la carta. Métanla en el sobre. Escriban su nombre afuera. Séllenlo." Recoge los 16 sobres. Cuéntalos.',
                '<b>ENTREGABLE: Entregar TODOS los sobres sellados a coordinación HOY. Coordinación los guarda hasta la graduación.</b>',
                ('SmallNote', 'Algunos estudiantes se van a emocionar. Eso es bueno. Este momento crea un ancla emocional con el programa. Cuando quieran rendirse en el mes 4, van a recordar esta carta.'),
            ]},
            {'time': '00:15–00:25', 'title': 'ANALIZO: REVISIÓN DE TAREA (10 min)', 'lines': [
                'Tarea de la Clase 1: grabarse diciendo 3 frases de pronunciación + escribir 2 sonidos a mejorar.',
                '<b>Primeros 3 min:</b> Di: "¿Quién envió su video de tarea?" Levanten la mano. Cuenta. Anota quiénes NO lo hicieron — repórtalo a coordinación.',
                'Di a los que no hicieron la tarea: "Mientras los demás trabajan en parejas, ustedes graban su video AHORA MISMO. 30 segundos, ojos cerrados, las 3 frases. Me lo envían antes de que termine esta actividad."',
                '<b>Siguientes 7 min:</b> Parejas. Di: "Lean a su compañero los 2 sonidos que identificaron como difíciles. Practiquen esos sonidos juntos. Un compañero dice la palabra, el otro revisa si suena bien." Camina escuchando. Corrige: "No. Listen." + versión correcta + repiten.',
            ]},
            {'time': '00:25–00:45', 'title': 'LIBRO: MÓDULO 2 — "WHAT" + PRONOMBRES SUJETOS (20 min)', 'lines': [
                'Di: "Abran su libro A1 en el Módulo 2 — What Can You Play? Lean la Guía 1 con su compañero. Tienen 8 minutos."',
                '<b>Primeros 8 min:</b> Leen en parejas. Camina. Si alguien se ve perdido, señálale las explicaciones en español.',
                '<b>Siguientes 12 min:</b> Siéntate con cada pareja. ELLOS te explican (tú NO explicas):',
                '1) ¿Cuáles son los 7 pronombres? → I, you, he, she, it, we, they. Haz que los digan en orden sin leer.',
                '2) ¿Cómo se reemplaza un nombre por un pronombre? → Dales 3 nombres: "Ana" → She. "Pedro y María" → They. "Tú y yo" → We.',
                '3) ¿Cómo se hace una pregunta con "what"? → "What can Juan play?" → respuesta con información. vs "Can Juan play?" → Yes/No.',
                'Si no pueden decir los 7 pronombres sin leer, vuelven a leer el módulo.',
            ]},
            {'time': '00:45–00:57', 'title': 'EJERCICIOS + RESPUESTAS (12 min)', 'lines': [
                'Di: "Hagan los ejercicios del módulo. Revisen con las Answer Keys. Pregúntenle a su compañero primero. Si ninguno sabe, levanten la mano."',
                'CAMINA — da la versión correcta solamente. Si más del 50% tiene el mismo error: PARA. Escríbelo en el tablero. Repiten.',
                ('SmallNote', 'Durante este tiempo, busca en YouTube un clip corto (máximo 60 segundos) de alguien presentándose o presentando a otros en inglés ("This is my friend, he is..., she can..."). Envía el link al grupo de WhatsApp.'),
            ]},
            {'time': '00:57–01:17', 'title': 'SIMULACIÓN: PRESENTAR A TU COMPAÑERO (20 min)', 'lines': [
                '<b>Qué es:</b> Los estudiantes se entrevistan y luego PRESENTAN a su compañero a la clase usando pronombres y "can." Esto los obliga a cambiar de "I" a "he/she" naturalmente.',
                '<b>Paso 1 — Entrevistar (5 min):</b> Di: "Van a entrevistar a su compañero." Escribe en el tablero: 1. "What is your name?" 2. "What can you play?" (deporte) 3. "What can you do?" (cook, swim, dance, sing, draw...). Parejas. Uno pregunta, el otro responde. Luego cambian. 2.5 min cada uno.',
                '<b>Paso 2 — Escribir la presentación (5 min):</b> Di: "Escriban 4 frases presentando a su compañero. NO digan su nombre después de la primera frase — usen HE o SHE." Modelo en el tablero: "This is [nombre]. He/She can play soccer. He/She can cook. He/She can\'t swim."',
                '<b>Paso 3 — Presentar (8 min):</b> Cada estudiante se para y presenta a su compañero. Si alguien dice "Juan can play" en vez de "HE can play": "No. Listen. HE can play." Repiten. Si alguien dice "Her can play": "No. Listen. SHE can play." (Confundir he/she/her/him es el error #1 aquí.)',
                '<b>Paso 4 — Clase pregunta (2 min):</b> Después de cada presentación, la clase hace una pregunta: "What can he play?" o "Can she cook?" El presentador responde.',
                ('SmallNote', 'Camina con papel de errores. Errores más comunes: "her" en vez de "she," "him" en vez de "he," olvidar "can," decir "play" sin "can."'),
            ]},
            {'time': '01:17–01:27', 'title': 'SHADOWING 5 PASOS (10 min)', 'lines': [
                'YouTube en los celulares de los estudiantes. Subtítulos ENCENDIDOS.',
                '<b>PASO 1 — ESCUCHAR (2 min):</b> Di: "Abran el video del WhatsApp. Solo escuchen."',
                '<b>PASO 2 — CON TEXTO (2 min):</b> Di: "Otra vez. Subtítulos encendidos. Repitan."',
                '<b>PASO 3 — SIN TEXTO (2 min):</b> Di: "Subtítulos APAGADOS. Repitan."',
                '<b>PASO 4 — OJOS CERRADOS (2 min):</b> Di: "Ojos cerrados. Repitan."',
                '<b>PASO 5 — PAREJAS (2 min):</b> Di: "Celulares ABAJO. Repitan de memoria en parejas."',
            ]},
            {'time': '01:27–01:39', 'title': 'JUEGO: ¿QUIÉN ES? — ADIVINA EL PRONOMBRE (12 min)', 'lines': [
                '<b>Qué es:</b> El profesor describe a alguien usando pronombres y "can." La clase adivina quién es. Luego los estudiantes hacen lo mismo.',
                '<b>Ronda 1 — Profesor describe (4 min):</b> Di: "Voy a describir a alguien de la clase. Adivinen quién es." Ejemplo: "THIS PERSON can play soccer. HE can\'t play tennis. HE can cook. Who is it?" La clase grita el nombre. 3-4 descripciones usando HE, SHE, THEY.',
                '<b>Ronda 2 — Estudiantes describen (5 min):</b> Di: "Ahora USTEDES. Cada persona piensa en alguien de la clase. Describan usando HE, SHE, o THEY + CAN. La clase adivina." Si usan el nombre en vez del pronombre: "No. Use HE or SHE." Repiten.',
                '<b>Ronda 3 — "What" questions (3 min):</b> Di: "Ahora la clase hace preguntas para adivinar. Solo preguntas con WHAT." Modelo: "What can this person play?" → "He can play basketball." De pie. Rápido.',
            ]},
            {'time': '01:39–01:49', 'title': 'COMPETENCIA: CARRERA DE PRONOMBRES (10 min)', 'lines': [
                '2 equipos de 8. De pie.',
                '<b>Ronda 1 — Reemplazar (4 min):</b> Di un nombre. El primer equipo en gritar el pronombre correcto gana el punto. "María" → "SHE!" / "Pedro" → "HE!" / "María y Pedro" → "THEY!" / "Tú y yo" → "WE!" / "El perro" → "IT!" 10 nombres rápidos.',
                '<b>Ronda 2 — Frase completa (4 min):</b> Di nombre + verbo. Frase con pronombre correcto. "Ana / play soccer" → "SHE can play soccer!" 8 frases rápidas.',
                '<b>Ronda 3 — Pregunta con What (2 min):</b> Di un pronombre. Deben formar la pregunta. "She" → "What can she play?" 5 preguntas rápidas. Puntajes en tablero.',
            ]},
            {'time': '01:42–01:45', 'title': 'CONSTRUIR + NOMBRAR (3 min)', 'lines': [
                'Di: "Con lo que tengan en el escritorio, construyan un personaje — robot, animal, persona. Tienen 1 minuto." Después: "Presenten su personaje en UNA frase: This is [nombre]. He/She/It can [verbo]." Cada estudiante dice su frase en 10 segundos. Corrige pronombres en vivo.',
            ]},
            {'time': '01:45–02:00', 'title': 'GOLDLIST + AUTOCHEQUEO + TAREA + CIERRE (15 min)', 'lines': [
                '<b>⚠ PREPARACIÓN DEL TABLERO:</b> ANTES de que lleguen los estudiantes (o durante una actividad donde no necesites el tablero), escribe las 20 frases del GoldList — AMBOS IDIOMAS, EXACTAMENTE como aparecen en esta guía. No traduzcas de memoria.',
                '<b>⚠ EL CUADERNO DE GOLDLIST SE QUEDA EN LA ACADEMIA.</b> Los estudiantes NO se lo llevan. Recoge todos los cuadernos al final. Esto asegura que no estudien en casa (lo cual arruinaría el método).',
                '<b>GoldList (10 min):</b> Di: "Tomen su cuaderno de GoldList. Fecha de hoy. Copien las frases del tablero: inglés a la izquierda, español a la derecha. No se apuren — con calma y buena letra." Los estudiantes copian (8 min): 1. Can I go to the bathroom? / ¿Puedo ir al baño? 2. How do you say ___ in English? / ¿Cómo se dice ___ en inglés? 3. Can you repeat that, please? / ¿Puede repetir? 4. I don\'t understand. / No entiendo. 5. How do you spell that? / ¿Cómo se deletrea? 6. What does ___ mean? / ¿Qué significa ___? 7. Can I borrow a pen? / ¿Me presta un lapicero? 8. What page are we on? / ¿En qué página vamos? 9. Can you speak slower, please? / ¿Puede hablar más lento? 10. I have a question. / Tengo una pregunta. 11. My name is ___. / Mi nombre es ___. 12. Nice to meet you. / Mucho gusto. 13. Where are you from? / ¿De dónde eres? 14. How old are you? / ¿Cuántos años tienes? 15. What do you do? / ¿A qué te dedicas? 16. I need help. / Necesito ayuda. 17. How much does it cost? / ¿Cuánto cuesta? 18. Where is the bathroom? / ¿Dónde está el baño? 19. I would like ___, please. / Me gustaría ___. 20. Thank you very much. / Muchas gracias. Cuando terminen (2 min): "Lean la lista UNA vez conmigo." Repiten. UNA vez. "Cierren el cuaderno. NO las estudien. En dos semanas volvemos." <b>RECOGE TODOS LOS CUADERNOS.</b>',
                ('SmallNote', 'PROFESOR: A partir de hoy, usa estas frases NATURALMENTE en clase sin decir "esto es de tu GoldList." Si un estudiante quiere ir al baño en español: "In English?" y espera. La exposición inconsciente es lo que hace funcionar el método.'),
                '<b>Autochequeo (3 min):</b> Entrega la hoja (Módulo 2). Llenan CADA casilla. RECOGE. REVISA. Envía a coordinación HOY.',
                '<b>Tarea (2 min):</b> Escribe en el tablero: TAREA — CLASE 3. 1) Escribe 5 frases sobre personas que conoces usando pronombres + "can": "My mom can cook. She can\'t play soccer." "My brother can swim. He can play basketball." "My friends can dance. They can\'t sing." 2) Grábate diciendo las 5 frases (ojos cerrados, 30 seg mínimo). Envía por WhatsApp. Etiqueta: TAREA A1-2 — [Tu Nombre].',
                'Di: "¿Preguntas? Nos vemos mañana."',
                ('SmallNote', 'DESPUÉS: Envía la tarea al grupo de WhatsApp EXACTA. Tarea profesor: Revisa tu papel de errores — ¿cuáles pronombres confundieron más? Asegúrate de que los 16 sobres de la "Carta a mi yo del futuro" estén entregados a coordinación.'),
            ]},
        ],
        S
    )

    # A1 CLASE 2 — REPORTE
    build_report(
        os.path.join(D, 'A1_Clase2_REPORTE.pdf'),
        'A1 | Clase 2 de 45',
        'Módulo 2: What Can You Play? — Pronombres Sujetos + "What"',
        [
            ('VATS: Prudencia', '5 min'),
            ('Carta a mi yo del futuro', '10 min'),
            ('Analizo: Revisión de tarea', '10 min'),
            ('Libro: Módulo 2 — Pronombres + What', '20 min'),
            ('Ejercicios + Respuestas', '12 min'),
            ('Simulación: Presentar a tu compañero', '20 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Juego: ¿Quién es? — Adivina el pronombre', '12 min'),
            ('Competencia: Carrera de pronombres', '10 min'),
            ('Construir + Nombrar', '3 min'),
            ('GoldList (20 frases)', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            '16 sobres "Carta a mi yo del futuro" (sellados)',
            'Hojas de autochequeo completadas (Módulo 2)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Prudencia)',
            'La "Carta a mi yo del futuro" se hizo con respeto y seriedad',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # ==============================================================
    # A2 CLASE 1 — GUÍA
    # ==============================================================
    build_guide(
        os.path.join(D, 'A2_Clase1_GUIA.pdf'),
        'HEIIU A2 | Clase 1 de 55 | SOLO PARA EL PROFESOR',
        'Módulo 1: I Will Play on Monday — El Futuro con "Will" + Días de la Semana | Profesor: ___________ | Fecha: ___/___/___ | Presentes: ___/16',
        [
            {'time': '00:00–00:07', 'title': 'VATS: VIRTUD DE LA SEMANA — TEMPLANZA (7 min)', 'lines': [
                'Escribe en el tablero: TEMPLANZA — "Is it easy to be patient when learning something new? When was the last time you wanted to quit but didn\'t?"',
                '<b>V — Virtud (1 min):</b> Señala el tablero. Lee la pregunta en voz alta. Di: "Esta semana hablamos de TEMPLANZA. Autocontrol. Paciencia. Disciplina."',
                '<b>A — Activar (30 seg):</b> Di: "30 segundos. Piensen en silencio. ¿Cuándo fue la última vez que quisieron rendirse pero no lo hicieron?"',
                '<b>T — Talk en parejas (3 min):</b> Di: "Parejas. Cuéntense en inglés — usen lo que saben. Si necesitan una palabra en español, díganla y sigan en inglés."',
                '<b>S — Share (2.5 min):</b> Di: "¿Quién quiere compartir?" 2-3 estudiantes comparten. Corrige solo si es necesario.',
            ]},
            {'time': '00:07–00:17', 'title': 'ROMPEHIELO: MI SEMANA PERFECTA (10 min)', 'lines': [
                'Di: "Imaginen su semana PERFECTA. ¿Qué hacen cada día? Vamos a usar los días en inglés."',
                'Escribe en el tablero: Monday — Tuesday — Wednesday — Thursday — Friday — Saturday — Sunday. Di cada día, la clase repite. Hazlo 2 veces.',
                '<b>Atención a la pronunciación de:</b> "Wednesday" → /WENZ-dei/ (la D del medio NO se pronuncia). "Tuesday" → /TUZ-dei/ (no "Chus-day"). "Thursday" → /THERZ-dei/ (con TH).',
                '<b>Ronda rápida (7 min):</b> Modelo tú primero: "On Monday, I play soccer. On Tuesday, I eat pizza. On Wednesday, I sleep ALL day." Cada estudiante dice 2-3 días. Si alguien dice "On Monday I will play..." — perfecto, ya están usando "will" naturalmente. No corrijas eso — es exactamente lo que van a aprender hoy. Si dicen el día mal: "No. Listen. WEDNESDAY." Repiten.',
                ('SmallNote', 'Escribe en tu papel de errores qué días pronuncian mal. Los más comunes: Wednesday, Tuesday, Thursday.'),
            ]},
            {'time': '00:17–00:27', 'title': 'ANALIZO: TRANSICIÓN A1→A2 (10 min)', 'lines': [
                'Di: "Bienvenidos a A2. Ya saben mucho. Vamos a probarlo." Escribe en el tablero 6 frases con errores de A1. Los estudiantes las corrigen en parejas:',
                '1) Juan can plays soccer. → can play (sin s). 2) She should to study. → should study (sin to). 3) What you can do? → What can you do? (orden). 4) I don\'t can swim. → I can\'t swim (can no usa do). 5) He play soccer yesterday. → He played (pasado). 6) Where she lives? → Where does she live? (auxiliar).',
                '<b>Primeros 4 min:</b> Parejas corrigen. Camina escuchando.',
                '<b>Siguientes 6 min:</b> Revisa en grupo. Para cada frase, un estudiante dice la corrección. Si está mal: "No. Listen." + versión correcta + repiten.',
                'Di: "Si todas estas les salieron bien, están listos para A2. Si alguna les costó, eso es normal — las vamos a seguir practicando."',
                ('SmallNote', 'Esto te da un diagnóstico rápido de qué necesita refuerzo. Anota cuáles frases causaron más problemas.'),
            ]},
            {'time': '00:27–00:47', 'title': 'LIBRO: MÓDULO 1 — EL FUTURO CON "WILL" + DÍAS (20 min)', 'lines': [
                'Di: "Abran su libro A2 en el Módulo 1 — I Will Play on Monday. Lean la Guía 1 con su compañero. Tienen 8 minutos."',
                '<b>Primeros 8 min:</b> Leen en parejas. Camina por el salón. Si alguien se ve perdido, señálale las explicaciones en español del libro.',
                '<b>Siguientes 12 min:</b> Siéntate con cada pareja. ELLOS te explican:',
                '1) ¿Cómo se forma una frase positiva con "will"? → "Juan will play soccer." 2) ¿Cómo se hace negativa? → "Juan will not play soccer" / "Juan won\'t play soccer." 3) ¿Cómo se hace pregunta? → "Will Juan play soccer?" 4) ¿Cuáles son las contracciones? → I\'ll, you\'ll, he\'ll, she\'ll, it\'ll, we\'ll, they\'ll. 5) ¿Qué preposición se usa para días? → "on" — "on Monday."',
                'Si no pueden explicar la diferencia entre "will" y "won\'t," vuelven a leer.',
            ]},
            {'time': '00:47–01:02', 'title': 'EJERCICIOS + RESPUESTAS (15 min)', 'lines': [
                'Di: "Hagan los ejercicios del módulo. Revisen sus respuestas con las Answer Keys. Pregúntenle a su compañero primero. Si ninguno sabe, levanten la mano."',
                'CAMINA por el salón — da la versión correcta solamente (nunca expliques reglas). Si más del 50% tiene el mismo error: PARA. Escríbelo en el tablero. Repiten.',
                ('SmallNote', 'Durante este tiempo, busca en YouTube un clip corto (máximo 60 segundos) de alguien hablando de sus planes para la semana — un vlogger, un podcast, o "my weekly routine." Envía el link al grupo de WhatsApp para el Shadowing.'),
            ]},
            {'time': '01:02–01:22', 'title': 'SIMULACIÓN: PLANIFICA LA SEMANA DE TU COMPAÑERO (20 min)', 'lines': [
                '<b>Qué es:</b> Los estudiantes son "asistentes personales" y deben planificar la semana de su compañero. Primero entrevistan, luego presentan el plan usando "will" + días + horas.',
                '<b>Paso 1 — Entrevistar (5 min):</b> Di: "Son asistentes personales. Van a planificar la semana PERFECTA de su compañero." Escribe en el tablero: "What will you do on Monday?" / "What time will you wake up on Tuesday?" / "Will you study on Wednesday?" / "What will you eat on Friday?" Parejas. Uno pregunta, el otro responde. Toman notas. 2.5 min cada uno, luego cambian.',
                '<b>Paso 2 — Escribir el plan (5 min):</b> Di: "Escriban el plan semanal de su compañero. Mínimo 7 frases — una por cada día." Modelo en el tablero: "On Monday, [nombre] will wake up at 6:00 AM. On Tuesday, he/she will play soccer at 3:00 PM. On Wednesday, he/she will study English at 7:00 PM..."',
                '<b>Paso 3 — Presentar (8 min):</b> Cada pareja presenta el plan a la clase. Di: "La clase escucha. Si escuchan un error, levanten la mano." Después de cada presentación: "¿Escucharon algún error?" Si sí, el estudiante que lo detectó dice la corrección. Si nadie lo escuchó, tú corriges.',
                '<b>Paso 4 — Voto (2 min):</b> Di: "¿Cuál plan semanal es el MÁS interesante? ¿Quién tiene la mejor semana?" Votan.',
                ('SmallNote', 'Camina con papel de errores durante los Pasos 2 y 3. Anota errores comunes: "will" olvidado, "on" faltante, pronunciación de días.'),
            ]},
            {'time': '01:22–01:34', 'title': 'SHADOWING 5 PASOS (12 min)', 'lines': [
                'Di: "Abran el video que envié al WhatsApp."',
                '<b>PASO 1 — ESCUCHAR (2 min):</b> Di: "Solo escuchen. No repitan. No lean. Solo ESCUCHEN." Boca cerrada.',
                '<b>PASO 2 — CON TEXTO (3 min):</b> Di: "Otra vez. Subtítulos encendidos. Repitan INMEDIATAMENTE después del hablante."',
                '<b>PASO 3 — SIN TEXTO (3 min):</b> Di: "Otra vez. Subtítulos APAGADOS. Pantalla boca abajo después de darle play."',
                '<b>PASO 4 — OJOS CERRADOS (2 min):</b> Di: "Última vez. Ojos cerrados. Máxima concentración."',
                '<b>PASO 5 — PAREJAS (2 min):</b> Di: "Celulares ABAJO. Parejas. Repitan lo que recuerden de memoria."',
            ]},
            {'time': '01:34–01:44', 'title': 'HISTORIA INTERACTIVA: EL LUNES LOCO DE VALENTINA (10 min)', 'lines': [
                '<b>Qué es:</b> Historia absurda sobre una semana caótica. Los estudiantes repiten frases clave con "will," actúan y predicen.',
                'Di: "Les voy a contar la historia de Valentina. Valentina tiene la semana más loca del mundo."',
                '"On Monday, Valentina will wake up at 3:00 AM. Why? Because her cat will eat her alarm clock." — "Say it: Her cat will eat her alarm clock." Repiten. "Will Valentina be happy?" Clase: "No!"',
                '"On Tuesday, Valentina will go to work... but she won\'t go by bus. She\'ll go by HORSE." — Actúalo: finge montar un caballo. "Stand up! You are Valentina on the horse!" Se paran y actúan. "Say it: She\'ll go by horse." Revisa la contracción "she\'ll."',
                '"On Wednesday, Valentina won\'t eat lunch. She\'ll eat... her textbook." — Clase: "Ewww!" "Say it: She won\'t eat lunch. She\'ll eat her textbook." Revisa "won\'t" y "she\'ll."',
                '"On Thursday, her boss will call her. Will he say good job? NO. He\'ll say: Valentina, you WILL come to my office NOW." — "Say it: You will come to my office now." Revisa "will" sin contracción (más serio/formal).',
                '"On Friday..." — Di: "¿Qué creen que pasará el viernes? Cada pareja inventa el viernes de Valentina. Usen will." Parejas (3 min). Cada pareja comparte. Las más creativas ganan aplausos.',
                '"On Saturday and Sunday, Valentina won\'t do ANYTHING. She\'ll sleep for 48 hours." — "Say: She\'ll sleep for 48 hours." Repiten.',
            ]},
            {'time': '01:44–01:52', 'title': 'COMPETENCIA: CARRERA DE "WILL" (8 min)', 'lines': [
                '2 equipos de 8. De pie.',
                '<b>Ronda 1 — Afirmativo (2 min):</b> Di un sujeto + un día. El primer equipo en gritar la frase completa correcta gana. "María / Monday" → "María will play on Monday!" (cualquier verbo vale). 4-5 frases.',
                '<b>Ronda 2 — Negativo (2 min):</b> La frase debe ser NEGATIVA. "Juan / Sunday" → "Juan won\'t work on Sunday!" 4-5 frases.',
                '<b>Ronda 3 — Pregunta (2 min):</b> Di sujeto + verbo. Deben formar la PREGUNTA. "Carlos / eat" → "Will Carlos eat on Friday?" 4-5 frases.',
                '<b>Ronda 4 — Contracción (2 min):</b> Di frase COMPLETA. Deben decirla con contracción. "I will go" → "I\'ll go!" / "She will not play" → "She won\'t play!" / "They will eat" → "They\'ll eat!" 5-6 frases. Puntajes en tablero.',
            ]},
            {'time': '01:52–02:00', 'title': 'GOLDLIST + AUTOCHEQUEO + TAREA + CIERRE (8 min)', 'lines': [
                '<b>GoldList (3 min):</b> Di: "Abran su cuaderno de GoldList. Fecha de hoy. Escriban estas palabras — solo ESCRÍBANLAS." Dicta lento: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, will, won\'t, wake up. Di: "Cierren el cuaderno."',
                '<b>Autochequeo (3 min):</b> Entrega la hoja (Módulo 1 A2). Di: "Llenen CADA casilla honestamente." RECOGE. REVISA. Devuelve incompletas. Envía a coordinación HOY.',
                '<b>Tarea (2 min):</b> Escribe en el tablero: TAREA — CLASE 2. 1) Escribe TU plan real para mañana. 7 frases usando "will" con hora y día. Ejemplo: "On Tuesday I will wake up at 6:00 AM. I will eat breakfast at 6:30 AM. I\'ll study at 8:00 AM..." 2) Grábate diciendo tu plan EN VOZ ALTA (ojos cerrados, 30 seg mínimo). Envía por WhatsApp ANTES de la próxima clase. Etiqueta: TAREA A2-1 — [Tu Nombre].',
                'Di: "¿Preguntas? Nos vemos mañana. Welcome to A2."',
                ('SmallNote', 'DESPUÉS: Envía la tarea al grupo de WhatsApp EXACTA. Tarea profesor: Busca en YouTube "how to pronounce days of the week in English" — practica Wednesday /WENZ-dei/ y Thursday /THERZ-dei/. Revisa errores de tu papel.'),
            ]},
        ],
        S,
        special_note='<b>⚠ PRIMERA CLASE DE A2.</b> Los estudiantes vienen de A1 — ya tienen base. Conocen can, should, would, could, might, present/past simple, pronombres, preguntas. HOY aprenden el futuro con "will." No los trates como principiantes — exígeles. Pero celebra que llegaron a A2.'
    )

    # A2 CLASE 1 — REPORTE
    build_report(
        os.path.join(D, 'A2_Clase1_REPORTE.pdf'),
        'A2 | Clase 1 de 55',
        'Módulo 1: I Will Play on Monday — El Futuro con "Will" + Días de la Semana',
        [
            ('VATS: Templanza', '7 min'),
            ('Rompehielo: Mi semana perfecta', '10 min'),
            ('Analizo: Transición A1→A2', '10 min'),
            ('Libro: Módulo 1 — Futuro con will + días', '20 min'),
            ('Ejercicios + Respuestas', '15 min'),
            ('Simulación: Planifica la semana de tu compañero', '20 min'),
            ('Shadowing 5 pasos', '12 min'),
            ('Historia: El lunes loco de Valentina', '10 min'),
            ('Competencia: Carrera de will', '8 min'),
            ('GoldList', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulo 1 A2)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS al inicio (Templanza)',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # ==============================================================
    # A2 CLASE 2 — GUÍA
    # ==============================================================
    build_guide(
        os.path.join(D, 'A2_Clase2_GUIA.pdf'),
        'HEIIU A2 | Clase 2 de 55 | SOLO PARA EL PROFESOR',
        'Módulo 2: Months and Years — Meses, Años y la Preposición "in" | Profesor: ___________ | Fecha: ___/___/___ | Presentes: ___/16',
        [
            {'time': '00:00–00:05', 'title': 'VATS: VIRTUD DE LA SEMANA — TEMPLANZA (5 min)', 'lines': [
                'Escribe en el tablero: TEMPLANZA — "What is the difference between discipline and punishment? Can discipline be positive?"',
                '<b>V (1 min):</b> Lee la pregunta. <b>A (30 seg):</b> "Think in silence." <b>T (2 min):</b> "Pairs. Discuss in English. Use what you know." <b>S (1.5 min):</b> 2-3 estudiantes comparten. Corrige solo si es necesario.',
            ]},
            {'time': '00:05–00:15', 'title': 'ROMPEHIELO: BINGO DE CUMPLEAÑOS (10 min)', 'lines': [
                '<b>Qué es:</b> Los estudiantes caminan por el salón buscando a alguien que cumpla años en cada mes. Esto introduce los 12 meses ANTES de abrir el libro.',
                'Escribe en el tablero los 12 meses. Pronúncialos. La clase repite CADA UNO: January — February — March — April — May — June — July — August — September — October — November — December.',
                '<b>Pronunciaciones difíciles:</b> February → /FEB-ru-eri/ (no "Febreri"). August → /AW-gust/ (la Au suena como Aw).',
                'Di: "Levántense. Caminen. Pregúntenle a cada persona: When is your birthday? La respuesta es: My birthday is in [month]. Cuando encuentren a alguien, escriban su nombre al lado del mes." Deben encontrar AL MENOS 6 meses diferentes en 5 minutos.',
                'Si nadie cumple en un mes, inventan: "If nobody has a birthday in March, find someone who knows someone with a birthday in March."',
                'Después de 5 min: "Siéntense. ¿Quién encontró los 12 meses? ¿10? ¿8?" Celebra. "What month has the MOST birthdays in this class?" Cuentan.',
            ]},
            {'time': '00:15–00:25', 'title': 'ANALIZO: REVISIÓN DE TAREA (10 min)', 'lines': [
                'Tarea de la Clase 1: Escribir plan real para mañana con "will" + 7 frases + grabación.',
                '<b>Primeros 3 min:</b> Di: "¿Quién envió su video de tarea?" Cuenta. Los que NO: "Escriban 3 frases con will sobre hoy AHORA MISMO. Me las enseñan antes de que termine la actividad."',
                '<b>Siguientes 7 min:</b> Parejas. Di: "Lean a su compañero sus 7 frases con will. El compañero revisa: ¿usaron will correctamente? ¿Usaron on para los días? ¿Las horas están bien?" Cada pareja comparte 1 frase con la clase. Corrige: "No. Listen." + versión correcta.',
            ]},
            {'time': '00:25–00:40', 'title': 'LIBRO: MÓDULO 2 — MESES Y AÑOS (15 min)', 'lines': [
                'Di: "Abran su libro A2 en el Módulo 2 — Months and Years. Lean la Guía 1 con su compañero. Tienen 6 minutos."',
                '<b>Primeros 6 min:</b> Leen en parejas. Camina.',
                '<b>Siguientes 9 min:</b> Siéntate con cada pareja. ELLOS te explican:',
                '1) ¿Qué preposición se usa para meses y años? → "in" — "in January," "in 2024." Contraste con "on" de la Clase 1: "ON Monday" vs "IN January."',
                '2) ¿Cómo se dicen los años en inglés? → Dos grupos de dos números: 1982 → "nineteen eighty-two."',
                '3) ¿Cuál es la excepción? → 2000-2009: "two thousand," "two thousand and one," etc.',
                'Dales 3 años: 1995 → "Nineteen ninety-five." 2024 → "Twenty twenty-four." 2003 → "Two thousand and three." Si está mal: "No. Listen." + versión correcta + repiten.',
                ('SmallNote', 'Si confunden "on" y "in": NO expliques la regla. Solo di: "IN January. ON Monday. IN 2024. ON Tuesday." Repiten. El patrón se absorbe.'),
            ]},
            {'time': '00:40–00:52', 'title': 'EJERCICIOS + RESPUESTAS (12 min)', 'lines': [
                'Di: "Hagan los ejercicios del módulo. Revisen con las Answer Keys. Pregúntenle a su compañero primero."',
                'CAMINA — versión correcta solamente. Si más del 50% tiene el mismo error: PARA, al tablero, repiten.',
                ('SmallNote', 'Busca en YouTube un clip para Shadowing: alguien hablando de fechas, cumpleaños, o planes futuros con meses ("I was born in March," "In 2025 I will..."). Envía el link al WhatsApp.'),
            ]},
            {'time': '00:52–01:12', 'title': 'SIMULACIÓN: LÍNEA DE TIEMPO DE MI VIDA (20 min)', 'lines': [
                '<b>Qué es:</b> Cada estudiante crea una línea de tiempo con 8 eventos de su vida usando meses, años, "in," y "will" para el futuro.',
                '<b>Paso 1 — Modelo (2 min):</b> Dibuja una línea horizontal en el tablero con 4 puntos del pasado y 4 del futuro. Lee en voz alta: "I was born in May, nineteen ninety. I started school in January, two thousand eight. In 2027, I will buy a house. In 2030, I will live in Canada."',
                '<b>Paso 2 — Crear (7 min):</b> Di: "Hagan su propia línea de tiempo. 4 eventos del PASADO y 4 del FUTURO. Usen meses, años, in, y will para el futuro." Camina ayudando. Errores comunes: "on 1995" (debe ser "in 1995"), "in Monday" (debe ser "on Monday"). Señala: "Check this. IN or ON?"',
                '<b>Paso 3 — Parejas (5 min):</b> Di: "Presenten su línea de tiempo a su compañero. El compañero escucha y hace UNA pregunta: What will you do in [year]?"',
                '<b>Paso 4 — Compartir (4 min):</b> 4 estudiantes comparten su evento futuro más interesante. "¿Quién tiene el plan más ambicioso? ¿El más loco?" Votan.',
                '<b>Paso 5 — Debate rápido (2 min):</b> "¿Es mejor planificar el futuro o vivir el momento?" Levantan mano. 2 de cada lado dicen UNA frase en inglés.',
            ]},
            {'time': '01:12–01:22', 'title': 'SHADOWING 5 PASOS (10 min)', 'lines': [
                '<b>PASO 1 — ESCUCHAR (2 min):</b> "Abran el video del WhatsApp. Solo escuchen."',
                '<b>PASO 2 — CON TEXTO (2 min):</b> "Otra vez. Subtítulos. Repitan."',
                '<b>PASO 3 — SIN TEXTO (2 min):</b> "Subtítulos APAGADOS. Repitan."',
                '<b>PASO 4 — OJOS CERRADOS (2 min):</b> "Ojos cerrados. Repitan."',
                '<b>PASO 5 — PAREJAS (2 min):</b> "Celulares ABAJO. De memoria en parejas."',
            ]},
            {'time': '01:22–01:37', 'title': 'HISTORIA INTERACTIVA: EL AÑO MÁS EXTRAÑO DE LA HISTORIA (15 min)', 'lines': [
                '<b>Qué es:</b> Historia absurda sobre eventos históricos inventados con meses y años. Los estudiantes participan, corrigen, y agregan.',
                'Di: "Les voy a contar sobre el año más extraño de la historia humana." Cuenta LENTO. Pausa para que repitan:',
                '"In January, nineteen ninety-nine, a man in Japan discovered that dogs can read." — "Say it: In January, nineteen ninety-nine." Revisa pronunciación.',
                '"In March, two thousand one, scientists found a pizza buried under the ocean. It was 500 years old." — "How do you say 2001?" Clase: "Two thousand and one!" "And when was the pizza made?" Clase hacen cálculos: "In fifteen oh one!" (1501). Celebra.',
                '"In August, twenty ten, a cat became the president of a small island." — "Say it: In August, twenty ten." Revisa "August" → /AW-gust/.',
                '"In February, twenty twenty-three, someone invented shoes that walk by themselves." — "Say: In February, twenty twenty-three." Revisa "February" → /FEB-ru-eri/.',
                '<b>"And now... el futuro. What WILL happen? In December, twenty thirty..."</b> — Señala una pareja: "¿Qué pasará en December, twenty thirty? Inventen algo." La pareja dice una frase con "will" + "in December, twenty thirty." Pasa a la siguiente pareja con un mes y año diferente. 4-5 parejas agregan al futuro de la historia.',
            ]},
            {'time': '01:37–01:49', 'title': 'COMPETENCIA: CARRERA DE FECHAS (12 min)', 'lines': [
                '2 equipos de 8. De pie.',
                '<b>Ronda 1 — Meses (3 min):</b> Di un número del 1 al 12. El primer equipo en gritar el mes correcto gana. "3" → "MARCH!" "9" → "SEPTEMBER!" "2" → "FEBRUARY!" 8-10 números.',
                '<b>Ronda 2 — Años (3 min):</b> Escribe un año en el tablero. Primer equipo en decirlo correctamente gana. 1987 → "Nineteen eighty-seven!" 2005 → "Two thousand and five!" 2024 → "Twenty twenty-four!" 1776 → "Seventeen seventy-six!" 6-8 años.',
                '<b>Ronda 3 — "In" o "On" (3 min):</b> Di una palabra. Gritan la preposición correcta. "January" → "IN!" "Monday" → "ON!" "2024" → "IN!" "Friday" → "ON!" 10 palabras rápidas.',
                '<b>Ronda 4 — Frase completa (3 min):</b> Di mes + año + verbo. Arman frase con "will." "July / 2026 / travel" → "I will travel in July, twenty twenty-six!" 5 frases. Puntajes en tablero.',
            ]},
            {'time': '01:42–01:45', 'title': 'CONSTRUIR: MI MES FAVORITO (3 min)', 'lines': [
                'Di: "Con lo que tengan en el escritorio, construyan algo que represente su MES FAVORITO. Tienen 1 minuto." Después: "Presenten en UNA frase: My favorite month is [month] because I will [verbo] in [month]." 10 seg cada uno.',
            ]},
            {'time': '01:45–02:00', 'title': 'GOLDLIST + AUTOCHEQUEO + TAREA + CIERRE (15 min)', 'lines': [
                '<b>⚠ PREPARACIÓN DEL TABLERO:</b> ANTES de que lleguen los estudiantes (o durante una actividad donde no necesites el tablero), escribe las 20 frases del GoldList — AMBOS IDIOMAS, EXACTAMENTE como aparecen en esta guía. No traduzcas de memoria.',
                '<b>⚠ EL CUADERNO DE GOLDLIST SE QUEDA EN LA ACADEMIA.</b> Los estudiantes NO se lo llevan. Recoge todos los cuadernos al final. Esto asegura que no estudien en casa (lo cual arruinaría el método).',
                '<b>GoldList (10 min):</b> Di: "Tomen su cuaderno de GoldList. Fecha de hoy. Copien las frases del tablero: inglés a la izquierda, español a la derecha. Con calma y buena letra." Los estudiantes copian (8 min): 1. I think that\'s a good idea. / Creo que es una buena idea. 2. I disagree because ___. / No estoy de acuerdo porque ___. 3. What do you think about ___? / ¿Qué piensas sobre ___? 4. In my opinion, ___. / En mi opinión, ___. 5. Could you explain that again? / ¿Podría explicar eso de nuevo? 6. I\'m planning to ___ next week. / Estoy planeando ___ la próxima semana. 7. What are you going to do this weekend? / ¿Qué vas a hacer este fin de semana? 8. I will try my best. / Voy a dar lo mejor de mí. 9. I haven\'t decided yet. / Todavía no he decidido. 10. It depends on ___. / Depende de ___. 11. It was one of the best experiences of my life. / Fue una de las mejores experiencias de mi vida. 12. I\'ve been studying English for ___ months. / He estado estudiando inglés por ___ meses. 13. I used to ___ when I was younger. / Yo solía ___ cuando era más joven. 14. The reason I\'m learning English is ___. / La razón por la que estoy aprendiendo inglés es ___. 15. I\'m interested in ___. / Estoy interesado/a en ___. 16. I\'m sorry, I didn\'t catch your name. / Lo siento, no escuché tu nombre. 17. Would you mind repeating that? / ¿Te importaría repetir eso? 18. I\'m looking for ___. / Estoy buscando ___. 19. Could you recommend something? / ¿Podría recomendar algo? 20. That makes sense. / Eso tiene sentido. Cuando terminen (2 min): "Lean la lista UNA vez conmigo." Repiten. UNA vez. "Cierren el cuaderno. NO las estudien. En dos semanas volvemos." <b>RECOGE TODOS LOS CUADERNOS.</b>',
                ('SmallNote', 'PROFESOR: A partir de hoy, usa estas frases NATURALMENTE en clase sin decir "esto es de tu GoldList." Modela: "I think that\'s a good idea," "What do you think about...?", "That makes sense." La exposición inconsciente hace funcionar el método.'),
                '<b>Autochequeo (3 min):</b> Entrega la hoja (Módulo 2 A2). RECOGE. REVISA. Envía a coordinación HOY.',
                '<b>Tarea (2 min):</b> Escribe en el tablero: TAREA — CLASE 3. 1) Escribe 6 eventos importantes de tu vida con el mes y el año. 3 del pasado, 3 del futuro. Ejemplo: "I was born in October, nineteen ninety-eight." "I will graduate in July, twenty twenty-seven." 2) Grábate diciendo los 12 meses en orden + 3 años importantes para ti (ojos cerrados, 30 seg mínimo). Envía por WhatsApp. Etiqueta: TAREA A2-2 — [Tu Nombre].',
                'Di: "¿Preguntas? Nos vemos mañana."',
                ('SmallNote', 'DESPUÉS: Envía la tarea al grupo de WhatsApp EXACTA. Tarea profesor: Practica la pronunciación de "February" /FEB-ru-eri/ y "August" /AW-gust/. Revisa tu papel de errores: ¿confundieron in y on? ¿Dijeron mal algún año?'),
            ]},
        ],
        S
    )

    # A2 CLASE 2 — REPORTE
    build_report(
        os.path.join(D, 'A2_Clase2_REPORTE.pdf'),
        'A2 | Clase 2 de 55',
        'Módulo 2: Months and Years — Meses, Años y la Preposición "in"',
        [
            ('VATS: Templanza', '5 min'),
            ('Rompehielo: Bingo de cumpleaños', '10 min'),
            ('Analizo: Revisión de tarea', '10 min'),
            ('Libro: Módulo 2 — Meses y años', '15 min'),
            ('Ejercicios + Respuestas', '12 min'),
            ('Simulación: Línea de tiempo de mi vida', '20 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Historia: El año más extraño', '15 min'),
            ('Competencia: Carrera de fechas', '12 min'),
            ('Construir: Mi mes favorito', '3 min'),
            ('GoldList (20 frases)', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulo 2 A2)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Templanza)',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # ==============================================================
    # REFUERZO YEISON — SESIÓN 1
    # ==============================================================
    build_guide(
        os.path.join(D, 'A1', 'REFUERZO_Yeison_Sesion1_GUIA.pdf'),
        'HEIIU A1 | REFUERZO PERSONALIZADO — SESIÓN 1 de 2 | SOLO PARA EL PROFESOR',
        'Estudiante: Yeison | Listening 6/24 (25%) · Reading 28/30 (93%) · Writing 18/30 (60%) · Speaking 10/16 (62%) · Total: 62% | Profesor: ___________ | Fecha: ___/___/___',
        [
            {'time': '00:00–00:08', 'title': 'ROMPER EL HIELO: CONVERSACIÓN REAL (8 min)', 'lines': [
                'Di: "Antes de empezar, quiero conocerte. Vamos a hablar en español primero."',
                'Pregúntale (en español): "¿Por qué estás aprendiendo inglés?" "¿Qué fue lo más difícil del nivel A1 para ti?" "¿Qué te gustaría poder hacer en inglés que hoy no puedes?"',
                'Escucha. No juzgues. Después di: "Perfecto. En estas 4 horas vamos a trabajar exactamente en eso. Hoy nos enfocamos en que tu oído empiece a entender inglés. Mañana en que puedas hablar con más confianza."',
                ('SmallNote', 'Yeison está aquí porque perdió. Probablemente se siente frustrado. Tu primer trabajo es que se sienta SEGURO. No digas "esto es fácil" ni "ya deberías saber esto."'),
            ]},
            {'time': '00:08–00:18', 'title': 'DIAGNÓSTICO RÁPIDO: ¿QUÉ ESCUCHAS? (10 min)', 'lines': [
                '<b>Qué es:</b> Tú dices frases simples en inglés. Yeison dice lo que entendió — en español está bien. Esto te dice EXACTAMENTE dónde está su oído.',
                'Di: "Voy a decirte unas frases en inglés. Dime lo que entiendas — puede ser en español, no importa. Solo quiero saber qué escuchas."',
                '1. "My name is Carlos." (¿Entendió name?) · 2. "I can play soccer." (¿can y play?) · 3. "She lives in Bogotá." (¿she y lives?) · 4. "What is your name?" (¿Reconoce la pregunta?) · 5. "I don\'t understand." (¿don\'t y understand?)',
                '6. "He played soccer yesterday." (¿played y yesterday?) · 7. "Can you repeat that?" (¿Reconoce la petición?) · 8. "They are my friends." (¿they y friends?) · 9. "Where do you live?" (¿where?) · 10. "I would like water, please." (¿would like y water?)',
                '<b>Anota cuáles entendió y cuáles no.</b> Esto te guía para el resto de la sesión. Di: "No te preocupes por las que no entendiste — para eso estamos aquí."',
            ]},
            {'time': '00:18–00:30', 'title': 'PRONOMBRES: ESCUCHAR + IDENTIFICAR (12 min)', 'lines': [
                '<b>Paso 1 — Escuchar y señalar (4 min).</b> Escribe en un papel los 7 pronombres: I, YOU, HE, SHE, IT, WE, THEY. Ponlo frente a Yeison.',
                'Di frases. Yeison señala el pronombre que escuchó. Empieza lento, ve más rápido. Las 15 frases: 1. "SHE can cook." 2. "THEY play soccer." 3. "WE are students." 4. "HE lives in Medellín." 5. "I don\'t understand." 6. "IT is very big." 7. "SHE plays guitar." 8. "THEY can\'t swim." 9. "HE went to school." 10. "WE like pizza." 11. "I can play soccer." 12. "SHE doesn\'t like coffee." 13. "THEY live in Bogotá." 14. "IT works very well." 15. "HE can\'t drive."',
                '<b>Paso 2 — Yeison produce (4 min).</b> Tú señalas un pronombre. Yeison dice una frase con ese pronombre. Si no puede, dale el inicio: "He can..." y Yeison completa.',
                '<b>Paso 3 — Dictado rápido (4 min).</b> Di 6 frases con pronombres. Yeison las ESCRIBE. Comparan. Revisa errores — ¿confunde he/she? ¿Olvida they?',
            ]},
            {'time': '00:30–00:42', 'title': 'CAN / CAN\'T: ESCUCHAR LA DIFERENCIA (12 min)', 'lines': [
                '<b>Paso 1 — La diferencia (3 min).</b> Di: "Escucha la diferencia." "I CAN swim." (can = /kæn/ rápido, átono) vs "I CAN\'T swim." (can\'t = /kænt/ con T final fuerte). Repite 5 veces cada una. Exagera la T. Yeison repite.',
                '<b>Paso 2 — ¿Can o can\'t? (5 min).</b> Di frases. Yeison dice CAN o CAN\'T. Si falla, repite más lento. Las 15 frases: 1. "I can play guitar" →CAN 2. "She can\'t cook" →CAN\'T 3. "They can dance" →CAN 4. "He can\'t swim" →CAN\'T 5. "We can speak English" →CAN 6. "I can\'t understand" →CAN\'T 7. "You can help me" →CAN 8. "She can\'t drive" →CAN\'T 9. "He can play piano" →CAN 10. "I can\'t sleep" →CAN\'T 11. "They can\'t come today" →CAN\'T 12. "We can do it" →CAN 13. "She can sing very well" →CAN 14. "I can\'t remember" →CAN\'T 15. "He can run fast" →CAN.',
                '<b>Paso 3 — Yeison produce (4 min).</b> Pregúntale una por una. Yeison responde: "Yes, I can." o "No, I can\'t." Las 10 preguntas: 1. "Can you cook?" 2. "Can you swim?" 3. "Can you drive?" 4. "Can you play an instrument?" 5. "Can you speak French?" 6. "Can you dance?" 7. "Can you sing?" 8. "Can you ride a bicycle?" 9. "Can you play chess?" 10. "Can you draw?" Corrige pronunciación de can/can\'t.',
            ]},
            {'time': '00:42–00:54', 'title': 'PRESENT SIMPLE: ESCUCHAR + REPETIR (12 min)', 'lines': [
                '<b>Paso 1 — Escuchar la S (4 min).</b> Tercera persona lleva S. Di pares, Yeison dice cuál tiene S: 1. "I play" vs "He plays" 2. "We live" vs "She lives" 3. "They work" vs "It works" 4. "I eat" vs "She eats" 5. "We study" vs "He studies" 6. "They like" vs "She likes" 7. "I cook" vs "He cooks" 8. "We dance" vs "She dances" 9. "They read" vs "He reads" 10. "I sleep" vs "It sleeps". Después di solo una frase y Yeison dice "con S" o "sin S."',
                '<b>Paso 2 — Preguntas DO/DOES (4 min).</b> Di preguntas, Yeison responde con frase completa. Las 8: 1. "Do you play soccer?" 2. "Does your mom cook?" 3. "Do your friends speak English?" 4. "Does your dad work?" 5. "Do you like pizza?" 6. "Does your sister study?" 7. "Do you live near here?" 8. "Does your best friend dance?"',
                '<b>Paso 3 — Yeison pregunta (4 min).</b> Yeison te hace preguntas a TI. Dale temas uno por uno: 1. Tu comida → "Do you like ___?" 2. Tu deporte → "Do you play ___?" 3. Tu hermano/a → "Does your brother/sister work?" 4. Tu mamá → "Does your mom cook?" 5. Tus amigos → "Do your friends speak English?" 6. Tu mascota → "Do you have a pet?" 7. Tu papá → "Does your dad play soccer?" 8. Dónde vives → "Do you live in ___?" Si la pregunta está mal: Di: "No." Di: "Listen. DOES your brother work?"',
            ]},
            {'time': '00:54–01:06', 'title': 'PAST SIMPLE: AYER VS HOY (12 min)', 'lines': [
                '<b>Paso 1 — Escuchar -ED (4 min).</b> Di presente y pasado. Yeison repite SOLO la pasada: play→played, cook→cooked, live→lived, work→worked, want→wanted, need→needed. Después al revés: di pasada, Yeison dice el verbo base.',
                '<b>Paso 2 — Irregulares comunes (4 min).</b> Escribe en un papel: go→went, eat→ate, have→had, see→saw, do→did, come→came, say→said, get→got. Di la forma pasada, Yeison dice el verbo base. Luego al revés. Después frases: "I went to the store" → went = go.',
                '<b>Paso 3 — Ayer (4 min).</b> Di: "Cuéntame qué hiciste ayer." Si Yeison usa presente ("I go to school"), di: "No. Listen. Yesterday, I WENT to school." Yeison repite. Pídele 5 frases de ayer. Corrige cada una.',
            ]},
            {'time': '01:06–01:18', 'title': 'LISTENING INTENSIVO: DICTADO PROGRESIVO (12 min)', 'lines': [
                '<b>Nivel 1 — Palabras sueltas (2 min).</b> Dicta 8 palabras: play, kitchen, yesterday, friend, bathroom, understand, soccer, beautiful. Yeison escribe. Revisa.',
                '<b>Nivel 2 — Frases cortas (3 min).</b> 5 frases: "I can play." "She lives here." "They don\'t understand." "He went to school." "Can you help me?" Yeison escribe. Revisa.',
                '<b>Nivel 3 — Frases largas (4 min).</b> 4 frases (di cada una 2 veces): "My friend played soccer yesterday." "She can\'t cook but she can dance very well." "Where do you live? I live in Bucaramanga." "He went to the store and he bought some water."',
                '<b>Nivel 4 — Mini-párrafo (3 min).</b> Di cada oración 2 veces: "My name is Carlos. I live in Bogotá. Yesterday I went to the park. I played soccer with my friends. They can play very well but I can\'t. I want to practice more." Yeison escribe. Revisan. Celebra lo que hizo bien.',
            ]},
            {'time': '01:18–01:30', 'title': 'DESCANSO + REFLEXIÓN (12 min)', 'lines': [
                'Di: "Vamos a descansar 10 minutos. Pero antes, dime: ¿qué fue lo más difícil hasta ahora? ¿Y qué sientes que ya entiendes mejor?"',
                'Escucha. Anota lo que dice — esto te ayuda para la segunda hora. Descanso real: agua, baño, celular.',
            ]},
            {'time': '01:30–01:42', 'title': 'PREGUNTAS: WH- QUESTIONS LISTENING (12 min)', 'lines': [
                '<b>Paso 1 — Identificar (4 min).</b> Di una pregunta. Yeison dice QUÉ palabra de pregunta escuchó: "What is your name?" → WHAT. "Where do you live?" → WHERE. "When did you go?" → WHEN. "How old are you?" → HOW. 12 preguntas. Si confunde: "No. Listen. WHERE do you live?" Exagera el WHERE.',
                '<b>Paso 2 — Responder (4 min).</b> Di preguntas WH-. Yeison responde con frase completa: "What is your name?" → "My name is Yeison." "Where do you live?" → "I live in [ciudad]." "How old are you?" → "I am [edad] years old." "Where did you go yesterday?" → "I went to [lugar]."',
                '<b>Paso 3 — Yeison pregunta (4 min).</b> Dale tarjetas con WHAT, WHERE, WHEN, HOW. Tú le das un tema y él hace la pregunta: mi nombre → "What is your name?" mi edad → "How old are you?" dónde vivo → "Where do you live?"',
            ]},
            {'time': '01:42–01:52', 'title': 'SHADOWING 1 A 1: IMITACIÓN EXACTA (10 min)', 'lines': [
                '<b>Ronda 1 — Frases cortas (3 min):</b> "I can play." "She lives here." "Where do you live?" "He went to school." "Can you help me?" Yeison repite EXACTAMENTE — ritmo, velocidad, entonación.',
                '<b>Ronda 2 — Frases largas (3 min):</b> "My friend can play soccer very well." "I don\'t understand what you said." "She went to the store yesterday." "What time does the class start?"',
                '<b>Ronda 3 — Velocidad normal (4 min):</b> Habla a velocidad NORMAL. Yeison intenta seguirte: "I went to the park yesterday and I played soccer with my friends." "She can\'t cook but she can dance and she loves music." Si no puede, baja UN POCO — pero no demasiado.',
            ]},
            {'time': '01:52–02:00', 'title': 'CIERRE: QUÉ APRENDIMOS + TAREA (8 min)', 'lines': [
                'Di: "Dime 3 cosas que sientes que mejoró tu oído hoy." Yeison responde (español está bien, pero anímalo a intentar en inglés).',
                '<b>Tarea para la Sesión 2:</b> 1) Busca en YouTube "English listening practice A1" — escoge un video de 3-5 min. Escúchalo 3 veces: 1ra solo escucha, 2da con subtítulos, 3ra sin subtítulos repitiendo lo que pueda. 2) Escribe 5 frases sobre tu día de ayer usando past simple. Ej: "I woke up at 7. I went to work." 3) Grábate diciendo las 5 frases (30 seg, ojos cerrados). Envía por WhatsApp.',
                'Di: "En la próxima sesión vamos a hablar MUCHO más. Hoy fue para que tu oído se abriera. Mañana es para que tu boca se suelte. Buen trabajo hoy."',
            ]},
        ],
        S,
        special_note='<b>⚠ SESIÓN 1 DE 2 — REFUERZO PERSONALIZADO.</b> Yeison perdió A1 con 62% (necesita 70%). Su listening es crítico (25%). Lee muy bien (93%) pero no entiende cuando escucha ni produce cuando habla. Esta sesión conecta lo que ya sabe leer con su oído. Sé paciente. No juzgues. Haz que se sienta seguro.',
        is_reinforcement=True
    )

    # REFUERZO YEISON — REPORTE SESIÓN 1
    build_report(
        os.path.join(D, 'A1', 'REFUERZO_Yeison_Sesion1_REPORTE.pdf'),
        'REFUERZO Yeison | Sesión 1 de 2',
        'Listening intensivo + Gramática oral | Estudiante: Yeison',
        [
            ('Romper el hielo: Conversación real', '8 min'),
            ('Diagnóstico: ¿Qué escuchas?', '10 min'),
            ('Pronombres: Escuchar + Identificar', '12 min'),
            ('Can/Can\'t: Escuchar la diferencia', '12 min'),
            ('Present simple: Escuchar + Repetir', '12 min'),
            ('Past simple: Ayer vs Hoy', '12 min'),
            ('Listening intensivo: Dictado progresivo', '12 min'),
            ('Descanso + Reflexión', '12 min'),
            ('Preguntas: WH- Questions listening', '12 min'),
            ('Shadowing 1 a 1: Imitación exacta', '10 min'),
            ('Cierre + Tarea', '8 min'),
        ],
        [
            'Papel de errores (entregado físico con la guía)',
            'Notas del diagnóstico inicial (10 frases)',
        ],
        [
            'Yeison se sintió seguro y cómodo',
            'Usé "No. Listen." + modelo (no expliqué reglas)',
            'Anoté errores frecuentes en papel',
            'Identifiqué qué necesita refuerzo en Sesión 2',
        ],
        S
    )

    # ==============================================================
    # REFUERZO YEISON — SESIÓN 2
    # ==============================================================
    build_guide(
        os.path.join(D, 'A1', 'REFUERZO_Yeison_Sesion2_GUIA.pdf'),
        'HEIIU A1 | REFUERZO PERSONALIZADO — SESIÓN 2 de 2 | SOLO PARA EL PROFESOR',
        'Estudiante: Yeison | Listening 6/24 (25%) · Reading 28/30 (93%) · Writing 18/30 (60%) · Speaking 10/16 (62%) · Total: 62% | Profesor: ___________ | Fecha: ___/___/___',
        [
            {'time': '00:00–00:08', 'title': 'REVISIÓN DE TAREA + CALENTAMIENTO (8 min)', 'lines': [
                '<b>Tarea (5 min):</b> Di: "¿Hiciste la tarea? Muéstrame." Si hizo las 5 frases en past simple: léanlas juntos. Corrige: "No. Listen." + versión correcta. Si grabó audio: escúchenlo juntos. Di: "Dos cosas que hiciste bien: [X] y [Y]. Dos cosas para mejorar: [X] y [Y]."',
                'Si NO hizo la tarea: No regañes. Di: "OK, vamos a hacerla juntos. Dime 5 cosas que hiciste ayer." Yeison dice, tú corriges, él escribe.',
                '<b>Calentamiento oral (3 min):</b> Di: "Ahora en inglés. Yo pregunto, tú respondes." Preguntas: "What did you do yesterday?" "What can you play?" "Where do you live?" "How old are you?" Si responde con frases incompletas ("Soccer"), di: "Full sentence. I can play soccer." Yeison repite la frase completa.',
            ]},
            {'time': '00:08–00:20', 'title': 'SPEAKING: HABLAR SOBRE MÍ — PRESENTACIÓN 1 MIN (12 min)', 'lines': [
                '<b>Modelo (2 min):</b> Tú primero: "My name is [nombre]. I am [edad] years old. I live in [ciudad]. I am a [profesión]. I can [habilidad] and I can [habilidad], but I can\'t [algo]. I like [algo]. Yesterday I [verbo pasado]."',
                '<b>Construir (5 min):</b> Di: "Ahora tú. Vamos frase por frase." Ayúdalo con el inicio: "My name is..." → Yeison completa. "I am... years old." → Yeison completa. "I live in..." "I am a..." "I can... and I can... but I can\'t..." "I like..." "Yesterday I..." Si dice "I have 25 years" → "No. Listen. I AM 25 years old." Repite.',
                '<b>Practicar (3 min):</b> Di: "Ahora dilo TODO de corrido. Sin ayuda." 3 intentos. Si se detiene, dale la primera palabra y deja que siga. Al tercer intento debería fluir.',
                '<b>Grabación (2 min):</b> Di: "Ahora te vas a grabar. Ojos cerrados. Sin notas. Solo tu voz." Yeison se graba. Escuchan juntos.',
            ]},
            {'time': '00:20–00:32', 'title': 'WRITING: CORREGIR ERRORES COMUNES (12 min)', 'lines': [
                '<b>Paso 1 — Corregir 10 frases (6 min).</b> Escribe en un papel estas frases con errores. Di: "Estas frases tienen errores. Corrígelas." Yeison las corrige:',
                '1. She can plays soccer → can play. 2. I have 25 years → I am 25 years old. 3. He don\'t like pizza → doesn\'t like. 4. Where you live? → Where do you live? 5. I go to school yesterday → went. 6. Him can swim → He can swim. 7. What you can do? → What can you do? 8. She don\'t can cook → She can\'t cook. 9. They plays soccer → They play. 10. I no understand → I don\'t understand.',
                '<b>Paso 2 — Dictado con trampas (6 min).</b> Dicta 6 frases — ALGUNAS correctas, OTRAS con errores. Yeison escribe lo que cree correcto: 1. "He can play guitar" (OK) 2. "She don\'t like coffee" (ERROR→doesn\'t) 3. "I went to the park yesterday" (OK) 4. "Where she lives?" (ERROR→Where does she live?) 5. "They can\'t swim" (OK) 6. "I am have a question" (ERROR→I have a question). Revisa juntos. AQUÍ sí puedes explicar brevemente porque es refuerzo.',
            ]},
            {'time': '00:32–00:44', 'title': 'LISTENING + SPEAKING: CONVERSACIÓN GUIADA (12 min)', 'lines': [
                '<b>Tema: Un día normal de Yeison.</b> Di: "Vamos a hablar de tu día normal. Yo pregunto, tú respondes con frase COMPLETA." Pregunta y espera respuesta completa:',
                '"What time do you wake up?" → "I wake up at [hora]." "What do you eat for breakfast?" → "I eat [comida]." "How do you go to work/school?" → "I go by [transporte]." "What do you do at work?" → "I [actividad]." "What time do you eat lunch?" → "I eat lunch at [hora]." "What do you do after work?" → "I [actividad]." Si responde con una sola palabra: "Full sentence. I wake up at 6."',
                '<b>Después cambia al PASADO:</b> "What did you eat for breakfast YESTERDAY?" → "I ate [comida]." "Where did you go yesterday?" → "I went to [lugar]." "What did you do last weekend?" → "I [verbo pasado]." Corrige cada error.',
            ]},
            {'time': '00:44–00:56', 'title': 'SPEAKING: DESCRIBE LA IMAGEN (12 min)', 'lines': [
                '<b>Paso 1 — Tú describes, Yeison escucha (3 min).</b> Dibuja una escena simple: familia + actividades. Describe: "This is a family. The father can cook. The mother plays soccer. They have two children. The boy is 10. Yesterday they went to the park." Después preguntas: "How old is the boy?" "Can the father cook?" "Where did they go?"',
                '<b>Paso 2 — Yeison describe (5 min).</b> Dibuja OTRA escena. Yeison la describe usando pronombres, can/can\'t, present simple, y mínimo 1 frase en pasado. Si se queda callado: "This is a..." y deja que siga.',
                '<b>Paso 3 — Preguntas cruzadas (4 min).</b> Yeison te hace preguntas sobre TU dibujo. Tú le haces preguntas sobre el de él. Todo en inglés. Si forma mal la pregunta: "No. Listen. DOES the father cook?"',
            ]},
            {'time': '00:56–01:08', 'title': 'DESCANSO + ESCUCHAR AUDIO (12 min)', 'lines': [
                'Descanso real: 5 min (agua, baño, celular).',
                '<b>Después (7 min):</b> Busca en YouTube un audio/video corto (máximo 60 segundos) nivel A1 — alguien hablando de su rutina o presentándose. 1ra vez: solo escucha. 2da vez: escribe las palabras que reconoce. 3ra vez: intenta repetir cada frase. Revisa lo que escribió. Celebra las palabras que reconoció.',
            ]},
            {'time': '01:08–01:20', 'title': 'WRITING: ESCRIBIR UN PÁRRAFO (12 min)', 'lines': [
                'Di: "Vas a escribir un párrafo sobre ti. Mínimo 8 frases. Incluye: nombre, edad, dónde vives, qué haces, qué puedes hacer, qué hiciste ayer. Tienes 8 minutos."',
                'Yeison escribe. NO lo ayudes — deja que cometa errores. Camina en silencio.',
                '<b>Revisión (4 min):</b> Revisa JUNTOS, frase por frase. Para cada error: señala, di "No. Listen." + versión correcta. Yeison escribe la corrección al lado. Cuenta errores: "Tuviste [X] errores en [Y] frases. La próxima vez va a ser menos."',
            ]},
            {'time': '01:20–01:32', 'title': 'SPEAKING: SIMULACIÓN — ENTREVISTA DE TRABAJO (12 min)', 'lines': [
                '<b>Preguntas:</b> 1. What is your name? 2. How old are you? 3. Where do you live? 4. What do you do? 5. What can you do well? 6. Can you work on weekends? 7. Where did you work before? 8. Why do you want this job?',
                '<b>Preparar respuestas (4 min):</b> Di: "Prepara tus respuestas. Dímelas EN VOZ ALTA — no las escribas." Yeison dice cada respuesta. Corriges gramática y pronunciación.',
                '<b>Simulación (4 min):</b> Di: "Ahora es en serio. Yo soy el entrevistador. Mírame a los ojos. Responde como si fuera una entrevista real." Haz las 8 preguntas. Sé serio. Contacto visual.',
                '<b>Retroalimentación (2 min):</b> Di: "Muy bien. Dos cosas que hiciste bien: [X] y [Y]. Dos cosas para mejorar: [X] y [Y]." Repite las 2 frases que más le costaron. Yeison las dice 3 veces.',
            ]},
            {'time': '01:32–01:42', 'title': 'LISTENING FINAL: DICTADO COMPLETO (10 min)', 'lines': [
                '<b>Mismas 10 frases del diagnóstico de la Sesión 1.</b> Dicta: 1. "My name is Carlos." 2. "I can play soccer." 3. "She lives in Bogotá." 4. "What is your name?" 5. "I don\'t understand." 6. "He played soccer yesterday." 7. "Can you repeat that?" 8. "They are my friends." 9. "Where do you live?" 10. "I would like water, please."',
                'Yeison las escribe. <b>Compara con Sesión 1:</b> "En la Sesión 1 entendiste [X] de 10. Hoy entendiste [Y] de 10. Mejoraste [diferencia]."',
            ]},
            {'time': '01:42–01:52', 'title': 'SIMULACIÓN FINAL: HABLAR 2 MINUTOS SIN PARAR (10 min)', 'lines': [
                'Di: "Voy a ponerte un tema. Vas a hablar durante 2 minutos. No importa si cometes errores — lo importante es NO PARAR. Si no sabes una palabra, usa otra."',
                '<b>Tema:</b> "Tell me about your life. Your name, your age, where you live, what you do, what you can do, what you did yesterday, and what you want to do in the future."',
                'Pon temporizador. 2 minutos. Yeison habla. Tú escuchas y anotas errores EN SILENCIO.',
                'Después: dile los 3 errores más importantes. Modela la versión correcta. Yeison repite cada una 3 veces. <b>Segundo intento:</b> 2 minutos otra vez, mismo tema. ¿Menos pausas? ¿Menos errores?',
            ]},
            {'time': '01:52–02:00', 'title': 'CIERRE: REFLEXIÓN + RECOMENDACIÓN (8 min)', 'lines': [
                '<b>Lo que mejoró (2 min):</b> Di 3 cosas concretas: "Tu listening mejoró: Sesión 1 [X]/10, hoy [Y]/10." "Tu speaking mejoró: pudiste hablar [X] minutos sin parar." "Tu gramática: ya no dices [error] — ahora dices [correcto]."',
                '<b>Lo que necesita (2 min):</b> 2-3 cosas para seguir practicando: escuchar inglés todos los días, hablar en voz alta aunque sea solo, las frases con más errores.',
                '<b>Recomendación para coordinación (4 min):</b> Escribe en el reporte tu recomendación honesta: ¿Listo para A2? ¿Necesita más refuerzo? ¿Puede avanzar con seguimiento especial?',
            ]},
        ],
        S,
        special_note='<b>⚠ SESIÓN 2 DE 2 — REFUERZO PERSONALIZADO.</b> Hoy Yeison tiene que HABLAR y ESCRIBIR. Ya trabajó su oído en la Sesión 1. Revisa las observaciones de la Sesión 1 antes de empezar: ¿cuáles fueron sus errores más frecuentes? Enfócate en esos.',
        is_reinforcement=True
    )

    # REFUERZO YEISON — REPORTE SESIÓN 2
    build_report(
        os.path.join(D, 'A1', 'REFUERZO_Yeison_Sesion2_REPORTE.pdf'),
        'REFUERZO Yeison | Sesión 2 de 2',
        'Speaking + Writing + Listening refuerzo | Estudiante: Yeison',
        [
            ('Revisión tarea + Calentamiento', '8 min'),
            ('Speaking: Hablar sobre mí', '12 min'),
            ('Writing: Corregir errores comunes', '12 min'),
            ('Listening + Speaking: Conversación guiada', '12 min'),
            ('Speaking: Describe la imagen', '12 min'),
            ('Descanso + Escuchar audio', '12 min'),
            ('Writing: Escribir un párrafo', '12 min'),
            ('Speaking: Entrevista de trabajo', '12 min'),
            ('Listening final: Dictado completo', '10 min'),
            ('Simulación final: Hablar 2 min sin parar', '10 min'),
            ('Cierre + Recomendación', '8 min'),
        ],
        [
            'Papel de errores (entregado físico con la guía)',
            'Resultado comparativo dictado (Sesión 1 vs 2)',
            'Recomendación escrita para coordinación',
        ],
        [
            'Usé "No. Listen." + modelo (no expliqué reglas)',
            'Anoté errores frecuentes en papel',
            'Comparé resultados Sesión 1 vs Sesión 2',
            'Escribí recomendación honesta para coordinación',
        ],
        S
    )

    # ==============================================================
    # A1 CLASE 3 — REPORTE
    # ==============================================================
    build_report(
        os.path.join(D, 'A1', 'A1_Clase3_REPORTE.pdf'),
        'A1 | Clase 3 de 45',
        'Módulo 3: No, I Can\'t — Short Answers',
        [
            ('VATS: Prudencia', '5 min'),
            ('Analizo: Revisión de tarea', '10 min'),
            ('Libro: Módulo 3 — Short Answers', '20 min'),
            ('Ejercicios + Respuestas', '12 min'),
            ('Simulación: Interview rápida', '20 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Historia interactiva', '12 min'),
            ('Competencia por equipos', '10 min'),
            ('Construir + Nombrar', '3 min'),
            ('GoldList (20 frases)', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulo 3)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Prudencia)',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # ==============================================================
    # A2 CLASE 3 — REPORTE
    # ==============================================================
    build_report(
        os.path.join(D, 'A2', 'A2_Clase3_REPORTE.pdf'),
        'A2 | Clase 3 de 55',
        'Módulo 3: Days of the Month — Números Ordinales',
        [
            ('VATS: Templanza', '5 min'),
            ('Analizo: Revisión de tarea', '10 min'),
            ('Libro: Módulo 3 — Ordinal Numbers', '15 min'),
            ('Ejercicios + Respuestas', '12 min'),
            ('Simulación: Calendario de la clase', '20 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Historia: El pingüino que viajó por el mundo', '12 min'),
            ('Competencia: Carrera de fechas', '10 min'),
            ('Construir + Presentar', '3 min'),
            ('GoldList (20 frases)', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulo 3 A2)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Templanza)',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # A1 CLASE 4 — REPORTE
    build_report(
        os.path.join(D, 'A1', 'A1_Clase4_REPORTE.pdf'),
        'A1 | Clase 4 de 45',
        'Módulo 4: Where Should We Live? — Should + Recomendaciones',
        [
            ('VATS: Prudencia', '5 min'),
            ('Analizo: Revisión de tarea', '10 min'),
            ('Libro: Módulo 4 — Should + Where', '20 min'),
            ('Ejercicios + Respuestas', '12 min'),
            ('Simulación: ¿Dónde debería vivir?', '20 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Historia interactiva', '12 min'),
            ('Competencia por equipos', '10 min'),
            ('Construir + Nombrar', '3 min'),
            ('GoldList (20 frases)', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulo 4)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Prudencia)',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # A2 CLASE 4 — REPORTE
    build_report(
        os.path.join(D, 'A2', 'A2_Clase4_REPORTE.pdf'),
        'A2 | Clase 4 de 55',
        'Módulo 5: The Future in Triplicate — Las 3 Formas del Futuro',
        [
            ('VATS: Templanza', '5 min'),
            ('Analizo: Revisión de tarea', '10 min'),
            ('Libro: Módulo 5 — 3 Formas del Futuro', '20 min'),
            ('Ejercicios + Respuestas', '12 min'),
            ('Simulación: Mi fin de semana perfecto', '20 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Historia interactiva', '12 min'),
            ('Competencia por equipos', '10 min'),
            ('Construir + Presentar', '3 min'),
            ('GoldList (20 frases)', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulo 5 A2)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Templanza)',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # B2 CLASE 12 — REPORTE
    build_report(
        os.path.join(D, 'B2', 'B2_Clase12_REPORTE.pdf'),
        'B2 | Class 12 of 50',
        'Module 7: Relative Pronouns & Embedded Questions',
        [
            ('Icebreaker: I Know Something You Don\'t Know', '20 min'),
            ('Homework Review (GRABO Home + Self-Assessment)', '15 min'),
            ('Book: Guide 1 — Simple Relative Pronouns', '20 min'),
            ('Exercises: Relative Pronouns', '20 min'),
            ('Correct the Teacher: Story with 12 Errors', '20 min'),
            ('BREAK', '20 min'),
            ('Book: Guide 2 — Restrictive Relative Clauses', '20 min'),
            ('Shadowing 5 Steps', '20 min'),
            ('The Person Who Changed My Life', '35 min'),
            ('Writing: The Place Where I Feel Most Alive', '15 min'),
            ('Debate: The Thing That Matters Most', '15 min'),
            ('60-Second Challenge (Blending)', '10 min'),
            ('Self-check + Homework + Close', '10 min'),
        ],
        [
            'Error paper (photographed + sent to coordination)',
            'Self-check sheets completed',
            'Homework sent to WhatsApp group (exact copy)',
            'Social media content (if recorded)',
        ],
        [
            'Students spoke 80%+ of the time',
            'I spoke less than 20 min total',
            'I was a guide, not a lecturer',
            'I walked with error paper (min 5 errors written)',
            'My phone was face-down',
            'I recorded social media content',
            'I sent deliverables to coordination',
            'I sent homework to WhatsApp group',
        ],
        S
    )

    # A1 CLASE 5 — REPORTE
    build_report(
        os.path.join(D, 'A1', 'A1_Clase5_REPORTE.pdf'),
        'A1 | Clase 5 de 45',
        'Módulo 5: Numbers to 100 — Números, Horas y Precios',
        [
            ('VATS: Justicia', '5 min'),
            ('Analizo: Revisión de tarea', '8 min'),
            ('Libro: Módulo 5 — Numbers, Time, Prices', '15 min'),
            ('Ejercicios + Respuestas', '10 min'),
            ('Simulación: La Tienda de Heiiu', '20 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Historia interactiva', '10 min'),
            ('Competencia: Carrera de números', '10 min'),
            ('Juego: ¿Qué hora es?', '7 min'),
            ('GoldList (20 frases)', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulo 5)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Justicia)',
            'Libro y ejercicios NO se pasaron de tiempo',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # A2 CLASE 5 — REPORTE
    build_report(
        os.path.join(D, 'A2', 'A2_Clase5_REPORTE.pdf'),
        'A2 | Clase 5 de 55',
        'Módulo 6: Right on Time! — Scheduled Events',
        [
            ('VATS: Justicia', '5 min'),
            ('Analizo: Revisión de tarea', '8 min'),
            ('Libro: Módulo 6 — Scheduled Future Events', '15 min'),
            ('Ejercicios + Respuestas', '10 min'),
            ('Simulación: El Aeropuerto', '20 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Historia interactiva', '10 min'),
            ('Competencia: Carrera de horarios', '10 min'),
            ('Juego: Planifica el viaje', '7 min'),
            ('GoldList (20 frases)', '10 min'),
            ('Autochequeo', '3 min'),
            ('Tarea + Cierre', '2 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulo 6 A2)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Justicia)',
            'Libro y ejercicios NO se pasaron de tiempo',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    # B2 CLASES 13-16 — REPORTES
    b2_selfeval = [
        'Students spoke 80%+ of the time',
        'I spoke less than 20 min total',
        'I was a guide, not a lecturer',
        'I walked with error paper (min 5 errors written)',
        'My phone was face-down',
        'I recorded social media content',
        'I sent deliverables to coordination',
        'I sent homework to WhatsApp group',
    ]
    b2_deliverables = [
        'Error paper (photographed + sent to coordination)',
        'Self-check sheets completed',
        'Homework sent to WhatsApp group (exact copy)',
        'Social media content (if recorded)',
    ]

    build_report(
        os.path.join(D, 'B2', 'B2_Clase13_REPORTE.pdf'),
        'B2 | Class 13 of 50',
        'Module 8: Reported Speech — He Said, She Said',
        [
            ('Icebreaker: Telephone Game', '20 min'),
            ('Homework Review', '15 min'),
            ('Book: Guide 1 — Object Order', '15 min'),
            ('Book: Guide 2 — Say/Tell/Ask', '20 min'),
            ('Exercises', '15 min'),
            ('Correct the Teacher (12 errors)', '20 min'),
            ('BREAK', '20 min'),
            ('Book: Guide 3 — Tense Backshift', '20 min'),
            ('Shadowing 5 Steps', '20 min'),
            ('The Gossip Chain', '25 min'),
            ('Final Project Workshop', '20 min'),
            ('Self-check + Homework + Close', '10 min'),
        ],
        b2_deliverables, b2_selfeval, S
    )

    build_report(
        os.path.join(D, 'B2', 'B2_Clase14_REPORTE.pdf'),
        'B2 | Class 14 of 50',
        'Module 9: Perfect Tenses — Not So Simple, Anymore!',
        [
            ('Icebreaker: Never Have I Ever', '20 min'),
            ('Homework Review', '15 min'),
            ('Book: Guide 1 — Past vs Present Perfect', '20 min'),
            ('Exercises', '15 min'),
            ('Interview: Have You Ever...?', '15 min'),
            ('BREAK', '20 min'),
            ('Book: Guide 2 — Past Perfect', '20 min'),
            ('Book: Guide 3 — Future Perfect', '15 min'),
            ('Shadowing 5 Steps', '20 min'),
            ('Correct the Teacher (12 errors)', '20 min'),
            ('Timeline of My Life', '10 min'),
            ('Final Project Workshop', '20 min'),
            ('Self-check + Homework + Close', '10 min'),
        ],
        b2_deliverables, b2_selfeval, S
    )

    build_report(
        os.path.join(D, 'B2', 'B2_Clase15_REPORTE.pdf'),
        'B2 | Class 15 of 50',
        'Module 10: The Causative — The Devil Made Me Do It',
        [
            ('Icebreaker: Made Me Do It', '20 min'),
            ('Homework Review', '15 min'),
            ('Book: Guide 1 — Active Causative', '25 min'),
            ('Exercises', '15 min'),
            ('Production: The Boss', '30 min'),
            ('BREAK', '20 min'),
            ('Book: Guide 2 — Passive Causative', '20 min'),
            ('Shadowing 5 Steps', '20 min'),
            ('Correct the Teacher (12 errors)', '20 min'),
            ('Production: The Service Center', '15 min'),
            ('Final Project Workshop', '20 min'),
            ('Self-check + Homework + Close', '10 min'),
        ],
        b2_deliverables, b2_selfeval, S
    )

    build_report(
        os.path.join(D, 'B2', 'B2_Clase16_REPORTE.pdf'),
        'B2 | Class 16 of 50',
        'Blending Review: Modules 7-10 + GRABO Selfie #3',
        [
            ('Icebreaker: Module Roulette', '20 min'),
            ('Homework Review', '15 min'),
            ('Station Rotation (4 stations)', '40 min'),
            ('BREAK', '20 min'),
            ('GRABO Selfie #3 (eyes closed, 3 min)', '35 min'),
            ('Shadowing 5 Steps', '20 min'),
            ('Correct the Teacher: Mega Story (15 errors)', '25 min'),
            ('Debate: Technology', '15 min'),
            ('Final Project Workshop', '20 min'),
            ('Self-check + Homework + Close', '10 min'),
        ],
        b2_deliverables + ['GRABO Selfie #3 videos (all students, sent same day)'],
        b2_selfeval + ['GRABO Selfie #3 completed and sent to coordination'],
        S
    )

    # A1 & A2 CLASES 6-9 — REPORTES
    a1_modules = {
        6: ('Módulo 6: What Time Will You Eat Lunch? — Futuro con Will', 'Justicia',
            [('VATS: Justicia','5'),('Analizo: Revisión de tarea','8'),('Libro: Módulo 6 — Will','15'),('Ejercicios + Respuestas','10'),('Simulación','20'),('Shadowing 5 pasos','10'),('Historia interactiva','10'),('Competencia por equipos','10'),('Juego','7'),('GoldList (20 frases)','10'),('Autochequeo','3'),('Tarea + Cierre','2')]),
        7: ('Módulo 7: Where and What Time? — Lugares + Horas', 'Justicia',
            [('VATS: Justicia','5'),('Analizo: Revisión de tarea','8'),('Libro: Módulo 7 — Where + Time','15'),('Ejercicios + Respuestas','10'),('Simulación','20'),('Shadowing 5 pasos','10'),('Historia interactiva','10'),('Competencia por equipos','10'),('Juego','7'),('GoldList (20 frases)','10'),('Autochequeo','3'),('Tarea + Cierre','2')]),
        8: ('Módulo 8: Where Do We Eat? — Present Simple Do/Does', 'Fortaleza',
            [('VATS: Fortaleza','5'),('Analizo: Revisión de tarea','8'),('Libro: Módulo 8 — Do/Does','15'),('Ejercicios + Respuestas','10'),('Simulación','20'),('Shadowing 5 pasos','10'),('Historia interactiva','10'),('Competencia por equipos','10'),('Juego','7'),('GoldList (20 frases)','10'),('Autochequeo','3'),('Tarea + Cierre','2')]),
        9: ('Módulo 9: He Eats in the Restaurant — Affirmative Exception -s/-es', 'Fortaleza',
            [('VATS: Fortaleza','5'),('Analizo: Revisión de tarea','8'),('Libro: Módulo 9 — Verb-s','15'),('Ejercicios + Respuestas','10'),('Simulación','20'),('Shadowing 5 pasos','10'),('Historia interactiva','10'),('Competencia por equipos','10'),('Juego','7'),('GoldList (20 frases)','10'),('Autochequeo','3'),('Tarea + Cierre','2')]),
    }
    a2_modules = {
        6: ('Módulo 7: You Might Learn Something — Modal Might', 'Justicia',
            [('VATS: Justicia','5'),('Analizo: Revisión de tarea','8'),('Libro: Módulo 7 — Might','15'),('Ejercicios + Respuestas','10'),('Simulación','20'),('Shadowing 5 pasos','10'),('Historia interactiva','10'),('Competencia por equipos','10'),('Juego','7'),('GoldList (20 frases)','10'),('Autochequeo','3'),('Tarea + Cierre','2')]),
        7: ('Módulo 8: I Think that I\'m Learning! — Relative That', 'Justicia',
            [('VATS: Justicia','5'),('Analizo: Revisión de tarea','8'),('Libro: Módulo 8 — That','15'),('Ejercicios + Respuestas','10'),('Simulación','20'),('Shadowing 5 pasos','10'),('Historia interactiva','10'),('Competencia por equipos','10'),('Juego','7'),('GoldList (20 frases)','10'),('Autochequeo','3'),('Tarea + Cierre','2')]),
        8: ('Módulo 10: I\'ll Buy Lunch! — First Conditional', 'Fortaleza',
            [('VATS: Fortaleza','5'),('Analizo: Revisión de tarea','8'),('Libro: Módulo 10 — First Conditional','15'),('Ejercicios + Respuestas','10'),('Simulación','20'),('Shadowing 5 pasos','10'),('Historia interactiva','10'),('Competencia por equipos','10'),('Juego','7'),('GoldList (20 frases)','10'),('Autochequeo','3'),('Tarea + Cierre','2')]),
        9: ('Módulo 11: I\'d Eat a Cookie — Second Conditional', 'Fortaleza',
            [('VATS: Fortaleza','5'),('Analizo: Revisión de tarea','8'),('Libro: Módulo 11 — Second Conditional','15'),('Ejercicios + Respuestas','10'),('Simulación','20'),('Shadowing 5 pasos','10'),('Historia interactiva','10'),('Competencia por equipos','10'),('Juego','7'),('GoldList (20 frases)','10'),('Autochequeo','3'),('Tarea + Cierre','2')]),
    }
    std_deliverables = [
        'Hojas de autochequeo completadas',
        'Papel de errores (entregado físico con la guía)',
        'Tarea enviada al grupo de WhatsApp (copia exacta)',
        'Contenido para redes sociales (si se grabó)',
    ]
    for cls_num, (mod_title, virtue, acts) in a1_modules.items():
        build_report(
            os.path.join(D, 'A1', f'A1_Clase{cls_num}_REPORTE.pdf'),
            f'A1 | Clase {cls_num} de 45', mod_title,
            [(a, t+' min') for a, t in acts],
            std_deliverables,
            [f'Los estudiantes hablaron 80%+ del tiempo', 'Hablé menos de 20 min en total',
             'Fui guía, no conferencista', 'Caminé con papel de errores (mín 5 errores)',
             'Mi celular estaba boca abajo', f'Hice el ritual VATS ({virtue})',
             'Libro y ejercicios NO se pasaron de tiempo', 'Grabé contenido para redes sociales',
             'Envié entregables a coordinación', 'Envié la tarea al grupo de WhatsApp'],
            S)
    for cls_num, (mod_title, virtue, acts) in a2_modules.items():
        build_report(
            os.path.join(D, 'A2', f'A2_Clase{cls_num}_REPORTE.pdf'),
            f'A2 | Clase {cls_num} de 55', mod_title,
            [(a, t+' min') for a, t in acts],
            std_deliverables,
            [f'Los estudiantes hablaron 80%+ del tiempo', 'Hablé menos de 20 min en total',
             'Fui guía, no conferencista', 'Caminé con papel de errores (mín 5 errores)',
             'Mi celular estaba boca abajo', f'Hice el ritual VATS ({virtue})',
             'Libro y ejercicios NO se pasaron de tiempo', 'Grabé contenido para redes sociales',
             'Envié entregables a coordinación', 'Envié la tarea al grupo de WhatsApp'],
            S)

    # B2 CLASE 17 — REPORTE
    build_report(
        os.path.join(D, 'B2', 'B2_Clase17_REPORTE.pdf'),
        'B2 | Class 17 of 50',
        'Module 11: Advanced Adjectives — Noun-Adjective Pairs + Prefixes/Suffixes',
        [
            ('Icebreaker: Describe Without Naming', '20 min'),
            ('Homework Review', '15 min'),
            ('Book: Guide 1 — Noun-Adjective Pairs', '20 min'),
            ('Exercises', '15 min'),
            ('Production: The Character Creator', '25 min'),
            ('BREAK', '20 min'),
            ('Book: Guide 2 — Prefixes and Suffixes', '20 min'),
            ('Shadowing 5 Steps', '20 min'),
            ('Correct the Teacher (12 errors)', '20 min'),
            ('Debate: Intelligence vs Wisdom', '15 min'),
            ('Final Project Workshop', '20 min'),
            ('Self-check + Homework + Close', '10 min'),
        ],
        b2_deliverables,
        b2_selfeval,
        S
    )

    # B2 CLASE 18 — REPORTE
    build_report(
        os.path.join(D, 'B2', 'B2_Clase18_REPORTE.pdf'),
        'B2 | Class 18 of 50',
        'Module 12: Advanced Pronouns — Indefinite + Reflexive',
        [
            ('Icebreaker: Has Anyone Ever...?', '20 min'),
            ('Homework Review', '15 min'),
            ('Book: Guide 1 — Indefinite Pronouns', '20 min'),
            ('Exercises', '15 min'),
            ('Structured Conversation: The Mystery', '30 min'),
            ('BREAK', '20 min'),
            ('Correct the Teacher (12 errors)', '20 min'),
            ('Production: The Detective', '25 min'),
            ('Debate: Can anyone do anything?', '15 min'),
            ('Final Project Workshop', '20 min'),
            ('Reflexive Pronouns drill', '10 min'),
            ('Self-check + Homework + Close', '10 min'),
        ],
        b2_deliverables,
        b2_selfeval + ['Wrote 10+ errors on error paper'],
        S
    )

    # A2 4H CLASE 1 — REPORTE
    build_report(
        os.path.join(D, 'A2', 'A2_4h_Clase1_REPORTE.pdf'),
        'A2 INTENSIVO | Clase 1',
        'Módulo 1: Will + Días + Módulo 2: Meses + Años',
        [
            ('VATS: Templanza', '5 min'),
            ('Bienvenida A2 + Mi semana perfecta', '10 min'),
            ('Libro: Módulo 1 — Will + Días', '15 min'),
            ('Ejercicios Módulo 1', '10 min'),
            ('Simulación: Planifica semana compañero', '20 min'),
            ('Historia: Valentina', '10 min'),
            ('Shadowing 5 pasos', '10 min'),
            ('Competencia: Carrera de Will', '10 min'),
            ('GoldList #1 (20 frases)', '10 min'),
            ('Transición', '10 min'),
            ('BREAK', '20 min'),
            ('Bingo de cumpleaños', '10 min'),
            ('Libro: Módulo 2 — Meses + Años', '15 min'),
            ('Ejercicios Módulo 2', '10 min'),
            ('Línea de tiempo de mi vida', '15 min'),
            ('Historia: El año más extraño', '10 min'),
            ('Competencia: Carrera de fechas', '10 min'),
            ('GoldList #2 (20 frases)', '10 min'),
            ('Autochequeo (ambos módulos)', '5 min'),
            ('Tarea + Cierre', '5 min'),
        ],
        [
            'Hojas de autochequeo completadas (Módulos 1+2)',
            'Papel de errores (entregado físico con la guía)',
            'Tarea enviada al grupo de WhatsApp (copia exacta)',
            'Contenido para redes sociales (si se grabó)',
        ],
        [
            'Los estudiantes hablaron 80%+ del tiempo',
            'Hablé menos de 20 min en total',
            'Fui guía, no conferencista',
            'Caminé con papel de errores (mín 5 errores)',
            'Mi celular estaba boca abajo',
            'Hice el ritual VATS (Templanza)',
            'Libro y ejercicios NO se pasaron de tiempo',
            'Grabé contenido para redes sociales',
            'Envié entregables a coordinación',
            'Envié la tarea al grupo de WhatsApp',
        ],
        S
    )

    print("\nDone: 34 PDFs generated.")


if __name__ == '__main__':
    main()
