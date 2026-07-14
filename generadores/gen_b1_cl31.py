#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 31 — HOJA DE RUTA (2 tracks). REPASO COMPRIMIDO A2.
ABRE JUSTICIA v2 (dia 1):
- CONV (primero): Describing People & Clothes + Front Desk. Prepara M36-M38 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M36 (ropa/colores, p.301-305) + M37
  (describir personas be/have, p.307-310) + M38 (orden de adjetivos, p.313-315).
  Familia DESCRIPCION. M35 y M40 NO EXISTEN. Frontera de salida: Cl 32 = M39+M41
  + JUSTICIA v2 dia 2. Libro B1 entra Cl 34.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'CONVERSACION', 'GUIAS'), exist_ok=True); os.makedirs(os.path.join(B1, 'GRAMATICA', 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'CONVERSACION', 'B1_Clase31_CONV_PRINT.md'),
          os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase31_CONV_GUIA.pdf'))
print('OK: B1_Clase31_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'GRAMATICA', 'B1_Clase31_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase31_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase31_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 31 generadas (V2).')
