#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""A2 PM noche Cl 14 — HOJA DE RUTA: M16 I Have Gone to Paris (Present Perfect Irregular, p.147-162).
JUSTICIA v1 dia 4. Presenta portafolio diario + ticket de salida (rituales nuevos)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_2H = os.path.join(D, 'VERSION_2', 'A2_2H')
os.makedirs(A2_2H, exist_ok=True)

md_to_pdf(os.path.join(A2_2H, 'A2_Class14_PRINT.md'), os.path.join(A2_2H, 'GUIAS', 'A2_Class14_GUIA.pdf'))
print('OK: A2_Class14_GUIA.pdf')

acts = [
    ('BLOQUE 1 - Apertura: recuperacion Cl 11 (already/still/until) + Cl 7 (that), oral de pie + Frase del Dia + revision tarea Cl 13', '22 min'),
    ('BLOQUE 2 - M16 Present Perfect IRREGULAR desde el libro (p.147-162): tabla participios + formas + 3 experiencias reales por estudiante', '43 min'),
    ('BLOQUE 3 - Simulacion TRAVEL AGENCY: 1 guest + 1 agente al frente, observers con tarea, profe coach, rotacion + debrief', '37 min'),
    ('BLOQUE 4 - Cierre: presentacion portafolio diario + ticket de salida (NUEVOS, guion en hoja) + ticket + tarea + error paper + VATS + anuncio', '18 min'),
]
deliv = [
    'Reporte firmado',
    'Error paper anonimo (fisico, viaja con la guia)',
    'Libreta privada: errores literales CON nombre para coordinacion',
    'Tickets de salida de TODOS los estudiantes (recogidos, sin evaluar)',
    'Tareas Cl 13 recogidas (perfil de experiencia) + lista de quien NO entrego',
    'Fotos/videos de la clase (tablero final + simulacion)',
]
ev = [
    'HABLE 100% en ingles',
    'Recuperacion oral DE PIE de Cl 11 y Cl 7 (sin cuaderno, sin explicacion larga)',
    'FRASE DEL DIA en tablero ANTES de clase + 3+ inserciones naturales',
    'Virtud Cl 14 = JUSTICIA v1 dia 4 (por numero de clase)',
    'Cubri M16 DESDE EL LIBRO (p.147-162): been/taken/driven/woken up/eaten/gone/told/found',
    'La actividad del bloque 2 termino en PRODUCTO (experiencias contadas al grupo)',
    'Simulacion PROFESIONAL (agencia de viajes); NUNCA jugue guest ni agente',
    'Observers con tarea concreta (2 errores, 1 acierto, 1 pregunta) + debrief',
    'PRESENTE portafolio diario y ticket de salida con el guion de la hoja',
    'Recogi el ticket de salida de TODOS sin evaluar ni comentar',
    'Tarea con due date explicita (Cl 15 antes de las 7:00 PM), 20-30 min, NO fragmentada',
    'CERO material impreso preparado; todo en tablero',
    'NO mencione GoldList; NO comunique nada de evaluaciones (coordinacion)',
]
build_report_v2(os.path.join(A2_2H, 'REPORTES', 'A2_Class14_REPORTE.pdf'),
    'A2 PM NOCHE | Clase 14 de 55 | M16 PRESENT PERFECT IRREGULAR | JUSTICIA v1 dia 4',
    'M16 I Have Gone to Paris (participios irregulares been/taken/driven/woken up/eaten/gone/told/found, p.147-162) + simulacion Travel Agency + arranque de portafolio diario y ticket de salida',
    acts, deliv, ev, S)
print('OK: A2_Class14_REPORTE.pdf')
