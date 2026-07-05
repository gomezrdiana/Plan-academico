#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera REPORTEs v2 de A1 Clase 17 (M17 Have+Any/Some) y A2 Clase 17 (M19 Passive Irregular)."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ===== A1 Clase 17 =====
a1_deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores (entregado fisico con la guia)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    'Foto/video del Shadowing Dia 3 (presentaciones de memoria) - material redes',
    'Cuadernos de GoldList con las 5 frases nuevas',
]

a1_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Fui guia, no conferencista',
    'En Shadowing Dia 3 NO use video, todos los grupos presentaron de memoria',
    'Camine con papel de errores (min 5 errores escritos)',
    'Mi celular estaba boca abajo',
    'Hice el ritual VATS (Justicia dia 3)',
    'Libro y ejercicios NO se pasaron de tiempo',
    'Grabe foto/video de las presentaciones del Shadowing Dia 3 para redes',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

a1_activities = [
    ('VATS Justicia dia 3', '5 min'),
    ('Analizo: Revision tarea like/love/hate', '8 min'),
    ('Libro M17: Have + Any/Some', '18 min'),
    ('Ejercicios + Parejas', '12 min'),
    ('Shadowing DIA 3: PRESENTACION DE MEMORIA (Beauty and the Beast)', '12 min'),
    ('Speed Dating - Sharing what we have', '15 min'),
    ('Competencia equipos: Have + any/some', '10 min'),
    ('GoldList Lista 17', '10 min'),
    ('Errores + Peer Correction', '10 min'),
    ('Autochequeo + Tarea + Cierre', '10 min'),
]

build_report_v2(
    os.path.join(D, 'A1', 'A1_Clase17_REPORTE.pdf'),
    'A1 | Clase 17 de 45',
    'M17: Do You Have Any Pizza? - Have + Any/Some + Shadowing Dia 3',
    a1_activities,
    a1_deliverables,
    a1_selfeval,
    S,
)
print('OK: A1_Clase17_REPORTE.pdf')

# ===== A2 Clase 17 =====
a2_deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores (entregado fisico con la guia)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    'Foto/video del Shadowing Dia 3 (presentaciones de memoria) - material redes',
    'Cuadernos de GoldList con las 5 frases nuevas',
]

a2_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Fui guia, no conferencista',
    'En Shadowing Dia 3 NO use video, todos los grupos presentaron de memoria',
    'Camine con papel de errores (min 5 errores escritos)',
    'Mi celular estaba boca abajo',
    'Hice el ritual VATS (Justicia dia 4)',
    'Libro y ejercicios NO se pasaron de tiempo',
    'Grabe foto/video de las presentaciones del Shadowing Dia 3 para redes',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

a2_activities = [
    ('VATS Justicia dia 4', '5 min'),
    ('Analizo: Revision tarea passive regular', '8 min'),
    ('Libro M19: Passive Voice IRREGULAR participles', '20 min'),
    ('Ejercicios + Parejas (activa->pasiva irregular)', '12 min'),
    ('Shadowing DIA 3: PRESENTACION DE MEMORIA', '12 min'),
    ('Speed Dating - News Headlines in Passive', '15 min'),
    ('Competencia equipos: activa->pasiva irregular', '10 min'),
    ('GoldList Lista 17', '10 min'),
    ('Errores + Peer Correction', '10 min'),
    ('Autochequeo + Tarea + Cierre', '8 min'),
]

build_report_v2(
    os.path.join(D, 'A2', 'A2_Clase17_REPORTE.pdf'),
    'A2 | Clase 17 de 55',
    'M19: Passive Voice Irregular Participles + Shadowing Dia 3',
    a2_activities,
    a2_deliverables,
    a2_selfeval,
    S,
)
print('OK: A2_Clase17_REPORTE.pdf')

print('\nListo. 2 reportes generados con formato v2.')
