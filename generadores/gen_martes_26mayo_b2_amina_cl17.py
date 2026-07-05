#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 17 (martes 26/05/2026):
- FASE 3 DIA 5/8 - DESARROLLA dentro del sub-bloque "ESTRUCTURA DEL
  MONOLOGO". Centro = ESCRITURA MANUSCRITA EN CLASE: PILLAR 1 + PILLAR 2
  pasan de 1 linea (esqueleto Cl 16) a parrafo completo del cuerpo
  (3-5 oraciones cada uno; Karen 2-3), registro academico, integrando
  Set #9 + Set #10, regla anti-inflado (cada oracion earn su linea),
  todo a mano sobre los esqueletos marcados ayer Cl 16. El HOOK firmado
  Cl 16 NO se toca. PILLAR 3 + CTA esperan Cl 18. Anti-fraude IA:
  a mano, en clase, sin dispositivos; texto de casa - incl. "ya
  desarrolle el pillar 1 en casa" / "ya tengo el parrafo del pillar 2"
  - NO cuenta.
- Academic B2 Vocab Set #10 (6 nuevas: pertinent/salient/mitigate/
  advocate/contend/deem -> total 60) + Frase del Dia + virtud
  FORTALEZA dia 2 (segundo dia del bloque - regla cohorte B2,
  rotacion estandar, NO supuesto).
- ~38 horas / ~27 dias hasta el Final (~22 junio) - derivado de Cl 16
  (40h/28d) +1 dia calendario (lun 25 -> mar 26) -2h clase (verificado:
  22/06/2026 - 26/05/2026 = 27 dias; 40h - 2h = 38h).
- Estructura Fase 3 segun ROADMAP 72h (autoritativo, reemplaza version
  90h, linea 115): Cl 16-18 = estructura final del monologo (hook 1 min
  + cuerpo 3 puntos 3-5 min + cierre call to action 30-60 seg). Cl 17 =
  segundo dia del sub-bloque "estructura" = desarrollar PILLAR 1 +
  PILLAR 2 a parrafo completo del cuerpo; el pillar 3 y el call to
  action son Cl 18; Cl 19-20 pulir + ensayo.
- CHECKPOINT: segun la seccion CHECKPOINTS del ROADMAP 72h, C2 = fin
  Cl 12, C3 = fin Cl 20 (NO en Cl 17). El siguiente entregable de
  coordinacion es C3 (guion escrito, fin Cl 20). Por eso Cl 17 NO tiene
  entregable de checkpoint; PILLAR 1 + PILLAR 2 desarrollados se
  archivan como evidencia anti-fraude que alimenta C3.
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase17_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase17_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase17_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 16)', '5 min'),
    ('EL POR QUE DE HOY (dia 5 de Fase 3 - desarrolla pillars 1 y 2)', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (FORTALEZA dia 2 - segundo dia del bloque)', '5 min'),
    ('RECAP EXPRESS - las 6 capas como sustrato del desarrollo de pillars', '5 min'),
    ('ACADEMIC B2 VOCAB SET #10 (6 palabras nuevas - total 60)', '8 min'),
    ('PLAN DE HOY: PILLAR 1 + PILLAR 2 a parrafo completo + REGLA ANTI-INFLADO (substance, not stuffing)', '12 min'),
    ('PEER TEACHER SLOT corto (error Cl 16)', '3 min'),
    ('ESCRITURA MANUSCRITA EN CLASE (anti-fraude): PILLAR 1 + PILLAR 2 desarrollados a parrafo completo (3-5 oraciones cada uno, registro academico, Set #9 + #10 dentro) - centro de hoy', '45 min'),
    ('LECTURA EN VOZ ALTA de PILLAR 1 + PILLAR 2 + ajuste', '12 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE (errores de escritura: registro mezclado hook/body, concordancia plural pillars, vocab Set #10 mal ubicado, oracion que no earn su linea)', '5 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 16',
    'Foto del tablero - Frase del Dia + B2 Set #10 + Plan de hoy (PILLAR 1 + PILLAR 2 a parrafo) + Anti-stuffing rule',
    'LAS 5 HOJAS MANUSCRITAS recogidas: PILLAR 1 + PILLAR 2 desarrollados (B2-AMINA-CL17-P1P2) + paginas Cl 15 con marcas [H][1][2][3] intactas (PILLAR 3 sin tocar) + HOJA HOOK Cl 16 sin tocar (artefacto escrito en clase - anti-fraude; archivar, alimenta Checkpoint C3 fin Cl 20)',
    'NOTAS DE DESARROLLO POR ESTUDIANTE (interno - NO se comunica nota): pillar 1/pillar 2 3-5 oraciones o se inflo / 2+ Set #10 + 1+ Set #9 en el cuerpo NO en el hook / discourse marker MID-paragraph / S5 parafrasis real o solo sinonimos / connector forward al final de pillar 1 aterriza en pillar 2 / pillar 2 es sustancia nueva o pillar 1 recoloreado / sigue siendo SU ingles vs sospecha IA',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: cualquier sospecha de texto IA / traido de casa (incl. "ya desarrolle el pillar 1 en casa" / "ya tengo el parrafo del pillar 2") (notificar al cierre - Regla 3 Roadmap)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 16',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 5: Cl 16 abrio estructura (HOOK firmado + 3 PILLARS marcados con 1 linea cada uno) / hoy DESARROLLA pillar 1 + pillar 2 a parrafo completo del cuerpo; Cl 18 = pillar 3 + call to action; Cl 19-20 pulir + ensayo',
    'ESCRIBI Frase del Dia + B2 Set #10 + Arquitectura (HOOK firmado / P1+P2 HOY / P3+CTA Cl 18) + Plan PILLAR 1+2 + Regla anti-stuffing en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 17 = FORTALEZA dia 2 (segundo dia del bloque - rotacion estandar cohorte B2, regla confirmada Diana 22/05)',
    'Hile FORTALEZA en VATS + Frase del Dia (coraje de no quedarse en el esqueleto comodo + coraje de comprometer una palabra Set #10 dentro del pillar que cuesta mas)',
    'Mantuve las 6 capas visibles como SUSTRATO del desarrollo de pillars (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing) - ahora viven DENTRO de cada pillar',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-16)',
    'Presente 6 palabras B2 Set #10 (pertinent/salient/mitigate/advocate/contend/deem) con pronunciacion + ejemplo ESCRIBIBLE para el CUERPO del monologo (total 60)',
    'Mostre la SHAPE del pillar paragraph en tablero (S1 chunk / S2 support / S3 depth con discourse marker / S4 opcional / S5 parafrasis-cierre con connector forward) con modelado en vivo',
    'Aplique la REGLA ANTI-INFLADO (substance not stuffing): cada oracion EARN su linea - corta repeticion de S1 con sinonimos / corta vocab decorativo / corta material de HOOK que se cuela al body',
    'Conduje la ESCRITURA MANUSCRITA EN CLASE como centro (45 min, a mano, sin dispositivos): PILLAR 1 desarrollado (3-5 oraciones; Karen 2-3) + PILLAR 2 desarrollado (misma shape, distinto Set #10 word) sobre los esqueletos Cl 16; HOOK firmado NO se toca; PILLAR 3 NO se toca',
    'APLIQUE LA REGLA ANTI-FRAUDE: a mano + en clase; el HOOK Cl 16 y los esqueletos [1][2][3] solo se releen para expandir; texto de casa (incl. "ya desarrolle el pillar 1 en casa" / "ya tengo el parrafo del pillar 2") NO cuenta y se reescribe aqui',
    'Circule en silencio y registre NOTAS DE DESARROLLO por estudiante (INTERNO) sin comunicar nota ni juicio',
    'Conduje la LECTURA EN VOZ ALTA de PILLAR 1 + PILLAR 2 como control de calidad (oral = soporte, NO Speak About); cohorte solo señala inflado / registro mezclado con mano arriba',
    'Camine con papel errores anonimo (errores de ESCRITURA: registro de hook colado al body, concordancia pillar/pillars, Set #10 decorativo, oracion que no earn su linea)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'RECOGI las 5 hojas manuscritas (PILLAR 1 + PILLAR 2 firmado B2-AMINA-CL17-P1P2 + paginas Cl 15 intactas con [H][1][2][3] + HOJA HOOK Cl 16 sin tocar)',
    'En Tarea explique el por que (27 dias hasta Final) + due date explicito (miercoles 27/05 antes de 6:00 PM) + aclare que el componente 3 es RE-LECTURA del texto escrito hoy en clase, NO texto nuevo de casa, y que la escritura evaluable es EN CLASE',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes o sospecha de texto IA/de casa',
    'Anuncie Cl 18 = Fase 3 dia 6 (PILLAR 3 a parrafo completo + CALL TO ACTION 30-60 seg, bridge de regreso al casual)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase17_REPORTE.pdf'),
    'B2 PM AMINA | Cl 17 de 36 | FASE 3 DIA 5/8 — DESARROLLA PILLAR 1 + PILLAR 2 A PARRAFO COMPLETO (anti-fraude + anti-stuffing) | DEL HABLA AL TEXTO + B2 SET #10 | FRASE DEL DIA (Goldlist retirado)',
    'FASE 3 DIA 5/8: Cl 16 ABRIO el sub-bloque "ESTRUCTURA DEL MONOLOGO" (HOOK firmado en hoja aparte + 3 PILLARS marcados [1][2][3] + 1 linea cada uno sobre paginas Cl 15) -> hoy Cl 17 DESARROLLA dentro del mismo sub-bloque (Cl 16-18, Roadmap 72h linea 115). Centro = ESCRITURA MANUSCRITA EN CLASE: PILLAR 1 y PILLAR 2 pasan de 1 linea cada uno a PARRAFO COMPLETO del cuerpo (3-5 oraciones cada uno; Karen 2-3), registro academico, integrando Set #9 + Set #10, con shape definida (S1 topic chunk / S2 support / S3 depth con discourse marker mid-paragraph / S4 opcional / S5 parafrasis-cierre con connector forward que aterriza en pillar 2) y REGLA ANTI-INFLADO activa (cada oracion EARN su linea - corta repeticion de S1 con sinonimos, corta vocab decorativo, corta material de HOOK que se cuela al body). El HOOK firmado Cl 16 NO se toca. PILLAR 3 + CALL TO ACTION son Cl 18 - NO se invaden hoy. Todo sobre los esqueletos ya marcados ayer (anti-fraude IA: a mano, en clase, sin dispositivos; HOOK + esqueletos Cl 16 solo se releen para expandir; texto de casa - incl. "ya desarrolle el pillar 1 en casa" / "ya tengo el parrafo del pillar 2" - NO cuenta) + Academic B2 Set #10 (pertinent/salient/mitigate/advocate/contend/deem -> total 60, registro cuerpo del monologo) + las 6 capas como sustrato que ahora vive DENTRO de cada pillar + lectura en voz alta de los 2 pillars como control de calidad + ~38h/~27 dias al Final + FRASE DEL DIA ("develop with substance, not with stuffing - and let each pillar warrant its place by what it earns, not by what it pads"). CHECKPOINTS Roadmap: C3 = fin Cl 20 (NO en Cl 17); PILLAR 1 + PILLAR 2 desarrollados se archivan como evidencia anti-fraude que alimenta C3. Calidad del desarrollo evaluada INTERNO, NO se comunica nota.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase17_REPORTE.pdf')

print('\n2 PDFs generados para martes 26/05 B2 PM Amina Cl 17:')
print('  - B2/B2_PM_Amina_Clase17_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase17_REPORTE.pdf')
