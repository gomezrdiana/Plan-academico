#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 15:
- M33 "How Much Money Do You Have? - Specifying Uncountable Quantities" (p.283-292)
  + M34 "How Much Does It Cost? - Describing Prices" (p.293-300).
- Virtud JUSTICIA v1 dia 5 de 5 (cierre de bloque; Cl 16-20 = FORTALEZA v1).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class15_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class15_GUIA.pdf'))
print('OK: A2_4h_Class15_GUIA.pdf')
