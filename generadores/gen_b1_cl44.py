#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 44 — HOJA DE RUTA CIERRE (SOLO CONV). SINTESIS dia 4
(las 4 virtudes integradas): consolidacion final del nivel.
- CONV UNICO: circuito de estaciones con TODAS las familias del LIBRO B1
  (M1-M12: reported/perfect/causative/adjectives/pronouns + tags/relativos/
  comparativos) + Carta a Mi Yo del Futuro (escrita en Cl 1) se devuelve y se
  lee + ticket final.
  Sin PASE, sin tarea. PROHIBIDO mencionar el examen (evaluador externo).
  Las Cartas de Cl 1 las trae COORDINACION, no el profe.
- NO se genera GRAMMAR Cl 44: el segundo bloque del dia (ultimas 2h) es el
  EXAMEN FINAL con evaluador externo, sin guia.
Solo guia (el reporte lo hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'B1_Clase44_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase44_CONV_GUIA.pdf'))
print('OK: B1_Clase44_CONV_GUIA.pdf')

print('\n1 guia Cl 44 generada (V2, SOLO CONV — el Final lo aplica evaluador externo).')
