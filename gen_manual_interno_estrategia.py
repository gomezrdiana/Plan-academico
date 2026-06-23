#!/usr/bin/env python3
"""Genera PDF del MANUAL_INTERNO_ESTRATEGIA_HEIIU.md (uso privado solo Pedro/coordinación)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
MANUALES_DIR = os.path.join(D, 'recursos', 'manuales')
md_to_pdf(
    os.path.join(MANUALES_DIR, 'MANUAL_INTERNO_ESTRATEGIA_HEIIU.md'),
    os.path.join(MANUALES_DIR, 'MANUAL_INTERNO_ESTRATEGIA_HEIIU.pdf'),
)
print('OK: MANUAL_INTERNO_ESTRATEGIA_HEIIU.pdf (USO PRIVADO — NO compartir con profesores)')
