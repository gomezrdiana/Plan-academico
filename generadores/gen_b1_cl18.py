#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery Cl 18 — NARRATIVE INTEGRATION (FORTALEZA v1 dia 3 de 5).
Genera 4 PDFs: CONV GUIA + REPORTE (track conversacional) y GRAMMAR GUIA +
REPORTE (track gramatica). Reportes en la MISMA carpeta del track (como Cl 13).
Conv va PRIMERO (PASE bidireccional). Topico compartido Conv/Grammar."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONV_DIR = os.path.join(D, 'B1', 'B1_conversacional_V2')
GRAM_DIR = os.path.join(D, 'B1', 'B1_gramatica_V2')

# ============================================================
# 1. CONV — GUIA PDF
# ============================================================
md_to_pdf(
    os.path.join(CONV_DIR, 'CONVERSACION', 'B1_Clase18_CONV_PRINT.md'),
    os.path.join(CONV_DIR, 'B1_Clase18_CONV_GUIA.pdf'),
)
print('OK: B1_Clase18_CONV_GUIA.pdf')

# ============================================================
# 2. CONV — REPORTE editable (para Danna)
# ============================================================
conv_act = [
    ('OPENER — Frase + FORTALEZA dia 3 + "My past story" roundup (PASE Grammar Cl 17)', '10 min'),
    ('CONTENT NARRATIVE INTEGRATION — form per clause + sequencing + build a story aloud', '50 min'),
    ('LIVE: JOB-INTERVIEW STORYTELLING — A CHALLENGE I OVERCAME (3 rotaciones + demo, DE PIE)', '45 min'),
    ('CIERRE — Error paper + frase close + virtud + tarea + PASE a Grammar + Cl 19', '15 min'),
]
conv_deliv = [
    'Reporte impreso lleno',
    'Foto del board final (5 errores tipicos + Frase del Dia)',
    'Foto/video del Job-Interview Storytelling (3 rotaciones + demo al frente)',
    'PASE "A CONV — CL 18" recibido de Grammar (archivado)',
    'PASE "A GRAMMAR — CL 18" entregado (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Conteo de cuantos estudiantes encadenaron scene->turning->resolution sin saltar al presente',
]
conv_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / teaching / interview / cierre)',
    'LEI la hoja PASE "A CONV — CL 18" de Grammar en el opener',
    'Conduje el "My past story" roundup (used to/was -ing + when + simple + then)',
    'Ensené a ELEGIR la forma por clausula (background=was -ing, event=simple, habit=used to)',
    'Ancle el frame was -ing ... when + simple a Module 12 del A2 Book',
    'Modele UNA historia completa en voz alta apuntando a las capas del board',
    'Simulacion fue PROFESIONAL/realista (entrevista, reto laboral) — NO fantasiosa',
    'La simulacion produjo historias de 6-8 lineas en pasado (3 rotaciones + demo)',
    'COACHE desde el lado — NO jugue rol de interviewer ni candidate',
    'Corregi saltos al presente con "Fortitude — stay in the past"',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE el PASE "A GRAMMAR — CL 18" antes de cambiar de bloque',
    'En Tarea exigi 30-45 min, 3 componentes, NO fragmentada, due antes de proxima clase 7:00 AM',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 19 = PAST PERFECT (had + past participle)',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Estudiantes hablaron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(CONV_DIR, 'B1_Clase18_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 18 de 44 | BLOQUE 1: CONVERSACIONAL (HOY VA PRIMERO)',
    'NARRATIVE INTEGRATION — contar una historia pasada completa (past simple + continuous + when/while + used to + sequencing) | FORTALEZA v1 dia 3 de 5 | Job-Interview Storytelling + PASE a Grammar',
    conv_act, conv_deliv, conv_eval, S,
)
print('OK: B1_Clase18_CONV_REPORTE.pdf')

# ============================================================
# 3. GRAMMAR — GUIA PDF
# ============================================================
md_to_pdf(
    os.path.join(GRAM_DIR, 'GRAMATICA', 'B1_Clase18_GRAMMAR_PRINT.md'),
    os.path.join(GRAM_DIR, 'B1_Clase18_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase18_GRAMMAR_GUIA.pdf')

# ============================================================
# 4. GRAMMAR — REPORTE editable (para Juan Diego)
# ============================================================
gram_act = [
    ('OPENER (STAND) — Frase + FORTALEZA dia 3 + 3 gaps (PASE Conv mismo dia) + bridge', '10 min'),
    ('CONTENT INTEGRATED MAP + CONNECTORS (STAND ~90%) — form-per-clause + transform + podium', '50 min'),
    ('LIVE: STORY-BUILD SPRINT (STAND 100%) — historia colaborativa, 18+ clausulas, 3 rounds', '45 min'),
    ('CIERRE (SEATED) — Error paper + frase close + virtud + tarea + PASE a Conv Cl 19', '15 min'),
]
gram_deliv = [
    'Reporte impreso lleno',
    'Foto del board final (5 errores + mapa integrado form-per-clause + Frase del Dia)',
    'Foto/video del Story-Build Sprint (historia completa 18+ clausulas) + podium "fix the clause"',
    'PASE "A GRAMMAR — CL 18" recibido de Conv (archivado)',
    'COPIA del PASE "A CONV — CL 19" entregado a Danna (con hora)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Nota: % de clase ejecutada DE PIE (objetivo ~86%)',
]
gram_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / map close / mid-round / cierre)',
    'LEI la hoja PASE "A GRAMMAR — CL 18" de Conv en el opener',
    'ESCRIBI el mapa integrado: una forma por clausula (used to+base / was -ing / when+simple)',
    'Ancle el frame was -ing ... when + simple a Module 12 del A2 Book',
    'Marque que used to/would va MAS ALLA del Module 12 (gramatica estandar)',
    'Conduje 8 transform-the-clause builds DE PIE en el board',
    'Conduje el podium "fix the clause" (8 clausulas rotas corregidas)',
    'Conduje el Story-Build Sprint: 18+ clausulas encadenadas, 3 rounds, lectura coral final',
    'Ejecutè ~86% de la clase DE PIE (Blocks 1-3 en/junto al board)',
    'Corregi "used to worked", "was call", saltos al presente con "Fortitude"',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE el PASE "A CONV — CL 19" (bridge a PAST PERFECT) a Danna',
    'En Tarea exigi 30-45 min, 3 componentes, NO fragmentada, due antes de proxima clase 7:00 AM',
    'NO acepte la excusa "esto ya lo sabia" ni "no me dio tiempo"',
    'Anuncie Cl 19 = PAST PERFECT (had + past participle)',
    'NO comunique notas/midterm/final (coordinacion maneja)',
]
build_report_v2(
    os.path.join(GRAM_DIR, 'B1_Clase18_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 18 de 44 | BLOQUE 2: GRAMMAR & WRITING (~86% DE PIE)',
    'NARRATIVE INTEGRATION — formalizar la maquina pasada integrada (form-per-clause + sequencing, una sola linea de tiempo) | FORTALEZA v1 dia 3 de 5 | Story-Build Sprint + PASE a Conv Cl 19',
    gram_act, gram_deliv, gram_eval, S,
)
print('OK: B1_Clase18_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados (Cl 18):')
print('  - B1/B1_conversacional_V2/B1_Clase18_CONV_GUIA.pdf')
print('  - B1/B1_conversacional_V2/B1_Clase18_CONV_REPORTE.pdf')
print('  - B1/B1_gramatica_V2/B1_Clase18_GRAMMAR_GUIA.pdf')
print('  - B1/B1_gramatica_V2/B1_Clase18_GRAMMAR_REPORTE.pdf')
