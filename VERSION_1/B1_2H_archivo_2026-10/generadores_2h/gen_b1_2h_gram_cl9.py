#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Grammar Cl 8/44 — HOJA DE RUTA.
Sella en papel A1 Book M13 (Guia 1 p.167, Ejercicios 1 p.168): FRECUENCIA + A(N) + PERIODO
al final de la frase, sostenida con can/should/will/did. Virtud TEMPLANZA, Cl 4 de 5.
B3 REDISENADO por anti-duplicado = SAFETY AND MAINTENANCE LOG AUDIT
(la fuente 4H usaba SCHEDULE BRIEFING, casi identico al B3 de Conv Cl 8)."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'GRAMATICA')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase9_GRAMMAR_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase9_GRAMMAR_PRINT.md'), pdf)
d = open(pdf, 'rb').read()
print('OK: B1_Clase9_GRAMMAR_GUIA.pdf | %d KB | %d paginas' % (
    len(d) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', d))))
