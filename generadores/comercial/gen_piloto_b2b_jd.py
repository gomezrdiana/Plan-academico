# -*- coding: utf-8 -*-
"""Piloto B2B del docente que abre alianzas (60 dias): tablero de metricas (docx) + tracker (xlsx con resumen automatico).
Documentos por ROL (sin nombres). Salida: recursos/comercial/B2B/"""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\B2B'
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x77, 0x77, 0x77)

# ---------- DOCX ----------
d = Document()
for s in d.sections:
    s.top_margin = Cm(1.4); s.bottom_margin = Cm(1.2); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)

def h(txt, size=12, before=8):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAR

def t(txt, bold=False, after=3, size=10, color=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.bold = bold; r.font.size = Pt(size)
    if color: r.font.color.rgb = color

def tabla(filas, anchos):
    tb = d.add_table(rows=len(filas), cols=len(filas[0])); tb.style = 'Table Grid'
    for i, fila in enumerate(filas):
        for j, txt in enumerate(fila):
            c = tb.rows[i].cells[j]; c.width = Cm(anchos[j])
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            r = p.add_run(txt); r.font.size = Pt(9)
            if i == 0: r.bold = True; shd(c, 'FFF8E7')
            elif j == 0: r.bold = True
    d.add_paragraph().paragraph_format.space_after = Pt(1)

h('PILOTO DE ALIANZAS EMPRESARIALES — TABLERO DE MÉTRICAS (60 DÍAS)', 14, before=0)
t('Para el docente habilitado comercialmente que abre alianzas (programa Heiiu Business Partner: beneficios del Fondo de Becas para los colaboradores de la empresa aliada, sin costo para la empresa). Se acuerda antes de la primera visita y se revisa cada viernes. Documento por rol.', color=GRIS, size=9, after=6)

h('1. Lo que no cambia (el marco de agosto)')
for x in [
    'Sale a visitar SOLO con el contrato docente v3.1 y el anexo de habilitación comercial firmados.',
    'Abre, presenta y cierra el convenio de alianza con el formato estándar sin cambiarle nada (no tiene costo ni condiciones negociables); gerencia lo firma por la academia. NO negocia ni cotiza: la formación pagada y todo lo que se salga del formato lo cierra gerencia.',
    'Empresas NUEVAS que él consiga. Las tibias (empleadores de estudiantes, aliadas ya en conversación) las trabaja gerencia.',
    'Las visitas no chocan con sus clases. El compromiso comercial no puede costarle calidad docente.',
    'Comisión según el anexo firmado (canal propio: sobre el recaudo de las matrículas que lleguen por alianzas que él abrió). Se liquida mensual contra el reporte de ingresos.',
]:
    t('• ' + x, after=2)

h('2. Las métricas (actividad primero, resultado después)')
tabla([
    ['Métrica', 'Qué cuenta', 'Meta por semana', 'Meta a 60 días'],
    ['Empresas contactadas', 'Primer contacto real con un decisor (gerente, RR. HH., dueño): llamada, visita o mensaje con respuesta. No cuenta dejar una carta en recepción.', '3', '10 (mínimo) · 20 (bueno)'],
    ['Reuniones logradas', 'Reunión agendada y realizada con el decisor, con la carta de alianza presentada.', '1-2', '5 (mínimo) · 10 (bueno)'],
    ['Convenios firmados', 'Convenio Heiiu Business Partner estándar firmado por la empresa (y por gerencia por la academia).', '—', '3 (mínimo) · 5 (bueno)'],
    ['Reuniones con gerencia', 'Gerentes que pidieron formación paga y quedaron agendados con gerencia (él no cotiza).', '—', '2 o más'],
    ['Leads que llegan', 'Personas que escriben o llegan a la sede por una beca de alianza (con el nombre de la empresa).', '—', '10 o más'],
    ['Matrículas por alianza', 'Matrículas efectivas y recaudadas que vienen de una empresa que él abrió. Es lo que paga comisión.', '—', '3 o más'],
], [3.3, 7.6, 2.6, 3.8])

h('3. Cómo se mide: el tracker y el reporte del viernes')
t('Él llena el tracker (una fila por empresa: contacto, fecha, estado, próximo paso con fecha) y cada viernes manda a gerencia una foto o el archivo con dos líneas por empresa. La hoja RESUMEN del tracker calcula sola las métricas de arriba. Lo que no está en el tracker no cuenta ni paga comisión.', after=4)

h('3-BIS. La rutina diaria (sin reunión)')
t('Todos los días hábiles, a las 6 PM (o antes de su clase de la noche), él manda a gerencia UN mensaje de tres líneas:', after=2)
t('"Hoy: contacté [N] empresas ([nombres]). Reuniones: [N] ([empresa, día y hora]). Convenios / agendados con gerencia: [N]. · Mañana: [qué va a hacer, con nombres]. · Necesito de ti: [nada / una cosa concreta]."', bold=True, after=3)
t('Gerencia lo lee en dos minutos, responde una línea y resuelve lo pedido en menos de 24 horas. Si un día no llega el mensaje, se pide. Si pasan tres días sin un contacto nuevo, se habla ese mismo día. El tracker se actualiza a diario; el viernes hay una llamada de 15 minutos con el tracker en pantalla para revisar la semana y ajustar el guion.', after=4)

h('4. Los dos cortes')
tabla([
    ['Corte', 'Qué se mira', 'Si va bien', 'Si no va'],
    ['Día 30', 'Actividad: contactadas y reuniones. Resultado mínimo: 1 convenio firmado o 3 reuniones con decisor.', 'Sigue; se ajusta el guion con lo que aprendió.', 'Se revisa juntos qué está fallando (puerta, discurso, público). Una semana más de prueba con el ajuste; si tampoco, se cierra el piloto sin drama.'],
    ['Día 60', 'Resultado: convenios firmados y matrículas por alianza.', '3 convenios o 3 matrículas → se formaliza el rol "docente + desarrollo comercial" con metas trimestrales y el anexo se renueva.', 'Se agradece, se documenta lo aprendido, y él sigue siendo docente. El material y los contactos quedan en la academia (contrato con IP).'],
], [1.6, 6.0, 4.9, 4.8])

h('5. Lo que gerencia pone')
for x in ['Material listo: carta de alianza v2, términos, mini-convenio revisado por contaduría, tarifario cerrado.', 'Role-play antes de la primera visita (gerente difícil: "¿qué cuesta?", "¿qué ganan?", "deme el descuento en plata"). Sale cuando pase sin regalar nada.', 'Respuesta en menos de 24 horas a cada gerente que él agende.', 'Liquidación de comisión mensual, transparente, contra el reporte de ingresos.']:
    t('• ' + x, after=2)

d.save(OUT + r'\PILOTO_B2B_TABLERO_METRICAS.docx'); print('OK tablero')

# ---------- XLSX TRACKER ----------
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'TRACKER'
cols = ['Empresa', 'Sector', 'Contacto (nombre y cargo)', 'Teléfono / correo', 'Fecha primer contacto', 'Canal (llamada / visita / mensaje / referido)', 'Estado', 'Fecha reunión', 'Próximo paso', 'Fecha próximo paso', 'Convenio firmado (fecha)', 'Nº becas', 'Reunión con gerencia (fecha)', 'Leads llegados', 'Matrículas', 'Notas']
ws.append(cols)
for c in ws[1]: c.font = Font(bold=True); c.fill = PatternFill('solid', fgColor='FFF8E7'); c.alignment = Alignment(wrap_text=True, vertical='top')
anchos = [24, 14, 26, 22, 14, 18, 20, 12, 28, 12, 14, 8, 14, 10, 10, 30]
for i, a in enumerate(anchos, 1): ws.column_dimensions[get_column_letter(i)].width = a
ws.row_dimensions[1].height = 42
estados = '"Por contactar,Contactada (con respuesta),Reunión agendada,Reunión hecha,Convenio firmado,Pasó a gerencia (formación paga),No interesada,Sin respuesta"'
dv = DataValidation(type='list', formula1=estados, allow_blank=True); ws.add_data_validation(dv); dv.add('G2:G300')
ws.freeze_panes = 'B2'

rs = wb.create_sheet('RESUMEN')
rs['A1'] = 'RESUMEN DEL PILOTO (se calcula solo desde la hoja TRACKER)'; rs['A1'].font = Font(bold=True, size=12)
filas = [
    ('Empresas en el tracker', '=COUNTA(TRACKER!A2:A300)'),
    ('Empresas contactadas (con respuesta)', '=COUNTIFS(TRACKER!G2:G300,"<>Por contactar",TRACKER!G2:G300,"<>Sin respuesta",TRACKER!G2:G300,"<>")'),
    ('Reuniones hechas', '=COUNTIF(TRACKER!H2:H300,"<>")'),
    ('Convenios firmados', '=COUNTIF(TRACKER!K2:K300,"<>")'),
    ('Becas comprometidas', '=SUM(TRACKER!L2:L300)'),
    ('Reuniones con gerencia (formación paga)', '=COUNTIF(TRACKER!M2:M300,"<>")'),
    ('Leads llegados por alianzas', '=SUM(TRACKER!N2:N300)'),
    ('Matrículas por alianza', '=SUM(TRACKER!O2:O300)'),
    ('Tasa contactada → reunión', '=IF(B3=0,0,B4/B3)'),
    ('Tasa reunión → convenio', '=IF(B4=0,0,B5/B4)'),
]
rs.append([]);
for a, f in filas: rs.append([a, f])
for r in range(3, 3 + len(filas)): rs.cell(row=r, column=1).font = Font(bold=True)
rs['B11'].number_format = '0%'; rs['B12'].number_format = '0%'
rs.column_dimensions['A'].width = 42; rs.column_dimensions['B'].width = 14
rs.append([]); rs.append(['Metas a 60 días: 10 contactadas · 5 reuniones · 3 convenios · 2 reuniones con gerencia · 10 leads · 3 matrículas. Cortes: día 30 y día 60.'])
wb.save(OUT + r'\PILOTO_B2B_TRACKER.xlsx'); print('OK tracker')
