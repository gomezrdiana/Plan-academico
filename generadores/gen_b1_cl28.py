#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 28 — HOJA DE RUTA (2 tracks). TEMPLANZA v2 dia 3:
- CONV (primero): The People I Work With + Onboarding Buddy. Prepara M23 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M23 "I Asked for A Pencil" — Basic
  Non-Separable Phrasal Verbs (look after / listen to / ask for) (p.221-224).
  Anuncio Cl 29 = M24 phrasal verbs separables + TEMPLANZA v2 dia 4.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase28_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase28_CONV_GUIA.pdf'))
print('OK: B1_Clase28_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase28_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase28_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase28_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 28 generadas (V2).')
