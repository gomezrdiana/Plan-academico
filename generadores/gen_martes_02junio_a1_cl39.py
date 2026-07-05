#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 39 (martes 02/06/2026):
- Repaso visual integrado M0-M35 (TIMELINE en tablero: PASADO/PRESENTE/FUTURO/
  MODALES/OTROS) + 10 ejercicios rapidos formato examen + Mini-Simulacro 15 items
  + Ensayo Miniproyecto en pares + Frase del Dia + virtud FORTALEZA v2 (dia 4 de 5).
- A1 Book termino en M35: Cl 34-44 = consolidacion, Cl 45 = Final. NO se introduce
  modulo nuevo. Patron inspirado en Cl 41 del plan estructural, adaptado a 2h.
- Cl 38 lunes cubrio practica miniproyecto + Time Capsule + FORTALEZA dia 3.
- Profesor Christian, cohorte de 6.
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class39_PRINT.md'), os.path.join(A1_DIR, 'A1_Class39_GUIA.pdf'))
print('OK: A1_Class39_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 38 = practica miniproyecto)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza dia 4 + sostener el esfuerzo en repaso)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 38 ensayo miniproyecto)', '7 min'),
    ('REPASO VISUAL INTEGRADO - TIMELINE M0-M35 (tablero + cuaderno)', '20 min'),
    ('10 EJERCICIOS RAPIDOS formato examen + autocorreccion en pares', '15 min'),
    ('MINI-SIMULACRO 15 items mixtos formato examen (silencio total)', '20 min'),
    ('ENSAYO MINIPROYECTO en pares 3-4 min c/u + feedback (DE PIE)', '15 min'),
    ('SHADOWING del ciclo activo', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '7 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + TIMELINE M0-M35',
    'Foto/video PEER TEACHER', 'Foto/video Ensayo Miniproyecto en pares',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 38',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Hojas de los 10 ejercicios + Mini-Simulacro (insumo coord., NO comunicar notas)',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 38 miniproyecto)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'DIBUJE la TIMELINE M0-M35 en tablero ANTES de clase',
    'IMPRIMI las hojas de 10 ejercicios y Mini-Simulacro ANTES de clase (1 por estudiante)',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en oracion nueva con going to',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 39 = FORTALEZA v2 dia 4 (bloque Cl 36-40)',
    'Hile FORTALEZA dia 4 en VATS (nombrar lo dificil del repaso + going to face it)',
    'CONFIRME que A1 Book termino en M35 (Cl 34-44 consolidacion, Cl 45 Final) - sin modulo nuevo hoy',
    'Conduje REPASO VISUAL completo M0-M35: PASADO/PRESENTE/FUTURO/MODALES/OTROS',
    'Cada estudiante COPIO la TIMELINE en su cuaderno',
    'Rote estudiantes para dar 1 afirmativa + 1 negativa + 1 pregunta por bloque',
    'Conduje los 10 ejercicios formato examen con cronometro (1 min por item)',
    'Hice autocorreccion en pares + conteo publico de niveles (8+, 5-7, 0-4)',
    'Conduje Mini-Simulacro 15 items en silencio total 15 min + 4 min autocorr.',
    'Recogi hojas del simulacro (insumo coord. - NO comunique notas)',
    'Conduje Ensayo Miniproyecto en pares 3-4 min c/u con cronometro y 1 feedback especifico',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente + due date explicito (miercoles 03/06 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 40 miercoles 03/06 (ensayo miniproyecto en grupos + Time Capsule polish + FORTALEZA dia 5)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class39_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 39 de 45 | REPASO VISUAL M0-M35 + MINI-SIMULACRO + ENSAYO MINIPROYECTO | FORTALEZA v2 dia 4 | FRASE DEL DIA (Goldlist retirado)',
    'Repaso visual integrado M0-M35 (TIMELINE: PASADO/PRESENTE/FUTURO/MODALES/OTROS) + 10 ejercicios formato examen + Mini-Simulacro 15 items + Ensayo Miniproyecto 3-4 min en pares + FRASE DEL DIA (A1 Book termino en M35 - Cl 34-44 consolidacion, Cl 45 Final)',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class39_REPORTE.pdf')

print('\n2 PDFs generados para martes 02/06 A1 Nocturno Cl 39:')
print('  - A1/A1_Class39_GUIA.pdf')
print('  - A1/reportes/A1_Class39_REPORTE.pdf')
