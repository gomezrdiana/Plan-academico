#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 23 — HOJA DE RUTA (2 tracks):
- CONV (primero): Experience Exchange + Promotion Interview (aplica el
  pivote experiencia abierta <-> detalle fechado; Grammar formaliza M17).
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M17 "You Didn't, or You
  Haven't?" — PP vs Simple Past (p.163-167): construccion desde el error
  + timeline walk + quarterly review.
PRUDENCIA v2 dia 3. Post-midterm: cero resultados (coordinacion)."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CV = os.path.join(D, 'VERSION_2', 'B1_4H')
GV = os.path.join(D, 'VERSION_2', 'B1_4H')

# ---------------- CONV ----------------
md_to_pdf(os.path.join(B1, 'B1_Clase23_CONV_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase23_CONV_GUIA.pdf'))
print('OK: B1_Clase23_CONV_GUIA.pdf')

act_c = [
    ('BLOQUE 1 — Apertura: recuperacion Cl 20/16 DE PIE + chequeo portafolio + Frase + tarea + PASE de Grammar', '20 min'),
    ('BLOQUE 2 — Experience Exchange: entrevistas "Have you ever...?" + pivote a detalle fechado + reporte en 3a persona', '40 min'),
    ('BLOQUE 3 — Promotion Interview (con observadores activos, 3 rotaciones, pivote x3 por candidato)', '35 min'),
    ('BLOQUE 4 — Cierre: ticket + tarea due Cl 24 + error paper + PASE a Grammar', '15 min'),
]
del_c = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos/videos: board (pivote) + interview',
    'PASE entregado a Grammar (mismo dia); PASE de Grammar recibido',
    'Libreta: 3 errores literales con NOMBRE (solo reporte)',
    'Conteo portafolio anotado',
]
eva_c = [
    'Lei la guia completa al menos 1 hora antes',
    'NO comunique resultados del midterm (coordinacion)',
    'Recuperacion Cl 20/16 oral y DE PIE, errores anonimos',
    'Frase del Dia antes + 3 inserciones + cierre de memoria',
    'Meta del Bloque 2 en 1 linea en ingles',
    'Avance MY STORY visible: linea "Since the midterm I have..."',
    'Pivote modelado: short answer -> detalle fechado',
    'Interview: profe coach, nunca guest; observers con tarea; escenario profesional realista',
    'Ticket de salida: TODOS, sin evaluar',
    'Tarea 30-45 min NO fragmentada + audio portafolio, due Cl 24 antes 7:00 PM',
    'Virtud PRUDENCIA v2 dia 3; sin nombres; sin GoldList',
    'Anuncie Cl 24 (procesos: "my work, explained")',
]
build_report_v2(
    os.path.join(B1, 'REPORTES', 'B1_Clase23_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 23 de 44 | CONV | EXPERIENCE EXCHANGE + PROMOTION INTERVIEW | PRUDENCIA v2 dia 3',
    'Pivote oral experiencia abierta ("I have...") <-> detalle fechado ("I ... in 2019"); Grammar formaliza M17 hoy mismo. MY STORY avanza rumbo al Final. PASE bidireccional. Cero resultados del midterm.',
    act_c, del_c, eva_c, S)
print('OK: B1_Clase23_CONV_REPORTE.pdf')

# ---------------- GRAMMAR ----------------
md_to_pdf(os.path.join(B1, 'B1_Clase23_GRAMMAR_PRINT.md'),
          os.path.join(B1, 'GUIAS', 'B1_Clase23_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase23_GRAMMAR_GUIA.pdf')

act_g = [
    ('BLOQUE 1 — Apertura DE PIE: recuperacion Cl 20/16 + chequeo portafolio + Frase + tarea + PASE de Conv', '20 min'),
    ('BLOQUE 2 — Construccion desde el error (4-6 errores REALES) + reglas M17 (p.164) + book drill p.165 — DE PIE', '40 min'),
    ('BLOQUE 3 — Timeline walk (zonas cerrado/abierto) + Quarterly Review (con observadores activos) — DE PIE 100%', '35 min'),
    ('BLOQUE 4 — Cierre sentado: ticket + tarea due Cl 24 + error paper + PASE a Conv Cl 24', '15 min'),
]
del_g = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos/videos: board errores reconstruidos + timeline walk + review',
    'PASE entregado a Conv (Cl 24); PASE de Conv recibido',
    'Libreta: 3 errores literales con NOMBRE (solo reporte)',
    'Nota del % real DE PIE (~86%)',
    'Conteo portafolio anotado',
]
eva_g = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES',
    'Cubri M17 DESDE EL LIBRO (p.163; Guia 1 p.164; Exercises p.165) citando verbatim',
    'Los 4 usos + implicacion del negativo (didn\'t = no va a pasar / haven\'t = todavia puede)',
    'Errores del Bloque 2 = REALES (cuaderno/PASE/error papers), anonimos, jamas inventados',
    'El bloque de error termino en PRODUCCION individual, no en explicacion',
    'Recuperacion Cl 20/16 DE PIE; Frase con inserciones; objetivos en 1 linea',
    'Bloques 1-3 DE PIE (~86%); movimiento con contenido',
    'Review: profe coach, nunca guest; observers con tarea',
    'Ticket: TODOS, sin evaluar',
    'Tarea 30-45 min NO fragmentada + audio, due Cl 24 antes 7:00 PM',
    'Virtud PRUDENCIA v2 dia 3; anuncie Cl 24 = M18 (voz pasiva)',
    'NO comunique resultados del midterm',
]
build_report_v2(
    os.path.join(B1, 'REPORTES', 'B1_Clase23_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 23 de 44 | GRAMMAR (~86% DE PIE) | M17 PP vs SIMPLE PAST',
    'A2 Book M17 "You Didn\'t, or You Haven\'t?" (p.163-167): construccion desde el error real + timeline walk cerrado/abierto + Quarterly Review con observadores activos. PRUDENCIA v2 dia 3. PASE bidireccional.',
    act_g, del_g, eva_g, S)
print('OK: B1_Clase23_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs Cl 23 generados (V2).')
