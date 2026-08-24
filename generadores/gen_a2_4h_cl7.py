#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 7 (cohorte nuevo):
- M15 "I Have Visited London" (Present Perfect regular, p.133-146) + M16 "I Have Gone to Paris"
  (Present Perfect irregular, p.147-162). Virtud TEMPLANZA v1 dia 2 de 5.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class7_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class7_GUIA.pdf'))
print('OK: A2_4h_Class7_GUIA.pdf')
