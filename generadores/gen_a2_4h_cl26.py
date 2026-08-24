#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 26:
- ARCO DE REPASO A2->B1, cluster PREPOSICIONES + ARTICULOS + CANTIDADES.
- Libro A2 agotado en M44 (Cl 20): no hay modulo nuevo.
- Virtud TEMPLANZA v2 dia 1 de 3 (apertura de bloque parcial: el nivel cierra en Cl 28).
- MY YEAR: ensayo de piezas 18-19 + tarea de armar la presentacion final de Cl 27.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class26_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class26_GUIA.pdf'))
print('OK: A2_4h_Class26_GUIA.pdf')
