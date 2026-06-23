#!/usr/bin/env python3
"""Genera PDF + reporte para A2 4h Cl 14 (lunes 11/05/2026)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REPORTES = os.path.join(A2_DIR, 'reportes')

os.makedirs(A2_REPORTES, exist_ok=True)

# GUÍA Cl 14
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class14_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Class14_GUIA.pdf'),
)

# REPORTE Cl 14
a2_c14_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo NUEVO)', '2 min'),
    ('VATS Justicia dia 4', '5 min'),
    ('PEER TEACHER SLOT (estudiante rotado ensena 1-2 errores)', '7 min'),
    ('Tarea Check Cl 12 + cierre breve del midterm', '8 min'),
    ('RECUPERACION PROYECTO - 2 estudiantes (18 min c/u)', '36 min'),
    ('RECUPERACION PROYECTO - 3er estudiante (18 min)', '18 min'),
    ('Retroalimentacion grupal de las 3 presentaciones', '13 min'),
    ('Cierre evaluativo del proyecto + transicion', '3 min'),
    ('VOCABULARY UPGRADE A2-tier para M29', '15 min'),
    ('LIBRO M29 lectura + explicacion dirigida', '22 min'),
    ('SIMULACION PROFESIONAL M29 (DE PIE)', '20 min'),
    ('Historia interactiva M29 - "El ejecutivo agotado"', '10 min'),
    ('Cierre M29', '5 min'),
    ('GoldList 20 frases A2-tier reflexivas', '15 min'),
    ('Shadowing Dia 1 NUEVO ciclo', '12 min'),
    ('Free production M29 (parejas DE PIE)', '10 min'),
    ('Error Paper Live (peer relay)', '8 min'),
    ('Tarea + Cierre + anuncio M30 martes', '11 min'),
]
a2_c14_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check (instruccion visible)',
    'Foto/video Shadowing Dia 1 nuevo ciclo - material redes',
    'Papel errores fisico (anonimo)',
    'Foto del tablero del WORD UPGRADE A1->A2-tier',
    '5 cuadernos GoldList con 20 frases A2-tier reflexivas',
    'Lista quienes NO entregaron tarea Cl 12',
    'Foto/video de las 3 presentaciones de recuperacion - material auditoria',
    'Rubricas oficiales llenas para los 3 estudiantes recuperados',
    'Tu libreta personal con 3 errores literales + nombre por bloque',
    'Notas de tu energia hoy - con que bloque te conectaste mas/menos',
]
a2_c14_eval = [
    'Lei el mensaje pedagogico al inicio de la guia ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque (cero espanol)',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad (repeti hasta que salio sin pensar)',
    'PROYECTE seguridad (preparacion previa, ritmo, sin titubeo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'Conduje MYSTERY HOMEWORK CHECK llamando estudiantes al azar (no solo voluntarios)',
    'ASIGNE estudiante de PEER TEACHER con anticipacion (rotacion visible)',
    'Conduje PEER TEACHER SLOT dejando al estudiante producir (sin rescate inmediato)',
    'ESCRIBI el WORD UPGRADE A2-tier en el tablero ANTES de clase',
    'Mantuve el WORD UPGRADE visible toda la clase',
    'Conduje las 3 presentaciones de recuperacion con cronometro estricto (18 min c/u)',
    'Hice retroalimentacion grupal sin nombres (errores anonimos)',
    'Cubri M29 completo (NO M30 - se mueve a Cl 15 martes)',
    'Simulacion fue PROFESIONAL/realista (no temas personales de familia)',
    'Lei las 20 frases del GoldList con la clase',
    'Conduje Shadowing Dia 1 con foco en ritmo y entonacion',
    'NO acepte la excusa "no me da tiempo" para no hacer tarea',
    'Camine con papel de errores anonimo (min 6 errores)',
    'En libreta personal anote 3 errores con NOMBRE',
    'Anuncie M30 para martes Cl 15',
]

build_report_v2(
    os.path.join(A2_REPORTES, 'A2_4h_Class14_REPORTE.pdf'),
    'A2 INTENSIVO | Clase 14 de 28 | 4 HORAS POST-MIDTERM',
    'M29 Degrees + RECUPERACION PROYECTO (3 estudiantes) + Mystery Homework Check + A2-tier Vocab | Justicia dia 4',
    a2_c14_act, a2_c14_deliv, a2_c14_eval, S,
)
print('OK: A2_4h_Class14_REPORTE.pdf')
print('\n2 PDFs generados:')
print('  - A2/A2_4h_Class14_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class14_REPORTE.pdf')
