#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 INTENSIVO 4H Cl 11:
- M15 I Love My Parents - The Possessive Adjectives (p.187-196), SOLO. Familia + posesivos.
- Virtud JUSTICIA v1 dia 1. Recuperacion N-3 Cl 8 / N-7 Cl 4. Simulacion MEET MY PEOPLE.
- Pieza 10 MY FAMILY. Tarea prepara mini-charla midterm. FRONTERA: Cl 12 = 1/2 MIDTERM + 1/2 M16.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(os.path.join(A1_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class11_PRINT.md'),
          os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class11_GUIA.pdf'))
print('OK: A1_4h_Class11_GUIA.pdf')
