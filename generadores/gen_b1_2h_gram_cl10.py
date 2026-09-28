#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Grammar Cl 10/44 — HOJA DE RUTA.
Sella en papel A1 Book M16 "I Like It!" (Guia 1 p.199; Ejemplos p.201): tabla sujeto-objeto,
los 7 pronombres objeto tras verbo y tras preposicion, afirmativo y negativo del libro.
CIERRA EL HITO de Conv Cl 10 con la NOTA DE SEGUIMIENTO escrita a mano en clase (12' sentados;
de pie ~78%). Virtud TEMPLANZA, Cl 5 de 5: CIERRA el bloque, con retrospectiva.
B3 REDISENADO por anti-duplicado = REFERENCE CHECK CALL (tercera persona, candidato ausente;
la fuente 4H usaba FOLLOW-UP BRIEFING, casi identico al WEEKLY FOLLOW-UP de Conv)."""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'GRAMATICA')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase10_GRAMMAR_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase10_GRAMMAR_PRINT.md'), pdf)
d = open(pdf, 'rb').read()
print('OK: B1_Clase10_GRAMMAR_GUIA.pdf | %d KB | %d paginas' % (
    len(d) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', d))))
