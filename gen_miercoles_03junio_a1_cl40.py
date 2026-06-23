#!/usr/bin/env python3
"""Genera la guia + reporte del A1 Nocturno 2H Cl 40 (miercoles 03/06/2026):
- Consolidacion post-M35: ultimo ensayo oral final + ultimo ensayo miniproyecto
  + Quiz formato examen final (15 preguntas) + motivacion pre-final.
- Virtud: FORTALEZA v2 dia 5 ULTIMO (cierre del bloque Cl 36-40). Manana Cl 41
  abre bloque SINTESIS (4 virtudes integradas Cl 41-45 hasta examen final Cl 45).
- A1 Book termino en M35; desde Cl 34 estamos en consolidacion (no hay modulos
  nuevos en libro). Adaptado del plan estructural Cl 42 a 2h reales y cohorte de 6.
- Profesor Christian. SIN GoldList. Reporte estatico (se llena a mano).
- NO comunicar formato/peso/notas del examen final mas alla de "same format".
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class40_PRINT.md'), os.path.join(A1_DIR, 'A1_Class40_GUIA.pdf'))
print('OK: A1_Class40_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 39 = oral final 2x + 5 frases going to)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza dia 5 ULTIMO + transicion a SINTESIS)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 39)', '7 min'),
    ('ULTIMO ENSAYO ORAL FINAL - grupos de 4, 3 min/persona (DE PIE)', '30 min'),
    ('ULTIMO ENSAYO MINIPROYECTO - parejas + feedback Christian individual', '20 min'),
    ('QUIZ FORMATO EXAMEN FINAL - 15 preguntas, 30 seg c/u', '20 min'),
    ('SHADOWING (verificar dia del ciclo)', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Motivacion pre-final (anuncio SINTESIS Cl 41)', '7 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Quiz tracker',
    'Foto/video PEER TEACHER',
    'Foto/video Ultimo Ensayo Oral Final (grupos de 4)',
    'Foto/video Ultimo Ensayo Miniproyecto (parejas)',
    'Hojas del Quiz formato examen (15 preguntas) auto-corregidas',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 39',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmacion: NO comunicaste formato/peso/notas del examen final',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 39: oral final 2x + 5 frases going to)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 40 = FORTALEZA v2 dia 5 ULTIMO del bloque Cl 36-40',
    'Hile cierre FORTALEZA en VATS (finish lo empezado) + transicion a SINTESIS manana Cl 41',
    'CONFIRME que A1 Book termino en M35 - hoy es consolidacion (NO modulo nuevo del libro)',
    'Conduje ULTIMO ENSAYO ORAL FINAL en grupos de 4 (3 min/persona, cronometro visible, rubrica)',
    'Rote entre grupos anotando errores literales con NOMBRE en libreta personal',
    'Conduje ULTIMO ENSAYO MINIPROYECTO en parejas + di feedback INDIVIDUAL (1 ajuste concreto por persona)',
    'Conduje QUIZ formato examen final (15 preguntas: 5 gramatica + 3 vocab + 3 traduccion + 2 escritura + 2 comprension)',
    'Auto-correccion del quiz inmediata por parejas',
    'NO comunique peso, nota, ni promedio del quiz (solo coordinacion)',
    'NO comunique formato detallado del examen final mas alla de "same format as today\'s quiz"',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (jueves 04/06 antes 7PM)',
    'Tarea NO fragmentada (miniproyecto 1x + oral final 2x + dormir bien)',
    'NO acepte la excusa "no me da tiempo"',
    'Cerre con motivacion pre-final + anuncie Cl 41 jueves = SINTESIS dia 1 (4 virtudes integradas Cl 41-45)',
    'Anuncie cronograma: Cl 41-42 ensayo, Cl 43 miniproyectos, Cl 44 ultimo repaso, Cl 45 examen final',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class40_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 40 de 45 | CONSOLIDACION: Ultimo Ensayo Oral Final + Ultimo Ensayo Miniproyecto + Quiz Formato Examen | FORTALEZA v2 dia 5 ULTIMO | FRASE DEL DIA',
    'Consolidacion post-M35: ultimo ensayo oral final (grupos 4, 3 min/p) + ultimo ensayo miniproyecto (parejas + feedback Christian) + Quiz formato examen final (15 preguntas) + motivacion pre-final. FORTALEZA v2 dia 5 ULTIMO (cierre bloque Cl 36-40). Manana Cl 41 abre SINTESIS (4 virtudes integradas Cl 41-45 hasta examen final). NO comunicar formato/peso/notas del examen.',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class40_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 03/06 A1 Nocturno Cl 40:')
print('  - A1/A1_Class40_GUIA.pdf')
print('  - A1/reportes/A1_Class40_REPORTE.pdf')
