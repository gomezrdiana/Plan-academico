#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 Nocturno PM (Tomas) - Clase 9 - GUIA + REPORTE.
M11 I'd Eat a Cookie. - The Second Conditional. TEMPLANZA v1 dia 4.
Salida en A2/V2/. Mirror estructural de A2_Class8_PRINT.md.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_DIR = os.path.join(D, 'A2', 'V2')
os.makedirs(V2_DIR, exist_ok=True)

# =================== GUIA Cl 9 ===================
md_to_pdf(
    os.path.join(V2_DIR, 'A2_Class9_PRINT.md'),
    os.path.join(V2_DIR, 'A2_Class9_GUIA.pdf'),
)

# =================== REPORTE Cl 9 ===================
a2_c9_act = [
    ('OPENER: Frase + TEMPLANZA dia 4 + mystery Cl 8 (first cond) + bridge al second conditional', '12 min'),
    ('CONTENT M11 2ND CONDITIONAL: if+pasado / would + contraste con 1st + negativo + pregunta + pares', '52 min'),
    ('LIVE: JOB INTERVIEW HYPOTHETICALS (DE PIE) - escenarios imaginarios if were/would', '36 min'),
    ('CIERRE: Error recap + frase close + VATS templanza dia 4 + tarea + Cl 10 announce', '20 min'),
]
a2_c9_deliv = [
    'Reporte impreso lleno',
    'Foto del board final con los 3 errores tipicos (anonimos)',
    'Foto/video de la Simulacion Job Interview Hypotheticals',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Lista quienes NO entregaron tarea Cl 8',
    'Conteo: 2 rotaciones simulacion + 1 demo al frente + observer count',
    'Respuestas VATS dia 4 (que actividad te controla / controlas) anotadas con nombres en libreta',
    'Lista actualizada de asistencia',
]
a2_c9_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / second conditional / simulacion / cierre)',
    'Conduje el mystery Cl 8 (first conditional) como termometro, sin corregir',
    'Cubri M11 Second Conditional DESDE EL LIBRO (if+pasado / would, eventos imaginarios)',
    'Mostre el CONTRASTE 1st vs 2nd (present+will / past+would) en 2 columnas',
    'Enseñe negativo (wouldn\'t / didn\'t have) y pregunta',
    'Corregi el error clave: "would" en la clausula del "if" y "will" por "would"',
    'Corregi "didn\'t had" -> "didn\'t have"',
    'Simulacion Job Interview fue PROFESIONAL/realista (no temas familiares)',
    'Mantuve la simulacion DE PIE',
    'Asigne observer count en round 2',
    'Camine con papel de errores anonimo en el cierre',
    'En libreta personal anote 3 errores con NOMBRE',
    'Conduje VATS dia 4 (que actividad te controla / controlas) - 2 respuestas max',
    'Di la tarea con DUE DATE explicita (antes de Cl 10, 7:00 PM) - no fragmentada',
    'NO acepte push-back sobre la longitud de la tarea',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 10 (M12 Past Simple vs Past Continuous + TEMPLANZA dia 5 CIERRA bloque)',
]

build_report_v2(
    os.path.join(V2_DIR, 'A2_Class9_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 9 de 55 | 2 HORAS | M11 SECOND CONDITIONAL',
    'M11 I\'d Eat a Cookie. (second conditional: if+pasado / would) + Job Interview Hypotheticals | TEMPLANZA v1 dia 4',
    a2_c9_act, a2_c9_deliv, a2_c9_eval, S,
)

print('\nA2 PM Clase 9 generada (GUIA + REPORTE) en A2/V2/.')
