#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 38 — HOJA DE RUTA (2 tracks). FORTALEZA v2 dia 3:
- CONV: What did they say? + The Message Relay. Aplica M8 oral.
- GRAMMAR (~86% DE PIE): B1 Book M8 "Reported Speech — He Said, She Said"
  (say/tell/ask + back-shift table) (p.83-96).
  Frontera: Cl 39 = M9 Perfect Tenses + FORTALEZA v2 dia 4.
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
