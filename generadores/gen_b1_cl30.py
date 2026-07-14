#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 30 — HOJA DE RUTA (2 tracks). REPASO COMPRIMIDO A2.
CIERRA TEMPLANZA v2 (dia 5):
- CONV (primero): How Many / How Much / Prices + Supply Order. Prepara M32-M34 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M32 (how many, p.273-275) + M33
  (how much, p.283-285) + M34 (precios be/cost + each, p.293-294). Familia
  CANTIDADES/PRECIOS. M31 y M35 NO EXISTEN (huecos). Anuncio Cl 31 = cluster
  DESCRIPCION M36-M38 + JUSTICIA v2 dia 1. Libro B1 entra Cl 34.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'CONVERSACION', 'GUIAS'), exist_ok=True); os.makedirs(os.path.join(B1, 'GRAMATICA', 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'CONVERSACION', 'B1_Clase30_CONV_PRINT.md'),
          os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase30_CONV_GUIA.pdf'))
print('OK: B1_Clase30_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'GRAMATICA', 'B1_Clase30_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase30_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase30_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 30 generadas (V2).')
