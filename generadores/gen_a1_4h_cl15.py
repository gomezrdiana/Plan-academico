#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 INTENSIVO 4H Cl 15:
- M20 You Should Be Happy! (be + auxiliares + sentimientos, p.245-262) + M21 I'm Juan! (be presente, p.263-268), PAR.
- Virtud JUSTICIA v1 dia 5 (cierre). Recuperacion N-3 Cl 12 / N-7 Cl 8. Simulacion JOB INTERVIEW.
- Pieza 13 WHO I AM / HOW I AM. FRONTERA: Cl 16 = M22 + M23 en par.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(os.path.join(A1_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class15_PRINT.md'),
          os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class15_GUIA.pdf'))
print('OK: A1_4h_Class15_GUIA.pdf')
