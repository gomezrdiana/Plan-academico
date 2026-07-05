import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Generate PDFs for B1 Conv classes Cl 39-43."""
import sys
sys.path.insert(0, r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu')
from gen_a1_a2_clases_pdfs import md_to_pdf

CLASSES = [39, 40, 41, 42, 43]

for n in CLASSES:
    md = rf'B1\B1_Clase{n}_CONV_PRINT.md'
    pdf = rf'B1\B1_Clase{n}_CONV_GUIA.pdf'
    print(f'Generating {pdf}...')
    md_to_pdf(md_path=md, pdf_path=pdf)
    print(f'  done')

print('All done.')
