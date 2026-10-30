# -*- coding: utf-8 -*-
"""Renderiza los PDFs del producto de nicho salud (Ingles para el turno)."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'NICHO_SALUD')
for name in ['FICHA_INGLES_PARA_EL_TURNO', 'SIMULACIONES_12_SESIONES', 'MENSAJES_VENTA_SALUD', 'HOJA_CLINICAS_B2B']:
    md = os.path.join(D, name + '.md'); pdf = os.path.join(D, name + '.pdf')
    md_to_pdf(md, pdf)
    print(name, os.path.getsize(pdf), 'bytes')
