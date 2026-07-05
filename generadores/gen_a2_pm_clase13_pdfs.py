#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 Nocturno PM (Tomas) - Clase 13 - GUIA + REPORTE.
M15 I Have Visited London - The Present Perfect (Regular Verbs) (p.133-146).
JUSTICIA v1 dia 3 (Cl 11-15); Cl 16 abre FORTALEZA.
Salida en A2/V2/. Mirror estructural de A2_Class12_PRINT.md.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_DIR = os.path.join(D, 'A2', 'V2')
os.makedirs(V2_DIR, exist_ok=True)

# =================== GUIA Cl 13 ===================
md_to_pdf(
    os.path.join(V2_DIR, 'A2_Class13_PRINT.md'),
    os.path.join(V2_DIR, 'A2_Class13_GUIA.pdf'),
)

# =================== REPORTE Cl 13 ===================
a2_c13_act = [
    ('OPENER: Frase + JUSTICIA dia 3 + mystery Cl 12 (while/during/again) + bridge al present perfect', '12 min'),
    ('CONTENT M15 PRESENT PERFECT (REGULAR): have/has + participio -ed + afirm/neg/interrog + abreviada + short answer', '52 min'),
    ('LIVE: JOB INTERVIEW - YOUR EXPERIENCE (DE PIE) - contar lo que has hecho (I have worked / studied / visited / helped)', '36 min'),
    ('CIERRE: Error recap + frase close + VATS justicia dia 3 + tarea + Cl 14 announce (M16 present perfect irregular)', '20 min'),
]
a2_c13_deliv = [
    'Reporte impreso lleno',
    'Foto del board final con los errores tipicos (anonimos)',
    'Foto/video de la Simulacion Job Interview - Your Experience',
    'Tu libreta personal con errores literales + NOMBRE por bloque',
    'Lista quienes NO entregaron tarea Cl 12',
    'Conteo: 2 rotaciones simulacion + 1 demo al frente + observer count (present perfect correctos + short answers)',
    'Respuestas del VATS dia 3 (trato a quien tiene menos) con nombres en libreta',
    'Lista actualizada de asistencia',
]
a2_c13_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / present perfect / simulacion / cierre)',
    'Conduje el mystery Cl 12 (while/during/again) como termometro, sin corregir',
    'Cubri M15 Present Perfect Regular DESDE EL LIBRO (have/has + participio -ed)',
    'Enseñe: he/she/it = has; participio regular = verbo + -ed; contraste con pasado simple',
    'Mostre afirmativo/negativo/interrogativo, version abreviada y short answer',
    'Corregi los errores tipicos: falta -ed / have con he / orden de pregunta / short answer repitiendo el verbo',
    'Simulacion Job Interview fue PROFESIONAL/realista (experiencia laboral, no fantasia)',
    'Mantuve la simulacion DE PIE',
    'Asigne observer count en round 2 (present perfect correctos + short answers)',
    'Camine con papel de errores anonimo en el cierre',
    'En libreta personal anote errores con NOMBRE',
    'Conduje el VATS dia 3 JUSTICIA (como tratas a quien tiene menos que tu)',
    'Active la virtud: nombrar lo justo que has hecho por otros (I have helped / shared)',
    'Di la tarea con DUE DATE explicita (antes de Cl 14, 7:00 PM) - no fragmentada',
    'NO acepte push-back sobre la longitud de la tarea',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 14 (M16 I Have Gone to Paris - present perfect irregular + JUSTICIA v1 dia 4)',
]

build_report_v2(
    os.path.join(V2_DIR, 'A2_Class13_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 13 de 55 | 2 HORAS | M15 PRESENT PERFECT (REGULAR)',
    'M15 I Have Visited London (have/has + participio -ed) + Job Interview Your Experience | JUSTICIA v1 dia 3',
    a2_c13_act, a2_c13_deliv, a2_c13_eval, S,
)

print('\nA2 PM Clase 13 generada (GUIA + REPORTE) en A2/V2/.')
