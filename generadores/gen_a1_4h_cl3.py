#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guia + reporte del A1 INTENSIVO 4H Cl 3:
- M4 Where Should We Live? - Giving Recommendations (p.41-60) + M5 Numbers to 100 (p.61-70)
- Virtud PRUDENCIA v1 dia 3. Recuperacion Cl 2 + Cl 1. Simulacion THE TRAVEL DESK.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'A1', '4h')
os.makedirs(A1_4H, exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class3_PRINT.md'), os.path.join(A1_4H, 'A1_4h_Class3_GUIA.pdf'))
print('OK: A1_4h_Class3_GUIA.pdf')

act = [
    ('BLOQUE 1 - Apertura (recuperacion Cl 2 y Cl 1 DE PIE + portafolio + Frase del Dia + tarea Cl 2)', '35 min'),
    ('BLOQUE 2 - M4 should + where y M5 numeros/horas/precios (historia interactiva + meta)', '85 min'),
    ('BLOQUE 3 - Drill de pie numeros/should + Simulacion THE TRAVEL DESK + MY WORLD pieza 3', '90 min'),
    ('BLOQUE 4 - Ticket de salida + tarea + error paper + anuncio Cl 4', '30 min'),
]
deliv = [
    'Reporte impreso lleno y firmado',
    'Tickets de salida (TODOS)',
    'Papel de errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Tareas Cl 2 recogidas + lista quienes NO entregaron',
    'Registro chequeo portafolio',
    'Foto del tablero - Frase del Dia + should/where + numeros',
    'Foto/video simulacion THE TRAVEL DESK',
]
ev = [
    'Lei la hoja de ruta COMPLETA antes de clase',
    'Recuperacion Cl 2 (pronombres + respuesta corta) y Cl 1 (can): oral, DE PIE, instruccion exacta',
    'Errores oidos al tablero ANONIMOS + 1 min de re-produccion',
    'Chequeo publico de portafolio: pregunte y ANOTE',
    'ESCRIBI la Frase del Dia ANTES + coro 2x + la inserte 3+ veces natural',
    'Al cierre 1 estudiante la dijo + 1 la uso en oracion nueva',
    'Recogi la tarea Cl 2 y anote quien NO entrego',
    'Verifique virtud Cl 3 = PRUDENCIA v1 dia 3',
    'Cubri M4 (should/shouldn\'t/where/in, p.43) y M5 (numeros/horas/precios, p.62-63) DESDE EL LIBRO',
    'Ensene pares trampa thirteen/thirty, fourteen/forty, fifteen/fifty',
    'Ensene la hora en dos grupos sin and + oh para :01-:09 + o\'clock en punto',
    'La historia fue narrada e interactiva (pausa + coro + agregar), sin huecos',
    'Drill de movimiento: TODOS DE PIE, velocidad creciente, cierre en produccion libre',
    'Simulacion TRAVEL DESK: 1 guest + observers con tarea + yo COACH (NUNCA jugue guest)',
    'Precios y horas del tablero los escribi YO en el momento (cero material impreso)',
    'NO use How much (no ensenado): el agente DA el precio y el cliente lo repite',
    'MY WORLD pieza 3 (my city + my numbers) dicha por cada estudiante',
    'Ticket de salida: recogi TODOS, sin evaluar ni comentar',
    'Tarea con due date explicito (Cl 4 before 7:00 PM), 15-20 min, NO fragmentada + portafolio diario',
    'Anuncie Cl 4 = What time will you eat lunch? (M6+M7 del libro)',
]
build_report_v2(os.path.join(A1_4H, 'A1_4h_Class3_REPORTE.pdf'),
    'A1 INTENSIVO 4H | Clase 3 | M4 SHOULD + WHERE + M5 NUMBERS TO 100 | PRUDENCIA v1 | FRASE DEL DIA',
    'M4 recomendaciones con should/shouldn\'t + where + in (p.43) + M5 numeros 0-100, horas (two ten / two oh eight / six o\'clock) y precios (seven thirty-five) (p.62-63) + historia interactiva donde vivir + simulacion THE TRAVEL DESK + MY WORLD pieza 3',
    act, deliv, ev, S)
print('OK: A1_4h_Class3_REPORTE.pdf')
print('\n2 PDFs generados en A1/4h/ para Cl 3.')
