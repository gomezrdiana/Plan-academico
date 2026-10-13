import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery 4H Cl 1 (CONV 8:00 + GRAMMAR 10:00). Edicion unificada 13/10: contenido de la maestra B1_2H Cl 1 con envoltorio 4H (110 min, PASE mismo dia)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')

def _gen(md, pdf):
    try:
        md_to_pdf(md, pdf); print('OK:', os.path.basename(pdf))
    except PermissionError:
        alt = pdf.replace('_GUIA.pdf', '_GUIA_NUEVA.pdf')
        md_to_pdf(md, alt); print('PDF ABIERTO -> escrito como', os.path.basename(alt))

_gen(os.path.join(B1, 'CONVERSACION', 'B1_Clase1_CONV_PRINT.md'),
     os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase1_CONV_GUIA.pdf'))
_gen(os.path.join(B1, 'GRAMATICA', 'B1_Clase1_GRAMMAR_PRINT.md'),
     os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase1_GRAMMAR_GUIA.pdf'))
print('2 PDFs Cl 1 generados (V2).')
