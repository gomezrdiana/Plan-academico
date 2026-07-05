#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 19 (lunes 18/05/2026):
- M42 "Getting Crazy!" (Changes of State con el verbo "get") + Shadowing Dia 3
  (mini-competencia) + Frase del Dia + virtud FORTALEZA v1.
- Sigue a Cl 18 (M39 + M41). SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class19_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class19_GUIA.pdf'))
print('OK: A2_4h_Class19_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 18 = M39+M41)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza + M42)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 18)', '7 min'),
    ('Tarea Check Cl 18', '5 min'),
    ('LIBRO M42 - "get" + cambios de estado (concepto + vocab)', '25 min'),
    ('SPEED DRILL M42 - "get" en los 5 tiempos', '17 min'),
    ('HISTORIA INTERACTIVA M42 - "The day everything changed" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL M42 - "Job: Day One" (DE PIE)', '28 min'),
    ('SIMULACION INTEGRADA M42+M41 - "What got you here?" (DE PIE)', '28 min'),
    ('SHADOWING - DIA 3: MINI-COMPETENCIA (DE PIE)', '20 min'),
    ('Free production M42 (parejas DE PIE)', '14 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 20 (M43 + M44)', '15 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 18 M39+M41)',
    'Foto del tablero - Frase del Dia + M42 tabla 5 tiempos + vocab',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "Job: Day One"',
    'Foto/video Simulacion integrada "What Got You Here?"',
    'Foto/video Shadowing Dia 3 mini-competencia (grupo ganador)',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO)',
    'Lista quienes NO entregaron tarea Cl 18',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 18 M39+M41)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'Verifique virtud CL 19 = FORTALEZA v1 (por numero de clase)',
    'Hile FORTALEZA en VATS con "get + cambio de estado"',
    'Cubri M42 Getting Crazy DESDE EL LIBRO (pag 333-337)',
    'Ensene "get" en los 5 tiempos (pres/pas/fut/cont. pres/cont. pas)',
    'Conecte M42 con M41 (-ED/-ING con "get": got interested/interesting)',
    'Conduje Speed Drill "get" en los 5 tiempos',
    'Conduje Historia Interactiva (absurdo cotidiano, NO fantasia)',
    'Conduje Simulacion "Job: Day One" PROFESIONAL (no familiar/fantasiosa)',
    'Conduje Simulacion integrada M42+M41 "What Got You Here?"',
    'Verifique que HOY = Shadowing DIA 3 y corri la MINI-COMPETENCIA',
    'Anuncie inicio de nuevo ciclo Shadowing (Dia 1) para proxima clase',
    'Camine con papel errores ANONIMO (protocolo doble)',
    'En libreta personal anote 3 errores con NOMBRE + cita literal',
    'En Tarea explique el por que + due date explicito (martes 19/05 7PM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 20 = M43 How Do You Do? + M44 I Want You to Go',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class19_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 19 de 28 | M42 GETTING CRAZY + SHADOWING DIA 3 | FORTALEZA v1 | FRASE DEL DIA (GoldList retirado)',
    'M42 Getting Crazy! (Changes of State con "get", 5 tiempos) + Job: Day One + What Got You Here + Shadowing Dia 3 mini-competencia + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class19_REPORTE.pdf')

print('\n2 PDFs generados para lunes 18/05 A2 INTENSIVO 4h AM Cl 19:')
print('  - A2/A2_4h_Class19_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class19_REPORTE.pdf')
