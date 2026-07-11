#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 37 — HOJA DE RUTA: M43 How Do You Do? (Adverbs of Manner, p.340-346).
FORTALEZA v2 dia 2. Anuncia Cl 38 = M44 (ultimo modulo del libro)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class37_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class37_GUIA.pdf'))
print('OK: A2_Class37_GUIA.pdf')
