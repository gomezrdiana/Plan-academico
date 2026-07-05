#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 31 (jueves 21/05/2026):
- M32 How Many People Are There? (Specifying Countable Quantities) + Frase del Dia + virtud JUSTICIA v2 (dia 1/nuevo bloque)
- Pasa de medir el nivel de una cualidad (M30) a contar cantidad de cosas contables (M32)
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA: Module 31 NO existe en el libro -> Cl 31 ejecuta M32 (salto M30->M32->M33 re-confirmado).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class31_PRINT.md'), os.path.join(A2_DIR, 'A2_Class31_GUIA.pdf'))
print('OK: A2_Class31_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 30 = M30)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia + M32)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 30)', '7 min'),
    ('LIBRO M32 - How many + vocabulario (pag 273-282)', '15 min'),
    ('SPEED DRILL - how many + respuesta (numero/people/many/a few)', '15 min'),
    ('SIMULACION PROFESIONAL - The Inventory Count (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio M33', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M32 how many + vocab',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Inventory Count',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 30',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 30 M30)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 31 = JUSTICIA v2 (dia 1/nuevo bloque, por numero de clase)',
    'Hile JUSTICIA en VATS con el patron how many (contar a cuantos sirves)',
    'Cubri M32 How Many People Are There DESDE EL LIBRO (pag 273-282)',
    'Ensene how many + ayudante + respuesta (numero / people irregular / many / a few)',
    'Conduje Speed Drill 15 items how many + respuesta en coro rapido',
    'Conduje Simulacion The Inventory Count con how many reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M33 How Much Money Do You Have para viernes (Module 31 NO existe - salto re-confirmado)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class31_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 31 de 55 | M32 HOW MANY PEOPLE ARE THERE | JUSTICIA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M32 How Many People Are There? (how many + ayudante / respuesta con numero, people irregular, many/a lot of, a few) + paso de medir nivel a contar cantidad contable + The Inventory Count + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class31_REPORTE.pdf')

print('\n2 PDFs generados para jueves 21/05 A2 PM Cl 31:')
print('  - A2/A2_Class31_GUIA.pdf')
print('  - A2/reportes/A2_Class31_REPORTE.pdf')
