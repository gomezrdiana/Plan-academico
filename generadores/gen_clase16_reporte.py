#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera el REPORTE de A1 Clase 16 — M16 Gustos (like/love/hate + verbo-ing) + Shadowing Dia 2."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores (entregado fisico con la guia)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    'Contenido para redes sociales (si se grabo)',
    'Lista de quienes NO entregaron tarea de Clase 15',
]

selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Fui guia, no conferencista',
    'En Shadowing modele wanna/gonna sin EXPLICAR la regla',
    'Camine con papel de errores (min 5 errores escritos)',
    'Mi celular estaba boca abajo',
    'Hice el ritual VATS (Justicia dia 2)',
    'Libro y ejercicios NO se pasaron de tiempo',
    'Grabe contenido para redes sociales',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

activities = [
    ('VATS Justicia dia 2', '5 min'),
    ('Analizo: Revision tarea posesivos', '8 min'),
    ('Activacion: Stand Up If You LOVE/HATE', '12 min'),
    ('Libro M16: Like/Love/Hate + verbo-ing', '18 min'),
    ('Ejercicios + Parejas', '12 min'),
    ('Shadowing DIA 2 (Beauty and the Beast - mismo video)', '12 min'),
    ('Speed Dating de gustos', '15 min'),
    ('Competencia equipos: gustos', '10 min'),
    ('GoldList Lista 16', '10 min'),
    ('Errores + Peer Correction', '8 min'),
    ('Autochequeo', '5 min'),
    ('Tarea + Cierre', '5 min'),
]

build_report_v2(
    os.path.join(D, 'A1', 'A1_Clase16_REPORTE.pdf'),
    'A1 | Clase 16 de 45',
    'M16: Gustos (like/love/hate + verbo-ing) + Shadowing Dia 2',
    activities,
    deliverables,
    selfeval,
    S,
)
print('OK: A1_Clase16_REPORTE.pdf')
