#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 16 — HOJA DE RUTA: M18 You Are Loved! (Passive Voice, participios regulares, p.173-180).
FORTALEZA v1 dia 1."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(A2_2H, exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class16_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class16_GUIA.pdf'))
print('OK: A2_Class16_GUIA.pdf')

acts = [
    ('BLOQUE 1 - Apertura: recuperacion Cl 13 (present perfect regular) + Cl 9 (second conditional) de pie + chequeo portafolio + Frase del Dia + revision tarea Cl 15', '22 min'),
    ('BLOQUE 2 - M18 Voz pasiva desde el libro (p.173-180): paciente + to be + participio (+ by agente) + 4 pasivas reales por estudiante', '43 min'),
    ('BLOQUE 3 - Simulacion NEW EMPLOYEE ORIENTATION: 1 guest + 1 supervisor, observers con tarea, profe coach, rotacion + debrief', '37 min'),
    ('BLOQUE 4 - Cierre: ticket de salida + tarea + error paper + VATS + anuncio', '18 min'),
]
deliv = [
    'Reporte firmado',
    'Error paper anonimo (fisico, viaja con la guia)',
    'Libreta privada: errores literales CON nombre para coordinacion',
    'Tickets de salida de TODOS los estudiantes (recogidos, sin evaluar)',
    'Registro de portafolio: quien SI / quien NO',
    'Tareas Cl 15 recogidas (My Week vs My Life) + lista de quien NO entrego',
    'Fotos/videos de la clase (tablero final + simulacion)',
]
ev = [
    'HABLE 100% en ingles',
    'Recuperacion oral DE PIE de Cl 13 y Cl 9 (sin cuaderno)',
    'Chequeo publico de portafolio: pregunte y ANOTE (sin revisar contenido)',
    'FRASE DEL DIA en tablero ANTES + 3+ inserciones naturales',
    'Virtud Cl 16 = FORTALEZA v1 dia 1 (abre bloque Cl 16-20)',
    'Cubri M18 DESDE EL LIBRO (p.173-180): activa vs pasiva, con by y sin agente, SOLO presente + participios regulares',
    'NO invente pasiva en pasado / irregulares / negativa-pregunta (no estan en el modulo)',
    'La actividad del bloque 2 termino en PRODUCTO (pasivas reales al grupo)',
    'Simulacion PROFESIONAL (orientacion de empleado nuevo); NUNCA jugue un rol',
    'Observers con tarea concreta + debrief anonimo',
    'Recogi el ticket de salida de TODOS sin evaluar ni comentar',
    'Tarea con due date explicita (Cl 17 antes de las 7:00 PM), 20-30 min, NO fragmentada',
    'CERO material impreso preparado; todo en tablero',
    'NO mencione GoldList; NO comunique nada de evaluaciones (coordinacion)',
]
build_report_v2(os.path.join(A2_2H, 'REPORTES', 'A2_Class16_REPORTE.pdf'),
    'A2 PM NOCHE | Clase 16 de 55 | M18 PASSIVE VOICE (REGULAR) | FORTALEZA v1 dia 1',
    'M18 You Are Loved! (voz pasiva presente con participios regulares: The lunch is prepared (by Juan) / Soccer is played in Colombia, p.173-180) + simulacion New Employee Orientation',
    acts, deliv, ev, S)
print('OK: A2_Class16_REPORTE.pdf')
