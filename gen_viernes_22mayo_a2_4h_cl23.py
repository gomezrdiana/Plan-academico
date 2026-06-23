#!/usr/bin/env python3
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 23 (viernes 22/05/2026):
- ARCO DE REPASO DE ERRORES COMUNES (Cl 21-28) — Cl 23 = arco clase 2.
  EL A2 BOOK TERMINO EN M44 (pag 352): NO hay Modulo 45, NO se inventa
  contenido. Cl 22 abrio el arco (control de tiempos). HOY = correccion
  sistematica del segundo cluster de mayor bloqueo hacia B1:
  COMPARATIVOS/SUPERLATIVOS + GERUNDIO vs INFINITIVO (comparativo vs
  superlativo + irregulares · gerundio como sujeto / tras preposicion ·
  "el primer verbo decide" infinitivo/gerundio) + drills de refuerzo +
  simulacion que fuerza las formas corregidas.
- Patrones de error TIPICOS/CANONICOS cosechados de las guias A2
  M27/M28/M29 (comparativos/superlativos) y B1 Grammar M20/M21/M22
  (gerundios), sin nombres (guia reutilizable).
- Shadowing Dia 1 = NUEVO ciclo (escuchar + repetir frase por frase;
  el ciclo anterior cerro en Cl 22 Dia 3) + Frase del Dia + virtud
  PRUDENCIA v2 (por numero de clase: Cl 21-25; Cl 23 = dia 3 v2).
- Sigue a Cl 22 (arco clase 1, control de tiempos). SIN GoldList.
  Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class23_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class23_GUIA.pdf'))
print('OK: A2_4h_Class23_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 22 = control de tiempos verbales)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v2 dia 3 + comparacion + gerundio/infinitivo)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de tiempos - refuerzo cluster Cl 22)', '7 min'),
    ('Tarea Check Cl 22', '5 min'),
    ('CORRECCION SISTEMATICA A - comparativos y superlativos', '24 min'),
    ('DRILL DE REFUERZO A - comparativo/superlativo (velocidad)', '15 min'),
    ('DESCANSO (fin primera mitad ~2h) / CORRECCION SISTEMATICA B - gerundio vs infinitivo (sujeto / preposicion / primer verbo decide)', '24 min'),
    ('HISTORIA INTERACTIVA - "The most complicated workday I have ever had" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL - "The Reference Call" (fuerza comparativos + gerundio/infinitivo, DE PIE)', '25 min'),
    ('SIMULACION INTEGRADA - "The Project Pitch" (comparacion + gerundio/infinitivo, DE PIE)', '22 min'),
    ('SHADOWING - DIA 1: NUEVO CICLO (escuchar + repetir frase por frase, DE PIE)', '18 min'),
    ('Free production - comparacion + gerundio/infinitivo (parejas DE PIE)', '14 min'),
    ('Error Paper Live EXPANDIDO (6 errores) + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 24 (cluster siguiente)', '10 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 22 control de tiempos verbales)',
    'Foto del tablero - Frase del Dia + Comparativo/Superlativo + Gerundio/Infinitivo',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "The Reference Call"',
    'Foto/video Simulacion integrada "The Project Pitch"',
    'Foto/video Shadowing Dia 1 (nuevo ciclo, escuchar + repetir)',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO) - ENTREGADO FISICAMENTE con la guia (no fotografiado)',
    'Lista quienes NO entregaron tarea Cl 22',
    'Libreta personal con 3 errores literales + NOMBRE (privado coordinacion)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'Entendi que el ARCO DE REPASO esta en marcha (Cl 23 = arco clase 2)',
    'Entendi que el A2 Book termino en M44, NO hay modulo nuevo',
    'NO invente contenido del libro ni resultados; patrones TIPICOS sin nombres',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 22 control de tiempos)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'Verifique virtud CL 23 = PRUDENCIA v2 dia 3 (por numero de clase, Cl 21-25)',
    'Hile PRUDENCIA en VATS = "weigh the comparison; choose gerund/infinitive on purpose"',
    'CORRECCION A: comparativo (2 cosas) vs superlativo (el extremo) + irregulares + no doble + the/than',
    'CORRECCION B1: gerundio como sujeto (singular) + gerundio tras preposicion (-ing)',
    'CORRECCION B2: doble verbo - "el primer verbo decide" infinitivo/gerundio',
    'Use SOLO patrones de error TIPICOS/CANONICOS, SIN nombres en la guia',
    'Conduje Drill de refuerzo A comparativo/superlativo (velocidad/automatico)',
    'Marque el descanso al cierre de la primera mitad (~2h)',
    'Conduje Historia Interactiva (dia de trabajo absurdo cotidiano, NO fantasia)',
    'Conduje Simulacion "The Reference Call" PROFESIONAL (fuerza ambos bloques)',
    'Conduje Simulacion integrada "The Project Pitch" (comparacion + gerundio/infinitivo)',
    'Verifique link + que HOY = Shadowing DIA 1 = NUEVO ciclo (video nuevo, NO el de Cl 20-22)',
    'Corri Shadowing Dia 1 escuchar + repetir frase por frase (NO evaluacion)',
    'Error Paper EXPANDIDO (6 errores) ANONIMO + entregado FISICAMENTE con la guia',
    'En libreta personal anote 3 errores con NOMBRE + cita literal (privado coord.)',
    'En Tarea explique el por que + due date explicito (lunes 25/05 7PM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 24 = arco clase 3 = phrasal verbs + voz pasiva',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class23_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 23 de 28 | ARCO DE REPASO DE ERRORES COMUNES (arco clase 2) - COMPARATIVOS/SUPERLATIVOS + GERUNDIO vs INFINITIVO | SHADOWING DIA 1 NUEVO CICLO | PRUDENCIA v2 (dia 3) | FRASE DEL DIA (GoldList retirado)',
    'ARCO REPASO - Comparativos/Superlativos + Gerundio/Infinitivo: comparativo vs superlativo + irregulares (no "more better"/"the most tallest") + gerundio como sujeto/tras preposicion + "el primer verbo decide" (no "I enjoy to read"/"before to start") - el A2 Book termino en M44, NO hay modulo nuevo. Correccion sistematica + drills de refuerzo + The Reference Call + The Project Pitch + Shadowing Dia 1 nuevo ciclo + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class23_REPORTE.pdf')

print('\n2 PDFs generados para viernes 22/05 A2 INTENSIVO 4h AM Cl 23:')
print('  - A2/A2_4h_Class23_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class23_REPORTE.pdf')
