#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 4 — HOJA DE RUTA: M5 The Future in Triplicate (will/going to/present continuous, p.31-40; M4 saltado).
PRUDENCIA v1 dia 4. Primera recuperacion N-3 real (trae Cl 1). Anuncia Cl 5 = M6 Right on Time."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class4_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class4_GUIA.pdf'))
print('OK: A2_Class4_GUIA.pdf')
