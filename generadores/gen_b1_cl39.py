#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 39 — HOJA DE RUTA (2 tracks). FORTALEZA v2 dia 4:
- CONV: Boring vs Bored + The Feedback Conversation. Prepara M41 oral.
- GRAMMAR (~86% DE PIE): A2 Book M41 "This Is Interesting!" — Participle
  Adjectives (-ing cause / -ed feeler) (p.326-330). M40 NO existe (saltado).
  Frontera: Cl 40 = M42 + FORTALEZA v2 dia 5.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase39_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase39_CONV_GUIA.pdf'))
print('OK: B1_Clase39_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase39_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase39_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase39_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 39 generadas (V2).')
