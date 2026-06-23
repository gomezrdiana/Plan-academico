#!/usr/bin/env python3
"""B2 PM Amina - Correcciones 05/05/2026:
- Cheat Sheet del Proyecto (nuevo)
- Roadmap actualizado a 72h (reemplaza el de 90h)
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
B2_DIR = os.path.join(D, 'B2')

# =================== CHEAT SHEET PROYECTO ===================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_PROJECT_CHEAT_SHEET_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_PROJECT_CHEAT_SHEET.pdf'),
)

# =================== ROADMAP 72h ===================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_ROADMAP_72h_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_ROADMAP_72h.pdf'),
)

print('\n2 PDFs B2 PM Amina generados (CHEAT SHEET + ROADMAP 72h).')
print('NOTA: el viejo ROADMAP_90h queda obsoleto. Reemplazar entrega a Amina.')
