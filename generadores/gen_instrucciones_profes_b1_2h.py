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
b('Grabación oral de entrada (solo Clase 1): ', 'Angie graba a cada estudiante 1-2 minutos hablando, mientras el resto trabaja. Es la foto de partida del nivel para la garantía. Se sube esa noche a la carpeta que coordinación indique.')
b('Portafolio = VIDEO diario, enviado: ', 'cada estudiante graba un video de mínimo 3 minutos, hablado de corrido y sin leer, y lo envía el mismo día al canal del cohorte. Ya no es audio y ya no se queda en el celular. Audio solo por excepción, máximo 2 por semana. El docente del día VE los videos antes de la clase y anota al menos UNA cosa por mejorar de cada uno (una frase, con el error real). Al inicio de la clase, con la lista en mano, marca quién ENVIÓ y le dice a cada uno su mejora en voz alta, en 5 segundos. Video recibido + mejora anotada van al reporte de la noche. Es la revisión más importante del día: el video es la clase particular de cada estudiante.')
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

sec('6. LAS VIRTUDES: LO QUE HACE QUE ESTO SEA HEIIU Y NO UN CURSO DE INGLÉS')
t('Cada bloque de 5 clases trabaja una de las cuatro virtudes cardinales, por calendario absoluto (Cl 1-5 Prudencia; la guía del día dice cuál sigue): PRUDENCIA (pensar antes de actuar, planear, decidir), FORTALEZA (coraje para hablar, iniciativa, no rendirse), TEMPLANZA (disciplina, manejo del tiempo, paciencia) y JUSTICIA (trabajo en equipo, liderazgo ético, empatía). La virtud no es un adorno: es el hilo del que cuelga la clase. La Frase del Día la lleva dentro, el ritual VATS de 5 a 7 minutos al inicio la activa (Virtud, Activar, Hablar, Compartir: una pregunta que junta la virtud con la gramática del día), y la simulación la pone a prueba. Por eso vendemos "inglés y carácter": puntualidad, constancia, decir la verdad, terminar lo que se empieza. Un estudiante que sale de aquí hablando inglés pero sin haber entrenado eso, no recibió el programa completo. El docente la nombra, la usa y la exige, todos los días, sin sermón: en una frase y en lo que pide.')

sec('7. LO QUE NO CAMBIA')
t('Frase del Día en el tablero antes de empezar (cada clase estrena la suya; la de ayer va en el PASE como referencia). Feedback diario del docente; notas y resultados solo por coordinación. Cuatro bloques largos. Cero material impreso preparado: todo en tablero o dictado. Simulación profesional con un guest, observadores con tarea y el docente como coach (nunca como guest). Tarea con hora de entrega: siempre antes de las 6:30 PM del día siguiente. Sin nombres de estudiantes en la guía; sin nombres de metodologías frente a los estudiantes.')

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(8)
r = p.add_run('La guía del día llega la noche anterior por el grupo de docentes, y el reporte se entrega la misma noche. Muy pronto las guías y los reportes se manejarán por una nueva plataforma de la academia; se avisará con anticipación. Dudas: coordinación, por el grupo.'); r.font.size = Pt(9); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\VERSION_2\B1_2H\SYLLABUS_B1_NOCTURNO_2H.docx'
os.makedirs(os.path.dirname(out), exist_ok=True)
doc.save(out); print('OK', out)
