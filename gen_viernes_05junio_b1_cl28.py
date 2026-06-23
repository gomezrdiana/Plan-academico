#!/usr/bin/env python3
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 28 (viernes 05/06/2026):
- Bloque 1 CONV (Danna, va PRIMERO): aplicacion oral de Order of Adjectives
  (Hot Topic "Two Right Words Beat Ten Loud Ones" + Simulacion "The Lost &
  Found Desk") + Page 26 MY DISCIPLINED CADENCE / WHAT I REPEAT EVERY WEEK
  Draft 1 (escritura en clase, alimenta segunda mitad del proyecto hacia
  Final Cl 44) + Frase del Dia + TEMPLANZA dia 3 v2
- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): A2 Book M38 Order
  of Adjectives (modulo p.313+; Reglas p.313; Ejemplos p.314; Ejercicios p.315;
  Practica Verbal Practice Guide p.316) — secuencia CANTIDAD -> OPINION ->
  TAMANO -> EDAD -> FORMA -> COLOR -> ORIGEN -> MATERIAL -> SUSTANTIVO +
  Podium Ceremony "Right Order" + Historia interactiva absurda profesional +
  Frase del Dia + TEMPLANZA dia 3 v2
  (M35 NO existe en el A2 Book — el libro salta de M34 a M36; auditado;
  patron consistente con M19/M25/M31 ya saltados.)
- SIN texto Heiiu nuevo (mismo criterio que Cl 14-27: gramatica
  estructural, no narrativa).
- Anuncio Cl 29 lunes 08/06 = M39 "Mine, All Mine" / Possessive Pronouns —
  confirmar verbatim antes de clase (M40 historicamente NO existe — auditar
  antes de Cl 30).
- Anuncio Final Cl 44 como hecho de cronograma en el cierre (sin
  nota/criterios — eso es coordinacion).
- Profesor NUNCA comunica resultados/notas/criterios del Final; si alguien
  pregunta: "Coordination handles results — not me. Focus on what comes
  next."
- Tarea fin de semana: due lunes 08/06 antes 7AM, 45-60 min (extra por fin
  de semana, dentro de regla), NO fragmentada.
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
# B1 Cl 28 CONV (Danna) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase28_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase28_CONV_GUIA.pdf'),
)
print('OK: B1_Clase28_CONV_GUIA.pdf')

b1_c28_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 27 Conv)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS TEMPLANZA dia 3 (v2) - 2-3 adjetivos en orden, no 10 sueltos', '7 min'),
    ('PEER TEACHER SLOT (errores del PASE de Juan Diego - Cl 27 Grammar M37)', '7 min'),
    ('HOT TOPIC - "Two Right Words Beat Ten Loud Ones" (orden de adjetivos, oral, profesional)', '17 min'),
    ('SIMULACION - "The Lost & Found Desk" (DE PIE, profesional, describir objetos/personas en orden correcto)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 26 - MY DISCIPLINED CADENCE / WHAT I REPEAT EVERY WEEK Draft 1 (escritura en clase anti-fraude, alimenta segunda mitad hacia Final Cl 44)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea fin de semana + Anuncio Cl 29 + Anuncio Final + Cierre', '7 min'),
]
b1_c28_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER (usando PASE de Juan Diego Cl 27 Grammar M37)',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video de The Lost & Found Desk simulacion',
    'Foto/video Mini-Pitch',
    'N Paginas 26 MY DISCIPLINED CADENCE / WHAT I REPEAT EVERY WEEK DRAFT 1 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista de quienes NO entregaron tarea Cl 27 (con NOMBRE)',
    'Notas individuales de estudiantes en riesgo (libreta aparte, NO en la guia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio Cl 29 lunes 08/06 = M39 "Mine, All Mine" / Possessive Pronouns (pendiente verbatim)',
]
b1_c28_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (2-3 adjetivos en orden)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui',
    'Verifique virtud CL 28 = TEMPLANZA dia 3 v2 (por numero de clase, Cl 26-30)',
    'Hile TEMPLANZA en VATS como dia 3 v2 (orden + dosificacion: 2-3 adjetivos, no 10; "every adjective in its right place")',
    'NO ensene gramatica nueva (Conv = aplicacion oral; Grammar formaliza esta tarde con M38)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-27)',
    'RECIBI el PASE escrito de Juan Diego (Cl 27 Grammar M37) para el Peer Teacher',
    'Conduje Hot Topic "Two Right Words Beat Ten Loud Ones" con requirements en tablero (2-3 adjetivos en orden natural)',
    'Conduje The Lost & Found Desk (describir 5-6 items/personas perdidos en orden correcto, DE PIE)',
    'Simulacion fue PROFESIONAL/realista cotidiana (no familiar ni fantasiosa)',
    'Conduje escritura Page 26 MY DISCIPLINED CADENCE / WHAT I REPEAT EVERY WEEK Draft 1 EN CLASE (anti-fraude IA; alimenta segunda mitad hacia Final Cl 44)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica (2-3 adjetivos en orden ya en boca del cohorte)',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique el por que + due date explicito (lunes 08/06 antes 7AM)',
    'Tarea es 45-60 min (extra por fin de semana, dentro de regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo" (tienen sabado y domingo enteros)',
    'Anuncie Cl 29 lunes 08/06',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase28_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 28 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'Aplicacion oral de Order of Adjectives: Hot Topic "Two Right Words Beat Ten Loud Ones" + Simulacion "The Lost & Found Desk" (describir objetos/personas perdidos en orden correcto: TAM antes de COLOR, OPIN antes de TAM, EDAD antes de COLOR antes de ORIGEN) + Page 26 MY DISCIPLINED CADENCE / WHAT I REPEAT EVERY WEEK Draft 1 anti-fraude (alimenta segunda mitad del proyecto hacia Final Cl 44) + FRASE DEL DIA + PASE a Juan Diego + TEMPLANZA dia 3 v2 (SIN texto Heiiu - gramatica estructural, mismo criterio que Cl 14-27; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 29 lunes 08/06 = M39 "Mine, All Mine" / Possessive Pronouns pendiente verbatim)',
    b1_c28_c_act, b1_c28_c_deliv, b1_c28_c_eval, S,
)
print('OK: B1_Clase28_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 28 GRAMMAR (Juan Diego) - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase28_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase28_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase28_GRAMMAR_GUIA.pdf')

b1_c28_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado - tarea Cl 27 = M37) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion - DE PIE', '4 min'),
    ('VATS TEMPLANZA dia 3 v2 (orden + dosificacion: 2-3 adjetivos, no 10) - DE PIE', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna - Cl 28 Conv) - DE PIE', '7 min'),
    ('LIBRO M38 Order of Adjectives (modulo p.313+; Reglas p.313 con secuencia 1..9) + BOARD RACE - DE PIE', '12 min'),
    ('WALKING TRANSFORMATION M38 reordenar 3 adjetivos mal puestos a secuencia correcta - DE PIE', '16 min'),
    ('LIBRO M38 (cont.) Ejemplos pag 314 verbatim + SORTING fisico por CATEGORIA de adjetivo (8 zonas: CANT/OPIN/TAM/EDAD/FORMA/COLOR/ORIGEN/MATERIAL) + Historia interactiva ABSURDA cotidiana profesional - DE PIE', '12 min'),
    ('HUMAN-SENTENCE LINE-UP (con tarjetas-CATEGORIA) + STATION ROTATION - 3 estaciones (TAM+COLOR / OPIN+TAM+COLOR / EDAD+COLOR+ORIGEN) - DE PIE', '12 min'),
    ('PODIUM CEREMONY "Right Order" + SPEED DRILL DE PIE - reordenar en cadena + cohorte nombra categorias en voz alta', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE - DE PIE', '12 min'),
    ('PASE ESCRITO a Danna + Tarea fin de semana + Anuncio Cl 29 (M39) + Anuncio Final Cl 44 + Cierre', '14 min'),
]
b1_c28_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M38 secuencia 1..9 + ejemplos pag 314',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto/video del Board Race (estudiantes en el tablero)',
    'Foto/video de la Walking Transformation (zonas WRONG/RIGHT)',
    'Foto/video del Sorting fisico por CATEGORIA de adjetivo (8 zonas) + Historia interactiva absurda profesional + Human-Sentence Line-up (con tarjetas-CATEGORIA) + Station Rotation',
    'Foto/video del PODIUM CEREMONY "Right Order"',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 27 (con NOMBRE)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que % del bloque fue realmente DE PIE',
    'Cuantas veces te preguntaron resultado/criterios del Final y respondiste "Coordination handles results"',
    'Confirmaste anuncio de Final Cl 44 como hecho de cronograma (sin nota/criterios)',
    'Confirmaste anuncio M39 lunes Cl 29 08/06 (pendiente verbatim) + nota M35 NO existe (saltado entre M34 y M36)',
]
b1_c28_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'Verifique con mis propios ojos que el modulo anterior fue M37 (Cl 27); M35 NO existe (saltado entre M34 y M36)',
    'Lei en voz alta las reglas del libro que voy a citar (sin parafrasear)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE tarjetas-CATEGORIA grandes (CANT/OPIN/TAM/EDAD/FORMA/COLOR/ORIGEN/MATERIAL/NOUN) para line-up + tarjetas de adjetivos sueltos + sustantivos para sorting y stations ANTES',
    'PREPARE la HISTORIA INTERACTIVA absurda cotidiana profesional con pausas marcadas (cohorte agrega 2-3 adjetivos en orden EN VOZ ALTA, no huecos)',
    'PREPARE el PODIO en el tablero ANTES de clase',
    'DESPEJE espacio para movimiento (board race + walking transformation + line-up + podium + 8 zonas sorting)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (sin nota, sin criterios, sin resultado - exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results — not me. Focus on what comes next." y segui el libro',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Verifique virtud CL 28 = TEMPLANZA dia 3 v2 (por numero de clase, Cl 26-30)',
    'Cubri M38 Order of Adjectives DESDE EL LIBRO (A2 Book modulo p.313+; Reglas p.313 secuencia 1..9; Ejemplos p.314; Ejercicios p.315; Practica Verbal Practice Guide p.316) citando reglas verbatim',
    'Explique la secuencia 1..9: CANTIDAD -> OPINION/CALIDAD -> TAMANO -> EDAD -> FORMA -> COLOR -> ORIGEN/NACIONALIDAD -> MATERIAL/USO -> SUSTANTIVO',
    'Use ejemplos verbatim del libro pag 314 (I have a big black car / I want a small red car / Jenna has long red hair / etc.)',
    'Reforce TEMPLANZA: 2-3 adjetivos, NUNCA 5+; orden, no volumen; cada adjetivo en su lugar',
    'CONFIRME que M35 NO existe en el A2 Book (el libro salta de M34 a M36) - verificado verbatim, patron consistente con M19/M25/M31 ya saltados',
    'NO ensene M39 "Mine, All Mine" (es Cl 29 lunes 08/06) ni Third Conditional / Could-Should have',
    'NO re-ensene M33/M34 (Cl 24-25), M36/M37 (Cl 26-27) - solo reciclaje natural en ejemplos (ropa, descripcion personas)',
    'NO use texto Heiiu (gramatica estructural - mismo criterio que Cl 14-27)',
    'Conduje BOARD RACE M38 (2 equipos en el tablero, reordenar frases)',
    'Conduje WALKING TRANSFORMATION (zonas WRONG/RIGHT, frases cotidianas/profesionales)',
    'Conduje SORTING fisico por CATEGORIA de adjetivo (8 zonas, tarjetas individuales)',
    'Conduje HISTORIA INTERACTIVA absurda cotidiana profesional con pausas (cohorte agrego 2-3 adjetivos en orden EN VOZ ALTA, NO huecos para llenar)',
    'Conduje HUMAN-SENTENCE LINE-UP con tarjetas-CATEGORIA (visible que orden = secuencia 1..9)',
    'Conduje STATION ROTATION 3 estaciones (TAM+COLOR / OPIN+TAM+COLOR / EDAD+COLOR+ORIGEN)',
    'Conduje PODIUM CEREMONY "Right Order" (cadena con coro "Confirmed - right order!")',
    'Conduje SPEED DRILL DE PIE (cadena reordenar + coro categorias)',
    'MANTUVE el bloque ~70%+ DE PIE / movimiento (objetivo ~85%, como Cl 23, Cl 19, Cl 18)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica + nota M35 NO existe + nota M39 lunes (pendiente verbatim)',
    'En Tarea explique el por que + due date explicito (lunes 08/06 antes 7AM)',
    'Tarea es 45-60 min (extra por fin de semana, dentro de regla B1), NO fragmentada',
    'NO acepte la excusa "no me da tiempo" (tienen sabado y domingo enteros)',
    'Anuncie siguiente modulo existente del A2 Book para Cl 29 lunes 08/06 (M35 NO existe; M36 fue Cl 26; M37 fue Cl 27; M38 fue hoy; sigue M39 "Mine, All Mine" / Possessive Pronouns - confirmar verbatim; M40 historicamente NO existe - auditar antes de Cl 30)',
    'Anuncie Final Cl 44 como hecho de cronograma SOLO (sin nota, sin criterios)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase28_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 28 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | M38 ORDER OF ADJECTIVES (M35 NO EXISTE)',
    'A2 Book M38 Order of Adjectives (modulo p.313+; Reglas p.313 con secuencia 1..9 verbatim: CANTIDAD -> OPINION/CALIDAD -> TAMANO -> EDAD -> FORMA -> COLOR -> ORIGEN/NACIONALIDAD -> MATERIAL/USO -> SUSTANTIVO; Ejemplos p.314 verbatim; Ejercicios p.315 "Agrega los adjetivos a la frase dada en el orden correcto"; Practica Verbal Practice Guide p.316 "Traduce las frases usando el orden de adjetivos correcto") + Board Race + Walking Transformation + Sorting fisico por CATEGORIA de adjetivo (8 zonas: CANT/OPIN/TAM/EDAD/FORMA/COLOR/ORIGEN/MATERIAL) + Historia interactiva ABSURDA cotidiana profesional con pausas (cohorte agrega 2-3 adjetivos en orden EN VOZ ALTA, NO huecos) + Human-Sentence Line-up (con tarjetas-CATEGORIA) + Station Rotation (TAM+COLOR / OPIN+TAM+COLOR / EDAD+COLOR+ORIGEN) + Podium Ceremony "Right Order" + Speed Drill DE PIE + FRASE DEL DIA (Goldlist retirado) + TEMPLANZA dia 3 v2 (orden + dosificacion: 2-3 adjetivos, NUNCA 5+) (M35 NO EXISTE - el libro salta de M34 a M36; verificado verbatim; patron consistente con M19/M25/M31 ya saltados; SIN texto Heiiu - gramatica estructural; profesor NUNCA comunica resultados/criterios del Final - exclusivo coordinacion; anuncio Final Cl 44 SOLO como hecho de cronograma; anuncio Cl 29 lunes 08/06 = M39 "Mine, All Mine" / Possessive Pronouns pendiente verbatim — M40 historicamente NO existe)',
    b1_c28_g_act, b1_c28_g_deliv, b1_c28_g_eval, S,
)
print('OK: B1_Clase28_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para viernes 05/06 B1 MASTERY Cl 28:')
print('  - B1/B1_Clase28_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase28_CONV_REPORTE.pdf')
print('  - B1/B1_Clase28_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase28_GRAMMAR_REPORTE.pdf')
