# -*- coding: utf-8 -*-
"""3 diapositivas para proyectar en el colegio despues de la clase en vivo.
Diseño: naranja del logo (#FF4A00), amarillo #FFC800, crema #FFF8E7; logo oficial sobre naranja; QR COL-01."""
import os, urllib.parse
import qrcode
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'NICHO_COLEGIOS')
LOGO = os.path.join(ROOT, 'recursos', 'marca heiiu', 'logo_heiiu_sobre_naranja.png')
NAR = RGBColor(0xFF, 0x4A, 0x00); NAR_OSC = RGBColor(0xE0, 0x42, 0x00); AMA = RGBColor(0xFF, 0xC8, 0x00)
CREMA = RGBColor(0xFF, 0xF8, 0xE7); BLANCO = RGBColor(0xFF, 0xFD, 0xF7); TINTA = RGBColor(0x2A, 0x1A, 0x12)
GRIS = RGBColor(0x5A, 0x46, 0x36); MELOCOTON = RGBColor(0xFF, 0xE9, 0xD6)
TIT = 'Arial Rounded MT Bold'; TXT = 'Arial'

TXT_WA = 'Hola, vengo de la visita de Heiiu a la UTS y quiero referir a un amigo para estudiar inglés. Código: REF-UTS'
QR = os.path.join(OUT, 'QR_REF-UTS.png')
qrcode.make('https://wa.me/573167688793?text=' + urllib.parse.quote(TXT_WA), box_size=14, border=1).save(QR)

prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BL = prs.slide_layouts[6]

def fondo(s, c):
    f = s.background.fill; f.solid(); f.fore_color.rgb = c

def forma(s, kind, x, y, w, h, color, radio=None):
    sh = s.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = color; sh.line.fill.background(); sh.shadow.inherit = False
    if radio is not None and kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = radio
    return sh

def texto(s, x, y, w, h, runs_por_parrafo, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, espacio=6):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame
    tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, runs in enumerate(runs_por_parrafo):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.alignment = align; p.space_after = Pt(espacio)
        for (t, size, bold, color, font) in runs:
            r = p.add_run(); r.text = t; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = font
    return tb

# ---------- 1. CORAJE ----------
s = prs.slides.add_slide(BL); fondo(s, NAR)
forma(s, MSO_SHAPE.RECTANGLE, 10.6, 0, 2.75, 7.5, RGBColor(0xFF, 0x6A, 0x2A))
forma(s, MSO_SHAPE.OVAL, 11.2, 5.4, 2.6, 2.6, AMA)
s.shapes.add_picture(LOGO, Inches(0.55), Inches(0.35), height=Inches(1.35))
texto(s, 0.85, 2.0, 9.2, 2.6, [[('Lo que acaban de hacer se llama ', 54, True, BLANCO, TIT), ('coraje.', 54, True, AMA, TIT)]])
texto(s, 0.85, 4.25, 9.5, 1.8, [
    [('Hablar en otro idioma frente a otros da miedo. Ustedes lo hicieron igual.', 22, False, BLANCO, TXT)],
    [('Eso no se aprende en un cuaderno: ', 22, True, BLANCO, TXT), ('se entrena.', 22, True, AMA, TXT)],
], espacio=10)
texto(s, 0.85, 6.65, 9.5, 0.5, [[('Salir de la zona de confort es el primer paso de todo lo que vale la pena.', 14, False, MELOCOTON, TXT)]])
s.notes_slide.notes_text_frame.text = 'Juan Diego cierra la clase con aplauso y pasa directo a esta. John la lee en voz alta, despacio, mirando a los estudiantes.'

# ---------- 2. MODULO DE GRADUACION ----------
s = prs.slides.add_slide(BL); fondo(s, CREMA)
texto(s, 0.85, 0.55, 8, 0.4, [[('TU PROYECTO EN INGLÉS', 14, True, NAR_OSC, TXT)]])
texto(s, 0.85, 0.95, 11.8, 0.9, [[('En el A2 eliges y construyes tu ', 32, True, TINTA, TIT), ('Módulo de Graduación.', 32, True, NAR_OSC, TIT)]])
cards = [
    ('Ruta Emprendedor', 'Sales con tu página web lista para publicar y tu primer mensaje de venta en inglés.', NAR),
    ('Ruta Pasaporte', 'Tu video de presentación, tu hoja de vida y carta en inglés, y tu entrevista ensayada.', AMA),
    ('En B2 lo pules', 'Networking, entrevistas, presentar una idea, negociación, pedir un aumento, tu pitch y un simulacro de jornada de trabajo.', NAR),
]
x = 0.85; w = 3.7; gap = 0.25
for i, (t, d, c) in enumerate(cards):
    cx = x + i * (w + gap)
    forma(s, MSO_SHAPE.ROUNDED_RECTANGLE, cx, 2.35, w, 2.75, BLANCO, 0.08)
    forma(s, MSO_SHAPE.RECTANGLE, cx + 0.25, 2.35, w - 0.5, 0.09, c)
    num = forma(s, MSO_SHAPE.OVAL, cx + 0.3, 2.65, 0.6, 0.6, c)
    tf = num.text_frame; tf.margin_left = tf.margin_right = 0; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = str(i + 1); r.font.size = Pt(20); r.font.bold = True; r.font.name = TIT
    r.font.color.rgb = NAR_OSC if c == AMA else BLANCO
    texto(s, cx + 0.3, 3.4, w - 0.6, 0.5, [[(t, 22, True, TINTA, TIT)]])
    texto(s, cx + 0.3, 3.95, w - 0.6, 1.1, [[(d, 15, False, GRIS, TXT)]])
forma(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, 5.35, 11.6, 1.0, NAR, 0.18)
texto(s, 1.2, 5.35, 11.0, 1.0, [[('¿No tienes un negocio ni un plan? No importa. ', 20, True, BLANCO, TXT), ('Lo que se entrena es atreverte a hacerlo.', 20, True, AMA, TXT)]], anchor=MSO_ANCHOR.MIDDLE)
texto(s, 0.85, 6.65, 11.6, 0.5, [[('Garantía por escrito: si cumples tu parte y no avanzas en inglés, te devolvemos el 100% del nivel.', 14, True, NAR_OSC, TXT)]])
s.notes_slide.notes_text_frame.text = ('En A2 el proyecto es una muestra; en B2 se pule. El módulo no es obligatorio: la academia lleva al estudiante a hacerlo, pero la decisión es suya. El mensaje es la exposición, no el negocio: quien no tiene idea hace la página de su perfil profesional o de un proyecto del colegio. '
    'Si preguntan qué es el Refuerzo PRO: se define con cada estudiante al llegar a B2. Nada de precios aquí: eso va en la cita con cada familia.')

# ---------- 3. PRIMER PASO ----------
s = prs.slides.add_slide(BL); fondo(s, NAR)
texto(s, 0.85, 0.7, 7.4, 1.6, [[('Trae a un amigo a estudiar ', 40, True, BLANCO, TIT), ('contigo.', 40, True, AMA, TIT)]])
pasos = ['Escanea el código', 'Cuéntanos a quién traes', 'Cuando se matricule, ganas $150.000']
for i, t in enumerate(pasos):
    y = 2.3 + i * 0.95
    c = forma(s, MSO_SHAPE.OVAL, 0.85, y, 0.68, 0.68, AMA)
    tf = c.text_frame; tf.margin_left = tf.margin_right = 0; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = str(i + 1); r.font.size = Pt(22); r.font.bold = True; r.font.name = TIT; r.font.color.rgb = NAR_OSC
    texto(s, 1.8, y, 6.2, 0.68, [[(t, 24, True, BLANCO, TXT)]], anchor=MSO_ANCHOR.MIDDLE)
texto(s, 0.85, 5.3, 7.0, 0.9, [
    [('Tu bono de $150.000 por cada amigo que se matricule.', 15, True, BLANCO, TXT)],
    [('Aplican términos del programa de referidos.', 13, False, MELOCOTON, TXT)],
], espacio=4)
forma(s, MSO_SHAPE.ROUNDED_RECTANGLE, 8.55, 1.0, 4.0, 4.75, BLANCO, 0.07)
s.shapes.add_picture(QR, Inches(8.85), Inches(1.3), width=Inches(3.4))
texto(s, 8.55, 4.95, 4.0, 0.5, [[('Código REF-UTS', 18, True, NAR_OSC, TIT)]], align=PP_ALIGN.CENTER)
s.shapes.add_picture(LOGO, Inches(0.55), Inches(6.35), height=Inches(0.85))
texto(s, 2.25, 6.6, 6, 0.4, [[('heiiu · english academy', 14, False, MELOCOTON, TXT)]])
s.notes_slide.notes_text_frame.text = 'Decir en voz alta: escaneen y envíen el mensaje tal como sale, sin borrarlo. El QR abre el WhatsApp de John con el mensaje de la UTS y el código REF-UTS. Dejar la diapositiva proyectada hasta que escaneen. El bono se paga cuando el amigo paga la inicial y asiste a la clase 5. Ningún dato del amigo se pide en el salón: el estudiante le avisa y el amigo escribe.'

path = os.path.join(OUT, os.environ.get('SLIDES_OUT', 'SLIDES_COLEGIO_3.pptx')); prs.save(path); print('OK', path, os.path.getsize(path))
