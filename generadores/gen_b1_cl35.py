#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 35 — HOJA DE RUTA (2 tracks). JUSTICIA v2 dia 5 (CIERRA):
- CONV (primero): Pricing Fairly + Budget/Quote Meeting. Prepara M33+M34 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M33 "How Much Money?" (uncountable,
  p.283-284) + M34 "How Much Does It Cost?" (prices, p.293-294). Emparejados por cierre.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase35_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase35_CONV_GUIA.pdf'))
print('OK: B1_Clase35_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase35_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase35_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase35_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 35 generadas (V2).')
