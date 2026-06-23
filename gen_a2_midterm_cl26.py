#!/usr/bin/env python3
"""Genera 3 PDFs para el MIDTERM A2 PM Nocturno (Cl 26, jueves 14/05/2026):
- A2_Class26_MIDTERM_PRINT — marcador del día (profesor NO asiste)
- A2_Class26_MIDTERM_COORD_KIT — kit operativo para Diana
- A2_Class26_MIDTERM_RUBRICA — 1 hoja por estudiante para evaluar
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')

files = [
    ('A2_Class26_MIDTERM_PRINT',       'A2_Class26_MIDTERM_MARKER.pdf'),
    ('A2_Class26_MIDTERM_COORD_KIT',   'A2_Class26_MIDTERM_COORD_KIT.pdf'),
    ('A2_Class26_MIDTERM_RUBRICA',     'A2_Class26_MIDTERM_RUBRICA.pdf'),
]

for md_name, pdf_name in files:
    md_to_pdf(
        os.path.join(A2_DIR, f'{md_name}.md'),
        os.path.join(A2_DIR, pdf_name),
    )

print(f'\n{len(files)} PDFs MIDTERM A2 PM Cl 26 generados:')
for _, pdf in files:
    print(f'  - A2/{pdf}')
