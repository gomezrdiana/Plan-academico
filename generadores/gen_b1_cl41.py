#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 41 — HOJA DE RUTA (2 tracks). SINTESIS dia 1 (PRUDENCIA+FORTALEZA):
- CONV: Everyone/someone/myself + The Closing Roundtable. Aplica M12 oral.
- GRAMMAR (~86% DE PIE): B1 Book M12 "Advanced Pronouns — I Can Do It Myself!"
  (indefinite p.147 + reflexive p.151 + reciprocal p.155) (p.145-155).
  M12 = ULTIMO modulo del libro B1 (CIERRA M1-M12; abre SINTESIS).
  Frontera: Cl 42 = armado de PRESENTACION FINAL + SINTESIS dia 2. Cl 44 = Final externo.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase41_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase41_CONV_GUIA.pdf'))
print('OK: B1_Clase41_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase41_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase41_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase41_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 41 generadas (V2).')
