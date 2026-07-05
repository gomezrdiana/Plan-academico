#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 22 (martes 02/06/2026):
- FASE 4 DIA 2/8 = chunk PILLAR 1 (~1 min). Mismo metodo que Cl 21
  (HOOK): memorizacion silenciosa + ensayo individual sin papel +
  ensayo en parejas sin papel + mini-audiencia sin papel. 30 seg de
  refresh silencioso del HOOK al inicio del bloque chunk
  (encadenamiento MENTAL, NO en voz alta - el encadenamiento real
  abre Cl 25).
- REGLA FIRME: texto del PILLAR 1 esta CERRADO desde C3 entregado
  Cl 20 (29/05). Hoy NO se edita una sola palabra. Hoy se MEMORIZA
  y se DICE SIN PAPEL. Si la estudiante quiere cambiar algo, va al
  margen como observacion, no se reescribe el texto. Profesora NO
  comunica nota, NO comunica resultado C3.
- Academic B2 Vocab Set #15 (6 nuevas: assert/substantiate/illustrate/
  exemplify/underpin/anchor -> total 90). Verbos de argumentacion
  alineados a PILLARS - se introducen como vocabulario "vive en
  pillars desde hoy" pero NO se inyectan en el PILLAR 1 ya escrito.
- Virtud PRUDENCIA dia 2 (Cl 21-25 PRUDENCIA v2 - SUPUESTO: inicio
  ciclo 2 de las 4 cardinales tras cierre FORTALEZA v1 Cl 16-20;
  verificar con coordinacion).
- ~28 horas / ~20 dias hasta el Final (~22 junio) - derivado de Cl 20
  (~32h/~24d) -4h (2 clases x 2h = Cl 21+22) y +4 dias calendario
  (vie 29/05 -> mar 02/06) (verificado: 22/06/2026 - 02/06/2026 =
  20 dias; 32h - 4h = 28h).
- Estructura Fase 4 segun ROADMAP 72h lineas 120-129: Cl 21-28 (16h)
  = practica en CHUNKS de 1 min. Cl 21-24 = 1-2 chunks por sesion,
  de memoria. Cl 25-28 = encadenar 2->3->4->5 chunks. C4 fin Cl 28 =
  video 3 min de memoria. Asignacion HOOK(Cl21)/PILLAR1(Cl22)/
  PILLAR2(Cl23)/PILLAR3(Cl24) es del profesorado Heiiu (orden
  arquitectonico natural); el Roadmap dice "1-2 chunks por sesion"
  pero no nombra cual chunk en que dia.
- TAREA STRICT 4 componentes due miercoles 03/06 antes 6 PM:
  (1) HOOK + PILLAR 1 100% memoria (separados, no encadenados en
      voz alta - eso arranca Cl 25);
  (2) audio HOOK -> PILLAR 1 encadenado 3 veces - UNICA excepcion
      intencional a la regla "no encadenar en voz alta" como
      diagnostico en casa (NO performance) para oir el handoff
      antes de Cl 25; si coordinacion prefiere mantener estricta
      la regla, reemplazar por "audio PILLAR 1 SOLO 3 tomas";
  (3) escuchar + 2 mejoras a mano sobre el handoff (NO reescribir
      texto);
  (4) repaso 90 vocab acumulados.
- Anuncio Cl 23 miercoles 03/06 = chunk PILLAR 2 (Fase 4 dia 3/8).
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase22_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase22_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase22_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 21: HOOK 100% memoria + audio + 2 mejoras + vocab 84)', '5 min'),
    ('EL POR QUE DE HOY (Fase 4 dia 2/8 - chunk PILLAR 1)', '4 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (PRUDENCIA dia 2 - Cl 21-25 PRUDENCIA v2 supuesto)', '5 min'),
    ('RECAP EXPRESS - arquitectura completa visible (HOOK + 3 PILLARS + CTA, PILLAR 1 rotulado hoy) + 6 capas como sustrato de P1', '5 min'),
    ('ACADEMIC B2 VOCAB SET #15 (6 verbos de argumentacion: assert/substantiate/illustrate/exemplify/underpin/anchor - total 90)', '7 min'),
    ('PLAN DE HOY: chunk PILLAR 1 + 4 pasos + REGLA NO PAPEL + REGLA TEXTO CERRADO desde C3 + REGLA NO ENCADENAR EN VOZ ALTA', '5 min'),
    ('PEER TEACHER SLOT corto (error oral Cl 21)', '3 min'),
    ('PILLAR 1 CHUNK - CENTRO DE HOY (45 min: 30 seg refresh silencioso HOOK + 4 pasos: memo silenciosa / individual sin papel / parejas sin papel feedback connector+vocab / mini-audiencia sin papel Q&A contenido)', '45 min'),
    ('FRASE DEL DIA cierre + Paraphrase check + auto-observacion 1 frase (NO nota)', '5 min'),
    ('ERROR PAPER LIVE (errores DEL PILLAR 1 sin papel: arranque dudoso / vocab B2 mal pronunciado bajo memoria / restart desde principio en vez de ultimo topic chunk / encadenamiento involuntario con cierre HOOK)', '7 min'),
    ('Auto-observacion + CIERRE Fase 4 dia 2/8 + ANUNCIO Cl 23 = chunk PILLAR 2 + TAREA STRICT 4 componentes due miercoles 6 PM', '12 min'),
    ('Buffer + cierre limpio (repasar pronunciacion debil del Set #15 / mirar tablero arquitectura HOOK ✓ P1 ✓ P2 manana)', '7 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 21',
    'Foto del tablero - Frase del Dia + B2 Set #15 + Arquitectura completa (PILLAR 1 rotulado hoy) + 4 pasos del chunk + Reglas (no editar texto cerrado / no encadenar en voz alta / no papel pasos 2-3-4)',
    'NOTAS DE LIBRETA PERSONAL POR ESTUDIANTE (interno - observacion de memoria, NO se comunica nota): por las 5 estudiantes, donde se cayo cada quien en el PILLAR 1 / que topic chunk se pierde / que connector se olvida / que B2 word se traba / tiempo real de cada pasada de mini-audiencia / si hubo restart desde ultimo topic chunk o desde primera palabra',
    'CHECKLIST especifico chunk PILLAR 1 hoy: refresh 30 seg silencio hecho / 4 pasos completados por las 5 estudiantes (memo silenciosa, individual sin papel, parejas sin papel, mini-audiencia sin papel) / vocab Set #15 introducido / NO se permitio edicion de texto / NO se permitio encadenamiento HOOK + PILLAR 1 en voz alta en clase',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante (hoy errores DEL PILLAR 1 sin papel)',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: si alguien NO completo las 4 pasadas del PILLAR 1 (falto / no logro soltar papel / se quedo bloqueada en mini-audiencia) - notificar al cierre',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 21',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 2/8 DE FASE 4 + chunk PILLAR 1: Cl 21 puso HOOK en voz / hoy ponemos PILLAR 1 en voz / manana PILLAR 2 / Cl 25-28 encadenamos',
    'ESCRIBI Frase del Dia + B2 Set #15 + Arquitectura completa (PILLAR 1 rotulado HOY) + 4 pasos del chunk + Reglas (no editar / no encadenar en voz alta / no papel pasos 2-3-4) en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 22 = PRUDENCIA dia 2 (Cl 21-25 PRUDENCIA v2 - SUPUESTO ciclo 2 cardinales, marque verificar con coordinacion)',
    'Hile PRUDENCIA en VATS + Frase del Dia (rehearse the connection, not just the line - atencion al handoff HOOK -> PILLAR 1 sin convertirlo en encadenamiento prematuro)',
    'Mantuve las 6 capas visibles como SUSTRATO del PILLAR 1 (topic chunks, connector forward, paraphrase, intonation, repetition, anchors bajos)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-21)',
    'Presente 6 palabras B2 Set #15 con pronunciacion + ejemplo orientado a PILLARS (total 90) - aclare que NO se inyectan en el texto cerrado de PILLAR 1, solo como vocabulario activo desde hoy',
    'Mostre la ARQUITECTURA COMPLETA en tablero (HOOK ✓ Cl 21 / PILLAR 1 ← HOY / PILLAR 2 manana / PILLAR 3 / CTA) como anclaje visual del chunk de hoy',
    'Explique las 4 PASADAS del chunk + el refresh de 30 seg silencioso + las 2 REGLAS (texto cerrado desde C3 / no encadenar en voz alta hoy)',
    'CONDUJE los 45 min del chunk PILLAR 1: refresh 30 seg silencio + Paso 1 memo silenciosa con guion (~10 min) + Paso 2 individual sin papel (~10 min) + Paso 3 parejas sin papel con feedback connector + 1 B2 word (~12 min) + Paso 4 mini-audiencia sin papel con Q&A contenido (~12 min)',
    'NO PERMITI edicion del texto del PILLAR 1 (cerrado desde C3)',
    'NO PERMITI encadenamiento HOOK + PILLAR 1 en voz alta hoy (el encadenamiento real abre Cl 25)',
    'En pasos 2/3/4 verifique que el papel estuviera GIRADO / EN BOLSILLO / ABAJO',
    'Enseñe la regla del RESTART desde ULTIMO TOPIC CHUNK recordado (NO desde la primera palabra) cuando alguien se cae',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (donde se cayo cada quien en P1 / que connector se olvido / que B2 word se trabo)',
    'Conduje la auto-observacion de 1 frase por estudiante (memoria mas fuerte en ___ / mas debil en ___) como PROCESO, NO como comunicacion de evaluacion',
    'Camine con papel errores anonimo (errores DEL PILLAR 1 sin papel: arranque dudoso / vocab B2 mal pronunciado / restart mal hecho / encadenamiento involuntario)',
    'ANUNCIE Cl 23 miercoles 03/06 = chunk PILLAR 2 (mismo metodo, mismo refresh, mismas 4 pasadas)',
    'En Tarea explique el por que (4 componentes: HOOK + P1 memoria separados, audio HOOK -> P1 encadenado 3 veces como UNICA excepcion diagnostica en casa, escuchar + 2 mejoras a mano sobre handoff, repaso 90 vocab) + due date explicito (miercoles 03/06 antes de 6:00 PM) + NADA de reescribir guion',
    'Aclare que el audio encadenado HOOK -> PILLAR 1 en casa es DIAGNOSTICO (oir el handoff propio), NO performance, y NO autoriza encadenamiento en voz alta en clase hasta Cl 25',
    'NO acepte la excusa "no me da tiempo"',
    'NO comunique nota ni resultado de C3 (regla permanente)',
    'Notifique a coordinacion al cierre si hay 2 strikes / sospecha IA residual / inasistencia hoy / chunk PILLAR 1 no completado por alguna estudiante',
    'Marque SUPUESTOS abiertos a verificar con coordinacion: (1) PRUDENCIA v2 como inicio ciclo 2 cardinales / (2) asignacion HOOK-P1-P2-P3 a Cl 21-24 / (3) audio encadenado en tarea como excepcion diagnostica',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase22_REPORTE.pdf'),
    'B2 PM AMINA | Cl 22 de 36 | FASE 4 DIA 2/8 - chunk PILLAR 1 (~1 min) sin papel | PRUDENCIA dia 2 | FRASE DEL DIA (Goldlist retirado)',
    'FASE 4 DIA 2/8 - chunk PILLAR 1 (~1 min). Cl 21 ayer puso HOOK en voz sin papel (4 pasos). Hoy mismo metodo con PILLAR 1: 30 seg refresh silencioso (encadenamiento MENTAL HOOK -> P1, NO en voz alta - el encadenamiento real abre Cl 25) + 4 pasadas (memorizacion silenciosa con guion / individual sin papel / parejas sin papel con feedback connector + 1 B2 word / mini-audiencia sin papel con Q&A de contenido). REGLA FIRME: texto del PILLAR 1 esta CERRADO desde C3 entregado Cl 20 - hoy NO se edita una sola palabra, solo se MEMORIZA y se DICE SIN PAPEL. Set #15 (assert/substantiate/illustrate/exemplify/underpin/anchor -> 90) son verbos de argumentacion que viven en pillars - se introducen como vocabulario activo desde hoy pero NO se inyectan en el texto cerrado de PILLAR 1. Restart desde ULTIMO TOPIC CHUNK recordado (NO desde primera palabra) cuando alguien se cae. Cl 22 = PRUDENCIA dia 2 (Cl 21-25 PRUDENCIA v2 - SUPUESTO ciclo 2 cardinales, verificar). ~28h/~20 dias al Final. Tarea STRICT 4 componentes (HOOK + P1 memoria separados / audio HOOK -> P1 encadenado 3 veces como UNICA excepcion diagnostica en casa / escuchar + 2 mejoras a mano sobre handoff / repaso 90 vocab) due miercoles 03/06 antes 6 PM. Anuncio Cl 23 miercoles = chunk PILLAR 2. Profesora NO comunica nota, NO autoriza edicion del texto cerrado, NO autoriza encadenamiento en voz alta en clase hasta Cl 25.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase22_REPORTE.pdf')

print('\n2 PDFs generados para martes 02/06 B2 PM Amina Cl 22:')
print('  - B2/B2_PM_Amina_Clase22_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase22_REPORTE.pdf')
