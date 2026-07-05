#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 30 (miercoles 20/05/2026):
- M30 Too Much or Just Enough? (Required Levels) + Frase del Dia + virtud TEMPLANZA v2 (dia 5/ultimo del bloque)
- Pasa de graduar libre (M29) a decidir el nivel requerido con enough/so/too
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA: Module 31 NO existe en el libro -> Cl 31 se anuncia con M32 (salto confirmado).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class30_PRINT.md'), os.path.join(A2_DIR, 'A2_Class30_GUIA.pdf'))
print('OK: A2_Class30_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 29 = M29)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Templanza + M30)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 29)', '7 min'),
    ('LIBRO M30 - Required Levels (enough/so/too) + vocabulario', '15 min'),
    ('SPEED DRILL - enough / so / too sobre descriptores', '15 min'),
    ('SIMULACION PROFESIONAL - The Fit Check (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio M32', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M30 enough/so/too + vocab',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Fit Check',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 29',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 29 M29)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 30 = TEMPLANZA v2 (dia 5/ultimo del bloque, por numero de clase)',
    'Hile TEMPLANZA en VATS con el patron enough/so/too (el nivel JUSTO)',
    'Cubri M30 Too Much or Just Enough? DESDE EL LIBRO (pag 266-272)',
    'Ensene enough (despues del adj) + so (alto/bueno) + too (excesivo) sin comparativo ni "than"',
    'Conduje Speed Drill 15 items enough/so/too en coro rapido',
    'Conduje Simulacion The Fit Check con enough/so/too reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M32 How Many People Are There para jueves (Module 31 NO existe - salto confirmado)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class30_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 30 de 55 | M30 TOO MUCH OR JUST ENOUGH | TEMPLANZA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M30 Too Much or Just Enough? (enough despues del descriptor / so alto-bueno / too excesivo) + paso de graduar libre a decidir el nivel requerido + The Fit Check + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class30_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 20/05 A2 PM Cl 30:')
print('  - A2/A2_Class30_GUIA.pdf')
print('  - A2/reportes/A2_Class30_REPORTE.pdf')
