#!/usr/bin/env python3
"""Genera la guia + reporte del A1 Nocturno 2H Cl 31 (jueves 21/05/2026):
- M34 Usually, but not Today (Present Simple vs. Present Continuous) + Frase del Dia + virtud JUSTICIA v2 (dia 1, apertura de bloque)
- Continua despues de M33 "The Present Continuous" (Cl 30); profesor Christian, cohorte de 6.
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

md_to_pdf(os.path.join(A1_DIR, 'A1_Class31_PRINT.md'), os.path.join(A1_DIR, 'A1_Class31_GUIA.pdf'))
print('OK: A1_Class31_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 30 = M33 be + verbo -ing)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia + M34)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 30)', '7 min'),
    ('LIBRO M34 - usually vs. today + reglas', '20 min'),
    ('USUALLY/TODAY DRILL - simple vs. continuo en movimiento', '15 min'),
    ('SIMULACION - The Fair Schedule Swap (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M34 usually vs. today',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Fair Schedule Swap',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 30',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 30 M33)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 31 = JUSTICIA v2 dia 1 apertura de bloque (por numero de clase)',
    'Hile JUSTICIA en VATS con usually vs. today (lo que hago siempre vs. hoy, justo)',
    'Cubri M34 "Present Simple vs. Present Continuous" DESDE EL LIBRO (pag 395-402)',
    'Ensene usually (simple) vs. today (continuo) (afirm/neg/preg) + elegir el tiempo correcto',
    'Hice Usually/Today Drill DE PIE con habito vs. accion de hoy',
    'Conduje Simulacion The Fair Schedule Swap con simple vs. continuo',
    'Simulacion fue COTIDIANA/PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M35 para el viernes (Cl 32)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class31_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 31 de 45 | M34 PRESENT SIMPLE vs. CONTINUOUS | JUSTICIA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M34 Usually, but not Today - Present Simple vs. Present Continuous + Simulacion The Fair Schedule Swap + FRASE DEL DIA',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class31_REPORTE.pdf')

print('\n2 PDFs generados para jueves 21/05 A1 Nocturno Cl 31:')
print('  - A1/A1_Class31_GUIA.pdf')
print('  - A1/reportes/A1_Class31_REPORTE.pdf')
