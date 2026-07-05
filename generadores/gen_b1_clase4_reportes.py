#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY - Clase 4 - REPORTEs Grammar y Conv usando build_report_v2 (formato unificado nuevo)."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(D, 'B1', 'reportes'), exist_ok=True)

# ===================== GRAMMAR =====================
grammar_deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores (entregado fisico con la guia)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    '16 cuadernos de GoldList con las 20 frases del Dia 3',
    'Foto del tablero de English Points del dia',
]

grammar_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Estuve DE PIE durante ~70% del bloque (movimiento es clave en B1 Grammar)',
    'Hice las 3 actividades fisicas: Stand-Up Drill, Gallery Walk, Walking Spelling Bee',
    'Camine con papel de errores (min 8 errores escritos)',
    'Mi celular estaba boca abajo (excepto cronometro)',
    'Hice el ritual VATS (Prudencia dia 4)',
    'NO permiti que estudiantes usaran celular en VATS para buscar palabras',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

grammar_activities = [
    ('VATS Prudencia dia 4 (in English)', '7 min'),
    ('Tarea Check - Walk & Share (3 rondas, DE PIE)', '12 min'),
    ('Stand-Up Grammar Drill - WILL (20 prompts, DE PIE)', '15 min'),
    ('Gallery Walk - 4 estaciones IN/ON/AT', '15 min'),
    ('GoldList Dia 3 - 20 frases nuevas', '15 min'),
    ('Writing Sprint x 3 rounds (60 sec each)', '15 min'),
    ('Walking Spelling Bee - Numbers & Times (DE PIE)', '12 min'),
    ('Error Paper Live - Peer Relay (DE PIE)', '12 min'),
    ('Tarea + Wrap', '7 min'),
]

build_report_v2(
    os.path.join(D, 'B1', 'reportes', 'B1_Clase4_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 4 de 44 | BLOQUE 1: GRAMMAR & WRITING',
    'M6 Simple Future (will) + M7 Times and Places (IN/ON/AT)',
    grammar_activities,
    grammar_deliverables,
    grammar_selfeval,
    S,
)
print('OK: B1_Clase4_GRAMMAR_REPORTE.pdf')

# ===================== CONV =====================
conv_deliverables = [
    'Hojas de autoevaluacion completadas',
    'Papel de errores (entregado fisico con la guia)',
    'URL del NUEVO video de Shadowing recibido para manana',
    'Foto/video del Shadowing Dia 3 (presentaciones de memoria) - material redes',
    'Foto del tablero de English Points del dia',
]

conv_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY como regla principal',
    'Hice el ritual VATS Reconnect (Prudencia dia 4)',
    'En Shadowing Dia 3 NO uso video, todos los grupos presentaron de memoria',
    'Asigne English Points y publique el ranking del dia',
    'Camine con papel de errores (min 8 errores escritos)',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'Project Page 3 (My Obstacles) - todos completaron al menos 1 obstaculo + 1 plan',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

conv_activities = [
    ('VATS Reconnect (in English)', '7 min'),
    ('Icebreaker - WILL YOU EVER lines (DE PIE)', '13 min'),
    ('Hot Topic - Will robots replace us? (debate)', '15 min'),
    ('TBLT - Escape Plan simulation (4 escenarios)', '25 min'),
    ('Shadowing - DIA 3 PRESENTACION DE MEMORIA (grupos de 4)', '20 min'),
    ('Project Workshop - Page 3 MY OBSTACLES IN ENGLISH', '15 min'),
    ('Error Paper Live (DE PIE)', '10 min'),
    ('Autoevaluacion + Tarea', '5 min'),
]

build_report_v2(
    os.path.join(D, 'B1', 'reportes', 'B1_Clase4_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 4 de 44 | BLOQUE 2: CONVERSACIONAL',
    'Aplicacion oral WILL + Times/Places + Shadowing Dia 3 PRESENTACION',
    conv_activities,
    conv_deliverables,
    conv_selfeval,
    S,
)
print('OK: B1_Clase4_CONV_REPORTE.pdf')

print('\nListo. 2 reportes B1 Clase 4 generados con formato v2.')
