#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 41 — HOJA DE RUTA REPASO 3/4: Connecting ideas & conditions (M8 p.61-74, M10 p.75-86, M11 p.87-98).
PRUDENCIA v3 dia 1. Anuncia Cl 42 = cluster 4 (pasado y marcadores de tiempo)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class41_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class41_GUIA.pdf'))
print('OK: A2_Class41_GUIA.pdf')
