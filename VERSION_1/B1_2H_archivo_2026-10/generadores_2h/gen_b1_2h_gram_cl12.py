#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Grammar Cl 12/44 — HOJA DE RUTA.
Sella en papel A2 Book M12 (mitad irregular) + A1 Book M11 (Guia 1 p.143, Ejemplos p.144): 5 grupos
de irregulares, trampa READ, dictado. De pie ~87%. Virtud JUSTICIA, Cl 2 de 5 (angulo: honestidad
con lo que es de todos). B3 REDISENADO por anti-duplicado = EXPENSE REPORT REVIEW AFTER A BUSINESS
TRIP (la fuente 4H usaba PROJECT DEBRIEF, mismo guion de reporte de equipo que el STAND-UP de Conv)."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'GRAMATICA')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase12_GRAMMAR_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase12_GRAMMAR_PRINT.md'), pdf)
d = open(pdf, 'rb').read()
print('OK: B1_Clase12_GRAMMAR_GUIA.pdf | %d KB | %d paginas' % (
    len(d) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', d))))
