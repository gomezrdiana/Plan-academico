#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera guias + reportes estaticos del B1 MASTERY 4h AM Cl 22 (jueves 28/05/2026):
DIA DE MIDTERM PRESENTATION — NO MODULO NUEVO HOY.

- Bloque 1 CONV (Danna, va PRIMERO): preparacion final del midterm + warm-up
  integrador (comparativos + superlativos + medidas + cantidades) + VATS
  PRUDENCIA dia 2 (v2) + presentaciones del SUBGRUPO A (3 estudiantes
  tentativo x 5 min pitch + 3-5 min Q&A) + Q&A grupal expandido + Error
  Paper Live anonimo + PASE a Juan Diego con observaciones tecnicas del
  subgrupo A + recoleccion de pages 16-20 y tarjetas + Frase del Dia.

- Bloque 2 GRAMMAR (Juan Diego, va SEGUNDO, ~85% DE PIE): Mystery breve +
  Frase del Dia (misma del dia) + VATS PRUDENCIA dia 2 breve + preparacion
  final del subgrupo B + recepcion del PASE de Danna + presentaciones del
  SUBGRUPO B (3 estudiantes tentativo) + Q&A grupal expandido + aplicacion
  oral consolidatoria breve de M28-M30 (sin nuevo contenido) + PASE a Danna
  + tarea ligera para Cl 23 + anuncio Cl 23 M32 + cierre + foto grupal
  post-midterm + entrega CONJUNTA con Danna a coordinacion.

NO-NEGOCIABLES HOY:
- NO modulo nuevo del A2 Book (midterm consume el dia).
- NO se enseña gramatica nueva — solo se RECICLA M28 (Cl 19), M29 (Cl 20)
  y M30 (Cl 21) si hay tiempo.
- NO Tarea pesada (midterm reemplaza la tarea); tarea ligera 20-25 min al
  cierre Grammar para viernes Cl 23.
- Page 21 (post-midterm reflection) arranca el VIERNES Cl 23, NO hoy.
- Profesores NUNCA comunican nota / criterio / rubrica / resultado del
  midterm — exclusivo coordinacion (Diana). Solo aplauso + "thank you".
- Entrega FISICA conjunta Danna+Juan Diego a coordinacion al cierre del
  dia: pages 16-20 escritas + tarjetas de 5 palabras + ambos PASES + ambos
  reportes impresos + video de cada presentacion.
- Frase del Dia UNICA del dia (compartida Conv+Grammar): "Today I show what
  I really built: the words I learned, the strength I named, the resources
  I really have. Prudence is presenting what is true, not what is shiny."
- VIRTUD: PRUDENCIA dia 2 (v2). Bloque PRUDENCIA v2 = Cl 21-25.
- Cl 23 viernes (29/05): post-midterm Conv + Grammar arranca M32 "How Many
  People Are There?" (M31 NO existe en A2 Book — el libro salta de M30 a
  M32 — confirmar verbatim antes de Cl 23). PRUDENCIA dia 3 (v2) manana.

SUPUESTOS VISIBLES:
- Split del cohorte en subgrupo A (manana) y B (tarde) lo define
  coordinacion previamente. Si no hay lista, distribuir 50/50 al azar y
  anotar.
- N estudiantes B1 = 6 (3+3 split estandar). Si N != 6, ajustar segun bloque
  7 de cada guia (Q&A grupal expandido / cuarta presentacion).
- Pages 16-20 escritas en Cl 16-20 (Page 16 abierta como SUPUESTO si no
  documentada; resto: Page 17 Cl 18, Page 18 Cl 19, Page 19 Cl 20 [segun
  mapa], Page 20 Cl 21 [segun mapa]).

SIN GoldList (eliminado 14/05/2026). Reportes ESTATICOS (se llenan a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_DIR = os.path.join(D, 'B1')
B1_REP = os.path.join(B1_DIR, 'reportes')
os.makedirs(B1_REP, exist_ok=True)

# ============================================================
# B1 Cl 22 CONV (Danna) - MIDTERM DIA - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase22_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase22_CONV_GUIA.pdf'),
)
print('OK: B1_Clase22_CONV_GUIA.pdf')

b1_c22_c_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 21 - ensayo midterm + Page 20)', '5 min'),
    ('EL POR QUE DE HOY (MIDTERM DAY)', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS PRUDENCIA dia 2 (v2) hilada al acto de presentar honestamente', '7 min'),
    ('PREPARACION FINAL DEL MIDTERM (warm-up integrador comparativos+superlativos+medidas+cantidades + respiracion + tarjeta 5 palabras + hospitalidad cohorte)', '17 min'),
    ('PRESENTACIONES SUBGRUPO A (3 estudiantes tentativo x 5 min pitch + 3-5 min Q&A + aplauso = ~10 min cada uno)', '30 min'),
    ('Continuacion subgrupo A (4to si lo hay) O Q&A GRUPAL EXPANDIDO + comentarios del cohorte sobre CLARIDAD/CONTENIDO/NARRATIVA (NO sobre nota)', '30 min'),
    ('ERROR PAPER LIVE anonimo de español-influenced cosechado de las presentaciones (sin nombres)', '10 min'),
    ('PASE a Juan Diego con observaciones tecnicas subgrupo A + recoleccion parcial de tarjetas + Cierre + anuncio: subgrupo B esta tarde', '5 min'),
]
b1_c22_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (tarea Cl 21)',
    'Foto del tablero - Frase del Dia + Warm-Up Chain ROUND 1-5',
    'VIDEO de cada presentacion del subgrupo A (consentimiento ya en contrato)',
    'FOTO grupal post-presentaciones subgrupo A',
    'Pages 16-20 escritas fisicamente del subgrupo A (RECOGIDAS)',
    'Tarjetas de 5 palabras del subgrupo A (RECOGIDAS)',
    'PASE ESCRITO a Juan Diego (foto antes de entregar)',
    'Papel errores fisico (anonimo)',
    'Libreta personal: por cada presentador -> nombre, tiempo real pitch, tiempo Q&A, estructura cubierta (Pages 16-20), 3 errores literales con NOMBRE, 1 fortaleza concreta',
    'Lista de quienes NO entregaron tarea Cl 21 (con NOMBRE)',
    'Lista de quienes NO entregaron Pages 16-20 al cierre (con NOMBRE)',
    'Cuantas veces inserte la Frase del Dia naturalmente (minimo 3)',
    'CONFIRME que NUNCA comunique nota / criterio / rubrica / resultado del midterm',
    'CONFIRME anuncio Cl 23 viernes = post-midterm + arranque M32 "How Many People Are There?" (M31 no existe)',
]
b1_c22_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad (cronometro firme, aplauso limpio, sin titubeo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PREPARE el cronometro visible al frente (5 min pitch + 3-5 min Q&A)',
    'PREPARE camara/telefono para grabar cada presentacion',
    'PREPARE carpeta fisica para recoger pages 16-20 + tarjetas',
    'CONFIRME con coordinacion el split del subgrupo A previamente (o distribui 50/50 y anote)',
    'PRESENTE Frase del Dia con coro 3x al inicio',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NUNCA comunique nada de evaluaciones / midterm / nota / criterio / resultado / rubrica - SOLO aplauso y "thank you" - exclusivo coordinacion',
    'Si alguien pregunto por nota: redirigui "Coordination handles results, not me."',
    'NO compare estudiantes en voz alta',
    'NO permite preguntas evaluativas de la audiencia (redirigi)',
    'Verifique virtud CL 22 = PRUDENCIA dia 2 v2 (por numero de clase, bloque Cl 21-25)',
    'Hile PRUDENCIA dia 2 en VATS como dia del bloque (presentar lo verdadero, no inflar, no esconder)',
    'NO ensene gramatica nueva (es midterm day)',
    'NO use texto Heiiu (Pages 16-20 escritas en clases anteriores son el "texto")',
    'Conduje warm-up integrador en cadena (comparativos + superlativos + medidas + cantidades + ROUND 1-5)',
    'Conduje respiracion 4-4-6 + tarjeta 5 palabras + hospitalidad del cohorte',
    'Cronometre cada presentacion (5 min pitch + 3-5 min Q&A) con cronometro visible',
    'Grabe cada presentacion del subgrupo A',
    'Anote PRIVADAMENTE en libreta por presentador: nombre, tiempo real, pages cubiertas, 3 errores literales con NOMBRE, 1 fortaleza concreta',
    'En cada Q&A hice 1 pregunta honesta de CONTENIDO (no evaluativa)',
    'Aplaudi + "thank you" al cierre de cada presentacion (sin mas comentario)',
    'Conduje Q&A grupal expandido sobre CLARIDAD/CONTENIDO/NARRATIVA (nunca nota)',
    'Conduje ERROR PAPER LIVE anonimo (sin nombres en tablero; nombres en libreta personal)',
    'ESCRIBI el PASE a Juan Diego con observaciones tecnicas del subgrupo A + tipo de error mas comun',
    'ENTREGUE FISICAMENTE el PASE a Juan Diego antes de su clase',
    'RECOGI pages 16-20 escritas + tarjetas de 5 palabras del subgrupo A',
    'CONTE entregas y anote quien no entrego (libreta - coordinacion)',
    'NO hay Tarea hoy (midterm la reemplaza); anuncie que la tarea ligera la pone Juan Diego al cierre del dia',
    'Anuncie Cl 23 viernes = post-midterm Conv (Page 21 reflection) + Grammar M32 "How Many People Are There?" como hecho de cronograma SOLO',
    'PRUDENCIA dia 3 v2 anunciada para manana',
    'Estudiantes (presentadores) hablaron 80%+ del tiempo durante sus pitches/Q&A',
    'CONFIRME entrega CONJUNTA con Juan Diego a coordinacion al cierre del dia (mi carpeta subgrupo A + su carpeta subgrupo B + ambos PASES + ambos reportes + videos)',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase22_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 22 de 44 | BLOQUE 1: CONV (HOY VA PRIMERO) | MIDTERM PRESENTATION DAY | FRASE DEL DIA (Goldlist retirado)',
    'DIA DE MIDTERM PRESENTATION - NO MODULO NUEVO. Preparacion final + VATS PRUDENCIA dia 2 (v2) + presentaciones del subgrupo A (3 estudiantes tentativo x 5 min pitch + 3-5 min Q&A) + Q&A grupal expandido (CLARIDAD/CONTENIDO/NARRATIVA - nunca nota) + Error Paper Live anonimo + PASE a Juan Diego + recoleccion fisica de pages 16-20 + tarjetas + FRASE DEL DIA unica del dia + PRUDENCIA dia 2 v2. Profesora NUNCA comunica nota/criterio/rubrica/resultado - solo aplauso y "thank you" - exclusivo coordinacion. Anuncio Cl 23 viernes = post-midterm + M32 (M31 no existe).',
    b1_c22_c_act, b1_c22_c_deliv, b1_c22_c_eval, S,
)
print('OK: B1_Clase22_CONV_REPORTE.pdf')

# ============================================================
# B1 Cl 22 GRAMMAR (Juan Diego) - MIDTERM DIA - GUIA + REPORTE  (~85% DE PIE)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase22_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase22_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase22_GRAMMAR_GUIA.pdf')

b1_c22_g_act = [
    ('MYSTERY CHECK breve (Frase del Dia Cl 21 de memoria) - DE PIE', '4 min'),
    ('EL POR QUE DE HOY (continua midterm)', '2 min'),
    ('FRASE DEL DIA - presentacion (misma del dia) - DE PIE', '4 min'),
    ('VATS PRUDENCIA dia 2 (v2) - DE PIE breve', '5 min'),
    ('PREPARACION FINAL subgrupo B + recepcion PASE de Danna (warm-up integrador comprimido + respiracion + tarjeta + hospitalidad)', '10 min'),
    ('PRESENTACIONES SUBGRUPO B (3 estudiantes tentativo x 5 min pitch + 3-5 min Q&A + aplauso = ~10 min cada uno)', '30 min'),
    ('Q&A GRUPAL EXPANDIDO + COMENTARIOS DEL COHORTE sobre claridad/contenido/narrativa (NO sobre nota) - dia completo (subgrupos A+B)', '30 min'),
    ('APLICACION ORAL CONSOLIDATORIA breve de M28-M30 (superlativos + medidas + cantidades) - sin nuevo contenido; se OMITE si tiempo se comio', '15 min'),
    ('PASE a Danna + Tarea ligera Cl 23 + Anuncio Cl 23 M32 (M31 no existe)', '5 min'),
    ('Cierre + foto grupal post-midterm (cohorte completo) + recoleccion subgrupo B + ENTREGA CONJUNTA con Danna a coordinacion', '5 min'),
]
b1_c22_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery breve',
    'Foto del tablero - Frase del Dia + Warm-Up Chain ROUND 1-4',
    'VIDEO de cada presentacion del subgrupo B (consentimiento ya en contrato)',
    'FOTO grupal post-midterm (cohorte completo, ambos subgrupos)',
    'Pages 16-20 escritas fisicamente del subgrupo B (RECOGIDAS)',
    'Tarjetas de 5 palabras del subgrupo B (RECOGIDAS)',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar)',
    'Papel errores fisico (anonimo) - si se hizo bloque 8',
    'Libreta personal: por cada presentador -> nombre, tiempo real pitch, tiempo Q&A, estructura cubierta (Pages 16-20), 3 errores literales con NOMBRE, 1 fortaleza concreta',
    'Lista de quienes NO trajeron Frase del Dia Cl 21 (con NOMBRE)',
    'Lista de quienes NO entregaron Pages 16-20 al cierre (con NOMBRE)',
    'Cuantas veces inserte la Frase del Dia naturalmente (minimo 3)',
    'Notas sobre que % del bloque fue realmente DE PIE (objetivo ~85%)',
    'CONFIRME que NUNCA comunique nota / criterio / rubrica / resultado del midterm',
    'CONFIRME anuncio Cl 23 viernes = post-midterm + arranque M32 "How Many People Are There?" (M31 no existe)',
    'ENTREGA CONJUNTA con Danna realizada al cierre del dia (mi carpeta subgrupo B + su carpeta subgrupo A + ambos PASES + ambos reportes + videos)',
]
b1_c22_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad (cronometro firme, aplauso limpio, sin titubeo)',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'PREPARE el SOBRE del Mystery Check breve ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase (misma del dia)',
    'PREPARE el cronometro visible al frente (5 min pitch + 3-5 min Q&A)',
    'PREPARE camara/telefono para grabar cada presentacion',
    'PREPARE carpeta fisica para recoger pages 16-20 + tarjetas del subgrupo B',
    'PREPARE carpeta CONJUNTA con Danna para entrega a coordinacion al cierre del dia',
    'CONFIRME con coordinacion el split del subgrupo B previamente (o el split que Danna anoto si no habia lista)',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE la Frase del Dia 3+ veces NATURALMENTE durante clase',
    'Lei en voz alta los 3 errores del PASE de Danna (sin nombres) para el subgrupo B como gift',
    'NO use GoldList ni mencione Lista (ritual cerrado)',
    'NUNCA comunique nada de evaluaciones / midterm / nota / criterio / resultado / rubrica - SOLO aplauso y "thank you" - exclusivo coordinacion',
    'Si alguien pregunto por nota: redirigui "Coordination handles results, not me."',
    'NO compare estudiantes en voz alta (ni con subgrupo A)',
    'NO permite preguntas evaluativas de la audiencia (redirigi)',
    'Verifique virtud CL 22 = PRUDENCIA dia 2 v2 (por numero de clase, bloque Cl 21-25)',
    'Hile PRUDENCIA dia 2 en VATS DE PIE breve (presentar lo verdadero, no inflar, no esconder)',
    'NO ensene gramatica nueva HOY (midterm day; NO M32 -> es Cl 23 viernes; NO re-enseno M28 ni M29 ni M30)',
    'NO use texto Heiiu (Pages 16-20 escritas en clases anteriores son el "texto")',
    'Conduje warm-up integrador comprimido en cadena (ROUND 1-4: equal/unequal comparative + superlative + measurement + quantity)',
    'Conduje respiracion 4-4-6 + tarjeta 5 palabras + hospitalidad del cohorte',
    'Cronometre cada presentacion (5 min pitch + 3-5 min Q&A) con cronometro visible',
    'Grabe cada presentacion del subgrupo B',
    'Anote PRIVADAMENTE en libreta por presentador: nombre, tiempo real, pages cubiertas, 3 errores literales con NOMBRE, 1 fortaleza concreta',
    'En cada Q&A hice 1 pregunta honesta de CONTENIDO (no evaluativa)',
    'Aplaudi + "thank you" al cierre de cada presentacion (sin mas comentario)',
    'Conduje Q&A grupal expandido sobre CLARIDAD/CONTENIDO/NARRATIVA (nunca nota) - dia completo (subgrupos A+B)',
    'Si tiempo permitio: conduje aplicacion oral consolidatoria breve M28-M30 SIN nuevo contenido (drill superlativo + drill medida/cantidad reciclados de los pitches)',
    'Si tiempo NO permitio: OMITI el bloque 8 limpio y prioritice cierre + entrega fisica',
    'MANTUVE el bloque ~70%+ DE PIE / U-shape (objetivo ~85%)',
    'ESCRIBI el PASE a Danna con 3 errores literales subgrupo B + tipo de error mas comun + nota para Cl 23 viernes (Page 21 reflection + M32)',
    'En Tarea LIGERA explique el por que + due date explicito (viernes 29/05 antes 7PM, 20-25 min - midterm reemplazo tarea pesada)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie siguiente modulo existente del A2 Book para Cl 23 viernes: M32 "How Many People Are There?" (M31 NO existe; el libro salta de M30 a M32; confirmar verbatim antes de clase)',
    'CONFIRME M31 NO existe en el A2 Book (patron: M19/M25/M31 no existen)',
    'Anuncie PRUDENCIA dia 3 (v2) para manana',
    'Tome foto grupal post-midterm del cohorte completo (ambos subgrupos)',
    'RECOGI pages 16-20 escritas + tarjetas de 5 palabras del subgrupo B',
    'CONTE entregas y anote quien no entrego (libreta - coordinacion)',
    'ENTREGA CONJUNTA con Danna a coordinacion al cierre del dia (mi carpeta subgrupo B + su carpeta subgrupo A + ambos PASES + ambos reportes + videos)',
    'Estudiantes (presentadores) hablaron 80%+ del tiempo durante sus pitches/Q&A',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase22_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 22 de 44 | BLOQUE 2: GRAMMAR (HOY VA SEGUNDO, ~85% DE PIE) | MIDTERM PRESENTATION DAY | NO MODULO NUEVO',
    'DIA DE MIDTERM PRESENTATION - NO MODULO NUEVO. Preparacion final subgrupo B + recepcion PASE de Danna + presentaciones del subgrupo B (3 estudiantes tentativo x 5 min pitch + 3-5 min Q&A) + Q&A grupal expandido dia completo + aplicacion oral consolidatoria breve M28-M30 sin nuevo contenido (se omite si tiempo se comio) + PASE a Danna + tarea ligera Cl 23 + foto grupal post-midterm + ENTREGA CONJUNTA con Danna a coordinacion + FRASE DEL DIA unica del dia + PRUDENCIA dia 2 v2. Profesor NUNCA comunica nota/criterio/rubrica/resultado - solo aplauso y "thank you" - exclusivo coordinacion. Cl 23 viernes = post-midterm Conv + Grammar arranca M32 "How Many People Are There?" (M31 NO existe en A2 Book - el libro salta de M30 a M32).',
    b1_c22_g_act, b1_c22_g_deliv, b1_c22_g_eval, S,
)
print('OK: B1_Clase22_GRAMMAR_REPORTE.pdf')

print('\n4 PDFs generados para jueves 28/05 B1 MASTERY Cl 22 (MIDTERM PRESENTATION DAY):')
print('  - B1/B1_Clase22_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase22_CONV_REPORTE.pdf')
print('  - B1/B1_Clase22_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase22_GRAMMAR_REPORTE.pdf')
