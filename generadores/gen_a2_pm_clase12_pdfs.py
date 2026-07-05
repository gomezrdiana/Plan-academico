#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 Nocturno PM (Tomas) - Clase 12 - GUIA + REPORTE.
M14 We Studied During the Game. Again! - While, During, and Again (p.121-132).
JUSTICIA v1 dia 2 (Cl 11-15); Cl 16 abre FORTALEZA.
Salida en A2/V2/. Mirror estructural de A2_Class11_PRINT.md.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_DIR = os.path.join(D, 'A2', 'V2')
os.makedirs(V2_DIR, exist_ok=True)

# =================== GUIA Cl 12 ===================
md_to_pdf(
    os.path.join(V2_DIR, 'A2_Class12_PRINT.md'),
    os.path.join(V2_DIR, 'A2_Class12_GUIA.pdf'),
)

# =================== REPORTE Cl 12 ===================
a2_c12_act = [
    ('OPENER: Frase + JUSTICIA dia 2 + mystery Cl 11 (already/still/until) + bridge a while/during/again', '12 min'),
    ('CONTENT M14 WHILE / DURING / AGAIN: while=mientras (dos clausulas), during=durante (evento/periodo), again=otra vez (al final)', '52 min'),
    ('LIVE: TEAM COORDINATION ON A BUSY SHIFT (DE PIE) - quien hizo que a la vez (while) / durante (during) / de nuevo (again) + credito justo', '36 min'),
    ('CIERRE: Error recap + frase close + VATS justicia dia 2 + tarea + Cl 13 announce (M15 present perfect)', '20 min'),
]
a2_c12_deliv = [
    'Reporte impreso lleno',
    'Foto del board final con los errores tipicos (anonimos)',
    'Foto/video de la Simulacion Team Coordination on a Busy Shift',
    'Tu libreta personal con errores literales + NOMBRE por bloque',
    'Lista quienes NO entregaron tarea Cl 11',
    'Conteo: 2 rotaciones simulacion + 1 demo al frente + observer count (usos correctos + creditos justos)',
    'Respuestas del VATS dia 2 (equipo bien/mal) con nombres en libreta',
    'Lista actualizada de asistencia',
]
a2_c12_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / while-during-again / simulacion / cierre)',
    'Conduje el mystery Cl 11 (already/still/until) como termometro, sin corregir',
    'Cubri M14 While / During / Again DESDE EL LIBRO (clausula vs periodo + posicion de again)',
    'Enseñe: while + dos clausulas (sujeto+verbo); during + evento/periodo (sustantivo); again al final',
    'Mostre la regla del futuro con while (segunda clausula en presente, no will)',
    'Corregi los errores tipicos: while+sustantivo / futuro doble con while / again mal colocado / during+clausula',
    'Simulacion Team Coordination fue PROFESIONAL/realista (turno de trabajo, no fantasia)',
    'Mantuve la simulacion DE PIE',
    'Asigne observer count en round 2 (usos correctos + creditos justos al equipo)',
    'Camine con papel de errores anonimo en el cierre',
    'En libreta personal anote errores con NOMBRE',
    'Conduje el VATS dia 2 JUSTICIA (cuando trabajaste bien/mal en equipo)',
    'Active la virtud: credito justo al companero (name them, fair share)',
    'Di la tarea con DUE DATE explicita (antes de Cl 13, 7:00 PM) - no fragmentada',
    'NO acepte push-back sobre la longitud de la tarea',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 13 (M15 I Have Visited London - present perfect + JUSTICIA v1 dia 3)',
]

build_report_v2(
    os.path.join(V2_DIR, 'A2_Class12_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 12 de 55 | 2 HORAS | M14 WHILE / DURING / AGAIN',
    'M14 We Studied During the Game. Again! (while=mientras / during=durante / again=otra vez) + Team Coordination | JUSTICIA v1 dia 2',
    a2_c12_act, a2_c12_deliv, a2_c12_eval, S,
)

print('\nA2 PM Clase 12 generada (GUIA + REPORTE) en A2/V2/.')
