#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 12 — HOJA DE RUTA (2 tracks, solo GUIAS).
CONV (primero) + GRAMMAR (segundo, ~86% DE PIE). JUSTICIA v1 dia 2.
Modulo A2 Book M12 (p.99-102) — Past Simple IRREGULAR."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')

for track in ('CONV', 'GRAMMAR'):
    md_to_pdf(os.path.join(B1, f'B1_Clase12_{track}_PRINT.md'),
              os.path.join(B1, 'GUIAS', f'B1_Clase12_{track}_GUIA.pdf'))
    print(f'OK: B1_Clase12_{track}_GUIA.pdf')
print('2 PDFs Cl 12 generados (V2).')
