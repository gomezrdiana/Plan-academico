#!/usr/bin/env python3
"""Genera la guia + reporte del B2 PM Amina Cl 14 (jueves 21/05/2026):
- FASE 3 DIA 2/8 - CONTINUA: DEL HABLA AL TEXTO. Centro = ESCRITURA MANUSCRITA
  EN CLASE: terminar/limpiar el AUDIO 1 (Steps 3->4->5) + empezar el AUDIO 2
  (Steps 1->2->3), ambos audios de Fase 2 a texto B2 limpio (anti-fraude IA:
  a mano, en clase, sin dispositivos; texto de casa - incl. "avance audio 1
  en casa" - NO cuenta).
- Academic B2 Vocab Set #7 (6 nuevas -> total 42) + Frase del Dia + virtud JUSTICIA dia 4
- 44 horas / 32 dias hasta el Final (~22 junio) — derivado de Cl 13 (46h/33d) -1 dia -2h clase
  (verificado: 22/06/2026 - 21/05/2026 = 32 dias)
- Estructura Fase 3 segun ROADMAP 72h (autoritativo, reemplaza version 90h):
  Fase 3 = Cl 13-20; Cl 13-15 = transcribir a mano 2 audios de Fase 2
  (Cl 13 = audio 1 arranque; Cl 14 = cerrar audio 1 + abrir audio 2; Cl 15 = cerrar audio 2).
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase14_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase14_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase14_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 13)', '5 min'),
    ('EL POR QUE DE HOY (dia 2 de Fase 3)', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (JUSTICIA dia 4)', '5 min'),
    ('RECAP EXPRESS - las 6 capas como sustrato del texto', '5 min'),
    ('ACADEMIC B2 VOCAB SET #7 (6 palabras nuevas - total 42)', '8 min'),
    ('PLAN DE HOY: cerrar AUDIO 1 + abrir AUDIO 2 + REGISTRO ESCRITO formal->casual', '12 min'),
    ('PEER TEACHER SLOT corto (error Cl 13)', '3 min'),
    ('ESCRITURA MANUSCRITA EN CLASE (anti-fraude): terminar AUDIO 1 + empezar AUDIO 2 - centro de hoy', '45 min'),
    ('LECTURA EN VOZ ALTA del propio texto + ajuste', '12 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE (errores de escritura)', '5 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 13',
    'Foto del tablero - Frase del Dia + B2 Set #7 + Plan de hoy (Audio 1/Audio 2)',
    'LAS 5 HOJAS MANUSCRITAS recogidas: AUDIO 1 final + AUDIO 2 iniciado (artefacto escrito en clase - anti-fraude; archivar, alimenta Checkpoint C3 fin Cl 20)',
    'NOTAS DE TRANSICION habla->texto POR ESTUDIANTE (interno - NO se comunica nota): cierra audio 1 o se atasca / audio 2 fluye o se bloquea / muletillas en la pagina / sigue siendo SU ingles vs sospecha IA / B2 Set #7 escrito / anchor+connector+parafrasis visibles',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: cualquier sospecha de texto IA / traido de casa (incl. "avance el audio 1 en casa") (notificar al cierre - Regla 3 Roadmap)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 13',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 2: ayer Cl 13 arranco audio 1 / hoy cierro audio 1 + abro audio 2',
    'ESCRIBI Frase del Dia + B2 Set #7 + Protocolo + Plan Audio 1/Audio 2 + Registro Escrito en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 14 = JUSTICIA dia 4 (por numero de clase)',
    'Hile JUSTICIA en VATS + Frase del Dia (justicia con su propia voz - fidelidad al ingles de Fase 2)',
    'Mantuve las 6 capas visibles como SUSTRATO del texto (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-13)',
    'Presente 6 palabras B2 Set #7 con pronunciacion + ejemplo ESCRIBIBLE (total 42)',
    'Recorde el PROTOCOLO de transcripcion a mano (5 pasos) y donde esta cada audio hoy, con modelado en vivo',
    'Aplique el bridge formal->casual al REGISTRO DE ESCRITURA (no al habla)',
    'Conduje la ESCRITURA MANUSCRITA EN CLASE como centro (45 min, a mano, sin dispositivos): cerrar AUDIO 1 (Steps 3->4->5) + abrir AUDIO 2 (Steps 1->2->3)',
    'APLIQUE LA REGLA ANTI-FRAUDE: a mano + en clase; audio Fase 2 solo se escucha/recuerda; texto de casa (incl. "avance audio 1 en casa") NO cuenta y se reescribe aqui',
    'Circule en silencio y registre NOTAS DE TRANSICION habla->texto por estudiante (INTERNO) sin comunicar nota ni juicio',
    'Conduje la LECTURA EN VOZ ALTA del propio texto (audio 1 final) como control de calidad (oral = soporte, NO Speak About)',
    'Camine con papel errores anonimo (errores de ESCRITURA: concordancia, mayuscula, muletilla escrita, B2 Set #7)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'RECOGI las 5 hojas manuscritas (AUDIO 1 final + AUDIO 2 iniciado)',
    'En Tarea explique el por que (32 dias hasta Final) + due date explicito + aclare que la escritura evaluable es EN CLASE',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes o sospecha de texto IA/de casa',
    'Anuncie Cl 15 = Fase 3 dia 3 (terminar audio 2 + cerrar sub-bloque de transcripcion)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase14_REPORTE.pdf'),
    'B2 PM AMINA | Cl 14 de 36 | FASE 3 DIA 2/8 — ESCRITURA (anti-fraude) | DEL HABLA AL TEXTO + B2 SET #7 | FRASE DEL DIA (Goldlist retirado)',
    'FASE 3 DIA 2/8: Fase 2 (oral) cerro Cl 12 -> Fase 3 (del habla al texto) arranco Cl 13 (audio 1) -> hoy Cl 14 continua. Centro = ESCRITURA MANUSCRITA EN CLASE: terminar/limpiar el AUDIO 1 iniciado ayer (Steps 3->4->5 = texto B2 final) + empezar el AUDIO 2 (Steps 1->2->3), ambos de audios de Fase 2 (anti-fraude IA: a mano, en clase, sin dispositivos; audio solo se escucha/recuerda; texto de casa - incl. "avance audio 1 en casa" - NO cuenta) + Academic B2 Set #7 (compelling/underscore/intricate/convey/emphatic/elaborate -> total 42, registro escrito) + las 6 capas como sustrato del texto + lectura en voz alta del propio texto como control de calidad + 44h/32 dias al Final + FRASE DEL DIA. Estructura Fase 3 segun ROADMAP 72h (Cl 13-20; Cl 13-15 transcripcion 2 audios). Salto habla->texto evaluado INTERNO, NO se comunica nota.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase14_REPORTE.pdf')

print('\n2 PDFs generados para jueves 21/05 B2 PM Amina Cl 14:')
print('  - B2/B2_PM_Amina_Clase14_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase14_REPORTE.pdf')
