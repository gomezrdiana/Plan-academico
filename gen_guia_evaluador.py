#!/usr/bin/env python3
"""Genera PDF de la guia del evaluador (venta invisible)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
MANUALES_DIR = os.path.join(D, 'recursos', 'manuales')
md_to_pdf(
    os.path.join(MANUALES_DIR, 'GUIA_EVALUADOR_VENTA_INVISIBLE.md'),
    os.path.join(MANUALES_DIR, 'GUIA_EVALUADOR_VENTA_INVISIBLE.pdf'),
)
print('OK: GUIA_EVALUADOR_VENTA_INVISIBLE.pdf')
print('USO INTERNO — NO compartir fuera del equipo de evaluacion y coordinacion.')
