#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 2:
- M3 "Days of the Month — The Ordinal Numbers" (p.21-30) + M5 "The Future in Triplicate" (p.31-40).
- El libro A2 NO tiene Module 4: se brinca de M3 a M5.
- Virtud PRUDENCIA v1 dia 2 de 5.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class2_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class2_GUIA.pdf'))
print('OK: A2_4h_Class2_GUIA.pdf')
