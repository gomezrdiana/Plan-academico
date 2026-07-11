#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 17 — HOJA DE RUTA: M20 Playing is Fun! (Gerunds as Subjects, p.181-196).
FORTALEZA v1 dia 2. M19 NO existe en el libro (salto directo M18 -> M20)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(A2_2H, exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class17_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class17_GUIA.pdf'))
print('OK: A2_Class17_GUIA.pdf')

acts = [
    ('BLOQUE 1 - Apertura: recuperacion Cl 14 (present perfect irregular) + Cl 10 (past simple vs continuous) de pie + chequeo portafolio + Frase del Dia + revision tarea Cl 16', '22 min'),
    ('BLOQUE 2 - M20 Gerundio como sujeto desde el libro (p.181-196): vocab 6 descriptores + Working is important + 5 opiniones reales por estudiante', '43 min'),
    ('BLOQUE 3 - Simulacion TEAM MEETING - THE TRAINING PLAN: 1 vocero guest + 1 jefe de comite, observers con tarea, profe coach, rotacion + votacion', '37 min'),
    ('BLOQUE 4 - Cierre: ticket de salida + tarea + error paper + VATS + anuncio', '18 min'),
]
deliv = [
    'Reporte firmado',
    'Error paper anonimo (fisico, viaja con la guia)',
    'Libreta privada: errores literales CON nombre para coordinacion',
    'Tickets de salida de TODOS los estudiantes (recogidos, sin evaluar)',
    'Registro de portafolio: quien SI / quien NO',
    'Tareas Cl 16 recogidas (How My World Works) + lista de quien NO entrego',
    'Fotos/videos de la clase (tablero final + simulacion)',
]
ev = [
    'HABLE 100% en ingles',
    'Recuperacion oral DE PIE de Cl 14 y Cl 10 (sin cuaderno)',
    'Chequeo publico de portafolio: pregunte y ANOTE (sin revisar contenido)',
    'FRASE DEL DIA en tablero ANTES + 3+ inserciones naturales',
    'Virtud Cl 17 = FORTALEZA v1 dia 2 (por numero de clase)',
    'Cubri M20 DESDE EL LIBRO (p.181-196): verbo+ing como sujeto + fun/boring/important/expensive/difficult/easy',
    'NO comente en clase el salto de numeracion del libro (nota interna)',
    'La actividad del bloque 2 termino en PRODUCTO (opinion polemica + voto del grupo)',
    'Simulacion PROFESIONAL (reunion de equipo); NUNCA jugue un rol',
    'Observers con tarea concreta + debrief anonimo',
    'Recogi el ticket de salida de TODOS sin evaluar ni comentar',
    'Tarea con due date explicita (Cl 18 antes de las 7:00 PM), 20-30 min, NO fragmentada',
    'CERO material impreso preparado; todo en tablero',
    'NO mencione GoldList; NO comunique nada de evaluaciones (coordinacion)',
]
build_report_v2(os.path.join(A2_2H, 'REPORTES', 'A2_Class17_REPORTE.pdf'),
    'A2 PM NOCHE | Clase 17 de 55 | M20 GERUNDS AS SUBJECTS | FORTALEZA v1 dia 2',
    'M20 Playing is Fun! (gerundio como sujeto: Playing soccer is fun / Speaking English is easy, vocab fun-boring-important-expensive-difficult-easy, p.181-196) + simulacion Team Meeting - Training Plan',
    acts, deliv, ev, S)
print('OK: A2_Class17_REPORTE.pdf')
