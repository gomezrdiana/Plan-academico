# -*- coding: utf-8 -*-
"""Presentación LIVIANA para FONDOS DE EMPLEADOS (versión 2, 26/10/2026, tras la investigación con fuentes):
6 diapositivas, una idea por diapositiva, titular como afirmación (Garner y Alley 2013), poco texto y nada para leer
(principios de coherencia y redundancia de Mayer), "sin costo" y la fecha al inicio, un solo pedido al final con fecha y hora
(Milkman et al. 2011). El detalle (licencias, horarios, tabla de precios, beneficios con fuentes) va en la HOJA que se deja al final:
gen_hoja_fondos_empleados.py. El guion de lo que se dice de palabra va en las NOTAS de cada diapositiva.
Estructura del analista financiero conservada: portada (ya con la respuesta), oferta + valor, beneficios, llamado a la acción
(la urgencia sube a la diapositiva 2), cierre con pregunta. "Somos Heiiu" pasa a la hoja y a 20 segundos de palabra.
Salida: recursos/comercial/B2B/PRESENTACION_FONDOS_EMPLEADOS_HEIIU.pptx (PDF por PowerPoint COM: topdf_fondos.ps1)."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

R = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
OUT = R + r'\recursos\comercial\B2B\PRESENTACION_FONDOS_EMPLEADOS_HEIIU.pptx'
LOGO_T = R + r'\recursos\marca heiiu\logo_heiiu_transparente.png'
LOGO_N = R + r'\recursos\marca heiiu\logo_heiiu_sobre_naranja.png'
MINI = R + r'\recursos\comercial\B2B\_convenio_entidad_miniatura.png'   # miniatura del convenio para la diapositiva de cierre
try:
    import fitz
    fitz.open(R + r'\recursos\comercial\B2B\CONVENIO_HEIIU_ENTIDAD_ALIADA_v1.pdf')[0].get_pixmap(dpi=110).save(MINI)
except Exception as e:
    print('miniatura no regenerada:', e)

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


def notas(sl, txt):
    sl.notes_slide.notes_text_frame.text = txt


def lamina(n, titulo, lineas, big=None, big_sub=None, dark=False, nota='', big_size=64):
    """Una idea: titular-afirmación grande, hasta 3 líneas cortas, y una cifra grande opcional a la derecha."""
    sl = prs.slides.add_slide(BLANK)
    rect(sl, 0, 0, W, H, OSCURO if dark else CREMA)
    rect(sl, 0, 0, W, Inches(0.42), NAR2)
    text(sl, Inches(0.55), Inches(0.04), Inches(6), Inches(0.36), f'{n} de 6', size=12, color=BLANCO, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(sl, Inches(7.2), Inches(0.04), Inches(5.6), Inches(0.36), 'HEIIU ENGLISH ACADEMY · PROGRAMA PARA FONDOS DE EMPLEADOS',
         size=11, color=BLANCO, bold=True, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    tw = Inches(7.9) if big else Inches(12.2)
    text(sl, Inches(0.6), Inches(1.0), tw, Inches(2.6), titulo, size=40, font=TIT, bold=True,
         color=BLANCO if dark else NAR, anchor=MSO_ANCHOR.MIDDLE, spacing=1.05)
    rect(sl, Inches(0.65), Inches(3.75), Inches(1.6), Emu(38000), AMA)
    paras = [[('▪ ', dict(color=AMA if dark else NAR, bold=True)), (l, {})] for l in lineas]
    text(sl, Inches(0.6), Inches(4.0), tw, Inches(2.7), paras, size=22, color=CREMA if dark else NEGRO, after=10, spacing=1.15)
    if big:
        rect(sl, Inches(8.9), Inches(1.0), Inches(3.9), Inches(5.6), NAR2)
        text(sl, Inches(9.0), Inches(1.4), Inches(3.7), Inches(2.6), big, size=big_size, font=TIT, bold=True, color=BLANCO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        text(sl, Inches(9.1), Inches(4.1), Inches(3.5), Inches(2.3), big_sub, size=18, color=BLANCO, align=PP_ALIGN.CENTER, spacing=1.2)
    text(sl, Inches(0.55), Inches(6.95), Inches(12.2), Inches(0.4), 'Línea de alianzas 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga',
         size=10, color=RGBColor(0xC9, 0xB8, 0xA3) if dark else GRIS, anchor=MSO_ANCHOR.MIDDLE)
    notas(sl, nota)
    return sl


# ---------------------------------------------------------------- 1. PORTADA CON LA RESPUESTA
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, OSCURO)
rect(sl, 0, Inches(6.1), W, Inches(1.4), NAR2)
sl.shapes.add_picture(LOGO_T, Inches(0.5), Inches(0.35), height=Inches(1.5))
text(sl, Inches(0.6), Inches(2.05), Inches(12), Inches(0.5), 'PROGRAMA DE INGLÉS PARA FONDOS DE EMPLEADOS', size=14, color=AMA, bold=True)
text(sl, Inches(0.6), Inches(2.55), Inches(12.2), Inches(2.4),
     [[('Beca del 45% en inglés para sus afiliados y sus familias, ', dict(color=BLANCO)),
       ('sin costo para el fondo.', dict(color=AMA, italic=True))]], size=44, font=TIT, bold=True, spacing=1.05)
text(sl, Inches(0.6), Inches(5.05), Inches(12), Inches(0.9),
     'Programa presencial de A1 a B2, en Bucaramanga. Con garantía de aprendizaje por escrito.', size=20, color=CREMA)
text(sl, Inches(0.6), Inches(6.3), Inches(8), Inches(1.0),
     [[('Para: ', dict(bold=True)), ('________________________________', {})],
      [('Bucaramanga · octubre de 2026', dict(size=13))]], size=15, color=BLANCO, anchor=MSO_ANCHOR.MIDDLE)
sl.shapes.add_picture(LOGO_N, Inches(10.9), Inches(6.25), height=Inches(1.1))
notas(sl, 'ANTES DE EMPEZAR (una pregunta): "¿Un convenio así lo firma usted o lo lleva a junta? ¿Cuándo se reúne la junta?" '
          'Con esa respuesta sabes si hoy sales con firma o con fecha de junta.\n'
          'QUÉ DECIR (20 segundos): "Vengo a proponerle un beneficio nuevo para sus afiliados que al fondo no le cuesta nada: '
          'beca del 45% en el programa de inglés de Heiiu, para ellos y sus familias, con el nombre del fondo. Somos una academia de '
          'Bucaramanga con licencia de la Secretaría de Educación desde 2012 y certificación ISO 9001 e ICONTEC; el detalle se lo dejo en una hoja. '
          'Le pido 10 minutos y salgo con una sola cosa: una fecha."\n'
          'NO leer la diapositiva. NO hablar de la academia más de 20 segundos. NO entregar la hoja todavía.')

# ---------------------------------------------------------------- 2. POR QUÉ AHORA
lamina(2, 'El próximo grupo arranca el martes 3 de noviembre.',
       ['Quedan 8 días. El grupo no para en diciembre: sigue hasta terminar el nivel.',
        'Este trimestre hay 3 becas con el nombre del fondo. Si todos cumplen, suben a 5.',
        'Los afiliados que no entren ahora esperan al siguiente grupo.'],
       big='3 NOV', big_sub='Martes 3 de noviembre de 2026. Grupos de máximo 16, por orden de matrícula con la inicial pagada.',
       nota='QUÉ DECIR: "Le hablo hoy y no el mes entrante por una razón: el grupo arranca el martes 3 de noviembre y no para en diciembre. '
            'Si firmamos esta semana, sus afiliados alcanzan a entrar. Si no, el siguiente grupo es [fecha real del siguiente grupo]."\n'
            'Decir solo cupos reales: grupos de 16 y 3 becas con nombre por trimestre. Nunca "últimos cupos" si no es cierto.')

# ---------------------------------------------------------------- 3. LA OFERTA (una sola cifra)
lamina(3, 'Afiliados y familias estudian con 45% de beca a nombre del fondo.',
       ['Programa completo de inglés, de A1 a B2: 575 horas presenciales, grupos de máximo 16.',
        'Para el afiliado, su cónyuge y sus hijos desde los 12 años.',
        'Con crédito del fondo o cesantías paga de contado, y la beca de contado es la mayor.'],
       big='$3.913.200', big_size=46, big_sub='menos por afiliado: $4.782.800 en lugar de $8.696.000, el programa completo.',
       nota='QUÉ DECIR: "El afiliado paga $4.782.800 por el programa completo que vale $8.696.000. Es beca del Fondo de Becas Heiiu, no un descuento: '
            'la misma tarifa y la misma garantía para todos los que entran con carta del fondo. Si el fondo le presta o paga con cesantías, '
            'cuenta como contado y recibe la beca mayor. También hay plan a cuotas con la academia; los números están en la hoja."\n'
            'NO mostrar ni recitar la tabla completa. Si pregunta por cuotas, horarios o profesores: "está en la hoja, se la dejo al final"; '
            'responde en una frase y vuelve al pedido.')

# ---------------------------------------------------------------- 4. RIESGO
lamina(4, 'Si el estudiante cumple y no avanza, le devolvemos el 100% del nivel.',
       ['Garantía por escrito, en el contrato de cada afiliado.',
        'El fondo no paga, no cobra ni gestiona nada: cada afiliado contrata directo con la academia.',
        'El convenio se termina con aviso de 30 días, sin afectar a los ya matriculados.'],
       big='100%', big_sub='del nivel devuelto si cumple asistencia, tareas y evaluaciones y no avanza. Por escrito.', dark=True,
       nota='QUÉ DECIR: "Lo que más le preocupa a un gerente es quedar mal con sus afiliados. Por eso lo firmamos: si el afiliado cumple su parte '
            '(asistencia del 80%, tarea diaria en video, evaluaciones) y no avanza, le devolvemos el 100% del nivel. Y el fondo no asume nada: '
            'no paga, no cobra, y puede terminar el convenio con aviso de 30 días."\n'
            'Si pregunta "¿y si nadie se inscribe?": "No le cuesta nada al fondo. Lo único que le pido es la charla de 20 minutos."')

# ---------------------------------------------------------------- 5. QUÉ GANA EL FONDO
lamina(5, 'Un beneficio nuevo con su nombre, sin presupuesto y con reporte.',
       ['Becas y certificados con el nombre del fondo, entregados en su propio evento.',
        'Reporte de asistencia y cumplimiento de cada becado: el fondo ve quién cumple.',
        'Cero carga operativa: el fondo postula con una carta, la academia hace el resto. Y diagnóstico de nivel para 10 afiliados, sin costo.'],
       nota='QUÉ DECIR: "Para el fondo esto es un beneficio más en su portafolio, con su nombre, sin tocar presupuesto. Usted postula con una carta '
            'de una página y nosotros hacemos el resto. Cada trimestre recibe el reporte de asistencia y cumplimiento de sus becados; nunca notas. '
            'Y la semana siguiente a la firma hacemos el diagnóstico de nivel a 10 afiliados sin costo."\n'
            'Si quiere datos de por qué inglés (26% más de ingreso, 1 de cada 8 sale del colegio con inglés): están en la hoja con fuente. '
            'Decir uno, no los seis.')

# ---------------------------------------------------------------- 6. CIERRE: UN SOLO PASO
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, OSCURO)
rect(sl, 0, 0, W, Inches(0.42), NAR2)
text(sl, Inches(0.55), Inches(0.04), Inches(6), Inches(0.36), '6 de 6', size=12, color=BLANCO, bold=True, anchor=MSO_ANCHOR.MIDDLE)
text(sl, Inches(7.2), Inches(0.04), Inches(5.6), Inches(0.36), 'HEIIU ENGLISH ACADEMY · PROGRAMA PARA FONDOS DE EMPLEADOS',
     size=11, color=BLANCO, bold=True, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
text(sl, Inches(0.6), Inches(0.9), Inches(8.2), Inches(2.3),
     [[('Un solo paso: ', dict(color=AMA)), ('firmar el convenio hoy y fijar la charla de 20 minutos con sus afiliados.', dict(color=BLANCO))]],
     size=36, font=TIT, bold=True, anchor=MSO_ANCHOR.MIDDLE, spacing=1.05)
rect(sl, Inches(0.65), Inches(3.3), Inches(1.6), Emu(38000), AMA)
rect(sl, Inches(0.6), Inches(3.6), Inches(8.2), Inches(1.5), NAR2)
text(sl, Inches(0.8), Inches(3.65), Inches(7.8), Inches(1.4),
     [[('¿La charla la hacemos el ', {}), ('________', dict(color=AMA)), (' a las ', {}), ('_____', dict(color=AMA)),
       (' o el ', {}), ('________', dict(color=AMA)), (' a las ', {}), ('_____', dict(color=AMA)), ('?', {})]],
     size=24, color=BLANCO, bold=True, anchor=MSO_ANCHOR.MIDDLE, spacing=1.2)
text(sl, Inches(0.6), Inches(5.3), Inches(8.2), Inches(1.4),
     [[('Si va a junta: ', dict(bold=True, color=AMA)), ('¿cuándo se reúne? Le dejo el convenio listo para esa fecha.', {})],
      [('Una hoja, sin costo, 12 meses, se termina con aviso de 30 días.', dict(color=RGBColor(0xC9, 0xB8, 0xA3), size=15))]],
     size=18, color=CREMA, spacing=1.2, after=6)
sl.shapes.add_picture(MINI, Inches(9.4), Inches(0.9), height=Inches(5.6))
text(sl, Inches(0.55), Inches(6.95), Inches(12.2), Inches(0.4),
     'Heiiu English Academy · Global Teacher S.A.S. · Línea de alianzas 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga · @Heiiu_english',
     size=10, color=RGBColor(0xC9, 0xB8, 0xA3), anchor=MSO_ANCHOR.MIDDLE)
notas(sl, 'QUÉ DECIR: "Le pido una sola cosa: que firmemos hoy este convenio de una página y me dé fecha y hora para la charla de 20 minutos '
          'con sus afiliados. ¿La hacemos el [día] a las [hora] o el [día] a las [hora]?" Y SILENCIO. Que responda él.\n'
          'Si debe ir a junta: "¿Cuándo se reúne la junta? Le dejo el convenio y la hoja listos para esa fecha, y lo llamo el día siguiente."\n'
          'AL FINAL, no antes: entregar la hoja (HOJA_FONDOS_EMPLEADOS_HEIIU.pdf impresa) y el convenio en dos copias.\n'
          'Lo que cuenta para el tablero: convenio firmado con fecha de charla, o fecha de junta anotada. Un "lo pienso" sin fecha no cuenta.')

try:
    prs.save(OUT); print('OK', OUT)
except PermissionError:
    OUT = OUT.replace('.pptx', '_v2.pptx'); prs.save(OUT); print('ABIERTO -> _v2', OUT)
