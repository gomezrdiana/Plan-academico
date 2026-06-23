#!/usr/bin/env python3
"""Genera REPORTES B1 Cl 10 Grammar + Conv para martes 12/05/2026."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
B1_REPORTES = os.path.join(D, 'B1', 'reportes')
os.makedirs(B1_REPORTES, exist_ok=True)

# ============================================================
# B1 Cl 10 GRAMMAR
# ============================================================
b1_c10_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (estudiante rotado - errores recurrentes Cl 9)', '7 min'),
    ('Vocabulary Upgrade Academic B2 + palabras de Freakonomics', '10 min'),
    ('LIBRO M16 - Object Pronouns (lectura + explicacion dirigida)', '15 min'),
    ('Ejercicios M16 + Speed Drill', '10 min'),
    ('LIBRO M17 - Have/Has (lectura + explicacion dirigida)', '15 min'),
    ('Ejercicios M17 + integracion M16+M17', '8 min'),
    ('GoldList Lista 10 - 20 frases reflexivas con M16+M17+B2', '13 min'),
    ('Error Paper Live (peer relay)', '10 min'),
    ('Entrega del PASE a Danna + Tarea + Cierre', '8 min'),
]
b1_c10_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero del WORD UPGRADE Academic B2 + Freakonomics',
    'Papel errores fisico (anonimo)',
    '17 cuadernos GoldList Lista 10 (20 frases con M16+M17 integrados)',
    'COPIA del PASE entregado a Danna (con hora de entrega)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista quienes NO entregaron tarea Cl 9 alternativa',
    'Notas de tu energia hoy',
]
b1_c10_g_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad',
    'PROYECTE seguridad (preparacion previa, ritmo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'Use errores RECURRENTES del cohorte (mi bloque va PRIMERO hoy)',
    'ESCRIBI WORD UPGRADE Academic B2 + Freakonomics en tablero ANTES de clase',
    'Integre palabras de Freakonomics si los estudiantes las trajeron',
    'Cubri LIBRO M16 (Object Pronouns) con explicacion dirigida',
    'Cubri LIBRO M17 (Have/Has) introduciendo Present Perfect',
    'Hice INTEGRACION M16+M17 en ejercicios mixtos',
    'Lei las 20 frases del GoldList con la clase',
    'CONDUJE Error Paper Live como peer relay',
    'ENTREGUE PASE escrito a Danna ANTES de las 10:10 AM',
    'En libreta personal anote 3 errores con NOMBRE',
    'NO acepte la excusa "esto ya lo sabia"',
    'NO acepte la excusa "no me dio tiempo"',
]
build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase10_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 10 de 44 | BLOQUE 1: GRAMMAR & WRITING',
    'M16 Object Pronouns + M17 Have/Has + Vocab Freakonomics + Mystery + Peer Teacher',
    b1_c10_g_act, b1_c10_g_deliv, b1_c10_g_eval, S,
)
print('OK: B1_Clase10_GRAMMAR_REPORTE.pdf')

# ============================================================
# B1 Cl 10 CONV
# ============================================================
b1_c10_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS Reconnect (virtud del dia)', '7 min'),
    ('PEER TEACHER SLOT (con errores del PASE de Juan Diego)', '7 min'),
    ('Hot Topic - debate etico con M16+M17', '17 min'),
    ('Simulacion Profesional - defender posicion controversial', '22 min'),
    ('Shadowing (verificar dia del ciclo)', '15 min'),
    ('Project Workshop ORAL - Page 9 INFLUENCES SHAPED ME', '18 min'),
    ('Mini-Pitch 90 seg + Q&A en vivo', '10 min'),
    ('Error Paper Live + Tarea + Cierre', '7 min'),
]
b1_c10_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER usando errores del PASE',
    'PASE recibido de Juan Diego (archivado)',
    'Foto/video del Hot Topic + Simulacion',
    'Foto/video del Mini-Pitch',
    'Foto/video Shadowing',
    'Papel errores fisico',
    'Lista de errores recurrentes para PASE al profesor de Grammar manana',
    '17 Paginas 9 del proyecto INFLUENCES SHAPED ME (foto)',
    'Libreta personal con 3 errores literales + nombre por bloque',
]
b1_c10_c_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad (preparacion previa, ritmo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'RECIBI el PASE escrito de Juan Diego ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con los errores del PASE',
    'Use TEMAS NO PERSONALES en todos los bloques',
    'Hot Topic fue debate etico con figuras publicas',
    'Simulacion fue defensa de posicion controversial (no familia)',
    'Mini-Pitch fue debate etico (no persona importante en mi vida)',
    'Project Page 9 fue INFLUENCES PROFESIONALES (no familia)',
    'Refoze M16 + M17 oralmente en debate real',
    'Conduje Shadowing con foco en ritmo y entonacion',
    'Anote 3 errores literales con NOMBRE en libreta personal',
    'Camine con papel errores anonimo',
    'PREPARE lista de errores para PASE de manana al Grammar',
    'Estudiantes hablaron 80%+ del tiempo',
]
build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase10_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 10 de 44 | BLOQUE 2: CONVERSACIONAL',
    'M16+M17 en debate + Page 9 INFLUENCES SHAPED ME + Mini-Pitch + PASE de Grammar',
    b1_c10_c_act, b1_c10_c_deliv, b1_c10_c_eval, S,
)
print('OK: B1_Clase10_CONV_REPORTE.pdf')

print('\n2 reportes generados.')
