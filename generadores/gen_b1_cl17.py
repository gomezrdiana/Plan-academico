#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera GUIA PDF + REPORTE PDF para B1 Cl 17 CONV (Danna) + GRAMMAR (Juan Diego).
Topico: USED TO / WOULD para habitos y estados pasados. FORTALEZA v1 dia 2 de 5.
Conv va PRIMERO (PASE bidireccional). Reportes van en la MISMA carpeta del track (como Cl 13)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONV_DIR = os.path.join(D, 'B1', 'B1_conversacional_V2')
GRAM_DIR = os.path.join(D, 'B1', 'B1_gramatica_V2')

# ============================================================
# 1. PDF GUIA Cl 17 CONV
# ============================================================
md_to_pdf(
    os.path.join(CONV_DIR, 'CONVERSACION', 'B1_Clase17_CONV_PRINT.md'),
    os.path.join(CONV_DIR, 'B1_Clase17_CONV_GUIA.pdf'),
)
print('OK: B1_Clase17_CONV_GUIA.pdf')

# ============================================================
# 2. PDF GUIA Cl 17 GRAMMAR
# ============================================================
md_to_pdf(
    os.path.join(GRAM_DIR, 'GRAMATICA', 'B1_Clase17_GRAMMAR_PRINT.md'),
    os.path.join(GRAM_DIR, 'B1_Clase17_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase17_GRAMMAR_GUIA.pdf')

# ============================================================
# 3. REPORTE Cl 17 CONV (los 4 bloques de la guia)
# ============================================================
c17_conv_act = [
    ('BLOCK 1 OPENER (Frase + FORTALEZA dia 2 + "How it used to be" roundup / PASE Grammar Cl 16 + bridge USED TO/WOULD)', '~10 min'),
    ('BLOCK 2 CONTENT USED TO / WOULD (tabla + didn\'t USE to + Did you USE to + WOULD acciones + used to vs past simple + 5 errores)', '~50 min'),
    ('BLOCK 3 LIVE: ONBOARDING / COMPANY-CHANGE CHAT (senior/new hire, 6+ used-to/would, 3 rotaciones + demo)', '~45 min'),
    ('BLOCK 4 CIERRE (error paper + frase close + virtud dia 2 + tarea + PASE a Grammar + Cl 18 anuncio)', '~15 min'),
]
c17_conv_deliv = [
    'Reporte impreso lleno',
    'FOTO del board final con 5 errores tipicos + Frase del Dia',
    'FOTO/video del Onboarding Chat (3 rotaciones + demo)',
    'PASE recibido de Grammar Cl 16 ("PASE A CONV — CL 17") leido en opener',
    'PASE escrito entregado a Grammar ("PASE A GRAMMAR — CL 17") antes del cambio de bloque (foto)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Conteo: cuantos usaron USED TO + bare clean vs cuantos necesitan refuerzo',
]
c17_conv_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada bloque ANTES de empezarlo',
    'ESCRIBI la Frase del Dia en board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / USED TO teaching / onboarding / cierre paraphrase)',
    'ACTIVE FORTALEZA v1 dia 2 en 3 momentos (opener / practica / cierre)',
    'LEI el PASE de Grammar Cl 16 en el opener ("How it used to be" roundup)',
    'Enseñe USED TO + BARE verb para habitos Y estados',
    'Enseñe didn\'t USE to / Did you USE to (bare USE, conexion BARE-after-DID de Cl 13)',
    'Enseñe WOULD + bare para acciones repetidas, NO para estados',
    'Contraste used to (repetido/extendido) vs past simple (un evento)',
    'Onboarding Chat fue PROFESIONAL/realista (no fantasiosa)',
    'COACHEE desde el lado — NO jugue rol de senior ni new hire',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE FISICAMENTE el PASE a Grammar antes del cambio de bloque',
    'En Tarea LEI la justificacion pedagogica y NO acepte "no me da tiempo"',
    'Anuncie Cl 18 = integracion narrativa',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'Estudiantes hablaron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(CONV_DIR, 'B1_Clase17_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 17 de 44 | BLOQUE 1: CONVERSACIONAL (HOY VA PRIMERO)',
    'USED TO / WOULD para habitos y estados pasados + Onboarding Chat + PASE a Grammar | FORTALEZA v1 dia 2 de 5',
    c17_conv_act, c17_conv_deliv, c17_conv_eval, S,
)
print('OK: B1_Clase17_CONV_REPORTE.pdf')

# ============================================================
# 4. REPORTE Cl 17 GRAMMAR (los 4 bloques de la guia)
# ============================================================
c17_gram_act = [
    ('BLOCK 1 OPENER de pie (Frase + FORTALEZA dia 2 + gaps PASE Conv mismo dia + bridge tabla)', '~10 min'),
    ('BLOCK 2 CONTENT TABLE + WOULD + vs PAST SIMPLE (USED TO + bare / didn\'t USE to / Did you USE to / WOULD acciones / contrast + podium 8 kits + 2 traps)', '~50 min'),
    ('BLOCK 3 LIVE: USED TO / WOULD SPRINT de pie (18 builds, 3 rounds, board grid)', '~45 min'),
    ('BLOCK 4 CIERRE (error paper + frase close + virtud dia 2 + tarea + PASE a Conv Cl 18)', '~15 min'),
]
c17_gram_deliv = [
    'Reporte impreso lleno',
    'FOTO del board final con tabla completa (3 moves + WOULD + contrast) + 5 errores + Frase del Dia',
    'FOTO/video del podium (8 kits + 2 traps) + Used To/Would Sprint grid (3 rounds + demo)',
    'PASE recibido de Conv ("PASE A GRAMMAR — CL 17") leido en opener',
    'PASE escrito entregado a Conv ("PASE A CONV — CL 18") antes de salir (foto)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Nota de % del bloque DE PIE (objetivo ~86%, piso 70%)',
]
c17_gram_eval = [
    'HABLE 100% EN INGLES durante todo el bloque',
    'Mantuve ~86% del bloque DE PIE (piso 70%) — solo se sientan a escribir tarea',
    'ESCRIBI la Frase del Dia en board ANTES de empezar',
    'INSERTE la Frase del Dia 4 veces (opener / table close / mid-round / cierre paraphrase)',
    'ACTIVE FORTALEZA v1 dia 2 en 3 momentos',
    'LEI los 3 gaps del PASE de Conv en el opener',
    'Formalice la tabla USED TO (afirmativo + negativo + pregunta) de pie',
    'Enseñe didn\'t USE to / Did you USE to (bare USE — conexion Cl 13 BARE-after-DID)',
    'Enseñe WOULD + bare para acciones repetidas, NO estados',
    'Contraste used to vs past simple (repetido/extendido vs un evento finalizado)',
    'Conduje podium (8 kits + 2 traps) + Used To/Would Sprint (18 builds, 3 rounds) de pie',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI y ENTREGUE FISICAMENTE el PASE a Conv (Cl 18) antes de salir',
    'Anuncie Cl 18 = integracion narrativa (past simple + past continuous + used to + time expr.)',
    'En Tarea NO acepte "no me dio tiempo"',
    'NO comunique notas/midterm/final (coordinacion maneja)',
    'NOTA INTERNA: used to/would NO esta en A2 Book Module 12 — gramatica estandar sin cita de libro',
]
build_report_v2(
    os.path.join(GRAM_DIR, 'B1_Clase17_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 17 de 44 | BLOQUE 2: GRAMMAR & WRITING (~86% DE PIE)',
    'USED TO / WOULD para habitos y estados pasados + Sprint de pie + PASE a Conv Cl 18 | FORTALEZA v1 dia 2 de 5',
    c17_gram_act, c17_gram_deliv, c17_gram_eval, S,
)
print('OK: B1_Clase17_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados (Cl 17):')
print('  - B1/B1_conversacional_V2/B1_Clase17_CONV_GUIA.pdf')
print('  - B1/B1_conversacional_V2/B1_Clase17_CONV_REPORTE.pdf')
print('  - B1/B1_gramatica_V2/B1_Clase17_GRAMMAR_GUIA.pdf')
print('  - B1/B1_gramatica_V2/B1_Clase17_GRAMMAR_REPORTE.pdf')
