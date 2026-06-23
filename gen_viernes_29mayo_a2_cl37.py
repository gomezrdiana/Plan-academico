#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 37 (viernes 29/05/2026):
- M39 Mine, All Mine! (Possessive Pronouns as Objects) + Frase del Dia + virtud FORTALEZA v2 (dia 2)
- Pasa de describir el sustantivo con orden de adjetivos (M38) a preguntar POR EL DUENO y reemplazarlo con un pronombre posesivo (M39)
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA INTERNA: tras M39 (pag 318-325) el libro salta directo a Module 41 (pag 326+); Module 40 NO existe en el libro.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class37_PRINT.md'), os.path.join(A2_DIR, 'A2_Class37_GUIA.pdf'))
print('OK: A2_Class37_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 36 = M38 orden de adjetivos)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza + M39)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 36)', '7 min'),
    ('LIBRO M39 - whose + pronombres posesivos (pag 318-325)', '15 min'),
    ('SPEED DRILL - whose + mine/yours/his/hers/ours/theirs + apostrofe s', '15 min'),
    ('SIMULACION PROFESIONAL - The Lost & Found Desk (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea fin de semana + Cierre + anuncio Cl 38', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M39 whose + pronombres posesivos',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Lost & Found Desk',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 36',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 36 M38)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 37 = FORTALEZA v2 (dia 2, por numero de clase)',
    'Hile FORTALEZA en VATS con el patron whose (fuerza propia mine / entregada yours sin testigo)',
    'Cubri M39 Mine All Mine DESDE EL LIBRO (pag 318-325)',
    'Ensene WHOSE como palabra de pregunta (pronunciada /huuz/, jus)',
    'Ensene pronombres posesivos MINE / YOURS / HIS / HERS / OURS / THEIRS',
    'Diferencie MY (con sustantivo) vs MINE (sin sustantivo) - NUNCA "It is my" ni "It is mine book"',
    'Ensene apostrofe + s con NOMBRES: Peter\'s / my brothers\' / Chris\' / the class\'',
    'Ensene pronombre como SUJETO en comparativos / superlativos (Mine is / Sam\'s is / Mine are)',
    'Conduje Speed Drill 15 items whose + posesivo en coro rapido',
    'Conduje Simulacion The Lost & Found Desk con whose reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (lunes 01/06 antes 7:00 AM, 30-45 min fin de semana A2)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 38 = siguiente modulo del libro (auditado antes; M40 inexistente en el libro, proximo seria M41 - nota interna, no se comenta en clase)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class37_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 37 de 55 | M39 MINE ALL MINE - POSSESSIVE PRONOUNS | FORTALEZA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M39 Mine, All Mine! (whose + pronombres posesivos mine/yours/his/hers/ours/theirs / apostrofe + s con nombres Peter\'s / my brothers\' / Chris\' / pronombre como sujeto en comparativos Mine is / Sam\'s is) + paso de describir el sustantivo con orden de adjetivos (M38) a preguntar POR EL DUENO y reemplazarlo con un pronombre posesivo + The Lost & Found Desk + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class37_REPORTE.pdf')

print('\n2 PDFs generados para viernes 29/05 A2 PM Cl 37:')
print('  - A2/A2_Class37_GUIA.pdf')
print('  - A2/reportes/A2_Class37_REPORTE.pdf')
