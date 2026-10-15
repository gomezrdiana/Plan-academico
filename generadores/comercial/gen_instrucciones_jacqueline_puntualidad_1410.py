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
r = p.add_run('INSTRUCCIONES PARA JACQUELINE — PUNTUALIDAD DOCENTE'); r.bold = True; r.font.size = Pt(13.5); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Heiiu English Academy · 14 de octubre de 2026 · Uso interno · Lo ejecuta Jacqueline; Diana solo recibe el reporte'); r.font.size = Pt(9); r.font.color.rgb = GRIS

sec('PARTE 1 — PUNTUALIDAD DOCENTE: una regla mecánica que corre sola desde el lunes 19/10')
t('La hora de inicio de cada clase es condición del servicio en el contrato docente, y el pago es por horas efectivamente impartidas. No se llama la atención: se registra y se liquida. Jacqueline lleva el registro; Diana lo ve los lunes.', bold=True)
item('Jacqueline anota en la tabla la hora a la que cada docente entra al salón, en cada clase. Esa es la hora de inicio real y la única prueba. No le pide nada al docente ni lo llama: anota. La Frase del Día debe estar en el tablero antes de que entre el primer estudiante; la foto al grupo de docentes es opcional y no sirve como prueba de hora.', 'Registro:')
item('Llegar tarde es llegar tarde: desde el minuto 1 queda registrado como clase iniciada tarde. Tres clases tarde en el mes: llamado de atención por escrito de Diana. El descuento corre por bloques: cada bloque de 15 minutos iniciado tarde se descuenta de la liquidación del mes (la fracción de hora no impartida no se paga). Ninguna situación se resuelve en el grupo: quien tenga una razón la escribe a Jacqueline ese mismo día.', 'Consecuencia:')
item('Jacqueline llena esta tabla cada día (toma 2 minutos) y la manda a Diana los lunes con la liquidación.', 'Tabla semanal:')
tabla([
 ['Día', 'Grupo', 'Docente (rol)', 'Hora de inicio', 'Hora de llegada (Jacqueline)', 'Minutos tarde', 'Bloques de 15 a descontar'],
 ['', '', '', '', '', '', ''], ['', '', '', '', '', '', ''], ['', '', '', '', '', '', ''],
], [1.6, 2.4, 3.2, 2.2, 2.4, 2.2, 3.2], fs=9)
t('Mensaje de Diana al grupo de docentes (se envía hoy; rige desde el lunes 19):', bold=True, after=1)
caja(['Profesores, les quiero recalcar lo que estamos construyendo. El programa que he venido desarrollando no busca solo enseñar inglés: busca formar al',
      'estudiante desde el ser. Es un programa distinto al de cualquier academia, y solo funciona si todos lo ejecutamos igual. Si no, lo que vendemos en la',
      'parte comercial no se ve en el aula y no cumplimos lo que prometimos.',
      'Hoy el programa evolucionó a esto: vendemos un entrenamiento tipo batallón, un bootcamp. Nada de eso es fácil. La competencia vende inglés fácil,',
      'flexible y divertido; nosotros vendemos lo contrario: mentoría, acompañamiento, constancia, disciplina y, sí, algo de dolor. Y lo que repiten los',
      'grandes, Steve Jobs, Elon Musk: para estar en el top hay que rodearse de los top y hacer cosas top. Uno se junta con top y es top. Punto.',
      'Por eso nos rodeamos de gente emprendedora, líder, que quiere estar ahí arriba. Y por eso cada uno de nosotros tiene que ser top en lo suyo: un estudiante que paga por ser top no puede tener un profe promedio.',
      'Eso lo tenemos que poder expresar todos. Estamos firmando garantías y un trabajo duro: video todos los días, asistencia, un ritmo que no se baja.',
      'Le pedimos al estudiante disciplina de soldado porque quiere subir de rango: un ascenso, una entrevista, una visa. Y un soldado así necesita un líder',
      'que llegue antes que él. Un coach que llega tarde no puede exigir puntualidad, ni tarea, ni ritmo: pierde la autoridad en el primer minuto.',
      'Pero no podemos tener a Jacqueline encima de ustedes pidiéndoles que lleguen a tiempo o llamándolos porque no han llegado. Eso no es',
      'comportamiento top. No es el trabajo de Jacqueline.',
      'Por eso desde el lunes 19 de octubre arranca el registro de inicio de clase. Jacqueline anota la hora a la que cada uno entra al salón; esa es la hora',
      'de inicio real. No les va a pedir nada ni a llamarlos: anota, y ya. La Frase del Día tiene que estar en el tablero antes de que entre el primer',
      'estudiante; la foto al grupo la pueden mandar si quieren, pero no es la prueba. Llegar tarde es llegar tarde: desde el primer minuto queda registrado. Como dice el contrato, se paga por horas efectivamente impartidas: cada bloque',
      'de 15 minutos iniciado tarde se descuenta en la liquidación del mes. Corre igual para todos. Cualquier situación se escribe a Jacqueline el mismo día.',
      'El profe que está a las 7:50 con la frase en el tablero ya ganó la clase antes de empezarla. Así se lidera a alguien que quiere subir de rango. Gracias.'])

sec('PARTE 2 — REPORTE DIARIO A DIANA (una sola línea, 12:30 p.m.)')
caja(['"Hoy: [x] clases · docentes a tiempo: [x]/[x] · tarde: [rol del docente, minutos]"'])
t('Esta semana (14 al 17/10) el reporte va todos los días para que la rutina quede montada antes del lunes 19. Desde la semana siguiente, solo los lunes con la tabla semanal, salvo que un docente inicie 15 minutos o más tarde: ese día se reporta de inmediato.', size=9.5, color=GRIS)

sec('CHECKLIST DE JACQUELINE — HOY 14/10')
for c in ['Leer la Parte 1 y confirmar a Diana que la entendió.', 'Diana envía hoy el mensaje de puntualidad al grupo de docentes; Jacqueline queda atenta a lo que respondan por privado.',
          'Mañana: anotar la hora de llegada de cada docente en la tabla semanal (aunque la regla rija desde el lunes 19, la tabla se empieza a llenar ya).',
          'Reporte de una línea a Diana a las 12:30 p.m. desde mañana.']:
    item(c, '☐')

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\documentos_operativos\politicas\INSTRUCCIONES_JACQUELINE_PUNTUALIDAD_DOCENTE_2026-10-14.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
