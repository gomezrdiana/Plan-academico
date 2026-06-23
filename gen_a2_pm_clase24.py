#!/usr/bin/env python3
"""Genera PDF + reporte para A2 PM Cl 24 (martes 12/05/2026 noche). M26 Equal Comparatives + Depuracion Lista 1."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REPORTES = os.path.join(A2_DIR, 'reportes')

os.makedirs(A2_REPORTES, exist_ok=True)

# GUIA Cl 24
md_to_pdf(
    os.path.join(A2_DIR, 'A2_Class24_PRINT.md'),
    os.path.join(A2_DIR, 'A2_Class24_GUIA.pdf'),
)

# REPORTE Cl 24
a2_c24_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS Prudencia dia 4 (v2)', '5 min'),
    ('PEER TEACHER SLOT (estudiante rotado ensena 1-2 errores Cl 22-23)', '7 min'),
    ('Tarea Check Cl 23', '5 min'),
    ('VOCABULARY UPGRADE A1->A2 para M26', '10 min'),
    ('LIBRO M26 Equal Comparatives (lectura + explicacion dirigida)', '19 min'),
    ('Ejercicios M26 (libro pag 244-245) + Speed Drill', '10 min'),
    ('SIMULACION PROFESIONAL M26 (DE PIE)', '15 min'),
    ('GOLDLIST DEPURACION LISTA 1 - PRIMERA VEZ DEL COHORTE', '13 min'),
    ('Shadowing (verificar dia del ciclo)', '9 min'),
    ('Error Paper Live', '5 min'),
    ('Tarea + Cierre + anuncio Cl 25 (M27 + depuracion Lista 2)', '5 min'),
]
a2_c24_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero del WORD UPGRADE M26',
    'Foto/video de la Simulacion profesional M26',
    'Foto de Lista 1 de TODOS los cuadernos con cruces - material auditoria',
    'Numero de tachadas por estudiante (anotado en reporte abajo)',
    'Foto del cuaderno con seccion "D1 of List 1" iniciada',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 23',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Lista actualizada de asistencia',
    'Notas de tu energia hoy',
]
a2_c24_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad',
    'PROYECTE seguridad (preparacion previa, ritmo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PRACTIQUE con mi propio cuaderno el modelado de depuracion (1 frase) ANTES de clase',
    'Conduje MYSTERY HOMEWORK CHECK llamando al azar',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'ESCRIBI el WORD UPGRADE M26 en tablero ANTES de clase',
    'Cubri M26 Equal Comparatives DESDE EL LIBRO (no inventando contenido)',
    'Hice INTEGRACION as...as positivo + negativo + ALMOST en ejercicios',
    'Conduje SPEED DRILL hasta que salio sin pensar',
    'Simulacion M26 fue PROFESIONAL/realista (no temas familiares)',
    'MODELE la depuracion GoldList con mi propio cuaderno (1 frase)',
    'NO permiti que estudiantes estudiaran Lista 1 antes de depurar',
    'Conduje la depuracion en silencio sin intervenir',
    'Tome foto de TODAS las Listas 1 con cruces',
    'Conte tachadas por estudiante y verifique rango 5-12',
    'CONDUJE Shadowing con foco en ritmo y entonacion',
    'NO acepte la excusa "no me dio tiempo" para no hacer tarea',
    'Camine con papel de errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'Anuncie Cl 25 (M27 Unequal Comparatives + depuracion Lista 2)',
]

build_report_v2(
    os.path.join(A2_REPORTES, 'A2_Class24_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 24 de 55 | 2 HORAS | M26 + PRIMERA DEPURACION GOLDLIST',
    'M26 Equal Comparatives (as...as) + Depuracion Lista 1 (primera del cohorte) + Mystery + Peer Teacher | Prudencia dia 4 (v2)',
    a2_c24_act, a2_c24_deliv, a2_c24_eval, S,
)
print('OK: A2_Class24_REPORTE.pdf')

print('\n2 PDFs generados:')
print('  - A2/A2_Class24_GUIA.pdf')
print('  - A2/reportes/A2_Class24_REPORTE.pdf')
