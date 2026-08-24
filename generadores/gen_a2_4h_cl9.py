#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 9 (cohorte nuevo):
- M20 "Playing is Fun!" Gerunds as Subjects (p.181-196) + M21 "We Shouldn't Swim After Eating"
  Gerunds after Prepositions (p.197-206). M19 NO existe: el libro brinca de M18 a M20.
- Virtud TEMPLANZA v1 dia 4 de 5. Simulacion: SAFETY INDUCTION (bodega, guest-observer).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class9_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class9_GUIA.pdf'))
print('OK: A2_4h_Class9_GUIA.pdf')
