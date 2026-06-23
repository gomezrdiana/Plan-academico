#!/usr/bin/env python3
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 15 (martes 19/05/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Gerundio tras Preposicion
  + Doble Verbo (Hot Topic "Habits That Build a Career" + Simulacion "The
  Onboarding Conversation") + Page 14 NARRATIVE Draft 4 / Final (escritura en
  clase) + Frase del Dia + JUSTICIA dia 5 v1 (ULTIMO del bloque)
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~86% DE PIE): A2 Book M21 Gerunds
  after Prepositions (p.197-201) + M22 Gerunds with Double Verbs (p.207-210) +
  Frase del Dia + JUSTICIA dia 5 v1 (ULTIMO del bloque)
- SIN texto Heiiu nuevo (mismo criterio que Cl 14: gramatica estructural, no
  narrativa — el mapa de Cl 14 no solicita texto para Cl 15).
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
# B1 Cl 15 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase15_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase15_CONV_GUIA.pdf'),
)
print('OK: B1_Clase15_CONV_GUIA.pdf')

b1_c15_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 14 Conv)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS JUSTICIA dia 5 (v1) - ULTIMO del bloque', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 14 Grammar)', '7 min'),
    ('HOT TOPIC - Habits That Build a Career (gerundio tras preposicion + doble verbo, oral)', '17 min'),
    ('SIMULACION - The Onboarding Conversation (DE PIE, profesional)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 14 - NARRATIVE Draft 4 / Final (escritura en clase anti-fraude)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Cierre', '7 min'),
]
b1_c15_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Onboarding Conversation simulacion',
    'Foto/video Mini-Pitch',
    '16 Paginas 14 NARRATIVE DRAFT 4 / FINAL (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 14 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b1_c15_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (prep+-ing / doble verbo)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final (exclusivo coordinacion)',
    'Verifique virtud CL 15 = JUSTICIA dia 5 v1 (ULTIMO del bloque, por numero de clase)',
    'Hile JUSTICIA en VATS como cierre del bloque (ayudar antes de ser agradecido)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14)',
    'RECIBI el PASE escrito de Juan Diego (Cl 14 Grammar) para el Peer Teacher',
    'Conduje Hot Topic Habits That Build a Career con requirements en tablero',
    'Conduje The Onboarding Conversation (consejos profesionales, prep+-ing + doble verbo, DE PIE)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 14 Draft 4 / Final EN CLASE (anti-fraude IA)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (miercoles 20/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 16 miercoles',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase15_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 15 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de Gerundio tras Preposicion + Doble Verbo: Hot Topic "Habits That Build a Career" + Simulacion "The Onboarding Conversation" + Page 14 NARRATIVE Draft 4 / Final anti-fraude + FRASE DEL DIA + PASE a Juan Diego + JUSTICIA dia 5 v1 ULTIMO del bloque (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14)',
    b1_c15_c_act, b1_c15_c_deliv, b1_c15_c_eval, S,
)
print('OK: B1_Clase15_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 15 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~86% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase15_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase15_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase15_GRAMMAR_GUIA.pdf')

b1_c15_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS JUSTICIA dia 5 (v1) ULTIMO del bloque - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M21 Gerund after Preposition (p.197-201) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M21 infinitivo<->prep+-ing - DE PIE', '16 min'),
    ('LIBRO M22 Double Verbs (p.207-210) + SORTING fisico infinitivo/gerundio - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP + STATION ROTATION - 3 estaciones (M21 / M22 / mixed) - DE PIE', '14 min'),
    ('SPEED DRILL DE PIE - prep+-ing + double verbs en cadena/coro', '12 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '10 min'),
    ('PASE ESCRITO a Danna + Tarea + Cierre', '12 min'),
]
b1_c15_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M21 prep+-ing + M22 double verbs',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico M22 + Human-Sentence Line-up + Station Rotation',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 14 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
]
b1_c15_g_eval = [
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
    'Verifique virtud CL 15 = JUSTICIA dia 5 v1 (ULTIMO del bloque, por numero de clase)',
    'Cubri M21 Gerunds after Prepositions DESDE EL LIBRO (A2 Book p.197-201) citando reglas',
    'Cubri M22 Gerunds with Double Verbs DESDE EL LIBRO (A2 Book p.207-210) citando reglas',
    'Explique la regla del libro: infinitivo=no ha empezado / gerundio=si ha empezado',
    'NO ensene M23/M24 (son Cl 16) ni Third Conditional / Could-Should have',
    'NO re-ensene M18/M20 (cerrados Cl 14 - solo reciclaje breve)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14)',
    'Conduje BOARD RACE preposition+-ing (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases profesionales)',
    'Conduje SORTING fisico M22 (primer verbo decide infinitivo o gerundio)',
    'Conduje HUMAN-SENTENCE LINE-UP (estudiantes como palabras)',
    'Conduje STATION ROTATION 3 estaciones (M21 / M22 / mixed)',
    'Conduje SPEED DRILL DE PIE (cadena + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~86%)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'En Tarea explique el por que + due date explicito (miercoles 20/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M23 Non-Separable + M24 Separable Phrasal Verbs para Cl 16 miercoles',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase15_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 15 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~86% DE PIE) | M21 GERUNDS AFTER PREPOSITIONS + M22 GERUNDS WITH DOUBLE VERBS',
    'A2 Book M21 Gerunds after Prepositions "We Shouldnt Swim After Eating" (p.197-201) + M22 Gerunds with Double Verbs "I Love Swimming!" (p.207-210) + Board Race + Walking Transformation + Sorting fisico + Human-Sentence Line-up + Station Rotation + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + JUSTICIA dia 5 v1 ULTIMO del bloque (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14)',
    b1_c15_g_act, b1_c15_g_deliv, b1_c15_g_eval, S,
)
print('OK: B1_Clase15_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para martes 19/05 B1 MASTERY Cl 15:')
print('  - B1/B1_Clase15_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase15_CONV_REPORTE.pdf')
print('  - B1/B1_Clase15_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase15_GRAMMAR_REPORTE.pdf')
