#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 40 (miercoles 03/06/2026):
- M43 How Do You Do? (Adverbs of Manner) + Frase del Dia + virtud FORTALEZA v2 (dia 5, ULTIMO)
- Pasa de marcar un CAMBIO de estado con "to get" (M42) a describir CÓMO se hace la accion con un adverbio de manera (M43)
- CIERRE bloque Fortaleza v2 (Cl 36-40); anuncio explicito Cl 41 jueves = PRUDENCIA v3 dia 1
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA INTERNA: M43 (pag 340-346) verificado verbatim; M44 (pag 347+) seria el siguiente modulo del libro.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class40_PRINT.md'), os.path.join(A2_DIR, 'A2_Class40_GUIA.pdf'))
print('OK: A2_Class40_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 39 = M42)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza dia 5 ULTIMO + transicion Prudencia + M43)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 39)', '7 min'),
    ('LIBRO M43 - adverbios de manera (pag 340-346)', '15 min'),
    ('SPEED DRILL - how + verbo + adverbio (-ly + irregulares + frecuencia)', '15 min'),
    ('SIMULACION PROFESIONAL - The Performance Review (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio Cl 41 (CAMBIO virtud PRUDENCIA v3)', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M43 how + verbo + adverbio de manera',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Performance Review',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 39',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Anuncio explicito CAMBIO de bloque Cl 41 = PRUDENCIA v3 dia 1',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 39 M42)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 40 = FORTALEZA v2 (dia 5, ULTIMO, por numero de clase)',
    'Hile FORTALEZA dia 5 en VATS con cierre de bloque (60 seg apertura) + patron how + adverbio de manera',
    'ANUNCIE explicitamente que MANANA Cl 41 abre PRUDENCIA v3 dia 1 (cambio de bloque)',
    'Cubri M43 How Do You Do DESDE EL LIBRO (pag 340-346)',
    'Ensene formacion del adverbio (adj + -ly, cambio -y a -ily) + irregulares (well, fast, hard, early/late)',
    'Ensene ubicacion del adverbio (despues del verbo o del objeto directo)',
    'Ensene pregunta con "How + do/does/did + sujeto + verbo"',
    'Ensene combinacion frecuencia (antes del verbo) + manera (despues del verbo)',
    'Conduje Speed Drill 15 items how + verbo + adverbio en coro rapido',
    'Conduje Simulacion The Performance Review con how + adverbio reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (jueves 04/06 antes 7:00 PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 41 = siguiente modulo del libro (auditado antes; M44 siguiente segun libro - nota interna) + PRUDENCIA v3 dia 1',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class40_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 40 de 55 | M43 HOW DO YOU DO - ADVERBS OF MANNER | FORTALEZA v2 DIA 5 ULTIMO | FRASE DEL DIA (Goldlist retirado)',
    'M43 How Do You Do? (adj + -ly, cambio -y a -ily, irregulares well - fast - hard - early - late - alone - together, ubicacion despues del verbo o del objeto directo, pregunta con How + auxiliar, combinacion frecuencia antes + manera despues) + paso de cambio de estado con to get (M42) a CÓMO se hace la accion (M43) + The Performance Review + cierre bloque Fortaleza + anuncio Prudencia v3 dia 1 manana Cl 41 + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class40_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 03/06 A2 PM Cl 40:')
print('  - A2/A2_Class40_GUIA.pdf')
print('  - A2/reportes/A2_Class40_REPORTE.pdf')
