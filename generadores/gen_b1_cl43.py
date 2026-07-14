#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 43 — HOJA DE RUTA PROTOCOLO (2 tracks, dia completo). SINTESIS dia 3
(FORTALEZA+JUSTICIA): PRESENTACIONES FINALES.
- CONV: conduce/cronometra presentaciones 7-10 min + 2-3 preguntas, orden aleatorio,
  NO evalua NI comunica (V13). Audiencia = observers activos.
- GRAMMAR (segundo bloque del dia): termina pendientes + debrief de fortalezas +
  ticket reflexivo + reframe de grabaciones. Sin modulo.
  Frontera: Cl 44 = SOLO CONV (cierre). Final = evaluador externo, sin guia.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase43_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase43_CONV_GUIA.pdf'))
print('OK: B1_Clase43_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'B1_Clase43_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase43_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase43_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 43 generadas (V2).')
