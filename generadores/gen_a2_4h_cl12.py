#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 12:
- M27 "I'm Smarter than Steve" (Unequal Comparatives, p.247-252) + M28 "You're the Best!"
  (The Superlative, p.253-260). Cierra el arco as...as -> -er/more than -> the -est/the most.
- Virtud JUSTICIA v1 dia 2 de 5.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class12_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class12_GUIA.pdf'))
print('OK: A2_4h_Class12_GUIA.pdf')
