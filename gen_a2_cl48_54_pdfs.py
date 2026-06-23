#!/usr/bin/env python3
"""
Genera PDFs B&W para las guias A2 Nocturno Cl 48-54 (immersive 4-block model).
Reutiliza md_to_pdf de gen_a1_a2_clases_pdfs.
"""
import sys, os
sys.path.insert(0, r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu')
from gen_a1_a2_clases_pdfs import md_to_pdf

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\A2'

for n in [48, 49, 50, 51, 52, 53, 54]:
    md = os.path.join(BASE, f'A2_Class{n}_PRINT.md')
    pdf = os.path.join(BASE, f'A2_Class{n}_GUIA.pdf')
    md_to_pdf(md_path=md, pdf_path=pdf)
    size_kb = os.path.getsize(pdf) / 1024
    print(f'Cl {n}: {pdf}  ({size_kb:.1f} KB)')
