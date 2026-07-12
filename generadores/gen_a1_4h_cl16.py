#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera SOLO la guia del A1 INTENSIVO 4H Cl 16:
- M22 You're Not Juan! (be negativo, p.269-274) + M23 Are You Juan? (be interrogativo, p.275-282), PAR.
- Virtud FORTALEZA v1 dia 1. Recuperacion N-3 Cl 13 / N-7 Cl 9. Simulacion FIRST DAY CHECK-IN.
- Pieza 14 TRUE OR FALSE ABOUT ME. FRONTERA: libro en M23 (p.282); Cl 17 = M24. Libro = 36 modulos (M0-M35).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(os.path.join(A1_4H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class16_PRINT.md'),
          os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class16_GUIA.pdf'))
print('OK: A1_4h_Class16_GUIA.pdf')
