#!/usr/bin/env python3
"""Genera PDF + reporte para A2 4h Cl 15 (martes 12/05/2026)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REPORTES = os.path.join(A2_DIR, 'reportes')

os.makedirs(A2_REPORTES, exist_ok=True)

# GUIA Cl 15
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class15_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Class15_GUIA.pdf'),
)

# NOTAS OPERATIVAS (aparte - estudiantes especificos)
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class15_NOTAS_OPERATIVAS_2026-05-12.md'),
    os.path.join(A2_DIR, 'A2_4h_Class15_NOTAS_OPERATIVAS_2026-05-12.pdf'),
)

# REPORTE Cl 15
a2_c15_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS Justicia dia 5', '5 min'),
    ('PEER TEACHER SLOT (estudiante rotado ensena 1-2 errores Cl 14)', '7 min'),
    ('Tarea Check Cl 14', '5 min'),
    ('DEPURACION GOLDLIST LISTA 1 - PRIMERA VEZ DEL COHORTE', '20 min'),
    ('VOCABULARY UPGRADE A2-tier para M30', '15 min'),
    ('LIBRO M30 Too Much / Too Many / Enough', '22 min'),
    ('SIMULACION PROFESIONAL M30 (DE PIE)', '20 min'),
    ('Historia interactiva M30 - "La agenda sobrecargada"', '10 min'),
    ('Cierre M30', '5 min'),
    ('GOLDLIST LISTA 15 escritura primera lista nuevo ciclo', '20 min'),
    ('Shadowing Dia 2 del ciclo (sin video, de memoria)', '12 min'),
    ('Free production M30 (parejas DE PIE)', '12 min'),
    ('Error Paper Live (peer relay)', '10 min'),
    ('Tarea + Cierre + anuncio M31 miercoles', '13 min'),
]
a2_c15_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto de TODAS las Listas 1 con cruces - material auditoria depuracion',
    'Numero de tachadas por estudiante (anotado en reporte abajo)',
    'Foto del tablero del WORD UPGRADE A2-tier M30',
    'Foto de las Listas 15 escritas (1 por estudiante presente)',
    'Foto/video Shadowing Dia 2 - material redes',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 14',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Notas de tu energia hoy - con que bloque te conectaste mas/menos',
]
a2_c15_eval = [
    'Lei el mensaje pedagogico al inicio de la guia ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque (cero espanol)',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad',
    'PROYECTE seguridad (preparacion previa, ritmo, sin titubeo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'Conduje MYSTERY HOMEWORK CHECK llamando al azar (no solo voluntarios)',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'Conduje PEER TEACHER SLOT dejando al estudiante producir (sin rescate inmediato)',
    'ESCRIBI el WORD UPGRADE A2-tier para M30 en el tablero ANTES de clase',
    'Mantuve el WORD UPGRADE visible toda la clase',
    'MODELE la depuracion GoldList con mi propio cuaderno (1 frase)',
    'NO permiti que estudiantes "estudiaran" la Lista 1 antes de depurar',
    'Conduje la depuracion en silencio sin intervenir',
    'Tome foto de TODAS las Listas 1 con cruces - material auditoria',
    'Cubri M30 completo (too much / too many / enough)',
    'Hice INTEGRACION M30 + A2-tier vocab en simulacion',
    'Conduje Shadowing Dia 2 sin mostrar el video (practica de memoria)',
    'Simulacion fue PROFESIONAL/realista (no temas personales de familia)',
    'NO acepte la excusa "no me da tiempo" para no hacer tarea',
    'Camine con papel de errores anonimo (min 6 errores)',
    'En libreta personal anote 3 errores con NOMBRE',
    'Anuncie M31 + Shadowing Dia 3 para miercoles Cl 16',
    'Lei la nota operativa aparte ANTES de clase (estudiantes en situacion particular)',
]

build_report_v2(
    os.path.join(A2_REPORTES, 'A2_4h_Class15_REPORTE.pdf'),
    'A2 INTENSIVO | Clase 15 de 28 | 4 HORAS | M30 + PRIMERA DEPURACION GOLDLIST',
    'M30 Too Much/Too Many/Enough + Depuracion Lista 1 (dia 15) + Lista 15 nueva + Shadowing Dia 2 | Justicia dia 5',
    a2_c15_act, a2_c15_deliv, a2_c15_eval, S,
)
print('OK: A2_4h_Class15_REPORTE.pdf')
print('\n3 PDFs generados:')
print('  - A2/A2_4h_Class15_GUIA.pdf')
print('  - A2/A2_4h_Class15_NOTAS_OPERATIVAS_2026-05-12.pdf')
print('  - A2/reportes/A2_4h_Class15_REPORTE.pdf')
