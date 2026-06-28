#!/usr/bin/env python3
"""A2 Nocturno PM (Tomas) - Clase 7 - GUIA + REPORTE.
M8 I Think that I'm Learning! - The Relative Pronoun "That". TEMPLANZA v1 dia 2.
Salida en A2/V2/. Mirror estructural de A2_Class6_PRINT.md.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
V2_DIR = os.path.join(D, 'A2', 'V2')
os.makedirs(V2_DIR, exist_ok=True)

# =================== GUIA Cl 7 ===================
md_to_pdf(
    os.path.join(V2_DIR, 'A2_Class7_PRINT.md'),
    os.path.join(V2_DIR, 'A2_Class7_GUIA.pdf'),
)

# =================== REPORTE Cl 7 ===================
a2_c7_act = [
    ('OPENER: Frase + TEMPLANZA dia 2 + mystery Cl 6 (might) + bridge a "that"', '12 min'),
    ('CONTENT M8 THAT: relativo "that" + concordancia de tiempos + practica pares', '52 min'),
    ('LIVE: WORKPLACE RELAY (DE PIE) - relatar lo dicho/pensado con "that"', '36 min'),
    ('CIERRE: Error recap + frase close + VATS templanza dia 2 + tarea + Cl 8 announce', '20 min'),
]
a2_c7_deliv = [
    'Reporte impreso lleno',
    'Foto del board final con los 3 errores tipicos (anonimos)',
    'Foto/video de la Simulacion Workplace Relay',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Lista quienes NO entregaron tarea Cl 6',
    'Conteo: 2 rotaciones simulacion + 1 demo al frente + observer count',
    'Respuestas VATS dia 2 (cuando te excediste) anotadas con nombres en libreta',
    'Lista actualizada de asistencia',
]
a2_c7_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / that / simulacion / cierre)',
    'Conduje el mystery Cl 6 (might) como termometro, sin corregir',
    'Cubri M8 THAT DESDE EL LIBRO (5 reglas + vocab know/think/see/hear/feel/say)',
    'Enseñe la concordancia de tiempos: verbo 1 pasado -> verbo 2 pasado',
    'Mostre el contraste presente/pasado del libro (p.63)',
    'Enseñe la regla 4: clausulas negativas e interrogativas con that',
    'Corregi los errores tipicos: concordancia rota / falta sujeto frase 2 / "no think"',
    'Simulacion Workplace Relay fue PROFESIONAL/realista (no temas familiares)',
    'Mantuve la simulacion DE PIE',
    'Asigne observer count en round 2',
    'Camine con papel de errores anonimo en el cierre',
    'En libreta personal anote 3 errores con NOMBRE',
    'Conduje VATS dia 2 (cuando te excediste) - 2 respuestas max',
    'Di la tarea con DUE DATE explicita (antes de Cl 8, 7:00 PM) - no fragmentada',
    'NO acepte push-back sobre la longitud de la tarea',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 8 (M10 First Conditional + TEMPLANZA dia 3)',
]

build_report_v2(
    os.path.join(V2_DIR, 'A2_Class7_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 7 de 55 | 2 HORAS | M8 RELATIVE PRONOUN "THAT"',
    'M8 I Think that I\'m Learning! (relativo "that" + concordancia de tiempos) + Workplace Relay | TEMPLANZA v1 dia 2',
    a2_c7_act, a2_c7_deliv, a2_c7_eval, S,
)

print('\nA2 PM Clase 7 generada (GUIA + REPORTE) en A2/V2/.')
