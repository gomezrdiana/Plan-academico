#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery nocturno 2h — Conv Cl 14/44 — HOJA DE RUTA.
Derivada de VERSION_2/B1_4H/CONVERSACION/B1_Clase14_CONV_PRINT.md (edicion unica manana/noche,
regla 13/10/2026): mismo contenido, envoltorio 2H (120 min, noche propia, PASE por el grupo,
video propio de la pista B1-2H-VIDEO-C-14). Correr desde la raiz del repo."""
import os
import fitz
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_2H = os.path.join(D, 'VERSION_2', 'B1_2H', 'CONVERSACION')
os.makedirs(os.path.join(B1_2H, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1_2H, 'REPORTES'), exist_ok=True)

pdf = os.path.join(B1_2H, 'GUIAS', 'B1_Clase14_CONV_GUIA.pdf')
md_to_pdf(os.path.join(B1_2H, 'B1_Clase14_CONV_PRINT.md'), pdf)
pages = fitz.open(pdf).page_count
kb = os.path.getsize(pdf) // 1024
print('OK: B1_Clase14_CONV_GUIA.pdf | %d KB | %d paginas%s' % (
    kb, pages, '' if pages <= 5 and kb > 2 else '  <-- REVISAR'))
