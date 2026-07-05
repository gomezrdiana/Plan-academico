#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDFs de la GUIA EVALUADORA - versiones ES y EN."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVAL_DIR = os.path.join(D, 'recursos', 'evaluaciones')

# =================== VERSION ES ===================
md_to_pdf(
    os.path.join(EVAL_DIR, 'GUIA_EVALUADORA_ES_PRINT.md'),
    os.path.join(EVAL_DIR, 'GUIA_EVALUADORA_ES.pdf'),
)

# =================== VERSION EN ===================
md_to_pdf(
    os.path.join(EVAL_DIR, 'GUIA_EVALUADORA_EN_PRINT.md'),
    os.path.join(EVAL_DIR, 'GUIA_EVALUADORA_EN.pdf'),
)

print('\n2 PDFs generados (ES + EN). Guia unica de Evaluadora — Diagnostico + Activacion Competitiva.')
