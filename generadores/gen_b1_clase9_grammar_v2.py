#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Re-genera B1 Cl 9 GRAMMAR v2 con ajustes (Shark Tank + B2-tier + Diferenciacion)
+ Comunicado para estudiantes."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_DIR = os.path.join(D, 'B1')
B1_REPORTES = os.path.join(B1_DIR, 'reportes')

# Re-genera GUIA Cl 9 Grammar
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase9_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase9_GRAMMAR_GUIA.pdf'),
)

# Re-genera REPORTE Cl 9 Grammar v2 (con bloques nuevos)
b1_c9_g_deliv = [
    'Hojas de autochequeo completadas',
    'Papel de errores fisico (anonimo)',
    'Tarea enviada al WhatsApp con DUE DATE + diferenciacion por nivel',
    '17 cuadernos GoldList con 20 frases del Dia 7 (B2-tier visible)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Foto del tablero del WORD UPGRADE A1->B2',
    'Foto/video del Shark Tank Grammar Edition (material redes)',
    'Foto del Battle Royale (ganador + grupo)',
    'Lista quienes NO entregaron tarea Cl 8',
    'Notas: tu energia hoy - con que bloque te conectaste mas/menos',
]
b1_c9_g_eval = [
    'Lei el mensaje pedagogico al inicio de la guia ANTES de clase',
    'Estudiantes hablaron 80%+ del tiempo',
    'Estuve DE PIE durante ~70% del bloque',
    'ESCRIBI el WORD UPGRADE B2-tier en el tablero ANTES de clase',
    'Mantuve el WORD UPGRADE visible toda la clase',
    'Conduje SHARK TANK GRAMMAR EDITION con energia y ritmo',
    'Conduje POSSESSIVE BATTLE ROYALE con velocidad',
    'Anuncie LA DIFERENCIACION visible (3 niveles) en el bloque Writing',
    'Asigne tarea con DIFERENCIACION explicita por nivel',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores con NOMBRE',
    'Hice VATS Justicia dia 2',
    'Refoze HIS vs HER (error fosilizable)',
    'NO acepte la excusa "es muy pesado"',
    'NO permiti tampoco la excusa "esto ya lo sabia" (respondi con vocabulario B2-tier)',
]
b1_c9_g_act = [
    ('VATS Justicia dia 2 (in English)', '7 min'),
    ('Tarea Check Walk & Share rapido (DE PIE)', '10 min'),
    ('VOCABULARY UPGRADE B2-TIER (NUEVO)', '8 min'),
    ('SHARK TANK GRAMMAR EDITION (NUEVO - DE PIE en grupos)', '17 min'),
    ('Gallery Walk Possessive Adjectives B2-tier (4 estaciones)', '13 min'),
    ('GoldList Dia 7 - 20 frases con B2-tier visible', '13 min'),
    ('Writing Sprint con DIFERENCIACION (3 niveles)', '13 min'),
    ('POSSESSIVE BATTLE ROYALE (NUEVO - DE PIE eliminacion)', '12 min'),
    ('Error Paper Live Peer Relay (DE PIE)', '10 min'),
    ('Tarea con DIFERENCIACION explicita + Wrap', '7 min'),
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase9_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 de 44 | BLOQUE 1: GRAMMAR & WRITING (v2 ajuste pedagogico)',
    'M14 Prepositions + M15 Possessive Adj + B2-TIER UPGRADE + Shark Tank + Battle Royale | Justicia dia 2',
    b1_c9_g_act, b1_c9_g_deliv, b1_c9_g_eval, S,
)
print('OK: B1 Cl 9 GRAMMAR v2 (con ajustes pedagogicos)')

# Comunicado para estudiantes
md_to_pdf(
    os.path.join(B1_DIR, 'COMUNICADO_B1_AJUSTE_PEDAGOGICO.md'),
    os.path.join(B1_DIR, 'COMUNICADO_B1_AJUSTE_PEDAGOGICO.pdf'),
)
print('OK: COMUNICADO para estudiantes')

print('\n2 PDFs generados.')
print('  - B1_Clase9_GRAMMAR_GUIA.pdf (v2 con ajustes)')
print('  - COMUNICADO_B1_AJUSTE_PEDAGOGICO.pdf (para enviar al cohorte despues de la reunion)')
