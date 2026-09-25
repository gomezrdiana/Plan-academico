# -*- coding: utf-8 -*-
"""Hoja para el CLIENTE 'Dos caminos' — version de diseno (reportlab, logo, colores de marca). Una pagina carta.
Reemplaza el PDF del generador docx. Colores: naranja de marca FF4A00 (presentacion), amarillo FBC900, crema FFF8E7."""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.utils import ImageReader

R = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
LOGO = R + r'\recursos\marca heiiu\logo_heiiu_sobre_naranja.png'
OUT = R + r'\recursos\comercial\INDUCCION_COMERCIAL\HOJA_CLIENTE_DOS_CAMINOS.pdf'

NAR = HexColor('#FF4A00'); NAR2 = HexColor('#E54C09'); AMA = HexColor('#FBC900'); CREMA = HexColor('#FFF8E7')
GRIS = HexColor('#5A5A5A'); GRISC = HexColor('#8A8A8A'); NEGRO = HexColor('#222222'); LINEA = HexColor('#F0D9C8')

W, H = letter
c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle('Heiiu — Dos caminos para hablar inglés de verdad')

def P(text, size=9.2, color=NEGRO, bold=False, align=TA_LEFT, leading=None, font=None):
    st = ParagraphStyle('p', fontName=font or ('Helvetica-Bold' if bold else 'Helvetica'), fontSize=size,
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

def bullets(items, x, y_top, w, gap=2.6, size=9.0):
    """items: list of (bold, text). Dibuja check + parrafo; devuelve y final."""
    y = y_top
    for b, t in items:
        para = P(f'<b>{b}</b>{t}', size=size, leading=size * 1.27)
        pw, ph = para.wrap(w - 14, 400)
        para.drawOn(c, x + 14, y - ph)
        check(x + 5, y - 6)
        y -= ph + gap
    return y

# ================= HEADER BAND =================
band_h = 112
c.setFillColor(NAR); c.rect(0, H - band_h, W, band_h, fill=1, stroke=0)
c.setFillColor(AMA); c.rect(0, H - band_h - 5, W, 5, fill=1, stroke=0)
logo = ImageReader(LOGO); lw_, lh_ = logo.getSize(); lh = 78; lw = lh * lw_ / lh_
c.drawImage(logo, 34, H - band_h + (band_h - lh) / 2, width=lw, height=lh, mask=None)
flow([P('Dos caminos para hablar<br/>inglés de verdad', 22, white, True, TA_LEFT, 25),
      P('Presencial en Bucaramanga · grupos de máximo 16 · la única academia de la ciudad con garantía de aprendizaje por escrito', 8.6, HexColor('#FFE7D6'), False, TA_LEFT, 11.5)],
     34 + lw + 22, H - band_h + 6, W - (34 + lw + 22) - 30, band_h - 28)

# ================= TWO CARDS =================
m = 30; gap = 12; cw = (W - 2 * m - gap) / 2
top = H - band_h - 5 - 16; card_h = 372; bot = top - card_h
# Card 1 (Arranque) — crema
rbox(m, bot, cw, card_h, CREMA, LINEA, 12)
rbox(m, top - 46, cw, 46, NAR, None, 12); c.setFillColor(NAR); c.rect(m, top - 46, cw, 14, fill=1, stroke=0)
flow([P('CAMINO 1 · ARRANQUE A1 + A2', 11.5, white, True, TA_CENTER), P('Empieza hoy y decide después', 8.4, HexColor('#FFE7D6'), False, TA_CENTER)], m + 8, top - 44, cw - 16, 42)
flow([P('$2.990.000', 24, NAR2, True, TA_CENTER, 26), P('Precio de lanzamiento · 20 cupos · cohorte del 5 de octubre', 7.8, GRIS, False, TA_CENTER, 10)], m + 8, top - 96, cw - 16, 48)
y = bullets([
    ('200 horas presenciales: ', 'los dos primeros niveles completos.'),
    ('Libros incluidos si aseguras tu cupo hoy mismo, ', 'y certificado oficial por cada nivel aprobado.'),
    ('Hablas desde el primer día: ', 'clases activas, en inglés, con situaciones reales: presentarte, tu trabajo, llamadas, entrevistas.'),
    ('Jornadas: ', 'mañana 8:00 a 12:00 (dos meses y medio) o noche 6:30 a 8:30 PM (cinco meses).'),
    ('Garantía por escrito ', 'en tu contrato.'),
    ('Módulo de Graduación incluido, ', 'a tu elección al terminar:'),
], m + 10, top - 104, cw - 20)
# sub-bullets modulos
for b, t in [('Emprendedor: ', 'sales con tu página web publicada, tu pitch en inglés y tu primer mensaje de venta enviado a un cliente real.'),
             ('Pasaporte: ', 'sales con tu video de presentación, tu hoja de vida en inglés y la entrevista ensayada para programas como Au Pair o Work and Travel.')]:
    para = P(f'<b><font color="#E54C09">{b}</font></b>{t}', 8.6, leading=11); pw, ph = para.wrap(cw - 44, 300); para.drawOn(c, m + 30, y - ph); y -= ph + 2.4
y = bullets([('Al terminar, ', 'si quieres seguir a B1 y B2, continúas con el Fondo de Becas.')], m + 10, y - 2, cw - 20)

# Card 2 (Completo) — blanco con borde
x2 = m + cw + gap
rbox(x2, bot, cw, card_h, white, NAR, 12, 1.4)
rbox(x2, top - 46, cw, 46, NAR2, None, 12); c.setFillColor(NAR2); c.rect(x2, top - 46, cw, 14, fill=1, stroke=0)
flow([P('CAMINO 2 · PROGRAMA COMPLETO A1 → B2', 11.5, white, True, TA_CENTER), P('Comprométete con la meta completa', 8.4, HexColor('#FFE7D6'), False, TA_CENTER)], x2 + 8, top - 44, cw - 16, 42)
flow([P('Beca del Fondo según tu perfil', 16, NAR2, True, TA_CENTER, 19), P('Precio pleno $8.696.000 · tu beca se define en la asesoría', 7.8, GRIS, False, TA_CENTER, 10)], x2 + 8, top - 96, cw - 16, 48)
bullets([
    ('575 horas presenciales: ', 'los cuatro niveles, de cero a nivel profesional.'),
    ('Libros incluidos si aseguras tu cupo hoy mismo, ', 'y certificado oficial por cada nivel aprobado.'),
    ('Todo lo del Arranque, ', 'y además B1 y B2: presentaciones, reuniones, negociación, entrevistas difíciles, pitch de 90 segundos, pedir un aumento, manejar un cliente molesto.'),
    ('Garantía por escrito ', 'en cada nivel.'),
    ('Módulo de Graduación ', 'al terminar A2 (Emprendedor o Pasaporte).'),
    ('Refuerzo PRO al terminar B2: ', 'pitch avanzado, negociación real en inglés y tu video del antes y después.'),
    ('La beca más alta: ', 'si eres afiliado a Cajasan, entras directo a la beca más alta del Fondo con tu carné.'),
    ('Un solo compromiso, un solo precio: ', 'los cuatro niveles juntos cuestan más de un millón menos que uno a uno.'),
], x2 + 10, top - 104, cw - 20)

# ================= GARANTIA =================
gy_top = bot - 14; g_h = 78; gy = gy_top - g_h
rbox(m, gy, W - 2 * m, g_h, CREMA, None, 10)
c.setFillColor(AMA); c.roundRect(m, gy, 7, g_h, 3, fill=1, stroke=0)
flow([P('LA GARANTÍA HEIIU, TAL COMO QUEDA EN TU CONTRATO', 9.6, NAR2, True, TA_CENTER),
      P('"Si cumples — asistencia, tareas, evaluaciones — y no avanzas, te devolvemos el 100% del nivel. Por escrito, en el contrato."', 10.4, NEGRO, True, TA_CENTER, 13.5),
      P('Es un trato: nosotros ponemos el método, el profesor y el respaldo. Tú pones el trabajo: asistir, hacer las tareas y grabar tu video corto de práctica todos los días. No te prometemos que sea fácil. Te prometemos que funciona si haces tu parte.', 8.3, GRIS, False, TA_CENTER, 10.6)],
     m + 18, gy + 6, W - 2 * m - 30, g_h - 10)

# ================= PAGO / SIGUIENTE PASO =================
py_top = gy - 12; p_h = 136; py = py_top - p_h
rbox(m, py, cw, p_h, white, LINEA, 10)
rbox(x2, py, cw, p_h, white, LINEA, 10)
flow([P('CÓMO PUEDES PAGAR', 9.6, NAR2, True)], m + 12, py_top - 18, cw - 24, 16)
bullets([('Contado: ', 'transferencia, tarjeta débito o crédito, o efectivo en la sede.'),
         ('Cesantías o crédito de tu cooperativa o banco: ', 'cuentan como pago de contado.'),
         ('A cuotas: ', 'con una inicial y mensualidades; el plan exacto se arma en tu asesoría.'),
         ('Afiliado a Cajasan: ', 'condiciones especiales por nuestro convenio, la única academia de inglés de la ciudad que lo tiene.')],
        m + 10, py_top - 24, cw - 20, gap=2.2, size=8.6)
flow([P('TU SIGUIENTE PASO', 9.6, NAR2, True)], x2 + 12, py_top - 18, cw - 24, 16)
bullets([('Asegura tu cupo HOY con $300.000: ', 'te congela el cupo y el precio por 7 días, te deja los libros incluidos, y se cruza con tu primer pago.'),
         ('Tienes 5 días hábiles ', 'para cambiar de opinión con devolución total, por ley.'),
         ('La matrícula se formaliza en la sede: ', 'Carrera 27 # 48-49, segundo piso, Sotomayor.'),
         ('Cohorte del Arranque: ', '5 de octubre. Los 20 cupos de lanzamiento se asignan en orden de llegada.')],
        x2 + 10, py_top - 24, cw - 20, gap=2.2, size=8.6)

# ================= FOOTER =================
fy = py - 12
c.setFillColor(NAR); c.rect(0, 0, W, 30, fill=1, stroke=0)
flow([P('Tu asesora: <b>Paula Saenz</b> · WhatsApp <b>315 547 0657</b> · Instagram @Heiiu_english · Heiiu English Academy, Bucaramanga', 8.8, white, False, TA_CENTER)], m, 9, W - 2 * m, 16)

c.showPage()

# ======================= PÁGINA 2: TU RUTA DE A1 A B2 =======================
band2 = 84
c.setFillColor(NAR); c.rect(0, H - band2, W, band2, fill=1, stroke=0)
c.setFillColor(AMA); c.rect(0, H - band2 - 5, W, 5, fill=1, stroke=0)
lh2 = 58; lw2 = lh2 * lw_ / lh_
c.drawImage(logo, 34, H - band2 + (band2 - lh2) / 2, width=lw2, height=lh2, mask=None)
flow([P('Tu ruta de A1 a B2', 22, white, True, TA_LEFT, 25),
      P('Qué aprendes en cada nivel · 575 horas presenciales · un certificado oficial por cada nivel aprobado', 8.6, HexColor('#FFE7D6'), False, TA_LEFT, 11.5)],
     34 + lw2 + 22, H - band2 + 8, W - (34 + lw2 + 22) - 30, band2 - 22)

niveles = [
 ('A1', 'FUNDAMENTOS', '90 horas',
  'Te presentas y presentas a otros, hablas de tu rutina, tu familia, tu trabajo y tu ciudad. Manejas números, hora y precios. Cuentas cosas en presente, en pasado y haces planes.',
  'Situaciones: conocer a alguien, describir tu día, pedir y dar información básica, hablar de lo que hiciste ayer.',
  'Cierra con tu presentación oral: MY WORLD.'),
 ('A2', 'VIDA DIARIA Y TRABAJO', '110 horas',
  'Hablas de futuro, condiciones y experiencias (presente perfecto), describes personas y cosas, comparas, usas los verbos con preposición que se oyen todos los días.',
  'Situaciones: entrevista de trabajo, llamadas, hotel, tienda, restaurante, servicio al cliente, reunión de equipo, primer día en un empleo.',
  'Cierra con tu presentación oral de 7 a 10 minutos: MY LIFE. Y eliges tu Módulo de Graduación: Emprendedor o Pasaporte.'),
 ('B1', 'COMUNICACIÓN CON FLUIDEZ', '175 horas',
  'Consolidas toda la gramática en contexto profesional y agregas la del nivel: deducir, el tercer condicional, "debí haber", conectores, preguntas indirectas, discurso indirecto y tiempos perfectos.',
  'Situaciones: briefings de trabajo, entrevistas, onboarding, coordinar horarios, planear proyectos, evaluaciones de desempeño, negociar con proveedores.',
  'Presentación intermedia MY STORY, MY GOALS; taller de pitch y presentaciones finales.'),
 ('B2', 'NIVEL PROFESIONAL', '200 horas',
  'Primera mitad, vida real: quejas en un restaurante, direcciones, compras y devoluciones, médico, arriendo, banco, aeropuerto, desacuerdos. Segunda mitad, mundo profesional.',
  'Situaciones: networking, tu CV en 3 minutos, entrevistas difíciles, reuniones, presentar una idea, cliente molesto, negociar y cerrar, dar y recibir feedback, pitch de 90 segundos, pedir un aumento.',
  'Cierra con un simulacro de una jornada completa de trabajo en inglés. Con el programa completo: Refuerzo PRO (pitch avanzado, negociación real y tu video del antes y después).'),
]
y_top = H - band2 - 5 - 14; card_h2 = 116; gap2 = 9; m2 = 30; cw2 = W - 2 * m2
fondos = [CREMA, white, CREMA, white]
for i, (niv, nom, horas, que, sit, cierre) in enumerate(niveles):
    yt = y_top - i * (card_h2 + gap2); yb = yt - card_h2
    rbox(m2, yb, cw2, card_h2, fondos[i], LINEA if fondos[i] == white else None, 12)
    # etiqueta de nivel a la izquierda
    rbox(m2, yb, 78, card_h2, NAR if i % 2 == 0 else NAR2, None, 12); c.setFillColor(NAR if i % 2 == 0 else NAR2); c.rect(m2 + 60, yb, 18, card_h2, fill=1, stroke=0)
    flow([P(niv, 30, white, True, TA_CENTER, 32), P(horas, 8.6, HexColor('#FFE7D6'), False, TA_CENTER)], m2 + 4, yb + card_h2 / 2 - 24, 70, 48)
    st_gap = ParagraphStyle('g', fontName='Helvetica', fontSize=3, leading=3)
    flow([P(nom, 11.5, NAR2, True), Paragraph('', st_gap), P(que, 9.6, NEGRO, False, TA_LEFT, 12.4), Paragraph('', st_gap), P('<b>' + sit + '</b>', 9.2, GRIS, False, TA_LEFT, 11.8), Paragraph('', st_gap), P(cierre, 9.2, NAR2, True, TA_LEFT, 11.8)],
         m2 + 90, yb + 6, cw2 - 100, card_h2 - 10)

# caja final: como sabemos que avanzas
by_top = y_top - 4 * (card_h2 + gap2) - 2; b_h = 74; by = by_top - b_h
rbox(m2, by, cw2, b_h, CREMA, None, 10); c.setFillColor(AMA); c.roundRect(m2, by, 7, b_h, 3, fill=1, stroke=0)
flow([P('LO QUE TE LLEVAS AL TERMINAR', 9.6, NAR2, True, TA_CENTER),
      P('Un certificado oficial por cada nivel, válido en cualquier ciudad. Tu Módulo de Graduación: la página web publicada y tu primer mensaje de venta en inglés, o tu video de presentación y tu hoja de vida listos para irte. Con el programa completo, el Refuerzo PRO. Y algo que nadie te puede quitar: tu propio video del primer día al lado del último, para que veas cuánto cambiaste.', 8.8, GRIS, False, TA_CENTER, 11.4)],
     m2 + 18, by + 6, cw2 - 30, b_h - 10)

# pie
c.setFillColor(NAR); c.rect(0, 0, W, 30, fill=1, stroke=0)
flow([P('Garantía por escrito en cada nivel · Tu asesora: <b>Paula Saenz</b> · WhatsApp <b>315 547 0657</b> · Instagram @Heiiu_english', 8.6, white, False, TA_CENTER)], m2, 9, W - 2 * m2, 16)

c.showPage(); c.save()
print('OK', OUT)
