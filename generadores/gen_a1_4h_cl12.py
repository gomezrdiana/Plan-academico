#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 INTENSIVO 4H Cl 12:
- 1/2 MIDTERM "My World so far" (integrado, sin marcador) + 1/2 M16 Object Pronouns (p.197-208).
- Virtud JUSTICIA v1 dia 2. Recuperacion N-3 Cl 9 / N-7 Cl 5. Simulacion TAKEOUT COUNTER.
- Profe NO comunica evaluaciones. SUPUESTO: midterm Cl 12 por confirmar Diana. FRONTERA: Cl 13 = M17.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(os.path.join(A1_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class12_PRINT.md'),
          os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class12_GUIA.pdf'))
print('OK: A1_4h_Class12_GUIA.pdf')
