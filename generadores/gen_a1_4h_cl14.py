#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 INTENSIVO 4H Cl 14:
- M18 What Do You Need? (want/need + articulos, p.223-232) + M19 Double Verbs (to+verbo, p.233-244), PAR.
- Virtud JUSTICIA v1 dia 4. Recuperacion N-3 Cl 11 / N-7 Cl 7. Simulacion OFFICE HELP DESK.
- Pieza 12 WHAT I NEED TO DO. FRONTERA: Cl 15 = M20 + M21 en par.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(os.path.join(A1_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class14_PRINT.md'),
          os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class14_GUIA.pdf'))
print('OK: A1_4h_Class14_GUIA.pdf')
