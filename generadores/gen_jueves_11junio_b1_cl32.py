#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 32 (jueves 11/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Adverbs of Manner
  (Hot Topic "How do people DO their work? Who works quickly? Who works
  carefully? Who speaks clearly?" + Simulacion "The Team Performance
  Recognition Meeting" con Guest Observer Pattern — 1 recognizer rotante,
  group observer, profesora coach NO juega recognizer) + Page 30 HOW I DO
  MY WORK — the manner of my work Draft 1 (escritura en clase anti-fraude
  IA; alimenta cuarto strand del proyecto hacia Final Cl 44) + Frase del
  Dia + JUSTICIA dia 2 v2 (CONTINUACION del bloque Cl 31-35; ayer Cl 31
  abrio JUSTICIA v2 dia 1 con M42)
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M43
  "How Do You Do?" / Adverbs of Manner (modulo p.340+; Vocabulario p.341
  con well/alone/together/early/late/fast/slowly/right/wrong/hard/suddenly/
  immediately/completely/easily/carefully; Guia 1 p.342 verbatim con 4
  reglas — (1) "Usamos adverbios de manera para describir como se hace
  una accion. Para responder a una pregunta como: How do you drive?";
  (2) "La mayoria de los adverbios se forman con la terminacion '-ly'
  (que corresponde a la terminacion '-mente' en espanol) despues del
  adjetivo. Ej. Sad → Sadly / Happy → Happily (cambiamos la terminacion
  '-ly' a '-ily')"; (3) "Sin embargo, hay unos irregulares. Ej. Fast →
  Fast. No existe la palabra 'fastly'. Ej. Good → Well"; (4) "En la gran
  mayoria de los casos, se coloca el adverbio de manera despues del
  verbo principal o despues del objeto directo, si hay. Yo juego bien →
  I play well. El juega futbol bien → He plays soccer well"; Ejemplos
  p.343 verbatim 17 pares adjetivo/adverbio — He plays well, He plays
  badly, William studies intelligently, Helena writes beautifully, Philip
  drives fast, Sebastian worked carefully, Mike speaks English correctly,
  Edgar's dog runs slowly, You play hard, James sings beautifully, The
  class worked together, etc.; Ejercicios p.344; Practice Guide
  p.345-346 verbatim con frecuencia + manera — I always believe you
  easily, He usually holds the pen hard, She sometimes writes
  intelligently, They often meet early, They occasionally change
  happily, She always understands slowly, They usually watch the airport
  carefully, She never reads wrong, He sometimes stops quickly, They
  occasionally speak beautifully, She always spends carefully, We often
  walk slowly, He occasionally remembers her sadly, They always wait for
  him together, He usually builds them wrong) + Board Race (transformar
  adjetivos a adverbios + posicionar en frase) + Walking Transformation
  WRONG/RIGHT FORM (fastly→fast / goodly→well / hardly→hard) +
  WRONG/RIGHT POSITION (entre S y V → despues del verbo o del objeto) +
  Sorting fisico tarjetas en 2 zonas (REGULAR -LY / IRREGULAR) +
  sub-zona TRAMPA (fastly/goodly/hardly NO EXISTEN para el sentido
  buscado) + Historia interactiva absurda profesional "The Performance
  Review Thursday" (cohorte responde EN VOZ ALTA en cada pausa por
  intern/developer/marketing manager/team lead/new hire/dog/YOU) +
  Human-Sentence Line-up "Subject + Verb + Object + Adverb" (o S+V+Adv
  si no hay objeto) + Station Rotation 3 estaciones (manner /
  frequency+manner con Practice Guide p.345-346 verbatim / contrast
  adjective vs adverb con Ejemplos p.343 verbatim) + Podium Ceremony
  "Right Manner" + Speed Drill + reversal trap.
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-31: gramatica
  estructural sobre adverbios de manera, no narrativa).
- Anuncio Cl 33 viernes 12/06 = M44 "I Want You to Go" / The Active
  Causative (verbatim linea 25055 A2 Book — Habilidades objetivas: "Sin
  dudar, formar y usar frases de volicion en el afirmativo, negativo e
  interrogativo. Sin dudar, distinguir entre las frases en las cuales no
  hay un cambio de sujeto: I want to go vs I want you to go") + JUSTICIA
  v2 dia 3 (apertura dia 1 Cl 31, dia 2 hoy, dia 3 manana — calendario
  absoluto Heiiu).
- PREGUNTA ABIERTA A DIANA en PASE de hoy: M44 ES EL ULTIMO MODULO del
  A2 Book confirmado. Cl 34-43 (10 clases) sin modulo nuevo hasta el
  Final Cl 44 — pregunta a coordinacion: ¿que plan oficial?
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin
  nota/criterios — eso es coordinacion).
- Profesor NUNCA comunica resultados/notas/criterios del Final; si alguien
  pregunta: "Coordination handles results — not me. Focus on what comes
  next."
- Tarea Cl 32: due viernes 12/06 antes 7AM, 30-45 min, NO fragmentada.
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
# B1 Cl 32 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase32_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase32_CONV_GUIA.pdf'),
)
print('OK: B1_Clase32_CONV_GUIA.pdf')

b1_c32_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 31 Conv = 12 frases get/become/go/turn + audio 2-3 min Team Recognition de cambios + reading 5 oraciones changes of state + TED career change/growth/burnout listening)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS JUSTICIA dia 2 v2 (CONTINUACION del bloque Cl 31-35 - ayer Cl 31 abrio JUSTICIA v2 dia 1): dar a cada accion su adverbio justo (regular adj + -ly o irregular well/fast/hard/late/early), en posicion correcta (despues del verbo o del objeto), reconocer publicamente COMO trabaja cada uno sin inflar ni borrar', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 31 Grammar M42 Changes of State: verbo equivocado — become para cambio rapido, go para emocion, turn para cansancio/virtud, am tired como cambio)', '7 min'),
    ('HOT TOPIC - "How do people DO their work? Who works quickly? Who works carefully? Who speaks clearly?" (adverbios de manera en contexto profesional - regulares -ly + irregulares well/fast/hard/late/early)', '17 min'),
    ('SIMULACION - "The Team Performance Recognition Meeting" (DE PIE, Guest Observer Pattern: 1 recognizer rotante + group observer + profesora coach - profesora NO juega recognizer; cada estudiante reconoce a un colega usando 3-4 adverbios de manera, JUSTICIA dia 2 cierre: sin inflar / sin borrar)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 30 - HOW I DO MY WORK - the manner of my work Draft 1 (escritura en clase anti-fraude IA; alimenta cuarto strand hacia Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea Cl 32 + Anuncio Cl 33 (M44 "I Want You to Go" / The Active Causative + JUSTICIA v2 dia 3) + Anuncio Final + Cierre', '7 min'),
]
b1_c32_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego Cl 31 Grammar M42)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Team Performance Recognition Meeting simulacion (Guest Observer Pattern: 1 recognizer rotante, group observer, profesora coach NO juega recognizer)',
    'Foto/video Mini-Pitch',
    'N Paginas 30 HOW I DO MY WORK DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 31 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio Cl 33 viernes 12/06 = M44 "I Want You to Go" / The Active Causative (verbatim linea 25055 A2 Book) + JUSTICIA v2 dia 3 (continuacion del bloque)',
]
b1_c32_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE cartelitos "CAREFULLY", "QUICKLY", "CLEARLY", "SLOWLY", "WELL", "HARD", "EARLY", "LATE", "TOGETHER" + carteles "MANNER" / "FREQUENCY" en tarjetas grandes + clipboard para Recognizer (Team Performance Recognition Meeting)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (1 regular -ly + 1 irregular)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui',
    'Verifique virtud CL 32 = JUSTICIA dia 2 v2 - SEGUNDO del bloque (Cl 31-35); ayer Cl 31 abrio JUSTICIA v2 dia 1 con M42',
    'Hile JUSTICIA en VATS como dia 2 v2 - CONTINUACION del bloque: dar a cada accion su adverbio justo (regular -ly o irregular), reconocer publicamente COMO trabaja cada uno sin inflar ni borrar',
    'ANUNCIE explicitamente al cierre que manana Cl 33 continua JUSTICIA v2 dia 3 con M44',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza en el segundo bloque con M43)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-31)',
    'RECIBI el PASE escrito de Juan Diego (Cl 31 Grammar M42 Changes of State) para el Peer Teacher',
    'Conduje Hot Topic "How do people DO their work?" con requirements en tablero (6+ adverbs of manner en posicion correcta + 2+ cosas work-specific + 1 JUSTICIA closure de reconocimiento publico sin inflar/borrar)',
    'Conduje The Team Performance Recognition Meeting con Guest Observer Pattern (1 recognizer rotante + group observer que cuenta adverbs of manner + profesora COACH NO juega recognizer)',
    'Simulacion fue PROFESIONAL/realista cotidiana (no familiar ni fantasiosa)',
    'Conduje escritura Page 30 HOW I DO MY WORK - the manner of my work Draft 1 EN CLASE (anti-fraude IA; alimenta cuarto strand hacia Final Cl 44)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica (adverbios de manera ya en boca del cohorte; patron mas comun: forma irregular equivocada — fastly/goodly/hardly; posicion incorrecta — entre S y V; JUSTICIA inflation/erasure)',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (viernes 12/06 antes 7AM)',
    'Tarea es 30-45 min (regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 33 viernes 12/06 = M44 "I Want You to Go" / The Active Causative (verbatim linea 25055 A2 Book — frases de volicion: I want to go vs I want you to go) + JUSTICIA v2 dia 3 (continua bloque)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase32_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 32 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado) | JUSTICIA dia 2 v2 - CONTINUACION DEL BLOQUE',
    'Aplicacion oral de Adverbs of Manner: Hot Topic "How do people DO their work? Who works quickly? Who works carefully? Who speaks clearly?" + Simulacion "The Team Performance Recognition Meeting" (DE PIE, Guest Observer Pattern: 1 recognizer rotante + group observer + profesora coach - profesora NO juega recognizer; cada estudiante reconoce a un colega usando 3-4 adverbios de manera regulares -ly + irregulares well/fast/hard/late/early + JUSTICIA closure: sin inflar ni borrar) + Page 30 HOW I DO MY WORK - the manner of my work Draft 1 anti-fraude IA (alimenta cuarto strand del proyecto hacia Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + JUSTICIA dia 2 v2 (CONTINUACION del bloque Cl 31-35 — ayer Cl 31 abrio JUSTICIA v2 dia 1 con M42) (SIN texto Heiiu - gramatica estructural sobre adverbios de manera, mismo criterio que Cl 14-31; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 33 viernes 12/06 = M44 "I Want You to Go" / The Active Causative — verbatim linea 25055 A2 Book — formar y usar frases de volicion en afirmativo/negativo/interrogativo + distinguir I want to go vs I want you to go + JUSTICIA v2 dia 3)',
    b1_c32_c_act, b1_c32_c_deliv, b1_c32_c_eval, S,
)
print('OK: B1_Clase32_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 32 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase32_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase32_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase32_GRAMMAR_GUIA.pdf')

b1_c32_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 31 = M42 Changes of State 12 frases get/become/go/turn + audio Team Recognition de cambios + reading 5 oraciones + TED career change/growth/burnout) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS JUSTICIA dia 2 v2 (CONTINUACION del bloque Cl 31-35 - ayer Cl 31 abrio JUSTICIA v2 dia 1 con M42): right adverb for the right manner, right form (regular -ly o irregular), right position (despues del verbo o del objeto), keep the block open - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna - Cl 32 Conv: forma irregular equivocada — fastly/goodly/hardly; posicion incorrecta — entre S y V; JUSTICIA inflation/erasure) - DE PIE', '7 min'),
    ('LIBRO M43 How Do You Do? / Adverbs of Manner (modulo p.340+; Vocabulario p.341 con well/alone/together/early/late/fast/slowly/right/wrong/hard/suddenly/immediately/completely/easily/carefully; Guia 1 p.342 verbatim con 4 reglas — (1) usamos adverbios para describir como se hace una accion / responder How do you drive?; (2) mayoria adj + -ly / Sad → Sadly / Happy → Happily; (3) irregulares Fast → Fast (NO fastly) / Good → Well; (4) posicion despues del verbo principal o del objeto directo — I play well / He plays soccer well) + BOARD RACE (transformar adjetivos a adverbios + posicionar en frase) - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M43 con zonas WRONG/RIGHT FORM (fastly→fast / goodly→well / hardly→hard) + WRONG/RIGHT POSITION (entre S y V → despues del verbo o del objeto) - caminar de "She carefully organizes the data" → "She organizes the data carefully" - DE PIE', '16 min'),
    ('LIBRO M43 (cont.) Ejemplos p.343 verbatim 17 pares adjetivo/adverbio (He plays well / He plays badly / The dog plays nicely / William studies intelligently / My class starts early / Your class starts late / John is speaking seriously / Helena writes beautifully / Philip drives fast / Suddenly I heard a noise / Please work on the problem immediately / Sebastian worked carefully / Mike speaks English correctly / Edgar\'s dog runs slowly / You play hard / James sings beautifully / The class worked together) + SORTING fisico tarjetas en 2 zonas (REGULAR -LY / IRREGULAR) + sub-zona TRAMPA (fastly/goodly/hardly NO existen para sentido buscado) + Historia interactiva ABSURDA profesional "The Performance Review Thursday" (cohorte responde EN VOZ ALTA en cada pausa por intern/developer/marketing manager/team lead/new hire/dog/YOU) - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP con tarjetas "Subject + Verb + Object + Adverb" (o S+V+Adv si no hay objeto) + STATION ROTATION - 3 estaciones (MANNER / FREQUENCY+MANNER con Practice Guide p.345-346 verbatim: I always believe you easily / He usually holds the pen hard / She sometimes writes intelligently / They often meet early / They always wait for him together / CONTRAST ADJ vs ADV con Ejemplos p.343 verbatim: He is a good player vs He plays well / Helena wrote a beautiful story vs Helena writes beautifully / Philip has a fast car vs Philip drives fast) - DE PIE', '12 min'),
    ('PODIUM CEREMONY "Right Manner" + SPEED DRILL DE PIE (cadena Adjetivo + Adverbio + frase completa con posicion correcta) + reversal trap rapido (fastly→fast / goodly→well / hardly→hard / posicion entre S y V → despues del verbo o del objeto)', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea Cl 32 + Anuncio Cl 33 (M44 "I Want You to Go" / The Active Causative + JUSTICIA v2 dia 3) + Anuncio Final Cl 44 + NOTA INTERNA pregunta abierta a Diana Cl 34-43 post-M44 + Cierre', '14 min'),
]
b1_c32_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M43 4 reglas pag 342 verbatim + Vocabulario pag 341 + Ejemplos pag 343 (17 pares adjetivo/adverbio)',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar) - INCLUYE pregunta abierta a coordinacion sobre Cl 34-43 post-M44',
    'Foto/video del Board Race (estudiantes en el tablero transformando adjetivos a adverbios + posicionando)',
    'Foto/video de la Walking Transformation con zonas WRONG/RIGHT FORM (fastly→fast / goodly→well / hardly→hard) + WRONG/RIGHT POSITION (entre S y V → despues del verbo o del objeto)',
    'Foto/video del Sorting fisico en 2 zonas (REGULAR -LY / IRREGULAR) + sub-zona TRAMPA (fastly/goodly/hardly) + Historia interactiva absurda profesional "The Performance Review Thursday" + Human-Sentence Line-up + Station Rotation 3 estaciones (manner / frequency+manner / contrast adj-vs-adv)',
    'Foto/video del PODIUM CEREMONY "Right Manner" + Speed Drill + reversal trap',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 31 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Cuantas veces te preguntaron resultado/criterios del Final y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio M44 viernes Cl 33 12/06 (M43 fue HOY; M44 verbatim linea 25055 A2 Book — ULTIMO modulo del A2 Book)',
    'Confirmaste anuncio JUSTICIA v2 dia 3 manana (apertura JUSTICIA dia 1 ayer Cl 31, dia 2 hoy Cl 32, dia 3 manana Cl 33 — calendario absoluto)',
    'PREGUNTA ABIERTA A DIANA en PASE: que plan oficial para Cl 34-43 post-M44 (10 clases sin modulo nuevo del libro hasta Final Cl 44)?',
]
b1_c32_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Verifique con mis propios ojos que el modulo anterior fue M42 (Cl 31 miercoles); M40 NO existe (auditado Cl 30 verbatim linea 22871 A2 Book)',
    'Verifique con mis propios ojos que el modulo siguiente para Cl 33 manana es M44 "I Want You to Go" / The Active Causative (verbatim, linea 25055 A2 Book)',
    'Lei en voz alta las 4 reglas del libro pag 342 que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas-adjetivo (sad / happy / careful / quick / clear / slow / beautiful / intelligent / serious / sudden / immediate / complete / easy / nice / bad) + tarjetas-irregular (fast / hard / late / early / good→well / together / alone / right / wrong) + tarjetas-trampa WRONG (fastly / goodly / hardly) + tarjetas-sujeto profesional (she / he / they / the team / our designer / the new hire / the senior dev / the team lead / our supervisor / William / Helena / Philip / Sebastian / Mike / Edgar\'s dog / the class) + tarjetas-verbo/objeto (plays soccer / plays / studies / writes / drives / works / sings / arrives / starts / runs / speaks English / heard a noise / organizes the data / presents the results / delivers the demo) + tarjetas-frecuencia (always / usually / often / sometimes / occasionally / never) ANTES',
    'PREPARE la HISTORIA INTERACTIVA absurda cotidiana profesional "The Performance Review Thursday" con pausas marcadas (cohorte agrega EN VOZ ALTA Plays well/Works hard/Speaks clearly/Codes slowly but beautifully/Arrives early/Responds quickly en cada pausa, NO huecos) — intern, developer, marketing manager, team lead, new hire, dog, y YOU',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation con zonas WRONG/RIGHT FORM + WRONG/RIGHT POSITION + line-up + podium + 2 zonas sorting + sub-zona TRAMPA + 3 stations)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui el libro',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 32 = JUSTICIA dia 2 v2 - SEGUNDO del bloque (Cl 31-35); ayer Cl 31 abrio JUSTICIA v2 dia 1',
    'Cubri M43 How Do You Do? / Adverbs of Manner DESDE EL LIBRO (A2 Book modulo p.340+; Vocabulario p.341; Guia 1 p.342 4 reglas verbatim; Ejemplos 1 p.343 17 pares verbatim; Ejercicios p.344; Practice Guide p.345-346 verbatim con frecuencia + manera) citando reglas y ejemplos verbatim',
    'Explique las 4 reglas del libro p.342 verbatim: (1) usamos adverbios de manera para describir como se hace una accion / responder How do you drive?; (2) mayoria adj + -ly (Sad → Sadly / Happy → Happily, cambio -y a -ily); (3) irregulares Fast → Fast (no fastly) / Good → Well; (4) posicion despues del verbo principal o del objeto directo si hay (I play well / He plays soccer well)',
    'Use el vocabulario verbatim del libro p.341 (well / alone / together / early / late / fast / slowly / right / wrong / hard / suddenly / immediately / completely / easily / carefully)',
    'Use los 17 pares adjetivo/adverbio del libro p.343 (He plays well / He plays badly / The dog plays nicely / William studies intelligently / My class starts early / Your class starts late / John is speaking seriously / Helena writes beautifully / Philip drives fast / Suddenly I heard a noise / Please work on the problem immediately / Sebastian worked carefully / Mike speaks English correctly / Edgar\'s dog runs slowly / You play hard / James sings beautifully / The class worked together)',
    'Use la Practice Guide p.345-346 verbatim con combinacion frecuencia + manera (I always believe you easily / He usually holds the pen hard / She sometimes writes intelligently to her mother / They often meet early / They occasionally change happily / She always understands slowly / They usually watch the airport carefully / She never reads wrong / He sometimes stops quickly / They occasionally speak beautifully / She always spends carefully / We often walk slowly / He occasionally remembers her sadly / They always wait for him together / He usually builds them wrong)',
    'Reforce JUSTICIA dia 2 v2 - CONTINUACION del bloque: right adverb for the right manner, right form (regular -ly o irregular), right position (despues del verbo o del objeto); anuncie explicitamente continuacion JUSTICIA dia 3 manana con M44',
    'CONFIRME que M40 NO existe en el A2 Book (auditado Cl 30 verbatim linea 22871) - patron consistente con M19/M25/M31/M35 ya saltados',
    'NO ensene M44 "I Want You to Go" / The Active Causative (es Cl 33 viernes 12/06) ni Third Conditional / Could-Should have',
    'NO re-ensene M33/M34 (Cl 24-25), M36/M37/M38 (Cl 26-28), M39 (Cl 29), M41 (Cl 30), M42 (Cl 31) - solo reciclaje natural en ejemplos (M42 se recicla en frases con get + adverbio: "she got angry suddenly" / "he gets frustrated easily")',
    'NO use texto Heiiu (gramatica estructural sobre adverbios de manera - mismo criterio que Cl 14-31)',
    'Conduje BOARD RACE M43 (2 equipos en el tablero, transformar adjetivos a adverbios con forma correcta — regular -ly o irregular — y construir frase completa con posicion correcta — despues del verbo o del objeto — basadas en Ejemplos p.343 + Practice Guide p.345-346)',
    'Conduje WALKING TRANSFORMATION con 4 zonas WRONG FORM (fastly/goodly/hardly) → RIGHT FORM (fast/well/hard) + WRONG POSITION (entre S y V) → RIGHT POSITION (despues del verbo o del objeto)',
    'Conduje SORTING fisico de tarjetas en 2 zonas (REGULAR -LY: carefully/quickly/clearly/slowly/beautifully/intelligently/seriously/suddenly/immediately/completely/easily/happily/sadly/nicely/badly/correctly) + (IRREGULAR: well/fast/hard/late/early/together/alone/right/wrong) + sub-zona TRAMPA (fastly/goodly/hardly NO existen para sentido buscado) + cohorte armo 4 frases (2 regulares + 2 irregulares) con POSICION CORRECTA',
    'Conduje HISTORIA INTERACTIVA absurda cotidiana profesional "The Performance Review Thursday" con pausas (cohorte agrego EN VOZ ALTA Plays well/Works hard/Speaks clearly/Codes slowly but beautifully/Arrives early/Responds quickly en cada pausa, NO huecos para llenar; pase por intern/developer/marketing manager/team lead/new hire/dog/YOU)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjetas "Subject + Verb + Object + Adverb" (o S+V+Adv si no hay objeto; visible la regla de posicion del libro p.342 regla 4 verbatim)',
    'Conduje STATION ROTATION 3 estaciones (MANNER / FREQUENCY+MANNER con Practice Guide p.345-346 verbatim / CONTRAST ADJ vs ADV con Ejemplos p.343 verbatim 17 pares)',
    'Conduje PODIUM CEREMONY "Right Manner" (cadena adjetivo → adverbio + frase completa con posicion correcta + coro "Confirmed - right manner!" cubriendo al menos 2 pares regulares + 2 pares irregulares + 2 pares con objeto)',
    'Conduje SPEED DRILL DE PIE (Practice Guide p.345-346: easy/I/believe you/always → easily / hard/he/holds the pen/usually → hard / intelligent/she/writes to her mother/sometimes → intelligently / early/they/meet/often → early / slow/she/understands/always → slowly / careful/they/watch the airport/usually → carefully / wrong/she/reads/never → wrong / beautiful/they/speak/occasionally → beautifully)',
    'Conduje SPEED DRILL reversal trap rapido (cohorte corrige EN VOZ ALTA frases con forma equivocada o posicion equivocada: "she drives fastly" -> "she drives FAST! (irregular no fastly)"; "he plays goodly" -> "he plays WELL! (good→well)"; "the new hire works hardly" -> "the new hire works HARD! (hardly = casi-no)"; "she carefully organizes the data" -> "she organizes the data CAREFULLY! (despues del OBJETO)"; "he quickly responds" -> "he responds QUICKLY! (despues del VERBO)"; "they clearly speak in standups" -> "they speak CLEARLY in standups!"; "she slowly speaks the English" -> "she speaks English SLOWLY!"; "he hard works in the factory" -> "he works HARD in the factory!")',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 31, Cl 30, Cl 29, Cl 28, Cl 23, Cl 19, Cl 18)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + nota M40 NO existe + nota M44 viernes (ULTIMO modulo del A2 Book) + nota JUSTICIA v2 dia 3 manana + PREGUNTA ABIERTA A DIANA sobre plan Cl 34-43 post-M44 (10 clases sin modulo nuevo)',
    'En Tarea explique el por que + due date explicito (viernes 12/06 antes 7AM)',
    'Tarea es 30-45 min (regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 33 viernes 12/06 (M43 fue hoy; sigue M44 "I Want You to Go" / The Active Causative - verbatim linea 25055 — frases de volicion: I want to go vs I want you to go)',
    'ANUNCIE explicitamente al cierre que manana Cl 33 continua JUSTICIA v2 dia 3 (apertura JUSTICIA dia 1 ayer Cl 31, dia 2 hoy, dia 3 manana — bloque sigue abierto)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'PLANTEE en PASE a Danna la PREGUNTA ABIERTA A COORDINACION (DIANA): M44 es el ULTIMO modulo del A2 Book confirmado; despues de Cl 33 viernes 12/06 quedan Cl 34-43 (10 clases) sin modulo nuevo hasta Final Cl 44; opciones esbozadas (a) repaso/refuerzo arco B1 con simulaciones acumuladas / (b) revision intensiva pre-Final de Pages 16-30 + grammar acumulada M14-M44 / (c) algo distinto que coordinacion decida; solicitar definicion antes de Cl 34 lunes 15/06',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase32_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 32 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M43 HOW DO YOU DO? / ADVERBS OF MANNER | JUSTICIA dia 2 v2 - CONTINUACION DEL BLOQUE',
    'A2 Book M43 "How Do You Do?" / Adverbs of Manner (modulo p.340+; Vocabulario p.341 con well/bien, alone/solo, together/juntos, early/temprano, late/tarde, fast/rapidamente de velocidad, slowly/lentamente, right/correctamente, wrong/incorrectamente, hard/duro, suddenly/repentinamente, immediately o right away/inmediatamente, completely/completamente, easily/facilmente, carefully/cuidadosamente; Guia 1 p.342 verbatim con 4 reglas — (1) "Usamos adverbios de manera para describir como se hace una accion. Para responder a una pregunta como: How do you drive?"; (2) "La mayoria de los adverbios se forman con la terminacion -ly (que corresponde a la terminacion -mente en espanol) despues del adjetivo. Ej. Sad → Sadly / Happy → Happily (cambiamos la terminacion -ly a -ily)"; (3) "Sin embargo, hay unos irregulares. Ej. Fast → Fast. No existe la palabra fastly. Ej. Good → Well"; (4) "En la gran mayoria de los casos, se coloca el adverbio de manera despues del verbo principal o despues del objeto directo, si hay. Yo juego bien → I play well. El juega futbol bien → He plays soccer well"; Ejemplos 1 p.343 verbatim 17 pares adjetivo/adverbio — He is a good player vs He plays well, He is a bad player vs He plays badly, James has a nice dog vs The dog plays nicely, William is an intelligent student vs William studies intelligently, I have an early class vs My class starts early, You have a late class vs Your class starts late, John is a serious doctor vs John is speaking seriously, Helena wrote a beautiful story vs Helena writes beautifully, Philip has a fast car vs Philip drives fast, I heard a sudden noise vs Suddenly I heard a noise, We have an immediate problem vs Please work on the problem immediately, Sebastian was a careful doctor vs Sebastian worked carefully, Mike speaks correct English vs Mike speaks English correctly, Edgar has a slow dog vs Edgar\'s dog runs slowly, You have a hard game vs You play hard, The song is beautiful vs James sings beautifully, The class is together vs The class worked together; Ejercicios p.344; Practice Guide p.345-346 verbatim — He did the homework well, She said good morning alone, They drove to the university together, She took a cookie early, He came to the house late, He found Nemo fast, He gave the money slowly, He worked hard in the factory, She talked happily with her friend, She played basketball beautifully, She ran badly on the sidewalk, He moved intelligently to Berlin, She lived seriously in Medellin + frecuencia+manera: I always believe you easily, He usually holds the pen hard, She sometimes writes intelligently to her mother, They often meet early, They occasionally change happily, She always understands slowly, They usually watch the airport carefully, She never reads wrong, He sometimes stops quickly, They occasionally speak beautifully, She always spends carefully, We often walk slowly, He occasionally remembers her sadly, They always wait for him together, He usually builds them wrong) + Board Race (transformar adjetivos a adverbios + posicionar en frase) + Walking Transformation WRONG/RIGHT FORM (fastly→fast / goodly→well / hardly→hard) + WRONG/RIGHT POSITION (entre S y V → despues del verbo o del objeto) + Sorting fisico tarjetas en 2 zonas (REGULAR -LY / IRREGULAR) + sub-zona TRAMPA (fastly/goodly/hardly NO existen para sentido buscado) + Historia interactiva ABSURDA cotidiana profesional "The Performance Review Thursday" con pausas (cohorte agrega Plays well/Works hard/Speaks clearly/Codes slowly but beautifully/Arrives early/Responds quickly EN VOZ ALTA, NO huecos) + Human-Sentence Line-up con tarjetas "Subject + Verb + Object + Adverb" (o S+V+Adv) + Station Rotation 3 estaciones (manner / frequency+manner con Practice Guide p.345-346 verbatim / contrast adjective vs adverb con Ejemplos p.343 verbatim 17 pares) + Podium Ceremony "Right Manner" + Speed Drill + reversal trap + FRASE DEL DIA (Goldlist retirado) + JUSTICIA dia 2 v2 - CONTINUACION DEL BLOQUE (right adverb, right form, right position, keep the block open; ayer Cl 31 abrio JUSTICIA v2 dia 1 con M42; manana Cl 33 continua JUSTICIA v2 dia 3 con M44 The Active Causative) (M40 NO EXISTE - auditado Cl 30 verbatim linea 22871; SIN texto Heiiu - gramatica estructural sobre adverbios de manera; profesor NUNCA comunica resultados/criterios del Final - exclusivo coordinacion; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 33 viernes 12/06 = M44 "I Want You to Go" / The Active Causative - verbatim linea 25055 A2 Book - formar y usar frases de volicion en afirmativo/negativo/interrogativo + distinguir I want to go vs I want you to go + JUSTICIA v2 dia 3; PREGUNTA ABIERTA A DIANA en PASE: M44 es el ULTIMO modulo del A2 Book confirmado, Cl 34-43 = 10 clases sin modulo nuevo hasta Final Cl 44 — solicitar plan oficial)',
    b1_c32_g_act, b1_c32_g_deliv, b1_c32_g_eval, S,
)
print('OK: B1_Clase32_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para jueves 11/06 B1 MASTERY Cl 32:')
print('  - B1/B1_Clase32_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase32_CONV_REPORTE.pdf')
print('  - B1/B1_Clase32_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase32_GRAMMAR_REPORTE.pdf')
