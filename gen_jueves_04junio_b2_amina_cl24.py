#!/usr/bin/env python3
"""Genera la guia + reporte del B2 PM Amina Cl 24 (jueves 04/06/2026):
- FASE 4 DIA 4/8 - CHUNK PILLAR 3.
  Centro = MEMORIZAR + ENSAYAR el TERCER pilar argumental del monologo
  (~60 seg) como pieza autonoma. Mismo metodo Cl 21-23: extraccion del
  guion fisico (5 min) + ensayo individual SIN papel (10 min) + ensayo
  en parejas con feedback landed/shaky (12 min) + mini-audiencia DE PIE
  SIN papel (15 min, ~3 min por estudiante).
- Principio del dia: STAND ON ITS OWN FIRST. PILLAR 3 se memoriza ALONE
  hoy; el encadenamiento es Cl 26-28 (la semana entrante).
- Refresh al inicio (~90 seg) = MENTAL, NO oral. Encadenar HOOK + P1 + P2
  en silencio para verificar que los 3 chunks anteriores (Cl 21/22/23)
  siguen vivos en la boca, antes de anadir el 4to.
- Profesora NO comunica nota ni juicio. NO es checkpoint hoy (C4 = fin
  Cl 28 = video 3 min de memoria). Hoja interna de NOTAS DE MEMORIZACION
  por estudiante para seguimiento Fase 4.
- Academic B2 Vocab Set #17 (6 nuevas: culminate/conclude/encompass/
  capture/distill/crystallize -> total 102). Vocabulario de CIERRE DE
  CUERPO + bridge a CTA; entra en uso pleno con el encadenamiento Cl 26-28.
- Virtud PRUDENCIA dia 4 (rotacion estandar cohorte B2, bloque PRUDENCIA
  v2 Cl 21-25; regla confirmada Diana 22/05/2026). Manana Cl 25 = dia 5
  (ultimo del bloque).
- ~24 horas / ~18 dias hasta el Final (~22 junio) - derivado de Cl 20
  (~32h/~24d) +6 dias calendario (vie 29 -> jue 04 jun) -8h bloque
  Cl 21-24 (4 clases x 2h) (verificado: 22/06/2026 - 04/06/2026 = 18
  dias; 32h - 8h = 24h).
- Estructura Fase 4 segun ROADMAP 72h lineas 120-129: Cl 21-28 (16h),
  1 chunk = 1 minuto del monologo, Cl 21-24 practican 1-2 chunks por
  sesion de memoria, Cl 25-28 encadenan 2->3->4->5 chunks, C4 fin Cl 28
  = video 3 min de memoria. La adaptacion "1 chunk por sesion Cl 21-25
  siguiendo el orden del monologo (HOOK/P1/P2/P3/CTA)" es del
  profesorado Heiiu - el Roadmap dice "1-2 chunks por sesion".
- ANUNCIO Cl 25 (manana viernes 05/06) = FASE 4 DIA 5 = chunk CTA +
  cierre primera semana Fase 4 + ultimo dia PRUDENCIA v2.
- Tarea STRICT 4 componentes (due viernes 05/06 antes 6 PM):
  (1) HOOK + 3 PILLARS de memoria por separado (15 min)
  (2) AUDIO encadenado HOOK->P1->P2->P3 (sin CTA todavia), 3 tomas (15-20 min)
  (3) Escucha de la 3a toma + 2 mejoras concretas (10-15 min)
  (4) Repaso 102 palabras Sets #1-#17 (5-10 min)
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase24_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase24_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase24_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 23)', '5 min'),
    ('EL POR QUE DE HOY (Fase 4 dia 4/8 - chunk PILLAR 3 + principio stand on its own first)', '4 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (PRUDENCIA dia 4 - prudence de no encadenar prematuramente)', '5 min'),
    ('RECAP EXPRESS - arquitectura completa con marca de progreso Fase 4 (HOOK/P1/P2 memorizados, P3 hoy, CTA manana) + 6 capas como sustrato del chunk aislado', '5 min'),
    ('ACADEMIC B2 VOCAB SET #17 (6 palabras nuevas - cierre argumental + bridge a CTA - total 102)', '7 min'),
    ('REFRESH MENTAL ~90 seg (HOOK + P1 + P2 encadenados en SILENCIO - NO en voz alta)', '2 min'),
    ('PLAN DE HOY: MEMORIZAR + ENSAYAR PILLAR 3 + PRINCIPIO STAND ON ITS OWN FIRST', '5 min'),
    ('PEER TEACHER SLOT corto (error oral Cl 23)', '3 min'),
    ('PRACTICA PILLAR 3 SIN PAPEL - CENTRO DE HOY: extraccion 5 min / individual 10 min / parejas 12 min landed-shaky / mini-audiencia DE PIE sin papel 15 min', '45 min'),
    ('FRASE DEL DIA cierre + Paraphrase check + auto-observacion (NO nota)', '5 min'),
    ('ERROR PAPER LIVE (errores DE MEMORIZACION del chunk PILLAR 3: peek multiple / chunk corto / conexion entrecortada / pronunciacion Set #17 / salto a CTA prematuro)', '5 min'),
    ('RECAP CHUNK PILLAR 3 + ANUNCIO CL 25 (chunk CTA manana + cierre semana 1 Fase 4) + cierre VATS dia 4', '6 min'),
    ('TAREA STRICT 4 componentes (HOOK+3PILLARS memoria / audio encadenado HOOK->P3 sin CTA 3 tomas / escucha + 2 mejoras / repaso 102 palabras) + foto tablero', '11 min'),
    ('Cierre del dia + recordatorio Cl 25 (chunk CTA)', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 23',
    'Foto del tablero - Frase del Dia + B2 Set #17 + Arquitectura completa con marca de progreso + Reglas chunk PILLAR 3 + Anuncio Cl 25',
    'NOTAS DE MEMORIZACION POR ESTUDIANTE (interno - alimenta seguimiento Fase 4, NO se comunica): por las 5 estudiantes, sin calificacion, solo observacion cruda (tiempo real del chunk / peek o no / sostuvo 60 seg / conexion interna / pronunciacion Sets #9-#17 / intonacion de cierre / pieza autonoma vs salto a CTA)',
    'CHECKLIST especifico chunk PILLAR 3 hoy: 5 estudiantes hicieron extraccion / 5 hicieron ensayo individual sin papel / 5 hicieron parejas con feedback landed/shaky / 5 hicieron mini-audiencia DE PIE sin papel / tiempo promedio del chunk anotado / 5 hojas de notas de memorizacion llenas',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante (hoy errores DE MEMORIZACION del chunk PILLAR 3)',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: si alguien NO logro sostener el chunk de memoria (corto a < 30 seg / multiples peeks / no pudo cerrar el papel) - notificar al cierre para soporte personalizado Fase 4',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 23',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 4/8 + CHUNK PILLAR 3: Cl 21-23 dejaron HOOK + P1 + P2 memorizados / hoy se agrega P3 / manana CTA / lunes Cl 26 inicia encadenamiento / C4 fin Cl 28',
    'ESCRIBI Frase del Dia + B2 Set #17 + Arquitectura completa con marca de progreso (HOOK/P1/P2 memorizados, P3 hoy, CTA manana) + Reglas chunk PILLAR 3 + Principio stand on its own first + Anuncio Cl 25 en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 24 = PRUDENCIA dia 4 (rotacion estandar cohorte B2, Cl 21-25 PRUDENCIA v2, regla confirmada Diana 22/05/2026)',
    'Hile PRUDENCIA en VATS + Frase del Dia (prudence de NO encadenar prematuramente - PILLAR 3 stands on its own first)',
    'Mantuve las 6 capas visibles como SUSTRATO del chunk aislado (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing) - drill verifica como cada capa funciona DENTRO de PILLAR 3 especificamente',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-23)',
    'Presente 6 palabras B2 Set #17 con pronunciacion + ejemplo orientado al cierre del cuerpo (total 102) - aclare que pueden usarse en PILLAR 3 si caen natural, NO forzar',
    'Conduje REFRESH MENTAL ~90 seg en silencio absoluto (HOOK + P1 + P2 encadenados en la mente - NO en voz alta) - cronometre los 90 seg',
    'EXPLIQUE el PRINCIPIO STAND ON ITS OWN FIRST claramente: hoy P3 se memoriza ALONE, encadenamiento es Cl 26-28 la semana entrante',
    'EXPLIQUE las REGLAS del chunk: extraccion 5 min con papel / individual 10 min DE PIE caminando sin papel / parejas 12 min con feedback landed/shaky no advice / mini-audiencia 15 min DE PIE sin papel ~3 min por estudiante',
    'CONDUJE 5 EXTRACCIONES + 5 ENSAYOS INDIVIDUALES + 5 RONDAS DE PAREJAS + 5 MINI-AUDIENCIAS de chunk PILLAR 3 sin interrumpir, cronometrando, anotando memorizacion interna en hoja por estudiante',
    'NO COMUNIQUE NOTA NI JUICIO (no hay checkpoint hoy - C4 es Cl 28) - solo observacion cruda en hoja interna',
    'En la extraccion verifique que cada quien identifico correctamente PILLAR 3 (no PILLAR 2 ni CTA)',
    'En el ensayo individual NO INTERRUMPI - observe peek / chunk corto a 35 seg / sostuvo 60 seg fluido',
    'En las parejas verifique que el feedback fue landed/shaky, NO advice ni "I would have said"',
    'En la mini-audiencia: NO Q&A hoy (chunks aislados no llevan Q&A); cada quien DE PIE al frente, paper face down, ~60 seg, aplauso breve',
    'Conduje la AUTO-OBSERVACION de cierre (cada quien dice que fue lo mas dificil de SU memorizacion P3) como PROCESO, NO como comunicacion de evaluacion',
    'Camine con papel errores anonimo (errores DE MEMORIZACION: peek multiple / chunk corto / conexion interna entrecortada / pronunciacion Set #17 / salto a CTA prematuro)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (DE MEMORIZACION, del chunk PILLAR 3)',
    'ANUNCIE CL 25 (manana viernes 05/06) = FASE 4 DIA 5 = chunk CTA + cierre primera semana Fase 4 + ultimo dia PRUDENCIA v2',
    'En Tarea explique el por que (puente al encadenamiento del lunes Cl 26) + due date explicito (viernes 05/06 antes de 6:00 PM) + componentes: (1) HOOK+3PILLARS memoria separados (2) audio encadenado HOOK->P3 SIN CTA todavia, 3 tomas (3) escucha 3a toma + 2 mejoras (4) repaso 102 palabras',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes / si alguien no logro sostener el chunk de memoria / inasistencia hoy / soporte personalizado requerido antes de C4',
    'Anuncie Cl 26 lunes = inicio ENCADENAMIENTO (2 chunks seguidos: HOOK + PILLAR 1 de memoria) + nueva virtud (SUPUESTO TEMPLANZA v2, verificar)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase24_REPORTE.pdf'),
    'B2 PM AMINA | Cl 24 de 36 | FASE 4 DIA 4/8 - CHUNK PILLAR 3 | MEMORIZAR + ENSAYAR EL TERCER PILAR SIN PAPEL | FRASE DEL DIA (Goldlist retirado)',
    'FASE 4 DIA 4/8 - CHUNK PILLAR 3. Cl 21-23 dejaron HOOK (Cl 21) + PILLAR 1 (Cl 22) + PILLAR 2 (Cl 23) memorizados como chunks de ~1 min cada uno (96 palabras B2 acumuladas Sets #1-#16). Hoy Cl 24 = chunk PILLAR 3 (tercer pilar argumental del monologo, ~60 seg, de memoria, SIN papel en el ensayo) + Set #17 (culminate/conclude/encompass/capture/distill/crystallize -> total 102). Centro = PRACTICA PILLAR 3 SIN PAPEL (45 min): extraccion del guion fisico 5 min + ensayo individual DE PIE caminando 10 min + parejas con feedback landed/shaky 12 min + mini-audiencia DE PIE sin papel ~3 min por estudiante 15 min. Principio del dia: STAND ON ITS OWN FIRST - P3 se memoriza ALONE hoy, el encadenamiento es Cl 26-28 la semana entrante. Refresh al inicio (~90 seg) = MENTAL, encadenar HOOK + P1 + P2 en silencio para verificar que los 3 chunks anteriores siguen vivos antes de anadir el 4to. Profesora NO comunica nota ni juicio; toma notas internas de memorizacion por estudiante (tiempo real / peek o no / sostuvo 60 seg / conexion interna / pronunciacion Sets / intonacion de cierre / pieza autonoma vs salto a CTA). NO es checkpoint hoy - C4 = fin Cl 28 = video 3 min de memoria. Cl 24 = PRUDENCIA dia 4 (rotacion estandar cohorte B2, Cl 21-25 PRUDENCIA v2). ~24h/~18 dias al Final. Tarea fin de hoy (due viernes 05/06 antes 6 PM, 45-60 min): (1) HOOK + 3 PILLARS de memoria por separado / (2) audio encadenado HOOK->P1->P2->P3 SIN CTA todavia, 3 tomas / (3) escucha 3a toma + 2 mejoras concretas / (4) repaso 102 palabras Sets #1-#17. Anuncio Cl 25 (manana viernes) = FASE 4 DIA 5 = chunk CTA + cierre primera semana Fase 4 + ultimo dia PRUDENCIA v2. Cl 26 lunes = inicio ENCADENAMIENTO + nueva virtud (SUPUESTO TEMPLANZA v2, verificar).',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase24_REPORTE.pdf')

print('\n2 PDFs generados para jueves 04/06 B2 PM Amina Cl 24:')
print('  - B2/B2_PM_Amina_Clase24_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase24_REPORTE.pdf')
