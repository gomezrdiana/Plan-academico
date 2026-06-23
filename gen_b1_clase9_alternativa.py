#!/usr/bin/env python3
"""Genera PDFs B1 Cl 9 ALTERNATIVA (Grammar + Conv) — reemplaza versiones anteriores.
Aplicada lunes 11/05/2026 — consolidacion M14+M15 con actividades nuevas post-reunion."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
B1_DIR = os.path.join(D, 'B1')
B1_REPORTES = os.path.join(B1_DIR, 'reportes')

os.makedirs(B1_REPORTES, exist_ok=True)

# ============================================================
# B1 Cl 9 GRAMMAR ALTERNATIVA
# ============================================================

md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase9_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase9_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase9_GRAMMAR_GUIA.pdf (ALTERNATIVA)')

b1_c9_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS Justicia dia 3 (filosofica)', '7 min'),
    ('PEER TEACHER SLOT (estudiante rotado ensena errores Cl 8)', '7 min'),
    ('Vocabulary Upgrade Academic B2 (palabras nuevas)', '10 min'),
    ('SPEED DATING CONVERSATIONAL (rotacion rapida prompts)', '16 min'),
    ('TRANSLATION CHAIN (A traduce, B mejora, C pule)', '13 min'),
    ('GoldList Dia NUEVO - 20 frases reflexivas DISTINTAS', '13 min'),
    ('Writing Sprint argumentativo con DIFERENCIACION', '12 min'),
    ('Possessive Battle Royale - figuras NUEVAS', '10 min'),
    ('Error Paper Live (peer relay)', '10 min'),
    ('Tarea con DIFERENCIACION + Wrap', '5 min'),
]
b1_c9_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check (instruccion visible)',
    'Foto/video del PEER TEACHER en accion - material auditoria',
    'Foto del tablero del WORD UPGRADE Academic B2 NUEVO',
    'Papel de errores fisico (anonimo)',
    '17 cuadernos GoldList con 20 frases NUEVAS reflexivas',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Foto/video del Speed Dating - material redes',
    'Lista quienes NO entregaron tarea Cl 8',
    'Foto del trabajo de Translation Chain (oraciones polishadas)',
    'Notas de tu energia hoy - con que bloque te conectaste mas/menos',
]
b1_c9_g_eval = [
    'Lei el mensaje pedagogico al inicio de la guia ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque (cero espanol)',
    'EXPLIQUE EL POR QUE DE HOY al inicio (2 min)',
    'EXPLIQUE EL OBJETIVO de cada actividad antes de empezarla',
    'APLIQUE consolidacion antes de complejidad',
    'PROYECTE seguridad (preparacion previa, ritmo, sin titubeo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion (rotacion visible)',
    'Conduje MYSTERY HOMEWORK CHECK llamando estudiantes al azar',
    'Conduje PEER TEACHER dejando que el estudiante produzca (sin rescate inmediato)',
    'ESCRIBI el WORD UPGRADE Academic B2 NUEVO en el tablero ANTES de clase',
    'Conduje SPEED DATING con cronometro estricto (5 rondas 90 seg)',
    'Conduje TRANSLATION CHAIN con 3 oraciones distintas',
    'Lei las 20 frases NUEVAS del GoldList con la clase',
    'Anuncie LA DIFERENCIACION visible (3 niveles) en el Writing argumentativo',
    'Conduje POSSESSIVE BATTLE ROYALE con figuras NUEVAS (no repeti Cl 8)',
    'Asigne tarea con DIFERENCIACION explicita por nivel',
    'NO permiti la excusa "esto ya lo sabia" (respondi con academic B2)',
    'En libreta personal anote 3 errores con NOMBRE',
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase9_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 ALTERNATIVA | BLOQUE 1: GRAMMAR & WRITING',
    'M14+M15 consolidacion + Mystery + Peer Teacher + Speed Dating + Translation Chain + Academic B2 nuevo | Justicia dia 3',
    b1_c9_g_act, b1_c9_g_deliv, b1_c9_g_eval, S,
)
print('OK: B1_Clase9_GRAMMAR_REPORTE.pdf (ALTERNATIVA)')

# ============================================================
# B1 Cl 9 CONV ALTERNATIVA
# ============================================================

md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase9_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase9_CONV_GUIA.pdf'),
)
print('OK: B1_Clase9_CONV_GUIA.pdf (ALTERNATIVA)')

b1_c9_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS Reconnect Justicia dia 3', '7 min'),
    ('PEER TEACHER SLOT (estudiante ensena errores de Grammar)', '7 min'),
    ('Hot Topic AI vs Human Creativity (NUEVO debate)', '17 min'),
    ('Press Conference Simulation (NUEVO formato - DE PIE)', '22 min'),
    ('Shadowing Dia 1 NUEVO ciclo', '15 min'),
    ('Project Workshop ORAL - Page 8 MY IMPACT', '18 min'),
    ('Mini-Pitch Elevator 60 seg (NUEVO formato)', '10 min'),
    ('Error Paper Live + Tarea + Cierre', '7 min'),
]
b1_c9_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto/video del Press Conference - material redes',
    'Foto/video del Mini-Pitch Elevator',
    'Foto/video Shadowing Dia 1 nuevo ciclo - material redes',
    'Papel errores fisico (anonimo)',
    'Lista de errores recurrentes para PASE al profesor de Bloque 1 martes',
    '17 Paginas 8 del proyecto MY IMPACT (foto)',
    'Foto del podio English Points',
    'Tu libreta personal con 3 errores literales + nombre por bloque oral',
]
b1_c9_c_eval = [
    'Lei el mensaje pedagogico al inicio de la guia',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL POR QUE DE HOY al inicio (2 min)',
    'PROYECTE seguridad con preparacion previa',
    'PREPARE el SOBRE del Mystery Homework Check',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'Conduje HOT TOPIC AI con debate fluido (no monologos)',
    'Conduje PRESS CONFERENCE con 5-6 estudiantes en roles diferentes',
    'Conduje MINI-PITCH ELEVATOR con 3 voluntarios + Q&A en vivo',
    'Conduje Shadowing Dia 1 nuevo ciclo con video confirmado',
    'Use TEMAS NO PERSONALES en todos los bloques',
    'Refoze HIS vs HER en contexto figuras publicas',
    'Practique 2+ academic B2 words por bloque',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase9_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 ALTERNATIVA | BLOQUE 2: CONVERSACIONAL',
    'HIS/HER + prepositions oral + AI debate + Press Conference + Mini-Pitch Elevator + Page 8 MY IMPACT | Justicia dia 3',
    b1_c9_c_act, b1_c9_c_deliv, b1_c9_c_eval, S,
)
print('OK: B1_Clase9_CONV_REPORTE.pdf (ALTERNATIVA)')

print('\n4 PDFs generados:')
print('  - B1/B1_Clase9_GRAMMAR_GUIA.pdf (ALTERNATIVA)')
print('  - B1/reportes/B1_Clase9_GRAMMAR_REPORTE.pdf (ALTERNATIVA)')
print('  - B1/B1_Clase9_CONV_GUIA.pdf (ALTERNATIVA)')
print('  - B1/reportes/B1_Clase9_CONV_REPORTE.pdf (ALTERNATIVA)')
