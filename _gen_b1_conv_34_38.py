import sys
import os
sys.path.insert(0, r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu')
from gen_a1_a2_clases_pdfs import md_to_pdf

base = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\B1'
for n in (34, 35, 36, 37, 38):
    md = os.path.join(base, f'B1_Clase{n}_CONV_PRINT.md')
    pdf = os.path.join(base, f'B1_Clase{n}_CONV_GUIA.pdf')
    print(f'== Cl {n} ==')
    print(f'  MD : {md}  exists={os.path.exists(md)}')
    md_to_pdf(md_path=md, pdf_path=pdf)
    size = os.path.getsize(pdf) if os.path.exists(pdf) else -1
    print(f'  PDF: {pdf}  size={size} bytes ({size//1024} KB)')
print('DONE')
