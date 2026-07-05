#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 Nocturno PM (Tomas) - Clase 8 - GUIA + REPORTE.
M10 I'll Buy Lunch! - The First Conditional (SE SALTA M9). TEMPLANZA v1 dia 3.
Salida en A2/V2/. Mirror estructural de A2_Class7_PRINT.md.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_DIR = os.path.join(D, 'A2', 'V2')
os.makedirs(V2_DIR, exist_ok=True)

# =================== GUIA Cl 8 ===================
md_to_pdf(
    os.path.join(V2_DIR, 'A2_Class8_PRINT.md'),
    os.path.join(V2_DIR, 'A2_Class8_GUIA.pdf'),
)

# =================== REPORTE Cl 8 ===================
a2_c8_act = [
    ('OPENER: Frase + TEMPLANZA dia 3 + mystery Cl 7 (that) + bridge al first conditional', '12 min'),
    ('CONTENT M10 1ST CONDITIONAL: if+presente / will + negativo + pregunta + practica pares', '52 min'),
    ('LIVE: CUSTOMER SERVICE / DEAL DESK (DE PIE) - condiciones probables if/will', '36 min'),
    ('CIERRE: Error recap + frase close + VATS templanza dia 3 + tarea + Cl 9 announce', '20 min'),
]
a2_c8_deliv = [
    'Reporte impreso lleno',
    'Foto del board final con los 3 errores tipicos (anonimos)',
    'Foto/video de la Simulacion Customer Service / Deal Desk',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Lista quienes NO entregaron tarea Cl 7',
    'Conteo: 2 rotaciones simulacion + 1 demo al frente + observer count',
    'Respuestas VATS dia 3 (decir mucho o poco) anotadas con nombres en libreta',
    'Lista actualizada de asistencia',
]
a2_c8_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / first conditional / simulacion / cierre)',
    'Conduje el mystery Cl 7 (that) como termometro, sin corregir',
    'CONFIRME que se salta M9 (hueco) y se pasa a M10 - no inventé contenido',
    'Cubri M10 First Conditional DESDE EL LIBRO (if+presente / will, eventos probables)',
    'Mostre las 2 columnas: clausula if (presente) / clausula resultado (will)',
    'Enseñe negativo en ambas clausulas (don\'t/won\'t) y pregunta en el resultado',
    'Corregi el error clave: "will" en la clausula del "if"',
    'Simulacion Deal Desk fue PROFESIONAL/realista (no temas familiares)',
    'Mantuve la simulacion DE PIE',
    'Asigne observer count en round 2',
    'Camine con papel de errores anonimo en el cierre',
    'En libreta personal anote 3 errores con NOMBRE',
    'Conduje VATS dia 3 (decir mucho o poco) - 2 respuestas max',
    'Di la tarea con DUE DATE explicita (antes de Cl 9, 7:00 PM) - no fragmentada',
    'NO acepte push-back sobre la longitud de la tarea',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 9 (M11 Second Conditional + TEMPLANZA dia 4)',
]

build_report_v2(
    os.path.join(V2_DIR, 'A2_Class8_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 8 de 55 | 2 HORAS | M10 FIRST CONDITIONAL (salta M9)',
    'M10 I\'ll Buy Lunch! (first conditional: if+presente / will) + Customer Service Deal Desk | TEMPLANZA v1 dia 3',
    a2_c8_act, a2_c8_deliv, a2_c8_eval, S,
)

print('\nA2 PM Clase 8 generada (GUIA + REPORTE) en A2/V2/.')
