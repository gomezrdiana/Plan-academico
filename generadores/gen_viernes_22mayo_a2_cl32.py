#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 32 (viernes 22/05/2026):
- M33 How Much Money Do You Have? (Specifying Uncountable Quantities) + Frase del Dia + virtud JUSTICIA v2 (dia 2)
- Pasa de contar cosas contables (M32) a medir sustancias incontables por unidades (M33)
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA: numeracion M32->M33->M34 continua (sin salto entre 32 y 33; el salto fue Module 31 inexistente, ya documentado en Cl 31).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class32_PRINT.md'), os.path.join(A2_DIR, 'A2_Class32_GUIA.pdf'))
print('OK: A2_Class32_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 31 = M32)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia + M33)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 31)', '7 min'),
    ('LIBRO M33 - How much + vocabulario (pag 283-292)', '15 min'),
    ('SPEED DRILL - how much + respuesta (unidad/dinero/a lot of/a bit of)', '15 min'),
    ('SIMULACION PROFESIONAL - The Supply & Budget Check (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio M34', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M33 how much + vocab',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Supply & Budget Check',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 31',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 31 M32)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 32 = JUSTICIA v2 (dia 2, por numero de clase)',
    'Hile JUSTICIA en VATS con el patron how much (medir cuanto tienes para repartir)',
    'Cubri M33 How Much Money Do You Have DESDE EL LIBRO (pag 283-292)',
    'Ensene how much + ayudante + respuesta (unidad / dinero / a lot of / a bit of)',
    'Conduje Speed Drill 15 items how much + respuesta en coro rapido',
    'Conduje Simulacion The Supply & Budget Check con how much reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (lunes 25/05)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie M34 How Much Does It Cost para lunes (numeracion M32->M33->M34 continua, sin salto)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class32_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 32 de 55 | M33 HOW MUCH MONEY DO YOU HAVE | JUSTICIA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M33 How Much Money Do You Have? (how much + ayudante / respuesta con unidad, dinero, a lot of, a bit of) + paso de contar contables a medir incontables por unidades + The Supply & Budget Check + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class32_REPORTE.pdf')

print('\n2 PDFs generados para viernes 22/05 A2 PM Cl 32:')
print('  - A2/A2_Class32_GUIA.pdf')
print('  - A2/reportes/A2_Class32_REPORTE.pdf')
