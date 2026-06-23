#!/usr/bin/env python3
"""Genera PDF del Bloque 0 - Apertura honesta de Diana en la reunion de profes."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(D, 'documentos_operativos')

md_to_pdf(os.path.join(DOCS, 'BLOQUE0_APERTURA_DIANA_PRINT.md'),
          os.path.join(DOCS, 'BLOQUE0_APERTURA_DIANA.pdf'))
print('OK: BLOQUE0_APERTURA_DIANA.pdf')
