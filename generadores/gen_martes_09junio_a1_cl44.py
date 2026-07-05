#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 44 (martes 09/06/2026):
- REPASO FINAL pre-Final + Simulacro completo formato Final + Cierre emocional
  pre-examen + SINTESIS dia 4. ULTIMA clase del nivel antes del Examen Final.
- 3 bloques mayores: (Bloque 6) repaso integrado por 3 estaciones rotativas
  - gramatica los 3 tiempos / vocabulario M1-M35 / speaking corto cotidiano,
  8 min c/u. (Bloque 7) simulacro completo formato Final 15 items: 18 min
  silencio + 5 min autocorreccion con KEY + 5 min dudas criticas. MISMO formato
  Cl 41/42 (reciclar hoja KEY). NO se anuncia puntaje. (Bloque 10) cierre
  emocional pre-Final: reconocimiento individual breve + "3 cosas que me llevo
  del nivel" en parejas + 2-3 voluntarios + tarea minimalista + anuncio Cl 45
  Final + "see you Friday - rest your voice".
- Virtud: SINTESIS dia 4 (Cl 41-45 = SINTESIS las 4 virtudes integradas -
  Prudencia para elegir palabras, Templanza para respirar, Justicia para
  escuchar, Fortaleza para terminar). Verificado en CALENDARIO_VIRTUDES_2026.md
  "A1 NOCTURNO 2H".
- Frase del Dia: "Friday I show what 10 weeks of work made me - Prudence to
  choose my words, Temperance to breathe, Justice to listen, Fortitude to
  finish. The Final is the celebration, not the test." (Reframe: Final =
  celebracion, no prueba; baja ansiedad pre-examen.)
- A1 Book TERMINO en M35 (pag 416). Cl 34-44 = consolidacion integrada hacia
  Examen Final (Cl 45). HOY Cl 44 = ENSAYO + CIERRE EMOCIONAL, NO evaluacion.
- DECISION DIANA 31/05/2026: este dia NO genera archivo _MARKER separado. El
  simulacro esta integrado como Bloque 7 - es ensayo del Final, NO el Final.
- Profesor Christian, cohorte 6, asistencia 50-67%. SIN GoldList. Reporte
  estatico (se llena a mano). Tarea pre-Final due jueves 11/06 antes 7 PM,
  15-20 min MAX, NO fragmentada, NO extendida (voz debe descansar):
  (a) 10 min repaso UNA vez del propio miniproyecto pulido + (b) 10 min
  habitos de descanso de voz + hidratacion.
- Profesor SOLO anuncia Cl 45 viernes 12/06 = EXAMEN FINAL (ultimas 2h del
  nivel, regla firme Diana 22/05/2026) como hecho de calendario. NO discute
  criterios/notas/rubrica/puntaje/formato/peso de Miniproyectos Cl 43 ni del
  Final escrito (exclusivo coordinacion).
- Rol del profesor HOY: facilitador de repaso + cronometro silencioso en el
  simulacro + guia del cierre emocional sin paternalismo. NO juez. NO comunica
  resultados. NO compara. NO anuncia puntaje individual ni grupal.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class44_PRINT.md'), os.path.join(A1_DIR, 'A1_Class44_GUIA.pdf'))
print('OK: A1_Class44_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (post-Miniproyectos Cl 43: como se sintieron + descanso de voz / chequea tarea Cl 44 = 3 frases reflexion + grabacion 2 min de voz)', '5 min'),
    ('EL POR QUE DE HOY', '3 min'),
    ('FRASE DEL DIA - presentacion ("Friday I show what 10 weeks made me - the Final is the celebration, not the test")', '4 min'),
    ('VATS (SINTESIS dia 4 - 4 virtudes ya integradas + UNA accion concreta entre hoy y viernes para prepararlas)', '6 min'),
    ('PEER TEACHER SLOT (1 error RECURRENTE del nivel Cl 41-43 - ultima correccion publica del nivel)', '7 min'),
    ('REPASO INTEGRADO POR 3 ESTACIONES rotativas 8 min c/u: (A) gramatica los 3 tiempos / (B) vocabulario M1-M35 / (C) speaking corto cotidiano - DE PIE estaciones', '25 min'),
    ('SIMULACRO COMPLETO FORMATO FINAL: 15 items escritos en silencio 18 min + autocorreccion con KEY 5 min + dudas criticas 5 min (MISMO formato Cl 41/42 - reciclar KEY - NO se anuncia puntaje, ES ENSAYO no examen)', '28 min'),
    ('SHADOWING corto suave (descanso de voz pre-Final - voz a media potencia, no proyeccion)', '10 min'),
    ('ERROR PAPER LIVE (errores tipicos del simulacro de hoy, anonimos en tablero) + Frase del Dia CIERRE (1 estudiante de memoria + 1 la adapta a su Final del viernes)', '8 min'),
    ('CIERRE EMOCIONAL PRE-FINAL: reconocimiento individual breve factual (3 min) + "3 cosas que me llevo del nivel" en parejas 90 seg c/u (3 min) + 2-3 voluntarios comparten al grupo (4 min) + anuncio Cl 45 Final como hecho de calendario (1 min) + tarea pre-Final minimalista (2 min) + cierre "see you Friday - rest your voice" (1 min)', '14 min'),
]
a1_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + 3 estaciones + Errores + 3 cosas que me llevo',
    'Foto/video PEER TEACHER (ultima correccion publica del nivel)',
    'Foto/video de las 3 estaciones rotando',
    'Foto del simulacro en silencio + KEY entregada',
    'Foto/video Shadowing corto suave (descanso de voz)',
    'Foto/video Error Paper Live + Frase del Dia CIERRE',
    'Foto/video del cierre emocional ("3 cosas que me llevo" en parejas + voluntarios)',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 44 (con NOMBRE)',
    'LIBRETA PERSONAL CENTRAL HOY: dudas recurrentes del simulacro de hoy + errores literales por estudiante en las 3 estaciones + estado emocional post-Miniproyectos por estudiante (esto es lo central para coordinacion hoy - datos que coordinacion necesita ANTES del Final)',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmaste anuncio Cl 45 viernes 12/06 = EXAMEN FINAL (hecho de calendario SOLO, sin criterios/notas)',
    'Confirmaste que NO comunicaste criterios/notas/rubrica/puntaje/formato/peso de Miniproyectos NI del Final',
    'Confirmaste que tarea pre-Final es MAX 20 min (voz debe descansar) y due jueves 11/06 antes 7 PM',
]
a1_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea como se sintieron en Miniproyectos Cl 43 + descanso de voz)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x y subraye reframe "Final = celebracion, no prueba"',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE durante clase (objetivo 4 inserciones marcadas)',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la adapto a su Final del viernes',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 44 = SINTESIS dia 4 (Cl 41-45 = SINTESIS las 4 integradas)',
    'Hile SINTESIS dia 4 en VATS: una accion concreta entre hoy y viernes para que las 4 virtudes esten LISTAS en el Final (preparacion + descanso)',
    'CONFIRME que el A1 Book termino en M35 (no hay modulo nuevo - HOY es REPASO + SIMULACRO + CIERRE)',
    'CONFIRME que este dia NO genera archivo _MARKER separado (decision Diana 31/05/2026: simulacro integrado como Bloque 7, es ensayo, NO es el Final)',
    'PREPARE 3 estaciones (A gramatica los 3 tiempos / B vocabulario M1-M35 / C speaking corto) antes de clase en cartulinas/papeles',
    'CRONOMETRO visible 8 min por estacion + 1 min transicion en Bloque 6',
    'IMPRIMI hoja simulacro 15 items formato Final + hoja KEY antes de clase (reciclar de Cl 41/42 - MISMO formato)',
    'CRONOMETRO visible 18 min silencio absoluto + 5 min autocorreccion KEY + 5 min dudas criticas en Bloque 7',
    'NO AYUDE / NO TRADUJE / NO CORREGI / NO COMENTE durante los 18 min de silencio del simulacro',
    'NO ANUNCIE puntaje individual ni grupal del simulacro (es ENSAYO, no examen)',
    'NO COMPARE puntajes entre estudiantes',
    'NO COMUNIQUE criterios/notas/rubrica/puntaje de Miniproyectos Cl 43 (esa info es de coordinacion)',
    'NO COMUNIQUE criterios/notas/rubrica/puntaje/formato/peso del Final Cl 45 (esa info es de coordinacion)',
    'Si alguien pregunto por criterios/notas/resultados, redirigi: "Coordination handles results - not me. Today you rehearse, you rest your voice, you sleep well." y segui',
    'Si alguien NO se sintio bien post-Miniproyectos NO procese emocionalmente en publico - una sola frase ("That is real. Coordination will follow up.") + a libreta personal con NOMBRE',
    'Conduje SHADOWING corto y SUAVE (voz a media potencia, no proyeccion, descanso pre-Final)',
    'Conduje ERROR PAPER LIVE con errores anonimos del simulacro de hoy (NO atribuibles a estudiante especifico - NO use este momento para "advertir" sobre el Final)',
    'Camine con papel errores anonimo',
    'Conduje RECONOCIMIENTO INDIVIDUAL BREVE FACTUAL (ayer 4 min en ingles, hoy 15 items en silencio, 10 semanas) - SIN paternalismo, SIN "estoy orgulloso", SIN "los voy a extranar"',
    'Facilite "3 cosas que me llevo del nivel" en parejas (1 lenguaje + 1 yo mismo + 1 grupo) 90 seg c/u',
    '2-3 voluntarios compartieron al grupo (NO obligue, NO cerre con "wow", solo aplauso corto + "Thank you")',
    'En Tarea pre-Final explique pedagogicamente el por que + due date explicito (JUEVES 11/06 antes 7 PM)',
    'Tarea pre-Final es MAX 15-20 min (NO fragmentada, NO extendida): 10 min repaso UNA vez del propio miniproyecto + 10 min habitos descanso de voz / hidratacion',
    'NO acepte la excusa "no me da tiempo" (15-20 min en 3 dias)',
    'EXPLIQUE que la tarea es CORTA deliberadamente porque la voz DEBE descansar para el viernes (NO porque sea menos importante)',
    'Anuncie Cl 45 viernes 12/06 = EXAMEN FINAL (ultimas 2h del nivel - regla firme) como HECHO DE CALENDARIO SOLO (sin nota, sin criterios, sin formato, sin peso - exclusivo coordinacion)',
    'Cierre seco y factual (NO drama, NO "se acabo el nivel", NO "fue un placer", NO "los voy a extranar" - el nivel se cierra viernes Cl 45, hoy se cierra el ENSAYO)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(
    os.path.join(A1_REP, 'A1_Class44_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 44 de 45 | REPASO FINAL pre-Final + Simulacro completo formato Final + Cierre emocional pre-examen | SINTESIS dia 4 | FRASE DEL DIA (GoldList retirado)',
    'REPASO FINAL pre-Final + simulacro completo formato Final + cierre emocional pre-examen. 3 bloques mayores: (B6 25min) repaso integrado 3 estaciones rotativas 8 min c/u - A gramatica los 3 tiempos / B vocabulario M1-M35 / C speaking corto cotidiano. (B7 28min) SIMULACRO COMPLETO FORMATO FINAL 15 items - 18 min silencio absoluto + 5 min autocorreccion con KEY + 5 min dudas criticas (MISMO formato Cl 41/42, reciclar KEY, NO se anuncia puntaje, ES ENSAYO no examen). (B10 14min) CIERRE EMOCIONAL pre-Final - reconocimiento individual breve factual + "3 cosas que me llevo del nivel" en parejas + 2-3 voluntarios + tarea pre-Final minimalista + anuncio Cl 45 Final como hecho de calendario + "see you Friday - rest your voice". Andamiaje: Mystery (post-Miniproyectos + descanso de voz) + Frase del Dia ("Friday I show what 10 weeks made me - the Final is the celebration, not the test") + VATS SINTESIS dia 4 (una accion concreta entre hoy y viernes) + Peer Teacher (1 error RECURRENTE del nivel - ultima correccion publica). Profesor cronometra SILENCIOSO en simulacro, NO ayuda/NO corrige/NO comenta/NO anuncia puntaje. Profesor NO comunica criterios/notas/rubrica/puntaje/formato/peso de Miniproyectos NI del Final (exclusivo coordinacion). Tarea pre-Final MAX 15-20 min due jueves 11/06 antes 7 PM (NO fragmentada, NO extendida - voz debe descansar): 10 min repaso UNA vez del propio miniproyecto + 10 min habitos descanso de voz/hidratacion. Cl 45 viernes 12/06 = EXAMEN FINAL (ultimas 2h del nivel - regla firme Diana 22/05/2026) - HECHO DE CALENDARIO SOLO. (A1 Book termino en M35 - Cl 34-44 = consolidacion integrada hacia Final Cl 45; NO archivo _MARKER separado - decision Diana 31/05/2026: simulacro integrado como Bloque 7, es ensayo del Final, NO es el Final)',
    a1_act, a1_deliv, a1_eval, S,
)
print('OK: A1_Class44_REPORTE.pdf')

print('\n2 PDFs generados para martes 09/06 A1 Nocturno Cl 44:')
print('  - A1/A1_Class44_GUIA.pdf')
print('  - A1/reportes/A1_Class44_REPORTE.pdf')
