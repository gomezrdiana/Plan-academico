#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 12 (martes 19/05/2026):
- FASE 2 Recoleccion Oral dia 7/7 - CIERRE: INTEGRACION TOTAL + RONDA EVALUATIVA (Speak About R7)
- Academic B2 Vocab Set #5 (6 nuevas -> total 30) + Frase del Dia + virtud JUSTICIA dia 2 v1
- 48 horas / 34 dias hasta el Final (~22 junio) — derivado de Cl 11 (50h/35d) -1 dia -2h clase
- Cl 13 = inicio Fase 3 (escritura). SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B2_DIR = os.path.join(D, 'B2')
B2_REP = os.path.join(B2_DIR, 'reportes')
os.makedirs(B2_REP, exist_ok=True)

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase12_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase12_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase12_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 11)', '5 min'),
    ('EL POR QUE DE HOY', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (JUSTICIA dia 2 v1)', '5 min'),
    ('RECAP EXPRESS - las 6 capas (Anchors -> Repetition/Paraphrasing)', '5 min'),
    ('ACADEMIC B2 VOCAB SET #5 (6 palabras nuevas - total 30)', '8 min'),
    ('INTEGRACION - las 6 capas como reflejo + reglas Ronda Evaluativa', '17 min'),
    ('PEER TEACHER SLOT corto (error Cl 11)', '3 min'),
    ('SPEAK ABOUT R7 - RONDA EVALUATIVA: todas las capas integradas', '50 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE', '7 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 11',
    'Foto del tablero - Frase del Dia + B2 Set #5 + Reglas Ronda Evaluativa',
    'Foto/video Speak About R7 (ronda evaluativa - todas las capas integradas)',
    'NOTAS DE INTEGRACION POR ESTUDIANTE (interno - NO se comunica nota): capas solas vs forzadas / repetition / paraphrase / discourse / intonation / B2 words Set #5 / chunks',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 11',
    'LEI PUBLICAMENTE los nombres de quien NO entrego',
    'ESCRIBI Frase del Dia + B2 Set #5 + Reglas Ronda Evaluativa en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 12 = JUSTICIA dia 2 v1 (por numero de clase)',
    'Hile JUSTICIA en VATS + Frase del Dia (fairness)',
    'Mantuve las 6 capas visibles (Anchors + Connectors + Q&A + Chunks + Discourse + Intonation + Repetition/Paraphrasing)',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-11)',
    'Presente 6 palabras B2 Set #5 con pronunciacion + ejemplo (total 30)',
    'Conduje el drill de INTEGRACION (las 6 capas como un solo reflejo)',
    'Mantuve el bridge formal->casual (version 1 formal / version 2 parafraseada)',
    'Conduje Speak About R7 como RONDA EVALUATIVA con turno mas completo + TODAS las capas integradas',
    'Lance pregunta HOSTIL/CURVEBALL a CADA estudiante post-presentacion',
    'Registre NOTAS DE INTEGRACION por estudiante (INTERNO) sin comunicar nota ni juicio',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'En Tarea explique pedagogicamente el por que (34 dias hasta Final) + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes',
    'Anuncie Cl 13 = TRANSICION A FASE 3 (empieza la escritura del proyecto)',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase12_REPORTE.pdf'),
    'B2 PM AMINA | Cl 12 de 36 | FASE 2 DIA 7/7 — INTEGRACION + RONDA EVALUATIVA | CIERRE FASE 2 + B2 SET #5 | FRASE DEL DIA (Goldlist retirado)',
    'Integracion de las 6 capas (Anchors/Connectors/Q&A/Chunks/Discourse+Intonation/Repetition+Paraphrasing) como un solo reflejo + Academic B2 Set #5 (delineate/pervasive/salient/preclude/cogent/albeit -> total 30) + Speak About R7 RONDA EVALUATIVA (turno mas completo + pregunta hostil a cada estudiante; integracion evaluada INTERNO, no se comunica nota) + cierre Fase 2 -> Cl 13 inicia Fase 3 escritura + FRASE DEL DIA',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase12_REPORTE.pdf')

print('\n2 PDFs generados para martes 19/05 B2 PM Amina Cl 12:')
print('  - B2/B2_PM_Amina_Clase12_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase12_REPORTE.pdf')
