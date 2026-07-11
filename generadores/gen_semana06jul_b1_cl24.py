#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 24 — HOJA DE RUTA (2 tracks):
- CONV (primero): My Work, Explained (procesos reales en 6 pasos) +
  bridge formal<->casual (doble produccion oral). Prepara M18 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M18 "You Are Loved!" — Passive
  Voice Regular Participles (p.173-175): tabla + conveyor chain + zone
  walk + Company Tour.
PRUDENCIA v2 dia 4."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CV = os.path.join(D, 'VERSION_2', 'B1_4H')
GV = os.path.join(D, 'VERSION_2', 'B1_4H')

# ---------------- CONV ----------------
md_to_pdf(os.path.join(B1, 'B1_Clase24_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase24_CONV_GUIA.pdf'))
print('OK: B1_Clase24_CONV_GUIA.pdf')

act_c = [
    ('BLOQUE 1 — Apertura: recuperacion Cl 21/17 DE PIE + chequeo portafolio + Frase + tarea + PASE de Grammar', '20 min'),
    ('BLOQUE 2 — My Work, Explained: proceso real en 6 pasos, pareja re-cuenta, voluntarios al frente', '40 min'),
    ('BLOQUE 3 — Dos registros, un mensaje: formal briefing vs casual (doble produccion + contraste + mini-situaciones)', '35 min'),
    ('BLOQUE 4 — Cierre: ticket + tarea due Cl 25 + error paper + PASE a Grammar', '15 min'),
]
del_c = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos/videos: board (molde de proceso + 2 registros) + procesos al frente',
    'PASE entregado a Grammar (mismo dia); PASE de Grammar recibido',
    'Libreta: 3 errores literales con NOMBRE (solo reporte)',
    'Conteo portafolio anotado',
]
eva_c = [
    'Lei la guia completa al menos 1 hora antes',
    'Recuperacion Cl 21/17 oral y DE PIE, errores anonimos',
    'Frase del Dia antes + 3 inserciones + cierre',
    'Meta del Bloque 2 en 1 linea en ingles',
    'Procesos REALES y cotidianos (cero fantasia)',
    'Avance MY STORY: linea de proceso "how I do what I do"',
    'Bloque 3: AMBOS registros producidos oralmente + contraste explicito + mini-situaciones',
    'NO enseñe la tabla de pasiva (Grammar la formaliza hoy)',
    'Ticket: TODOS, sin evaluar',
    'Tarea 30-45 min NO fragmentada + audio casual (portafolio), due Cl 25 antes 7:00 PM',
    'Virtud PRUDENCIA v2 dia 4; sin nombres; sin GoldList',
    'Anuncie Cl 25 (actividades como sujeto)',
]
build_report_v2(
    os.path.join(B1, 'REPORTES', 'B1_Clase24_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 24 de 44 | CONV | MY WORK EXPLAINED + BRIDGE FORMAL/CASUAL | PRUDENCIA v2 dia 4',
    'Procesos reales en 6 pasos ("the order is received...") + doble produccion formal<->casual con contraste. Grammar formaliza M18 hoy mismo. PASE bidireccional.',
    act_c, del_c, eva_c, S)
print('OK: B1_Clase24_CONV_REPORTE.pdf')

# ---------------- GRAMMAR ----------------
md_to_pdf(os.path.join(B1, 'B1_Clase24_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase24_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase24_GRAMMAR_GUIA.pdf')

act_g = [
    ('BLOQUE 1 — Apertura DE PIE: recuperacion Cl 21/17 + chequeo portafolio + Frase + tarea + PASE de Conv', '20 min'),
    ('BLOQUE 2 — M18 voz pasiva en papel (p.173-175): tabla + conveyor chain + zone walk — DE PIE', '40 min'),
    ('BLOQUE 3 — The Company Tour (guest guia la sala, 3 rotaciones) — DE PIE 100%', '35 min'),
    ('BLOQUE 4 — Cierre sentado: ticket + tarea due Cl 25 + error paper + PASE a Conv Cl 25', '15 min'),
]
del_g = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos/videos: board M18 + zone walk + tour',
    'PASE entregado a Conv (Cl 25); PASE de Conv recibido',
    'Libreta: 3 errores literales con NOMBRE (solo reporte)',
    'Nota del % real DE PIE (~86%)',
    'Conteo portafolio anotado',
]
eva_g = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES',
    'Cubri M18 DESDE EL LIBRO (p.173; Guia 1 p.174; Examples 1 p.175) citando verbatim',
    'Estructura: sujeto (paciente) + TO BE + participio + (by + agente); agente eliminable',
    'Solo participios REGULARES hoy (alcance del modulo)',
    'Recuperacion Cl 21/17 DE PIE; Frase con inserciones; objetivos en 1 linea',
    'Bloques 1-3 DE PIE (~86%); movimiento con contenido',
    'Tour: profe coach, nunca guest; observers con tarea; escenario realista',
    'Drill nunca cerro bloque: cerro uso libre',
    'Ticket: TODOS, sin evaluar',
    'Tarea 30-45 min NO fragmentada + audio tour (portafolio), due Cl 25 antes 7:00 PM',
    'Virtud PRUDENCIA v2 dia 4; anuncie Cl 25 = M20 (M19 NO existe — verificado)',
]
build_report_v2(
    os.path.join(B1, 'REPORTES', 'B1_Clase24_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 24 de 44 | GRAMMAR (~86% DE PIE) | M18 PASSIVE VOICE (M19 NO EXISTE)',
    'A2 Book M18 "You Are Loved!" (p.173-175): to be + participio regular, agente con by o eliminado + Company Tour con observadores activos. Anuncio Cl 25 = M20 "Playing is Fun!" (el libro salta M19). PRUDENCIA v2 dia 4.',
    act_g, del_g, eva_g, S)
print('OK: B1_Clase24_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs Cl 24 generados (V2).')
