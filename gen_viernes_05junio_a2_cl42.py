#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 42 (viernes 05/06/2026):
- ARCO DE REPASO DE ERRORES COMUNES - CLUSTER 1: CONTROL DE TIEMPOS VERBALES
  (presente simple vs continuo / pasado simple vs continuo / presente perfecto vs pasado simple)
- El A2 Book termino en M44 (pag 352); Cl 41 cerro el libro. A partir de Cl 42 = arco de repaso A2->B1.
- Replica del modelo A2 4h Cl 22 (mismo cluster), adaptado a 2h.
- FRASE DEL DIA + virtud PRUDENCIA v3 dia 2 (Cl 41-45 = PRUDENCIA v3, calendario absoluto).
- Error Paper EXPANDIDO (6 errores, 2 por cluster A/B/C).
- Tarea fin de semana 30-45 min, due lunes 08/06 antes 7:00 AM, NO fragmentada.
- Anuncio Cl 43 (lun 08/06): arco clase 2 = comparativos/superlativos + gerundio vs infinitivo + PRUDENCIA v3 dia 3.
- SIN GoldList. Sin nombres. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class42_PRINT.md'), os.path.join(A2_DIR, 'A2_Class42_GUIA.pdf'))
print('OK: A2_Class42_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 41)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v3 dia 2 + 3 tiempos)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de tiempos)', '7 min'),
    ('CORRECCION SISTEMATICA A - presente simple vs continuo', '15 min'),
    ('CORRECCION SISTEMATICA B+C - pasado simple vs continuo / pres perfecto vs pasado', '15 min'),
    ('SPEED DRILL - los 3 contrastes en velocidad', '15 min'),
    ('SIMULACION PROFESIONAL - The Daily Report at Work (DE PIE)', '20 min'),
    ('SHADOWING (verificar dia del ciclo)', '10 min'),
    ('Error Paper EXPANDIDO (6 errores) + Frase del Dia CIERRE', '8 min'),
    ('Tarea fin de semana + Cierre + anuncio Cl 43', '4 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Tiempos A + Tiempos B/C + Errores',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Daily Report at Work',
    'Foto/video Shadowing',
    'Papel errores fisico (anonimo, 6 errores EXPANDIDO) - entregado fisicamente con la guia',
    'Lista quienes NO entregaron tarea Cl 41',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 41)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 42 = PRUDENCIA v3 (dia 2, por numero de clase, Cl 41-45)',
    'Hile PRUDENCIA en VATS con los 3 tiempos (rutina / pasado / presente perfecto)',
    'ENTENDI que HOY arranca el ARCO DE REPASO (Cl 42 = arco clase 1)',
    'NO inventé contenido: el A2 Book termino en M44; hoy = CORRECCION sistematica de errores tipicos',
    'CORRECCION A: presente simple vs continuo (rutina vs ahora, verbos de estado)',
    'CORRECCION B: pasado simple vs continuo (terminado vs en progreso interrumpido)',
    'CORRECCION C: presente perfecto vs pasado simple (experiencia/since-for vs tiempo especifico)',
    'Conduje Speed Drill 15 items mezclando los 3 contrastes en coro rapido',
    'Conduje Simulacion The Daily Report at Work forzando los 5 tiempos',
    'Simulacion fue PROFESIONAL (tienda u oficina, no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'ERROR PAPER EXPANDIDO (6 errores, 2 por cluster A/B/C) - anonimo en clase / libreta con nombres',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (lunes 08/06 antes 7:00 AM)',
    'Tarea fin de semana 30-45 min, NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 43 = arco clase 2 (comparativos/superlativos + gerundio vs infinitivo + PRUDENCIA v3 dia 3)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class42_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 42 de 55 | ARCO REPASO Cl 1 - CONTROL DE TIEMPOS VERBALES | PRUDENCIA v3 dia 2 | FRASE DEL DIA (Goldlist retirado)',
    'ARCO DE REPASO A2->B1 - CLUSTER 1: CONTROL DE TIEMPOS VERBALES (presente simple vs continuo / pasado simple vs continuo / presente perfecto vs pasado simple) + Speed Drill 3 contrastes + The Daily Report at Work + Error Paper EXPANDIDO 6 errores + FRASE DEL DIA. El A2 Book termino en M44 (Cl 41 cerro); a partir de hoy = correccion sistematica de errores tipicos para llegar fuerte al B1. Replica del modelo A2 4h Cl 22 adaptado a 2h.',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class42_REPORTE.pdf')

print('\n2 PDFs generados para viernes 05/06 A2 PM Cl 42:')
print('  - A2/A2_Class42_GUIA.pdf')
print('  - A2/reportes/A2_Class42_REPORTE.pdf')
