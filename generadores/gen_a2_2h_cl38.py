#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 38 — HOJA DE RUTA: M44 I Want You to Go (Active Causative, p.347-350).
ULTIMO modulo del libro A2. FORTALEZA v2 dia 3. Anuncia Cl 39 = arco de repaso (consolidacion)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class38_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class38_GUIA.pdf'))
print('OK: A2_Class38_GUIA.pdf')
