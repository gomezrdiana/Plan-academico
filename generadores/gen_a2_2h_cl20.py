#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 20 — HOJA DE RUTA: M23 I Asked for A Pencil (Non-Separable Phrasal Verbs, p.221-232).
FORTALEZA v1 dia 5. Anuncia Cl 21 = M24 I'll Pick You Up at 8:00 (separable phrasal verbs)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class20_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class20_GUIA.pdf'))
print('OK: A2_Class20_GUIA.pdf')
