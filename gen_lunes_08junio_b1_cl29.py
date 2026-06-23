#!/usr/bin/env python3
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 29 (lunes 08/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Possessive Pronouns as
  Objects (Hot Topic "Whose Is This? / What's Mine vs What's Ours?" +
  Simulacion "The Lost & Found Desk Returns") + Page 27 WHAT IS MINE IN
  THIS PROJECT / WHAT I CLAIM AUTHORSHIP OF Draft 1 (escritura en clase,
  alimenta segunda mitad del proyecto hacia Final Cl 44) + Frase del Dia +
  TEMPLANZA dia 4 v2
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M39
  "Mine, All Mine!" / Possessive Pronouns as Objects (modulo p.318+; Guia 1
  p.319 con tabla canonica; Ejemplos p.320; Ejercicios 1 p.321; Ejercicios
  2 p.322; Practice Guide p.323-325) — tabla canonica my->mine, your->yours,
  his->his (cuidado: misma forma), her->hers, our->ours, their->theirs;
  WHOSE como palabra de pregunta + Podium Ceremony "Right Possessive" +
  Historia interactiva absurda profesional "Whose is this?" + Frase del Dia
  + TEMPLANZA dia 4 v2
  (M40 NO existe en el A2 Book — el libro salta de M39 a M41; auditado
  verbatim linea 22871; patron consistente con M19/M25/M31/M35 ya saltados.)
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-28: gramatica
  estructural/sustitucion, no narrativa).
- Anuncio Cl 30 martes 09/06 = M41 "This Is Interesting!" / Participle
  Adjectives — verificado verbatim antes de clase (M40 NO existe).
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin
  nota/criterios — eso es coordinacion).
- Profesor NUNCA comunica resultados/notas/criterios del Final; si alguien
  pregunta: "Coordination handles results — not me. Focus on what comes
  next."
- Tarea Cl 29: due martes 09/06 antes 7AM, 30-45 min, NO fragmentada.
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
# B1 Cl 29 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase29_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase29_CONV_GUIA.pdf'),
)
print('OK: B1_Clase29_CONV_GUIA.pdf')

b1_c29_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 28 Conv = Page 26 Disciplined Cadence + audio + reading + TED listening)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS TEMPLANZA dia 4 (v2) - owning only what is truly yours: nombrar la propiedad limpia con MINE/YOURS/HIS/HERS/OURS/THEIRS', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 28 Grammar M38 Order of Adjectives)', '7 min'),
    ('HOT TOPIC - "Whose Is This? / What\'s Mine vs What\'s Ours?" (posesivos pronombres objeto en contexto profesional)', '17 min'),
    ('SIMULACION - "The Lost & Found Desk Returns" (DE PIE, profesional, reclamar/negar/preguntar propiedad con It\'s mine / It\'s hers / Whose is this?)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 27 - WHAT IS MINE IN THIS PROJECT / WHAT I CLAIM AUTHORSHIP OF Draft 1 (escritura en clase anti-fraude, alimenta segunda mitad hacia Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea Cl 29 + Anuncio Cl 30 (M41 - M40 NO existe) + Anuncio Final + Cierre', '7 min'),
]
b1_c29_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego Cl 28 Grammar M38)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Lost & Found Desk Returns simulacion (con objetos reales: chaqueta, llaves, esfero, cuaderno, mochila, etc.)',
    'Foto/video Mini-Pitch',
    'N Paginas 27 WHAT IS MINE IN THIS PROJECT / WHAT I CLAIM AUTHORSHIP OF DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 28 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio Cl 30 martes 09/06 = M41 "This Is Interesting!" / Participle Adjectives (M40 NO existe — auditado verbatim linea 22871 A2 Book)',
]
b1_c29_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE 8-10 objetos reales para Lost & Found Returns (chaqueta, llaves, esfero, cuaderno, botella, mochila, etc.)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (MINE/OURS/HERS como objetos + WHOSE pregunta)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui',
    'Verifique virtud CL 29 = TEMPLANZA dia 4 v2 (por numero de clase, Cl 26-30)',
    'Hile TEMPLANZA en VATS como dia 4 v2 (owning only what is truly yours: pronombre correcto + propiedad honesta, sin inflar)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza en el segundo bloque con M39)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-28)',
    'RECIBI el PASE escrito de Juan Diego (Cl 28 Grammar M38 Order of Adjectives) para el Peer Teacher',
    'Conduje Hot Topic "Whose Is This? / What\'s Mine vs What\'s Ours?" con requirements en tablero (6+ MINE/YOURS/HIS/HERS/OURS/THEIRS objetos + 2+ WHOSE)',
    'Conduje The Lost & Found Desk Returns (reclamar/negar/preguntar 6+ items con pronombres posesivos objeto, DE PIE)',
    'Simulacion fue PROFESIONAL/realista cotidiana (no familiar ni fantasiosa)',
    'Conduje escritura Page 27 WHAT IS MINE IN THIS PROJECT / WHAT I CLAIM AUTHORSHIP OF Draft 1 EN CLASE (anti-fraude IA; alimenta segunda mitad hacia Final Cl 44)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica (MINE/YOURS/OURS ya en boca del cohorte; patron mas comun: adjetivo en posicion de objeto)',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (martes 09/06 antes 7AM)',
    'Tarea es 30-45 min (regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 30 martes 09/06 = M41 "This Is Interesting!" / Participle Adjectives (M40 NO existe — auditado verbatim)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase29_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 29 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de Possessive Pronouns as Objects: Hot Topic "Whose Is This? / What\'s Mine vs What\'s Ours?" + Simulacion "The Lost & Found Desk Returns" (reclamar/negar/preguntar propiedad de 6+ items con MINE / YOURS / HIS / HERS / OURS / THEIRS como objetos + 2+ WHOSE questions) + Page 27 WHAT IS MINE IN THIS PROJECT / WHAT I CLAIM AUTHORSHIP OF Draft 1 anti-fraude (alimenta segunda mitad del proyecto hacia Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + TEMPLANZA dia 4 v2 (SIN texto Heiiu - gramatica estructural/sustitucion, mismo criterio que Cl 14-28; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 30 martes 09/06 = M41 "This Is Interesting!" / Participle Adjectives — M40 NO existe, auditado verbatim linea 22871 A2 Book)',
    b1_c29_c_act, b1_c29_c_deliv, b1_c29_c_eval, S,
)
print('OK: B1_Clase29_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 29 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase29_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase29_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase29_GRAMMAR_GUIA.pdf')

b1_c29_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 28 = M38 Order of Adjectives 12 frases + audio + reading + TED listening) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS TEMPLANZA dia 4 v2 (owning only what is truly yours: pronombre correcto en posicion de objeto, propiedad honesta) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna - Cl 29 Conv: adjetivo posesivo en posicion de objeto) - DE PIE', '7 min'),
    ('LIBRO M39 Mine, All Mine! / Possessive Pronouns as Objects (modulo p.318+; Guia 1 p.319 tabla canonica verbatim my->mine/your->yours/his->his/her->hers/our->ours/their->theirs; "Whose" como palabra de pregunta) + BOARD RACE (transformar adjetivo en posicion de objeto -> pronombre correcto) - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M39 con tarjetas yo/tu/el/ella/nos/ellos - zonas WRONG ("It is my") -> RIGHT ("It\'s mine") - DE PIE', '16 min'),
    ('LIBRO M39 (cont.) Ejemplos p.320 verbatim + SORTING fisico POSSESSIVE ADJECTIVES (antes del sustantivo) vs POSSESSIVE PRONOUNS (solos, como objeto) - 2 zonas + Historia interactiva ABSURDA profesional "Whose is this?" (cohorte responde EN VOZ ALTA mine/hers/ours/theirs en cada pausa) - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP con tarjetas "Subject + Verb + POSSESSIVE PRONOUN object" + STATION ROTATION - 3 estaciones (Whose questions / Mine-Yours-Ours statements / Comparativos con pronombres) - DE PIE', '12 min'),
    ('PODIUM CEREMONY "Right Possessive" + SPEED DRILL DE PIE - cadena Whose-pregunta + Pronombre-respuesta', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea Cl 29 + Anuncio Cl 30 (M41 - M40 NO existe) + Anuncio Final Cl 44 + Cierre', '14 min'),
]
b1_c29_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M39 tabla canonica + ejemplos pag 320',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation con tarjetas yo/tu/el/ella/nos/ellos (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico POSSESSIVE ADJECTIVES vs POSSESSIVE PRONOUNS (2 zonas) + Historia interactiva absurda profesional "Whose is this?" + Human-Sentence Line-up + Station Rotation',
    'Foto/video del PODIUM CEREMONY "Right Possessive"',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 28 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Cuantas veces te preguntaron resultado/criterios del Final y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio M41 martes Cl 30 09/06 (M40 NO existe - auditado verbatim linea 22871 A2 Book)',
]
b1_c29_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Verifique con mis propios ojos que el modulo anterior fue M38 (Cl 28); M40 NO existe (el libro salta de M39 a M41 verbatim, linea 22871 A2 Book)',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas-SUJETO grandes (yo/tu/el/ella/nosotros/ellos) + tarjetas-PRONOMBRE OBJETO (mine/yours/his/hers/ours/theirs) + tarjetas-ADJETIVO POSESIVO (my/your/his/her/our/their/its) + tarjetas-SUSTANTIVO (car/keys/book/printer/wallet/laptop/meeting room) para line-up, sorting y stations ANTES',
    'PREPARE la HISTORIA INTERACTIVA absurda cotidiana profesional "Whose is this?" con pausas marcadas (cohorte agrega EN VOZ ALTA mine/hers/ours/theirs en cada pausa, NO huecos)',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation con tarjetas-sujeto + line-up + podium + 2 zonas sorting)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui el libro',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 29 = TEMPLANZA dia 4 v2 (por numero de clase, Cl 26-30)',
    'Cubri M39 Mine, All Mine! / Possessive Pronouns as Objects DESDE EL LIBRO (A2 Book modulo p.318+; Guia 1 p.319 con tabla canonica; Ejemplos p.320; Ejercicios 1 p.321; Ejercicios 2 p.322; Practice Guide p.323-325) citando reglas verbatim',
    'Explique la tabla canonica del libro p.319: my->mine, your->yours, his->his (cuidado: misma forma), her->hers, our->ours, their->theirs, its->its',
    'Explique "whose" como palabra de pregunta (pronunciacion "jus" segun libro) y diferencia entre ADJETIVO (antes del sustantivo) vs PRONOMBRE (solo, como objeto)',
    'Use ejemplos verbatim del libro pag 320 (Whose keys are those? They\'re mine. / Whose house is that? It\'s yours. / Whose car is this? It\'s Frank\'s. / Is this Sarah\'s marker? Yes, it\'s hers. / Is that Miguel\'s motorcycle? Yes, it\'s his. / Is this Marie and Celeste\'s house? Yes, it\'s theirs. / Is that my apartment? No, it\'s not yours, it\'s mine. / etc.)',
    'Reforce TEMPLANZA: right shape (pronombre, no adjetivo, en posicion de objeto) + right ownership (own only what is truly yours, no inflar, no robar credito)',
    'CONFIRME que M40 NO existe en el A2 Book (el libro salta de M39 a M41 verbatim, linea 22871 A2 Book.md) - patron consistente con M19/M25/M31/M35 ya saltados',
    'NO ensene M41 "This Is Interesting!" (es Cl 30 martes 09/06) ni Third Conditional / Could-Should have',
    'NO re-ensene M33/M34 (Cl 24-25), M36/M37/M38 (Cl 26-28) - solo reciclaje natural en ejemplos',
    'NO use texto Heiiu (gramatica estructural/sustitucion - mismo criterio que Cl 14-28)',
    'Conduje BOARD RACE M39 (2 equipos en el tablero, transformar adjetivo en posicion de objeto -> pronombre correcto)',
    'Conduje WALKING TRANSFORMATION con tarjetas yo/tu/el/ella/nos/ellos (zonas WRONG/RIGHT, frases cotidianas/profesionales)',
    'Conduje SORTING fisico POSSESSIVE ADJECTIVES vs POSSESSIVE PRONOUNS (2 zonas, tarjetas individuales)',
    'Conduje HISTORIA INTERACTIVA absurda cotidiana profesional "Whose is this?" con pausas (cohorte agrego mine/hers/ours/theirs EN VOZ ALTA, NO huecos para llenar)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjetas "Subject + Verb + POSSESSIVE PRONOUN object" (visible la estructura)',
    'Conduje STATION ROTATION 3 estaciones (Whose questions / Mine-Yours-Ours statements / Comparativos con pronombres)',
    'Conduje PODIUM CEREMONY "Right Possessive" (cadena Whose-pregunta + Pronombre-respuesta con coro "Confirmed - right possessive!")',
    'Conduje SPEED DRILL DE PIE (cadena adjetivo posesivo -> pronombre objeto + coro)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 28, Cl 23, Cl 19, Cl 18)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + nota M40 NO existe + nota M41 martes',
    'En Tarea explique el por que + due date explicito (martes 09/06 antes 7AM)',
    'Tarea es 30-45 min (regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 30 martes 09/06 (M39 fue hoy; M40 NO existe - auditado verbatim; sigue M41 "This Is Interesting!" / Participle Adjectives)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase29_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 29 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M39 MINE, ALL MINE! / POSSESSIVE PRONOUNS AS OBJECTS (M40 NO EXISTE)',
    'A2 Book M39 "Mine, All Mine!" / Possessive Pronouns as Objects (modulo p.318+; Guia 1 p.319 con tabla canonica verbatim: my->mine, your->yours, his->his (cuidado: misma forma), her->hers, our->ours, their->theirs, its->its; "whose" como palabra de pregunta; Ejemplos p.320 verbatim; Ejercicios 1 p.321 "Responde a la pregunta usando la respuesta dada o genera la pregunta"; Ejercicios 2 p.322 "Responde a la pregunta usando mine, yours, his, hers, ours, o theirs"; Practice Guide p.323-325 "Formar preguntas sobre el dueno" + "Reemplace el adjetivo posesivo y objeto con el pronombre posesivo") + Board Race + Walking Transformation con tarjetas yo/tu/el/ella/nos/ellos + Sorting fisico POSSESSIVE ADJECTIVES vs POSSESSIVE PRONOUNS (2 zonas) + Historia interactiva ABSURDA cotidiana profesional "Whose is this?" con pausas (cohorte agrega mine/hers/ours/theirs EN VOZ ALTA, NO huecos) + Human-Sentence Line-up con tarjetas "Subject + Verb + POSSESSIVE PRONOUN object" + Station Rotation (Whose questions / Mine-Yours-Ours statements / Comparativos con pronombres) + Podium Ceremony "Right Possessive" + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + TEMPLANZA dia 4 v2 (right shape + right ownership: pronombre correcto en posicion de objeto, propiedad honesta) (M40 NO EXISTE - el libro salta de M39 a M41; verificado verbatim linea 22871 A2 Book.md; patron consistente con M19/M25/M31/M35 ya saltados; SIN texto Heiiu - gramatica estructural/sustitucion; profesor NUNCA comunica resultados/criterios del Final - exclusivo coordinacion; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 30 martes 09/06 = M41 "This Is Interesting!" / Participle Adjectives)',
    b1_c29_g_act, b1_c29_g_deliv, b1_c29_g_eval, S,
)
print('OK: B1_Clase29_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para lunes 08/06 B1 MASTERY Cl 29:')
print('  - B1/B1_Clase29_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase29_CONV_REPORTE.pdf')
print('  - B1/B1_Clase29_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase29_GRAMMAR_REPORTE.pdf')
