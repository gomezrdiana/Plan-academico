#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 33 — HOJA DE RUTA (2 tracks). REPASO COMPRIMIDO A2.
CIERRE DEL LIBRO A2. JUSTICIA v2 dia 3:
- CONV (primero): Get / Adverbs / I Want You To + Weekly Debrief. Prepara M42-M44 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M42 "Getting Crazy!" (get + adjetivo,
  p.334-335) + M43 "How Do You Do?" (adverbios de manera -ly, p.341-342) + M44
  "I Want You to Go" (causativo activo, p.347-348, ULTIMO modulo del libro A2).
  M44 cierra el libro como hito verbal. Frontera de salida: Cl 34 abre el LIBRO B1
  Module 1.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'CONVERSACION', 'GUIAS'), exist_ok=True); os.makedirs(os.path.join(B1, 'GRAMATICA', 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'CONVERSACION', 'B1_Clase33_CONV_PRINT.md'),
          os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase33_CONV_GUIA.pdf'))
print('OK: B1_Clase33_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'GRAMATICA', 'B1_Clase33_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase33_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase33_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 33 generadas (V2).')
