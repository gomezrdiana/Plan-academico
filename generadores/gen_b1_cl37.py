#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 37 — HOJA DE RUTA (2 tracks). FORTALEZA v2 dia 2. CIERRA PRIMERA
MITAD del libro B1 (M1-M7):
- CONV (primero): Combining Ideas (relative pronouns) + The Courteous Inquiry.
- GRAMMAR (segundo, ~86% DE PIE): B1 Book M7 "Relative Pronouns & Embedded Questions"
  (p.63-81), modulo denso -> sesion de un solo modulo.
  Frontera de salida: Cl 38 = M8 "Reported Speech" (p.83+). Libro B1 = 12 modulos.
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
