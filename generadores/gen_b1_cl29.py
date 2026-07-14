#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 29 — HOJA DE RUTA (2 tracks). REPASO COMPRIMIDO A2 (libro B1 entra Cl 34).
TEMPLANZA v2 dia 4. Modulos comprimidos HOY = M29 + M30 (grados/intensificadores + so/too/enough):
- CONV (primero): describir con la intensidad justa en el trabajo (very/quite/too/enough).
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M29 (grados/intensificadores) + M30 (so/too/enough),
  activacion rapida + mezcla + simulacion integradora.
  Anuncio Cl 30 = quantities and prices (how many / how much) + TEMPLANZA v2 dia 5.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'CONVERSACION', 'GUIAS'), exist_ok=True); os.makedirs(os.path.join(B1, 'GRAMATICA', 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'CONVERSACION', 'B1_Clase29_CONV_PRINT.md'),
          os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase29_CONV_GUIA.pdf'))
print('OK: B1_Clase29_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'GRAMATICA', 'B1_Clase29_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase29_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase29_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 29 generadas (V2).')
