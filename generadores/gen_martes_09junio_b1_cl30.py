#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 30 (martes 09/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Participle Adjectives
  (Hot Topic "What is ENGAGING vs DRAINING in my work week?" + Simulacion
  "The Engagement Survey" con Guest Observer Pattern — 1 guest consultor,
  group observer, profesora coach) + Page 28 WHAT ENGAGES ME / WHAT DRAINS
  ME (and what that means for my long-term project) Draft 1 (escritura en
  clase anti-fraude IA; alimenta segunda mitad del proyecto hacia Final
  Cl 44) + Frase del Dia + TEMPLANZA dia 5 v2 (CIERRE del bloque)
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M41
  "This Is Interesting!" / Participle Adjectives (modulo p.326+;
  Vocabulario p.327 con 15 pares verbatim boring/bored, depressing/
  depressed, disappointing/disappointed, exciting/excited, interesting/
  interested, surprising/surprised, tiring/tired, amazing/amazed,
  annoying/annoyed, confusing/confused, distracting/distracted,
  embarrassing/embarrassed, frustrating/frustrated, relaxing/relaxed,
  worrying/worried; Guia 1 p.328 regla canonica verbatim — participio
  PRESENTE -ing para producir el efecto / participio PASADO -ed para
  sentirlo; Ejemplos 1 p.329 verbatim; Ejercicios 1 p.330; Practice Guide
  p.331-332) + Board Race -ING vs -ED + Walking Transformation con zonas
  CAUSE→-ING / FEELING→-ED + Sorting fisico tarjetas adjetivo (2 zonas) +
  Historia interactiva absurda profesional "The Office Energy Audit"
  (cohorte responde EN VOZ ALTA boring/bored/exciting/excited/tiring/tired
  en cada pausa) + Human-Sentence Line-up "Subject + BE + -ING/-ED +
  (preposition)" + Station Rotation 3 estaciones (pares boring/bored /
  exciting/excited / tiring-tired + confusing-confused) + Podium Ceremony
  "Right Participle" + Speed Drill con reversal trap + Frase del Dia +
  TEMPLANZA dia 5 v2 (CIERRE del bloque)
  (M40 NO existe en el A2 Book — el libro salta de M39 a M41; auditado
  verbatim linea 22871; patron consistente con M19/M25/M31/M35 ya saltados.)
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-29: gramatica
  estructural sobre formacion de adjetivos a partir de participios, no
  narrativa).
- Anuncio Cl 31 miercoles 10/06 = M42 "Getting Crazy!" / Changes of State
  (verbatim linea 23529 A2 Book — verbo 'to get' para cambios de estado y
  de animo; presente, pasado, futuro, formas continuas) + JUSTICIA v2 dia
  1 (cierre TEMPLANZA hoy con dia 5, apertura JUSTICIA manana — calendario
  absoluto Heiiu).
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin
  nota/criterios — eso es coordinacion).
- Profesor NUNCA comunica resultados/notas/criterios del Final; si alguien
  pregunta: "Coordination handles results — not me. Focus on what comes
  next."
- Tarea Cl 30: due miercoles 10/06 antes 7AM, 30-45 min, NO fragmentada.
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
# B1 Cl 30 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase30_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase30_CONV_GUIA.pdf'),
)
print('OK: B1_Clase30_CONV_GUIA.pdf')

b1_c30_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 29 Conv = Page 27 What Is Mine + audio Whose-Is-This + reading 5 oraciones con posesivos + TED ownership listening)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS TEMPLANZA dia 5 v2 (CIERRE del bloque Cl 26-30 - manana abre JUSTICIA v2 dia 1): nombrar la energia de la semana con -ING (causa) / -ED (persona), cierre limpio', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 29 Grammar M39 Possessive Pronouns: adjetivo posesivo en posicion de objeto)', '7 min'),
    ('HOT TOPIC - "What is ENGAGING vs DRAINING in my work week?" (-ING/-ED en contexto profesional)', '17 min'),
    ('SIMULACION - "The Engagement Survey" (DE PIE, Guest Observer Pattern: 1 guest consultor + group observer + profesora coach - profesora NO juega guest; consultor entrevista al cohorte sobre engaging/draining/exciting/excited/tiring/tired/confusing/confused)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 28 - WHAT ENGAGES ME / WHAT DRAINS ME (and what that means for my long-term project) Draft 1 (escritura en clase anti-fraude IA; alimenta segunda mitad hacia Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea Cl 30 + Anuncio Cl 31 (M42 "Getting Crazy!" + JUSTICIA v2 dia 1) + Anuncio Final + Cierre', '7 min'),
]
b1_c30_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego Cl 29 Grammar M39)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Engagement Survey simulacion (Guest Observer Pattern: 1 guest consultor, group observer, profesora coach)',
    'Foto/video Mini-Pitch',
    'N Paginas 28 WHAT ENGAGES ME / WHAT DRAINS ME DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 29 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio Cl 31 miercoles 10/06 = M42 "Getting Crazy!" / Changes of State (verbatim linea 23529 A2 Book) + JUSTICIA v2 dia 1 (cierre TEMPLANZA hoy con dia 5)',
]
b1_c30_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE cartelitos "ENGAGING" y "DRAINING" en tarjetas grandes + clipboard para Consultor (Engagement Survey)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (-ING para causa + -ED para persona)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui',
    'Verifique virtud CL 30 = TEMPLANZA dia 5 v2 - ULTIMO del bloque (Cl 26-30); manana Cl 31 abre JUSTICIA v2 dia 1',
    'Hile TEMPLANZA en VATS como dia 5 v2 - CIERRE del bloque: nombrar la energia de la semana con la forma correcta (-ing causa, -ed persona), sin inflar, sin estirar',
    'ANUNCIE explicitamente al cierre que manana Cl 31 abre JUSTICIA v2 dia 1 (nuevo bloque, nueva virtud)',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza en el segundo bloque con M41)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-29)',
    'RECIBI el PASE escrito de Juan Diego (Cl 29 Grammar M39 Possessive Pronouns) para el Peer Teacher',
    'Conduje Hot Topic "What is ENGAGING vs DRAINING in my work week?" con requirements en tablero (6+ pares -ING/-ED + 2+ cosas work-specific + 1 TEMPLANZA closure)',
    'Conduje The Engagement Survey con Guest Observer Pattern (1 guest consultor rotante + group observer que cuenta pares + profesora COACH NO juega guest)',
    'Simulacion fue PROFESIONAL/realista cotidiana (no familiar ni fantasiosa)',
    'Conduje escritura Page 28 WHAT ENGAGES ME / WHAT DRAINS ME (and what that means for my long-term project) Draft 1 EN CLASE (anti-fraude IA; alimenta segunda mitad hacia Final Cl 44)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica (pares -ING/-ED ya en boca del cohorte; patron mas comun: invertir formas)',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (miercoles 10/06 antes 7AM)',
    'Tarea es 30-45 min (regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 31 miercoles 10/06 = M42 "Getting Crazy!" / Changes of State (verbatim linea 23529 A2 Book — verbo to get para cambios de estado y de animo) + JUSTICIA v2 dia 1 (cierra TEMPLANZA hoy con dia 5, abre JUSTICIA manana)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase30_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 30 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado) | TEMPLANZA dia 5 v2 - CIERRE DEL BLOQUE',
    'Aplicacion oral de Participle Adjectives: Hot Topic "What is ENGAGING vs DRAINING in my work week?" + Simulacion "The Engagement Survey" (DE PIE, Guest Observer Pattern: 1 guest consultor + group observer + profesora coach - profesora NO juega guest; consultor entrevista al cohorte con 6+ pares -ING/-ED naturales + TEMPLANZA closure honesta) + Page 28 WHAT ENGAGES ME / WHAT DRAINS ME (and what that means for my long-term project) Draft 1 anti-fraude IA (alimenta segunda mitad del proyecto hacia Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + TEMPLANZA dia 5 v2 (CIERRE del bloque Cl 26-30 — manana Cl 31 abre JUSTICIA v2 dia 1) (SIN texto Heiiu - gramatica estructural sobre formacion de adjetivos a partir de participios, mismo criterio que Cl 14-29; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 31 miercoles 10/06 = M42 "Getting Crazy!" / Changes of State — verbatim linea 23529 A2 Book — verbo to get para cambios de estado y de animo + JUSTICIA v2 dia 1; M40 NO existe — auditado verbatim linea 22871)',
    b1_c30_c_act, b1_c30_c_deliv, b1_c30_c_eval, S,
)
print('OK: B1_Clase30_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 30 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase30_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase30_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase30_GRAMMAR_GUIA.pdf')

b1_c30_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 29 = M39 Possessive Pronouns 12 frases + audio Whose-Is-This + reading 5 oraciones + TED ownership) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS TEMPLANZA dia 5 v2 (CIERRE del bloque Cl 26-30 - manana abre JUSTICIA v2 dia 1): nombrar la forma correcta del adjetivo (-ing causa, -ed feeler), cierre limpio - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna - Cl 30 Conv: invierten formas -ING/-ED) - DE PIE', '7 min'),
    ('LIBRO M41 This Is Interesting! / Participle Adjectives (modulo p.326+; Vocabulario p.327 con 15 pares verbatim boring/bored, exciting/excited, tiring/tired, interesting/interested, confusing/confused, etc.; Guia 1 p.328 regla canonica verbatim — participio PRESENTE -ing para crear el efecto / participio PASADO -ed para sentirlo; tabla canonica del libro: "The teacher is boring / The student is bored", "He is amazing / She is amazed"; M40 NO existe — auditado verbatim linea 22871 A2 Book) + BOARD RACE (clasificar -ING vs -ED en oraciones invertidas / incompletas) - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M41 con zonas CAUSE → -ING / FEELING → -ED - caminar de la forma incorrecta a la correcta segun rol del sujeto - DE PIE', '16 min'),
    ('LIBRO M41 (cont.) Ejemplos p.329 verbatim (This is a really boring book / Mark was sleeping in the class. He was really bored / Julio is always sad. He is very depressing / Santiago is very interested in the English class / The soccer game was very exciting / Running the Boston Marathon is really tiring / Did Juan wake up early today? I am amazed / My little brother is very annoying / The teacher is annoyed / The movie was very confusing / I was very distracted / It was very embarrassing!) + SORTING fisico tarjetas adjetivo (interesting/interested/boring/bored/exciting/excited/tiring/tired/confusing/confused/frustrating/frustrated/relaxing/relaxed/annoying/annoyed/amazing/amazed/surprising/surprised/embarrassing/embarrassed/depressing/depressed/disappointing/disappointed/distracting/distracted/worrying/worried) en 2 zonas (CAUSE / FEELING) + Historia interactiva ABSURDA profesional "The Office Energy Audit" (cohorte responde EN VOZ ALTA boring/bored/exciting/excited/tiring/tired/confusing/confused/depressing/depressed/relaxing/relaxed/amazing/amazed/interesting/interested en cada pausa) - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP con tarjetas "Subject + BE + -ING/-ED + (preposition)" + STATION ROTATION - 3 estaciones (pares boring/bored / pares exciting/excited / pares tiring-tired + confusing-confused) - DE PIE', '12 min'),
    ('PODIUM CEREMONY "Right Participle" + SPEED DRILL DE PIE - cadena Cause-sentence + Feeling-sentence + reversal trap rapido', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea Cl 30 + Anuncio Cl 31 (M42 "Getting Crazy!" + JUSTICIA v2 dia 1) + Anuncio Final Cl 44 + Cierre', '14 min'),
]
b1_c30_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M41 regla canonica pag 328 + Vocabulario pag 327 + Ejemplos pag 329',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero clasificando -ING vs -ED)',
    'Foto/video de la Walking Transformation con zonas CAUSE → -ING / FEELING → -ED',
    'Foto/video del Sorting fisico de tarjetas adjetivo en 2 zonas (CAUSE / FEELING) + Historia interactiva absurda profesional "The Office Energy Audit" + Human-Sentence Line-up + Station Rotation',
    'Foto/video del PODIUM CEREMONY "Right Participle"',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 29 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Cuantas veces te preguntaron resultado/criterios del Final y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio M42 miercoles Cl 31 10/06 (M40 ya auditado como inexistente; M41 fue HOY; M42 verbatim linea 23529 A2 Book)',
    'Confirmaste anuncio JUSTICIA v2 dia 1 manana (cierre TEMPLANZA dia 5 hoy, apertura JUSTICIA manana — calendario absoluto)',
]
b1_c30_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Verifique con mis propios ojos que el modulo anterior fue M39 (Cl 29 lunes); M40 NO existe (el libro salta de M39 a M41 verbatim, linea 22871 A2 Book)',
    'Verifique con mis propios ojos que el modulo siguiente para Cl 31 manana es M42 "Getting Crazy!" / Changes of State (verbatim, linea 23529 A2 Book)',
    'Lei en voz alta las reglas del libro pag 328 que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas-ADJETIVO -ING grandes (interesting/boring/exciting/tiring/confusing/frustrating/relaxing/annoying/amazing/surprising/embarrassing/depressing/disappointing/distracting/worrying) + tarjetas-ADJETIVO -ED (interested/bored/excited/tired/confused/frustrated/relaxed/annoyed/amazed/surprised/embarrassed/depressed/disappointed/distracted/worried) + tarjetas-SUJETO CAUSE (the meeting/the project/the policy/the report/ten hours of email/the Friday status/the dashboard/the new client) + tarjetas-SUJETO FEELER (I/the team/the boss/my colleague/the cohort/the supervisor) para line-up, sorting y stations ANTES',
    'PREPARE la HISTORIA INTERACTIVA absurda cotidiana profesional "The Office Energy Audit" con pausas marcadas (cohorte agrega EN VOZ ALTA boring/bored/exciting/excited/tiring/tired/confusing/confused en cada pausa, NO huecos)',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation con zonas CAUSE/FEELING + line-up + podium + 2 zonas sorting + 3 stations)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui el libro',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 30 = TEMPLANZA dia 5 v2 - ULTIMO del bloque (Cl 26-30); manana Cl 31 abre JUSTICIA v2 dia 1',
    'Cubri M41 This Is Interesting! / Participle Adjectives DESDE EL LIBRO (A2 Book modulo p.326+; Vocabulario p.327 con 15 pares verbatim; Guia 1 p.328 regla canonica; Ejemplos 1 p.329; Ejercicios 1 p.330; Practice Guide p.331-332) citando reglas y ejemplos verbatim',
    'Explique la regla canonica del libro p.328 verbatim: (1) espanol usa "ser/estar" para distinguir causa/feeler; (2) ingles usa participio PRESENTE (-ing) para la cosa/persona que CREA el efecto; (3) participio PASADO (-ed) para la persona que SIENTE el efecto; (4) algunos participios pasados son irregulares (Lose -> Lost: "We are lost.")',
    'Use la tabla canonica del libro p.328: "The teacher is BORING / The student is BORED", "He is AMAZING / She is AMAZED"',
    'Use el vocabulario verbatim del libro p.327 (15 pares: boring/bored, depressing/depressed, disappointing/disappointed, exciting/excited, interesting/interested, surprising/surprised, tiring/tired, amazing/amazed, annoying/annoyed, confusing/confused, distracting/distracted, embarrassing/embarrassed, frustrating/frustrated, relaxing/relaxed, worrying/worried)',
    'Use ejemplos verbatim del libro p.329 (This is a really boring book / Mark was sleeping in the class. He was really bored / I was very depressed after the sad movie / Julio is always sad. He is very depressing / Monica is disappointed that her father cannot visit / Santiago is very interested in the English class / My marks were very disappointing last year / The soccer game was very exciting / Running the Boston Marathon is really tiring / Did Juan wake up early today? Im amazed / The movie was very confusing. I didnt understand it / etc.)',
    'Reforce TEMPLANZA dia 5 - CIERRE: right shape on right side (-ing causa, -ed feeler), cierre del bloque sin estirar; anuncie explicitamente apertura JUSTICIA v2 dia 1 manana',
    'CONFIRME que M40 NO existe en el A2 Book (el libro salta de M39 a M41 verbatim, linea 22871) - patron consistente con M19/M25/M31/M35 ya saltados',
    'NO ensene M42 "Getting Crazy!" / Changes of State (es Cl 31 miercoles 10/06) ni Third Conditional / Could-Should have',
    'NO re-ensene M33/M34 (Cl 24-25), M36/M37/M38 (Cl 26-28), M39 (Cl 29) - solo reciclaje natural en ejemplos',
    'NO use texto Heiiu (gramatica estructural sobre formacion de adjetivos a partir de participios - mismo criterio que Cl 14-29)',
    'Conduje BOARD RACE M41 (2 equipos en el tablero, clasificar -ING vs -ED en oraciones invertidas/incompletas basadas en Vocabulario p.327 + Ejemplos p.329)',
    'Conduje WALKING TRANSFORMATION con zonas CAUSE→-ING / FEELING→-ED (frases cotidianas/profesionales; incluyo trampa "Julio is depressing/depressed" para entrenar pensar el rol del sujeto)',
    'Conduje SORTING fisico de tarjetas adjetivo (-ING vs -ED) en 2 zonas + cohorte armo 6 pares profesionales (boring/bored, exciting/excited, tiring/tired, interesting/interested, confusing/confused, frustrating/frustrated)',
    'Conduje HISTORIA INTERACTIVA absurda cotidiana profesional "The Office Energy Audit" con pausas (cohorte agrego boring/bored/exciting/excited/tiring/tired EN VOZ ALTA, NO huecos para llenar; pase por developer/accountant/marketing manager/compliance officer/cleaning supervisor/auditor)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjetas "Subject + BE + -ING/-ED + (preposition)" (visible la estructura completa)',
    'Conduje STATION ROTATION 3 estaciones (Pares boring/bored / Pares exciting/excited / Pares tiring-tired + confusing-confused) con frases verbatim del libro p.329',
    'Conduje PODIUM CEREMONY "Right Participle" (cadena CAUSE-sentence + FEELING-sentence con coro "Confirmed - right participle!" cubriendo al menos 6 pares)',
    'Conduje SPEED DRILL DE PIE con reversal trap (cohorte corrige EN VOZ ALTA frases invertidas tipo "I am exciting" -> "I am EXCITED!")',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 29, Cl 28, Cl 23, Cl 19, Cl 18)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + nota M40 NO existe + nota M42 miercoles + nota JUSTICIA v2 dia 1 manana',
    'En Tarea explique el por que + due date explicito (miercoles 10/06 antes 7AM)',
    'Tarea es 30-45 min (regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 31 miercoles 10/06 (M41 fue hoy; sigue M42 "Getting Crazy!" / Changes of State - verbatim linea 23529)',
    'ANUNCIE explicitamente al cierre que manana Cl 31 abre JUSTICIA v2 dia 1 (cierre TEMPLANZA hoy con dia 5 — nuevo bloque, nueva virtud)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase30_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 30 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M41 THIS IS INTERESTING! / PARTICIPLE ADJECTIVES (M40 NO EXISTE) | TEMPLANZA dia 5 v2 - CIERRE DEL BLOQUE',
    'A2 Book M41 "This Is Interesting!" / Participle Adjectives (modulo p.326+; Vocabulario p.327 con 15 pares verbatim: boring/bored, depressing/depressed, disappointing/disappointed, exciting/excited, interesting/interested, surprising/surprised, tiring/tired, amazing/amazed, annoying/annoyed, confusing/confused, distracting/distracted, embarrassing/embarrassed, frustrating/frustrated, relaxing/relaxed, worrying/worried; Guia 1 p.328 regla canonica verbatim — participio PRESENTE -ing para la cosa/persona que CREA el efecto / participio PASADO -ed para la persona que SIENTE el efecto / irregulares como Lose->Lost->"We are lost"; tabla canonica del libro: "The teacher is BORING / The student is BORED", "He is AMAZING / She is AMAZED"; Ejemplos 1 p.329 verbatim; Ejercicios 1 p.330; Practice Guide p.331-332 "Traduce la frase" + "Use el evento y adjetivo dados para formar una frase en el pasado") + Board Race -ING vs -ED + Walking Transformation con zonas CAUSE→-ING / FEELING→-ED + Sorting fisico de tarjetas adjetivo en 2 zonas (cause/feeling) + Historia interactiva ABSURDA cotidiana profesional "The Office Energy Audit" con pausas (cohorte agrega boring/bored/exciting/excited/tiring/tired EN VOZ ALTA, NO huecos) + Human-Sentence Line-up con tarjetas "Subject + BE + -ING/-ED + (preposition)" + Station Rotation 3 estaciones (pares boring/bored / exciting/excited / tiring-tired + confusing-confused) + Podium Ceremony "Right Participle" + Speed Drill con reversal trap + FRASE DEL DIA (Goldlist retirado) + TEMPLANZA dia 5 v2 - CIERRE DEL BLOQUE (right shape, right side, cierre limpio; manana Cl 31 abre JUSTICIA v2 dia 1) (M40 NO EXISTE - el libro salta de M39 a M41; verificado verbatim linea 22871 A2 Book.md; patron consistente con M19/M25/M31/M35 ya saltados; SIN texto Heiiu - gramatica estructural sobre formacion de adjetivos a partir de participios; profesor NUNCA comunica resultados/criterios del Final - exclusivo coordinacion; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 31 miercoles 10/06 = M42 "Getting Crazy!" / Changes of State - verbatim linea 23529 A2 Book - verbo to get para cambios de estado y de animo + JUSTICIA v2 dia 1)',
    b1_c30_g_act, b1_c30_g_deliv, b1_c30_g_eval, S,
)
print('OK: B1_Clase30_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para martes 09/06 B1 MASTERY Cl 30:')
print('  - B1/B1_Clase30_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase30_CONV_REPORTE.pdf')
print('  - B1/B1_Clase30_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase30_GRAMMAR_REPORTE.pdf')
