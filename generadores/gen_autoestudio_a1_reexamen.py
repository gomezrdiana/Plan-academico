#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera los 3 PDFs de AUTOESTUDIO A1 REEXAMEN (guias para la ESTUDIANTE).
PRINT.md ya estan en refuerzos/. Aqui solo se convierten a PDF.
"""
import sys, os
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
sys.path.insert(0, BASE)
os.makedirs(os.path.join(BASE, 'refuerzos'), exist_ok=True)
from gen_a1_a2_clases_pdfs import md_to_pdf

for n in (1, 2, 3):
    md = os.path.join(BASE, 'refuerzos', f'AUTOESTUDIO_A1_REEXAMEN_Sesion{n}_PRINT.md')
    pdf = os.path.join(BASE, 'refuerzos', f'AUTOESTUDIO_A1_REEXAMEN_Sesion{n}_GUIA.pdf')
    md_to_pdf(md_path=md, pdf_path=pdf)
