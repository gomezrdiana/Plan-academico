#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 17 (jueves 21/05/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Comparativos Iguales
  (Hot Topic "Comparing Two Jobs / Two Tools / Two Days" + Simulacion "The Two
  Options Briefing") + Page 16 THE COMPARISON / WHERE I STAND Draft 1 (escritura
  en clase) + Frase del Dia + FORTALEZA dia 2 v1
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~86% DE PIE): A2 Book M26 Equal
  Comparatives (modulo p.241; Guia 1 p.243; Ejemplos/Ejercicios p.244) +
  Frase del Dia + FORTALEZA dia 2 v1
  (M25 NO existe en el A2 Book — el libro salta de M24 a M26).
- SIN texto Heiiu nuevo (mismo criterio que Cl 14/15/16: gramatica estructural,
  no narrativa — el mapa de Cl 16 anuncio solo "M26 Equal Comparatives").
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
# B1 Cl 17 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase17_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase17_CONV_GUIA.pdf'),
)
print('OK: B1_Clase17_CONV_GUIA.pdf')

b1_c17_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 16 Conv)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS FORTALEZA dia 2 (v1)', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 16 Grammar)', '7 min'),
    ('HOT TOPIC - Comparing Two Jobs / Two Tools / Two Days (comparativos iguales, oral)', '17 min'),
    ('SIMULACION - The Two Options Briefing (DE PIE, profesional)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 16 - THE COMPARISON / WHERE I STAND Draft 1 (escritura en clase anti-fraude)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Cierre', '7 min'),
]
b1_c17_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Two Options Briefing simulacion',
    'Foto/video Mini-Pitch',
    '17 Paginas 16 THE COMPARISON / WHERE I STAND DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 16 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b1_c17_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (comparativos iguales)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final (exclusivo coordinacion)',
    'Verifique virtud CL 17 = FORTALEZA dia 2 v1 (por numero de clase)',
    'Hile FORTALEZA en VATS como dia 2 del bloque (medir honesto: no encoger problema ni persona)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14/15/16)',
    'RECIBI el PASE escrito de Juan Diego (Cl 16 Grammar) para el Peer Teacher',
    'Conduje Hot Topic Comparing Two Jobs / Two Tools / Two Days con requirements en tablero',
    'Conduje The Two Options Briefing (dos opciones equivalentes, comparativos iguales, DE PIE)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 16 THE COMPARISON / WHERE I STAND Draft 1 EN CLASE (anti-fraude IA)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (viernes 22/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 18 viernes',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase17_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 17 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de Comparativos Iguales: Hot Topic "Comparing Two Jobs / Two Tools / Two Days" + Simulacion "The Two Options Briefing" + Page 16 THE COMPARISON / WHERE I STAND Draft 1 anti-fraude + FRASE DEL DIA + PASE a Juan Diego + FORTALEZA dia 2 v1 (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14/15/16)',
    b1_c17_c_act, b1_c17_c_deliv, b1_c17_c_eval, S,
)
print('OK: B1_Clase17_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 17 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~86% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase17_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase17_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase17_GRAMMAR_GUIA.pdf')

b1_c17_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS FORTALEZA dia 2 (v1) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M26 Equal Comparatives (modulo p.241; Guia 1 p.243) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M26 as...as / not as...as / almost as...as - DE PIE', '16 min'),
    ('LIBRO M26 (cont.) negativa + aproximada + adjetivo BASE + SORTING fisico equal/not-equal/almost - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP + STATION ROTATION - 3 estaciones (as...as / not as...as / almost as...as) - DE PIE', '14 min'),
    ('SPEED DRILL DE PIE - equal + not-equal + almost en cadena/coro', '12 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '10 min'),
    ('PASE ESCRITO a Danna + Tarea + Cierre', '12 min'),
]
b1_c17_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M26 equal / not-equal / almost',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico EQUAL/NOT-EQUAL/ALMOST + Human-Sentence Line-up + Station Rotation',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 16 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
]
b1_c17_g_eval = [
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
    'Verifique virtud CL 17 = FORTALEZA dia 2 v1 (por numero de clase)',
    'Cubri M26 Equal Comparatives DESDE EL LIBRO (A2 Book modulo p.241; Guia 1 p.243; Ejemplos/Ejercicios p.244) citando reglas',
    'Explique la regla del libro: "as + adjetivo BASE + as" (igual) / "not as ... as" (menos) / "almost as ... as" (casi)',
    'Reforce: adjetivo SIEMPRE en forma BASE (nunca "as better as") y NUNCA "than" (eso es M27)',
    'CONFIRME que M25 NO existe en el A2 Book (el libro salta de M24 a M26) - verificado verbatim',
    'NO ensene M27 Unequal Comparatives (es Cl 18) ni Third Conditional / Could-Should have',
    'NO re-ensene M23/M24 (cerrados Cl 16 - solo reciclaje breve)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14/15/16)',
    'Conduje BOARD RACE equal comparative "as + base + as" (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases profesionales)',
    'Conduje SORTING fisico EQUAL / NOT-EQUAL / ALMOST (que modificador, adjetivo base)',
    'Conduje HUMAN-SENTENCE LINE-UP (estudiantes como palabras, "as" abraza el adjetivo, not/almost al frente)',
    'Conduje STATION ROTATION 3 estaciones (as...as / not as...as / almost as...as)',
    'Conduje SPEED DRILL DE PIE (cadena form-on-command + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~86%, como Cl 16)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'En Tarea explique el por que + due date explicito (viernes 22/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 18 viernes (M25 no existe; M26 fue hoy; sigue M27 Unequal Comparatives - confirmar verbatim)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase17_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 17 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~86% DE PIE) | M26 EQUAL COMPARATIVES (M25 NO EXISTE)',
    'A2 Book M26 Equal Comparatives "Im as Big as My Dad." (modulo p.241; Vocabulario 1 p.242; Guia 1 p.243; Ejemplos/Ejercicios p.244; Practica Verbal p.245-246) + Board Race + Walking Transformation + Sorting fisico equal/not-equal/almost + Human-Sentence Line-up + Station Rotation + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + FORTALEZA dia 2 v1 (M25 NO existe - el libro salta de M24 a M26; SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14/15/16)',
    b1_c17_g_act, b1_c17_g_deliv, b1_c17_g_eval, S,
)
print('OK: B1_Clase17_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para jueves 21/05 B1 MASTERY Cl 17:')
print('  - B1/B1_Clase17_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase17_CONV_REPORTE.pdf')
print('  - B1/B1_Clase17_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase17_GRAMMAR_REPORTE.pdf')
