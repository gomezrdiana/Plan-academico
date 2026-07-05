#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B2 PM Amina - Clase 2 - GUIA + REPORTE.
Formato hoy: 90 min academico + 30 min actividad externa.
Shadowing CON video confirmado.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B2_DIR = os.path.join(D, 'B2')

# =================== GUIA ===================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase2_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase2_GUIA.pdf'),
)

# =================== REPORTE ===================
deliverables = [
    'Hojas de autochequeo completadas (5 estudiantes)',
    'URL del video de Shadowing usado anotada (Dia 1 ciclo nuevo)',
    'Papel de errores fisico (anonimo, sin nombres)',
    'Tarea enviada al grupo de WhatsApp con DUE DATE explicita',
    'Libreta personal con minimo 3 errores literales + NOMBRE',
    'Foto/video del Mini-Pitch para redes Heiiu',
    'Foto del banco comun de palabras B2-tier del tablero',
    'Lista de quienes NO entregaron audio antes de Cl 1',
    'Notas sobre la actividad externa (que paso, participacion)',
]

selfeval = [
    'Las estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY como regla principal',
    'Hice el ritual VATS (Templanza dia 3)',
    'RE-EXPLIQUE el proyecto con el Cheat Sheet en bloque 2',
    'Cada estudiante construyo 5 palabras B2-tier especificas a su tema',
    'Cada estudiante hizo Mini-Pitch 90 seg + Q&A en vivo',
    'Hice Shadowing 5 pasos completos con video confirmado',
    'Anote URL del video en el reporte',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En mi libreta personal anote 3 errores literales con NOMBRE',
    'NO acepte la excusa "es muy pesado de un dia para otro" en tarea',
    'Asigne tarea Cl 3 con DUE DATE + tiempo estimado explicitos',
    'Acompane al grupo a la actividad externa (puntualidad)',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

activities = [
    ('VATS Templanza dia 3 (in English)', '7 min'),
    ('RE-EXPLICAR el proyecto con Cheat Sheet', '10 min'),
    ('Revision tarea Cl 1 - audio antes', '8 min'),
    ('Vocabulario + frases por tema escogido', '18 min'),
    ('MINI-PITCH 90 seg + Q&A en vivo (5 estudiantes)', '18 min'),
    ('Shadowing 5 pasos - Dia 1 nuevo ciclo', '15 min'),
    ('Error Paper Live + Tarea con due date + Cierre', '14 min'),
    ('ACTIVIDAD EXTERNA (coordinacion)', '30 min'),
]

build_report_v2(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase2_REPORTE.pdf'),
    'B2 PM AMINA | Clase 2 de 36 | 70h hasta el Final',
    'Re-explicar proyecto + Vocabulario por tema + Mini-Pitch + Shadowing Dia 1 nuevo ciclo | Templanza dia 3 | 90 min academico + 30 min actividad externa',
    activities,
    deliverables,
    selfeval,
    S,
)
print('OK: B2_PM_Amina_Clase2_REPORTE.pdf')

print('\nB2 PM Amina Clase 2 generada (GUIA + REPORTE).')
print('Recuerda: video Shadowing https://www.youtube.com/watch?v=sKIzIOgHfW4')
