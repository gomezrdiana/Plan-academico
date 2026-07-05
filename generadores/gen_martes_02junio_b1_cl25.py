#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 25 (martes 02/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de M34 Describing
  Prices (Hot Topic "What Does It Really Cost?" + Simulacion "The Price
  Briefing") + Page 22 MY HONEST PRICE TAGS / WHAT THIS PATH COSTS ME
  Draft 1 (escritura en clase, alimenta el Final Cl 44) + Frase del Dia +
  PRUDENCIA dia 5 v2 ULTIMO (anuncia transicion a TEMPLANZA v2 manana)
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M34
  "How Much Does It Cost? / Describing Prices" (modulo p.293; Guia 1
  p.294; Practica Verbal 1 p.295; Respuestas p.296; Practica Verbal 2
  p.297; Respuestas p.298; Practica Verbal 3 p.299; Respuestas p.300) +
  Price Podium Ceremony + Historia interactiva absurda profesional +
  Frase del Dia + PRUDENCIA dia 5 v2 ULTIMO (confirma cambio a TEMPLANZA
  v2 manana)
  (M35 NO existe en el A2 Book — el libro salta de M34 a M36; patron
  consistente con M19/M25/M31 ya saltados.)
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-24: gramatica
  estructural transaccional, no narrativa).
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin
  nota/criterios — eso es coordinacion).
- Anuncio CAMBIO DE VIRTUD: manana Cl 26 = TEMPLANZA v2 dia 1
  (PRUDENCIA v2 termina hoy con Cl 25 dia 5 ULTIMO).
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
# B1 Cl 25 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase25_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase25_CONV_GUIA.pdf'),
)
print('OK: B1_Clase25_CONV_GUIA.pdf')

b1_c25_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 24 Conv M33 how much + uncountable)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS PRUDENCIA dia 5 v2 (ULTIMO - anuncia transicion a TEMPLANZA v2 manana)', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 24 Grammar M33)', '7 min'),
    ('HOT TOPIC - What Does It Really Cost? (price questions/answers, oral)', '17 min'),
    ('SIMULACION - The Price Briefing (DE PIE, costos reales del proximo trimestre)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 22 - MY HONEST PRICE TAGS / WHAT THIS PATH COSTS ME Draft 1 (escritura en clase anti-fraude, alimenta Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Anuncio Cl 26 + Anuncio CAMBIO VIRTUD a TEMPLANZA v2 + Anuncio Final + Cierre', '7 min'),
]
b1_c25_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego Cl 24 M33)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Price Briefing simulacion',
    'Foto/video Mini-Pitch',
    'N Paginas 22 MY HONEST PRICE TAGS DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 24 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de CAMBIO VIRTUD (manana Cl 26 = TEMPLANZA v2 dia 1)',
    'Confirmaste anuncio del Final Cl 44 como hecho de cronograma (sin nota/criterios)',
]
b1_c25_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (price Q + A)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Verifique virtud CL 25 = PRUDENCIA dia 5 v2 ULTIMO (por numero de clase, calendario absoluto)',
    'Hile PRUDENCIA en VATS como dia 5 ULTIMO del bloque (precio honesto del camino: no inflar, no esconder)',
    'ANUNCIE EXPLICITAMENTE al cierre que manana Cl 26 = TEMPLANZA v2 dia 1 (cambio de bloque visible)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica estructural transaccional - mismo criterio que Cl 14-24)',
    'RECIBI el PASE escrito de Juan Diego (Cl 24 Grammar M33) para el Peer Teacher',
    'Conduje Hot Topic What Does It Really Cost? con requirements en tablero',
    'Conduje The Price Briefing (5-6 precios honestos del proximo trimestre, DE PIE)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 22 MY HONEST PRICE TAGS Draft 1 EN CLASE (anti-fraude IA; alimenta Final Cl 44)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (miercoles 03/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 26 miercoles',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase25_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 25 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado) | PRUDENCIA dia 5 v2 ULTIMO',
    'Aplicacion oral de M34 Describing Prices: Hot Topic "What Does It Really Cost?" + Simulacion "The Price Briefing" + Page 22 MY HONEST PRICE TAGS / WHAT THIS PATH COSTS ME Draft 1 anti-fraude (alimenta Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + PRUDENCIA dia 5 v2 ULTIMO (SIN texto Heiiu - gramatica estructural transaccional, mismo criterio que Cl 14-24; anuncio CAMBIO VIRTUD a TEMPLANZA v2 manana Cl 26; anuncio Final Cl 44 SOLO como hecho de cronograma)',
    b1_c25_c_act, b1_c25_c_deliv, b1_c25_c_eval, S,
)
print('OK: B1_Clase25_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 25 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase25_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase25_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase25_GRAMMAR_GUIA.pdf')

b1_c25_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 24 Grammar M33) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS PRUDENCIA dia 5 v2 ULTIMO (confirma transicion a TEMPLANZA v2 manana) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M34 Describing Prices (modulo p.293; Guia 1 p.294) - estructura A "cost" + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION entre estructura A "How much DOES + subj + COST?" y estructura B "How much IS + subj?" - DE PIE', '16 min'),
    ('LIBRO M34 (cont.) estructura B "be" + "each" por unidad + SORTING fisico (cost vs be / each vs total) + HISTORIA INTERACTIVA absurda profesional - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP (con tarjeta "DOES") + STATION ROTATION - 3 estaciones (cost / be / each) - DE PIE', '12 min'),
    ('PRICE PODIUM CEREMONY + SPEED DRILL DE PIE - ambas estructuras + each en cadena/coro', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea + Anuncio Cl 26 (M36 - M35 no existe) + CONFIRMACION CAMBIO VIRTUD a TEMPLANZA v2 + Anuncio Final + Cierre', '14 min'),
]
b1_c25_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M34 estructura A (cost) + estructura B (be) + "each"',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas COST/BE)',
    'Foto/video del Sorting fisico (cost vs be / each vs total) + Historia interactiva absurda profesional + Human-Sentence Line-up (con tarjeta "DOES") + Station Rotation',
    'Foto/video del PRICE PODIUM CEREMONY',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 24 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Confirmaste anuncio de CAMBIO VIRTUD (manana Cl 26 = TEMPLANZA v2 dia 1)',
    'Confirmaste anuncio del Final Cl 44 como hecho de cronograma (sin nota/criterios)',
]
b1_c25_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas/tiras para board race, sorting, human-line-up (con tarjeta "DOES") y stations ANTES',
    'PREPARE el PODIO de precios en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up + price podium)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 25 = PRUDENCIA dia 5 v2 ULTIMO (por numero de clase, calendario absoluto)',
    'CONFIRME EXPLICITAMENTE al cierre que manana Cl 26 = TEMPLANZA v2 dia 1 (cambio de bloque visible)',
    'Cubri M34 Describing Prices DESDE EL LIBRO (A2 Book modulo p.293; Guia 1 p.294; Practica Verbal 1 p.295; Respuestas p.296; Practica Verbal 2 p.297; Respuestas p.298; Practica Verbal 3 p.299; Respuestas p.300) citando reglas',
    'Explique las DOS estructuras del libro: (a) "How much DOES/DO + subject + COST?" -> "It costs $X / They cost $X each" (verbo cost + ayudante do/does + -s en 3a sing.); (b) "How much IS/ARE + subject?" -> "It\'s $X / They\'re $X each" (verbo be, sin ayudante)',
    'Reforce: "each" = por unidad (al final de la respuesta); la pregunta implica "how much money" pero NO se dice "money"; pasado irregular de "cost" = "cost"',
    'CONFIRME que M35 NO existe en el A2 Book (el libro salta de M34 a M36) - verificado verbatim; patron consistente con M19/M25/M31',
    'NO ensene M36 "What Are You Wearing? / Describing Clothing" (es Cl 26) ni Third Conditional / Could-Should have',
    'NO re-ensene M33 (cerrado Cl 24 - solo contraste breve) ni M32 (cerrado Cl 23) ni modulos anteriores',
    'NO use texto Heiiu (gramatica estructural transaccional - mismo criterio que Cl 14-24)',
    'Conduje BOARD RACE precios (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION entre las DOS estructuras (zonas COST/BE, frases profesionales)',
    'Conduje SORTING fisico (cost vs be / each vs total)',
    'Conduje HISTORIA INTERACTIVA absurda profesional (la caja de clips de 89 dolares) con pausas marcadas y cohorte en voz alta',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjeta "DOES" (solo va con estructura cost; NO con be)',
    'Conduje STATION ROTATION 3 estaciones (cost / be / each)',
    'Conduje PRICE PODIUM CEREMONY (cadena con coro "Confirmed - that\'s the honest price!")',
    'Conduje SPEED DRILL DE PIE (cadena form-on-command ambas estructuras + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 19/21/23)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'En Tarea explique el por que + due date explicito (miercoles 03/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 26 miercoles (M35 no existe; M36 "What Are You Wearing? / Describing Clothing" p.301+ - confirmar verbatim)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase25_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 25 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M34 DESCRIBING PRICES (M35 NO EXISTE) | PRUDENCIA dia 5 v2 ULTIMO',
    'A2 Book M34 "How Much Does It Cost? / Describing Prices" (modulo p.293; Guia 1 p.294; Practica Verbal 1 p.295; Respuestas p.296; Practica Verbal 2 p.297; Respuestas p.298; Practica Verbal 3 p.299; Respuestas p.300) - DOS estructuras: (a) "How much DOES + subj + COST?" -> "It costs $X / They cost $X each" + (b) "How much IS/ARE + subj?" -> "It\'s $X / They\'re $X each" + "each" por unidad. Board Race + Walking Transformation entre las dos estructuras + Sorting fisico (cost vs be / each vs total) + Historia interactiva absurda profesional + Human-Sentence Line-up (con tarjeta "DOES") + Station Rotation + Price Podium Ceremony + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + PRUDENCIA dia 5 v2 ULTIMO (M35 NO existe - el libro salta de M34 a M36 "What Are You Wearing? / Describing Clothing" p.301+; patron consistente con M19/M25/M31; SIN texto Heiiu - gramatica estructural transaccional; anuncio CAMBIO VIRTUD a TEMPLANZA v2 manana Cl 26; anuncio Final Cl 44 SOLO como hecho de cronograma)',
    b1_c25_g_act, b1_c25_g_deliv, b1_c25_g_eval, S,
)
print('OK: B1_Clase25_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para martes 02/06 B1 MASTERY Cl 25:')
print('  - B1/B1_Clase25_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase25_CONV_REPORTE.pdf')
print('  - B1/B1_Clase25_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase25_GRAMMAR_REPORTE.pdf')
