#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 20 (viernes 29/05/2026):
- FASE 3 DIA 8/8 - ULTIMO DIA DE FASE 3 + CHECKPOINT C3 + CIERRE FORMAL.
  Centro = SEGUNDO ENSAYO ORAL COMPLETO (5-7 min por estudiante) frente
  al grupo (mini-audiencia interna, NO publico externo) + Q&A breve del
  grupo (1-2 preguntas honestas) + arquitectura interna anotada por
  estudiante (NO se comunica nota) + ENTREGABLE C3 entregado FISICAMENTE
  a Diana al cierre del dia (sobre rotulado: 5 guiones fisicos completos
  + 5 audios o notas Amina + 5 hojas arquitectura + foto cierre Fase 3).
- Profesora NO inventa criterios C3 (eso es coordinacion); entrega el
  material crudo + sus notas; Diana / coordinacion deciden C3 despues
  de clase. La estudiante NO sabe resultado hoy.
- Academic B2 Vocab Set #13 (6 nuevas: rehearse/encapsulate/condense/
  signpost/calibrate/hone -> total 78). Set #13 es vocabulario PUENTE
  a Fase 4 (chunks/practica/memoria); entra en uso el LUNES Cl 21, NO
  en el ensayo de hoy.
- Virtud FORTALEZA dia 5 (ULTIMO dia del bloque - regla cohorte B2,
  rotacion estandar, NO supuesto; Cl 16-20 FORTALEZA v1 cerrado).
  Cl 21 lunes = nueva virtud (SUPUESTO: PRUDENCIA v2 - inicio ciclo 2
  de las 4 cardinales; verificar con coordinacion).
- ~32 horas / ~24 dias hasta el Final (~22 junio) - derivado de Cl 16
  (~40h/~28d) +4 dias calendario (lun 25 -> vie 29) -8h bloque Cl 17-20
  (4 clases x 2h) (verificado: 22/06/2026 - 29/05/2026 = 24 dias;
  40h - 8h = 32h).
- Estructura Fase 3 segun ROADMAP 72h (lineas 115-118): Cl 13-15
  transcripcion / Cl 16-18 estructura / Cl 19-20 pulir vocabulario B2.
  CHECKPOINT C3 (linea 152) = fin Cl 20 = "guion escrito de cada
  estudiante", pregunta de coordinacion "¿listo para memorizar?".
  El 2do ensayo oral + entrega fisica es FORMATO Heiiu interno como
  mejor evidencia anti-fraude del cierre - NO inventa criterio C3.
- PUENTE A FASE 4: Cl 21-28 (16h, Roadmap lineas 120-129) = practica
  en CHUNKS de 1 minuto. Cl 21-24 = 1-2 chunks por sesion, de memoria.
  Cl 25-28 = encadenar 2->3->4->5 chunks. C4 fin Cl 28 = video 3 min
  de memoria. Por eso tarea fin de semana es LIGERA + DESCANSO DE VOZ.
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase20_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase20_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase20_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 19)', '5 min'),
    ('EL POR QUE DE HOY (Fase 3 dia 8/8 - CHECKPOINT C3 + CIERRE)', '4 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (FORTALEZA dia 5 - ULTIMO dia del bloque + puente nuevo bloque virtud)', '5 min'),
    ('RECAP EXPRESS - arquitectura completa (HOOK + 3 PILLARS + CTA) + 6 capas como sustrato sostenido en voz', '5 min'),
    ('ACADEMIC B2 VOCAB SET #13 (6 palabras nuevas - puente a Fase 4 chunks - total 78)', '7 min'),
    ('PLAN DE HOY: 2do ENSAYO COMPLETO + INSTRUCCIONES MINI-AUDIENCIA + REGLA C3 (no comunicar nota)', '5 min'),
    ('PEER TEACHER SLOT corto (error Cl 19)', '3 min'),
    ('SEGUNDO ENSAYO ORAL COMPLETO - CENTRO DE HOY (5 estudiantes x ~12 min: 5-7 min monologo + 1-2 min Q&A grupo + transiciones)', '60 min'),
    ('FRASE DEL DIA cierre + Paraphrase check + auto-observacion (NO nota)', '5 min'),
    ('ERROR PAPER LIVE (errores DE ORAL del 2do ensayo: muletillas / transiciones / pronunciacion vocab / CTA flojo)', '5 min'),
    ('CIERRE FORMAL FASE 3 + PUENTE FASE 4 (chunks lunes Cl 21) + FOTO CIERRE + TAREA STRICT (ligera, descanso voz)', '4 min'),
    ('ENTREGA FISICA C3 A DIANA al cierre (sobre rotulado: 5 guiones + audios/notas + 5 hojas arquitectura + foto cierre Fase 3)', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 19',
    'Foto del tablero - Frase del Dia + B2 Set #13 + Arquitectura completa + Reglas 2do ensayo + Mensaje cierre Fase 3',
    'PAQUETE C3 FISICO entregado a Diana al cierre (sobre rotulado: 5 guiones fisicos completos + 5 audios o notas + 5 hojas arquitectura + 1 foto cierre Fase 3) - confirmar recibido con firma/hora',
    'NOTAS DE ARQUITECTURA POR ESTUDIANTE (interno - alimenta C3, NO se comunica): por las 5 estudiantes, sin calificacion, solo observacion cruda (HOOK / 3 PILLARS / CTA / vocab B2 / fluidez / transiciones / muletillas / Q&A / arquitectura global / tiempo real)',
    'CHECKLIST especifico C3 hoy: 5 ensayos orales hechos / tiempo promedio anotado / Q&A grupo activa / arquitectura interna anotada por las 5 / guion fisico recogido por las 5 / audio grabado por las 5 (o nota "no grabado") / entregable C3 entregado fisicamente a Diana al cierre / foto cierre Fase 3 tomada',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante (hoy errores DE ORAL del 2do ensayo)',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'ALERTA coordinacion: si alguien NO completo el 2do ensayo (falto / se corto / pidio no grabar) - notificar al cierre',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 19',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (accountability, NO comunicacion de evaluacion)',
    'EXPLIQUE EL DIA 8/8 + C3: Cl 13-15 cerro transcripcion / Cl 16-18 construyo arquitectura / Cl 19 cerro pulido + 1er ensayo / hoy Cl 20 = 2do ensayo + entrega fisica C3 + cierre Fase 3 + puente Fase 4',
    'ESCRIBI Frase del Dia + B2 Set #13 + Arquitectura completa (HOOK + 3 PILLARS + CTA) + Reglas 2do ensayo + Mensaje cierre Fase 3 + puente chunks en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 20 = FORTALEZA dia 5 (ULTIMO dia del bloque - rotacion estandar cohorte B2, regla confirmada Diana 22/05) + anuncie que Cl 21 abre nuevo bloque virtud',
    'Hile FORTALEZA en VATS + Frase del Dia (coraje de un 2do ensayo honesto bajo el peso de C3 + coraje de no saber el resultado hoy)',
    'Mantuve las 6 capas visibles como SUSTRATO sostenido en voz (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-19)',
    'Presente 6 palabras B2 Set #13 con pronunciacion + ejemplo orientado a Fase 4 chunks (total 78) - aclare que Set #13 entra en uso el LUNES, no hoy',
    'Mostre la ARQUITECTURA COMPLETA en tablero (HOOK + 3 PILLARS + CTA) como anclaje del 2do ensayo',
    'Explique las INSTRUCCIONES de la mini-audiencia (manos abajo, 1-2 preguntas honestas, NO advice, NO interrumpir) + la REGLA C3 (no comunico nota, paquete va a coordinacion al cierre, estudiante no sabe resultado hoy)',
    'CONDUJE 5 ENSAYOS ORALES COMPLETOS (5-7 min cada uno + Q&A grupo 1-2 preguntas) sin interrumpir, cronometrando, anotando arquitectura interna en hoja por estudiante',
    'NO INVENTE CRITERIOS C3 (no di puntaje, no di juicio, no comunique resultado) - solo observacion cruda en hoja interna',
    'RECOGI los 5 guiones fisicos completos (HOOK + 3 PILLARS + CTA + revisiones Cl 16-19) al cierre de cada ensayo',
    'GRABE audio del 2do ensayo cuando fue posible / marque "no grabado - notas en su lugar" cuando no',
    'TOME foto cierre Fase 3 (cohorte con guiones en mano)',
    'Conduje la AUTO-OBSERVACION de cierre (cada quien dice que fue lo mas dificil de SU 2do ensayo) como PROCESO, NO como comunicacion de evaluacion',
    'Camine con papel errores anonimo (errores de ORAL: muletillas que volvieron / transicion fria entre pillars / pronunciacion vocab Set #1-#12 / CTA flojo)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante (DE ORAL, del 2do ensayo)',
    'ANUNCIE FORMALMENTE el cierre de Fase 3 + puente a Fase 4 (Cl 21-28 = chunks de 1 min, Cl 21-24 memorizan 1-2 chunks, Cl 25-28 encadenan 2->5 chunks, C4 = video 3 min de memoria)',
    'En Tarea explique el por que (LIGERA, descanso de voz antes de Fase 4) + due date explicito (lunes 01/06 antes de 6:00 PM) + NADA NUEVO (NO mas guion, NO audios largos)',
    'NO acepte la excusa "no me da tiempo"',
    'ENTREGUE FISICAMENTE el sobre C3 a Diana al cierre del dia (5 guiones + audios o notas + 5 hojas arquitectura + foto cierre Fase 3) - confirme firma/hora de recibido',
    'NO comunique a las estudiantes "ya entregue C3" ni resultado (no existe resultado hoy)',
    'Notifique a coordinacion al cierre si hay 2 strikes / sospecha IA residual / inasistencia hoy / ensayo no completado',
    'Anuncie Cl 21 lunes = FASE 4 ABRE = chunks de 1 minuto, de memoria + nueva virtud (SUPUESTO PRUDENCIA v2, verificar)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase20_REPORTE.pdf'),
    'B2 PM AMINA | Cl 20 de 36 | FASE 3 DIA 8/8 — CHECKPOINT C3 + CIERRE FASE 3 | 2do ENSAYO ORAL COMPLETO + ENTREGA FISICA C3 A DIANA | FRASE DEL DIA (Goldlist retirado)',
    'FASE 3 DIA 8/8 - ULTIMO DIA + CHECKPOINT C3 + CIERRE FORMAL FASE 3. Cl 13-15 cerro TRANSCRIPCION (audio 1 + audio 2 a texto B2 limpio). Cl 16-18 cerro ESTRUCTURA (HOOK + 3 PILLARS + CTA). Cl 19 cerro PULIDO B2 + 1er ensayo oral. Hoy Cl 20 cierra todo: SEGUNDO ENSAYO ORAL COMPLETO (5-7 min por estudiante) frente al grupo (mini-audiencia interna, NO publico externo) + Q&A breve del grupo (1-2 preguntas honestas) + arquitectura interna anotada por estudiante (interna - alimenta C3, NO se comunica nota) + ENTREGABLE C3 entregado FISICAMENTE a Diana al cierre del dia (sobre rotulado: 5 guiones fisicos completos + 5 audios o notas Amina + 5 hojas arquitectura + foto cierre Fase 3). Profesora NO inventa criterios C3 (eso es coordinacion); entrega el material crudo + sus notas; Diana/coordinacion deciden C3 despues de clase; la estudiante NO sabe resultado hoy. Academic B2 Set #13 (rehearse/encapsulate/condense/signpost/calibrate/hone -> total 78) = vocabulario PUENTE a Fase 4 (chunks/practica/memoria); entra en uso el LUNES Cl 21, no hoy. Cl 20 = FORTALEZA dia 5 (ULTIMO dia del bloque cohorte B2; Cl 21 abre nuevo bloque virtud - SUPUESTO PRUDENCIA v2, verificar). ~32h/~24 dias al Final. PUENTE A FASE 4: Cl 21-28 (16h) = practica en CHUNKS de 1 min, Cl 21-24 memorizan 1-2 chunks por sesion, Cl 25-28 encadenan 2->3->4->5 chunks, C4 fin Cl 28 = video 3 min de memoria. Tarea fin de semana LIGERA + DESCANSO DE VOZ (nada nuevo) - due lunes 01/06 antes 6 PM.',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase20_REPORTE.pdf')

print('\n2 PDFs generados para viernes 29/05 B2 PM Amina Cl 20:')
print('  - B2/B2_PM_Amina_Clase20_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase20_REPORTE.pdf')
