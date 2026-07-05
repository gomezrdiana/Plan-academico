#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF del documento consolidado GUIA_REUNION_DIANA.
Reemplaza el uso simultaneo de AGENDA + BLOQUE0 + scripts dispersos."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(D, 'documentos_operativos')

md_to_pdf(os.path.join(DOCS, 'GUIA_REUNION_DIANA_PRINT.md'),
          os.path.join(DOCS, 'GUIA_REUNION_DIANA.pdf'))
print('OK: GUIA_REUNION_DIANA.pdf')
