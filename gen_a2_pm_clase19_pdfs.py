#!/usr/bin/env python3
"""A2 Nocturno PM (Tomas) - Clase 19 - GUIA + REPORTE.
Formato hoy: 90 min academico + 30 min actividad externa.
Shadowing CON video confirmado. VATS Fortaleza dia 4 (canonico).
M21 Gerundios con Preposiciones.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page

D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')

# =================== GUIA Cl 19 ===================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_Class19_PRINT.md'),
    os.path.join(A2_DIR, 'A2_Clase19_GUIA.pdf'),
)

# =================== REPORTE Cl 19 (con shadowing Dia 1) ===================
a2_pm_c19_blocks = [
    ('00:00-00:05', 'VATS Fortaleza dia 4'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 18'),
    ('00:13-00:28', 'Libro M21 Gerundios con Preposiciones'),
    ('00:28-00:38', 'Ejercicios + Parejas'),
    ('00:38-00:53', 'Simulacion Soy bueno en, malo en, miedo a (DE PIE)'),
    ('00:53-01:08', 'Shadowing 5 pasos - Dia 1 ciclo nuevo'),
    ('01:08-01:18', 'MINI-PITCH 90 seg + Q&A en vivo (estudiantes excepcionales)'),
    ('01:18-01:26', 'GoldList Lista 19 - 5 frases'),
    ('01:26-01:30', 'Errores + Tarea con due date + Cierre'),
    ('01:30-02:00', 'ACTIVIDAD EXTERNA (coordinacion - 30 min)'),
]

a2_pm_c19_obs = [
    ('Gerundios con Preposiciones - dominaron prep + ING?',
     'Mayoria si / mayoria no. Errores tipicos: "good at to cook" (debe ser cooking)'),
    ('Mini-Pitch + Q&A - quien destaco / quien evito?',
     'OBJETIVO ARCO: estudiantes excepcionales. Cita nombres'),
    ('3 errores LITERALES con NOMBRE de estudiante',
     'OBLIGATORIO. Auditable por sistema'),
    ('URL video Shadowing usado',
     'https://www.youtube.com/watch?v=MFXOcfz177Q'),
    ('Estudiantes que dijeron "es muy pesado" sobre tarea anterior',
     'Si aplico la regla firme. Nombres si pidieron aflojar'),
]

build_report_1page(
    'A2 NOCTURNO 2H', 19,
    'Mod 21 Gerundios con Preposiciones - Fortaleza dia 4 - Shadowing Dia 1 nuevo ciclo',
    a2_pm_c19_blocks, a2_pm_c19_obs,
    os.path.join(A2_DIR, 'A2_Clase19_REPORTE.pdf'),
    cycle_day=1,  # Dia 1 del ciclo Shadowing - video confirmado
)

print('\nA2 PM Clase 19 generada (GUIA + REPORTE).')
print('Video Shadowing: https://www.youtube.com/watch?v=MFXOcfz177Q')
