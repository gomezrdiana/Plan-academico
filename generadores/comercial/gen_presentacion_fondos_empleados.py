# -*- coding: utf-8 -*-
"""Presentación para FONDOS DE EMPLEADOS — v4 (26/10/2026): estructura del analista financiero AL PIE DE LA LETRA
(1 portada · 2 somos Heiiu · 3 oferta Plan A · 4 valor económico · 5 beneficios · 6 llamado a la acción con fechas y cupos ·
7 cierre con pregunta) con lo que respalda la evidencia: una idea por diapositiva, titular como afirmación, POCAS PALABRAS
(máximo tres líneas cortas por diapositiva; el detalle va en la hoja que se deja al final: gen_hoja_fondos_empleados.py),
"sin costo" en la portada y un solo pedido con fecha y hora. Guion de lo que se dice en las NOTAS de cada diapositiva.
Diseño v4: naranja claro + crema + café oscuro, con el naranja de marca como acento; tipografías Lato y Oswald (instaladas aquí;
el PDF las lleva incrustadas: exportar siempre con topdf_fondos.ps1 y presentar desde el PDF en otro equipo).
Salida: recursos/comercial/B2B/PRESENTACION_FONDOS_EMPLEADOS_HEIIU.pptx"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

R = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
OUT = R + r'\recursos\comercial\B2B\PRESENTACION_FONDOS_EMPLEADOS_HEIIU.pptx'
LOGO_T = R + r'\recursos\marca heiiu\logo_heiiu_transparente.png'     # letras blancas y amarillas: solo sobre fondo de color
MINI = R + r'\recursos\comercial\B2B\_convenio_entidad_miniatura.png'
try:
    import fitz
    fitz.open(R + r'\recursos\comercial\B2B\CONVENIO_HEIIU_ENTIDAD_ALIADA_v1.pdf')[0].get_pixmap(dpi=110).save(MINI)
except Exception as e:
    print('miniatura no regenerada:', e)

# paleta v4 (más clara que la v3)
AZUL = RGBColor(0xF3, 0x9A, 0x55)      # NARANJA CLARO (decisión de gerencia 26/10): fondos de portada, llamado a la acción y cierre
AZUL2 = RGBColor(0xFF, 0xFF, 0xFF)     # tarjetas sobre naranja claro: blancas
AZULT = RGBColor(0x3B, 0x2A, 0x20)     # café oscuro: titulares sobre crema y sobre naranja claro
CELESTE = RGBColor(0xFD, 0xE9, 0xD8)   # tarjetas suaves sobre crema
CREMA = RGBColor(0xFB, 0xF5, 0xEE)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
NAR = RGBColor(0xE5, 0x4C, 0x09)       # naranja de marca: acento
ORO = RGBColor(0xFB, 0xC9, 0x00)       # amarillo de marca: cifras sobre azul
TEXTO = RGBColor(0x2B, 0x34, 0x45)
SUAVE = RGBColor(0x7A, 0x82, 0x8F)
CLARO = RGBColor(0x6B, 0x4A, 0x33)     # café suave: texto secundario sobre naranja claro
BORDE = RGBColor(0xF0, 0xDC, 0xC8)
HB = 'Lato Black'; NUM = 'Oswald'; B = 'Lato'
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


def logo_pill(sl, x, y, h=Inches(0.62), fill=NAR):
    w = int((h - Inches(0.16)) * 1.78 + Inches(0.4))   # ancho del logo (proporción 2454x1380) más márgenes
    rect(sl, x, y, w, h, fill, radius=0.5)
    sl.shapes.add_picture(LOGO_T, x + Inches(0.2), y + Inches(0.08), height=h - Inches(0.16))


def marco(n, overline, titulo, dark=False, title_w=Inches(11.5)):
    sl = prs.slides.add_slide(BLANK)
    rect(sl, 0, 0, W, HH, AZUL if dark else CREMA)
    logo_pill(sl, Inches(0.6), Inches(0.42))
    text(sl, Inches(10.3), Inches(0.42), Inches(2.5), Inches(0.62), f'{n} / 7', size=12, color=CLARO if dark else SUAVE,
         align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE, font=NUM)
    text(sl, Inches(0.6), Inches(1.4), Inches(8), Inches(0.35), overline.upper(), size=11, color=AZULT if dark else NAR, bold=True, spc=250)
    text(sl, Inches(0.6), Inches(1.75), title_w, Inches(1.8), titulo, size=36, font=HB, bold=True,
         color=AZULT, anchor=MSO_ANCHOR.TOP, spacing=1.08)
    text(sl, Inches(0.6), Inches(7.0), Inches(12.2), Inches(0.35), 'Heiiu English Academy · Línea de alianzas 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga',
         size=9.5, color=CLARO if dark else SUAVE, anchor=MSO_ANCHOR.MIDDLE)
    return sl


def lineas(sl, x, y, w, h, items, size=20, color=TEXTO, dot=NAR, gap=12):
    paras = [[('—  ', dict(color=dot, bold=True)), (t, {})] for t in items]
    return text(sl, x, y, w, h, paras, size=size, color=color, after=gap, spacing=1.2)


# ================================================================ 1. PORTADA
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, HH, AZUL)
rect(sl, Inches(9.6), 0, Inches(3.733), HH, AZUL2)
rect(sl, Inches(9.6), 0, Emu(60000), HH, NAR)
logo_pill(sl, Inches(0.6), Inches(0.55), h=Inches(1.0))
text(sl, Inches(0.6), Inches(2.35), Inches(8.6), Inches(0.35), 'PROGRAMA DE INGLÉS PARA FONDOS DE EMPLEADOS', size=11, color=AZULT, bold=True, spc=250)
text(sl, Inches(0.6), Inches(2.75), Inches(8.7), Inches(2.6),
     [[('Beca del 45% en inglés para sus afiliados y sus familias, ', dict(color=AZULT)), ('sin costo para el fondo.', dict(color=BLANCO))]],
     size=42, font=HB, bold=True, spacing=1.06)
text(sl, Inches(0.6), Inches(5.45), Inches(8.4), Inches(0.8), 'Presencial, en Bucaramanga. Con garantía de aprendizaje por escrito.',
     size=18, color=CLARO, spacing=1.2)
text(sl, Inches(0.6), Inches(6.45), Inches(8.4), Inches(0.6),
     [[('Presentación para  ', dict(color=CLARO)), ('_______________________________', dict(color=CLARO)),
       ('     Bucaramanga, octubre de 2026', dict(color=CLARO))]], size=13)
text(sl, Inches(9.95), Inches(2.3), Inches(3.1), Inches(1.2), '45%', size=96, font=NUM, color=NAR, anchor=MSO_ANCHOR.MIDDLE)
text(sl, Inches(9.95), Inches(3.55), Inches(3.1), Inches(0.9), 'de beca, a nombre del fondo', size=15, color=AZULT, spacing=1.2)
text(sl, Inches(9.95), Inches(4.75), Inches(3.1), Inches(1.0), '$0', size=72, font=NUM, color=NAR, anchor=MSO_ANCHOR.MIDDLE)
text(sl, Inches(9.95), Inches(5.8), Inches(3.1), Inches(0.9), 'para el fondo. Una hoja, 12 meses.', size=15, color=AZULT, spacing=1.2)
notas(sl, 'ANTES DE EMPEZAR (una pregunta): "¿Un convenio así lo firma usted o lo lleva a junta? ¿Cuándo se reúne la junta?" '
          'Con esa respuesta sabes si hoy sales con firma o con fecha de junta.\n'
          'QUÉ DECIR (20 segundos): "Vengo a proponerle un beneficio nuevo para sus afiliados que al fondo no le cuesta nada: beca del 45% '
          'en el programa de inglés de Heiiu, para ellos y sus familias, con el nombre del fondo. Le pido 10 minutos y salgo con una sola cosa: una fecha."\n'
          'NO leer la diapositiva. NO entregar la hoja todavía.')

# ================================================================ 2. SOMOS HEIIU
sl = marco(2, 'Somos Heiiu', 'Una academia de Bucaramanga que responde por el resultado.')
for i, (num, lab) in enumerate([('2012', 'Licencia de la Secretaría de Educación'), ('ISO 9001', 'Certificación ISO e ICONTEC'),
                                ('575 h', 'De A1 a B2, presencial y certificado'), ('100%', 'Garantía por escrito: devolvemos el nivel')]):
    x = Inches(0.6) + i * Inches(3.1); y = Inches(3.75)
    rect(sl, x, y, Inches(2.9), Inches(2.6), BLANCO, BORDE, radius=0.06)
    rect(sl, x + Inches(0.3), y + Inches(0.3), Inches(0.5), Emu(30000), NAR)
    text(sl, x + Inches(0.25), y + Inches(0.5), Inches(2.5), Inches(1.0), num, size=46, font=NUM, color=AZULT, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, x + Inches(0.3), y + Inches(1.6), Inches(2.35), Inches(0.9), lab, size=14, color=TEXTO, spacing=1.2)
notas(sl, 'QUÉ DECIR (máximo 20 segundos): "Somos una academia de Bucaramanga con licencia de la Secretaría de Educación desde 2012 '
          'y certificación ISO 9001 e ICONTEC. Un solo programa, de A1 a B2, presencial. Y lo que ninguna otra firma: la garantía por escrito." '
          'El detalle está en la hoja que se deja al final. Hablar de la academia más de 2 minutos baja el cierre.')

# ================================================================ 3. OFERTA EDUCATIVA (PLAN A)
sl = marco(3, 'Oferta educativa · Plan A', 'Programa completo de A1 a B2: 575 horas presenciales.')
for i, (tt, body) in enumerate([('HORARIOS', 'Mañana, noche o sábados'), ('INTENSIDAD', '20 h o 10 h por semana, más un video diario'),
                                ('DOCENTES', 'Bilingües, trabajan como coach'), ('EVALUACIÓN', 'Entrada, por nivel y evaluador externo'),
                                ('CERTIFICACIÓN', 'Por nivel y por programa completo'), ('GARANTÍA', 'Cumple y no avanza: devolvemos el 100%')]):
    col, row = i % 3, i // 3
    x = Inches(0.6) + col * Inches(4.1); y = Inches(3.7) + row * Inches(1.55)
    rect(sl, x, y, Inches(0.5), Emu(30000), NAR)
    text(sl, x, y + Inches(0.12), Inches(3.8), Inches(0.35), tt, size=11, color=AZULT, bold=True, spc=200)
    text(sl, x, y + Inches(0.47), Inches(3.8), Inches(0.9), body, size=17, color=TEXTO, spacing=1.15)
notas(sl, 'QUÉ DECIR: "Programa completo, presencial, en la mañana o en la noche; con 8 afiliados o más, el horario lo pone el fondo. '
          'Profesores que trabajan como coach y evaluador externo al cierre de cada nivel. Y lo firmamos: si cumple y no avanza, devolvemos el nivel."\n'
          'Horarios exactos: mañana 8:00 a 12:00, noche 6:30 a 8:30 p. m., sábados 8:00 a 12:00. Todo está en la hoja; no leer las seis casillas.')

# ================================================================ 4. VALOR ECONÓMICO
sl = marco(4, 'Oferta educativa · Valor económico', 'El afiliado paga la mitad por venir con carta del fondo.', title_w=Inches(7.8))
lineas(sl, Inches(0.6), Inches(3.8), Inches(7.8), Inches(3.0), [
    '$4.782.800 de contado, en lugar de $8.696.000.',
    'Crédito del fondo o cesantías cuentan como contado.',
    '3 becas por trimestre con el nombre del fondo.'], size=20)
x, y, w, h = Inches(8.9), Inches(1.4), Inches(3.85), Inches(5.25)
rect(sl, x, y, w, h, AZUL, radius=0.06)
rect(sl, x + Inches(0.35), y + Inches(0.35), Inches(0.6), Emu(30000), AZULT)
text(sl, x + Inches(0.25), y + Inches(0.7), w - Inches(0.5), Inches(2.4), '$3.913.200', size=48, font=NUM, color=AZULT, anchor=MSO_ANCHOR.MIDDLE)
text(sl, x + Inches(0.35), y + Inches(3.2), w - Inches(0.7), Inches(1.9), 'menos por afiliado. Beca, no descuento: misma tarifa y misma garantía para todos.', size=15, color=AZULT, spacing=1.25)
notas(sl, 'QUÉ DECIR: "El afiliado paga $4.782.800 por el programa que vale $8.696.000. Si el fondo le presta o paga con cesantías, es contado y recibe la beca mayor. '
          'Y tres afiliados por trimestre, los que el fondo elija, reciben la beca con el nombre del fondo aunque paguen a cuotas."\n'
          'A cuotas con la academia: $5.565.440 (36%); ejemplo $1.113.088 hoy y 11 cuotas de $452.348. Plan Empresa si el fondo paga los cupos: '
          '$4.782.800 por cupo de 3 a 7, $4.350.000 de 8 a 15, $3.950.000 de 16 a 30. Todo en la hoja. "Beca", nunca "descuento".')

# ================================================================ 5. BENEFICIOS
sl = marco(5, 'Beneficios · ¿Qué gano yo?', 'El fondo gana un beneficio con su nombre. El afiliado, un inglés que le sirve.')
for i, (hdr, lst) in enumerate([('EL FONDO', ['Sin costo ni presupuesto', 'Becas y certificados con su nombre', 'Reporte: ve quién cumple']),
                                ('EL AFILIADO Y SU FAMILIA', ['Paga la mitad, también cónyuge e hijos', 'Garantía: si cumple y no avanza, 100% de vuelta', 'Nadie entrena solo: coach y video diario'])]):
    x = Inches(0.6) + i * Inches(6.2)
    rect(sl, x, Inches(3.7), Inches(5.9), Inches(2.95), BLANCO if i == 0 else AZUL, BORDE if i == 0 else None, radius=0.05)
    text(sl, x + Inches(0.35), Inches(3.9), Inches(5.2), Inches(0.35), hdr, size=11, color=NAR if i == 0 else AZULT, bold=True, spc=200)
    lineas(sl, x + Inches(0.3), Inches(4.35), Inches(5.3), Inches(2.3), lst, size=18, color=TEXTO if i == 0 else AZULT, dot=NAR if i == 0 else BLANCO, gap=8)
notas(sl, 'QUÉ DECIR: "Para el fondo es un beneficio más en su portafolio, con su nombre y sin tocar presupuesto: usted postula con una carta y nosotros hacemos el resto. '
          'Para el afiliado es pagar la mitad, con garantía, y que lo acompañen hasta que hable." UN dato si hace falta: quien certifica su inglés gana cerca de un 26% más (DNP). '
          'Diagnóstico de nivel para 10 afiliados sin costo la semana siguiente a la firma.\n'
          'Si pregunta "¿y si nadie se inscribe?": "No le cuesta nada al fondo. Lo único que le pido es la charla de 20 minutos."')

# ================================================================ 6. LLAMADO A LA ACCIÓN
sl = marco(6, 'Llamado a la acción', 'El próximo grupo arranca el martes 3 de noviembre. Firmemos esta semana.', dark=True)
for i, (num, lab, body) in enumerate([('3 NOV', 'INICIO', 'Y no para en diciembre.'),
                                      ('16', 'CUPOS POR GRUPO', 'Por orden de matrícula.'),
                                      ('3', 'BECAS CON SU NOMBRE', 'Este trimestre. Suben a 5.')]):
    x = Inches(0.6) + i * Inches(4.1)
    rect(sl, x, Inches(3.7), Inches(3.85), Inches(2.8), AZUL2, radius=0.06)
    text(sl, x + Inches(0.3), Inches(3.8), Inches(3.3), Inches(1.0), num, size=54, font=NUM, color=NAR, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, x + Inches(0.3), Inches(4.85), Inches(3.3), Inches(0.3), lab, size=10.5, color=AZULT, bold=True, spc=200)
    text(sl, x + Inches(0.3), Inches(5.2), Inches(3.3), Inches(1.1), body, size=17, color=TEXTO, spacing=1.2)
notas(sl, 'QUÉ DECIR: "Le hablo hoy y no el mes entrante por una razón: el grupo arranca el martes 3 de noviembre y no para en diciembre; solo descansa los festivos. '
          'Si firmamos esta semana, sus afiliados alcanzan a entrar. El convenio no tiene costo ni obligaciones, se firma en una hoja, dura 12 meses '
          'y se termina con aviso de 30 días. Lo único que le pido es 20 minutos con sus afiliados."\n'
          'Decir solo cupos reales (3 becas con nombre). Nunca "últimos cupos" si no es cierto.')

# ================================================================ 7. CIERRE CON PREGUNTA
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, HH, AZUL)
logo_pill(sl, Inches(0.6), Inches(0.5), h=Inches(0.8))
text(sl, Inches(10.3), Inches(0.5), Inches(2.5), Inches(0.8), '7 / 7', size=12, color=CLARO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE, font=NUM)
text(sl, Inches(0.6), Inches(1.9), Inches(8.3), Inches(0.35), 'UN SOLO PASO', size=11, color=AZULT, bold=True, spc=250)
text(sl, Inches(0.6), Inches(2.3), Inches(8.3), Inches(2.2),
     [[('¿Cuántos de sus afiliados quiere ver hablando inglés ', dict(color=AZULT)), ('el próximo año?', dict(color=BLANCO))]],
     size=38, font=HB, bold=True, spacing=1.06)
rect(sl, Inches(0.6), Inches(4.65), Inches(8.3), Inches(1.15), NAR, radius=0.3)
text(sl, Inches(0.85), Inches(4.65), Inches(7.9), Inches(1.15),
     [[('Firmamos hoy. ¿La charla la hacemos el ', {}), ('_______', dict(color=ORO)), (' a las ', {}), ('_____', dict(color=ORO)),
       (' o el ', {}), ('_______', dict(color=ORO)), (' a las ', {}), ('_____', dict(color=ORO)), ('?', {})]],
     size=19, color=BLANCO, bold=True, anchor=MSO_ANCHOR.MIDDLE, spacing=1.2)
text(sl, Inches(0.6), Inches(5.95), Inches(8.3), Inches(0.9),
     [[('Si va a junta: ', dict(bold=True, color=AZULT)), ('¿cuándo se reúne? Le dejo el convenio listo.', dict(color=AZULT))],
      [('Una hoja · sin costo · 12 meses · se termina con aviso de 30 días.', dict(color=CLARO, size=13))]], size=16, spacing=1.25, after=4)
rect(sl, Inches(9.55), Inches(1.75), Inches(3.3), Inches(4.45), BLANCO, radius=0.02)
sl.shapes.add_picture(MINI, Inches(9.62), Inches(1.82), height=Inches(4.31))
text(sl, Inches(9.55), Inches(6.3), Inches(3.3), Inches(0.4), 'El convenio: una hoja', size=11, color=CLARO, align=PP_ALIGN.CENTER)
text(sl, Inches(0.6), Inches(7.0), Inches(12.2), Inches(0.35), 'Heiiu English Academy · Global Teacher S.A.S. · Línea de alianzas 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga · @Heiiu_english',
     size=9.5, color=CLARO, anchor=MSO_ANCHOR.MIDDLE)
notas(sl, 'QUÉ DECIR: "¿Cuántos de sus afiliados quiere ver hablando inglés el próximo año? Dígame cuántos y hoy mismo definimos a quiénes. '
          'Le pido una sola cosa: que firmemos hoy este convenio de una página y me dé fecha y hora para la charla. ¿La hacemos el [día] a las [hora] o el [día] a las [hora]?" '
          'Y SILENCIO. Que responda él.\n'
          'Si debe ir a junta: "¿Cuándo se reúne? Le dejo el convenio y la hoja listos para esa fecha, y lo llamo al día siguiente."\n'
          'AL FINAL, no antes: entregar la hoja de detalle impresa y el convenio en dos copias. Lo que cuenta para el tablero: convenio firmado con fecha de charla, o fecha de junta anotada.')

try:
    prs.save(OUT); print('OK', OUT)
except PermissionError:
    OUT = OUT.replace('.pptx', '_v2.pptx'); prs.save(OUT); print('ABIERTO -> _v2', OUT)
