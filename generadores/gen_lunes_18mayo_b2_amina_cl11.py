#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del B2 PM Amina Cl 11 (lunes 18/05/2026):
- FASE 2 Recoleccion Oral dia 6/7 - Layer 6 Repetition/Paraphrasing + Speak About R6
- Academic B2 Vocab Set #4 (6 nuevas -> total 24) + Frase del Dia + virtud JUSTICIA dia 1 v1
- 50 horas / 35 dias hasta el Final (~22 junio)
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

md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase11_PRINT.md'),
          os.path.join(B2_DIR, 'B2_PM_Amina_Clase11_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase11_GUIA.pdf')

b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas (tarea Cl 10)', '5 min'),
    ('EL POR QUE DE HOY', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (JUSTICIA dia 1 v1)', '5 min'),
    ('RECAP EXPRESS - Anchors + Connectors + Q&A + Chunks + Discourse + Intonation', '5 min'),
    ('ACADEMIC B2 VOCAB SET #4 (6 palabras nuevas - total 24)', '8 min'),
    ('REPETITION / PARAPHRASING - Layer 6 (NUEVO)', '17 min'),
    ('PEER TEACHER SLOT corto (error Cl 10)', '3 min'),
    ('SPEAK ABOUT R6 - todas las capas + repetition/paraphrasing consciente', '50 min'),
    ('FRASE DEL DIA cierre + Paraphrase check', '5 min'),
    ('ERROR PAPER LIVE', '7 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 10',
    'Foto del tablero - Frase del Dia + B2 Set #4 + Repetition/Paraphrasing',
    'Foto/video Speak About R6 (todas las capas + recuperacion bajo presion)',
    'Notas POR ESTUDIANTE: repetition/stall / paraphrase / discourse markers / intonation / B2 words / chunks',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 10',
    'LEI PUBLICAMENTE los nombres de quien NO entrego',
    'ESCRIBI Frase del Dia + B2 Set #4 + Repetition/Paraphrasing en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (incluida 1 parafraseada)',
    'AL CIERRE 1 estudiante la dijo + 1 la parafraseo',
    'NO use GoldList (ritual cerrado)',
    'Verifique virtud CL 11 = JUSTICIA dia 1 v1 (por numero de clase)',
    'Hile JUSTICIA en VATS + Frase del Dia (fairness)',
    'Mantuve Anchors + Connectors + Q&A + Chunks + Discourse + Intonation visibles',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS (no Cl 6-10)',
    'Presente 6 palabras B2 Set #4 con pronunciacion + ejemplo (total 24)',
    'Ensene Repetition (echo/stall/key-word) + Paraphrasing (simpler/stronger/shorter)',
    'Mantuve el bridge formal->casual (version 1 formal / version 2 parafraseada)',
    'Conduje Speak About R6 con TODAS las capas + repetition/paraphrasing consciente',
    'Lance pregunta HOSTIL/CURVEBALL a CADA estudiante post-presentacion',
    'Anote por estudiante: repetition / paraphrase / discourse / intonation / B2 words / chunks',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'En Tarea explique pedagogicamente el por que (35 dias hasta Final) + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes',
    'Anuncie Cl 12 = integracion total + Round evaluativo de Fase 2',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase11_REPORTE.pdf'),
    'B2 PM AMINA | Cl 11 de 36 | FASE 2 DIA 6/7 | LAYER 6 REPETITION/PARAPHRASING + B2 SET #4 | FRASE DEL DIA (Goldlist retirado)',
    'Repetition (echo/stall/key-word) + Paraphrasing (simpler/stronger/shorter) + Academic B2 Set #4 (discernible/juxtapose/tenuous/corroborate/overarching/notwithstanding -> total 24) + Speak About R6 todas las capas bajo presion + FRASE DEL DIA',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase11_REPORTE.pdf')

print('\n2 PDFs generados para lunes 18/05 B2 PM Amina Cl 11:')
print('  - B2/B2_PM_Amina_Clase11_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase11_REPORTE.pdf')
