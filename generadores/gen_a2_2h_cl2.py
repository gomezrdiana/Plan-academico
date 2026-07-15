#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 2 — HOJA DE RUTA: M2 Months and Years (mes + anio + IN, p.13-20).
PRUDENCIA v1 dia 2. Arranca chequeo publico de portafolio. Anuncia Cl 3 = M3 Days of the Month."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class2_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class2_GUIA.pdf'))
print('OK: A2_Class2_GUIA.pdf')
