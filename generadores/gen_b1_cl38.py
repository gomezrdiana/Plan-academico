#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 38 — HOJA DE RUTA (2 tracks). FORTALEZA v2 dia 3:
- CONV: Whose is this? + The Handover Meeting. Prepara M39 oral.
- GRAMMAR (~86% DE PIE): A2 Book M39 "Mine, All Mine!" — Possessive Pronouns
  as Objects (whose + mine/yours/his/hers/ours/theirs + 's) (p.318-320).
  Frontera: Cl 39 = M41 (M40 NO existe) + FORTALEZA v2 dia 4.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase38_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase38_CONV_GUIA.pdf'))
print('OK: B1_Clase38_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase38_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase38_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase38_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 38 generadas (V2).')
