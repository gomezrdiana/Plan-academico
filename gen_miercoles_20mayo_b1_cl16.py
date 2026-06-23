#!/usr/bin/env python3
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 16 (miercoles 20/05/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Verbos Frasales
  (Hot Topic "When Work Gets Hard" + Simulacion "The Handover Briefing") +
  Page 15 RESILIENCE TURN Draft 1 (escritura en clase) + Frase del Dia +
  FORTALEZA dia 1 v1 (PRIMER del bloque nuevo)
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~86% DE PIE): A2 Book M23 Basic
  Non-Separable Phrasal Verbs (p.221-232) + M24 Separable Phrasal Verbs
  (p.233-240) + Frase del Dia + FORTALEZA dia 1 v1 (PRIMER del bloque nuevo)
- SIN texto Heiiu nuevo (mismo criterio que Cl 14/15: gramatica estructural,
  no narrativa — el mapa de Cl 15 no solicita texto para Cl 16).
- SIN GoldList (eliminado 14/05/2026). Reportes ESTATICOS (se llenan a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
B1_DIR = os.path.join(D, 'B1')
B1_REP = os.path.join(B1_DIR, 'reportes')
os.makedirs(B1_REP, exist_ok=True)

# ============================================================
# B1 Cl 16 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase16_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase16_CONV_GUIA.pdf'),
)
print('OK: B1_Clase16_CONV_GUIA.pdf')

b1_c16_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 15 Conv)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS FORTALEZA dia 1 (v1) - PRIMER del bloque nuevo', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 15 Grammar)', '7 min'),
    ('HOT TOPIC - When Work Gets Hard (verbos frasales en momentos dificiles, oral)', '17 min'),
    ('SIMULACION - The Handover Briefing (DE PIE, profesional)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 15 - RESILIENCE TURN Draft 1 (escritura en clase anti-fraude)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Cierre', '7 min'),
]
b1_c16_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Handover Briefing simulacion',
    'Foto/video Mini-Pitch',
    '16 Paginas 15 RESILIENCE TURN DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 15 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b1_c16_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (verbos frasales)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final (exclusivo coordinacion)',
    'Verifique virtud CL 16 = FORTALEZA dia 1 v1 (PRIMER del bloque nuevo, por numero de clase)',
    'Hile FORTALEZA en VATS como inicio del bloque (no rendirse cuando se acumula el trabajo)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14/15)',
    'RECIBI el PASE escrito de Juan Diego (Cl 15 Grammar) para el Peer Teacher',
    'Conduje Hot Topic When Work Gets Hard con requirements en tablero',
    'Conduje The Handover Briefing (instrucciones profesionales, verbos frasales, DE PIE)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 15 RESILIENCE TURN Draft 1 EN CLASE (anti-fraude IA)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (jueves 21/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 17 jueves',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase16_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 16 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de Verbos Frasales: Hot Topic "When Work Gets Hard" + Simulacion "The Handover Briefing" + Page 15 RESILIENCE TURN Draft 1 anti-fraude + FRASE DEL DIA + PASE a Juan Diego + FORTALEZA dia 1 v1 PRIMER del bloque nuevo (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14/15)',
    b1_c16_c_act, b1_c16_c_deliv, b1_c16_c_eval, S,
)
print('OK: B1_Clase16_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 16 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~86% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase16_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase16_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase16_GRAMMAR_GUIA.pdf')

b1_c16_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS FORTALEZA dia 1 (v1) PRIMER del bloque nuevo - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M23 Non-Separable Phrasal Verbs (p.221-232) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M23 objeto/pronombre al final - DE PIE', '16 min'),
    ('LIBRO M24 Separable Phrasal Verbs (p.233-240) + SORTING fisico separable/no separable - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP + STATION ROTATION - 3 estaciones (M23 / M24 / mixed) - DE PIE', '14 min'),
    ('SPEED DRILL DE PIE - no separable + separable + pronombre en cadena/coro', '12 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '10 min'),
    ('PASE ESCRITO a Danna + Tarea + Cierre', '12 min'),
]
b1_c16_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M23 non-separable + M24 separable',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico M23/M24 + Human-Sentence Line-up + Station Rotation',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 15 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
]
b1_c16_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas/tiras para board race, sorting, human-line-up y stations ANTES',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final (exclusivo coordinacion)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 16 = FORTALEZA dia 1 v1 (PRIMER del bloque nuevo, por numero de clase)',
    'Cubri M23 Basic Non-Separable Phrasal Verbs DESDE EL LIBRO (A2 Book p.221-232) citando reglas',
    'Cubri M24 Separable Phrasal Verbs DESDE EL LIBRO (A2 Book p.233-240) citando reglas',
    'Explique la regla del libro: no separable=objeto/pronombre AL FINAL / separable=pronombre EN MEDIO',
    'NO ensene M26 Equal Comparatives (es Cl 17; M25 no existe) ni Third Conditional / Could-Should have',
    'NO re-ensene M21/M22 (cerrados Cl 15 - solo reciclaje breve)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14/15)',
    'Conduje BOARD RACE no separable pronombre al final (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases profesionales)',
    'Conduje SORTING fisico M23/M24 (separable vs no separable, posicion del pronombre)',
    'Conduje HUMAN-SENTENCE LINE-UP (estudiantes como palabras, pronombre se mueve al medio)',
    'Conduje STATION ROTATION 3 estaciones (M23 / M24 / mixed)',
    'Conduje SPEED DRILL DE PIE (cadena + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~86%)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'En Tarea explique el por que + due date explicito (jueves 21/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 17 jueves (M25 no existe; M26 Equal Comparatives - confirmar verbatim)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase16_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 16 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~86% DE PIE) | M23 BASIC NON-SEPARABLE PHRASAL VERBS + M24 SEPARABLE PHRASAL VERBS',
    'A2 Book M23 Basic Non-Separable Phrasal Verbs "I Asked for A Pencil." (p.221-232) + M24 Separable Phrasal Verbs "Ill Pick You Up at 8:00." (p.233-240) + Board Race + Walking Transformation + Sorting fisico separable/no separable + Human-Sentence Line-up + Station Rotation + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + FORTALEZA dia 1 v1 PRIMER del bloque nuevo (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14/15)',
    b1_c16_g_act, b1_c16_g_deliv, b1_c16_g_eval, S,
)
print('OK: B1_Clase16_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para miercoles 20/05 B1 MASTERY Cl 16:')
print('  - B1/B1_Clase16_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase16_CONV_REPORTE.pdf')
print('  - B1/B1_Clase16_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase16_GRAMMAR_REPORTE.pdf')
