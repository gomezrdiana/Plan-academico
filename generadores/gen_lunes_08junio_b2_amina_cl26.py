#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 26 (lunes 08/06/2026):
- FASE 4 PRACTICA EN CHUNKS dia 6/8 - SEMANA 2 ABRE - ENCADENAMIENTO
  HOOK + PILLAR 1 (SEAM #1). Cl 21-25 cerraron HOOK + 3 PILLARS + CTA
  memorizados individualmente. Hoy abre formalmente la SEMANA 2 = ya
  no se aprenden chunks nuevos, se ENCADENAN los 5 que ya estan
  aprendidos. Primer eslabon: HOOK -> PILLAR 1.
- Centro = PRACTICA ENCADENAMIENTO HOOK+PILLAR 1 SIN PAPEL 45 min en
  3 fases: ALONE 10 min (planning line del seam + memo chained con
  paper) + PAIRS 15 min (drill sin papel, partner B escucha SOLO el
  seam y flag 1 observacion) + MINI-AUDIENCIA 20 min (cada estudiante
  HOOK+SEAM+PILLAR 1 de memoria + 1 observacion del grupo SOBRE EL
  SEAM). + Recap completo 9 min (1 vez mas sin coaching).
- Refresh mental 2 min ANTES de la practica: HOOK individual + PILLAR
  1 individual SILENCIOSO (mental, no out loud) - confirma que las 2
  piezas siguen vivas antes de unirlas con seam. NO es ensayo, es
  chequeo.
- Academic B2 Vocab Set #19 (6 nuevas: bridge/pivot/segue/link/
  transition/connect -> total 114). Set #19 es vocabulario de
  TRANSICION / BRIDGES discursivos / signposting para SEAM #1 y los
  3 seams que vienen; UNA palabra elegida y drillada, no 6
  sampleadas.
- Virtud TEMPLANZA v2 dia 1 (NUEVO BLOQUE, Cl 26-30 TEMPLANZA v2
  ciclo 2). Razon pedagogica directa: encadenar sin templanza =
  apurarse y borrar el trabajo de memorizacion de la semana 1. La
  transicion pide 1 segundo de respiracion real, no atropellarse.
  Cl 25 viernes cerro PRUDENCIA v2 (rotacion estandar cohorte B2
  confirmada Diana 22/05/2026, memoria
  project-b2-virtud-rotacion-estandar).
- ~20 horas / ~14 dias hasta el Final (~22 junio) - derivado de Cl 25
  (~22h/~17d) - 2h netas Cl 26 hoy (verificado calendario:
  22/06/2026 - 08/06/2026 = 14 dias).
- Estructura Fase 4 segun ROADMAP 72h (lineas 120-129): Cl 21-28,
  16h, chunk = 1 min, Cl 21-24 practicaron 1-2 chunks por sesion de
  memoria, Cl 25-28 encadenan 2->3->4->5 chunks. Cl 26 es el PRIMER
  dia del encadenamiento real con voz audible (Cl 25 fue puente que
  cerro aprendizaje individual). Cl 27 = HOOK+P1+P2 (2 seams). Cl 28
  = monologo COMPLETO + C4 (video 3 min memoria a coordinacion;
  ROADMAP lineas 146-153).
- SEAM #1 = closing marker firme del HOOK + 1 segundo de breath
  real + opening marker casual del PILLAR 1 + bridge formal->casual
  + 1 anchor word que camina + opcional 1 palabra Set #19.
- Tarea: 5 drills audio HOOK+PILLAR 1 chained (LINK1-DRILL1..5) + 1
  audio FULL-V3 monologo completo de mantenimiento + 3 mejoras a
  mano EN EL SEAM + repaso 114 palabras (due martes 09/06 antes 6
  PM). 45-60 min, NO se fragmenta, NO se acepta push-back.
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B2_DIR = os.path.join(D, 'B2')
B2_REP = os.path.join(B2_DIR, 'reportes')
os.makedirs(B2_REP, exist_ok=True)

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase26_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase26_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase26_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 25 fin de semana INTENSO: monologo completo memoria + audios FULL-V1/V2 + 3 mejoras + repaso 108)', '5 min'),
    ('EL POR QUE DE HOY (Fase 4 dia 6/8 - semana 2 abre - encadenamiento HOOK+P1 con SEAM #1)', '4 min'),
    ('FRASE DEL DIA - presentacion ("Temperance lives between two ideas - the breath that joins them holds them both up")', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos - foco fonetico TRANSICIONES: clusters /br/ /tr/ /sp/ /st/ /θ/ que ligan)', '6 min'),
    ('VATS (TEMPLANZA v2 dia 1 - NUEVO BLOQUE - templanza vive entre dos ideas - apertura del bloque virtud Cl 26-30)', '5 min'),
    ('RECAP EXPRESS - arquitectura completa (HOOK ✅ + SEAM #1 HOY + PILLAR 1 ✅ + 3 SEAMS pendientes + PILLAR 2/3 + CTA ✅) + 6 capas como sustrato del SEAM', '5 min'),
    ('ACADEMIC B2 VOCAB SET #19 (6 palabras nuevas - TRANSICION/BRIDGES/signposting: bridge/pivot/segue/link/transition/connect - total 114)', '7 min'),
    ('REFRESH MENTAL: HOOK individual + PILLAR 1 individual SILENCIOSO sin papel (chequeo memoria de las 2 piezas antes de unirlas con seam, NO ensayo)', '2 min'),
    ('PLAN DE HOY: PRACTICA ENCADENAMIENTO HOOK->PILLAR 1 SIN PAPEL - instrucciones 3 fases + regla SEAM (planning line + no improvisar + 1 seg breath real)', '5 min'),
    ('PEER TEACHER SLOT corto (error oral Cl 25: tipicamente cierre vago del CTA - hoy se pivota a "mismo problema tecnico que seam atropellado": falta cierre firme + breath real antes del siguiente movimiento)', '3 min'),
    ('PRACTICA ENCADENAMIENTO HOOK->PILLAR 1 SIN PAPEL - CENTRO DE HOY: ALONE 10 min (planning line seam + 3 chained drills con paper) + PAIRS 15 min (drill sin papel coach SEAM ONLY) + MINI-AUDIENCIA 20 min (cada HOOK+SEAM+PILLAR 1 de memoria + 1 observacion seam del grupo)', '45 min'),
    ('RECAP COMPLETO: cada estudiante recita HOOK+SEAM+PILLAR 1 encadenado de memoria 1 vez mas sin coaching (5 estudiantes)', '9 min'),
    ('FRASE DEL DIA cierre + Paraphrase check + auto-observacion SEAM (que parte del seam quedo solida / cual falto precision; NO nota)', '5 min'),
    ('ERROR PAPER LIVE (errores DE TRANSICION: seam atropellado / closing marker ausente / opening marker abrupto-academico / bridge formal-casual perdido / improvisar transicion cada intento / silencio incomodo >2 seg / muletillas "and now I want to talk about")', '5 min'),
    ('APERTURA FORMAL SEMANA 2 FASE 4 + APERTURA TEMPLANZA v2 dia 1 + TAREA STRICT 4 componentes (5 drills audio LINK1-DRILL1..5 + 1 audio FULL-V3 mantenimiento + 3 mejoras a mano EN EL SEAM + repaso 114 palabras; due martes 09/06 antes 6 PM)', '10 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 25 (fin de semana INTENSO: monologo completo memoria + audios FULL-V1/V2 + 3 mejoras + repaso 108)',
    'Foto del tablero - Frase del Dia + B2 Set #19 (6 palabras transicion) + Arquitectura completa (SEAM #1 marcado HOY entre HOOK y PILLAR 1) + Reglas practica encadenamiento (3 fases + SEAM rule + no improvisar + 1 seg breath) + Mensaje apertura semana 2 Fase 4',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante (hoy errores DE TRANSICION: seam atropellado / closing marker ausente / opening marker abrupto / bridge perdido / improvisar transicion cada intento / muletillas en el seam / intonacion ascendente al final del HOOK / PILLAR 1 entra alta-tensa)',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: si alguien NO logro HOOK+SEAM+PILLAR 1 chained de memoria en Fase C mini-audiencia (levanto papel mas de 1 vez / seam atropellado repetido / pieza individual HOOK o PILLAR 1 se cayo) - notificar al cierre',
    'ALERTA coordinacion: cuantas estudiantes intentaron "hacer el monologo entero" en lugar de quedarse en HOOK+PILLAR 1 (impulso natural del fin de semana FULL-V1/V2)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente (objetivo: 5 inserciones marcadas #1-#5 + cierre parafrasis por estudiante)',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 25 (4 componentes fin de semana INTENSO)',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 6/8 + SEMANA 2 ABRE: Cl 21-25 cerraron 5 chunks memorizados individualmente / hoy Cl 26 abre encadenamiento = SEAM #1 entre HOOK y PILLAR 1 / unidad de hoy son 2 piezas chained, NO 5 / Cl 27 anade PILLAR 2 / Cl 28 monologo completo + C4',
    'ESCRIBI Frase del Dia + B2 Set #19 (6 palabras transicion: bridge/pivot/segue/link/transition/connect) + Arquitectura completa (SEAM #1 marcado HOY entre HOOK y PILLAR 1) + Reglas practica encadenamiento en 3 fases + Mensaje apertura semana 2 + cambio virtud (PRUDENCIA cerrada / TEMPLANZA abre) en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x (enfasis sereno en "temperance lives" + pausa contemplativa en "between two ideas" + enfasis preciso en "the breath that joins them" + cierre firme en "holds them both up")',
    'INSERTE Frase del Dia 5 veces NATURALMENTE (Insercion #1 en El Por Que + #2 en VATS + #3 al cierre instrucciones practica + #4 durante mini-audiencia cuando un breath se sintio real + #5 parafraseada por estudiante al cierre)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (~14 dias) - sin nota, sin criterios, sin resultado (exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results - not me. Focus on what comes next." y segui',
    'Verifique virtud CL 26 = TEMPLANZA v2 dia 1 (PRIMER dia del bloque - rotacion estandar cohorte B2 confirmada Diana 22/05) + anuncie que PRUDENCIA v2 cerro viernes Cl 25 y TEMPLANZA v2 abre hoy',
    'Hile TEMPLANZA en VATS + Frase del Dia (templanza vive ENTRE dos ideas, no DENTRO de una sola; templanza operativa = 1 segundo de respiracion real entre HOOK y PILLAR 1, no atropellarse; encadenar sin templanza = apurarse y borrar el trabajo de memorizacion de la semana 1)',
    'Mantuve las 6 capas visibles como SUSTRATO del SEAM (closing marker del HOOK / opening marker del PILLAR 1 / bridge formal->casual EN la seam / repetition que ata anchor / intonacion desciende firme en HOOK / abre fresca en PILLAR 1)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-25) - elegidos con foco fonetico TRANSICIONES (clusters /br/ /tr/ /sp/ /st/ /θ/ que ligan; ecos semanticos bridge/pivot/segue/threshold/seam)',
    'Presente 6 palabras B2 Set #19 con pronunciacion + ejemplo orientado a SEAM (bridge/pivot/segue/link/transition/connect - total 114) + aclare que UNA se elige y se drilla, NO 6 sampleadas',
    'Conduje REFRESH MENTAL 2 min (HOOK individual + PILLAR 1 individual SILENCIOSO, NO out loud, NO ensayo) - chequeo de las 2 piezas vivas antes de unirlas con seam',
    'Explique las INSTRUCCIONES de la practica encadenamiento en 3 fases (ALONE 10 min planning line del seam + 3 chained drills con paper / PAIRS 15 min sin papel coach SEAM ONLY / MINI-AUDIENCIA 20 min cada HOOK+SEAM+PILLAR 1 de memoria) + REGLA SEAM (closing marker + 1 seg breath real + opening marker + bridge formal->casual + anchor word) + NO IMPROVISAR (1 seam elegida y drillada, NO 5 inventadas)',
    'CONDUJE FASE A ALONE 10 min (planning line escrita del seam + cubrir paper + 3 intentos chained limpios) - NO interrumpi, anote en libreta privada quien tardo mas en escribir la planning line (senal: seam improvisada en vivo, riesgo manana)',
    'CONDUJE FASE B PAIRS 15 min (papel face down en piso, 3-4 vueltas por persona, partner B flag UNA observacion SEAM ONLY: breath real / closing marker / opening marker / bridge casual) - rote silenciosa 2-3 min por pareja, intervine SOLO si se desviaron a corregir contenido del HOOK o PILLAR 1',
    'CONDUJE FASE C MINI-AUDIENCIA 20 min (5 estudiantes x ~4 min: HOOK+SEAM+PILLAR 1 de memoria ~2-2.7 min + 1 observacion seam del grupo, NO advice) - cronometre, anote arquitectura interna del seam por estudiante en libreta privada',
    'CONTUVE el impulso del cohorte a "hacer el monologo entero" (vienen del fin de semana FULL-V1/V2) - "Today we forge the first link only. The whole monologue is for Wednesday Cl 28."',
    'CONTUVE el impulso a inventar transicion nueva cada intento - "You pick ONE transition and you drill THAT one"',
    'NO INVENTE CRITERIOS DE EVALUACION (no di puntaje, no di juicio, no comunique resultado) - solo observacion cruda en libreta privada + papel anonimo publico',
    'CONDUJE RECAP COMPLETO 9 min (cada estudiante recita HOOK+SEAM+PILLAR 1 chained 1 vez mas de memoria, sin coaching, sin comentario de calidad - solo "thank you, next")',
    'Conduje la AUTO-OBSERVACION de cierre (cada quien dice que parte de SU seam quedo solida y cual falto precision) como PROCESO, NO como comunicacion de evaluacion',
    'Camine con papel errores anonimo (errores de TRANSICION: seam atropellado / closing marker ausente / opening marker abrupto-academico / bridge perdido / improvisar transicion cada intento / silencio incomodo >2 seg / muletillas "and now I want to talk about" / intonacion ascendente al final del HOOK)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (DE TRANSICION hoy)',
    'ANUNCIE FORMALMENTE la apertura de SEMANA 2 FASE 4 + puente a Cl 27 (HOOK+P1+P2 con SEAM #1 + SEAM #2 nueva) + Cl 28 (monologo completo + C4 video 3 min memoria a coordinacion - derivado ROADMAP lineas 146-153)',
    'ANUNCIE el cambio de virtud (PRUDENCIA v2 cerro viernes Cl 25 / TEMPLANZA v2 abre hoy Cl 26 con el encadenamiento)',
    'En Tarea explique el por que (DRILL del seam de hoy en boca = si no entra esta noche, manana se apila mal el segundo seam encima de uno frio) + due date explicito (martes 09/06 antes de 6:00 PM) + 4 componentes claros (5 drills LINK1-DRILL1..5 + 1 audio FULL-V3 mantenimiento monologo completo + escuchar mejor drill + 3 mejoras a mano EN EL SEAM + repaso 114 palabras Sets #1-#19)',
    'NO acepte la excusa "no me da tiempo" (45-60 min compactos)',
    'NO acepte fragmentar (los 5 drills + 1 FULL-V3 + 3 mejoras + repaso son una sola sesion compacta)',
    'NO acepte "no lo memorize entero" - si una pieza (HOOK o PILLAR 1) no entra, vuelve a esa pieza aislada antes de drillar el chained set (orden no se salta)',
    'Notifique a coordinacion al cierre si hay 2 strikes / sospecha IA residual / inasistencia hoy / HOOK+SEAM+PILLAR 1 no logrado de memoria en Fase C',
    'Anuncie Cl 27 martes = SEMANA 2 FASE 4 DIA 2/4 = HOOK + PILLAR 1 + PILLAR 2 chained (SEAM #1 + SEAM #2) + TEMPLANZA v2 dia 2 + Set #20 (vocab de PIVOT/SHIFT/ESCALATION B2 para SEAM #2 narrativo)',
    'Anuncie Cl 28 miercoles = monologo COMPLETO de memoria (5 bloques + 4 seams) + CHECKPOINT C4 (video 3 min memoria a coordinacion) + TEMPLANZA v2 dia 3',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase26_REPORTE.pdf'),
    'B2 PM AMINA | Cl 26 de 36 | FASE 4 PRACTICA EN CHUNKS DIA 6/8 | SEMANA 2 ABRE - ENCADENAMIENTO HOOK + PILLAR 1 (SEAM #1) | FRASE DEL DIA (Goldlist retirado)',
    'FASE 4 PRACTICA EN CHUNKS DIA 6/8 - SEMANA 2 ABRE - ENCADENAMIENTO HOOK + PILLAR 1 con SEAM #1 (1 segundo de breath real + closing marker firme del HOOK + opening marker casual del PILLAR 1 + bridge formal->casual + 1 anchor word que camina + opcional 1 palabra Set #19). Cl 21-25 cerraron HOOK + 3 PILLARS + CTA memorizados individualmente. Hoy Cl 26 abre formalmente la SEMANA 2 = ya no se aprenden chunks nuevos, se ENCADENAN los 5 que ya estan aprendidos, pieza por pieza. Primer eslabon: HOOK -> PILLAR 1. Centro = PRACTICA ENCADENAMIENTO SIN PAPEL 45 min en 3 fases: ALONE 10 min (planning line del seam escrita + 3 chained drills con paper) + PAIRS 15 min (drill sin papel, partner B coach SEAM ONLY: breath real / closing marker / opening marker / bridge casual) + MINI-AUDIENCIA 20 min (cada estudiante HOOK+SEAM+PILLAR 1 de memoria ~2-2.7 min + 1 observacion seam del grupo NO advice) + Recap completo 9 min (1 vez mas sin coaching). Refresh mental 2 min ANTES: HOOK individual + PILLAR 1 individual SILENCIOSO (NO out loud, NO ensayo) - chequeo de las 2 piezas vivas antes de unirlas. Con el cierre de hoy SEAM #1 tiene cara. Manana Cl 27 = HOOK + P1 + P2 chained (SEAM #1 + SEAM #2 nueva) + TEMPLANZA v2 dia 2 + Set #20. Miercoles Cl 28 = monologo COMPLETO + CHECKPOINT C4 (video 3 min memoria a coordinacion - ROADMAP lineas 146-153) + TEMPLANZA v2 dia 3. Academic B2 Set #19 (bridge/pivot/segue/link/transition/connect -> total 114) = vocab de TRANSICION/BRIDGES/signposting para SEAM #1 y los 3 seams que vienen; UNA palabra elegida y drillada, NO 6 sampleadas. Profesora NUNCA comunica nota - observacion privada en libreta + papel anonimo publico. Cl 26 = TEMPLANZA v2 dia 1 (PRIMER dia del bloque cohorte B2 ciclo 2 Cl 26-30; Cl 25 viernes cerro PRUDENCIA v2). Razon pedagogica: templanza vive ENTRE dos ideas, no DENTRO; encadenar sin templanza = apurarse y borrar el trabajo de memorizacion de la semana 1. La trampa de hoy: vienen del fin de semana FULL-V1/V2 con impulso a "hacer el monologo entero" - tu trabajo es contenerlas en el primer eslabon (2 piezas, NO 5). ~20h/~14 dias al Final. Tarea: 5 drills audio HOOK+PILLAR 1 chained (LINK1-DRILL1..5) + 1 audio FULL-V3 monologo completo de mantenimiento + 3 mejoras a mano EN EL SEAM + repaso 114 palabras (due martes 09/06 antes 6 PM). 45-60 min compactos, NO se fragmenta, NO se acepta push-back.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase26_REPORTE.pdf')

print('\n2 PDFs generados para lunes 08/06 B2 PM Amina Cl 26:')
print('  - B2/B2_PM_Amina_Clase26_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase26_REPORTE.pdf')
