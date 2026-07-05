#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF del Anexo Error Paper Review."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANEXOS_DIR = os.path.join(D, 'recursos', 'anexos')
md_to_pdf(
    os.path.join(ANEXOS_DIR, 'ANEXO_ERROR_PAPER_REVIEW.md'),
    os.path.join(ANEXOS_DIR, 'ANEXO_ERROR_PAPER_REVIEW.pdf'),
)
print('OK: ANEXO_ERROR_PAPER_REVIEW.pdf')
