#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 18 (miercoles 27/05/2026):
- FASE 3 DIA 6/8 - CIERRA EL SUB-BLOQUE "ESTRUCTURA DEL MONOLOGO".
  Centro = ESCRITURA MANUSCRITA EN CLASE: PILLAR 3 desarrollado a
  parrafo completo del cuerpo (mismo formato Cl 17 - registro academico,
  topic chunk + connector apuntando al CTA, 2+ B2 Set #11 adentro) +
  CALL TO ACTION (30-60 seg hablados, escrito a mano, registro
  casual/directo, ECHO del HOOK + verbo de accion imperative + linea
  final que cierra el arco). Anti-fraude IA: a mano, en clase, sin
  dispositivos; texto de casa - incl. "ya escribi el pillar 3 en casa" /
  "ya tengo el CTA" - NO cuenta.
- Cuando suene la ultima campana, la arquitectura COMPLETA del monologo
  esta en papel: HOOK (Cl 16) + PILLAR 1 + PILLAR 2 (Cl 17) + PILLAR 3 +
  CTA (hoy). Cl 19-20 NO agrega arquitectura: pule, integra y monta
  ensayos orales del monologo completo.
- Academic B2 Vocab Set #11 (6 nuevas: imperative/summon/urge/compel/
  beckon/prevail -> total 66) + Frase del Dia + virtud FORTALEZA dia 3
  (TERCER dia del bloque - regla cohorte B2, rotacion estandar,
  NO supuesto).
- ~36 horas / ~26 dias hasta el Final (~22 junio) - derivado de Cl 16
  (40h/28d) -2h Cl 17 -2h Cl 18 (verificado: 22/06/2026 - 27/05/2026 =
  26 dias; 40h - 4h = 36h).
- Estructura Fase 3 segun ROADMAP 72h (autoritativo, reemplaza version
  90h, linea 115): Cl 16-18 = estructura final del monologo (hook 1 min
  + cuerpo 3 puntos 3-5 min + cierre call to action 30-60 seg). Cl 18 =
  ultimo dia del sub-bloque "estructura" = PILLAR 3 parrafo completo +
  CALL TO ACTION; Cl 19-20 = pulir e integrar + ensayos orales del
  monologo completo.
- CHECKPOINT: segun la seccion CHECKPOINTS del ROADMAP 72h, C2 = fin
  Cl 12, C3 = fin Cl 20 (NO en Cl 18). El siguiente entregable de
  coordinacion es C3 (guion escrito completo, fin Cl 20). Por eso Cl 18
  NO tiene entregable de checkpoint; el PILLAR 3 + CTA hoy se archivan
  junto al HOOK Cl 16 y los pillars Cl 17 como la evidencia anti-fraude
  COMPLETA que alimenta C3.
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase18_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase18_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase18_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 17)', '5 min'),
    ('EL POR QUE DE HOY (dia 6 de Fase 3 - cierra estructura)', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (FORTALEZA dia 3 - TERCER dia del bloque)', '5 min'),
    ('RECAP EXPRESS - las 6 capas como sustrato del cierre del monologo', '5 min'),
    ('ACADEMIC B2 VOCAB SET #11 (6 palabras nuevas - total 66)', '8 min'),
    ('PLAN DE HOY: PILLAR 3 parrafo completo + CALL TO ACTION + BRIDGE DE VUELTA (pillar 3 academico / CTA casual ECHO del HOOK)', '12 min'),
    ('PEER TEACHER SLOT corto (error Cl 17)', '3 min'),
    ('ESCRITURA MANUSCRITA EN CLASE (anti-fraude): PILLAR 3 parrafo (mismo formato Cl 17) + CTA 30-60 seg (ECHO HOOK + verbo accion) - centro de hoy', '45 min'),
    ('LECTURA EN VOZ ALTA del PILLAR 3 + CTA + ajuste', '12 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE (errores de escritura del PILLAR 3 / CTA)', '5 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 17',
    'Foto del tablero - Frase del Dia + B2 Set #11 + Plan de hoy (PILLAR 3 + CTA) + Bridge de vuelta al registro del HOOK',
    'LAS 10 HOJAS MANUSCRITAS recogidas: PILLAR 3 (B2-AMINA-CL18-PILLAR3) + CTA (B2-AMINA-CL18-CTA) de cada estudiante (artefacto escrito en clase - anti-fraude; archivar junto a HOOK Cl 16 + P1+P2 Cl 17 - CIERRA la captura de evidencia para Checkpoint C3 fin Cl 20)',
    'NOTAS DE ARQUITECTURA POR ESTUDIANTE (interno - NO se comunica nota): PILLAR 3 mantiene formato academico de Cl 17 o se mezclo registro / PILLAR 3 connector apuntando al CTA o queda colgado / Set #11 dentro de PILLAR 3 / CTA casual/directo o se colo academico / CTA ECOA la imagen del HOOK transformada en accion o no conecta / CTA tiene verbo de accion imperative o se diluye / sigue siendo SU ingles vs sospecha IA',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: cualquier sospecha de texto IA / traido de casa (incl. "ya escribi el pillar 3 en casa" / "ya tengo el CTA") (notificar al cierre - Regla 3 Roadmap)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 17',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 6: Cl 16 escribio el HOOK / Cl 17 desarrollo PILLAR 1 + PILLAR 2 / hoy CIERRA el sub-bloque "estructura" = PILLAR 3 parrafo completo + CALL TO ACTION; Cl 19-20 pule e integra todo + ensayos orales',
    'ESCRIBI Frase del Dia + B2 Set #11 + Arquitectura COMPLETA (hook Cl16 / P1+P2 Cl17 / P3+CTA HOY) + Plan PILLAR 3 + CTA + Bridge de vuelta en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 18 = FORTALEZA dia 3 (TERCER dia del bloque - rotacion estandar cohorte B2, regla confirmada Diana 22/05)',
    'Hile FORTALEZA en VATS + Frase del Dia (coraje de un CTA que no se esconde en "so, yeah, that\'s it" + coraje de declarar EXPLICITAMENTE que el oyente debe HACER)',
    'Mantuve las 6 capas visibles como SUSTRATO del cierre del monologo (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-17)',
    'Presente 6 palabras B2 Set #11 con pronunciacion + ejemplo ESCRIBIBLE para PILLAR 3 / CTA (total 66)',
    'Mostre la ARQUITECTURA COMPLETA en tablero (HOOK Cl16 + P1+P2 Cl17 + P3+CTA HOY) con modelado en vivo (desarrollar pillar 3 + escribir CTA que ECOA hook)',
    'Aplique el bridge formal->casual al REGISTRO DE ESCRITURA CON BRIDGE DE VUELTA (PILLAR 3 academico - Set #11 vive aqui / CTA casual/directo - vuelve al registro del HOOK; Set #11 NO en el hook que ya esta cerrado Cl 16)',
    'Conduje la ESCRITURA MANUSCRITA EN CLASE como centro (45 min, a mano, sin dispositivos): PILLAR 3 (~120-160 palabras, ~80-110 Karen) + CTA (~70-130 palabras, ~50-80 Karen, 30-60 seg hablados)',
    'APLIQUE LA REGLA ANTI-FRAUDE: a mano + en clase; las paginas Cl 15-17 solo se releen para anclar PILLAR 3 y CTA; texto de casa (incl. "ya escribi el pillar 3 en casa" / "ya tengo el CTA") NO cuenta y se reescribe aqui',
    'Circule en silencio y registre NOTAS DE ARQUITECTURA por estudiante (INTERNO) sin comunicar nota ni juicio',
    'Conduje la LECTURA EN VOZ ALTA del PILLAR 3 + CTA como control de calidad (oral = soporte, NO Speak About) - sin pausa larga entre P3 y CTA para oir si el bridge funciona',
    'Camine con papel errores anonimo (errores de ESCRITURA: registro mezclado pillar3/CTA, B2 Set #11 mal ubicado, CTA sin echo al hook, CTA sin verbo accion imperative, concordancia 3a persona "summons/compels")',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'RECOGI las 10 hojas manuscritas (PILLAR 3 B2-AMINA-CL18-PILLAR3 + CTA B2-AMINA-CL18-CTA, 2 por estudiante)',
    'En Tarea explique el por que (26 dias hasta Final) + due date explicito (jueves 28/05 antes de 6:00 PM) + aclare que la escritura evaluable es EN CLASE',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes o sospecha de texto IA/de casa',
    'Anuncie Cl 19 = Fase 3 dia 7 (PULIR e INTEGRAR todo el guion completo + 1er ENSAYO ORAL del monologo completo)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase18_REPORTE.pdf'),
    'B2 PM AMINA | Cl 18 de 36 | FASE 3 DIA 6/8 — CIERRA ESTRUCTURA MONOLOGO: PILLAR 3 + CALL TO ACTION (anti-fraude) | DEL HABLA AL TEXTO + B2 SET #11 | FRASE DEL DIA (Goldlist retirado)',
    'FASE 3 DIA 6/8: Cl 16 abrio el sub-bloque ESTRUCTURA con HOOK + 3 PILLARS marcados; Cl 17 desarrollo PILLAR 1 + PILLAR 2 a parrafo completo del cuerpo -> hoy Cl 18 CIERRA el sub-bloque "ESTRUCTURA DEL MONOLOGO" (Roadmap 72h linea 115). Centro = ESCRITURA MANUSCRITA EN CLASE: PILLAR 3 desarrollado a parrafo completo del cuerpo (mismo formato Cl 17 - registro academico, topic chunk + connector apuntando al CTA, 2+ B2 Set #11 adentro) + CALL TO ACTION (30-60 seg hablados, registro casual/directo, ECHO del HOOK + verbo de accion imperative + linea final que cierra el arco), todo a mano sobre el guion ya cerrado Cl 13-17 (anti-fraude IA: a mano, en clase, sin dispositivos; las paginas Cl 15-17 solo se releen para anclar PILLAR 3 y CTA; texto de casa - incl. "ya escribi el pillar 3 en casa" / "ya tengo el CTA" - NO cuenta) + Academic B2 Set #11 (imperative/summon/urge/compel/beckon/prevail -> total 66, registro cierre del monologo) + las 6 capas como sustrato + lectura en voz alta del PILLAR 3 + CTA como control de calidad (sin pausa larga entre P3 y CTA para oir el bridge) + ~36h/~26 dias al Final + FRASE DEL DIA. Cuando suene la ultima campana, la arquitectura COMPLETA del monologo esta en papel: HOOK (Cl 16) + PILLAR 1 + PILLAR 2 (Cl 17) + PILLAR 3 + CTA (HOY). Estructura Fase 3 segun ROADMAP 72h: Cl 16-18 = hook 1 min + cuerpo 3 puntos 3-5 min + cierre call to action 30-60 seg (Cl 18 = ultimo dia = pillar 3 + CTA; Cl 19-20 = pulir e integrar todo + ensayos orales del monologo completo). CHECKPOINTS Roadmap: C3 = fin Cl 20 (NO en Cl 18); el PILLAR 3 + CTA hoy se archivan junto al HOOK Cl 16 y los pillars Cl 17 como la evidencia anti-fraude COMPLETA que alimenta C3. Calidad de la arquitectura evaluada INTERNO, NO se comunica nota.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase18_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 27/05 B2 PM Amina Cl 18:')
print('  - B2/B2_PM_Amina_Clase18_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase18_REPORTE.pdf')
