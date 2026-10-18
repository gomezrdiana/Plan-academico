# -*- coding: utf-8 -*-
"""Orden de examen médico ocupacional de ingreso (Res. 2346/2007). Formato por rol con espacios en blanco; gerencia lo llena
y firma. Salida (git): recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/ORDEN_EXAMEN_MEDICO_INGRESO.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
d = Document()
for s in d.sections:
    s.top_margin = Cm(2); s.bottom_margin = Cm(2); s.left_margin = Cm(2.5); s.right_margin = Cm(2.5)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(11)
def t(txt, after=8, bold=False, size=11, align=None, color=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align: p.alignment = align
    r = p.add_run(txt); r.bold = bold; r.font.size = Pt(size)
    if color: r.font.color.rgb = color
t('GLOBAL TEACHER S.A.S. — Heiiu English Academy', bold=True, size=12, color=NAR, after=0)
t('NIT 900.422.478-2 · Bucaramanga', size=10, color=GRIS, after=14)
t('ORDEN DE EXAMEN MÉDICO OCUPACIONAL DE INGRESO', bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, after=14)
t('Bucaramanga, ____ de ____________ de 2026', after=12)
t('Señores\nIPS de Salud Ocupacional: ______________________________________', after=12)
t('De acuerdo con la Resolución 2346 de 2007, solicitamos practicar examen médico ocupacional de ingreso a:', after=8)
t('Nombre completo: ______________________________________________\nCédula: ______________________\nCargo a desempeñar: Gerente de Alianzas Empresariales\nFecha prevista de ingreso: ____ / ____ / 2026', after=10)
t('Descripción del cargo: labor comercial de relacionamiento con empresas; trabajo de oficina (computador, teléfono) y visitas a empresas en el área metropolitana con desplazamientos urbanos; no manipula cargas ni maquinaria. Riesgo laboral clase I.', after=8)
t('Exámenes solicitados: examen médico ocupacional de ingreso con énfasis osteomuscular y los paraclínicos que la IPS considere pertinentes para el cargo. El concepto de aptitud se remite a la empresa; la historia clínica queda en custodia de la IPS conforme a la ley.', after=8)
t('El costo del examen lo asume la empresa. Favor facturar a Global Teacher S.A.S., NIT 900.422.478-2.', after=24)
t('Atentamente,', after=30)
t('_________________________________\nDiana Marcela Gómez Rangel\nGerente · Global Teacher S.A.S.', after=0)
out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\ORDEN_EXAMEN_MEDICO_INGRESO.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
