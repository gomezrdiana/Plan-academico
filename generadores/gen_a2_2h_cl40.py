#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 40 — HOJA DE RUTA REPASO 2/4: Ways to talk about the future (M5 p.31-40, M6 p.41-50, M7 p.51-60).
FORTALEZA v2 dia 5. Anuncia Cl 41 = cluster 3 (conectar ideas y condicionales)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class40_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class40_GUIA.pdf'))
print('OK: A2_Class40_GUIA.pdf')
