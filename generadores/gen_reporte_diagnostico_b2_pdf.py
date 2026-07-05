#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF imprimible del reporte diagnostico B2 (para llenar a mano)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVAL_DIR = os.path.join(D, 'recursos', 'evaluaciones')
md_to_pdf(
    os.path.join(EVAL_DIR, 'REPORTE_DIAGNOSTICO_COHORTE_B2.md'),
    os.path.join(EVAL_DIR, 'REPORTE_DIAGNOSTICO_COHORTE_B2.pdf'),
)
print('OK: REPORTE_DIAGNOSTICO_COHORTE_B2.pdf (printable, fill by hand)')
