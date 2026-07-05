#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 14 (lunes 18/05/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Voz Pasiva (Hot Topic
  "Who Gets the Credit?" + Simulacion "The Process Walkthrough") + Page 13
  NARRATIVE Draft 3 (escritura en clase) + Frase del Dia + JUSTICIA dia 4 v1
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~86% DE PIE): A2 Book M18 Passive
  Voice (p.173-174) + M20 Gerunds as Subjects (p.181-183) [M19 no existe] +
  Frase del Dia + JUSTICIA dia 4 v1
- SIN texto Heiiu nuevo (el de Cl 13 fue un hito unico — no se reinventa).
- SIN GoldList (eliminado 14/05/2026). Reportes ESTATICOS (se llenan a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_DIR = os.path.join(D, 'B1')
B1_REP = os.path.join(B1_DIR, 'reportes')
os.makedirs(B1_REP, exist_ok=True)

# ============================================================
# B1 Cl 14 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase14_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase14_CONV_GUIA.pdf'),
)
print('OK: B1_Clase14_CONV_GUIA.pdf')

b1_c14_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 13)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS JUSTICIA dia 4 (v1)', '7 min'),
    ('PEER TEACHER SLOT (errores Cl 13 Conv de tu libreta)', '7 min'),
    ('HOT TOPIC - Who Gets the Credit? (Voz Pasiva oral)', '17 min'),
    ('SIMULACION - The Process Walkthrough (DE PIE, profesional)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 13 - NARRATIVE Draft 3 (escritura en clase anti-fraude)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Cierre', '7 min'),
]
b1_c14_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER',
    'Foto/video de The Process Walkthrough simulacion',
    'Foto/video Mini-Pitch',
    '16 Paginas 13 NARRATIVE DRAFT 3 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 13 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b1_c14_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (passive)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final (exclusivo coordinacion)',
    'Verifique virtud CL 14 = JUSTICIA dia 4 v1 (por numero de clase)',
    'Hile JUSTICIA en VATS con voz pasiva (trabajo compartido / credito)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (el de Cl 13 fue hito unico - no se reinventa)',
    'Conduje Hot Topic Who Gets the Credit con requirements en tablero',
    'Conduje The Process Walkthrough (proceso profesional en voz pasiva, DE PIE)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 13 Draft 3 EN CLASE (anti-fraude IA)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (martes 19/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 15 martes',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase14_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 14 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de Voz Pasiva: Hot Topic "Who Gets the Credit?" + Simulacion "The Process Walkthrough" + Page 13 NARRATIVE Draft 3 anti-fraude + FRASE DEL DIA + PASE a Juan Diego + JUSTICIA dia 4 v1 (SIN texto Heiiu - el de Cl 13 fue hito unico)',
    b1_c14_c_act, b1_c14_c_deliv, b1_c14_c_eval, S,
)
print('OK: B1_Clase14_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 14 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~86% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase14_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase14_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase14_GRAMMAR_GUIA.pdf')

b1_c14_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS JUSTICIA dia 4 (v1) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M18 Passive Voice (p.173-174) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M18 active<->passive - DE PIE', '16 min'),
    ('LIBRO M20 Gerunds as Subjects (p.181-183) + SORTING fisico - DE PIE', '12 min'),
    ('STATION ROTATION - 3 estaciones (M18 / M20 / mixed) - DE PIE', '14 min'),
    ('SPEED DRILL DE PIE - gerund-subject + passive en cadena/coro', '12 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '10 min'),
    ('PASE ESCRITO a Danna + Tarea + Cierre', '12 min'),
]
b1_c14_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M18 active->passive + M20 gerund-subject',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas ACTIVE/PASSIVE)',
    'Foto/video del Sorting fisico M20 + Station Rotation',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 13 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
]
b1_c14_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas/tiras para board race, sorting y stations ANTES',
    'DESPEJE espacio para movimiento (board race + walking transformation)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final (exclusivo coordinacion)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 14 = JUSTICIA dia 4 v1 (por numero de clase)',
    'Cubri M18 Passive Voice DESDE EL LIBRO (A2 Book p.173-174) citando reglas',
    'Cubri M20 Gerunds as Subjects DESDE EL LIBRO (A2 Book p.181-183) citando reglas',
    'Explique que M19 NO existe en el libro (salto confirmado en mapa Cl 13)',
    'NO ensene M21/M22 (son Cl 15) ni Passive con perfectos / Third Conditional',
    'NO use texto Heiiu (el de Cl 13 fue hito unico - no se reinventa)',
    'Conduje BOARD RACE active->passive (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas ACTIVE/PASSIVE, frases profesionales)',
    'Conduje SORTING fisico M20 (verbo + is+adjetivo -> gerundio sujeto)',
    'Conduje STATION ROTATION 3 estaciones (M18 / M20 / mixed)',
    'Conduje SPEED DRILL DE PIE (cadena + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~86%)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'En Tarea explique el por que + due date explicito (martes 19/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M21 Gerunds after Prepositions + M22 Double Verbs para Cl 15 martes',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase14_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 14 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~86% DE PIE) | M18 PASSIVE VOICE + M20 GERUNDS AS SUBJECTS',
    'A2 Book M18 The Passive Voice for Regular Participles (p.173-174) + M20 Gerunds as Subjects "Playing is Fun!" (p.181-183) [M19 no existe] + Board Race + Walking Transformation + Sorting fisico + Station Rotation + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + JUSTICIA dia 4 v1 (SIN texto Heiiu - el de Cl 13 fue hito unico)',
    b1_c14_g_act, b1_c14_g_deliv, b1_c14_g_eval, S,
)
print('OK: B1_Clase14_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para lunes 18/05 B1 MASTERY Cl 14:')
print('  - B1/B1_Clase14_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase14_CONV_REPORTE.pdf')
print('  - B1/B1_Clase14_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase14_GRAMMAR_REPORTE.pdf')
