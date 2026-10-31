# -*- coding: utf-8 -*-
"""3 diapositivas para proyectar en el colegio despues de la clase en vivo (valores + video + cita)."""
import os, urllib.parse
import qrcode
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'NICHO_COLEGIOS')
LOGO = os.path.join(ROOT, 'recursos', 'marca heiiu', 'logo_heiiu_transparente.png')
NAR = RGBColor(0xE5, 0x4C, 0x09); CREMA = RGBColor(0xFF, 0xF8, 0xE7); NEGRO = RGBColor(0x22, 0x22, 0x22); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)

TXT_WA = 'Hola, vi la clase de Heiiu en mi colegio y quiero ver el video y agendar mi cita. Código de asesor: COL-01'
URL = 'https://wa.me/573167688793?text=' + urllib.parse.quote(TXT_WA)
QR = os.path.join(OUT, 'QR_COL-01.png')
qrcode.make(URL, box_size=12, border=2).save(QR)

prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

def fondo(s, color):
    f = s.background.fill; f.solid(); f.fore_color.rgb = color

def caja(s, x, y, w, h, textos, align=PP_ALIGN.LEFT):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    for i, (t, size, bold, color) in enumerate(textos):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(10)
        r = p.add_run(); r.text = t; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = 'Arial'
    return tb

def logo(s):
    if os.path.exists(LOGO):
        s.shapes.add_picture(LOGO, Inches(11.4), Inches(0.35), height=Inches(0.9))

# 1. Valores
s = prs.slides.add_slide(blank); fondo(s, NAR)
caja(s, 0.9, 1.6, 11.5, 4.5, [
    ('Lo que acaban de hacer se llama coraje.', 54, True, BLANCO),
    ('Hablar en otro idioma frente a otros da miedo. Ustedes lo hicieron igual.', 30, False, BLANCO),
    ('Eso no se aprende en un cuaderno: se entrena.', 30, True, BLANCO),
])
caja(s, 0.9, 6.3, 11.5, 0.8, [('Salir de la zona de confort es el primer paso de todo lo que vale la pena.', 20, False, CREMA)])

# 2. Como se entrena
s = prs.slides.add_slide(blank); fondo(s, CREMA); logo(s)
caja(s, 0.9, 0.6, 10, 1.2, [('Así se entrena en Heiiu', 44, True, NAR)])
caja(s, 0.9, 1.9, 11.6, 5, [
    ('•  Clases presenciales con escenas reales: entrevistas, clientes, viajes.', 26, False, NEGRO),
    ('•  Un video corto cada día: te ves avanzar.', 26, False, NEGRO),
    ('•  Valores además del idioma: coraje, disciplina, trabajo en equipo.', 26, False, NEGRO),
    ('•  Garantía por escrito: si cumples tu parte y no avanzas en inglés, te devolvemos el 100% del nivel.', 26, True, NAR),
])
caja(s, 0.9, 6.5, 11.6, 0.7, [('La única academia presencial de Bucaramanga con garantía de aprendizaje por escrito.', 18, False, NEGRO)])

# 3. Primer paso
s = prs.slides.add_slide(blank); fondo(s, BLANCO); logo(s)
caja(s, 0.9, 0.7, 7.3, 1.2, [('Da el primer paso hoy', 46, True, NAR)])
caja(s, 0.9, 2.0, 7.3, 4.5, [
    ('1.  Escanea el código.', 28, True, NEGRO),
    ('2.  Mira el video y conoce cómo se entrena.', 28, False, NEGRO),
    ('3.  Agenda tu cita con tu familia.', 28, False, NEGRO),
    ('Con el código de tu asesora puedes aplicar a una beca.', 20, True, NAR),
    ('Afiliados a Cajasan: condiciones especiales con carné o certificado vigente.', 18, False, NEGRO),
])
s.shapes.add_picture(QR, Inches(8.7), Inches(1.6), height=Inches(4.2))
caja(s, 8.5, 5.9, 4.6, 0.6, [('Código COL-01', 18, True, NAR)], PP_ALIGN.CENTER)
caja(s, 0.9, 6.7, 11.6, 0.6, [('Heiiu · Gerente de Alianzas · 316 768 8793', 18, False, NEGRO)])

pptx_path = os.path.join(OUT, 'SLIDES_COLEGIO_3.pptx')
prs.save(pptx_path)
print('OK', pptx_path, os.path.getsize(pptx_path))
