# -*- coding: utf-8 -*-
"""HOJA DE ARRANQUE — B1 Mastery 4H, cohorte que inicia 13/10/2026. Para los dos docentes (Cristian: Gramática;
Danna: Conversación con el grupo B2 unido) y para coordinación. Complementa el SYLLABUS_B1_MASTERY_4H (que sigue vigente)
con lo específico de este arranque: orden del día, bloque mixto B1+B2, discurso del cambio, grabación de entrada,
añadidos a la Cl 1 y checklist previo. Salida: VERSION_2/B1_4H/HOJA_ARRANQUE_B1_2026-10-13.docx (+ .pdf si Word está)."""
import os, re
from docx import Document
from docx.shared import Pt, RGBColor

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
OUT = os.path.join(BASE, r'VERSION_2\B1_4H\HOJA_ARRANQUE_B1_2026-10-13.docx')
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)

d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(54); s.top_margin = s.bottom_margin = Pt(46)
def h(t, size=13):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAR
def p(t, color=None, size=10.5, after=4):
    x = d.add_paragraph(); x.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        r = x.add_run(part[2:-2] if part.startswith('**') else part); r.bold = part.startswith('**'); r.font.size = Pt(size)
        if color: r.font.color.rgb = color
def li(t): p('•  ' + t, after=2)
def check(t): p('☐  ' + t, after=2)
def caja(t):
    tb = d.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.rows[0].cells[0]
    first = True
    for ln in t.split('\n'):
        x = c.paragraphs[0] if first else c.add_paragraph(); first = False
        r = x.add_run(ln); r.font.size = Pt(10); r.italic = True
    d.add_paragraph()

p('HEIIU · B1 MASTERY 4H · COHORTE QUE INICIA EL MARTES 13 DE OCTUBRE DE 2026', GRIS, 10)
p('HOJA DE ARRANQUE — CRISTIAN (GRAMÁTICA) Y DANNA (CONVERSACIÓN)', NAR, 15)
p('Léanla completa antes del martes (15 minutos). Esta hoja complementa el SYLLABUS B1 MASTERY 4H, que sigue vigente; aquí está solo lo específico de este arranque. Lo que no esté aquí ni en la guía del día, se pregunta a coordinación: no se improvisa.', GRIS, 9.5)

h('1. Cómo funciona el día (8:00 a 12:00, lunes a viernes)')
tb = d.add_table(rows=1, cols=4); tb.style = 'Table Grid'
for j, v in enumerate(['Hora', 'Quién', 'Grupo', 'Qué']):
    r = tb.rows[0].cells[j].paragraphs[0].add_run(v); r.bold = True; r.font.size = Pt(9.5)
for row in [('8:00 – 10:00', 'Cristian', 'B1 solos', 'GRAMÁTICA — guía B1_Clase{N}_GRAMMAR del día'),
            ('8:00 – 10:00', 'Danna', 'B2 solos', 'Conversación B2 (su trabajo habitual con el grupo B2)'),
            ('10:00 – 12:00', 'Danna', 'B1 + B2 juntos', 'CONVERSACIÓN — guía B1_Clase{N}_CONV del día, para todos')]:
    c = tb.add_row().cells
    for j, v in enumerate(row):
        r = c[j].paragraphs[0].add_run(v); r.font.size = Pt(9.5); r.bold = (j == 0)
d.add_paragraph()
p('Cada docente recibe **solo la guía de su pista**, numerada del 1 al 44. El mismo número se dicta el mismo día: Gramática Cl 1 y Conversación Cl 1 el martes; Cl 2 el miércoles, y así. Festivos: no hay clase y no se corre la numeración; las clases perdidas se recuperan al final del nivel.')
p('**Una regla de lectura, porque las guías se escribieron con Conversación primero:** donde la guía de Gramática diga "lo que salió de sus bocas esta mañana", léase "ayer en Conversación"; donde la de Conversación diga "mañana en Gramática", léase "hoy a las 8 ya lo vieron". El contenido del día es el mismo en las dos pistas (la caja HOY SOLO coincide): Gramática lo pone en papel a las 8, Conversación lo pone en uso a las 10. Nada más cambia.')
p('**El PASE (3 líneas por el grupo de docentes, obligatorio):** Cristian → Danna a las 10:00, antes de que ella abra ("esto sellamos, esto quedó frágil"); Danna → Cristian al cerrar las 12:00 ("esto salió hablado, estos 3 errores se repiten, esto quedó pendiente"). Cristian abre el día siguiente con ese PASE. Regla dura: la simulación de Conversación nunca repite la de Gramática del mismo día.')

h('2. Lo que cambia para los estudiantes — y cómo se les dice el primer día')
p('Los B1 vienen de un nivel con otro ritmo. Que sientan el cambio desde el minuto uno es intencional: este nivel es más exigente y se dice de frente, como parte de la formación, no como amenaza. **Cristian lo dice a las 8:00 del martes, antes de abrir la guía (3 minutos, en español); Danna lo repite en una frase a las 10:00.** Guion sugerido:')
caja('"Bienvenidos a B1. Les voy a decir desde ya cómo funciona este nivel, para que nadie se sorprente en la semana dos.\n'
     'Uno: aquí se habla inglés todo el tiempo. Desde hoy. Si se equivocan, los corregimos y lo vuelven a decir; para eso vinieron.\n'
     'Dos: el video diario no es opcional. Todos los días, mínimo 3 minutos hablando de corrido, sin leer, al grupo de WhatsApp antes de la medianoche. Lo vemos antes de clase y cada uno recibe una corrección. Es su clase particular.\n'
     'Tres: la clase empieza a las 8:00 en punto. Después de las 8:15 cuenta como llegada tarde, y tres llegadas tarde son una inasistencia.\n'
     'Cuatro: tienen una garantía por escrito, y esa garantía tiene condiciones: 80% de asistencia, 90% de tareas con el video diario incluido, y presentar todas las evaluaciones. Las tres se verifican en los registros de la academia.\n'
     'Va a sentirse duro. Es porque es rápido, y es rápido porque es intenso. De notas y resultados no hablo yo: eso es coordinación. De todo lo demás, cuenten conmigo todos los días."')
p('Después de eso, Cristian abre la guía de Gramática Cl 1 tal cual. No se vuelve a explicar nada de esto en las clases siguientes: se cumple.')

h('3. Danna — el bloque mixto de Conversación (10:00 a 12:00)')
p('**Sí: usas la guía de Conversación B1 del día para todo el grupo**, B1 y B2 juntos. No hay una guía aparte para el B2 en ese bloque y no la necesitas: la guía ya trae la clase minuto a minuto. Lo que haces distinto con los B2 es repartirles los roles. Así se aprovechan los niveles:')
for t in ['**Simulaciones (Bloque 3 de cada guía):** el rol exigente (el gerente, el entrevistador, el cliente difícil, el que pregunta) lo hace un B2; el rol del que responde (candidato, empleado nuevo, quien pide algo) lo hace un B1. Los observadores B2 anotan UN error de gramática que oyeron; los observadores B1 anotan UNA cosa que el guest hizo bien. Rotas para que todos los B1 pasen por el rol central.',
          '**Trabajo en parejas o tríos (Bloques 2 y 3):** siempre mezclados: un B2 con uno o dos B1. El B2 modela la frase primero, el B1 la produce después. Si un B2 corrige mal, corriges tú en voz alta: la autoridad del contenido es tuya.',
          '**Recuperación espaciada y Frase del Día (Bloque 1):** todos participan igual. El ritual de virtud también: es el mismo para los dos niveles.',
          '**Chequeo público de portafolio (Bloque 1):** SOLO para los B1 ("Who sent their video?"). Los B2 tienen su propio esquema; en ese momento ellos trabajan en lo que la guía ponga como warm-up o simplemente observan. No expliques a los B1 el esquema de los B2 ni al revés: a cada grupo se le habla de lo suyo.',
          '**Ticket de salida (Bloque 4):** lo escriben todos (a los B2 también les sirve), pero coordinación procesa los de los B1. La tarea y el video diario de la guía son de los B1; los B2 siguen con lo que tú les tengas asignado.',
          '**Error paper:** uno solo, anónimo, para todo el salón. En la libreta con nombres, marca B1 o B2 al lado de cada nombre.']: li(t)
p('**Cómo se lee una guía en 10 minutos (nunca has trabajado con una; esto es todo lo que necesitas):**')
for t in ['El encabezado trae la virtud de la semana, la Frase del Día (va al tablero al inicio) y la caja **HOY SOLO / NO TOCAR AÚN**: eso delimita qué entra hoy y qué no. Si un estudiante pregunta algo de "NO TOCAR AÚN", se responde "that is for another class".',
          'Cuatro bloques con sus minutos. Lo que está **en cursiva entre comillas** es lo que dices, tal cual. Lo que está en `letra de código` es lo que escribes en el tablero. Si un bloque se alarga, el **Plan B** de ese bloque dice qué recortar; nunca se recorta el ticket de salida ni la tarea.',
          'El checklist de salida del final es tu lista para el reporte de la plataforma: asistencia con llegada tarde, videos recibidos y la mejora de cada uno, error paper (foto) y libreta con nombres, tickets recogidos, PASE enviado.',
          'La **NOTA INTERNA** del final no se lee en clase ni se comenta con los estudiantes: es para ti.',
          'Material: cero. Todo va al tablero o al papel del propio estudiante. Si la guía pide algo físico, lo pide como tarea al estudiante y trae Plan B.']: li(t)

h('4. Grabación de entrada (Danna, martes, dentro de la Conversación Cl 1)')
p('Es la **foto de partida** de cada B1 para la garantía: al final del nivel se graba la misma con las mismas preguntas y se comparan. Se hace el martes, **en paralelo al Bloque 2 o 3**, mientras el grupo trabaja: llamas a UN B1 a la vez a una esquina (su pareja se suma a otra pareja; la clase no se detiene). **60 a 90 segundos por persona, en video, una sola toma, sin corregir y sin repetir.** Quien no quede grabado el martes (llegó tarde, salió antes, entró después) se graba en su primera clase, con la misma etiqueta: ningún B1 queda sin grabación de entrada. Los B2 no se graban.')
p('**Las 4 preguntas (quedan escritas en una esquina del tablero; antes de grabar dices en 10 segundos: "This is your starting photo. Speak, do not read."):**')
caja('(1) Who are you and what do you do?\n(2) Why are you studying English, and what do you need it for?\n(3) What did you do last weekend?\n(4) What have you achieved in English this year?')
p('**Quién graba y con qué:** tú con tu celular (vertical, cerca, sin ruido). Si prefieres, un estudiante B2 sostiene el celular mientras tú haces las preguntas; el que graba no interviene. **Nombre de cada archivo: B1-4H-ENTRADA-CL1-[Nombre Apellido].** Esa misma mañana, antes de salir de la academia, se las envías **a Jacqueline por WhatsApp, una por una, con el nombre del estudiante**; ella las guarda en el computador de la academia en la carpeta del cohorte (B1 MASTERY OCT-2026 → ENTRADA). Tu reporte del martes lleva la lista de grabados y faltantes.')
p('**Cómo saldrán:** al computador de la academia solo van la grabación de entrada, un **video de hito cada 10 clases (Cl 10, 20, 30 y 40: ese día reenvías a Jacqueline el video de cada B1 con su nombre)** y la grabación de salida del nivel, con las mismas 4 preguntas. Los videos diarios se quedan en el grupo de WhatsApp del cohorte: no se descargan.')

h('5. Añadidos a la Cl 1 (no están escritos en las guías; se hacen igual)')
for t in ['**Conversación Cl 1, Bloque 1, al anunciar el cronograma:** agrega que el examen final de la Cl 44 **lo aplica un evaluador externo**, no la docente, y di una sola vez las tres condiciones de la garantía (80% asistencia · 90% tareas con el video diario · todas las evaluaciones, incluida la grabación de entrada de hoy). De formato de examen, notas o resultados no se habla: es coordinación.',
          '**Conversación Cl 1, tarea:** donde la guía dice "PORTFOLIO audio #1 — 2 min", es **VIDEO de 3 minutos**, al grupo de WhatsApp del cohorte, antes de la medianoche. En todas las clases es video, no audio.',
          '**Conversación Cl 1, Bloque 4 (Carta a Mi Yo del Futuro):** la hacen solo los B1. Los B2, en esos 12 minutos, escriben su ticket de salida y, si sobra tiempo, una frase de consejo en inglés para un B1 (no se lee en voz alta; se entrega con los tickets).',
          '**Gramática Cl 1, Bloque 1:** el chequeo de "llegó el video No. 1" no aplica el martes (todavía no hay tarea). Aplica desde el miércoles: Cristian ve los videos antes de las 8:00 y le dice a cada B1 su mejora en 5 segundos.']: li(t)

h('6. Checklist de 10 minutos antes de la Cl 1 (martes 7:45 a.m.)')
p('**Cristian**', after=2)
for t in ['Guía B1_Clase1_GRAMMAR leída completa, con el anexo. HOY SOLO identificado.',
          'El guion del cambio (sección 2) listo para decirlo a las 8:00, antes de abrir la guía.',
          'Reloj, marcadores, libreta personal con columna "llegada tarde".',
          'Grupo de WhatsApp del cohorte en el celular (lo crea coordinación: estudiantes B1 + Cristian + Danna + Jacqueline).']: check(t)
p('**Danna**', after=2)
for t in ['Guía B1_Clase1_CONV leída completa. Sección 3 de esta hoja leída: roles de los B2 decididos antes de entrar (quién hace de gerente en "Meet the Team").',
          'Las 4 preguntas de la grabación copiadas para escribirlas en la esquina del tablero. Celular cargado y con espacio.',
          'Lista de los B1 con nombre y apellido para etiquetar los videos. Chat con Jacqueline abierto.',
          'Hojas: ninguna. La Carta se escribe en papel del propio estudiante.']: check(t)
p('**Jacqueline (coordinación)**', after=2)
for t in ['Cada B1 nuevo con contrato de matrícula y ANEXO DE GARANTÍA firmados antes de entrar al salón (ella firma por Heiiu).',
          'Grupo de WhatsApp del cohorte creado y lista de estudiantes enviada a los dos docentes el lunes.',
          'Carpeta en el computador de la academia: B1 MASTERY OCT-2026 → ENTRADA · HITOS · SALIDA.',
          'Las Cartas cerradas se reciben el martes al mediodía y se guardan hasta el final del nivel.',
          'Reporte de la plataforma habilitado para los dos docentes; recordarles que se llena al salir de cada clase.']: check(t)

p('Dudas durante la semana: por el grupo de docentes o directamente a coordinación. Si algo de la guía no se puede hacer como está escrito, se hace la versión más cercana y se anota en el reporte; no se inventa otra clase.', GRIS, 9.5)

try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
