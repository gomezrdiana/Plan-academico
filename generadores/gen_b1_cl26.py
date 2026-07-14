#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 26 — HOJA DE RUTA (2 tracks). REPASO COMPRIMIDO A2 (libro B1 entra Cl 34).
ABRE TEMPLANZA v2 (dia 1). Modulos comprimidos HOY = M21 + M22 (familia gerundios):
- CONV (primero): rutinas (before/after/without + -ing) + metas (want to / love -ing).
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M21 (gerundio tras preposicion, p.197-200)
  + M22 (doble verbo to/-ing, p.207-209), activacion rapida + mezcla + simulacion.
  Anuncio Cl 27 = M23 + M24 (phrasal verbs) + TEMPLANZA v2 dia 2.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase26_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase26_CONV_GUIA.pdf'))
print('OK: B1_Clase26_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase26_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase26_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase26_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 26 generadas (V2).')
