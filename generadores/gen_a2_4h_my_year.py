#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera el INSTRUCTIVO del proyecto MY YEAR (A2 4H) — documento solo para el profesor."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_MY_YEAR_INSTRUCTIVO_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_MY_YEAR_INSTRUCTIVO.pdf'))
print('OK: A2_4h_MY_YEAR_INSTRUCTIVO.pdf')
