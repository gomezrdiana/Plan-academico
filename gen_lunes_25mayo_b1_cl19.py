#!/usr/bin/env python3
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 19 (lunes 25/05/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de El Superlativo
  (Hot Topic "The Best, The Worst, The Most ..." + Simulacion "The Award
  Briefing") + Page 18 THE PEAK / THE STRONGEST POINT Draft 1 (escritura
  en clase, alimenta el midterm Cl 22 jueves) + Frase del Dia + FORTALEZA
  dia 4 v1
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M28 The
  Superlative "You're the Best!" (modulo p.253; Guia 1 p.254; Ejemplos p.255;
  Ejercicios p.255; Practica Verbal 1 p.257; Respuestas p.258; Practica
  Verbal 2 Mezclado p.259; Respuestas p.260) + Podium Ceremony + Frase del
  Dia + FORTALEZA dia 4 v1
  (M25 NO existe en el A2 Book — el libro salta de M24 a M26 a M27 a M28).
- SIN texto Heiiu nuevo (mismo criterio que Cl 14/15/16/17/18: gramatica
  estructural, no narrativa — el mapa de Cl 18 anuncio solo "M28 The
  Superlative").
- Anuncio Midterm Cl 22 jueves 28/05 como hecho de cronograma en el cierre
  (sin nota/criterios — eso es coordinacion).
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
# B1 Cl 19 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase19_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase19_CONV_GUIA.pdf'),
)
print('OK: B1_Clase19_CONV_GUIA.pdf')

b1_c19_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 18 Conv)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS FORTALEZA dia 4 (v1)', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 18 Grammar)', '7 min'),
    ('HOT TOPIC - The Best, The Worst, The Most ... (superlativos, oral)', '17 min'),
    ('SIMULACION - The Award Briefing (DE PIE, profesional)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 18 - THE PEAK / THE STRONGEST POINT Draft 1 (escritura en clase anti-fraude, alimenta midterm Cl 22)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Anuncio Midterm + Cierre', '7 min'),
]
b1_c19_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Award Briefing simulacion',
    'Foto/video Mini-Pitch',
    'N Paginas 18 THE PEAK / THE STRONGEST POINT DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 18 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de Midterm Cl 22 jueves como hecho de cronograma (sin nota/criterios)',
]
b1_c19_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (superlativos)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Verifique virtud CL 19 = FORTALEZA dia 4 v1 (por numero de clase)',
    'Hile FORTALEZA en VATS como dia 4 del bloque (peak honesto: no inventar logro, no esconder uno real)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14/15/16/17/18)',
    'RECIBI el PASE escrito de Juan Diego (Cl 18 Grammar) para el Peer Teacher',
    'Conduje Hot Topic The Best, The Worst, The Most ... con requirements en tablero',
    'Conduje The Award Briefing (anunciar 5-6 #1s del trimestre, superlativos, DE PIE)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 18 THE PEAK / THE STRONGEST POINT Draft 1 EN CLASE (anti-fraude IA; alimenta midterm Cl 22)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (martes 26/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 20 martes',
    'Anuncie Midterm Cl 22 jueves como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase19_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 19 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de El Superlativo: Hot Topic "The Best, The Worst, The Most ..." + Simulacion "The Award Briefing" + Page 18 THE PEAK / THE STRONGEST POINT Draft 1 anti-fraude (alimenta midterm Cl 22) + FRASE DEL DIA + PASE a Juan Diego + FORTALEZA dia 4 v1 (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14/15/16/17/18; anuncio Midterm Cl 22 jueves SOLO como hecho de cronograma)',
    b1_c19_c_act, b1_c19_c_deliv, b1_c19_c_eval, S,
)
print('OK: B1_Clase19_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 19 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase19_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase19_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase19_GRAMMAR_GUIA.pdf')

b1_c19_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS FORTALEZA dia 4 (v1) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M28 The Superlative (modulo p.253; Guia 1 p.254) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M28 the -est / the -iest / the most ... / the best-worst - DE PIE', '16 min'),
    ('LIBRO M28 (cont.) 2+ silabas the most ... + irregulares + SORTING fisico por tipo de adjetivo - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP (con tarjeta "the") + STATION ROTATION - 3 estaciones - DE PIE', '12 min'),
    ('PODIUM CEREMONY + SPEED DRILL DE PIE - 1 silaba + -y + 2+ silabas + irregular en cadena/coro', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea + Anuncio Midterm + Cierre', '14 min'),
]
b1_c19_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M28 1-silaba / -y / 2+-silaba / irregular',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico por tipo de adjetivo + Human-Sentence Line-up (con tarjeta "the") + Station Rotation',
    'Foto/video del PODIUM CEREMONY',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 18 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Confirmaste anuncio de Midterm Cl 22 jueves como hecho de cronograma (sin nota/criterios)',
]
b1_c19_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas/tiras para board race, sorting, human-line-up (con tarjeta "the") y stations ANTES',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up + podium)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 19 = FORTALEZA dia 4 v1 (por numero de clase)',
    'Cubri M28 The Superlative DESDE EL LIBRO (A2 Book modulo p.253; Guia 1 p.254; Ejemplos p.255; Ejercicios p.255; Practica Verbal 1 p.257; Respuestas p.258; Practica Verbal 2 p.259; Respuestas p.260) citando reglas',
    'Explique las 4 formas del libro: 1 silaba "the -est" / "-y" -> "the -iest" / 2+ silabas "the most ..." / irregulares good-bad "the best / the worst"',
    'Reforce: SIEMPRE "the" delante; no "the more good"/"the most cheap"; con superlativo va "of/in" no "than"',
    'CONFIRME que M25 NO existe en el A2 Book (el libro salta de M24 a M26 a M27 a M28) - verificado verbatim',
    'NO ensene M29 "How Tall Are You?" (es Cl 20) ni Third Conditional / Could-Should have',
    'NO re-ensene M27 (cerrado Cl 18 - solo contraste breve) ni M26 (cerrado Cl 17) ni M23/M24 (cerrados Cl 16)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14/15/16/17/18)',
    'Conduje BOARD RACE superlativo (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases profesionales)',
    'Conduje SORTING fisico por tipo de adjetivo (1 silaba / -y / 2+ silabas / irregular)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjeta "the" (alguien la sostiene SIEMPRE)',
    'Conduje STATION ROTATION 3 estaciones (1 silaba / -y+irregular / 2+ silabas)',
    'Conduje PODIUM CEREMONY (cadena con coro "Confirmed - the [adj] one!")',
    'Conduje SPEED DRILL DE PIE (cadena form-on-command + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 18 ~86%)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'En Tarea explique el por que + due date explicito (martes 26/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 20 martes (M25 no existe; M26 fue Cl 17; M27 fue Cl 18; M28 fue hoy; sigue M29 "How Tall Are You?" - confirmar verbatim)',
    'Anuncie Midterm Cl 22 jueves como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase19_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 19 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M28 THE SUPERLATIVE (M25 NO EXISTE)',
    'A2 Book M28 The Superlative "Youre the Best!" (modulo p.253; Guia 1 p.254; Ejemplos p.255; Ejercicios p.255; Practica Verbal 1 p.257; Respuestas p.258; Practica Verbal 2 Mezclado p.259; Respuestas p.260) + Board Race + Walking Transformation + Sorting fisico por tipo de adjetivo + Human-Sentence Line-up (con tarjeta "the") + Station Rotation + Podium Ceremony + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + FORTALEZA dia 4 v1 (M25 NO existe - el libro salta de M24 a M26 a M27 a M28; SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14/15/16/17/18; anuncio Midterm Cl 22 jueves SOLO como hecho de cronograma)',
    b1_c19_g_act, b1_c19_g_deliv, b1_c19_g_eval, S,
)
print('OK: B1_Clase19_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para lunes 25/05 B1 MASTERY Cl 19:')
print('  - B1/B1_Clase19_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase19_CONV_REPORTE.pdf')
print('  - B1/B1_Clase19_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase19_GRAMMAR_REPORTE.pdf')
