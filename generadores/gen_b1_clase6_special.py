#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY - Clase 6 ESPECIAL - Día de Conversación y Juegos (sin gramática)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_DIR = os.path.join(D, 'B1')
REPORTES_DIR = os.path.join(B1_DIR, 'reportes')
os.makedirs(REPORTES_DIR, exist_ok=True)

# =================== GUIA ===================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase6_SPECIAL_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase6_SPECIAL_GUIA.pdf'),
)

# =================== REPORTE ===================
deliverables = [
    'Hojas de reflexion individual completadas (todos los presentes)',
    'Papel de errores fisico (anonimo, sin nombres) - minimo 12 errores',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    'Libreta personal con MINIMO 5 errores literales + NOMBRE de estudiante',
    'Foto/video del Mini-Pitch (responde a meta material redes)',
    'Foto del podio de English Points',
    'Lista de quienes NO entregaron tarea de Clase 5',
]

selfeval = [
    'Las estudiantes hablaron 90%+ del tiempo (formato especial conversacion)',
    'Hable menos de 15 min en total (formato especial)',
    'Mantuve ENGLISH ONLY como regla principal todo el dia',
    'Hice el ritual VATS extendido (Templanza dia 3) - 10 min',
    'Hice el Warm-up Two Truths and a Lie con todos DE PIE',
    'Hice el Hot Topic Round Robin con 3 rotaciones de pareja',
    'Hice el Mini-Pitch 90 seg con Q&A en vivo (5 estudiantes)',
    'Hice el Storyteller Chain en circulo (todos los presentes)',
    'Hice el Game Taboo English en equipos',
    'Hice el Project Workshop ORAL (no escrito) con 2 rondas',
    'Hice el Speed Debate de 5 rondas con rotacion',
    'Hice el Error Paper Live final con 8 errores anonimos',
    'Camine con papel de errores anonimo (min 12 errores escritos)',
    'En mi libreta personal anote 5 errores literales con NOMBRE',
    'Asigne English Points y publique podio del dia',
    'NO usé libro, NO ensené gramatica, NO hice ejercicios escritos',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

activities = [
    ('VATS Templanza dia 3 EXTENDIDO (10 min, in English)', '10 min'),
    ('Warm-up Two Truths and a Lie (DE PIE)', '20 min'),
    ('Hot Topic Round Robin - 3 temas, rotacion parejas', '30 min'),
    ('Mini-Pitch 90 seg + Q&A en vivo (estudiantes excepcionales)', '25 min'),
    ('Storyteller Chain - historia colectiva absurda (circulo)', '25 min'),
    ('BREAK', '20 min'),
    ('Game Taboo English (equipos DE PIE)', '25 min'),
    ('Project Workshop ORAL - MY STORY MY GOALS (parejas)', '25 min'),
    ('Game Speed Debate - 5 rondas con rotacion', '30 min'),
    ('Error Paper Live final (DE PIE)', '15 min'),
    ('English Points + Reflexion + Tarea + Cierre', '15 min'),
]

build_report_v2(
    os.path.join(REPORTES_DIR, 'B1_Clase6_SPECIAL_REPORTE.pdf'),
    'B1 MASTERY | Clase 6 de 44 | DIA ESPECIAL: CONVERSACION Y JUEGOS',
    'Sin bloque de gramatica - 3h40min conversacion + juegos | Templanza dia 3',
    activities,
    deliverables,
    selfeval,
    S,
)
print('OK: B1_Clase6_SPECIAL_REPORTE.pdf')

print('\nB1 Clase 6 ESPECIAL generada (GUIA + REPORTE).')
