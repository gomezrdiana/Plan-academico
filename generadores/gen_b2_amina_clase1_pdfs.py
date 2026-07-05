#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B2 PM Amina - Clase 1 + Roadmap 90h - GUIA + REPORTE + ROADMAP."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B2_DIR = os.path.join(D, 'B2')

# =================== GUIA Clase 1 ===================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase1_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase1_GUIA.pdf'),
)

# =================== ROADMAP 90h ===================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_ROADMAP_90h_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_ROADMAP_90h.pdf'),
)

# =================== REPORTE Clase 1 ===================
deliverables = [
    'Hojas de autochequeo completadas (5 estudiantes)',
    'Papel de errores fisico (anonimo, sin nombres)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    '5 sobres con tema escogido por estudiante (entregar a coordinacion)',
    'Libreta personal con minimo 3 errores literales + NOMBRE de estudiante',
    'Diagnostico completo de Maria Alejandra (5 preguntas con skill ratings)',
    'Foto del tablero con los 7 sub-temas Colombia y journey 90h',
]

selfeval = [
    'Las estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY como regla principal',
    'Hice el ritual VATS (Templanza dia 2)',
    'Hice el Big Reveal del proyecto Why Colombia con energia',
    'Cada estudiante escogio su tema y lo escribio en sobre cerrado',
    'Cada estudiante hizo su mini-presentacion 60 seg DE PIE',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En mi libreta personal anote 3 errores literales con NOMBRE',
    'Diagnostique a Maria Alejandra (5 preguntas + skill ratings)',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'NO hable de notas, midterm anterior, ni profesores anteriores',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

activities = [
    ('VATS Templanza dia 2 (in English)', '7 min'),
    ('Welcome Amina + reset del grupo', '8 min'),
    ('BIG REVEAL - Why Colombia, el Final', '15 min'),
    ('Brainstorm en parejas - escoger tema (sobre cerrado)', '15 min'),
    ('Hot Topic - Best thing about Colombia for a foreigner', '20 min'),
    ('Mini-presentacion 60 seg - My Colombia Angle (DE PIE)', '15 min'),
    ('Pronunciacion + Vocabulario integrado', '20 min'),
    ('Error Paper Live (anonimo)', '8 min'),
    ('Tarea + Cierre', '5 min'),
]

build_report_v2(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase1_REPORTE.pdf'),
    'B2 PM AMINA | Clase 1 de 45 | Hora 110 de 200',
    'Reset + Big Reveal Proyecto Why Colombia | Templanza dia 2 | Diagnostico Maria Alejandra',
    activities,
    deliverables,
    selfeval,
    S,
)
print('OK: B2_PM_Amina_Clase1_REPORTE.pdf')

print('\nListo. 3 PDFs B2 PM Amina generados (GUIA Clase 1 + REPORTE Clase 1 + ROADMAP 90h).')
