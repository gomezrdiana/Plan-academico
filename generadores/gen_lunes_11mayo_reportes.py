#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera REPORTES para las 3 clases nocturnas del lunes 11/05/2026."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_REPORTES = os.path.join(D, 'A1', 'reportes')
A2_REPORTES = os.path.join(D, 'A2', 'reportes')
B2_REPORTES = os.path.join(D, 'B2', 'reportes')

os.makedirs(A1_REPORTES, exist_ok=True)
os.makedirs(A2_REPORTES, exist_ok=True)
os.makedirs(B2_REPORTES, exist_ok=True)

# ============================================================
# B2 PM AMINA Cl 6
# ============================================================
b2_c6_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VOCALIZACION DRILL (trabalenguas)', '3 min'),
    ('PEER TEACHER SLOT (estudiante rotada)', '7 min'),
    ('ANCLAS DE CONEXION (frases-puente bajo blanco)', '12 min'),
    ('CONTRASTE TIEMPOS VERBALES drill', '10 min'),
    ('Transicion a Speak About', '6 min'),
    ('SPEAK ABOUT YOUR TOPIC (4 estudiantes x 11 min)', '45 min'),
    ('GoldList Lista 6 - 20 frases argumentativas B2', '15 min'),
    ('Error Paper Live', '8 min'),
    ('Tarea + Cierre + anuncio Cl 7', '7 min'),
]
b2_c6_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero de ANCHORS OF CONNECTION',
    'Foto/video de UN Speak About (5 min) - material redes',
    'Papel errores fisico',
    '4-5 cuadernos GoldList Lista 6 (20 frases argumentativas)',
    'Lista quienes NO entregaron tarea Cl 5 (audio 3 min)',
    'Tu libreta personal con 3 errores literales + NOMBRE por estudiante',
    'Asistencia: anotar si Maria Alejandra vino o no',
    'Notas de tu energia hoy',
]
b2_c6_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES (Amina native = facil pero verificar)',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad (libro B1 base)',
    'PROYECTE seguridad (preparacion previa, ritmo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion (rotacion visible)',
    'Conduje MYSTERY HOMEWORK CHECK llamando estudiantes al azar',
    'Conduje VOCALIZACION DRILL (3 trabalenguas)',
    'Conduje PEER TEACHER dejando producir sin rescate inmediato',
    'ESCRIBI ANCHORS OF CONNECTION en el tablero ANTES de clase',
    'Conduje el drill de Anchors con presion (3 seg max para arrancar)',
    'Conduje CONTRASTE TIEMPOS VERBALES con 8-10 ejemplos',
    'SPEAK ABOUT YOUR TOPIC: cada estudiante 5 min + preguntas (no presentaciones largas)',
    'Lei las 20 frases ARGUMENTATIVAS del GoldList con la clase',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'Camine con papel errores anonimo durante Speak About',
    'NO acepte la excusa "no me dio tiempo"',
    'Anote si Maria Alejandra asistio o no',
]
build_report_v2(
    os.path.join(B2_REPORTES, 'B2_PM_Amina_Clase6_REPORTE.pdf'),
    'B2 PM AMINA | Clase 6 de 36 | ARRANQUE FASE 2',
    'Recoleccion Oral + Anchors of Connection + Vocalization + Speak About Your Topic',
    b2_c6_act, b2_c6_deliv, b2_c6_eval, S,
)
print('OK: B2_PM_Amina_Clase6_REPORTE.pdf')

# ============================================================
# A2 PM Cl 23
# ============================================================
a2_c23_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (estudiante rotado errores Cl 22)', '7 min'),
    ('Tarea Check Cl 22', '5 min'),
    ('Vocabulary Upgrade A2-tier para phrasal verbs', '10 min'),
    ('LIBRO M25 - Phrasal Verbs INSEPARABLES (lectura + explicacion)', '20 min'),
    ('Ejercicios M25 (Separables vs Inseparables)', '10 min'),
    ('SIMULACION PROFESIONAL M25 (DE PIE)', '15 min'),
    ('GoldList Lista 23 - 20 frases A2-tier', '13 min'),
    ('Shadowing (verificar dia del ciclo)', '10 min'),
    ('Error Paper Live', '5 min'),
    ('Tarea + Cierre', '3 min'),
]
a2_c23_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero del WORD UPGRADE phrasal verbs',
    'Foto/video de la Simulacion profesional - material redes',
    'Foto/video Shadowing - material redes',
    'Papel errores fisico (anonimo)',
    '10 cuadernos GoldList Lista 23 (20 frases A2-tier)',
    'Lista quienes NO entregaron tarea Cl 22',
    'Tu libreta personal con 3 errores literales + nombre por bloque',
    'Notas de tu energia hoy',
]
a2_c23_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque (cero espanol)',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad',
    'PROYECTE seguridad (preparacion previa, ritmo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion (rotacion visible)',
    'Conduje MYSTERY HOMEWORK CHECK llamando estudiantes al azar',
    'Conduje PEER TEACHER dejando producir sin rescate inmediato',
    'ESCRIBI WORD UPGRADE phrasal verbs en tablero ANTES de clase',
    'Mantuve WORD UPGRADE visible toda la clase',
    'Cubri LIBRO M25 con contraste M24 (separables vs inseparables)',
    'Simulacion fue PROFESIONAL/realista (no temas personales de familia)',
    'Lei las 20 frases del GoldList con la clase',
    'Conduje Shadowing con foco en ritmo y entonacion',
    'NO acepte la excusa "no me dio tiempo"',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
]
build_report_v2(
    os.path.join(A2_REPORTES, 'A2_Class23_REPORTE.pdf'),
    'A2 NOCTURNO 2H | Clase 23 de 55',
    'M25 Phrasal Verbs INSEPARABLES + Mystery + Peer Teacher + Vocab Upgrade A2-tier',
    a2_c23_act, a2_c23_deliv, a2_c23_eval, S,
)
print('OK: A2_Class23_REPORTE.pdf')

# ============================================================
# A1 Cl 23 (POST-MIDTERM)
# ============================================================
a1_c23_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (estudiante rotado)', '7 min'),
    ('Tarea Check Cl 21 + cierre breve del midterm', '7 min'),
    ('Vocabulary Upgrade A1->A2-tier', '10 min'),
    ('LIBRO M26 (lectura + explicacion dirigida)', '19 min'),
    ('Ejercicios M26', '10 min'),
    ('SIMULACION PROFESIONAL M26 (DE PIE)', '15 min'),
    ('GoldList Lista 23 - 20 frases A1->A2-tier', '13 min'),
    ('Shadowing (verificar dia del ciclo)', '9 min'),
    ('Error Paper Live', '5 min'),
    ('Tarea + Cierre', '3 min'),
]
a1_c23_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero del WORD UPGRADE A1->A2',
    'Foto/video de la Simulacion profesional',
    'Papel errores fisico (anonimo)',
    '6 cuadernos GoldList Lista 23 (20 frases)',
    'Lista quienes NO entregaron tarea Cl 21',
    'Tu libreta personal con 3 errores literales + nombre por bloque',
    'Lista actualizada de asistencia (cohorte 50-67%)',
    'Notas de tu energia hoy',
]
a1_c23_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad (especial A1)',
    'PROYECTE seguridad (preparacion previa, ritmo, sin titubeo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'Conduje MYSTERY HOMEWORK CHECK llamando al azar',
    'Conduje PEER TEACHER dejando producir',
    'ESCRIBI WORD UPGRADE A1->A2 en tablero ANTES de clase',
    'CIERRE breve del midterm SIN comunicar notas (regla firme)',
    'Cubri M26 con verificacion del plan estructural',
    'Simulacion fue PROFESIONAL/realista (no familia)',
    'Lei las 20 frases del GoldList con la clase',
    'Conduje Shadowing con foco en ritmo',
    'NO acepte la excusa "no me dio tiempo"',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'Anote asistencia (cohorte tiene problema 50-67%)',
]
build_report_v2(
    os.path.join(A1_REPORTES, 'A1_Class23_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 23 de 45 (POST-MIDTERM)',
    'M26 + Mystery + Peer Teacher + Vocab Upgrade A1->A2 + Cierre del midterm',
    a1_c23_act, a1_c23_deliv, a1_c23_eval, S,
)
print('OK: A1_Class23_REPORTE.pdf')

print('\n3 reportes generados.')
