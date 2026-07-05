#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 28 (lunes 18/05/2026):
- M28 The Superlative ("You're the Best!") + Frase del Dia + virtud TEMPLANZA v2
- Cierra el trio comparativo M26 (equal) -> M27 (unequal) -> M28 (superlative)
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class28_PRINT.md'), os.path.join(A2_DIR, 'A2_Class28_GUIA.pdf'))
print('OK: A2_Class28_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 27 = M27)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Templanza + M28)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 27)', '7 min'),
    ('LIBRO M28 - The Superlative + vocabulario', '15 min'),
    ('SPEED DRILL - formacion del superlativo', '15 min'),
    ('SIMULACION PROFESIONAL - The Annual Team Awards (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio M29', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M28 3 reglas + vocab',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Annual Team Awards',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 27',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 27 M27)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 28 = TEMPLANZA v2 (por numero de clase)',
    'Hile TEMPLANZA en VATS con superlativo',
    'Cubri M28 The Superlative DESDE EL LIBRO (pag 253-255)',
    'Ensene las 3 reglas (THE -est / THE most / irregulares) sin "than"',
    'Conduje Speed Drill 15 adjetivos en coro rapido',
    'Conduje Simulacion The Annual Team Awards con superlativos reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M29 Degrees of Adjectives para martes',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class28_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 28 de 55 | M28 THE SUPERLATIVE | TEMPLANZA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M28 The Superlative (the -est / the most / the best-worst) + cierre del trio comparativo + The Annual Team Awards + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class28_REPORTE.pdf')

print('\n2 PDFs generados para lunes 18/05 A2 PM Cl 28:')
print('  - A2/A2_Class28_GUIA.pdf')
print('  - A2/reportes/A2_Class28_REPORTE.pdf')
