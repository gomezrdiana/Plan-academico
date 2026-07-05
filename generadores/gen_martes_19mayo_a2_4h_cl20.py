#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 20 (martes 19/05/2026):
- M43 "How Do You Do?" (Adverbs of Manner) + M44 "I Want You to Go" (The
  Active Causative) + Shadowing Dia 1 (nuevo ciclo) + Frase del Dia +
  virtud FORTALEZA v1 (por numero de clase: Cl 16-20).
- Sigue a Cl 19 (M42 "get"). SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class20_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class20_GUIA.pdf'))
print('OK: A2_4h_Class20_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 19 = M42 "get")', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza + M43/M44)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 19)', '7 min'),
    ('Tarea Check Cl 19', '5 min'),
    ('LIBRO M43 - adverbios de manera (concepto + vocab)', '22 min'),
    ('SPEED DRILL M43 - adjetivo -> adverbio + ubicacion', '15 min'),
    ('LIBRO M44 - el causativo activo "I want you to..."', '20 min'),
    ('HISTORIA INTERACTIVA M43+M44 - "The strange office day" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL - "Performance Review" (DE PIE)', '25 min'),
    ('SIMULACION INTEGRADA M43+M44 - "Who does what, and how?" (DE PIE)', '23 min'),
    ('SHADOWING - DIA 1: NUEVO CICLO (escuchar + repetir) (DE PIE)', '18 min'),
    ('Free production M43+M44 (parejas DE PIE)', '14 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 21 (miercoles)', '10 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 19 M42 "get")',
    'Foto del tablero - Frase del Dia + M43 adverbios + M44 patron causativo',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "Performance Review"',
    'Foto/video Simulacion integrada "Who Does What, And How?"',
    'Foto/video Shadowing Dia 1 nuevo ciclo',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO)',
    'Lista quienes NO entregaron tarea Cl 19',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 19 M42 "get")',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'Verifique virtud CL 20 = FORTALEZA v1 (por numero de clase, Cl 16-20)',
    'Hile FORTALEZA en VATS con adverbio de manera + causativo',
    'Cubri M43 How Do You Do DESDE EL LIBRO (pag 340-346)',
    'Ensene adjetivo + -ly + irregulares (good->well, fast, hard)',
    'Ensene ubicacion del adverbio + manera vs frecuencia',
    'Cubri M44 I Want You to Go DESDE EL LIBRO (pag 347-351)',
    'Contraste "I want to go" vs "I want YOU to go" (cambio de sujeto)',
    'Marque el error de calco "I want that you go" como INCORRECTO',
    'Conecte M43 con M44 ("I want you to do it carefully")',
    'Conduje Speed Drill adjetivo->adverbio + ubicacion',
    'Conduje Historia Interactiva (oficina absurda cotidiana, NO fantasia)',
    'Conduje Simulacion "Performance Review" PROFESIONAL (no familiar)',
    'Conduje Simulacion integrada M43+M44 "Who Does What, And How?"',
    'Verifique link + que HOY = Shadowing DIA 1 (nuevo ciclo, video NUEVO)',
    'Corri Shadowing Dia 1: escuchar + repetir frase por frase',
    'Camine con papel errores ANONIMO (protocolo doble)',
    'En libreta personal anote 3 errores con NOMBRE + cita literal',
    'En Tarea explique el por que + due date explicito (miercoles 20/05 7PM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 21 (miercoles) = continuacion hacia el cierre del A2 Book',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class20_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 20 de 28 | M43 HOW DO YOU DO + M44 I WANT YOU TO GO | SHADOWING DIA 1 | FORTALEZA v1 | FRASE DEL DIA (GoldList retirado)',
    'M43 How Do You Do? (Adverbs of Manner) + M44 I Want You to Go (Active Causative) + Performance Review + Who Does What And How + Shadowing Dia 1 nuevo ciclo + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class20_REPORTE.pdf')

print('\n2 PDFs generados para martes 19/05 A2 INTENSIVO 4h AM Cl 20:')
print('  - A2/A2_4h_Class20_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class20_REPORTE.pdf')
