#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera las 3 guias + 3 reportes para miercoles 6 mayo NOCHE:
- A1 Christian Cl 20 - M20 Emociones + should be - Fortaleza dia 5 - Shadowing Dia 2
- A2 PM Tomas Cl 20 - M22 Gerundios con Verbos Dobles - Fortaleza dia 5 - Shadowing Dia 2
- B2 PM Amina Cl 3 - Fase 1 Cl 3 (3 datos sé + 3 a investigar) - Templanza dia 4 - Shadowing Dia 2
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf, build_report_1page
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A2_DIR = os.path.join(D, 'A2')
B2_DIR = os.path.join(D, 'B2')

# =================== A1 Cl 20 ===================
md_to_pdf(
    os.path.join(A1_DIR, 'A1_Class20_PRINT.md'),
    os.path.join(A1_DIR, 'A1_Clase20_GUIA.pdf'),
)

a1_c20_blocks = [
    ('00:00-00:05', 'VATS Fortaleza dia 5'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 19'),
    ('00:13-00:28', 'Libro M20 Emociones + should be'),
    ('00:28-00:38', 'Ejercicios + Parejas'),
    ('00:38-00:53', 'Simulacion Como te sentiste hoy (DE PIE)'),
    ('00:53-01:08', 'Shadowing 5 pasos Dia 2 mismo video'),
    ('01:08-01:23', 'Juego Emotion Charades (DE PIE)'),
    ('01:23-01:33', 'Historia Interactiva absurda - El gato Pedrito'),
    ('01:33-01:43', 'GoldList Lista 20 - 5 frases'),
    ('01:43-01:55', 'Errores + Peer Correction (focus worry/worried)'),
    ('01:55-02:00', 'Autochequeo + Tarea + Cierre'),
]

a1_c20_obs = [
    ('Emociones - dominaron worry/worried, boring/bored, was/were?',
     'Errores tipicos: I am worry, She is boring (queriendo decir bored)'),
    ('Simulacion Como te sentiste - quien destaco?',
     'Tema cotidiano emocional'),
    ('3 errores LITERALES con NOMBRE de estudiante', 'OBLIGATORIO'),
    ('URL video Shadowing Dia 2', 'https://www.youtube.com/watch?v=je5idXVBcEk'),
    ('Estudiantes que dijeron "es muy pesado"', 'Si aplico la regla firme'),
]

build_report_1page(
    'A1 NOCTURNO 2H', 20,
    'Mod 20 Emociones + should be - Fortaleza dia 5 - Shadowing Dia 2',
    a1_c20_blocks, a1_c20_obs,
    os.path.join(A1_DIR, 'A1_Clase20_REPORTE.pdf'),
    cycle_day=2,
)
print('OK: A1 Cl 20 (GUIA + REPORTE)')

# =================== A2 PM Cl 20 ===================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_Class20_PRINT.md'),
    os.path.join(A2_DIR, 'A2_Clase20_GUIA.pdf'),
)

a2_c20_blocks = [
    ('00:00-00:05', 'VATS Fortaleza dia 5'),
    ('00:05-00:13', 'Analisis Revision Tarea Cl 19'),
    ('00:13-00:28', 'Libro M22 Gerundios con Verbos Dobles'),
    ('00:28-00:38', 'Ejercicios + Parejas'),
    ('00:38-00:53', 'Simulacion Lo que amo / lo que quiero (DE PIE)'),
    ('00:53-01:08', 'Shadowing 5 pasos Dia 2 mismo video'),
    ('01:08-01:20', 'Historia Interactiva absurda - El abuelo que ama bailar'),
    ('01:20-01:32', 'MINI-PITCH 90 seg + Q&A en vivo (estudiantes excepcionales)'),
    ('01:32-01:42', 'GoldList Lista 20 - 5 frases'),
    ('01:42-01:55', 'Errores + Peer Correction (love-ing vs want-to)'),
    ('01:55-02:00', 'Autochequeo + Tarea + Cierre'),
]

a2_c20_obs = [
    ('Verbos dobles - dominaron love+ing vs want+to+verb?',
     'Errores tipicos: I want learning, I love to swim'),
    ('Mini-Pitch + Q&A - quien destaco?', 'Estudiantes excepcionales'),
    ('3 errores LITERALES con NOMBRE de estudiante', 'OBLIGATORIO'),
    ('URL video Shadowing Dia 2', 'https://www.youtube.com/watch?v=MFXOcfz177Q'),
    ('Estudiantes que dijeron "es muy pesado"', 'Si aplico la regla firme'),
]

build_report_1page(
    'A2 NOCTURNO 2H', 20,
    'Mod 22 Gerundios con Verbos Dobles - Fortaleza dia 5 - Shadowing Dia 2',
    a2_c20_blocks, a2_c20_obs,
    os.path.join(A2_DIR, 'A2_Clase20_REPORTE.pdf'),
    cycle_day=2,
)
print('OK: A2 PM Cl 20 (GUIA + REPORTE)')

# =================== B2 PM Amina Cl 3 ===================
md_to_pdf(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase3_PRINT.md'),
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase3_GUIA.pdf'),
)

deliverables = [
    'Hojas de autochequeo completadas',
    'URL del video Shadowing Dia 2 anotada',
    'Papel de errores fisico (anonimo)',
    '5 hojas con 3 datos se + 3 a investigar (foto o copia para archivo del proyecto)',
    'Cuadernos GoldList con 5 frases Lista 21',
    'Lista de quienes NO entregaron audio Cl 2',
    'Libreta personal con minimo 3 errores literales + NOMBRE',
    'Foto/video del Round Table o Mini-Pitch para redes',
    'Notas: 1 fortaleza + 1 area de mejora por estudiante',
]

selfeval = [
    'Las estudiantes hablaron 80%+ del tiempo',
    'Hable menos de 20 min en total',
    'Mantuve ENGLISH ONLY',
    'Hice VATS Templanza dia 4',
    'Conduje el bloque 3 datos se + 3 a investigar (15 min individual + 7 min pareja)',
    'Conduje el Round Table - cada estudiante presento 3+3 al grupo',
    'Hice Shadowing 5 pasos Dia 2 con video confirmado',
    'Anote URL del video en el reporte',
    'Hice Mini-Pitch 90 seg + Q&A en vivo (5 estudiantes)',
    'Ensene 10 phrases B2-tier para investigacion',
    'Camine con papel de errores anonimo (min 8 errores)',
    'En libreta personal anote 3 errores literales con NOMBRE',
    'NO acepte la excusa "es muy pesado"',
    'Asigne tarea Cl 4 con DUE DATE + tiempo estimado explicitos',
    'Envie entregables a coordinacion',
    'Envie la tarea al grupo de WhatsApp',
]

activities = [
    ('VATS Templanza dia 4 (in English)', '7 min'),
    ('Revision tarea Cl 2 - audio why my topic important', '8 min'),
    ('3 DATOS QUE SE + 3 DATOS QUE VOY A INVESTIGAR', '25 min'),
    ('Round Table - cada estudiante presenta 3+3 al grupo', '20 min'),
    ('Shadowing 5 pasos - Dia 2 mismo video', '15 min'),
    ('MINI-PITCH 90 seg + Q&A en vivo sobre tema', '18 min'),
    ('Vocabulario B2-tier para investigacion (10 phrases)', '12 min'),
    ('Error Paper Live + Tarea con due date', '8 min'),
    ('GoldList Lista 21 + Cierre', '7 min'),
]

build_report_v2(
    os.path.join(B2_DIR, 'B2_PM_Amina_Clase3_REPORTE.pdf'),
    'B2 PM AMINA | Clase 3 de 36 | 68h hasta el Final',
    'Fase 1 Dia 3 - 3 datos se + 3 a investigar + Round Table + Shadowing Dia 2 | Templanza dia 4',
    activities,
    deliverables,
    selfeval,
    S,
)
print('OK: B2 PM Amina Cl 3 (GUIA + REPORTE)')

print('\n3 guias + 3 reportes generados para miercoles 6 mayo noche.')
print('Videos:')
print('  A1 Christian: https://www.youtube.com/watch?v=je5idXVBcEk (Dia 2)')
print('  A2 PM Tomas:  https://www.youtube.com/watch?v=MFXOcfz177Q (Dia 2)')
print('  B2 Amina:     https://www.youtube.com/watch?v=sKIzIOgHfW4 (Dia 2)')
