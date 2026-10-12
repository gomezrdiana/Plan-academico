#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B2 nocturno 2h Cl 50 — HOJA DE RUTA (Fase 2) con MIDTERM integrado. TEMPLANZA v3 dia 5. Fuente: Libro B1."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B2_2H = os.path.join(D, 'VERSION_2', 'B2_2H')
os.makedirs(os.path.join(B2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B2_2H, 'B2_Clase50_PRINT.md'),
          os.path.join(B2_2H, 'GUIAS', 'B2_Clase50_GUIA.pdf'))
print('OK: B2_Clase50_GUIA.pdf')
