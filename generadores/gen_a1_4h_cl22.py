#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 INTENSIVO 4H Cl 22:
- CIERRE DEL NIVEL (protocolo dia completo): PRESENTACIONES FINALES MY WORLD (proyecto completo) + circuito
  de consolidacion de todo el nivel + ticket reflexivo final. Profe conduce/cronometra, NO evalua NI comunica.
- Virtud PRUDENCIA v2 dia 2 (parcial, el nivel termina). Cl 23 = examen final (evaluador externo, SIN guia).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(os.path.join(A1_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class22_PRINT.md'),
          os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class22_GUIA.pdf'))
print('OK: A1_4h_Class22_GUIA.pdf')
