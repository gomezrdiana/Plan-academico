#!/usr/bin/env python3
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 31 (miercoles 10/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Changes of State
  (Hot Topic "How do people CHANGE in this work week? When do you GET tired
  / GET bored / GET excited / BECOME more confident?" + Simulacion "The
  Team Check-in" con Guest Observer Pattern — 1 reporter rotante, group
  observer, profesora coach NO juega reporter) + Page 29 HOW I AM CHANGING
  THROUGH THIS WORK — what I'm getting better at, what I'm becoming Draft 1
  (escritura en clase anti-fraude IA; alimenta tercer strand del proyecto
  hacia Final Cl 44) + Frase del Dia + JUSTICIA dia 1 v2 (APERTURA del
  nuevo bloque Cl 31-35; ayer Cl 30 cerro TEMPLANZA v2 dia 5)
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M42
  "Getting Crazy!" / Changes of State (modulo p.333+; Vocabulario p.334
  con to lose/to hurt/to scare/to marry + huge/far/tough/quiet/active/
  famous; Guia 1 p.335 regla canonica verbatim — "El ingles usa el verbo
  'to get' o (muy formalmente) 'to become'. Esto puede ser usado en
  cualquier tiempo." + tabla Before/Change/After: not sick → I get sick /
  not happy → we get happy / not angry → she gets angry / not lost → I
  got lost; regla 4 conecta M41+M42 — "Los adjetivos de participio que
  aprendimos en el ultimo capitulo se usan muy frecuentemente de esta
  manera" / "She got interested / She got interesting"; Ejemplos 1 p.336
  verbatim ~20 frases — Camila got bored, Miguel got tired, I got sick,
  Liam got excited, I got confused, I got hurt playing soccer, iPhones
  got huge, the class got quiet, the dog got lost in Piedecuesta, etc.;
  Ejercicios 1 p.337; Practice Guide p.338-339 tabla 5 tiempos The dog
  gets/got/will get/is getting/was getting tired aplicada a dog tired,
  day late, my marks low, your hair long, the boys active, my friends
  married, I bored in the Spanish class, the book boring) + extension
  canonica Heiiu (GO + adj idiomatico: crazy/red/bald/quiet/pale; TURN
  + edad/color: turn 30/turn red) + Board Race GET vs BECOME vs GO vs
  TURN + Walking Transformation STATE → CHANGE (caminar de "I am tired"
  → "I am getting tired") + Sorting fisico tarjetas en 4 zonas + Historia
  interactiva absurda profesional "The Office Transformation Tuesday"
  (cohorte responde EN VOZ ALTA got tired/got excited/became a manager/
  went crazy/turned 50 en cada pausa) + Human-Sentence Line-up "Subject +
  GET/BECOME/GO/TURN + adj/noun/number" + Station Rotation 3 estaciones
  (cuerpo / emocion / situacion con Practice Guide p.338-339 tabla 5
  tiempos) + Podium Ceremony "Right Change" + Speed Drill en 5 tiempos +
  reversal trap + Frase del Dia + JUSTICIA dia 1 v2 (APERTURA del bloque)
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-30: gramatica
  estructural sobre verbos de cambio de estado, no narrativa).
- Anuncio Cl 32 jueves 11/06 = M43 "How Do You Do?" / Adverbs of Manner
  (verbatim linea 24275 A2 Book — Habilidades objetivas: "Sin dudar,
  formar y usar los adverbios de manera en la ubicacion correcta. Sin
  dudar, distinguir entre adverbios de frecuencia y adverbios de manera
  y colocar ambos correctamente en una oracion.") + JUSTICIA v2 dia 2
  (apertura JUSTICIA hoy con dia 1, continua dia 2 manana — calendario
  absoluto Heiiu).
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin
  nota/criterios — eso es coordinacion).
- Profesor NUNCA comunica resultados/notas/criterios del Final; si alguien
  pregunta: "Coordination handles results — not me. Focus on what comes
  next."
- Tarea Cl 31: due jueves 11/06 antes 7AM, 30-45 min, NO fragmentada.
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
# B1 Cl 31 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase31_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase31_CONV_GUIA.pdf'),
)
print('OK: B1_Clase31_CONV_GUIA.pdf')

b1_c31_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 30 Conv = 12 frases -ING/-ED + audio 2-3 min Engagement + reading 5 oraciones participle adjectives + TED engagement/burnout listening)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS JUSTICIA dia 1 v2 (APERTURA del bloque Cl 31-35 - ayer Cl 30 cerro TEMPLANZA v2 dia 5): dar a cada cambio su verbo correcto (GET rapido, BECOME lento, GO idiomatico, TURN edad/color), empatia con el otro al nombrar su cambio', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 30 Grammar M41 Participle Adjectives: invertir -ING/-ED / "I am exciting" / "The meeting was tired" / "I am interesting in" / "The class is bored" sentido invertido / formas raras "exciteded")', '7 min'),
    ('HOT TOPIC - "How do people CHANGE in this work week?" (get/become/go/turn en contexto profesional)', '17 min'),
    ('SIMULACION - "The Team Check-in" (DE PIE, Guest Observer Pattern: 1 reporter rotante + group observer + profesora coach - profesora NO juega reporter; cada estudiante reporta cambios propios y de un colega de la semana usando get/become/go/turn forms naturalmente)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 29 - HOW I AM CHANGING THROUGH THIS WORK - what I am getting better at, what I am becoming Draft 1 (escritura en clase anti-fraude IA; alimenta tercer strand hacia Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea Cl 31 + Anuncio Cl 32 (M43 "How Do You Do?" / Adverbs of Manner + JUSTICIA v2 dia 2) + Anuncio Final + Cierre', '7 min'),
]
b1_c31_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego Cl 30 Grammar M41)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Team Check-in simulacion (Guest Observer Pattern: 1 reporter rotante, group observer, profesora coach NO juega reporter)',
    'Foto/video Mini-Pitch',
    'N Paginas 29 HOW I AM CHANGING THROUGH THIS WORK DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 30 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio Cl 32 jueves 11/06 = M43 "How Do You Do?" / Adverbs of Manner (verbatim linea 24275 A2 Book) + JUSTICIA v2 dia 2 (apertura JUSTICIA hoy con dia 1, continua dia 2 manana)',
]
b1_c31_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE cartelitos "GET TIRED", "GET EXCITED", "GET BORED", "GET CONFUSED", "BECOME PROFESSIONAL", "GO CRAZY", "TURN 30" en tarjetas grandes + clipboard para Reporter (Team Check-in)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (1 GET form + 1 BECOME form)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui',
    'Verifique virtud CL 31 = JUSTICIA dia 1 v2 - PRIMERO del bloque (Cl 31-35); ayer Cl 30 cerro TEMPLANZA v2 dia 5',
    'Hile JUSTICIA en VATS como dia 1 v2 - APERTURA del bloque: dar a cada cambio su verbo correcto (GET / BECOME / GO / TURN), nombrar el cambio del otro sin inflar ni borrar',
    'ANUNCIE explicitamente al cierre que manana Cl 32 continua JUSTICIA v2 dia 2 (apertura JUSTICIA hoy con dia 1)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza en el segundo bloque con M42)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-30)',
    'RECIBI el PASE escrito de Juan Diego (Cl 30 Grammar M41 Participle Adjectives) para el Peer Teacher',
    'Conduje Hot Topic "How do people CHANGE in this work week?" con requirements en tablero (6+ get/become/go/turn forms + 2+ cosas work-specific + 1 JUSTICIA closure con cambio de un colega nombrado fairly)',
    'Conduje The Team Check-in con Guest Observer Pattern (1 reporter rotante + group observer que cuenta change forms + profesora COACH NO juega reporter)',
    'Simulacion fue PROFESIONAL/realista cotidiana (no familiar ni fantasiosa)',
    'Conduje escritura Page 29 HOW I AM CHANGING THROUGH THIS WORK - what I am getting better at, what I am becoming Draft 1 EN CLASE (anti-fraude IA; alimenta tercer strand hacia Final Cl 44)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica (cambios get/become/go/turn ya en boca del cohorte; patron mas comun: verbo equivocado — become para cambio rapido, go para emocion, turn para cansancio, am tired como cambio)',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (jueves 11/06 antes 7AM)',
    'Tarea es 30-45 min (regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 32 jueves 11/06 = M43 "How Do You Do?" / Adverbs of Manner (verbatim linea 24275 A2 Book — adverbios de manera en ubicacion correcta + distinguir frecuencia vs manera) + JUSTICIA v2 dia 2 (continua bloque)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase31_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 31 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado) | JUSTICIA dia 1 v2 - APERTURA DEL BLOQUE',
    'Aplicacion oral de Changes of State: Hot Topic "How do people CHANGE in this work week?" + Simulacion "The Team Check-in" (DE PIE, Guest Observer Pattern: 1 reporter rotante + group observer + profesora coach - profesora NO juega reporter; cada estudiante reporta cambios propios y de un colega con 6+ get/become/go/turn forms naturales + JUSTICIA closure: nombrar el cambio del otro sin inflar ni borrar) + Page 29 HOW I AM CHANGING THROUGH THIS WORK - what I am getting better at, what I am becoming Draft 1 anti-fraude IA (alimenta tercer strand del proyecto hacia Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + JUSTICIA dia 1 v2 (APERTURA del nuevo bloque Cl 31-35 — ayer Cl 30 cerro TEMPLANZA v2 dia 5) (SIN texto Heiiu - gramatica estructural sobre verbos de cambio de estado, mismo criterio que Cl 14-30; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 32 jueves 11/06 = M43 "How Do You Do?" / Adverbs of Manner — verbatim linea 24275 A2 Book — formar y usar adverbios de manera en ubicacion correcta + distinguir adverbios de frecuencia vs manera + JUSTICIA v2 dia 2)',
    b1_c31_c_act, b1_c31_c_deliv, b1_c31_c_eval, S,
)
print('OK: B1_Clase31_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 31 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase31_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase31_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase31_GRAMMAR_GUIA.pdf')

b1_c31_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 30 = M41 Participle Adjectives 12 frases -ING/-ED + audio Engagement + reading 5 oraciones + TED engagement/burnout) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS JUSTICIA dia 1 v2 (APERTURA del bloque Cl 31-35 - ayer Cl 30 cerro TEMPLANZA v2 dia 5): right verb for the right change (GET / BECOME / GO / TURN), open the block clean - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna - Cl 31 Conv: verbo equivocado — become para cambio rapido, go para emocion, turn para cansancio, am tired como cambio) - DE PIE', '7 min'),
    ('LIBRO M42 Getting Crazy! / Changes of State (modulo p.333+; Vocabulario p.334 con to lose/to hurt/to scare/to marry + huge/far/tough/quiet/active/famous; Guia 1 p.335 regla canonica verbatim — "El ingles usa el verbo to get o (muy formalmente) to become — esto puede ser usado en cualquier tiempo" + tabla Before/Change/After: not sick → I get sick / not happy → we get happy / not angry → she gets angry / not lost → I got lost; regla 4 conecta M41+M42 — "Los adjetivos de participio que aprendimos en el ultimo capitulo se usan muy frecuentemente de esta manera" / She got interested / She got interesting) + extension canonica Heiiu (GO + adj idiomatico: crazy/red/bald/quiet/pale; TURN + edad/color) + BOARD RACE (clasificar GET vs BECOME vs GO vs TURN en frases con verbo equivocado o incompletas) - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M42 con zonas STATE → CHANGE - caminar de "I am tired" → "I am getting tired" / "I got tired" usando el verbo correcto segun tipo de cambio (incluye trampa M41+M42: "She is interesting" → "She got interesting" vs "She is interested" → "She got interested") - DE PIE', '16 min'),
    ('LIBRO M42 (cont.) Ejemplos p.336 verbatim (Camila got bored / My sister got tall / Miguel got tired / James got surprised / Don\'t get lost in Bogota / I got sick last night / If you don\'t keep learning you will get boring / Liam got excited / I got sad / I got confused / If I do not call my mother will get worried / I got hurt playing soccer / iPhones got huge in the US / The class got quiet before the test / The dog got lost in Piedecuesta / etc.) + SORTING fisico tarjetas frase-tarjeta en 4 zonas (GET cambio rapido / BECOME lento permanente / GO idiomatico crazy-red-bald-quiet / TURN edad-color) + Historia interactiva ABSURDA profesional "The Office Transformation Tuesday" (cohorte responde EN VOZ ALTA got tired/got excited/became a manager/went crazy/turned 50 en cada pausa por intern/developer/marketing manager/compliance officer/project/team/YOU) - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP con tarjetas "Subject + GET/BECOME/GO/TURN + adj/noun/number + complemento contextual" + STATION ROTATION - 3 estaciones (CUERPO / EMOCION / SITUACION) usando Practice Guide p.338-339 tabla 5 tiempos (The dog gets/got/will get/is getting/was getting tired aplicada a dog tired, day late, my marks low, your hair long, the boys active, my friends married, I bored, the book boring) - DE PIE', '12 min'),
    ('PODIUM CEREMONY "Right Change" + SPEED DRILL DE PIE en 5 tiempos (Practice Guide p.338-339) - cadena State-sentence + Change-sentence con coro "Confirmed - right change!" + reversal trap rapido (verbo equivocado corregido en coro)', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea Cl 31 + Anuncio Cl 32 (M43 "How Do You Do?" / Adverbs of Manner + JUSTICIA v2 dia 2) + Anuncio Final Cl 44 + Cierre', '14 min'),
]
b1_c31_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M42 regla canonica pag 335 + tabla Before/Change/After + Vocabulario pag 334 + Ejemplos pag 336',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero clasificando GET vs BECOME vs GO vs TURN)',
    'Foto/video de la Walking Transformation con zonas STATE → CHANGE (incluye trampa M41+M42 "interesting/interested")',
    'Foto/video del Sorting fisico de tarjetas frase-tarjeta en 4 zonas (GET / BECOME / GO / TURN) + Historia interactiva absurda profesional "The Office Transformation Tuesday" + Human-Sentence Line-up + Station Rotation 3 estaciones (cuerpo/emocion/situacion)',
    'Foto/video del PODIUM CEREMONY "Right Change" + Speed Drill en 5 tiempos (Practice Guide p.338-339)',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 30 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Cuantas veces te preguntaron resultado/criterios del Final y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio M43 jueves Cl 32 11/06 (M42 fue HOY; M43 verbatim linea 24275 A2 Book — adverbios de manera en ubicacion correcta + distinguir frecuencia vs manera)',
    'Confirmaste anuncio JUSTICIA v2 dia 2 manana (apertura JUSTICIA hoy con dia 1, continua dia 2 manana — calendario absoluto)',
]
b1_c31_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Verifique con mis propios ojos que el modulo anterior fue M41 (Cl 30 martes); M40 NO existe (auditado Cl 30 verbatim linea 22871 A2 Book)',
    'Verifique con mis propios ojos que el modulo siguiente para Cl 32 manana es M43 "How Do You Do?" / Adverbs of Manner (verbatim, linea 24275 A2 Book)',
    'Lei en voz alta las reglas del libro pag 335 que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas-frase GET (Camila ___ bored / Miguel ___ tired / I ___ sick / Liam ___ excited / I ___ confused / I ___ hurt playing soccer / iPhones ___ huge / The class ___ quiet / The dog ___ lost / She ___ interested / I ___ tired by 6 PM / She ___ angry on Friday) + tarjetas-frase BECOME (She ___ a senior manager / I am ___ more patient / He is ___ the go-to person / Our company ___ profitable / He ___ rich / She is ___ famous) + tarjetas-frase GO (The team ___ quiet / I ___ red / He is ___ bald / She ___ crazy / The room ___ pale) + tarjetas-frase TURN (Our supervisor ___ 50 / I am ___ 30 / My hair is ___ grey / The leaves ___ red) para sorting, line-up y stations ANTES',
    'PREPARE la HISTORIA INTERACTIVA absurda cotidiana profesional "The Office Transformation Tuesday" con pausas marcadas (cohorte agrega EN VOZ ALTA got tired/got excited/became a manager/went crazy/turned 50 en cada pausa, NO huecos) — intern, developer, marketing manager, compliance officer (turned 50), proyecto, equipo, y YOU',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation con zonas STATE→CHANGE + line-up + podium + 4 zonas sorting + 3 stations)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui el libro',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 31 = JUSTICIA dia 1 v2 - PRIMERO del bloque (Cl 31-35); ayer Cl 30 cerro TEMPLANZA v2 dia 5',
    'Cubri M42 Getting Crazy! / Changes of State DESDE EL LIBRO (A2 Book modulo p.333+; Vocabulario p.334; Guia 1 p.335 regla canonica; Ejemplos 1 p.336 ~20 frases; Ejercicios 1 p.337; Practice Guide p.338-339 tabla 5 tiempos) citando reglas y ejemplos verbatim',
    'Explique la regla canonica del libro p.335 verbatim: (1) si no estuve enfermo antes pero ahora estoy, ocurrio un cambio de estado; (2) espanol usa muchos verbos con reflexivos se/me/te; (3) ingles usa "to get" o (muy formalmente) "to become" — esto puede ser usado en cualquier tiempo; (4) los adjetivos de participio M41 se usan muy frecuentemente con get (She got interested / She got interesting)',
    'Use la tabla Before/Change/After del libro p.335: not sick → I get sick / not happy → we get happy / not angry → she gets angry / not lost → I got lost (past tense)',
    'Use el vocabulario verbatim del libro p.334 (to lose / to hurt / to scare / to marry + huge / far / tough / quiet / active / famous)',
    'Use ejemplos verbatim del libro p.336 (Camila got bored / My sister got tall / Miguel got tired / James got surprised / Don\'t get lost in Bogota / I got sick last night / If you don\'t keep learning you will get boring / Liam got excited / I got sad / I got confused / If I do not call my mother will get worried / It\'s almost 7:00 I have to get up / I get frustrated with my Spanish exams / Mike got interested in the history class / The movie got confusing / The dog got lost in Piedecuesta / iPhones got huge in the US / I got hurt playing soccer / I got fat when I was living in Canada / The class got quiet before the test)',
    'Use la Practice Guide p.338-339 tabla 5 tiempos (The dog gets/got/will get/is getting/was getting tired) aplicada a al menos 4 sujetos diferentes (dog tired, day late, my marks low, your hair long, the boys active, my friends married, I bored in the Spanish class, the book boring)',
    'Introduje la extension canonica Heiiu fuera de p.333-339 pero consistente (GO + adj idiomatico: crazy/red/bald/quiet/pale; TURN + edad/color: turn 30 / turn red) clarificando que es uso natural B1 mas alla del libro pero del mismo dominio',
    'Reforce JUSTICIA dia 1 v2 - APERTURA: right verb for the right change (GET quick / BECOME slow-permanent / GO idiomatic / TURN age-color); anuncie explicitamente continuacion JUSTICIA dia 2 manana',
    'CONFIRME que M40 NO existe en el A2 Book (auditado Cl 30 verbatim linea 22871) - patron consistente con M19/M25/M31/M35 ya saltados',
    'NO ensene M43 "How Do You Do?" / Adverbs of Manner (es Cl 32 jueves 11/06) ni M44 (es Cl 33) ni Third Conditional / Could-Should have',
    'NO re-ensene M33/M34 (Cl 24-25), M36/M37/M38 (Cl 26-28), M39 (Cl 29), M41 (Cl 30) - solo reciclaje natural en ejemplos (M41 se recicla fuerte por la regla 4 pag 335 que conecta M41+M42)',
    'NO use texto Heiiu (gramatica estructural sobre verbos de cambio de estado - mismo criterio que Cl 14-30)',
    'Conduje BOARD RACE M42 (2 equipos en el tablero, clasificar GET vs BECOME vs GO vs TURN en frases con verbo equivocado/incompletas basadas en Ejemplos p.336 + Practice Guide p.338-339)',
    'Conduje WALKING TRANSFORMATION con zonas STATE → CHANGE (frases cotidianas/profesionales; incluye trampa M41+M42 "She is interesting" → "She got interesting" vs "She is interested" → "She got interested" para entrenar conexion explicita regla 4 pag 335)',
    'Conduje SORTING fisico de tarjetas frase-tarjeta en 4 zonas (GET / BECOME / GO / TURN) + cohorte armo 1 frase por cada zona usando una tarjeta de esa zona',
    'Conduje HISTORIA INTERACTIVA absurda cotidiana profesional "The Office Transformation Tuesday" con pausas (cohorte agrego got tired/got excited/became a manager/went crazy/turned 50 EN VOZ ALTA en cada pausa, NO huecos para llenar; pase por intern/developer/marketing manager/compliance officer/proyecto/equipo/YOU)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjetas "Subject + GET/BECOME/GO/TURN + adj/noun/number + complemento contextual" (visible la estructura completa)',
    'Conduje STATION ROTATION 3 estaciones (CUERPO / EMOCION / SITUACION) usando Practice Guide p.338-339 tabla 5 tiempos verbatim',
    'Conduje PODIUM CEREMONY "Right Change" (cadena STATE-sentence + CHANGE-sentence con coro "Confirmed - right change!" cubriendo al menos 1 par por cada tipo: GET, BECOME, GO, TURN)',
    'Conduje SPEED DRILL DE PIE en 5 tiempos (Practice Guide p.338-339: gets/got/will get/is getting/was getting) sobre al menos 4 sujeto-adjetivo pares (the dog tired / my marks low / the day late / your hair long / my friends married / I bored)',
    'Conduje SPEED DRILL reversal trap rapido (cohorte corrige EN VOZ ALTA frases con verbo equivocado tipo "she become angry" -> "she GOT angry!"; "she went confused" -> "she GOT confused!"; "I am turning tired" -> "I am GETTING tired!"; "she is turning patient" -> "she is BECOMING patient!"; "the team got crazy" -> "the team WENT crazy!"; "our supervisor got 50" -> "our supervisor TURNED 50!")',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 30, Cl 29, Cl 28, Cl 23, Cl 19, Cl 18)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + nota M40 NO existe + nota M43 jueves + nota JUSTICIA v2 dia 2 manana',
    'En Tarea explique el por que + due date explicito (jueves 11/06 antes 7AM)',
    'Tarea es 30-45 min (regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 32 jueves 11/06 (M42 fue hoy; sigue M43 "How Do You Do?" / Adverbs of Manner - verbatim linea 24275 — adverbios de manera en ubicacion correcta + distinguir frecuencia vs manera)',
    'ANUNCIE explicitamente al cierre que manana Cl 32 continua JUSTICIA v2 dia 2 (apertura JUSTICIA hoy con dia 1 — nuevo bloque, nueva virtud)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase31_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 31 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M42 GETTING CRAZY! / CHANGES OF STATE | JUSTICIA dia 1 v2 - APERTURA DEL BLOQUE',
    'A2 Book M42 "Getting Crazy!" / Changes of State (modulo p.333+; Vocabulario p.334 con to lose/perder, to hurt/lastimar, to scare/asustar, to marry/casarse + huge/enorme, far/lejos, tough/duro-informal, quiet/quieto, active/activo, famous/famoso; Guia 1 p.335 regla canonica verbatim — (1) si no estuve enfermo antes pero ahora estoy ocurrio un cambio de estado; (2) espanol usa muchos verbos con reflexivos se/me/te; (3) ingles usa "to get" o (muy formalmente) "to become" — esto puede ser usado en cualquier tiempo; (4) los adjetivos de participio M41 se usan muy frecuentemente de esta manera con get/became — She got interested in the class / She got interesting after university; tabla Before/Change/After verbatim: not sick → I get sick / not happy → we get happy / not angry → she gets angry / not lost → I got lost; Ejemplos 1 p.336 verbatim ~20 frases — Camila got bored, My sister got tall, Miguel got tired, James got surprised, Dont get lost in Bogota, I got sick last night, If you dont keep learning you will get boring, Liam got excited, I got sad, I got confused, If I do not call my mother will get worried, I got hurt playing soccer, iPhones got huge in the US, The class got quiet before the test, The dog got lost in Piedecuesta, etc.; Ejercicios 1 p.337; Practice Guide p.338-339 tabla 5 tiempos The dog gets/got/will get/is getting/was getting tired aplicada a dog tired, day late, my marks low, your hair long, the boys active, my friends married, I bored in the Spanish class, the book boring) + extension canonica Heiiu consistente fuera de p.333-339 (GO + adj idiomatico: crazy/red/bald/quiet/pale; TURN + edad/color: turn 30 / turn red) + Board Race GET vs BECOME vs GO vs TURN + Walking Transformation con zonas STATE → CHANGE (incluye trampa M41+M42 "interesting/interested" — regla 4 p.335) + Sorting fisico de tarjetas frase-tarjeta en 4 zonas (GET / BECOME / GO / TURN) + Historia interactiva ABSURDA cotidiana profesional "The Office Transformation Tuesday" con pausas (cohorte agrega got tired/got excited/became a manager/went crazy/turned 50 EN VOZ ALTA, NO huecos) + Human-Sentence Line-up con tarjetas "Subject + GET/BECOME/GO/TURN + adj/noun/number + complemento" + Station Rotation 3 estaciones (cuerpo / emocion / situacion con Practice Guide tabla 5 tiempos) + Podium Ceremony "Right Change" + Speed Drill en 5 tiempos + reversal trap + FRASE DEL DIA (Goldlist retirado) + JUSTICIA dia 1 v2 - APERTURA DEL BLOQUE (right verb for the right change, open the block clean; ayer Cl 30 cerro TEMPLANZA v2 dia 5; manana Cl 32 continua JUSTICIA v2 dia 2 con M43 Adverbs of Manner) (M40 NO EXISTE - auditado Cl 30 verbatim linea 22871; SIN texto Heiiu - gramatica estructural sobre verbos de cambio de estado; profesor NUNCA comunica resultados/criterios del Final - exclusivo coordinacion; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 32 jueves 11/06 = M43 "How Do You Do?" / Adverbs of Manner - verbatim linea 24275 A2 Book - formar y usar adverbios de manera en ubicacion correcta + distinguir adverbios de frecuencia vs manera + JUSTICIA v2 dia 2)',
    b1_c31_g_act, b1_c31_g_deliv, b1_c31_g_eval, S,
)
print('OK: B1_Clase31_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para miercoles 10/06 B1 MASTERY Cl 31:')
print('  - B1/B1_Clase31_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase31_CONV_REPORTE.pdf')
print('  - B1/B1_Clase31_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase31_GRAMMAR_REPORTE.pdf')
