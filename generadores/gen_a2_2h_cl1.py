#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 1 — HOJA DE RUTA: M1 I Will Play on Monday (Future WILL + days + ON, p.1-12).
PRUDENCIA v1 dia 1 ABRE. Clase especial: cronograma del nivel + Carta al Yo del Futuro + rituales. Anuncia Cl 2 = M2 Months and Years."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class1_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class1_GUIA.pdf'))
print('OK: A2_Class1_GUIA.pdf')
