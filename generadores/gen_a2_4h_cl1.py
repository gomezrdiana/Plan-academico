#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 1 (cohorte nuevo, 28 clases / 110h):
- M1 "I Will Play on Monday" (will + dias, p.1-12) + M2 "Months and Years" (p.13-20).
- Cl 1 de cohorte nuevo: presentacion de rituales + Carta/Capsula + cronograma del nivel.
- Virtud PRUDENCIA v1 dia 1 de 5.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class1_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class1_GUIA.pdf'))
print('OK: A2_4h_Class1_GUIA.pdf')
