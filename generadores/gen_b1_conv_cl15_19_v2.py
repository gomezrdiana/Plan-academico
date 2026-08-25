#!/usr/bin/env python3
"""B1 Mastery CONV Cl 15-19 (VERSION_2) — arco del pasado COMPRIMIDO (decision coordinacion 25/08/2026).
Cl 15 consolidacion oral · Cl 16 used to/would · Cl 17 narrativa 4 capas · Cl 18 past perfect · Cl 19 clinica oral.
Solo regenera las GUIAS. Los REPORTES los produce: python generadores/gen_reporte_v3.py B1_4H/CONVERSACION
Correr desde la raiz: python generadores/gen_b1_conv_cl15_19_v2.py
"""
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))

import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONV = os.path.join(D, 'VERSION_2', 'B1_4H', 'CONVERSACION')
GUIAS = os.path.join(CONV, 'GUIAS')

for n in (15, 16, 17, 18, 19):
    src = os.path.join(CONV, 'B1_Clase%d_CONV_PRINT.md' % n)
    dst = os.path.join(GUIAS, 'B1_Clase%d_CONV_GUIA.pdf' % n)
    md_to_pdf(src, dst)
    print('OK: B1_Clase%d_CONV_GUIA.pdf (%d KB)' % (n, os.path.getsize(dst) // 1024))

print('\n5 GUIAS regeneradas en VERSION_2/B1_4H/CONVERSACION/GUIAS/')
