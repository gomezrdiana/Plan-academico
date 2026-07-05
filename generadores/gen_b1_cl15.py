#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery Cl 15 — Past Continuous (was/were + -ing, A2 Module 12). JUSTICIA v1 dia 5 (CIERRA).
Genera GUIA + REPORTE para CONV (Danna) y GRAMMAR (Juan Diego). REPORTE va en la misma carpeta del track."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONV_DIR = os.path.join(D, 'B1', 'B1_conversacional_V2')
GRAM_DIR = os.path.join(D, 'B1', 'B1_gramatica_V2')

# ============================================================
# 1. GUIA PDFs
# ============================================================
md_to_pdf(os.path.join(CONV_DIR, 'B1_Clase15_CONV_PRINT.md'),
          os.path.join(CONV_DIR, 'B1_Clase15_CONV_GUIA.pdf'))
print('OK: B1_Clase15_CONV_GUIA.pdf')
md_to_pdf(os.path.join(GRAM_DIR, 'B1_Clase15_GRAMMAR_PRINT.md'),
          os.path.join(GRAM_DIR, 'B1_Clase15_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase15_GRAMMAR_GUIA.pdf')

# ============================================================
# 2. REPORTE CONV (Danna)
# ============================================================
conv_act = [
    ('OPENER — Frase + JUSTICIA dia 5 (CIERRA) + PASE Grammar Cl 14 (Ongoing Past roundup) + bridge', '10 min'),
    ('CONTENT PAST CONTINUOUS — WAS vs WERE + -ing + negatives/questions/short answers + contraste con past simple', '50 min'),
    ('LIVE: INCIDENT TIMELINE — What were you doing? (3 rotaciones + demo, DE PIE)', '45 min'),
    ('CIERRE — Error paper + frase close + virtud cierra Justicia + tarea + PASE a Grammar + Cl 16 (Fortaleza)', '15 min'),
]
conv_deliv = [
    'Reporte impreso lleno',
    'FOTO del board final con 5 errores tipicos + Frase del Dia',
    'FOTO/video del Incident Timeline (3 rotaciones + demo)',
    'PASE de Grammar Cl 14 recibida y leida en opener (archivada)',
    'PASE a Grammar Teacher Cl 15 entregada antes del cambio de bloque (foto antes de entregar)',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Conteo: cuantos mantienen was/were + -ing vs cuantos necesitan refuerzo',
]
conv_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en board ANTES de empezar',
    'LEI la PASE de Grammar Cl 14 en el opener (Ongoing Past roundup)',
    'Active JUSTICIA dia 5 y anuncie que CIERRA el bloque',
    'Anuncie que Cl 16 abre FORTALEZA',
    'Enseñe WAS (I/he/she/it) vs WERE (you/we/they) + -ing',
    'Enseñe negatives wasn\'t/weren\'t + questions Was/Were + short answers',
    'Contraste past simple (dot) vs past continuous (line)',
    'Use frases modelo del A2 Book Module 12',
    'Simulacion Incident Timeline fue PROFESIONAL/realista (no fantasiosa)',
    'Inserte la Frase del Dia 4 veces (opener / teaching / timeline / cierre)',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE FISICAMENTE la PASE a Grammar antes del cambio de bloque',
    'En Tarea NO acepte "no me da tiempo" (30-45 min, no fragmentada)',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Estudiantes hablaron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(CONV_DIR, 'B1_Clase15_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 15 de 44 | BLOQUE 1: CONVERSACIONAL (HOY VA PRIMERO)',
    'Past Continuous (was/were + -ing, A2 Module 12) + Incident Timeline + JUSTICIA dia 5 CIERRA + PASE a Grammar',
    conv_act, conv_deliv, conv_eval, S,
)
print('OK: B1_Clase15_CONV_REPORTE.pdf')

# ============================================================
# 3. REPORTE GRAMMAR (Juan Diego)
# ============================================================
gram_act = [
    ('OPENER — Frase + JUSTICIA dia 5 (CIERRA) + 60-sec mystery (PASE Conv mismo dia) + bridge a tabla (DE PIE)', '10 min'),
    ('CONTENT TABLE WAS/WERE + -ing + negatives/questions/short answers + contraste + transformacion + podium (~80% DE PIE)', '50 min'),
    ('LIVE: WAS/WERE + -ING SPRINT — 18 builds, 3 rounds, board grid (100% DE PIE)', '45 min'),
    ('CIERRE — Error paper + frase close + virtud cierra Justicia + tarea + PASE a Conv Cl 16 (DE PIE)', '15 min'),
]
gram_deliv = [
    'Reporte impreso lleno',
    'FOTO del board final con 5 errores + tabla completa + Frase del Dia',
    'FOTO/video del podium (8 kits + 2 challenges) + Was/Were Sprint grid (3 rounds + demo)',
    'PASE de Conv recibida y leida en opener (archivada)',
    'PASE a Conv Teacher Cl 16 entregada (con hora de entrega)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Confirmacion: ~86% del bloque DE PIE (piso 70%)',
]
gram_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en board ANTES de empezar',
    'LEI la PASE de Conv en el opener (3 gaps orales mismo dia)',
    'Active JUSTICIA dia 5 y anuncie que CIERRA el bloque',
    'Anuncie que Cl 16 abre FORTALEZA',
    'Escribi la tabla completa was/were + -ing en board',
    'Enseñe agreement WAS (I/he/she/it) vs WERE (you/we/they)',
    'Enseñe negatives wasn\'t/weren\'t + questions Was/Were + short answers',
    'Contraste past simple (dot) vs past continuous (line)',
    'Use frases modelo del A2 Book Module 12',
    'Conduje 10 transformation drills + podium con 8 kits + 2 challenges',
    'Conduje Was/Were Sprint (PHASE A x10 + PHASE B x8 + 2 negatives, 3 rounds)',
    'Ejecute ~86% del bloque DE PIE (piso 70%)',
    'Inserte la Frase del Dia 4 veces (opener / table / mid-round / cierre)',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'ESCRIBI y ENTREGUE FISICAMENTE la PASE a Conv Cl 16 (bridge a when/while interrupcion)',
    'En Tarea NO acepte "no me da tiempo" (30-45 min, no fragmentada)',
    'NO comunique notas/midterm/final (coordinacion maneja)',
]
build_report_v2(
    os.path.join(GRAM_DIR, 'B1_Clase15_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 15 de 44 | BLOQUE 2: GRAMMAR & WRITING',
    'Past Continuous table (was/were + -ing, A2 Module 12) + Was/Were Sprint + JUSTICIA dia 5 CIERRA + ~86% DE PIE + PASE a Conv Cl 16',
    gram_act, gram_deliv, gram_eval, S,
)
print('OK: B1_Clase15_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados (Cl 15 CONV + GRAMMAR, GUIA + REPORTE).')
