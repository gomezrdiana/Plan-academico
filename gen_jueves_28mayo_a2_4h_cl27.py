#!/usr/bin/env python3
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 27 (jueves 28/05/2026):
- ARCO DE REPASO DE ERRORES COMUNES (Cl 21-28) - Cl 27 = arco clase 6.
  EL A2 BOOK TERMINO EN M44 (pag 352): NO hay Modulo 45, NO se inventa
  contenido. Cl 22 abrio el arco (tiempos), Cl 23 comparacion + gerundio/
  infinitivo, Cl 24 phrasal + pasivo, Cl 25 preguntas/negativos/auxiliares
  + orden, Cl 26 preposiciones + articulos/cuantificadores. HOY =
  correccion sistematica del sexto y ULTIMO cluster antes del mastery
  integrado y examen final:
  CONCORDANCIA / 3a PERSONA -S + THERE IS/ARE + CAUSATIVO
    A) 3a -s: he/she/it + verb+S; DOESN'T + base; has/goes/watches/does
    B) there is (singular) / there are (plural); was/were; "it have" NO
    C) causativo: want/tell/ask + obj + TO + verb; make/let + obj +
       verb BASE (sin "to"); have/get + obj + V3 (causativo pasivo)
  + drills de refuerzo + simulacion que fuerza las formas corregidas.
- Patrones de error TIPICOS/CANONICOS cosechados de A2 Book M2/M4
  (3a -s, doesn't, has), M14 (there is/are, was/were) y M44 (Active
  Causative: want/tell/ask + to; make/let SIN to; have/get + V3 pasivo),
  mas interferencia del espanol (calco "I want THAT you go" / "I made
  him TO work"), sin nombres (guia reutilizable).
- Shadowing Dia 2 = MISMO ciclo, SIN video, de memoria (el ciclo abrio
  en Cl 26 Dia 1) + Frase del Dia + virtud TEMPLANZA v2 dia 2 (por
  numero de clase: Cl 26-28 = TEMPLANZA v2 parcial - nivel termina).
- Sigue a Cl 26 (arco clase 5, preposiciones + articulos/cuantificadores).
  SIN GoldList. Reporte estatico (se llena a mano).
- ANUNCIO Cl 28 = MASTERY INTEGRADO (primeras 2h) + EXAMEN FINAL
  (ultimas 2h). El profesor NO comunica detalles del examen
  (criterios/contenido/calificacion) - eso es coordinacion. Solo
  anuncia el hecho de cronograma al cierre.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class27_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class27_GUIA.pdf'))
print('OK: A2_4h_Class27_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 26 = preposiciones + articulos/cuantificadores)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Templanza v2 dia 2 + 3a -s + there is/are + causativo)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de preposiciones o articulos/cuantificadores - refuerzo cluster Cl 26)', '7 min'),
    ('Tarea Check Cl 26', '5 min'),
    ('CORRECCION SISTEMATICA A - 3a persona -s (verb+S, doesn\'t, has/goes/watches)', '20 min'),
    ('DRILL DE REFUERZO A - 3a persona -s (velocidad, automaticidad)', '15 min'),
    ('DESCANSO (fin primera mitad ~2h) / CORRECCION SISTEMATICA B - there is/are (singular vs plural, was/were)', '17 min'),
    ('CORRECCION SISTEMATICA C - causativo (want/tell/ask + to; make/let SIN to; have/get + V3)', '20 min'),
    ('HISTORIA INTERACTIVA - "The day the boss had everything done" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL - "The Team Briefing" (fuerza 3a -s + causativo, DE PIE)', '25 min'),
    ('SIMULACION INTEGRADA - "The Office Tour" (there is/are + 3a -s + causativo, DE PIE)', '20 min'),
    ('SHADOWING - DIA 2: MISMO CICLO, SIN VIDEO, DE MEMORIA (DE PIE)', '18 min'),
    ('Free production - 3a -s + there is/are + causativo (parejas DE PIE)', '12 min'),
    ('Error Paper Live EXPANDIDO (6 errores) + Frase del Dia CIERRE + Tarea + Anuncio Cl 28 (MASTERY + EXAMEN FINAL)', '13 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 26 preposiciones + articulos/cuantificadores)',
    'Foto del tablero - Frase del Dia + 3a -s + There is/are + Causativo',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "The Team Briefing"',
    'Foto/video Simulacion integrada "The Office Tour"',
    'Foto/video Shadowing Dia 2 (sin video, de memoria)',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO) - ENTREGADO FISICAMENTE con la guia (no fotografiado)',
    'Lista quienes NO entregaron tarea Cl 26',
    'Libreta personal con 3 errores literales + NOMBRE (privado coordinacion)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmacion: NO comunicaste detalles del Examen Final de manana',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'Entendi que el ARCO DE REPASO esta en marcha (Cl 27 = arco clase 6)',
    'Entendi que el A2 Book termino en M44, NO hay modulo nuevo',
    'NO invente contenido del libro ni resultados; patrones TIPICOS sin nombres',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 26 preposiciones + articulos/cuantificadores)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 4+ veces NATURALMENTE (3 inserciones marcadas + cierre)',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'NO comunique criterios/contenido/calificacion del EXAMEN FINAL de manana',
    'Verifique virtud CL 27 = TEMPLANZA v2 dia 2 (por numero de clase, Cl 26-28 parcial)',
    'Hile TEMPLANZA en VATS = "match the verb to the subject; the right form for the right number"',
    'CORRECCION A1: 3a persona singular -> verbo + S/ES ("He GOES", "She WATCHES")',
    'CORRECCION A2: negativa 3a singular -> DOESN\'T + verbo BASE ("She DOESN\'T like")',
    'CORRECCION A3: pregunta 3a singular -> DOES + verbo BASE ("Does he PLAY?", no "plays")',
    'CORRECCION A4: have -> HAS en 3a singular; everybody/nobody = singular -> HAS',
    'CORRECCION B1: there is (singular) vs there are (plural); was/were para pasado',
    'CORRECCION B2: "It have" NUNCA para existencia -> "There is/are" + recordar THERE',
    'CORRECCION C1: want/tell/ask + OBJECT + TO + verb ("I want YOU TO go"); NO "that"',
    'CORRECCION C2: make/let + OBJECT + verb BASE (SIN "to"): "I made him WORK"',
    'CORRECCION C3: have/get + OBJECT + V3 = causativo pasivo: "I have my hair CUT"',
    'Use SOLO patrones de error TIPICOS/CANONICOS, SIN nombres en la guia',
    'Conduje Drill de refuerzo A 3a -s (singular/plural/negativos/preguntas, automatico)',
    'Marque el descanso al cierre de la primera mitad (~2h)',
    'Conduje Historia Interactiva (dia de oficina absurdo cotidiano, NO fantasia)',
    'Conduje Simulacion "The Team Briefing" PROFESIONAL (fuerza 3a -s + causativo)',
    'Conduje Simulacion integrada "The Office Tour" (there is/are + 3a -s + causativo)',
    'Verifique link + que HOY = Shadowing DIA 2 = MISMO ciclo, SIN video (de memoria)',
    'Corri Shadowing Dia 2 SIN video, recuperacion de memoria (NO evaluacion)',
    'Error Paper EXPANDIDO (6 errores: 2 3a-s + 2 there is/are + 2 causativo) ANONIMO + entregado FISICAMENTE',
    'En libreta personal anote 3 errores con NOMBRE + cita literal (privado coord.)',
    'En Tarea explique el por que + due date explicito (viernes 29/05 antes 7AM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 28 = MASTERY INTEGRADO (primeras 2h) + EXAMEN FINAL (ultimas 2h) - hecho de cronograma SIN detalles',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class27_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 27 de 28 | ARCO REPASO - 3a Persona -S + There Is/Are + Causativo',
    'ARCO REPASO - Concordancia / 3a Persona -S + There Is/Are + Causativo: A) 3a -s (verb+S, doesn\'t, has/goes/watches) + B) there is (singular) vs there are (plural), was/were + C) causativo (want/tell/ask + TO; make/let SIN to; have/get + V3 pasivo) - el A2 Book termino en M44, NO hay modulo nuevo. Correccion sistematica + drills de refuerzo + The Team Briefing + The Office Tour + Shadowing Dia 2 (sin video, de memoria) + FRASE DEL DIA. Virtud TEMPLANZA v2 dia 2 (Cl 26-28 parcial). Anuncio Cl 28 = mastery integrado + EXAMEN FINAL (hecho de cronograma, sin detalles - coordinacion maneja el examen).',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class27_REPORTE.pdf')

print('\n2 PDFs generados para jueves 28/05 A2 INTENSIVO 4h AM Cl 27:')
print('  - A2/A2_4h_Class27_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class27_REPORTE.pdf')
