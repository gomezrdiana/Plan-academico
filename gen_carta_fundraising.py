#!/usr/bin/env python3
"""Genera PDF de la carta de presentacion para posible patrocinador / fundraising."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(D, 'documentos_operativos')

md_to_pdf(os.path.join(DOCS, 'CARTA_PRESENTACION_FUNDRAISING_PRINT.md'),
          os.path.join(DOCS, 'CARTA_PRESENTACION_FUNDRAISING.pdf'))
print('OK: CARTA_PRESENTACION_FUNDRAISING.pdf')
