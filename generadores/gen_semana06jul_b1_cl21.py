#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 21 — formato HOJA DE RUTA (2 tracks):
- CONV (primero): pitch v2 con present perfect (aplica M15 oral) + ensayo
  general del midterm + presenta portafolio diario y ticket de salida.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M15 "I Have Visited London" —
  Present Perfect Regular (p.133-135) + Progress Briefing.
PRUDENCIA v2 dia 1 (ABRE). PASE bidireccional. Reportes estaticos en V2."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(B1, exist_ok=True); os.makedirs(os.path.join(B1, 'GUIAS'), exist_ok=True); os.makedirs(os.path.join(B1, 'REPORTES'), exist_ok=True)

# ---------------- CONV ----------------
md_to_pdf(os.path.join(B1, 'B1_Clase21_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase21_CONV_GUIA.pdf'))
print('OK: B1_Clase21_CONV_GUIA.pdf')

act_c = [
    ('BLOQUE 1 — Apertura: recuperacion Cl 18/14 oral DE PIE + Frase del Dia + revision tarea + PASE de Grammar', '20 min'),
    ('BLOQUE 2 — Pitch v2: historia en pasado + 3 lineas "I have..." (meta anunciada, producto verificable)', '40 min'),
    ('BLOQUE 3 — Ensayo general midterm: 4-5 presentadores 5 min, observers con tarea, profe coach/cronometro', '35 min'),
    ('BLOQUE 4 — Cierre: presentacion portafolio+ticket (guion) + ticket de salida + tarea due Cl 22 + error paper + PASE a Grammar', '15 min'),
]
del_c = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, con nombre, sin evaluar)',
    'Fotos/videos: board (Frase + pitch map) + ensayo general',
    'PASE escrito entregado a Grammar antes del cambio de bloque',
    'PASE de Grammar (Cl 20) recibido y leido en apertura',
    'Libreta personal: 3 errores literales con NOMBRE (solo reporte)',
    'Tarea anotada por todos (due Cl 22 antes de 7:00 PM)',
]
eva_c = [
    'Lei la guia completa al menos 1 hora antes',
    'Recuperacion Cl 18/14 oral y DE PIE, sin cuaderno, errores anonimos al board',
    'Frase del Dia en board ANTES de clase + 3 inserciones + cierre de memoria',
    'Verifique virtud Cl 21 = PRUDENCIA v2 dia 1 (ABRE, por numero de clase)',
    'Anuncie meta del Bloque 2 en 1 linea en ingles ANTES de empezar',
    'Avance visible de MY STORY: pitch v2 (pasado + 3 "I have...")',
    'Ensayo: profe NUNCA presento; observers con tarea (2 fortalezas/1 mejora/1 pregunta)',
    'Presente portafolio diario + ticket de salida con las 2 lineas guionadas',
    'Ticket de salida: TODOS entregaron, NO evalue ni comente ninguno',
    'Tarea 30-45 min NO fragmentada, due date explicita, sin excusas',
    'NO mencione GoldList; NO di nombres de estudiantes en publico',
    'NO comunique nada de evaluacion/criterios del midterm (coordinacion)',
    'Anuncie Cl 22 = midterm presentations "My Story, My Goals" 5 min c/u',
]
build_report_v2(
    os.path.join(B1, 'REPORTES', 'B1_Clase21_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 21 de 44 | CONV (va PRIMERO) | HOJA DE RUTA | PRUDENCIA v2 dia 1',
    'Pitch v2 con "I have..." (aplica M15 oral; Grammar formaliza) + ensayo general midterm + estreno portafolio diario y ticket de salida + PASE bidireccional. Midterm Cl 22 anunciado desde Cl 1. Profe no comunica evaluaciones.',
    act_c, del_c, eva_c, S)
print('OK: B1_Clase21_CONV_REPORTE.pdf')

# ---------------- GRAMMAR ----------------
md_to_pdf(os.path.join(GV, 'B1_Clase21_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase21_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase21_GRAMMAR_GUIA.pdf')

act_g = [
    ('BLOQUE 1 — Apertura DE PIE: recuperacion Cl 18/14 + Frase del Dia + tarea + PASE de Conv (hoy)', '20 min'),
    ('BLOQUE 2 — M15 Present Perfect Regular en papel (p.133-135): tabla + drill circulo + zone walk — DE PIE', '40 min'),
    ('BLOQUE 3 — Progress Briefing (con observadores activos, 3 rotaciones) — DE PIE 100%', '35 min'),
    ('BLOQUE 4 — Cierre sentado: ticket de salida + tarea due Cl 22 + error paper + PASE a Conv Cl 22', '15 min'),
]
del_g = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos/videos: board M15 + zone walk + briefing',
    'PASE escrito entregado a Conv (Cl 22) antes de salir',
    'PASE de Conv (Cl 21) recibido y leido en apertura',
    'Libreta personal: 3 errores literales con NOMBRE (solo reporte)',
    'Nota del % real DE PIE del bloque (objetivo ~86%, piso 70%)',
]
eva_g = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES todo el bloque',
    'Cubri M15 DESDE EL LIBRO (p.133 modulo; Guia 1 p.134; Examples p.135) citando verbatim',
    'Explique: have/has + participio -ed; 3a persona HAS; short answers',
    'Recuperacion Cl 18/14 oral y DE PIE, errores anonimos',
    'Frase del Dia en board antes + 3 inserciones + cierre de memoria',
    'Objetivo de cada bloque dicho en 1 linea en ingles',
    'Bloques 1-3 DE PIE (~86%); movimiento SIEMPRE con contenido (cero stand up/sit down simple)',
    'Drill nunca cerro el bloque: cerro produccion libre',
    'Briefing: profe coach, NUNCA guest; observers con tarea',
    'Ticket de salida: TODOS, sin evaluar ni comentar',
    'Tarea 30-45 min NO fragmentada + audio portafolio, due Cl 22 antes 7:00 PM',
    'Virtud Cl 21 = PRUDENCIA v2 dia 1; NO GoldList; NO nombres en publico',
    'NO comunique nada del midterm de Cl 22 (coordinacion)',
]
build_report_v2(
    os.path.join(B1, 'REPORTES', 'B1_Clase21_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 21 de 44 | GRAMMAR (va SEGUNDO, ~86% DE PIE) | M15 PRESENT PERFECT REGULAR',
    'A2 Book M15 "I Have Visited London" (p.133-135): have/has + participio regular en papel + Progress Briefing con observadores activos + PASE bidireccional + PRUDENCIA v2 dia 1. Cl 22: Conv corre el midterm; Grammar sigue el libro (M16).',
    act_g, del_g, eva_g, S)
print('OK: B1_Clase21_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs Cl 21 generados (V2).')
