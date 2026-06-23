#!/usr/bin/env python3
"""Genera los PDFs de la reunion general de profesores Heiiu:
- AGENDA_REUNION_PROFESORES.pdf (agenda + talking points 2h 15min)
- MATERIAL_SOPORTE_REUNION.pdf (4 hojas operativas para entregar a profes)
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(D, 'documentos_operativos')

md_to_pdf(os.path.join(DOCS, 'AGENDA_REUNION_PROFESORES_PRINT.md'),
          os.path.join(DOCS, 'AGENDA_REUNION_PROFESORES.pdf'))
print('OK: AGENDA_REUNION_PROFESORES.pdf')

md_to_pdf(os.path.join(DOCS, 'MATERIAL_SOPORTE_REUNION_PRINT.md'),
          os.path.join(DOCS, 'MATERIAL_SOPORTE_REUNION.pdf'))
print('OK: MATERIAL_SOPORTE_REUNION.pdf')

print('\nReunion profesores - 2 PDFs generados:')
print('  - documentos_operativos/AGENDA_REUNION_PROFESORES.pdf')
print('  - documentos_operativos/MATERIAL_SOPORTE_REUNION.pdf')
