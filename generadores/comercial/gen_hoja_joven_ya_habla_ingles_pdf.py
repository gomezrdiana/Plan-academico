# -*- coding: utf-8 -*-
"""Hoja para el ACUDIENTE de un joven que YA habla ingles y no quiere perderlo (misma linea grafica de la hoja 'Dos caminos').
Pagina 1: por que un idioma que no se usa se pierde, que hace Heiiu con un joven que ya habla, que ve el acudiente, garantia, como empezar.
Pagina 2: su ruta segun el nivel de entrada (A1-B2), con B2 reescrito como LIDERAZGO Y ORATORIA (sin CV, LinkedIn, aumento ni clientes).
Contenido de niveles = guias vigentes (VERSION_2); portafolio = entrada + hito cada 10 clases + salida. Por rol, sin nombres.
Salida: recursos/personalizados/JOVEN_BILINGUE/HOJA_ACUDIENTE_JOVEN_YA_HABLA_INGLES.pdf
Uso: python -X utf8 generadores/comercial/gen_hoja_joven_ya_habla_ingles_pdf.py"""
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
OUT = os.path.join(OUTDIR, 'HOJA_ACUDIENTE_JOVEN_YA_HABLA_INGLES.pdf')

NAR = HexColor('#FF4A00'); NAR2 = HexColor('#E54C09'); AMA = HexColor('#FBC900'); CREMA = HexColor('#FFF8E7')
GRIS = HexColor('#5A5A5A'); NEGRO = HexColor('#222222'); LINEA = HexColor('#F0D9C8'); CLARO = HexColor('#FFE7D6')

W, H = letter
c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle('Heiiu — Para que no pierda el inglés: que lo use')

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

# ======================= PÁGINA 1 =======================
band_h = 112
header('Para que no pierda el inglés:<br/>que lo use',
       'Programa presencial en Bucaramanga para un joven que ya habla inglés · la única academia de la ciudad con garantía de aprendizaje por escrito', band_h)

m = 30; gap = 12; cw = (W - 2 * m - gap) / 2
top = H - band_h - 5 - 16
x2 = m + cw + gap

# --- Columna izquierda: diagnóstico + qué hacemos ---
card_h = 380; bot = top - card_h
rbox(m, bot, cw, card_h, CREMA, LINEA, 12)
rbox(m, top - 46, cw, 46, NAR, None, 12); c.setFillColor(NAR); c.rect(m, top - 46, cw, 14, fill=1, stroke=0)
flow([P('UN IDIOMA QUE NO SE USA SE PIERDE', 11, white, True, TA_CENTER), P('y qué hacemos con un joven que ya habla', 8.4, CLARO, False, TA_CENTER)], m + 8, top - 44, cw - 16, 42)
flow([P('Un idioma se sostiene con uso. Un joven que aprendió inglés y hoy solo lo oye en pantallas lo va perdiendo sin notarlo: primero la soltura, después el vocabulario, al final la confianza para hablar frente a otros. '
        'La respuesta no es volver a estudiar lo que ya sabe: es ponerlo a <b>usar el inglés en voz alta, todas las semanas, con exigencia y con público.</b>', 8.9, NEGRO, False, TA_LEFT, 11.6)],
     m + 12, top - 128, cw - 24, 80)
flow([P('QUÉ HACE HEIIU CON ÉL', 9.6, NAR2, True)], m + 12, top - 146, cw - 24, 14)
bullets([
    ('Entra donde está, no donde empiezan todos: ', 'prueba de ubicación (examen en línea más entrevista oral) y arranca en su nivel real. No repite lo que ya sabe.'),
    ('Horas de inglés hablado en grupo presencial: ', 'clases en inglés, de pie, con situaciones reales. Nadie se esconde detrás de una pantalla.'),
    ('Video diario de práctica: ', 'cada día graba un video corto que su profesor revisa. Es la tarea que mantiene el idioma vivo entre clase y clase.'),
    ('Un rol que lo hace crecer: ', 'en las simulaciones toma los papeles de presentador, mediador y coach: observa a sus compañeros, anota y les da retroalimentación en inglés.'),
    ('Carácter, no solo idioma: ', 'cada semana se trabaja una virtud (prudencia, coraje, templanza, justicia) y se entrena la disciplina de cumplir.'),
], m + 10, top - 154, cw - 20)

# --- Columna derecha: lo que ve el acudiente + garantía ---
rbox(x2, bot, cw, card_h, white, NAR, 12, 1.4)
rbox(x2, top - 46, cw, 46, NAR2, None, 12); c.setFillColor(NAR2); c.rect(x2, top - 46, cw, 14, fill=1, stroke=0)
flow([P('LO QUE USTED VE COMO ACUDIENTE', 11, white, True, TA_CENTER), P('pruebas, no promesas', 8.4, CLARO, False, TA_CENTER)], x2 + 8, top - 44, cw - 16, 42)
y = bullets([
    ('Grabación de entrada el primer día: ', 'queda archivada en la academia como punto de partida.'),
    ('Video de hito cada 10 clases: ', 'usted ve el avance con sus propios ojos, no por una nota.'),
    ('Reporte de asistencia y avance: ', 'puntualidad, tareas entregadas y lo que ya domina. Las evaluaciones las comunica coordinación, nunca el profesor en el pasillo.'),
    ('Grabación de salida y presentación final en vivo, ', 'con preguntas del público, al cerrar cada nivel.'),
    ('Certificado oficial ', 'por cada nivel aprobado, con examen final aplicado por un evaluador externo.'),
], x2 + 10, top - 56, cw - 20)
# garantía dentro de la tarjeta
gy_h = 150; gy = bot + 10
rbox(x2 + 10, gy, cw - 20, gy_h, CREMA, None, 10)
c.setFillColor(AMA); c.roundRect(x2 + 10, gy, 6, gy_h, 3, fill=1, stroke=0)
flow([P('LA GARANTÍA HEIIU, TAL COMO QUEDA EN EL CONTRATO', 8.8, NAR2, True, TA_CENTER),
      P('"Si cumple su parte (asistencia, tareas y evaluaciones) y no avanza en inglés, le devolvemos el 100% del nivel. Por escrito, en el contrato."', 9.4, NEGRO, True, TA_CENTER, 12.2),
      P('Nosotros ponemos el método, el profesor y el respaldo. Él pone el trabajo: asistir, hacer las tareas y grabar su video todos los días. No le prometemos que sea fácil. Le prometemos que funciona si hace su parte.', 7.9, GRIS, False, TA_CENTER, 10.2)],
     x2 + 22, gy + 6, cw - 40, gy_h - 12)

# --- Fila inferior: cómo empezar + jornadas ---
py_top = bot - 14; p_h = 150; py = py_top - p_h
rbox(m, py, cw, p_h, white, LINEA, 10)
rbox(x2, py, cw, p_h, white, LINEA, 10)
flow([P('CÓMO EMPEZAR', 9.6, NAR2, True)], m + 12, py_top - 18, cw - 24, 16)
bullets([('1. Prueba de ubicación: ', 'examen en línea desde casa y una entrevista oral corta con nosotros. Con eso sabemos en qué nivel entra.'),
         ('2. Asesoría con el acudiente: ', 'se define nivel, jornada y plan de pagos. El menor de 18 años entra con su acudiente, que firma el contrato.'),
         ('3. Cupo y arranque: ', 'se separa con $300.000, que se cruzan con el primer pago; los libros quedan incluidos si separa el mismo día.'),
         ('Tiene 5 días hábiles ', 'para cambiar de opinión con devolución total, por ley.')],
        m + 10, py_top - 24, cw - 20, gap=2.4, size=8.6)
flow([P('JORNADAS Y VALOR', 9.6, NAR2, True)], x2 + 12, py_top - 18, cw - 24, 16)
bullets([('Desde los 12 años en cualquier jornada: ', 'mañana 8:00 a 12:00, noche 6:30 a 8:30 PM, sabatino 8:00 a 12:00 (hasta B1) o tarde entre semana, en apertura.'),
         ('Se escoge la que cuadre con el colegio ', 'y se sostiene: la asistencia es parte de la garantía.'),
         ('El valor depende del nivel de entrada ', 'y de la forma de pago. Queda por escrito el día de la asesoría, antes de firmar.'),
         ('Afiliados a Cajasan: ', 'condiciones especiales con carné o certificado vigente.')],
        x2 + 10, py_top - 24, cw - 20, gap=2.4, size=8.6)

footer('Heiiu English Academy · Carrera 27 # 48-49, segundo piso, Sotomayor, Bucaramanga · Instagram @Heiiu_english')
c.showPage()

# ======================= PÁGINA 2: SU RUTA =======================
band2 = 84
header('Su ruta, según donde entre', 'Qué hace en cada nivel un joven que ya habla · los niveles anteriores a su ubicación ya los tiene y no los repite · un certificado oficial por cada nivel aprobado', band2)

niveles = [
 ('A1', 'FUNDAMENTOS', '90 horas',
  'Si entra aquí, ordena lo que sabe de oído: presentarse y presentar a otros, su rutina, su familia, su ciudad, números, hora y precios. Cuenta en presente y en pasado y hace planes.',
  'Situaciones: conocer a alguien, describir su día, pedir y dar información, contar lo que hizo ayer.',
  'Cierra con su presentación oral en vivo: MY WORLD.'),
 ('A2', 'VIDA DIARIA', '110 horas',
  'Habla de futuro, condiciones y experiencias, describe personas y cosas, compara, usa los verbos con preposición que se oyen todos los días.',
  'Situaciones: llamadas, hotel, tienda, restaurante, servicio al cliente, reunión de equipo, primer día en un lugar nuevo.',
  'Cierra con su presentación oral de 7 a 10 minutos: MY LIFE.'),
 ('B1', 'COMUNICACIÓN CON FLUIDEZ', '175 horas',
  'Consolida toda la gramática en contexto y agrega la del nivel: deducir, el tercer condicional, "debí haber", conectores, preguntas indirectas, discurso indirecto y tiempos perfectos. Dos profesores: uno de conversación y uno de gramática, que se pasan sus errores a diario.',
  'Situaciones: entrevistas, coordinar horarios, planear proyectos, evaluar un trabajo, negociar, debatir.',
  'Presentación intermedia MY STORY, MY GOALS; taller de pitch y presentaciones finales frente al grupo.'),
 ('B2', 'LIDERAZGO Y ORATORIA', '200 horas',
  'Primera mitad, la vida real en inglés: un restaurante donde todo sale mal, perderse en una ciudad, compras y devoluciones, aeropuerto, banco, vecinos, desacuerdos en la mesa, y el simulacro donde alguien tiene que tomar el mando. '
  'Segunda mitad, hablar en público y liderar: quién es en tres minutos, una presentación de tres minutos con una sola idea, dar buenas y malas noticias, debatir sin pelear, reconocer un error, dar y recibir retroalimentación, mediar en un conflicto de equipo, un pitch de 90 segundos de un proyecto propio, la entrevista para un intercambio o una beca, y manejar una crisis cuando todo se rompe a la vez.',
  'Rol en cada simulación: presentador, mediador o coach de sus compañeros. Banco de vocabulario y trabalenguas en cada clase.',
  'Cierra con su proyecto final en vivo, con preguntas del público, y su video del antes y el después.'),
]
y_top = H - band2 - 5 - 16; m2 = 30; cw2 = W - 2 * m2; gap2 = 10
alturas = [100, 104, 124, 184]
fondos = [CREMA, white, CREMA, white]
yt = y_top
for i, (niv, nom, horas, que, sit, cierre) in enumerate(niveles):
    card_h2 = alturas[i]; yb = yt - card_h2
    rbox(m2, yb, cw2, card_h2, fondos[i], LINEA if fondos[i] == white else None, 12)
    col = NAR if i % 2 == 0 else NAR2
    rbox(m2, yb, 78, card_h2, col, None, 12); c.setFillColor(col); c.rect(m2 + 60, yb, 18, card_h2, fill=1, stroke=0)
    flow([P(niv, 30, white, True, TA_CENTER, 32), P(horas, 8.6, CLARO, False, TA_CENTER)], m2 + 4, yb + card_h2 / 2 - 24, 70, 48)
    st_gap = ParagraphStyle('g', fontName='Helvetica', fontSize=3, leading=3)
    flow([P(nom, 11.5, NAR2, True), Paragraph('', st_gap), P(que, 9.6, NEGRO, False, TA_LEFT, 12.4), Paragraph('', st_gap),
          P('<b>' + sit + '</b>', 9.2, GRIS, False, TA_LEFT, 11.8), Paragraph('', st_gap), P(cierre, 9.4, NAR2, True, TA_LEFT, 12)],
         m2 + 90, yb + 7, cw2 - 100, card_h2 - 12)
    yt = yb - gap2

# nota final
nh = 78; ny = yt - 2 - nh
rbox(m2, ny, cw2, nh, CREMA, None, 10)
c.setFillColor(AMA); c.roundRect(m2, ny, 6, nh, 3, fill=1, stroke=0)
flow([P('Lo que no vendemos: ', 9.2, NAR2, True),
      P('no prometemos que sea fácil, ni rápido, ni un resultado por tener el cupo. Prometemos horas de inglés hablado con exigencia, un profesor que revisa su video cada día, y pruebas en video de dónde empezó y dónde va. Si él hace su parte, el inglés no se le pierde: se le vuelve una herramienta para pararse frente a otros y hablar.', 8.8, NEGRO, False, TA_LEFT, 11.4)],
     m2 + 16, ny + 5, cw2 - 28, nh - 10)

footer('Garantía por escrito en cada nivel · Heiiu English Academy, Bucaramanga · Instagram @Heiiu_english')
c.showPage(); c.save()
print('OK', OUT)
