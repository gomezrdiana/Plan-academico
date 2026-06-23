#!/usr/bin/env python3
"""Genera la guia + reporte del B2 PM Amina Cl 16 (lunes 25/05/2026):
- FASE 3 DIA 4/8 - ABRE EL SUB-BLOQUE "ESTRUCTURA DEL MONOLOGO".
  Centro = ESCRITURA MANUSCRITA EN CLASE: HOOK (1 min, casual/directo,
  registro punchy) escrito fresco a mano sobre el guion ya transcrito
  Cl 13-15 + ESQUELETO DEL CUERPO marcado a mano (3 PILLARS [1][2][3]
  + 1 linea bajo cada uno) sobre las paginas cerradas Cl 15 (registro
  academico - Set #9 vive aqui). Anti-fraude IA: a mano, en clase, sin
  dispositivos; texto de casa - incl. "ya hice el hook en casa" / "ya
  organice los 3 puntos en casa" - NO cuenta.
- Academic B2 Vocab Set #9 (6 nuevas: proponent/discern/constitute/
  endure/stipulate/warrant -> total 54) + Frase del Dia + virtud
  FORTALEZA dia 1 (PRIMER dia del bloque - regla cohorte B2,
  rotacion estandar, NO supuesto).
- ~40 horas / ~28 dias hasta el Final (~22 junio) - derivado de Cl 15
  (42h/31d) +3 dias calendario (vie 22 -> lun 25) -2h clase (verificado:
  22/06/2026 - 25/05/2026 = 28 dias; 42h - 2h = 40h).
- Estructura Fase 3 segun ROADMAP 72h (autoritativo, reemplaza version
  90h, linea 115): Cl 16-18 = estructura final del monologo (hook 1 min
  + cuerpo 3 puntos 3-5 min + cierre call to action 30-60 seg). Cl 16 =
  primer dia del sub-bloque "estructura" = HOOK + esqueleto del cuerpo
  (3 pillars); el call to action y el desarrollo de cada pillar son
  Cl 17-18.
- CHECKPOINT: segun la seccion CHECKPOINTS del ROADMAP 72h, C2 = fin
  Cl 12, C3 = fin Cl 20 (NO en Cl 16). El siguiente entregable de
  coordinacion es C3 (guion escrito, fin Cl 20). Por eso Cl 16 NO tiene
  entregable de checkpoint; el HOOK + las marcas [H][1][2][3] se
  archivan como evidencia anti-fraude que alimenta C3.
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase16_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase16_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase16_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 15)', '5 min'),
    ('EL POR QUE DE HOY (dia 4 de Fase 3 - abre estructura)', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (FORTALEZA dia 1 - PRIMER dia del bloque)', '5 min'),
    ('RECAP EXPRESS - las 6 capas como sustrato del cuerpo del monologo', '5 min'),
    ('ACADEMIC B2 VOCAB SET #9 (6 palabras nuevas - total 54)', '8 min'),
    ('PLAN DE HOY: HOOK + ESQUELETO CUERPO (3 PILLARS) + REGISTRO SPLIT (hook casual / body academico)', '12 min'),
    ('PEER TEACHER SLOT corto (error Cl 15)', '3 min'),
    ('ESCRITURA MANUSCRITA EN CLASE (anti-fraude): HOOK (1 min) + 3 PILLARS marcados sobre Cl 15 - centro de hoy', '45 min'),
    ('LECTURA EN VOZ ALTA del HOOK + ajuste', '12 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE (errores de escritura del hook / arquitectura)', '5 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 15',
    'Foto del tablero - Frase del Dia + B2 Set #9 + Plan de hoy (HOOK + 3 PILLARS) + Registro Split',
    'LAS 5 HOJAS MANUSCRITAS recogidas: HOOK NUEVO (B2-AMINA-CL16-HOOK) + paginas Cl 15 con marcas [H][1][2][3] y 1 linea bajo cada pillar (artefacto escrito en clase - anti-fraude; archivar, alimenta Checkpoint C3 fin Cl 20)',
    'NOTAS DE ARQUITECTURA POR ESTUDIANTE (interno - NO se comunica nota): HOOK casual/directo o se le colo academico / HOOK 1 anchor + opening marker o cualquiera / HOOK ~1 min o desbordado / 3 PILLARS distintos o repetidos / uso Set #9 en pillars NO en hook / sigue siendo SU ingles vs sospecha IA',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: cualquier sospecha de texto IA / traido de casa (incl. "ya hice el hook en casa" / "ya organice los 3 puntos en casa") (notificar al cierre - Regla 3 Roadmap)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 15',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 4: Cl 13-15 cerro la transcripcion (audio 1 + audio 2 en texto B2 limpio) / hoy ABRE el sub-bloque "estructura": HOOK + esqueleto del cuerpo (3 pillars); Cl 17-18 desarrolla cada pillar + call to action',
    'ESCRIBI Frase del Dia + B2 Set #9 + Arquitectura (hook/3 pillars/CTA Cl 17-18) + Plan HOOK + Registro Split en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 16 = FORTALEZA dia 1 (PRIMER dia del bloque - rotacion estandar cohorte B2, regla confirmada Diana 22/05)',
    'Hile FORTALEZA en VATS + Frase del Dia (coraje de un HOOK que no se esconde en muletillas + coraje de declarar SOLO 3 pillars fuertes)',
    'Mantuve las 6 capas visibles como SUSTRATO del cuerpo del monologo (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-15)',
    'Presente 6 palabras B2 Set #9 con pronunciacion + ejemplo ESCRIBIBLE para el CUERPO del monologo (total 54)',
    'Mostre la ARQUITECTURA en tablero (hook 1 min + 3 pillars 3-5 min + CTA Cl 17-18) con modelado en vivo (marcar [H][1][2][3] + escribir hook)',
    'Aplique el bridge formal->casual al REGISTRO DE ESCRITURA con SPLIT intencional (HOOK casual/directo vs CUERPO academico - Set #9 vive en el cuerpo, NO en el hook)',
    'Conduje la ESCRITURA MANUSCRITA EN CLASE como centro (45 min, a mano, sin dispositivos): HOOK fresco (1 min spoken, casual) + 3 PILLARS marcados [1][2][3] sobre Cl 15 + 1 linea bajo cada pillar',
    'APLIQUE LA REGLA ANTI-FRAUDE: a mano + en clase; los 2 textos Cl 15 solo se releen para extraer arquitectura; texto de casa (incl. "ya hice el hook en casa" / "ya organice los 3 puntos en casa") NO cuenta y se reescribe aqui',
    'Circule en silencio y registre NOTAS DE ARQUITECTURA por estudiante (INTERNO) sin comunicar nota ni juicio',
    'Conduje la LECTURA EN VOZ ALTA del HOOK como control de calidad (oral = soporte, NO Speak About)',
    'Camine con papel errores anonimo (errores de ESCRITURA: registro mezclado hook/body, concordancia plural pillars, B2 Set #9 mal ubicado, muletilla en hook)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'RECOGI las 5 hojas manuscritas (HOOK B2-AMINA-CL16-HOOK + paginas Cl 15 con marcas [H][1][2][3] y 1 linea bajo cada pillar)',
    'En Tarea explique el por que (28 dias hasta Final) + due date explicito (miercoles 27/05 antes de 6:00 PM) + aclare que la escritura evaluable es EN CLASE',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes o sospecha de texto IA/de casa',
    'Anuncie Cl 17 = Fase 3 dia 5 (desarrollar PILLAR 1 + PILLAR 2 a parrafo completo del cuerpo)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase16_REPORTE.pdf'),
    'B2 PM AMINA | Cl 16 de 36 | FASE 3 DIA 4/8 — ESTRUCTURA MONOLOGO HOOK + CUERPO (anti-fraude) | DEL HABLA AL TEXTO + B2 SET #9 | FRASE DEL DIA (Goldlist retirado)',
    'FASE 3 DIA 4/8: Cl 13-15 cerro el sub-bloque de TRANSCRIPCION (audio 1 final + audio 2 final en texto B2 limpio) -> hoy Cl 16 ABRE el sub-bloque "ESTRUCTURA DEL MONOLOGO" (Cl 16-18, Roadmap 72h linea 115). Centro = ESCRITURA MANUSCRITA EN CLASE: HOOK fresco a mano (1 min spoken, registro casual/directo, punchy - "the line that compels a listener to stay") + ESQUELETO DEL CUERPO marcado a mano (3 PILLARS [1][2][3] + 1 linea bajo cada uno) directamente sobre las paginas cerradas Cl 15 (registro academico - Set #9 vive aqui, NO en el hook), todo sobre el guion ya transcrito Cl 13-15 (anti-fraude IA: a mano, en clase, sin dispositivos; los 2 textos cerrados solo se releen para extraer arquitectura; texto de casa - incl. "ya hice el hook en casa" / "ya organice los 3 puntos en casa" - NO cuenta) + Academic B2 Set #9 (proponent/discern/constitute/endure/stipulate/warrant -> total 54, registro cuerpo del monologo) + las 6 capas como sustrato de la arquitectura + lectura en voz alta del HOOK como control de calidad + ~40h/~28 dias al Final + FRASE DEL DIA. Estructura Fase 3 segun ROADMAP 72h: Cl 16-18 = hook 1 min + cuerpo 3 puntos 3-5 min + cierre call to action 30-60 seg (Cl 16 = primer dia = hook + esqueleto; Cl 17-18 = desarrollar cada pillar + agregar CTA). CHECKPOINTS Roadmap: C3 = fin Cl 20 (NO en Cl 16); el HOOK + las marcas [H][1][2][3] se archivan como evidencia anti-fraude que alimenta C3. Calidad de la arquitectura evaluada INTERNO, NO se comunica nota.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase16_REPORTE.pdf')

print('\n2 PDFs generados para lunes 25/05 B2 PM Amina Cl 16:')
print('  - B2/B2_PM_Amina_Clase16_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase16_REPORTE.pdf')
