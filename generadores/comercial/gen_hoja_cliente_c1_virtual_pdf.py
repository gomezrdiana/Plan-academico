# -*- coding: utf-8 -*-
"""Hoja para el CLIENTE 'Dos cosas que te van a decir en todas partes' (C1 y virtual), mismo diseño de la hoja
'Dos caminos' (reportlab, logo, colores de marca). Una página carta. Sin nombres de otras academias, sin precios.
Salida: recursos/comercial/INDUCCION_COMERCIAL/HOJA_CLIENTE_C1_Y_VIRTUAL.pdf"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.utils import ImageReader

R = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
LOGO = R + r'\recursos\marca heiiu\logo_heiiu_sobre_naranja.png'
OUT = R + r'\recursos\comercial\INDUCCION_COMERCIAL\HOJA_CLIENTE_C1_Y_VIRTUAL.pdf'

NAR = HexColor('#FF4A00'); NAR2 = HexColor('#E54C09'); AMA = HexColor('#FBC900'); CREMA = HexColor('#FFF8E7')
GRIS = HexColor('#5A5A5A'); NEGRO = HexColor('#222222'); LINEA = HexColor('#F0D9C8')

W, H = letter
try:
    open(OUT, 'ab').close()
except PermissionError:
    OUT = OUT.replace('.pdf', '_v2.pdf'); print('ABIERTO -> _v2')
c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle('Heiiu — Dos cosas que te van a decir en todas partes')

def P(text, size=9.2, color=NEGRO, bold=False, align=TA_LEFT, leading=None):
    st = ParagraphStyle('p', fontName='Helvetica-Bold' if bold else 'Helvetica', fontSize=size,
                        leading=leading or size * 1.28, textColor=color, alignment=align)
    return Paragraph(text, st)
def flow(items, x, y, w, h):
    Frame(x, y, w, h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, showBoundary=0).addFromList(list(items), c)
def rbox(x, y, w, h, fill, stroke=None, r=10, lw=1):
    c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)
def check(x, y, color=NAR):
    c.setFillColor(color); c.circle(x, y, 3.6, fill=1, stroke=0)
    c.setStrokeColor(white); c.setLineWidth(1.3)
    c.line(x - 1.9, y, x - 0.5, y - 1.6); c.line(x - 0.5, y - 1.6, x + 2.2, y + 1.8)
def bullets(items, x, y_top, w, gap=3.0, size=9.0):
    y = y_top
    for b, t in items:
        para = P(f'<b>{b}</b>{t}', size=size, leading=size * 1.27)
        pw, ph = para.wrap(w - 14, 400)
        para.drawOn(c, x + 14, y - ph)
        check(x + 5, y - 6)
        y -= ph + gap
    return y

# ================= HEADER =================
band_h = 112
c.setFillColor(NAR); c.rect(0, H - band_h, W, band_h, fill=1, stroke=0)
c.setFillColor(AMA); c.rect(0, H - band_h - 5, W, 5, fill=1, stroke=0)
logo = ImageReader(LOGO); lw_, lh_ = logo.getSize(); lh = 78; lw = lh * lw_ / lh_
c.drawImage(logo, 34, H - band_h + (band_h - lh) / 2, width=lw, height=lh, mask=None)
flow([P('Dos cosas que te van a decir<br/>en todas partes', 22, white, True, TA_LEFT, 25),
      P('Antes de decidir dónde aprender inglés, léelas. Presencial en Bucaramanga · grupos de máximo 16 · la única academia presencial de la ciudad con garantía de aprendizaje por escrito', 8.6, HexColor('#FFE7D6'), False, TA_LEFT, 11.5)],
     34 + lw + 22, H - band_h + 6, W - (34 + lw + 22) - 30, band_h - 28)

# ================= TWO CARDS =================
m = 30; gap = 12; cw = (W - 2 * m - gap) / 2
top = H - band_h - 5 - 16; card_h = 384; bot = top - card_h

# ---- Card 1: C1
rbox(m, bot, cw, card_h, CREMA, LINEA, 12)
rbox(m, top - 46, cw, 46, NAR, None, 12); c.setFillColor(NAR); c.rect(m, top - 46, cw, 14, fill=1, stroke=0)
flow([P('"AQUÍ LLEGAS HASTA C1"', 11.5, white, True, TA_CENTER), P('Lo que te van a decir', 8.4, HexColor('#FFE7D6'), False, TA_CENTER)], m + 8, top - 44, cw - 16, 42)
flow([P('Lo que de verdad te piden: B2', 15, NAR2, True, TA_CENTER, 18),
      P('Vacantes, entrevistas, universidades y programas en el exterior piden B2. C1 es para traducir, enseñar o investigar.', 8.2, GRIS, False, TA_CENTER, 10.5)], m + 10, top - 100, cw - 20, 52)
y = bullets([
    ('"Hasta C1" es un nombre en una lista. ', 'Pregunta en cualquier academia dos cosas: cuántos de sus estudiantes llegaron, y quién lo garantiza por escrito.'),
    ('En Heiiu llegas a B2 en 575 horas presenciales, ', 'con garantía por escrito en cada nivel: si cumples y no avanzas, te devolvemos el nivel.'),
    ('Al terminar B2, Refuerzo PRO: ', 'lo que irías a buscar en un C1, en menos tiempo y enfocado en lo que vas a usar: pitch avanzado, negociación real en inglés, entrevistas difíciles y tu video del antes y después. Es para el estudiante que quiere usar el inglés, no coleccionar niveles.'),
    ('Módulo de Graduación al terminar A2: ', 'Emprendedor (tu página web publicada y tu primer mensaje de venta en inglés a un cliente real) o Pasaporte (tu hoja de vida en inglés, tu video de presentación y tu entrevista ensayada).'),
    ('¿Y qué es C1, entonces? ', 'Leer textos largos y académicos, captar el humor, los dobles sentidos y lo que no se dice. Eso no lo da un salón: lo da usar el inglés todos los días, trabajando o viviendo en él. Primero se habla. Eso es B2, y es lo que te garantizamos. Lo demás es un argumento de venta, no un resultado.'),
], m + 10, top - 108, cw - 20)

# ---- Card 2: Virtual
x2 = m + cw + gap
rbox(x2, bot, cw, card_h, CREMA, LINEA, 12)
rbox(x2, top - 46, cw, 46, NAR, None, 12); c.setFillColor(NAR); c.rect(x2, top - 46, cw, 14, fill=1, stroke=0)
flow([P('"TAMBIÉN TENEMOS VIRTUAL"', 11.5, white, True, TA_CENTER), P('Lo que te van a decir', 8.4, HexColor('#FFE7D6'), False, TA_CENTER)], x2 + 8, top - 44, cw - 16, 42)
flow([P('Hablar se entrena en un salón', 15, NAR2, True, TA_CENTER, 18),
      P('Lo que te hace hablar no es la pantalla: es la simulación real, el grupo y el profesor que te corrige ahí mismo.', 8.2, GRIS, False, TA_CENTER, 10.5)], x2 + 10, top - 100, cw - 20, 52)
y2 = bullets([
    ('En grupo somos presenciales a propósito. ', 'Cada clase tiene una simulación real (una entrevista, una llamada, una reunión) con el profesor como coach, en grupos de máximo 16 y con el celular guardado. Eso no se reemplaza con una cámara apagada.'),
    ('Lo que sí es virtual: tu práctica diaria. ', 'Todos los días grabas un video corto en inglés desde tu casa y tu profesor te lo devuelve con una mejora. Entrenas en el salón y en tu celular.'),
    ('Si necesitas virtual de verdad, lo tenemos: ', 'clases personalizadas, uno a uno por videollamada, desde 30 horas, en tu horario. Se cotizan en la asesoría.'),
    ('Jornadas presenciales: ', 'mañana 8:00 a 12:00, noche 6:30 a 8:30 p. m., y sábados 8:00 a 12:00. Dos horas en tu día, a cambio de hablar.'),
    ('Lo que pasa con el virtual, de frente: ', 'en los cursos en línea solo 3 de cada 100 inscritos terminan (estudio de MIT y Harvard sobre cursos masivos, revista Science, 2019). Se arranca con ganas y a la tercera semana ganan el gato, la visita o el cansancio; la clase se deja y queda la sensación de haber pagado por nada. No es falta de voluntad: es que nadie te está mirando. Aquí sí.'),
], x2 + 10, top - 108, cw - 20)

# ================= GUARANTEE BAND =================
gy = bot - 12; gh = 118
rbox(m, gy - gh, W - 2 * m, gh, NAR, None, 12)
flow([P('LA GARANTÍA HEIIU, TAL COMO QUEDA EN TU CONTRATO', 9.5, AMA, True, TA_CENTER),
      P('"Si cumples — asistencia, tareas, evaluaciones — y no avanzas, te devolvemos el 100% del nivel. Por escrito, en el contrato."', 9.6, white, True, TA_CENTER, 12.5),
      P('<b>¿Por qué nadie más la da?</b> Porque quien vende acceso (horas, plataforma, niveles en una lista) no puede responder por el resultado. Nosotros vendemos el resultado, y por eso respondemos por él.', 8.3, HexColor('#FFE7D6'), False, TA_CENTER, 10.8),
      P('<b>¿A quién le debería dar miedo?</b> Al que no va a cumplir su parte: asistir (máximo 20% de faltas por nivel), hacer las tareas (90%) y presentar las evaluaciones. A ese no le sirve, y se lo decimos antes de pagar. Al que cumple, le funciona; y si no, le devolvemos el 100% del nivel. No te prometemos que sea fácil. Te prometemos que funciona si haces tu parte.', 8.3, HexColor('#FFE7D6'), False, TA_CENTER, 10.8)],
     m + 14, gy - gh + 6, W - 2 * m - 28, gh - 10)

# ================= FOOTER =================
fy = gy - gh - 12
flow([P('<b>Pregúntanos qué fecha te queda. Escríbenos.</b> · Carrera 27 # 48-49, Sotomayor, Bucaramanga · Instagram @Heiiu_english · Licencia desde 2012 · Certificación ICONTEC', 8.2, GRIS, False, TA_CENTER, 10.5)],
     m, fy - 24, W - 2 * m, 24)
c.save(); print('OK', OUT)
