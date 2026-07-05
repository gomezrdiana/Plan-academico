#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Regenera SOLO la GUIA + REPORTE de A2 4H Clase 10 (v2 sin shadowing)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page, a2_c10_blocks, a2_c10_obs

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')

# GUIA
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class10_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Clase10_GUIA.pdf'),
)

# REPORTE -- sin shadowing (cycle_day=None)
build_report_1page(
    'A2 INTENSIVO 4H', 10,
    'Mod 22 Double Verbs + Mod 23 Phrasal Verbs - Templanza dia 2',
    a2_c10_blocks, a2_c10_obs,
    os.path.join(A2_DIR, 'A2_4h_Clase10_REPORTE.pdf'),
    cycle_day=None,
)

print('\nClase 10 v2 regenerada (GUIA + REPORTE).')
