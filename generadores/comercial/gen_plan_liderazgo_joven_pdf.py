# -*- coding: utf-8 -*-
"""PLAN DE LIDERAZGO EN INGLÉS — hoja para el acudiente de un joven que YA habla inglés y entra directo a B2.
Reglas de Diana (28/10/2026): sin garantía (ya habla), sin video diario, sin libros (B2 no tiene), sin Cajasan.
Enfoque: experiencia única y retadora, liderazgo y competencias para su vida. Contenido = guías B2 vigentes (VERSION_2/B2_2H),
sistema de carácter del Blueprint (4 virtudes, fortalezas, carta al yo del futuro), portafolio (entrada, hito cada 10 clases, salida).
Página 1: punto de partida, cómo es su experiencia, competencias, carácter, lo que ve el acudiente, cómo empezar.
Página 2: las 200 horas en dos fases + proyecto final. Por rol, sin nombres.
Salida: recursos/personalizados/JOVEN_BILINGUE/PLAN_LIDERAZGO_B2_JOVEN.pdf
Uso: python -X utf8 generadores/comercial/gen_plan_liderazgo_joven_pdf.py"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.utils import ImageReader

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGO = os.path.join(R, 'recursos', 'marca heiiu', 'logo_heiiu_sobre_naranja.png')
OUTDIR = os.path.join(R, 'recursos', 'personalizados', 'JOVEN_BILINGUE')
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, 'PLAN_LIDERAZGO_B2_JOVEN.pdf')

NAR = HexColor('#FF4A00'); NAR2 = HexColor('#E54C09'); AMA = HexColor('#FBC900'); CREMA = HexColor('#FFF8E7')
GRIS = HexColor('#5A5A5A'); NEGRO = HexColor('#222222'); LINEA = HexColor('#F0D9C8'); CLARO = HexColor('#FFE7D6')

W, H = letter
c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle('Heiiu — Plan de liderazgo en inglés')

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

def bullets(items, x, y_top, w, gap=2.8, size=9.0):
    y = y_top
    for b, t in items:
        para = P('<b>%s</b>%s' % (b, t), size=size, leading=size * 1.27)
        pw, ph = para.wrap(w - 14, 400)
        para.drawOn(c, x + 14, y - ph)
        check(x + 5, y - 6)
        y -= ph + gap
    return y

def header(titulo, sub, band_h):
    c.setFillColor(NAR); c.rect(0, H - band_h, W, band_h, fill=1, stroke=0)
    c.setFillColor(AMA); c.rect(0, H - band_h - 5, W, 5, fill=1, stroke=0)
    logo = ImageReader(LOGO); lw_, lh_ = logo.getSize(); lh = band_h - 34; lw = lh * lw_ / lh_
    c.drawImage(logo, 34, H - band_h + (band_h - lh) / 2, width=lw, height=lh, mask=None)
    flow([P(titulo, 21, white, True, TA_LEFT, 24), P(sub, 8.6, CLARO, False, TA_LEFT, 11.5)],
         34 + lw + 22, H - band_h + 6, W - (34 + lw + 22) - 30, band_h - 24)

def footer(texto):
    c.setFillColor(NAR); c.rect(0, 0, W, 30, fill=1, stroke=0)
    flow([P(texto, 8.6, white, False, TA_CENTER)], 30, 9, W - 60, 16)

def titulo_tarjeta(x, top, w, t1, t2, col):
    rbox(x, top - 46, w, 46, col, None, 12); c.setFillColor(col); c.rect(x, top - 46, w, 14, fill=1, stroke=0)
    flow([P(t1, 11, white, True, TA_CENTER), P(t2, 8.4, CLARO, False, TA_CENTER)], x + 8, top - 44, w - 16, 42)

# ======================= PÁGINA 1 =======================
band_h = 112
header('Plan de liderazgo en inglés',
       'Una experiencia única y retadora para un joven que ya habla inglés · 200 horas presenciales en el nivel B2 · Bucaramanga', band_h)

m = 30; gap = 12; cw = (W - 2 * m - gap) / 2
top = H - band_h - 5 - 16
x2 = m + cw + gap
card_h = 372; bot = top - card_h

# --- Izquierda: punto de partida + experiencia ---
rbox(m, bot, cw, card_h, CREMA, LINEA, 12)
titulo_tarjeta(m, top, cw, 'EL PUNTO DE PARTIDA', 'el inglés ya lo trae; lo que falta es usarlo para liderar', NAR)
flow([P('Él ya habla inglés. Lo que todavía no ha hecho es <b>usarlo para dirigir</b>: pararse frente a un grupo, defender una idea, '
        'mediar un desacuerdo, reconocer un error en voz alta, presentar un proyecto y responder preguntas. Ese es el reto. '
        'El inglés es la herramienta; lo que se entrena es el carácter y la forma de liderar.', 8.9, NEGRO, False, TA_LEFT, 11.6)],
     m + 12, top - 118, cw - 24, 70)
flow([P('CÓMO ES SU EXPERIENCIA', 9.6, NAR2, True)], m + 12, top - 136, cw - 24, 14)
bullets([
    ('Entra directo a B2: ', 'la prueba de ubicación (examen en línea y entrevista oral) confirma el nivel. No repite nada.'),
    ('Clases presenciales en inglés, de pie, ', 'con simulaciones de la vida real y del mundo profesional. Nada de pantalla.'),
    ('Un rol en cada simulación: ', 'presentador, mediador o coach. Como coach observa a sus compañeros, anota y les da retroalimentación en inglés.'),
    ('Énfasis en liderazgo: ', 'en cada clase se le pide dirigir algo: una presentación, un debate o una decisión del grupo.'),
    ('Tarea: ', 'preparar sus intervenciones (la presentación, el debate, el pitch) para llegar a defenderlas.'),
], m + 10, top - 144, cw - 20)

# --- Derecha: competencias + carácter ---
rbox(x2, bot, cw, card_h, white, NAR, 12, 1.4)
titulo_tarjeta(x2, top, cw, 'COMPETENCIAS PARA SU VIDA', 'lo que se lleva, además del inglés', NAR2)
bullets([
    ('Hablar en público: ', 'tres minutos, una idea, de pie y sin leer.'),
    ('Pensamiento crítico: ', 'deducir, argumentar y cambiar de opinión con razones.'),
    ('Liderazgo y trabajo en equipo: ', 'tomar el mando cuando nadie lo hace y repartir el trabajo.'),
    ('Resolución de conflictos: ', 'quedar en la mitad de dos que no se entienden.'),
    ('Comunicación asertiva: ', 'decir que no, dar malas noticias y reconocer un error.'),
    ('Negociación: ', 'pedir, ceder y cerrar un acuerdo.'),
], x2 + 10, top - 56, cw - 20, gap=2.4, size=8.8)
gy_h = 118; gy = bot + 10
rbox(x2 + 10, gy, cw - 20, gy_h, CREMA, None, 10)
c.setFillColor(AMA); c.roundRect(x2 + 10, gy, 6, gy_h, 3, fill=1, stroke=0)
flow([P('CARÁCTER, NO SOLO IDIOMA', 8.8, NAR2, True, TA_CENTER),
      P('Cada semana se trabaja una virtud: prudencia, coraje, templanza y justicia. Cada mes, su Tarjeta de Crecimiento de Carácter: curiosidad, inteligencia social, perseverancia, entusiasmo, autocontrol, gratitud y optimismo. '
        'El primer día escribe una carta a su yo del futuro; se abre el día de su graduación.', 8.4, NEGRO, False, TA_LEFT, 11)],
     x2 + 22, gy + 6, cw - 40, gy_h - 12)

# --- Fila inferior: lo que ve el acudiente + cómo empezar ---
py_top = bot - 14; p_h = 166; py = py_top - p_h
rbox(m, py, cw, p_h, white, LINEA, 10)
rbox(x2, py, cw, p_h, white, LINEA, 10)
flow([P('LO QUE USTED RECIBE COMO ACUDIENTE', 9.6, NAR2, True)], m + 12, py_top - 18, cw - 24, 16)
bullets([('Reporte de asistencia y avance: ', 'puntualidad, participación y roles cumplidos en clase.'),
         ('Las evaluaciones las comunica coordinación, ', 'nunca el profesor en el pasillo.'),
         ('Un plan con énfasis en liderazgo: ', 'el inglés es el medio; lo que se le exige es dirigir, presentar, mediar y decidir.')],
        m + 10, py_top - 24, cw - 20, gap=2.2, size=8.6)
flow([P('CÓMO EMPEZAR', 9.6, NAR2, True)], x2 + 12, py_top - 18, cw - 24, 16)
bullets([('1. Prueba de ubicación ', 'que confirme el nivel B2 (examen en línea desde casa y entrevista oral corta).'),
         ('2. Asesoría con el acudiente: ', 'jornada y plan de pagos. El acudiente firma el contrato.'),
         ('3. Cupo: ', 'se separa con $300.000, que se cruzan con el primer pago.'),
         ('Jornadas de B2, entre semana: ', 'noche 6:30 a 8:30 PM (unos 5 meses) o mañana 8:00 a 12:00 (unos 2 meses y medio). Se escoge la que cuadre con el colegio y se sostiene.'),
         ('El valor queda por escrito ', 'el día de la asesoría, antes de firmar. 5 días hábiles para cambiar de opinión con devolución total, por ley.')],
        x2 + 10, py_top - 24, cw - 20, gap=2.2, size=8.6)

footer('Heiiu English Academy · Carrera 27 # 48-49, segundo piso, Sotomayor, Bucaramanga · Instagram @Heiiu_english')
c.showPage()

# ======================= PÁGINA 2: LAS 200 HORAS =======================
band2 = 84
header('Su plan: 200 horas en B2', 'Dos fases · cada simulación con un rol para él · énfasis en liderazgo', band2)

fases = [
 ('FASE 1', 'LA VIDA REAL EN INGLÉS', 'primera mitad',
  'Situaciones donde algo sale mal y alguien tiene que resolverlo: un restaurante donde la cena se arruina, perderse en una ciudad, compras y devoluciones, contar su historia de principio a fin, el aeropuerto con maletas y retrasos, '
  'el primer día en un lugar nuevo, los vecinos y el muro de en medio, el banco y el dinero que no aparece, pedir ayuda o hacerlo solo, la máquina que no funciona, el cuerpo que pide parar, la mesa donde nadie está de acuerdo, '
  'y el simulacro donde alguien tiene que tomar el mando.',
  'Su rol: reacciona, resuelve y toma el mando. Cierra la fase con veinte noches en un mismo salón: una prueba de resistencia conversacional.'),
 ('FASE 2', 'HABLAR EN PÚBLICO Y LIDERAR', 'segunda mitad',
  'Quién es en tres minutos y su historia de principio a fin. Las preguntas clásicas y las difíciles de una entrevista, como la de un intercambio o una beca. Pedir sin hundirse y meterse en una conversación de grupo. '
  'La presentación: tres minutos, una idea. Dar buenas y malas noticias. Mantener la calma con alguien molesto. Negociar: poner un precio y encontrarse en la mitad. Decir que no sin decir que no. Reconocer un error. '
  'Dar y recibir retroalimentación. Quedar en la mitad de un conflicto de equipo. El pitch de 90 segundos de un proyecto propio. Una reunión solo con voces. La crisis cuando todo se rompe a la vez. Cinco puertas, un líder. '
  'Entregar su trabajo en manos de otro. Sentarse en la otra silla: él hace las preguntas. De la charla corta a la propuesta en cuatro minutos. Presentar los números de un proyecto.',
  'Su rol: presentador, mediador o coach de sus compañeros, con banco de vocabulario y trabalenguas en cada clase.'),
]
y_top = H - band2 - 5 - 16; m2 = 30; cw2 = W - 2 * m2; gap2 = 10
alturas = [130, 188]
yt = y_top
for i, (fase, nom, cuando, que, rol) in enumerate(fases):
    card_h2 = alturas[i]; yb = yt - card_h2
    rbox(m2, yb, cw2, card_h2, CREMA if i == 0 else white, None if i == 0 else LINEA, 12)
    col = NAR if i == 0 else NAR2
    rbox(m2, yb, 78, card_h2, col, None, 12); c.setFillColor(col); c.rect(m2 + 60, yb, 18, card_h2, fill=1, stroke=0)
    flow([P(fase, 19, white, True, TA_CENTER, 22), P(cuando, 8.4, CLARO, False, TA_CENTER)], m2 + 4, yb + card_h2 / 2 - 18, 70, 40)
    st_gap = ParagraphStyle('g', fontName='Helvetica', fontSize=3, leading=3)
    flow([P(nom, 11.5, NAR2, True), Paragraph('', st_gap), P(que, 9.4, NEGRO, False, TA_LEFT, 12.2), Paragraph('', st_gap),
          P('<b>' + rol + '</b>', 9.2, GRIS, False, TA_LEFT, 11.8)],
         m2 + 90, yb + 7, cw2 - 100, card_h2 - 12)
    yt = yb - gap2

# nota final
nh = 84; ny = yt - nh
rbox(m2, ny, cw2, nh, CREMA, None, 10)
c.setFillColor(AMA); c.roundRect(m2, ny, 6, nh, 3, fill=1, stroke=0)
flow([P('Lo que no vendemos: ', 9.2, NAR2, True),
      P('no es un curso de inglés para él: el inglés ya lo trae. Es un entrenamiento de liderazgo exigente, en inglés y en un grupo de adultos, donde se le pide más de lo que está acostumbrado a dar. '
        'No prometemos que sea fácil ni cómodo. Prometemos un reto a su medida y un rol en cada clase.', 8.8, NEGRO, False, TA_LEFT, 11.4)],
     m2 + 16, ny + 5, cw2 - 28, nh - 10)

footer('Heiiu English Academy, Bucaramanga · Instagram @Heiiu_english')
c.showPage(); c.save()
print('OK', OUT)
