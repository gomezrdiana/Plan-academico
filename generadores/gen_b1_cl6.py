#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 6 — HOJA DE RUTA (2 tracks). TEMPLANZA v1 dia 1 (ABRE bloque):
- CONV (primero): Tu semana en presente + New-Hire Routine Briefing (uso oral;
  la capa nueva del dia, HAS, sale en boca de ellos).
- GRAMMAR (segundo, ~86% DE PIE): capa NUEVA unicamente — A1 Book M17 "have -> HAS"
  (Guia 1 p.211; Ejemplos p.212) + A1 Book M9 Guia 1 punto 4, los 3 sonidos de la -s
  (p.112). Todo lo demas es APLICACION de lo lockeado en Cl 5 (audit desk + handover).
  NO re-enseña la tabla do/does de Cl 5.
Solo guias (los reportes los hace gen_reporte_v3.py)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(os.path.join(B1, 'CONVERSACION', 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(B1, 'GRAMATICA', 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(B1, 'CONVERSACION', 'B1_Clase6_CONV_PRINT.md'),
          os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase6_CONV_GUIA.pdf'))
print('OK: B1_Clase6_CONV_GUIA.pdf')

md_to_pdf(os.path.join(B1, 'GRAMATICA', 'B1_Clase6_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase6_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase6_GRAMMAR_GUIA.pdf')

print('\n2 guias Cl 6 generadas (V2).')
