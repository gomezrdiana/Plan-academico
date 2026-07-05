#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 33 (lunes 25/05/2026):
- M34 How Much Does It Cost? (Describing Prices) + Frase del Dia + virtud JUSTICIA v2 (dia 3)
- Pasa de medir sustancias incontables por unidades (M33) a preguntar/dar el PRECIO de algo (M34, "money" implicito)
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA INTERNA: tras M34 (pag 293-300) el libro salta directo a Module 36 (pag 301); Module 35 NO existe en el libro.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class33_PRINT.md'), os.path.join(A2_DIR, 'A2_Class33_GUIA.pdf'))
print('OK: A2_Class33_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 32 = M33)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia + M34)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 32)', '7 min'),
    ('LIBRO M34 - How much + cost/be (pag 293-300)', '15 min'),
    ('SPEED DRILL - how much + precio (cost / be / each)', '15 min'),
    ('SIMULACION PROFESIONAL - The Store Price Check (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio Cl 34', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M34 how much + cost/be + items',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Store Price Check',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 32',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 32 M33)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 33 = JUSTICIA v2 (dia 3, por numero de clase)',
    'Hile JUSTICIA en VATS con el patron how much does it cost (precio honesto de la equidad)',
    'Cubri M34 How Much Does It Cost DESDE EL LIBRO (pag 293-300)',
    'Ensene how much + DOES/DO + sujeto + cost (con respuesta It costs / They cost)',
    'Ensene how much + IS/ARE + sujeto (con respuesta It is / They are)',
    'Ensene "each" = cada / por unidad ("$X each")',
    'Conduje Speed Drill 15 items how much + precio en coro rapido',
    'Conduje Simulacion The Store Price Check con how much reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (martes 26/05 antes 7:00 PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 34 = siguiente modulo del libro (auditado antes; M35 inexistente en el libro - nota interna, no se comenta en clase)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class33_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 33 de 55 | M34 HOW MUCH DOES IT COST | JUSTICIA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M34 How Much Does It Cost? (how much + does/do + sujeto + cost / how much + is/are + sujeto / respuesta con It costs - They cost - It is - They are + precio, "each" = por unidad) + paso de medir incontables por unidades a preguntar el PRECIO con "money" implicito + The Store Price Check + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class33_REPORTE.pdf')

print('\n2 PDFs generados para lunes 25/05 A2 PM Cl 33:')
print('  - A2/A2_Class33_GUIA.pdf')
print('  - A2/reportes/A2_Class33_REPORTE.pdf')
