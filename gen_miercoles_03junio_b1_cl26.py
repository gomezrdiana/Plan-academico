#!/usr/bin/env python3
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 26 (miercoles 03/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de M36 Describing Clothing
  (Hot Topic "Dress for the Role, Not the Show" + Simulacion "The Professional
  Wardrobe Briefing") + Page 23 THE CALM PROFESSIONAL SELF I CHOOSE Draft 1
  (escritura en clase, primera pagina del capitulo TEMPLANZA hacia el Final
  Cl 44) + Frase del Dia + TRANSICION PRUDENCIA v2 -> TEMPLANZA v2 dia 1
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M36
  "What Are You Wearing? / Describing Clothing" (modulo p.301; Vocabulario 1
  Prendas de Vestir p.302; Vocabulario 2 Los Colores p.303; Guia 1 La Ropa
  p.304; Ejemplos Adjetivos p.305; Ejercicios Adjetivos p.306) + Board Race
  + Walking Transformation + Sorting fisico (clothing/colors/modifier/verb)
  + Historia interactiva absurda profesional + Human-Sentence Line-up
  (tarjeta "ADJ-BEFORE-NOUN") + Wardrobe Walk / Dress-Up Station +
  Station Rotation + TEMPERANCE PODIUM CEREMONY (3 contextos profesionales)
  + Speed Drill DE PIE + Frase del Dia + TRANSICION PRUDENCIA v2 ->
  TEMPLANZA v2 dia 1
  (M35 NO existe en el A2 Book -- el libro salta de M34 a M36; patron
  consistente con M19/M25/M31 ya saltados).
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-25: gramatica lexico-
  estructural, no narrativa).
- TRANSICION DE VIRTUD HOY: PRUDENCIA v2 (Cl 21-25) -> TEMPLANZA v2
  (Cl 26-30). Hoy Cl 26 = dia 1 del nuevo bloque -- nombrar VISIBLEMENTE
  en el VATS al inicio (no implicita). Calendario absoluto verificado.
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin nota/
  criterios -- eso es coordinacion).
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
# B1 Cl 26 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase26_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase26_CONV_GUIA.pdf'),
)
print('OK: B1_Clase26_CONV_GUIA.pdf')

b1_c26_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 25 Conv + M33/M34 reciclados)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS TRANSICION PRUDENCIA v2 -> TEMPLANZA v2 dia 1 (NUEVO BLOQUE Cl 26-30)', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 25 Grammar M34 prices)', '7 min'),
    ('HOT TOPIC - "Dress for the Role, Not the Show" (codigo profesional + balance, oral)', '17 min'),
    ('SIMULACION - "The Professional Wardrobe Briefing" (DE PIE, 3 contextos, M36 preview)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 23 - THE CALM PROFESSIONAL SELF I CHOOSE Draft 1 (escritura en clase anti-fraude, primera pagina del capitulo TEMPLANZA hacia Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Anuncio Cl 27 + Cierre', '7 min'),
]
b1_c26_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego Cl 25 M34)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Professional Wardrobe Briefing simulacion',
    'Foto/video Mini-Pitch',
    'N Paginas 23 THE CALM PROFESSIONAL SELF I CHOOSE DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 25 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'CONFIRMASTE que nombraste VISIBLEMENTE la TRANSICION PRUDENCIA v2 -> TEMPLANZA v2 dia 1 en el VATS (no implicita)',
    'Cuantas veces te preguntaron resultado del midterm o como sera el Final y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Cl 44 Final como hecho de cronograma (sin nota/criterios)',
]
b1_c26_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (M36 + right amount)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Verifique virtud CL 26 = TEMPLANZA dia 1 v2 (NUEVO BLOQUE Cl 26-30) por numero de clase',
    'NOMBRE VISIBLEMENTE la TRANSICION PRUDENCIA v2 (Cl 21-25) -> TEMPLANZA v2 dia 1 (Cl 26-30) en el VATS al inicio - no implicita',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica lexico-estructural - mismo criterio que Cl 14-25)',
    'RECIBI el PASE escrito de Juan Diego (Cl 25 Grammar M34 prices) para el Peer Teacher',
    'Conduje Hot Topic "Dress for the Role, Not the Show" con requirements en tablero',
    'Conduje The Professional Wardrobe Briefing (3 contextos profesionales: client / internal / field, DE PIE, M36 preview)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 23 THE CALM PROFESSIONAL SELF I CHOOSE Draft 1 EN CLASE (anti-fraude IA; primera pagina del capitulo TEMPLANZA hacia Final Cl 44)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica + transicion virtud',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (jueves 04/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 27 jueves',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase26_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 26 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | NUEVO BLOQUE TEMPLANZA v2 DIA 1 (TRANSICION VISIBLE)',
    'Aplicacion oral de M36 Describing Clothing: Hot Topic "Dress for the Role, Not the Show" + Simulacion "The Professional Wardrobe Briefing" (3 contextos) + Page 23 THE CALM PROFESSIONAL SELF I CHOOSE Draft 1 anti-fraude (primera pagina del capitulo TEMPLANZA hacia Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + TRANSICION PRUDENCIA v2 (Cl 21-25) -> TEMPLANZA v2 dia 1 (Cl 26-30) nombrada VISIBLEMENTE en el VATS (no implicita) (SIN texto Heiiu - gramatica lexico-estructural, mismo criterio que Cl 14-25; anuncio Final Cl 44 SOLO como hecho de cronograma; M35 NO existe en el A2 Book - el libro salta de M34 a M36)',
    b1_c26_c_act, b1_c26_c_deliv, b1_c26_c_eval, S,
)
print('OK: B1_Clase26_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 26 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase26_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase26_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase26_GRAMMAR_GUIA.pdf')

b1_c26_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - M33/M34 reciclados) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS TRANSICION PRUDENCIA v2 -> TEMPLANZA v2 dia 1 (NUEVO BLOQUE Cl 26-30) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M36 Vocab Ropa p.302 + Vocab Colores p.303 + Guia 1 p.304 (adj antes del noun, sin plural) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M36 (zonas WRONG/RIGHT: adj antes del noun, sin plural, dark/light) - DE PIE', '16 min'),
    ('LIBRO M36 (cont.) Ejemplos p.305 + "dark/light" modificador + SORTING fisico (clothing/colors/modifier/verb) + HISTORIA INTERACTIVA absurda profesional - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP (tarjeta "ADJ-BEFORE-NOUN") + WARDROBE WALK / DRESS-UP STATION + STATION ROTATION 3 estaciones - DE PIE', '12 min'),
    ('TEMPERANCE PODIUM CEREMONY (3 contextos profesionales: client meeting / internal presentation / field work) + SPEED DRILL DE PIE', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea + Anuncio Cl 27 (M37, M35 NO existe) + Anuncio Final Cl 44 + Cierre', '14 min'),
]
b1_c26_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check (M33 + M34 reciclados)',
    'Foto del tablero - FRASE DEL DIA + M36 esquema (Vocab Ropa / Vocab Colores / Guia 1 reglas)',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico (clothing/colors/modifier/verb) + Historia interactiva absurda + Human-Sentence Line-up (con tarjeta "ADJ-BEFORE-NOUN") + Wardrobe Walk + Station Rotation',
    'Foto/video de la TEMPERANCE PODIUM CEREMONY (3 contextos profesionales con el AMOUNT correcto)',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 25 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'CONFIRMASTE que nombraste VISIBLEMENTE la TRANSICION PRUDENCIA v2 -> TEMPLANZA v2 dia 1 en el VATS (no implicita)',
    'Cuantas veces te preguntaron resultado del midterm o como sera el Final y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Cl 44 Final como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio Cl 27 jueves = M37 (siguiente modulo existente; M35 NO existe)',
]
b1_c26_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas/tiras para board race, sorting (clothing/colors/modifier/verb), human-line-up (con tarjeta "ADJ-BEFORE-NOUN"), wardrobe walk / dress-up station y stations ANTES',
    'PREPARE el TEMPERANCE PODIO en el tablero ANTES de clase (3 contextos: client / internal / field)',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up + podium)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 26 = TEMPLANZA dia 1 v2 (NUEVO BLOQUE Cl 26-30) por numero de clase',
    'NOMBRE VISIBLEMENTE la TRANSICION PRUDENCIA v2 (Cl 21-25) -> TEMPLANZA v2 dia 1 (Cl 26-30) en el VATS al inicio - no implicita',
    'Cubri M36 "What Are You Wearing? / Describing Clothing" DESDE EL LIBRO (A2 Book modulo p.301; Vocab 1 Prendas p.302; Vocab 2 Colores p.303; Guia 1 La Ropa p.304; Ejemplos Adjetivos p.305; Ejercicios Adjetivos p.306) citando reglas',
    'Explique las 3 reglas del libro: (1) "I have X" / "I am wearing X" / (2) ADJ siempre ANTES del NOUN, NUNCA cambia de forma (no plural) / (3) "dark X" / "light X" - primer adj modifica al segundo',
    'Reforce: ADJ va ANTES del NOUN (no como en espanol); ADJ NO toma plural ("red cars" no "reds cars"); "dark/light" no "clear/obscure"',
    'CONFIRME que M35 NO existe en el A2 Book (el libro salta de M34 a M36) - verificado verbatim - patron consistente con M19/M25/M31',
    'NO ensene M37 (es Cl 27) ni Third Conditional / Could-Should have',
    'NO re-ensene M34 (cerrado Cl 25 - solo reciclaje breve) ni M33 (cerrado Cl 24)',
    'NO use texto Heiiu (gramatica lexico-estructural - mismo criterio que Cl 14-25)',
    'Conduje BOARD RACE M36 (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases profesionales)',
    'Conduje SORTING fisico por categoria (clothing / colors / modifier "dark-light" / verb "have-wearing")',
    'Conduje HISTORIA INTERACTIVA absurda profesional (narras + pausa + cohorte agrega EN VOZ ALTA M36 form, NO huecos)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjeta "ADJ-BEFORE-NOUN" (alguien la sostiene SIEMPRE)',
    'Conduje WARDROBE WALK / DRESS-UP STATION (tarjetas fisicas de prendas + colores)',
    'Conduje STATION ROTATION 3 estaciones ("I am wearing" / "He/She has" / "dark-light + color")',
    'Conduje TEMPERANCE PODIUM CEREMONY (3 contextos profesionales: client meeting / internal presentation / field work; cadena con coro "Confirmed - the right amount on purpose!")',
    'Conduje SPEED DRILL DE PIE (cadena form-on-command + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 19/23)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + transicion virtud + M35 NO existe',
    'En Tarea explique el por que + due date explicito (jueves 04/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 27 jueves (M37 p.307+; M35 NO existe - el libro salta M34 -> M36 - confirmar verbatim)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase26_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 26 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M36 DESCRIBING CLOTHING (M35 NO EXISTE) | NUEVO BLOQUE TEMPLANZA v2 DIA 1 (TRANSICION VISIBLE)',
    'A2 Book M36 "What Are You Wearing? / Describing Clothing" (modulo p.301; Vocabulario 1 Prendas de Vestir p.302; Vocabulario 2 Los Colores p.303; Guia 1 La Ropa p.304; Ejemplos Adjetivos p.305; Ejercicios Adjetivos p.306) + Board Race + Walking Transformation + Sorting fisico (clothing/colors/modifier/verb) + Historia interactiva absurda profesional + Human-Sentence Line-up (tarjeta "ADJ-BEFORE-NOUN") + Wardrobe Walk / Dress-Up Station + Station Rotation + TEMPERANCE PODIUM CEREMONY (3 contextos: client meeting / internal presentation / field work) + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + TRANSICION PRUDENCIA v2 (Cl 21-25) -> TEMPLANZA v2 dia 1 (Cl 26-30) nombrada VISIBLEMENTE en el VATS (no implicita) (M35 NO existe - el libro salta de M34 a M36; SIN texto Heiiu - gramatica lexico-estructural, mismo criterio que Cl 14-25; anuncio Final Cl 44 SOLO como hecho de cronograma; Cl 27 jueves = M37 p.307+ a confirmar verbatim)',
    b1_c26_g_act, b1_c26_g_deliv, b1_c26_g_eval, S,
)
print('OK: B1_Clase26_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para miercoles 03/06 B1 MASTERY Cl 26:')
print('  - B1/B1_Clase26_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase26_CONV_REPORTE.pdf')
print('  - B1/B1_Clase26_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase26_GRAMMAR_REPORTE.pdf')
