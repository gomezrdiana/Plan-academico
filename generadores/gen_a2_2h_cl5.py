#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 5 — HOJA DE RUTA: M6 Right on Time! Scheduled Events (present simple horarios, p.41-50).
PRUDENCIA v1 dia 5 CIERRA. Frontera de salida: tarea 8 sentences M6 DUE Cl 6; anuncia Cl 6 = Module 7 + TEMPLANZA."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(os.path.join(A2_2H, 'GUIAS'), exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class5_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class5_GUIA.pdf'))
print('OK: A2_Class5_GUIA.pdf')
