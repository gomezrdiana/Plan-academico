#!/usr/bin/env python3
"""Genera la guia + reporte del B2 PM Amina Cl 27 (martes 09/06/2026):
- FASE 4 PRACTICA EN CHUNKS dia 7/8 - SEMANA 2 DIA 2/4 - ENCADENAMIENTO
  HOOK + PILLAR 1 + PILLAR 2 (SEAM #2). Cl 26 ayer forjo SEAM #1
  (HOOK->PILLAR 1). Hoy se agrega PILLAR 2 al encadenamiento -> 3
  chunks + 2 seams. SEAM #1 viva en el fondo + SEAM #2 nueva en foco.
  Cl 28 manana = monologo COMPLETO (5 bloques + 4 seams) + C4.
- SEAM #2 = la MAS DIFICIL de las 4 seams - no por tecnica sino por
  MOMENTUM acumulado. Cuando la oradora llega a SEAM #2 viene con
  ~2-3 min de habla atras (HOOK+SEAM#1+PILLAR 1); su impulso natural
  es ACELERAR para "no perder el flujo." Eso erosiona la seam.
- TEMPLANZA dia 2 = FRENO INTENCIONAL contra el momentum. La tecnica
  Heiiu del dia: BRAKE FISICO (eye lift / shoulder drop / nose inhale)
  - elegido ANTES en la planning line, entrenado en los 3 fases.
  Brake fisico no es natural; es entrenado.
- Centro = PRACTICA ENCADENAMIENTO HOOK+P1+P2 SIN PAPEL 45 min en 3
  fases: ALONE 10 min (SEAM #2 planning line + brake fisico elegido +
  3 chained drills con paper) + PAIRS 15 min (drill sin papel, partner
  B coach SEAM #2 PRIORITARIO + opcional 1 palabra SEAM #1 alive/
  drifted) + MINI-AUDIENCIA 20 min (cada estudiante HOOK+SEAM#1+P1+
  SEAM#2+P2 de memoria ~3-4.5 min + 1 observacion SEAM #2 del grupo
  NO advice). + Recap completo 9 min (1 vez mas sin coaching).
- Refresh mental 2 min ANTES de la practica: HOOK+SEAM#1+P1 (de ayer)
  silencioso + PILLAR 2 individual silencioso - chequeo de que las
  piezas siguen vivas antes de unirlas con SEAM #2. NO es ensayo.
- Academic B2 Vocab Set #20 (6 nuevas: moreover/consequently/
  furthermore/nevertheless/accordingly/thereby -> total 120). Set #20
  es vocabulario de COHESION / FLUIDEZ EXTENDIDA / signposting de
  transicion prolongada B2 - vocabulario que sostiene un encadenamiento
  de 3-4 min sin colapsar; clave para el FULL de manana. UNA palabra
  elegida y drillada, no 6 sampleadas.
- Virtud TEMPLANZA v2 dia 2 (mismo bloque, segundo dia). Cl 26 dia 1
  = "templanza vive ENTRE dos ideas." Hoy dia 2 = "templanza es el
  FRENO ante el momentum." Razon pedagogica directa: la segunda seam
  exige una pausa que se siente fisicamente antinatural porque el
  cuerpo ya esta en marcha - templanza entrenada, no espontanea.
  Bloque Cl 26-30 TEMPLANZA v2 ciclo 2 (rotacion estandar cohorte B2
  confirmada Diana 22/05/2026, memoria
  project-b2-virtud-rotacion-estandar).
- ~18 horas / ~13 dias hasta el Final (~22 junio) - derivado de Cl 26
  (~20h/~14d) - 2h netas Cl 27 hoy (verificado calendario:
  22/06/2026 - 09/06/2026 = 13 dias).
- Estructura Fase 4 segun ROADMAP 72h (lineas 120-129): Cl 21-28,
  16h, chunk = 1 min, Cl 21-24 practicaron 1-2 chunks por sesion de
  memoria, Cl 25-28 encadenan 2->3->4->5 chunks. Cl 27 = 3 chunks
  encadenados (paso de 2 a 3, segundo dia del encadenamiento real).
  Cl 28 = monologo COMPLETO + C4 (video 3 min memoria a coordinacion;
  ROADMAP lineas 146-153).
- SEAM #2 = closing marker firme del PILLAR 1 + 1 segundo de breath
  real con BRAKE FISICO + opening marker casual del PILLAR 2 + bridge
  formal->casual + 1 anchor word que camina + opcional 1 palabra Set
  #20. SEAM #1 (forjada ayer) se mantiene viva en el fondo.
- Tarea: 5 drills audio HOOK+P1+P2 chained (LINK2-DRILL1..5) + 1
  audio FULL-V4 monologo completo (base para C4 manana) + 3 mejoras
  a mano EN EL SEAM #2 + repaso 120 palabras (due miercoles 10/06
  antes 6 PM). 45-60 min, NO se fragmenta, NO se acepta push-back.
- LOGISTICA C4 - verificar con coordinacion HOY al cierre (dispositivo
  grabacion, protocolo envio, formato del video, que 3 minutos del
  monologo). Manana es el dia.
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
B2_DIR = os.path.join(D, 'B2')
B2_REP = os.path.join(B2_DIR, 'reportes')
os.makedirs(B2_REP, exist_ok=True)

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase27_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase27_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase27_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 26: 5 drills LINK1-DRILL1..5 + 1 audio FULL-V3 + 3 mejoras a mano EN EL SEAM #1 + repaso 114 palabras)', '5 min'),
    ('EL POR QUE DE HOY (Fase 4 dia 7/8 - semana 2 dia 2/4 - encadenamiento HOOK+P1+P2 con SEAM #2 - la mas dificil por momentum)', '4 min'),
    ('FRASE DEL DIA - presentacion ("The second bridge is the hardest - momentum already carries you; temperance is what slows you down enough to land")', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos - foco fonetico TRANSICIONES DE PIVOTE: clusters /tw/ /sw/ /θr/ /fl/ /pl/ /cr/ /sn/ /sm/ que pivotan sin perder centro)', '6 min'),
    ('VATS (TEMPLANZA v2 dia 2 - mismo bloque virtud, segundo dia - templanza como FRENO contra momentum acumulado - eleccion brake fisico: eye lift / shoulder drop / nose inhale)', '5 min'),
    ('RECAP EXPRESS - arquitectura completa (HOOK ✅ + SEAM #1 ✅ ayer + PILLAR 1 ✅ + SEAM #2 HOY + PILLAR 2 ✅ + SEAM #3-#4 pendientes + PILLAR 3 + CTA ✅) + 6 capas como sustrato de las DOS TRANSICIONES + drill coro closing marker P1 / opening marker P2 / brake SEAM #2', '5 min'),
    ('ACADEMIC B2 VOCAB SET #20 (6 palabras nuevas - COHESION/FLUIDEZ EXTENDIDA/signposting transicion prolongada: moreover/consequently/furthermore/nevertheless/accordingly/thereby - total 120 - para sostener un encadenamiento de 3-4 min sin colapsar)', '7 min'),
    ('REFRESH MENTAL: HOOK+SEAM#1+PILLAR 1 (de ayer) SILENCIOSO + PILLAR 2 individual SILENCIOSO sin papel (chequeo memoria de las piezas antes de unirlas con SEAM #2, NO ensayo)', '2 min'),
    ('PLAN DE HOY: PRACTICA ENCADENAMIENTO HOOK+P1+P2 SIN PAPEL - instrucciones 3 fases + regla SEAM #2 (planning line + brake fisico elegido + no improvisar + 1 seg breath real + momentum warning)', '5 min'),
    ('PEER TEACHER SLOT corto (error oral Cl 26: tipicamente SEAM #1 atropellada al final de mini-audiencia por cansancio - hoy se pivota a "imaginen SEAM #2 con momentum acumulado - tecnica del freno no es ocasional, es repetida")', '3 min'),
    ('PRACTICA ENCADENAMIENTO HOOK+P1+P2 SIN PAPEL - CENTRO DE HOY: ALONE 10 min (SEAM #2 planning line + brake fisico + 3 chained drills con paper) + PAIRS 15 min (drill sin papel coach SEAM #2 prioritario + 1 palabra opcional SEAM #1 alive/drifted) + MINI-AUDIENCIA 20 min (cada HOOK+SEAM#1+P1+SEAM#2+P2 de memoria ~3-4.5 min + 1 observacion SEAM #2 del grupo)', '45 min'),
    ('RECAP COMPLETO: cada estudiante recita HOOK+SEAM#1+P1+SEAM#2+P2 encadenado de memoria 1 vez mas sin coaching (5 estudiantes)', '9 min'),
    ('FRASE DEL DIA cierre + Paraphrase check + auto-observacion SEAM #2 (que parte del seam quedo solida / cual falto precision / brake fisico funciono o se olvido bajo momentum; NO nota)', '5 min'),
    ('ERROR PAPER LIVE (errores DE TRANSICION SEAM #2: momentum gano / SEAM #2 atropellada / closing marker P1 ausente / opening marker P2 abrupto-academico / bridge formal-casual perdido / improvisar SEAM #2 cada intento / muletillas "and then"/"and so" / SEAM #1 colapsada por cansancio)', '5 min'),
    ('CONTINUACION SEMANA 2 FASE 4 + TEMPLANZA v2 dia 2 + TAREA STRICT 4 componentes (5 drills audio LINK2-DRILL1..5 + 1 audio FULL-V4 base para C4 manana + 3 mejoras a mano EN EL SEAM #2 + repaso 120 palabras; due miercoles 10/06 antes 6 PM) + ANUNCIO Cl 28 FULL + CHECKPOINT C4 (video 3 min memoria a coordinacion)', '10 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 26 (5 drills LINK1-DRILL1..5 + 1 audio FULL-V3 + 3 mejoras a mano EN EL SEAM #1 + repaso 114 palabras)',
    'Foto del tablero - Frase del Dia + B2 Set #20 (6 palabras cohesion) + Arquitectura completa (SEAM #1 viva ✅ ayer + SEAM #2 marcada HOY entre PILLAR 1 y PILLAR 2) + Reglas practica encadenamiento (3 fases + SEAM #2 rule + brake fisico + no improvisar + momentum warning) + Mensaje continuacion semana 2 Fase 4',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante (hoy errores DE TRANSICION SEAM #2: momentum gana / SEAM #2 atropellada / closing marker P1 ausente / opening marker P2 abrupto / bridge perdido / improvisar SEAM #2 cada intento / muletillas "and then" / SEAM #1 colapsada por cansancio / intonacion ascendente al final del PILLAR 1 / PILLAR 2 entra alta-tensa / brake fisico olvidado bajo momentum)',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion URGENTE: si alguien NO logro HOOK+SEAM#1+P1+SEAM#2+P2 chained de memoria en Fase C mini-audiencia (levanto papel mas de 1 vez / SEAM #2 atropellada repetida / pieza individual se cayo / SEAM #1 colapsada) - notificar al cierre URGENTE porque manana es FULL + C4',
    'ALERTA coordinacion: LOGISTICA C4 manana - confirmar dispositivo de grabacion + protocolo de envio del video 3 min por estudiante + formato + que 3 minutos del monologo (los primeros 3 o ventana flexible) - derivado ROADMAP lineas 146-153',
    'ALERTA coordinacion: cuantas estudiantes intentaron "hacer el monologo entero" en lugar de quedarse en HOOK+P1+P2 (impulso natural acumulado del fin de semana + Cl 26)',
    'ALERTA coordinacion: cuantas estudiantes "saltaron" la SEAM #2 entera (pegaron PILLAR 1 a PILLAR 2 sin breath) - senal extrema de momentum incontrolado, riesgo critico para C4',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente (objetivo: 5 inserciones marcadas #1-#5 + cierre parafrasis por estudiante)',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 26 (4 componentes: 5 drills LINK1-DRILL1..5 + 1 audio FULL-V3 + 3 mejoras EN EL SEAM #1 + repaso 114 palabras)',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 7/8 + SEMANA 2 DIA 2/4: Cl 26 ayer forjo SEAM #1 / hoy Cl 27 agrega SEAM #2 (PILLAR 1->PILLAR 2, la mas dificil por momentum) / unidad de hoy son 3 piezas chained con 2 seams, NO 5 / SEAM #1 viva en el fondo + SEAM #2 nueva en foco / Cl 28 manana = monologo COMPLETO 5 bloques + 4 seams + C4 (video 3 min memoria a coordinacion)',
    'ESCRIBI Frase del Dia + B2 Set #20 (6 palabras cohesion: moreover/consequently/furthermore/nevertheless/accordingly/thereby) + Arquitectura completa (SEAM #1 viva ayer + SEAM #2 marcada HOY entre PILLAR 1 y PILLAR 2) + Reglas practica encadenamiento en 3 fases + Mensaje continuacion semana 2 + recordatorio virtud (TEMPLANZA dia 2) en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x (enfasis preciso en "the second bridge is the hardest" + enfasis cinetico ligeramente acelerado en "momentum already carries you" + pausa contemplativa antes de "temperance" + cierre firme y aterrizado en "slows you down enough to land")',
    'INSERTE Frase del Dia 5 veces NATURALMENTE (Insercion #1 en El Por Que + #2 en VATS TEMPLANZA dia 2 + #3 al cierre instrucciones practica + #4 durante mini-audiencia cuando un brake en SEAM #2 se sintio real y aterrizado + #5 parafraseada por estudiante al cierre)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'NO comunique nada de evaluaciones/Final mas alla del HECHO DE CALENDARIO (~13 dias) - sin nota, sin criterios, sin resultado (exclusivo coordinacion)',
    'Si alguien pregunto resultado/criterios del Final respondi "Coordination handles results - not me. Focus on what comes next." y segui',
    'Verifique virtud CL 27 = TEMPLANZA v2 dia 2 (mismo bloque, segundo dia - rotacion estandar cohorte B2 confirmada Diana 22/05) + recorde que dia 1 fue "vive entre dos ideas" y dia 2 es "freno contra momentum"',
    'Hile TEMPLANZA dia 2 en VATS + Frase del Dia (templanza dia 2 = freno intencional contra momentum natural; cuando el cuerpo ya esta en marcha por 2-3 min de habla, parar se siente antinatural y por eso es entrenado; encadenar sin templanza day-2 = SEAM #2 muerta y manana FULL con agujero en la mitad para C4)',
    'PRESENTE la tecnica BRAKE FISICO (eye lift / shoulder drop / nose inhale) - cada estudiante elige UNO en VATS + lo escribe en la SEAM #2 planning line + lo entrena en los 3 fases',
    'Mantuve las 6 capas visibles como SUSTRATO de las DOS SEAMS (SEAM #1 viva en el fondo + SEAM #2 nueva en foco: closing marker del PILLAR 1 / opening marker del PILLAR 2 / bridge formal->casual EN la SEAM #2 / repetition que ata anchor / intonacion desciende firme en PILLAR 1 / abre fresca en PILLAR 2)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-26) - elegidos con foco fonetico TRANSICIONES DE PIVOTE (clusters /tw/ /sw/ /θr/ /fl/ /pl/ /cr/ /sn/ /sm/ que pivotan sin perder centro; ecos semanticos swivel/throughline/pivot/threshold/snap/smooth)',
    'Presente 6 palabras B2 Set #20 con pronunciacion + ejemplo orientado a SEAM #2 narrativo (moreover/consequently/furthermore/nevertheless/accordingly/thereby - total 120) + aclare que UNA se elige y se drilla, NO 6 sampleadas',
    'Conduje REFRESH MENTAL 2 min (HOOK+SEAM#1+PILLAR 1 de ayer SILENCIOSO + PILLAR 2 individual SILENCIOSO, NO out loud, NO ensayo) - chequeo de las piezas vivas antes de unirlas con SEAM #2',
    'Explique las INSTRUCCIONES de la practica encadenamiento en 3 fases (ALONE 10 min SEAM #2 planning line con brake fisico + 3 chained drills con paper / PAIRS 15 min sin papel coach SEAM #2 prioritario + 1 palabra opcional SEAM #1 / MINI-AUDIENCIA 20 min cada HOOK+SEAM#1+P1+SEAM#2+P2 de memoria) + REGLA SEAM #2 (closing marker P1 + 1 seg breath real + brake fisico + opening marker P2 + bridge formal->casual + anchor word) + NO IMPROVISAR (1 SEAM #2 elegida y drillada, NO 5 inventadas) + MOMENTUM WARNING (el cuerpo querra acelerar - brake entrenado)',
    'CONDUJE FASE A ALONE 10 min (SEAM #2 planning line escrita con brake fisico elegido + cubrir paper + 3 intentos chained limpios) - NO interrumpi, anote en libreta privada quien tardo mas en escribir la SEAM #2 planning line (senal: SEAM #2 improvisada en vivo, riesgo critico para C4 manana)',
    'CONDUJE FASE B PAIRS 15 min (papel face down en piso, 3 vueltas por persona, partner B flag UNA observacion SEAM #2 ONLY: breath real con brake / closing marker P1 / opening marker P2 / bridge casual + opcional 1 palabra SEAM #1 alive/drifted) - rote silenciosa 2-3 min por pareja, intervine SOLO si se desviaron a corregir contenido del PILLAR 1 o PILLAR 2 o si SEAM #1 se colapso flagrante',
    'CONDUJE FASE C MINI-AUDIENCIA 20 min (5 estudiantes x ~5 min: HOOK+SEAM#1+P1+SEAM#2+P2 de memoria ~3-4.5 min + 1 observacion SEAM #2 del grupo + opcional 1 palabra SEAM #1, NO advice) - cronometre tight, anote arquitectura interna del SEAM #2 + brake fisico usado por estudiante en libreta privada',
    'CONTUVE el impulso del cohorte a "hacer el monologo entero" (vienen con momentum del fin de semana + Cl 26 acumulado) - "Today we add the second link only. Full monologue is tomorrow Cl 28."',
    'CONTUVE el impulso a inventar SEAM #2 nueva cada intento - "You pick ONE seam #2 and you drill THAT one"',
    'CONTUVE el impulso de momentum en SEAM #2 - cuando vi acelerar en pairs/mini-audiencia, recorde "the brake is intentional, not natural - use your physical brake move"',
    'MANTUVE SEAM #1 viva en el fondo - cuando se atropello flagrante, regreso breve: "SEAM #1 lives. Dont waste yesterdays work."',
    'NO INVENTE CRITERIOS DE EVALUACION (no di puntaje, no di juicio, no comunique resultado) - solo observacion cruda en libreta privada + papel anonimo publico',
    'CONDUJE RECAP COMPLETO 9 min (cada estudiante recita HOOK+SEAM#1+P1+SEAM#2+P2 chained 1 vez mas de memoria, sin coaching, sin comentario de calidad - solo "thank you, next")',
    'Conduje la AUTO-OBSERVACION de cierre (cada quien dice que parte de SU SEAM #2 quedo solida y cual falto precision / si el brake fisico funciono o se olvido bajo momentum) como PROCESO, NO como comunicacion de evaluacion',
    'Camine con papel errores anonimo (errores de TRANSICION SEAM #2: momentum gano / SEAM #2 atropellada / closing marker P1 ausente / opening marker P2 abrupto-academico / bridge perdido / improvisar SEAM #2 cada intento / silencio incomodo >2 seg / muletillas "and then"/"and so" / intonacion ascendente al final del PILLAR 1 / SEAM #1 colapsada por cansancio / brake fisico olvidado)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (DE TRANSICION SEAM #2 hoy)',
    'ANUNCIE FORMALMENTE la continuacion de SEMANA 2 FASE 4 dia 2/4 + puente a Cl 28 (monologo COMPLETO 5 bloques + 4 seams + CHECKPOINT C4 video 3 min memoria a coordinacion - derivado ROADMAP lineas 146-153)',
    'ANUNCIE TEMPLANZA dia 2 sostenida (mismo bloque virtud, segundo dia / manana sera dia 3 con el FULL)',
    'VERIFIQUE CON COORDINACION HOY al cierre la LOGISTICA DE C4 MANANA (dispositivo grabacion + protocolo envio + formato del video + que 3 minutos del monologo)',
    'En Tarea explique el por que (DRILL del SEAM #2 de hoy en boca = si no entra esta noche, manana el FULL va a tener un agujero en la mitad y C4 saldra con ese agujero a coordinacion) + due date explicito (miercoles 10/06 antes de 6:00 PM) + 4 componentes claros (5 drills LINK2-DRILL1..5 + 1 audio FULL-V4 base para C4 manana + escuchar mejor drill + 3 mejoras a mano EN EL SEAM #2 + repaso 120 palabras Sets #1-#20)',
    'NO acepte la excusa "no me da tiempo" (45-60 min compactos)',
    'NO acepte fragmentar (los 5 drills + 1 FULL-V4 + 3 mejoras + repaso son una sola sesion compacta)',
    'NO acepte "no lo memorize entero" - si una pieza (HOOK o PILLAR 1 o PILLAR 2) no entra, vuelve a esa pieza aislada antes de drillar el chained set (orden no se salta)',
    'Notifique a coordinacion al cierre si hay 2 strikes / sospecha IA residual / inasistencia hoy / HOOK+SEAM#1+P1+SEAM#2+P2 no logrado de memoria en Fase C / logistica C4 sin confirmar',
    'Anuncie Cl 28 miercoles = SEMANA 2 FASE 4 DIA 3/4 = MONOLOGO COMPLETO de memoria (5 bloques + 4 seams) + CHECKPOINT C4 (video 3 min memoria a coordinacion) + TEMPLANZA v2 dia 3 + Set #21 si hay espacio post-FULL (vocab de CALL TO ACTION/cierre B2 para reforzar SEAM #4 PILLAR 3->CTA)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase27_REPORTE.pdf'),
    'B2 PM AMINA | Cl 27 de 36 | FASE 4 PRACTICA EN CHUNKS DIA 7/8 | SEMANA 2 DIA 2/4 - ENCADENAMIENTO HOOK + PILLAR 1 + PILLAR 2 (SEAM #2 - LA MAS DIFICIL POR MOMENTUM) | FRASE DEL DIA (Goldlist retirado)',
    'FASE 4 PRACTICA EN CHUNKS DIA 7/8 - SEMANA 2 DIA 2/4 - ENCADENAMIENTO HOOK + PILLAR 1 + PILLAR 2 con SEAM #2 (1 segundo de breath real con BRAKE FISICO (eye lift / shoulder drop / nose inhale) + closing marker firme del PILLAR 1 + opening marker casual del PILLAR 2 + bridge formal->casual + 1 anchor word que camina + opcional 1 palabra Set #20). Cl 26 ayer forjo SEAM #1 (HOOK->PILLAR 1); hoy Cl 27 agrega PILLAR 2 al encadenamiento -> 3 chunks + 2 seams. SEAM #1 viva en el fondo + SEAM #2 nueva en foco. SEAM #2 es la MAS DIFICIL de las 4 - no por tecnica (es identica a SEAM #1) sino por MOMENTUM acumulado: cuando la oradora llega a SEAM #2 viene con ~2-3 min de habla atras y su impulso natural es ACELERAR para "no perder el flujo." Eso erosiona la seam. Centro = PRACTICA ENCADENAMIENTO SIN PAPEL 45 min en 3 fases: ALONE 10 min (SEAM #2 planning line escrita con brake fisico elegido + 3 chained drills con paper) + PAIRS 15 min (drill sin papel, partner B coach SEAM #2 PRIORITARIO: breath real con brake / closing marker P1 / opening marker P2 / bridge casual + opcional 1 palabra SEAM #1 alive/drifted) + MINI-AUDIENCIA 20 min (cada estudiante HOOK+SEAM#1+P1+SEAM#2+P2 de memoria ~3-4.5 min + 1 observacion SEAM #2 del grupo NO advice) + Recap completo 9 min (1 vez mas sin coaching). Refresh mental 2 min ANTES: HOOK+SEAM#1+P1 (de ayer) SILENCIOSO + PILLAR 2 individual SILENCIOSO - chequeo de las piezas vivas antes de unirlas. Con el cierre de hoy SEAM #2 tiene cara. Manana Cl 28 = monologo COMPLETO (5 bloques + 4 seams) + CHECKPOINT C4 (video 3 min memoria a coordinacion - derivado ROADMAP lineas 146-153). Academic B2 Set #20 (moreover/consequently/furthermore/nevertheless/accordingly/thereby -> total 120) = vocab de COHESION/FLUIDEZ EXTENDIDA/signposting de transicion prolongada B2; sostiene un encadenamiento de 3-4 min sin colapsar; clave para el FULL de manana. UNA palabra elegida y drillada, NO 6 sampleadas. Profesora NUNCA comunica nota - observacion privada en libreta + papel anonimo publico. Cl 27 = TEMPLANZA v2 dia 2 (mismo bloque, segundo dia - cohorte B2 ciclo 2 Cl 26-30; Cl 26 dia 1 fue "vive entre dos ideas"; hoy dia 2 es "freno intencional contra momentum"). Razon pedagogica: la segunda seam exige una pausa que se siente fisicamente antinatural porque el cuerpo ya esta en marcha - templanza entrenada, no espontanea. Tecnica BRAKE FISICO (eye lift / shoulder drop / nose inhale) elegida ANTES en planning line. La trampa de hoy: el cohorte viene con momentum acumulado del fin de semana + Cl 26 - su impulso sera "hacer el monologo entero"; tu trabajo es contenerlas en el segundo eslabon (3 piezas, NO 5). ~18h/~13 dias al Final. Tarea: 5 drills audio HOOK+P1+P2 chained (LINK2-DRILL1..5) + 1 audio FULL-V4 monologo completo (base para C4 manana) + 3 mejoras a mano EN EL SEAM #2 + repaso 120 palabras (due miercoles 10/06 antes 6 PM). 45-60 min compactos, NO se fragmenta, NO se acepta push-back. LOGISTICA C4 - verificar con coordinacion HOY al cierre (dispositivo grabacion, protocolo envio, formato del video, que 3 minutos del monologo).',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase27_REPORTE.pdf')

print('\n2 PDFs generados para martes 09/06 B2 PM Amina Cl 27:')
print('  - B2/B2_PM_Amina_Clase27_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase27_REPORTE.pdf')
