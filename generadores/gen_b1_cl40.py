#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 40 — HOJA DE RUTA (2 tracks). FORTALEZA v2 dia 5 (CIERRA bloque):
- CONV: Get it done + Tell me about it + The Handover Briefing. Aplica M10+M11 oral.
- GRAMMAR (~86% DE PIE): B1 Book M10 "The Causative" (active + passive, p.117-126)
  + M11 "Advanced Adjectives" (noun-adj, prefixes/suffixes, compound, impersonal,
  p.127-144), doble.
  Frontera: Cl 41 = M12 Advanced Pronouns (ULTIMO modulo, cierra libro) + SINTESIS dia 1.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase40_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase40_CONV_GUIA.pdf'))
print('OK: B1_Clase40_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase40_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase40_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase40_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 40 generadas (V2).')
