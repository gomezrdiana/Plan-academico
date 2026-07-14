#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 6 — HOJA DE RUTA: M7 You Might Learn Something (The Modal "Might", p.51-60).
TEMPLANZA v1 dia 1 (ABRE bloque). Anuncia Cl 7 = M8 relative "that"."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class6_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class6_GUIA.pdf'))
print('OK: A2_Class6_GUIA.pdf')
