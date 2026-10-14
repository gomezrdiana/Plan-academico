# -*- coding: utf-8 -*-
"""Ficha de cifras que llena el candidato (Ejecutivo/a Senior de Alianzas) en la reunión del filtro 2, 1 página.
Reutilizable para cualquier candidato (sin nombre). Incluye autorización de datos y referencias (Ley 1581).
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/FICHA_CIFRAS_CANDIDATO_ALIANZAS.docx (+PDF)"""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0); s.left_margin = Cm(1.6); s.right_margin = Cm(1.6)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(9.5)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NAR
def t(txt, size=9.5, color=None, after=2, bold=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def tabla(filas, anchos, fs=9, alto=None):
    tb = doc.add_table(rows=len(filas), cols=len(filas[0])); tb.style = 'Table Grid'
    for i, fila in enumerate(filas):
        for j, v in enumerate(fila):
            c = tb.cell(i, j); c.width = Cm(anchos[j]); c.paragraphs[0].paragraph_format.space_after = Pt(0)
            r = c.paragraphs[0].add_run(v); r.font.size = Pt(fs)
            if i == 0: r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); shd(c, 'E54C09')
            elif j == 0: r.bold = True; shd(c, 'FFF8E7')
        if alto and i > 0: tb.rows[i].height = Cm(alto)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('FICHA DE TRAYECTORIA COMERCIAL'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(4)
r = p.add_run('Ejecutivo(a) Senior de Alianzas Empresariales · Heiiu English Academy · Bucaramanga'); r.font.size = Pt(9); r.font.color.rgb = GRIS
t('Nombre: ________________________________________    Celular: __________________    Fecha: ____ / ____ / 2026', after=4)
t('Gracias por llenarla con números exactos, no con rangos. Lo que escribas aquí se contrasta después con tus soportes (desprendibles o anexo de comisiones) y con tus jefes directos; por eso vale más un número real que uno bonito. Si no recuerdas un dato, escribe "no recuerdo": es mejor que inventarlo.', size=9, color=GRIS, after=4)

sec('1. Tus últimas tres empresas (la más reciente primero)')
tabla([
 ['Dato', 'Empresa 1 (la más reciente)', 'Empresa 2', 'Empresa 3'],
 ['Empresa y cargo', '', '', ''],
 ['Desde / hasta (mes y año)', '', '', ''],
 ['Qué vendías y a quién (empresa, aliado, persona)', '', '', ''],
 ['Meta mensual (¿en qué: desembolsos, colocación, ventas, aliados?)', '', '', ''],
 ['% de cumplimiento del último año (promedio y el mes más bajo)', '', '', ''],
 ['Ticket promedio (por aliado, crédito o venta)', '', '', ''],
 ['Clientes o aliados nuevos firmados al mes (promedio)', '', '', ''],
 ['Ciclo de venta: del primer contacto a la firma (días o semanas)', '', '', ''],
 ['Ingreso mensual total que alcanzaste (fijo + comisiones, un mes bueno y uno normal)', '', '', ''],
 ['Motivo real de tu salida', '', '', ''],
 ['Jefe directo: nombre, cargo y celular', '', '', ''],
], [5.2, 4.2, 4.2, 4.2], fs=8.5, alto=0.75)

sec('2. Lo que traes a este cargo')
tabla([
 ['Pregunta', 'Tu respuesta'],
 ['De tus contactos actuales (empresas, clínicas, aliados), ¿con cuántos dueños o gerentes podrías sentarte en las próximas 2 semanas? Escribe el número y 3 nombres de empresa.', ''],
 ['¿Cuántos de esos contactos movían volumen de verdad en tu última empresa?', ''],
 ['La última cartera que construiste desde cero: ¿cómo conseguiste las primeras 10 empresas y en qué números cerraste el primer trimestre?', ''],
 ['¿Qué te haría quedarte 3 años en un cargo?', ''],
 ['Aspiración salarial: fijo ____________ · total mensual con comisiones ____________', ''],
 ['¿Desde qué fecha exacta puedes empezar, presencial en Bucaramanga?', ''],
], [8.6, 9.2], fs=8.5, alto=1.1)

sec('3. Autorización de datos y referencias')
t('Autorizo a GLOBAL TEACHER S.A.S. (Heiiu English Academy) a tratar los datos de esta ficha y de mi hoja de vida con la finalidad exclusiva del proceso de selección, a contactar a los jefes directos que indiqué como referencia y a verificar los soportes que entregue, conforme a la Ley 1581 de 2012. Puedo pedir la corrección o eliminación de mis datos en cualquier momento escribiendo a la academia. Declaro que la información consignada es verdadera.', size=8.5, after=6)
t('Firma: ______________________________          C.C. ______________________          Fecha: ____ / ____ / 2026', size=9)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\FICHA_CIFRAS_CANDIDATO_ALIANZAS.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
