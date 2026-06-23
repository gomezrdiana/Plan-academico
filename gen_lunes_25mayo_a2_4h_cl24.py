#!/usr/bin/env python3
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 24 (lunes 25/05/2026):
- ARCO DE REPASO DE ERRORES COMUNES (Cl 21-28) — Cl 24 = arco clase 3.
  EL A2 BOOK TERMINO EN M44 (pag 352): NO hay Modulo 45, NO se inventa
  contenido. Cl 22 abrio el arco (control de tiempos), Cl 23 atacó
  comparacion + gerundio/infinitivo. HOY = correccion sistematica del
  tercer cluster de mayor bloqueo hacia B1:
  PHRASAL VERBS + VOZ PASIVA (no separables: pronombre AL FINAL ·
  separables: pronombre EN EL MEDIO · voz pasiva: TO BE + V3 + by
  agente opcional) + drills de refuerzo + simulacion que fuerza las
  formas corregidas.
- Patrones de error TIPICOS/CANONICOS cosechados de A2 Book M23/M24
  (phrasal verbs, pag 221-235) y M18 (voz pasiva, pag 173-174), mas
  guia B1 Cl 14 Grammar (active->passive), sin nombres (guia reutilizable).
- Shadowing Dia 2 = MISMO ciclo, SIN video, de memoria (el ciclo abrio
  en Cl 23 Dia 1) + Frase del Dia + virtud PRUDENCIA v2 (por numero de
  clase: Cl 21-25; Cl 24 = dia 4 v2).
- Sigue a Cl 23 (arco clase 2, comparacion + gerundio/infinitivo).
  SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class24_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class24_GUIA.pdf'))
print('OK: A2_4h_Class24_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 23 = comparacion + gerundio/infinitivo)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v2 dia 4 + phrasal verbs + voz pasiva)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de comparacion o gerundio/infinitivo - refuerzo cluster Cl 23)', '7 min'),
    ('Tarea Check Cl 23', '5 min'),
    ('CORRECCION SISTEMATICA A - phrasal verbs (separables vs no separables)', '24 min'),
    ('DRILL DE REFUERZO A - phrasal verbs (pronombre en posicion correcta, velocidad)', '15 min'),
    ('DESCANSO (fin primera mitad ~2h) / CORRECCION SISTEMATICA B - voz pasiva (TO BE + V3 + by; cuando omitir el agente)', '24 min'),
    ('HISTORIA INTERACTIVA - "The day everything was turned off and nobody picked it up" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL - "The Help Desk Call" (fuerza phrasal verbs + voz pasiva, DE PIE)', '25 min'),
    ('SIMULACION INTEGRADA - "The Process Briefing" (phrasal + pasivo a la vez, DE PIE)', '22 min'),
    ('SHADOWING - DIA 2: MISMO CICLO, SIN VIDEO, DE MEMORIA (DE PIE)', '18 min'),
    ('Free production - phrasal verbs + voz pasiva (parejas DE PIE)', '14 min'),
    ('Error Paper Live EXPANDIDO (6 errores) + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 25 (cluster siguiente)', '10 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 23 comparacion + gerundio/infinitivo)',
    'Foto del tablero - Frase del Dia + Phrasal Verbs + Voz Pasiva',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "The Help Desk Call"',
    'Foto/video Simulacion integrada "The Process Briefing"',
    'Foto/video Shadowing Dia 2 (sin video, de memoria)',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO) - ENTREGADO FISICAMENTE con la guia (no fotografiado)',
    'Lista quienes NO entregaron tarea Cl 23',
    'Libreta personal con 3 errores literales + NOMBRE (privado coordinacion)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'Entendi que el ARCO DE REPASO esta en marcha (Cl 24 = arco clase 3)',
    'Entendi que el A2 Book termino en M44, NO hay modulo nuevo',
    'NO invente contenido del libro ni resultados; patrones TIPICOS sin nombres',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 23 comparacion + gerundio/infinitivo)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'Verifique virtud CL 24 = PRUDENCIA v2 dia 4 (por numero de clase, Cl 21-25)',
    'Hile PRUDENCIA en VATS = "plan the verb; put the pronoun in the middle; put the action on the subject"',
    'CORRECCION A1: phrasal NO SEPARABLE - pronombre AL FINAL ("look AFTER her")',
    'CORRECCION A2: phrasal SEPARABLE - pronombre EN EL MEDIO ("pick HER up", "look IT up")',
    'CORRECCION B1: voz pasiva = TO BE + V3 (NO base "is review", NO V2 "was make")',
    'CORRECCION B2: "by + agente" opcional - omitir cuando es desconocido/irrelevante',
    'Use SOLO patrones de error TIPICOS/CANONICOS, SIN nombres en la guia',
    'Conduje Drill de refuerzo A phrasal verbs (pronombre en posicion correcta, automatico)',
    'Marque el descanso al cierre de la primera mitad (~2h)',
    'Conduje Historia Interactiva (dia de trabajo absurdo cotidiano, NO fantasia)',
    'Conduje Simulacion "The Help Desk Call" PROFESIONAL (fuerza ambos bloques)',
    'Conduje Simulacion integrada "The Process Briefing" (phrasal + pasivo)',
    'Verifique link + que HOY = Shadowing DIA 2 = MISMO ciclo, SIN video (de memoria)',
    'Corri Shadowing Dia 2 SIN video, recuperacion de memoria (NO evaluacion)',
    'Error Paper EXPANDIDO (6 errores) ANONIMO + entregado FISICAMENTE con la guia',
    'En libreta personal anote 3 errores con NOMBRE + cita literal (privado coord.)',
    'En Tarea explique el por que + due date explicito (martes 26/05 7PM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 25 = arco clase 4 = preguntas/negativos/auxiliares + orden de palabras',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class24_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 24 de 28 | ARCO REPASO - Phrasal Verbs + Voz Pasiva',
    'ARCO REPASO - Phrasal Verbs + Voz Pasiva: no separables (pronombre AL FINAL) vs separables (pronombre EN EL MEDIO) + voz pasiva (TO BE + V3 + by agente opcional) - el A2 Book termino en M44, NO hay modulo nuevo. Correccion sistematica + drills de refuerzo + The Help Desk Call + The Process Briefing + Shadowing Dia 2 (sin video, de memoria) + FRASE DEL DIA. Virtud PRUDENCIA v2 dia 4 (Cl 21-25).',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class24_REPORTE.pdf')

print('\n2 PDFs generados para lunes 25/05 A2 INTENSIVO 4h AM Cl 24:')
print('  - A2/A2_4h_Class24_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class24_REPORTE.pdf')
