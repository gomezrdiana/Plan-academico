#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 20 — HOJA DE RUTA (2 tracks: CONV + GRAMMAR). Solo GUIAS."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
G = os.path.join(B1, 'GUIAS')
os.makedirs(G, exist_ok=True)

N = 20
for track in ('CONV', 'GRAMMAR'):
    md = os.path.join(B1, f'B1_Clase{N}_{track}_PRINT.md')
    pdf = os.path.join(G, f'B1_Clase{N}_{track}_GUIA.pdf')
    md_to_pdf(md, pdf)
    print('OK:', os.path.basename(pdf))
