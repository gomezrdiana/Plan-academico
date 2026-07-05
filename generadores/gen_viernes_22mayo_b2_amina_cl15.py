#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 15 (viernes 22/05/2026):
- FASE 3 DIA 3/8 - CIERRA EL SUB-BLOQUE DE TRANSCRIPCION: DEL HABLA AL TEXTO.
  Centro = ESCRITURA MANUSCRITA EN CLASE: terminar/limpiar el AUDIO 2
  (Steps 3->4->5 = texto B2 final) + CIERRE del sub-bloque (audio 1 final +
  audio 2 final juntos = semilla del guion del Final). Ambos audios de Fase 2
  a texto B2 limpio (anti-fraude IA: a mano, en clase, sin dispositivos;
  texto de casa - incl. "avance audio 2 en casa" - NO cuenta).
- Academic B2 Vocab Set #8 (6 nuevas -> total 48) + Frase del Dia +
  virtud JUSTICIA dia 5 (ultimo del bloque).
- ~42 horas / ~31 dias hasta el Final (~22 junio) — derivado de Cl 14
  (44h/32d) -1 dia calendario -2h clase (verificado: 22/06/2026 - 22/05/2026
  = 31 dias; 44h - 2h = 42h).
- Estructura Fase 3 segun ROADMAP 72h (autoritativo, reemplaza version 90h):
  Fase 3 = Cl 13-20; Cl 13-15 = transcribir a mano 2 audios de Fase 2
  (Cl 13 = audio 1 arranque; Cl 14 = cerrar audio 1 + abrir audio 2;
  Cl 15 = cerrar audio 2 + cerrar sub-bloque).
- CHECKPOINT: segun la seccion CHECKPOINTS del ROADMAP 72h, C2 = FIN CL 12
  (NO en Cl 15). El siguiente entregable de coordinacion es C3 = fin Cl 20
  (guion escrito). Por eso Cl 15 NO tiene entregable de checkpoint; las hojas
  manuscritas se archivan como evidencia anti-fraude que alimenta C3.
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase15_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase15_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase15_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 14)', '5 min'),
    ('EL POR QUE DE HOY (dia 3 de Fase 3 - cierre del sub-bloque)', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (JUSTICIA dia 5 - ultimo del bloque)', '5 min'),
    ('RECAP EXPRESS - las 6 capas como sustrato del texto', '5 min'),
    ('ACADEMIC B2 VOCAB SET #8 (6 palabras nuevas - total 48)', '8 min'),
    ('PLAN DE HOY: cerrar AUDIO 2 + CIERRE sub-bloque + REGISTRO ESCRITO formal->casual', '12 min'),
    ('PEER TEACHER SLOT corto (error Cl 14)', '3 min'),
    ('ESCRITURA MANUSCRITA EN CLASE (anti-fraude): terminar AUDIO 2 + cerrar sub-bloque - centro de hoy', '45 min'),
    ('LECTURA EN VOZ ALTA del propio texto + ajuste', '12 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE (errores de escritura)', '5 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 14',
    'Foto del tablero - Frase del Dia + B2 Set #8 + Plan de hoy (Audio 2 / cierre sub-bloque)',
    'LAS 5 HOJAS MANUSCRITAS recogidas: AUDIO 1 final + AUDIO 2 final (sub-bloque de transcripcion CERRADO - los 2 audios en texto B2) (artefacto escrito en clase - anti-fraude; archivar, alimenta Checkpoint C3 fin Cl 20)',
    'NOTAS DE TRANSICION habla->texto POR ESTUDIANTE (interno - NO se comunica nota): cierra audio 2 o se atasca / los 2 textos coherentes o uno muy flojo / muletillas en la pagina / sigue siendo SU ingles vs sospecha IA / B2 Set #8 escrito / anchor+connector+parafrasis visibles en ambos',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: cualquier sospecha de texto IA / traido de casa (incl. "avance el audio 2 en casa") (notificar al cierre - Regla 3 Roadmap)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 14',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 3: Cl 13 arranco audio 1 / Cl 14 cerro audio 1 + abrio audio 2 / hoy cierro audio 2 + cierro el sub-bloque',
    'ESCRIBI Frase del Dia + B2 Set #8 + Protocolo + Plan Audio 2/Cierre sub-bloque + Registro Escrito en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 15 = JUSTICIA dia 5 (ultimo del bloque - por numero de clase)',
    'Hile JUSTICIA en VATS + Frase del Dia (justicia con su propia voz - fidelidad al TODO del ingles de Fase 2)',
    'Mantuve las 6 capas visibles como SUSTRATO del texto (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-14)',
    'Presente 6 palabras B2 Set #8 con pronunciacion + ejemplo ESCRIBIBLE (total 48)',
    'Recorde el PROTOCOLO de transcripcion a mano (5 pasos) y donde esta cada audio hoy, con modelado en vivo',
    'Aplique el bridge formal->casual al REGISTRO DE ESCRITURA (no al habla)',
    'Conduje la ESCRITURA MANUSCRITA EN CLASE como centro (45 min, a mano, sin dispositivos): cerrar AUDIO 2 (Steps 3->4->5) + CIERRE del sub-bloque (audio 1 final + audio 2 final juntos)',
    'APLIQUE LA REGLA ANTI-FRAUDE: a mano + en clase; audio Fase 2 solo se escucha/recuerda; texto de casa (incl. "avance audio 2 en casa") NO cuenta y se reescribe aqui',
    'Circule en silencio y registre NOTAS DE TRANSICION habla->texto por estudiante (INTERNO) sin comunicar nota ni juicio',
    'Conduje la LECTURA EN VOZ ALTA del propio texto (audio 2 final) como control de calidad (oral = soporte, NO Speak About)',
    'Camine con papel errores anonimo (errores de ESCRITURA: concordancia, mayuscula, muletilla escrita, preposicion, B2 Set #8)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'RECOGI las 5 hojas manuscritas (AUDIO 1 final + AUDIO 2 final = sub-bloque de transcripcion CERRADO)',
    'En Tarea explique el por que (31 dias hasta Final) + due date explicito (lunes 25/05 antes de 6:00 PM) + aclare que la escritura evaluable es EN CLASE',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes o sospecha de texto IA/de casa',
    'Anuncie Cl 16 = Fase 3 dia 4 (estructura final del monologo: hook + 3 puntos + cierre, a partir de los 2 textos cerrados)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase15_REPORTE.pdf'),
    'B2 PM AMINA | Cl 15 de 36 | FASE 3 DIA 3/8 — ESCRITURA (anti-fraude) — CIERRA SUB-BLOQUE TRANSCRIPCION | DEL HABLA AL TEXTO + B2 SET #8 | FRASE DEL DIA (Goldlist retirado)',
    'FASE 3 DIA 3/8: Fase 2 (oral) cerro Cl 12 -> Fase 3 (del habla al texto) arranco Cl 13 (audio 1) -> Cl 14 cerro audio 1 + abrio audio 2 -> hoy Cl 15 CIERRA el sub-bloque. Centro = ESCRITURA MANUSCRITA EN CLASE: terminar/limpiar el AUDIO 2 iniciado ayer (Steps 3->4->5 = texto B2 final) + CIERRE del sub-bloque de transcripcion (audio 1 final + audio 2 final juntos = semilla del guion del Final), ambos de audios de Fase 2 (anti-fraude IA: a mano, en clase, sin dispositivos; audio solo se escucha/recuerda; texto de casa - incl. "avance audio 2 en casa" - NO cuenta) + Academic B2 Set #8 (culminate/paramount/attest/divergent/foreground/cohesion -> total 48, registro escrito) + las 6 capas como sustrato del texto + lectura en voz alta del propio texto como control de calidad + ~42h/~31 dias al Final + FRASE DEL DIA. Estructura Fase 3 segun ROADMAP 72h (Cl 13-20; Cl 13-15 transcripcion 2 audios). CHECKPOINTS Roadmap: C2 = FIN CL 12 (NO en Cl 15); siguiente entregable de coordinacion = C3 fin Cl 20 (guion escrito) -> Cl 15 NO tiene entregable de checkpoint; las hojas manuscritas se archivan como evidencia anti-fraude que alimenta C3. Salto habla->texto evaluado INTERNO, NO se comunica nota.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase15_REPORTE.pdf')

print('\n2 PDFs generados para viernes 22/05 B2 PM Amina Cl 15:')
print('  - B2/B2_PM_Amina_Clase15_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase15_REPORTE.pdf')
