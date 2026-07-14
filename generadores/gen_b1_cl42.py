#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 42 — HOJA DE RUTA (2 tracks). SINTESIS dia 2 (TEMPLANZA+JUSTICIA):
Re-anclada al LIBRO B1 COMPLETO (M1-M12) cerrado en Cl 41.
- CONV: Build the Skeleton (proyecto final MY STORY, 3 partes) + primer ensayo.
  La presentacion luce las estructuras del curso B1.
- GRAMMAR (~86% DE PIE): Taller de precision del pitch (5 estructuras: reported
  speech/back-shift M8, perfect tenses M9, relative/embedded M7, question tags M1,
  comparativos) + ensayo general. NO modulo nuevo (libro cerrado en Cl 41).
  SUPUESTO: tema/formato del proyecto final por confirmar por Diana.
  Recuperacion: N-3 = Cl 39 (M9 perfect), N-7 = Cl 35 (M3-M4 deduction/3er cond).
  Frontera: Cl 43 = PRESENTACIONES FINALES + SINTESIS dia 3.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase42_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase42_CONV_GUIA.pdf'))
print('OK: B1_Clase42_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase42_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase42_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase42_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 42 generadas (V2).')
