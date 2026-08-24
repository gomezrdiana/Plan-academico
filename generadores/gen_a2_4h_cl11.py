#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 11:
- M24 "I'll Pick You Up at 8:00" (Separable Phrasal Verbs, p.233-240) + M26 "I'm as Big as My Dad"
  (Equal Comparatives, p.241-246). M25 NO existe en el libro: se salta.
- Virtud JUSTICIA v1 dia 1 de 5 (apertura de virtud nueva, mini-ritual en Bloque 1).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class11_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class11_GUIA.pdf'))
print('OK: A2_4h_Class11_GUIA.pdf')
