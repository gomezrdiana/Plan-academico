# -*- coding: utf-8 -*-
"""Presentación para FONDOS DE EMPLEADOS (estructura del analista financiero, 26/10/2026):
1 Portada · 2 Somos Heiiu · 3 Oferta educativa (Plan A) + valor económico · 4 Beneficios ("qué gano yo") · 5 Llamado a la acción · 6 Cierre con pregunta.
Contenido tomado de las piezas de empresas (gen_piezas_conciencia), el convenio Business Partner, la hoja de cierre a cuotas y la hoja de cliente.
Reglas: sin nativos, sin "gratis"/"patrocinio", sin nombres de competidores ni de entidades, sin empleo/visa, "beca, no descuento",
nada en construcción (portafolio, hoja de vida, LinkedIn, módulos de empleabilidad), teléfono de alianzas 316 768 8793.
Salida: recursos/comercial/B2B/PRESENTACION_FONDOS_EMPLEADOS_HEIIU.pptx (el PDF lo exporta PowerPoint por COM, ver topdf_fondos.ps1)."""
import os, shutil
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

R = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
OUT = R + r'\recursos\comercial\B2B\PRESENTACION_FONDOS_EMPLEADOS_HEIIU.pptx'
JOHN = R + r'\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza'
LOGO_T = R + r'\recursos\marca heiiu\logo_heiiu_transparente.png'
LOGO_N = R + r'\recursos\marca heiiu\logo_heiiu_sobre_naranja.png'

OSCURO = RGBColor(0x1C, 0x17, 0x14); NAR = RGBColor(0xE5, 0x4C, 0x09); NAR2 = RGBColor(0xFF, 0x4A, 0x00)
AMA = RGBColor(0xFB, 0xC9, 0x00); CREMA = RGBColor(0xFF, 0xF8, 0xE7); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
GRIS = RGBColor(0x5A, 0x5A, 0x5A); NEGRO = RGBColor(0x22, 0x22, 0x22); LINEA = RGBColor(0xF0, 0xD9, 0xC8)
TIT = 'Constantia'; CUERPO = 'Segoe UI'
W, H = Inches(13.333), Inches(7.5)

prs = Presentation(); prs.slide_width = W; prs.slide_height = H
BLANK = prs.slide_layouts[6]


def rect(sl, x, y, w, h, fill, line=None):
    s = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None: s.line.fill.background()
    else: s.line.color.rgb = line; s.line.width = Pt(1)
    s.shadow.inherit = False
    return s


def text(sl, x, y, w, h, parts, size=16, color=NEGRO, font=CUERPO, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, spacing=1.15, after=0):
    """parts: str, o lista de párrafos; cada párrafo = str o lista de (texto, dict(bold/color/size/italic/font))."""
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
    return tb


def bullets(sl, x, y, w, h, items, size=15, color=NEGRO, gap=7, bcolor=NAR):
    """items: lista de (negrita, resto)."""
    paras = []
    for b, rest in items:
        paras.append([('▪ ', dict(color=bcolor, bold=True)), (b, dict(bold=True)), (rest, {})])
    return text(sl, x, y, w, h, paras, size=size, color=color, after=gap, spacing=1.12)


def header(sl, label, title, dark=False):
    """Banda superior naranja con la etiqueta de la sección y el título grande."""
    bg = OSCURO if dark else CREMA
    rect(sl, 0, 0, W, H, bg)
    rect(sl, 0, 0, W, Inches(0.42), NAR2)
    text(sl, Inches(0.55), Inches(0.04), Inches(9), Inches(0.36), label, size=12, color=BLANCO, bold=True,
         anchor=MSO_ANCHOR.MIDDLE)
    text(sl, Inches(10.2), Inches(0.04), Inches(2.6), Inches(0.36), 'HEIIU ENGLISH ACADEMY', size=11, color=BLANCO,
         bold=True, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, Inches(0.55), Inches(0.6), Inches(12.2), Inches(1.15), title, size=32, font=TIT, bold=True,
         color=BLANCO if dark else NAR, anchor=MSO_ANCHOR.MIDDLE, spacing=1.05)
    rect(sl, Inches(0.6), Inches(1.78), Inches(1.6), Emu(38000), AMA)


def footer(sl, txt, dark=False):
    text(sl, Inches(0.55), Inches(6.95), Inches(12.2), Inches(0.4), txt, size=10,
         color=RGBColor(0xC9, 0xB8, 0xA3) if dark else GRIS, anchor=MSO_ANCHOR.MIDDLE)


def card(sl, x, y, w, h, titulo, cuerpo, size=13, tcolor=NAR, fill=BLANCO):
    rect(sl, x, y, w, h, fill, LINEA)
    text(sl, x + Inches(0.18), y + Inches(0.12), w - Inches(0.36), Inches(0.45), titulo, size=13, bold=True, color=tcolor)
    text(sl, x + Inches(0.18), y + Inches(0.55), w - Inches(0.36), h - Inches(0.65), cuerpo, size=size, color=NEGRO, spacing=1.12)


# ---------------------------------------------------------------- 1. PORTADA
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, OSCURO)
rect(sl, 0, Inches(6.1), W, Inches(1.4), NAR2)
sl.shapes.add_picture(LOGO_T, Inches(0.5), Inches(0.35), height=Inches(1.6))
text(sl, Inches(0.6), Inches(2.1), Inches(12), Inches(0.5), 'PROGRAMA DE INGLÉS PARA FONDOS DE EMPLEADOS', size=14,
     color=AMA, bold=True)
text(sl, Inches(0.6), Inches(2.6), Inches(12.2), Inches(2.2),
     [[('Las otras academias le prometen inglés. ', dict(color=BLANCO)),
       ('Nosotros le devolvemos un mejor afiliado.', dict(color=AMA, italic=True))]],
     size=40, font=TIT, bold=True, spacing=1.05)
text(sl, Inches(0.6), Inches(4.75), Inches(12), Inches(1.2),
     'Becas con el nombre de su fondo para sus afiliados y sus hijos, sin costo para el fondo. '
     'Con garantía de aprendizaje por escrito: si el estudiante cumple su parte y no avanza, le devolvemos el 100% del nivel.',
     size=17, color=CREMA, spacing=1.2)
text(sl, Inches(0.6), Inches(6.3), Inches(8), Inches(1.0),
     [[('Presentación para: ', dict(bold=True)), ('________________________________', {})],
      [('Bucaramanga · octubre de 2026', dict(size=13))]], size=15, color=BLANCO, anchor=MSO_ANCHOR.MIDDLE)
sl.shapes.add_picture(LOGO_N, Inches(10.9), Inches(6.25), height=Inches(1.1))

# ---------------------------------------------------------------- 2. SOMOS HEIIU
sl = prs.slides.add_slide(BLANK)
header(sl, '2 · SOMOS HEIIU', 'Una academia presencial de Bucaramanga que responde por el resultado')
bullets(sl, Inches(0.55), Inches(2.0), Inches(6.2), Inches(4.6), [
    ('Desde 2012. ', 'Heiiu English Academy es la marca de Global Teacher S.A.S., con licencia de la Secretaría de Educación '
                     '(educación para el trabajo y el desarrollo humano) y sede propia en Sotomayor, Carrera 27 # 48-49.'),
    ('Certificada. ', 'Certificación de calidad ISO 9001 e ICONTEC.'),
    ('Un solo programa, completo. ', 'De A1 a B2 en 575 horas presenciales certificadas, en grupos de máximo 16 personas. '
                                     'B2 es el nivel que piden las vacantes, las universidades y los programas en el exterior.'),
    ('Nuestro logro: la garantía. ', 'Es la que queda por escrito en el contrato de cada estudiante: si cumple su parte y no avanza, '
                                     'le devolvemos el 100% del nivel. Pregunte en cualquier academia quién la firma.'),
    ('Convenios vigentes ', 'con entidades y empresas de la región, con becas a nombre de cada una.'),
], size=14)
card(sl, Inches(7.1), Inches(2.0), Inches(5.7), Inches(1.45), 'HABLAS DESDE EL PRIMER DÍA',
     'Cada clase tiene una simulación real (una llamada, una reunión, un cliente, una entrevista) con un profesor que corrige ahí mismo. '
     'Celular guardado.', size=12)
card(sl, Inches(7.1), Inches(3.58), Inches(5.7), Inches(1.45), 'AQUÍ NADIE ENTRENA SOLO',
     'Video corto en inglés todos los días desde la casa, devuelto con una mejora. Si falta y no avisa, lo llamamos ese mismo día. '
     'Cada clase registra la hora de llegada.', size=12)
card(sl, Inches(7.1), Inches(5.16), Inches(5.7), Inches(1.45), 'SE NOTA, Y SE PUEDE MOSTRAR',
     'Prueba de entrada y de salida, evaluador externo al cierre de cada nivel, y el video del primer día junto al del último. '
     'Lo que avanza queda por escrito, no en una sensación.', size=12)
footer(sl, 'Vender inglés es fácil. Lo difícil es que la gente aprenda. En Heiiu queremos la parte difícil: que venga, que se suelte a hablar y que no se rinda.')

# ---------------------------------------------------------------- 3. OFERTA EDUCATIVA (PLAN A)
sl = prs.slides.add_slide(BLANK)
header(sl, '3 · OFERTA EDUCATIVA · PLAN A', 'Programa completo de inglés, de A1 a B2: 575 horas presenciales')
cw = Inches(3.95); gx = Inches(0.17); x0 = Inches(0.55); y0 = Inches(2.0); ch = Inches(2.2)
card(sl, x0, y0, cw, ch, 'HORARIOS',
     [[('Mañana: ', dict(bold=True)), ('lunes a viernes, 8:00 a 12:00.', {})],
      [('Noche: ', dict(bold=True)), ('lunes a viernes, 6:30 a 8:30 p. m.', {})],
      [('Sábados: ', dict(bold=True)), ('8:00 a 12:00 (taller).', {})],
      [('Con 8 o más afiliados en el mismo grupo, el horario lo define el fondo.', dict(color=GRIS, size=11))]], size=12.5)
card(sl, x0 + cw + gx, y0, cw, ch, 'INTENSIDAD',
     [[('Súper intensivo: ', dict(bold=True)), ('20 horas a la semana, programa completo en unos 7 meses.', {})],
      [('Intensivo: ', dict(bold=True)), ('10 horas a la semana, en unos 14 meses.', {})],
      [('Más la práctica diaria: ', dict(bold=True)), ('un video corto en inglés desde la casa, todos los días, devuelto con una mejora.', {})]], size=12.5)
card(sl, x0 + 2 * (cw + gx), y0, cw, ch, 'DOCENTES',
     [[('Profesores bilingües colombianos, ', dict(bold=True)), ('un profesor por grupo de máximo 16.', {})],
      [('Trabajan como coach: ', dict(bold=True)), ('dirigen la simulación, corrigen en el momento y revisan el video de cada día.', {})],
      [('Coordinación académica ', dict(bold=True)), ('sigue asistencia, tareas y evaluaciones.', {})]], size=12.5)
y1 = y0 + ch + Inches(0.17); ch2 = Inches(2.35)
card(sl, x0, y1, cw, ch2, 'EVALUACIÓN',
     [[('Prueba de entrada ', dict(bold=True)), ('el primer día.', {})],
      [('Evaluaciones durante el nivel ', dict(bold=True)), ('y evaluación final con evaluador externo al cierre de cada nivel.', {})],
      [('Reporte al fondo: ', dict(bold=True)), ('asistencia y cumplimiento de tareas de cada afiliado becado. Nunca notas: esas son del estudiante.', {})]], size=12.5)
card(sl, x0 + cw + gx, y1, cw, ch2, 'CERTIFICACIÓN',
     [[('Certificado Heiiu por cada nivel terminado ', dict(bold=True)), ('(A1, A2, B1, B2) y por el programa completo, según los estándares de la Secretaría de Educación.', {})],
      [('Certificado de beca ', dict(bold=True)), ('a nombre del fondo para cada becado, entregado en el fondo o en la sede.', {})]], size=12.5)
rect(sl, x0 + 2 * (cw + gx), y1, cw, ch2, OSCURO)
text(sl, x0 + 2 * (cw + gx) + Inches(0.2), y1 + Inches(0.12), cw - Inches(0.4), Inches(0.4), 'LA GARANTÍA, TAL COMO QUEDA EN EL CONTRATO',
     size=12, bold=True, color=AMA)
text(sl, x0 + 2 * (cw + gx) + Inches(0.2), y1 + Inches(0.55), cw - Inches(0.4), ch2 - Inches(0.65),
     [[('Si el estudiante cumple (asistencia del 80%, 90% de las tareas con video diario, todas las evaluaciones) y no avanza, ', dict(color=BLANCO)),
       ('le devolvemos el 100% del nivel.', dict(color=AMA, bold=True))],
      [('No prometemos que sea fácil ni rápido. Prometemos que funciona si hace su parte, y lo firmamos.', dict(color=CREMA, size=11, italic=True))]],
     size=12.5, spacing=1.15, after=6)
footer(sl, 'Y a cada estudiante lo empujamos a pensar una idea de negocio propia y a contarla en inglés.')

# ---------------------------------------------------------------- 3b. VALOR ECONÓMICO
sl = prs.slides.add_slide(BLANK)
header(sl, '3 · OFERTA EDUCATIVA · VALOR ECONÓMICO', 'Lo que paga el afiliado con carta del fondo: beca del Fondo de Becas Heiiu')
# tabla principal
rows = [('Programa completo A1 a B2 (575 h)', 'Valor de lista', 'Con carta del fondo'),
        ('De contado (transferencia, tarjeta, cesantías o crédito del fondo o de una cooperativa)', '$8.696.000', '$4.782.800  ·  beca del 45%'),
        ('A cuotas, con crédito directo de la academia', '$8.696.000', '$5.565.440  ·  beca del 36%'),
        ('Ejemplo a cuotas: inicial del 20% y 11 cuotas', '', '$1.113.088 hoy y 11 cuotas de $452.348')]
tx, ty = Inches(0.55), Inches(2.0); colw = [Inches(6.3), Inches(2.4), Inches(3.5)]; rh = Inches(0.58)
for i, row in enumerate(rows):
    x = tx
    for j, cell in enumerate(row):
        fill = NAR if i == 0 else (BLANCO if i % 2 else CREMA)
        rect(sl, x, ty + i * rh, colw[j], rh, fill, LINEA)
        text(sl, x + Inches(0.1), ty + i * rh, colw[j] - Inches(0.2), rh, cell, size=12.5 if i else 12,
             bold=(i == 0 or j == 2), color=BLANCO if i == 0 else (NAR if j == 2 else NEGRO), anchor=MSO_ANCHOR.MIDDLE)
        x += colw[j]
text(sl, Inches(0.55), Inches(4.4), Inches(12.2), Inches(0.5),
     'Es beca del Fondo de Becas Heiiu, no un descuento: la misma tarifa y la misma garantía para todos los que entran con carta del fondo. '
     'El crédito del fondo cuenta como pago de contado, y da la beca de contado.', size=12, color=GRIS, spacing=1.15)
card(sl, Inches(0.55), Inches(5.05), Inches(6.0), Inches(1.75), 'BECA CON EL NOMBRE DEL FONDO',
     'Hasta 3 afiliados por trimestre, elegidos por el fondo, reciben el 45% aunque paguen a cuotas, más los libros del programa y prioridad de cupo. '
     'Si todos sus becados cumplen, el cupo sube a 5 el trimestre siguiente.', size=12)
card(sl, Inches(6.75), Inches(5.05), Inches(6.05), Inches(1.75), 'SI EL FONDO PREFIERE PAGAR LOS CUPOS (PLAN EMPRESA)',
     [[('$4.782.800 por cupo de 3 a 7 · $4.350.000 de 8 a 15 · $3.950.000 de 16 a 30. ', dict(bold=True)),
       ('De contado o con inicial y 3 cuotas. El fondo escoge a quién, y con 8 o más el horario es suyo.', {})]], size=12)
footer(sl, 'Valores vigentes 30 días desde la presentación. Todo pago entra directamente a la academia; el fondo no recibe ni gestiona pagos.')

# ---------------------------------------------------------------- 4. BENEFICIOS
sl = prs.slides.add_slide(BLANK)
header(sl, '4 · BENEFICIOS', '¿Qué gano yo? Lo que recibe el fondo y lo que recibe cada afiliado')
rect(sl, Inches(0.55), Inches(2.0), Inches(6.0), Inches(0.45), NAR)
text(sl, Inches(0.7), Inches(2.0), Inches(5.8), Inches(0.45), 'EL FONDO', size=13, bold=True, color=BLANCO, anchor=MSO_ANCHOR.MIDDLE)
bullets(sl, Inches(0.55), Inches(2.55), Inches(6.0), Inches(4.3), [
    ('Un beneficio nuevo para sus afiliados, sin costo para el fondo. ', 'El fondo postula, no paga ni cobra nada.'),
    ('Becas con el nombre del fondo ', 'y certificado a su nombre, entregado en su propio evento.'),
    ('Reporte periódico ', 'de asistencia y cumplimiento de cada becado: el fondo ve quién cumple.'),
    ('Diagnóstico de nivel de inglés ', 'para hasta 10 afiliados, sin costo.'),
    ('Un afiliado que avanza se lo agradece al fondo. ', 'Y lo que el fondo hace por su hijo, no lo olvida.'),
], size=13.5, gap=6)
rect(sl, Inches(6.8), Inches(2.0), Inches(6.0), Inches(0.45), OSCURO)
text(sl, Inches(6.95), Inches(2.0), Inches(5.8), Inches(0.45), 'EL AFILIADO Y SU FAMILIA', size=13, bold=True, color=AMA, anchor=MSO_ANCHOR.MIDDLE)
bullets(sl, Inches(6.8), Inches(2.55), Inches(6.0), Inches(4.3), [
    ('Paga la mitad por ser afiliado: ', 'beca del 45% sobre el programa completo, para él, su cónyuge y sus hijos desde los 12 años.'),
    ('Quien certifica su inglés gana cerca de un 26% más ', 'que quien hace el mismo trabajo sin él.¹'),
    ('Garantía por escrito: ', 'si cumple su parte y no avanza, recibe el 100% del nivel de vuelta.'),
    ('No entrena solo: ', 'un profesor que corrige ahí mismo y un coach que no lo deja rendirse.'),
    ('Sale con algo que mostrar: ', 'el video del primer día junto al del último, y una idea de negocio propia contada en inglés.'),
    ('Para sus hijos que salen del colegio: ', 'un año de inglés con disciplina abre la beca, el intercambio y la carrera que sí es. Solo 1 de cada 8 sale del colegio con un inglés que le sirva.²'),
], size=13.5, gap=6)
footer(sl, '¹ DNP, Archivos de Economía, Bilingüismo laboral en Colombia. ² Pruebas Saber 11 de 2025, análisis del Observatorio de Realidades Educativas de la Universidad Icesi.')

# ---------------------------------------------------------------- 5. LLAMADO A LA ACCIÓN
sl = prs.slides.add_slide(BLANK)
header(sl, '5 · LLAMADO A LA ACCIÓN', 'Firmemos el convenio esta semana y hablemos con sus afiliados', dark=True)
text(sl, Inches(0.55), Inches(2.05), Inches(12.2), Inches(0.9),
     'El convenio no tiene costo ni obligaciones económicas para el fondo. Se firma en una hoja, dura 12 meses, y lo único que le pedimos es '
     '20 minutos con sus afiliados para contarles el programa y el Pacto antes de que decidan.', size=16, color=CREMA, spacing=1.2)
for i, (t1, t2) in enumerate([
        ('3 BECAS CON SU NOMBRE', 'Este trimestre, para los afiliados que el fondo elija. Si todos cumplen, suben a 5.'),
        ('INICIO 3 DE NOVIEMBRE','Grupos de máximo 16; el cupo se asigna por orden de matrícula con la inicial pagada. El grupo no para en diciembre: sigue hasta terminar el nivel, solo descansa los festivos.'),
        ('10 PRUEBAS DE NIVEL', 'Diagnóstico sin costo para hasta 10 afiliados, en su sede o en la nuestra, la semana siguiente a la firma.')]):
    x = Inches(0.55) + i * Inches(4.12)
    rect(sl, x, Inches(3.25), Inches(3.95), Inches(2.3), NAR2)
    text(sl, x + Inches(0.2), Inches(3.4), Inches(3.55), Inches(0.6), t1, size=19, font=TIT, bold=True, color=BLANCO)
    text(sl, x + Inches(0.2), Inches(4.05), Inches(3.55), Inches(1.45), t2, size=13, color=BLANCO, spacing=1.15)
text(sl, Inches(0.55), Inches(5.8), Inches(12.2), Inches(1.0),
     [[('Hoy: ', dict(bold=True, color=AMA)), ('firma del convenio y fecha de la charla con los afiliados.  ', {}),
       ('Esta semana: ', dict(bold=True, color=AMA)), ('diagnóstico de nivel.  ', {}),
       ('Antes del 3 de noviembre: ', dict(bold=True, color=AMA)), ('los primeros afiliados en su grupo.', {})]],
     size=15, color=BLANCO, spacing=1.2)
footer(sl, 'Línea de alianzas: 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga · Instagram @Heiiu_english', dark=True)

# ---------------------------------------------------------------- 6. CIERRE
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, OSCURO)
rect(sl, 0, Inches(6.1), W, Inches(1.4), NAR2)
sl.shapes.add_picture(LOGO_T, Inches(0.5), Inches(0.35), height=Inches(1.3))
text(sl, Inches(0.6), Inches(1.95), Inches(12.2), Inches(1.4),
     [[('Nuestro objetivo es que su afiliado salga hablando inglés. Si no se logra, algo está mal: o él dejó de entrenar, o nosotros no estamos cumpliendo. '
        'Por eso lo firmamos.', dict(color=CREMA))]], size=17, spacing=1.25)
text(sl, Inches(0.6), Inches(3.5), Inches(12.2), Inches(1.9),
     [[('¿Cuántos de sus afiliados quiere ver hablando inglés ', dict(color=BLANCO)),
       ('el próximo año?', dict(color=AMA, italic=True))]], size=38, font=TIT, bold=True, spacing=1.05)
text(sl, Inches(0.6), Inches(5.35), Inches(12.2), Inches(0.6), 'Dígame cuántos, y hoy mismo definimos a quiénes.', size=18, color=CREMA)
text(sl, Inches(0.6), Inches(6.3), Inches(9), Inches(1.0),
     [[('Heiiu English Academy · Global Teacher S.A.S.', dict(bold=True))],
      [('Línea de alianzas 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga · @Heiiu_english', dict(size=13))]],
     size=15, color=BLANCO, anchor=MSO_ANCHOR.MIDDLE)
sl.shapes.add_picture(LOGO_N, Inches(10.9), Inches(6.25), height=Inches(1.1))

try:
    prs.save(OUT); print('OK', OUT)
except PermissionError:
    OUT = OUT.replace('.pptx', '_v2.pptx'); prs.save(OUT); print('ABIERTO -> _v2', OUT)
