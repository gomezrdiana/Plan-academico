import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 Mastery 4H Cl 2 (CONV 8:00 + GRAMMAR 10:00). Edicion unificada 13/10: contenido de la maestra B1_2H Cl 2 con envoltorio 4H (110 min, PASE mismo dia)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')

md_to_pdf(os.path.join(B1, 'CONVERSACION', 'B1_Clase2_CONV_PRINT.md'),
          os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase2_CONV_GUIA.pdf'))
print('OK: B1_Clase2_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'GRAMATICA', 'B1_Clase2_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase2_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase2_GRAMMAR_GUIA.pdf')

print('2 PDFs Cl 2 generados (V2).')
