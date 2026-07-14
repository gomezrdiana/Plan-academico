#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 36 — HOJA DE RUTA (2 tracks). ABRE FORTALEZA v2 (dia 1):
- CONV (primero): Describing Truly + Airport Pickup. Prepara M36+M37 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M36 "What Are You Wearing?" (clothing,
  p.301-304) + M37 "What Do You Look Like?" (describing people, p.307-310).
  M35 NO existe (salta 34->36). Emparejados por cierre de nivel.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase36_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase36_CONV_GUIA.pdf'))
print('OK: B1_Clase36_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase36_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase36_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase36_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 36 generadas (V2).')
