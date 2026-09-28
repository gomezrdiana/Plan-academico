#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h Cl 2/88 — GRAMATICA — HOJA DE RUTA.
Clase par (29/09/2026, 6:30-8:30 PM): la dicta el profe de GRAMATICA, que NO estuvo en la Cl 1.
Sella en papel M17 capa 2 (negativo didn't vs haven't, pregunta con short answer, for,
participios, Exercises 1 p.165). Virtud PRUDENCIA v2 (dia 2 de 5).
B3 = INCIDENT REPORT TO HR (distinto de MEET THE NEW TEAM de Conv Cl 1)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'GRAMATICA')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

md_to_pdf(os.path.join(B1_2H, 'B1_Clase2_GRAMMAR_PRINT.md'),
          os.path.join(B1_2H, 'GUIAS', 'B1_Clase2_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase2_GRAMMAR_GUIA.pdf')
