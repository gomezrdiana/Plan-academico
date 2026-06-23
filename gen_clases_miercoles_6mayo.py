#!/usr/bin/env python3
"""Genera las 3 guias + 3 reportes para miercoles 6 mayo 2026:
- A2 4h AM Cl 11 (Tomas AM) - M24 Separable Phrasal Verbs + M26 Equal Comparatives - Justicia dia 1 - Shadowing Dia 1
- B1 Mastery Cl 7 GRAMMAR - M10 Past Simple Reg + M11 Past Simple Irreg - Templanza dia 4
- B1 Mastery Cl 7 CONV - aplicacion oral M10+M11 - Templanza dia 4 - Shadowing Dia 1
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
B1_DIR = os.path.join(D, 'B1')
B1_REPORTES = os.path.join(B1_DIR, 'reportes')
os.makedirs(B1_REPORTES, exist_ok=True)

# =================== A2 4h AM Cl 11 ===================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class11_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Clase11_GUIA.pdf'),
)

a2_c11_blocks = [
    ('8:00-8:05', 'VATS Justicia dia 1'),
    ('8:05-8:13', 'Analizo Revision tarea'),
    ('8:13-8:23', 'Rompehielo I will Pick You Up'),
    ('8:23-8:38', 'Libro Modulo 24 Separable Phrasal Verbs'),
    ('8:38-8:50', 'Ejercicios + Respuestas Mod 24'),
    ('8:50-9:10', 'Simulacion Moving Day (separable phrasal verbs)'),
    ('9:10-9:22', 'Shadowing 5 pasos Dia 1 ciclo nuevo'),
    ('9:22-9:32', 'Historia Interactiva absurda - El Robot Roberto'),
    ('9:32-9:42', 'Competencia equipos Mod 24'),
    ('9:42-9:52', 'GoldList 20 frases'),
    ('9:52-9:57', 'Autochequeo'),
    ('9:57-10:00', 'Transicion'),
    ('10:00-10:20', 'BREAK'),
    ('10:20-10:25', 'Reconnect virtud + Re-anclaje'),
    ('10:25-10:35', 'Intro Equal Comparatives'),
    ('10:35-10:50', 'Libro Modulo 26 Equal Comparatives'),
    ('10:50-11:00', 'Ejercicios + Respuestas Mod 26'),
    ('11:00-11:20', 'Simulacion Comparando Mi Vida (equal comparatives)'),
    ('11:20-11:30', 'Historia Interactiva absurda - Maria y su Gato'),
    ('11:30-11:40', 'Competencia equipos Mod 26'),
    ('11:40-11:48', 'Free Production conversacion mixta M24+M26'),
    ('11:48-11:55', 'Autochequeo + Error Paper colectivo'),
    ('11:55-12:00', 'Tarea + Cierre'),
]

a2_c11_obs = [
    ('Modulo 24 - dominaron Separable Phrasal Verbs con pronombre obligatorio?',
     'Mayoria si / mayoria no. Errores tipicos: "I turn on it" en lugar de "Turn it on"'),
    ('Modulo 26 - dominaron Equal Comparatives "as ___ as ___"?',
     'Errores tipicos: "as more than" o doble adjetivo'),
    ('3 errores LITERALES con NOMBRE de estudiante',
     'OBLIGATORIO. Auditable por sistema.'),
    ('URL video Shadowing Dia 1',
     'https://www.youtube.com/watch?v=MFXOcfz177Q'),
    ('Estudiantes que dijeron "es muy pesado" sobre tarea anterior',
     'Si aplico la regla firme. Nombres si pidieron aflojar'),
]

build_report_1page(
    'A2 INTENSIVO 4H', 11,
    'Mod 24 Separable Phrasal Verbs + Mod 26 Equal Comparatives - Justicia dia 1 (M25 saltado)',
    a2_c11_blocks, a2_c11_obs,
    os.path.join(A2_DIR, 'A2_4h_Clase11_REPORTE.pdf'),
    cycle_day=1,
)

print('OK: A2 4h AM Cl 11 (GUIA + REPORTE)')

# =================== B1 GRAMMAR Cl 7 ===================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase7_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase7_GRAMMAR_GUIA.pdf'),
)

grammar_deliverables = [
    'Hojas de autochequeo completadas',
    'Papel de errores fisico (anonimo, sin nombres)',
    'Tarea enviada al grupo de WhatsApp con DUE DATE explicita',
    '17 cuadernos de GoldList con las 20 frases del Dia 5',
    'Libreta personal con minimo 3 errores literales + NOMBRE de estudiante',
    'Foto del tablero del Walking Spelling Bee (ganador)',
    'Lista de quienes NO entregaron tarea de Cl 5',
]

grammar_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Estuve DE PIE durante ~70% del bloque',
    'Hice las 4 actividades fisicas: Walk & Share, Stand-Up Drill, Gallery Walk, Walking Spelling Bee, Error Paper Relay',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En mi libreta personal anote 3 errores literales con NOMBRE',
    'Mi celular estaba boca abajo (excepto cronometro)',
    'Hice el ritual VATS (Templanza dia 4)',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'NO acepte la excusa "es muy pesado" sobre tarea estandar B1',
    'Asigne tarea Cl 8 con DUE DATE + tiempo estimado explicitos',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

grammar_activities = [
    ('VATS Templanza dia 4 (in English)', '7 min'),
    ('Tarea Check - Walk & Share (3 rondas, DE PIE)', '12 min'),
    ('Stand-Up Drill - Simple Past Regular (DE PIE)', '15 min'),
    ('Gallery Walk - 4 estaciones Irregular Verbs', '15 min'),
    ('GoldList Dia 5 - 20 frases nuevas', '15 min'),
    ('Writing Sprint x 3 rondas - My Yesterday', '15 min'),
    ('Walking Spelling Bee - Past Tenses (DE PIE)', '12 min'),
    ('Error Paper Live - Peer Relay (DE PIE)', '12 min'),
    ('Tarea + Wrap', '7 min'),
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase7_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 7 de 44 | BLOQUE 1: GRAMMAR & WRITING',
    'M10 Simple Past Regular + M11 Simple Past Irregular | Templanza dia 4',
    grammar_activities,
    grammar_deliverables,
    grammar_selfeval,
    S,
)
print('OK: B1 Mastery Cl 7 GRAMMAR (GUIA + REPORTE)')

# =================== B1 CONV Cl 7 ===================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase7_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase7_CONV_GUIA.pdf'),
)

conv_deliverables = [
    'Hojas de autoevaluacion completadas',
    'URL del video de Shadowing Dia 1 anotada',
    'Papel de errores fisico (anonimo, sin nombres)',
    'Lista de errores recurrentes para PASE al profesor de Bloque 1 manana',
    'Libreta personal con minimo 3 errores literales + NOMBRE',
    '17 Paginas 5 del proyecto (en cuaderno personal - fotografiar)',
    'Foto del podio de English Points del dia',
]

conv_selfeval = [
    'Los estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY como regla principal',
    'Hice el ritual VATS Reconnect (Templanza dia 4)',
    'Hice Shadowing 5 pasos completos con video confirmado',
    'Anote URL del video en el reporte',
    'Asigne English Points y publique podio del dia',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En mi libreta personal anote 3 errores literales con NOMBRE',
    'Aplique tecnica No-Listen-Repeat sin explicar gramatica',
    'Hice la simulacion Reportando lo que paso (entrevista periodistica)',
    'Project Page 5 (My Milestones Past) - todos hablaron primero, luego escribieron',
    'Hice el Mini-Pitch 90 seg con Q&A en vivo (3 estudiantes)',
    'NO acepte la excusa "es muy pesado" sobre tarea estandar B1',
    'Asigne tarea Cl 8 con DUE DATE + tiempo estimado explicitos',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

conv_activities = [
    ('VATS Reconnect Templanza dia 4 (in English)', '7 min'),
    ('Icebreaker - Yesterday I... (DE PIE rotando)', '13 min'),
    ('Hot Topic - The day my life changed (debate parejas)', '18 min'),
    ('Simulacion - Reportando lo que paso (entrevista periodistica DE PIE)', '22 min'),
    ('Shadowing 5 pasos - Dia 1 ciclo nuevo', '15 min'),
    ('Project Workshop ORAL - Page 5 MY MILESTONES PAST', '18 min'),
    ('Mini-Pitch 90 seg + Q&A en vivo (3 estudiantes excepcionales)', '10 min'),
    ('Error Paper Live + Tarea con due date + Cierre', '7 min'),
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase7_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 7 de 44 | BLOQUE 2: CONVERSACIONAL',
    'Aplicacion oral M10+M11 Simple Past + Project Page 5 + Shadowing Dia 1 nuevo ciclo | Templanza dia 4',
    conv_activities,
    conv_deliverables,
    conv_selfeval,
    S,
)
print('OK: B1 Mastery Cl 7 CONV (GUIA + REPORTE)')

print('\n3 guias + 3 reportes generados para miercoles 6 mayo 2026.')
print('Videos:')
print('  A2 4h AM:    https://www.youtube.com/watch?v=MFXOcfz177Q')
print('  B1 Conv:     https://www.youtube.com/watch?v=sKIzIOgHfW4')
