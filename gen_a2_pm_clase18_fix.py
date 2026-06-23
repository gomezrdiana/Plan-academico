#!/usr/bin/env python3
"""A2 Nocturno PM (Tomas) - Clase 18 FIX - regenera con contenido correcto M20 (Gerundios como Sujeto).
La version inicial tenia Reported Speech por error de inferencia.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page

D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')

# =================== GUIA Cl 18 FIX ===================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_Class18_PRINT.md'),
    os.path.join(A2_DIR, 'A2_Clase18_GUIA.pdf'),
)

# =================== REPORTE Cl 18 FIX (sin shadowing, contenido M20 correcto) ===================
a2_pm_c18_blocks = [
    ('00:00-00:05', 'VATS Fortaleza dia 3'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 17'),
    ('00:13-00:31', 'Libro M20 Gerundios como Sujeto'),
    ('00:31-00:43', 'Ejercicios + Parejas'),
    ('00:43-01:05', 'Simulacion Lo que me hace bien y lo que me dana (DE PIE)'),
    ('01:05-01:20', 'Historia Interactiva absurda - Cocinar es Peligroso'),
    ('01:20-01:30', 'Speed Dating Gerundios como Sujeto (DE PIE)'),
    ('01:30-01:42', 'MINI-PITCH 90 seg + Q&A en vivo (estudiantes excepcionales)'),
    ('01:42-01:52', 'GoldList Lista 18 - 5 frases'),
    ('01:52-01:57', 'Errores + Peer Correction'),
    ('01:57-02:00', 'Autochequeo + Tarea + Cierre'),
]

a2_pm_c18_obs = [
    ('Gerundios como Sujeto - dominaron "Swimming is fun" (no "To swim is fun")?',
     'Mayoria si / mayoria no. Errores tipicos: usar infinitivo como sujeto'),
    ('Mini-Pitch + Q&A - quien destaco / quien evito?',
     'OBJETIVO ARCO: estudiantes excepcionales. Cita nombres'),
    ('3 errores LITERALES con NOMBRE de estudiante',
     'OBLIGATORIO. Auditable por sistema. Ej: Taliana dijo "To swim is fun"'),
    ('Material para redes - grabaste el Mini-Pitch?',
     'Meta minima: 1 video. Responde a hallazgo H-005 de AUD-002'),
    ('Errores nuevos del libro (errata)',
     'Confirma que M20 del libro = Gerundios como Sujeto'),
]

build_report_1page(
    'A2 NOCTURNO 2H', 18,
    'Mod 20 Gerundios como Sujeto - Fortaleza dia 3 (M19 saltado)',
    a2_pm_c18_blocks, a2_pm_c18_obs,
    os.path.join(A2_DIR, 'A2_Clase18_REPORTE.pdf'),
    cycle_day=None,
)

print('\nA2 PM Clase 18 ARCHIVO CORREGIDO (M20 Gerundios como Sujeto, no Reported Speech).')
