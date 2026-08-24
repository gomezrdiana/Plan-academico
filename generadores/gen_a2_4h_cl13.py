#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 13:
- M29 "How Tall Are You?" — Degrees of Adjectives (Libro A2 p.261-266). MODULO UNICO: los 4 bloques
  giran alrededor de M29 (instalacion de la regla + drill de pie + simulacion de ficha de ingreso).
- Virtud JUSTICIA v1 dia 3 de 5. Cl 14 = M30 + M32 (M31 no existe en el libro).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class13_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class13_GUIA.pdf'))
print('OK: A2_4h_Class13_GUIA.pdf')
