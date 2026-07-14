#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 32 — HOJA DE RUTA (2 tracks). REPASO COMPRIMIDO A2.
JUSTICIA v2 dia 2:
- CONV (primero): Whose Is It? / Tiring vs Tired + Project Handover. Prepara M39+M41 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M39 "Mine, All Mine!" (pronombres
  posesivos + whose, p.318-319) + M41 "This Is Interesting!" (participios -ed/-ing,
  p.327-328). M40 NO EXISTE (salta 39->41). Frontera: Cl 33 = M42-M44 (cierre del
  libro A2) + JUSTICIA v2 dia 3. Libro B1 entra Cl 34.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase32_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase32_CONV_GUIA.pdf'))
print('OK: B1_Clase32_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase32_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase32_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase32_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 32 generadas (V2).')
