#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 SUPLETORIO oct-2026 — 3 sesiones de 4 h (refuerzo + taller de videos) — HOJA DE RUTA.
Grupo de 3-4 estudiantes que perdieron el final A2; un reintento con evaluador externo.
S1 = M12 + M14 · S2 = M17 (con M15-M16) + M5 · S3 = simulacro integrado. Virtud FORTALEZA 1/3-3/3.
Los reportes los produce despues: python generadores/gen_reporte_v3.py A2_SUPLETORIO_2026-10
Correr SIEMPRE desde la raiz: python generadores/gen_a2_supletorio_2026_10.py
"""
import os, re
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUP = os.path.join(D, 'VERSION_2', 'A2_SUPLETORIO_2026-10')
os.makedirs(os.path.join(SUP, 'GUIAS'), exist_ok=True)
os.makedirs(os.path.join(SUP, 'REPORTES'), exist_ok=True)

for n in range(1, 4):
    md = os.path.join(SUP, 'A2_Supletorio_Sesion%d_PRINT.md' % n)
    if not os.path.exists(md):
        print('SKIP (no existe): A2_Supletorio_Sesion%d_PRINT.md' % n)
        continue
    pdf = os.path.join(SUP, 'GUIAS', 'A2_Supletorio_Sesion%d_GUIA.pdf' % n)
    md_to_pdf(md, pdf)
    d = open(pdf, 'rb').read()
    print('OK: A2_Supletorio_Sesion%d_GUIA.pdf | %d KB | %d paginas' % (
        n, len(d) // 1024, len(re.findall(rb'/Type\s*/Page[^s]', d))))
