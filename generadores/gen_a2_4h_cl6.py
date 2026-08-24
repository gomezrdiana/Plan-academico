#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 6 (cohorte nuevo, 28 clases):
- M13 "I already knew that!" — Already, Still, Until (p.107-120) + M14 "We Studied During the Game
  Again!" — While, During, Again (p.121-132).
- Virtud TEMPLANZA v1 dia 1 de 5 (apertura de virtud: mini-ritual en Bloque 1).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class6_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class6_GUIA.pdf'))
print('OK: A2_4h_Class6_GUIA.pdf')
