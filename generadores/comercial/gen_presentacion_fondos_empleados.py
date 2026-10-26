# -*- coding: utf-8 -*-
"""Presentación para FONDOS DE EMPLEADOS — v3 (26/10/2026): estructura del analista financiero AL PIE DE LA LETRA
(1 portada · 2 somos Heiiu · 3 oferta Plan A · 4 valor económico · 5 beneficios · 6 llamado a la acción con fechas y cupos ·
7 cierre con pregunta) + lo que respalda la evidencia: una idea por diapositiva, titular como afirmación, poco texto,
"sin costo" en la portada, un solo pedido con fecha y hora. Guion de lo que se dice en las NOTAS de cada diapositiva.
Diseño v3: paleta azul tinta + crema + naranja de marca como acento; tipografías Lato (texto y titulares) y Oswald (cifras),
instaladas en este equipo; el PDF las lleva incrustadas (exportar siempre el PDF: topdf_fondos.ps1).
El detalle completo va en la hoja que se deja al final: gen_hoja_fondos_empleados.py.
Salida: recursos/comercial/B2B/PRESENTACION_FONDOS_EMPLEADOS_HEIIU.pptx"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

R = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
OUT = R + r'\recursos\comercial\B2B\PRESENTACION_FONDOS_EMPLEADOS_HEIIU.pptx'
LOGO_T = R + r'\recursos\marca heiiu\logo_heiiu_transparente.png'     # letras blancas y amarillas: solo sobre fondo oscuro
MINI = R + r'\recursos\comercial\B2B\_convenio_entidad_miniatura.png'
try:
    import fitz
    fitz.open(R + r'\recursos\comercial\B2B\CONVENIO_HEIIU_ENTIDAD_ALIADA_v1.pdf')[0].get_pixmap(dpi=110).save(MINI)
except Exception as e:
    print('miniatura no regenerada:', e)

# paleta v3
TINTA = RGBColor(0x0F, 0x1B, 0x2D)     # azul tinta (fondo oscuro y titulares)
TINTA2 = RGBColor(0x1B, 0x2A, 0x41)    # tarjetas sobre tinta
CREMA = RGBColor(0xF6, 0xF1, 0xE9)     # fondo claro
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
NAR = RGBColor(0xE5, 0x4C, 0x09)       # naranja de marca: acento
ORO = RGBColor(0xFB, 0xC9, 0x00)       # amarillo de marca: cifras sobre tinta
TEXTO = RGBColor(0x2B, 0x34, 0x45)
SUAVE = RGBColor(0x7A, 0x82, 0x8F)
BORDE = RGBColor(0xE3, 0xDB, 0xCF)
H = 'Lato'; HB = 'Lato Black'; NUM = 'Oswald'; B = 'Lato'
W, HH = Inches(13.333), Inches(7.5)

prs = Presentation(); prs.slide_width = W; prs.slide_height = HH
BLANK = prs.slide_layouts[6]


def rect(sl, x, y, w, h, fill, line=None, radius=None):
    s = sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, x, y, w, h)
    if radius: s.adjustments[0] = radius
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None: s.line.fill.background()
    else: s.line.color.rgb = line; s.line.width = Pt(0.75)
    s.shadow.inherit = False
    return s


def text(sl, x, y, w, h, parts, size=16, color=TEXTO, font=B, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, spacing=1.15, after=0, spc=None):
    tb = sl.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05); tf.margin_top = tf.margin_bottom = Inches(0.03)
    tf.vertical_anchor = anchor
    paras = parts if isinstance(parts, list) else [parts]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.line_spacing = spacing; p.space_after = Pt(after)
        runs = para if isinstance(para, list) else [(para, {})]
        for txt, st in runs:
            r = p.add_run(); r.text = txt
            r.font.name = st.get('font', font); r.font.size = Pt(st.get('size', size))
            r.font.bold = st.get('bold', bold); r.font.italic = st.get('italic', False)
            r.font.color.rgb = st.get('color', color)
            if spc or st.get('spc'): r._r.get_or_add_rPr().set('spc', str(st.get('spc', spc)))
    return tb


def notas(sl, txt): sl.notes_slide.notes_text_frame.text = txt


def logo_pill(sl, x, y, h=Inches(0.62), fill=TINTA):
    """Logo (letras blancas) dentro de una pastilla azul tinta, para fondos claros."""
    w = Inches(1.55)
    rect(sl, x, y, w, h, fill, radius=0.5)
    sl.shapes.add_picture(LOGO_T, x + Inches(0.2), y + Inches(0.08), height=h - Inches(0.16))


def marco(n, overline, titulo, dark=False, title_w=Inches(7.6)):
    sl = prs.slides.add_slide(BLANK)
    rect(sl, 0, 0, W, HH, TINTA if dark else CREMA)
    logo_pill(sl, Inches(0.6), Inches(0.42), fill=TINTA2 if dark else TINTA)
    text(sl, Inches(10.3), Inches(0.42), Inches(2.5), Inches(0.62), f'{n} / 7', size=12, color=SUAVE if not dark else RGBColor(0x9A, 0xA4, 0xB5),
         align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE, font=NUM)
    text(sl, Inches(0.6), Inches(1.35), Inches(8), Inches(0.35), overline.upper(), size=11, color=NAR, bold=True, spc=250)
    text(sl, Inches(0.6), Inches(1.7), title_w, Inches(1.9), titulo, size=34, font=HB, bold=True,
         color=CREMA if dark else TINTA, anchor=MSO_ANCHOR.TOP, spacing=1.08)
    text(sl, Inches(0.6), Inches(7.0), Inches(12.2), Inches(0.35), 'Heiiu English Academy · Línea de alianzas 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga',
         size=9.5, color=RGBColor(0x9A, 0xA4, 0xB5) if dark else SUAVE, anchor=MSO_ANCHOR.MIDDLE)
    return sl


def viñetas(sl, x, y, w, h, items, size=17, color=TEXTO, dot=NAR, gap=9):
    paras = [[('—  ', dict(color=dot, bold=True)), (b, dict(bold=True, color=color)), (r, {})] for b, r in items]
    return text(sl, x, y, w, h, paras, size=size, color=color, after=gap, spacing=1.18)


def panel_cifra(sl, cifra, sub, x=Inches(8.9), y=Inches(1.35), w=Inches(3.85), h=Inches(5.3), size=66):
    rect(sl, x, y, w, h, TINTA, radius=0.06)
    rect(sl, x + Inches(0.35), y + Inches(0.35), Inches(0.6), Emu(30000), NAR)
    text(sl, x + Inches(0.25), y + Inches(0.7), w - Inches(0.5), Inches(2.4), cifra, size=size, font=NUM, color=ORO,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    text(sl, x + Inches(0.35), y + Inches(3.2), w - Inches(0.7), h - Inches(3.4), sub, size=15, color=CREMA, spacing=1.25)


# ================================================================ 1. PORTADA
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, HH, TINTA)
rect(sl, Inches(9.6), 0, Inches(3.733), HH, TINTA2)
rect(sl, Inches(9.6), 0, Emu(60000), HH, NAR)
sl.shapes.add_picture(LOGO_T, Inches(0.6), Inches(0.55), height=Inches(1.25))
text(sl, Inches(0.6), Inches(2.35), Inches(8.6), Inches(0.35), 'PROGRAMA DE INGLÉS PARA FONDOS DE EMPLEADOS', size=11, color=NAR, bold=True, spc=250)
text(sl, Inches(0.6), Inches(2.75), Inches(8.7), Inches(2.6),
     [[('Beca del 45% en inglés para sus afiliados y sus familias, ', dict(color=CREMA)), ('sin costo para el fondo.', dict(color=ORO))]],
     size=42, font=HB, bold=True, spacing=1.06)
text(sl, Inches(0.6), Inches(5.45), Inches(8.4), Inches(0.8), 'Programa presencial de A1 a B2 en Bucaramanga, con garantía de aprendizaje por escrito.',
     size=18, color=RGBColor(0xC9, 0xD0, 0xDB), spacing=1.2)
text(sl, Inches(0.6), Inches(6.45), Inches(8.4), Inches(0.6),
     [[('Presentación para  ', dict(color=SUAVE)), ('_______________________________', dict(color=RGBColor(0x9A, 0xA4, 0xB5))),
       ('     Bucaramanga, octubre de 2026', dict(color=SUAVE))]], size=13)
text(sl, Inches(9.95), Inches(2.3), Inches(3.1), Inches(1.2), '45%', size=96, font=NUM, color=ORO, anchor=MSO_ANCHOR.MIDDLE)
text(sl, Inches(9.95), Inches(3.55), Inches(3.1), Inches(1.0), 'de beca sobre el programa completo, a nombre del fondo', size=15, color=CREMA, spacing=1.2)
text(sl, Inches(9.95), Inches(4.75), Inches(3.1), Inches(1.0), '$0', size=72, font=NUM, color=CREMA, anchor=MSO_ANCHOR.MIDDLE)
text(sl, Inches(9.95), Inches(5.8), Inches(3.1), Inches(0.9), 'de costo para el fondo. Una hoja, 12 meses.', size=15, color=CREMA, spacing=1.2)
notas(sl, 'ANTES DE EMPEZAR (una pregunta): "¿Un convenio así lo firma usted o lo lleva a junta? ¿Cuándo se reúne la junta?" '
          'Con esa respuesta sabes si hoy sales con firma o con fecha de junta.\n'
          'QUÉ DECIR (20 segundos): "Vengo a proponerle un beneficio nuevo para sus afiliados que al fondo no le cuesta nada: beca del 45% '
          'en el programa de inglés de Heiiu, para ellos y sus familias, con el nombre del fondo. Le pido 10 minutos y salgo con una sola cosa: una fecha."\n'
          'NO leer la diapositiva. NO entregar la hoja todavía.')

# ================================================================ 2. SOMOS HEIIU
sl = marco(2, 'Somos Heiiu', 'Una academia presencial de Bucaramanga que responde por el resultado.', title_w=Inches(11))
tiles = [('2012', 'Licencia de la Secretaría de Educación desde 2012. Sede propia en Sotomayor.'),
         ('ISO 9001', 'Certificación de calidad ISO 9001 e ICONTEC.'),
         ('575 h', 'Un solo programa, completo: de A1 a B2, presencial, en grupos de máximo 16.'),
         ('100%', 'Nuestro logro: la garantía por escrito. Si el estudiante cumple y no avanza, le devolvemos el 100% del nivel.')]
for i, (num, lab) in enumerate(tiles):
    x = Inches(0.6) + i * Inches(3.1); y = Inches(3.75)
    rect(sl, x, y, Inches(2.9), Inches(2.85), BLANCO, BORDE, radius=0.06)
    rect(sl, x + Inches(0.3), y + Inches(0.3), Inches(0.5), Emu(30000), NAR)
    text(sl, x + Inches(0.25), y + Inches(0.5), Inches(2.5), Inches(1.0), num, size=44, font=NUM, color=TINTA, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, x + Inches(0.3), y + Inches(1.55), Inches(2.35), Inches(1.25), lab, size=13, color=TEXTO, spacing=1.2)
notas(sl, 'QUÉ DECIR (máximo 20 segundos, no más): "Somos una academia de Bucaramanga con licencia de la Secretaría de Educación desde 2012 '
          'y certificación ISO 9001 e ICONTEC. Un solo programa, de A1 a B2, presencial. Y lo que ninguna otra firma: la garantía por escrito." '
          'El detalle está en la hoja que se deja al final. Hablar de la academia más de 2 minutos baja el cierre.')

# ================================================================ 3. OFERTA EDUCATIVA (PLAN A)
sl = marco(3, 'Oferta educativa · Plan A', 'Programa completo de inglés, de A1 a B2: 575 horas presenciales.', title_w=Inches(11))
items = [('HORARIOS', 'Mañana 8:00 a 12:00 · Noche 6:30 a 8:30 p. m. · Sábados 8:00 a 12:00. Con 8 o más afiliados, el horario lo define el fondo.'),
         ('INTENSIDAD', '20 h por semana (unos 7 meses) o 10 h por semana (unos 14 meses). Más un video corto en inglés cada día.'),
         ('DOCENTES', 'Profesores bilingües colombianos, uno por grupo de máximo 16, que trabajan como coach y corrigen en el momento.'),
         ('EVALUACIÓN', 'Prueba de entrada, evaluaciones por nivel y evaluador externo al cierre. El fondo recibe asistencia y cumplimiento; nunca notas.'),
         ('CERTIFICACIÓN', 'Certificado Heiiu por nivel y por programa completo, según la Secretaría de Educación. Certificado de beca a nombre del fondo.'),
         ('GARANTÍA', 'Si cumple su parte (asistencia 80%, tareas 90%, evaluaciones) y no avanza, le devolvemos el 100% del nivel. Por escrito.')]
for i, (tt, body) in enumerate(items):
    col, row = i % 3, i // 3
    x = Inches(0.6) + col * Inches(4.1); y = Inches(3.55) + row * Inches(1.7)
    rect(sl, x, y, Inches(0.5), Emu(30000), NAR)
    text(sl, x, y + Inches(0.12), Inches(3.8), Inches(0.35), tt, size=11, color=TINTA, bold=True, spc=200)
    text(sl, x, y + Inches(0.47), Inches(3.8), Inches(1.2), body, size=12.5, color=TEXTO, spacing=1.2)
notas(sl, 'QUÉ DECIR: "Es un programa completo, presencial, en nuestra sede, en la mañana o en la noche; con 8 afiliados o más, el horario lo pone el fondo. '
          'Un profesor por grupo de máximo 16, y evaluador externo al cierre de cada nivel. Y lo firmamos: si cumple y no avanza, devolvemos el nivel."\n'
          'NO leer las seis casillas. Si pregunta por una, responde en una frase: el detalle está en la hoja.')

# ================================================================ 4. VALOR ECONÓMICO
sl = marco(4, 'Oferta educativa · Valor económico', 'El afiliado paga la mitad por venir con carta del fondo.')
viñetas(sl, Inches(0.6), Inches(3.7), Inches(7.8), Inches(3.2), [
    ('De contado: $4.782.800 ', 'en lugar de $8.696.000 (beca del 45%). Crédito del fondo o cesantías cuentan como contado.'),
    ('A cuotas con la academia: $5.565.440 ', '(beca del 36%). Ejemplo: $1.113.088 hoy y 11 cuotas de $452.348.'),
    ('Beca con el nombre del fondo: ', '3 afiliados por trimestre reciben el 45% aunque paguen a cuotas, más los libros. Si todos cumplen, suben a 5.'),
], size=15)
panel_cifra(sl, '$3.913.200', 'menos por afiliado sobre el programa completo. Es beca del Fondo de Becas Heiiu, no un descuento: misma tarifa y misma garantía para todos.', size=48)
notas(sl, 'QUÉ DECIR: "El afiliado paga $4.782.800 por el programa que vale $8.696.000. Si el fondo le presta o paga con cesantías, es contado y recibe la beca mayor. '
          'Y tres afiliados por trimestre, los que el fondo elija, reciben la beca con el nombre del fondo aunque paguen a cuotas."\n'
          'Si el fondo quiere pagar los cupos: Plan Empresa, $4.782.800 por cupo de 3 a 7, $4.350.000 de 8 a 15, $3.950.000 de 16 a 30 (está en la hoja). '
          'NO recitar la tabla. "Beca", nunca "descuento".')

# ================================================================ 5. BENEFICIOS
sl = marco(5, 'Beneficios · ¿Qué gano yo?', 'El fondo gana un beneficio con su nombre. El afiliado gana un inglés que le sirve.', title_w=Inches(11.5))
for i, (hdr, lst) in enumerate([
        ('EL FONDO', [('Sin costo ni presupuesto. ', 'El fondo postula con una carta; no paga ni cobra nada.'),
                      ('Becas y certificados con su nombre, ', 'entregados en su propio evento.'),
                      ('Reporte de asistencia y cumplimiento ', 'de cada becado: el fondo ve quién cumple.'),
                      ('10 diagnósticos de nivel sin costo ', 'la semana siguiente a la firma.')]),
        ('EL AFILIADO Y SU FAMILIA', [('Paga la mitad, ', 'y la beca cubre también a su cónyuge y a sus hijos desde los 12 años.'),
                                     ('Gana cerca de un 26% más ', 'quien certifica su inglés, frente a quien hace el mismo trabajo sin él.¹'),
                                     ('Garantía por escrito: ', 'si cumple y no avanza, recibe el 100% del nivel de vuelta.'),
                                     ('No entrena solo: ', 'profesor que corrige ahí mismo, coach que no lo deja rendirse, y el video del primer día junto al del último.')])]):
    x = Inches(0.6) + i * Inches(6.2)
    rect(sl, x, Inches(3.55), Inches(5.9), Inches(3.3), BLANCO if i == 0 else TINTA, BORDE if i == 0 else None, radius=0.05)
    text(sl, x + Inches(0.35), Inches(3.75), Inches(5.2), Inches(0.35), hdr, size=11, color=NAR, bold=True, spc=200)
    viñetas(sl, x + Inches(0.3), Inches(4.15), Inches(5.3), Inches(2.7), lst, size=13, color=TEXTO if i == 0 else CREMA, gap=6)
text(sl, Inches(0.6), Inches(6.72), Inches(12), Inches(0.3), '¹ DNP, Archivos de Economía, Bilingüismo laboral en Colombia.', size=9, color=SUAVE)
notas(sl, 'QUÉ DECIR: "Para el fondo es un beneficio más en su portafolio, con su nombre y sin tocar presupuesto: usted postula con una carta y nosotros hacemos el resto. '
          'Para el afiliado es pagar la mitad, con garantía, y que lo acompañen hasta que hable." Decir UN dato, no todos.\n'
          'Si pregunta "¿y si nadie se inscribe?": "No le cuesta nada al fondo. Lo único que le pido es la charla de 20 minutos."')

# ================================================================ 6. LLAMADO A LA ACCIÓN
sl = marco(6, 'Llamado a la acción', 'El próximo grupo arranca el martes 3 de noviembre. Firmemos esta semana.', dark=True, title_w=Inches(11.5))
for i, (num, lab, body) in enumerate([
        ('3 NOV', 'INICIO', 'Martes 3 de noviembre de 2026. El grupo no para en diciembre: sigue hasta terminar el nivel, solo descansa los festivos.'),
        ('16', 'CUPOS POR GRUPO', 'Grupos de máximo 16, por orden de matrícula con la inicial pagada. Los que no entren ahora esperan al siguiente grupo.'),
        ('3', 'BECAS CON SU NOMBRE', 'Este trimestre, para los afiliados que el fondo elija. Si todos cumplen, suben a 5 el siguiente.')]):
    x = Inches(0.6) + i * Inches(4.1)
    rect(sl, x, Inches(3.55), Inches(3.85), Inches(3.1), TINTA2, radius=0.06)
    text(sl, x + Inches(0.3), Inches(3.65), Inches(3.3), Inches(1.0), num, size=50, font=NUM, color=ORO, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, x + Inches(0.3), Inches(4.65), Inches(3.3), Inches(0.3), lab, size=10.5, color=NAR, bold=True, spc=200)
    text(sl, x + Inches(0.3), Inches(5.0), Inches(3.3), Inches(1.6), body, size=13, color=CREMA, spacing=1.2)
notas(sl, 'QUÉ DECIR: "Le hablo hoy y no el mes entrante por una razón: el grupo arranca el martes 3 de noviembre y no para en diciembre. '
          'Si firmamos esta semana, sus afiliados alcanzan a entrar. El convenio no tiene costo ni obligaciones, se firma en una hoja, dura 12 meses '
          'y se termina con aviso de 30 días. Lo único que le pido es 20 minutos con sus afiliados."\n'
          'Decir solo cupos reales (grupos de 16, 3 becas con nombre). Nunca "últimos cupos" si no es cierto.')

# ================================================================ 7. CIERRE CON PREGUNTA
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, HH, TINTA)
sl.shapes.add_picture(LOGO_T, Inches(0.6), Inches(0.5), height=Inches(1.0))
text(sl, Inches(10.3), Inches(0.5), Inches(2.5), Inches(1.0), '7 / 7', size=12, color=RGBColor(0x9A, 0xA4, 0xB5), align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE, font=NUM)
text(sl, Inches(0.6), Inches(1.9), Inches(8.3), Inches(0.35), 'UN SOLO PASO', size=11, color=NAR, bold=True, spc=250)
text(sl, Inches(0.6), Inches(2.3), Inches(8.3), Inches(2.2),
     [[('¿Cuántos de sus afiliados quiere ver hablando inglés ', dict(color=CREMA)), ('el próximo año?', dict(color=ORO))]],
     size=38, font=HB, bold=True, spacing=1.06)
rect(sl, Inches(0.6), Inches(4.65), Inches(8.3), Inches(1.15), NAR, radius=0.3)
text(sl, Inches(0.85), Inches(4.65), Inches(7.9), Inches(1.15),
     [[('Firmamos hoy y la charla de 20 minutos la hacemos el ', {}), ('_______', dict(color=ORO)), (' a las ', {}), ('_____', dict(color=ORO)),
       (' o el ', {}), ('_______', dict(color=ORO)), (' a las ', {}), ('_____', dict(color=ORO)), ('.', {})]],
     size=19, color=BLANCO, bold=True, anchor=MSO_ANCHOR.MIDDLE, spacing=1.2)
text(sl, Inches(0.6), Inches(5.95), Inches(8.3), Inches(0.9),
     [[('Si va a junta: ', dict(bold=True, color=ORO)), ('¿cuándo se reúne? Le dejo el convenio listo para esa fecha.', dict(color=CREMA))],
      [('Una hoja · sin costo · 12 meses · se termina con aviso de 30 días.', dict(color=RGBColor(0x9A, 0xA4, 0xB5), size=13))]], size=16, spacing=1.25, after=4)
rect(sl, Inches(9.55), Inches(1.75), Inches(3.3), Inches(4.45), BLANCO, radius=0.02)
sl.shapes.add_picture(MINI, Inches(9.62), Inches(1.82), height=Inches(4.31))
text(sl, Inches(9.55), Inches(6.3), Inches(3.3), Inches(0.4), 'El convenio: una hoja', size=11, color=RGBColor(0x9A, 0xA4, 0xB5), align=PP_ALIGN.CENTER)
text(sl, Inches(0.6), Inches(7.0), Inches(12.2), Inches(0.35), 'Heiiu English Academy · Global Teacher S.A.S. · Línea de alianzas 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga · @Heiiu_english',
     size=9.5, color=RGBColor(0x9A, 0xA4, 0xB5), anchor=MSO_ANCHOR.MIDDLE)
notas(sl, 'QUÉ DECIR: "¿Cuántos de sus afiliados quiere ver hablando inglés el próximo año? Dígame cuántos y hoy mismo definimos a quiénes. '
          'Le pido una sola cosa: que firmemos hoy este convenio de una página y me dé fecha y hora para la charla. ¿La hacemos el [día] a las [hora] o el [día] a las [hora]?" '
          'Y SILENCIO. Que responda él.\n'
          'Si debe ir a junta: "¿Cuándo se reúne? Le dejo el convenio y la hoja listos para esa fecha, y lo llamo al día siguiente."\n'
          'AL FINAL, no antes: entregar la hoja de detalle impresa y el convenio en dos copias. Lo que cuenta para el tablero: convenio firmado con fecha de charla, o fecha de junta anotada.')

try:
    prs.save(OUT); print('OK', OUT)
except PermissionError:
    OUT = OUT.replace('.pptx', '_v2.pptx'); prs.save(OUT); print('ABIERTO -> _v2', OUT)
