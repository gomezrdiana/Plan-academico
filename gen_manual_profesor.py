#!/usr/bin/env python3
"""Genera PDF del MANUAL_PROFESOR_REGLAS_GENERALES.md"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
MANUALES_DIR = os.path.join(D, 'recursos', 'manuales')
md = os.path.join(MANUALES_DIR, 'MANUAL_PROFESOR_REGLAS_GENERALES.md')
pdf = os.path.join(MANUALES_DIR, 'MANUAL_PROFESOR_REGLAS_GENERALES.pdf')
md_to_pdf(md, pdf)
print(f'OK: {pdf}')
