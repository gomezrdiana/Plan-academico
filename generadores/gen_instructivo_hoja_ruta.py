#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera el INSTRUCTIVO del profesor: como ejecutar una hoja de ruta Heiiu (entrega con contrato)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(D, 'documentos_operativos', 'INSTRUCTIVO_HOJA_DE_RUTA_PROFESOR.md')
OUT = os.path.join(D, 'documentos_operativos', 'INSTRUCTIVO_HOJA_DE_RUTA_PROFESOR.pdf')
md_to_pdf(SRC, OUT)
print('OK: INSTRUCTIVO_HOJA_DE_RUTA_PROFESOR.pdf')
