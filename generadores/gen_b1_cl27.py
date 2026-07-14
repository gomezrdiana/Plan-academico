#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 27 — HOJA DE RUTA (2 tracks). REPASO COMPRIMIDO A2 (libro B1 entra Cl 34).
TEMPLANZA v2 dia 2. Modulos comprimidos HOY = M23 + M24 (familia phrasal verbs):
- CONV (primero): personas que manejas (look after/listen to/ask for) + cosas que
  cambias (turn it off / pick her up), aplicacion oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M23 (no separables, objeto al final, p.221-224)
  + M24 (separables, pronombre en medio, p.233-236), activacion rapida + mezcla + simulacion.
  Anuncio Cl 28 = M26 + M27 + M28 (comparacion completa; M25 NO existe) + TEMPLANZA v2 dia 3.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'CONVERSACION', 'GUIAS'), exist_ok=True); os.makedirs(os.path.join(B1, 'GRAMATICA', 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'CONVERSACION', 'B1_Clase27_CONV_PRINT.md'),
          os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase27_CONV_GUIA.pdf'))
print('OK: B1_Clase27_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'GRAMATICA', 'B1_Clase27_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase27_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase27_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 27 generadas (V2).')
