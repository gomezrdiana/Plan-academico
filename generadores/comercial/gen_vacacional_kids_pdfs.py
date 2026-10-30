# -*- coding: utf-8 -*-
"""Renderiza los PDFs del vacacional de ninos (7 a 12)."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from gen_a1_a2_clases_pdfs import md_to_pdf
D = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'VACACIONAL_KIDS')
for name in ['FICHA_VACACIONAL_PADRES', 'PLAN_SEMANAS_PROFE', 'MENSAJES_VACACIONAL', 'FICHA_INSCRIPCION_NINO']:
    md_to_pdf(os.path.join(D, name + '.md'), os.path.join(D, name + '.pdf'))
    print(name, os.path.getsize(os.path.join(D, name + '.pdf')), 'bytes')
