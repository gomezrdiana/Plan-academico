#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 32 (viernes 22/05/2026):
- M35 "Going to" and "Gonna" - Another Form of the Future + Frase del Dia + virtud JUSTICIA v2 (dia 2)
- Continua despues de M34 "Usually, but not Today" (Cl 31); profesor Christian, cohorte de 6.
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

md_to_pdf(os.path.join(A1_DIR, 'A1_Class32_PRINT.md'), os.path.join(A1_DIR, 'A1_Class32_GUIA.pdf'))
print('OK: A1_Class32_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 31 = M34 usually vs. today)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia + M35)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 31)', '7 min'),
    ('LIBRO M35 - going to / gonna + reglas', '20 min'),
    ('GOING TO DRILL - el futuro en movimiento', '15 min'),
    ('SIMULACION - The Fair Plan Meeting (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M35 going to / gonna',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Fair Plan Meeting',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 31',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 31 M34)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 32 = JUSTICIA v2 dia 2 (por numero de clase)',
    'Hile JUSTICIA en VATS con going to (a quien voy a agradecer / ayudar, justo)',
    'Cubri M35 "Going to and Gonna" DESDE EL LIBRO (pag 403-413)',
    'Ensene be + going to + verbo base (afirm/neg/preg) + gonna como forma hablada',
    'Hice Going To Drill DE PIE con planes y promesas a futuro',
    'Conduje Simulacion The Fair Plan Meeting con going to',
    'Simulacion fue COTIDIANA/PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M36 para el lunes (Cl 33)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class32_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 32 de 45 | M35 GOING TO / GONNA | JUSTICIA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M35 "Going to" and "Gonna" - Another Form of the Future + Simulacion The Fair Plan Meeting + FRASE DEL DIA',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class32_REPORTE.pdf')

print('\n2 PDFs generados para viernes 22/05 A1 Nocturno Cl 32:')
print('  - A1/A1_Class32_GUIA.pdf')
print('  - A1/reportes/A1_Class32_REPORTE.pdf')
