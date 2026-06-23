#!/usr/bin/env python3
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 28 (viernes 29/05/2026):
- ULTIMA CLASE DEL NIVEL A2 4h. ARCO DE REPASO DE ERRORES COMUNES
  (Cl 21-28) - Cl 28 = arco clase 7 = MASTERY INTEGRADO + EXAMEN FINAL.
  EL A2 BOOK TERMINO EN M44 (pag 352): NO hay Modulo 45, NO se inventa
  contenido. Cl 22-27 corrieron los 6 clusters del arco. HOY = recorrido
  relampago de los 6 clusters en drill mixto + simulacion integrada
  profesional final + Shadowing Dia 3 (mini-competencia, cierre del
  ciclo) + cierre del arco + Examen Final A2 (escrito 75 min + oral
  ~30 min + cierre 10 min).
- ESTRUCTURA DOBLE: 00:00-02:00 mastery + cierre del arco; 02:00-04:00
  Examen Final (contenido y rubrica de coordinacion - el profesor solo
  aplica, recolecta y entrega).
- Patrones de error TIPICOS/CANONICOS de las 6 guias previas Cl 22-27
  + A2 Book (M2/M4/M14/M18/M23/M24/M27/M44) + pedagogia estandar A2->B1,
  sin nombres (guia reutilizable).
- Shadowing Dia 3 = MISMO ciclo, mini-competencia (CIERRE del ciclo).
  El ciclo abrio en Cl 26 (Dia 1 con video), Cl 27 fue Dia 2 (sin video).
  Va en la PRIMERA MITAD - si por tiempo no entra, se OMITE LIMPIO
  y se anuncia cierre del ciclo (no se reasigna a otro dia).
- Frase del Dia (ULTIMO dia del ritual en A2 4h) + virtud TEMPLANZA v2
  dia 3 (por numero de clase: Cl 26-28 = TEMPLANZA v2 parcial - nivel
  termina).
- Cierre del nivel: Tarjeta de Crecimiento de Caracter + foto grupal +
  entrega fisica de examenes y portafolios a coordinacion.
- Profesor NUNCA comunica notas/criterios/contenido/resultados (exclusivo
  coordinacion). Anti-fraude: escritura a mano, sin dispositivos, oral
  en vivo.
- Sigue a Cl 27 (arco clase 6, 3a -s + there is/are + causativo).
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

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class28_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class28_GUIA.pdf'))
print('OK: A2_4h_Class28_GUIA.pdf')

a2_act = [
    ('MITAD 1 / MYSTERY HOMEWORK CHECK (tarea Cl 27 = 3a -s + there is/are + causativo)', '5 min'),
    ('EL POR QUE DE HOY (anuncio doble mitad: mastery + examen)', '2 min'),
    ('FRASE DEL DIA - presentacion (CIERRE del nivel A2 4h)', '4 min'),
    ('VATS (Templanza v2 dia 3 - ULTIMO dia del nivel - 6 clusters integrados)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de 3a -s / there is/are / causativo - refuerzo cluster Cl 27 - ULTIMO del nivel)', '7 min'),
    ('Tarea Check Cl 27', '5 min'),
    ('MASTERY INTEGRADO - drill rapido de los 6 clusters del arco Cl 22-27 (tiempos / comparacion+ger-inf / phrasal+pasiva / preguntas-aux+orden / preposiciones+art-cuant / 3a-s+there+causativo)', '35 min'),
    ('SIMULACION INTEGRADA PROFESIONAL FINAL - "The Handover Briefing" (las 6 familias en contexto, DE PIE)', '30 min'),
    ('SHADOWING DIA 3 - MINI-COMPETENCIA (cierre del ciclo, DE PIE) - SI TIEMPO PERMITE; si no, OMITIR LIMPIO', '15 min'),
    ('CIERRE DEL ARCO + Error Paper Live EXPANDIDO (6 errores - 1 por cluster) + Frase del Dia CIERRE DEL NIVEL', '10 min'),
    ('Transicion calmada al examen (agua, bano, telefonos al frente, tablero limpio)', '2 min'),
    ('MITAD 2 / EXAMEN FINAL A2 / E1 PREP - instrucciones, hojas en pupitres, 1 duda procedimiento por persona', '5 min'),
    ('E2 EXAMEN ESCRITO A2 (5 secciones genericas - contenido de coordinacion: gramatica mixta / vocabulario / traduccion / escritura / lectura) - A MANO EN PLUMA, SIN DISPOSITIVOS', '75 min'),
    ('E3 EXAMEN ORAL A2 (~5 min x estudiante - temas asignados por coordinacion - profesor NO da feedback)', '30 min'),
    ('E4 CIERRE DEL NIVEL - Tarjeta de Crecimiento de Caracter + foto grupal + entrega fisica de examenes y portafolios a coordinacion', '10 min'),
]
a2_deliv = [
    'Reporte impreso lleno (con checklist del FINAL aplicado)',
    'Foto del SOBRE Mystery (chequea Cl 27 = 3a -s + there is/are + causativo)',
    'Foto del tablero - Frase del Dia + 6 secciones del mastery (ANTES de borrarlo para el examen)',
    'Foto/video PEER TEACHER (ultimo del nivel)',
    'Foto/video Simulacion integrada FINAL "The Handover Briefing"',
    'Foto/video Shadowing Dia 3 mini-competencia (si entro por tiempo; si no, marcar OMITIDO LIMPIO)',
    'Papel errores fisico EXPANDIDO (ANONIMO, 6 errores - 1 por cluster) - ENTREGADO FISICAMENTE con la guia (no fotografiado)',
    'Examenes ESCRITOS fisicos (en orden de lista, contados) - ENTREGA FISICA a coordinacion',
    'Hoja de anotaciones del ORAL (nombres + notas privadas para coordinacion)',
    'Tarjetas de Crecimiento de Caracter del nivel (1 por estudiante)',
    'Portafolios fisicos del nivel (entregados por estudiante segun pida coordinacion)',
    'Foto grupal de cierre (camara del salon, NO del profesor)',
    'Lista NO PRESENTADOS al ESCRITO (con nombres)',
    'Lista NO PRESENTADOS al ORAL (con nombres)',
    'Lista quienes NO entregaron tarea Cl 27',
    'Libreta personal con 3 errores literales + NOMBRE + observaciones del mastery por cluster (privado coordinacion)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente (ULTIMO dia del ritual A2 4h)',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'Entendi que HOY es la ULTIMA CLASE del nivel A2 4h (Cl 28 = arco clase 7)',
    'Entendi la ESTRUCTURA DOBLE: 00:00-02:00 mastery / 02:00-04:00 examen',
    'Entendi que el A2 Book termino en M44, NO hay modulo nuevo, mastery = recorrido de Cl 22-27',
    'NO invente contenido del libro ni resultados; patrones TIPICOS sin nombres',
    'HABLE 100% EN INGLES (incluido durante el examen)',
    'EXPLIQUE OBJETIVO de cada actividad ANTES (mastery y examen)',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 27 = 3a -s + there is/are + causativo)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE durante el mastery',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion (CIERRE DEL NIVEL)',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'NO di detalles del examen (criterios, contenido, peso) ni respondi preguntas sobre contenido',
    'Verifique virtud CL 28 = TEMPLANZA v2 dia 3 (por numero de clase: Cl 26-28 parcial - nivel termina)',
    'Hile TEMPLANZA en VATS = "plan the verb, match the subject, place the word - the right form for the right number"',
    'CONDUJE el MASTERY INTEGRADO recorriendo los 6 clusters en ~5-6 min cada uno (~35 min total)',
    'CLUSTER 1 (Tiempos) cubierto en mastery',
    'CLUSTER 2 (Comparacion + gerundio/infinitivo) cubierto en mastery',
    'CLUSTER 3 (Phrasal + voz pasiva) cubierto en mastery',
    'CLUSTER 4 (Preguntas/auxiliares + orden palabras) cubierto en mastery',
    'CLUSTER 5 (Preposiciones + articulos/cuantificadores) cubierto en mastery',
    'CLUSTER 6 (3a -s + there is/are + causativo) cubierto en mastery',
    'CIERRE del mastery: 5 estudiantes AL AZAR produjeron oraciones que combinan 2+ clusters',
    'Conduje Simulacion integrada FINAL "The Handover Briefing" (las 6 familias en contexto profesional)',
    'Verifique link + que HOY = Shadowing DIA 3 = MINI-COMPETENCIA (cierre del ciclo)',
    'Corri Shadowing Dia 3 mini-competencia O lo OMITI LIMPIO por tiempo (sin reasignar)',
    'Error Paper EXPANDIDO (6 errores, 1 por cluster) ANONIMO + entregado FISICAMENTE con la guia',
    'En libreta personal anote 3 errores con NOMBRE + cita literal + observaciones por cluster (privado coord.)',
    'Transicion calmada al examen: telefonos al frente, pupitres separados, tablero LIMPIO, sin pistas',
    'EXAMEN ESCRITO aplicado 75 min - escritura A MANO en PLUMA, sin diccionarios/notas/dispositivos',
    'Avisos de tiempo dados: 30 min, 60 min, 70 min (5 final), 75 min (pens down)',
    'Circule cada ~10 min verificando anti-fraude; no ayude con contenido',
    'EXAMEN ORAL aplicado ~30 min - temas asignados por coordinacion - sin feedback al estudiante',
    'Cumpli tiempos del examen como SAGRADOS (no acorte el examen para alargar mastery)',
    'CIERRE DEL NIVEL: Tarjeta de Crecimiento de Caracter entregada (1 por estudiante) + 2 min de escritura',
    'FOTO GRUPAL tomada con camara del salon (NO la del profesor)',
    'ENTREGA FISICA a coordinacion: examenes escritos + hoja oral + papel errores + tarjetas + portafolios + listas NO presentados',
    'Cierre verbal: "A2 is closed. Plan the verb. Match the subject. Place the word."',
    'NO acepte la excusa "no me da tiempo" en Tarea Check (es la ultima clase, no hay otra oportunidad)',
    'NO anuncie B1 (la coordinacion decide cuando y con que cohorte arranca)',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class28_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 28 de 28 | ULTIMA - MASTERY INTEGRADO + EXAMEN FINAL A2',
    'ULTIMA CLASE DEL NIVEL A2 4h. ESTRUCTURA DOBLE: (1) primeras 2h = MASTERY INTEGRADO de los 6 clusters del arco Cl 22-27 (tiempos / comparacion+ger-inf / phrasal+pasiva / preguntas-aux+orden / preposiciones+art-cuant / 3a-s+there+causativo) + simulacion integrada "The Handover Briefing" + Shadowing Dia 3 mini-competencia (cierre del ciclo) + cierre del arco; (2) ultimas 2h = EXAMEN FINAL A2 (escrito 75 min + oral ~30 min + cierre 10 min). El A2 Book termino en M44, NO hay modulo nuevo - mastery integra lo trabajado Cl 22-27. Contenido y rubrica del examen = COORDINACION (profesor solo aplica/recolecta/entrega). Anti-fraude: a mano, sin dispositivos, oral en vivo. Cierre: Tarjeta de Crecimiento de Caracter + foto grupal + entrega fisica de examenes y portafolios. FRASE DEL DIA (ULTIMO dia del ritual A2 4h): "Plan the verb. Match the subject. Place the word. That\'s A2 ready for B1." Virtud TEMPLANZA v2 dia 3 (Cl 26-28 parcial - nivel termina).',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class28_REPORTE.pdf')

print('\n2 PDFs generados para viernes 29/05 A2 INTENSIVO 4h AM Cl 28 (ULTIMA del nivel):')
print('  - A2/A2_4h_Class28_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class28_REPORTE.pdf')
