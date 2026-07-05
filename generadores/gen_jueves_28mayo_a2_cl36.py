#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 36 (jueves 28/05/2026):
- M38 Order of Adjectives + Frase del Dia + virtud FORTALEZA v2 DIA 1 (CAMBIO DE BLOQUE Justicia -> Fortaleza)
- Pasa de placement aleatorio de adjetivos a orden tradicional (cantidad-opinion-tamano-edad-forma-color-origen-material-sustantivo)
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA INTERNA: M38 verificado en A2 Book.md pag 312-317 (existe). Cl 37 esperado = M39 (existe).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class36_PRINT.md'), os.path.join(A2_DIR, 'A2_Class36_GUIA.pdf'))
print('OK: A2_Class36_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 35 = M37)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS - CIERRE JUSTICIA + APERTURA FORTALEZA v2 dia 1 + M38', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 35)', '7 min'),
    ('LIBRO M38 - Order of Adjectives (pag 312-317)', '15 min'),
    ('SPEED DRILL - re-ordenar adjetivos', '15 min'),
    ('SIMULACION PROFESIONAL - The Lost & Found Desk (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio Cl 37', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M38 orden adjetivos (cantidad-opinion-tamano-edad-forma-color-origen-material-sustantivo)',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Lost & Found Desk',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 35',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmacion de apertura del bloque FORTALEZA v2 (transicion narrada en VATS)',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 35 M37)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 36 = FORTALEZA v2 DIA 1 (CAMBIO DE BLOQUE - cierre Justicia v2)',
    'NARRE EXPLICITAMENTE en VATS la transicion JUSTICIA -> FORTALEZA (60 seg apertura)',
    'Hile FORTALEZA en VATS con el patron M38 (promesas pequenas-viejas-de madera, orden de adjetivos)',
    'Cubri M38 Order of Adjectives DESDE EL LIBRO (pag 312-317)',
    'Ensene el orden tradicional: cantidad > opinion > tamano > edad > forma > color > origen > material > sustantivo',
    'Ensene que orden incorrecto es comprensible pero NO suena ingles',
    'Conduje Speed Drill 15 items re-ordenar adjetivos en coro rapido',
    'Conduje Simulacion The Lost & Found Desk con minimo 3 adjetivos en orden M38',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo (errores de ORDEN, no de palabra)',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (viernes 29/05 antes 7:00 PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 37 = siguiente modulo del libro (esperado M39, auditar antes) + FORTALEZA v2 dia 2',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class36_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 36 de 55 | M38 ORDER OF ADJECTIVES | FORTALEZA v2 DIA 1 (CAMBIO DE BLOQUE) | FRASE DEL DIA (Goldlist retirado)',
    'M38 Order of Adjectives (orden tradicional: cantidad > opinion > tamano > edad > forma > color > origen > material > sustantivo; "a small old wooden box", "2 pretty blue eyes", "a beautiful big white house") + paso de placement aleatorio a orden M38 + The Lost & Found Desk + FRASE DEL DIA + APERTURA BLOQUE FORTALEZA v2 con transicion narrada desde JUSTICIA v2',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class36_REPORTE.pdf')

print('\n2 PDFs generados para jueves 28/05 A2 PM Cl 36:')
print('  - A2/A2_Class36_GUIA.pdf')
print('  - A2/reportes/A2_Class36_REPORTE.pdf')
