import sys
import os

BASE_REPO = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
sys.path.insert(0, BASE_REPO)

from gen_a1_a2_clases_pdfs import md_to_pdf

BASE = os.path.join(BASE_REPO, 'A2')

results = []
for n in range(48, 55):
    md = os.path.join(BASE, f'A2_Class{n}_PRINT.md')
    pdf = os.path.join(BASE, f'A2_Class{n}_GUIA.pdf')
    try:
        md_to_pdf(md_path=md, pdf_path=pdf)
        size = os.path.getsize(pdf) // 1024
        results.append(f'Cl {n}: OK ({size} KB)')
    except Exception as e:
        results.append(f'Cl {n}: FAIL - {type(e).__name__}: {e}')

print('\n'.join(results))
