#!/usr/bin/env python3
"""Genera la guia + reporte del B2 PM Amina Cl 19 (jueves 28/05/2026):
- FASE 3 DIA 7/8 - ABRE EL SUB-BLOQUE "PULIR + ENSAYO".
  Centro = LECTURA COMPLETA EN VOZ ALTA POR PRIMERA VEZ (HOOK + 3
  PILLARS + CTA, target 5-7 min cronometrados) + REVISION EN PAREJAS
  (1 feedback de COHERENCIA + 1 feedback de VOCAB ACADEMICO, exactos)
  + REESCRITURA A MANO de las mejoras SOBRE las mismas hojas Cl 16-18
  (tachon limpio + correccion encima/margen + firma "/19" + flecha "<<")
  - mismo papel, NO hoja nueva, trazabilidad anti-fraude. Anti-fraude IA:
  a mano, en clase, sin dispositivos; texto pulido en casa - incl. "ya
  puli en casa" / "tengo la version limpia mecanografiada" - NO cuenta.
- Academic B2 Vocab Set #12 (6 nuevas: scrutinize/refine/elaborate/
  synthesize/articulate/integrate -> total 72) - VERBOS DE POLISH:
  viven en la metalengua de la revision, NO en el contenido del
  monologo + Frase del Dia + virtud FORTALEZA dia 4 (rotacion
  estandar cohorte B2, bloques de 5 - Cl 16-20 FORTALEZA v1, hoy
  dia 4 del bloque, regla confirmada Diana 22/05, NO supuesto).
- ~34 horas / ~25 dias hasta el Final (~22 junio) - derivado de Cl 16
  (40h/28d) +3 dias calendario (lun 25 -> jue 28) -6h cursadas Cl 17-19
  (verificado: 22/06/2026 - 28/05/2026 = 25 dias; 40h - 6h = 34h).
- Estructura Fase 3 segun ROADMAP 72h (autoritativo, reemplaza version
  90h, linea 116): Cl 19-20 = pulir vocabulario B2 + ensayo oral completo
  + cierre Fase 3 + Checkpoint C3 (fin Cl 20). Cl 19 = primer dia del
  sub-bloque "pulir + ensayo" = LEER COMPLETO + REVISAR EN PAREJAS +
  REESCRIBIR MEJORAS sobre las mismas hojas Cl 16-18; el 2do ensayo
  formal + cierre Fase 3 + entrega C3 son Cl 20.
- CHECKPOINT: segun la seccion CHECKPOINTS del ROADMAP 72h, C3 = fin
  Cl 20 (NO en Cl 19). Por eso Cl 19 NO tiene entregable de checkpoint;
  las hojas Cl 16-18 con las reescrituras /19 de hoy se archivan como
  evidencia anti-fraude que SE SUMA a las reescrituras /20 de manana
  para conformar el entregable C3 completo.
- ANUNCIO Cl 20 = CHECKPOINT C3 (entrega del guion escrito completo a
  coordinacion) + 2do ensayo oral + cierre Fase 3 = hecho de calendario.
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase19_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase19_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase19_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 18)', '5 min'),
    ('EL POR QUE DE HOY (dia 7 de Fase 3 - abre pulir + ensayo)', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (FORTALEZA dia 4 - rotacion estandar cohorte B2)', '5 min'),
    ('RECAP EXPRESS - las 6 capas + ARQUITECTURA COMPLETA visible (HOOK + 3 PILLARS + CTA)', '5 min'),
    ('ACADEMIC B2 VOCAB SET #12 (6 palabras nuevas - verbos de POLISH - total 72)', '8 min'),
    ('PLAN DE HOY: LEER COMPLETO EN VOZ ALTA + REVISAR EN PAREJAS (1 coherencia + 1 vocab) + REESCRIBIR MEJORAS A MANO sobre Cl 16-18', '9 min'),
    ('PEER TEACHER SLOT corto (error Cl 18)', '3 min'),
    ('LECTURA EN VOZ ALTA COMPLETA + REVISION EN PAREJAS + REESCRIBIR MEJORAS A MANO sobre Cl 16-18 - centro de hoy (cronometrado 5-7 min por lectura, parejas + floater, reescritura con /19)', '45 min'),
    ('CIERRE ORAL - 1 estudiante lee completo ante el grupo + feedback colectivo estructurado', '12 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE (errores ORALES de hoy: pronunciacion, conexion entre pillars, transicion a CTA)', '5 min'),
    ('TAREA STRICT 4 componentes + ANUNCIO CL 20 = CHECKPOINT C3 + CIERRE', '5 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 18',
    'Foto del tablero - Frase del Dia + B2 Set #12 + Arquitectura completa (HOOK + 3 PILLARS + CTA) + Plan de hoy (LEER + PAIR REVIEW + REWRITE) + Protocolo de pareja (1 coherencia + 1 vocab)',
    'LAS 5 HOJAS CL 16-18 CON LAS MARCAS DE CL 19 recogidas y devueltas: minutos hablados al tope del HOOK + 2-5 tachones limpios + correcciones firmadas /19 + flechas << en margen + 1 linea de feedback de pareja al tope del CTA (artefacto escrito en clase - anti-fraude; archivar, alimenta CHECKPOINT C3 fin Cl 20 manana)',
    'NOTAS DE LECTURA + REVISION POR ESTUDIANTE (interno - NO se comunica nota): duracion 5-7 min o no / joints flojos (hook-p1, p1-p2, p2-p3, p3-CTA) / pareja dio 2 feedbacks exactos o se desvio / reescribio sobre mismas hojas con /19 o trajo hoja nueva / uso Set #12 en metalengua o solo en contenido / sigue siendo SU ingles vs sospecha IA',
    'Papel errores fisico (anonimo) - hoy errores ORALES: pronunciacion, conexion entre pillars, transicion a CTA',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: cualquier sospecha de texto IA / traido de casa (incl. "ya puli en casa" / "tengo la version limpia mecanografiada") (notificar al cierre - Regla 3 Roadmap)',
    'CONFIRMACION PARA COORDINACION: CHECKPOINT C3 manana Cl 20 - entrega del guion escrito completo (Cl 16-18 + rewrites /19 + rewrites finales /20)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 18',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 7: Cl 16-18 cerro la estructura (monologo entero HOOK + 3 PILLARS + CTA escrito a mano) / hoy ABRE el sub-bloque "pulir + ensayo": LEER COMPLETO + PAIR REVIEW + REWRITE sobre Cl 16-18; Cl 20 manana = 2do ensayo + CHECKPOINT C3 + cierre Fase 3',
    'ESCRIBI Frase del Dia + B2 Set #12 + Arquitectura completa (HOOK + 3 PILLARS + CTA) + Plan LEER+REVISAR+REESCRIBIR + Protocolo de pareja (2 feedbacks exactos) en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 19 = FORTALEZA dia 4 (rotacion estandar cohorte B2, bloques de 5 - Cl 16-20 FORTALEZA v1, hoy dia 4 del bloque, regla confirmada Diana 22/05)',
    'Hile FORTALEZA en VATS + Frase del Dia (coraje de leer 5-7 min sin parar + coraje de recibir el feedback de la pareja sin defenderse + coraje de reescribir sobre el mismo papel sin desechar)',
    'Mantuve las 6 capas + la ARQUITECTURA COMPLETA visible en tablero (HOOK + 3 PILLARS + CTA + tiempo total 5-7 min)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-18)',
    'Presente 6 palabras B2 Set #12 (scrutinize/refine/elaborate/synthesize/articulate/integrate) con pronunciacion + ejemplo de ACCION DE POLISH - aclare que viven en la METALENGUA de la revision NO en el contenido del monologo (total 72)',
    'Mostre los 4 JOINTS donde vive el pulido (hook->pillar 1, pillar 1->pillar 2, pillar 2->pillar 3, pillar 3->CTA) y modele en vivo como suena un joint flojo vs un joint con connector',
    'Aplique el bridge formal->casual al CIERRE del monologo (CTA = bridge) y al PULIDO (HOOK queda casual, no se sube a academico; BODY queda academico, no se baja a charla; CTA = bridge)',
    'Conduje la LECTURA COMPLETA EN VOZ ALTA por primera vez (cronometrada 5-7 min) - asignacion de parejas (2 parejas + 1 floater rotando) - protocolo estricto de pareja: EXACTAMENTE 2 feedbacks (1 COHERENCIA + 1 VOCAB ACADEMICO) - PROHIBIDO juicio / pronunciacion / "estuvo bonito" / mas de 2 feedbacks',
    'Conduje la REESCRITURA A MANO sobre las mismas hojas Cl 16-18 (tachon limpio + correccion encima/margen + firma /19 + flecha << en margen) - minimo 2 reescrituras, maximo 5 - NO hoja nueva, NO descartar',
    'Conduje el 2do micro-ensayo post-pulido en parejas (lectura SOLO de las partes reescritas + confirmacion 1 palabra: sharper/clearer/still flat)',
    'Conduje el CIERRE ORAL: 1 estudiante AL AZAR leyo COMPLETO ante el grupo (5-7 min) + feedback colectivo estructurado (2 coherencia + 1 vocab + 1 confirmacion de proceso)',
    'APLIQUE LA REGLA ANTI-FRAUDE: a mano + en clase + sobre las MISMAS hojas Cl 16-18; texto pulido en casa (incl. "ya puli en casa" / "tengo la version limpia mecanografiada") NO cuenta y se reescribe aqui sobre Cl 16-18',
    'Circule en silencio con cronometro y libreta personal y registre NOTAS DE LECTURA + REVISION por estudiante (INTERNO) sin comunicar nota ni juicio',
    'Camine con papel errores anonimo (errores ORALES de hoy: pronunciacion, joints sin connector, CTA leida como otro pillar, Set #12 mal ubicado en el monologo en vez de en la metalengua)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (pronunciacion, conexion entre pillars, transicion a CTA)',
    'RECOGI las 5 hojas Cl 16-18 con las marcas de Cl 19 (minutos al tope del HOOK + tachones /19 + flechas << + 1 linea de feedback de pareja al tope del CTA)',
    'En Tarea explique el por que (25 dias hasta Final + Checkpoint C3 manana) + due date explicito (viernes 29/05 antes de 6:00 PM) + 4 componentes B2 Amina (lectura completa x3 en casa + audio completo 5-7 min + escucha + 3 mejoras + repaso vocab 72 palabras) + aclare que la escritura evaluable es EN CLASE',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes o sospecha de texto IA/de casa',
    'ANUNCIE CL 20 (manana viernes 29/05) = FASE 3 DIA 8 = CHECKPOINT C3 como HECHO DE CALENDARIO (entrega del guion escrito completo Cl 16-18 + /19 + /20 a coordinacion) + 2do ensayo oral completo en frente del grupo + cierre formal de Fase 3 - SIN comunicar nota ni juicio',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase19_REPORTE.pdf'),
    'B2 PM AMINA | Cl 19 de 36 | FASE 3 DIA 7/8 — PULIR + 1ER ENSAYO ORAL COMPLETO (anti-fraude, mismo papel) | LECTURA COMPLETA + PAIR REVIEW + REWRITE /19 + B2 SET #12 | FRASE DEL DIA (Goldlist retirado)',
    'FASE 3 DIA 7/8: Cl 16-18 cerro el sub-bloque de ESTRUCTURA (monologo entero HOOK + 3 PILLARS + CTA escrito a mano sobre el guion transcrito Cl 13-15) -> hoy Cl 19 ABRE el sub-bloque "PULIR + ENSAYO" (Cl 19-20, Roadmap 72h linea 116). Centro = LECTURA COMPLETA EN VOZ ALTA POR PRIMERA VEZ del monologo entero (HOOK + 3 PILLARS + CTA, target 5-7 min cronometrados) + REVISION EN PAREJAS con protocolo estricto (EXACTAMENTE 2 feedbacks: 1 COHERENCIA + 1 VOCAB ACADEMICO - NADA de juicio, pronunciacion ni "estuvo bonito") + REESCRITURA A MANO de las mejoras SOBRE las mismas hojas Cl 16-18 (tachon limpio + correccion encima/margen + firma "/19" + flecha "<<" en margen - mismo papel, NO hoja nueva, trazabilidad anti-fraude). Anti-fraude IA: a mano, en clase, sin dispositivos; texto pulido en casa - incl. "ya puli en casa" / "tengo la version limpia mecanografiada" - NO cuenta + Academic B2 Set #12 (scrutinize/refine/elaborate/synthesize/articulate/integrate -> total 72) VERBOS DE POLISH que viven en la metalengua de la revision NO en el contenido del monologo + las 6 capas + ARQUITECTURA COMPLETA visible como sustrato + 2do micro-ensayo post-pulido en parejas + cierre oral con 1 lectura completa ante el grupo + feedback colectivo estructurado + ~34h/~25 dias al Final + FRASE DEL DIA. Estructura Fase 3 segun ROADMAP 72h: Cl 19-20 = pulir + ensayo oral + cierre Fase 3 + Checkpoint C3 (Cl 19 = primer dia = leer completo + pair review + rewrite; Cl 20 = 2do ensayo formal + entrega C3 + cierre Fase 3). CHECKPOINTS Roadmap: C3 = fin Cl 20 (NO en Cl 19); las hojas Cl 16-18 con rewrites /19 se archivan como evidencia anti-fraude que SE SUMA a rewrites /20 manana para conformar el entregable C3 completo. ANUNCIO CL 20 = HECHO DE CALENDARIO. Calidad oral + revision evaluada INTERNO, NO se comunica nota.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase19_REPORTE.pdf')

print('\n2 PDFs generados para jueves 28/05 B2 PM Amina Cl 19:')
print('  - B2/B2_PM_Amina_Clase19_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase19_REPORTE.pdf')
