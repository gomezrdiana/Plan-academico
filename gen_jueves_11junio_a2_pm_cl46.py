#!/usr/bin/env python3
"""Genera la guia + reporte del A2 PM Nocturno Cl 46 (jueves 11/06/2026):
- ARCO DE REPASO DE ERRORES COMUNES - CLUSTER 5: PREPOSICIONES + ARTICULOS/CUANTIFICADORES
  (in/on/at en tiempo y lugar / a, an, the, 0 segun primera mencion, especifico o general /
   much incontable / many plural contable / a lot of, few/little, some/any + there is/are)
- El A2 Book termino en M44 (pag 352); Cl 41 cerro el libro;
  Cl 42 abrio el arco (tiempos); Cl 43 corrigio comparativos/superlativos + gerundio vs infinitivo;
  Cl 44 corrigio phrasal verbs + voz pasiva;
  Cl 45 corrigio preguntas/negativos/auxiliares + orden de palabras.
  Cl 46 = quinto cluster del arco de repaso A2->B1.
- FRASE DEL DIA + virtud TEMPLANZA v3 dia 1 APERTURA del bloque (Cl 46-50 = TEMPLANZA v3).
- ANUNCIO EXPLICITO en VATS y cierre: hoy ABRE TEMPLANZA v3 (ayer Cl 45 cerro PRUDENCIA v3).
- Error Paper EXPANDIDO (6 errores: 2 preposiciones + 2 articulos + 2 cuantificadores).
- Tarea 20-30 min, due viernes 12/06 antes 7:00 PM, NO fragmentada.
- Anuncio Cl 47 (vie 12/06): arco clase 6 = concordancia / 3a persona -s + there is/are + causativo
  + TEMPLANZA v3 dia 2.
- SIN GoldList. Sin nombres. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class46_PRINT.md'), os.path.join(A2_DIR, 'A2_Class46_GUIA.pdf'))
print('OK: A2_Class46_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 45 - cluster 4: preguntas + negativos + orden palabras)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (TEMPLANZA v3 dia 1 APERTURA + cierre del bloque PRUDENCIA v3)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de preposicion de tiempo: "in Monday" / "on June" / "in 8 PM")', '7 min'),
    ('CORRECCION SISTEMATICA A - PREPOSICIONES (in/on/at - tiempo + lugar)', '13 min'),
    ('CORRECCION SISTEMATICA B - ARTICULOS (a/an primera mencion / the especifico / 0 general)', '12 min'),
    ('CORRECCION SISTEMATICA C - CUANTIFICADORES (much incontable / many contable / a lot of / few-little / some-any + there is/are)', '14 min'),
    ('SPEED DRILL - los 3 sub-clusters en velocidad (15 items + parejas)', '12 min'),
    ('SIMULACION PROFESIONAL - The Inventory Check at the Warehouse (DE PIE, fuerza preposiciones + cuantificadores + articulos + concordancia)', '16 min'),
    ('SHADOWING (verificar dia del ciclo)', '8 min'),
    ('Error Paper EXPANDIDO (6 errores: 2 preposiciones + 2 articulos + 2 cuantificadores) + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + ANUNCIO Cl 47 (cluster 6: concordancia/3a persona + there is/are + causativo + TEMPLANZA v3 dia 2)', '4 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Preposiciones + Articulos + Cuantificadores + Errores',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Inventory Check at the Warehouse',
    'Foto/video Shadowing',
    'Papel errores fisico (anonimo, 6 errores EXPANDIDO: 2 preposiciones + 2 articulos + 2 cuantificadores) - entregado fisicamente con la guia',
    'Lista quienes NO entregaron tarea Cl 45 (las 3 partes: 12 oraciones mixtas + audio job interview 2 min + listening 5 preguntas + 5 negativos)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmacion de que ANUNCIASTE explicitamente Cl 46 = TEMPLANZA v3 dia 1 APERTURA (en VATS y en cierre)',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 45)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion (preposicion + cuantificador o articulo + preposicion)',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 46 = TEMPLANZA v3 dia 1 APERTURA (por numero de clase, Cl 46-50)',
    'Hile TEMPLANZA en VATS con medir / dosificar / no exceder ni quedarse corto',
    'ANUNCIE EXPLICITAMENTE el cierre del bloque PRUDENCIA v3 (ayer Cl 45) + apertura TEMPLANZA v3 hoy',
    'ENTENDI que HOY es la QUINTA clase del ARCO DE REPASO (Cl 46 = arco clase 5)',
    'NO invente contenido: el A2 Book termino en M44; hoy = CORRECCION sistematica de errores tipicos',
    'CORRECCION A: preposiciones (in/on/at TIEMPO: mes=in / dia=on / hora=at; LUGAR: cerrado=in / superficie=on / punto=at)',
    'CORRECCION B: articulos (a/an primera mencion singular contable / the especifico / 0 general incontable o plural)',
    'CORRECCION C: cuantificadores (much incontable / many contable / a lot of / few-little / some afirmativo - any negativo / there IS uncountable - there ARE plural)',
    'Conduje Speed Drill 15 items mezclando preposiciones (tiempo+lugar) + articulos (a/the/0) + cuantificadores (much/many/there is-are)',
    'Conduje Simulacion The Inventory Check at the Warehouse forzando preposiciones + cuantificadores + articulos + concordancia',
    'Simulacion fue PROFESIONAL (warehouse inventory o calendar coordination, supervisor pregunta + employee responde, rotacion)',
    'Conduje Shadowing del ciclo activo',
    'ERROR PAPER EXPANDIDO (6 errores: 2 preposiciones + 2 articulos + 2 cuantificadores) - anonimo en clase / libreta con nombres',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (viernes 12/06 antes 7:00 PM)',
    'Tarea 20-30 min (A2), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'ANUNCIE EXPLICITAMENTE Cl 47 = arco clase 6 (concordancia/3a persona + there is/are + causativo) + TEMPLANZA v3 dia 2',
    'APERTURA del bloque TEMPLANZA v3 marcada explicitamente como primer dia + recordatorio de cierre PRUDENCIA v3 ayer',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class46_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 46 de 55 | ARCO REPASO Cl 5 - PREPOSICIONES + ARTICULOS/CUANTIFICADORES | TEMPLANZA v3 dia 1 APERTURA | FRASE DEL DIA (Goldlist retirado)',
    'ARCO DE REPASO A2->B1 - CLUSTER 5: PREPOSICIONES + ARTICULOS/CUANTIFICADORES (in/on/at en TIEMPO: mes=in, dia=on, hora=at; en LUGAR: cerrado=in, superficie=on, punto=at / a-an primera mencion singular contable, the especifico, 0 general incontable o plural / much incontable, many plural contable, a lot of ambos, few-little, some afirmativo - any negativo, there IS uncountable - there ARE plural) + Speed Drill 3 sub-clusters + The Inventory Check at the Warehouse (o Calendar Coordination Call) + Error Paper EXPANDIDO 6 errores (2+2+2) + FRASE DEL DIA. El A2 Book termino en M44 (Cl 41 cerro); Cl 42-45 corrieron clusters 1-4; hoy Cl 46 = quinto cluster (piezas pequenas que delatan precision A2 vs B1). TEMPLANZA v3 dia 1 = APERTURA del bloque (Cl 46-50); ayer Cl 45 cerro PRUDENCIA v3. ANUNCIO EXPLICITO en VATS y cierre. Cl 47 = arco clase 6 (concordancia / 3a persona -s + there is/are + causativo) + TEMPLANZA v3 dia 2.',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class46_REPORTE.pdf')

print('\n2 PDFs generados para jueves 11/06 A2 PM Cl 46:')
print('  - A2/A2_Class46_GUIA.pdf')
print('  - A2/reportes/A2_Class46_REPORTE.pdf')
