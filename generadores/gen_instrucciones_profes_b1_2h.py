# -*- coding: utf-8 -*-
"""Hoja de instrucciones para los dos profesores del B1 nocturno 2h: como funciona el cohorte y que hace cada uno."""
import os
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.3); s.bottom_margin = Cm(1.1); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)

def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR

def t(txt, bold=False, after=3):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(10); r.bold = bold

def b(bold_txt, txt):
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5); p.paragraph_format.space_after = Pt(2)
    r = p.add_run('• ' + bold_txt); r.bold = True; r.font.size = Pt(10)
    r2 = p.add_run(txt); r2.font.size = Pt(10)

def tabla(filas, anchos):
    tb = doc.add_table(rows=len(filas), cols=len(filas[0])); tb.style = 'Table Grid'
    for i, fila in enumerate(filas):
        for j, v in enumerate(fila):
            c = tb.cell(i, j); c.width = Cm(anchos[j]); c.paragraphs[0].paragraph_format.space_after = Pt(0)
            r = c.paragraphs[0].add_run(v); r.font.size = Pt(9.5)
            if i == 0: r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); shd(c, 'E54C09')
            elif j == 0: r.bold = True; shd(c, 'FFF8E7')

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('SYLLABUS — B1 NOCTURNO'); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('Cómo funciona este cohorte y qué hace cada docente'); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Instrucciones para los dos docentes · Inicia 28 de septiembre de 2026 · 6:30 a 8:30 PM, lunes a viernes · 88 clases'); r.font.size = Pt(9); r.font.color.rgb = GRIS

sec('1. DOS PISTAS, DOS DOCENTES, DÍAS ALTERNOS')
t('Es el mismo nivel B1 Mastery del cohorte de la mañana, pero en 2 horas diarias. En vez de dos clases el mismo día, las pistas se reparten por día de la semana:')
tabla([
    ['Pista', 'Docente', 'Clases', 'Qué hace'],
    ['CONVERSACIÓN', 'Angie', 'Lunes y miércoles, y viernes alternos (empieza el viernes 3 de octubre)', 'Produce ORAL el módulo del día: historia, pares, simulación profesional. No enseña la regla en papel.'],
    ['GRAMÁTICA', 'Cristian', 'Martes y jueves, y viernes alternos (empieza el viernes 10 de octubre)', 'Sella EN PAPEL lo que salió oral el día anterior: regla del libro citada en el tablero, drill, ejercicio escrito, y una simulación DISTINTA a la de Conversación.'],
], [3.2, 2.2, 3.0, 8.6])
t('Hoy, Clase 1, abre Conversación. Mañana, Clase 2, Gramática. Cada docente recibe únicamente la guía de su día.', bold=True)
t('Cuando un mismo docente dicta dos clases seguidas (viernes y lunes de Angie; jueves y viernes de Cristian), la segunda es de CONSOLIDACIÓN de su pista: en Conversación, producción extendida y simulación larga; en Gramática, taller de precisión y escritura. Ahí es donde caen los hitos del nivel (entrevistas simuladas, taller de pitch). La guía del día lo trae resuelto; el docente no tiene que decidirlo.')

sec('2. EL PASE ENTRE LOS DOS (lo que hace que esto funcione)')
b('Al terminar cada clase, ', 'el docente escribe el PASE al otro: 3 líneas con lo que salió bien, los 3 errores más repetidos y qué queda pendiente del módulo. Se manda por el grupo de docentes esa misma noche.')
b('El que dicta al día siguiente lo lee antes de entrar ', 'y abre su clase con eso: "ayer les salió X; hoy lo sellamos".')
b('Regla dura: ', 'la simulación de Gramática NUNCA repite la de Conversación del día anterior. Mismo punto gramatical, escenario distinto. Si los estudiantes sienten que es "la misma clase de ayer", falló el PASE.')

sec('3. LO NUEVO DESDE ESTE COHORTE (aplica a los dos)')
b('Grabación oral de entrada (solo Clase 1): ', 'Angie graba a cada estudiante 1-2 minutos hablando, mientras el resto trabaja. Es la foto de partida del nivel para la garantía. Esa misma noche se las envía a Jacqueline (auxiliar administrativa) por WhatsApp, una por una con el nombre, y ella las guarda en el computador de la academia.')
b('Portafolio = VIDEO diario, enviado: ', 'cada estudiante graba un video de mínimo 3 minutos, hablado de corrido y sin leer, y lo envía el mismo día al grupo de WhatsApp del cohorte (donde están los dos docentes y Jacqueline). El grupo ES el archivo del portafolio: los videos diarios no se descargan. Solo se guardan en el computador de la academia la grabación de entrada y la de salida de cada nivel. Ya no es audio y ya no se queda en el celular. Audio solo por excepción, máximo 2 por semana. El docente del día VE los videos antes de la clase y anota al menos UNA cosa por mejorar de cada uno (una frase, con el error real). Al inicio de la clase, con la lista en mano, marca quién ENVIÓ y le dice a cada uno su mejora en voz alta, en 5 segundos. Video recibido + mejora anotada van al reporte de la noche. Es la revisión más importante del día: el video es la clase particular de cada estudiante.')
b('Puntualidad: ', 'la clase empieza a las 6:30 en punto. Llegada después de las 6:45 se marca como LLEGADA TARDE en el reporte; cada 3 cuentan como una inasistencia para el contrato y la garantía. Se dice en la Clase 1 como parte de la formación: llegar a tiempo es lo que estamos entrenando, no un castigo.')
b('Las condiciones de la garantía se dicen una vez, en Clase 1: ', 'asistencia mínima 80%, 90% de tareas incluido el video diario, todas las evaluaciones. Después no se vuelven a explicar: se cumplen.')
b('Inglés: ', '100% inglés desde el Bloque 2 de la Clase 1. El español solo para el cronograma, los rituales y la Cápsula en la primera clase.')
b('Feedback sí, notas no: ', 'el docente da feedback TODOS los días y de frente: la mejora de cada video, el error paper, la corrección en la simulación, "esto te salió, esto te falta". Eso es lo que el estudiante más valora y es tuyo. Lo único que el docente NO comunica son NOTAS y RESULTADOS de las evaluaciones (midterm, final, aprobó o no, garantía): eso lo comunica coordinación, para que nadie negocie una nota con su profesor. Si preguntan "¿cómo voy?", se responde con feedback concreto; si preguntan "¿qué nota saqué?", se responde "eso te lo dice coordinación".')

sec('4. EL REPORTE DE CADA CLASE (en la plataforma, al terminar la clase)')
t('Se llena en la plataforma de reportes de la academia la misma noche, al salir de la clase, con estas cinco piezas:')
b('Asistencia ', 'con la columna nueva de llegada tarde.')
b('Videos recibidos ', 'del día anterior: quién envió, quién no, y la mejora anotada por cada video visto.')
b('Error paper ', 'sin nombres (foto del papel) y el registro con nombres aparte, solo para coordinación.')
b('Tickets de salida ', 'recogidos (foto, o entrega física al día siguiente).')
b('El PASE ', 'al otro docente, por el grupo.')

sec('5. EL PLAN DEL NIVEL (para que los dos lo tengan en la cabeza)')
t('Cl 1-5 puente de repaso A1/A2 · Cl 6-43 módulos con simulaciones profesionales, con entrevistas simuladas en Cl 20 y Cl 36 · Cl 44 MIDTERM "My Story, My Goals" (5 min) · Cl 45-85 segunda mitad, con negociación en Cl 56 y Cl 70 y debate en Cl 62 y Cl 76 · Cl 80-84 taller de pitch · Cl 86-87 presentaciones finales en formato panel ("Shark Tank": 3 minutos ante tres compañeros que preguntan) · Cl 88 examen final con evaluador externo. Estos hitos llegan dentro de la guía del día; en la Clase 1 solo se anuncian las fechas del midterm y del final.')

sec('6. LAS VIRTUDES: POR QUÉ LAS HACEMOS Y CÓMO SE HACEN BIEN')
t('Por qué, en tres frases que puedes repetir:', bold=True)
b('Porque es lo que vendemos. ', 'Al estudiante no se le prometió inglés: se le prometió entrenamiento con garantía y un destino (un trabajo, irse, emprender). Lo que decide si llega a ese destino no es la gramática: es si aparece a tiempo, si sostiene el esfuerzo cuando ya no es novedad, si se atreve a hablar con miedo, si cumple lo que dijo. Eso es lo que un jefe, una familia de Au Pair o un cliente evalúan primero. Las virtudes son ese entrenamiento, con nombre.')
b('Porque el inglés no se aprende sin ellas. ', 'Repetir mil veces lo mismo es templanza. Hablar frente a otros sabiendo que te vas a equivocar es fortaleza. Grabar el video el día que no quieres es prudencia y templanza juntas. Un estudiante que entiende que la virtud del bloque es lo que le va a permitir sostener el nivel, deja de ver el ritual como relleno.')
b('Porque es lo que hace que se queden. ', 'El que abandona en la semana 3 no abandona por la gramática: abandona porque no tenía nombre para lo que le estaba pasando. Cuando el docente le dice "esto que sientes es la parte de fortaleza del nivel, y por eso la estamos entrenando", el estudiante se queda. La retención del grupo depende de esto más que de cualquier otra cosa que hagas.')
t('Las cuatro, por calendario absoluto (bloques de 5 clases; Cl 1-5 Prudencia; la guía del día dice cuál sigue, y no se desplaza por festivos):', bold=True)
b('PRUDENCIA: ', 'pensar antes de actuar, planear, decidir. En inglés: preparar lo que vas a decir antes de decirlo; elegir el tiempo verbal antes de abrir la boca.')
b('FORTALEZA: ', 'coraje para hablar con miedo, iniciativa, no rendirse. En inglés: pedir la palabra, ser el guest en la simulación, grabar el video aunque salga mal.')
b('TEMPLANZA: ', 'disciplina, manejo del tiempo, paciencia con la repetición. En inglés: el video diario, llegar a tiempo, hacer el drill completo sin atajos.')
b('JUSTICIA: ', 'trabajo en equipo, liderazgo ético, empatía. En inglés: escuchar al compañero en la simulación, corregir sin humillar, ayudar al que va más lento.')
t('Cómo se hace bien, en 5 a 7 minutos (el ritual VATS, al inicio de la clase):', bold=True)
b('V, Virtud (1 min): ', 'el docente nombra la virtud del bloque y la conecta con lo de HOY en una frase: "Esta semana es fortaleza. Hoy la simulación es una entrevista: la fortaleza es contestar aunque no tengas la palabra perfecta."')
b('A, Activar (2 min): ', 'una pregunta, en inglés, que junte la virtud con la gramática del día. Ejemplo con presente perfecto: "What is something you have done this year that took courage?" Cada uno piensa 30 segundos.')
b('T, Hablar (2-3 min): ', 'en parejas o en cadena de pie, cada uno responde en una o dos frases. El docente escucha y anota errores para el error paper, no corrige aquí.')
b('S, Compartir (1 min): ', 'dos o tres respuestas al grupo. El docente cierra con una sola frase que conecta: "That is why today you speak first and think second."')
t('Lo que NO es: no es un sermón, no es una charla de motivación, no dura 15 minutos y no se salta cuando "no hay tiempo". Es una frase, una pregunta y las voces de ellos. Si el docente lo recorta, la clase pierde su hilo y el estudiante pierde la razón para volver mañana.')
t('Cuando un estudiante pregunte "¿y esto qué tiene que ver con inglés?", la respuesta es esta:', bold=True)
t('"Todo. Aquí no te estamos enseñando palabras: te estamos entrenando para el día que las necesites de verdad, en una entrevista, en un vuelo, frente a un cliente. Ese día no te va a fallar el vocabulario: te va a fallar el nervio, o la constancia, o la preparación. Eso es lo que entrenamos con las virtudes. Y es lo que hace que el que se gradúa aquí no solo hable inglés: se le nota."')

sec('7. LOS RITUALES Y POR QUÉ EXISTEN (lo que no cambia)')
t('Ninguno de estos es un capricho ni una formalidad. Cada uno resuelve un problema concreto que ya nos costó estudiantes. El docente que entiende para qué sirve cada uno, lo hace bien; el que lo ve como regla, lo recorta.')
b('La Frase del Día en el tablero, antes de que entren. ', 'QUÉ ES: una sola oración en inglés, escrita por la academia en la guía del día (el docente no la inventa), que junta la estructura gramatical de esa clase con la virtud de la semana. Ejemplo real, Clase 1 de este cohorte (módulo: pasado cerrado vs abierto; virtud: prudencia): "Prudence weighs the clock before it speaks: what I did last year is closed, and what I have achieved this year is still open." Ahí están el simple past, el present perfect y la prudencia en una frase que se puede decir en voz alta. CÓMO SE HACE, en orden: (1) el docente la escribe en el tablero ANTES de que entren los estudiantes, arriba y grande, y ahí se queda toda la clase; (2) en el Bloque 1 la lee dos veces, el grupo la repite en coro dos veces, y un estudiante la dice solo; (3) el docente la explica en una sola línea ("two pasts in one sentence: I did closes the door, I have done leaves it open"), sin clase de gramática; (4) durante la clase el docente la usa de forma natural al menos tres veces, en lo que dice; (5) al cierre, un estudiante la dice de memoria y otro la usa en una oración propia. Total: unos 4 minutos, repartidos. Por qué: una frase que se oye, se dice y se usa diez veces en contexto se queda; una lista de veinte palabras copiadas no. Es la forma más barata de repetición espaciada que existe, y es el ancla visible de toda la clase: el estudiante distraído levanta la vista y sabe de qué se trata hoy. Reemplazó a las listas de vocabulario en cuaderno, que nadie volvía a abrir. Cada clase estrena la suya; la de ayer va en el reporte solo como referencia.')
b('El chequeo de portafolio, al abrir. ', 'Quién envió el video y una mejora dicha en voz alta a cada uno. Por qué: es el único momento del día en que cada estudiante recibe feedback personal, y es lo que hace que el video se grabe mañana también. Un portafolio que nadie ve muere en dos semanas.')
b('La recuperación al abrir (lo de hace 3 y hace 7 clases). ', 'Dos o tres preguntas de pie sobre lo que se vio hace tres y siete clases, antes de lo nuevo. Por qué: lo que se recupera justo cuando se está olvidando se fija para siempre; lo que se vio una sola vez se pierde en diez días. Son tres minutos que valen una clase de repaso.')
b('Cuatro bloques largos, no doce cortos. ', 'Por qué: hablar un idioma exige tiempo sostenido en una misma situación; con actividades de ocho minutos el estudiante nunca llega a la parte difícil, que es donde se aprende.')
b('La simulación con un guest, observadores con tarea y el docente como coach (nunca como guest). ', 'Por qué: el estudiante que hace de guest vive la situación real (una entrevista, una queja, una negociación) y los que observan trabajan con una ficha, así nadie mira el techo. Si el docente hace de guest, la simulación se vuelve una conversación con el profesor, que es justo lo que el estudiante ya sabe hacer.')
b('El error paper: anónimo en el tablero, con nombres solo para coordinación. ', 'Por qué: el error sin nombre se corrige entre todos y nadie se avergüenza, así que la próxima vez se atreven a hablar igual; el registro con nombres le permite a coordinación ver quién repite qué y actuar antes de que se vuelva un retiro.')
b('El ticket de salida, en los últimos 5 minutos. ', 'Tres a cinco frases escritas por cada estudiante con la estructura de hoy, con nombre, sin calificar. Por qué: es la evidencia diaria de que cada uno aprendió lo de ese día, sin depender de la opinión de nadie. Es lo que sostiene la garantía y lo que le muestra a coordinación quién va y quién no. Se recogen todos: un ticket que falta es una señal.')
b('La tarea con hora de entrega, sin excepciones. ', 'Por qué: la constancia no se enseña con discursos, se entrena con fechas que se cumplen. Y la hora fija (antes de la clase siguiente) evita el "te lo mando después", que es el principio del abandono.')
b('Cero material impreso: todo en el tablero, en el papel del estudiante o dictado. ', 'Por qué: sin hoja, la atención está en el docente y en hablar; con hoja, el estudiante lee en vez de escuchar. Y el material de Heiiu es propiedad intelectual de la academia: la guía es solo para el docente y no se fotografía ni se comparte.')
b('Sin nombres de estudiantes en las guías, sin nombres de metodologías frente a ellos, sin notas de boca del docente. ', 'Por qué: la guía es reutilizable y no lleva casos personales; los nombres de las técnicas son de la academia y no se enseñan; y las notas van por coordinación para que ningún estudiante negocie su resultado con su profesor.')

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(8)
r = p.add_run('La guía del día llega la noche anterior por el grupo de docentes, y el reporte se entrega la misma noche. Muy pronto las guías y los reportes se manejarán por una nueva plataforma de la academia; se avisará con anticipación. Dudas: coordinación, por el grupo.'); r.font.size = Pt(9); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\VERSION_2\B1_2H\SYLLABUS_B1_NOCTURNO_2H.docx'
os.makedirs(os.path.dirname(out), exist_ok=True)
doc.save(out); print('OK', out)
