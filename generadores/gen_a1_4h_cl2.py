#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guia + reporte del A1 INTENSIVO 4H Cl 2:
- M2 What Can You Play? - "What" & Subject Pronouns (p.19-32) + M3 No, I can't. - Short Answer (p.33-40)
- Virtud PRUDENCIA v1 dia 2. Primer chequeo publico de portafolio. Recuperacion de Cl 1.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(A1_4H, exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class2_PRINT.md'), os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class2_GUIA.pdf'))
print('OK: A1_4h_Class2_GUIA.pdf')

act = [
    ('BLOQUE 1 - Apertura (recuperacion Cl 1 DE PIE + 1er chequeo portafolio + Frase del Dia + tarea Cl 1)', '35 min'),
    ('BLOQUE 2 - M2 what + pronombres sujetos y M3 respuesta corta (historia interactiva + meta)', '85 min'),
    ('BLOQUE 3 - Drill de pie pronombres/respuesta corta + Simulacion TEAM TRYOUT + MY WORLD pieza 2', '90 min'),
    ('BLOQUE 4 - Ticket de salida + tarea + error paper + anuncio Cl 3', '30 min'),
]
deliv = [
    'Reporte impreso lleno y firmado',
    'Tickets de salida (TODOS)',
    'Papel de errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Tareas Cl 1 recogidas + lista quienes NO entregaron',
    'Registro chequeo portafolio (quien hizo el audio/video diario)',
    'Foto del tablero - Frase del Dia + pronombres + respuesta corta',
    'Foto/video simulacion TEAM TRYOUT',
]
ev = [
    'Lei la hoja de ruta COMPLETA antes de clase',
    'Recuperacion de Cl 1: oral, DE PIE, en cadena, sin cuaderno, con instruccion exacta',
    'Errores oidos fueron al tablero ANONIMOS + 1 min de re-produccion',
    'Hice el PRIMER chequeo publico de portafolio y ANOTE (sin revisar contenido)',
    'ESCRIBI la Frase del Dia ANTES + coro 2x + la inserte 3+ veces natural',
    'Al cierre 1 estudiante la dijo + 1 la uso en oracion nueva',
    'Recogi la tarea Cl 1 y anote quien NO entrego (push-back NO aceptado)',
    'Verifique virtud Cl 2 = PRUDENCIA v1 dia 2',
    'Cubri M2 (what + pronombres, p.21) y M3 (respuesta corta, p.34) DESDE EL LIBRO, verbatim',
    'Ensene: a pregunta con WHAT no se responde yes/no',
    'La historia fue narrada e interactiva (pausa + coro + agregar), sin huecos',
    'Drill de movimiento: TODOS DE PIE, velocidad creciente, cierre en produccion libre',
    'Simulacion TEAM TRYOUT: 1 guest + observers con tarea + yo COACH (NUNCA jugue guest)',
    'MY WORLD pieza 2 (my people) dicha por cada estudiante',
    'Ticket de salida: recogi TODOS, sin evaluar ni comentar',
    'Tarea con due date explicito (Cl 3 before 7:00 PM), 15-20 min, NO fragmentada + portafolio diario',
    'Cero material impreso preparado: todo en tablero',
    'NO comente nada de evaluaciones (cronograma ya anunciado en Cl 1)',
    'Anuncie Cl 3 = recommendations and numbers (M4+M5 del libro)',
]
build_report_v2(os.path.join(A1_4H, 'REPORTES', 'A1_4h_Class2_REPORTE.pdf'),
    'A1 INTENSIVO 4H | Clase 2 | M2 WHAT + PRONOMBRES + M3 SHORT ANSWER | PRUDENCIA v1 | FRASE DEL DIA',
    'M2 palabra interrogativa what + pronombres sujetos I/you/he/she/it/we/they (p.20-21) + M3 respuesta corta Yes I can / No I can\'t (p.34) + historia interactiva con pronombres + simulacion TEAM TRYOUT + MY WORLD pieza 2 (my people)',
    act, deliv, ev, S)
print('OK: A1_4h_Class2_REPORTE.pdf')
print('\n2 PDFs generados en A1/4h/ para Cl 2.')
