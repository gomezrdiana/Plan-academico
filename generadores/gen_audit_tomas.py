#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF del Reporte del Sistema de Auditoria - Tomas A2 AM."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT_DIR = os.path.join(D, 'Sistema_Auditoria', 'Tomas_A2_AM')
md_to_pdf(
    os.path.join(AUDIT_DIR, 'AUD-A2AM-S17-2026-001.md'),
    os.path.join(AUDIT_DIR, 'AUD-A2AM-S17-2026-001.pdf'),
)
print('OK: AUD-A2AM-S17-2026-001.pdf')
