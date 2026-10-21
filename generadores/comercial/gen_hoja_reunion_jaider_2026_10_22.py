# -*- coding: utf-8 -*-
"""Hoja de una pagina para la reunion con LaHaus del jueves 22/10 a las 10:00: numeros de la prueba A/B (casillas para
llenar desde SAMI), reglas de la prueba, reactivacion de octubre, tres reglas del agente y pendientes con fecha.
Por rol, sin nombres del personal ni de leads. Salida (git):
recursos/comercial/plataforma LaHaus/HOJA_REUNION_JAIDER_2026-10-22.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus\HOJA_REUNION_JAIDER_2026-10-22.docx'
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
d = Document()
for s in d.sections:
    s.top_margin = Cm(0.9); s.bottom_margin = Cm(0.7); s.left_margin = Cm(1.3); s.right_margin = Cm(1.3)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(1)
    x = p.add_run(t); x.bold = True; x.font.size = Pt(10.5); x.font.color.rgb = NAR
def t(txt, size=9, color=None, after=1, bold=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    x = p.add_run(txt); x.font.size = Pt(size); x.bold = bold
    if color: x.font.color.rgb = color
def bullets(items, size=9):
    for it in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); x = p.add_run(it); x.font.size = Pt(size)
def tabla(hdr, filas, anchos, size=8.5):
    tb = d.add_table(rows=1, cols=len(hdr)); tb.style = 'Table Grid'
    for i, hh in enumerate(hdr):
        c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
        x = c.paragraphs[0].add_run(hh); x.bold = True; x.font.size = Pt(size); x.font.color.rgb = BLANCO
    for f in filas:
        row = tb.add_row().cells
        for i, txt in enumerate(f):
            row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
            x = row[i].paragraphs[0].add_run(txt); x.font.size = Pt(size); x.bold = (i == 0)
    for row in tb.rows:
        for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    d.add_paragraph().paragraph_format.space_after = Pt(0)

p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
x = p.add_run('REUNIÓN CON LAHAUS — JUEVES 22 DE OCTUBRE DE 2026, 10:00 A. M.'); x.bold = True; x.font.size = Pt(13); x.font.color.rgb = NAR
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(4)
x = p.add_run('Hoja de gerencia · 30 minutos · los números se llenan antes de la reunión desde SAMI y el panel; dato que no llegó se escribe SIN DATO'); x.font.size = Pt(8.5); x.font.color.rgb = GRIS

sec('1. Números de la prueba A/B (desde el 20/10; corte final 5/11)')
tabla(['Grupo', 'Leads', 'Respondieron', 'Citas agendadas', 'Citas asistidas', 'Separaron', 'Paso donde más se caen'], [
    ('PAR · 7 pasos', '', '', '', '', '', ''),
    ('IMPAR · flujo corto', '', '', '', '', '', ''),
    ('Reactivación 6/10 (aparte)', '', '', '', '', '', ''),
], [3.6, 1.6, 2.2, 2.4, 2.3, 1.9, 4.2])
t('Gana el flujo con más citas ASISTIDAS por lead, no el que más agenda. Separación y matrícula las seguimos nosotros por grupo. Jaider trae en qué paso se cae cada lead desde el 20/10.', size=8.5, color=GRIS)

sec('2. Reactivación de octubre (enviada hoy jueves 9:00 a. m., o viernes si Meta no aprobó)')
tabla(['Plantilla', 'Enviados', 'Entregados', 'Botón "quiero mi fecha"', 'Botón "más adelante"', '"Ya no" / BAJA', 'Por texto', 'Citas'],
      [('A · perder la oportunidad', '', '', '', '', '', '', ''), ('B · que no te dé miedo hablar', '', '', '', '', '', '', '')],
      [3.6, 1.8, 1.9, 2.7, 2.4, 2.0, 1.7, 1.7])
t('Dos plantillas mitad y mitad; la que dé más citas por enviado se queda para la reserva del bot anterior (unos 1.500), que sale la primera semana de noviembre. "Más adelante" entra a la reactivación de la semana del 23 de noviembre.', size=8.5, color=GRIS)

sec('3. Tres reglas del agente que se piden hoy (vienen de un caso real probado en otra empresa)')
bullets([
    'Mensaje que no está en el flujo (dos preguntas, un cálculo, una petición rara): el agente NO reinicia ni vuelve a pedir el nombre. Dice "eso te lo resuelve la asesora, te la paso ahora", notifica y conserva el contexto. ¿Cómo está configurado hoy y qué dispara un reinicio?',
    'Duración del contexto: ¿cuántos minutos u horas conserva la conversación antes de empezar de cero? Si hay un límite, el paso 7 (cita) debe llegar antes de ese límite.',
    'Conversación que murió a mitad del flujo (el lead dio datos y no llegó a la cita): aparece en un filtro del panel el mismo día, para que la asesora la llame. Hoy esas conversaciones no las ve nadie.',
])

sec('4. Pendientes de LaHaus con fecha')
tabla(['Tema', 'Qué se espera', 'Fecha'], [
    ('Casos reportados (dos leads: mensaje tras la pausa; precios inexistentes)', 'Causa y corrección', 'Hoy 22/10 (prometido para el 21)'),
    ('Cambios del documento del agente (menores de 12, 12 a 17, "para otra persona", sin TOEFL/IELTS)', 'Confirmar carga: reemplaza, no se suma', 'Hoy'),
    ('Anticipación mínima para agendar: de 24 h a 4 h dentro del horario', 'Configurado', 'Esta semana'),
    ('Campaña de interacción del 10/10: Meta reporta 84 conversaciones y el panel muestra 15', '¿En qué bandeja caen?', 'Hoy'),
    ('Informe semanal por fuente y por número de toque', 'Fecha de entrega o cómo sacarlo de SAMI', 'Hoy'),
    ('Revisión de cadencia (día 0, 1, 3 y 7, misma pregunta) + disparadores de aviso a la asesora', 'Reunión', 'Viernes 30/10 en la mañana'),
    ('Corte de evaluación del primer mes', 'Números completos por fuente', 'Sábado 31/10'),
], [8.2, 5.2, 4.4])

sec('5. Lo nuestro (no se discute con LaHaus, se revisa antes de entrar)')
bullets([
    'Barridos de la asesora a las 12:00 y 6:00 p. m.: filtro de contacto humano + conversaciones a mitad de flujo. Un solo mensaje, dos franjas, llamada si no responde en 2 horas.',
    'Cada mañana a las 8:00 gerencia confirma por WhatsApp la modalidad de las citas del día (llamada o enlace de video).',
    'Cruce de los que agendaron con el bot anterior contra la lista de estudiantes: lo hace coordinación antes de subir esa base.',
], size=8.5)

try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
