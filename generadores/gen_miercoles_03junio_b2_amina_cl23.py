#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 23 (miercoles 03/06/2026):
- FASE 4 DIA 3/8 - chunk PILLAR 2.
  Centro = MEMORIZACION + ENSAYO de PILLAR 2 (~1 min) SIN PAPEL.
  Mismo metodo validado Cl 21 (HOOK) y Cl 22 (PILLAR 1):
  memorizacion guiada -> individual -> parejas -> mini-audiencia.
  Empalme P1 -> P2 trabajado en 2do paso de mini-audiencia.
- Refresh inicial corto encadenando HOOK + PILLAR 1 + arranque
  de PILLAR 2 (3 min, dentro del centro). NO se encadenan los
  3 chunks completos hoy - encadenamiento formal inicia Cl 25.
- Academic B2 Vocab Set #16 (6 nuevas: consolidate/reinforce/
  complement/extend/amplify/segue -> total 96). Set #16 ayuda
  a que PILLAR 2 suene de CONSOLIDACION argumental, NO de
  repeticion de PILLAR 1. Entra en uso HOY.
- Virtud PRUDENCIA dia 3 (bloque Cl 21-25 PRUDENCIA v2 -
  rotacion estandar cohorte B2, regla confirmada Diana 22/05).
- ~26 horas / ~21 dias hasta el Final (~22 junio) - derivado
  de Cl 20 (~32h/~24 dias al 29/05) +5 dias calendario
  (vie 29 -> mie 03) -6h bloque Cl 21-23 (3 clases x 2h).
- Estructura Fase 4 segun ROADMAP 72h (lineas 120-129):
  Cl 21-24 memorizan 1-2 chunks por sesion, Cl 25-28 encadenan
  2->3->4->5 chunks, C4 fin Cl 28 = video 3 min de memoria.
  El formato CONCRETO (memorizacion + individual + parejas +
  mini-audiencia + 2do paso empalme) es metodo operativo
  Heiiu del cohorte Amina, NO inventa criterio C4.
- HOY NO ES CHECKPOINT. No va paquete a coordinacion; el
  proximo checkpoint formal es C4 fin Cl 28.
- Tarea STRICT 4 componentes (HOOK+P1+P2 memoria + audio
  encadenado x3 + auto-escucha + 2 mejoras + repaso 96 palabras)
  due jueves 04/06 antes 6 PM. Anuncio Cl 24 = chunk PILLAR 3.
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase23_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase23_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase23_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 22)', '5 min'),
    ('EL POR QUE DE HOY (Fase 4 dia 3 - chunk PILLAR 2 sin papel)', '4 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (PRUDENCIA dia 3 - dia del medio del bloque)', '5 min'),
    ('RECAP EXPRESS - arquitectura (HOOK+P1 cerrados, P2 hoy) + 6 capas (connectors + topic chunks + paraphrase bridge en el empalme)', '5 min'),
    ('ACADEMIC B2 VOCAB SET #16 (6 palabras de consolidacion argumental para PILLAR 2 - total 96)', '7 min'),
    ('PLAN DE HOY: chunk PILLAR 2 sin papel + metodo repetido (memorizacion / individual / parejas / mini-audiencia)', '5 min'),
    ('PEER TEACHER SLOT corto (error oral Cl 22)', '3 min'),
    ('CHUNK PILLAR 2 SIN PAPEL - CENTRO DE HOY (45 min: refresh HOOK+P1+arranque P2 + memorizacion guiada + ensayo individual + parejas + mini-audiencia)', '45 min'),
    ('2do paso mini-audiencia P2 + EMPALME con P1 ya cerrado (chunks P1+P2 encadenados, 1 pregunta honesta por estudiante)', '10 min'),
    ('FRASE DEL DIA cierre + Paraphrase check + auto-observacion (NO nota)', '5 min'),
    ('ERROR PAPER LIVE (errores DE PILLAR 2: empalme frio / P2=P1 / vocab Set #16 mal colocado / voz al papel)', '5 min'),
    ('CIERRE + ANUNCIO Cl 24 (chunk PILLAR 3) + TAREA STRICT 4 componentes (HOOK+P1+P2 memoria + audio x3 + 2 mejoras + repaso 96)', '6 min'),
    ('Buffer / contingencia / despedida', '5 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 22',
    'Foto del tablero - Frase del Dia + B2 Set #16 + Arquitectura (HOOK+P1 cerrados, P2 hoy) + Reglas Fase 4 chunk + Metodo repetido',
    'HOJA INTERNA SEGUIMIENTO CHUNKS por estudiante (Fase 4: HOOK cerrado / P1 cerrado / P2 HOY - sin papel si/no, empalme limpio si/no, P2 distinto de P1 si/no, palabra Set #16 usada, tiempo real). NO va a coordinacion hoy - mapa interno; coordinacion reabre con C4 fin Cl 28',
    'CHECKLIST especifico Fase 4 dia 3 hoy: 5 estudiantes hicieron PILLAR 2 sin papel en mini-audiencia / 5 hicieron 2do paso EMPALME P1+P2 / orden de mini-audiencia anotado / tiempo promedio del chunk anotado / # de "restart por glance" anotado por estudiante / 1 palabra Set #16 usada por estudiante',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante (hoy errores de PILLAR 2: empalme frio / P2 que repite P1 / vocab Set #16 mal colocado / voz al papel)',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: si alguien NO logro PILLAR 2 sin papel ni en 2do intento (no juicio - solo dato) - notificar al cierre',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 22',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 3/8 DE FASE 4: Cl 21 cerro HOOK / Cl 22 cerro PILLAR 1 / hoy Cl 23 = PILLAR 2 sin papel (mismo metodo) / manana PILLAR 3 / Cl 25+ encadenamiento / Cl 28 = C4 video 3 min',
    'ESCRIBI Frase del Dia + B2 Set #16 + Arquitectura completa (HOOK y P1 marcados CERRADOS, P2 marcado HOY) + Reglas chunk Fase 4 + Metodo repetido (memorizacion/individual/parejas/mini-audiencia) en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 23 = PRUDENCIA dia 3 (bloque Cl 21-25 PRUDENCIA v2 - rotacion estandar cohorte B2, regla confirmada Diana 22/05)',
    'Hile PRUDENCIA en VATS + Frase del Dia (la prudencia del dia del medio: hacer el chunk de hoy sin acelerar a encadenar ni regresar a re-pulir el guion)',
    'Mantuve las 6 capas visibles como SUSTRATO (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing) con foco hoy en connectors + topic chunks + paraphrase bridge en el EMPALME P1->P2',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-22)',
    'Presente 6 palabras B2 Set #16 con pronunciacion + ejemplo orientado al EMPALME P1->P2 y a la consolidacion argumental de PILLAR 2 (total 96)',
    'Mostre la ARQUITECTURA con HOOK y PILLAR 1 marcados CERRADOS (Cl 21-22) y PILLAR 2 marcado HOY como anclaje del trabajo del dia',
    'Conduje el REFRESH inicial encadenando HOOK + PILLAR 1 + arranque PILLAR 2 (2 estudiantes al azar, ~1 min cada uno) sin papel',
    'Conduje las 4 etapas del metodo: (A) memorizacion guiada 10 min / (B) individual voz baja 10 min / (C) parejas 10 min / (D) mini-audiencia 12 min con 5 estudiantes x ~1 min sin papel',
    'APLIQUE LA REGLA "paper face down": si una estudiante miro papel en una rep, le pedi restart de esa rep (no continuar leyendo)',
    'Conduje el 2DO PASO mini-audiencia (10 min) con EMPALME P1+P2 encadenados (~2 min por estudiante) + 1 pregunta honesta del grupo',
    'NO INVENTE CRITERIOS C4 (hoy no es checkpoint) - hoja interna es mapa, NO comunicacion de evaluacion; coordinacion reabre con C4 fin Cl 28',
    'NO comunique nota ni juicio a ninguna estudiante - "you said P2 without paper X times today" es dato, no nota',
    'Conduje la AUTO-OBSERVACION de cierre (cada quien dice lo mas dificil de SU pillar 2) como PROCESO, NO como comunicacion de evaluacion',
    'Camine con papel errores anonimo (errores de PILLAR 2: empalme frio con connector / P2 que repite P1 / Set #16 mal pronunciado / voz que volvio al papel)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (DE PILLAR 2)',
    'ANUNCIE Cl 24 jueves = FASE 4 DIA 4 = chunk PILLAR 3 (mismo metodo, ultimo pillar antes de encadenar)',
    'En Tarea explique el por que (Fase 4 = memoria diaria, NO descanso) + due date explicito (jueves 04/06 antes de 6:00 PM) + 4 componentes (HOOK+P1+P2 memoria / audio encadenado x3 / auto-escucha + 2 mejoras / repaso 96 palabras)',
    'NO acepte la excusa "no me da tiempo" (Fase 4 sube intensidad respecto al fin de semana de descanso)',
    'Notifique a coordinacion al cierre si hay 2 strikes / si alguien NO logro PILLAR 2 sin papel ni en 2do intento / inasistencia hoy',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase23_REPORTE.pdf'),
    'B2 PM AMINA | Cl 23 de 36 | FASE 4 DIA 3/8 — CHUNK PILLAR 2 SIN PAPEL | EMPALME P1->P2 + SET #16 CONSOLIDACION | FRASE DEL DIA (Goldlist retirado)',
    'FASE 4 DIA 3/8 - chunk PILLAR 2 (~1 min) DE MEMORIA SIN PAPEL. Cl 21 cerro HOOK + Cl 22 cerro PILLAR 1 (ambos sin papel, mismo metodo). Hoy Cl 23 repite el metodo sobre PILLAR 2: (A) memorizacion guiada 10 min - script abierto 1 vez, luego cerrado / (B) ensayo individual voz baja 10 min sin papel, restart si glance / (C) parejas 10 min con foco en EMPALME P1->P2 / (D) mini-audiencia 12 min, 5 estudiantes x ~1 min sin papel. Luego 2do paso mini-audiencia (10 min) encadenando PILLAR 1 + PILLAR 2 (~2 min por estudiante) + 1 pregunta honesta del grupo. Refresh inicial corto (3 min) encadenando HOOK + PILLAR 1 + arranque PILLAR 2 - NO se encadenan los 3 chunks completos hoy (encadenamiento formal inicia Cl 25). Academic B2 Set #16 (consolidate/reinforce/complement/extend/amplify/segue - total 96) entra en uso HOY para que PILLAR 2 suene de CONSOLIDACION argumental, NO de repeticion de PILLAR 1. Cl 23 = PRUDENCIA dia 3 (bloque Cl 21-25 PRUDENCIA v2 - rotacion estandar cohorte B2, regla confirmada Diana 22/05). ~26h/~21 dias al Final. HOY NO ES CHECKPOINT - coordinacion reabre con C4 fin Cl 28 (video 3 min de memoria). Tarea STRICT 4 componentes (HOOK+P1+P2 memoria + audio encadenado x3 + auto-escucha + 2 mejoras + repaso 96 palabras) due jueves 04/06 antes 6 PM. Anuncio Cl 24 = chunk PILLAR 3.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase23_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 03/06 B2 PM Amina Cl 23:')
print('  - B2/B2_PM_Amina_Clase23_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase23_REPORTE.pdf')
