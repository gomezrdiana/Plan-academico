#!/usr/bin/env python3
"""Genera PDFs de los anexos Carta del Yo del Futuro y Capsula de 30 Dias."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
ANEXOS_DIR = os.path.join(D, 'recursos', 'anexos')
for name in ['ANEXO_CARTA_YO_FUTURO', 'ANEXO_CAPSULA_30_DIAS']:
    md = os.path.join(ANEXOS_DIR, f'{name}.md')
    pdf = os.path.join(ANEXOS_DIR, f'{name}.pdf')
    md_to_pdf(md, pdf)
    print(f'OK: {pdf}')
