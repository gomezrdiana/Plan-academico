#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 37 — HOJA DE RUTA (2 tracks). FORTALEZA v2 dia 2:
- CONV (primero): The Full Picture in Order + Product Spec Desk. Prepara M38 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M38 "Order of Adjectives" (p.313-315).
  Consolida M36-M37.
  Frontera de salida: Cl 38 = M39 possessive pronouns (verificar) + FORTALEZA v2 dia 3.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase37_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase37_CONV_GUIA.pdf'))
print('OK: B1_Clase37_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase37_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase37_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase37_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 37 generadas (V2).')
