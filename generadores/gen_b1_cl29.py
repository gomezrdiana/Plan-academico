#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 29 — HOJA DE RUTA (2 tracks). TEMPLANZA v2 dia 4:
- CONV (primero): Running the Logistics + Event Coordination Call. Prepara M24 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M24 "I'll Pick You Up at 8:00" —
  Separable Phrasal Verbs (pronombre en medio: pick her up / turn it off) (p.233-236).
  Anuncio Cl 30 = M26 comparativos iguales (M25 NO existe) + TEMPLANZA v2 dia 5.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase29_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase29_CONV_GUIA.pdf'))
print('OK: B1_Clase29_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase29_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase29_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase29_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 29 generadas (V2).')
