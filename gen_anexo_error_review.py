#!/usr/bin/env python3
"""Genera PDF del Anexo Error Paper Review."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
ANEXOS_DIR = os.path.join(D, 'recursos', 'anexos')
md_to_pdf(
    os.path.join(ANEXOS_DIR, 'ANEXO_ERROR_PAPER_REVIEW.md'),
    os.path.join(ANEXOS_DIR, 'ANEXO_ERROR_PAPER_REVIEW.pdf'),
)
print('OK: ANEXO_ERROR_PAPER_REVIEW.pdf')
