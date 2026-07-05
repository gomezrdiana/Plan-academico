#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 25 (viernes 05/06/2026):
- FASE 4 PRACTICA EN CHUNKS dia 5/8 - CIERRE SEMANA 1 FASE 4 +
  MEMORIZACION DEL CTA (Call To Action). Cl 21-24 cerraron HOOK +
  PILLAR 1 + PILLAR 2 + PILLAR 3 sin papel. Hoy cierra el ULTIMO
  chunk individual: CTA (30-60 seg, el mas corto y el mas critico
  porque es lo ultimo que la audiencia se lleva).
- Centro = PRACTICA CTA SIN PAPEL 45 min en 3 fases: ALONE 10 min
  (memo solo con paper) + PAIRS 15 min (drill coach honesto sin
  papel) + MINI-AUDIENCIA 20 min (cada estudiante CTA de memoria
  + 1 observacion precision del grupo). + Recap completo 9 min (1
  vez mas, sin coaching).
- Refresh mental 2 min ANTES de la practica: HOOK + 3 PILLARS
  encadenados SILENCIOSO (mental, no out loud) - confirma que las
  4 piezas anteriores estan vivas antes de anadir la quinta. NO es
  ensayo, es chequeo.
- Academic B2 Vocab Set #18 (6 nuevas: mobilize/galvanize/propel/
  summon/rally/prompt -> total 108). Set #18 es vocabulario de
  ACCION / CIERRE para CTA; puede entrar al apretarlo, pero la
  version escrita en Cl 18-19 es la base que se memoriza.
- Virtud PRUDENCIA v2 dia 5 (ULTIMO dia del bloque, Cl 21-25
  PRUDENCIA v2 ciclo 2 cerrado). Cl 26 lunes abre TEMPLANZA v2
  dia 1 (rotacion estandar cohorte B2 confirmada Diana 22/05/2026,
  memoria project-b2-virtud-rotacion-estandar).
- ~22 horas / ~17 dias hasta el Final (~22 junio) - derivado de
  Cl 20 (~32h/~24d) -10h bloque Cl 21-25 (5 clases x 2h) (verificado
  calendario: 22/06/2026 - 05/06/2026 = 17 dias).
- Estructura Fase 4 segun ROADMAP 72h (lineas 120-129): Cl 21-28,
  16h, chunk = 1 min, Cl 21-24 practican 1-2 chunks por sesion de
  memoria, Cl 25-28 encadenan 2->3->4->5 chunks. Cl 25 es dia
  PUENTE: anade el ULTIMO chunk individual (CTA) y conceptualmente
  abre el encadenamiento que arranca lunes con voz audible.
- CIERRE SEMANA 1 FASE 4: con el cierre de hoy, las 5 piezas
  (HOOK + 3 PILLARS + CTA) viven memorizadas como bloques
  individuales. Lunes Cl 26 abre semana 2 = encadenar HOOK +
  PILLAR 1 con transicion real + TEMPLANZA v2 dia 1.
- Tarea fin de semana INTENSA: primer monologo COMPLETO de
  memoria (HOOK + 3 PILLARS + CTA, 5-7 min, sin papel) + 2 audios
  FULL-V1/V2 + 3 mejoras a mano + repaso 108 palabras (due lunes
  08/06 antes 6 PM).
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase25_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase25_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase25_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 24)', '5 min'),
    ('EL POR QUE DE HOY (Fase 4 dia 5/8 - CTA + cierre semana 1)', '4 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (PRUDENCIA v2 dia 5 - ULTIMO dia del bloque + puente TEMPLANZA v2 lunes Cl 26)', '5 min'),
    ('RECAP EXPRESS - arquitectura completa (HOOK + 3 PILLARS + CTA hoy) + 6 capas como sustrato del CTA', '5 min'),
    ('ACADEMIC B2 VOCAB SET #18 (6 palabras nuevas - accion/cierre para CTA - total 108)', '7 min'),
    ('REFRESH MENTAL: HOOK + 3 PILLARS encadenados SILENCIOSO sin papel (chequeo memoria, NO ensayo)', '2 min'),
    ('PLAN DE HOY: PRACTICA CTA SIN PAPEL - instrucciones 3 fases + regla precision (no improvisar)', '5 min'),
    ('PEER TEACHER SLOT corto (error oral Cl 24)', '3 min'),
    ('PRACTICA CTA SIN PAPEL - CENTRO DE HOY: ALONE 10 min (memo con paper) + PAIRS 15 min (drill sin papel coach honesto) + MINI-AUDIENCIA 20 min (cada CTA de memoria + 1 observacion precision)', '45 min'),
    ('RECAP COMPLETO: cada estudiante recita CTA de memoria 1 vez mas sin coaching (5 estudiantes)', '9 min'),
    ('FRASE DEL DIA cierre + Paraphrase check + auto-observacion (NO nota)', '5 min'),
    ('ERROR PAPER LIVE (errores DE MEMORIA CTA: precision palabras / cierre vago / bridge perdido / muletillas / intonacion ascendente al final)', '5 min'),
    ('CIERRE FORMAL SEMANA 1 FASE 4 + PUENTE SEMANA 2 (encadenamiento lunes Cl 26 + TEMPLANZA v2 dia 1) + TAREA STRICT 4 componentes (intensa - primer monologo completo de memoria)', '10 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 24',
    'Foto del tablero - Frase del Dia + B2 Set #18 + Arquitectura completa (CTA marcado HOY) + Reglas practica CTA + Mensaje cierre semana 1 Fase 4',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante (hoy errores DE MEMORIA CTA: precision palabras / cierre vago / bridge casual perdido / muletillas / intonacion ascendente al final)',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: si alguien NO logro CTA de memoria en Fase C mini-audiencia (levanto papel mas de 1 vez / cierre vago repetido) - notificar al cierre',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 24',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 5/8 + CIERRE SEMANA 1: Cl 21-24 cerraron HOOK + 3 PILLARS de memoria / hoy Cl 25 cierra CTA = el chunk mas corto y critico / con esto las 5 piezas viven memorizadas / lunes Cl 26 abre semana 2 = encadenar HOOK + PILLAR 1',
    'ESCRIBI Frase del Dia + B2 Set #18 + Arquitectura completa (HOOK + 3 PILLARS + CTA marcado hoy) + Reglas practica CTA en 3 fases + Mensaje cierre semana 1 + puente encadenamiento lunes en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 25 = PRUDENCIA v2 dia 5 (ULTIMO dia del bloque - rotacion estandar cohorte B2 confirmada Diana 22/05) + anuncie que Cl 26 lunes abre TEMPLANZA v2 dia 1',
    'Hile PRUDENCIA en VATS + Frase del Dia (sabiduria practica = el cierre es lo que se recuerda + escribir CTA pensando en la memoria de la audiencia, NO en el oido propio)',
    'Mantuve las 6 capas visibles como SUSTRATO del CTA (closing marker mirror de opening / anchor devuelto del hook / bridge formal->casual / repetition deliberate / intonacion descendente firme al final)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-24) - elegidos con eco fonetico de Set #18 (closing/mobilize/propel/rally)',
    'Presente 6 palabras B2 Set #18 con pronunciacion + ejemplo orientado a CTA (mobilize/galvanize/propel/summon/rally/prompt - total 108) + aclare que pueden entrar en CTA al apretarlo pero la version escrita en Cl 18-19 es la base que se memoriza',
    'Conduje REFRESH MENTAL 2 min (HOOK + 3 PILLARS encadenados SILENCIOSO, NO out loud, NO ensayo) - chequeo de memoria viva antes de anadir CTA',
    'Explique las INSTRUCCIONES de la practica CTA en 3 fases (ALONE 10 min con paper / PAIRS 15 min sin papel coach honesto / MINI-AUDIENCIA 20 min cada CTA de memoria) + REGLA PRECISION (memorizan la version SUYA escrita en Cl 18-19, NO improvisan)',
    'CONDUJE FASE A ALONE 10 min (silencio en sala, drill whispered + cubrir paper + 3 intentos limpios) - NO interrumpi, anote en libreta privada quien tardo mas en cubrir paper (senal CTA menos memorizable)',
    'CONDUJE FASE B PAIRS 15 min (papel face down en piso, 3-4 vueltas por persona, partner B flag UNA observacion precision) - rote silenciosa 2-3 min por pareja, intervine SOLO si se desviaron a reescribir',
    'CONDUJE FASE C MINI-AUDIENCIA 20 min (5 estudiantes x ~4 min: CTA de memoria + 1 observacion precision del grupo, NO advice) - cronometre, anote arquitectura interna por estudiante en libreta privada',
    'NO INVENTE CRITERIOS DE EVALUACION (no di puntaje, no di juicio, no comunique resultado) - solo observacion cruda en libreta privada + papel anonimo publico',
    'CONDUJE RECAP COMPLETO 9 min (cada estudiante recita CTA 1 vez mas de memoria, sin coaching, sin comentario de calidad - solo "thank you, next")',
    'Conduje la AUTO-OBSERVACION de cierre (cada quien dice que parte de SU CTA quedo solida y cual falto precision) como PROCESO, NO como comunicacion de evaluacion',
    'Camine con papel errores anonimo (errores de MEMORIA CTA: precision palabras / cierre vago / bridge casual perdido / muletillas / intonacion ascendente al final / improvisar palabras nuevas)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (DE MEMORIA CTA hoy)',
    'ANUNCIE FORMALMENTE el cierre de SEMANA 1 FASE 4 + puente a SEMANA 2 (Cl 26 lunes = encadenar HOOK + PILLAR 1 con transicion real / Cl 27 = + PILLAR 2 / Cl 28 = monologo completo de memoria + C4 video 3 min)',
    'ANUNCIE el cambio de virtud (PRUDENCIA v2 cierra hoy / TEMPLANZA v2 abre lunes Cl 26 con el encadenamiento)',
    'En Tarea explique el por que (INTENSA - primer monologo COMPLETO de memoria) + due date explicito (lunes 08/06 antes de 6:00 PM) + 4 componentes claros (monologo de memoria mental drill + 2 audios FULL-V1 sabado FULL-V2 domingo + escuchar mejor audio + 3 mejoras a mano + repaso 108 palabras)',
    'NO acepte la excusa "no me da tiempo"',
    'NO acepte la excusa "no lo memorize entero" - si una pieza no entra, vuelve a esa pieza aislada antes de intentar el monologo entero (orden HOOK-P1-P2-P3-CTA no se salta)',
    'Notifique a coordinacion al cierre si hay 2 strikes / sospecha IA residual / inasistencia hoy / CTA no logrado de memoria en Fase C',
    'Anuncie Cl 26 lunes = SEMANA 2 FASE 4 ABRE = encadenamiento HOOK + PILLAR 1 con transicion real + TEMPLANZA v2 dia 1 (nuevo bloque virtud)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase25_REPORTE.pdf'),
    'B2 PM AMINA | Cl 25 de 36 | FASE 4 PRACTICA EN CHUNKS DIA 5/8 | CIERRE SEMANA 1 FASE 4 + MEMORIZACION CTA SIN PAPEL | FRASE DEL DIA (Goldlist retirado)',
    'FASE 4 PRACTICA EN CHUNKS DIA 5/8 - CIERRE SEMANA 1 + MEMORIZACION DEL CTA (Call To Action, 30-60 seg, el chunk mas corto y mas critico - lo ultimo que la audiencia se lleva). Cl 21-24 cerraron HOOK + 3 PILLARS de memoria sin papel. Hoy Cl 25 cierra el ULTIMO chunk individual: CTA. Centro = PRACTICA CTA SIN PAPEL 45 min en 3 fases: ALONE 10 min (memo con paper) + PAIRS 15 min (drill sin papel coach honesto) + MINI-AUDIENCIA 20 min (cada CTA de memoria + 1 observacion precision grupo) + Recap completo 9 min (1 vez mas sin coaching). Refresh mental 2 min ANTES de la practica: HOOK + 3 PILLARS encadenados SILENCIOSO (NO out loud, NO ensayo) - chequeo de memoria viva antes de anadir la quinta pieza. Con el cierre de hoy, las 5 piezas del monologo (HOOK + 3 PILLARS + CTA) viven memorizadas como bloques individuales. Lunes Cl 26 abre SEMANA 2 = encadenar HOOK + PILLAR 1 con transicion real + TEMPLANZA v2 dia 1 (cambio virtud). Academic B2 Set #18 (mobilize/galvanize/propel/summon/rally/prompt -> total 108) = vocab de ACCION/CIERRE para CTA; puede entrar al apretarlo, pero la version escrita en Cl 18-19 es la base que se memoriza. Profesora NUNCA comunica nota - observacion privada en libreta + papel anonimo publico. Cl 25 = PRUDENCIA v2 dia 5 (ULTIMO dia del bloque cohorte B2 ciclo 2; Cl 26 abre TEMPLANZA v2 dia 1). ~22h/~17 dias al Final. Tarea fin de semana INTENSA: primer monologo COMPLETO de memoria (HOOK + 3 PILLARS + CTA, 5-7 min, sin papel) + 2 audios FULL-V1 sabado FULL-V2 domingo + escuchar mejor audio + 3 mejoras a mano + repaso 108 palabras (due lunes 08/06 antes 6 PM).',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase25_REPORTE.pdf')

print('\n2 PDFs generados para viernes 05/06 B2 PM Amina Cl 25:')
print('  - B2/B2_PM_Amina_Clase25_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase25_REPORTE.pdf')
