#!/usr/bin/env python3
"""Genera B1 Cl 16 CONV + GRAMMAR: GUIA PDFs + REPORTE PDFs (en la misma carpeta de cada track).
Topico: PAST SIMPLE vs PAST CONTINUOUS (WHEN/WHILE interruption, A2 Book Module 12).
Virtud: FORTALEZA v1 dia 1 de 5 (ABRE bloque; Justicia cerro Cl 15). Conv va PRIMERO."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
CONV_DIR = os.path.join(D, 'B1', 'B1_conversacional_V2')
GRAM_DIR = os.path.join(D, 'B1', 'B1_gramatica_V2')

# ============================================================
# 1. GUIA PDFs
# ============================================================
md_to_pdf(os.path.join(CONV_DIR, 'B1_Clase16_CONV_PRINT.md'),
          os.path.join(CONV_DIR, 'B1_Clase16_CONV_GUIA.pdf'))
print('OK: B1_Clase16_CONV_GUIA.pdf')

md_to_pdf(os.path.join(GRAM_DIR, 'B1_Clase16_GRAMMAR_PRINT.md'),
          os.path.join(GRAM_DIR, 'B1_Clase16_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase16_GRAMMAR_GUIA.pdf')

# ============================================================
# 2. REPORTE CONV (en la carpeta del track)
# ============================================================
conv_act = [
    ('OPENER — Frase + FORTALEZA dia 1 + "When the call came" roundup (PASE Grammar Cl 15) + bridge WHEN/WHILE', '~10 min'),
    ('CONTENT WHEN/WHILE — long continuous vs short simple + WHEN+simple / WHILE+continuous + dos acciones largas', '~50 min'),
    ('LIVE: BEHAVIORAL INTERVIEW "Tell me about a time" — interrupcion + push through, 3 rotaciones + demo', '~45 min'),
    ('CIERRE — Error paper + frase close + VATS Fortaleza + tarea + PASE a Grammar + Cl 17 anuncio', '~15 min'),
]
conv_deliv = [
    'Reporte impreso lleno',
    'FOTO del board final con 5 errores tipicos + Frase del Dia',
    'FOTO/video del Behavioral Interview (3 rotaciones + demo)',
    'PASE recibido de Grammar (Cl 15) archivado',
    'COPIA del PASE a Grammar Cl 16 entregado (foto antes de entregar)',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Conteo de cuantos mantienen continuous en la accion larga vs cuantos la dejan en simple',
]
conv_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en board ANTES de empezar',
    'LEI la PASE recibida de Grammar Cl 15 en el opener',
    'Abri con el "When the call came" roundup (1 frase por persona)',
    'Active FORTALEZA dia 1 (ABRE bloque; Justicia cerro Cl 15)',
    'Enseñe long action = PAST CONTINUOUS / short interruption = PAST SIMPLE',
    'Enseñe WHEN + simple / WHILE + continuous + dos acciones largas',
    'Ancle el contenido a A2 Book Module 12 (no invente reglas)',
    'Inserte la Frase del Dia 4 veces',
    'Behavioral Interview fue PROFESIONAL/realista (interrupcion + push through)',
    'COACHE desde el lado — NO jugue rol de interviewer ni candidate',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI el PASE a Grammar con 3 gaps orales + patrones',
    'ENTREGUE FISICAMENTE el PASE a Grammar antes del cambio de bloque',
    'En Tarea NO acepte la excusa "no me da tiempo" (30-45 min, no fragmentada)',
    'Anuncie Cl 17 = USED TO / WOULD',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Estudiantes hablaron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(CONV_DIR, 'B1_Clase16_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 16 de 44 | BLOQUE 1: CONVERSACIONAL (HOY VA PRIMERO)',
    'Past Simple vs Past Continuous (WHEN/WHILE interruption, A2 Module 12) + Behavioral Interview + FORTALEZA v1 dia 1 + PASE a Grammar',
    conv_act, conv_deliv, conv_eval, S,
)
print('OK: B1_Clase16_CONV_REPORTE.pdf')

# ============================================================
# 3. REPORTE GRAMMAR (en la carpeta del track)
# ============================================================
gram_act = [
    ('OPENER (Stand) — Frase + FORTALEZA dia 1 + 60-sec mystery (PASE Conv mismo dia) + bridge a tabla', '~10 min'),
    ('CONTENT TABLE WHEN/WHILE (~80% Stand) — long continuous vs short simple + WHEN/WHILE + dos largas + question order + podium', '~50 min'),
    ('LIVE: WHEN/WHILE INTERRUPTION SPRINT (100% de pie) — 18 builds, 3 rounds, board grid', '~45 min'),
    ('CIERRE (Stand) — Error paper + frase close + virtud dia 1 + tarea + PASE a Conv Cl 17', '~15 min'),
]
gram_deliv = [
    'Reporte impreso lleno',
    'FOTO del board final con 5 errores + tabla completa + Frase del Dia',
    'FOTO/video del podium (8 WHEN/WHILE kits + 2 two-long-actions) + Sprint grid',
    'PASE recibido de Conv (mismo dia) archivado',
    'COPIA del PASE a Conv Cl 17 entregado (con hora)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Nota: % del bloque corrido DE PIE (target ~86%, piso 70%)',
]
gram_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en board ANTES de empezar',
    'RECIBI y LEI la PASE de Conv (mismo dia) en el opener',
    'Active FORTALEZA dia 1 (ABRE bloque; Justicia cerro Cl 15)',
    'ESCRIBI la tabla completa (long continuous vs short simple) en board',
    'Enseñe WHEN + simple / WHILE + continuous + dos acciones largas + question order',
    'Ancle el contenido a A2 Book Module 12 (no invente reglas)',
    'Corri el podium (8 WHEN/WHILE kits + 2 two-long-actions)',
    'Corri el When/While Interruption Sprint (18 builds, 3 rounds)',
    'Mantuve el bloque ~86% DE PIE (piso 70%)',
    'Inserte la Frase del Dia 4 veces',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI el PASE a Conv Cl 17 (bridge a USED TO / WOULD)',
    'ENTREGUE FISICAMENTE el PASE a Conv antes de salir',
    'En Tarea NO acepte la excusa "no me dio tiempo" (30-45 min, no fragmentada)',
    'Anuncie Cl 17 = USED TO / WOULD',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Estudiantes produjeron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(GRAM_DIR, 'B1_Clase16_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 16 de 44 | BLOQUE 2: GRAMMAR & WRITING (~86% DE PIE)',
    'Past Simple vs Past Continuous (WHEN/WHILE interruption, A2 Module 12) + When/While Sprint + FORTALEZA v1 dia 1 + PASE a Conv Cl 17',
    gram_act, gram_deliv, gram_eval, S,
)
print('OK: B1_Clase16_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados (Cl 16 CONV + GRAMMAR, GUIA + REPORTE).')
