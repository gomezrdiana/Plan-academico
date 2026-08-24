#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 16:
- M36 "What Are You Wearing? - Describing Clothing" (p.301-306)
  + M37 "What Do You Look Like? - Describing People" (p.307-312).
  M35 NO existe: el libro brinca de M34 a M36.
- Virtud FORTALEZA v1 dia 1 de 5 (apertura de bloque, mini-ritual en Bloque 1).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class16_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class16_GUIA.pdf'))
print('OK: A2_4h_Class16_GUIA.pdf')
