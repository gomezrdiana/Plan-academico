#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera las guias del A1 NOCTURNO 2H Cl 21-31 (VERSION_2/A1_2H).
Los reportes los produce despues: python generadores/gen_reporte_v3.py A1_2H
Correr SIEMPRE desde la raiz: python generadores/gen_a1_2h_cl21_31.py
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_2H = os.path.join(D, 'VERSION_2', 'A1_2H')
os.makedirs(os.path.join(A1_2H, 'GUIAS'), exist_ok=True)

for n in range(21, 32):
    md = os.path.join(A1_2H, 'A1_2h_Class%d_PRINT.md' % n)
    if not os.path.exists(md):
        print('SKIP (no existe todavia): A1_2h_Class%d_PRINT.md' % n)
        continue
    pdf = os.path.join(A1_2H, 'GUIAS', 'A1_2h_Class%d_GUIA.pdf' % n)
    md_to_pdf(md, pdf)
    print('OK: A1_2h_Class%d_GUIA.pdf' % n)
