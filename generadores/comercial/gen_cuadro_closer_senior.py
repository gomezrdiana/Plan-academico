# -*- coding: utf-8 -*-
"""Cuadro de ingreso del closer de planta perfil senior (decision Diana 08/10/2026).
Meta en CONTRATOS firmados con inicial pagada; comision 7% sobre RECAUDO desde la primera venta; bono de arranque meses 1-2 que se suma.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/CUADRO_INGRESO_CLOSER_SENIOR.xlsx"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

EQ = 2_990_000; COM = 0.08; COM_ACEL = 0.10; COM_UNIT = EQ * COM; COM_UNIT_ACEL = EQ * COM_ACEL   # 8% hasta la meta, 10% por encima
BASICO = {1: 2_000_000, 2: 2_000_000, 3: 2_000_000, 4: 2_300_000, 5: 2_300_000, 6: 2_300_000, 7: 2_600_000}
BONO = 1_500_000
META = {1: 6, 2: 8, 3: 8, 4: 10, 5: 10, 6: 10, 7: 12}
CONTRATOS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]
FILAS = [(1, 'Mes 1'), (2, 'Mes 2'), (3, 'Mes 3'), (4, 'Meses 4-6'), (7, 'Meses 7-12')]
INICIAL, CUOTA, N_CUOTAS = 1_200_000, 450_000, 4   # ejemplo de plan a cuotas: inicial + 4 cuotas (= $3.0M)

def comision(mes, n):
    meta = META[min(mes, 7)]
    return min(n, meta) * COM_UNIT + max(0, n - meta) * COM_UNIT_ACEL

def ingreso_contado(mes, n):
    b = BASICO[min(mes, 7)]; com = comision(mes, n)
    bono = BONO if (mes <= 2 and n >= META[mes] / 2) else 0
    return b + bono + com

H = Font(bold=True, color='FFFFFF'); F = PatternFill('solid', fgColor='E54C09'); C = PatternFill('solid', fgColor='FFF8E7'); G = PatternFill('solid', fgColor='EEEEEE')
thin = Side(style='thin', color='CCCCCC'); B = Border(left=thin, right=thin, top=thin, bottom=thin)
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'CUADRO'
ws['A1'] = 'CLOSER DE PLANTA (PERFIL SENIOR) — CUÁNTO GANA SEGÚN LO QUE CIERRE · decisión 08/10/2026'; ws['A1'].font = Font(bold=True, size=13, color='E54C09')
ws['A2'] = ('REGLAS. Meta: contratos firmados con la inicial pagada (mes 1: 6 · mes 2 y 3: 8 · meses 4-6: 10 · desde el mes 7: 12). Básico $2.000.000 (sube a $2.300.000 en el mes 4 y a $2.600.000 en el mes 7, por resultados). '
            'Bono de arranque meses 1 y 2: $1.500.000, se SUMA a la comisión, con condición: 5 citas atendidas por semana y al menos la mitad de la meta (3 contratos el mes 1, 4 el mes 2). '
            f'Comisión: 8% del RECAUDO desde la primera venta (= ${COM_UNIT:,.0f} por matrícula de ${EQ:,.0f} pagada completa) y 10% sobre lo que cierre por encima de la meta del mes (= ${COM_UNIT_ACEL:,.0f}); 4% si es cliente antiguo. Si es a cuotas, la comisión entra mes a mes mientras el cliente paga. La celda sombreada es la meta.')
ws['A2'].alignment = Alignment(wrap_text=True); ws.merge_cells('A2:P2'); ws.row_dimensions[2].height = 75

r0 = 4
ws.cell(row=r0, column=1, value='CUADRO 1 — INGRESO DEL MES SEGÚN CONTRATOS CERRADOS (si todos pagan de contado)').font = Font(bold=True, size=12, color='E54C09')
hdr = ['Mes', 'Meta', 'Básico'] + [f'Cierra {n}' for n in CONTRATOS]
for j, h in enumerate(hdr, 1):
    c = ws.cell(row=r0 + 1, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center'); c.border = B
for i, (m, lab) in enumerate(FILAS, r0 + 2):
    ws.cell(row=i, column=1, value=lab).border = B; ws.cell(row=i, column=2, value=META[m]).border = B
    c = ws.cell(row=i, column=3, value=BASICO[min(m, 7)]); c.number_format = '$#,##0'; c.border = B
    for j, n in enumerate(CONTRATOS, 4):
        c = ws.cell(row=i, column=j, value=ingreso_contado(m, n)); c.number_format = '$#,##0'; c.border = B
        if n == META[m]: c.font = Font(bold=True); c.fill = C
        elif n < META[m] / 2: c.fill = G
r = r0 + 2 + len(FILAS)
ws.cell(row=r, column=1, value='Gris: por debajo de la mitad de la meta (en meses 1-2 no hay bono). Ejemplo mes 1 con 5 contratos: $2.000.000 + $1.500.000 + 5 x $239.200 = $4.696.000. Mes 1 con 2 contratos: $2.000.000 + 2 x $239.200 = $2.478.400 (sin bono). Por encima de la meta cada contrato vale $299.000.').alignment = Alignment(wrap_text=True)
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=16); ws.row_dimensions[r].height = 30
r += 2

# CUADRO 2: cartera a cuotas
ws.cell(row=r, column=1, value=f'CUADRO 2 — SI VENDE A CUOTAS: CÓMO CRECE SU CARTERA (ejemplo: cada contrato = inicial ${INICIAL:,.0f} + {N_CUOTAS} cuotas de ${CUOTA:,.0f}; cierra la meta cada mes)').font = Font(bold=True, size=12, color='E54C09'); r += 1
hdr2 = ['Mes', 'Contratos nuevos', 'Recaudo de ventas nuevas (iniciales)', 'Recaudo de cartera (cuotas de meses anteriores)', 'Recaudo total', 'Comisión del mes (8%)', 'Bono', 'Básico', 'INGRESO DEL MES']
for j, h in enumerate(hdr2, 1):
    c = ws.cell(row=r, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center', wrap_text=True); c.border = B
ws.row_dimensions[r].height = 45; r += 1
activos = []  # lista de (cuotas restantes) por contrato
for m in range(1, 13):
    n = META[min(m, 7)]
    cartera = sum(CUOTA for q in activos if q > 0)
    activos = [q - 1 for q in activos if q - 1 > 0]
    activos += [N_CUOTAS] * n
    nuevas = n * INICIAL
    total = nuevas + cartera; com = total * COM  # a cuotas se simplifica al 8% del recaudo
    bono = BONO if m <= 2 else 0
    b = BASICO[min(m, 7)]
    vals = [f'Mes {m}', n, nuevas, cartera, total, com, bono, b, b + bono + com]
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=j, value=v); c.border = B
        if j >= 3: c.number_format = '$#,##0'
        if j == 9: c.font = Font(bold=True); c.fill = C
    r += 1
ws.cell(row=r, column=1, value='Lectura: a cuotas, la comisión del mes de la venta es menor (solo la inicial), pero desde el mes 3 la cartera de cuotas le paga comisión aunque ese mes venda menos. Lo que ella gana a meta termina siendo lo mismo que de contado, repartido en el tiempo; y a la academia le interesa porque la comisión solo se paga sobre plata que entró.').alignment = Alignment(wrap_text=True)
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=16); ws.row_dimensions[r].height = 45; r += 2

ws.cell(row=r, column=1, value='CUADRO 3 — PARA GANAR X, CUÁNTOS CONTRATOS NECESITA (de contado; desde el mes 3, sin bono)').font = Font(bold=True, size=12, color='E54C09'); r += 1
hdr3 = ['Quiere ganar', 'Mes 3 (básico $2.0M, meta 8)', 'Meses 4-6 (básico $2.3M, meta 10)', 'Desde el mes 7 (básico $2.6M, meta 12)']
for j, h in enumerate(hdr3, 1):
    c = ws.cell(row=r, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center', wrap_text=True); c.border = B
ws.row_dimensions[r].height = 32; r += 1
def contratos_para(mes, objetivo):
    n = 0
    while ingreso_contado(mes, n) < objetivo and n < 40: n += 1
    return n
for obj in (3_500_000, 4_000_000, 5_000_000, 6_000_000, 7_000_000):
    vals = [obj] + [contratos_para(m, obj) for m in (3, 4, 7)]
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=j, value=v); c.border = B
        if j == 1: c.number_format = '$#,##0'; c.font = Font(bold=True)
    r += 1
r += 1
ws.cell(row=r, column=1, value='LO QUE ARRIESGA LA ACADEMIA Y LAS CONDICIONES').font = Font(bold=True, color='E54C09'); r += 1
for t in ['• Si no vende nada: solo el básico ($2.000.000 al mes); el bono de arranque exige la mitad de la meta, así que no se paga con 0 ventas.',
          '• Peor caso con bono: meses 1 y 2 a media meta (3 y 4 contratos): $3.500.000 + comisión de 3 y 4 contratos. Todo lo demás sale de ventas ya cobradas.',
          '• Condiciones: prueba práctica de cierre antes de firmar; período de prueba de 2 meses (coincide con el bono); metas y mediciones del REGLAMENTO_MEDICION_COMERCIAL (este rol tiene su propia curva: 6/8/8/10/12, comisión 8% desde la primera venta y 10% por encima de la meta); ascensos de básico solo por resultados.',
          '• Empresas que ella abra (fuera del piloto docente): 3% del recaudo corporativo del primer año.',
          '• Frontera con la asesora actual (comisión pura): citas del asistente y franjas que la asesora no cubre van a la closer; canales propios de cada una se respetan; la comisión es de quien atiende y cierra.']:
    ws.cell(row=r, column=1, value=t); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=16); r += 1
for col, w in zip('ABCDEFGHIJKLMNOP', (13, 9, 16, 18, 14, 14, 12, 12, 16) + (12,) * 7): ws.column_dimensions[col].width = w
out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\CUADRO_INGRESO_CLOSER_SENIOR.xlsx'
try: wb.save(out); print('OK', out)
except PermissionError: wb.save(out.replace('.xlsx', '_v2.xlsx')); print('ABIERTO -> _v2')
for m, lab in FILAS: print(lab, META[m], [f'{ingreso_contado(m, n)/1e6:.2f}' for n in CONTRATOS])
