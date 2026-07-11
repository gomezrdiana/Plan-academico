#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guia + reporte del A1 INTENSIVO 4H Cl 4:
- M6 What Time Will You Eat Lunch? - Simple Future (p.71-88) + M7 Where and What Time? (p.89-98)
- Virtud PRUDENCIA v1 dia 4. Recuperacion Cl 3/2/1. Simulacion HOTEL FRONT DESK.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(A1_4H, exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class4_PRINT.md'), os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class4_GUIA.pdf'))
print('OK: A1_4h_Class4_GUIA.pdf')

act = [
    ('BLOQUE 1 - Apertura (recuperacion Cl 3/2/1 DE PIE + portafolio + Frase del Dia + tarea Cl 3)', '35 min'),
    ('BLOQUE 2 - M6 will + what time + at y M7 the + lugares (historia interactiva + MY PLAN)', '85 min'),
    ('BLOQUE 3 - Drill de pie will/estaciones + Simulacion HOTEL FRONT DESK + MY WORLD pieza 4', '90 min'),
    ('BLOQUE 4 - Ticket de salida + tarea + error paper + anuncio Cl 5', '30 min'),
]
deliv = [
    'Reporte impreso lleno y firmado',
    'Tickets de salida (TODOS)',
    'Papel de errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Tareas Cl 3 recogidas + lista quienes NO entregaron',
    'Registro chequeo portafolio',
    'Foto del tablero - Frase del Dia + will/won\'t + lugares con the',
    'Foto/video simulacion HOTEL FRONT DESK',
]
ev = [
    'Lei la hoja de ruta COMPLETA antes de clase',
    'Recuperacion Cl 3 (horas/precios/should), Cl 2 (pronombres) y Cl 1 (can): oral, DE PIE, instruccion exacta',
    'Errores oidos al tablero ANONIMOS + 1 min de re-produccion',
    'Chequeo publico de portafolio: pregunte y ANOTE',
    'ESCRIBI la Frase del Dia ANTES + coro 2x + la inserte 3+ veces natural',
    'Al cierre 1 estudiante la dijo + 1 la uso en oracion nueva',
    'Recogi la tarea Cl 3 y anote quien NO entrego',
    'Verifique virtud Cl 4 = PRUDENCIA v1 dia 4',
    'Cubri M6 (will/won\'t + what time + at, p.73) y M7 (the tha/thiy + lugares, p.90) DESDE EL LIBRO',
    'Ensene los verbos de rutina con mimica (wake up, shower, eat breakfast/lunch/dinner, study, go to bed)',
    'La historia del plan loco fue narrada e interactiva (pausa + coro + agregar), sin huecos',
    'Producto del bloque: cada estudiante dijo su plan real con will + lugar + hora',
    'Drill de movimiento: TODOS DE PIE, estaciones del tablero, velocidad creciente',
    'Simulacion HOTEL FRONT DESK: 1 guest + observers con tarea + yo COACH (NUNCA jugue guest)',
    'Horarios del hotel los escribi YO en tablero en el momento (cero material impreso)',
    'MY WORLD pieza 4 (my plan) dicha por cada estudiante',
    'Ticket de salida: recogi TODOS, sin evaluar ni comentar',
    'Tarea con due date explicito (Cl 5 before 7:00 PM), 15-20 min, NO fragmentada + portafolio diario',
    'NO comente nada de evaluaciones',
    'Anuncie Cl 5 = Where do we eat? - the present (M8 del libro)',
]
build_report_v2(os.path.join(A1_4H, 'REPORTES', 'A1_4h_Class4_REPORTE.pdf'),
    'A1 INTENSIVO 4H | Clase 4 | M6 WILL + WHAT TIME + M7 THE + PLACES | PRUDENCIA v1 | FRASE DEL DIA',
    'M6 futuro simple will/won\'t + what time + at (p.73) con rutina diaria (p.72) + M7 articulo the (tha/thiy) + lugares house/apartment/school/park/office/pool/restaurant + swim/work/eat (p.90) + MY PLAN TODAY (p.75) + simulacion HOTEL FRONT DESK + MY WORLD pieza 4',
    act, deliv, ev, S)
print('OK: A1_4h_Class4_REPORTE.pdf')
print('\n2 PDFs generados en A1/4h/ para Cl 4.')
