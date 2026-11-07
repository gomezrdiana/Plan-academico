# -*- coding: utf-8 -*-
"""Hojas de producto B2B por nicho y bloques (markdown con tablas -> PDF carta).
Uso: python generadores/comercial/gen_hoja_nicho_bloques.py  (renderiza las hojas listadas en HOJAS)
Soporta: '# ' titulo, '## ' seccion, '**...**' negrita, '- ' viñetas, tablas '| a | b |', parrafos."""
import os, re, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'NICHO_SALUD')
HOJAS = ['HOJA_SALUD_A1_3_BLOQUES', 'MAPA_SALUD_A1_3_BLOQUES_INTERNO']
NARANJA = colors.HexColor('#E54C09'); CREMA = colors.HexColor('#FFF8E7'); TINTA = colors.HexColor('#2A1A12')

st_h1 = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=NARANJA, spaceAfter=6)
st_h2 = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11.5, leading=15, textColor=TINTA, spaceBefore=7, spaceAfter=3)
st_p = ParagraphStyle('p', fontName='Helvetica', fontSize=9.6, leading=13.2, textColor=TINTA, spaceAfter=5)
st_cell = ParagraphStyle('c', fontName='Helvetica', fontSize=8.8, leading=11.6, textColor=TINTA)
st_cellb = ParagraphStyle('cb', parent=st_cell, fontName='Helvetica-Bold')

def inline(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'<i>\1</i>', t)
    return t

def build(md_path, pdf_path):
    lines = open(md_path, encoding='utf-8').read().splitlines()
    story = []; i = 0; bullets = []
    def flush_bullets():
        nonlocal bullets
        if bullets:
            story.append(ListFlowable([ListItem(Paragraph(inline(b), st_p), leftIndent=10) for b in bullets],
                                      bulletType='bullet', start='•', leftIndent=12, bulletFontSize=8))
            bullets = []
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            flush_bullets(); i += 1; continue
        if ln.startswith('# '):
            flush_bullets(); story.append(Paragraph(inline(ln[2:]), st_h1))
        elif ln.startswith('## '):
            flush_bullets(); story.append(Paragraph(inline(ln[3:]), st_h2))
        elif ln.startswith('- '):
            bullets.append(ln[2:])
        elif ln.startswith('|'):
            flush_bullets(); rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            ncol = max(len(r) for r in rows)
            data = [[Paragraph(inline(c), st_cellb if ri == 0 else st_cell) for c in r + [''] * (ncol - len(r))] for ri, r in enumerate(rows)]
            avail = letter[0] - 2 * 2.0 * cm
            # ancho proporcional al largo medio del texto por columna, con minimos
            lens = [max(12, sum(len(r[k]) for r in rows) / len(rows)) for k in range(ncol)]
            tot = sum(lens); widths = [max(3.0 * cm, avail * l / tot) for l in lens]
            s = sum(widths); widths = [w * avail / s for w in widths]
            t = Table(data, colWidths=widths, repeatRows=1)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), CREMA), ('LINEBELOW', (0, 0), (-1, 0), 0.8, NARANJA),
                ('GRID', (0, 1), (-1, -1), 0.3, colors.HexColor('#C9BFB3')), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
            story.append(t); story.append(Spacer(1, 5)); continue
        else:
            flush_bullets(); story.append(Paragraph(inline(ln), st_p))
        i += 1
    flush_bullets()
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=2.0 * cm, rightMargin=2.0 * cm, topMargin=1.5 * cm, bottomMargin=1.5 * cm,
                            title=os.path.basename(pdf_path)[:-4].replace('_', ' '), author='Heiiu English Academy')
    doc.build(story)
    print('OK', pdf_path, os.path.getsize(pdf_path))

if __name__ == '__main__':
    names = sys.argv[1:] or HOJAS
    for n in names:
        build(os.path.join(D, n + '.md'), os.path.join(D, n + '.pdf'))
