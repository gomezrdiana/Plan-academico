#!/usr/bin/env python3
"""Genera PDFs + reportes para A1 Christian Cl 24 + B2 Amina Cl 7 (martes 12/05/2026)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A1_DIR = os.path.join(D, 'A1')
B2_DIR = os.path.join(D, 'B2')
A1_REPORTES = os.path.join(A1_DIR, 'reportes')
B2_REPORTES = os.path.join(B2_DIR, 'reportes')

os.makedirs(A1_REPORTES, exist_ok=True)
os.makedirs(B2_REPORTES, exist_ok=True)

# ============================================================
# A1 Christian Cl 24
# ============================================================
md_to_pdf(
    os.path.join(A1_DIR, 'A1_Class24_PRINT.md'),
    os.path.join(A1_DIR, 'A1_Class24_GUIA.pdf'),
)

a1_c24_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS PRUDENCIA dia 4 (v2)', '5 min'),
    ('PEER TEACHER SLOT (estudiante rotado ensena 1-2 errores Cl 23)', '7 min'),
    ('Tarea Check Cl 23', '7 min'),
    ('VOCABULARY UPGRADE A1->A2-tier para M27 (acumula con Cl 23)', '10 min'),
    ('LIBRO M27 (lectura + explicacion dirigida)', '19 min'),
    ('Ejercicios M27', '10 min'),
    ('SIMULACION PROFESIONAL M27 (DE PIE)', '15 min'),
    ('GoldList Lista 24 - 20 frases con Prudencia + A2-tier', '13 min'),
    ('Shadowing (verificar dia del ciclo)', '9 min'),
    ('Error Paper Live', '5 min'),
    ('Tarea + Cierre', '3 min'),
]
a1_c24_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero del WORD UPGRADE A1->A2-tier (acumulado Cl 23+24)',
    'Foto/video de la Simulacion profesional',
    'Papel errores fisico (anonimo)',
    '6 cuadernos GoldList Lista 24 (20 frases con Prudencia)',
    'Lista quienes NO entregaron tarea Cl 23',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Lista actualizada de asistencia (cohorte 50-67%)',
    'Notas de tu energia hoy',
]
a1_c24_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad',
    'PROYECTE seguridad (preparacion previa, ritmo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'Conduje MYSTERY HOMEWORK CHECK llamando al azar (no solo voluntarios)',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'Conduje PEER TEACHER SLOT dejando al estudiante producir (sin rescate)',
    'ESCRIBI el WORD UPGRADE A1->A2-tier en el tablero ANTES de clase',
    'Mantuve el WORD UPGRADE de Cl 23 + agregue palabras nuevas para M27',
    'Cubri M27 completo (lectura libro + explicacion dirigida + ejercicios)',
    'Simulacion fue PROFESIONAL/realista (no temas personales de familia)',
    'Lei las 20 frases del GoldList con la clase',
    'CONDUJE Shadowing con foco en ritmo y entonacion',
    'NO acepte la excusa "no me dio tiempo" para no hacer tarea',
    'Camine con papel de errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'Anote asistencia hoy (cohorte tiene patron 50-67%)',
]

build_report_v2(
    os.path.join(A1_REPORTES, 'A1_Class24_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 24 de 45 | 2 HORAS',
    'M27 + Mystery + Peer Teacher + Vocabulary Upgrade + Simulacion | Prudencia dia 4 (v2)',
    a1_c24_act, a1_c24_deliv, a1_c24_eval, S,
)
print('OK: A1_Class24_REPORTE.pdf')

# ============================================================
# B2 Amina Cl 7
# ============================================================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase7_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase7_GUIA.pdf'),
)

b2_c7_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VOCALIZACION DRILL (trabalenguas NUEVOS)', '3 min'),
    ('VATS TEMPLANZA dia 2', '5 min'),
    ('ANCHOR RECAP - drill rapido (mantener Cl 6)', '5 min'),
    ('CONECTORES DE ARGUMENTACION Group A (NUEVO BLOQUE)', '15 min'),
    ('CONTRASTE TIEMPOS VERBALES drill', '8 min'),
    ('PEER TEACHER SLOT (corto - errores Cl 6)', '4 min'),
    ('Transicion a Speak About - criterios actualizados', '4 min'),
    ('SPEAK ABOUT YOUR TOPIC round 2 (criterios: anclas + connectors)', '45 min'),
    ('GoldList Lista 7 - 20 frases con connectors integrados', '12 min'),
    ('Error Paper Live (peer relay)', '7 min'),
    ('Tarea + Cierre + anuncio Cl 8', '5 min'),
]
b2_c7_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero de CONNECTORS (Group A escrito)',
    'Foto del tablero de ANCHORS (mantenidos de Cl 6)',
    'Foto/video de UN Speak About round 2 (con conteo visible de anchors + connectors usados)',
    'Papel errores fisico',
    '4-5 cuadernos GoldList Lista 7 (20 frases con connectors)',
    'Lista quienes NO entregaron tarea Cl 6 (audio 3 min)',
    'Tu libreta personal con 3 errores literales + NOMBRE por estudiante',
    'Asistencia: quien vino + quien falto',
    'Notas de tu energia hoy',
]
b2_c7_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'CONSOLIDE B1 antes de empujar a B2 puro (consolidacion antes de complejidad)',
    'PROYECTE seguridad (mi seguridad baja contagia los nervios del cohorte)',
    'NO puse a presentar largo (mini-bloques 5-7 min, no presentaciones largas que paralicen)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'PREPARE trabalenguas NUEVOS para Vocalizacion (no repeti los de Cl 6)',
    'ESCRIBI los CONNECTORS en seccion nueva del tablero ANTES de clase',
    'Mantuve las ANCHORS de Cl 6 en el tablero',
    'Conduje ANCHOR RECAP con pregunta sorpresa (no solo lectura)',
    'Introduje CONNECTORS Group A (addition / contrast / emphasis) - NO Group B',
    'Conduje SPEAK ABOUT con criterios actualizados (anclas + connectors + verb tenses)',
    'Verifique que las estudiantes usaran connectors organicamente (no solo lectura)',
    'PEER TEACHER fue CORTO (4 min) para no comer tiempo de Speak About',
    'Conduje Verb Tense Contrast drill mas rapido que ayer',
    'Anote 3 errores literales con NOMBRE por estudiante en libreta',
    'Conte cuantas estudiantes usaron connectors organicamente - si <50% reporto a Diana',
    'Camine con papel errores anonimo',
    'Anuncie Cl 8: Connectors Group B (resultado + conclusion)',
]

build_report_v2(
    os.path.join(B2_REPORTES, 'B2_PM_Amina_Clase7_REPORTE.pdf'),
    'B2 PM AMINA | Clase 7 de 36 | 2 HORAS | FASE 2 dia 2/7',
    'Speak About round 2 + Connectors Group A + Anchor recap + Vocalization + Verb Contrast | Templanza dia 2 (v1)',
    b2_c7_act, b2_c7_deliv, b2_c7_eval, S,
)
print('OK: B2_PM_Amina_Clase7_REPORTE.pdf')

print('\n4 PDFs generados:')
print('  - A1/A1_Class24_GUIA.pdf')
print('  - A1/reportes/A1_Class24_REPORTE.pdf')
print('  - B2/B2_PM_Amina_Clase7_GUIA.pdf')
print('  - B2/reportes/B2_PM_Amina_Clase7_REPORTE.pdf')
