#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF del MANUAL_PROFESOR_POR_QUE.md"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUALES_DIR = os.path.join(D, 'recursos', 'manuales')
md_to_pdf(
    os.path.join(MANUALES_DIR, 'MANUAL_PROFESOR_POR_QUE.md'),
    os.path.join(MANUALES_DIR, 'MANUAL_PROFESOR_POR_QUE.pdf'),
)
print('OK: MANUAL_PROFESOR_POR_QUE.pdf')
