#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 2h noche — INSTRUCTIVO del proyecto MY LIFE (solo profe)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2 = os.path.join(D, 'VERSION_2', 'A2_2H')
md_to_pdf(os.path.join(A2, 'A2_2h_MY_LIFE_INSTRUCTIVO_PRINT.md'), os.path.join(A2, 'GUIAS', 'A2_2h_MY_LIFE_INSTRUCTIVO.pdf'))
print('OK: A2_2h_MY_LIFE_INSTRUCTIVO.pdf')
