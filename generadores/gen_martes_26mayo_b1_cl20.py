#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 20 (martes 26/05/2026):
- Bloque 1 CONV (Danna, va PRIMERO): cierre del cluster M28 superlativos +
  intro oral M29 "How + adjective" (Hot Topic "How + Adjective?
  Measuring What Matters at Work" + Simulacion "The Product Specs
  Interview") + Page 19 MY MEASURABLE PROGRESS / WHERE I STAND NOW Draft 1
  (escritura en clase, alimenta el midterm Cl 22 jueves) + Frase del Dia +
  FORTALEZA dia 5 v1 (ULTIMO dia del bloque; manana Cl 21 = PRUDENCIA v2
  dia 1)
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M29
  "How Tall Are You?" / Degrees of Adjectives (modulo p.261; Guia 1 — Los
  Intensificadores p.262; Ejemplos p.263; Ejercicios 1 p.264; Practica
  Verbal 1 p.265; Respuestas p.266) + Measurement-Line Ceremony + Frase
  del Dia + FORTALEZA dia 5 v1
  (M25 NO existe en el A2 Book — el libro salta de M24 a M26 a M27 a M28 a
  M29; M30 "Too Much or Just Enough? / Required Levels" es Cl 21).
- SIN texto Heiiu nuevo (mismo criterio que Cl 14/15/16/17/18/19: gramatica
  estructural, no narrativa — el mapa de Cl 19 anuncio solo "M29 'How Tall
  Are You?'").
- Anuncio Midterm Cl 22 jueves 28/05 como hecho de cronograma en el cierre
  (sin nota/criterios — eso es coordinacion).
- Anuncio CAMBIO DE VIRTUD: hoy ULTIMO dia FORTALEZA v1; manana Cl 21
  abre PRUDENCIA v2 dia 1.
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
# B1 Cl 20 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase20_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase20_CONV_GUIA.pdf'),
)
print('OK: B1_Clase20_CONV_GUIA.pdf')

b1_c20_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 19 Conv)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS FORTALEZA dia 5 v1 - ULTIMO dia del bloque', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 19 Grammar)', '7 min'),
    ('HOT TOPIC - How + Adjective? Measuring What Matters at Work (preguntas de grado, oral)', '17 min'),
    ('SIMULACION - The Product Specs Interview (DE PIE, profesional, "How + adj" + intensificadores)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 19 - MY MEASURABLE PROGRESS / WHERE I STAND NOW Draft 1 (escritura en clase anti-fraude, alimenta midterm Cl 22)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Anuncio Midterm + Anuncio Cambio Virtud (Cl 21 = PRUDENCIA v2 dia 1) + Cierre', '7 min'),
]
b1_c20_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Product Specs Interview simulacion',
    'Foto/video Mini-Pitch',
    'N Paginas 19 MY MEASURABLE PROGRESS / WHERE I STAND NOW DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 19 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de Midterm Cl 22 jueves como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio de cambio de virtud Cl 21 (PRUDENCIA v2 dia 1)',
]
b1_c20_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion ("How + adjective" + intensificador)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Verifique virtud CL 20 = FORTALEZA dia 5 v1 (ULTIMO dia del bloque)',
    'Hile FORTALEZA en VATS como dia 5 - ULTIMO del bloque (medida honesta del tamano de lo construido)',
    'Anuncie al cierre el cambio de virtud Cl 21 = PRUDENCIA v2 dia 1',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14/15/16/17/18/19)',
    'RECIBI el PASE escrito de Juan Diego (Cl 19 Grammar) para el Peer Teacher',
    'Conduje Hot Topic "How + Adjective? Measuring What Matters at Work" con requirements en tablero',
    'Conduje The Product Specs Interview (buyer pregunta "How + adj", vendor responde con intensificador, DE PIE)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 19 MY MEASURABLE PROGRESS / WHERE I STAND NOW Draft 1 EN CLASE (anti-fraude IA; alimenta midterm Cl 22)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (miercoles 27/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 21 miercoles',
    'Anuncie Midterm Cl 22 jueves como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase20_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 20 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Cierre cluster M28 superlativos + intro oral M29 "How + adjective" + intensificadores: Hot Topic "How + Adjective? Measuring What Matters at Work" + Simulacion "The Product Specs Interview" + Page 19 MY MEASURABLE PROGRESS / WHERE I STAND NOW Draft 1 anti-fraude (alimenta midterm Cl 22) + FRASE DEL DIA + PASE a Juan Diego + FORTALEZA dia 5 v1 ULTIMO dia del bloque (manana Cl 21 = PRUDENCIA v2 dia 1) (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14/15/16/17/18/19; anuncio Midterm Cl 22 jueves SOLO como hecho de cronograma)',
    b1_c20_c_act, b1_c20_c_deliv, b1_c20_c_eval, S,
)
print('OK: B1_Clase20_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 20 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase20_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase20_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase20_GRAMMAR_GUIA.pdf')

b1_c20_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS FORTALEZA dia 5 v1 (ULTIMO dia del bloque) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M29 "How Tall Are You?" / Degrees of Adjectives (modulo p.261; Guia 1 p.262) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M29 pregunta "How + adj + to be + subject?" + respuesta con intensificador - DE PIE', '16 min'),
    ('LIBRO M29 (cont.) los 6 intensificadores (really/very/kinda/sorta/pretty/not very) + SORTING fisico por intensidad - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP (con tarjeta "HOW") + STATION ROTATION - 3 estaciones (pregunta / strong / so-so-quite-polite) - DE PIE', '12 min'),
    ('MEASUREMENT-LINE CEREMONY + SPEED DRILL DE PIE - linea fisica (not very / kinda-sorta / pretty / really-very) en cadena/coro', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea + Anuncio Midterm + Anuncio Cambio Virtud (Cl 21 = PRUDENCIA v2 dia 1) + Cierre', '14 min'),
]
b1_c20_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M29 "How + adj + to be + subject?" + 6 intensificadores',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico por intensidad + Human-Sentence Line-up (con tarjeta "HOW") + Station Rotation',
    'Foto/video del MEASUREMENT-LINE CEREMONY (linea fisica con 4 marcas)',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 19 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Confirmaste anuncio de Midterm Cl 22 jueves como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio de cambio de virtud Cl 21 (PRUDENCIA v2 dia 1)',
]
b1_c20_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas/tiras para board race, sorting por intensidad, human-line-up (con tarjeta "HOW") y stations ANTES',
    'PREPARE la MEASUREMENT-LINE en el piso/tablero ANTES de clase (4 marcas: not very / kinda-sorta / pretty / really-very)',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up + measurement-line)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 20 = FORTALEZA dia 5 v1 (ULTIMO dia del bloque)',
    'Anuncie al cierre el cambio de virtud Cl 21 = PRUDENCIA v2 dia 1',
    'Cubri M29 "How Tall Are You?" DESDE EL LIBRO (A2 Book modulo p.261; Guia 1 Los Intensificadores p.262; Ejemplos p.263; Ejercicios 1 p.264; Practica Verbal 1 p.265; Respuestas p.266) citando reglas',
    'Explique la pregunta "How + adjetivo + to be + sujeto?" y los 6 intensificadores: REALLY / VERY (strong) / KINDA / SORTA (so-so) / PRETTY (quite) / NOT VERY (polite opposite)',
    'Reforce: orden de la pregunta (NO "How is busy Monday?"); intensificador VA ANTES del adjetivo (NO "busy really"); "not very" para negacion cortes (NO "not too")',
    'CONFIRME que M25 NO existe en el A2 Book (el libro salta de M24 a M26 a M27 a M28 a M29) - verificado verbatim',
    'NO ensene M30 "Too Much or Just Enough? / Required Levels" (es Cl 21) ni Third Conditional / Could-Should have',
    'NO re-ensene M28 (cerrado Cl 19 - solo contraste breve) ni M27 (cerrado Cl 18) ni M26 (cerrado Cl 17) ni M23/M24 (cerrados Cl 16)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14/15/16/17/18/19)',
    'Conduje BOARD RACE "How + adj" (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, preguntas profesionales + respuesta con intensificador)',
    'Conduje SORTING fisico por intensidad (STRONG really-very / SO-SO kinda-sorta / QUITE pretty / POLITE OPPOSITE not very)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjeta "HOW" (alguien la sostiene SIEMPRE al inicio)',
    'Conduje STATION ROTATION 3 estaciones (pregunta / strong answers / so-so-quite-polite answers)',
    'Conduje MEASUREMENT-LINE CEREMONY (linea fisica 4 marcas, cohorte se ubica honestamente, coro "Confirmed - [intensifier] [adj]!")',
    'Conduje SPEED DRILL DE PIE (cadena form-on-command + coro rapido pregunta+respuesta)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 19)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + aviso cambio de virtud',
    'En Tarea explique el por que + due date explicito (miercoles 27/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 21 miercoles (M25 no existe; M26 fue Cl 17; M27 fue Cl 18; M28 fue Cl 19; M29 fue hoy; sigue M30 "Too Much or Just Enough? / Required Levels" - confirmar verbatim)',
    'Anuncie Midterm Cl 22 jueves como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase20_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 20 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M29 "HOW TALL ARE YOU?" / DEGREES OF ADJECTIVES (M25 NO EXISTE)',
    'A2 Book M29 "How Tall Are You?" / Degrees of Adjectives (modulo p.261; Guia 1 Los Intensificadores p.262; Ejemplos p.263; Ejercicios 1 p.264; Practica Verbal 1 p.265; Respuestas p.266) + Board Race + Walking Transformation + Sorting fisico por intensidad + Human-Sentence Line-up (con tarjeta "HOW") + Station Rotation + Measurement-Line Ceremony + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + FORTALEZA dia 5 v1 ULTIMO dia (manana Cl 21 = PRUDENCIA v2 dia 1) (M25 NO existe - el libro salta de M24 a M26 a M27 a M28 a M29; SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14/15/16/17/18/19; anuncio Midterm Cl 22 jueves SOLO como hecho de cronograma)',
    b1_c20_g_act, b1_c20_g_deliv, b1_c20_g_eval, S,
)
print('OK: B1_Clase20_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para martes 26/05 B1 MASTERY Cl 20:')
print('  - B1/B1_Clase20_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase20_CONV_REPORTE.pdf')
print('  - B1/B1_Clase20_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase20_GRAMMAR_REPORTE.pdf')
