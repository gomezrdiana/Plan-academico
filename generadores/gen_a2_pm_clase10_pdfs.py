#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 Nocturno PM (Tomas) - Clase 10 - GUIA + REPORTE.
M12 I Was Playing when My Mom Called. - Past Simple vs Past Continuous.
TEMPLANZA v1 dia 5 CIERRA bloque; Cl 11 abre JUSTICIA.
Salida en A2/V2/. Mirror estructural de A2_Class9_PRINT.md.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_DIR = os.path.join(D, 'A2', 'V2')
os.makedirs(V2_DIR, exist_ok=True)

# =================== GUIA Cl 10 ===================
md_to_pdf(
    os.path.join(V2_DIR, 'A2_Class10_PRINT.md'),
    os.path.join(V2_DIR, 'A2_Class10_GUIA.pdf'),
)

# =================== REPORTE Cl 10 ===================
a2_c10_act = [
    ('OPENER: Frase + TEMPLANZA dia 5 CIERRA + mystery Cl 9 (2nd cond) + bridge al pasado interrumpido', '12 min'),
    ('CONTENT M12 PAST SIMPLE vs CONTINUOUS: was/were+ing (larga) interrumpida por past simple (corta) + when/while', '52 min'),
    ('LIVE: INCIDENT REPORT AT WORK (DE PIE) - que estaba pasando cuando algo interrumpio', '36 min'),
    ('CIERRE: Error recap + frase close + VATS templanza dia 5 (cierra bloque) + tarea + Cl 11 announce (JUSTICIA)', '20 min'),
]
a2_c10_deliv = [
    'Reporte impreso lleno',
    'Foto del board final con los 3 errores tipicos (anonimos)',
    'Foto/video de la Simulacion Incident Report at Work',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Lista quienes NO entregaron tarea Cl 9',
    'Conteo: 2 rotaciones simulacion + 1 demo al frente + observer count',
    'Respuestas de la retrospectiva oral TEMPLANZA (como mantienes la calma) con nombres en libreta',
    'Lista actualizada de asistencia',
]
a2_c10_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / past continuous / simulacion / cierre)',
    'Conduje el mystery Cl 9 (second conditional) como termometro, sin corregir',
    'Cubri M12 Past Simple vs Past Continuous DESDE EL LIBRO (interrupcion + when/while)',
    'Enseñe: accion larga = was/were + -ing; interrupcion corta = past simple',
    'Mostre el uso de when (antes de la corta) y while (antes de la larga)',
    'Corregi los errores tipicos: falta -ing / formas invertidas / pregunta mal armada',
    'Simulacion Incident Report fue PROFESIONAL/realista (no temas familiares)',
    'Mantuve la simulacion DE PIE',
    'Asigne observer count en round 2',
    'Camine con papel de errores anonimo en el cierre',
    'En libreta personal anote 3 errores con NOMBRE',
    'Conduje la RETROSPECTIVA oral que CIERRA TEMPLANZA (VATS dia 5: como mantienes la calma)',
    'Di la tarea con DUE DATE explicita (antes de Cl 11, 7:00 PM) - no fragmentada',
    'NO acepte push-back sobre la longitud de la tarea',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 11 (siguiente modulo del libro + JUSTICIA v1 dia 1 ABRE nuevo bloque)',
]

build_report_v2(
    os.path.join(V2_DIR, 'A2_Class10_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 10 de 55 | 2 HORAS | M12 PAST SIMPLE vs PAST CONTINUOUS',
    'M12 I Was Playing when My Mom Called. (interrupcion: was/were+ing + past simple) + Incident Report | TEMPLANZA v1 dia 5 CIERRA bloque (Cl 11 abre JUSTICIA)',
    a2_c10_act, a2_c10_deliv, a2_c10_eval, S,
)

print('\nA2 PM Clase 10 generada (GUIA + REPORTE) en A2/V2/.')
