# -*- coding: utf-8 -*-
"""Guion del taller para padres de colegios (8 a 11) — formato de marca."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NARANJA = RGBColor(0xE5, 0x4C, 0x09)
GRIS = RGBColor(0x77, 0x77, 0x77)
CREMA = 'FFF8E7'
NARANJA_HEX = 'E54C09'

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.6); s.bottom_margin = Cm(1.4); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(11.5)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd'); el.set(qn('w:val'), 'clear'); el.set(qn('w:fill'), color)
    tcPr.append(el)

def titulo(txt, sub=None):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(18); r.font.color.rgb = NARANJA
    if sub:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(sub); r.font.size = Pt(10.5); r.font.color.rgb = GRIS
    doc.add_paragraph()

def sec(txt):
    p = doc.add_paragraph(); r = p.add_run(txt); r.bold = True; r.font.size = Pt(13.5); r.font.color.rgb = NARANJA
    p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(4)

def t(txt, bold=False, size=11.5):
    p = doc.add_paragraph(); r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    p.paragraph_format.space_after = Pt(4)

def frase(txt):
    tab = doc.add_table(rows=1, cols=1); tab.style = 'Table Grid'
    c = tab.rows[0].cells[0]; shd(c, CREMA)
    for k, ln in enumerate(txt.split('\n')):
        p = c.paragraphs[0] if k == 0 else c.add_paragraph()
        r = p.add_run(ln); r.font.size = Pt(11.5); r.italic = True
    esp = doc.add_paragraph(); esp_r = esp.add_run(''); esp_r.font.size = Pt(4)
    esp.paragraph_format.space_after = Pt(0)

titulo('TALLER PARA PADRES — "EL PLAN BILINGÜE: DEL COLEGIO A LA UNIVERSIDAD"',
       'Guion interno · 60-75 min · Lo dicta GERENCIA · La asesora captura y agenda en sala · Público: padres de 8° a 11°')

sec('LAS 3 REGLAS (antes de empezar)')
t('1. REGISTRO PREVIO CON DATOS, siempre: nombre del padre, nombre y grado del hijo, teléfono. Cada silla es un lead con nombre — la asesora maneja la planilla en sala y confirma datos a la salida.', bold=True)
t('2. Se presenta como taller de la escuela de padres del colegio — NUNCA como "charla informativa de Heiiu". El colegio invita; Heiiu aporta el contenido.')
t('3. La oferta del cierre es SOLO PARA ASISTENTES y vence en 72 horas (la vigencia de siempre). Sin excepción — el Fondo audita las fechas.')

sec('PARTE 1 — EL DATO-DOLOR (10 min)')
t('Para papás de 11°: qué pasa entre noviembre y la universidad — 6 a 8 meses muertos, el inglés del colegio se evapora, y "descansar" se convierte en perder el semestre más aprovechable de su vida.')
t('Para papás de 8°-10°: el inglés del colegio NO alcanza para la universidad ni para las oportunidades reales — y esperarse a grado 11 para "apurarlo" es la versión cara y estresante. La ventana que nadie usa: los sábados.')
frase('"Hoy no vengo a venderles clases. Vengo a mostrarles el mapa que a mí me hubiera gustado que alguien le mostrara a mis papás."')

sec('PARTE 2 — QUE LO VIVAN (15 min): mini-clase inmersiva CON los papás')
t('Los papás VIVEN 10 minutos de una clase real: todos de pie, una historia corta narrada con pausas que el grupo repite en coro, y 5 frases de inglés real que se llevan puestas. Cerrar con: "esto que acaban de vivir 10 minutos, sus hijos lo viven 2 horas diarias — así se aprende un idioma: hablándolo de pie, no copiando del tablero".')
t('Regla: nada de nombres internos de metodologías. Se muestra la experiencia, jamás la maquinaria.', bold=True)

sec('PARTE 3 — EL MAPA HONESTO (10 min)')
t('Para 11°: las 4 opciones del gap (universidad inmediata · preuniversitario · trabajar · inglés intensivo) con pros y contras DE VERDAD. La honestidad de esta parte compra la credibilidad del cierre.')
t('Para 8°-10°: la ruta sabatina — A1 en 8°, A2 en 9°, B1 en 10° (4 horas cada sábado, sin tocar el colegio) → llega a grado 11 con B1, y su semestre de gap es el B2 + su proyecto de graduación (página web propia o aplicación para irse). Se gradúa del colegio y de la universidad del inglés casi al tiempo.')

sec('PARTE 4 — CÓMO EVALUAR CUALQUIER ACADEMIA (10 min): las 5 preguntas')
t('"Vayan a la academia que quieran — pero vayan con estas 5 preguntas":')
t('1. ¿Cuál es el precio FINAL — con matrícula, libros, TODO?')
t('2. ¿Cuántas horas REALES de clase incluye?')
t('3. ¿La garantía está POR ESCRITO en el contrato — o es de palabra?')
t('4. ¿Cómo MIDEN el avance de mi hijo — y me lo muestran?')
t('5. ¿Quién aplica el examen final — el mismo profesor, o un evaluador externo?')
frase('Cada pregunta es una que solo Heiiu responde bien. Los papás la van a usar contra la competencia — es educación al consumidor, y es nuestro mejor vendedor.')

sec('PARTE 5 — EL CIERRE DE SALA (10 min)')
t('Para 11°: el Arranque de enero — A1+A2 completos, garantía firmada, Módulo de Graduación — con prioridad de cupo para el colegio aliado.')
t('Para 8°-10°: la ruta sabatina, nivel por año, con el beneficio de convenio del colegio.')
t('LA OFERTA DE SALA: "por ser de [colegio] y estar aquí hoy: cita de valoración esta semana + prioridad de cupo + [beneficio de convenio]. Vence el [día] a las 6 PM." La asesora agenda citas AHÍ MISMO, en la salida, con día y hora.', bold=True)
t('Todo asistente sale con: fecha de su cita O motivo anotado. Sala sin agenda = taller perdido.', bold=True)

sec('DESPUÉS DEL TALLER (la asesora, mismo día y +24h)')
t('· Mismo día: WhatsApp de gracias a TODOS los registrados + confirmación a los agendados.')
t('· +24h: llamada a los que no agendaron ("¿qué te quedó sonando del taller?") — motivo real anotado.')
t('· Los datos entran al reporte diario como cualquier canal.')

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\B2B\TALLER_PADRES_COLEGIOS.docx'
doc.save(out); print('OK', out)
