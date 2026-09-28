#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Grammar Cl 6/44 — GRAMATICA — HOJA DE RUTA.
Derivada de VERSION_2/B1_4H/GRAMATICA/B1_Clase6_GRAMMAR_PRINT.md, adaptada a 120 min.
Sella en papel lo que Conv Cl 6 hablo la noche anterior. B3 con escenario DISTINTO
al de Conv Cl 6 (regla de no duplicacion entre pistas). ~87% de pie."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'GRAMATICA')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase6_GRAMMAR_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase6_GRAMMAR_PRINT.md'), pdf)
_b = open(pdf, 'rb').read()
print('OK: B1_Clase6_GRAMMAR_GUIA.pdf  %d KB  paginas=%d'
      % (len(_b) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', _b))))
