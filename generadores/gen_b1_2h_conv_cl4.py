#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — CONVERSACION Cl 4/44 — HOJA DE RUTA.
Derivada de VERSION_2/B1_4H/CONVERSACION/B1_Clase4_CONV_PRINT.md, adaptada a 120 min
(6:30-8:30 PM), con VATS de 6 min, chequeo de portafolio con lista en mano, tarea = solo
el video diario (la escrita es de Gramatica) y PASE escrito a Grammar Cl 4.
Virtud Cl 1-5 de cada pista = PRUDENCIA."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'CONVERSACION')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase4_CONV_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase4_CONV_PRINT.md'), pdf)
raw = open(pdf, 'rb').read()
pages = len(re.findall(rb'/Type\s*/Page[^s]', raw))
print('OK: B1_Clase4_CONV_GUIA.pdf  |  %d KB  |  %d paginas%s' % (
    len(raw) // 1024, pages, '' if pages <= 5 else '  <-- EXCEDE 5 PAGINAS'))
