#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF del Reporte AUD-003 (Christian A1 Noche)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT_DIR = os.path.join(D, 'Sistema_Auditoria', 'Christian_A1_Noche')
md_to_pdf(
    os.path.join(AUDIT_DIR, 'AUD-A1NOC-S17-2026-003.md'),
    os.path.join(AUDIT_DIR, 'AUD-A1NOC-S17-2026-003.pdf'),
)
print('OK: AUD-A1NOC-S17-2026-003.pdf')
