#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A2 INTENSIVO 4H Cl 27 (cohorte nuevo):
- Media sesion: PRESENTACION FINAL MY YEAR (evento integrado, protocolo Cl 14).
- Media sesion: arco de repaso, cluster concordancia 3a persona + there is/are + causativo.
- Virtud TEMPLANZA v2 dia 2 de 3. Libro agotado en M44: sin modulo nuevo.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_4H = os.path.join(D, 'VERSION_2', 'A2_4H')
os.makedirs(os.path.join(A2_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_4H, 'A2_4h_Class27_PRINT.md'),
          os.path.join(A2_4H, 'GUIAS', 'A2_4h_Class27_GUIA.pdf'))
print('OK: A2_4h_Class27_GUIA.pdf')
