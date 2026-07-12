#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 INTENSIVO 4H Cl 13:
- M17 Do You Have Any Pizza? - Have + Indefinite Adjectives (p.209-222), SOLO (denso).
- Virtud JUSTICIA v1 dia 3. Recuperacion N-3 Cl 10 / N-7 Cl 6. Simulacion THE RESTAURANT.
- Pieza 11 WHAT I HAVE. FRONTERA: Cl 14 = M18 + M19 en par.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(os.path.join(A1_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class13_PRINT.md'),
          os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class13_GUIA.pdf'))
print('OK: A1_4h_Class13_GUIA.pdf')
