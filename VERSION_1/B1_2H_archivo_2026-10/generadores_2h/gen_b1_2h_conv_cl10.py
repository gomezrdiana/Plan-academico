#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Conv Cl 10/44 — HOJA DE RUTA. HITO DEL NIVEL.
Modulo A1 Book M16 "I Like It!" (Guia 1 p.199; ejemplos p.201; rango p.197-201), solo USO ORAL.
Virtud TEMPLANZA, Cl 5 de 5 (Cl 6-10): CIERRA el bloque, con retrospectiva en el B4.
B3 = HITO ENTREVISTA SIMULADA (3 min por candidato, 1 toma, grabada por el docente;
patron guest-observer, docente coach). Las 6 preguntas reciclan Cl 3, 7, 8, 9 y 10.
Derivada de VERSION_2/B1_4H/CONVERSACION/B1_Clase10_CONV_PRINT.md (cuyo B3 era
WEEKLY FOLLOW-UP), adaptada a 120 min con los 10 min extra al Bloque 3."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'CONVERSACION')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase10_CONV_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase10_CONV_PRINT.md'), pdf)
d = open(pdf, 'rb').read()
print('OK: B1_Clase10_CONV_GUIA.pdf | %d KB | %d paginas' % (
    len(d) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', d))))
