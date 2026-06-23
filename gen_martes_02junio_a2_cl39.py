#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 39 (martes 02/06/2026):
- M42 Getting Crazy! (Changes of State con "to get") + Frase del Dia + virtud FORTALEZA v2 (dia 4)
- Pasa de describir un estado con participle adjectives (M41) a marcar el CAMBIO de estado en cualquier tiempo con "to get" + adjetivo (M42)
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA INTERNA: tras M42 (pag 333-339) el libro continua con Module 43 (pag 340+, "How Do You Do? - Adverbs of Manner"). NO hay salto entre M42 y M43.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class39_PRINT.md'), os.path.join(A2_DIR, 'A2_Class39_GUIA.pdf'))
print('OK: A2_Class39_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 38 = M41 participle adjectives)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza + M42)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 38)', '7 min'),
    ('LIBRO M42 - to get + cambio de estado (pag 333-339)', '15 min'),
    ('SPEED DRILL - to get en 5 tiempos (gets/got/will get/is getting/was getting)', '15 min'),
    ('SIMULACION PROFESIONAL - The Shift Change Report (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio Cl 40', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M42 to get + cambio de estado en 5 tiempos',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Shift Change Report',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 38',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 38 M41)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 39 = FORTALEZA v2 (dia 4, por numero de clase)',
    'Hile FORTALEZA en VATS con el patron got (got tired pero got up again sin aplauso ni testigo)',
    'Cubri M42 Getting Crazy DESDE EL LIBRO (pag 333-339)',
    'Ensene "to get" + adjetivo = CAMBIO DE ESTADO (de "antes" a "ahora")',
    'Ensene los 5 TIEMPOS: presente gets / pasado got / futuro will get / continuo presente is getting / continuo pasado was getting',
    'Ensene que el espanol usa muchos verbos reflexivos (me enfermo / se pone brava / nos ponemos felices / me perdi) y el ingles usa UN verbo: get',
    'Ensene combinacion con participle adjectives de M41 (got bored / got interested / got worried / got confused / got surprised)',
    'Ensene diferencia got BORED (cambio en mi) vs got BORING (cambio en lo que yo causo en otros)',
    'Ensene vocabulario nuevo M42 (lose/lost, hurt, scare, marry/married, huge, far, tough, quiet, active, famous)',
    'Conduje Speed Drill 20 items to get en 5 tiempos en coro rapido',
    'Conduje Simulacion The Shift Change Report con got y is getting reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (miercoles 03/06 antes 7:00 PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 40 = siguiente modulo del libro (auditado antes; M43 continua sin salto) y ULTIMO dia de FORTALEZA v2 antes de cambiar de virtud',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class39_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 39 de 55 | M42 GETTING CRAZY - CHANGES OF STATE | FORTALEZA v2 | FRASE DEL DIA (Goldlist retirado)',
    'M42 Getting Crazy! (to get + adjetivo = CAMBIO DE ESTADO en 5 tiempos: gets / got / will get / is getting / was getting; combinacion con participle adjectives de M41 got bored / got interested / got confused; vocabulario nuevo lose/lost, hurt, scare, marry/married, huge, far, tough, quiet, active, famous) + paso de describir un estado (M41) a marcar el CAMBIO de estado en cualquier tiempo (M42) + The Shift Change Report + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class39_REPORTE.pdf')

print('\n2 PDFs generados para martes 02/06 A2 PM Cl 39:')
print('  - A2/A2_Class39_GUIA.pdf')
print('  - A2/reportes/A2_Class39_REPORTE.pdf')
