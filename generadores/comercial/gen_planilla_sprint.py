# -*- coding: utf-8 -*-
"""Planilla del sprint: ofertas/vencimientos + canales fuera del bot + termometro."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side

NARANJA = PatternFill('solid', fgColor='E54C09')
CREMA = PatternFill('solid', fgColor='FFF8E7')
BLANCO_B = Font(bold=True, color='FFFFFF', size=11)
B = Font(bold=True, size=11)
N = Font(size=11)
ROJO = Font(bold=True, size=10, color='C00000')
borde = Border(*[Side(style='thin')]*4)

wb = openpyxl.Workbook()

# ===== HOJA 1: OFERTAS Y VENCIMIENTOS =====
ws = wb.active; ws.title = 'OFERTAS Y VENCIMIENTOS'
ws.cell(1, 1, 'TODA oferta que no cierra sale POR ESCRITO y entra AQUÍ el mismo día. Rutina diaria: filtrar la columna VENCE por HOY y llamar. La fecha SE CUMPLE: vencida = vencida.').font = ROJO
ws.cell(2, 1, 'Las columnas con LISTA: haz clic EN la celda y aparece la flechita a la derecha. Si el archivo se abre en Vista protegida (franja amarilla), dale HABILITAR EDICION para que funcionen.').font = ROJO
cols = ['Fecha oferta', 'Nombre y APELLIDO', 'Teléfono', 'Qué se ofreció ($ y programa)', 'VENCE (fecha + 6 PM)', 'Abono $300k (S/N)', 'Llamada de vencimiento (fecha)', 'Estado (CERRÓ / VENCIÓ / RE-PRESENTADA)', 'Motivo / próximo paso']
for j, c in enumerate(cols, 1):
    cel = ws.cell(3, j, c); cel.font = BLANCO_B; cel.fill = NARANJA; cel.border = borde
    ws.column_dimensions[chr(64 + j)].width = 22
ej = ['15/09', 'Andrea Gómez', '300 123 4567', 'Arranque $2.990.000', '18/09 6PM', 'N', '18/09', 'VENCIÓ', 'La prima de dic — rescate en nov']
for j, v in enumerate(ej, 1):
    cel = ws.cell(4, j, v); cel.font = N; cel.fill = CREMA; cel.border = borde

# ===== HOJA 2: FUERA DEL BOT =====
ws2 = wb.create_sheet('FUERA DEL BOT')
ws2.cell(1, 1, 'Todo contacto que NO nació en el bot vive aquí: colegios (talleres), empresas (becados), grupos de Facebook, LinkedIn, referidos. Los del bot NO se duplican aquí — allá tienen sus comentarios.').font = ROJO
ws2.cell(2, 1, 'Las columnas con LISTA: haz clic EN la celda y aparece la flechita. En Vista protegida: HABILITAR EDICION primero.').font = ROJO
cols2 = ['Fecha', 'Canal (COLEGIO / EMPRESA / GRUPO FB / LINKEDIN / REFERIDO)', 'Detalle del origen (qué colegio / empresa / grupo / quién refirió)', 'Nombre y APELLIDO', 'Teléfono', 'Convenio (Cajasan / Empresa / Colegio / No)', 'Toque 1 (fecha + resultado)', 'Toque 2', 'Toque 3', 'Estado (CITA / OFERTA / NO+motivo)', 'Próximo paso (con fecha)']
for j, c in enumerate(cols2, 1):
    cel = ws2.cell(3, j, c); cel.font = BLANCO_B; cel.fill = NARANJA; cel.border = borde
    ws2.column_dimensions[chr(64 + j)].width = 20
ej2 = ['17/09', 'COLEGIO', 'Taller padres Colegio San José — hijo en 10°', 'Braulio Pérez', '301 234 5678', 'Colegio', '17/09 gracias enviado', '18/09 llamada: pide info sabatino', '', 'CITA', 'Cita sáb 20/09 10am']
for j, v in enumerate(ej2, 1):
    cel = ws2.cell(4, j, v); cel.font = N; cel.fill = CREMA; cel.border = borde

# ===== HOJA 3: TERMOMETRO =====
ws3 = wb.create_sheet('TERMÓMETRO')
ws3.cell(1, 1, 'Se actualiza CADA día al enviar el reporte de las 6 PM. Qué se le DICE al cliente según el contador (incluso con 0 ventas): DUDA #4 de la hoja de Dudas.').font = ROJO
filas = [
 ['CUPOS ARRANQUE VENDIDOS (de 20)', ''],
 ['Abonos de separación vigentes', ''],
 ['Ofertas vivas (sin vencer)', ''],
 ['', ''],
 ['SEMANA (lunes a sábado)', 'Real'],
 ['Contactos salientes (meta 200)', ''],
 ['Citas agendadas (meta 25)', ''],
 ['Citas asistidas (meta 12)', ''],
 ['Matrículas/abonos (meta 4-5)', ''],
 ['Caja de la semana ($)', ''],
]
for i, (a, b) in enumerate(filas, 3):
    c1 = ws3.cell(i, 1, a); c2 = ws3.cell(i, 2, b)
    if a and ('CUPOS' in a or 'SEMANA' in a):
        c1.font = B; c1.fill = CREMA
    else:
        c1.font = N
    c1.border = borde; c2.border = borde
ws3.column_dimensions['A'].width = 40; ws3.column_dimensions['B'].width = 15


# ===== DROPLISTS (validacion de datos, filas 4 a 500) =====
from openpyxl.worksheet.datavalidation import DataValidation

def dv(hoja, col, opciones):
    d = DataValidation(type='list', formula1='"' + ','.join(opciones) + '"', allow_blank=True, showDropDown=False)
    d.error = 'Elige una opción de la lista'; d.showErrorMessage = True
    hoja.add_data_validation(d)
    d.add(col + '4:' + col + '500')

# Hoja 1: OFERTAS Y VENCIMIENTOS
dv(ws, 'D', ['Arranque $2.990.000', 'A1-B2 completo', 'A2-B2', 'B1-B2', 'Solo B2', 'Nivel suelto', 'Sabatino', 'Personalizadas'])
dv(ws, 'F', ['S', 'N'])
dv(ws, 'H', ['VIGENTE', 'CERRÓ', 'VENCIÓ', 'RE-PRESENTADA'])

# Hoja 2: FUERA DEL BOT
dv(ws2, 'B', ['COLEGIO', 'EMPRESA', 'GRUPO FB', 'LINKEDIN', 'REFERIDO', 'OPERADOR'])
dv(ws2, 'F', ['Cajasan', 'Empresa', 'Colegio', 'No'])
dv(ws2, 'J', ['EN SEGUIMIENTO', 'CITA AGENDADA', 'OFERTA EMITIDA', 'MATRICULADO', 'NO - motivo anotado', 'NO CONTACTAR (reclamo)'])

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\PLANILLA_SPRINT.xlsx'
wb.save(out); print('OK', out)
