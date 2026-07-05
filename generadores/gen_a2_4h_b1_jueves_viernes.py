#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera 6 guias + 6 reportes para JUEVES 7 + VIERNES 8 mayo 2026:

A2 4h MAÑANA (Tomas AM):
- Cl 12 jueves - M27 Unequal + M28 Superlative - Justicia dia 2 - Shadowing Dia 2
- Cl 13 viernes - M29 Degrees + M30 Required Levels - Justicia dia 3 - Shadowing Dia 3 memoria

B1 MASTERY:
- Cl 8 Grammar jueves - M12 Frequency Adverbs + M13 Frequency Expressions - Justicia dia 1
- Cl 8 Conv jueves - aplicacion oral M12+M13 - Justicia dia 1 - Shadowing Dia 2
- Cl 9 Grammar viernes - M14 Prepositions + M15 Possessive Adjectives - Justicia dia 2
- Cl 9 Conv viernes - aplicacion oral M14+M15 - Justicia dia 2 - Shadowing Dia 3 memoria
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
B1_DIR = os.path.join(D, 'B1')
B1_REPORTES = os.path.join(B1_DIR, 'reportes')
os.makedirs(B1_REPORTES, exist_ok=True)

# ===========================================
# A2 4h AM Cl 12 (jueves)
# ===========================================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class12_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Clase12_GUIA.pdf'),
)
a2_4h_c12_blocks = [
    ('8:00-8:05', 'VATS Justicia dia 2'),
    ('8:05-8:13', 'Analizo Revision tarea Cl 11'),
    ('8:13-8:23', 'Rompehielo Im Smarter than'),
    ('8:23-8:38', 'Libro Modulo 27 Unequal Comparatives'),
    ('8:38-8:50', 'Ejercicios + Respuestas Mod 27'),
    ('8:50-9:10', 'Simulacion Comparando Mi Vida (DE PIE)'),
    ('9:10-9:22', 'Shadowing 5 pasos Dia 2 mismo video'),
    ('9:22-9:32', 'Historia Interactiva absurda - El hermano mayor'),
    ('9:32-9:42', 'Competencia equipos Mod 27'),
    ('9:42-9:52', 'GoldList 20 frases'),
    ('9:52-9:57', 'Autochequeo'),
    ('9:57-10:00', 'Transicion'),
    ('10:00-10:20', 'BREAK'),
    ('10:20-10:25', 'Reconnect virtud + Re-anclaje'),
    ('10:25-10:35', 'Intro Superlative'),
    ('10:35-10:50', 'Libro Modulo 28 Superlative'),
    ('10:50-11:00', 'Ejercicios + Respuestas Mod 28'),
    ('11:00-11:20', 'Simulacion El mejor de... (DE PIE)'),
    ('11:20-11:30', 'Historia Interactiva absurda - El mejor perro Max'),
    ('11:30-11:40', 'Competencia equipos Mod 28'),
    ('11:40-11:48', 'Free Production conversacion mixta M27+M28'),
    ('11:48-11:55', 'Autochequeo + Error Paper'),
    ('11:55-12:00', 'Tarea + Cierre'),
]
a2_4h_c12_obs = [
    ('M27 Unequal Comparatives - dominaron -er than / more than / irregulares?',
     'Errores: more taller, gooder than'),
    ('M28 Superlative - dominaron the -est / the most / the best?',
     'Errores: most kind, more big'),
    ('3 errores LITERALES con NOMBRE de estudiante', 'OBLIGATORIO'),
    ('URL video Shadowing Dia 2', 'https://www.youtube.com/watch?v=MFXOcfz177Q'),
    ('Estudiantes que dijeron "es muy pesado"', 'Si aplico la regla firme'),
]
build_report_1page(
    'A2 INTENSIVO 4H', 12,
    'Mod 27 Unequal Comparatives + Mod 28 Superlative - Justicia dia 2',
    a2_4h_c12_blocks, a2_4h_c12_obs,
    os.path.join(A2_DIR, 'A2_4h_Clase12_REPORTE.pdf'),
    cycle_day=2,
)
print('OK: A2 4h Cl 12 (jueves)')

# ===========================================
# A2 4h AM Cl 13 (viernes)
# ===========================================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class13_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Clase13_GUIA.pdf'),
)
a2_4h_c13_blocks = [
    ('8:00-8:05', 'VATS Justicia dia 3'),
    ('8:05-8:13', 'Analizo Revision tarea Cl 12'),
    ('8:13-8:23', 'Rompehielo How tired are you'),
    ('8:23-8:38', 'Libro Modulo 29 Degrees of Adjectives'),
    ('8:38-8:50', 'Ejercicios + Respuestas Mod 29'),
    ('8:50-9:10', 'Simulacion Interviewing My Friend (DE PIE)'),
    ('9:10-9:22', 'Shadowing Dia 3 PRESENTACION DE MEMORIA (sin video)'),
    ('9:22-9:32', 'Historia Interactiva absurda - La mujer ocupada Maria'),
    ('9:32-9:42', 'Competencia equipos Mod 29'),
    ('9:42-9:52', 'GoldList 20 frases'),
    ('9:52-9:57', 'Autochequeo'),
    ('9:57-10:00', 'Transicion'),
    ('10:00-10:20', 'BREAK'),
    ('10:20-10:25', 'Reconnect virtud + Re-anclaje'),
    ('10:25-10:35', 'Intro Required Levels'),
    ('10:35-10:50', 'Libro Modulo 30 Required Levels'),
    ('10:50-11:00', 'Ejercicios + Respuestas Mod 30'),
    ('11:00-11:20', 'Simulacion Mi vida demasiado o lo justo (DE PIE)'),
    ('11:20-11:30', 'Historia Interactiva absurda - El millonario infeliz Diego'),
    ('11:30-11:40', 'Competencia equipos Mod 30'),
    ('11:40-11:48', 'Free Production conversacion mixta M29+M30'),
    ('11:48-11:55', 'Autochequeo + Error Paper'),
    ('11:55-12:00', 'Tarea + Cierre'),
]
a2_4h_c13_obs = [
    ('M29 Degrees - dominaron pretty/quite/very/extremely?',
     'Errores tipicos en posicion'),
    ('M30 Required Levels - dominaron too much vs too many vs enough?',
     'Errores: too much problems, too many sugar'),
    ('3 errores LITERALES con NOMBRE', 'OBLIGATORIO'),
    ('Foto/video del Shadowing Dia 3 (presentacion memoria)', 'Material redes'),
    ('Estudiantes que dijeron "es muy pesado"', 'Si aplico la regla firme'),
]
build_report_1page(
    'A2 INTENSIVO 4H', 13,
    'Mod 29 Degrees of Adjectives + Mod 30 Required Levels - Justicia dia 3 - Shadowing Dia 3',
    a2_4h_c13_blocks, a2_4h_c13_obs,
    os.path.join(A2_DIR, 'A2_4h_Clase13_REPORTE.pdf'),
    cycle_day='3-Present',
)
print('OK: A2 4h Cl 13 (viernes)')

# ===========================================
# B1 Cl 8 Grammar (jueves)
# ===========================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase8_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase8_GRAMMAR_GUIA.pdf'),
)
b1_c8_g_deliv = [
    'Hojas de autochequeo completadas',
    'Papel de errores fisico (anonimo)',
    'Tarea enviada al WhatsApp con DUE DATE',
    '17 cuadernos GoldList con 20 frases del Dia 6',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Foto del tablero del Walking Adverb Drill',
    'Lista quienes NO entregaron tarea Cl 7',
]
b1_c8_g_eval = [
    'Estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Estuve DE PIE durante ~70% del bloque',
    'Hice 4 actividades fisicas (Walk Share, Stand-Up Drill, Gallery, Walking Adverb, Error Relay)',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores literales con NOMBRE',
    'Hice VATS Justicia dia 1 (cambio de virtud)',
    'Aplique tecnica No-Listen-Repeat',
    'NO acepte la excusa "es muy pesado"',
    'Asigne tarea Cl 9 con DUE DATE explicita',
    'Envie entregables a coordinacion',
]
b1_c8_g_act = [
    ('VATS JUSTICIA dia 1 (in English)', '7 min'),
    ('Tarea Check Walk & Share (3 rondas DE PIE)', '12 min'),
    ('Stand-Up Drill Frequency Adverbs (DE PIE)', '15 min'),
    ('Gallery Walk Frequency Expressions (4 estaciones)', '15 min'),
    ('GoldList Dia 6 - 20 frases', '15 min'),
    ('Writing Sprint x 3 - My Weekly Habits', '15 min'),
    ('Walking Adverb Drill posicion correcta (DE PIE)', '12 min'),
    ('Error Paper Live Peer Relay (DE PIE)', '12 min'),
    ('Tarea + Wrap', '7 min'),
]
build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase8_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 8 de 44 | BLOQUE 1: GRAMMAR & WRITING',
    'M12 Frequency Adverbs + M13 Frequency Expressions | Justicia dia 1',
    b1_c8_g_act, b1_c8_g_deliv, b1_c8_g_eval, S,
)
print('OK: B1 Cl 8 GRAMMAR (jueves)')

# ===========================================
# B1 Cl 8 Conv (jueves)
# ===========================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase8_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase8_CONV_GUIA.pdf'),
)
b1_c8_c_deliv = [
    'Hojas de autoevaluacion completadas',
    'URL del video Shadowing Dia 2 anotada',
    'Papel de errores fisico (anonimo)',
    'Lista de errores recurrentes para PASE al profesor Bloque 1 manana',
    '17 Paginas 6 del proyecto (foto)',
    'Foto del podio English Points',
    'Libreta personal con 3 errores literales + NOMBRE',
]
b1_c8_c_eval = [
    'Estudiantes hablaron 80%+ del tiempo',
    'Mantuve ENGLISH ONLY',
    'Hice VATS Reconnect Justicia dia 1',
    'Hice Shadowing 5 pasos Dia 2 con video confirmado',
    'Anote URL del video en el reporte',
    'Asigne English Points y publique podio',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores con NOMBRE',
    'Hice la simulacion Tell me about your week',
    'Project Page 6 (My Habits Now) - todos hablaron primero, luego escribieron',
    'Hice Mini-Pitch 90 seg + Q&A en vivo (3 estudiantes)',
    'NO acepte la excusa "es muy pesado"',
    'Asigne tarea Cl 9 con DUE DATE explicita',
]
b1_c8_c_act = [
    ('VATS Reconnect Justicia dia 1', '7 min'),
    ('Icebreaker How often do you (DE PIE rotando)', '13 min'),
    ('Hot Topic What habits define our generation', '18 min'),
    ('Simulacion Tell me about your week (entrevista DE PIE)', '22 min'),
    ('Shadowing 5 pasos Dia 2 mismo video', '15 min'),
    ('Project Workshop ORAL Page 6 MY HABITS NOW', '18 min'),
    ('Mini-Pitch 90 seg + Q&A en vivo (3 estudiantes)', '10 min'),
    ('Error Paper Live + Tarea con due date + Cierre', '7 min'),
]
build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase8_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 8 de 44 | BLOQUE 2: CONVERSACIONAL',
    'Aplicacion oral M12+M13 + Project Page 6 + Shadowing Dia 2 | Justicia dia 1',
    b1_c8_c_act, b1_c8_c_deliv, b1_c8_c_eval, S,
)
print('OK: B1 Cl 8 CONV (jueves)')

# ===========================================
# B1 Cl 9 Grammar (viernes)
# ===========================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase9_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase9_GRAMMAR_GUIA.pdf'),
)
b1_c9_g_deliv = [
    'Hojas de autochequeo completadas',
    'Papel de errores fisico (anonimo)',
    'Tarea enviada al WhatsApp con DUE DATE',
    '17 cuadernos GoldList con 20 frases del Dia 7',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Foto del tablero del Walking Possessive Bee',
    'Lista quienes NO entregaron tarea Cl 8',
]
b1_c9_g_eval = [
    'Estudiantes hablaron 80%+ del tiempo',
    'Estuve DE PIE durante ~70% del bloque',
    'Hice 4 actividades fisicas (Walk Share, Stand-Up Prep, Gallery, Walking Possessive, Error Relay)',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores con NOMBRE',
    'Hice VATS Justicia dia 2',
    'Aplique tecnica No-Listen-Repeat',
    'Refoze especialmente HIS vs HER (error fosilizable)',
    'NO acepte la excusa "es muy pesado"',
    'Asigne tarea Cl 10 con DUE DATE explicita',
]
b1_c9_g_act = [
    ('VATS Justicia dia 2', '7 min'),
    ('Tarea Check Walk & Share (DE PIE)', '12 min'),
    ('Stand-Up Drill Prepositions (DE PIE)', '15 min'),
    ('Gallery Walk Possessive Adjectives (4 estaciones)', '15 min'),
    ('GoldList Dia 7 - 20 frases', '15 min'),
    ('Writing Sprint x 3 - MY PEOPLE', '15 min'),
    ('Walking Possessive Bee (DE PIE)', '12 min'),
    ('Error Paper Live Peer Relay (DE PIE)', '12 min'),
    ('Tarea + Wrap', '7 min'),
]
build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase9_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 de 44 | BLOQUE 1: GRAMMAR & WRITING',
    'M14 Prepositions + M15 Possessive Adjectives | Justicia dia 2',
    b1_c9_g_act, b1_c9_g_deliv, b1_c9_g_eval, S,
)
print('OK: B1 Cl 9 GRAMMAR (viernes)')

# ===========================================
# B1 Cl 9 Conv (viernes)
# ===========================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase9_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase9_CONV_GUIA.pdf'),
)
b1_c9_c_deliv = [
    'Hojas de autoevaluacion completadas',
    'Foto/video del Shadowing Dia 3 (presentacion memoria) - material redes',
    'Papel de errores fisico (anonimo)',
    'Lista de errores recurrentes para PASE al profesor Bloque 1 lunes',
    '17 Paginas 7 del proyecto (foto)',
    'Foto del podio English Points',
    'Libreta personal con 3 errores literales + NOMBRE',
]
b1_c9_c_eval = [
    'Estudiantes hablaron 80%+ del tiempo',
    'Mantuve ENGLISH ONLY',
    'Hice VATS Reconnect Justicia dia 2',
    'Hice Shadowing Dia 3 PRESENTACION DE MEMORIA (sin video)',
    'Grabe video del Shadowing Dia 3 para redes',
    'Asigne English Points y publique podio',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores con NOMBRE',
    'Hice la simulacion Describe 3 people you depend on',
    'Project Page 7 (MY PEOPLE) - todos hablaron primero, luego escribieron',
    'Hice Mini-Pitch 90 seg + Q&A en vivo (3 estudiantes)',
    'Refoze especialmente HIS vs HER',
    'NO acepte la excusa "es muy pesado"',
    'Asigne tarea Cl 10 con DUE DATE explicita',
]
b1_c9_c_act = [
    ('VATS Reconnect Justicia dia 2', '7 min'),
    ('Icebreaker Tell me about HIS/HER (DE PIE)', '13 min'),
    ('Hot Topic Justice in YOUR family', '18 min'),
    ('Simulacion Describe 3 people you depend on (DE PIE)', '22 min'),
    ('Shadowing Dia 3 PRESENTACION DE MEMORIA (sin video)', '15 min'),
    ('Project Workshop ORAL Page 7 MY PEOPLE', '18 min'),
    ('Mini-Pitch 90 seg + Q&A en vivo (3 estudiantes)', '10 min'),
    ('Error Paper Live + Tarea con due date + Cierre', '7 min'),
]
build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase9_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 de 44 | BLOQUE 2: CONVERSACIONAL',
    'Aplicacion oral M14+M15 + Project Page 7 MY PEOPLE + Shadowing Dia 3 memoria | Justicia dia 2',
    b1_c9_c_act, b1_c9_c_deliv, b1_c9_c_eval, S,
)
print('OK: B1 Cl 9 CONV (viernes)')

print('\n6 guias + 6 reportes generados (A2 4h + B1 Mastery jueves + viernes)')
