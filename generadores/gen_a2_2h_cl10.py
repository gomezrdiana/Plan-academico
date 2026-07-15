#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 10 — HOJA DE RUTA: M12 I Was Playing when My Mom Called (Past Simple vs Past Continuous, p.99-106).
TEMPLANZA v1 dia 5 (cierra bloque). Anuncia Cl 11 = M13 already/still/until + JUSTICIA."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class10_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class10_GUIA.pdf'))
print('OK: A2_Class10_GUIA.pdf')
