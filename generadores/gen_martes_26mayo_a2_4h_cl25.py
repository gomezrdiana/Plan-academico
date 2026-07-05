#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 25 (martes 26/05/2026):
- ARCO DE REPASO DE ERRORES COMUNES (Cl 21-28) - Cl 25 = arco clase 4.
  EL A2 BOOK TERMINO EN M44 (pag 352): NO hay Modulo 45, NO se inventa
  contenido. Cl 22 abrio el arco (control de tiempos), Cl 23 atacó
  comparacion + gerundio/infinitivo, Cl 24 corrigió phrasal verbs +
  voz pasiva. HOY = correccion sistematica del cuarto cluster de
  mayor bloqueo hacia B1:
  PREGUNTAS/NEGATIVOS/AUXILIARES + ORDEN DE PALABRAS (WH + AUX +
  SUJETO + V base; Yes/No + AUX + V base; negativo con DOESN'T/
  DIDN'T; modal + V base SIN "to"; una sola negacion + any-; adjetivo
  ANTES del sustantivo; frecuencia ANTES del verbo principal / DESPUES
  de BE) + drills de refuerzo + simulacion que fuerza las formas
  corregidas.
- Patrones de error TIPICOS/CANONICOS cosechados de A2 Book M3/M5/
  M8/M10/M12 (preguntas con DO/DOES/DID, con BE, con modal) y guias
  B1 Cl 14-18 (orden adjetivo opinion-tamano-color-origen, frecuencia,
  doble negacion corregida con any-), sin nombres (guia reutilizable).
- Shadowing Dia 3 = MINI-COMPETENCIA = cierre del ciclo (el ciclo
  abrio Cl 23 Dia 1 con video, Cl 24 Dia 2 sin video). Cl 26 abre
  NUEVO ciclo con NUEVO video.
- Frase del Dia + virtud PRUDENCIA v2 (por numero de clase: Cl 21-25;
  Cl 25 = dia 5 v2, ULTIMO dia del bloque PRUDENCIA). Cl 26 cambia
  a TEMPLANZA v2 dia 1.
- Sigue a Cl 24 (arco clase 3, phrasal verbs + voz pasiva).
  SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class25_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class25_GUIA.pdf'))
print('OK: A2_4h_Class25_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 24 = phrasal verbs + voz pasiva)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v2 dia 5 - ultimo dia bloque + preguntas + orden)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de phrasal verbs o voz pasiva - refuerzo cluster Cl 24)', '7 min'),
    ('Tarea Check Cl 24', '5 min'),
    ('CORRECCION SISTEMATICA A - preguntas WH + Yes/No + negativos + modales + una sola negacion', '24 min'),
    ('DRILL DE REFUERZO A - preguntas y negativos (velocidad, auxiliar primero)', '15 min'),
    ('DESCANSO (fin primera mitad ~2h) / CORRECCION SISTEMATICA B - orden de palabras (adjetivo antes del sustantivo + frecuencia antes del verbo / despues de BE)', '24 min'),
    ('HISTORIA INTERACTIVA - "The day nobody knew where the new red big project was" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL - "The Job Interview" (fuerza preguntas WH + Yes/No + negativos, DE PIE)', '25 min'),
    ('SIMULACION INTEGRADA - "The Customer Inquiry" (preguntas + orden + frecuencia, DE PIE)', '22 min'),
    ('SHADOWING - DIA 3: MINI-COMPETENCIA (cierre del ciclo, DE PIE)', '18 min'),
    ('Free production - preguntas + orden (parejas DE PIE)', '14 min'),
    ('Error Paper Live EXPANDIDO (6 errores) + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 26 (cluster siguiente + cambio de virtud TEMPLANZA v2)', '10 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 24 phrasal verbs + voz pasiva)',
    'Foto del tablero - Frase del Dia + Preguntas/Negativos + Orden de palabras',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "The Job Interview"',
    'Foto/video Simulacion integrada "The Customer Inquiry"',
    'Foto/video Shadowing Dia 3 mini-competencia (cierre del ciclo)',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO) - ENTREGADO FISICAMENTE con la guia (no fotografiado)',
    'Lista quienes NO entregaron tarea Cl 24',
    'Libreta personal con 3 errores literales + NOMBRE (privado coordinacion)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'Entendi que el ARCO DE REPASO esta en marcha (Cl 25 = arco clase 4)',
    'Entendi que el A2 Book termino en M44, NO hay modulo nuevo',
    'NO invente contenido del libro ni resultados; patrones TIPICOS sin nombres',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 24 phrasal verbs + voz pasiva)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'Verifique virtud CL 25 = PRUDENCIA v2 dia 5 (ULTIMO dia del bloque PRUDENCIA, Cl 21-25)',
    'Hile PRUDENCIA en VATS = "plan the question; auxiliary first; verb in base; adjective before noun"',
    'CORRECCION A1: WH-Q = WH + AUX + SUJETO + V base ("Where DID you GO?")',
    'CORRECCION A2: Yes/No-Q = AUX + SUJETO + V base ("DO you LIKE coffee?"); modal SIN "to"',
    'CORRECCION A3: Negativo = SUJ + AUX + NOT + V base ("She DOESN\'T work"); una sola negacion con "any-"',
    'CORRECCION B1: adjetivo SIEMPRE antes del sustantivo ("a RED car", NO "a car red")',
    'CORRECCION B2: frecuencia ANTES del verbo principal / DESPUES de BE ("I ALWAYS drink", "She IS always late")',
    'Use SOLO patrones de error TIPICOS/CANONICOS, SIN nombres en la guia',
    'Conduje Drill de refuerzo A preguntas/negativos (auxiliar primero, automatico)',
    'Marque el descanso al cierre de la primera mitad (~2h)',
    'Conduje Historia Interactiva (dia de trabajo absurdo cotidiano, NO fantasia)',
    'Conduje Simulacion "The Job Interview" PROFESIONAL (fuerza preguntas + descripciones)',
    'Conduje Simulacion integrada "The Customer Inquiry" (preguntas + orden + frecuencia)',
    'Verifique link + que HOY = Shadowing DIA 3 = MINI-COMPETENCIA = cierre del ciclo',
    'Corri Shadowing Dia 3 como mini-competencia gamificada (NO evaluacion, NO notas)',
    'Anuncie que Cl 26 abre NUEVO ciclo con NUEVO video (coordinacion confirma)',
    'Error Paper EXPANDIDO (6 errores) ANONIMO + entregado FISICAMENTE con la guia',
    'En libreta personal anote 3 errores con NOMBRE + cita literal (privado coord.)',
    'En Tarea explique el por que + due date explicito (miercoles 27/05 7PM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 26 = arco clase 5 = preposiciones + articulos/cuantificadores',
    'Anuncie CAMBIO DE VIRTUD: Cl 25 cierra PRUDENCIA v2; Cl 26 abre TEMPLANZA v2 dia 1',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class25_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 25 de 28 | ARCO REPASO - Preguntas/Negativos/Auxiliares + Orden de Palabras',
    'ARCO REPASO - Preguntas/Negativos/Auxiliares + Orden de Palabras: WH + AUX + SUJETO + V base; Yes/No + AUX + V base; negativo con DOESN\'T/DIDN\'T; modal + V base SIN "to"; una sola negacion + any-; adjetivo ANTES del sustantivo (opinion-tamano-color-origen); frecuencia ANTES del verbo principal / DESPUES de BE - el A2 Book termino en M44, NO hay modulo nuevo. Correccion sistematica + drills de refuerzo + The Job Interview + The Customer Inquiry + Shadowing Dia 3 mini-competencia (cierre del ciclo) + FRASE DEL DIA. Virtud PRUDENCIA v2 dia 5 (ULTIMO dia del bloque, Cl 21-25). Cl 26 abre TEMPLANZA v2 dia 1 + NUEVO ciclo shadowing.',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class25_REPORTE.pdf')

print('\n2 PDFs generados para martes 26/05 A2 INTENSIVO 4h AM Cl 25:')
print('  - A2/A2_4h_Class25_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class25_REPORTE.pdf')
