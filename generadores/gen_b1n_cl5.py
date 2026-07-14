import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')

md_to_pdf(os.path.join(B1, 'B1_Clase5_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase5_CONV_GUIA.pdf'))
print('OK: B1_Clase5_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase5_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase5_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase5_GRAMMAR_GUIA.pdf')

print('2 PDFs Cl 5 generados (V2).')
