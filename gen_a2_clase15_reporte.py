#!/usr/bin/env python3
"""Genera el REPORTE de A2 Clase 15 — M17 Present Perfect vs Past Simple + Shadowing Dia 1 nuevo ciclo."""
import os
from generate_pdfs import get_styles, build_report

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))

deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores (entregado fisico con la guia)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    'Contenido para redes sociales (si se grabo)',
    'URL del video de Shadowing usado hoy (Dia 1 del ciclo)',
    'Lista de quienes NO entregaron tarea de Clase 14',
]

selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Fui guia, no conferencista',
    'Hice el puente M16 -> M17 (participio vs past simple, 12 min)',
    'En Shadowing modele contracciones (wanna, gonna) sin EXPLICAR',
    'Camine con papel de errores (min 5 errores escritos)',
    'Mi celular estaba boca abajo',
    'Hice el ritual VATS (Justicia dia 2)',
    'Libro y ejercicios NO se pasaron de tiempo',
    'Anote la URL del video de Shadowing en el reporte',
    'Grabe contenido para redes sociales',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

activities = [
    ('VATS Justicia dia 2', '5 min'),
    ('Analizo: Revision tarea irregulares', '8 min'),
    ('REFUERZO CRITICO past participle vs past simple + auxiliares', '12 min'),
    ('Libro M17: Present Perfect vs Past Simple', '18 min'),
    ('Ejercicios + Parejas (escoger tiempo correcto)', '12 min'),
    ('Shadowing DIA 1 del nuevo ciclo (mismo video A2 manana)', '12 min'),
    ('Speed Dating de experiencias (con contraste)', '15 min'),
    ('Competencia equipos: past simple vs present perfect', '10 min'),
    ('GoldList Lista 15', '10 min'),
    ('Errores + Peer Correction', '8 min'),
    ('Autochequeo', '5 min'),
    ('Tarea + Cierre', '5 min'),
]

build_report(
    os.path.join(D, 'A2', 'A2_Clase15_REPORTE.pdf'),
    'A2 | Clase 15 de 55',
    'M17: Present Perfect vs Past Simple + Refuerzo participio irregular + Auxiliares Have/Has',
    activities,
    deliverables,
    selfeval,
    S,
)
print('OK: A2_Clase15_REPORTE.pdf')
