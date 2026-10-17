# -*- coding: utf-8 -*-
"""Modelo de CARTA DE POSTULACIÓN que la empresa aliada (Convenio Heiiu Business Partner) emite por cada colaborador
para que acceda a la beca de alianza. Una página, en papel de la empresa. Salida: recursos/comercial/B2B/CARTA_POSTULACION_EMPRESA_ALIADA.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
GRIS = RGBColor(0x66, 0x66, 0x66)
d = Document()
for s in d.sections:
    s.top_margin = Cm(2); s.bottom_margin = Cm(2); s.left_margin = Cm(2.5); s.right_margin = Cm(2.5)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(11)
def t(txt, after=8, bold=False, size=11, align=None, color=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align: p.alignment = align
    r = p.add_run(txt); r.bold = bold; r.font.size = Pt(size)
    if color: r.font.color.rgb = color
    return p
t('[Papel membretado de la empresa]', after=14, size=9, color=GRIS)
t('CARTA DE POSTULACIÓN — ALIANZA HEIIU BUSINESS PARTNER', bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, after=14)
t('Bucaramanga, ____ de ____________ de 2026', after=12)
t('Señores\nHeiiu English Academy — Global Teacher S.A.S.\nBucaramanga', after=12)
t('La empresa ______________________________________, NIT ____________________, en el marco del Convenio Heiiu Business Partner suscrito el ____ / ____ / 2026, postula a:', after=8)
t('Nombre completo: ______________________________________________\nCédula: ______________________   Cargo: ______________________________\nCelular: ______________________   Correo: ______________________________', after=10)
t('para que acceda, como colaborador de nuestra empresa, al beneficio de la alianza: la beca del Fondo de Becas de la academia en la columna de alianza, aplicable al programa que el colaborador elija.', after=8)
t('Esta postulación no genera obligación económica ni responsabilidad alguna para la empresa. El contrato de matrícula, sus condiciones académicas y de pago los asume directamente el colaborador. La empresa autoriza a la academia a reportarle únicamente asistencia y cumplimiento del colaborador, nunca calificaciones.', after=16)
t('Atentamente,', after=30)
t('_________________________________\nNombre: ______________________________\nCargo (contacto designado de talento humano): ______________________\nTeléfono / correo: ______________________________', after=16)
t('Uso interno de la academia: esta carta se entrega en la sede junto con el contrato de matrícula del colaborador. Una carta por colaborador. Sin carta vigente no aplica la beca de alianza.', size=9, color=GRIS, after=0)
out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\B2B\CARTA_POSTULACION_EMPRESA_ALIADA.docx'
d.save(out); print('OK', out)
