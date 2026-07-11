#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 42 — HOJA DE RUTA REPASO 4/4: Past & time markers (M12 p.99-106, M13 p.107-120, M14 p.121-132).
PRUDENCIA v3 dia 2. Cierra parte 1 del repaso (M1-M14). Anuncia Cl 43 = bloque 2 del repaso (M15 en adelante)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class42_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class42_GUIA.pdf'))
print('OK: A2_Class42_GUIA.pdf')
