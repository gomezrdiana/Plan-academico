#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 26 (miercoles 27/05/2026):
- ARCO DE REPASO DE ERRORES COMUNES (Cl 21-28) - Cl 26 = arco clase 5.
  EL A2 BOOK TERMINO EN M44 (pag 352): NO hay Modulo 45, NO se inventa
  contenido. Cl 22 abrio el arco (control de tiempos), Cl 23 ataco
  comparacion + gerundio/infinitivo, Cl 24 ataco phrasal + voz pasiva,
  Cl 25 ataco preguntas/negativos/auxiliares + orden palabras.
  HOY = correccion sistematica del quinto cluster de mayor bloqueo
  hacia B1: PREPOSICIONES + ARTICULOS/CUANTIFICADORES
  (in/on/at tiempo y lugar + dependencias good AT / depend ON /
  listen TO / worried ABOUT / arrive AT-IN / live IN +
  a/an/the/sin articulo + much/many/some/any/a lot of en posicion
  correcta) + drills de refuerzo + simulacion que fuerza las formas
  corregidas.
- Patrones de error TIPICOS/CANONICOS cosechados de A2 Book M1/M6/M8
  (preposiciones), M11 (a/an), M14 (some/any), M27 (much/many/a lot of)
  y dependencias verbo/adjetivo estandar, sin nombres (guia reutilizable).
- Shadowing Dia 1 NUEVO ciclo (con video, escuchar + repetir frase por
  frase) - el ciclo anterior cerro en Cl 25 (Dia 3 mini-competencia) +
  Frase del Dia + virtud TEMPLANZA v2 dia 1 (CAMBIO HOY: Cl 21-25 fue
  PRUDENCIA v2; Cl 26-28 = TEMPLANZA v2 parcial porque el nivel termina
  en Cl 28).
- Sigue a Cl 25 (arco clase 4, preguntas/auxiliares + orden palabras).
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

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class26_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class26_GUIA.pdf'))
print('OK: A2_4h_Class26_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 25 = preguntas/negativos/auxiliares + orden palabras)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Templanza v2 dia 1 - TRANSICION desde Prudencia + preposiciones + articulos/cuantificadores)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de preguntas/negativos/auxiliares + orden palabras - refuerzo cluster Cl 25)', '7 min'),
    ('Tarea Check Cl 25', '5 min'),
    ('CORRECCION SISTEMATICA A - preposiciones (in/on/at tiempo y lugar + dependencias good AT, depend ON, listen TO, worried ABOUT, arrive AT-IN, live IN)', '24 min'),
    ('DRILL DE REFUERZO A - preposiciones (velocidad, sin pensar dos veces)', '15 min'),
    ('DESCANSO (fin primera mitad ~2h) / CORRECCION SISTEMATICA B - articulos a/an/the/sin articulo + cuantificadores much/many/some/any/a lot of', '24 min'),
    ('HISTORIA INTERACTIVA - "The Monday morning meeting that had no coffee and too many people" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL - "The Appointment Booking" (agendar citas - fuerza preposiciones de tiempo y lugar, DE PIE)', '25 min'),
    ('SIMULACION INTEGRADA - "The Office Tour & Supply Order" (describir lugar + pedir cantidades - articulos + cuantificadores + preposiciones, DE PIE)', '22 min'),
    ('SHADOWING - DIA 1 NUEVO CICLO: con video, escuchar + repetir frase por frase (DE PIE)', '18 min'),
    ('Free production - preposiciones + articulos/cuantificadores (parejas DE PIE)', '14 min'),
    ('Error Paper Live EXPANDIDO (6 errores) + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 27 (cluster siguiente)', '10 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 25 preguntas/negativos/auxiliares + orden palabras)',
    'Foto del tablero - Frase del Dia + Preposiciones + Articulos/Cuantificadores',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "The Appointment Booking"',
    'Foto/video Simulacion integrada "The Office Tour & Supply Order"',
    'Foto/video Shadowing Dia 1 NUEVO ciclo (con video, escuchar + repetir)',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO) - ENTREGADO FISICAMENTE con la guia (no fotografiado)',
    'Lista quienes NO entregaron tarea Cl 25',
    'Libreta personal con 3 errores literales + NOMBRE (privado coordinacion)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'Entendi que el ARCO DE REPASO esta en marcha (Cl 26 = arco clase 5)',
    'Entendi que el A2 Book termino en M44, NO hay modulo nuevo',
    'NO invente contenido del libro ni resultados; patrones TIPICOS sin nombres',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 25 preguntas/negativos/auxiliares + orden palabras)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'Verifique virtud CL 26 = TEMPLANZA v2 dia 1 (CAMBIO HOY: Cl 21-25 fue PRUDENCIA v2; Cl 26-28 = TEMPLANZA v2 parcial)',
    'ANUNCIE la transicion PRUDENCIA -> TEMPLANZA al inicio de VATS',
    'Hile TEMPLANZA en VATS = "choose the right preposition, the right article, the right amount - not too much, not too little"',
    'CORRECCION A1: preposiciones de tiempo - AT hora / ON dia/fecha / IN mes-anio-parte del dia',
    'CORRECCION A2: preposiciones de lugar - AT punto especifico / IN dentro-ciudad-pais / ON superficie',
    'CORRECCION A3: dependencias fijas verbo/adjetivo (good AT, depend ON, listen TO, worried ABOUT, arrive AT-IN, live IN)',
    'CORRECCION B1: articulos a/an (por SONIDO no por letra: "a university", "an hour") / the (especifico/cardinales/superlativos) / sin articulo (abstractos/incontables en general)',
    'CORRECCION B2: cuantificadores - MANY (contable) / A LOT OF (afirmativo) / MUCH (solo neg/preg) / SOME (afirm + ofertas) / ANY (neg/preg)',
    'NUNCA dije "a money" (uncountable NO va con a/an)',
    'Use SOLO patrones de error TIPICOS/CANONICOS, SIN nombres en la guia',
    'Conduje Drill de refuerzo A preposiciones (velocidad, automatico)',
    'Marque el descanso al cierre de la primera mitad (~2h)',
    'Conduje Historia Interactiva (reunion de lunes absurda cotidiana, NO fantasia)',
    'Conduje Simulacion "The Appointment Booking" PROFESIONAL (fuerza preposiciones tiempo y lugar)',
    'Conduje Simulacion integrada "The Office Tour & Supply Order" (articulos + cuantificadores + preposiciones)',
    'Verifique link + que HOY = Shadowing DIA 1 NUEVO ciclo, CON video (escuchar + repetir)',
    'Corri Shadowing Dia 1 CON video, escucha pasiva + repeticion frase por frase (NO evaluacion)',
    'Error Paper EXPANDIDO (6 errores) ANONIMO + entregado FISICAMENTE con la guia',
    'En libreta personal anote 3 errores con NOMBRE + cita literal (privado coord.)',
    'En Tarea explique el por que + due date explicito (jueves 28/05 7PM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 27 = arco clase 6 = concordancia / 3a persona -s + there is/are + causativo (TEMPLANZA v2 dia 2)',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class26_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 26 de 28 | ARCO REPASO - Preposiciones + Articulos/Cuantificadores',
    'ARCO REPASO - Preposiciones + Articulos/Cuantificadores: in/on/at tiempo y lugar + dependencias (good AT / depend ON / listen TO / worried ABOUT / arrive AT-IN / live IN) + a/an/the/sin articulo + much/many/some/any/a lot of - el A2 Book termino en M44, NO hay modulo nuevo. Correccion sistematica + drills de refuerzo + The Appointment Booking + The Office Tour & Supply Order + Shadowing Dia 1 NUEVO ciclo (con video) + FRASE DEL DIA. Virtud TEMPLANZA v2 dia 1 - CAMBIO HOY (Cl 21-25 fue PRUDENCIA v2; Cl 26-28 = TEMPLANZA v2 parcial porque el nivel termina en Cl 28).',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class26_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 27/05 A2 INTENSIVO 4h AM Cl 26:')
print('  - A2/A2_4h_Class26_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class26_REPORTE.pdf')
