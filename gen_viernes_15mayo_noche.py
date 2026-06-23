#!/usr/bin/env python3
"""Genera 6 PDFs para clases nocturnas del viernes 15/05/2026 (SIN GoldList - Frase del Dia):
- A1 Cl 27 (Christian)   - M30 The Possessive Case + Frase del Dia
- A2 PM Cl 27 (Tomas)    - M27 Unequal Comparatives + Frase del Dia (post-midterm)
- B2 Amina Cl 10         - Discourse Markers + Intonation Layer 5 + B2 Set #3 + Frase del Dia
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A1_DIR = os.path.join(D, 'A1'); A2_DIR = os.path.join(D, 'A2'); B2_DIR = os.path.join(D, 'B2')
A1_REP = os.path.join(A1_DIR, 'reportes'); A2_REP = os.path.join(A2_DIR, 'reportes'); B2_REP = os.path.join(B2_DIR, 'reportes')
for r in (A1_REP, A2_REP, B2_REP):
    os.makedirs(r, exist_ok=True)

# ===== A1 Cl 27 =====
md_to_pdf(os.path.join(A1_DIR, 'A1_Class27_PRINT.md'), os.path.join(A1_DIR, 'A1_Class27_GUIA.pdf'))
print('OK: A1_Class27_GUIA.pdf')
a1_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 26)', '7 min'),
    ('LIBRO M30 - The Possessive Case + vocabulario', '20 min'),
    ('POSSESSIVE DRILL - apostrofe S en movimiento', '15 min'),
    ('SIMULACION - Whose Is This? Lost objects party (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M30 Possessive',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion Whose Is This',
    'Foto/video Shadowing', 'Papel errores fisico',
    'Lista quienes NO entregaron tarea Cl 26',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Cubri M30 The Possessive Case DESDE EL LIBRO',
    'Hice Possessive Drill DE PIE con objetos reales',
    'Conduje Simulacion Whose Is This con WHOSE + apostrofe S',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que',
    'NO acepte la excusa "no me da tiempo"',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class27_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 27 de 45 | M30 THE POSSESSIVE CASE | FRASE DEL DIA (Goldlist retirado)',
    'M30 When Is Juan Birthday - The Possessive Case (apostrofe S) + Simulacion Whose Is This + FRASE DEL DIA',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class27_REPORTE.pdf')

# ===== A2 PM Cl 27 =====
md_to_pdf(os.path.join(A2_DIR, 'A2_Class27_PRINT.md'), os.path.join(A2_DIR, 'A2_Class27_GUIA.pdf'))
print('OK: A2_Class27_GUIA.pdf')
a2_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 24)', '7 min'),
    ('LIBRO M27 - Unequal Comparatives + vocabulario', '15 min'),
    ('SPEED DRILL - formacion de comparativos', '15 min'),
    ('SIMULACION PROFESIONAL - Two Job Candidates (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio M28', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M27 2 reglas + vocab',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion Two Job Candidates',
    'Foto/video Shadowing', 'Papel errores fisico',
    'Lista quienes NO entregaron tarea Cl 24',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Cubri M27 Unequal Comparatives DESDE EL LIBRO (pag 247)',
    'Conduje Speed Drill 15 adjetivos en coro rapido',
    'Conduje Simulacion Two Job Candidates con comparaciones reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M28 The Superlative para lunes',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class27_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 27 de 55 | M27 UNEQUAL COMPARATIVES | POST-MIDTERM | FRASE DEL DIA (Goldlist retirado)',
    'M27 Unequal Comparatives (-er than / more...than / irregulares) + Two Job Candidates + retoma post-midterm + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class27_REPORTE.pdf')

# ===== B2 Amina Cl 10 =====
md_to_pdf(os.path.join(B2_DIR, 'B2_PM_Amina_Clase10_PRINT.md'), os.path.join(B2_DIR, 'B2_PM_Amina_Clase10_GUIA.pdf'))
print('OK: B2_PM_Amina_Clase10_GUIA.pdf')
b2_act = [
    ('MYSTERY + LECTURA PUBLICA no-entregas', '5 min'),
    ('EL POR QUE DE HOY', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VOCALIZACION DRILL (3-4 trabalenguas nuevos)', '6 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('RECAP EXPRESS - Anchors + Connectors + Q&A + Chunks', '5 min'),
    ('ACADEMIC B2 VOCAB SET #3 (6 palabras nuevas)', '8 min'),
    ('DISCOURSE MARKERS + INTONATION - Layer 5 (NUEVO)', '17 min'),
    ('PEER TEACHER SLOT corto', '3 min'),
    ('SPEAK ABOUT R5 - todas las capas + discourse markers + intonation', '50 min'),
    ('FRASE DEL DIA cierre + Discourse Marker check', '5 min'),
    ('ERROR PAPER LIVE', '7 min'),
    ('TAREA STRICT 4 componentes + CIERRE', '2 min'),
]
b2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'LISTA NOMINAL no-entregas Cl 9',
    'Foto del tablero - Frase del Dia + B2 Set #3 + Discourse Markers',
    'Foto/video Speak About R5 (todas las capas + intonation)',
    'Notas POR ESTUDIANTE: discourse markers / intonation / B2 words / chunks',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por estudiante',
    'ALERTA coordinacion: estudiantes con 2 strikes (notificar al cierre)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b2_eval = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PROYECTE seguridad', 'PREPARE el SOBRE del Mystery ANTES',
    'PREPARE LISTA NOMINAL no-entregas Cl 9',
    'LEI PUBLICAMENTE los nombres de quien NO entrego',
    'ESCRIBI Frase del Dia + B2 Set #3 + Discourse Markers en tablero ANTES',
    'PRESENTE Frase del Dia con intonacion modelada + coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE con intonacion',
    'NO use GoldList (ritual cerrado)',
    'Mantuve Anchors + Connectors + Q&A patterns + Chunks visibles',
    'Conduje Vocalizacion 3-4 trabalenguas NUEVOS',
    'Presente 6 palabras B2 Set #3 con pronunciacion + ejemplo',
    'Ensene Discourse Markers (7 categorias) + Intonation (rising/falling/contrastive/pause)',
    'Conduje Speak About R5 con TODAS las capas + intonation consciente',
    'Lance pregunta hostil a cada estudiante post-presentacion',
    'Anote por estudiante: discourse markers / intonation / B2 words / chunks',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'En Tarea explique pedagogicamente el por que (38 dias hasta Final)',
    'NO acepte la excusa "no me da tiempo"',
    'Notifique a coordinacion al cierre si hay 2 strikes',
    'Anuncie Layer 6 (Repetition/Paraphrasing) para Cl 11',
]
build_report_v2(os.path.join(B2_REP, 'B2_PM_Amina_Clase10_REPORTE.pdf'),
    'B2 PM AMINA | Cl 10 de 36 | FASE 2 DIA 5/7 | DISCOURSE MARKERS + INTONATION (Layer 5) + B2 SET #3 | FRASE DEL DIA (Goldlist retirado)',
    'Discourse Markers (7 categorias) + Intonation (rising/falling/contrastive/pause) + Academic B2 Set #3 (pivotal/contentious/ambivalent/conducive/plausible/nuanced) + Speak About R5 todas las capas + FRASE DEL DIA',
    b2_act, b2_deliv, b2_eval, S)
print('OK: B2_PM_Amina_Clase10_REPORTE.pdf')

print('\n6 PDFs generados para viernes 15/05 noche:')
print('  - A1/A1_Class27_GUIA.pdf + reporte')
print('  - A2/A2_Class27_GUIA.pdf + reporte')
print('  - B2/B2_PM_Amina_Clase10_GUIA.pdf + reporte')
