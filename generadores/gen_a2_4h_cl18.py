#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 18 (cohorte nuevo):
- M41 "This Is Interesting! - Participle Adjectives" (p.326-332) como MODULO UNICO (M40 no existe en el libro).
- Virtud FORTALEZA v1 dia 3 de 5. Simulacion CUSTOMER FEEDBACK DESK (guest-observer, cero material).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class18_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class18_GUIA.pdf'))
print('OK: A2_4h_Class18_GUIA.pdf')
