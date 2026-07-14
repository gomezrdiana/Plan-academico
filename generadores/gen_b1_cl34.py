#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 34 — HOJA DE RUTA (2 tracks). JUSTICIA v2 dia 4:
- CONV (primero): Counting Fairly + Staffing Meeting. Prepara M32 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M32 "How Many People Are There?" —
  countable quantities (how many / many / a few / a lot of, p.273-275).
  M31 NO existe (salta 30->32).
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase34_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase34_CONV_GUIA.pdf'))
print('OK: B1_Clase34_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase34_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase34_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase34_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 34 generadas (V2).')
