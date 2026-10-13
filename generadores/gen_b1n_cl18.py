import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery 4H (manana) — Cl 18/44, CONV (8:00) + GRAMMAR (10:00), mismo dia.
Edicion nueva (regla 13/10/2026, una sola edicion manana/noche): reescrita desde la
guia 4H anterior (25/08) con el formato de las Cl 1-12. Correr desde la raiz del repo."""
import os
import fitz
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')

for folder, track in (('CONVERSACION', 'CONV'), ('GRAMATICA', 'GRAMMAR')):
    os.makedirs(os.path.join(B1, folder, 'GUIAS'), exist_ok=True)
    pdf = os.path.join(B1, folder, 'GUIAS', 'B1_Clase18_%s_GUIA.pdf' % track)
    md_to_pdf(os.path.join(B1, folder, 'B1_Clase18_%s_PRINT.md' % track), pdf)
    pages = fitz.open(pdf).page_count
    kb = os.path.getsize(pdf) // 1024
    print('OK: B1_Clase18_%s_GUIA.pdf | %d KB | %d paginas%s' % (
        track, kb, pages, '' if pages <= 5 and kb > 2 else '  <-- REVISAR'))
