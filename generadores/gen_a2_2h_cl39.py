#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 39 — HOJA DE RUTA REPASO 1/4: Future & Dates (M1 p.1-12, M2 p.13-20, M3 p.21-30).
FORTALEZA v2 dia 4. Anuncia Cl 40 = cluster 2 (formas de futuro)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class39_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class39_GUIA.pdf'))
print('OK: A2_Class39_GUIA.pdf')
