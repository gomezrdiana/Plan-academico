#!/usr/bin/env python3
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 22 (jueves 21/05/2026):
- ARCO DE REPASO DE ERRORES COMUNES (Cl 21-28) — Cl 22 = arco clase 1.
  EL A2 BOOK TERMINO EN M44 (pag 352): NO hay Modulo 45, NO se inventa
  contenido. Cl 21 consolido M43+M44. HOY = correccion sistematica del
  cluster de mayor bloqueo hacia B1: CONTROL DE TIEMPOS VERBALES
  (presente simple vs continuo · pasado simple vs continuo · presente
  perfecto vs pasado simple) + drills de refuerzo + simulacion que
  fuerza las formas corregidas.
- Shadowing Dia 3 = mini-competencia (cierre del ciclo; mismo video de
  Cl 20 Dia 1 / Cl 21 Dia 2) + Frase del Dia + virtud PRUDENCIA v2 (por
  numero de clase: Cl 21-25).
- Sigue a Cl 21 (consolidacion M43+M44). SIN GoldList. Patrones de error
  TIPICOS/CANONICOS, sin nombres (guia reutilizable). Reporte estatico
  (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class22_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class22_GUIA.pdf'))
print('OK: A2_4h_Class22_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 21 = adverbio M43 + causativo M44)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v2 + control de tiempos)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de tiempos verbales)', '7 min'),
    ('Tarea Check Cl 21', '5 min'),
    ('CORRECCION SISTEMATICA A - presente simple vs presente continuo', '24 min'),
    ('DRILL DE REFUERZO A - simple vs continuo (velocidad)', '15 min'),
    ('DESCANSO (fin primera mitad ~2h) / CORRECCION SISTEMATICA B+C - pasado simple vs continuo + pres. perfecto vs pasado', '24 min'),
    ('HISTORIA INTERACTIVA - "The day the timeline broke" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL - "Job Interview" (fuerza tiempos corregidos, DE PIE)', '25 min'),
    ('SIMULACION INTEGRADA - "The Daily Report" (los 3 contrastes, DE PIE)', '22 min'),
    ('SHADOWING - DIA 3: MINI-COMPETENCIA (cierre del ciclo, DE PIE)', '18 min'),
    ('Free production - tiempos (parejas DE PIE)', '14 min'),
    ('Error Paper Live EXPANDIDO (6 errores) + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 23 (cluster siguiente)', '10 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 21 M43 adverbio + M44 causativo)',
    'Foto del tablero - Frase del Dia + Tiempos A + Tiempos B/C',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "Job Interview"',
    'Foto/video Simulacion integrada "The Daily Report"',
    'Foto/video Shadowing Dia 3 (mini-competencia, cierre del ciclo)',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO) - ENTREGADO FISICAMENTE con la guia (no fotografiado)',
    'Lista quienes NO entregaron tarea Cl 21',
    'Libreta personal con 3 errores literales + NOMBRE (privado coordinacion)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'Entendi que HOY arranca el ARCO DE REPASO (Cl 22 = arco clase 1)',
    'Entendi que el A2 Book termino en M44, NO hay modulo nuevo',
    'NO invente contenido del libro ni resultados; patrones TIPICOS sin nombres',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 21 M43+M44)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'Verifique virtud CL 22 = PRUDENCIA v2 (por numero de clase, Cl 21-25)',
    'Hile PRUDENCIA en VATS = "think before you speak, choose the right tense"',
    'CORRECCION A: presente simple (rutina) vs continuo (ahora) + verbos de estado',
    'CORRECCION B: pasado simple (terminado) vs continuo (en progreso) + "did + base"',
    'CORRECCION C: presente perfecto (experiencia/since-for) vs pasado (tiempo especifico)',
    'Use SOLO patrones de error TIPICOS/CANONICOS, SIN nombres en la guia',
    'Conduje Drill de refuerzo A simple vs continuo (velocidad/automatico)',
    'Marque el descanso al cierre de la primera mitad (~2h)',
    'Conduje Historia Interactiva (dia de trabajo absurdo cotidiano, NO fantasia)',
    'Conduje Simulacion "Job Interview" PROFESIONAL (fuerza los 3 contrastes)',
    'Conduje Simulacion integrada "The Daily Report" (los 5 tiempos)',
    'Verifique link + que HOY = Shadowing DIA 3 = mini-competencia (mismo video)',
    'Corri Shadowing Dia 3 mini-competencia AMISTOSA (NO evaluacion) + cierre ciclo',
    'Error Paper EXPANDIDO (6 errores) ANONIMO + entregado FISICAMENTE con la guia',
    'En libreta personal anote 3 errores con NOMBRE + cita literal (privado coord.)',
    'En Tarea explique el por que + due date explicito (viernes 22/05 7PM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 23 = arco clase 2 = comparativos/superlativos + gerundio vs infinitivo',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class22_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 22 de 28 | ARCO DE REPASO DE ERRORES COMUNES (arco clase 1) - CONTROL DE TIEMPOS VERBALES | SHADOWING DIA 3 MINI-COMPETENCIA | PRUDENCIA v2 | FRASE DEL DIA (GoldList retirado)',
    'ARCO REPASO - Control de Tiempos Verbales: presente simple vs continuo, pasado simple vs continuo, presente perfecto vs pasado simple - el A2 Book termino en M44, NO hay modulo nuevo. Correccion sistematica + drills de refuerzo + Job Interview + The Daily Report + Shadowing Dia 3 mini-competencia + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class22_REPORTE.pdf')

print('\n2 PDFs generados para jueves 21/05 A2 INTENSIVO 4h AM Cl 22:')
print('  - A2/A2_4h_Class22_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class22_REPORTE.pdf')
