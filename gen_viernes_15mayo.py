#!/usr/bin/env python3
"""Genera PDFs para clases del viernes 15/05/2026:
- B1 Cl 13 Conv (Danna, primero)
- B1 Cl 13 Grammar (Juan Diego, segundo) + texto Heiiu estudiante PDF
- A2 4hr AM Cl 18 (Tomas) - M39 + M41 + Frase del Dia
TODO sin GoldList (eliminado 14/05/2026)
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
B1_DIR = os.path.join(D, 'B1')
A2_REP = os.path.join(A2_DIR, 'reportes')
B1_REP = os.path.join(B1_DIR, 'reportes')
for r in (A2_REP, B1_REP):
    os.makedirs(r, exist_ok=True)

# ============================================================
# B1 Cl 13 Conv (Danna)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase13_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase13_CONV_GUIA.pdf'),
)
print('OK: B1_Clase13_CONV_GUIA.pdf')

b1_c13_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS JUSTICIA dia 3 (v1)', '7 min'),
    ('PEER TEACHER SLOT (errores Cl 12 Conv de tu libreta)', '7 min'),
    ('HOT TOPIC - What Have I Learned This Week?', '17 min'),
    ('SIMULACION - My English Story mini-presentation (DE PIE)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 12 - NARRATIVE Draft 2 (escritura en clase anti-fraude)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '8 min'),
    ('Error Paper Live + Frase del Dia CIERRE + PASE a Juan Diego + Tarea + Cierre', '7 min'),
]
b1_c13_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + Hot Topic requirements',
    'Foto/video del PEER TEACHER',
    'Foto/video de My English Story simulation',
    'Foto/video Mini-Pitch',
    '16 Paginas 12 NARRATIVE DRAFT 2 (foto - escritura en clase)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre los 2 estudiantes en riesgo (Yuli + Vanessa) en My English Story',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
b1_c13_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni menciono Lista (ritual cerrado)',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'Conduje Hot Topic con requirements en tablero',
    'Conduje My English Story con todos los tiempos del nivel',
    'Conduje escritura Page 12 EN CLASE (anti-fraude IA)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'Camine con papel errores anonimo',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGARE FISICAMENTE el PASE a Juan Diego ANTES de su clase',
    'En Tarea explique pedagogicamente el por que',
    'NO acepte la excusa "no me da tiempo"',
    'Anote evidencia especifica de los 2 estudiantes en riesgo',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase13_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 13 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | FRASE DEL DIA (Goldlist retirado)',
    'My English Story mini-presentation + Hot Topic semanal + Page 12 NARRATIVE Draft 2 anti-fraude + FRASE DEL DIA + PASE a Juan Diego + JUSTICIA dia 3',
    b1_c13_c_act, b1_c13_c_deliv, b1_c13_c_eval, S,
)
print('OK: B1_Clase13_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 13 Grammar (Juan Diego) - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase13_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase13_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase13_GRAMMAR_GUIA.pdf')

# Texto Heiiu Cl 13 ESTUDIANTE
md_to_pdf(
    os.path.join(B1_DIR, 'B1_TEXTO_HEIIU_Cl13_TimeAndEnglish_ESTUDIANTE.md'),
    os.path.join(B1_DIR, 'B1_TEXTO_HEIIU_Cl13_TimeAndEnglish_ESTUDIANTE.pdf'),
)
print('OK: B1_TEXTO_HEIIU_Cl13_TimeAndEnglish_ESTUDIANTE.pdf')

b1_c13_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '4 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS JUSTICIA dia 3 (v1)', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna)', '7 min'),
    ('LIBRO M16 - Present Perfect Irregular + lista 30 V3', '15 min'),
    ('LIBRO M17 - Present Perfect vs Past Simple', '13 min'),
    ('EJERCICIO IDENTIFY-THE-TENSE con texto Heiiu Cl 13', '20 min'),
    ('LISTENING + ANALISIS del texto Heiiu (profe lee en voz alta)', '12 min'),
    ('SPEED DRILL - Present Perfect Irregular oraciones', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '10 min'),
    ('PASE ESCRITO a Danna + Tarea + Cierre', '8 min'),
]
b1_c13_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - Frase del Dia + M16 lista V3 + M17 comparison',
    'Foto/video del PEER TEACHER usando PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto de 4-5 textos Heiiu ESTUDIANTE con tabla identify-the-tense completada',
    'Foto/video del Listening con ojos cerrados',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 12',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre cuantas veces lograste insertar Frase del Dia',
    'Notas sobre que tiempos costaron mas identificar en el texto',
]
b1_c13_g_eval = [
    'Lei la guia COMPLETA + ANEXO PROFESOR al menos 1 hora antes',
    'Lei el texto Heiiu en voz alta UNA vez antes de clase (practica ritmo)',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'Cubri M16 Present Perfect Irregular con lista 30 V3 DESDE EL LIBRO',
    'Cubri M17 Present Perfect vs Past Simple con regla clara DESDE EL LIBRO',
    'NO ensene Past Perfect formal (solo PREVIEW como B2 en el texto)',
    'NO ensene Third Conditional ni modales perfectos',
    'Imprimi 17 copias del texto Heiiu Cl 13 ESTUDIANTE',
    'Entregue 1 copia por estudiante',
    'Conduje ejercicio identify-the-tense con tabla de categorizacion',
    'Conduje Listening con ojos cerrados (estudiantes notando ritmo de tiempos)',
    'Conduje Speed Drill con 15 verbos irregulares en coro rapido',
    'En libreta personal anote 3 errores con NOMBRE',
    'Camine con papel errores anonimo',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'En Tarea explique pedagogicamente el por que',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M18 Passive Voice para Cl 14 lunes',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase13_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 13 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO) | M16 + M17 + TEXTO HEIIU IDENTIFY-THE-TENSE',
    'A2 Book M16 Present Perfect Irregular (30 V3) + M17 PP vs Past Simple + Texto Heiiu Cl 13 "What Time Has Taught Me" (cubre TODOS los tiempos + preview Past Perfect B2) + Identify-the-Tense exercise + Listening con ojos cerrados + FRASE DEL DIA (Goldlist retirado) + JUSTICIA dia 3',
    b1_c13_g_act, b1_c13_g_deliv, b1_c13_g_eval, S,
)
print('OK: B1_Clase13_GRAMMAR_REPORTE.pdf')

# ============================================================
# A2 4hr Cl 18 (Tomas)
# ============================================================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class18_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Class18_GUIA.pdf'),
)
print('OK: A2_4h_Class18_GUIA.pdf')

a2_4h_c18_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion (NUEVO ritual)', '4 min'),
    ('CIERRE RITUAL GOLDLIST (anuncio sin drama)', '2 min'),
    ('VATS FORTALEZA dia 3 (v1)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 17)', '7 min'),
    ('Tarea Check Cl 17', '5 min'),
    ('LIBRO M39 - Possessive Pronouns + Speed Drill', '20 min'),
    ('SIMULACION M39 - Lost and Found (DE PIE)', '25 min'),
    ('LIBRO M41 - -ED vs -ING adjectives + ejemplos', '25 min'),
    ('Historia interactiva M41 - The most interesting/boring movie', '10 min'),
    ('SIMULACION INTEGRADA M39+M41 - Whose Feelings Are These? (DE PIE)', '30 min'),
    ('SHADOWING DIA 2 nuevo ciclo', '12 min'),
    ('Free production M39+M41 (parejas DE PIE)', '18 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 19 lunes', '17 min'),
]
a2_4h_c18_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto del tablero - FRASE DEL DIA + M39 + M41 tablas',
    'Foto/video del PEER TEACHER',
    'Foto/video Lost and Found simulacion',
    'Foto/video Whose Feelings Are These (integrada M39+M41)',
    'Foto/video Free Production',
    'Foto/video Shadowing Dia 2 nuevo ciclo',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 17',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Notas sobre como recibieron el cambio GoldList -> Frase del Dia',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_4h_c18_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE durante clase',
    'COMUNIQUE el cierre del ritual GoldList sin drama (2 min)',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'ESCRIBI M39 Possessive Pronouns tabla + M41 -ED/-ING tabla ANTES de clase',
    'Cubri M39 Mine All Mine DESDE EL LIBRO (saltando M40)',
    'Cubri M41 -ED vs -ING adjectives DESDE EL LIBRO',
    'Hice INTEGRACION M39+M41 en Whose Feelings Are These',
    'Conduje Shadowing DIA 2 del nuevo ciclo (no Dia 1)',
    'Simulaciones fueron PROFESIONALES/realistas',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M42 Getting Crazy para Cl 19 lunes + Shadowing Dia 3 mini-competencia',
    'Anote feedback sobre el cambio del ritual',
]

build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class18_REPORTE.pdf'),
    'A2 INTENSIVO | Cl 18 de 28 | M39 + M41 (saltando M40) + FRASE DEL DIA NUEVO RITUAL (Goldlist retirado)',
    'M39 Mine All Mine (Possessive Pronouns) + M41 -ED vs -ING adjectives + Lost and Found + Whose Feelings Are These integrated + Shadowing Dia 2 nuevo ciclo + FRASE DEL DIA primer dia + cierre ritual GoldList sin drama + FORTALEZA dia 3 v1',
    a2_4h_c18_act, a2_4h_c18_deliv, a2_4h_c18_eval, S,
)
print('OK: A2_4h_Class18_REPORTE.pdf')

print('\n5 PDFs generados para viernes 15/05:')
print('  - B1/B1_Clase13_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase13_CONV_REPORTE.pdf')
print('  - B1/B1_Clase13_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase13_GRAMMAR_REPORTE.pdf')
print('  - B1/B1_TEXTO_HEIIU_Cl13_TimeAndEnglish_ESTUDIANTE.pdf')
print('  - A2/A2_4h_Class18_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class18_REPORTE.pdf')
