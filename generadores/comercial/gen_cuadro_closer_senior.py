# -*- coding: utf-8 -*-
"""Cuadro de ingreso del closer de planta perfil senior (propuesta 08/10/2026): metas, basico, garantia de arranque, comision.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/CUADRO_INGRESO_CLOSER_SENIOR.xlsx"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

EQ = 2_990_000          # 1 matricula-equivalente = recaudo de un Arranque
COM = 0.07              # comision sobre recaudo, desde la primera venta
BASICO = {1: 2_000_000, 2: 2_000_000, 3: 2_000_000, 4: 2_300_000, 5: 2_300_000, 6: 2_300_000, 7: 2_600_000}  # ascensos mes 4 y 7 (PROPUESTA)
GARANTIA = 3_500_000    # meses 1 y 2: ingreso garantizado si cumple actividad
META = {1: 4, 2: 6, 3: 8, 4: 10, 5: 10, 6: 10, 7: 12}

def ingreso(mes, ventas):
    b = BASICO[min(mes, 7)]
    com = ventas * EQ * COM
    total = b + com
    if mes <= 2:
        total = max(total, GARANTIA)
    return b, com, total

wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'CUADRO'
H = Font(bold=True, color='FFFFFF'); F = PatternFill('solid', fgColor='E54C09'); C = PatternFill('solid', fgColor='FFF8E7')
thin = Side(style='thin', color='CCCCCC'); B = Border(left=thin, right=thin, top=thin, bottom=thin)
ws['A1'] = 'CLOSER DE PLANTA (PERFIL SENIOR) — CUÁNTO GANA SEGÚN LO QUE CIERRE · propuesta 08/10/2026'; ws['A1'].font = Font(bold=True, size=13, color='E54C09')
ws['A2'] = f'1 matrícula-equivalente = ${EQ:,.0f} de recaudo (un Arranque). Comisión {COM:.0%} del recaudo desde la primera venta. Meses 1 y 2: ingreso garantizado ${GARANTIA:,.0f} si cumple actividad (5 citas atendidas/semana). Ascensos de básico mes 4 y mes 7 (montos propuestos).'
ws['A2'].alignment = Alignment(wrap_text=True); ws.merge_cells('A2:M2'); ws.row_dimensions[2].height = 45
hdr = ['Mes', 'Meta (matrículas)', 'Recaudo a meta', 'Básico', 'SI VENDE 0', 'Vende (matr.)', 'SI VENDE LA MITAD', 'Vende (matr.)', 'SI CUMPLE LA META', 'Vende (matr.)', 'SI VENDE MÁS', 'Comisión a meta', 'Nota']
for j, h in enumerate(hdr, 1):
    c = ws.cell(row=4, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center', wrap_text=True); c.border = B
ws.row_dimensions[4].height = 32
rows = [1, 2, 3, 4, 5, 6, 7]
labels = {1: 'Mes 1', 2: 'Mes 2', 3: 'Mes 3', 4: 'Mes 4', 5: 'Mes 5', 6: 'Mes 6', 7: 'Mes 7 en adelante'}
notas = {1: 'Garantía de arranque', 2: 'Garantía de arranque', 3: 'Fin de la garantía: gana lo que cierra', 4: 'Primer ascenso de básico', 5: '', 6: '', 7: 'Segundo ascenso de básico'}
tot = {'0': 0, 'mitad': 0, 'meta': 0, 'mas': 0}
for i, m in enumerate(rows, 5):
    meta = META[m]
    b, com_meta, t_meta = ingreso(m, meta)
    _, _, t_0 = ingreso(m, 0)
    _, _, t_mitad = ingreso(m, meta / 2)
    _, _, t_mas = ingreso(m, meta * 1.5)
    vals = [labels[m], meta, meta * EQ, b, t_0, meta / 2, t_mitad, meta, t_meta, meta * 1.5, t_mas, com_meta, notas[m]]
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=i, column=j, value=v); c.border = B
        if j in (3, 4, 5, 7, 9, 11, 12): c.number_format = '$#,##0'
        if j == 9: c.font = Font(bold=True); c.fill = C
    mult = 6 if m == 7 else 1  # meses 7-12
    tot['0'] += t_0 * mult; tot['mitad'] += t_mitad * mult; tot['meta'] += t_meta * mult; tot['mas'] += t_mas * mult
r = 5 + len(rows)
ws.cell(row=r, column=1, value='AÑO 1 (12 meses)').font = Font(bold=True)
for j, k in zip((5, 7, 9, 11), ('0', 'mitad', 'meta', 'mas')):
    c = ws.cell(row=r, column=j, value=tot[k]); c.number_format = '$#,##0'; c.font = Font(bold=True); c.border = B
ws.cell(row=r, column=13, value='Promedio mensual a meta: ' + f'${tot["meta"]/12:,.0f}')
r += 2
for t in ['CÓMO LEERLO:',
          '• "Si vende 0": lo que recibe aunque no cierre nada (básico; en meses 1-2 la garantía). Es lo que la academia arriesga.',
          '• "Si cumple la meta": básico + 7% del recaudo de la meta. Es el número que se le promete como alcanzable, no como fijo.',
          '• La comisión se paga sobre RECAUDO: como los clientes pagan en cuotas, parte de la comisión de una venta le entra en los meses siguientes (su "cartera").',
          '• Costo para la academia a meta: básico + comisión; la comisión sale de ventas ya cobradas. Peor caso: $3.5M x 2 meses sin ventas = $7M.',
          '• Condiciones: prueba práctica de cierre antes de firmar; período de prueba 2 meses (coincide con la garantía); metas y mediciones del REGLAMENTO_MEDICION_COMERCIAL; ascensos solo por resultados.',
          '• Empresas que ella abra (fuera del piloto docente): 3% del recaudo corporativo del primer año.']:
    ws.cell(row=r, column=1, value=t); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=13); r += 1
for col, w in zip('ABCDEFGHIJKLM', (18, 12, 15, 13, 14, 9, 16, 9, 17, 9, 15, 15, 30)): ws.column_dimensions[col].width = w
out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\CUADRO_INGRESO_CLOSER_SENIOR.xlsx'
wb.save(out); print('OK', out)
for m in rows:
    print(labels[m], META[m], [f'{ingreso(m, v)[2]:,.0f}' for v in (0, META[m]/2, META[m], META[m]*1.5)])
print('año a meta', f'{tot["meta"]:,.0f}', '| sin ventas', f'{tot["0"]:,.0f}')
