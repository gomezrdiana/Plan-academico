#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 30 (miercoles 20/05/2026):
- M33 What Are You Doing? (The Present Continuous) + Frase del Dia + virtud TEMPLANZA v2 (dia 5, cierre de bloque)
- Continua despues de M32 "Be" in the Simple Past (Cl 29); profesor Christian, cohorte de 6.
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

md_to_pdf(os.path.join(A1_DIR, 'A1_Class30_PRINT.md'), os.path.join(A1_DIR, 'A1_Class30_GUIA.pdf'))
print('OK: A1_Class30_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 29 = M32 was/were + marcadores)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Templanza + M33)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 29)', '7 min'),
    ('LIBRO M33 - be + verbo -ing + vocabulario', '20 min'),
    ('CONTINUOUS DRILL - be + -ing en movimiento', '15 min'),
    ('SIMULACION - The Live Update Call (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M33 be + verbo -ing',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Live Update Call',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 29',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 29 M32)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 30 = TEMPLANZA v2 dia 5 cierre de bloque (por numero de clase)',
    'Hile TEMPLANZA en VATS con be + verbo -ing (lo que hago AHORA con calma)',
    'Cubri M33 "The Present Continuous" DESDE EL LIBRO (pag 375-382)',
    'Ensene be + verbo -ing (afirm/neg/preg) + respuestas cortas + simple vs continuo',
    'Hice Continuous Drill DE PIE con acciones reales (ahora mismo)',
    'Conduje Simulacion The Live Update Call con be + verbo -ing',
    'Simulacion fue COTIDIANA/PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M34 para el jueves (Cl 31)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class30_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 30 de 45 | M33 THE PRESENT CONTINUOUS | TEMPLANZA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M33 What Are You Doing? - The Present Continuous (be + verbo -ing) + Simulacion The Live Update Call + FRASE DEL DIA',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class30_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 20/05 A1 Nocturno Cl 30:')
print('  - A1/A1_Class30_GUIA.pdf')
print('  - A1/reportes/A1_Class30_REPORTE.pdf')
