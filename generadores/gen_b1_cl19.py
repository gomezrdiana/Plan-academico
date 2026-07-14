#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery Cl 19 — PAST PERFECT (had + past participle) (FORTALEZA v1 dia 4 de 5).
Genera 4 PDFs: CONV GUIA + REPORTE (track conversacional) y GRAMMAR GUIA +
REPORTE (track gramatica). Reportes en la MISMA carpeta del track (como Cl 18).
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
    os.path.join(CONV_DIR, 'CONVERSACION', 'B1_Clase19_CONV_PRINT.md'),
    os.path.join(CONV_DIR, 'B1_Clase19_CONV_GUIA.pdf'),
)
print('OK: B1_Clase19_CONV_GUIA.pdf')

# ============================================================
# 2. CONV — REPORTE editable (para Danna)
# ============================================================
conv_act = [
    ('OPENER — Frase + FORTALEZA dia 4 + "Before that..." roundup (PASE Grammar Cl 18)', '10 min'),
    ('CONTENT PAST PERFECT — had + participle = the earlier event + 3 signal frames + past simple vs past perfect contrast', '50 min'),
    ('LIVE: BACKSTORY INTERVIEW — "WHAT HAD YOU ALREADY DONE?" (3 rotaciones + demo, DE PIE)', '45 min'),
    ('CIERRE — Error paper + frase close + virtud + tarea + PASE a Grammar + Cl 20', '15 min'),
]
conv_deliv = [
    'Reporte impreso lleno',
    'Foto del board final (5 errores tipicos + Frase del Dia)',
    'Foto/video del Backstory Interview (3 rotaciones + demo al frente)',
    'PASE "A CONV — CL 19" recibido de Grammar (archivado)',
    'PASE "A GRAMMAR — CL 19" entregado (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Conteo de cuantos estudiantes colocaron el evento anterior en HAD + participle con el orden correcto',
]
conv_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / past-perfect teaching / backstory interview / cierre)',
    'LEI la hoja PASE "A CONV — CL 19" de Grammar en el opener',
    'Conduje el "Before that..." roundup (2 eventos pasados + un evento anterior con "had already / before")',
    'Ensené HAD + participle = el evento ANTERIOR; el evento principal se queda en past simple',
    'Ancle el PARTICIPIO a A2 Book M15 (regulares) y M16 (irregulares)',
    'Ensené los 3 signal frames (by the time / because / before) y el contraste past simple vs past perfect',
    'Modele UNA historia completa en voz alta con 2-3 flashbacks (had + participle)',
    'Simulacion fue PROFESIONAL/realista (logro o recuperacion laboral) — NO fantasiosa',
    'La simulacion produjo historias con evento principal + 2 flashbacks (3 rotaciones + demo)',
    'COACHE desde el lado — NO jugue rol de interviewer ni candidate',
    'Corregi "had went / had ate", verbo pelado tras HAD, y eventos aplanados con "Fortitude"',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE el PASE "A GRAMMAR — CL 19" antes de cambiar de bloque',
    'En Tarea exigi 30-45 min, 3 componentes, NO fragmentada, due antes de proxima clase 7:00 AM',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 20 = MAESTRIA DEL SISTEMA PASADO (consolidacion antes del midterm, cierra FORTALEZA)',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Estudiantes hablaron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(CONV_DIR, 'B1_Clase19_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 19 de 44 | BLOQUE 1: CONVERSACIONAL (HOY VA PRIMERO)',
    'PAST PERFECT — colocar un evento pasado ANTES de otro dentro de la historia (had + participle) | FORTALEZA v1 dia 4 de 5 | Backstory Interview + PASE a Grammar',
    conv_act, conv_deliv, conv_eval, S,
)
print('OK: B1_Clase19_CONV_REPORTE.pdf')

# ============================================================
# 3. GRAMMAR — GUIA PDF
# ============================================================
md_to_pdf(
    os.path.join(GRAM_DIR, 'GRAMATICA', 'B1_Clase19_GRAMMAR_PRINT.md'),
    os.path.join(GRAM_DIR, 'B1_Clase19_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase19_GRAMMAR_GUIA.pdf')

# ============================================================
# 4. GRAMMAR — REPORTE editable (para Juan Diego)
# ============================================================
gram_act = [
    ('OPENER (STAND) — Frase + FORTALEZA dia 4 + 3 gaps (PASE Conv mismo dia) + bridge a past perfect', '10 min'),
    ('CONTENT HAD + PARTICIPLE + SIGNAL FRAMES (STAND ~90%) — form map + participle recall + transform + podium "which came first"', '50 min'),
    ('LIVE: TWO-LAYER STORY SPRINT (STAND 100%) — historia colaborativa, 18+ clausulas, 8+ flashbacks, 3 rounds', '45 min'),
    ('CIERRE (SEATED) — Error paper + frase close + virtud + tarea + PASE a Conv Cl 20', '15 min'),
]
gram_deliv = [
    'Reporte impreso lleno',
    'Foto del board final (5 errores + mapa had + participle + Frase del Dia)',
    'Foto/video del Two-Layer Story Sprint (18+ clausulas con flashbacks) + podium "which came first"',
    'PASE "A GRAMMAR — CL 19" recibido de Conv (archivado)',
    'COPIA del PASE "A CONV — CL 20" entregado a Danna (con hora)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Nota: % de clase ejecutada DE PIE (objetivo ~86%)',
]
gram_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / map close / mid-round / cierre)',
    'LEI la hoja PASE "A GRAMMAR — CL 19" de Conv en el opener',
    'ESCRIBI el mapa: HAD + participle (HAD nunca cambia) + los 3 signal frames',
    'Ancle el PARTICIPIO a A2 Book M15 (regulares) y M16 (irregulares)',
    'Marque que el PAST PERFECT (had + participle para el evento anterior) va MAS ALLA del A2 Book (extension B1 estandar)',
    'Conduje 8 transform-the-clause builds DE PIE (evento anterior -> HAD + participle)',
    'Conduje el podium "which came first" (8 pares de eventos, evento anterior en HAD + participle)',
    'Conduje el Two-Layer Story Sprint: 18+ clausulas, 8+ flashbacks encadenados, 3 rounds, lectura coral final',
    'Ejecutè ~86% de la clase DE PIE (Blocks 1-3 en/junto al board)',
    'Corregi "had went", "had start", verbo pelado tras HAD, eventos aplanados con "Fortitude"',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE el PASE "A CONV — CL 20" (bridge a MAESTRIA del sistema pasado) a Danna',
    'En Tarea exigi 30-45 min, 3 componentes, NO fragmentada, due antes de proxima clase 7:00 AM',
    'NO acepte la excusa "esto ya lo sabia" ni "no me dio tiempo"',
    'Anuncie Cl 20 = MAESTRIA DEL SISTEMA PASADO (used to + was -ing + when + simple + past perfect en una narracion)',
    'NO comunique notas/midterm/final (coordinacion maneja)',
]
build_report_v2(
    os.path.join(GRAM_DIR, 'B1_Clase19_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 19 de 44 | BLOQUE 2: GRAMMAR & WRITING (~86% DE PIE)',
    'PAST PERFECT — formalizar had + participle en papel: el evento anterior de dos eventos pasados | FORTALEZA v1 dia 4 de 5 | Two-Layer Story Sprint + PASE a Conv Cl 20',
    gram_act, gram_deliv, gram_eval, S,
)
print('OK: B1_Clase19_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados (Cl 19):')
print('  - B1/B1_conversacional_V2/B1_Clase19_CONV_GUIA.pdf')
print('  - B1/B1_conversacional_V2/B1_Clase19_CONV_REPORTE.pdf')
print('  - B1/B1_gramatica_V2/B1_Clase19_GRAMMAR_GUIA.pdf')
print('  - B1/B1_gramatica_V2/B1_Clase19_GRAMMAR_REPORTE.pdf')
