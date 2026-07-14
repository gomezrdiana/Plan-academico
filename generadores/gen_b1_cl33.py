#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 33 — HOJA DE RUTA (2 tracks). JUSTICIA v2 dia 3:
- CONV (primero): The Right Level + Workload Review. Prepara M30 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M30 "Too Much or Just Enough?" —
  so/too/enough (p.267-269). M31 NO existe (salta 30->32).
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase33_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase33_CONV_GUIA.pdf'))
print('OK: B1_Clase33_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase33_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase33_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase33_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 33 generadas (V2).')
