#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 41 (jueves 04/06/2026):
- M44 I Want You to Go! (The Active Causative) - ULTIMO MODULO DEL LIBRO A2
- CAMBIO DE BLOQUE DE VIRTUD: FORTALEZA v2 -> PRUDENCIA v3 dia 1 (Cl 41-45)
- Pasa de describir COMO se hace una accion con adverbio de manera (M43) a EXPRESAR EL DESEO de que OTRA persona haga la accion sin "that" (M44)
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA INTERNA: M44 (pag 347-352) es el ULTIMO modulo del libro A2. Cl 42-55 = 14 clases de consolidacion / repaso para llegar fuerte a B1 (analogo a A2 4h Cl 21-28, definicion formal por coordinacion).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class41_PRINT.md'), os.path.join(A2_DIR, 'A2_Class41_GUIA.pdf'))
print('OK: A2_Class41_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 40 = M43 adverbs of manner)', '5 min'),
    ('EL POR QUE DE HOY (incluye anuncio cierre libro + cambio virtud)', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (PRUDENCIA v3 dia 1 + M44) - TRANSICION visible desde FORTALEZA v2', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 40)', '7 min'),
    ('LIBRO M44 - want/need/would like + OBJ + to + verb (pag 347-352)', '15 min'),
    ('SPEED DRILL - voluntad con cambio de sujeto (15 items)', '15 min'),
    ('SIMULACION PROFESIONAL - The Project Kick-off Meeting (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + cierre del libro + anuncio Cl 42', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M44 want/need/would like + OBJ + to + verb + marca transicion FORTALEZA->PRUDENCIA v3 + marca CIERRE LIBRO A2',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Project Kick-off Meeting',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 40',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Nota como el cohorte recibio el cierre del libro A2 + apertura del bloque PRUDENCIA v3',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 40 M43)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 41 = PRUDENCIA v3 DIA 1 (clases 41-45, por numero de clase) - CAMBIO DE BLOQUE desde FORTALEZA v2',
    'MARQUE VISIBLEMENTE en tablero y en discurso la TRANSICION FORTALEZA v2 -> PRUDENCIA v3',
    'Hile PRUDENCIA en VATS con el patron M44 (querer que el otro pause / piense antes de actuar, no comando)',
    'Cubri M44 I Want You to Go DESDE EL LIBRO (pag 347-352)',
    'Ensene Sujeto + want/need/would like + OBJ + TO + verbo (sin "that")',
    'Ensene diferencia SIN cambio de sujeto (I want to go) vs CON cambio (I want YOU to go)',
    'Ensene pronombres OBJETO me/you/him/her/us/them (NUNCA sujeto tipo "wants I")',
    'Ensene formas negativa (don\'t want / doesn\'t need) e interrogativa (Do/Does + sujeto + want + OBJ + to + verbo)',
    'Ensene preguntas Wh- con cambio de sujeto (Where do you want US to go? / What do you need ME to do?)',
    'Conduje Speed Drill 15 items volicion con cambio de sujeto en coro rapido',
    'Conduje Simulacion The Project Kick-off Meeting con voliciones reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (viernes 05/06 antes 7:00 PM)',
    'NO acepte la excusa "no me da tiempo"',
    'ANUNCIE el CIERRE DEL LIBRO A2 (M44 ultimo modulo) y que Cl 42-55 = consolidacion A2 para llegar fuerte a B1 (plan exacto lo confirma coordinacion - en clase solo se dice "consolidacion A2")',
    'Anuncie Cl 42 = PRUDENCIA v3 dia 2 + primera clase de consolidacion post-libro',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class41_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 41 de 55 | M44 I WANT YOU TO GO - ACTIVE CAUSATIVE (ULTIMO MODULO A2) | PRUDENCIA v3 dia 1 (CAMBIO desde FORTALEZA v2) | FRASE DEL DIA (Goldlist retirado)',
    'M44 I Want You to Go! - The Active Causative (Sujeto + want/need/would like + OBJ pronombre objeto + TO + verbo infinitivo / SIN "that" / diferencia SIN cambio "I want to go" vs CON cambio "I want YOU to go" / negativa don\'t want / interrogativa Do you want me to / Wh- What do you need me to do) + paso de describir COMO se hace una accion con adverbio (M43) a EXPRESAR EL DESEO de que OTRA persona la haga (M44) + The Project Kick-off Meeting + FRASE DEL DIA + CAMBIO DE BLOQUE FORTALEZA v2 -> PRUDENCIA v3 dia 1 + CIERRE DEL LIBRO A2 (M44 ultimo modulo; Cl 42-55 entran en consolidacion A2 para llegar fuerte a B1, plan exacto por coordinacion)',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class41_REPORTE.pdf')

print('\n2 PDFs generados para jueves 04/06 A2 PM Cl 41:')
print('  - A2/A2_Class41_GUIA.pdf')
print('  - A2/reportes/A2_Class41_REPORTE.pdf')
