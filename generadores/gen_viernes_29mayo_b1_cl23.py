#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 23 (viernes 29/05/2026) — POST-MIDTERM:
- Bloque 1 CONV (Danna, va PRIMERO): Hot Topic POST-MIDTERM "What Worked
  in the Room Yesterday?" (sin nombres, sin notas, TYPES + HOW MANY) +
  Simulacion "The Quarterly Briefing" (integra superlativos M28 + medidas
  M29 + cantidades M30 + preview "how many" M32) + Page 21 MY OPEN ROAD /
  WHERE I GO FROM HERE Draft 1 (escritura en clase post-midterm, mira al
  Final Cl 44) + Frase del Dia + PRUDENCIA dia 3 v2.
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M32
  "How Many People Are There?" / Specifying Countable Quantities (modulo
  p.273; Vocabulario 1 p.274; Guia 1 "How many?" p.275; Practica Verbal 1
  p.277; Respuestas p.278; Practica Verbal 2 p.279; Respuestas p.280;
  Practica Verbal 3 p.281; Respuestas p.282) + Podium Ceremony "How Many
  ___ ?" + Historia interactiva absurda profesional + Frase del Dia +
  PRUDENCIA dia 3 v2.
  (M31 NO existe en el A2 Book — el libro salta de M30 directamente a M32;
  verificado verbatim contra el libro; patron consistente con M19/M25 ya
  saltados.)
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-22: gramatica
  estructural, no narrativa).
- Anuncio Cl 24 lunes 01/06 = M33 "How Much Money Do You Have?" /
  Uncountable Quantities (pareja de M32).
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin
  nota/criterios — eso es coordinacion).
- Profesor NUNCA comunica resultados/notas del midterm de ayer Cl 22; si
  alguien pregunta: "Coordination handles results — not me. Focus on what
  comes next."
- Tarea fin de semana: due lunes 01/06 antes 7AM, 45-60 min (extra por
  fin de semana, dentro de regla), NO fragmentada.
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
# B1 Cl 23 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase23_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase23_CONV_GUIA.pdf'),
)
print('OK: B1_Clase23_CONV_GUIA.pdf')

b1_c23_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - preparacion midterm Cl 22, NO resultado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS PRUDENCIA dia 3 (v2) - how many honest steps al Final Cl 44', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 22 Grammar post-midterm)', '7 min'),
    ('HOT TOPIC POST-MIDTERM - "What Worked in the Room Yesterday?" (sin nombres, sin notas, TYPES + HOW MANY)', '17 min'),
    ('SIMULACION - "The Quarterly Briefing" (DE PIE, profesional, integra M28 superlativos + M29 medidas + M30 cantidades + M32 preview how many)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 21 - MY OPEN ROAD / WHERE I GO FROM HERE Draft 1 (escritura en clase post-midterm, mira al Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea fin de semana + Anuncio Cl 24 + Anuncio Final + Cierre', '7 min'),
]
b1_c23_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check (preparacion, NO resultado)',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE post-midterm de Juan Diego)',
    'PASE recibido de Juan Diego (archivado - observaciones post-midterm)',
    'Foto/video de The Quarterly Briefing simulacion',
    'Foto/video Mini-Pitch',
    'N Paginas 21 MY OPEN ROAD / WHERE I GO FROM HERE DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron preparacion (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Cuantas veces te preguntaron resultado del midterm y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Cl 44 Final como hecho de cronograma (sin nota/criterios)',
]
b1_c23_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase (verifica preparacion midterm, NO resultado)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (how many honesto)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique NADA de resultados/notas/criterios del midterm Cl 22 (exclusivo coordinacion)',
    'Si alguien pregunto resultado del midterm respondi "Coordination handles results — not me. Focus on what comes next." y segui',
    'Verifique virtud CL 23 = PRUDENCIA dia 3 v2 (por numero de clase)',
    'Hile PRUDENCIA en VATS como dia 3 v2 post-midterm (how many honest steps al Final — sin inflar, sin esconder)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde con M32)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-22)',
    'RECIBI el PASE escrito de Juan Diego (Cl 22 Grammar post-midterm) para el Peer Teacher',
    'Conduje Hot Topic POST-MIDTERM "What Worked in the Room Yesterday?" — SIN nombres, SIN notas, SIN comparar personas',
    'Cohorte hablo de TIPOS (no de quien) y nombro HOW MANY cosas concretas para el Final',
    'Conduje The Quarterly Briefing (5 puntos: superlativos + medidas + cantidades + how many + cierre honesto, DE PIE)',
    'Simulacion fue PROFESIONAL/realista cotidiana (no familiar ni fantasiosa)',
    'Conduje escritura Page 21 MY OPEN ROAD / WHERE I GO FROM HERE Draft 1 EN CLASE (anti-fraude IA; alimenta segunda mitad del proyecto hacia Final Cl 44)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica + nota M31 NO existe',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (lunes 01/06 antes 7AM)',
    'Tarea es 45-60 min (extra por fin de semana, dentro de regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo" (tienen sabado y domingo)',
    'Anuncie Cl 24 lunes',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase23_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 23 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | POST-MIDTERM | FRASE DEL DIA (Goldlist retirado)',
    'POST-MIDTERM (Cl 22 jueves fue ayer): Hot Topic "What Worked in the Room Yesterday?" (sin nombres / sin notas / TYPES + HOW MANY) + Simulacion "The Quarterly Briefing" (integra M28 superlativos + M29 medidas + M30 cantidades + M32 preview how many) + Page 21 MY OPEN ROAD / WHERE I GO FROM HERE Draft 1 anti-fraude (primera pagina post-midterm, mira al Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + PRUDENCIA dia 3 v2 (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14-22; profesor NUNCA comunica resultados/notas/criterios del midterm — exclusivo coordinacion; anuncio Final Cl 44 SOLO como hecho de cronograma)',
    b1_c23_c_act, b1_c23_c_deliv, b1_c23_c_eval, S,
)
print('OK: B1_Clase23_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 23 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase23_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase23_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase23_GRAMMAR_GUIA.pdf')

b1_c23_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - preparacion midterm, NO resultado) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS PRUDENCIA dia 3 v2 (how many honest steps al Final) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna - Cl 23 Conv post-midterm) - DE PIE', '7 min'),
    ('LIBRO M32 How Many? (modulo p.273; Guia 1 p.275) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M32 how many + plural / how much + uncountable / there are vs there is plural / a few sin "of" - DE PIE', '16 min'),
    ('LIBRO M32 (cont.) Respuestas Practica Verbal + SORTING fisico countable plural vs uncountable (preview M33) + Historia interactiva ABSURDA cotidiana profesional - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP (con tarjeta "HOW MANY") + STATION ROTATION - 3 estaciones (there are / do you have / want-need) - DE PIE', '12 min'),
    ('PODIUM CEREMONY "How Many ___ ?" + SPEED DRILL DE PIE - cadena form-on-command + coro rapido', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea fin de semana + Anuncio Cl 24 (M33) + Anuncio Final Cl 44 + Cierre', '14 min'),
]
b1_c23_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check (preparacion, NO resultado)',
    'Foto del tablero - FRASE DEL DIA + M32 esquema (how many + plural contable / respuestas numero / a few / many / a lot of)',
    'Foto/video del PEER TEACHER usando PASE de Danna (post-midterm)',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico countable plural vs uncountable + Historia interactiva absurda profesional + Human-Sentence Line-up (con tarjeta "HOW MANY") + Station Rotation',
    'Foto/video del PODIUM CEREMONY',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron preparacion (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Cuantas veces te preguntaron resultado del midterm y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Cl 44 Final como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio M33 lunes Cl 24 (M31 NO existe — el libro salta M30 -> M32)',
]
b1_c23_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Verifique con mis propios ojos que M31 NO aparece en el A2 Book (el libro salta M30 p.272 -> M32 p.273)',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase (verifica preparacion, NO resultado)',
    'PREPARE tarjetas/tiras para board race, sorting countable/uncountable, human-line-up (con tarjeta "HOW MANY") y stations ANTES',
    'PREPARE la HISTORIA INTERACTIVA absurda cotidiana profesional con pausas marcadas (cohorte agrega EN VOZ ALTA, no huecos)',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up + podium)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique NADA de resultados/notas/criterios del midterm Cl 22 (exclusivo coordinacion)',
    'Si alguien pregunto resultado del midterm respondi "Coordination handles results — not me. Focus on what comes next." y segui el libro',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 23 = PRUDENCIA dia 3 v2 (por numero de clase)',
    'Cubri M32 "How Many People Are There?" / Countable Quantities DESDE EL LIBRO (A2 Book modulo p.273; Vocab p.274; Guia 1 p.275; Practica Verbal 1 p.277; Resp p.278; PV2 p.279; Resp p.280; PV3 p.281; Resp p.282) citando reglas verbatim',
    'Explique estructura: HOW MANY + sustantivo CONTABLE PLURAL + (do/does + sujeto + verbo)? / HOW MANY + plural + are there?',
    'Explique respuestas: NUMERO ("there are 7 nurses"; "1 -> there IS 1 secretary"), a few (~3-5), many / a lot of / lots of',
    'Reforce: "people" es plural irregular -> "there ARE people", nunca "there is"; "a few" va SIN "of"; "how much" NO con contable plural',
    'CONFIRME que M31 NO existe en el A2 Book (el libro salta de M30 p.272 a M32 p.273) - verificado verbatim',
    'CONFIRME patron M19/M25/M31 ya saltados consistentemente (mismo criterio Diana 19/05 + 25/05)',
    'NO ensene M33 "How Much Money Do You Have?" / Uncountable (es Cl 24 lunes) ni Third Conditional / Could-Should have',
    'NO re-ensene M28 (Cl 19) ni M29 (Cl 20) ni M30 (Cl 21) - solo contraste integrado breve',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-22)',
    'Conduje BOARD RACE M32 (2 equipos en el tablero)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases profesionales)',
    'Conduje SORTING fisico countable plural vs uncountable (preview M33 lunes)',
    'Conduje HISTORIA INTERACTIVA absurda cotidiana profesional con pausas (cohorte agrego EN VOZ ALTA, NO huecos para llenar)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjeta "HOW MANY" (alguien la sostiene SIEMPRE)',
    'Conduje STATION ROTATION 3 estaciones (there are / do/does have / want-need)',
    'Conduje PODIUM CEREMONY "How Many ___ ?" (cadena con coro "Confirmed - how many indeed!")',
    'Conduje SPEED DRILL DE PIE (cadena form-on-command + coro rapido)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 19 y Cl 18)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + nota M31 NO existe',
    'En Tarea explique el por que + due date explicito (lunes 01/06 antes 7AM)',
    'Tarea es 45-60 min (extra por fin de semana, dentro de regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo" (tienen sabado y domingo enteros)',
    'Anuncie siguiente modulo existente del A2 Book para Cl 24 lunes (M31 NO existe; M30 fue Cl 21; M32 fue hoy; sigue M33 "How Much Money Do You Have?" p.283+ - confirmar verbatim)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase23_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 23 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | POST-MIDTERM | M32 HOW MANY (M31 NO EXISTE)',
    'A2 Book M32 "How Many People Are There?" / Specifying Countable Quantities (modulo p.273; Vocab p.274; Guia 1 "How many?" p.275; Practica Verbal 1 p.277; Respuestas p.278; PV2 p.279; Resp p.280; PV3 p.281; Resp p.282) + Board Race + Walking Transformation + Sorting fisico countable plural vs uncountable (preview M33 lunes) + Historia interactiva ABSURDA cotidiana profesional con pausas (cohorte agrega EN VOZ ALTA, NO huecos) + Human-Sentence Line-up (con tarjeta "HOW MANY") + Station Rotation + Podium Ceremony "How Many ___ ?" + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + PRUDENCIA dia 3 v2 (M31 NO EXISTE - el libro salta de M30 p.272 directamente a M32 p.273; verificado verbatim; patron consistente con M19/M25 ya saltados; SIN texto Heiiu - gramatica estructural; profesor NUNCA comunica resultados del midterm Cl 22 — exclusivo coordinacion; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 24 lunes = M33 "How Much Money Do You Have?" / Uncountable Quantities pareja de M32)',
    b1_c23_g_act, b1_c23_g_deliv, b1_c23_g_eval, S,
)
print('OK: B1_Clase23_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para viernes 29/05 B1 MASTERY Cl 23 (POST-MIDTERM):')
print('  - B1/B1_Clase23_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase23_CONV_REPORTE.pdf')
print('  - B1/B1_Clase23_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase23_GRAMMAR_REPORTE.pdf')
