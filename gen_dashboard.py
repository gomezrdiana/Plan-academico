#!/usr/bin/env python3
"""Genera PDF del Dashboard Diana."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
md_to_pdf(
    os.path.join(D, 'DASHBOARD_DIANA_2026-05-04.md'),
    os.path.join(D, 'DASHBOARD_DIANA_2026-05-04.pdf'),
)
print('OK: DASHBOARD_DIANA_2026-05-04.pdf')
