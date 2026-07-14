#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 22 — HOJA DE RUTA (2 tracks):
- CONV (primero): MIDTERM PRESENTATIONS "My Story, My Goals" 5 min c/u,
  INTEGRADAS en la guia regular (orden por sorteo, observers con tarea,
  sin rubrica, sin resultados — coordinacion evalua).
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M16 "I Have Gone to Paris" —
  Present Perfect Irregular (p.147-150) + The Handover.
PRUDENCIA v2 dia 2. Chequeo publico de portafolio ARRANCA hoy."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')
os.makedirs(B1, exist_ok=True); os.makedirs(os.path.join(B1, 'CONVERSACION', 'GUIAS'), exist_ok=True); os.makedirs(os.path.join(B1, 'GRAMATICA', 'GUIAS'), exist_ok=True); os.makedirs(os.path.join(B1, 'CONVERSACION', 'REPORTES'), exist_ok=True); os.makedirs(os.path.join(B1, 'GRAMATICA', 'REPORTES'), exist_ok=True)

# ---------------- CONV ----------------
md_to_pdf(os.path.join(B1, 'CONVERSACION', 'B1_Clase22_CONV_PRINT.md'),
          os.path.join(B1, 'CONVERSACION', 'GUIAS', 'B1_Clase22_CONV_GUIA.pdf'))
print('OK: B1_Clase22_CONV_GUIA.pdf')

act_c = [
    ('BLOQUE 1 — Apertura: recuperacion Cl 19/15 DE PIE + 1er chequeo publico portafolio + Frase + sorteo del orden', '20 min'),
    ('BLOQUE 2 — MIDTERM ronda A: slots de 5 min (4 pitch + 1 pregunta observer), profe cronometro/coach', '40 min'),
    ('BLOQUE 3 — MIDTERM ronda B (todos presentan; Plan B slot 4 min si 15+) + debrief por TIPOS', '35 min'),
    ('BLOQUE 4 — Cierre: ticket de salida + tarea due Cl 23 + error paper + PASE a Grammar', '15 min'),
]
del_c = [
    'Reporte firmado (orden real + asistencia en numeros)',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos: board (reglas + orden por iniciales) + foto general de la sesion',
    'PASE escrito entregado a Grammar (gaps literales de los pitches)',
    'Conteo del 1er chequeo de portafolio (numeros; nombres solo en libreta)',
    'Libreta personal: errores literales con NOMBRE por presentador (solo coordinacion)',
]
eva_c = [
    'Lei la guia completa al menos 1 hora antes',
    'NO comunique resultados/criterios/notas — "Coordination handles evaluation"',
    'Sorteo con tiras del cuaderno de los propios estudiantes (cero material del profe)',
    'Cronometro estricto: aviso 3:00, corte 4:00; cero interrupciones',
    'Observers con tarea en TODOS los pitches (2 fortalezas-TIPOS, 1 pregunta, 1 frase)',
    'Debrief final por TIPOS, jamas personas',
    'Chequeo publico de portafolio: conteo en voz alta, sin nombres en publico',
    'Recuperacion Cl 19/15 oral y DE PIE (8 min, sin tocar contenido del midterm)',
    'Frase del Dia en board antes + inserciones + cierre',
    'Virtud Cl 22 = PRUDENCIA v2 dia 2',
    'Ticket de salida: TODOS, sin evaluar',
    'Tarea 30-45 min NO fragmentada + audio portafolio, due Cl 23 antes 7:00 PM',
    'Anuncie Cl 23 (experiencia abierta vs evento fechado)',
]
build_report_v2(
    os.path.join(B1, 'CONVERSACION', 'REPORTES', 'B1_Clase22_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 22 de 44 | CONV | MIDTERM PRESENTATIONS INTEGRADAS | PRUDENCIA v2 dia 2',
    '"My Story, My Goals" 5 min c/u, orden por sorteo, observers con tarea, profe cronometro/coach. SIN rubrica separada, SIN resultados (coordinacion evalua). 1er chequeo publico de portafolio. PASE a Grammar con gaps literales.',
    act_c, del_c, eva_c, S)
print('OK: B1_Clase22_CONV_REPORTE.pdf')

# ---------------- GRAMMAR ----------------
md_to_pdf(os.path.join(B1, 'GUIAS', 'GRAMATICA', 'B1_Clase22_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GRAMATICA', 'GUIAS', 'B1_Clase22_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase22_GRAMMAR_GUIA.pdf')

act_g = [
    ('BLOQUE 1 — Apertura DE PIE: recuperacion Cl 19/15 + chequeo portafolio + Frase + PASE de Conv (post-midterm)', '20 min'),
    ('BLOQUE 2 — M16 participios irregulares en papel (p.147-150): tabla del libro + triple-form chain + zone walk — DE PIE', '40 min'),
    ('BLOQUE 3 — The Handover (con observadores activos, 3 rotaciones + cadenas entre rondas) — DE PIE 100%', '35 min'),
    ('BLOQUE 4 — Cierre sentado: ticket + tarea due Cl 23 + error paper + PASE a Conv Cl 23', '15 min'),
]
del_g = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos/videos: board M16 (tabla p.148) + handover',
    'PASE entregado a Conv (Cl 23); PASE de Conv recibido y leido',
    'Libreta: 3 errores literales con NOMBRE (solo reporte)',
    'Nota del % real DE PIE (objetivo ~86%)',
    'Conteo portafolio anotado',
]
eva_g = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES',
    'Cubri M16 DESDE EL LIBRO (p.147; Vocabulary p.148; Guia 1 p.149) citando verbatim',
    'Tabla del libro: been/taken/driven/woken up/eaten/gone/told/found',
    'Explique: irregulares impredecibles, ~30 en uso comun, se memorizan',
    'NO comunique nada del midterm de esta mañana (coordinacion)',
    'Recuperacion Cl 19/15 DE PIE; Frase del Dia con inserciones',
    'Objetivo de cada bloque en 1 linea en ingles',
    'Bloques 1-3 DE PIE (~86%); movimiento con contenido',
    'Handover: profe coach, nunca guest; observers con tarea',
    'Ticket de salida: TODOS, sin evaluar',
    'Tarea 30-45 min NO fragmentada + audio portafolio, due Cl 23 antes 7:00 PM',
    'Virtud PRUDENCIA v2 dia 2; anuncie Cl 23 = M17 (cerrado vs abierto)',
]
build_report_v2(
    os.path.join(B1, 'GRAMATICA', 'REPORTES', 'B1_Clase22_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 22 de 44 | GRAMMAR (~86% DE PIE) | M16 PRESENT PERFECT IRREGULAR | clase regular',
    'A2 Book M16 "I Have Gone to Paris" (p.147-150): participios irregulares en papel + The Handover con observadores activos. El midterm corrio en Conv (SUPUESTO: track no especificado en Cl 1); aqui cero comentarios de resultados. PRUDENCIA v2 dia 2.',
    act_g, del_g, eva_g, S)
print('OK: B1_Clase22_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs Cl 22 generados (V2).')
