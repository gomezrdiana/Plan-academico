#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 29 (martes 19/05/2026):
- M29 Degrees of Adjectives ("How Tall Are You?") + Frase del Dia + virtud TEMPLANZA v2
- Pasa de comparar (M26-M28) a graduar UNA cualidad con "How+adj" + intensificador
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class29_PRINT.md'), os.path.join(A2_DIR, 'A2_Class29_GUIA.pdf'))
print('OK: A2_Class29_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 28 = M28)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Templanza + M29)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 28)', '7 min'),
    ('LIBRO M29 - Degrees of Adjectives + vocabulario', '15 min'),
    ('SPEED DRILL - pregunta How+adj + intensificador', '15 min'),
    ('SIMULACION PROFESIONAL - The Reference Call (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio M30', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M29 How+adj + 6 intensificadores + vocab',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Reference Call',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 28',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 28 M28)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 29 = TEMPLANZA v2 (por numero de clase)',
    'Hile TEMPLANZA en VATS con el patron How+adj + intensificador',
    'Cubri M29 Degrees of Adjectives DESDE EL LIBRO (pag 260-263)',
    'Ensene la pregunta How+adj + los 6 intensificadores sin comparativo ni "than"',
    'Conduje Speed Drill 15 items pregunta How+adj en coro rapido',
    'Conduje Simulacion The Reference Call con intensificadores reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M30 Too Much or Just Enough para miercoles',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class29_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 29 de 55 | M29 DEGREES OF ADJECTIVES | TEMPLANZA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M29 Degrees of Adjectives (How+adj + really/very/kinda/sorta/pretty/not very) + paso de comparar a graduar + The Reference Call + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class29_REPORTE.pdf')

print('\n2 PDFs generados para martes 19/05 A2 PM Cl 29:')
print('  - A2/A2_Class29_GUIA.pdf')
print('  - A2/reportes/A2_Class29_REPORTE.pdf')
