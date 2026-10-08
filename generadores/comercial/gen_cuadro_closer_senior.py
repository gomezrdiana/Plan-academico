# -*- coding: utf-8 -*-
"""Cuadro de ingreso del closer de planta perfil senior (propuesta 08/10/2026): cuanto gana cada mes segun matriculas cerradas,
en dos versiones de los meses 1-2 (A piso garantizado / B basico + bono + comision).
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/CUADRO_INGRESO_CLOSER_SENIOR.xlsx"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

EQ = 2_990_000; COM = 0.07; COM_UNIT = EQ * COM          # $209.300 por matricula
BASICO = {1: 2_000_000, 2: 2_000_000, 3: 2_000_000, 4: 2_300_000, 5: 2_300_000, 6: 2_300_000, 7: 2_600_000}
BONO = 1_500_000; GARANTIA = 3_500_000
META = {1: 4, 2: 6, 3: 8, 4: 10, 5: 10, 6: 10, 7: 12}
VENTAS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]
FILAS = [(1, 'Mes 1'), (2, 'Mes 2'), (3, 'Mes 3'), (4, 'Meses 4-6'), (7, 'Meses 7-12')]

def ingreso(mes, n, version):
    b = BASICO[min(mes, 7)]; com = n * COM_UNIT
    if mes <= 2:
        return max(b + com, GARANTIA) if version == 'A' else b + BONO + com
    return b + com

H = Font(bold=True, color='FFFFFF'); F = PatternFill('solid', fgColor='E54C09'); C = PatternFill('solid', fgColor='FFF8E7'); G = PatternFill('solid', fgColor='EEEEEE')
thin = Side(style='thin', color='CCCCCC'); B = Border(left=thin, right=thin, top=thin, bottom=thin)
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'CUADRO'
ws['A1'] = 'CLOSER DE PLANTA (PERFIL SENIOR) — CUÁNTO GANA CADA MES SEGÚN LAS MATRÍCULAS QUE CIERRE · propuesta 08/10/2026'; ws['A1'].font = Font(bold=True, size=13, color='E54C09')
ws['A2'] = (f'1 matrícula = ${EQ:,.0f} de recaudo (un Arranque). Comisión {COM:.0%} del recaudo desde la primera venta = ${COM_UNIT:,.0f} por matrícula. '
            f'Básico $2.000.000 (sube a $2.300.000 en el mes 4 y a $2.600.000 en el mes 7, por resultados). Meses 1 y 2: ingreso garantizado ${GARANTIA:,.0f} si cumple actividad (5 citas atendidas por semana). '
            'La celda sombreada es la META del mes. Comisión sobre RECAUDO: la de una venta a cuotas sigue entrando los meses siguientes.')
ws['A2'].alignment = Alignment(wrap_text=True); ws.merge_cells('A2:P2'); ws.row_dimensions[2].height = 60

def tabla(r0, titulo, version, nota):
    ws.cell(row=r0, column=1, value=titulo).font = Font(bold=True, size=12, color='E54C09')
    ws.cell(row=r0 + 1, column=1, value=nota).alignment = Alignment(wrap_text=True); ws.merge_cells(start_row=r0 + 1, start_column=1, end_row=r0 + 1, end_column=16); ws.row_dimensions[r0 + 1].height = 30
    hdr = ['Mes', 'Meta', 'Básico'] + [f'Vende {n}' for n in VENTAS]
    for j, h in enumerate(hdr, 1):
        c = ws.cell(row=r0 + 2, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center'); c.border = B
    for i, (m, lab) in enumerate(FILAS, r0 + 3):
        ws.cell(row=i, column=1, value=lab).border = B
        ws.cell(row=i, column=2, value=META[m]).border = B
        c = ws.cell(row=i, column=3, value=BASICO[min(m, 7)]); c.number_format = '$#,##0'; c.border = B
        for j, n in enumerate(VENTAS, 4):
            c = ws.cell(row=i, column=j, value=ingreso(m, n, version)); c.number_format = '$#,##0'; c.border = B
            if n == META[m]: c.font = Font(bold=True); c.fill = C
            elif n < META[m] / 2: c.fill = G
    return r0 + 3 + len(FILAS)

r = tabla(4, 'VERSIÓN A — PISO GARANTIZADO (meses 1 y 2: recibe $3.500.000 o básico + comisión, lo que sea mayor)', 'A',
          'Vender 0 o vender 5 en el mes 1 paga lo mismo ($3.500.000); la comisión solo supera el piso desde 8 matrículas. Más barata para la academia; menos estímulo al arranque.')
r = tabla(r + 2, 'VERSIÓN B — BÁSICO + BONO + COMISIÓN (meses 1 y 2: $2.000.000 + $1.500.000 de bono de arranque + 7% de lo que cierre)', 'B',
          'Cada cierre paga desde el día uno. Cuesta hasta $1.500.000 más por mes en los dos primeros meses (a meta). Solo con condición dura de actividad.')
r += 1
ws.cell(row=r, column=1, value='LO QUE ARRIESGA LA ACADEMIA').font = Font(bold=True, color='E54C09'); r += 1
for t in [f'• Versión A, si no vende nada: ${GARANTIA:,.0f} x 2 meses = ${GARANTIA*2:,.0f}; desde el mes 3 solo el básico.',
          f'• Versión B, si no vende nada: igual ${GARANTIA*2:,.0f}; si vende a meta, ${BONO*2 + (META[1]+META[2])*COM_UNIT:,.0f} en bonos y comisiones de los dos primeros meses.',
          '• Desde el mes 3, en las dos versiones, todo lo que gana por encima del básico sale de ventas ya cobradas.',
          '• Condiciones: prueba práctica de cierre antes de firmar; período de prueba de 2 meses (coincide con la garantía); metas y mediciones del REGLAMENTO_MEDICION_COMERCIAL; ascensos solo por resultados; empresas que ella abra (fuera del piloto docente): 3% del recaudo corporativo del primer año.']:
    ws.cell(row=r, column=1, value=t); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=16); r += 1
for col, w in zip('ABCDEFGHIJKLMNOP', (13, 7, 12) + (12,) * 13): ws.column_dimensions[col].width = w
out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\CUADRO_INGRESO_CLOSER_SENIOR.xlsx'
try: wb.save(out); print('OK', out)
except PermissionError: wb.save(out.replace('.xlsx', '_v2.xlsx')); print('ABIERTO -> _v2')
for v in 'AB':
    print('Version', v)
    for m, lab in FILAS: print(' ', lab, [f'{ingreso(m, n, v)/1e6:.2f}' for n in VENTAS])
