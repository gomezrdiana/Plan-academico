#!/usr/bin/env python3
"""B1 MASTERY - Clase 3 - REPORTEs Grammar y Conv usando build_report_v2 (formato unificado nuevo)."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'B1', 'reportes'), exist_ok=True)

# ===================== GRAMMAR =====================
grammar_deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores (entregado fisico con la guia)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    '16 cuadernos de GoldList con las 20 frases del Dia 2',
    'Cartas de Recommendation pegadas en cuadernos personales',
]

grammar_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Camine con papel de errores (min 8 errores escritos)',
    'Mi celular estaba boca abajo',
    'Hice el ritual VATS (Prudencia dia 3)',
    'NO permiti que estudiantes usaran celular en VATS para buscar palabras',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'Reforce diferencia entre 13/30, 14/40, 15/50 (numbers pronunciation)',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

grammar_activities = [
    ('VATS Prudencia dia 3 (in English)', '7 min'),
    ('Tarea Check (homework Cl 2)', '11 min'),
    ('Gramatica: Should/Shouldnt + Numbers', '20 min'),
    ('Ejercicios Aplicados (8 oraciones)', '17 min'),
    ('GoldList Dia 2 - 20 frases nuevas', '15 min'),
    ('Writing - Recommendations Letter', '20 min'),
    ('Error Paper Live', '15 min'),
    ('Tarea + Wrap', '5 min'),
]

build_report_v2(
    os.path.join(D, 'B1', 'reportes', 'B1_Clase3_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 3 de 44 | BLOQUE 1: GRAMMAR & WRITING',
    'M4 Should/Shouldnt + M5 Numbers',
    grammar_activities,
    grammar_deliverables,
    grammar_selfeval,
    S,
)
print('OK: B1_Clase3_GRAMMAR_REPORTE.pdf')

# ===================== CONV =====================
conv_deliverables = [
    'Hojas de autoevaluacion completadas',
    'Papel de errores (entregado fisico con la guia)',
    'URL del video de Shadowing usado hoy (Dia 2 del ciclo)',
    'Foto del tablero de English Points del dia',
]

conv_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY como regla principal',
    'Hice el ritual VATS Reconnect (Prudencia dia 3)',
    'En Shadowing Dia 2 use el MISMO video que Clase 2',
    'Asigne English Points y publique el ranking del dia',
    'Camine con papel de errores (min 8 errores escritos)',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'Project Page 2 (My Milestones) - todos completaron',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

conv_activities = [
    ('VATS Reconnect (in English)', '7 min'),
    ('Icebreaker - Would You Rather (fisico)', '13 min'),
    ('Hot Topic - Best Advice Ever (debate)', '15 min'),
    ('TBLT - Travel Advisory Board Bucaramanga', '25 min'),
    ('Shadowing - DIA 2 de ciclo (mismo video Cl 2)', '15 min'),
    ('Project Workshop - Page 2 MY MILESTONES', '20 min'),
    ('Error Paper Live', '10 min'),
    ('Autoevaluacion + Tarea', '5 min'),
]

build_report_v2(
    os.path.join(D, 'B1', 'reportes', 'B1_Clase3_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 3 de 44 | BLOQUE 2: CONVERSACIONAL',
    'Aplicacion oral SHOULD + Numbers + Shadowing Dia 2',
    conv_activities,
    conv_deliverables,
    conv_selfeval,
    S,
)
print('OK: B1_Clase3_CONV_REPORTE.pdf')

print('\nListo. 2 reportes B1 Clase 3 generados con formato v2.')
