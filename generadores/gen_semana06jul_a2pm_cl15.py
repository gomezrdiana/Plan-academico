#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 15 — HOJA DE RUTA: M17 You Didn't, or You Haven't? (Present Perfect vs Simple Past, p.163-172).
JUSTICIA v1 dia 5. Primer chequeo publico de portafolio."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(A2_2H, exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class15_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class15_GUIA.pdf'))
print('OK: A2_Class15_GUIA.pdf')

acts = [
    ('BLOQUE 1 - Apertura: recuperacion Cl 12 (while/during/again) + Cl 8 (first conditional) de pie + chequeo publico portafolio + Frase del Dia + revision tarea Cl 14', '22 min'),
    ('BLOQUE 2 - M17 Past simple vs Present perfect desde el libro (p.163-172): periodo cerrado vs abierto + 2+2 frases reales por estudiante', '43 min'),
    ('BLOQUE 3 - Drill fisico PAST SIDE / PERFECT SIDE: zonas del salon, cadenas en circulo, velocidad creciente, cierre en produccion libre', '37 min'),
    ('BLOQUE 4 - Cierre: ticket de salida + tarea + error paper + VATS + anuncio', '18 min'),
]
deliv = [
    'Reporte firmado',
    'Error paper anonimo (fisico, viaja con la guia)',
    'Libreta privada: errores literales CON nombre para coordinacion',
    'Tickets de salida de TODOS los estudiantes (recogidos, sin evaluar)',
    'Registro de portafolio: quien SI / quien NO hizo su audio diario',
    'Tareas Cl 14 recogidas (My Experience Map) + lista de quien NO entrego',
    'Fotos/videos de la clase (tablero final + drill)',
]
ev = [
    'HABLE 100% en ingles',
    'Recuperacion oral DE PIE de Cl 12 y Cl 8 (sin cuaderno)',
    'Chequeo publico de portafolio: pregunte y ANOTE (sin revisar contenido)',
    'FRASE DEL DIA en tablero ANTES + 3+ inserciones naturales',
    'Virtud Cl 15 = JUSTICIA v1 dia 5 (por numero de clase)',
    'Cubri M17 DESDE EL LIBRO (p.163-172): periodo cerrado = past / abierto = perfect + implicaciones del negativo',
    'La actividad del bloque 2 termino en PRODUCTO (parejas de frases al grupo)',
    'Drill del bloque 3 fue FISICO y DE PIE, con velocidad creciente, y CERRO en uso libre (mini timeline personal)',
    'Recogi el ticket de salida de TODOS sin evaluar ni comentar',
    'Tarea con due date explicita (Cl 16 antes de las 7:00 PM), 20-30 min, NO fragmentada',
    'CERO material impreso preparado; todo en tablero',
    'NO mencione GoldList; NO comunique nada de evaluaciones (coordinacion)',
]
build_report_v2(os.path.join(A2_2H, 'REPORTES', 'A2_Class15_REPORTE.pdf'),
    'A2 PM NOCHE | Clase 15 de 55 | M17 PAST SIMPLE vs PRESENT PERFECT | JUSTICIA v1 dia 5',
    'M17 You Didn\'t, or You Haven\'t? (pasado = punto especifico / perfecto = periodo abierto o no especificado, p.163-172) + drill fisico Past side / Perfect side + primer chequeo publico de portafolio',
    acts, deliv, ev, S)
print('OK: A2_Class15_REPORTE.pdf')
