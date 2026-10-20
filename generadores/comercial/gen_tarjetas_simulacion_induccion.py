# -*- coding: utf-8 -*-
"""Tarjetas de simulación para la inducción del Gerente de Alianzas (gerencia actúa de decisor): dos reuniones de 10 min
y una charla de 5 min. Por rol. Salida (git): recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/TARJETAS_SIMULACION_INDUCCION_ALIANZAS.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\TARJETAS_SIMULACION_INDUCCION_ALIANZAS.docx'
d = Document()
for s in d.sections:
    s.top_margin = Cm(1.0); s.bottom_margin = Cm(0.8); s.left_margin = Cm(1.5); s.right_margin = Cm(1.5)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9.5)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAR
def t(txt, size=9.5, color=None, after=2, bold=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def caja(txt, size=9.5):
    tb = d.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(txt); r.font.size = Pt(size); r.italic = True
    d.add_paragraph().paragraph_format.space_after = Pt(0)
def bullets(items, size=9.5):
    for x in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); r = p.add_run(x); r.font.size = Pt(size)

p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('TARJETAS DE SIMULACIÓN — INDUCCIÓN DEL GERENTE DE ALIANZAS'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(5)
r = p.add_run('Gerencia actúa de decisor. Él lleva la reunión de 6 pasos del kit. Regla: dos correcciones por simulación, no diez; se dicen al final, no en medio.'); r.font.size = Pt(8.5); r.font.color.rgb = GRIS

sec('Simulación 1 · Gerente de una clínica de 80 empleados (10 minutos)')
t('Quién eres: gerente general, ocupada, te dieron 10 minutos. Tu interés real: retener personal asistencial y verte bien con la junta. No sabes nada de la academia.', size=9.5)
t('Lo que dices, en este orden:', bold=True, after=1)
bullets([
 'Apertura fría: "Tengo diez minutos. ¿Esto me va a costar plata?"',
 'Cuando mencione la alianza sin costo: "¿Y entonces ustedes qué ganan?"',
 'Cuando mencione el plan empresa: "Ya tuvimos un convenio con una academia y nadie terminó el curso."',
 'Cuando mencione la garantía: "¿Garantía de qué? ¿Me devuelven la plata a mí o al empleado?"',
 'Cuando pida la charla: "Mis turnos son rotativos; no puedo sacar a nadie 20 minutos."',
 'Cierre: "Mándeme la propuesta por correo y lo pensamos." (No cedas: espera a ver si él te propone fecha igual.)'])
t('Lo que miras en él (marca sí/no):', bold=True, after=1)
bullets([
 'Dijo la causa en una frase y pasó a qué gana la clínica, sin vender el curso.',
 'Ofreció primero el plan empresa y después la alianza, no al revés.',
 'A "nadie terminó" respondió con la garantía y el seguimiento de asistencia, no con descuentos.',
 'A "turnos rotativos" ofreció dos charlas cortas o una por turno, y no cedió a "mándeme la propuesta" sin fecha.',
 'Cerró con dos opciones de fecha y silencio.'])
caja('Corrección típica: se va a los precios antes de que preguntes. Si pasa, al final: "Me diste el precio antes de saber si yo quería formar o premiar. Pregunta primero."')

sec('Simulación 2 · Directora de una fundación (10 minutos)')
t('Quién eres: directora de una fundación con 120 beneficiarios jóvenes y 15 empleados. Te importa la causa social, no tienes presupuesto, y desconfías de "convenios" que son publicidad disfrazada.', size=9.5)
t('Lo que dices, en este orden:', bold=True, after=1)
bullets([
 'Apertura: "Nosotros no tenemos presupuesto para esto."',
 'Cuando hable de becas con el nombre de la fundación: "¿Cuántas becas y de cuánto? ¿Es beca o es descuento?"',
 'Cuando hable de los jóvenes: "Mis muchachos no tienen 4 millones. ¿Qué les ofrecen a ellos?"',
 'Cuando hable de la empresa aliada: "¿Puedo poner esto en mi informe a los donantes?"',
 'Cierre: "¿Y qué me toca hacer a mí?"'])
t('Lo que miras en él:', bold=True, after=1)
bullets([
 'Explicó la diferencia entre beca del Fondo y descuento sin enredarse.',
 'No prometió cupos gratis ni precios distintos; mandó lo especial a gerencia.',
 'Dejó claro lo que firma la fundación (convenio, cartas de postulación, difusión) y que no gestiona pagos.',
 'Pidió la charla con fecha.'])
caja('Corrección típica: promete cosas para los jóvenes que no existen. Al final: "Lo que no está en el kit se agenda con gerencia; no se promete."')

sec('Charla de 5 minutos a empleados (tú eres la sala: 3 empleados en uno)')
bullets([
 'Tú preguntas lo que preguntan siempre: "¿Cuánto vale?" a los 30 segundos; "¿Es virtual?"; "¿Y si no aprendo?"; "¿Hay clase de prueba?".',
 'Lo que miras: El Pacto antes de los precios; las opciones en orden (empresa, beca de alianza, Arranque); la garantía con su texto y sus condiciones; cómo se inscribe hoy; registro de interesados con nombre y celular.'])

sec('Cierre de las simulaciones (2 minutos)')
t('Dos correcciones en total, no más, y una cosa que hizo bien dicha con el mismo peso. Luego: "A las 4 lo haces de verdad, con los 18."', size=9.5, after=0)

try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
