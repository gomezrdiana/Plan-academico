#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera 4 PDFs para clases nocturnas del jueves 14/05/2026:
- A1 Cl 26 (Christian)  - M29 When Is It + FRASE DEL DIA (nuevo ritual, GoldList retired)
- B2 Amina Cl 9         - Topic-Specific Vocab Chunks + Academic B2 Set #2 + Speak About R4 + Frase del Dia
+ los reportes correspondientes
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
B2_DIR = os.path.join(D, 'B2')
A1_REP = os.path.join(A1_DIR, 'reportes')
B2_REP = os.path.join(B2_DIR, 'reportes')
for r in (A1_REP, B2_REP):
    os.makedirs(r, exist_ok=True)

# ============================================================
# A1 Cl 26 - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(A1_DIR, 'A1_Class26_PRINT.md'),
    os.path.join(A1_DIR, 'A1_Class26_GUIA.pdf'),
)
print('OK: A1_Class26_GUIA.pdf')

a1_c26_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion (NUEVO ritual)', '4 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 25)', '7 min'),
    ('CIERRE RITUAL GOLDLIST (anuncio sin drama)', '2 min'),
    ('LIBRO M29 - When Is It? + vocabulario tiempo', '20 min'),
    ('TIME DRILL - clock + days + prepositions', '15 min'),
    ('SIMULACION "Making an Appointment" (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '10 min'),
]
a1_c26_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M29 + Time prepositions',
    'Foto/video del PEER TEACHER en accion',
    'Foto/video Simulacion Making Appointment',
    'Foto/video Shadowing',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 25',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6 (anota quien falto hoy)',
    'Notas sobre como recibieron el cambio GoldList -> Frase del Dia',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_c26_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en seccion dedicada del tablero ANTES de clase',
    'PRESENTE la Frase del Dia al inicio con coro 3x',
    'INSERTE la Frase del Dia NATURALMENTE 3+ veces durante la clase',
    'AL CIERRE: 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'COMUNIQUE el cierre del ritual GoldList sin drama (2 min)',
    'NO use GoldList ni mencione Lista 3 en clase',
    'Cubri M29 When Is It DESDE EL LIBRO',
    'Hice Time Drill DE PIE con clock + days + prepositions',
    'Conduje Simulacion Making Appointment con AT/ON correctos',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que',
    'NO acepte la excusa "no me da tiempo"',
    'Anote como recibieron el cohorte el cambio GoldList -> Frase del Dia',
]

build_report_v2(
    os.path.join(A1_REP, 'A1_Class26_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 26 de 45 | M29 + FRASE DEL DIA NUEVO RITUAL | GOLDLIST RETIRADO',
    'M29 When Is It? Time Expressions (AT + hour, ON + day, IN + month) + Simulacion Making Appointment + FRASE DEL DIA primer dia (reemplaza GoldList) + cierre ritual GoldList sin drama',
    a1_c26_act, a1_c26_deliv, a1_c26_eval, S,
)
print('OK: A1_Class26_REPORTE.pdf')

# ============================================================
# B2 Amina Cl 9 - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase9_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase9_GUIA.pdf'),
)
print('OK: B2_PM_Amina_Clase9_GUIA.pdf')

b2_c9_act = [
    ('MYSTERY HOMEWORK CHECK + LECTURA PUBLICA no-entregas', '5 min'),
    ('EL POR QUE DE HOY + CIERRE RITUAL GOLDLIST', '3 min'),
    ('FRASE DEL DIA - presentacion (NUEVO ritual)', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas NUEVOS)', '6 min'),
    ('VATS TEMPLANZA dia 4 (v1)', '5 min'),
    ('ANCHOR + CONNECTOR RECAP express', '3 min'),
    ('Q&A HANDLING - 5 patterns recap rapido', '5 min'),
    ('ACADEMIC B2 VOCABULARY BANK - SET #2 (6 palabras NUEVAS)', '8 min'),
    ('TOPIC-SPECIFIC VOCABULARY CHUNKS - cada estudiante construye SU banco (NUEVO)', '14 min'),
    ('PEER TEACHER SLOT corto', '3 min'),
    ('SPEAK ABOUT R4 - todas las capas integradas + Q&A hostil + 2+ chunks propios', '50 min'),
    ('FRASE DEL DIA cierre + Q&A pattern check', '5 min'),
    ('ERROR PAPER LIVE', '7 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_c9_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'LISTA NOMINAL de quien NO entrego tarea Cl 8 (no anonimo)',
    'Foto del tablero - Frase del Dia + B2 Set #2 + Topic Chunks examples',
    'Foto/video Speak About Round 4 (todas las capas)',
    'Notas POR ESTUDIANTE: anchors/connectors/B2 words/chunks usados',
    'Lista escrita de chunks especificos de cada estudiante (banco personal)',
    'Papel errores fisico (anonimo)',
    'Tu libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA a coordinacion: estudiantes con 2 strikes consecutivos',
    'Notas sobre como recibieron el cambio GoldList -> Frase del Dia',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_c9_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE LISTA NOMINAL de no-entregas Cl 8',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (no anonimo)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE la Frase del Dia al inicio con coro 3x',
    'INSERTE la Frase del Dia NATURALMENTE 3+ veces durante la clase',
    'AL CIERRE: 1 estudiante la dijo + 1 la uso en nueva oracion',
    'COMUNIQUE el cierre del ritual GoldList sin drama',
    'NO use GoldList ni mencione Lista 9 en clase',
    'Mantuve ANCHORS + CONNECTORS + Q&A 5 patterns visibles en tablero',
    'Conduje Vocalizacion con 3-4 trabalenguas NUEVOS',
    'Presente 6 palabras B2 SET #2 con pronunciacion + ejemplo',
    'Conduje TOPIC-SPECIFIC CHUNKS - cada estudiante construyo 6-8 chunks propios',
    'Conduje Speak About R4 con todas las capas integradas (R4 = mas bar que R3)',
    'Lance pregunta hostil a cada estudiante post-presentacion',
    'Anote por estudiante: anchors/connectors/B2 words/chunks propios usados',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'En Tarea explique pedagogicamente el por que (39 dias hasta Final)',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay estudiantes con 2 strikes',
    'Anuncie Layer 5 (Discourse Markers + Intonation) para Cl 10',
]

build_report_v2(
    os.path.join(B2_REP, 'B2_PM_Amina_Clase9_REPORTE.pdf'),
    'B2 PM AMINA | Cl 9 de 36 | FASE 2 DIA 4/7 | TOPIC CHUNKS + B2 SET #2 + FRASE DEL DIA (Goldlist retirado)',
    'TOPIC-SPECIFIC VOCABULARY CHUNKS (cada estudiante construye su banco) + Academic B2 SET #2 (6 nuevas: undermine/exacerbate/alleviate/ubiquitous/scrutinize/advocate) + Speak About R4 todas las capas + cierre ritual GoldList sin drama + FRASE DEL DIA primer dia + TEMPLANZA dia 4 v1',
    b2_c9_act, b2_c9_deliv, b2_c9_eval, S,
)
print('OK: B2_PM_Amina_Clase9_REPORTE.pdf')

print('\n4 PDFs generados para jueves 14/05 noche:')
print('  - A1/A1_Class26_GUIA.pdf')
print('  - A1/reportes/A1_Class26_REPORTE.pdf')
print('  - B2/B2_PM_Amina_Clase9_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase9_REPORTE.pdf')
