#!/usr/bin/env python3
"""A2 Nocturno PM (Tomas) - Clase 11 - GUIA + REPORTE.
M13 I already knew that! - Already, Still, and Until (p.107-120).
JUSTICIA v1 dia 1 ABRE bloque (Cl 11-15); Cl 16 abre FORTALEZA.
Salida en A2/V2/. Mirror estructural de A2_Class10_PRINT.md.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
V2_DIR = os.path.join(D, 'A2', 'V2')
os.makedirs(V2_DIR, exist_ok=True)

# =================== GUIA Cl 11 ===================
md_to_pdf(
    os.path.join(V2_DIR, 'A2_Class11_PRINT.md'),
    os.path.join(V2_DIR, 'A2_Class11_GUIA.pdf'),
)

# =================== REPORTE Cl 11 ===================
a2_c11_act = [
    ('OPENER: Frase + JUSTICIA dia 1 ABRE + mystery Cl 10 (dia interrumpido) + bridge a especificadores de tiempo', '12 min'),
    ('CONTENT M13 ALREADY / STILL / UNTIL: already=ya (antes del verbo / tras to be), still=todavia, until=hasta + pasado/presente/futuro + continuo', '52 min'),
    ('LIVE: PROJECT STATUS UPDATE AT WORK (DE PIE) - reportar ya hecho / sigue en proceso / hasta cuando + thank the team', '36 min'),
    ('CIERRE: Error recap + frase close + VATS justicia dia 1 (abre bloque) + tarea + Cl 12 announce (M14 While/During/Again)', '20 min'),
]
a2_c11_deliv = [
    'Reporte impreso lleno',
    'Foto del board final con los errores tipicos (anonimos)',
    'Foto/video de la Simulacion Project Status Update at Work',
    'Tu libreta personal con errores literales + NOMBRE por bloque',
    'Lista quienes NO entregaron tarea Cl 10',
    'Conteo: 2 rotaciones simulacion + 1 demo al frente + observer count (usos correctos + thank you)',
    'Respuestas del VATS dia 1 (a quien le debes un gracias) con nombres en libreta',
    'Lista actualizada de asistencia',
]
a2_c11_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / already-still-until / simulacion / cierre)',
    'Conduje el mystery Cl 10 (past continuous interrumpido) como termometro, sin corregir',
    'Cubri M13 Already / Still / Until DESDE EL LIBRO (posiciones + pasado/presente/futuro + continuo)',
    'Enseñe: already/still antes del verbo o tras to be; until antes del punto de parada (como en español)',
    'Mostre el uso en continuo (was already living / still working / will be living until)',
    'Corregi los errores tipicos: orden con to be / already al inicio / until afirmativo donde pide negativo / still + verbo mal',
    'Simulacion Project Status Update fue PROFESIONAL/realista (equipo de trabajo, no fantasia)',
    'Mantuve la simulacion DE PIE',
    'Asigne observer count en round 2 (usos correctos + thank you al equipo)',
    'Camine con papel de errores anonimo en el cierre',
    'En libreta personal anote errores con NOMBRE',
    'Conduje el VATS dia 1 que ABRE JUSTICIA (a quien le debes un gracias)',
    'Active la virtud: credito justo al equipo (name the teammate, thank you)',
    'Di la tarea con DUE DATE explicita (antes de Cl 12, 7:00 PM) - no fragmentada',
    'NO acepte push-back sobre la longitud de la tarea',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 12 (M14 While, During, Again + JUSTICIA v1 dia 2)',
]

build_report_v2(
    os.path.join(V2_DIR, 'A2_Class11_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 11 de 55 | 2 HORAS | M13 ALREADY / STILL / UNTIL',
    'M13 I already knew that! (already=ya / still=todavia / until=hasta) + Project Status Update | JUSTICIA v1 dia 1 ABRE bloque (Cl 16 abre FORTALEZA)',
    a2_c11_act, a2_c11_deliv, a2_c11_eval, S,
)

print('\nA2 PM Clase 11 generada (GUIA + REPORTE) en A2/V2/.')
