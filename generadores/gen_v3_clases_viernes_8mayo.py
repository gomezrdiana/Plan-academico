#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDFs v3 para B1 Cl 9 GRAMMAR + B1 Cl 9 CONV + A2 4h Cl 13 (08/05/2026)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_DIR = os.path.join(D, 'B1')
B1_REPORTES = os.path.join(B1_DIR, 'reportes')
A2_DIR = os.path.join(D, 'A2')
A2_REPORTES = os.path.join(A2_DIR, 'reportes')

os.makedirs(B1_REPORTES, exist_ok=True)
os.makedirs(A2_REPORTES, exist_ok=True)

# ============================================================
# 1. B1 Cl 9 GRAMMAR v3
# ============================================================

md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase9_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase9_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase9_GRAMMAR_GUIA.pdf (v3)')

b1_c9_g_act = [
    ('MYSTERY OPENER (sobre cerrado, NUEVO)', '5 min'),
    ('VATS JUSTICIA dia 2 (filosofica)', '7 min'),
    ('Tarea Check Walk & Share rapido', '10 min'),
    ('VOCABULARY UPGRADE ACADEMIC B2 (paramount, sustainable, etc.)', '10 min'),
    ('SHARK TANK ETHICS EDITION (problemas sociales, no negocios)', '18 min'),
    ('Gallery Walk Public Figures + Policies (NO familia)', '13 min'),
    ('GoldList Dia 7 - 20 frases reflexivas (justicia, etica)', '13 min'),
    ('Writing Sprint ARGUMENTATIVO con DIFERENCIACION', '12 min'),
    ('Possessive Battle Royale - Figuras historicas', '10 min'),
    ('Error Paper Live Peer Relay', '8 min'),
    ('Tarea con DIFERENCIACION explicita + Wrap', '4 min'),
]
b1_c9_g_deliv = [
    'Hojas de autochequeo completadas',
    'Papel de errores fisico (anonimo)',
    'Tarea enviada al WhatsApp con DUE DATE + diferenciacion por nivel',
    '17 cuadernos GoldList con 20 frases reflexivas (Dia 7)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Foto del tablero del WORD UPGRADE A1->Academic B2',
    'Foto del SOBRE del Mystery Opener (con letra visible)',
    'Foto/video del Shark Tank Ethics Edition (material redes)',
    'Foto del Battle Royale Historical (ganador + grupo)',
    'Lista quienes NO entregaron tarea Cl 8',
    'Notas: tu energia hoy - con que bloque te conectaste mas/menos',
]
b1_c9_g_eval = [
    'Lei el mensaje pedagogico al inicio de la guia ANTES de clase',
    'PREPARE el SOBRE del Mystery Opener con letra escrita en el frente',
    'ESCRIBI el WORD UPGRADE Academic B2 en el tablero ANTES de clase',
    'Mantuve el WORD UPGRADE visible toda la clase',
    'Conduje MYSTERY OPENER con energia (5 min)',
    'Hice VATS Justicia dia 2 con pregunta filosofica (NO familiar)',
    'Conduje SHARK TANK ETHICS EDITION con ritmo (problemas sociales reales)',
    'Conduje GALLERY WALK con figuras publicas y politicas (no familia)',
    'Lei las 20 frases reflexivas del GoldList con la clase',
    'Anuncie LA DIFERENCIACION visible (3 niveles) en el Writing argumentativo',
    'Conduje POSSESSIVE BATTLE ROYALE HISTORICAL con velocidad',
    'Asigne tarea con DIFERENCIACION explicita por nivel',
    'NO permiti la excusa "esto ya lo sabia" (respondi con vocabulario academico B2)',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores con NOMBRE',
    'Refoze HIS vs HER en contexto profesional/historico (error fosilizable)',
    'Estudiantes hablaron 80%+ del tiempo',
    'Estuve DE PIE durante ~70% del bloque',
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase9_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 de 44 | BLOQUE 1: GRAMMAR & WRITING (v3)',
    'M14+M15 + Mystery Opener + Academic B2 + Ethics Shark Tank + Reflexive GoldList | Justicia dia 2',
    b1_c9_g_act, b1_c9_g_deliv, b1_c9_g_eval, S,
)
print('OK: B1_Clase9_GRAMMAR_REPORTE.pdf (v3)')

# ============================================================
# 2. B1 Cl 9 CONV v2
# ============================================================

md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase9_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase9_CONV_GUIA.pdf'),
)
print('OK: B1_Clase9_CONV_GUIA.pdf (v2)')

b1_c9_c_act = [
    ('VATS Reconnect JUSTICIA dia 2 (filosofica, no familiar)', '7 min'),
    ('Icebreaker - HIS/HER sobre FIGURAS CONOCIDAS (NO familia)', '13 min'),
    ('Hot Topic - Is justice universal or cultural? (debate)', '18 min'),
    ('Simulacion - Defend an ethical position (DE PIE)', '22 min'),
    ('Shadowing Dia 3 PRESENTACION MEMORIA (sin video)', '15 min'),
    ('Project Workshop ORAL - Page 7 MY PEOPLE (profesional/intelectual)', '18 min'),
    ('Mini-Pitch 90 seg + Q&A en vivo (DEBATE etico)', '10 min'),
    ('Error Paper Live + Tarea + Cierre', '7 min'),
]
b1_c9_c_deliv = [
    'Reporte impreso lleno',
    'Foto/video Shadowing Dia 3 (presentacion memoria) - material redes',
    'Papel errores fisico (anonimo)',
    'Lista de errores recurrentes para PASE al profesor de Bloque 1 lunes',
    '17 Paginas 7 del proyecto MY PEOPLE (profesional, no familiar)',
    'Foto del podio English Points',
    'Tu libreta personal con 3 errores literales + nombre por bloque oral',
]
b1_c9_c_eval = [
    'Lei el mensaje pedagogico al inicio de la guia',
    'Use TEMAS NO PERSONALES en todos los bloques (figuras publicas, etica, debate)',
    'VATS Reconnect fue filosofica (no "tu familia")',
    'Icebreaker fue con figuras conocidas (no familiares)',
    'Hot Topic fue debate etico filosofico (universal vs cultural)',
    'Simulacion fue defensa de posicion etica (no "describe tu familia")',
    'Mini-Pitch fue debate etico (no "persona importante en tu vida")',
    'Project Page 7 fue PROFESIONAL/INTELECTUAL (mentores, autores, lideres)',
    'Refoze HIS vs HER en contexto figuras publicas/profesionales',
    'Practique 2+ academic B2 words por bloque oral',
    'Conduje Shadowing Dia 3 sin video y grabo presentacion',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'Estudiantes hablaron 80%+ del tiempo',
    'Estuve DE PIE durante ~60% del bloque',
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase9_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 de 44 | BLOQUE 2: CONVERSACIONAL (v2)',
    'HIS/HER + prepositions en debate etico + figuras publicas | Justicia dia 2',
    b1_c9_c_act, b1_c9_c_deliv, b1_c9_c_eval, S,
)
print('OK: B1_Clase9_CONV_REPORTE.pdf (v2)')

# ============================================================
# 3. A2 4h Cl 13 versión 2h
# ============================================================

md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class13_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Class13_GUIA.pdf'),
)
print('OK: A2_4h_Class13_GUIA.pdf (v2 - 2h)')

a2_c13_act = [
    ('VATS Justicia dia 3', '5 min'),
    ('Tarea Check Cl 12', '8 min'),
    ('Rompehielo - How TIRED are you? (DE PIE)', '10 min'),
    ('LIBRO M29 (lectura + explicacion)', '15 min'),
    ('Ejercicios M29', '12 min'),
    ('Simulacion - Interviewing my friend (DE PIE)', '15 min'),
    ('Shadowing Dia 3 PRESENTACION MEMORIA', '12 min'),
    ('GoldList 20 frases (Degrees)', '15 min'),
    ('Competencia por equipos', '7 min'),
    ('Autochequeo', '5 min'),
    ('Error Paper Live', '4 min'),
    ('Tarea + Cierre', '2 min'),
]
a2_c13_deliv = [
    'Reporte impreso lleno',
    'Foto/video Shadowing Dia 3 - material redes',
    'Papel errores fisico (anonimo)',
    '5 papelitos Autochequeo',
    '5 cuadernos GoldList con 20 frases (Degrees)',
    'Lista quienes NO entregaron tarea Cl 12',
    'Tu libreta personal con 3 errores literales + nombre por bloque',
]
a2_c13_eval = [
    'Lei el mensaje pedagogico al inicio',
    'Ejecute esta clase como REGULAR del programa (no usandola para "repaso" del midterm)',
    'Cubri SOLO M29 - M30 movido al lunes Cl 14',
    'Hice VATS Justicia dia 3',
    'Modelo el formato How + adj + verb correctamente',
    'Diferencie VERY vs EXTREMELY vs REALLY claramente',
    'Conduje Simulation Interviewing my friend con ritmo',
    'Grabo Shadowing Dia 3 (sin video)',
    'Lei 20 frases del GoldList con la clase',
    'Estudiantes copian GoldList sin estudiar',
    'NO acepte la excusa "estoy cansado por el midterm" para no participar',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
]

build_report_v2(
    os.path.join(A2_REPORTES, 'A2_4h_Class13_REPORTE.pdf'),
    'A2 INTENSIVO | Clase 13 de 28 | 2 HORAS DE CLASE (otras 2h son midterm)',
    'M29 Degrees of Adjectives | Justicia dia 3 | M30 movido al lunes Cl 14',
    a2_c13_act, a2_c13_deliv, a2_c13_eval, S,
)
print('OK: A2_4h_Class13_REPORTE.pdf (v2)')

print('\n6 PDFs generados:')
print('  B1:')
print('    - B1/B1_Clase9_GRAMMAR_GUIA.pdf (v3)')
print('    - B1/reportes/B1_Clase9_GRAMMAR_REPORTE.pdf (v3)')
print('    - B1/B1_Clase9_CONV_GUIA.pdf (v2)')
print('    - B1/reportes/B1_Clase9_CONV_REPORTE.pdf (v2)')
print('  A2 4h:')
print('    - A2/A2_4h_Class13_GUIA.pdf (v2 - 2h)')
print('    - A2/reportes/A2_4h_Class13_REPORTE.pdf (v2)')
