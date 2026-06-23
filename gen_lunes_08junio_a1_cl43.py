#!/usr/bin/env python3
"""Genera la guia + reporte del A1 Nocturno 2H Cl 43 (lunes 08/06/2026):
- MINIPROYECTOS - Presentaciones de Cierre (evaluacion speaking/listening) + SINTESIS dia 3.
  6 estudiantes x ~8 min c/u (3-4 min presentacion + 30 seg Q&A audiencia + 30 seg
  transicion + aplauso/cambio). Profesor cronometra silencioso, anota errores con
  NOMBRE en libreta personal, NO interrumpe, NO comunica criterios/notas.
- Virtud: SINTESIS dia 3 (Cl 41-45 = SINTESIS las 4 virtudes integradas - Prudencia
  para planear, Templanza para no acelerar, Justicia para dar tiempo, Fortaleza para
  terminar fuerte). Verificado en CALENDARIO_VIRTUDES_2026.md "A1 NOCTURNO 2H".
- Frase del Dia: "Today I present myself in English - Prudence to plan, Temperance to
  breathe, Justice to give each idea its time, Fortitude to finish strong. All four
  virtues live in this 4-minute presentation."
- A1 Book TERMINO en M35 (pag 416). Cl 34-44 = consolidacion integrada hacia Examen
  Final (Cl 45). HOY Cl 43 = MINIPROYECTOS, el dia central de cierre del nivel.
- DECISION DIANA 31/05/2026: este evento NO genera archivo _MARKER separado. Los
  eventos (presentaciones/midterm/final) se INTEGRAN en la guia regular del dia
  porque los profes no ejecutan ni las guias regulares completas y agregar artifacts
  los satura.
- Profesor Christian, cohorte 6, asistencia 50-67%. SIN GoldList. Reporte estatico
  (se llena a mano). Tarea Cl 44 due martes 09/06 antes 7 PM, 15-20 min, NO
  fragmentada (reflexion 3 frases + grabacion 2 min de voz + descanso de voz pre-Final).
- Profesor SOLO anuncia que Cl 44 martes = repaso final pre-Final y Cl 45 viernes =
  Examen Final (ultimas 2h del nivel, regla firme Diana 22/05/2026). NO discute
  criterios/notas/rubrica/puntaje de Miniproyectos ni del Final escrito (exclusivo
  coordinacion).
- Rol del profesor HOY: cronometro silencioso + facilitador + observador con libreta
  personal. NO juez. NO interrumpe presentaciones. NO comunica evaluacion.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class43_PRINT.md'), os.path.join(A1_DIR, 'A1_Class43_GUIA.pdf'))
print('OK: A1_Class43_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 42 fin de semana = practicar miniproyecto 2x voz alta + descansar voz + dormir bien)', '5 min'),
    ('EL POR QUE DE HOY', '3 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (SINTESIS dia 3 - las 4 virtudes en el acto de presentarse + cual virtud susurras antes de subir)', '5 min'),
    ('PEER TEACHER SLOT (1 error tipico bloqueante Cl 41-42: pronunciacion o tiempo verbal de presentacion personal)', '7 min'),
    ('RECORDATORIO 3 REGLAS DE ORO (tarjeta 5 palabras MAX / NO leer / mistakes OK) + ORDEN DE PRESENTACIONES escrito en tablero', '4 min'),
    ('MINIPROYECTOS - PRESENTACIONES (6 estudiantes x ~8 min: 3-4 min presentacion + aplauso + 1 Q audiencia en ingles + transicion) - DE PIE presentador / sentados audiencia', '52 min'),
    ('SHADOWING corto (descanso post-presentacion, voz suave)', '8 min'),
    ('ERROR PAPER LIVE (errores tipicos de las presentaciones, anonimos en tablero) + Frase del Dia CIERRE (1 estudiante de memoria + 1 adapta a su miniproyecto)', '10 min'),
    ('RECONOCIMIENTO GRUPAL (factual: 9 semanas, 90 horas, 4 min cada uno) + Tarea Cl 44 + Anuncio Cl 44 martes = repaso final + Anuncio Cl 45 viernes = EXAMEN FINAL (hecho de calendario) + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Orden de Presentaciones + 3 Reglas de Oro + Errores',
    'Foto/video PEER TEACHER',
    'Foto/video de las 6 presentaciones (1 foto + 1 video corto por presentador si se puede)',
    'Foto/video del Shadowing post-presentaciones',
    'Foto/video del Error Paper Live + Frase del Dia CIERRE',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 42 (con NOMBRE)',
    'LIBRETA PERSONAL CENTRAL HOY: NOMBRE + errores literales por estudiante + tiempo real de cada presentacion + 1 fortaleza observada por estudiante (esto es lo central para coordinacion hoy)',
    'Tarjeta de 5 palabras MAX de cada estudiante (foto rapida antes/despues)',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio Cl 44 martes 09/06 = repaso final pre-Final',
    'Confirmaste anuncio Cl 45 viernes 12/06 = EXAMEN FINAL (hecho de calendario, sin criterios/notas)',
    'Confirmaste que NO comunicaste criterios/notas/rubrica/puntaje de Miniproyectos ni del Final',
]
a1_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 42 = practicar 2x voz alta + descansar voz)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE durante clase (objetivo 4 inserciones marcadas)',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la adapto a su miniproyecto recien presentado',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 43 = SINTESIS dia 3 (Cl 41-45 = SINTESIS las 4 integradas)',
    'Hile SINTESIS dia 3 en VATS: cual virtud susurras antes de subir a presentar + las otras 3 viven igual',
    'CONFIRME que el A1 Book termino en M35 (no hay modulo nuevo - HOY es PRESENTACION total)',
    'CONFIRME que este evento NO genera archivo _MARKER separado (decision Diana 31/05/2026: integrado en la guia regular)',
    'ESCRIBI EL ORDEN de las 6 presentaciones en el tablero ANTES de empezar bloque 6 (criterio interno - momentum - no se vota)',
    'CRONOMETRO visible durante TODO el bloque 7 (alarma a 3:30, corte suave a 4:00, "Thank you. Applause." a 4:30)',
    'CHEQUE la tarjeta de 5 palabras MAX de cada estudiante ANTES de que suba ("Show me your card. Five words. OK, go.")',
    'NO INTERRUMPI durante NINGUNA presentacion (ni para corregir, ni para felicitar, ni para "ayudar")',
    'NO CORREGI durante las presentaciones (errores van solo a libreta personal con NOMBRE + cita textual)',
    'NO TRADUJE durante las presentaciones',
    'NO COMUNIQUE criterios/notas/rubrica/puntaje de Miniproyectos (esa info es de coordinacion)',
    'NO COMUNIQUE criterios/notas/rubrica/puntaje/formato/peso del Final (esa info es de coordinacion)',
    'Si alguien pregunto por criterios/notas, redirigi: "Coordination will share criteria. Your job: present, listen, support each other." y segui',
    'Si alguien CONGELO en su presentacion conte 5 seg internos + 1 frase "Take a breath. Next keyword." (NO complete frases por ellos)',
    'Si alguien se PASO de 4 min: "Bring it to a close" a 4:00 + corte limpio a 4:30',
    'Si alguien LEYO la tarjeta mas de 3 seg seguidos: 1 palmada suave + "Eyes up" (1 vez por presentacion)',
    'AUDIENCIA hizo 1 pregunta corta en ingles a cada presentador (refuerza listening activo)',
    'APLAUSO grupal real (no simbolico) despues de cada presentacion',
    'En LIBRETA PERSONAL anote por cada estudiante: NOMBRE + 3 errores literales + tiempo real + 1 fortaleza observada',
    'Conduje SHADOWING corto y suave (voz suave, no proyeccion, descanso post-presentacion)',
    'Conduje ERROR PAPER LIVE con errores anonimos de las presentaciones (NO atribuibles a estudiante especifico)',
    'Camine con papel errores anonimo',
    'Conduje RECONOCIMIENTO GRUPAL factual (9 semanas, 90 horas, 4 min cada uno) - SIN paternalismo, SIN "estoy orgulloso", SIN "estuvieron geniales"',
    'En Tarea Cl 44 explique pedagogicamente el por que + due date explicito (MARTES 09/06 antes 7 PM)',
    'Tarea Cl 44 es 15-20 min (regla A1), NO fragmentada (reflexion 3 frases + grabacion 2 min de voz + descanso de voz pre-Final)',
    'NO acepte la excusa "no me da tiempo" (15-20 min en una noche)',
    'Anuncie Cl 44 martes 09/06 = repaso final pre-Final + tarea de descanso de voz',
    'Anuncie Cl 45 viernes 12/06 = EXAMEN FINAL (ultimas 2h del nivel - regla firme) como HECHO DE CALENDARIO SOLO (sin nota, sin criterios, sin formato, sin peso - exclusivo coordinacion)',
    'Cierre seco y factual (NO drama, NO "se acabo el nivel" - el nivel se acaba viernes Cl 45)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(
    os.path.join(A1_REP, 'A1_Class43_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 43 de 45 | MINIPROYECTOS - Presentaciones de Cierre (evaluacion speaking/listening) | SINTESIS dia 3 | FRASE DEL DIA (GoldList retirado)',
    'MINIPROYECTOS - 6 estudiantes presentan 3-4 min su miniproyecto elegido (A My Presentation Video / B My City Tourist Guide / C My Before and After) con tarjeta de 5 palabras MAX, SIN LEER, mistakes OK. Audiencia hace 1 pregunta corta en ingles por presentador (listening activo). Profesor cronometra SILENCIOSO, anota errores con NOMBRE en libreta personal, NO interrumpe, NO corrige, NO comunica criterios/notas (exclusivo coordinacion). Andamiaje pre: Mystery (verifica practica fin de semana) + Frase del Dia (4 virtudes en el acto de presentarse) + VATS SINTESIS dia 3 + Peer Teacher (1 error bloqueante anonimo) + Recordatorio 3 reglas de oro + Orden de presentaciones. Aterrizaje post: Shadowing corto (descanso de voz) + Error Paper Live (errores tipicos anonimos) + Frase del Dia CIERRE + Reconocimiento grupal factual + Tarea Cl 44 + Anuncio Cl 44 martes (repaso final pre-Final) + Anuncio Cl 45 viernes (Examen Final - ultimas 2h del nivel - hecho de calendario SOLO) (A1 Book termino en M35 - Cl 34-44 = consolidacion integrada hacia Final Cl 45; NO archivo _MARKER separado - decision Diana 31/05/2026: eventos se INTEGRAN en la guia regular del dia)',
    a1_act, a1_deliv, a1_eval, S,
)
print('OK: A1_Class43_REPORTE.pdf')

print('\n2 PDFs generados para lunes 08/06 A1 Nocturno Cl 43:')
print('  - A1/A1_Class43_GUIA.pdf')
print('  - A1/reportes/A1_Class43_REPORTE.pdf')
