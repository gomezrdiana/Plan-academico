#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 25:
- ARCO DE REPASO A2->B1, cluster PREGUNTAS / NEGATIVOS / ORDEN DE AUXILIARES.
- Libro A2 agotado en M44 (Cl 20): no hay modulo nuevo.
- Virtud PRUDENCIA v2 dia 5 de 5 (cierre); Cl 26-28 = TEMPLANZA v2 parcial.
- MY YEAR: ensayo de piezas 16-17 (sin piezas nuevas).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class25_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class25_GUIA.pdf'))
print('OK: A2_4h_Class25_GUIA.pdf')
