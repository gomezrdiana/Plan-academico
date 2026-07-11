#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 22 — HOJA DE RUTA: M26 I'm as Big as My Dad (Equal Comparatives, p.241-246).
M25 no existe en el libro (24->26); se salta. PRUDENCIA v2 dia 2. Anuncia Cl 23 = M27 Unequal Comparatives."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class22_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class22_GUIA.pdf'))
print('OK: A2_Class22_GUIA.pdf')
