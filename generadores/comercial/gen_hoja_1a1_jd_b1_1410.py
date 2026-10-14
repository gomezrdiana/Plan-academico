# -*- coding: utf-8 -*-
"""Hoja para Juan Diego: 1 a 1 de retención con los 4 estudiantes del B1 de la mañana (14/10/2026). 1 página, en usted.
Salida: documentos_operativos/politicas/HOJA_1A1_JUAN_DIEGO_B1_MANANA_2026-10-14.docx (+PDF)"""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(7); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR
def t(txt, bold=False, size=10, color=None, after=3):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
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
r = p.add_run('1 A 1 CON EL B1 DE LA MAÑANA — PARA JUAN DIEGO'); r.bold = True; r.font.size = Pt(13.5); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Heiiu English Academy · 14 de octubre de 2026 · Uso interno · Hoy, antes de las 5:00 p.m.'); r.font.size = Pt(9); r.font.color.rgb = GRIS

t('Usted abrió este grupo y ellos le creen. Desde el lunes 13 tienen profe nuevo en Gramática y hay estudiantes que no están llegando. Diana le pide una cosa concreta: hablar hoy con cada uno de los 4, uno por uno, 10 minutos, y mandarle a Jacqueline una línea por estudiante a las 5:00 p.m. Esto no es una clase ni una venta: es una conversación para que vuelvan mañana a las 8:00.', bold=True)

sec('1. QUÉ SÍ Y QUÉ NO')
tabla([
 ['Sí', 'No'],
 ['Escuchar primero. Preguntar qué pasó y anotar sus palabras.', 'Reabrir el cambio de profe o dar a entender que usted podría volver a dar el grupo.'],
 ['Respaldar al profe actual con nombre: usted lo conoce y sabe lo que hace.', 'Pedir disculpas en nombre de la academia o criticar al profe actual.'],
 ['Reconocer que el cambio cuesta y que en dos semanas se nota.', 'Bajar el ritmo, acortar la tarea por su cuenta o prometer que será más fácil.'],
 ['Repetir la hora: 8:00, la que eligieron al matricularse.', 'Preguntar si otra hora les sirve mejor. La hora no se negocia.'],
 ['Cerrar con "mañana a las 8:00".', 'Hablar de referidos, de bonos o del programa nuevo en esta llamada. Eso es otra conversación, otro día.'],
 ['Reportar a Jacqueline a las 5:00 p.m.', 'Comunicar notas, evaluaciones o quién va bien o mal. Eso es de coordinación.'],
], [8.4, 8.8])

sec('2. GUION (llamada; si puede verlos en la sede, mejor)')
caja(['"Hola, [nombre], le habla Juan Diego. Le llamo porque este grupo lo empecé yo y me importa cómo le va. No lo vimos en clase y quiero saber cómo está.',
      '1. ¿Qué pasó?',
      '2. ¿Hay algo del cambio que le complique: el profe nuevo, el ritmo, el acento? Dígamelo con confianza, para eso le llamo.',
      '3. ¿Mañana a las 8:00 va?"',
      'Cierre: "A [nombre del profe] lo conozco, sabe lo que hace y le va a exigir lo mismo que yo, porque usted puede. Yo sigo en la academia y nos vamos a cruzar.',
      'Lo único que le pido es que no falte: cada clase que se pierde cuesta más recuperarla que asistir. Mañana a las 8:00."'])

sec('3. QUÉ RESPONDE SI LE DICEN…')
tabla([
 ['Le dicen', 'Usted responde'],
 ['"No tengo tiempo para la tarea"', '"Son 3 minutos de video al día y 20 o 30 de preparación. Y desde mañana la tarea escrita de Gramática queda a la mitad: 15 o 20 minutos. Menos de una hora en total. Lo que no existe es aprender inglés sin hablar todos los días."'],
 ['"Me da pena grabarme"', '"El video lo ve solo el profe, nadie de la clase. Y es para eso: la pena se gasta ahí, no delante de un jefe o un entrevistador. Desde mañana el video arranca con 3 frases que usted copia de alguien en internet; no empieza en blanco."'],
 ['"No le entiendo el acento"', '"Acentos hay millones y el oído se entrena en casa, no cambiando de profe. Desde esta semana la tarea arranca con 2 minutos de otro acento. Si hoy le cuesta entenderle, en dos semanas entiende a cualquiera; eso es lo que está comprando."'],
 ['"Es muy duro / muy rápido"', '"El ritmo existe por la garantía por escrito: si usted cumple y no avanza, se le devuelve el nivel. Por eso no se baja."'],
 ['"¿Y usted no vuelve?"', '"Yo sigo en la academia, pero este grupo ya lo lleva [nombre del profe] y está en buenas manos. Lo que necesito es verlo mañana a las 8:00."'],
 ['Algo personal (trabajo, salud, dinero)', 'Se anota con fecha de regreso y se le pasa a Jacqueline. Si es dinero, no lo resuelve usted: "Eso lo ve Jacqueline con usted, yo le aviso hoy."'],
], [4.6, 12.6])

sec('4. REPORTE A JACQUELINE (5:00 p.m., una línea por estudiante)')
caja(['"[Nombre]: hablé [hora] · causa: [sus palabras] · ¿vuelve mañana?: sí / no / no contestó · pendiente para Jacqueline: [nada / dinero / fecha de regreso]"'])
t('Si alguno no contesta, un mensaje corto y se reintenta mañana a las 9:00 a.m. Si tampoco contesta, lo toma Jacqueline el jueves.', size=9.5, color=GRIS)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\documentos_operativos\politicas\HOJA_1A1_JUAN_DIEGO_B1_MANANA_2026-10-14.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
