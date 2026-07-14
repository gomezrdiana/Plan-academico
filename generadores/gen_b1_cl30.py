#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 30 — HOJA DE RUTA (2 tracks). CIERRA TEMPLANZA v2 (dia 5):
- CONV (primero): Weighing Two Options + Procurement Meeting. Prepara M26 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M26 "I'm as Big as My Dad" — Equal
  Comparatives (as ... as / not as ... as / almost as ... as) (p.241-244).
  M25 NO EXISTE (salta M24 -> M26). Anuncio Cl 31 = M27 comparativos desiguales
  + JUSTICIA v2 dia 1.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase30_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase30_CONV_GUIA.pdf'))
print('OK: B1_Clase30_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase30_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase30_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase30_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 30 generadas (V2).')
