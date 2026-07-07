#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 18 — HOJA DE RUTA: M21 We Shouldn't Swim After Eating (Gerunds after Prepositions, p.197-206).
FORTALEZA v1 dia 3. Anuncia Cl 19 = M22 I Love Swimming! (gerunds with double verbs)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2V2 = os.path.join(D, 'A2', 'V2')
os.makedirs(A2V2, exist_ok=True)

md_to_pdf(os.path.join(A2V2, 'A2_Class18_PRINT.md'), os.path.join(A2V2, 'A2_Class18_GUIA.pdf'))
print('OK: A2_Class18_GUIA.pdf')

acts = [
    ('BLOQUE 1 - Apertura: recuperacion Cl 15 (past vs perfect) + Cl 11 (already/still/until) de pie + chequeo portafolio + Frase del Dia + revision tarea Cl 17', '22 min'),
    ('BLOQUE 2 - M21 Gerundio despues de preposicion desde el libro (p.197-206): before/after/without/about + -ing + rutina real por estudiante', '43 min'),
    ('BLOQUE 3 - Simulacion SAFETY BRIEFING - FIRST DAY RULES: 1 empleado nuevo guest + 1 supervisor, observers con tarea, profe coach, rotacion + debrief', '37 min'),
    ('BLOQUE 4 - Cierre: ticket de salida + tarea + error paper + VATS + anuncio Cl 19', '18 min'),
]
deliv = [
    'Reporte firmado',
    'Error paper anonimo (fisico, viaja con la guia)',
    'Libreta privada: errores literales CON nombre para coordinacion',
    'Tickets de salida de TODOS los estudiantes (recogidos, sin evaluar)',
    'Registro de portafolio: quien SI / quien NO',
    'Tareas Cl 17 recogidas (My Opinion List) + lista de quien NO entrego',
    'Fotos/videos de la clase (tablero final + simulacion)',
]
ev = [
    'HABLE 100% en ingles',
    'Recuperacion oral DE PIE de Cl 15 y Cl 11 (sin cuaderno)',
    'Chequeo publico de portafolio: pregunte y ANOTE (sin revisar contenido)',
    'FRASE DEL DIA en tablero ANTES + 3+ inserciones naturales',
    'Virtud Cl 18 = FORTALEZA v1 dia 3 (por numero de clase)',
    'Cubri M21 DESDE EL LIBRO (p.197-206): preposicion + verbo-ING siempre (before/after/without/about)',
    'La actividad del bloque 2 termino en PRODUCTO (frase util con should al grupo)',
    'Simulacion PROFESIONAL (induccion de seguridad); NUNCA jugue un rol',
    'Observers con tarea concreta + debrief anonimo',
    'Recogi el ticket de salida de TODOS sin evaluar ni comentar',
    'Tarea con due date explicita (Cl 19 antes de las 7:00 PM), 20-30 min, NO fragmentada',
    'Anuncie Cl 19 = siguiente modulo del libro (verbos con doble verbo)',
    'CERO material impreso preparado; todo en tablero',
    'NO mencione GoldList; NO comunique nada de evaluaciones (coordinacion)',
]
build_report_v2(os.path.join(A2V2, 'A2_Class18_REPORTE.pdf'),
    'A2 PM NOCHE | Clase 18 de 55 | M21 GERUNDS AFTER PREPOSITIONS | FORTALEZA v1 dia 3',
    'M21 We Shouldn\'t Swim After Eating (gerundio tras preposicion: I never swim after eating / You should ask before using the car / without thinking / about playing, p.197-206) + simulacion Safety Briefing',
    acts, deliv, ev, S)
print('OK: A2_Class18_REPORTE.pdf')
