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

sec('PARTE 1 — EL B1 DE LA MAÑANA (4 estudiantes): averiguar la causa HOY, no suponerla')
t('El grupo cambió de docente el lunes 13 y hay estudiantes que no están llegando. Con 4 estudiantes, cada ausencia es el 25% del grupo. Hoy mismo, antes de las 5:00 p.m., Jacqueline llama a CADA ausente (llamada, no mensaje; si no contesta, un mensaje y se reintenta mañana a las 9:00 a.m.).', bold=True)
t('Guion de la llamada (3 preguntas, se anotan las respuestas tal cual):', bold=True, after=1)
caja(['"Hola [nombre], te habla [nombre], de Heiiu. Te llamo porque no te vimos en clase y queremos saber cómo estás.',
      '1. ¿Qué pasó hoy?',
      '2. ¿Vuelves mañana a las 8:00?',
      '3. ¿Hay algo del cambio que te complique: el profe nuevo, el ritmo, el acento? Dímelo con confianza, para eso te llamo."',
      'Cierre: "Te esperamos mañana a las 8:00. Tu avance queda registrado y tu garantía depende de tu asistencia; por eso te llamo hoy y no en un mes."'])
t('Lo que NO se dice esta semana: amenazas con el contrato, "si no vienes pierdes la garantía", ni "el profe anterior ya no está". Se escucha y se anota.', size=9.5, color=GRIS)
tabla([
 ['Estudiante', 'Lun 13', 'Mar 14', 'Llamado (hora)', 'Causa (sus palabras)', '¿Vuelve mañana?', 'Acción'],
 ['1', '', '', '', '', '', ''], ['2', '', '', '', '', '', ''], ['3', '', '', '', '', '', ''], ['4', '', '', '', '', '', ''],
], [2.2, 1.3, 1.3, 2.2, 5.0, 2.2, 3.0], fs=9)
t('Qué hacer según la causa (la decisión la toma Jacqueline):', bold=True, after=1)
tabla([
 ['Causa', 'Acción'],
 ['El cambio de profe', 'Hoy: el docente anterior manda un audio de 30 segundos al grupo (texto abajo). Mañana: el docente actual se presenta 5 minutos antes de empezar la guía, sin pedir disculpas por nada: quién es, cómo trabaja, qué espera de ellos.'],
 ['El ritmo o la exigencia', 'No se baja el ritmo. Se le recuerda el trato: el ritmo existe por la garantía por escrito; si cumple y no avanza, se le devuelve el nivel. Se le ofrece hablar 10 minutos con el docente actual al final de la clase de mañana.'],
 ['El acento del profe nuevo ("no le entiendo")', 'Es parte del entrenamiento, no un defecto: en la vida real van a oír millones de acentos, y el oído se entrena en casa, no cambiando de profe. Desde esta semana la tarea diaria arranca con 2 minutos de un hablante con otro acento (LISTEN FIRST) y el video diario se abre con 3 frases de eso. Se le dice: "Si hoy te cuesta entenderle, en dos semanas vas a entender a cualquiera; eso es exactamente lo que estás comprando."'],
 ['Algo personal (trabajo, salud, dinero)', 'Se anota con fecha de regreso. Si es dinero, pasa a Experiencia al Cliente con el protocolo de cobranza, no al docente.'],
 ['No contesta ni hoy ni mañana', 'Mensaje escrito el jueves con la frase de garantía y asistencia. Se reporta a gerencia como "sin contacto".'],
], [4.0, 13.2])
t('Audio del docente anterior al grupo (lo graba él hoy; Jacqueline se lo pide y lo reenvía si él no está en el grupo):', bold=True, after=1)
caja(['"Hola, equipo. Les hablo porque este grupo lo empecé yo y me importa cómo les va. Desde esta semana su profe de gramática es [nombre]:',
      'lo conozco, sabe lo que hace y va a exigirles lo mismo que yo, porque ustedes pueden. Yo sigo en la academia y nos vamos a cruzar.',
      'Lo único que les pido es que no falten: cada clase que se pierden es más difícil de recuperar que de asistir. Nos vemos."'])
t('Presentación del docente actual (mañana, 5 minutos, antes de la guía): quién es, dónde aprendió, cómo trabaja (de pie, hablando, corrigiendo), qué espera (video diario, tarea, puntualidad) y una frase de cierre: "Mi trabajo es que salgan hablando; el de ustedes, venir y entrenar". Sin disculparse por el acento ni por el cambio.', size=9.5, color=GRIS)

t('Mensaje de Jacqueline al grupo del B1 (hoy, después de las llamadas; también sirve como cierre de cada llamada):', bold=True, after=1)
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
caja(['"B1 mañana: [x]/4 asistieron · ausentes llamados: [x] · causas: [palabra por cada uno] · docentes a tiempo hoy: [x]/[x]"'])
t('Esta semana (14 al 17/10) el reporte va todos los días. Desde la semana siguiente, solo los lunes en la reunión fija, salvo que un día falten 2 o más del B1: ese día se reporta de inmediato.', size=9.5, color=GRIS)

sec('CHECKLIST DE JACQUELINE — HOY 14/10')
for c in ['Llamar a cada ausente del B1 antes de las 5:00 p.m. y llenar la tabla.', 'Pedir hoy el audio al docente anterior y reenviarlo al grupo del B1.',
          'Avisar al docente actual que mañana abre con 5 minutos de presentación.', 'Enviar el mensaje de puntualidad al grupo de docentes (lo manda Diana).',
          'Mensaje al grupo del B1 (Parte 1) hoy, después de las llamadas.', 'Reporte de una línea a Diana a las 12:30 p.m. desde mañana.']:
    item(c, '☐')

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\documentos_operativos\politicas\INSTRUCCIONES_JACQUELINE_ASISTENCIA_B1_Y_PUNTUALIDAD_2026-10-14.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
