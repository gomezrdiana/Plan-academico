#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 21 (lunes 01/06/2026):
- FASE 4 DIA 1/8 - ABRE FASE 4 - PRACTICA EN CHUNKS - HOOK CHUNK 1 MIN
  SIN PAPEL. Primera clase del nuevo arco: el manuscrito C3 entregado
  viernes queda en archivo coordinacion, no vuelve al aula. La voz se
  separa del papel por primera vez.
- Centro = PRACTICA HOOK SIN PAPEL en 3 etapas (45 min):
    Stage 1 individual silencioso (12 min) - 1 min refresh papel
      opcional al inicio, luego cerrado y guardado.
    Stage 2 parejas (15 min) - uno habla sin papel, otro coachea sin
      papel; rotacion para entrenar oido a HOOKs ajenos.
    Stage 3 mini-audiencia (15 min) - 5 estudiantes x ~3 min, una a
      la vez DE PIE frente al grupo, ZERO papel en ninguna mano.
- Amina corrige SOLO FORMA (acento / ritmo / pausa / transicion /
  muletilla) en vivo - NO contenido (cerrado Cl 19), NO arquitectura
  (cerrada Fase 3), NO C3 (coordinacion decide).
- Transicion virtud VISIBLE en tablero y en VATS: FORTALEZA v1
  (Cl 16-20, cerrada viernes) -> PRUDENCIA v2 (Cl 21-25, abre HOY)
  - regla cohorte B2 rotacion estandar 5 clases/bloque, Diana 22/05.
  Ciclo 2 de las 4 cardinales reinicia con PRUDENCIA porque ciclo 1
  cerro Cl 1-20 (P-T-J-F).
- Academic B2 Vocab Set #14 (6 nuevas: rehearsal / refrain /
  intonation / cadence / emphasis / pivot -> total 84). Set #14 son
  VERBOS DE PRACTICA Y REFINAMIENTO del HOOK - se usan para HABLAR
  SOBRE el ensayo, no para AGREGAR al HOOK (cerrado).
- Tarea STRICT 4 componentes due martes 02/06 antes 6 PM:
    (1) Memorizar HOOK 100% (15-20 min) - sentido por sentido, no
        palabra por palabra
    (2) Grabar HOOK 3 veces (10 min) etiquetado
        B2-AMINA-CL21-HOOK-V1/V2/V3
    (3) Escuchar 3 grabaciones + 2 mejoras a mano (10-15 min) -
        solo forma, trae la hoja a Cl 22
    (4) Repaso vocab acumulado 84 palabras (5-10 min) - marca las
        12 que mas se cruzan
- ~30 horas / ~21 dias al Final - derivado de Cl 20 (~32h/~24d)
  +3 dias calendario (vie 29 -> lun 01) -2h bloque Cl 21
  (verificado: 22/06/2026 - 01/06/2026 = 21 dias; 32h - 2h = 30h).
- Estructura Fase 4 segun ROADMAP 72h lineas 120-129: Cl 21-24
  1-2 chunks/sesion de memoria / Cl 25-28 encadenar 2->5 chunks /
  C4 fin Cl 28 = video 3 min de memoria. La secuencia Cl 21 HOOK ->
  Cl 22 PILLAR 1 -> Cl 23 PILLAR 2 -> Cl 24 PILLAR 3 + CTA es
  formato Heiiu interno que CONCRETA "1-2 chunks por sesion" del
  Roadmap, NO inventa criterios.
- ANTI-FRAUDE estructural: el papel NO entra al aula. Sin papel =
  imposible leer = obligado a memoria honesta. Mirada de
  verificacion silenciosa 2 min al final - despues de la practica -
  para que la estudiante descubra su propio gap.
- Anuncio Cl 22 = Fase 4 dia 2 = PILLAR 1 chunk (1 min memorizable,
  mismo formato).
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase21_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase21_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase21_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea fin de semana ligera)', '5 min'),
    ('EL POR QUE DE HOY (Fase 4 dia 1/8 - ABRE FASE 4 - HOOK chunk sin papel)', '4 min'),
    ('FRASE DEL DIA - presentacion ("Plan the chunk - then own it without the paper")', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos, no Cl 6-20)', '6 min'),
    ('VATS (PRUDENCIA dia 1 - ABRE bloque nuevo - TRANSICION VISIBLE desde FORTALEZA v1 cerrada viernes)', '5 min'),
    ('RECAP EXPRESS - arquitectura completa (HOOK marcado CHUNK 1 HOY + 3 PILLARS + CTA) + 6 capas como sustrato sostenido SIN papel', '5 min'),
    ('ACADEMIC B2 VOCAB SET #14 (6 palabras nuevas: rehearsal/refrain/intonation/cadence/emphasis/pivot - verbos practica/refinamiento - total 84)', '7 min'),
    ('PLAN DE HOY: HOOK CHUNK SIN PAPEL + REGLAS FASE 4 (papel NO entra al aula) + LECTURA OPCIONAL 1 MIN REFRESCO inicio', '5 min'),
    ('PEER TEACHER SLOT corto (error oral observado Cl 20: muletilla bajo presion checkpoint / transicion fria HOOK-PILLAR / pronunciacion vocab caida en 5-7 min)', '3 min'),
    ('PRACTICA HOOK SIN PAPEL - CENTRO DE HOY (3 etapas: Stage 1 INDIVIDUAL silencioso 12 min con 1 min refresh opcional / Stage 2 PAREJAS 15 min uno habla otro coachea / Stage 3 MINI-AUDIENCIA 15 min 5 estudiantes x ~3 min DE PIE zero papel)', '45 min'),
    ('FRASE DEL DIA cierre + Paraphrase check + auto-observacion memoria (que se sintio distinto sin papel vs con papel)', '5 min'),
    ('ERROR PAPER LIVE (errores DE ORAL SIN PAPEL: muletillas que volvieron / pausa rellenada con sonido / habla acelerada por miedo a olvidar / vaguedad sin ancla del texto)', '5 min'),
    ('MIRADA DE VERIFICACION SILENCIOSA (2 min papel - SOLO al final, despues de la practica) + CIERRE FASE 4 dia 1 + TAREA STRICT 4 componentes (memorizar HOOK + 3 grabaciones + 2 mejoras + repaso 84 vocab, due martes 6PM) + ANUNCIO Cl 22 = PILLAR 1 chunk', '10 min'),
    ('AUTO-EVALUACION INTERNA profesora (libreta, NO se comunica) + RECOGIDA + transicion a Cl 22 (sin comunicar nota, sin comunicar C3)', '11 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas fin de semana',
    'Foto del tablero - Frase del Dia + B2 Set #14 + Arquitectura completa con HOOK marcado CHUNK 1 HOY + TRANSICION VIRTUD FORTALEZA v1 cerrada -> PRUDENCIA v2 abre + Reglas Fase 4 dia 1',
    'HOJA DE OBSERVACION FASE 4 DIA 1 POR ESTUDIANTE (interno - alimenta Cl 22-28, NO se comunica): por las 5 estudiantes, sin calificacion, solo observacion cruda de FORMA (voz sin papel / memoria del HOOK / arquitectura preservada / intonacion / cadencia / emphasis / muletillas vueltas al quitar papel / pronunciacion B2 / comportamiento manos / reaccion a memoria blank - breathed+pivoted vs froze vs pidio papel / pieza corregida / listo para PILLAR 1 manana)',
    'CHECKLIST especifico Fase 4 dia 1 hoy: 5 HOOKs dichos sin papel en mini-audiencia / 3 etapas completadas (individual / parejas / mini-audiencia) / papel NO entro al aula (guiones en mochila) / lectura de refresco 1 min al inicio (opcional, no obligatorio) / mirada de verificacion silenciosa 2 min al final / hoja observacion llena por las 5',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante (hoy errores DE ORAL SIN PAPEL: pronunciacion / ritmo / pausa / transicion / muletilla que vuelve cuando se cae el ancla del texto)',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: si alguien NO logro HOOK por memoria (se congelo / pidio papel a mitad / no termino la ronda mini-audiencia) - notificar al cierre para coordinar ajuste antes de Cl 22',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas fin de semana',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE QUE ABRE FASE 4: el manuscrito C3 entregado viernes queda en archivo coordinacion, NO vuelve al aula; la voz se separa del papel por primera vez; 8 sesiones (Cl 21-28) de chunks; hoy = HOOK chunk (chunk 1 del monologo)',
    'ESCRIBI Frase del Dia + B2 Set #14 + Arquitectura completa con HOOK marcado CHUNK 1 HOY + TRANSICION VIRTUD (FORTALEZA v1 cerrada -> PRUDENCIA v2 abre) + Reglas Fase 4 dia 1 + Anuncio Cl 22 PILLAR 1 en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 21 = PRUDENCIA dia 1 (PRIMER dia bloque nuevo - rotacion estandar cohorte B2, regla confirmada Diana 22/05) + MENCIONE VISIBLEMENTE la transicion desde FORTALEZA v1 cerrada (no callada)',
    'Hile PRUDENCIA en VATS + Frase del Dia (prudencia = confiar lo que ya sabes sin red, el acto de no buscar papel que no esta) + bridge desde fortitude del viernes (coraje de poner en el record) a prudence de hoy (sabiduria de confiar la voz sin papel)',
    'Mantuve las 6 capas visibles como SUSTRATO sostenido SIN papel (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing) - hoy se probo si sobreviven sin el ancla del texto',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-20)',
    'Presente 6 palabras B2 Set #14 con pronunciacion + ejemplo orientado a HABLAR SOBRE el ensayo (rehearsal/refrain/intonation/cadence/emphasis/pivot - total 84) - aclare que Set #14 es para HABLAR SOBRE el HOOK, no para AGREGAR al HOOK (cerrado)',
    'Mostre la ARQUITECTURA COMPLETA en tablero con HOOK marcado CHUNK 1 HOY + secuencia chunks Cl 22-24 + encadenamiento Cl 25-28',
    'Explique las REGLAS FASE 4 dia 1 (papel NO entra al aula / guiones en mochila / lectura refresco 1 min OPCIONAL al inicio / mirada de verificacion 2 min al final / si memoria blank = breathe + pivot + rebuild forward, NO freeze, NO papel) + la REGLA C3 (no comunico resultado, coordinacion decide en su clock)',
    'CONDUJE 3 ETAPAS COMPLETAS (Stage 1 INDIVIDUAL silencioso 12 min con refresh opcional / Stage 2 PAREJAS 15 min uno habla otro coachea rotando / Stage 3 MINI-AUDIENCIA 15 min 5 estudiantes x ~3 min DE PIE zero papel ninguno)',
    'CORREGI SOLO FORMA en vivo (acento / ritmo / pausa / transicion / muletilla) - NO contenido (cerrado), NO arquitectura (cerrada), NO C3 (coordinacion)',
    'Interrumpi a parejas que se desviaron a contenido ("Content is closed - only form. What did you HEAR in her cadence?")',
    'GARANTICE que el papel NO entro al aula durante la practica (guiones en mochila) - solo refresh 1 min OPCIONAL al inicio y mirada de verificacion 2 min al final',
    'LLENE la hoja de observacion FASE 4 dia 1 por estudiante (interna, NO se comunica) - sin calificacion, solo observacion cruda de FORMA + reaccion a memoria blank + lista para PILLAR 1 manana',
    'Conduje la AUTO-OBSERVACION de cierre (cada quien dice que se sintio distinto sin papel vs con papel) como PROCESO, NO como comunicacion de evaluacion',
    'Camine con papel errores anonimo (errores SIN PAPEL: muletillas que volvieron al quitar ancla / pausa rellenada con sonido / habla acelerada por miedo a olvidar / vaguedad sin texto de respaldo)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (DE ORAL SIN PAPEL: pronunciacion / ritmo / pausa / transicion / muletilla)',
    'CONDUJE la mirada de verificacion silenciosa 2 min al final (despues de la practica, NO antes) - para que la estudiante descubra su propio gap sin que yo lo senale',
    'En Tarea explique el por que (consolidacion HOOK por memoria antes de Cl 22 PILLAR 1) + due date explicito (martes 02/06 antes de 6:00 PM) + 4 componentes claros + etiquetado exacto de grabaciones (B2-AMINA-CL21-HOOK-V1/V2/V3)',
    'NO acepte la excusa "no me da tiempo"',
    'NO comunique a las estudiantes calificacion del HOOK de hoy ("today was the lift - tomorrow PILLAR 1")',
    'NO comunique resultado C3 si alguien pregunto (respuesta: coordination clock, not mine; today we opened Phase 4)',
    'Notifique a coordinacion al cierre si hay 2 strikes / sospecha IA residual / inasistencia hoy / no logro HOOK por memoria',
    'Anuncie Cl 22 martes = FASE 4 DIA 2 = PILLAR 1 chunk (1 min memorizable, mismo formato, mismo papel-fuera)',
    'AUTO-EVAL INTERNA (libreta): cuantas lograron HOOK 100% sin glance / cuantas refresh-minute / cuantas memoria blank y como reaccionaron / muletillas vueltas / patron mas comun de error / riesgo para Cl 22 / hay alguna NO lista para PILLAR 1 manana',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase21_REPORTE.pdf'),
    'B2 PM AMINA | Cl 21 de 36 | FASE 4 DIA 1/8 — ABRE FASE 4 — HOOK CHUNK 1 MIN SIN PAPEL | TRANSICION VIRTUD FORTALEZA v1 cerrada -> PRUDENCIA v2 abre | FRASE DEL DIA (Goldlist retirado)',
    'FASE 4 DIA 1/8 - ABRE FASE 4 - PRACTICA EN CHUNKS - HOOK CHUNK 1 MIN SIN PAPEL. El manuscrito C3 entregado a coordinacion viernes queda en archivo, NO vuelve al aula. La voz se separa del papel por primera vez. Centro = PRACTICA HOOK SIN PAPEL en 3 etapas (45 min): Stage 1 INDIVIDUAL silencioso 12 min (1 min refresh papel opcional al inicio, luego cerrado y guardado en mochila); Stage 2 PAREJAS 15 min (uno habla sin papel, otro coachea sin papel, rotacion para entrenar oido a HOOKs ajenos); Stage 3 MINI-AUDIENCIA 15 min (5 estudiantes x ~3 min, una a la vez DE PIE frente al grupo, ZERO papel en NINGUNA mano). Amina corrige SOLO FORMA en vivo (acento / ritmo / pausa / transicion / muletilla) - NO contenido (cerrado Cl 19), NO arquitectura (cerrada Fase 3), NO C3 (coordinacion decide en su clock). Anti-fraude estructural: sin papel en el aula = imposible leer = obligado a memoria honesta. Mirada de verificacion silenciosa 2 min SOLO al final (despues de la practica) - estudiante descubre su propio gap. TRANSICION VIRTUD VISIBLE en tablero y VATS: FORTALEZA v1 (Cl 16-20, cerrada viernes) -> PRUDENCIA v2 dia 1 (Cl 21-25, abre HOY) - regla cohorte B2 rotacion estandar, Diana 22/05; ciclo 2 de las 4 cardinales reinicia con PRUDENCIA. Academic B2 Set #14 (rehearsal/refrain/intonation/cadence/emphasis/pivot -> total 84) = verbos de PRACTICA Y REFINAMIENTO del HOOK; se usan para HABLAR SOBRE el ensayo, NO para AGREGAR al HOOK (cerrado). Tarea STRICT 4 componentes due martes 02/06 antes 6 PM: memorizar HOOK 100% (sentido por sentido, no palabra por palabra) + 3 grabaciones etiquetadas B2-AMINA-CL21-HOOK-V1/V2/V3 + escucha 3 grabaciones + 2 mejoras de FORMA a mano (trae hoja a Cl 22) + repaso 84 vocab (marca las 12 que mas cruzan). ~30h/~21 dias al Final. ANUNCIO Cl 22 = FASE 4 dia 2 = PILLAR 1 chunk (1 min memorizable, mismo formato).',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase21_REPORTE.pdf')

print('\n2 PDFs generados para lunes 01/06 B2 PM Amina Cl 21:')
print('  - B2/B2_PM_Amina_Clase21_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase21_REPORTE.pdf')
