#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 13 (miercoles 20/05/2026):
- FASE 3 DIA 1/8 - ARRANQUE: DEL HABLA AL TEXTO. Centro = TRANSCRIPCION MANUSCRITA
  EN CLASE de un audio de Fase 2 a texto B2 limpio (anti-fraude IA: a mano, en clase,
  sin dispositivos; texto de casa NO cuenta).
- Academic B2 Vocab Set #6 (6 nuevas -> total 36) + Frase del Dia + virtud JUSTICIA dia 3
- 46 horas / 33 dias hasta el Final (~22 junio) — derivado de Cl 12 (48h/34d) -1 dia -2h clase
  (verificado: 22/06/2026 - 20/05/2026 = 33 dias)
- Estructura Fase 3 segun ROADMAP 72h (autoritativo, reemplaza version 90h):
  Fase 3 = Cl 13-20; Cl 13-15 = transcribir a mano 2 audios de Fase 2.
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase13_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase13_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase13_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 12)', '5 min'),
    ('EL POR QUE DE HOY (transicion a Fase 3)', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (JUSTICIA dia 3)', '5 min'),
    ('RECAP EXPRESS - las 6 capas ahora como sustrato del texto', '5 min'),
    ('ACADEMIC B2 VOCAB SET #6 (6 palabras nuevas - total 36)', '8 min'),
    ('PROTOCOLO TRANSCRIPCION A MANO + REGISTRO ESCRITO formal->casual', '12 min'),
    ('PEER TEACHER SLOT corto (error Cl 12)', '3 min'),
    ('TRANSCRIPCION MANUSCRITA EN CLASE (anti-fraude) - centro de hoy', '45 min'),
    ('LECTURA EN VOZ ALTA del propio texto + ajuste', '12 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE (errores de escritura)', '5 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 12',
    'Foto del tablero - Frase del Dia + B2 Set #6 + Protocolo Transcripcion',
    'LAS 5 HOJAS MANUSCRITAS de transcripcion recogidas (artefacto escrito en clase - anti-fraude; archivar, alimenta Checkpoint C3 fin Cl 20)',
    'NOTAS DE TRANSICION habla->texto POR ESTUDIANTE (interno - NO se comunica nota): vuelca habla a texto o se bloquea / muletillas en la pagina / sigue siendo SU ingles vs sospecha IA / B2 Set #6 escrito / anchor+connector+parafrasis visibles',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: cualquier sospecha de texto IA / traido de casa (notificar al cierre - Regla 3 Roadmap)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 12',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE LA TRANSICION: Fase 2 cerro ayer (oral) / Fase 3 arranca hoy (texto)',
    'ESCRIBI Frase del Dia + B2 Set #6 + Protocolo Transcripcion + Registro Escrito en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 13 = JUSTICIA dia 3 (por numero de clase)',
    'Hile JUSTICIA en VATS + Frase del Dia (justicia con su propia voz - anti-fraude)',
    'Mantuve las 6 capas visibles como SUSTRATO del texto (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-12)',
    'Presente 6 palabras B2 Set #6 con pronunciacion + ejemplo ESCRIBIBLE (total 36)',
    'Enseñe el PROTOCOLO de transcripcion a mano (5 pasos) con modelado en vivo',
    'Aplique el bridge formal->casual al REGISTRO DE ESCRITURA (no al habla)',
    'Conduje la TRANSCRIPCION MANUSCRITA EN CLASE como centro (45 min, a mano, sin dispositivos)',
    'APLIQUE LA REGLA ANTI-FRAUDE: a mano + en clase; audio Fase 2 solo se escucha/recuerda; texto de casa NO cuenta y se reescribe aqui',
    'Circule en silencio y registre NOTAS DE TRANSICION habla->texto por estudiante (INTERNO) sin comunicar nota ni juicio',
    'Conduje la LECTURA EN VOZ ALTA del propio texto como control de calidad (oral = soporte, NO Speak About)',
    'Camine con papel errores anonimo (errores de ESCRITURA: concordancia, mayuscula, muletilla escrita)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'RECOGI las 5 hojas manuscritas (artefacto escrito en clase)',
    'En Tarea explique el por que (33 dias hasta Final) + due date explicito + aclare que la escritura evaluable es EN CLASE',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes o sospecha de texto IA/de casa',
    'Anuncie Cl 14 = Fase 3 dia 2 (transcribir 2do audio + refinar)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase13_REPORTE.pdf'),
    'B2 PM AMINA | Cl 13 de 36 | FASE 3 DIA 1 — ESCRITURA (anti-fraude) | DEL HABLA AL TEXTO + B2 SET #6 | FRASE DEL DIA (Goldlist retirado)',
    'TRANSICION DE FASE: Fase 2 (oral) cerro Cl 12 -> Fase 3 (del habla al texto) arranca hoy. Centro = TRANSCRIPCION MANUSCRITA EN CLASE de un audio de Fase 2 a texto B2 limpio siguiendo protocolo de 5 pasos (anti-fraude IA: a mano, en clase, sin dispositivos; audio solo se escucha/recuerda; texto de casa NO cuenta) + Academic B2 Set #6 (articulate/underpin/resonate/succinct/coherent/render -> total 36, registro escrito) + las 6 capas como sustrato del texto + lectura en voz alta del propio texto como control de calidad + 46h/33 dias al Final + FRASE DEL DIA. Estructura Fase 3 segun ROADMAP 72h (Cl 13-20; Cl 13-15 transcripcion). Salto habla->texto evaluado INTERNO, NO se comunica nota.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase13_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 20/05 B2 PM Amina Cl 13:')
print('  - B2/B2_PM_Amina_Clase13_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase13_REPORTE.pdf')
