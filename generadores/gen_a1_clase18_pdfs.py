#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A1 Nocturno - Clase 18 - GUIA + REPORTE (sin shadowing por excepcion, Fortaleza dia 3 canonico)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')

# =================== GUIA ===================
md_to_pdf(
    os.path.join(A1_DIR, 'A1_Class18_PRINT.md'),
    os.path.join(A1_DIR, 'A1_Clase18_GUIA.pdf'),
)

# =================== REPORTE (sin shadowing) ===================
a1_c18_blocks = [
    ('00:00-00:05', 'VATS Fortaleza dia 3'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 17'),
    ('00:13-00:31', 'Libro M18 Want/Need/Have'),
    ('00:31-00:45', 'Ejercicios + Respuestas'),
    ('00:45-01:05', 'Simulacion Compras en Tienda (DE PIE)'),
    ('01:05-01:20', 'Historia Interactiva absurda - El Sastre y los 100 Botones'),
    ('01:20-01:32', 'Speed Dating Want vs Need (DE PIE)'),
    ('01:32-01:40', 'Competencia equipos HAS irregular'),
    ('01:40-01:50', 'GoldList Lista 18 - 5 frases'),
    ('01:50-01:55', 'Errores + Peer Correction'),
    ('01:55-02:00', 'Autochequeo + Tarea + Cierre'),
]

a1_c18_obs = [
    ('Want / Need / Have - dominaron HAS en 3ra persona?',
     'Mayoria si / mayoria no. Errores tipicos: "She have" en lugar de HAS'),
    ('Simulacion Compras - quien destaco / quien evito hablar?',
     'Soft skill: cliente y servicio en tienda real'),
    ('3 errores LITERALES con NOMBRE de estudiante',
     'OBLIGATORIO. Ej: Miguel dijo "She have a car"'),
    ('Errores nuevos encontrados en el libro (errata)',
     'Solo si encontro typo o numeracion mala'),
]

build_report_1page(
    'A1 NOCTURNO 2H', 18,
    'Mod 18 Want/Need/Have - Fortaleza dia 3',
    a1_c18_blocks, a1_c18_obs,
    os.path.join(A1_DIR, 'A1_Clase18_REPORTE.pdf'),
    cycle_day=None,  # SIN shadowing por excepcion
)

print('\nClase 18 A1 nocturno generada (GUIA + REPORTE).')
