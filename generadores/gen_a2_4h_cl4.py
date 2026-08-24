#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 4 (cohorte nuevo, 28 clases):
- M8 "I Think that I'm Learning! / Relative 'That'" (p.61-74) + M10 "I'll Buy Lunch! / 1st Conditional" (p.75-84).
- M9 NO existe en el libro: se salta. Virtud PRUDENCIA v1, dia 4 de 5.
- Simulacion: customer service desk, the order did not arrive (guest-observer).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class4_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class4_GUIA.pdf'))
print('OK: A2_4h_Class4_GUIA.pdf')
