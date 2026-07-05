#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A1 Nocturno (Christian) - Clase 19 - GUIA + REPORTE.
Formato hoy: 90 min academico + 30 min actividad externa.
Shadowing CON video confirmado. VATS Fortaleza dia 4 (canonico).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')

# =================== GUIA ===================
md_to_pdf(
    os.path.join(A1_DIR, 'A1_Class19_PRINT.md'),
    os.path.join(A1_DIR, 'A1_Clase19_GUIA.pdf'),
)

# =================== REPORTE (con shadowing Dia 1) ===================
a1_c19_blocks = [
    ('00:00-00:05', 'VATS Fortaleza dia 4'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 18'),
    ('00:13-00:28', 'Libro M19 Double Verbs (want/need/love TO)'),
    ('00:28-00:38', 'Ejercicios + Parejas'),
    ('00:38-00:53', 'Simulacion Mis Planes Fin de Semana (DE PIE)'),
    ('00:53-01:08', 'Shadowing 5 pasos - Dia 1 ciclo nuevo'),
    ('01:08-01:16', 'GoldList Lista 19 - 5 frases'),
    ('01:16-01:30', 'Errores + Tarea con due date + Cierre'),
    ('01:30-02:00', 'ACTIVIDAD EXTERNA (coordinacion - 30 min)'),
]

a1_c19_obs = [
    ('Double Verbs - dominaron WANT TO / NEED TO / LOVE TO + verbo?',
     'Mayoria si / mayoria no. Errores tipicos: "I want travel" sin TO'),
    ('Simulacion Fin de Semana - quien destaco / quien evito?',
     'Tema cotidiano profesional/familiar'),
    ('3 errores LITERALES con NOMBRE de estudiante',
     'OBLIGATORIO. Auditable por sistema'),
    ('URL video Shadowing usado',
     'https://www.youtube.com/watch?v=je5idXVBcEk'),
    ('Estudiantes que dijeron "es muy pesado" sobre tarea anterior',
     'Si aplico la regla firme. Nombres si pidieron aflojar'),
]

build_report_1page(
    'A1 NOCTURNO 2H', 19,
    'Mod 19 Double Verbs (want/need/love TO) - Fortaleza dia 4 - Shadowing Dia 1 nuevo ciclo',
    a1_c19_blocks, a1_c19_obs,
    os.path.join(A1_DIR, 'A1_Clase19_REPORTE.pdf'),
    cycle_day=1,  # Dia 1 del ciclo Shadowing - video confirmado
)

print('\nA1 nocturno Clase 19 generada (GUIA + REPORTE).')
print('Video Shadowing: https://www.youtube.com/watch?v=je5idXVBcEk')
