#!/usr/bin/env python3
"""
Genera PDFs B&W (guias + reportes 1 hoja) desde los PRINT.md de:
- A1 Clase 15
- A2 4h Clases 6, 7, 8, 9, 10

Estrategia: lee el .md, lo convierte a PDF B&W usando reportlab.
Para los reportes, usa la estructura de checklist/observaciones especifica.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, PageBreak, KeepTogether)
from reportlab.pdfgen import canvas
import os, re

GRAY = HexColor('#555555')
LIGHT = HexColor('#e8e8e8')
DARKBOX = HexColor('#1a1a1a')
w, h = letter

styles = getSampleStyleSheet()
for n, fs, ld, f, c, sb, sa in [
    ('T1', 14, 17, 'Helvetica-Bold', black, 0, 3),
    ('Sub', 8, 10, 'Helvetica', GRAY, 0, 4),
    ('SH', 10, 12, 'Helvetica-Bold', black, 6, 2),
    ('AT', 9, 11, 'Helvetica-Bold', black, 5, 2),
    ('B', 8, 10.5, 'Helvetica', black, 0, 1.5),
    ('BB', 8, 10.5, 'Helvetica-Bold', black, 0, 1.5),
    ('BI', 7.5, 9.5, 'Helvetica-Oblique', GRAY, 0, 1),
    ('SM', 7, 9, 'Helvetica', GRAY, 0, 1),
    ('TC', 7.5, 9.5, 'Helvetica', black, 0, 0),
    ('TCB', 7.5, 9.5, 'Helvetica-Bold', black, 0, 0),
    ('TH', 7.5, 9.5, 'Helvetica-Bold', white, 0, 0),
    ('Box', 7.5, 9.5, 'Helvetica', black, 0, 1),
    ('Warn', 8, 10.5, 'Helvetica-Bold', black, 0, 1.5),
]:
    if n not in styles.byName:
        styles.add(ParagraphStyle(n, parent=styles['Normal'], fontSize=fs,
            leading=ld, fontName=f, textColor=c, spaceBefore=sb, spaceAfter=sa))

def box_bw(text, border_thick=1.0):
    t = Table([[Paragraph(text, styles['Box'])]], colWidths=[7.2 * inch])
    t.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), border_thick, black),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t

def gray_box(text, pad=4):
    t = Table([[Paragraph(text, styles['Box'])]], colWidths=[7.2 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT),
        ('BOX', (0, 0), (-1, -1), 0.5, black),
        ('TOPPADDING', (0, 0), (-1, -1), pad),
        ('BOTTOMPADDING', (0, 0), (-1, -1), pad),
        ('LEFTPADDING', (0, 0), (-1, -1), pad + 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), pad + 2),
    ]))
    return t

# ===========================================================================
# CONVERTIR MARKDOWN A PDF (estilo B&W)
# ===========================================================================
def md_to_pdf(md_path, pdf_path, max_lines_per_section=None, compact=False):
    """Convierte markdown a PDF B&W. Maneja headers, listas, codigo, etc.
    compact=True reduce márgenes, espaciados y interlineado para minimizar páginas."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if compact:
        doc = SimpleDocTemplate(pdf_path, pagesize=letter,
            topMargin=0.3*inch, bottomMargin=0.3*inch,
            leftMargin=0.45*inch, rightMargin=0.45*inch)
        # Aggressive style overrides for compact mode
        for stname, fs, ld, sb, sa in [
            ('SH', 9, 11, 2, 1),
            ('AT', 8.5, 10, 2, 1),
            ('B', 7.5, 9, 0, 0.3),
            ('BB', 7.5, 9, 0, 0.3),
            ('BI', 7, 8.5, 0, 0.3),
        ]:
            if stname in styles.byName:
                styles[stname].fontSize = fs
                styles[stname].leading = ld
                styles[stname].spaceBefore = sb
                styles[stname].spaceAfter = sa
    else:
        doc = SimpleDocTemplate(pdf_path, pagesize=letter,
            topMargin=0.4*inch, bottomMargin=0.4*inch,
            leftMargin=0.5*inch, rightMargin=0.5*inch)
        # Restore defaults
        for stname, fs, ld, sb, sa in [
            ('SH', 10, 12, 6, 2),
            ('AT', 9, 11, 5, 2),
            ('B', 8, 10.5, 0, 1.5),
            ('BB', 8, 10.5, 0, 1.5),
            ('BI', 7.5, 9.5, 0, 1),
        ]:
            if stname in styles.byName:
                styles[stname].fontSize = fs
                styles[stname].leading = ld
                styles[stname].spaceBefore = sb
                styles[stname].spaceAfter = sa
    s = []

    lines = content.split('\n')
    i = 0
    in_code_block = False
    code_lines = []

    while i < len(lines):
        line = lines[i]

        # Page break marker
        if line.strip() == '[PAGEBREAK]':
            s.append(PageBreak())
            i += 1
            continue

        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                # Close code block — chunk if too tall (reportlab fails over ~80 lines)
                CHUNK = 60
                font_sz = 6 if compact else 7
                for k in range(0, len(code_lines), CHUNK):
                    code_text = '\n'.join(code_lines[k:k+CHUNK])
                    code_text_html = code_text.replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>')
                    s.append(gray_box(f'<font face="Courier" size="{font_sz}">{code_text_html}</font>', pad=2 if compact else 4))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Skip empty lines but add small space
        if line.strip() == '':
            s.append(Spacer(1, 0.5 if compact else 2))
            i += 1
            continue

        # H1 (# at start)
        if line.startswith('# ') and not line.startswith('# ='):
            text = line[2:].strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            s.append(Paragraph(text, styles['SH']))
            i += 1
            continue

        # H3 (### at start)
        if line.startswith('### '):
            text = line[4:].strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            s.append(Paragraph(text, styles['AT']))
            i += 1
            continue

        # H2 (## at start)
        if line.startswith('## '):
            text = line[3:].strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            s.append(Paragraph(text, styles['SH']))
            i += 1
            continue

        # Title (=== separator means previous line is title)
        if line.strip().startswith('==='):
            i += 1
            continue

        # Horizontal rule
        if line.strip() == '---':
            s.append(HRFlowable(width="100%", thickness=0.5, color=black))
            s.append(Spacer(1, 1 if compact else 3))
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            text = line[2:].strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            s.append(Paragraph(f'<i>&gt; {text}</i>', styles['BI']))
            i += 1
            continue

        # List items
        if line.startswith('- ') or line.startswith('* '):
            text = line[2:].strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
            s.append(Paragraph(f'• {text}', styles['B']))
            i += 1
            continue

        # Numbered list
        if re.match(r'^\d+\.\s', line):
            text = line.strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
            s.append(Paragraph(text, styles['B']))
            i += 1
            continue

        # Plain paragraph
        text = line.strip()
        # Convert markdown to reportlab markup
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
        # Keep as-is, escape XML special chars carefully
        text = text.replace('&', '&amp;').replace('&amp;lt;', '&lt;').replace('&amp;gt;', '&gt;').replace('&amp;amp;', '&amp;')
        # But preserve our reportlab tags
        text = text.replace('&amp;lt;b&amp;gt;', '<b>').replace('&amp;lt;/b&amp;gt;', '</b>')
        text = text.replace('&amp;lt;i&amp;gt;', '<i>').replace('&amp;lt;/i&amp;gt;', '</i>')

        # Boxes for warning text
        if 'WARNING' in text or '⚠️' in text or 'NO NEGOCIABLE' in text or 'AUDITABLE' in text:
            s.append(box_bw(text, 1.0))
        else:
            s.append(Paragraph(text, styles['B']))
        i += 1

    doc.build(s)
    with open(pdf_path, 'rb') as f:
        pages = len(re.findall(rb'/Type\s*/Page[^s]', f.read()))
    print(f'OK: {pdf_path} - {pages} pag')


# ===========================================================================
# REPORTE 1 HOJA B&W (no editable, lineas en blanco)
# ===========================================================================
def build_report_1page(level, class_num, title, blocks, observations, output_path,
                       cycle_day=None, video_url=None):
    """Reporte 1 hoja B&W. Lineas en blanco. Checkboxes vacios.

    cycle_day: 1, 2, '3-Present', or None (sin shadowing hoy)
    video_url: URL del video del ciclo o None si Dia 3
    """
    c = canvas.Canvas(output_path, pagesize=letter)
    margin_l = 0.5 * inch
    margin_r = 0.5 * inch
    page_w = w - margin_l - margin_r
    y = h - 0.4 * inch

    # HEADER
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(margin_l, y, f'{level} - REPORTE CLASE {class_num}')
    y -= 11
    c.setFont('Helvetica-Bold', 8.5)
    c.drawString(margin_l, y, title[:90])
    y -= 10
    c.setFont('Helvetica-Oblique', 7)
    c.setFillColor(GRAY)
    c.drawString(margin_l, y, 'Confidencial - Imprimir y llenar a mano - Entregar a coordinacion al final de la clase')
    y -= 12

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
    y -= 12

    # SHADOWING CYCLE AUDIT (PROMINENTE - modelo de 3 dias)
    if cycle_day is not None:
        c.setFillColor(black)
        c.rect(margin_l, y - 3, page_w, 14, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont('Helvetica-Bold', 8)
        c.drawString(margin_l + 3, y, f'AUDITORIA CICLO SHADOWING - HOY ES DIA {cycle_day}')
        y -= 16
        c.setFillColor(black)
        c.setFont('Helvetica', 7.5)

        if cycle_day == 1:
            c.rect(margin_l + 4, y - 1, 8, 8, stroke=1, fill=0)
            c.drawString(margin_l + 16, y, 'Dia 1 del ciclo: 5 pasos completos con NUEVO video.')
            y -= 11
            c.drawString(margin_l + 16, y, 'Video usado:')
            c.line(margin_l + 70, y - 1, margin_l + page_w - 4, y - 1)
            y -= 11
        elif cycle_day == 2:
            c.rect(margin_l + 4, y - 1, 8, 8, stroke=1, fill=0)
            c.drawString(margin_l + 16, y, 'Dia 2 del ciclo: 5 pasos OTRA VEZ con MISMO video de ayer.')
            y -= 11
            c.drawString(margin_l + 16, y, 'Video confirmado igual al de Dia 1:')
            c.rect(margin_l + 175, y - 1, 8, 8, stroke=1, fill=0)
            c.drawString(margin_l + 187, y, 'Si')
            c.rect(margin_l + 210, y - 1, 8, 8, stroke=1, fill=0)
            c.drawString(margin_l + 222, y, 'No (cual?):')
            c.line(margin_l + 270, y - 1, margin_l + page_w - 4, y - 1)
            y -= 11
        elif str(cycle_day).startswith('3'):
            c.rect(margin_l + 4, y - 1, 8, 8, stroke=1, fill=0)
            c.drawString(margin_l + 16, y, 'Dia 3 del ciclo: PRESENTACION mini-competencia. NO video nuevo.')
            y -= 11
            c.drawString(margin_l + 16, y, '# de grupos que presentaron:')
            c.line(margin_l + 130, y - 1, margin_l + 180, y - 1)
            c.drawString(margin_l + 195, y, 'Ganadores:')
            c.line(margin_l + 245, y - 1, margin_l + page_w - 4, y - 1)
            y -= 11
        y -= 3

    # CHECKLIST DE BLOQUE
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'CHECKLIST DE BLOQUE - Marca lo que SI ocurrio')
    y -= 14

    c.setFillColor(black)
    c.setFont('Helvetica', 7.5)
    checklist = [
        'VATS al inicio (5-7 min) con virtud de la semana',
        'Todas actividades de la guia se completaron',
        'Ninguna actividad excedio 20 min',
        '80% estudiantes hablaron / 20% profesor',
        'Hubo cambios de formato (movimiento)',
        'Error paper fisico anonimo',
        'Tarea revisada (si aplica)',
        'GoldList: frases nuevas escritas + cuadernos recogidos',
        'Autochequeo / Exit ticket al cierre',
        'Errores del libro abordados segun guia',
    ]
    col_w = page_w / 2
    for i, item in enumerate(checklist):
        col = i % 2
        row = i // 2
        x_pos = margin_l + col * col_w + 4
        c.rect(x_pos, y - row * 10 - 1, 7, 7, stroke=1, fill=0)
        c.drawString(x_pos + 11, y - row * 10, item)
    y -= ((len(checklist) + 1) // 2) * 10 + 3

    # BLOQUES DE LA SESION
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'BLOQUES DE LA SESION - Marca cada uno realizado')
    y -= 14

    c.setFillColor(black)
    c.setFont('Helvetica', 6.5)
    for tiempo, titulo in blocks:
        c.rect(margin_l + 4, y - 1, 7, 7, stroke=1, fill=0)
        c.setFont('Helvetica-Bold', 6.5)
        c.drawString(margin_l + 15, y, tiempo)
        c.setFont('Helvetica', 6.5)
        c.drawString(margin_l + 65, y, titulo[:80])
        y -= 9
    y -= 3

    # OBSERVACIONES
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'OBSERVACIONES CLAVE - Llenar al final')
    y -= 13

    c.setFillColor(black)
    for title, prompt in observations:
        c.setFont('Helvetica-Bold', 7)
        c.drawString(margin_l + 2, y, title + ':')
        if prompt:
            c.setFont('Helvetica-Oblique', 6)
            c.setFillColor(GRAY)
            c.drawString(margin_l + 2 + c.stringWidth(title + ':', 'Helvetica-Bold', 7) + 3, y, prompt)
            c.setFillColor(black)
        y -= 8
        for _ in range(2):
            c.line(margin_l + 4, y, margin_l + page_w - 4, y)
            y -= 9
        y -= 1

    # ESTUDIANTE EN RIESGO
    c.setFillColor(DARKBOX)
    c.rect(margin_l, y - 2, page_w, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(margin_l + 4, y + 1, 'ESTUDIANTE EN RIESGO HOY (solo si aplica)')
    y -= 13

    c.setFillColor(black)
    c.setFont('Helvetica', 7)
    c.drawString(margin_l + 2, y, 'Nombre:')
    c.line(margin_l + 40, y - 1, margin_l + 220, y - 1)
    c.drawString(margin_l + 230, y, 'Razon (vacio = sin riesgo):')
    c.line(margin_l + 350, y - 1, margin_l + page_w - 4, y - 1)
    y -= 11
    c.drawString(margin_l + 2, y, 'Accion sugerida:')
    c.line(margin_l + 80, y - 1, margin_l + page_w - 4, y - 1)
    y -= 11

    # AUSENCIAS / TAREA
    y -= 1
    c.setFont('Helvetica-Bold', 7)
    c.drawString(margin_l + 2, y, 'Ausentes:')
    c.line(margin_l + 50, y - 1, margin_l + page_w - 4, y - 1)
    y -= 10

    c.drawString(margin_l + 2, y, 'No hicieron tarea:')
    c.line(margin_l + 90, y - 1, margin_l + page_w - 4, y - 1)
    y -= 10

    c.drawString(margin_l + 2, y, 'Errores nuevos del libro encontrados:')
    c.line(margin_l + 175, y - 1, margin_l + page_w - 4, y - 1)
    y -= 12

    # FIRMA
    c.setFont('Helvetica', 7)
    c.drawString(margin_l + 2, y, 'Firma profesor:')
    c.line(margin_l + 75, y - 1, margin_l + 280, y - 1)
    c.drawString(margin_l + 295, y, 'Recibido coordinacion:')
    c.line(margin_l + 400, y - 1, margin_l + page_w - 4, y - 1)

    c.save()
    with open(output_path, 'rb') as f:
        pages = len(re.findall(rb'/Type\s*/Page[^s]', f.read()))
    print(f'OK: {output_path} - {pages} pag')


# ===========================================================================
# CONFIGURACION DE CADA CLASE
# ===========================================================================

# A1 Clase 15
a1_c15_blocks = [
    ('00:00-00:05', 'VATS Justicia'),
    ('00:05-00:13', 'Analizo: Revision de tarea'),
    ('00:13-00:28', 'Libro: Modulo 15 Possessive Adjectives'),
    ('00:28-00:40', 'Ejercicios + Respuestas'),
    ('00:40-01:00', 'Simulacion Meet My Family'),
    ('01:00-01:10', 'Shadowing 5 pasos'),
    ('01:10-01:20', 'Historia Interactiva'),
    ('01:20-01:30', 'Competencia por equipos'),
    ('01:30-01:38', 'Juego Whose Is This?'),
    ('01:38-01:48', 'GoldList 5 frases'),
    ('01:48-01:51', 'Autochequeo'),
    ('01:51-01:53', 'Tarea + Cierre'),
]
a1_c15_obs = [
    ('Modulo 15 - los estudiantes dominaron my/your/his/her/its/our/their?',
     'Mayoria si / mayoria no / mitad. Quien fallo el ITS?'),
    ('Errores recurrentes', 'Ej: my\'s, I house, she father'),
    ('Estado de la clase con virtud JUSTICIA',
     'Conexion con familia se sintio? Apertura emocional?'),
    ('Que ajustar en la proxima clase', 'Recomendacion concreta'),
]

# A2 4h Clase 6
a2_c6_blocks = [
    ('8:00-8:05', 'VATS Fortaleza dia 2'),
    ('8:05-8:15', 'Rompehielo What have you already done'),
    ('8:15-8:30', 'Libro Modulo 13 Already/Still/Until'),
    ('8:30-8:42', 'Ejercicios + Respuestas'),
    ('8:42-9:02', 'Simulacion The Impatient Mother'),
    ('9:02-9:12', 'Shadowing 5 pasos #1'),
    ('9:12-9:22', 'Historia Interactiva'),
    ('9:22-9:32', 'Competencia por equipos'),
    ('9:32-9:42', 'Juego Already or Still?'),
    ('9:42-9:52', 'GoldList 5 frases'),
    ('9:52-9:57', 'Autochequeo primera mitad'),
    ('10:00-10:20', 'BREAK'),
    ('10:20-10:25', 'VATS Reconnect'),
    ('10:25-10:35', 'Intro While I was'),
    ('10:35-10:50', 'Libro Modulo 14 While/During/Again'),
    ('10:50-11:00', 'Ejercicios + Respuestas'),
    ('11:00-11:20', 'Simulacion Multitasking Day'),
    ('11:20-11:30', 'Shadowing 5 pasos #2'),
    ('11:30-11:40', 'Historia Interactiva'),
    ('11:40-11:48', 'Competencia equipos M13+M14'),
    ('11:48-11:53', 'GoldList 5 frases mas'),
    ('11:53-11:57', 'Autochequeo + Error Paper'),
    ('11:57-12:00', 'Tarea + Cierre'),
]
a2_c6_obs = [
    ('Modulos 13 y 14 - dominaron Already/Still/Until y While/During/Again?',
     'Mayoria si / mayoria no'),
    ('Errores recurrentes', 'Tipico: while/during confusion, already mal posicionado'),
    ('Simulaciones - como salieron?', 'The Impatient Mother + Multitasking Day'),
    ('Errores del libro encontrados nuevos', ''),
]

# A2 4h Clase 7
a2_c7_blocks = [
    ('8:00-8:05', 'VATS Prudencia dia 1'),
    ('8:05-8:13', 'Analizo Revision tarea'),
    ('8:13-8:23', 'Rompehielo Have You Ever?'),
    ('8:23-8:38', 'Libro Modulo 15 Present Perfect Regular'),
    ('8:38-8:50', 'Ejercicios + Respuestas'),
    ('8:50-9:10', 'Simulacion Job Interview'),
    ('9:10-9:20', 'Shadowing 5 pasos #1'),
    ('9:20-9:30', 'Historia Interactiva'),
    ('9:30-9:40', 'Competencia equipos'),
    ('9:40-9:48', 'GoldList 5 frases'),
    ('9:48-9:55', 'Autochequeo'),
    ('10:00-10:20', 'BREAK'),
    ('10:20-10:25', 'Reconnect virtud'),
    ('10:25-10:35', 'Intro I have gone to'),
    ('10:35-10:50', 'Libro Modulo 16 Present Perfect Irregular'),
    ('10:50-11:00', 'Ejercicios + Respuestas'),
    ('11:00-11:20', 'Simulacion Bucket List Interview'),
    ('11:20-11:30', 'Shadowing 5 pasos #2'),
    ('11:30-11:40', 'Juego Two Truths Life Edition'),
    ('11:40-11:50', 'GoldList 5 frases mas'),
    ('11:50-11:55', 'Autochequeo + Error Paper'),
    ('11:55-12:00', 'Tarea + Cierre'),
]
a2_c7_obs = [
    ('Present Perfect - dominaron have/has + participio?',
     'Mayoria si / mayoria no. Errores tipicos'),
    ('Verbos irregulares - cuales son los mas dificiles?',
     'gone, eaten, taken, been, done, seen'),
    ('Job Interview simulation - quien se destaco hablando?',
     'Soft skill: Entrevistas'),
    ('Errores del libro encontrados', 'Modulo 15 pag 138 already mencionado en guia'),
]

# A2 4h Clase 8
a2_c8_blocks = [
    ('8:00-8:05', 'VATS Prudencia dia 2'),
    ('8:05-8:13', 'Analizo Revision tarea'),
    ('8:13-8:23', 'Rompehielo Did You or Have You'),
    ('8:23-8:38', 'Libro Modulo 17 Past vs Perfect'),
    ('8:38-8:50', 'Ejercicios + Respuestas'),
    ('8:50-9:10', 'Simulacion Time Traveler Interview'),
    ('9:10-9:20', 'Shadowing 5 pasos #1'),
    ('9:20-9:30', 'Historia Interactiva'),
    ('9:30-9:40', 'Competencia equipos'),
    ('9:40-9:48', 'GoldList 5 frases'),
    ('9:48-9:55', 'Autochequeo'),
    ('10:00-10:20', 'BREAK'),
    ('10:20-10:25', 'Reconnect'),
    ('10:25-10:35', 'Intro What is done in'),
    ('10:35-10:50', 'Libro Modulo 18 Passive Voice'),
    ('10:50-11:00', 'Ejercicios + Respuestas'),
    ('11:00-11:20', 'Simulacion Breaking News Reporter'),
    ('11:20-11:30', 'Shadowing 5 pasos #2'),
    ('11:30-11:40', 'Historia Interactiva'),
    ('11:40-11:48', 'Juego Who Dunnit'),
    ('11:48-11:55', 'GoldList 5 frases mas'),
    ('11:55-11:58', 'Autochequeo + Error Paper'),
    ('11:58-12:00', 'Tarea + Cierre'),
]
a2_c8_obs = [
    ('Past Simple vs Present Perfect - distinguen periodo cerrado vs abierto?',
     'Mayoria si / mayoria no'),
    ('Voz Pasiva - dominaron to be + participio?',
     'Errores tipicos: olvidar to be, mal participio'),
    ('Breaking News simulation - quien se destaco?',
     'Soft skill: Public Speaking + Pitch'),
    ('Errores del libro encontrados', 'Mod 17 pag 165 + Mod 18 pag 173 mencionados en guia'),
]

# A2 4h Clase 9
a2_c9_blocks = [
    ('8:00-8:05', 'VATS Templanza dia 1'),
    ('8:05-8:13', 'Analizo Revision tarea'),
    ('8:13-8:23', 'Rompehielo What is your favorite'),
    ('8:23-8:38', 'Libro Modulo 20 Gerunds as Subjects'),
    ('8:38-8:48', 'Ejercicios + Respuestas'),
    ('8:48-9:08', 'Simulacion Pros and Cons Debate'),
    ('9:08-9:18', 'Shadowing 5 pasos #1'),
    ('9:18-9:28', 'Historia Interactiva'),
    ('9:28-9:38', 'Competencia equipos'),
    ('9:38-9:48', 'GoldList 5 frases'),
    ('9:48-9:55', 'Autochequeo'),
    ('10:00-10:20', 'BREAK'),
    ('10:20-10:25', 'Reconnect'),
    ('10:25-10:35', 'Intro After/Before/Without'),
    ('10:35-10:50', 'Libro Modulo 21 Gerunds after Prep'),
    ('10:50-11:00', 'Ejercicios + Respuestas'),
    ('11:00-11:20', 'Simulacion Daily Routine Balance'),
    ('11:20-11:30', 'Shadowing 5 pasos #2'),
    ('11:30-11:40', 'Historia Interactiva'),
    ('11:40-11:48', 'Juego Finish My Sentence'),
    ('11:48-11:55', 'GoldList 5 frases mas'),
    ('11:55-11:58', 'Autochequeo + Error Paper'),
    ('11:58-12:00', 'Tarea + Cierre'),
]
a2_c9_obs = [
    ('Gerundios como sujeto - dominaron?',
     'Reading is fun, etc'),
    ('Gerundios despues de prep - dominaron?',
     'Error tipico A2-B1: before to eat -> debe ser before eating'),
    ('Pros and Cons Debate - participacion?',
     'Soft skill: Debate'),
    ('Errores del libro encontrados', ''),
]

# A2 4h Clase 10 (v2 - sin shadowing por excepcion logistica)
a2_c10_blocks = [
    ('8:00-8:05', 'VATS Templanza dia 2'),
    ('8:05-8:13', 'Analizo Revision tarea'),
    ('8:13-8:23', 'Rompehielo Love-ing vs Want to'),
    ('8:23-8:38', 'Libro Modulo 22 Gerunds Double Verbs'),
    ('8:38-8:50', 'Ejercicios + Respuestas Mod 22'),
    ('8:50-9:12', 'Simulacion Mi Proximo Proyecto (gerundios + infinitivos)'),
    ('9:12-9:30', 'Historia Interactiva absurda Mod 22'),
    ('9:30-9:40', 'Competencia equipos Mod 22'),
    ('9:40-9:52', 'GoldList 20 frases'),
    ('9:52-9:57', 'Autochequeo'),
    ('9:57-10:00', 'Transicion'),
    ('10:00-10:20', 'BREAK'),
    ('10:20-10:25', 'Reconnect virtud'),
    ('10:25-10:35', 'Intro Phrasal verbs'),
    ('10:35-10:50', 'Libro Modulo 23 Phrasal Verbs'),
    ('10:50-11:00', 'Ejercicios + Respuestas Mod 23'),
    ('11:00-11:20', 'Simulacion Customer Service Call'),
    ('11:20-11:36', 'Historia Interactiva absurda Mod 23'),
    ('11:36-11:44', 'Juego Phrasal Verb Roulette'),
    ('11:44-11:54', 'Free Production conversacion Mod 23'),
    ('11:54-11:57', 'Autochequeo + Error Paper colectivo'),
    ('11:57-12:00', 'Tarea + Cierre'),
]
a2_c10_obs = [
    ('Gerundio vs infinitivo - dominaron love/want/enjoy/decide/etc?',
     'Mayoria si / mayoria no. Errores tipicos: I want learning / I love to swim'),
    ('10 phrasal verbs basicos - dominio?',
     'Cuales fueron los mas dificiles. Cita ejemplos'),
    ('3 errores LITERALES con NOMBRE de estudiante',
     'OBLIGATORIO. Ej: Vero dijo "I want learning piano"'),
    ('Customer Service Call - quien destaco / quien lo evito?',
     'Soft skill: Atencion al cliente telefonica'),
    ('Errores nuevos encontrados en el libro (errata)',
     'Solo si encontro typo o numeracion mala'),
]

# ===========================================================================
# EJECUCION
# ===========================================================================
if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))

    # PROTOCOLO PDF
    md_to_pdf(os.path.join(base, 'PROTOCOLO_PROFESOR_HEIIU.md'),
              os.path.join(base, 'PROTOCOLO_PROFESOR_HEIIU.pdf'))

    # INVENTARIO COORDINACION
    md_to_pdf(os.path.join(base, 'INVENTARIO_COORDINACION.md'),
              os.path.join(base, 'INVENTARIO_COORDINACION.pdf'))

    # CALENDARIO VIRTUDES
    md_to_pdf(os.path.join(base, 'CALENDARIO_VIRTUDES_2026.md'),
              os.path.join(base, 'CALENDARIO_VIRTUDES_2026.pdf'))

    # GUIAS PDF B&W (desde markdown)
    md_to_pdf(os.path.join(base, 'A1', 'A1_Class15_PRINT.md'),
              os.path.join(base, 'A1', 'A1_Clase15_GUIA.pdf'))
    md_to_pdf(os.path.join(base, 'A2', 'A2_4h_Class6_PRINT.md'),
              os.path.join(base, 'A2', 'A2_4h_Clase6_GUIA.pdf'))
    md_to_pdf(os.path.join(base, 'A2', 'A2_4h_Class7_PRINT.md'),
              os.path.join(base, 'A2', 'A2_4h_Clase7_GUIA.pdf'))
    md_to_pdf(os.path.join(base, 'A2', 'A2_4h_Class8_PRINT.md'),
              os.path.join(base, 'A2', 'A2_4h_Clase8_GUIA.pdf'))
    md_to_pdf(os.path.join(base, 'A2', 'A2_4h_Class9_PRINT.md'),
              os.path.join(base, 'A2', 'A2_4h_Clase9_GUIA.pdf'))
    md_to_pdf(os.path.join(base, 'A2', 'A2_4h_Class10_PRINT.md'),
              os.path.join(base, 'A2', 'A2_4h_Clase10_GUIA.pdf'))

    # REPORTES 1 HOJA B&W
    # A1 Clase 15 = Dia 1 del ciclo (Beauty and the Beast)
    build_report_1page('A1', 15,
                       'Modulo 15 Possessive Adjectives - Justicia',
                       a1_c15_blocks, a1_c15_obs,
                       os.path.join(base, 'A1', 'A1_Clase15_REPORTE.pdf'),
                       cycle_day=1)

    # A2 4h Clases - mapeadas al ciclo
    cycle_map = {
        6: 1,           # Lu Dia 1: Friends
        7: 2,           # Ma Dia 2: Friends
        8: '3-Present', # Mi Dia 3: Presentacion Friends
        9: 1,           # Ju Dia 1: NUEVO video (coordinacion provee)
        10: None,       # Lu (post-festivo): SIN shadowing por excepcion logistica
    }
    for class_num, blocks, obs, modules in [
        (6, a2_c6_blocks, a2_c6_obs, 'Mod 13 Already/Still/Until + Mod 14 While/During/Again - Fortaleza dia 2'),
        (7, a2_c7_blocks, a2_c7_obs, 'Mod 15 Present Perfect Reg + Mod 16 Irreg - Prudencia dia 1'),
        (8, a2_c8_blocks, a2_c8_obs, 'Mod 17 Past vs Perfect + Mod 18 Voz Pasiva - Prudencia dia 2'),
        (9, a2_c9_blocks, a2_c9_obs, 'Mod 20 Gerunds Subj + Mod 21 Gerunds Prep - Templanza dia 1'),
        (10, a2_c10_blocks, a2_c10_obs, 'Mod 22 Double Verbs + Mod 23 Phrasal Verbs - Templanza dia 2'),
    ]:
        build_report_1page('A2 INTENSIVO 4H', class_num, modules, blocks, obs,
                           os.path.join(base, 'A2', f'A2_4h_Clase{class_num}_REPORTE.pdf'),
                           cycle_day=cycle_map[class_num])

    print('\nTodos los PDFs generados.')
