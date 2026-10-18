# -*- coding: utf-8 -*-
"""Formato del RETO DE 15 DÍAS (20/10 al 3/11/2026) del ejecutivo de alianzas.
Hojas: EMPRESAS (20 filas con formato y desplegable de estado), REPORTE DIARIO (3 líneas por día, del 20/10 al 3/11),
INTERESADOS (registro de la charla, imprimible; datos personales solo aquí).
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/FORMATO_15_EMPRESAS_RETO.xlsx
Correr desde la raíz: python generadores/comercial/gen_formato_15_empresas.py"""
import datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial'
NAR = 'E54C09'; CREMA = 'FFF8E7'
HDR_FILL = PatternFill('solid', fgColor=NAR); CREMA_FILL = PatternFill('solid', fgColor=CREMA)
HDR_FONT = Font(name='Calibri', bold=True, color='FFFFFF', size=10)
TIT_FONT = Font(name='Calibri', bold=True, color=NAR, size=14)
NOTA_FONT = Font(name='Calibri', italic=True, color='666666', size=9)
thin = Side(style='thin', color='BFBFBF'); BORDE = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical='center')
CENT = Alignment(horizontal='center', vertical='center', wrap_text=True)

wb = Workbook()

# ------------------------------------------------------------ EMPRESAS
ws = wb.active; ws.title = 'EMPRESAS'
ws['A1'] = 'RETO DE 15 DÍAS · EMPRESAS (20/10 al 3/11/2026)'; ws['A1'].font = TIT_FONT
ws['A2'] = ('Toda empresa se registra aquí ANTES de la primera reunión. Empresas de 40 a 150 empleados donde el dueño o el gerente decide. '
            'Planilla al día antes de la llamada de las 8:00 a. m. Uso interno: los datos no se comparten.')
ws['A2'].font = NOTA_FONT; ws.merge_cells('A2:O2'); ws.row_dimensions[2].height = 28; ws['A2'].alignment = WRAP
cols = [('#', 5), ('Empresa', 24), ('Sector', 16), ('Nº empleados', 11), ('Decisor (nombre)', 22), ('Cargo', 16),
        ('Celular', 14), ('Cómo lo conoces', 18), ('Fecha contacto', 12), ('Fecha reunión', 12),
        ('Charla autorizada (sí/no, fecha)', 18), ('Interesados', 11), ('Inscritos pagados', 11), ('Estado', 18), ('Notas', 34)]
HR = 4
for i, (h, w) in enumerate(cols, 1):
    c = ws.cell(row=HR, column=i, value=h); c.fill = HDR_FILL; c.font = HDR_FONT; c.alignment = CENT; c.border = BORDE
    ws.column_dimensions[get_column_letter(i)].width = w
ws.row_dimensions[HR].height = 32
N = 20
estados = ['contactado', 'reunión agendada', 'reunión hecha', 'charla autorizada', 'charla hecha', 'inscribiendo', 'cerrado', 'descartado']
dv = DataValidation(type='list', formula1='"' + ','.join(estados) + '"', allow_blank=True,
                    showErrorMessage=True, errorTitle='Estado', error='Elige un estado de la lista.')
dv_si = DataValidation(type='whole', operator='greaterThanOrEqual', formula1='0', allow_blank=True,
                       showErrorMessage=True, error='Escribe un número entero.')
dv_fecha = DataValidation(type='date', operator='between', formula1='DATE(2026,10,1)', formula2='DATE(2026,12,31)', allow_blank=True,
                          showErrorMessage=True, error='Escribe una fecha (dd/mm/aaaa).')
ws.add_data_validation(dv); ws.add_data_validation(dv_si); ws.add_data_validation(dv_fecha)
for r in range(HR + 1, HR + 1 + N):
    for ci in range(1, len(cols) + 1):
        c = ws.cell(row=r, column=ci); c.border = BORDE; c.alignment = WRAP; c.font = Font(name='Calibri', size=10)
        if (r - HR) % 2 == 0: c.fill = CREMA_FILL
    ws.cell(row=r, column=1, value=r - HR).alignment = CENT
    for ci in (9, 10): ws.cell(row=r, column=ci).number_format = 'DD/MM/YYYY'
    ws.row_dimensions[r].height = 20
last = HR + N
dv.add(f'N{HR + 1}:N{last}')
dv_si.add(f'D{HR + 1}:D{last}'); dv_si.add(f'L{HR + 1}:M{last}')
dv_fecha.add(f'I{HR + 1}:J{last}')
tr = last + 1
ws.cell(row=tr, column=11, value='TOTALES').font = Font(name='Calibri', bold=True, color=NAR)
ws.cell(row=tr, column=12, value=f'=SUM(L{HR + 1}:L{last})').font = Font(name='Calibri', bold=True)
ws.cell(row=tr, column=13, value=f'=SUM(M{HR + 1}:M{last})').font = Font(name='Calibri', bold=True)
ws.cell(row=tr + 1, column=11, value='Empresas registradas').font = NOTA_FONT
ws.cell(row=tr + 1, column=12, value=f'=COUNTA(B{HR + 1}:B{last})')
ws.cell(row=tr + 2, column=11, value='Reuniones hechas o más').font = NOTA_FONT
ws.cell(row=tr + 2, column=12, value=f'=COUNTIF(N{HR + 1}:N{last},"reunión hecha")+COUNTIF(N{HR + 1}:N{last},"charla autorizada")+COUNTIF(N{HR + 1}:N{last},"charla hecha")+COUNTIF(N{HR + 1}:N{last},"inscribiendo")+COUNTIF(N{HR + 1}:N{last},"cerrado")')
ws.cell(row=tr + 3, column=11, value='Meta del reto (inscritos pagados)').font = NOTA_FONT
ws.cell(row=tr + 3, column=12, value=10)
ws.freeze_panes = ws.cell(row=HR + 1, column=3)
ws.page_setup.orientation = 'landscape'; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
ws.sheet_properties.pageSetUpPr.fitToPage = True

# ------------------------------------------------------------ REPORTE DIARIO
wr = wb.create_sheet('REPORTE DIARIO')
wr['A1'] = 'REPORTE DIARIO · se llena antes de la llamada de las 8:00 a. m.'; wr['A1'].font = TIT_FONT
wr['A2'] = ('Tres líneas por día. Inscritos pagados = inicial en la cuenta de Heiiu, verificada por coordinación. '
            'Corte: martes 3/11 a las 6:00 p. m. El lunes 2/11 es festivo.')
wr['A2'].font = NOTA_FONT; wr.merge_cells('A2:E2'); wr['A2'].alignment = WRAP; wr.row_dimensions[2].height = 28
hdr = [('Fecha', 13), ('Empresas contactadas hoy', 16), ('Reuniones hechas hoy', 16), ('Inscritos pagados acumulados', 18), ('Nota del día (1 línea)', 50)]
for i, (h, w) in enumerate(hdr, 1):
    c = wr.cell(row=4, column=i, value=h); c.fill = HDR_FILL; c.font = HDR_FONT; c.alignment = CENT; c.border = BORDE
    wr.column_dimensions[get_column_letter(i)].width = w
wr.row_dimensions[4].height = 32
dias = []
d = dt.date(2026, 10, 19)
while d <= dt.date(2026, 11, 3):
    if d.weekday() < 5: dias.append(d)
    d += dt.timedelta(days=1)
dv_n = DataValidation(type='whole', operator='greaterThanOrEqual', formula1='0', allow_blank=True, showErrorMessage=True, error='Número entero.')
wr.add_data_validation(dv_n)
for k, dia in enumerate(dias):
    r = 5 + k
    c = wr.cell(row=r, column=1, value=dia); c.number_format = 'DD/MM/YYYY'
    for ci in range(1, 6):
        cc = wr.cell(row=r, column=ci); cc.border = BORDE; cc.alignment = WRAP; cc.font = Font(name='Calibri', size=10)
        if k % 2 == 1: cc.fill = CREMA_FILL
    if dia == dt.date(2026, 11, 2):
        wr.cell(row=r, column=5, value='Festivo: sin contacto a clientes')
    if dia == dt.date(2026, 11, 3):
        wr.cell(row=r, column=5, value='CORTE 6:00 p. m.')
    wr.row_dimensions[r].height = 20
lr = 4 + len(dias)
dv_n.add(f'B5:D{lr}')
wr.cell(row=lr + 1, column=1, value='TOTAL').font = Font(name='Calibri', bold=True, color=NAR)
wr.cell(row=lr + 1, column=2, value=f'=SUM(B5:B{lr})').font = Font(name='Calibri', bold=True)
wr.cell(row=lr + 1, column=3, value=f'=SUM(C5:C{lr})').font = Font(name='Calibri', bold=True)
wr.cell(row=lr + 1, column=4, value=f'=MAX(D5:D{lr})').font = Font(name='Calibri', bold=True)
wr.cell(row=lr + 3, column=1, value='Ritmo mínimo').font = Font(name='Calibri', bold=True, color=NAR)
for j, txt in enumerate(['Mar 20/10: 15 empresas contactadas con el decisor (acumulado).',
                         'Vie 23/10: 8 reuniones con decisor y 3 charlas autorizadas para la semana 2.',
                         'Mar 3/11, 6:00 p. m.: 10 inscritos pagados.']):
    wr.cell(row=lr + 4 + j, column=1, value=txt).font = NOTA_FONT
wr.freeze_panes = 'B5'

# ------------------------------------------------------------ INTERESADOS
wi = wb.create_sheet('INTERESADOS')
wi['A1'] = 'INTERESADOS · CHARLA HEIIU'; wi['A1'].font = TIT_FONT
wi['A2'] = 'Empresa: ______________________________   Fecha de la charla: ____ / ____ / 2026'; wi['A2'].font = Font(name='Calibri', size=10)
wi['A3'] = ('Al escribir mis datos autorizo a Heiiu English Academy (Global Teacher S.A.S.) a contactarme por este celular para informarme '
            'sobre sus programas, conforme a la Ley 1581 de 2012. Puedo pedir la actualización o supresión de mis datos escribiendo a la academia.')
wi['A3'].font = NOTA_FONT; wi.merge_cells('A3:G3'); wi['A3'].alignment = WRAP; wi.row_dimensions[3].height = 30
hi = [('#', 4), ('Nombre completo', 30), ('Celular', 15), ('Para qué el inglés (trabajo / viaje / estudio / hijo)', 22),
      ('Jornada que le sirve', 16), ('Seguimiento (día y hora)', 16), ('Inicial pagada (sí/no, fecha)', 16)]
for i, (h, w) in enumerate(hi, 1):
    c = wi.cell(row=5, column=i, value=h); c.fill = HDR_FILL; c.font = HDR_FONT; c.alignment = CENT; c.border = BORDE
    wi.column_dimensions[get_column_letter(i)].width = w
wi.row_dimensions[5].height = 36
for k in range(25):
    r = 6 + k
    wi.cell(row=r, column=1, value=k + 1).alignment = CENT
    for ci in range(1, 8):
        cc = wi.cell(row=r, column=ci); cc.border = BORDE; cc.font = Font(name='Calibri', size=10)
        if k % 2 == 1: cc.fill = CREMA_FILL
    wi.row_dimensions[r].height = 22
wi.page_setup.orientation = 'landscape'; wi.page_setup.fitToWidth = 1; wi.page_setup.fitToHeight = 1
wi.sheet_properties.pageSetUpPr.fitToPage = True

out = BASE + r'\FORMATO_15_EMPRESAS_RETO.xlsx'
try:
    wb.save(out); print('OK', out)
except PermissionError:
    wb.save(out.replace('.xlsx', '_v2.xlsx')); print('ABIERTO -> _v2')
