#!/usr/bin/env python3
"""B1 Mastery Cl 20 — PAST SYSTEM MASTERY (FORTALEZA v1 dia 5 de 5 — CIERRA bloque).
Genera 4 PDFs: CONV GUIA + REPORTE (track conversacional) y GRAMMAR GUIA +
REPORTE (track gramatica). Reportes en la MISMA carpeta del track (como Cl 18-19).
Conv va PRIMERO (PASE bidireccional). Topico compartido Conv/Grammar.
Consolidacion de las 5 formas del pasado antes del midterm (Cl 22)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
CONV_DIR = os.path.join(D, 'B1', 'B1_conversacional_V2')
GRAM_DIR = os.path.join(D, 'B1', 'B1_gramatica_V2')

# ============================================================
# 1. CONV — GUIA PDF
# ============================================================
md_to_pdf(
    os.path.join(CONV_DIR, 'B1_Clase20_CONV_PRINT.md'),
    os.path.join(CONV_DIR, 'B1_Clase20_CONV_GUIA.pdf'),
)
print('OK: B1_Clase20_CONV_GUIA.pdf')

# ============================================================
# 2. CONV — REPORTE editable (para Danna)
# ============================================================
conv_act = [
    ('OPENER — Frase + FORTALEZA dia 5 (cierra) + "Whole-Story" roundup (PASE Grammar Cl 19)', '10 min'),
    ('CONTENT FIVE-FORM MASTERY — la cadena de las 5 formas + build one full story aloud + self-check card', '50 min'),
    ('LIVE: FULL-STORY SHOWCASE — "MY HARDEST CHALLENGE, START TO FINISH" (3 rotaciones + demos al frente)', '45 min'),
    ('CIERRE — Error paper + frase close + virtud dia 5 CIERRA FORTALEZA + tarea + PASE a Grammar + Cl 21', '15 min'),
]
conv_deliv = [
    'Reporte impreso lleno',
    'Foto del board final (5 errores tipicos + cadena de 5 formas + Frase del Dia)',
    'Foto/video del Full-Story Showcase (3 rotaciones + demos al frente)',
    'PASE "A CONV — CL 20" recibido de Grammar (archivado)',
    'PASE "A GRAMMAR — CL 20" entregado (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Conteo de cuantos estudiantes encadenaron las 5 formas en una historia sin saltar al presente',
]
conv_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / five-form chain / showcase / cierre)',
    'LEI la hoja PASE "A CONV — CL 20" de Grammar en el opener',
    'Conduje el "Whole-Story" roundup (historia con las 5 formas: used to / was -ing / when + simple / had + participle / connector)',
    'ESCRIBI la cadena de las 5 formas y modele UNA historia completa en voz alta tocando cada capa',
    'Ancle las formas al libro: was -ing y when + simple a A2 Book M12; participio a M15/M16',
    'Corri la self-check card (5 preguntas) para que cada pareja detecte la capa faltante',
    'Simulacion fue PROFESIONAL/realista (reto laboral o de estudio) — NO fantasiosa',
    'El showcase produjo historias de 7-8 lineas con las 5 formas verificadas (3 rotaciones + demos)',
    'COACHE desde el lado — NO jugue rol de teller ni scorer',
    'Corregi capas caidas y saltos al presente con "Fortitude — finish the story, hold all five"',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE el PASE "A GRAMMAR — CL 20" antes de cambiar de bloque',
    'En Tarea exigi 30-45 min, 3 componentes, NO fragmentada, due antes de proxima clase 7:00 AM (draft del midterm)',
    'NO acepte la excusa "no me da tiempo"',
    'CERRE el bloque FORTALEZA (dia 5) y anuncie Cl 21 = PRESENT PERFECT + apertura PRUDENCIA v2 + midterm prep',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Estudiantes hablaron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(CONV_DIR, 'B1_Clase20_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 20 de 44 | BLOQUE 1: CONVERSACIONAL (HOY VA PRIMERO)',
    'PAST SYSTEM MASTERY — la maquina pasada completa en una narracion (used to / was -ing / when + simple / had + participle / connectors) | FORTALEZA v1 dia 5 de 5 CIERRA | Full-Story Showcase + PASE a Grammar',
    conv_act, conv_deliv, conv_eval, S,
)
print('OK: B1_Clase20_CONV_REPORTE.pdf')

# ============================================================
# 3. GRAMMAR — GUIA PDF
# ============================================================
md_to_pdf(
    os.path.join(GRAM_DIR, 'B1_Clase20_GRAMMAR_PRINT.md'),
    os.path.join(GRAM_DIR, 'B1_Clase20_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase20_GRAMMAR_GUIA.pdf')

# ============================================================
# 4. GRAMMAR — REPORTE editable (para Juan Diego)
# ============================================================
gram_act = [
    ('OPENER (STAND) — Frase + FORTALEZA dia 5 (cierra) + 3 gaps (PASE Conv mismo dia) + bridge a maestria', '10 min'),
    ('CONTENT FIVE-FORM MACHINE ON PAPER (STAND ~90%) — cadena de 5 formas + labeling drill + fix-the-leak + podium "name the form"', '50 min'),
    ('LIVE: MASTERY RELAY (STAND 100%) — historia colaborativa, cada clausula etiquetada 1-5, 20+ clausulas, 3 rounds', '45 min'),
    ('CIERRE (SEATED) — Error paper + frase close + virtud dia 5 CIERRA FORTALEZA + tarea + PASE a Conv Cl 21', '15 min'),
]
gram_deliv = [
    'Reporte impreso lleno',
    'Foto del board final (5 errores + cadena de 5 formas + Frase del Dia)',
    'Foto/video del Mastery Relay (20+ clausulas etiquetadas 1-5) + podium "name the form"',
    'PASE "A GRAMMAR — CL 20" recibido de Conv (archivado)',
    'COPIA del PASE "A CONV — CL 21" entregado a Danna (con hora)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Nota: % de clase ejecutada DE PIE (objetivo ~86%)',
]
gram_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'ESCRIBI la Frase del Dia en el board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / five-form chain / mid-relay / cierre)',
    'LEI la hoja PASE "A GRAMMAR — CL 20" de Conv en el opener',
    'ESCRIBI la cadena completa de las 5 formas + la self-check card (misma que Conv uso)',
    'Ancle las formas al libro: was -ing y when + simple a A2 Book M12; participio a M15/M16',
    'Marque que used to/would y past perfect van MAS ALLA del A2 Book (extension B1 estandar)',
    'Conduje el labeling drill (etiquetar cada clausula 1-5 + arreglar los 3 errores plantados)',
    'Conduje el podium "name the form" (8 clausulas, forma 1-5 + fix de present leaks)',
    'Conduje el Mastery Relay: 20+ clausulas etiquetadas, las 5 formas x3+, 3 rounds, lectura coral + form count',
    'Ejecutè ~86% de la clase DE PIE (Blocks 1-3 en/junto al board)',
    'Corregi "used to worked", "was prepare", "had went", y present leaks con "Fortitude"',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE el PASE "A CONV — CL 21" (bridge a PRESENT PERFECT + midterm prep) a Danna',
    'En Tarea exigi 30-45 min, 3 componentes, NO fragmentada, due antes de proxima clase 7:00 AM (draft del midterm)',
    'NO acepte la excusa "esto ya lo sabia" ni "no me dio tiempo"',
    'CERRE el bloque FORTALEZA (dia 5) y anuncie Cl 21 = PRESENT PERFECT + apertura PRUDENCIA v2 + midterm prep',
    'NO comunique notas/midterm/final (coordinacion maneja)',
]
build_report_v2(
    os.path.join(GRAM_DIR, 'B1_Clase20_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 20 de 44 | BLOQUE 2: GRAMMAR & WRITING (~86% DE PIE)',
    'PAST SYSTEM MASTERY — lockear la maquina pasada integrada en papel (5 formas, una narracion, cero present leaks) | FORTALEZA v1 dia 5 de 5 CIERRA | Mastery Relay + PASE a Conv Cl 21',
    gram_act, gram_deliv, gram_eval, S,
)
print('OK: B1_Clase20_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados (Cl 20):')
print('  - B1/B1_conversacional_V2/B1_Clase20_CONV_GUIA.pdf')
print('  - B1/B1_conversacional_V2/B1_Clase20_CONV_REPORTE.pdf')
print('  - B1/B1_gramatica_V2/B1_Clase20_GRAMMAR_GUIA.pdf')
print('  - B1/B1_gramatica_V2/B1_Clase20_GRAMMAR_REPORTE.pdf')
