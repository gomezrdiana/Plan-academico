#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 42 (viernes 05/06/2026):
- Consolidacion Final 2 post-M35 - SINTESIS dia 2: Ultimo simulacro mini-examen formato
  Final (15 items + autocorreccion + KEY) + Ultimo ensayo oral miniproyecto (grupos de 4,
  3-4 min c/u + feedback) + Quiz formato examen (4 equipos, 15 preguntas, 30 seg c/u) +
  Motivacion pre-Miniproyectos con 3 reglas de oro (5 palabras MAX / NO leer / errores OK).
- Virtud: SINTESIS dia 2 (Cl 41-45 = SINTESIS las 4 virtudes integradas - Prudencia para
  planear, Templanza para no acelerarse, Justicia para dar tiempo a cada idea, Fortaleza
  para terminar fuerte). Verificado en CALENDARIO_VIRTUDES_2026.md "A1 NOCTURNO 2H".
- Frase del Dia: "I can speak about my past, my present, and my future - all four virtues
  live in my English now."
- A1 Book TERMINO en M35 (pag 416); Cl 34-44 = CONSOLIDACION INTEGRADA hacia Miniproyectos
  (Cl 43 lunes 08/06) y Examen Final (Cl 45 viernes 12/06). Hoy NO hay modulo nuevo - solo
  ensayo y consolidacion total. Inspirado en plan estructural Cl 42 (Parte 4) adaptado
  SIN GoldList.
- Profesor Christian, cohorte 6, asistencia 50-67%. SIN GoldList. Reporte estatico
  (se llena a mano). Tarea FIN DE SEMANA due lunes 08/06 antes 7AM, 30-40 min, NO
  fragmentada (practicar miniproyecto 2x + descansar voz + dormir bien).
- Profesor SOLO anuncia que Cl 43 lunes = MINIPROYECTOS (presentaciones de cierre,
  evaluacion speaking/listening) con 3 reglas de oro; NO discute criterios/notas/
  rubrica de Miniproyectos ni del Final escrito (eso es coordinacion).
- Anuncio Cl 43 lunes 08/06 = MINIPROYECTOS (presentaciones 3-4 min, evaluacion
  speaking/listening) + SINTESIS dia 3.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class42_PRINT.md'), os.path.join(A1_DIR, 'A1_Class42_GUIA.pdf'))
print('OK: A1_Class42_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 41 = practicar miniproyecto + repasar tiempos debiles)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (SINTESIS dia 2 - las 4 virtudes en mi ingles + cual es la mas dificil al hablar)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 41 simulacro + speaking libre: was/were, falta be, modal+to)', '7 min'),
    ('ULTIMO SIMULACRO MINI-EXAMEN FORMATO FINAL (15 items: gramatica/vocab/traduccion/escritura/lectura + autocorreccion con KEY)', '25 min'),
    ('ULTIMO ENSAYO ORAL MINIPROYECTO en grupos de 4 (3-4 min c/u + 30 seg feedback) - DE PIE', '25 min'),
    ('QUIZ FORMATO EXAMEN - 4 equipos, 15 preguntas, 30 seg c/u - DE PIE', '17 min'),
    ('SHADOWING (verificar dia del ciclo)', '8 min'),
    ('MOTIVACION PRE-MINIPROYECTOS (3 reglas oro: 5 palabras MAX / NO leer / errores OK) + Error Paper Live + Frase del Dia CIERRE + Tarea fin de semana + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + 3 reglas de oro Miniproyectos + Errores',
    'Foto/video PEER TEACHER',
    'Foto/video simulacro escrito en silencio + KEY entregada',
    'Foto/video ultimo ensayo oral miniproyecto en grupos de 4',
    'Foto/video Quiz formato examen (4 equipos)',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 41',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista: quien quedo listo para Miniproyectos lunes / quien aun necesita coaching',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 41 = practicar miniproyecto + tiempos debiles)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la adapto a su miniproyecto del lunes',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 42 = SINTESIS dia 2 (Cl 41-45 = SINTESIS las 4 integradas)',
    'Hile SINTESIS dia 2 en VATS con las 4 virtudes en uso al hablar + cual es la mas dificil',
    'CONFIRME que el A1 Book termino en M35 (no hay modulo nuevo - hoy es ENSAYO total)',
    'IMPRIMI la hoja del simulacro formato Final (15 items) + hoja KEY ANTES de clase',
    'Conduje el simulacro escrito en SILENCIO TOTAL (sin ayudar, sin traducir, sin corregir durante)',
    'Entregue KEY para auto-correccion + permiti 1-2 dudas criticas (sin discutir notas)',
    'Forme grupos de 4 para ultimo ensayo oral miniproyecto (o 3+3 si son 6)',
    'Cada estudiante presento su miniproyecto 3-4 min + grupo dio 30 seg feedback',
    'NO interrumpi durante presentaciones (errores van solo a libreta personal con NOMBRE)',
    'Forme 4 equipos para Quiz formato examen + cronometra 30 seg por pregunta',
    'Equipo ganador recibio +10 EP',
    'Conduje Shadowing del ciclo activo',
    'Di MOTIVACION pre-Miniproyectos con las 3 REGLAS DE ORO (5 palabras MAX / NO leer / errores OK)',
    'NO discuti criterios/notas/rubrica/duracion exacta de Miniproyectos ni del Final escrito (esa info es de coordinacion)',
    'Si preguntaron por criterios, redirigi: "Coordination will share criteria. Your job: rehearse twice, rest your voice, show up Monday."',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En libreta personal anote: quien quedo listo para Miniproyectos lunes / quien necesita coaching',
    'En Tarea explique pedagogicamente el por que + due date explicito (LUNES 08/06 antes 7 AM)',
    'Confirme que tarea es FIN DE SEMANA (30-40 min, NO se fragmenta, NO se reduce)',
    'NO acepte la excusa "no me da tiempo" (tienen sabado, domingo y madrugada del lunes)',
    'Anuncie Cl 43 lunes 08/06 = MINIPROYECTOS (presentaciones de cierre, evaluacion speaking/listening) + SINTESIS dia 3',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class42_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 42 de 45 | CONSOLIDACION FINAL 2 - Ultimo Simulacro Formato Final + Ultimo Ensayo Oral Miniproyecto + Quiz Formato Examen + Motivacion pre-Miniproyectos | SINTESIS dia 2 | FRASE DEL DIA (GoldList retirado)',
    'Ultimo simulacro mini-examen formato Final (15 items + autocorreccion con KEY) + Ultimo ensayo oral miniproyecto en grupos de 4 (3-4 min c/u + 30 seg feedback) + Quiz formato examen (4 equipos, 15 preguntas, 30 seg c/u) + Motivacion pre-Miniproyectos con 3 reglas de oro (5 palabras MAX / NO leer / errores OK) + FRASE DEL DIA (A1 Book termino en M35 - Cl 34-44 = consolidacion integrada hacia Miniproyectos Cl 43 lunes 08/06 y Final Cl 45)',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class42_REPORTE.pdf')

print('\n2 PDFs generados para viernes 05/06 A1 Nocturno Cl 42:')
print('  - A1/A1_Class42_GUIA.pdf')
print('  - A1/reportes/A1_Class42_REPORTE.pdf')
