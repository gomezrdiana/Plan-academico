# -*- coding: utf-8 -*-
"""PLANILLA ÚNICA DE REFERIDOS (Anexo C del programa de referidos, 14/10/2026) como Excel listo para usar.
Plantilla VACÍA (va a git). La copia viva se sube a Drive/Sheets y se comparte con el docente; nunca vuelve al repo con datos.
Hojas: REFERIDOS · EGRESADOS · REPORTE · LIQUIDACION · REGLAS.  Salida: recursos/comercial/PLANILLA_REFERIDOS.xlsx"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

NAR = PatternFill('solid', fgColor='E54C09'); CREMA = PatternFill('solid', fgColor='FFF8E7'); GRIS = PatternFill('solid', fgColor='F2F2F2')
HB = Font(bold=True, color='FFFFFF', size=10, name='Calibri'); B = Font(bold=True, size=10, name='Calibri'); N = Font(size=10, name='Calibri')
borde = Border(*[Side(style='thin', color='D9D9D9')] * 4)
wrap = Alignment(wrap_text=True, vertical='center')
FILAS = 300

wb = openpyxl.Workbook()

def hoja(ws, cols, anchos, filas=FILAS):
    ws.append([c for c, _ in cols])
    ws.append([d for _, d in cols])
    for i, (c, d) in enumerate(cols, 1):
        a = ws.cell(row=1, column=i); a.fill = NAR; a.font = HB; a.alignment = wrap; a.border = borde
        b = ws.cell(row=2, column=i); b.fill = CREMA; b.font = Font(size=8.5, italic=True, color='666666'); b.alignment = wrap; b.border = borde
        ws.column_dimensions[get_column_letter(i)].width = anchos[i - 1]
    ws.row_dimensions[1].height = 30; ws.row_dimensions[2].height = 48
    for r in range(3, filas + 3):
        for i in range(1, len(cols) + 1):
            c = ws.cell(row=r, column=i); c.font = N; c.border = borde; c.alignment = Alignment(vertical='center')
    ws.freeze_panes = 'C3'

def lista(ws, col, opciones, filas=FILAS):
    dv = DataValidation(type='list', formula1='"' + ','.join(opciones) + '"', allow_blank=True)
    ws.add_data_validation(dv); dv.add(f'{col}3:{col}{filas + 2}')

# ---------------- REFERIDOS ----------------
ws = wb.active; ws.title = 'REFERIDOS'
cols = [
 ('#', 'Consecutivo'),
 ('Fecha registro', 'Día en que se anota al referido, ANTES del primer contacto'),
 ('Hora', 'Hora del registro'),
 ('Referido', 'Nombre completo'),
 ('Teléfono', 'Celular entregado por quien refiere'),
 ('Quién refiere', 'Nombre del estudiante o egresado'),
 ('Tipo', 'Activo / Egresado'),
 ('Grupo o nivel', 'Grupo actual, o nivel terminado y fecha si es egresado'),
 ('Al día', 'Quien refiere está al día en pagos: Sí / No'),
 ('Recolectado por', 'Docente / Asesora / Otro'),
 ('Verificación 30 días', 'Coordinación revisa base, bot y formularios: Limpio / Ya estaba (= lead de pauta, sin bono ni 5%)'),
 ('Fecha 1er mensaje', 'Desde la línea de referidos de Heiiu, el mismo día del registro'),
 ('Respuesta', 'SÍ / NO (se borra el número) / Sin respuesta'),
 ('Llamada 24 h', 'Fecha de la llamada si no respondió'),
 ('Cierre día 3', 'Fecha del último mensaje si siguió sin responder'),
 ('Estado', 'Registrado → Contactado → Clase de prueba → Cita → Inicial pagada → Clase 5 → Bono pagado / Cerrado'),
 ('Fecha clase de prueba', ''),
 ('Fecha cita', 'Asesoría por llamada'),
 ('Fecha inicial pagada', 'Fecha del primer abono'),
 ('Quién condujo la asesoría', 'Docente / Asesora / Acompañado'),
 ('Programa', 'Completo contado / Completo cuotas / Arranque'),
 ('Valor matrícula', 'Valor total del contrato'),
 ('Bono: valor', ''),
 ('Bono: forma', 'Transferencia / Abono a cuotas / 2 horas'),
 ('Bono: fecha pago', 'Después de la clase 5 y del retracto'),
 ('Comisión a', 'Docente 5% / Asesora 5% / Docente 2%'),
 ('Mes liquidación', 'Mes en que se liquida (contra pagos con retracto vencido)'),
 ('Límite cita (día 7)', 'Fórmula: registro + 7'),
 ('Límite cierre (día 14)', 'Fórmula: registro + 14'),
 ('Pasó a asesora', 'Sí / No (si pasa, el docente queda con el 2%)'),
 ('Notas', 'Motivo del referido, objeciones, acuerdos'),
]
anchos = [5, 12, 7, 24, 14, 22, 11, 20, 8, 14, 18, 13, 14, 12, 12, 18, 13, 12, 13, 16, 18, 14, 12, 16, 13, 16, 13, 13, 13, 12, 36]
hoja(ws, cols, anchos)
for r in range(3, FILAS + 3):
    ws.cell(row=r, column=1, value=f'=IF(D{r}="","",ROW()-2)')
    ws.cell(row=r, column=28, value=f'=IF(B{r}="","",B{r}+7)'); ws.cell(row=r, column=28).number_format = 'DD/MM/YYYY'
    ws.cell(row=r, column=29, value=f'=IF(B{r}="","",B{r}+14)'); ws.cell(row=r, column=29).number_format = 'DD/MM/YYYY'
    for c in (2, 12, 14, 15, 17, 18, 19, 25): ws.cell(row=r, column=c).number_format = 'DD/MM/YYYY'
    for c in (22, 23): ws.cell(row=r, column=c).number_format = '$#,##0'
lista(ws, 'G', ['Activo', 'Egresado']); lista(ws, 'I', ['Sí', 'No']); lista(ws, 'J', ['Docente', 'Asesora', 'Otro'])
lista(ws, 'K', ['Limpio', 'Ya estaba']); lista(ws, 'M', ['SÍ', 'NO', 'Sin respuesta'])
lista(ws, 'P', ['Registrado', 'Contactado', 'Clase de prueba', 'Cita', 'Inicial pagada', 'Clase 5', 'Bono pagado', 'Cerrado'])
lista(ws, 'T', ['Docente', 'Asesora', 'Acompañado']); lista(ws, 'U', ['Completo contado', 'Completo cuotas', 'Arranque'])
lista(ws, 'X', ['Transferencia', 'Abono a cuotas', '2 horas']); lista(ws, 'Z', ['Docente 5%', 'Asesora 5%', 'Docente 2%']); lista(ws, 'AD', ['Sí', 'No'])

# ---------------- EGRESADOS ----------------
ws = wb.create_sheet('EGRESADOS')
cols = [('#', ''), ('Nombre', 'Lista la arma coordinación'), ('Nivel terminado', ''), ('Fecha de salida', ''), ('Teléfono', ''),
        ('Fecha llamada', 'Desde la línea de Heiiu, horario legal'), ('Resultado', 'Contestó / No contestó / Número errado'),
        ('Mensaje enviado', 'Fecha, si no contestó'), ('Reintento', 'Fecha del segundo intento'),
        ('Referido entregado', 'Nombre (se registra en REFERIDOS)'), ('Notas', '')]
hoja(ws, cols, [5, 26, 14, 13, 14, 13, 16, 13, 12, 24, 36], filas=200)
for r in range(3, 203):
    ws.cell(row=r, column=1, value=f'=IF(B{r}="","",ROW()-2)')
    for c in (4, 6, 8, 9): ws.cell(row=r, column=c).number_format = 'DD/MM/YYYY'
lista(ws, 'G', ['Contestó', 'No contestó', 'Número errado'], filas=200)

# ---------------- REPORTE ----------------
ws = wb.create_sheet('REPORTE')
ws['A1'] = 'REPORTE DIARIO (6:00 p.m., 3 líneas por WhatsApp) — se llena aquí y se copia'; ws['A1'].font = Font(bold=True, size=12, color='E54C09')
cols = [('Fecha', ''), ('A quién pidió hoy', 'Grupos o egresados a los que les pidió referidos'), ('Referidos nuevos', 'Registrados hoy'),
        ('Citas agendadas', 'Hoy'), ('Notas', '')]
ws.append([]); ws.append([c for c, _ in cols]); ws.append([d for _, d in cols])
for i, _ in enumerate(cols, 1):
    a = ws.cell(row=3, column=i); a.fill = NAR; a.font = HB; a.alignment = wrap; a.border = borde
    b = ws.cell(row=4, column=i); b.fill = CREMA; b.font = Font(size=8.5, italic=True, color='666666'); b.alignment = wrap; b.border = borde
for w_, l in zip([12, 40, 14, 14, 40], 'ABCDE'): ws.column_dimensions[l].width = w_
for r in range(5, 45):
    for i in range(1, 6): ws.cell(row=r, column=i).border = borde
    ws.cell(row=r, column=1).number_format = 'DD/MM/YYYY'
ws['G1'] = 'LUNES, 5 LÍNEAS (se calculan solas desde REFERIDOS)'; ws['G1'].font = Font(bold=True, size=12, color='E54C09')
filas5 = [('Registrados', '=COUNTA(REFERIDOS!D3:D302)'),
          ('Contactados (respondieron SÍ)', '=COUNTIF(REFERIDOS!M3:M302,"SÍ")'),
          ('Citas', '=COUNTA(REFERIDOS!R3:R302)'),
          ('Matrículas con inicial', '=COUNTA(REFERIDOS!S3:S302)'),
          ('Bonos por pagar (clase 5 sin bono pagado)', '=COUNTIF(REFERIDOS!P3:P302,"Clase 5")'),
          ('Cerrados / NO', '=COUNTIF(REFERIDOS!P3:P302,"Cerrado")+COUNTIF(REFERIDOS!M3:M302,"NO")'),
          ('Días promedio registro → cita', '=IFERROR(AVERAGE(IF(REFERIDOS!R3:R302<>"",REFERIDOS!R3:R302-REFERIDOS!B3:B302)),"")')]
for k, (lab, f) in enumerate(filas5, start=3):
    ws.cell(row=k, column=7, value=lab).font = B; ws.cell(row=k, column=7).border = borde; ws.cell(row=k, column=7).fill = GRIS
    c = ws.cell(row=k, column=8, value=f); c.border = borde; c.font = N
ws.column_dimensions['G'].width = 42; ws.column_dimensions['H'].width = 12
ws.cell(row=11, column=7, value='Corte del piloto: 30/10/2026. Sigue si llegó a la meta o si el costo por matrícula referida (bonos + comisiones) es menor que el de pauta.').font = Font(size=9, italic=True, color='666666')

# ---------------- LIQUIDACION ----------------
ws = wb.create_sheet('LIQUIDACION')
cols = [('Mes', 'Mes que se liquida'), ('Referido', 'Nombre (de REFERIDOS)'), ('Pagos con retracto vencido', 'Suma de lo que entró a caja ese mes por ese estudiante'),
        ('% docente', '5% si él cerró, 2% si cerró la asesora'), ('Comisión docente', 'Fórmula'), ('% asesora', '5% si cerró ella, 0 si no'), ('Comisión asesora', 'Fórmula'),
        ('Bono a quien refirió', 'Solo si ya pasó la clase 5'), ('Devolución / retracto a descontar', ''), ('Aprobado gerencia', 'Sí / No y fecha'), ('Pagado', 'Fecha')]
hoja(ws, cols, [10, 26, 18, 10, 16, 10, 16, 16, 18, 16, 12], filas=200)
for r in range(3, 203):
    ws.cell(row=r, column=5, value=f'=IF(C{r}="","",C{r}*D{r})'); ws.cell(row=r, column=7, value=f'=IF(C{r}="","",C{r}*F{r})')
    for c in (3, 5, 7, 8, 9): ws.cell(row=r, column=c).number_format = '$#,##0'
    for c in (4, 6): ws.cell(row=r, column=c).number_format = '0%'
    ws.cell(row=r, column=11).number_format = 'DD/MM/YYYY'
lista(ws, 'D', ['5%', '2%', '0%'], filas=200); lista(ws, 'F', ['5%', '0%'], filas=200)
ws.freeze_panes = 'C3'

# ---------------- REGLAS ----------------
ws = wb.create_sheet('REGLAS')
ws.column_dimensions['A'].width = 120
reglas = [
 'REGLAS DE LA PLANILLA ÚNICA DE REFERIDOS (piloto 15 al 30/10/2026)',
 '1. Se registra al referido ANTES de escribirle. Lo que no está en la planilla no existe ni se paga.',
 '2. Coordinación verifica antes del primer contacto que no estaba en la base, el bot ni un formulario en los últimos 30 días. Si ya estaba, es lead de pauta: sin bono y sin 5%.',
 '3. El primer mensaje sale el mismo día del registro, solo desde la línea de referidos de Heiiu, nunca desde un celular personal. Si responde NO, se borra el número y se marca.',
 '4. Sin respuesta: una llamada en horario legal a las 24 h; si tampoco, un último mensaje al tercer día y se cierra.',
 '5. Plazos desde el registro: cita en 7 días, cierre en 14. Si no se cumplen, el referido pasa a la asesora y el docente queda con el 2%.',
 '6. Una sola comisión por matrícula: nunca cobran los dos el 5% por el mismo recaudo. En "Quién condujo la asesoría" queda quién llevó el caso hasta el abono.',
 '7. Comisiones y bono se liquidan a fin de mes contra esta planilla, sobre pagos con el retracto vencido. Devolución o retracto se descuenta de la siguiente liquidación.',
 '8. No cuentan como referidos el personal de Heiiu ni sus familiares. El bono no se usa como argumento ante el referido.',
 '9. Las listas de estudiantes, egresados y referidos no salen de esta planilla. No se copian a celulares personales.',
 '10. Reporte: 3 líneas todos los días a las 6:00 p.m. y 5 líneas los lunes (hoja REPORTE). Corte del piloto el 30/10.',
]
for i, rg in enumerate(reglas, 1):
    c = ws.cell(row=i, column=1, value=rg); c.alignment = Alignment(wrap_text=True, vertical='top')
    c.font = Font(bold=True, size=12, color='E54C09') if i == 1 else N
    ws.row_dimensions[i].height = 22 if i == 1 else 30

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\PLANILLA_REFERIDOS.xlsx'
try: wb.save(out); print('OK', out)
except PermissionError: wb.save(out.replace('.xlsx', '_v2.xlsx')); print('ABIERTO -> _v2')
