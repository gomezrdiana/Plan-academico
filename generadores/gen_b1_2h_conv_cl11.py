#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Conv Cl 11/44 — HOJA DE RUTA.
Modulo A2 Book M12 (p.99-102), mitad pasado simple REGULAR + A1 Book M10 Guia 1 p.125, solo USO ORAL.
Virtud JUSTICIA, Cl 1 de 5 (Cl 11-15): ABRE el bloque (angulo: credito a quien hizo el trabajo).
B3 = YESTERDAY'S WORKDAY DEBRIEF (guest-observer, docente coach). Tarea = solo video No. 21.
Derivada de VERSION_2/B1_4H/CONVERSACION/B1_Clase11_CONV_PRINT.md, adaptada a 120 min."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'CONVERSACION')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase11_CONV_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase11_CONV_PRINT.md'), pdf)
d = open(pdf, 'rb').read()
print('OK: B1_Clase11_CONV_GUIA.pdf | %d KB | %d paginas' % (
    len(d) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', d))))
