#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF guia + REPORTE para B1 Cl 14 CONV + GRAMMAR.
Cl 14 = PAST TIME EXPRESSIONS + SEQUENCING (AT/ON/IN/LAST/AGO + first/then/after that/finally).
Anclado A2 Book Module 12. JUSTICIA v1 dia 4 de 5. Conv va PRIMERO (PASE Conv->Grammar mismo dia)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONV_DIR = os.path.join(D, 'B1', 'B1_conversacional_V2')
GRAM_DIR = os.path.join(D, 'B1', 'B1_gramatica_V2')

# ============================================================
# 1. PDF GUIA Cl 14 CONV + GRAMMAR (desde PRINT.md)
# ============================================================
md_to_pdf(
    os.path.join(CONV_DIR, 'B1_Clase14_CONV_PRINT.md'),
    os.path.join(CONV_DIR, 'B1_Clase14_CONV_GUIA.pdf'),
)
print('OK: B1_Clase14_CONV_GUIA.pdf')

md_to_pdf(
    os.path.join(GRAM_DIR, 'B1_Clase14_GRAMMAR_PRINT.md'),
    os.path.join(GRAM_DIR, 'B1_Clase14_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase14_GRAMMAR_GUIA.pdf')

# ============================================================
# 2. REPORTE Cl 14 CONV (Danna)
# ============================================================
conv_act = [
    ('OPENER — Frase + JUSTICIA dia 4 + Past Time Anchor roundup (Grammar pase Cl 13)', '10 min'),
    ('CONTENT TIME EXPRESSIONS + SEQUENCING (AGO/LAST/IN/ON/AT + position + first/then/after that)', '50 min'),
    ('LIVE: WEEKLY RECAP MEETING (pares team lead + reporter, 3 rotaciones + demo)', '45 min'),
    ('CIERRE — Error paper + frase + virtud dia 4 + tarea + PASE a Grammar + Cl 15 anuncio', '15 min'),
]
conv_deliv = [
    'Foto del board final con 5 errores tipicos + Frase del Dia',
    'Foto/video del Weekly Recap Meeting (3 rotaciones + demo)',
    'Libreta personal con 3 errores literales + NOMBRES',
    'PASE "PASE A GRAMMAR — CL 14" entregada (foto antes de entregar)',
    'PASE "PASE A CONV — CL 14" recibida de Grammar (archivada)',
    'Marca en reporte: JUSTICIA v1 dia 4 de 5',
    'Conteo: 3 rotaciones de Weekly Recap completas + UNA demo',
]
conv_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI la frase del dia en board e INSERTE 4 veces',
    'LEI el PASE recibido del Grammar y corri el Past Time Anchor roundup en el opener',
    'Ensene AGO (after period) / LAST (no "the") / IN+year / ON+day / AT+clock',
    'Ensene position (time word al END o front + comma)',
    'Ensene sequencing chain (first/then/after that/before/finally)',
    'Weekly Recap fue simulacion PROFESIONAL realista (no fantasiosa, no familiar)',
    'Corri 3 rotaciones + UNA demo al frente, profe COACHA (no juega rol)',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo (board)',
    'ESCRIBI y ENTREGUE el PASE a Grammar ANTES del cambio de bloque',
    'En Tarea LEI la justificacion pedagogica (30-45 min, NO fragmentada)',
    'NO acepte la excusa "no me da tiempo"',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 15 = past continuous + cierre bloque JUSTICIA',
    'Estudiantes hablaron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(CONV_DIR, 'B1_Clase14_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 14 de 44 | BLOQUE 1: CONVERSACIONAL (HOY VA PRIMERO)',
    'Past Time Expressions + Sequencing (AGO/LAST/IN/ON/AT + first/then/after that) | A2 Module 12 | JUSTICIA v1 dia 4 de 5 | Weekly Recap Meeting + PASE a Grammar',
    conv_act, conv_deliv, conv_eval, S,
)
print('OK: B1_Clase14_CONV_REPORTE.pdf')

# ============================================================
# 3. REPORTE Cl 14 GRAMMAR (Juan Diego)
# ============================================================
gram_act = [
    ('OPENER (DE PIE) — Frase + JUSTICIA dia 4 + Conv pase (mismo dia) + bridge a tabla', '10 min'),
    ('CONTENT TABLE + POSITION + SEQUENCING (DE PIE) — AT/ON/IN/LAST/AGO + transformacion + podium', '50 min'),
    ('LIVE: TIME-ANCHOR SPRINT + SEQUENCING BUILD (DE PIE) — 18 builds, 3 rounds, board grid', '45 min'),
    ('CIERRE — Error paper + frase + virtud dia 4 + tarea + PASE a Conv Cl 15', '15 min'),
]
gram_deliv = [
    'Foto del board con tabla completa (AT/ON/IN/LAST/AGO + position + sequencing) + 5 errores + Frase',
    'Foto/video del podium (sequencing sprint + 3 anchor challenges) + Time-Anchor Sprint grid',
    'Libreta personal con 3 errores literales + NOMBRES',
    'PASE "PASE A CONV — CL 15" entregada (con bridge a past continuous)',
    'PASE "PASE A GRAMMAR — CL 14" recibida de Conv (leida en opener)',
    'Marca en reporte: JUSTICIA v1 dia 4 de 5',
    'Conteo: 3 rounds (PHASE A x10 + PHASE B x8) + UNA demo',
]
gram_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'EJECUTE ~86% del bloque DE PIE (board / podium / sprint / grid)',
    'LEI la frase del dia en board e INSERTE 4 veces',
    'LEI el PASE recibido de Conv en el opener (mismo dia)',
    'Formalice la tabla AT/ON/IN/LAST/AGO con anclaje al A2 Module 12',
    'Ensene position (END o front + comma) y la regla AGO after / LAST no "the" / no "in"',
    'Ensene sequencing chain (first/then/after that/before/finally)',
    'Corri 10 anchor drills + podium sequencing + Time-Anchor Sprint (18 builds, 3 rounds)',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo (board)',
    'ESCRIBI y ENTREGUE el PASE a Conv Cl 15 (bridge a past continuous) ANTES de salir',
    'En Tarea LEI la justificacion pedagogica (30-45 min, NO fragmentada)',
    'NO acepte la excusa "no me da tiempo"',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Anuncie Cl 15 = past continuous + cierre JUSTICIA + Cl 16 abre FORTALEZA',
]
build_report_v2(
    os.path.join(GRAM_DIR, 'B1_Clase14_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 14 de 44 | BLOQUE 2: GRAMMAR & WRITING',
    'Past Time Expressions + Sequencing (AT/ON/IN/LAST/AGO + position + first/then/after that) | A2 Module 12 | JUSTICIA v1 dia 4 de 5 | ~86% DE PIE | PASE a Conv Cl 15',
    gram_act, gram_deliv, gram_eval, S,
)
print('OK: B1_Clase14_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados (Cl 14 CONV + GRAMMAR, guia + reporte).')
