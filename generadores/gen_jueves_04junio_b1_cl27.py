#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 27 (jueves 04/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Describir Personas
  (Hot Topic "What Does a Professional Look Like in My Industry?" +
  Simulacion "The Witness Description") + Project THE TEAM PORTRAIT Draft 1
  (escritura en clase, alimenta Final Cl 44) + Frase del Dia + TEMPLANZA
  dia 2 v2
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M37 "What
  Do You Look Like?" / Describing People (modulo p.307; Vocabulario 1
  Partes del Cuerpo p.308; Vocabulario 2 Adjetivos Personales p.309; Guia 1
  "What Are You Like?" p.310; Ejemplos p.311; Ejercicios p.312) + Podium
  Ceremony + Historia interactiva absurda profesional + Frase del Dia +
  TEMPLANZA dia 2 v2
  (M35 NO existe en el A2 Book — el libro salta de M34 a M36).
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-26: gramatica
  estructural/lexica, no narrativa).
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin
  nota/criterios — eso es coordinacion).
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
# B1 Cl 27 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase27_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase27_CONV_GUIA.pdf'),
)
print('OK: B1_Clase27_CONV_GUIA.pdf')

b1_c27_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 26 Conv)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS TEMPLANZA dia 2 (v2)', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 26 Grammar)', '7 min'),
    ('HOT TOPIC - What Does a Professional Look Like in My Industry? (descripcion de personas, oral)', '17 min'),
    ('SIMULACION - The Witness Description (DE PIE, profesional, sin chisme/sin juicio)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP - THE TEAM PORTRAIT Draft 1 (escritura en clase anti-fraude, alimenta Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Anuncio Cl 28 + Anuncio Final + Cierre', '7 min'),
]
b1_c27_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Witness Description simulacion',
    'Foto/video Mini-Pitch',
    'N THE TEAM PORTRAIT DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 26 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
]
b1_c27_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (look like / to be / to have)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Verifique virtud CL 27 = TEMPLANZA dia 2 v2 (por numero de clase; bloque Cl 26-30)',
    'Hile TEMPLANZA en VATS como dia 2 del bloque (que version de ti SE VE: calm, steady, sin dramatizar la mejora)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-26)',
    'RECIBI el PASE escrito de Juan Diego (Cl 26 Grammar) para el Peer Teacher',
    'Conduje Hot Topic "What Does a Professional Look Like in My Industry?" con requirements en tablero (5+ "to be"/"to have" + 3+ adjetivos personales + 1+ modificador, sin juicio/sin chisme)',
    'Conduje The Witness Description (DE PIE, describir fisicamente a alguien del trabajo para identificacion profesional, sin chisme/sin juicio)',
    'Simulacion fue PROFESIONAL/realista cotidiana (no fantasiosa)',
    'Conduje escritura THE TEAM PORTRAIT Draft 1 EN CLASE (anti-fraude IA; alimenta Final Cl 44; sin chisme, sin juicio - solo descripcion limpia)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (viernes 05/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 28 viernes (siguiente modulo existente A2 Book)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase27_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 27 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de Describir Personas: Hot Topic "What Does a Professional Look Like in My Industry?" + Simulacion "The Witness Description" + Project THE TEAM PORTRAIT Draft 1 anti-fraude (alimenta Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + TEMPLANZA dia 2 v2 (SIN texto Heiiu - gramatica estructural/lexica, mismo criterio que Cl 14-26; anuncio Final Cl 44 SOLO como hecho de cronograma; sin chisme/sin juicio - descripcion limpia)',
    b1_c27_c_act, b1_c27_c_deliv, b1_c27_c_eval, S,
)
print('OK: B1_Clase27_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 27 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase27_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase27_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase27_GRAMMAR_GUIA.pdf')

b1_c27_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS TEMPLANZA dia 2 (v2) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna) - DE PIE', '7 min'),
    ('LIBRO M37 Uso idiomatico de "like" (modulo p.307; Guia 1 p.310) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M37 look like / to be / to have / modificadores - DE PIE', '16 min'),
    ('LIBRO M37 (cont.) Describir con "to be" + "to have" + modificadores + SORTING fisico por categoria (body part / personal adj / modifier / use of "like") + HISTORIA INTERACTIVA absurda profesional - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP (con tarjeta "LIKE") + STATION ROTATION - 3 estaciones (uso de "like" / "to be"+"to have" / modificadores) - DE PIE', '12 min'),
    ('PODIUM CEREMONY + SPEED DRILL DE PIE - 4 piezas en cadena/coro', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea + Anuncio Cl 28 + Anuncio Final + Cierre', '14 min'),
]
b1_c27_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M37 uso de "like" / "to be" / "to have" / modificadores',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico por categoria + Human-Sentence Line-up (con tarjeta "LIKE") + Station Rotation',
    'Foto/video del PODIUM CEREMONY',
    'Foto/video de la HISTORIA INTERACTIVA absurda profesional (nuevo auditor)',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 26 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
]
b1_c27_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas/tiras para board race, sorting, human-line-up (con tarjeta "LIKE") y stations ANTES',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up + podium)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/midterm/final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 27 = TEMPLANZA dia 2 v2 (por numero de clase; bloque Cl 26-30)',
    'Cubri M37 The Description DESDE EL LIBRO (A2 Book modulo p.307; Vocab 1 partes del cuerpo p.308; Vocab 2 adjetivos personales p.309; Guia 1 "What Are You Like?" p.310; Ejemplos p.311; Ejercicios p.312) citando reglas',
    'Explique los 3 trabajos de "like": gustar (what do you LIKE?) / personalidad (what ARE you LIKE?) / apariencia (what do you LOOK LIKE?), mas "como" comparativo + "how are you" para estado de animo',
    'Explique describir con "to be" + adjetivo personal vs "to have" + parte del cuerpo (NO mezclar)',
    'Explique modificadores "very" (amplifica) / "somewhat" (minimiza) UNO A LA VEZ - NUNCA juntos',
    'CONFIRME que M35 NO existe en el A2 Book (el libro salta de M34 a M36) - verificado verbatim. Patron consistente con M19/M25/M31',
    'NO ensene M38 "Order of Adjectives" (es Cl 28) ni conditional avanzado / modal perfect / passive avanzado',
    'NO re-ensene M36 (cerrado Cl 26 - solo contraste breve) ni M34 (cerrado Cl 25) ni M33 (cerrado Cl 24) ni M32 (cerrado Cl 23)',
    'NO use texto Heiiu (gramatica estructural/lexica - mismo criterio que Cl 14-26)',
    'Conduje BOARD RACE uso de "like" (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases profesionales)',
    'Conduje SORTING fisico por categoria (body part / personal adj / modifier / use of "like")',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjeta "LIKE" (alguien la sostiene cuando es pregunta de apariencia/personalidad)',
    'Conduje STATION ROTATION 3 estaciones (uso de "like" / "to be"+adj / "to have"+body)',
    'Conduje HISTORIA INTERACTIVA absurda profesional (nuevo auditor) tipo Cl 1: profe narra + pausa + cohorte repite + cohorte agrega - SIN huecos para llenar',
    'Conduje PODIUM CEREMONY (cadena con coro "Confirmed - described!")',
    'Conduje SPEED DRILL DE PIE (cadena form-on-command + coro pregunta-tipo)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 19 y Cl 26)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'En Tarea explique el por que + due date explicito (viernes 05/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 28 viernes (M35 no existe; M36 fue Cl 26; M37 fue hoy; sigue M38 "Order of Adjectives" p.313+ - confirmar verbatim)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase27_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 27 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M37 WHAT DO YOU LOOK LIKE? (M35 NO EXISTE)',
    'A2 Book M37 "What Do You Look Like?" / Describing People (modulo p.307; Vocab 1 partes del cuerpo p.308; Vocab 2 adjetivos personales p.309; Guia 1 "What Are You Like?" p.310; Ejemplos p.311; Ejercicios p.312) + Board Race uso de "like" + Walking Transformation + Sorting fisico por categoria + Human-Sentence Line-up (con tarjeta "LIKE") + Station Rotation + Historia interactiva absurda profesional (nuevo auditor) + Podium Ceremony + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + TEMPLANZA dia 2 v2 (M35 NO existe - el libro salta de M34 a M36; SIN texto Heiiu - gramatica estructural/lexica, mismo criterio que Cl 14-26; anuncio Final Cl 44 SOLO como hecho de cronograma)',
    b1_c27_g_act, b1_c27_g_deliv, b1_c27_g_eval, S,
)
print('OK: B1_Clase27_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para jueves 04/06 B1 MASTERY Cl 27:')
print('  - B1/B1_Clase27_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase27_CONV_REPORTE.pdf')
print('  - B1/B1_Clase27_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase27_GRAMMAR_REPORTE.pdf')
