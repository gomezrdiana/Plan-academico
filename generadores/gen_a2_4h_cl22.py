#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 22:
- ARCO DE REPASO A2->B1, clase 2 de 8: CLUSTER TIEMPOS VERBALES
  (presente simple vs continuo · pasado simple vs continuo · presente perfecto vs pasado).
- Libro A2 agotado en M44 (p.352): NO hay modulo nuevo.
- Virtud PRUDENCIA v2 dia 2 de 5. MY YEAR: ensayo de ensamble, piezas 6-8.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class22_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class22_GUIA.pdf'))
print('OK: A2_4h_Class22_GUIA.pdf')
