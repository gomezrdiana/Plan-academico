# -*- coding: utf-8 -*-
"""Carta de salida a LaHaus: PDF tipo carta de oficina (Helvetica 11, interlineado amplio, espacio entre parrafos).
Fuente: recursos/comercial/plataforma LaHaus/CARTA_SALIDA_LAHAUS_2026-11-03.md"""
import os, re, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, 'recursos', 'comercial', 'plataforma LaHaus')
MD = os.path.join(D, 'CARTA_SALIDA_LAHAUS_2026-11-03.md')
PDF = os.path.join(D, sys.argv[1] if len(sys.argv) > 1 else 'CARTA_SALIDA_LAHAUS_2026-11-03.pdf')

body = ParagraphStyle('b', fontName='Helvetica', fontSize=11, leading=17, spaceAfter=11, alignment=TA_JUSTIFY)
plain = ParagraphStyle('p', parent=body, alignment=0, spaceAfter=2)
item = ParagraphStyle('i', parent=body, spaceAfter=6)

def inline(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\*(.+?)\*', r'<i>\1</i>', t)
    return t

story = []
lines = open(MD, encoding='utf-8').read().splitlines()
i = 0
head = True
while i < len(lines):
    ln = lines[i].rstrip()
    if not ln:
        if head: story.append(Spacer(1, 8))
        i += 1; continue
    if ln.startswith('- ') or re.match(r'^\d+\. ', ln):
        items = []
        numbered = bool(re.match(r'^\d+\. ', ln))
        while i < len(lines) and (lines[i].startswith('- ') or re.match(r'^\d+\. ', lines[i])):
            txt = re.sub(r'^(- |\d+\. )', '', lines[i].rstrip())
            txt = txt.replace('**', '')  # sin negritas dentro de las listas: lectura de carta, no de informe
            items.append(ListItem(Paragraph(inline(txt), item), leftIndent=18))
            i += 1
        story.append(ListFlowable(items, bulletType='1' if numbered else 'bullet', start='1' if numbered else None, bulletFormat='%s.' if numbered else None,
                                  bulletFontName='Helvetica', bulletFontSize=11, leftIndent=18))
        story.append(Spacer(1, 4))
        continue
    if ln.startswith('Estimado'):
        head = False
    if ln.startswith('Cordialmente'):
        story.append(Paragraph(inline(ln), body)); story.append(Spacer(1, 40)); head = True; i += 1; continue
    story.append(Paragraph(inline(ln), plain if head else body))
    i += 1

doc = SimpleDocTemplate(PDF, pagesize=letter, leftMargin=2.6*cm, rightMargin=2.6*cm, topMargin=2.6*cm, bottomMargin=2.4*cm,
                        title='Carta Global Teacher S.A.S. a LaHaus', author='Global Teacher S.A.S.')
doc.build(story)
print('OK', PDF, os.path.getsize(PDF))
