#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h Cl 1/88 — CONVERSACION — HOJA DE RUTA (apertura del nivel).
Cohorte nuevo 28/09/2026, 6:30-8:30 PM, dias alternos Conv (impares) / Grammar (pares)
con DOS profesores y PASE escrito bidireccional entre dias.
Virtud Cl 1-5 = PRUDENCIA v1. Modulo ancla: A2 Book M17 p.163-164 (uso oral)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

md_to_pdf(os.path.join(B1_2H, 'B1_Clase1_CONV_PRINT.md'),
          os.path.join(B1_2H, 'GUIAS', 'B1_Clase1_CONV_GUIA.pdf'))
print('OK: B1_Clase1_CONV_GUIA.pdf')
