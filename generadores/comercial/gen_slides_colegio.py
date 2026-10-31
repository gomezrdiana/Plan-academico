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

# ---------- 0b. VIDEO TECNICA O ACTITUD (abre la visita) ----------
VIDEO = os.path.join(OUT, 'Tecnica_o_Actitud_h264.mp4'); POSTER = os.path.join(OUT, 'POSTER_TECNICA_ACTITUD.jpg')
if os.path.exists(VIDEO):
    s = prs.slides.add_slide(BL); fondo(s, TINTA)
    texto(s, 0.85, 0.9, 7.6, 0.5, [[('UNA PREGUNTA', 14, True, AMA, TXT)]])
    texto(s, 0.85, 1.5, 7.6, 3.2, [[('¿Qué es más importante: la ', 44, True, BLANCO, TIT), ('técnica', 44, True, AMA, TIT), (' o la ', 44, True, BLANCO, TIT), ('actitud?', 44, True, AMA, TIT)]])
    texto(s, 0.85, 4.75, 7.2, 1.2, [[('Escuchen lo que responde este entrenador.', 22, False, MELOCOTON, TXT)]])
    s.shapes.add_picture(LOGO, Inches(0.55), Inches(6.35), height=Inches(0.85))
    vh = 6.6; vw = vh * 720 / 1280
    _pic = s.shapes.add_picture(POSTER, Inches(12.5 - vw), Inches(0.45), Inches(vw), Inches(vh)); _pic.name = 'VIDEO::' + os.path.basename(VIDEO)
    s.notes_slide.notes_text_frame.text = ('ABRE LA VISITA. El profesor saluda y, antes de pasar a esta diapositiva, pregunta al salon: levanten la mano, quien cree que la tecnica? quien cree que la actitud? '
        'Luego play (40 segundos; clic sobre el video). Al terminar, una sola frase: la tecnica se la enseñamos nosotros; la actitud la tiene que traer cada uno. Por eso no trabajamos con cualquiera. Y pasa a la siguiente diapositiva.')

# ---------- 0. APERTURA (despues del video, antes de la clase) ----------
s = prs.slides.add_slide(BL); fondo(s, TINTA)
s.shapes.add_picture(LOGO, Inches(0.55), Inches(0.35), height=Inches(1.1))
texto(s, 0.85, 1.75, 11.6, 2.6, [[('“I’m giving you these comments because I have ', 34, True, BLANCO, TIT), ('very high expectations', 34, True, AMA, TIT), (' and I know that you can reach them.”', 34, True, BLANCO, TIT)]])
texto(s, 0.85, 4.35, 11.0, 1.2, [[('“Te hago estos comentarios porque tengo expectativas muy altas y sé que puedes alcanzarlas.”', 20, False, MELOCOTON, TXT)]])
forma(s, MSO_SHAPE.RECTANGLE, 0.85, 5.75, 1.2, 0.07, NAR)
texto(s, 0.85, 5.95, 11.0, 0.9, [[('Aquí no te lo vamos a poner fácil. Vamos a estar contigo hasta que lo logres.', 20, True, BLANCO, TXT)]])
texto(s, 0.85, 6.75, 11.0, 0.4, [[('Frase de un estudio con estudiantes de colegio que cita Adam Grant.', 12, False, RGBColor(0xB8, 0xA8, 0x9A), TXT)]])
s.notes_slide.notes_text_frame.text = (
 'DESPUES DEL VIDEO, 2 minutos. El profesor, de pie, despacio:\n'
 '"Y ahora les comparto una frase de un estudio que cita Adam Grant. A unos estudiantes les devolvieron sus trabajos corregidos con una nota encima: te hago estos comentarios porque tengo expectativas muy altas y sé que puedes alcanzarlas. Muchos más de esos estudiantes decidieron volver a hacer su trabajo.\n'
 'Eso es lo que hacemos en Heiiu. Como papás, todos queremos proteger a nuestros hijos, y está bien. Y a todos nos gusta lo fácil. En nuestros años de academia lo hemos visto, y por eso nuestro programa cambió.\n'
 'Hoy trabajamos con estudiantes que quieren estar rodeados de gente como ellos: no el que está pegado al celular, no el que está porque el papá lo mandó, sino el que sabe que va a ser difícil y que lo va a lograr.\n'
 'Les vamos a sacar de la zona de confort. Se van a aburrir algunos días y van a encontrar la motivación otra vez. Les va a tocar hacer tareas todos los días, y son esos hábitos los que los van a diferenciar.\n'
 'No les vamos a prometer que es fácil. Les prometemos que vamos a estar ahí hasta que lo logren. Y para que lo vean, en vez de explicarles, vamos a hacerlo ya."\n'
 'Y pasa a la diapositiva de la actividad.')

# ---------- 0c. ACTIVIDAD (antes de coraje) ----------
s = prs.slides.add_slide(BL); fondo(s, TINTA)
texto(s, 0.85, 0.6, 8, 0.4, [[('AHORA USTEDES', 14, True, AMA, TXT)]])
texto(s, 0.85, 1.0, 11.6, 1.0, [[('¡Listo! ', 44, True, AMA, TIT), ('Hagamos una actividad.', 44, True, BLANCO, TIT)]])
texto(s, 0.85, 1.85, 11.6, 0.7, [[('Interviewer:  ', 24, False, MELOCOTON, TXT), ('“Tell me about yourself.”', 30, True, AMA, TIT)]], anchor=MSO_ANCHOR.MIDDLE)
frases = [('What’s your name?', 'Hi, my name is ', '______', '. I’m from Bucaramanga.'),
          ('What are you good at?', 'I’m good at ', '______', '.'),
          ('What can you do?', 'I can ', '______', '.'),
          ('Why do you want this job?', 'I want this job because ', '______', '.')]
for i, (q, a, b, c) in enumerate(frases):
    y = 2.75 + i * 0.95
    forma(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, y, 11.6, 0.8, CREMA, 0.25)
    forma(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, y, 4.0, 0.8, AMA, 0.25)
    texto(s, 1.1, y, 3.6, 0.8, [[(q, 18, True, TINTA, TIT)]], anchor=MSO_ANCHOR.MIDDLE)
    texto(s, 5.1, y, 7.2, 0.8, [[(a, 22, True, TINTA, TIT), (b, 22, True, NAR_OSC, TIT), (c, 22, True, TINTA, TIT)]], anchor=MSO_ANCHOR.MIDDLE)
s.shapes.add_picture(LOGO, Inches(11.3), Inches(0.35), height=Inches(0.75))
s.notes_slide.notes_text_frame.text = ('ACTIVIDAD, 15 minutos (ver la guía del profesor). Esta diapositiva reemplaza el tablero: queda proyectada toda la actividad. '
    'Coro, modelo, parejas y 4 voluntarios al frente. Cierra con aplauso y pasa a la siguiente.')

# ---------- 1. CORAJE ----------
s = prs.slides.add_slide(BL); fondo(s, TINTA)
forma(s, MSO_SHAPE.RECTANGLE, 10.6, 0, 2.75, 7.5, RGBColor(0x3D, 0x2B, 0x20))
forma(s, MSO_SHAPE.OVAL, 11.2, 5.4, 2.6, 2.6, AMA)
s.shapes.add_picture(LOGO, Inches(0.55), Inches(0.35), height=Inches(1.35))
texto(s, 0.85, 2.0, 9.2, 2.6, [[('Lo que acaban de hacer se llama ', 54, True, BLANCO, TIT), ('coraje.', 54, True, AMA, TIT)]])
texto(s, 0.85, 4.25, 9.5, 1.8, [
    [('Hablar en otro idioma frente a otros da miedo. Ustedes lo hicieron igual.', 22, False, BLANCO, TXT)],
    [('Eso no se aprende en un cuaderno: ', 22, True, BLANCO, TXT), ('se entrena.', 22, True, AMA, TXT)],
], espacio=10)
texto(s, 0.85, 6.65, 9.5, 0.5, [[('Salir de la zona de confort es el primer paso de todo lo que vale la pena.', 14, False, MELOCOTON, TXT)]])
s.notes_slide.notes_text_frame.text = 'Después del aplauso de la actividad. El profesor la lee en voz alta, despacio, y sigue: Es una de las cuatro virtudes cardinales que trabajamos en cada clase: sabiduría, coraje, templanza y justicia. ¿Por qué? Porque el inglés se aprende en cientos de días, y lo que hace que alguien llegue al final no es el talento: es el carácter. Y ese carácter les va a servir para la universidad, el trabajo y la vida. (Ver el cuadro de las virtudes en la guía.)'

# ---------- 1b. VIDEO TAREA (despues de coraje) ----------
VT = os.path.join(OUT, 'tarea_estudiante_b1_60s_h264.mp4'); PT = os.path.join(OUT, 'POSTER_tarea_estudiante_b1_60s.jpg')
if os.path.exists(VT):
    s = prs.slides.add_slide(BL); fondo(s, TINTA)
    texto(s, 0.85, 0.9, 7.6, 0.5, [[('ASÍ SE VE UNA TAREA', 14, True, AMA, TXT)]])
    texto(s, 0.85, 1.5, 7.6, 2.4, [[('Se equivoca. ', 44, True, BLANCO, TIT), ('Y lo hace igual.', 44, True, AMA, TIT)]])
    texto(s, 0.85, 3.4, 7.3, 2.4, [
        [('Una estudiante de B1 en su video diario de tarea.', 22, False, MELOCOTON, TXT)],
        [('Lo que importa no es que salga perfecto: es que se deja guiar y hace el trabajo difícil todos los días.', 22, True, BLANCO, TXT)],
    ], espacio=12)
    s.shapes.add_picture(LOGO, Inches(0.55), Inches(6.35), height=Inches(0.85))
    vh = 6.6; vw = vh * 478 / 850
    _pic = s.shapes.add_picture(PT, Inches(12.5 - vw), Inches(0.45), Inches(vw), Inches(vh)); _pic.name = 'VIDEO::' + os.path.basename(VT)
    s.notes_slide.notes_text_frame.text = ('Play (60 segundos). Al terminar: esto es lo que hacen todos los días. No es perfecto, y no tiene que serlo. '
        'Lo que diferencia a un estudiante no es el talento: es que vuelve a intentarlo con la corrección.')

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
forma(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, 5.35, 11.6, 1.0, TINTA, 0.18)
texto(s, 1.2, 5.35, 11.0, 1.0, [[('¿No tienes un negocio ni un plan? No importa. ', 20, True, BLANCO, TXT), ('Lo que se entrena es atreverte a hacerlo.', 20, True, AMA, TXT)]], anchor=MSO_ANCHOR.MIDDLE)
texto(s, 0.85, 6.65, 11.6, 0.5, [[('Garantía por escrito: si cumples tu parte y no avanzas en inglés, te devolvemos el 100% del nivel.', 14, True, NAR_OSC, TXT)]])
s.notes_slide.notes_text_frame.text = ('En A2 el proyecto es una muestra; en B2 se pule. El módulo no es obligatorio: la academia lleva al estudiante a hacerlo, pero la decisión es suya. El mensaje es la exposición, no el negocio: quien no tiene idea hace la página de su perfil profesional o de un proyecto del colegio. '
    'Si preguntan qué es el Refuerzo PRO: se define con cada estudiante al llegar a B2. Nada de precios aquí: eso va en la cita con cada familia.')

# ---------- 2b. TESTIMONIOS (despues del modulo) ----------
VM = os.path.join(OUT, 'testimonio_maria_alejandra_h264.mp4'); PM = os.path.join(OUT, 'POSTER_testimonio_maria_alejandra.jpg')
VS = os.path.join(OUT, 'testimonio_sarita_h264.mp4'); PS = os.path.join(OUT, 'POSTER_testimonio_sarita.jpg')
if os.path.exists(VM) and os.path.exists(VS):
    s = prs.slides.add_slide(BL); fondo(s, TINTA)
    texto(s, 0.85, 0.9, 5.2, 0.5, [[('ELLAS YA LO HICIERON', 14, True, AMA, TXT)]])
    texto(s, 0.85, 1.5, 5.2, 2.4, [[('Dos caminos. ', 40, True, BLANCO, TIT), ('Una misma actitud.', 40, True, AMA, TIT)]])
    texto(s, 0.85, 3.6, 5.0, 2.4, [
        [('María Alejandra', 20, True, AMA, TIT)], [('Se fue a Canadá.', 18, False, BLANCO, TXT)],
        [('Sarita', 20, True, AMA, TIT)], [('Estudia en casa, quiere ser médica y está terminando B2.', 18, False, BLANCO, TXT)],
    ], espacio=4)
    s.shapes.add_picture(LOGO, Inches(0.55), Inches(6.35), height=Inches(0.85))
    vh = 5.9; vw = vh * 720 / 1280
    _pic = s.shapes.add_picture(PM, Inches(5.95), Inches(0.8), Inches(vw), Inches(vh)); _pic.name = 'VIDEO::' + os.path.basename(VM)
    _pic = s.shapes.add_picture(PS, Inches(5.95 + vw + 0.25), Inches(0.8), Inches(vw), Inches(vh)); _pic.name = 'VIDEO::' + os.path.basename(VS)
    s.notes_slide.notes_text_frame.text = ('Primero el de la izquierda (María Alejandra, 57 s), luego el de la derecha (Sarita, 23 s): clic sobre cada video. '
        'Sin comentarios largos después: dejar que hablen ellas y pasar a la última diapositiva.')

# ---------- 2c. LO QUE CUESTA (remata el Gerente de Alianzas) ----------
s = prs.slides.add_slide(BL); fondo(s, CREMA)
texto(s, 0.85, 0.55, 8, 0.4, [[('LO QUE CUESTA', 14, True, NAR_OSC, TXT)]])
texto(s, 0.85, 0.95, 11.8, 0.9, [[('Programa completo A1 → B2', 36, True, TINTA, TIT)]])
texto(s, 0.85, 1.75, 11.8, 0.5, [[('575 horas presenciales · garantía por escrito · valor de lista $8.696.000', 18, False, GRIS, TXT)]])
# una sola tarjeta: de contado
forma(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, 2.45, 11.8, 2.0, BLANCO, 0.08)
forma(s, MSO_SHAPE.RECTANGLE, 1.1, 2.45, 11.3, 0.09, NAR)
texto(s, 1.2, 2.7, 11.0, 0.5, [[('De contado, con beca del Fondo', 20, True, NAR_OSC, TIT)]])
texto(s, 1.2, 3.3, 11.0, 1.0, [[('entre $4.782.800 y $5.913.280', 40, True, TINTA, TIT)]])
texto(s, 0.85, 4.6, 11.8, 0.5, [[('Con beca del Fondo según el perfil de cada familia. La beca exacta se asigna en la cita.', 15, False, GRIS, TXT)]])
forma(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, 5.05, 11.8, 1.5, TINTA, 0.18)
texto(s, 1.2, 5.1, 11.2, 1.4, [[('Separa hoy tu cupo desde $150.000: ', 22, True, AMA, TIT), ('congelas tu beca hasta el inicio del grupo y se abona a tu inicial.', 22, True, BLANCO, TIT)], [('Solo quienes separan hoy: taller de bienvenida de 2 horas en diciembre. ', 16, True, AMA, TXT), ('Es lo que cuesta una salida a comer para dos; aprender inglés es un mundo de oportunidades.', 16, False, MELOCOTON, TXT)]], anchor=MSO_ANCHOR.MIDDLE, espacio=4)
texto(s, 0.85, 6.6, 11.8, 0.4, [[('Afiliados a Cajasan: condiciones especiales con carné o certificado vigente.', 14, True, TINTA, TXT)]])
s.notes_slide.notes_text_frame.text = ('LA REMATA EL GERENTE DE ALIANZAS. Lee el precio de contado. Si preguntan por cuotas: eso se ve en la cita con la familia. Nunca decir descuento: se dice beca del Fondo. '
    'Cierre: hoy mismo separan desde $150.000 en la mesa (hoja de separación + QR de pagos). No se devuelve; se abona a la inicial y congela la beca hasta el inicio del grupo. La cita con la familia se concreta a más tardar el miércoles 4 de noviembre (el lunes es festivo). Si necesitan financiación, el Gerente de Alianzas les ayuda a buscarla.')

# ---------- 3. PRIMER PASO ----------
s = prs.slides.add_slide(BL); fondo(s, TINTA)
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
s.notes_slide.notes_text_frame.text = 'REMATA EL GERENTE DE ALIANZAS. Decir en voz alta: escaneen y envíen el mensaje tal como sale, sin borrarlo. El QR abre el WhatsApp del Gerente de Alianzas con el mensaje de la UTS y el código REF-UTS. Dejar la diapositiva proyectada hasta que escaneen. El bono se paga cuando el amigo paga la inicial y asiste a la clase 5. Ningún dato del amigo se pide en el salón: el estudiante le avisa y el amigo escribe.'

path = os.path.join(OUT, os.environ.get('SLIDES_OUT', 'SLIDES_COLEGIO_3.pptx')); prs.save(path); print('OK', path, os.path.getsize(path))
