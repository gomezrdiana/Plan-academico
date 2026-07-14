#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 9 — HOJA DE RUTA: M11 I'd Eat a Cookie (Second Conditional, p.87-98).
TEMPLANZA v1 dia 4. Anuncia Cl 10 = Module 12 (past simple vs past continuous)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class9_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class9_GUIA.pdf'))
print('OK: A2_Class9_GUIA.pdf')
