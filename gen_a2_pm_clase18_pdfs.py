#!/usr/bin/env python3
"""A2 Nocturno PM (Tomas) - Clase 18 + Auditoria AUD-002.
Genera: AUD-A2PM-S17-2026-002.pdf + GUIA Cl 18 + REPORTE Cl 18.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page

D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
AUDIT_DIR = os.path.join(D, 'Sistema_Auditoria', 'Tomas_A2_PM')

# =================== AUDITORIA AUD-002 ===================
md_to_pdf(
    os.path.join(AUDIT_DIR, 'AUD-A2PM-S17-2026-002.md'),
    os.path.join(AUDIT_DIR, 'AUD-A2PM-S17-2026-002.pdf'),
)

# =================== GUIA Clase 18 ===================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_Class18_PRINT.md'),
    os.path.join(A2_DIR, 'A2_Clase18_GUIA.pdf'),
)

# =================== REPORTE Clase 18 (sin shadowing) ===================
a2_pm_c18_blocks = [
    ('00:00-00:05', 'VATS Fortaleza dia 3'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 17'),
    ('00:13-00:31', 'Libro M20 Reported Speech'),
    ('00:31-00:43', 'Ejercicios + Parejas'),
    ('00:43-01:05', 'Simulacion El Chisme Profesional (DE PIE)'),
    ('01:05-01:20', 'Historia Interactiva absurda - Lo que dijo el alcalde'),
    ('01:20-01:30', 'Speed Dating Reportando conversaciones (DE PIE)'),
    ('01:30-01:42', 'MINI-PITCH 90 seg + Q&A en vivo (estudiantes excepcionales)'),
    ('01:42-01:52', 'GoldList Lista 18 - 5 frases'),
    ('01:52-01:57', 'Errores + Peer Correction'),
    ('01:57-02:00', 'Autochequeo + Tarea + Cierre'),
]

a2_pm_c18_obs = [
    ('Reported Speech - dominaron said/told + cambio de tiempo verbal?',
     'Mayoria si / mayoria no. Errores tipicos: "she said she IS tired"'),
    ('Mini-Pitch + Q&A - quien destaco / quien evito?',
     'OBJETIVO ARCO: estudiantes excepcionales. Cita nombres'),
    ('3 errores LITERALES con NOMBRE de estudiante',
     'OBLIGATORIO. Auditable por sistema. Ej: Taliana dijo "she said she IS tired"'),
    ('Material para redes - grabaste el Mini-Pitch?',
     'Responde a hallazgo H-005 de AUD-002. Meta minima: 1 video'),
    ('Errores nuevos del libro (errata)',
     'Confirma status de M19 (segun reporte Cl 17 no existe en libro)'),
]

build_report_1page(
    'A2 NOCTURNO 2H', 18,
    'Mod 20 Reported Speech - Fortaleza dia 3 (M19 saltado)',
    a2_pm_c18_blocks, a2_pm_c18_obs,
    os.path.join(A2_DIR, 'A2_Clase18_REPORTE.pdf'),
    cycle_day=None,  # SIN shadowing por excepcion
)

print('\nA2 PM Clase 18 generada (AUD-002 + GUIA + REPORTE).')
