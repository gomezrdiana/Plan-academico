#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guia + reporte del A1 INTENSIVO 4H Cl 5:
- M8 Where Do We Eat? - The Simple Present (p.99-110), SOLO (primer tiempo con dos auxiliares do/does)
- Virtud PRUDENCIA v1 dia 5. Recuperacion Cl 4/3/2. Simulacion THE GYM REGISTRATION DESK.
- Cierre anuncia Cl 6 = SPECIAL SESSION (sin detalles).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(A1_4H, exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class5_PRINT.md'), os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class5_GUIA.pdf'))
print('OK: A1_4h_Class5_GUIA.pdf')

act = [
    ('BLOQUE 1 - Apertura (recuperacion Cl 4/3/2 DE PIE + portafolio + Frase del Dia + tarea Cl 4)', '35 min'),
    ('BLOQUE 2 - M8 presente simple do/does (historia interactiva + instalacion do-vs-does + meta)', '85 min'),
    ('BLOQUE 3 - Drill de pie do/does + Simulacion THE GYM REGISTRATION DESK + MY WORLD pieza 5', '90 min'),
    ('BLOQUE 4 - Ticket de salida + tarea + error paper + anuncio Cl 6 SPECIAL SESSION', '30 min'),
]
deliv = [
    'Reporte impreso lleno y firmado',
    'Tickets de salida (TODOS)',
    'Papel de errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Tareas Cl 4 (MY PLAN TODAY) recogidas + lista quienes NO entregaron',
    'Registro chequeo portafolio',
    'Foto del tablero - Frase del Dia + tabla do/does',
    'Foto/video simulacion THE GYM REGISTRATION DESK',
]
ev = [
    'Lei la hoja de ruta COMPLETA antes de clase',
    'Recuperacion Cl 4 (will+lugares), Cl 3 (should+numeros) y Cl 2 (pronombres): oral, DE PIE, instruccion exacta',
    'Errores oidos al tablero ANONIMOS + 1 min de re-produccion',
    'Chequeo publico de portafolio: pregunte y ANOTE',
    'ESCRIBI la Frase del Dia ANTES + coro 2x + la inserte 3+ veces natural',
    'Al cierre 1 estudiante la dijo + 1 la uso en oracion nueva',
    'Recogi la tarea Cl 4 y anote quien NO entrego',
    'Verifique virtud Cl 5 = PRUDENCIA v1 dia 5 (cierre del bloque de virtud)',
    'Cubri M8 DESDE EL LIBRO (p.100): do (du) / does (daz), unico tiempo con DOS auxiliares',
    'Ensene la tabla: he/she/it -> DOES; I/you/we/they -> DO',
    'Ensene don\'t (dont) / doesn\'t (dazunt) + respuestas cortas do/does',
    'Ensene la forma del libro I DO PLAY (NO adelante la omision del auxiliar - eso es M9)',
    'La historia de la rutina del perro fue narrada e interactiva (pausa + coro + agregar), sin huecos',
    'Drill do-or-does: TODOS DE PIE, cambio de lugar con frase correcta, velocidad creciente',
    'Simulacion GYM DESK: formulario oral integrando do/does + what time + where + can',
    'Simulacion: 1 guest + observers con tarea + yo COACH (NUNCA jugue guest)',
    'MY WORLD pieza 5 (my habits) dicha por cada estudiante',
    'Ticket de salida: recogi TODOS, sin evaluar ni comentar',
    'Tarea con due date explicito (Cl 6 before 7:00 PM), 15-20 min, NO fragmentada + portafolio diario',
    'Anuncie Cl 6 SOLO como SPECIAL SESSION (cero detalles de formato/contenido/evaluacion)',
]
build_report_v2(os.path.join(A1_4H, 'REPORTES', 'A1_4h_Class5_REPORTE.pdf'),
    'A1 INTENSIVO 4H | Clase 5 | M8 SIMPLE PRESENT DO/DOES | PRUDENCIA v1 | FRASE DEL DIA',
    'M8 presente simple con do/does (p.100): unico tiempo con dos auxiliares, tabla he/she/it=does, don\'t/doesn\'t, respuestas cortas + historia rutina del perro + simulacion THE GYM REGISTRATION DESK (formulario oral que integra Cl 1-4) + MY WORLD pieza 5 (my habits) + anuncio Cl 6 special session',
    act, deliv, ev, S)
print('OK: A1_4h_Class5_REPORTE.pdf')
print('\n2 PDFs generados en A1/4h/ para Cl 5.')
