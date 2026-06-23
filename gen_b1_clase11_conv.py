#!/usr/bin/env python3
"""Genera PDF guia + PDF texto ESTUDIANTE + REPORTE editable para B1 Cl 11 CONV (miercoles 13/05/2026). Danna: Present Perfect (M16/A2) + Present Perfect vs Past Simple (M17/A2). Conv va PRIMERO."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
B1_DIR = os.path.join(D, 'B1')
B1_REPORTES = os.path.join(B1_DIR, 'reportes')
os.makedirs(B1_REPORTES, exist_ok=True)

# ============================================================
# 1. PDF GUIA Cl 11 CONV (incluye anexo PROFESOR integrado al final)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase11_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase11_CONV_GUIA.pdf'),
)
print('OK: B1_Clase11_CONV_GUIA.pdf')

# ============================================================
# 2. PDF TEXTO HEIIU CL 11 ESTUDIANTE (texto limpio - 17 copias)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_TEXTO_HEIIU_Cl11_FirstTimes_ESTUDIANTE.md'),
    os.path.join(B1_DIR, 'B1_TEXTO_HEIIU_Cl11_FirstTimes_ESTUDIANTE.pdf'),
)
print('OK: B1_TEXTO_HEIIU_Cl11_FirstTimes_ESTUDIANTE.pdf')

# ============================================================
# 3. REPORTE editable Cl 11 CONV (para Danna)
# ============================================================
b1_c11_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS (virtud del dia segun calendario absoluto)', '7 min'),
    ('PEER TEACHER SLOT (errores de AYER de mi libreta personal)', '7 min'),
    ('Reframe POR QUE GRABAMOS (30 seg) + Intro Present Perfect formal (2.5 min)', '3 min'),
    ('TEXTO HEIIU Cl 11 - First-Time Experiences (lectura + categorizacion verbal)', '15 min'),
    ('HOT TOPIC - debate de la tesis del texto', '17 min'),
    ('SIMULACION PROFESIONAL - your first-time experience (DE PIE)', '20 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Project Workshop Page 10 - FIRST-TIME EXPERIENCES SHAPED ME (FLEXIBLE)', '10 min'),
    ('Error Paper Live + PASE ESCRITO a Juan Diego + Tarea + Cierre', '9 min'),
]
b1_c11_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER usando errores de AYER',
    'PASE ESCRITO entregado a Juan Diego (foto antes de entregar)',
    'Foto/video del Hot Topic + Simulacion',
    'Foto/video Shadowing',
    'Papel errores fisico (anonimo)',
    '17 Paginas 10 del proyecto FIRST-TIME EXPERIENCES SHAPED ME (foto)',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Observacion especifica de los 2 estudiantes en riesgo (NOTA APARTE - no en guia)',
    'Conteo de cuantos estudiantes captaron rapido Present Perfect vs cuantos necesitan refuerzo',
]
b1_c11_c_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad (preparacion previa, ritmo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'LEI el REFRAME POR QUE GRABAMOS antes del primer bloque grabado (30 seg)',
    'INTRODUJE Present Perfect formalmente (primera exposicion sistematica del cohorte)',
    'Entregue Texto Heiiu Cl 11 ESTUDIANTE a los 17 estudiantes',
    'Conduje lectura silenciosa + paired + busqueda gramatical en tablero',
    'Estudiantes categorizaron verbos en 3 columnas (PP regular / PP irregular / PS)',
    'Conduje Hot Topic con tesis explicita del texto (no del aire)',
    'Simulacion fue PROFESIONAL/realista (no fantasiosa, no familiar)',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego ANTES de que empiece su clase',
    'En Tarea LEI la justificacion pedagogica ("If you skip tonight...")',
    'NO acepte la excusa "no me da tiempo"',
    'Anote evidencia especifica de los 2 estudiantes en riesgo (aparte del reporte general)',
    'Estudiantes hablaron 80%+ del tiempo',
    'Observe quien capto Present Perfect rapido y quien necesita refuerzo individual',
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase11_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 11 de 44 | BLOQUE 1: CONVERSACIONAL (HOY VA PRIMERO)',
    'Present Perfect (M16/A2 Regular + Irregular) + Present Perfect vs Past Simple (M17/A2) + Texto Heiiu Cl 11 First-Time Experiences + PASE escrito a Juan Diego',
    b1_c11_c_act, b1_c11_c_deliv, b1_c11_c_eval, S,
)
print('OK: B1_Clase11_CONV_REPORTE.pdf')

print('\n3 PDFs generados:')
print('  - B1/B1_Clase11_CONV_GUIA.pdf  (guia + anexo PROFESOR integrado)')
print('  - B1/B1_TEXTO_HEIIU_Cl11_FirstTimes_ESTUDIANTE.pdf  (17 copias para estudiantes)')
print('  - B1/reportes/B1_Clase11_CONV_REPORTE.pdf  (editable para Danna)')
