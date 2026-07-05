#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera 3 guias + 3 reportes para clases nocturnas del miercoles 13/05/2026:
- A1 Cl 25 (Christian) - M28 Where Is It Prepositions + Depuracion Lista 2
- A2 Cl 25 (Tomas)     - M27 Unequal Comparatives + Depuracion Lista 2
- B2 Amina Cl 8         - Fase 2 dia 3/7 + Q&A Handling NUEVO + Speak About round 3
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A2_DIR = os.path.join(D, 'A2')
B2_DIR = os.path.join(D, 'B2')
A1_REP = os.path.join(A1_DIR, 'reportes')
A2_REP = os.path.join(A2_DIR, 'reportes')
B2_REP = os.path.join(B2_DIR, 'reportes')
for r in (A1_REP, A2_REP, B2_REP):
    os.makedirs(r, exist_ok=True)

# ============================================================
# A1 Cl 25 - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(A1_DIR, 'A1_Class25_PRINT.md'),
    os.path.join(A1_DIR, 'A1_Class25_GUIA.pdf'),
)
print('OK: A1_Class25_GUIA.pdf')

a1_c25_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 24)', '7 min'),
    ('LIBRO M28 - Where Is It? Prepositions of Location + vocabulario', '15 min'),
    ('PREPOSITIONS DRILL - movimiento', '15 min'),
    ('SIMULACION "Where is my breakfast?" (DE PIE)', '20 min'),
    ('DEPURACION GOLDLIST LISTA 2 (Modelo D limpio)', '15 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Tarea + Cierre', '11 min'),
]
a1_c25_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero del M28 vocabulary + prepositions',
    'Foto de Lista 2 de TODOS los cuadernos con cruces',
    'Numero de tachadas por estudiante (comparar con Cl 24 Lista 1)',
    'Foto del cuaderno con seccion "D1 of List 2" iniciada',
    'Foto/video de la Simulacion breakfast (DE PIE)',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 24',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Asistencia real / 6 (anota quien falto hoy)',
]
a1_c25_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'NO permiti escritura Lista nueva hoy (Modelo D limpio - solo depuracion Lista 2)',
    'Conduje DEPURACION Lista 2 con el mismo procedimiento de Cl 24',
    'Tome foto de TODAS las Listas 2 con cruces',
    'Conte tachadas por estudiante y compare con Cl 24 Lista 1',
    'ESCRIBI vocabulario M28 + prepositions en tablero ANTES de clase',
    'Cubri M28 Where Is It DESDE EL LIBRO (no inventando)',
    'Hice Prepositions Drill DE PIE con movimiento',
    'Conduje Simulacion breakfast con vocabulario + prepositions integrados',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que (no solo asignar)',
    'NO acepte la excusa "no me da tiempo"',
    'Anote asistencia real y compare con Cl 24',
]

build_report_v2(
    os.path.join(A1_REP, 'A1_Class25_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 25 de 45 | 2 HORAS | M28 + DEPURACION LISTA 2',
    'M28 Where Is It Prepositions of Location + vocabulario food items + Simulacion breakfast + Depuracion Lista 2 (segunda) + Shadowing',
    a1_c25_act, a1_c25_deliv, a1_c25_eval, S,
)
print('OK: A1_Class25_REPORTE.pdf')

# ============================================================
# A2 Cl 25 - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_Class25_PRINT.md'),
    os.path.join(A2_DIR, 'A2_Class25_GUIA.pdf'),
)
print('OK: A2_Class25_GUIA.pdf')

a2_c25_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 24)', '7 min'),
    ('Tarea Check Cl 24', '5 min'),
    ('LIBRO M27 - Unequal Comparatives + vocabulario', '15 min'),
    ('SPEED DRILL - formacion de comparativos (-er than / more...than)', '15 min'),
    ('SIMULACION PROFESIONAL "Two job candidates" (DE PIE)', '20 min'),
    ('DEPURACION GOLDLIST LISTA 2 (Modelo D limpio)', '15 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live', '8 min'),
    ('Tarea + Cierre + anuncio M28', '8 min'),
]
a2_c25_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero del M27 - 2 reglas + vocabulario',
    'Foto de Lista 2 de TODOS los cuadernos con cruces',
    'Numero de tachadas por estudiante (comparar con Cl 24 Lista 1)',
    'Foto del cuaderno con seccion "D1 of List 2" iniciada',
    'Foto/video de la Simulacion Job Candidates (DE PIE)',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 24',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Notas sobre tu energia hoy',
]
a2_c25_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'NO permiti escritura Lista nueva hoy (Modelo D limpio - solo depuracion Lista 2)',
    'Conduje DEPURACION Lista 2 con el mismo procedimiento de Cl 24',
    'Tome foto de TODAS las Listas 2 con cruces',
    'Conte tachadas por estudiante y compare con Cl 24 Lista 1',
    'ESCRIBI 2 reglas M27 (-er than / more...than) + vocabulario en tablero',
    'Cubri M27 Unequal Comparatives DESDE EL LIBRO (no inventando)',
    'Conduje Speed Drill con 15 adjetivos en coro rapido',
    'Conduje Simulacion Job Candidates con comparaciones reales',
    'Simulacion fue PROFESIONAL (no temas familiares ni fantasiosos)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M28 The Superlative para manana',
]

build_report_v2(
    os.path.join(A2_REP, 'A2_Class25_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 25 de 55 | 2 HORAS | M27 + DEPURACION LISTA 2',
    'M27 Unequal Comparatives (more X than / -er than) + vocabulario rich/pretty/ugly/serious/early/late/complicated + Simulacion Two Job Candidates + Depuracion Lista 2 + Shadowing',
    a2_c25_act, a2_c25_deliv, a2_c25_eval, S,
)
print('OK: A2_Class25_REPORTE.pdf')

# ============================================================
# B2 Amina Cl 8 - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase8_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase8_GUIA.pdf'),
)
print('OK: B2_PM_Amina_Clase8_GUIA.pdf')

b2_c8_act = [
    ('MYSTERY HOMEWORK CHECK + LECTURA PUBLICA de quien NO entrego', '5 min'),
    ('EL POR QUE DE HOY', '3 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas NUEVOS - mas volumen)', '6 min'),
    ('VATS TEMPLANZA dia 3 (v1)', '5 min'),
    ('ANCHOR RECAP (drill rapido - mantener Cl 6)', '3 min'),
    ('CONNECTOR RECAP - drill (mantener Cl 7) + bridge formal->casual', '3 min'),
    ('ACADEMIC B2 VOCABULARY BANK - 6 palabras NUEVAS (NUEVO)', '8 min'),
    ('Q&A HANDLING - 5 patterns + drill con preguntas hostiles (NUEVO)', '14 min'),
    ('CONTRASTE TIEMPOS VERBALES drill', '6 min'),
    ('PEER TEACHER SLOT corto (error Cl 7)', '3 min'),
    ('SPEAK ABOUT round 3 - connectors EN MONOLOGO Y Q&A + min 2 B2 words + 1 pregunta hostil', '50 min'),
    ('GOLDLIST Lista 8 - PHRASE EXPOSURE ORAL (no copy en clase)', '5 min'),
    ('ERROR PAPER LIVE', '7 min'),
    ('TAREA STRICT 4 COMPONENTES + CIERRE', '2 min'),
]
b2_c8_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'LISTA NOMINAL de quien NO entrego tarea Cl 7 (no anonimo)',
    'Foto del tablero - ACADEMIC B2 WORDS + Q&A 5 patterns',
    'Foto/video del PEER TEACHER',
    'Foto/video de Speak About round 3 con Q&A hostiles',
    'Notas escritas POR ESTUDIANTE: cuantas anchors / connectors monologo / connectors casual / B2 words usadas',
    'Papel errores fisico (anonimo)',
    'Tu libreta personal con 3 errores literales + NOMBRE por estudiante por bloque',
    'ALERTA a coordinacion: estudiantes con 2 strikes consecutivos (notificar al cierre)',
    'Anotacion sobre quien manejo pregunta hostil con composure vs quien colapso',
]
b2_c8_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad (tu nervios contagia al cohorte)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE LISTA NOMINAL de quien no entrego tarea Cl 7',
    'LEI PUBLICAMENTE los nombres de quien NO entrego (no anonimo)',
    'ESCRIBI ACADEMIC B2 WORDS (6 palabras + ejemplos) en tablero ANTES de clase',
    'ESCRIBI Q&A 5 patterns en tablero ANTES de clase',
    'Mantuve ANCHORS y CONNECTORS de Cl 6 y Cl 7 en tablero',
    'Conduje Vocalizacion Drill con 3-4 trabalenguas NUEVOS (cubriendo distintos sonidos)',
    'Conduje VATS TEMPLANZA dia 3 con prompt apropiado',
    'Presente 6 palabras B2 con pronunciacion + definicion + ejemplo + aplicacion',
    'Lance 5 preguntas hostiles del banco durante Q&A drill',
    'Cohorte voto que pattern uso cada estudiante en Q&A',
    'Conduje Speak About round 3 con MAYOR bar (anchors + connectors monologo + connectors casual + 2 B2 words)',
    'Anote por estudiante: cuantas anchors / connectors monologo / connectors casual / B2 words usadas',
    'Conduje GoldList ORAL (lectura mia + repeticion oral - SIN copiar en clase)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'En Tarea explique pedagogicamente el por que (40 dias hasta Final)',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay estudiantes con 2 strikes',
    'Anuncie Layer 4 (Vocab Chunks) para Cl 9',
]

build_report_v2(
    os.path.join(B2_REP, 'B2_PM_Amina_Clase8_REPORTE.pdf'),
    'B2 PM AMINA | Cl 8 de 36 | FASE 2 DIA 3/7 | 2 CAPAS NUEVAS: ACADEMIC B2 VOCAB BANK + Q&A HANDLING',
    'Academic B2 Vocab Bank 6 palabras (prevalent/substantiate/detrimental/mitigate/inherent/discrepancy) + Q&A Handling 5 patterns + Speak About R3 bridge formal->casual + Vocalizacion 4 trabalenguas + TAREA STRICT 4 componentes + lectura publica no-entregas + TEMPLANZA dia 3 v1',
    b2_c8_act, b2_c8_deliv, b2_c8_eval, S,
)
print('OK: B2_PM_Amina_Clase8_REPORTE.pdf')

print('\n6 PDFs generados:')
print('  - A1/A1_Class25_GUIA.pdf')
print('  - A1/reportes/A1_Class25_REPORTE.pdf')
print('  - A2/A2_Class25_GUIA.pdf')
print('  - A2/reportes/A2_Class25_REPORTE.pdf')
print('  - B2/B2_PM_Amina_Clase8_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase8_REPORTE.pdf')
