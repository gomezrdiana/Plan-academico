#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF de la plantilla v2 del contrato del profesor (hora catedra)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRATOS_DIR = os.path.join(D, 'contratos')
md_to_pdf(
    os.path.join(CONTRATOS_DIR, 'PLANTILLA_CONTRATO_HORA_CATEDRA_HEIIU_2026_v2.md'),
    os.path.join(CONTRATOS_DIR, 'PLANTILLA_CONTRATO_HORA_CATEDRA_HEIIU_2026_v2.pdf'),
)
print('OK: PLANTILLA_CONTRATO_HORA_CATEDRA_HEIIU_2026_v2.pdf')
print('NOTA: Revisar con asesor legal antes de uso formal.')
