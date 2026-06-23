#!/usr/bin/env python3
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 24 (lunes 01/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de "how much" + uncountable
  (Hot Topic "How Much Do I Really Have?" + Simulacion "The Resource Audit") +
  Page 22 MY HONEST RESOURCES Draft 1 (segunda pagina post-midterm, escritura
  en clase) + Frase del Dia + PRUDENCIA dia 4 v2
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M33
  "How Much Money Do You Have?" / Specifying Uncountable Quantities (modulo
  p.283; Vocabulario 1 p.284; Guia 1 "How much?" p.285; Practica Verbal 1
  p.287; Respuestas p.288; Practica Verbal 2 p.289; Respuestas p.290; Practica
  Verbal 3 p.291; Respuestas p.292) + Sorting countable/uncountable +
  Historia interactiva absurda profesional + Podium Ceremony +
  Frase del Dia + PRUDENCIA dia 4 v2
  (M31 NO existe en el A2 Book — confirmado viernes Cl 23; el libro salta de
  M30 a M32; M32 fue Cl 23; M33 hoy; M34 sera Cl 25 a confirmar verbatim).
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-23: gramatica estructural,
  no narrativa).
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin nota/criterios
  — eso es coordinacion). Limite midterm: "Coordination handles results — not me."
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
# B1 Cl 24 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase24_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase24_CONV_GUIA.pdf'),
)
print('OK: B1_Clase24_CONV_GUIA.pdf')

b1_c24_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea fin de semana = Page 21 polish + grabo + listening + reading)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS PRUDENCIA dia 4 (v2)', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 23 Grammar M32)', '7 min'),
    ('HOT TOPIC - How Much Do I Really Have? (uncountable: time/money/energy/attention/information/coffee/work, oral)', '17 min'),
    ('SIMULACION - The Resource Audit (DE PIE, uncountable + cantidad sin numero, profesional)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 22 - MY HONEST RESOURCES Draft 1 (escritura en clase anti-fraude, segunda pagina post-midterm)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Anuncio Cl 25 + Anuncio Final + Cierre', '7 min'),
]
b1_c24_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego - Cl 23 M32)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Resource Audit simulacion',
    'Foto/video Mini-Pitch',
    'N Paginas 22 MY HONEST RESOURCES DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea fin de semana (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Cuantas veces te preguntaron resultado del midterm y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Cl 44 Final como hecho de cronograma (sin nota/criterios)',
]
b1_c24_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (how much + uncountable)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Cuando me preguntaron resultado del midterm respondi "Coordination handles results — not me. Focus on what comes next." y segui',
    'Verifique virtud CL 24 = PRUDENCIA dia 4 v2 (por numero de clase)',
    'Hile PRUDENCIA en VATS como dia 4 del bloque (cantidad real uncountable: no inflar, no esconder)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-23)',
    'RECIBI el PASE escrito de Juan Diego (Cl 23 Grammar M32) para el Peer Teacher',
    'Conduje Hot Topic "How Much Do I Really Have?" con requirements en tablero (UNCOUNTABLE ONLY)',
    'Conduje The Resource Audit (5-6 puntos uncountable, respuestas SIN numero "a little/a lot/some/not much/enough/too much", DE PIE)',
    'Simulacion fue PROFESIONAL/realista (no familiar ni fantasiosa)',
    'Conduje escritura Page 22 MY HONEST RESOURCES Draft 1 EN CLASE (anti-fraude IA; segunda pagina post-midterm, responde a Page 21)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica (M33 referencia paginas)',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (martes 02/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 25 martes',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase24_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 24 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de "how much" + UNCOUNTABLE: Hot Topic "How Much Do I Really Have?" + Simulacion "The Resource Audit" + Page 22 MY HONEST RESOURCES Draft 1 anti-fraude (segunda pagina post-midterm) + FRASE DEL DIA + PASE a Juan Diego + PRUDENCIA dia 4 v2 (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14-23; anuncio Final Cl 44 SOLO como hecho de cronograma; limite midterm "Coordination handles results")',
    b1_c24_c_act, b1_c24_c_deliv, b1_c24_c_eval, S,
)
print('OK: B1_Clase24_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 24 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase24_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase24_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase24_GRAMMAR_GUIA.pdf')

b1_c24_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS PRUDENCIA dia 4 (v2) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna - Cl 24 Conv) - DE PIE', '7 min'),
    ('LIBRO M33 How Much? (modulo p.283; Guia 1 p.285) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M33 how much + uncountable + respuesta UNIDAD o cualitativa - DE PIE', '16 min'),
    ('LIBRO M33 (cont.) Respuestas Practica Verbal + SORTING fisico COUNTABLE M32 vs UNCOUNTABLE M33 + HISTORIA INTERACTIVA absurda profesional - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP (con tarjeta "HOW MUCH") + STATION ROTATION - 3 estaciones - DE PIE', '12 min'),
    ('PODIUM CEREMONY "How Much ___ ?" + SPEED DRILL DE PIE - cadena form-on-command + coro rapido', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea + Anuncio Cl 25 (M34) + Anuncio Final + Cierre', '14 min'),
]
b1_c24_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M33 esquema (how much + uncountable / respuestas unidad o cualitativa)',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico COUNTABLE M32 vs UNCOUNTABLE M33 + Historia interactiva absurda profesional + Human-Sentence Line-up (con tarjeta "HOW MUCH") + Station Rotation',
    'Foto/video del PODIUM CEREMONY',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea fin de semana (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Cuantas veces te preguntaron resultado del midterm y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Cl 44 Final como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio M34 martes Cl 25 (M31 NO existe, ya confirmado viernes)',
]
b1_c24_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas/tiras para board race, sorting COUNTABLE M32 vs UNCOUNTABLE M33, human-line-up (con tarjeta "HOW MUCH") y stations ANTES',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up + podium)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Cuando me preguntaron resultado del midterm respondi "Coordination handles results — not me. Focus on what comes next." y segui el libro',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 24 = PRUDENCIA dia 4 v2 (por numero de clase)',
    'Cubri M33 "How Much Money Do You Have?" DESDE EL LIBRO (A2 Book modulo p.283; Vocabulario 1 p.284; Guia 1 "How much?" p.285; Practica Verbal 1 p.287; Respuestas p.288; Practica Verbal 2 p.289; Respuestas p.290; Practica Verbal 3 p.291; Respuestas p.292) citando reglas',
    'Explique estructura del libro: "how much" + sustantivo UNCOUNTABLE; respuestas con UNIDAD ("1 liter of milk / 3 kilos of pasta / 300 pesos") o cualitativa ("a bit of / a little / a lot of / lots of")',
    'Reforce: "there IS" + uncountable (NO "there are" salvo con UNIDAD plural "there are 4 liters of"); "a few" es contable, uncountable usa "a little" / "a bit of"',
    'Conduje CONTRASTE breve con M32 viernes (countable plural "how many") sin re-ensenar M32',
    'CONFIRME que M31 NO existe en el A2 Book (ya confirmado viernes Cl 23 - el libro salta de M30 a M32)',
    'NO ensene M34 (es Cl 25) ni Third Conditional / Could-Should have',
    'NO re-ensene M32 (Cl 23 - solo contraste breve) ni M28 (Cl 19) ni M29 (Cl 20) ni M30 (Cl 21)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-23)',
    'Conduje BOARD RACE M33 (2 equipos en el tablero; incluye contraste M32 vs M33)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases profesionales uncountable)',
    'Conduje SORTING fisico COUNTABLE PLURAL (M32 viernes) vs UNCOUNTABLE (M33 hoy)',
    'Conduje HISTORIA INTERACTIVA absurda cotidiana profesional con uncountable (cohorte agrega EN VOZ ALTA en cada pausa, sin huecos para llenar)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjeta "HOW MUCH" (alguien la sostiene SIEMPRE)',
    'Conduje STATION ROTATION 3 estaciones (there is / do you have / want-need)',
    'Conduje PODIUM CEREMONY (cadena con coro "Confirmed - how much indeed!")',
    'Conduje SPEED DRILL DE PIE (cadena form-on-command + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 23 ~85%, Cl 19 ~85%, Cl 18 ~86%)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + paginas M33',
    'En Tarea explique el por que + due date explicito (martes 02/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 25 martes (M34 p.293+ - confirmar verbatim)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Recorde que manana Cl 25 cierra PRUDENCIA v2 con dia 5',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase24_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 24 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M33 HOW MUCH MONEY DO YOU HAVE? (M31 NO EXISTE)',
    'A2 Book M33 "How Much Money Do You Have?" / Specifying Uncountable Quantities (modulo p.283; Vocabulario 1 p.284; Guia 1 "How much?" p.285; Practica Verbal 1 p.287; Respuestas p.288; Practica Verbal 2 p.289; Respuestas p.290; Practica Verbal 3 p.291; Respuestas p.292) + Board Race + Walking Transformation + Sorting fisico COUNTABLE M32 vs UNCOUNTABLE M33 + Historia interactiva absurda profesional + Human-Sentence Line-up (con tarjeta "HOW MUCH") + Station Rotation + Podium Ceremony + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + PRUDENCIA dia 4 v2 (M31 NO existe - confirmado viernes Cl 23 - el libro salta de M30 a M32; M32 fue Cl 23; M33 hoy; M34 sera Cl 25 a confirmar verbatim; SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14-23; anuncio Final Cl 44 SOLO como hecho de cronograma; limite midterm "Coordination handles results")',
    b1_c24_g_act, b1_c24_g_deliv, b1_c24_g_eval, S,
)
print('OK: B1_Clase24_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para lunes 01/06 B1 MASTERY Cl 24:')
print('  - B1/B1_Clase24_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase24_CONV_REPORTE.pdf')
print('  - B1/B1_Clase24_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase24_GRAMMAR_REPORTE.pdf')
