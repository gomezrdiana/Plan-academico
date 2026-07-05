#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 Nocturno PM (Tomas) - Clase 6 - GUIA + REPORTE.
M7 You Might Learn Something - The Modal "Might". TEMPLANZA v1 dia 1 ABRE bloque.
Salida en A2/V2/. Mirror estructural de A2_Class5_PRINT.md.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_DIR = os.path.join(D, 'A2', 'V2')
os.makedirs(V2_DIR, exist_ok=True)

# =================== GUIA Cl 6 ===================
md_to_pdf(
    os.path.join(V2_DIR, 'A2_Class6_PRINT.md'),
    os.path.join(V2_DIR, 'A2_Class6_GUIA.pdf'),
)

# =================== REPORTE Cl 6 ===================
a2_c6_act = [
    ('OPENER: Frase + TEMPLANZA dia 1 ABRE + mystery Cl 5 + bridge a "might"', '12 min'),
    ('CONTENT M7 MIGHT: reglas del libro + respuestas a preguntas futuras + practica pares', '52 min'),
    ('LIVE: TEAM PLANNING CALL (DE PIE) - respuestas inciertas con might', '36 min'),
    ('CIERRE: Error recap + frase close + VATS templanza dia 1 + tarea + Cl 7 announce', '20 min'),
]
a2_c6_deliv = [
    'Reporte impreso lleno',
    'Foto del board final con los 3 errores tipicos (anonimos)',
    'Foto/video de la Simulacion Team Planning Call',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Lista quienes NO entregaron tarea Cl 5',
    'Conteo: 2 rotaciones simulacion + 1 demo al frente + observer count',
    'Respuestas VATS dia 1 (autocontrol mas/menos) anotadas con nombres en libreta',
    'Lista actualizada de asistencia',
]
a2_c6_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / might / simulacion / cierre)',
    'ABRI el bloque TEMPLANZA: explique autocontrol/balance/calma',
    'Conduje el mystery Cl 5 (schedule + plan) como termometro, sin corregir',
    'Cubri M7 MIGHT DESDE EL LIBRO (5 reglas, estructura sujeto+might+verbo base)',
    'Enseñe que "might" RESPONDE preguntas futuras (no se usa en interrogativo)',
    'Enseñe la respuesta corta "might" / "might not"',
    'Corregi los errores tipicos: "to" / S / -ing / "will might" despues de might',
    'Simulacion Team Planning Call fue PROFESIONAL/realista (no temas familiares)',
    'Mantuve la simulacion DE PIE',
    'Asigne observer count en round 2',
    'Camine con papel de errores anonimo en el cierre',
    'En libreta personal anote 3 errores con NOMBRE',
    'Conduje VATS dia 1 (autocontrol mas/menos) - 2 respuestas max',
    'Di la tarea con DUE DATE explicita (antes de Cl 7, 7:00 PM) - no fragmentada',
    'NO acepte push-back sobre la longitud de la tarea',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 7 (M8 relative pronoun "that" + TEMPLANZA dia 2)',
]

build_report_v2(
    os.path.join(V2_DIR, 'A2_Class6_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 6 de 55 | 2 HORAS | M7 THE MODAL "MIGHT"',
    'M7 You Might Learn Something (modal "might" para posibilidad) + Team Planning Call | TEMPLANZA v1 dia 1 ABRE bloque',
    a2_c6_act, a2_c6_deliv, a2_c6_eval, S,
)

print('\nA2 PM Clase 6 generada (GUIA + REPORTE) en A2/V2/.')
