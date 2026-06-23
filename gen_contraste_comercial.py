#!/usr/bin/env python3
"""Genera PDF del contraste Guia Comercial v15 vs Master Blueprint v1.2."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(D, 'documentos_operativos')

md_to_pdf(os.path.join(DOCS, 'CONTRASTE_GUIA_COMERCIAL_vs_BLUEPRINT_PRINT.md'),
          os.path.join(DOCS, 'CONTRASTE_GUIA_COMERCIAL_vs_BLUEPRINT.pdf'))
print('OK: CONTRASTE_GUIA_COMERCIAL_vs_BLUEPRINT.pdf')
