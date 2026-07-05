#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera 6 guias + 6 reportes para JUEVES 7 mayo + VIERNES 8 mayo 2026:

JUEVES (3):
- A1 Cl 21 - M25 How are you? + Prep Midterm - Prudencia v2 dia 1 - Shadowing Dia 3 (memoria)
- A2 PM Cl 21 - M23 Phrasal Verbs No Separables - Prudencia v2 dia 1 - Shadowing Dia 3 (memoria)
- B2 Amina Cl 4 - Estructura monologo - Templanza dia 5 - Shadowing Dia 3 (memoria)

VIERNES (3):
- A1 Cl 22 MIDTERM A1 - Prudencia v2 dia 2 - SIN shadowing
- A2 PM Cl 22 - M24 Separable Phrasal Verbs - Prudencia v2 dia 2 - Shadowing Dia 1 NUEVO
- B2 Amina Cl 5 CIERRE FASE 1 - Justicia dia 1 - Shadowing Dia 1 NUEVO
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A2_DIR = os.path.join(D, 'A2')
B2_DIR = os.path.join(D, 'B2')

# ===================================================
# JUEVES 7/5
# ===================================================

# === A1 Cl 21 ===
md_to_pdf(
    os.path.join(A1_DIR, 'A1_Class21_PRINT.md'),
    os.path.join(A1_DIR, 'A1_Clase21_GUIA.pdf'),
)
a1_c21_blocks = [
    ('00:00-00:05', 'VATS Prudencia v2 dia 1'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 20'),
    ('00:13-00:28', 'Libro M25 Respuestas reales a How are you'),
    ('00:28-00:38', 'REPARTO TEMAS DEL MIDTERM + escogen'),
    ('00:38-01:00', 'PREP MIDTERM Presentaciones 90 seg en grupos'),
    ('01:00-01:15', 'Shadowing Dia 3 PRESENTACION DE MEMORIA'),
    ('01:15-01:35', 'Repaso Final Pre-Midterm 5 errores mas peligrosos A1'),
    ('01:35-01:45', 'GoldList Lista 21 - 5 frases'),
    ('01:45-02:00', 'Tarea + Cierre + animo final'),
]
a1_c21_obs = [
    ('Quienes escogieron cada tema del Midterm?', 'Anotar nombre + tema'),
    ('2-3 estudiantes con apoyo necesario antes del Midterm', 'Que necesitan'),
    ('3 errores LITERALES con NOMBRE', 'OBLIGATORIO'),
    ('Foto/video del Shadowing Dia 3 Memoria', 'Material redes'),
    ('Estudiantes que dijeron "es muy pesado"', 'Si aplico la regla firme'),
]
build_report_1page(
    'A1 NOCTURNO 2H', 21,
    'M25 How are you respuestas reales + PREP MIDTERM - Prudencia v2 dia 1',
    a1_c21_blocks, a1_c21_obs,
    os.path.join(A1_DIR, 'A1_Clase21_REPORTE.pdf'),
    cycle_day='3-Present',
)
print('OK: A1 Cl 21 (jueves)')

# === A2 PM Cl 21 ===
md_to_pdf(
    os.path.join(A2_DIR, 'A2_Class21_PRINT.md'),
    os.path.join(A2_DIR, 'A2_Clase21_GUIA.pdf'),
)
a2_c21_blocks = [
    ('00:00-00:05', 'VATS Prudencia v2 dia 1'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 20'),
    ('00:13-00:28', 'Libro M23 Phrasal Verbs No Separables'),
    ('00:28-00:38', 'Ejercicios + Parejas'),
    ('00:38-00:53', 'Simulacion Customer Service Call (DE PIE)'),
    ('00:53-01:08', 'Shadowing Dia 3 PRESENTACION DE MEMORIA'),
    ('01:08-01:20', 'Historia Interactiva absurda - Pedro y la Sandia'),
    ('01:20-01:32', 'MINI-PITCH 90 seg + Q&A en vivo'),
    ('01:32-01:42', 'GoldList Lista 21 - 5 frases'),
    ('01:42-01:55', 'Errores + Peer Correction'),
    ('01:55-02:00', 'Autochequeo + Tarea + Cierre'),
]
a2_c21_obs = [
    ('Phrasal Verbs No Separables - dominaron prep correcta?',
     'Errores tipicos: looking my keys for, listening the music'),
    ('Mini-Pitch + Q&A - quien destaco?', 'Estudiantes excepcionales'),
    ('3 errores LITERALES con NOMBRE de estudiante', 'OBLIGATORIO'),
    ('Foto/video del Shadowing Dia 3 Memoria', 'Material redes'),
    ('Estudiantes que dijeron "es muy pesado"', 'Si aplico la regla firme'),
]
build_report_1page(
    'A2 NOCTURNO 2H', 21,
    'M23 Phrasal Verbs No Separables - Prudencia v2 dia 1 - Shadowing Dia 3',
    a2_c21_blocks, a2_c21_obs,
    os.path.join(A2_DIR, 'A2_Clase21_REPORTE.pdf'),
    cycle_day='3-Present',
)
print('OK: A2 PM Cl 21 (jueves)')

# === B2 Amina Cl 4 ===
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase4_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase4_GUIA.pdf'),
)
b2_c4_deliverables = [
    'Hojas de autochequeo completadas',
    'Foto/video del Shadowing Dia 3 (presentacion memoria) - material redes',
    'Papel de errores fisico (anonimo)',
    '5 hojas con esqueleto del monologo (hook + 3 puntos + cierre)',
    'Cuadernos GoldList con 5 frases Lista 22',
    'Lista de quienes NO entregaron tarea Cl 3',
    'Libreta personal con minimo 3 errores literales + NOMBRE',
    'Notas: estructura mas fuerte / mas debil del grupo',
]
b2_c4_selfeval = [
    'Las estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY',
    'Hice VATS Templanza dia 5',
    'Conduje el bloque ESTRUCTURA DEL MONOLOGO (hook + 3 puntos + cierre)',
    'Cada estudiante armo SU esqueleto en voz alta',
    'Hice Shadowing Dia 3 PRESENTACION DE MEMORIA (sin video)',
    'Grabe video del Shadowing Dia 3 para redes',
    'Hice Mini-Pitch del esqueleto + Q&A en vivo (5 estudiantes)',
    'Ensene 10 phrases B2-tier para hook + cierre',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores literales con NOMBRE',
    'NO acepte la excusa "es muy pesado"',
    'Asigne tarea Cl 5 con DUE DATE explicita',
    'Envie entregables a coordinacion',
]
b2_c4_activities = [
    ('VATS Templanza dia 5 (in English)', '7 min'),
    ('Revision tarea Cl 3 - 3 datos investigados + audio', '8 min'),
    ('ESTRUCTURA DEL MONOLOGO - HOOK + 3 PUNTOS + CIERRE', '25 min'),
    ('Cada estudiante arma SU esqueleto en voz alta', '25 min'),
    ('Shadowing Dia 3 PRESENTACION DE MEMORIA (sin video)', '15 min'),
    ('MINI-PITCH del esqueleto + Q&A en vivo', '20 min'),
    ('Vocabulario B2-tier para HOOK + CIERRE (10 phrases)', '10 min'),
    ('Error Paper Live + Tarea con due date', '7 min'),
    ('GoldList Lista 22 + Cierre', '3 min'),
]
build_report_v2(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase4_REPORTE.pdf'),
    'B2 PM AMINA | Clase 4 de 36 | 66h hasta el Final',
    'Fase 1 Dia 4 - Estructura del monologo (hook + 3 puntos + cierre) + Shadowing Dia 3 | Templanza dia 5',
    b2_c4_activities,
    b2_c4_deliverables,
    b2_c4_selfeval,
    S,
)
print('OK: B2 Amina Cl 4 (jueves)')


# ===================================================
# VIERNES 8/5
# ===================================================

# === A1 Cl 22 MIDTERM ===
md_to_pdf(
    os.path.join(A1_DIR, 'A1_Class22_MIDTERM_PRINT.md'),
    os.path.join(A1_DIR, 'A1_Clase22_MIDTERM_GUIA.pdf'),
)
a1_c22_blocks = [
    ('00:00-00:05', 'VATS Prudencia v2 dia 2 - calmar ansiedad'),
    ('00:05-00:10', 'Repaso del formato + 5 errores fosilizables'),
    ('00:10-00:15', 'Sortear orden de presentacion'),
    ('00:15-01:45', 'MIDTERM - 6 estudiantes x 5 min cada uno'),
    ('01:45-01:55', 'Cierre del midterm - sin revelar notas'),
    ('01:55-02:00', 'Tarea (descanso) + Cierre'),
]
a1_c22_obs = [
    ('6 RUBRICAS LLENAS (1 por estudiante)', 'OBLIGATORIO. Entregar a coordinacion'),
    ('3 errores literales por estudiante con cita textual', 'OBLIGATORIO en libreta'),
    ('1-2 fortalezas observadas por estudiante', 'OBLIGATORIO'),
    ('Recomendacion especifica por estudiante para proximas clases', 'Que reforzar'),
    ('Tabla hora inicio/fin por presentacion', 'Para coordinacion'),
]
build_report_1page(
    'A1 NOCTURNO 2H', 22,
    'MIDTERM A1 OFICIAL - Speaking + Q&A en vivo - Prudencia v2 dia 2',
    a1_c22_blocks, a1_c22_obs,
    os.path.join(A1_DIR, 'A1_Clase22_REPORTE.pdf'),
    cycle_day=None,  # SIN shadowing por midterm
)
print('OK: A1 Cl 22 MIDTERM (viernes)')

# === A2 PM Cl 22 ===
md_to_pdf(
    os.path.join(A2_DIR, 'A2_Class22_PRINT.md'),
    os.path.join(A2_DIR, 'A2_Clase22_GUIA.pdf'),
)
a2_c22_blocks = [
    ('00:00-00:05', 'VATS Prudencia v2 dia 2'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 21'),
    ('00:13-00:28', 'Libro M24 Separable Phrasal Verbs'),
    ('00:28-00:38', 'Ejercicios + Parejas'),
    ('00:38-00:53', 'Simulacion Moving Day (DE PIE)'),
    ('00:53-01:08', 'Shadowing 5 pasos DIA 1 NUEVO ciclo'),
    ('01:08-01:20', 'Historia Interactiva absurda - El Robot Roberto'),
    ('01:20-01:32', 'MINI-PITCH 90 seg + Q&A en vivo'),
    ('01:32-01:42', 'GoldList Lista 22 - 5 frases'),
    ('01:42-01:55', 'Errores + Peer Correction'),
    ('01:55-02:00', 'Autochequeo + Tarea + Cierre'),
]
a2_c22_obs = [
    ('Phrasal Verbs Separables - dominaron pronombre OBLIGATORIO separar?',
     'Errores: turn on it, pick up them'),
    ('Mini-Pitch + Q&A - quien destaco?', 'Estudiantes excepcionales'),
    ('3 errores LITERALES con NOMBRE', 'OBLIGATORIO'),
    ('URL video Shadowing Dia 1 NUEVO',
     'https://www.youtube.com/watch?v=L147kFfchtI'),
    ('Estudiantes que dijeron "es muy pesado"', 'Si aplico la regla firme'),
]
build_report_1page(
    'A2 NOCTURNO 2H', 22,
    'M24 Separable Phrasal Verbs - Prudencia v2 dia 2 - Shadowing Dia 1 NUEVO',
    a2_c22_blocks, a2_c22_obs,
    os.path.join(A2_DIR, 'A2_Clase22_REPORTE.pdf'),
    cycle_day=1,
)
print('OK: A2 PM Cl 22 (viernes)')

# === B2 Amina Cl 5 ===
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase5_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase5_GUIA.pdf'),
)
b2_c5_deliverables = [
    'Hojas de autochequeo completadas',
    'URL del video Shadowing Dia 1 NUEVO ciclo anotada',
    'Papel de errores fisico (anonimo)',
    '5 esqueletos del monologo (foto o copia) - hook + 3 puntos + cierre',
    'Cuadernos GoldList con 5 frases Lista 23',
    'Lista de quienes NO entregaron tarea Cl 4',
    'CHECKPOINT 1 - libreta personal con dx actualizado de las 5 + 1 fortaleza + 1 area mejora por esqueleto',
    'Foto/video del Round Table o Cierre Fase 1 para redes',
]
b2_c5_selfeval = [
    'Las estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY',
    'Hice VATS Justicia dia 1 (cambio de virtud)',
    'Conduje las 5 PRESENTACIONES del esqueleto (3 min cada una + 1 Q&A)',
    'Hice Shadowing Dia 1 NUEVO ciclo con video confirmado',
    'Anote URL del video nuevo en el reporte',
    'Conduje el Round Table de feedback grupal',
    'Ensene 10 phrases B2-tier connectors para BODY',
    'Hice mini-presentacion cierre 1 frase por estudiante',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores literales con NOMBRE',
    'En libreta anote 1 fortaleza + 1 area mejora del esqueleto de cada una',
    'NO acepte la excusa "es muy pesado" (tarea fin de semana)',
    'Asigne tarea Cl 6 con DUE DATE explicita',
    'CHECKPOINT 1 entregables completos para coordinacion',
]
b2_c5_activities = [
    ('VATS JUSTICIA dia 1 (cambio de virtud)', '7 min'),
    ('Revision tarea Cl 4 - audio 3 min monologo', '8 min'),
    ('PRESENTACION del esqueleto - 3 min x 5 estudiantes + Q&A', '30 min'),
    ('Shadowing 5 pasos DIA 1 NUEVO ciclo (video nuevo)', '15 min'),
    ('Round Table - feedback grupal del esqueleto', '15 min'),
    ('Vocabulario B2-tier para BODY del monologo (10 phrases)', '15 min'),
    ('Mini-presentacion cierre - 1 frase por persona', '10 min'),
    ('Error Paper Live + Tarea con due date', '10 min'),
    ('GoldList Lista 23 + Cierre Fase 1 + animo', '10 min'),
]
build_report_v2(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase5_REPORTE.pdf'),
    'B2 PM AMINA | Clase 5 de 36 | CIERRE FASE 1 | 64h hasta el Final',
    'Cierre Fase 1 - Esqueleto presentado + Round Table + Shadowing Dia 1 NUEVO | Justicia dia 1',
    b2_c5_activities,
    b2_c5_deliverables,
    b2_c5_selfeval,
    S,
)
print('OK: B2 Amina Cl 5 CIERRE FASE 1 (viernes)')

print('\n6 guias + 6 reportes generados:')
print('JUEVES 7/5: A1 Cl 21, A2 PM Cl 21, B2 Amina Cl 4')
print('VIERNES 8/5: A1 Cl 22 MIDTERM, A2 PM Cl 22, B2 Amina Cl 5')
print('\nVideos confirmados:')
print('  Viernes A2 PM: https://www.youtube.com/watch?v=L147kFfchtI')
print('  Viernes B2 Amina: https://www.youtube.com/watch?v=zJf-J5RXxw8')
print('  Lunes 11/5 A1 (proxima sesion): https://www.youtube.com/watch?v=pONmJiKK_WI')
