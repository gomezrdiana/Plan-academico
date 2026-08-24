#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 10 (cohorte nuevo):
- M22 "I Love Swimming!" Gerunds with Double Verbs (p.207-220) + M23 "I Asked for A Pencil."
  Basic, Non-Separable Phrasal Verbs (p.221-232).
- Virtud TEMPLANZA v1 dia 5 de 5 (CIERRE; Cl 11-15 = JUSTICIA v1).
- Simulacion: THE RETURNS COUNTER (tienda, guest-observer). Frontera: M25 no existe -> Cl 11 = M24 + M26.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class10_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class10_GUIA.pdf'))
print('OK: A2_4h_Class10_GUIA.pdf')
