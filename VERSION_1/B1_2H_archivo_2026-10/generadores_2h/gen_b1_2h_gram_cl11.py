#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Grammar Cl 11/44 — HOJA DE RUTA.
Sella en papel A2 Book M12 (mitad regular) + A1 Book M10 (Guia 1 p.125, Ejemplos p.126): 4 familias
de ortografia del -ED, 3 sonidos del libro, dictado. De pie ~87%. Virtud JUSTICIA, Cl 1 de 5: ABRE
(angulo: corregir sin humillar). B3 REDISENADO por anti-duplicado = PACKAGE TRACE AT THE COURIER
COUNTER (la fuente 4H usaba WORKDAY BRIEFING, casi identico al WORKDAY DEBRIEF de Conv)."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'GRAMATICA')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase11_GRAMMAR_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase11_GRAMMAR_PRINT.md'), pdf)
d = open(pdf, 'rb').read()
print('OK: B1_Clase11_GRAMMAR_GUIA.pdf | %d KB | %d paginas' % (
    len(d) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', d))))
