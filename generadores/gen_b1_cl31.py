#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 31 — HOJA DE RUTA (2 tracks). ABRE JUSTICIA v2 (dia 1):
- CONV (primero): The Fair Recommendation + Hiring Panel. Prepara M27 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M27 "I'm Smarter than Steve" — Unequal
  Comparatives (-er/-ier/more ... than + better/worse) (p.247-249).
  Frontera de salida: Cl 32 = M28 (siguiente modulo existente) + JUSTICIA v2 dia 2.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase31_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase31_CONV_GUIA.pdf'))
print('OK: B1_Clase31_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase31_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase31_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase31_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 31 generadas (V2).')
