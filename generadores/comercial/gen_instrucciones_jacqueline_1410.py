# -*- coding: utf-8 -*-
"""Instrucciones para Jacqueline (14/10/2026): (1) asistencia del B1 de la mañana tras el cambio de docente (4 estudiantes),
(2) regla de puntualidad docente que corre sola, (3) reporte diario a gerencia. Dirigido a Jacqueline por decisión de gerencia (14/10); sin nombres de estudiantes.
Salida: documentos_operativos/politicas/INSTRUCCIONES_JACQUELINE_ASISTENCIA_B1_Y_PUNTUALIDAD_2026-10-14.docx (+PDF)"""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.3); s.bottom_margin = Cm(1.1); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR
def t(txt, bold=False, size=10, color=None, after=3):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def item(txt, prefix=None):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1.5); p.paragraph_format.left_indent = Cm(0.4)
    if prefix:
        r = p.add_run(prefix + ' '); r.bold = True; r.font.size = Pt(10)
    r = p.add_run(txt); r.font.size = Pt(10)
def caja(lines):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run('\n'.join(lines)); r.font.size = Pt(9.5); r.italic = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
def tabla(filas, anchos, fs=9.5):
    tb = doc.add_table(rows=len(filas), cols=len(filas[0])); tb.style = 'Table Grid'
    for i, fila in enumerate(filas):
        for j, v in enumerate(fila):
            c = tb.cell(i, j); c.width = Cm(anchos[j]); c.paragraphs[0].paragraph_format.space_after = Pt(0)
            r = c.paragraphs[0].add_run(v); r.font.size = Pt(fs)
            if i == 0: r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); shd(c, 'E54C09')
            elif j == 0: r.bold = True; shd(c, 'FFF8E7')
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('INSTRUCCIONES PARA JACQUELINE — ASISTENCIA DEL B1 Y PUNTUALIDAD DOCENTE'); r.bold = True; r.font.size = Pt(13.5); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Heiiu English Academy · 14 de octubre de 2026 · Uso interno · Lo ejecuta Jacqueline; Diana solo recibe el reporte'); r.font.size = Pt(9); r.font.color.rgb = GRIS

sec('PARTE 1 — EL B1 DE LA MAÑANA (4 estudiantes): el 1 a 1 lo hace Juan Diego; Jacqueline registra y cierra')
t('El grupo cambió de docente el lunes 13 y hay estudiantes que no están llegando. Con 4 estudiantes, cada ausencia es el 25% del grupo. Diana decidió que Juan Diego, que abrió el grupo, hable HOY con cada uno en un 1 a 1 (él tiene su propia hoja). Jacqueline no llama a los estudiantes; hace tres cosas con hora:', bold=True)
item('Le pasa a Juan Diego la lista de los 4 con la asistencia del lunes y el martes y el celular de cada uno.', '1. Antes de la 1:00 p.m.:')
item('Recibe de Juan Diego, por escrito, una línea por estudiante (causa en sus palabras y si vuelve mañana) y llena la tabla de abajo. Si a las 5:00 no ha llegado, se la pide.', '2. A las 5:00 p.m.:')
item('Lo que el 1 a 1 no resuelve lo toma Jacqueline con la tabla de causas: dinero, sin contacto, o un estudiante que escriba después pidiendo cambiar la hora o bajar el ritmo.', '3. Después:')
tabla([
 ['Estudiante', 'Lun 13', 'Mar 14', '1 a 1 (hora)', 'Causa (según Juan Diego)', '¿Vuelve mañana?', 'Acción de Jacqueline'],
 ['1', '', '', '', '', '', ''], ['2', '', '', '', '', '', ''], ['3', '', '', '', '', '', ''], ['4', '', '', '', '', '', ''],
], [2.2, 1.3, 1.3, 2.2, 5.0, 2.2, 3.0], fs=9)
t('Qué responde Jacqueline según la causa (cuando el estudiante le escriba a ella o cuando Juan Diego le reporte algo pendiente):', bold=True, after=1)
tabla([
 ['Causa', 'Acción'],
 ['El cambio de profe', 'Lo cierra Juan Diego en el 1 a 1. El docente actual ya se presentó el martes: no se vuelve a presentar ni pide disculpas por nada; al que faltó y vuelve, una frase de bienvenida y a la guía.'],
 ['El ritmo o la exigencia (confirmado hoy por el docente: "no tienen tiempo", "les da pena")', 'No se baja el ritmo. Se le recuerda el trato: el ritmo existe por la garantía por escrito; si cumple y no avanza, se le devuelve el nivel.'],
 ['"No tengo tiempo"', '"Son 3 minutos de video al día; la preparación son 20 o 30 minutos. Y desde mañana la tarea escrita de Gramática se acorta a la mitad: 15 o 20 minutos. En total, menos de una hora al día. Lo que no existe es aprender inglés sin hablar todos los días; eso ya lo sabe por lo que intentó antes."'],
 ['"Me da pena"', '"El video lo ve solo el profe, nadie de la clase. Y es exactamente para eso: la pena se gasta ahí, no delante de un jefe o un entrevistador. Desde mañana el video empieza con 3 frases que usted copia de alguien en internet; no arranca en blanco."'],
 ['El acento del profe nuevo ("no le entiendo")', 'Es parte del entrenamiento, no un defecto: en la vida real van a oír millones de acentos, y el oído se entrena en casa, no cambiando de profe. Desde esta semana la tarea diaria arranca con 2 minutos de un hablante con otro acento (LISTEN FIRST) y el video diario se abre con 3 frases de eso. Se le dice: "Si hoy te cuesta entenderle, en dos semanas vas a entender a cualquiera; eso es exactamente lo que estás comprando."'],
 ['Pide cambiar la hora de las 8:00', 'No se pregunta ni se negocia: matricularon a las 8:00 y ese es su horario. "Su horario es el de las 8:00, el que eligió al matricularse."'],
 ['Algo personal (trabajo, salud, dinero)', 'Se anota con fecha de regreso. Si es dinero, pasa a Experiencia al Cliente con el protocolo de cobranza, no al docente.'],
 ['Juan Diego no logró contacto hoy ni mañana', 'Mensaje escrito de Jacqueline el jueves con la frase de garantía y asistencia. Se reporta a Diana como "sin contacto".'],
], [4.0, 13.2])

t('Mensaje de Jacqueline al grupo del B1 (hoy, después de que Juan Diego reporte los 1 a 1):', bold=True, after=1)
caja(['"Equipo del B1: les hablo con franqueza. Son un grupo pequeño, de 4, y eso tiene dos caras: cada uno recibe más atención del profe,',
      'y cada ausencia pesa más. Con el cambio de profe el avance no se va a notar en una semana: toma tiempo, y hay que hacerlo.',
      'Y sobre el acento: acentos hay millones y el oído se entrena. Por eso desde esta semana la tarea arranca con 2 minutos de otro acento.',
      'Su horario es el de las 8:00, el que eligieron al matricularse, y ahí los esperamos mañana. Cualquier cosa que les complique venir,',
      'me la escriben a mí. Nos vemos a las 8:00."'])

sec('PARTE 2 — PUNTUALIDAD DOCENTE: una regla mecánica que corre sola desde el lunes 19/10')
t('La hora de inicio de cada clase es condición del servicio en el contrato docente, y el pago es por horas efectivamente impartidas. No se llama la atención: se registra y se liquida. Jacqueline lleva el registro; Diana lo ve los lunes.', bold=True)
item('A la hora exacta de inicio de cada clase, el docente envía al grupo de docentes la FOTO del tablero con la Frase del Día escrita. La hora del mensaje es la hora de inicio real. Sin foto = clase iniciada tarde.', 'Registro:')
item('Cada bloque de 15 minutos iniciado tarde se descuenta de la liquidación del mes (la fracción de hora no impartida no se paga). Hasta 5 minutos no cuenta. Tres clases tarde en el mes: llamado de atención por escrito de Diana. Ninguna situación se resuelve en el grupo: quien tenga una razón la escribe a Jacqueline ese mismo día.', 'Consecuencia:')
item('Jacqueline llena esta tabla cada día (toma 2 minutos) y la manda a Diana los lunes con la liquidación.', 'Tabla semanal:')
tabla([
 ['Día', 'Grupo', 'Docente (rol)', 'Hora de inicio', 'Hora de la foto', 'Minutos tarde', 'Bloques de 15 a descontar'],
 ['', '', '', '', '', '', ''], ['', '', '', '', '', '', ''], ['', '', '', '', '', '', ''],
], [1.6, 2.4, 3.2, 2.2, 2.4, 2.2, 3.2], fs=9)
t('Mensaje de Diana al grupo de docentes (se envía hoy; rige desde el lunes 19):', bold=True, after=1)
caja(['Equipo, desde el lunes 19 de octubre arranca el registro de inicio de clase. A la hora exacta de inicio, cada uno envía a este grupo',
      'la foto del tablero con la Frase del Día. Esa hora es la hora de inicio real. Como dice el contrato, se paga por horas efectivamente',
      'impartidas: cada bloque de 15 minutos iniciado tarde se descuenta en la liquidación del mes (hasta 5 minutos no cuenta).',
      'No es un regaño: es un registro, y corre igual para todos. Cualquier situación se escribe a Jacqueline el mismo día. Gracias.'])

sec('PARTE 3 — REPORTE DIARIO A DIANA (una sola línea, 12:30 p.m.)')
caja(['"B1 mañana: [x]/4 asistieron · 1 a 1 hechos por Juan Diego: [x] · causas: [palabra por cada uno] · docentes a tiempo hoy: [x]/[x]"'])
t('Esta semana (14 al 17/10) el reporte va todos los días. Desde la semana siguiente, solo los lunes en la reunión fija, salvo que un día falten 2 o más del B1: ese día se reporta de inmediato.', size=9.5, color=GRIS)

sec('CHECKLIST DE JACQUELINE — HOY 14/10')
for c in ['Antes de la 1:00 p.m.: lista de los 4 (asistencia lun/mar + celular) a Juan Diego.', 'A las 5:00 p.m.: recibir de Juan Diego la línea por estudiante y llenar la tabla.',
          'Mensaje al grupo del B1 (Parte 1) hoy, después del reporte de Juan Diego.', 'Enviar el mensaje de puntualidad al grupo de docentes (lo manda Diana).',
          'Reporte de una línea a Diana a las 12:30 p.m. desde mañana.']:
    item(c, '☐')

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\documentos_operativos\politicas\INSTRUCCIONES_JACQUELINE_ASISTENCIA_B1_Y_PUNTUALIDAD_2026-10-14.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
