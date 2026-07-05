#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 28 (lunes 18/05/2026):
- M31 Is There Any Bread? (The Existence of Things) + Frase del Dia + virtud TEMPLANZA v2
- Continua despues de M30 The Possessive Case (Cl 27); profesor Christian, cohorte de 6.
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class28_PRINT.md'), os.path.join(A1_DIR, 'A1_Class28_GUIA.pdf'))
print('OK: A1_Class28_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 27 = M30 possessive)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Templanza + M31)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 27)', '7 min'),
    ('LIBRO M31 - There is/are + some/any + vocabulario', '20 min'),
    ('EXISTENCE DRILL - there is/are en movimiento', '15 min'),
    ('SIMULACION - The Kitchen Inventory (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M31 There is-are + some-any',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Kitchen Inventory',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 27',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 27 M30)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 28 = TEMPLANZA v2 (por numero de clase)',
    'Hile TEMPLANZA en VATS con there is/are (lo que hay y lo que falta)',
    'Cubri M31 The Existence of Things DESDE EL LIBRO (pag 343-348)',
    'Ensene there is/are + some/any (afirm/neg/preg) + respuestas cortas',
    'Hice Existence Drill DE PIE con este salon reales',
    'Conduje Simulacion The Kitchen Inventory con there is/are + some/any',
    'Simulacion fue COTIDIANA/PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M32 para el martes (Cl 29)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class28_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 28 de 45 | M31 THE EXISTENCE OF THINGS | TEMPLANZA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M31 Is There Any Bread - The Existence of Things (there is/are + some/any) + Simulacion The Kitchen Inventory + FRASE DEL DIA',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class28_REPORTE.pdf')

print('\n2 PDFs generados para lunes 18/05 A1 Nocturno Cl 28:')
print('  - A1/A1_Class28_GUIA.pdf')
print('  - A1/reportes/A1_Class28_REPORTE.pdf')
