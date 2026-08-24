#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 21:
- ARCO DE REPASO A2->B1, clase 1 de 8: consolidacion M43 (adverbios de manera)
  + M44 (causativo activo) con la correccion como centro + apertura del arco.
- Libro A2 agotado en M44 (p.352): NO hay modulo nuevo.
- Virtud PRUDENCIA v2 dia 1 de 5. MY YEAR: primer ensayo de ensamble, piezas 1-5.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class21_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class21_GUIA.pdf'))
print('OK: A2_4h_Class21_GUIA.pdf')
