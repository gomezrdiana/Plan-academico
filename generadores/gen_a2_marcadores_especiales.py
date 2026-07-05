#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera/regenera los MARCADORES de secuencia A2 PM Nocturno (días especiales
que consumen numero consecutivo de clase con contenido especial):
- Cl 25 PRESENTACIONES (mie 13/05) -> A2_Class25_PRESENTACIONES_MARKER.pdf
- Cl 26 MIDTERM        (jue 14/05) -> A2_Class26_MIDTERM_MARKER.pdf  (regenerado, refs corregidas)
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')

files = [
    ('A2_Class25_PRESENTACIONES_PRINT', 'A2_Class25_PRESENTACIONES_MARKER.pdf'),
    ('A2_Class26_MIDTERM_PRINT',        'A2_Class26_MIDTERM_MARKER.pdf'),
]

for md_name, pdf_name in files:
    md_to_pdf(
        os.path.join(A2_DIR, f'{md_name}.md'),
        os.path.join(A2_DIR, pdf_name),
    )

print(f'\n{len(files)} marcadores A2 PM generados:')
for _, pdf in files:
    print(f'  - A2/{pdf}')
