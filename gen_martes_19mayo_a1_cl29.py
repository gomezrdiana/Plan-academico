#!/usr/bin/env python3
"""Genera la guia + reporte del A1 Nocturno 2H Cl 29 (martes 19/05/2026):
- M32 Diego Was Sick Yesterday ("Be" in the Simple Past) + Frase del Dia + virtud TEMPLANZA v2
- Continua despues de M31 The Existence of Things (Cl 28); profesor Christian, cohorte de 6.
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class29_PRINT.md'), os.path.join(A1_DIR, 'A1_Class29_GUIA.pdf'))
print('OK: A1_Class29_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 28 = M31 there is/are + some/any)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Templanza + M32)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 28)', '7 min'),
    ('LIBRO M32 - was/were + marcadores + vocabulario', '20 min'),
    ('PAST DRILL - was/were en movimiento', '15 min'),
    ('SIMULACION - The Shift Report (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M32 was-were + marcadores',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Shift Report',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 28',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 28 M31)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 29 = TEMPLANZA v2 (por numero de clase)',
    'Hile TEMPLANZA en VATS con was/were (ayer: lo que fue y lo que no fue)',
    'Cubri M32 "Be" in the Simple Past DESDE EL LIBRO (pag 359-374)',
    'Ensene was/were (afirm/neg/preg) + respuestas cortas + marcadores de tiempo',
    'Hice Past Drill DE PIE con momentos reales (ayer/semana pasada)',
    'Conduje Simulacion The Shift Report con was/were + marcadores',
    'Simulacion fue COTIDIANA/PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M33 para el miercoles (Cl 30)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class29_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 29 de 45 | M32 "BE" IN THE SIMPLE PAST | TEMPLANZA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M32 Diego Was Sick Yesterday - "Be" in the Simple Past (was/were) + Simulacion The Shift Report + FRASE DEL DIA',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class29_REPORTE.pdf')

print('\n2 PDFs generados para martes 19/05 A1 Nocturno Cl 29:')
print('  - A1/A1_Class29_GUIA.pdf')
print('  - A1/reportes/A1_Class29_REPORTE.pdf')
