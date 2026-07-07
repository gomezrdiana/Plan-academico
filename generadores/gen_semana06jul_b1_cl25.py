#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""B1 MASTERY Cl 25 — HOJA DE RUTA (2 tracks). CIERRA PRUDENCIA v2:
- CONV (primero): What Matters Here (prioridades con actividad-sujeto) +
  Onboarding Panel. Prepara M20 oral.
- GRAMMAR (segundo, ~86% DE PIE): A2 Book M20 "Playing is Fun!" —
  Gerunds as Subjects (p.181-184). M19 NO EXISTE (el libro lo salta).
  Anuncio Cl 26 = M21 "We Shouldn't Swim After Eating" + TEMPLANZA v2."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CV = os.path.join(D, 'B1', 'B1_conversacional_V2')
GV = os.path.join(D, 'B1', 'B1_gramatica_V2')

# ---------------- CONV ----------------
md_to_pdf(os.path.join(CV, 'B1_Clase25_CONV_PRINT.md'),
          os.path.join(CV, 'B1_Clase25_CONV_GUIA.pdf'))
print('OK: B1_Clase25_CONV_GUIA.pdf')

act_c = [
    ('BLOQUE 1 — Apertura: recuperacion Cl 22/18 DE PIE + chequeo portafolio + Frase + tarea + PASE de Grammar', '20 min'),
    ('BLOQUE 2 — What Matters Here: 3 prioridades con actividad-sujeto + mini-debates + vuelta completa', '40 min'),
    ('BLOQUE 3 — Onboarding Panel (con observadores activos, 3 rotaciones) + cierre PRUDENCIA (2 respuestas)', '35 min'),
    ('BLOQUE 4 — Cierre: ticket + tarea due Cl 26 + error paper + PASE a Grammar', '15 min'),
]
del_c = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos/videos: board (molde actividad-sujeto) + panel',
    'PASE entregado a Grammar (mismo dia); PASE de Grammar recibido',
    'Libreta: 3 errores literales con NOMBRE (solo reporte)',
    'Conteo portafolio anotado',
]
eva_c = [
    'Lei la guia completa al menos 1 hora antes',
    'Recuperacion Cl 22/18 oral y DE PIE, errores anonimos',
    'Frase del Dia antes + 3 inserciones + cierre de memoria',
    'Meta del Bloque 2 en 1 linea en ingles',
    'Prioridades REALES de trabajo/estudio (cero fantasia)',
    'Avance MY STORY: linea "what doing this course has meant"',
    'Panel: profe coach, nunca guest; observers con tarea',
    'Cerre PRUDENCIA v2 (dia 5) y anuncie TEMPLANZA v2 para Cl 26',
    'NO enseñe la regla del gerundio (Grammar formaliza M20 hoy)',
    'Ticket: TODOS, sin evaluar',
    'Tarea 30-45 min NO fragmentada + audio portafolio, due Cl 26 antes 7:00 PM',
    'Sin nombres; sin GoldList; evaluaciones = coordinacion',
]
build_report_v2(
    os.path.join(CV, 'B1_Clase25_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 25 de 44 | CONV | WHAT MATTERS HERE + ONBOARDING PANEL | PRUDENCIA v2 dia 5 (CIERRA)',
    'Prioridades y principios con la actividad como sujeto ("Arriving on time is respect") + panel de onboarding con observadores activos. Grammar formaliza M20 hoy. Cierra PRUDENCIA v2; Cl 26 abre TEMPLANZA v2. PASE bidireccional.',
    act_c, del_c, eva_c, S)
print('OK: B1_Clase25_CONV_REPORTE.pdf')

# ---------------- GRAMMAR ----------------
md_to_pdf(os.path.join(GV, 'B1_Clase25_GRAMMAR_PRINT.md'),
          os.path.join(GV, 'B1_Clase25_GRAMMAR_GUIA.pdf'))
print('OK: B1_Clase25_GRAMMAR_GUIA.pdf')

act_g = [
    ('BLOQUE 1 — Apertura DE PIE: recuperacion Cl 22/18 + chequeo portafolio + Frase + tarea + PASE de Conv', '20 min'),
    ('BLOQUE 2 — M20 gerundio como sujeto (p.181-184): regla + 12 principios del equipo en el board — DE PIE', '40 min'),
    ('BLOQUE 3 — Cadena de conversion + Advice Round (con observadores activos) + cierre PRUDENCIA — DE PIE 100%', '35 min'),
    ('BLOQUE 4 — Cierre sentado: ticket + tarea due Cl 26 + error paper + PASE a Conv Cl 26 (anuncia M21)', '15 min'),
]
del_g = [
    'Reporte firmado',
    'Error paper fisico anonimo recogido',
    'Tickets de salida recogidos (TODOS, sin evaluar)',
    'Fotos/videos: board 12 principios + advice round',
    'PASE entregado a Conv (Cl 26); PASE de Conv recibido',
    'Libreta: 3 errores literales con NOMBRE (solo reporte)',
    'Nota del % real DE PIE (~86%)',
    'Conteo portafolio anotado',
]
eva_g = [
    'Lei la guia completa al menos 1 hora antes',
    'HABLE 100% EN INGLES',
    'Cubri M20 DESDE EL LIBRO (p.181; Guia 1 p.183; Ejemplos p.184) citando verbatim',
    'Verifique con mis ojos que M19 NO existe en el A2 Book (salta M18 -> M20)',
    'Contraste gerundio vs continuo explicado ("I am working" vs "Working is hard")',
    'Recuperacion Cl 22/18 DE PIE; Frase con inserciones; objetivos en 1 linea',
    'Bloques 1-3 DE PIE (~86%); movimiento con contenido',
    'Advice round: profe coach, nunca guest; observers con tarea',
    'Cerre PRUDENCIA v2 y anuncie TEMPLANZA v2 (Cl 26)',
    'Anuncie Cl 26 = M21 "We Shouldn\'t Swim After Eating" (gerunds after prepositions)',
    'Ticket: TODOS, sin evaluar',
    'Tarea 30-45 min NO fragmentada + audio portafolio, due Cl 26 antes 7:00 PM',
]
build_report_v2(
    os.path.join(GV, 'B1_Clase25_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 25 de 44 | GRAMMAR (~86% DE PIE) | M20 GERUNDS AS SUBJECTS (M19 NO EXISTE) | PRUDENCIA v2 CIERRA',
    'A2 Book M20 "Playing is Fun!" (p.181-184): gerundio en posicion de sujeto + contraste con continuo + Advice Round con observadores activos. M19 NO existe (verificado). Anuncio Cl 26 = M21 + TEMPLANZA v2.',
    act_g, del_g, eva_g, S)
print('OK: B1_Clase25_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs Cl 25 generados (V2).')
