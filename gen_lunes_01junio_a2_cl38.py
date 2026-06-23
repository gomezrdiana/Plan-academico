#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 38 (lunes 01/06/2026):
- M41 This Is Interesting! (Participle Adjectives) + Frase del Dia + virtud FORTALEZA v2 (dia 3)
- Pasa de preguntar por el DUEÑO del sustantivo (M39) a usar DOS adjetivos por verbo de emocion:
  -ING (produce el efecto, "ser ___") vs -ED (siente el efecto, "estar ___")
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA INTERNA: el libro salta de Module 39 (pag 318-325) directo a Module 41 (pag 326+).
  Module 40 NO existe en el libro. Patron documentado en A2 (M19/M25/M31/M35/M40 saltados).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class38_PRINT.md'), os.path.join(A2_DIR, 'A2_Class38_GUIA.pdf'))
print('OK: A2_Class38_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 37 = M39 whose + posesivos)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza + M41)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 37)', '7 min'),
    ('LIBRO M41 - -ING vs -ED (pag 326-332)', '15 min'),
    ('SPEED DRILL - pares -ING / -ED (ser vs estar)', '15 min'),
    ('SIMULACION PROFESIONAL - The End-of-Day Team Debrief (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio Cl 39', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M41 -ING vs -ED + tabla de pares',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The End-of-Day Team Debrief',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 37',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 37 M39)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 38 = FORTALEZA v2 (dia 3, por numero de clase)',
    'Hile FORTALEZA en VATS con el patron -ING / -ED (cansancio que no descalifica)',
    'Cubri M41 This Is Interesting DESDE EL LIBRO (pag 326-332)',
    'Ensene -ING = produce el efecto (ser) vs -ED = siente el efecto (estar)',
    'Cubri los 15 pares del vocabulario (libro pag 327)',
    'Incluyo el irregular "We are LOST" (libro pag 328)',
    'Cubri las TRES formas: afirmativa, negativa, interrogativa',
    'Conduje Speed Drill 20 items -ING / -ED en coro rapido',
    'Conduje Simulacion The End-of-Day Team Debrief con -ING / -ED reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (martes 02/06 antes 7:00 PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 39 = siguiente modulo del libro + FORTALEZA v2 dia 4 (M42 candidato, auditado antes; M40 inexistente en el libro - nota interna, no se comenta en clase)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class38_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 38 de 55 | M41 THIS IS INTERESTING (PARTICIPLE ADJECTIVES) | FORTALEZA v2 dia 3 | FRASE DEL DIA (Goldlist retirado)',
    'M41 This Is Interesting! (Participle Adjectives: -ING = produce el efecto / -ED = siente el efecto; 15 pares boring/bored, exciting/excited, interesting/interested, surprising/surprised, tiring/tired, amazing/amazed, annoying/annoyed, confusing/confused, distracting/distracted, embarrassing/embarrassed, frustrating/frustrated, relaxing/relaxed, worrying/worried, depressing/depressed, disappointing/disappointed; irregular "We are lost"; tres formas afirmativa/negativa/interrogativa) + paso de preguntar por el DUEÑO del sustantivo (M39) a usar DOS adjetivos por verbo de emocion (M41) + The End-of-Day Team Debrief + FRASE DEL DIA. M40 NO existe en el libro - salto auditado.',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class38_REPORTE.pdf')

print('\n2 PDFs generados para lunes 01/06 A2 PM Cl 38:')
print('  - A2/A2_Class38_GUIA.pdf')
print('  - A2/reportes/A2_Class38_REPORTE.pdf')
