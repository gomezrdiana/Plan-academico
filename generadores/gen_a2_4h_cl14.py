#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 14:
- M30 "Too Much or Just Enough?" — Required Levels (p.267-272) + M32 "How Many People Are There?"
  — Specifying Countable Quantities (p.273-282). M31 NO EXISTE: el libro brinca de M30 a M32.
- Virtud JUSTICIA v1 dia 4 de 5. Cl 15 = M33 (p.283) + M34 (p.293).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class14_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class14_GUIA.pdf'))
print('OK: A2_4h_Class14_GUIA.pdf')
