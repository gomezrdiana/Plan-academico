#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Conv Cl 8/44 — HOJA DE RUTA.
Modulo A1 Book M13 "We Play Hockey Twice a Week" (Guia 1 p.167; rango p.165-169), solo USO ORAL.
Virtud TEMPLANZA, Cl 3 de 5 (Cl 6-10). B3 = RECURRING-MEETING SCHEDULING.
Derivada de VERSION_2/B1_4H/CONVERSACION/B1_Clase9_CONV_PRINT.md, adaptada a 120 min."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'CONVERSACION')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase9_CONV_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase9_CONV_PRINT.md'), pdf)
d = open(pdf, 'rb').read()
print('OK: B1_Clase9_CONV_GUIA.pdf | %d KB | %d paginas' % (
    len(d) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', d))))
