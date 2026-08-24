#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 28 (ULTIMA CLASE DEL NIVEL):
- Primeras 2h: mastery integrado de los 7 clusters del arco + cierre del nivel.
- Ultimas 2h: FINAL del nivel aplicado por EVALUADOR EXTERNO (marcador, sin guia pedagogica).
- Virtud TEMPLANZA v2 dia 3 de 3. Libro agotado en M44: sin modulo nuevo. Sin tarea.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class28_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class28_GUIA.pdf'))
print('OK: A2_4h_Class28_GUIA.pdf')
