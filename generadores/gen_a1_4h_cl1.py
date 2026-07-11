#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guia + reporte del A1 INTENSIVO 4H Cl 1 (cohorte nuevo):
- M0 English Pronunciation (p.3-6) + M1 Juan Can Play Soccer - Structure of English (p.7-18)
- Virtud PRUDENCIA v1 dia 1. Frase del Dia. Carta a Mi Yo del Futuro. Cronograma del nivel anunciado.
- Formato HOJA DE RUTA 4 bloques (240 min). Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_4H = os.path.join(D, 'VERSION_2', 'A1_4H')
os.makedirs(A1_4H, exist_ok=True)

md_to_pdf(os.path.join(A1_4H, 'A1_4h_Class1_PRINT.md'), os.path.join(A1_4H, 'GUIAS', 'A1_4h_Class1_GUIA.pdf'))
print('OK: A1_4h_Class1_GUIA.pdf')

act = [
    ('BLOQUE 1 - Apertura y bienvenida (warm-up + rituales guionados + Frase del Dia + cronograma)', '35 min'),
    ('BLOQUE 2 - M0 pronunciacion 8 trucos + M1 estructura con CAN (historia interactiva + meta)', '90 min'),
    ('BLOQUE 3 - Drill de pie CAN + Simulacion THE SPORTS CLUB + MY WORLD pieza 1', '85 min'),
    ('BLOQUE 4 - Carta a Mi Yo del Futuro + ticket de salida + tarea + error paper', '30 min'),
]
deliv = [
    'Reporte impreso lleno y firmado',
    'CARTAS del futuro cerradas (TODAS, a coordinacion)',
    'Tickets de salida (TODOS)',
    'Papel de errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Foto del tablero - Frase del Dia + marco Sujeto/Ayudante/Verbo',
    'Foto/video historia interactiva y simulacion',
    'Lista quienes NO hicieron nada (primera clase: solo asistencia)',
]
ev = [
    'Lei la hoja de ruta COMPLETA antes de clase',
    'HABLE ingles ultra simple (A1 Cl 1) y modele con gestos',
    'ESCRIBI la Frase del Dia en tablero ANTES de clase',
    'Presente Frase del Dia con coro 2x y la inserte 3+ veces natural',
    'Al cierre 1 estudiante la dijo + 1 la uso en oracion nueva',
    'Presente los 4 rituales con guion de 2-3 lineas (frase / portafolio / ticket / error paper)',
    'Anuncie el cronograma del nivel SOLO con numeros de clase (Cl 6, 11-12, 17, 22-23), sin detalles',
    'NO comente contenido, formato ni notas de ninguna evaluacion',
    'Verifique virtud Cl 1 = PRUDENCIA v1 dia 1 (por numero de clase)',
    'Cubri M0 (8 trucos, p.4) y M1 (marco can, p.9) DESDE EL LIBRO, verbatim',
    'La historia fue narrada e interactiva: pausa + coro + estudiantes AGREGAN (sin huecos, sin texto escrito)',
    'Drill de movimiento: TODOS DE PIE, velocidad creciente, cierre en produccion libre',
    'Simulacion SPORTS CLUB: 1 guest + observers con tarea escrita + yo COACH (NUNCA jugue guest)',
    'MY WORLD pieza 1 dicha en voz alta por cada estudiante',
    'Carta del futuro: recogida CERRADA de todos, sin leerlas',
    'Ticket de salida: recogi TODOS, sin evaluar ni comentar',
    'Tarea con due date explicito (Cl 2 before 7:00 PM), 15-20 min, NO fragmentada + portafolio diario',
    'NO acepte push-back de la tarea',
    'Cero material impreso preparado: todo en tablero',
    'Anuncie Cl 2 = What can you play? (M2+M3 del libro)',
]
build_report_v2(os.path.join(A1_4H, 'REPORTES', 'A1_4h_Class1_REPORTE.pdf'),
    'A1 INTENSIVO 4H | Clase 1 | M0 PRONUNCIACION + M1 CAN - STRUCTURE | PRUDENCIA v1 | FRASE DEL DIA',
    'Primera clase del cohorte: rituales permanentes + cronograma del nivel + M0 8 trucos de pronunciacion (p.4) + M1 marco Sujeto/Ayudante/(Not)/Verbo/Complemento con CAN (p.9) + historia interactiva + simulacion THE SPORTS CLUB + Carta a Mi Yo del Futuro + MY WORLD pieza 1',
    act, deliv, ev, S)
print('OK: A1_4h_Class1_REPORTE.pdf')
print('\n2 PDFs generados en A1/4h/ para Cl 1.')
