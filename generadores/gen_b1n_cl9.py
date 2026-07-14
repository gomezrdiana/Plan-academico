#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY 4h Cl 9 — HOJA DE RUTA (2 tracks). Solo GUIAS (no reportes).
CONV + GRAMMAR: Possessives (A1 Book M15 p.187-196 + M30 p.333-336). Libro NO cubre whose.
TEMPLANZA v1 dia 4. Genera 2 PDFs en VERSION_2/B1_4H/GUIAS/."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
N = 9

for track in ('CONV', 'GRAMMAR'):
    md = os.path.join(B1, f'B1_Clase{N}_{track}_PRINT.md')
    pdf = os.path.join(B1, 'GUIAS', f'B1_Clase{N}_{track}_GUIA.pdf')
    md_to_pdf(md, pdf)
    print('OK:', os.path.basename(pdf))

print(f'\n2 PDFs Cl {N} generados (V2).')
