#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 12 — HOJA DE RUTA: M14 We Studied During the Game Again! (While, During, Again, p.121-132).
JUSTICIA v1 dia 2. Anuncia Cl 13 = M15 present perfect regular."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class12_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class12_GUIA.pdf'))
print('OK: A2_Class12_GUIA.pdf')
