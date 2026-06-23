#!/usr/bin/env python3
"""Genera el REPORTE de A2 Clase 16 — M18 Passive Voice (Regular Participles) — usa build_report_v2."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))

deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores (entregado fisico con la guia)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    'URL del video de Shadowing usado hoy (Dia 2 del ciclo)',
    'Cuadernos de GoldList con las 5 frases nuevas',
]

selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Fui guia, no conferencista',
    'En Shadowing modele wanna/gonna sin EXPLICAR la regla',
    'Camine con papel de errores (min 5 errores escritos)',
    'Mi celular estaba boca abajo',
    'Hice el ritual VATS (Justicia dia 3)',
    'Libro y ejercicios NO se pasaron de tiempo',
    'Anote la URL del video de Shadowing en el reporte',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

activities = [
    ('VATS Justicia dia 3', '5 min'),
    ('Analizo: Revision tarea past/present perfect', '8 min'),
    ('Libro M18: Passive Voice (Regular Participles)', '20 min'),
    ('Ejercicios + Parejas (activa -> pasiva)', '12 min'),
    ('Shadowing DIA 2 del ciclo', '12 min'),
    ('Speed Dating de noticias pasivas', '15 min'),
    ('Competencia equipos: activa -> pasiva', '10 min'),
    ('GoldList Lista 16', '10 min'),
    ('Errores + Peer Correction', '10 min'),
    ('Autochequeo + Tarea + Cierre', '8 min'),
]

build_report_v2(
    os.path.join(D, 'A2', 'A2_Clase16_REPORTE.pdf'),
    'A2 | Clase 16 de 55',
    'M18: Passive Voice (Regular Participles) - "You Are Loved!"',
    activities,
    deliverables,
    selfeval,
    S,
)
print('OK: A2_Clase16_REPORTE.pdf')
