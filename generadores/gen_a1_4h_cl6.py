#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 INTENSIVO 4H Cl 6:
- M9 He Eats in the Restaurant - Simple Present, Affirmative Exception (p.111-122), media sesion
- MINI-PRESENTACION MY WORLD (evento integrado, media sesion) - SUPUESTO por confirmar Diana
- Virtud TEMPLANZA v1 dia 1. Recuperacion N-3 Cl 3 (N-7 n/a). Frase del Dia.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(os.path.join(A1_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class6_PRINT.md'),
          os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class6_GUIA.pdf'))
print('OK: A1_4h_Class6_GUIA.pdf')
