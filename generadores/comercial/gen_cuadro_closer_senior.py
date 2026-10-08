# -*- coding: utf-8 -*-
"""Closer de planta perfil senior — MODELO ABSORBIBLE (decision Diana 08/10/2026):
piso $3.5M meses 1-3 con minimos; desde el mes 4 solo comision 12% del recaudo hasta la meta y 15% por encima.
Hoja 2: tablero semanal de seguimiento. Salida: .../contratacion comercial/CUADRO_INGRESO_CLOSER_SENIOR.xlsx"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

EQ = 2_990_000
COM, COM_ACEL, COM_ANTIGUO = 0.12, 0.15, 0.06
PISO = 3_500_000; MESES_PISO = 3
MINIMO = {1: 3, 2: 4, 3: 6}                     # contratos con inicial pagada para acceder al piso
META = {1: 6, 2: 8, 3: 8, 4: 10, 5: 10, 6: 10, 7: 12}
CONTRATOS = [0, 2, 3, 4, 5, 6, 8, 10, 12, 14, 15, 18, 20]
FILAS = [(1, 'Mes 1'), (2, 'Mes 2'), (3, 'Mes 3'), (4, 'Meses 4-6'), (7, 'Meses 7-12')]
INICIAL, CUOTA, N_CUOTAS = 1_200_000, 450_000, 4

def comision(mes, n):
    meta = META[min(mes, 7)]
    return min(n, meta) * EQ * COM + max(0, n - meta) * EQ * COM_ACEL

def ingreso(mes, n):
    com = comision(mes, n)
    if mes <= MESES_PISO:
        return max(com, PISO) if n >= MINIMO[mes] else com
    return com

H = Font(bold=True, color='FFFFFF'); F = PatternFill('solid', fgColor='E54C09'); C = PatternFill('solid', fgColor='FFF8E7'); G = PatternFill('solid', fgColor='EEEEEE')
thin = Side(style='thin', color='CCCCCC'); B = Border(left=thin, right=thin, top=thin, bottom=thin)
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'INGRESO'
ws['A1'] = 'CLOSER SENIOR — MODELO ABSORBIBLE: CUÁNTO GANA SEGÚN LO QUE CIERRE · decisión 08/10/2026'; ws['A1'].font = Font(bold=True, size=13, color='E54C09')
ws['A2'] = (f'SIN BÁSICO. Meses 1 a 3: PISO (absorbible) de ${PISO:,.0f} si cumple los mínimos (3, 4 y 6 contratos con inicial pagada) y 5 citas atendidas por semana; si sus comisiones superan el piso, se pagan las comisiones y el piso se absorbe. '
            f'Desde el mes 4: solo comisión. Comisión: {COM:.0%} del RECAUDO hasta la meta del mes (= ${EQ*COM:,.0f} por matrícula de ${EQ:,.0f} pagada completa) y {COM_ACEL:.0%} por encima de la meta (= ${EQ*COM_ACEL:,.0f}); {COM_ANTIGUO:.0%} cliente antiguo. '
            'Meta en CONTRATOS firmados con inicial pagada: 6 · 8 · 8 · 10 · 10 · 10 · 12. A cuotas, la comisión entra mes a mes mientras el cliente paga (cartera). La celda sombreada es la meta.')
ws['A2'].alignment = Alignment(wrap_text=True); ws.merge_cells('A2:P2'); ws.row_dimensions[2].height = 80

r = 4
ws.cell(row=r, column=1, value='CUADRO 1 — INGRESO DEL MES SEGÚN CONTRATOS CERRADOS (si todos pagan de contado)').font = Font(bold=True, size=12, color='E54C09'); r += 1
hdr = ['Mes', 'Meta', 'Mínimo p/ piso'] + [f'Cierra {n}' for n in CONTRATOS]
for j, h in enumerate(hdr, 1):
    c = ws.cell(row=r, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center'); c.border = B
r += 1
for m, lab in FILAS:
    ws.cell(row=r, column=1, value=lab).border = B; ws.cell(row=r, column=2, value=META[m]).border = B
    ws.cell(row=r, column=3, value=MINIMO.get(m, '—')).border = B
    for j, n in enumerate(CONTRATOS, 4):
        c = ws.cell(row=r, column=j, value=ingreso(m, n)); c.number_format = '$#,##0'; c.border = B
        if n == META[m]: c.font = Font(bold=True); c.fill = C
        elif m <= MESES_PISO and n < MINIMO[m]: c.fill = G
    r += 1
ws.cell(row=r, column=1, value='Gris: por debajo del mínimo, no hay piso (solo comisión). Ejemplo mes 1 con 5 contratos: comisión 5 x $358.800 = $1.794.000 < piso → recibe $3.500.000. Mes 1 con 12: 6 x $358.800 + 6 x $448.500 = $4.843.800 → recibe eso (el piso se absorbe). Mes 5 con 5: $1.794.000, sin piso.').alignment = Alignment(wrap_text=True)
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=16); ws.row_dimensions[r].height = 32; r += 2

ws.cell(row=r, column=1, value='CUADRO 2 — PARA GANAR X, CUÁNTOS CONTRATOS NECESITA (de contado)').font = Font(bold=True, size=12, color='E54C09'); r += 1
hdr3 = ['Quiere ganar', 'Meses 1-3 (piso $3.5M)', 'Meses 4-6 (meta 10)', 'Desde el mes 7 (meta 12)']
for j, h in enumerate(hdr3, 1):
    c = ws.cell(row=r, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center', wrap_text=True); c.border = B
ws.row_dimensions[r].height = 32; r += 1
def contratos_para(mes, objetivo):
    n = 0
    while ingreso(mes, n) < objetivo and n < 60: n += 1
    return n
for obj in (3_500_000, 4_000_000, 5_000_000, 6_000_000, 7_000_000):
    vals = [obj] + [contratos_para(m, obj) for m in (3, 4, 7)]
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=j, value=v); c.border = B
        if j == 1: c.number_format = '$#,##0'; c.font = Font(bold=True)
    r += 1
r += 1

ws.cell(row=r, column=1, value=f'CUADRO 3 — SI VENDE A CUOTAS: CÓMO CRECE SU CARTERA (ejemplo: cada contrato = inicial ${INICIAL:,.0f} + {N_CUOTAS} cuotas de ${CUOTA:,.0f}; cierra la meta cada mes)').font = Font(bold=True, size=12, color='E54C09'); r += 1
hdr2 = ['Mes', 'Contratos nuevos', 'Recaudo ventas nuevas (iniciales)', 'Recaudo de cartera (cuotas anteriores)', 'Recaudo total', 'Comisión 12%', 'Piso aplica', 'INGRESO DEL MES']
for j, h in enumerate(hdr2, 1):
    c = ws.cell(row=r, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center', wrap_text=True); c.border = B
ws.row_dimensions[r].height = 45; r += 1
activos = []
for m in range(1, 13):
    n = META[min(m, 7)]
    cartera = sum(CUOTA for q in activos if q > 0)
    activos = [q - 1 for q in activos if q - 1 > 0]; activos += [N_CUOTAS] * n
    nuevas = n * INICIAL; total = nuevas + cartera; com = total * COM
    piso = (m <= MESES_PISO)
    ing = max(com, PISO) if piso else com
    vals = [f'Mes {m}', n, nuevas, cartera, total, com, 'sí' if piso else 'no', ing]
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=j, value=v); c.border = B
        if j in (3, 4, 5, 6, 8): c.number_format = '$#,##0'
        if j == 8: c.font = Font(bold=True); c.fill = C
    r += 1
ws.cell(row=r, column=1, value='Lectura: a cuotas, los meses 1-3 los sostiene el piso mientras la cartera crece; desde el mes 4 la cartera de cuotas ya paga comisión todos los meses aunque venda menos. La comisión solo se paga sobre plata que entró.').alignment = Alignment(wrap_text=True)
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=16); ws.row_dimensions[r].height = 32; r += 2
ws.cell(row=r, column=1, value='RIESGO Y CONDICIONES').font = Font(bold=True, color='E54C09'); r += 1
for t in [f'• Riesgo máximo de la academia: ${PISO*MESES_PISO:,.0f} (tres meses de piso si solo cumple los mínimos). Desde el mes 4, cero fijo: todo sale de recaudo.',
          '• El piso se gana por semana: los viernes se miden citas atendidas (mínimo 5) y contratos; si una semana no cumple, el piso del mes se paga proporcional.',
          '• Forma del contrato: prestación de servicios con honorarios mínimos garantizados por tres meses (como trabaja la industria de seguros); revisar con el abogado. Si fuera laboral: salario mínimo legal + comisiones.',
          '• Prueba práctica de cierre antes de firmar. Tres resultados escritos cada corte: PASA · CARTA DE AMPLIACIÓN (una semana con meta escrita) · SALIDA (ver REGLAMENTO_MEDICION_COMERCIAL).',
          '• Empresas que ella abra (fuera del piloto docente): 3% del recaudo corporativo del primer año. Frontera con la asesora actual: la comisión es de quien atiende la cita y cierra.']:
    ws.cell(row=r, column=1, value=t); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=16); r += 1
for col, w in zip('ABCDEFGHIJKLMNOP', (13, 9, 14, 16, 14, 13, 11, 16) + (12,) * 8): ws.column_dimensions[col].width = w

# ---------- hoja: como cuenta cada tipo de venta
k = wb.create_sheet('REGLAS DE CONTEO')
k['A1'] = 'CÓMO CUENTA CADA TIPO DE VENTA (para la meta y para la comisión)'; k['A1'].font = Font(bold=True, size=13, color='E54C09')
hdr = ['Tipo de venta', 'Cuenta para la meta', 'Comisión', 'Nota']
for j, h in enumerate(hdr, 1):
    c = k.cell(row=3, column=j, value=h); c.font = H; c.fill = F; c.border = B
filas = [
 ('Programa completo de contado ($4.78M-$5.9M)', '1 contrato', '12% / 15% del recaudo, de una vez ($574k-$709k)', 'Mejor venta posible'),
 ('Arranque de contado ($2.99M)', '1 contrato', '$358.800 de una vez (12%)', ''),
 ('Cualquier programa a cuotas', '1 contrato cuando la INICIAL está pagada (mínimo $1.000.000 o 30%)', '12% de la inicial ese mes + 12% de cada cuota cuando entra', 'La cartera: comisión mes a mes'),
 ('Separación de $300.000 sola', '0 (lead en proceso)', '12% de los $300.000; el resto cuando pague la inicial', 'No llena la meta'),
 ('Nivel suelto / sabatino ($1.6M-$2.3M)', '½ contrato', '12% del recaudo', ''),
 ('Cliente antiguo (continuidad, supletorio)', '½ contrato', '6% del recaudo', ''),
 ('Plan empresa que ella abra (fuera del piloto docente)', '1 contrato por cupo', '3% del recaudo corporativo del primer año', 'Gerencia firma'),
]
for i, fila in enumerate(filas, 4):
    for j, v in enumerate(fila, 1):
        c = k.cell(row=i, column=j, value=v); c.border = B; c.alignment = Alignment(wrap_text=True, vertical='top')
k.cell(row=12, column=1, value='Regla: la meta solo se cumple con programas con inicial pagada; separaciones y niveles sueltos no la llenan. La comisión siempre es sobre plata que entró.').font = Font(italic=True)
k.merge_cells('A12:D12')
k.cell(row=14, column=1, value='LO QUE RECIBE LA ACADEMIA (si fueran de contado)').font = Font(bold=True, color='E54C09')
hdr = ['Contratos al mes', 'Recaudo', 'Comisión (12%/15%)', 'Neto academia', '% para ella']
for j, h in enumerate(hdr, 1):
    c = k.cell(row=15, column=j, value=h); c.font = H; c.fill = F; c.border = B
for i, n in enumerate((8, 10, 12, 15, 18), 16):
    rec = n * EQ; com = comision(7, n) if n >= 12 else comision(4, n)
    vals = [n, rec, com, rec - com, com / rec]
    for j, v in enumerate(vals, 1):
        c = k.cell(row=i, column=j, value=v); c.border = B
        if j in (2, 3, 4): c.number_format = '$#,##0'
        if j == 5: c.number_format = '0.0%'
k.cell(row=22, column=1, value='12 contratos al mes = la academia sana (~100 estudiantes pagando, ~$35M de caja). A cuotas, el recaudo del mes arranca en ~$14M de iniciales y llega a ~$36M hacia el quinto mes con la cartera; la comisión va igual de atrás.').alignment = Alignment(wrap_text=True)
k.merge_cells('A22:E22'); k.row_dimensions[22].height = 40
for col, w in zip('ABCDE', (44, 30, 40, 18, 12)): k.column_dimensions[col].width = w

# ---------- hoja 2: tablero semanal
t = wb.create_sheet('TABLERO SEMANAL')
t['A1'] = 'TABLERO SEMANAL DEL CLOSER — lo llena ella cada viernes; gerencia lo revisa en 10 minutos'; t['A1'].font = Font(bold=True, size=13, color='E54C09')
t['A2'] = 'Regla: lo que no está en el tablero no existe. Cada viernes: citas atendidas (mínimo 5), contratos con inicial pagada, recaudo. El segundo viernes del mes es el pre-corte (alerta); el último viernes, la medición.'
t['A2'].alignment = Alignment(wrap_text=True); t.merge_cells('A2:K2'); t.row_dimensions[2].height = 35
hdr = ['Semana (viernes)', 'Mes', 'Citas agendadas', 'Citas atendidas', 'Contratos con inicial', 'Recaudo de la semana', 'Acumulado contratos del mes', 'Meta del mes', '% de meta', 'Resultado (PASA / CARTA / SALIDA)', 'Observación']
for j, h in enumerate(hdr, 1):
    c = t.cell(row=4, column=j, value=h); c.font = H; c.fill = F; c.alignment = Alignment(horizontal='center', wrap_text=True); c.border = B
t.row_dimensions[4].height = 40
for i in range(5, 57):
    for j in range(1, 12): t.cell(row=i, column=j).border = B
    t.cell(row=i, column=6).number_format = '$#,##0'
    t.cell(row=i, column=9, value=f'=IF(H{i}="","",G{i}/H{i})').number_format = '0%'
for col, w in zip('ABCDEFGHIJK', (16, 8, 12, 12, 14, 16, 16, 10, 9, 22, 30)): t.column_dimensions[col].width = w

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\CUADRO_INGRESO_CLOSER_SENIOR.xlsx'
try: wb.save(out); print('OK', out)
except PermissionError: wb.save(out.replace('.xlsx', '_v2.xlsx')); print('ABIERTO -> _v2')
for m, lab in FILAS: print(lab, META[m], [f'{ingreso(m, n)/1e6:.2f}' for n in CONTRATOS])
