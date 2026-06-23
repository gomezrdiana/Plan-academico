#!/usr/bin/env python3
"""Genera la guia + reporte del A1 Nocturno 2H Cl 37 (viernes 29/05/2026):
- Consolidacion Integrada post-M35: Speed Dating 5 rondas (CAN/SHOULD/PASADO/CONTINUO/
  GOING TO) + Portafolio A1 (recogen mejores escritos + reflexion "I couldn't / Now I can")
  + Explicacion 3 miniproyectos (A Mi Video / B Guia Turistica / C Antes y Despues)
  con tarjeta de 5 palabras clave + Practica en parejas con feedback + ANUNCIO 5 TEMAS
  ORAL FINAL Cl 45 (Guia Bucaramanga / Restaurante ideal / Mi vida en 5 anos / Mi
  familia al mundo / Un dia loco).
- Virtud: FORTALEZA v2 dia 2 (Cl 36-40 = FORTALEZA v2).
- Frase del Dia: "I'm going to choose my topic and finish strong - that's what fortitude
  looks like."
- A1 Book TERMINO en M35 (pag 416); Cl 34-44 = CONSOLIDACION INTEGRADA hacia Oral Final
  (Cl 45). No hay modulo nuevo. Inspirado en Cl 38 plan estructural Parte 4, adaptado
  SIN GoldList.
- Profesor Christian, cohorte 6, asistencia 50-67%. SIN GoldList. Reporte estatico
  (se llena a mano). Tarea FIN DE SEMANA due lunes 01/06 antes 7AM, 25-30 min, NO
  fragmentada.
- Profesor SOLO anuncia los 5 temas como hecho de cronograma; NO discute criterios/
  notas/rubrica del Oral Final ni del Final escrito (eso es coordinacion).
- Anuncio Cl 38 lunes = Practica intensiva miniproyecto + Time Capsule + FORTALEZA v2
  dia 3.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class37_PRINT.md'), os.path.join(A1_DIR, 'A1_Class37_GUIA.pdf'))
print('OK: A1_Class37_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 36 = Mi Ciudad Ideal + simulaciones libres)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza dia 2 + decision de tema honesto)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 36 simulaciones libres: tiempos / comparativos / preguntas)', '7 min'),
    ('SPEED DATING 5 RONDAS - CAN/SHOULD/PASADO/CONTINUO/GOING TO (DE PIE, 2 min x ronda)', '20 min'),
    ('PORTAFOLIO A1 - elegir 3 mejores escritos + reflexion "I couldn\'t / Now I can"', '15 min'),
    ('EXPLICACION 3 MINIPROYECTOS (A/B/C) + tarjeta 5 palabras clave', '15 min'),
    ('PRACTICA MINIPROYECTO EN PAREJAS + feedback entre pares (DE PIE, 2 rondas)', '12 min'),
    ('SHADOWING (verificar dia del ciclo)', '13 min'),
    ('ANUNCIO 5 TEMAS ORAL FINAL Cl 45 + Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Speed Dating preguntas + 5 TEMAS Oral Final',
    'Foto/video PEER TEACHER', 'Foto/video Speed Dating (5 rondas, rotacion visible)',
    'Foto/video parejas practicando miniproyecto',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 36',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Lista: que miniproyecto (A/B/C) eligio cada estudiante + que TEMA Oral Final eligio (o pendiente lunes)',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 36 Mi Ciudad Ideal + simulaciones libres)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso con su tema elegido del Oral Final',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 37 = FORTALEZA v2 dia 2 (Cl 36-40 = FORTALEZA v2)',
    'Hile FORTALEZA dia 2 en VATS con decision de tema honesto (no facil)',
    'CONFIRME que el A1 Book termino en M35 (no hay modulo nuevo - solo consolidacion)',
    'ESCRIBI las 5 preguntas del Speed Dating en tablero ANTES de clase',
    'ACOMODE 2 filas enfrentadas para Speed Dating',
    'Conduje las 5 RONDAS completas (CAN/SHOULD/PASADO/CONTINUO/GOING TO), 2 min c/u, palmada=rotan',
    'NO corregi DURANTE Speed Dating (errores van solo a libreta personal con NOMBRE)',
    'Conduje Portafolio A1: cada estudiante eligio 3 mejores escritos + escribio "I couldn\'t / Now I can" en primera pagina del cuaderno',
    'Explique las 3 opciones de miniproyecto (A Video / B Guia Turistica / C Antes y Despues) con ejemplo de 5 palabras clave',
    'Entregue tarjeta en blanco - cada estudiante escribio sus 5 palabras clave',
    'Anote en libreta personal que opcion (A/B/C) eligio cada estudiante',
    'Conduje 2 rondas de practica miniproyecto en parejas con feedback entre pares (cambio de companero en R2)',
    'Miniproyectos elegidos son COTIDIANOS/PROFESIONALES (no fantasiosos)',
    'Conduje Shadowing del ciclo activo',
    'ESCRIBI los 5 TEMAS del Oral Final en tablero ANTES de clase',
    'ANUNCIE los 5 temas como HECHO de cronograma (lei los 5 en voz alta, repitieron 2x)',
    'NO discuti criterios/notas/rubrica/duracion exacta del Oral Final ni del Final escrito (esa info es de coordinacion)',
    'Si preguntaron por criterios, redirigi: "Coordination will share criteria. Your job: pick your topic and start preparing."',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En libreta personal anote: quien eligio que miniproyecto (A/B/C) y que tema Oral Final',
    'En Tarea explique pedagogicamente el por que + due date explicito (lunes 01/06 antes 7 AM)',
    'Confirme que tarea es FIN DE SEMANA (25-30 min, NO se fragmenta, NO se reduce)',
    'NO acepte la excusa "no me da tiempo" (tienen sabado y domingo)',
    'Anuncie Cl 38 lunes 01/06 = Practica intensiva miniproyecto + Time Capsule + FORTALEZA v2 dia 3',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class37_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 37 de 45 | CONSOLIDACION INTEGRADA - Speed Dating 5 rondas + Portafolio A1 + Pre-Miniproyecto + ANUNCIO 5 TEMAS ORAL FINAL | FORTALEZA v2 dia 2 | FRASE DEL DIA (GoldList retirado)',
    'Speed Dating 5 rondas (CAN/SHOULD/PASADO/CONTINUO/GOING TO) + Portafolio A1 (3 mejores escritos + reflexion I couldn\'t / Now I can) + Explicacion 3 miniproyectos (A Video / B Guia Turistica / C Antes y Despues) + tarjeta 5 palabras clave + Practica parejas con feedback + ANUNCIO 5 TEMAS ORAL FINAL Cl 45 (Guia Bucaramanga / Restaurante ideal / Mi vida en 5 anos / Mi familia al mundo / Un dia loco) + FRASE DEL DIA (A1 Book termino en M35 - Cl 34-44 = consolidacion integrada hacia Oral Final)',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class37_REPORTE.pdf')

print('\n2 PDFs generados para viernes 29/05 A1 Nocturno Cl 37:')
print('  - A1/A1_Class37_GUIA.pdf')
print('  - A1/reportes/A1_Class37_REPORTE.pdf')
