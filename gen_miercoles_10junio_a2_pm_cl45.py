#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 45 (miercoles 10/06/2026):
- ARCO DE REPASO DE ERRORES COMUNES - CLUSTER 4: PREGUNTAS / NEGATIVOS / AUXILIARES + ORDEN DE PALABRAS
  (aux + S + V en 5 tiempos / don't/doesn't/didn't/isn't/aren't/haven't/hasn't/won't /
   SVO + adverbios de frecuencia antes del verbo principal pero despues de "to be")
- El A2 Book termino en M44 (pag 352); Cl 41 cerro el libro; Cl 42 abrio el arco (tiempos);
  Cl 43 corrigio comparativos/superlativos + gerundio vs infinitivo;
  Cl 44 corrigio phrasal verbs + voz pasiva.
  Cl 45 = cuarto cluster del arco de repaso A2->B1.
- FRASE DEL DIA + virtud PRUDENCIA v3 dia 5 ULTIMO del bloque (Cl 41-45 = PRUDENCIA v3).
- ANUNCIO EXPLICITO: Cl 46 jueves abre TEMPLANZA v3 dia 1 (NUEVO BLOQUE virtud, Cl 46-50).
- Error Paper EXPANDIDO (6 errores: 2 preguntas + 2 negativos/auxiliares + 2 orden palabras).
- Tarea 20-30 min, due jueves 11/06 antes 7:00 PM, NO fragmentada.
- Anuncio Cl 46 (jue 11/06): arco clase 5 = preposiciones + articulos/cuantificadores
  + TEMPLANZA v3 dia 1 (NUEVO BLOQUE virtud).
- SIN GoldList. Sin nombres. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class45_PRINT.md'), os.path.join(A2_DIR, 'A2_Class45_GUIA.pdf'))
print('OK: A2_Class45_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 44 - cluster 3: phrasal verbs + voz pasiva)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v3 dia 5 ULTIMO + puente a TEMPLANZA v3 manana)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de pregunta sin auxiliar: "Where you go?")', '7 min'),
    ('CORRECCION SISTEMATICA A - PREGUNTAS (aux + S + V en 5 tiempos)', '15 min'),
    ('CORRECCION SISTEMATICA B - NEGATIVOS + AUXILIARES (don\'t/doesn\'t/didn\'t/isn\'t/aren\'t/haven\'t/hasn\'t/won\'t)', '14 min'),
    ('CORRECCION SISTEMATICA C - ORDEN DE PALABRAS (SVO + adv. frecuencia antes del verbo / despues de be + objetos)', '14 min'),
    ('SPEED DRILL - los 3 sub-clusters en velocidad (15 items + parejas)', '12 min'),
    ('SIMULACION PROFESIONAL - The Job Interview (DE PIE, fuerza preguntas + negativos + auxiliares + orden)', '17 min'),
    ('SHADOWING (verificar dia del ciclo)', '8 min'),
    ('Error Paper EXPANDIDO (6 errores: 2 preguntas + 2 negativos/auxiliares + 2 orden palabras) + Frase del Dia CIERRE', '5 min'),
    ('Tarea + Cierre + ANUNCIO Cl 46 (cluster 5 + TEMPLANZA v3 dia 1 = NUEVO BLOQUE VIRTUD)', '2 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Preguntas + Negativos + Orden Palabras + Errores',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Job Interview',
    'Foto/video Shadowing',
    'Papel errores fisico (anonimo, 6 errores EXPANDIDO: 2 preguntas + 2 negativos/auxiliares + 2 orden palabras) - entregado fisicamente con la guia',
    'Lista quienes NO entregaron tarea Cl 44 (las 3 partes: 10 oraciones phrasal+pasiva + audio handover 2 min + listening 5 phrasal + 3 pasivas)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmacion de que ANUNCIASTE explicitamente Cl 46 = TEMPLANZA v3 dia 1 (nuevo bloque virtud)',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 44)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion (pregunta + negativo o pregunta + adverbio)',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 45 = PRUDENCIA v3 dia 5 ULTIMO (por numero de clase, Cl 41-45)',
    'Hile PRUDENCIA en VATS con preguntar + negar + ordenar antes de hablar',
    'ENTENDI que HOY es la CUARTA clase del ARCO DE REPASO (Cl 45 = arco clase 4)',
    'NO invente contenido: el A2 Book termino en M44; hoy = CORRECCION sistematica de errores tipicos',
    'CORRECCION A: preguntas (aux + S + V en 5 tiempos: presente, pasado, continuo, pres. perf., futuro)',
    'CORRECCION B: negativos (don\'t/didn\'t/haven\'t/won\'t + base; "no" suelto NO; haven\'t + past participle)',
    'CORRECCION C: orden palabras (SVO / frecuencia ANTES del verbo / DESPUES de be / manera/tiempo al final)',
    'Conduje Speed Drill 15 items mezclando preguntas (5 tiempos) + negativos + orden con adverbios',
    'Conduje Simulacion The Job Interview forzando preguntas en 4+ tiempos + negativos + adverbios bien ubicados',
    'Simulacion fue PROFESIONAL (entrevista real, interviewer pregunta + candidate responde, rotacion)',
    'Conduje Shadowing del ciclo activo',
    'ERROR PAPER EXPANDIDO (6 errores: 2 preguntas + 2 negativos/auxiliares + 2 orden palabras) - anonimo en clase / libreta con nombres',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (jueves 11/06 antes 7:00 PM)',
    'Tarea 20-30 min (A2), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'ANUNCIE EXPLICITAMENTE Cl 46 = arco clase 5 (preposiciones + articulos/cuantificadores) + TEMPLANZA v3 dia 1 = NUEVO BLOQUE VIRTUD',
    'CIERRE del bloque PRUDENCIA v3 marcado como ultimo dia + apertura TEMPLANZA v3 manana',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class45_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 45 de 55 | ARCO REPASO Cl 4 - PREGUNTAS / NEGATIVOS / AUXILIARES + ORDEN DE PALABRAS | PRUDENCIA v3 dia 5 ULTIMO | FRASE DEL DIA (Goldlist retirado)',
    'ARCO DE REPASO A2->B1 - CLUSTER 4: PREGUNTAS / NEGATIVOS / AUXILIARES + ORDEN DE PALABRAS (aux + S + V en 5 tiempos: presente, pasado, continuo, pres. perf., futuro / don\'t/doesn\'t/didn\'t/isn\'t/aren\'t/haven\'t/hasn\'t/won\'t + base o past participle / SVO + adverbios de frecuencia ANTES del verbo principal pero DESPUES de "to be" + objetos directos/indirectos) + Speed Drill 3 sub-clusters + The Job Interview + Error Paper EXPANDIDO 6 errores (2+2+2) + FRASE DEL DIA. El A2 Book termino en M44 (Cl 41 cerro); Cl 42-44 corrieron clusters 1-3; hoy Cl 45 = cuarto cluster (sostener conversacion real: preguntar bien, negar bien, ordenar bien). PRUDENCIA v3 dia 5 = ULTIMO del bloque (Cl 41-45). ANUNCIO EXPLICITO de Cl 46 = arco clase 5 (preposiciones + articulos/cuantificadores) + TEMPLANZA v3 dia 1 = NUEVO BLOQUE VIRTUD (Cl 46-50).',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class45_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 10/06 A2 PM Cl 45:')
print('  - A2/A2_Class45_GUIA.pdf')
print('  - A2/reportes/A2_Class45_REPORTE.pdf')
