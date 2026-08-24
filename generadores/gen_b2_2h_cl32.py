#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B2 nocturno 2h Cl 32 — HOJA DE RUTA (Fase 2, el mundo profesional).
Cl 26-30 TEMPLANZA v2 · Cl 31-35 JUSTICIA v2. Fuente: Libro B1 (12 modulos, 155 pags)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B2_2H = os.path.join(D, 'VERSION_2', 'B2_2H')
os.makedirs(os.path.join(B2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B2_2H, 'B2_Clase32_PRINT.md'),
          os.path.join(B2_2H, 'GUIAS', 'B2_Clase32_GUIA.pdf'))
print('OK: B2_Clase32_GUIA.pdf')
