#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 NOCTURNO 2H Cl 13 (cohorte nuevo, VERSION_2/A1_2H).
El reporte lo produce despues: python generadores/gen_reporte_v3.py A1_2H
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_2H = os.path.join(D, 'VERSION_2', 'A1_2H')
os.makedirs(os.path.join(A1_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_2H, 'A1_2h_Class13_PRINT.md'),
          os.path.join(A1_2H, 'GUIAS', 'A1_2h_Class13_GUIA.pdf'))
print('OK: A1_2h_Class13_GUIA.pdf')
