#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY - Clase 5 - GUIA + REPORTE Grammar y Conv (sin shadowing por excepcion)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_DIR = os.path.join(D, 'B1')
REPORTES_DIR = os.path.join(B1_DIR, 'reportes')
os.makedirs(REPORTES_DIR, exist_ok=True)

# =================== GUIAS (md -> PDF) ===================
md_to_pdf(
    os.path.join(B1_DIR, 'GRAMATICA', 'B1_Clase5_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase5_GRAMMAR_GUIA.pdf'),
)
md_to_pdf(
    os.path.join(B1_DIR, 'CONVERSACION', 'B1_Clase5_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase5_CONV_GUIA.pdf'),
)

# =================== REPORTE GRAMMAR ===================
grammar_deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores fisico (anonimo, sin nombres)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    '16 cuadernos de GoldList con las 20 frases del Dia 4',
    'Libreta personal con minimo 3 errores literales + NOMBRE de estudiante',
    'Foto del tablero del Walking Conjugation Bee (ganador)',
]

grammar_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Estuve DE PIE durante ~70% del bloque (movimiento es clave en B1 Grammar)',
    'Hice las 4 actividades fisicas: Walk & Share, Stand-Up Drill, Gallery Walk, Walking Conjugation Bee, Error Paper Relay',
    'Camine con papel de errores anonimo (min 8 errores escritos)',
    'En mi libreta personal anote 3 errores literales con NOMBRE para el reporte',
    'Mi celular estaba boca abajo (excepto cronometro)',
    'Hice el ritual VATS (Templanza dia 2)',
    'NO permiti que estudiantes usaran celular en VATS para buscar palabras',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

grammar_activities = [
    ('VATS Templanza dia 2 (in English)', '7 min'),
    ('Tarea Check - Walk & Share (3 rondas, DE PIE)', '12 min'),
    ('Stand-Up Drill - Simple Present + 3rd person -s (DE PIE)', '15 min'),
    ('Gallery Walk - 4 estaciones 3rd person -s', '15 min'),
    ('GoldList Dia 4 - 20 frases nuevas', '15 min'),
    ('Writing Sprint x 3 rounds - My Daily Routine', '15 min'),
    ('Walking Conjugation Bee 3rd person -s (DE PIE)', '12 min'),
    ('Error Paper Live - Peer Relay (DE PIE)', '12 min'),
    ('Tarea + Wrap', '7 min'),
]

build_report_v2(
    os.path.join(REPORTES_DIR, 'B1_Clase5_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 5 de 44 | BLOQUE 1: GRAMMAR & WRITING',
    'M8 Simple Present (afirmativo) + M9 3rd Person -s | Templanza dia 2',
    grammar_activities,
    grammar_deliverables,
    grammar_selfeval,
    S,
)
print('OK: B1_Clase5_GRAMMAR_REPORTE.pdf')

# =================== REPORTE CONV ===================
conv_deliverables = [
    'Hojas de autoevaluacion completadas',
    'Papel de errores fisico (anonimo, sin nombres)',
    'Lista de errores recurrentes para PASE al profesor de Bloque 1 manana',
    'Libreta personal con minimo 3 errores literales + NOMBRE de estudiante',
    '16 Paginas 4 del proyecto (en cuaderno personal - fotografiar para registro)',
    'Foto del tablero de English Points del dia',
]

conv_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY como regla principal',
    'Hice el ritual VATS Reconnect (Templanza dia 2)',
    'Asigne English Points y publique el ranking del dia',
    'Camine con papel de errores anonimo (min 8 errores escritos)',
    'En mi libreta personal anote 3 errores literales con NOMBRE para el reporte',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'Hice la simulacion (Coordinar Agenda) - todos las parejas presentaron',
    'Hice la Historia Interactiva absurda - estudiantes agregaron al final',
    'Project Page 4 (My Daily Habits) - todos completaron al menos 2 secciones',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

conv_activities = [
    ('VATS Reconnect Templanza dia 2 (in English)', '7 min'),
    ('Icebreaker - Rutinas Absurdas (DE PIE)', '13 min'),
    ('Hot Topic - Disciplina hoy vs hace 30 anos (debate parejas)', '18 min'),
    ('Simulacion - Coordinar Agenda con Companero (DE PIE, 4 parejas presentan)', '25 min'),
    ('Historia Interactiva absurda - La Doctora Olimpica', '18 min'),
    ('Project Workshop - Page 4 MY DAILY HABITS THAT BUILD MY ENGLISH', '18 min'),
    ('Error Paper Live (DE PIE)', '8 min'),
    ('Autoevaluacion + Tarea', '3 min'),
]

build_report_v2(
    os.path.join(REPORTES_DIR, 'B1_Clase5_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 5 de 44 | BLOQUE 2: CONVERSACIONAL',
    'Aplicacion oral M8 Simple Present + M9 3rd Person -s | SIN shadowing por excepcion | Templanza dia 2',
    conv_activities,
    conv_deliverables,
    conv_selfeval,
    S,
)
print('OK: B1_Clase5_CONV_REPORTE.pdf')

print('\nListo. 4 PDFs B1 Clase 5 generados (2 GUIA + 2 REPORTE).')
