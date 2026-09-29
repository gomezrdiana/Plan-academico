# -*- coding: utf-8 -*-
"""SYLLABUS (hoja de instrucciones de entrada al docente) para los 6 formatos de cohorte Heiiu.

Un solo generador parametrizado. Misma estructura y tono que
generadores/gen_instrucciones_profes_b1_2h.py (7 secciones, Calibri, titulos naranja
E54C09, tabla con encabezado naranja y primera columna crema FFF8E7).

Correr desde la raiz:  python generadores/gen_syllabus_cohortes.py
Salida: VERSION_2/{COHORTE}/SYLLABUS_*.docx  (los PDF se convierten aparte con Word COM)

Fuentes de los datos (nada inventado; lo que no esta en fuente dice "lo define coordinacion"):
- documentos_operativos/MASTER_BLUEPRINT_HEIIU.md (horas y clases por formato, virtudes)
- documentos_operativos/ARQUITECTURA_ACADEMICA_HEIIU.md  2-BIS (reparto de bloques por formato)
- La Clase 1 de cada cohorte en VERSION_2 (cronograma, proyecto, rituales)
- VERSION_2/A2_2H/A2_2h_MY_LIFE_INSTRUCTIVO_PRINT.md y A2_4H/A2_4h_MY_YEAR_INSTRUCTIVO_PRINT.md
- recursos/comercial/plataforma LaHaus/INFO_ACADEMIA_PARA_ASISTENTE.md  10 (promesa por nivel)
"""
import os
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAR = RGBColor(0xE5, 0x4C, 0x09)
GRIS = RGBColor(0x66, 0x66, 0x66)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)

PIE = ('La guia del dia llega la noche anterior por el grupo de docentes; el reporte se entrega la misma '
       'noche. Muy pronto las guias y los reportes se manejaran por una nueva plataforma de la academia; '
       'se avisara con anticipacion. Dudas: coordinacion, por el grupo.')

VIRTUDES = ('Cada bloque de 5 clases trabaja una de las cuatro virtudes cardinales, por calendario absoluto '
            '(Cl 1-5 Prudencia; la virtud no se desplaza por festivos ni por clases canceladas, y la guia del dia '
            'dice cual sigue): PRUDENCIA (pensar antes de actuar, planear, decidir), FORTALEZA (coraje para hablar, '
            'iniciativa, no rendirse), TEMPLANZA (disciplina, manejo del tiempo, paciencia) y JUSTICIA (trabajo en '
            'equipo, liderazgo etico, empatia). La virtud no es un adorno: es el hilo del que cuelga la clase. '
            'La Frase del Dia la lleva dentro, el ritual VATS de 5 a 7 minutos al inicio la activa (Virtud, Activar, '
            'Hablar, Compartir: una pregunta que junta la virtud con la estructura del dia), y la simulacion la pone '
            'a prueba. Por eso vendemos "ingles y caracter": puntualidad, constancia, decir la verdad, terminar lo '
            'que se empieza. Un estudiante que sale de aqui hablando ingles pero sin haber entrenado eso, no recibio '
            'el programa completo. El docente la nombra, la usa y la exige todos los dias, sin sermon: en una frase '
            'y en lo que pide.')


# ----------------------------------------------------------------------------- helpers docx
def _shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color)
    tcPr.append(el)


class Doc:
    def __init__(self):
        self.doc = Document()
        for s in self.doc.sections:
            s.top_margin = Cm(1.3); s.bottom_margin = Cm(1.1)
            s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
        self.doc.styles['Normal'].font.name = 'Calibri'
        self.doc.styles['Normal'].font.size = Pt(10)

    def sec(self, txt):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(2)
        r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR

    def t(self, txt, bold=False, after=3, size=10):
        p = self.doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
        r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold

    def b(self, bold_txt, txt):
        p = self.doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.5); p.paragraph_format.space_after = Pt(2)
        r = p.add_run('• ' + bold_txt); r.bold = True; r.font.size = Pt(10)
        r2 = p.add_run(txt); r2.font.size = Pt(10)

    def tabla(self, filas, anchos):
        tb = self.doc.add_table(rows=len(filas), cols=len(filas[0]))
        tb.style = 'Table Grid'
        for i, fila in enumerate(filas):
            for j, v in enumerate(fila):
                c = tb.cell(i, j); c.width = Cm(anchos[j])
                c.paragraphs[0].paragraph_format.space_after = Pt(0)
                r = c.paragraphs[0].add_run(v); r.font.size = Pt(9.5)
                if i == 0:
                    r.bold = True; r.font.color.rgb = BLANCO; _shd(c, 'E54C09')
                elif j == 0:
                    r.bold = True; _shd(c, 'FFF8E7')

    def titulo(self, t1, t2, t3):
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(t1); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = NAR
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(t2); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAR
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(t3); r.font.size = Pt(9); r.font.color.rgb = GRIS

    def pie(self):
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        r = p.add_run(PIE); r.font.size = Pt(9); r.font.color.rgb = GRIS

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.doc.save(path)


# ----------------------------------------------------------------------------- datos por cohorte
COHORTES = [
    # ------------------------------------------------------------------ A1 4H
    dict(
        out='VERSION_2/A1_4H/SYLLABUS_A1_INTENSIVO_4H.docx',
        titulo='SYLLABUS — A1 INTENSIVO 4H',
        linea3=('Instrucciones para el docente del cohorte · Jornada de la mañana del ARRANQUE A1+A2 · '
                'Inicia el 5 de octubre de 2026 · 8:00 a 12:00 M, lunes a viernes · 23 clases, 90 horas'),
        sec1_titulo='1. CÓMO FUNCIONA EL COHORTE',
        sec1_intro=('Es el nivel A1 completo en jornada intensiva de la mañana: una sola clase diaria de 4 horas '
                    'con un solo docente. Una clase de 4 horas son dos clases de 2 horas seguidas con pausa — el '
                    'reparto de los cuatro bloques es B1 30-35\' · B2 80-90\' · B3 80-90\' · B4 25-30\', '
                    'y la pausa va entre el Bloque 2 y el Bloque 3 sin contar en esos tiempos.'),
        sec1_tabla=[
            ['Dato', 'Cómo es en este cohorte'],
            ['Formato y horario', '4 horas diarias, lunes a viernes, 8:00 a 12:00 M. 23 clases, 90 horas. '
                                  'Es la jornada de la mañana del ARRANQUE A1+A2 (al terminar A1 sigue A2 en el mismo horario).'],
            ['Docente', 'Un solo docente dicta la sesión completa. El docente asignado lo define coordinación.'],
            ['Contenido', 'Libro oficial A1, módulo por módulo en orden. El módulo que no exista en el libro se '
                          'salta: nunca se inventa contenido ni se infiere.'],
            ['Proyecto del nivel', 'MY WORLD. Se anuncia en la Clase 1 y se construye una pieza por clase — la pieza del '
                                   'día es el video del portafolio de ese día. Se presenta completo en Cl 22, de 3 a 5 minutos.'],
            ['Idioma', 'La Clase 1 admite español para el cronograma, la virtud, los rituales y la Carta. Desde el Bloque 2 de '
                       'la Clase 1 el docente habla en inglés, con el inglés muy simple que pide A1.'],
        ],
        sec1_anchos=[3.6, 13.4],
        sec1_cierre=None,
        sec2_titulo='2. LA CONTINUIDAD ENTRE CLASES (lo que hace que esto funcione)',
        sec2=[
            ('Al abrir cada clase, la recuperación espaciada: ',
             '3 a 5 disparadores de la Clase N-3 y de la Clase N-7, orales, DE PIE, en cadena, sin cuaderno. Los errores que se '
             'oigan van al tablero anónimos y se re-producen correctos en 1 minuto. No es explicación: es recordar hablando.'),
            ('Enseguida, el error paper del día anterior: ',
             '4 a 6 errores REALES del grupo, anónimos, en el tablero; el grupo diagnostica qué está mal y por qué, '
             'se reconstruye la forma correcta y cada estudiante produce un ejemplo nuevo propio. Errores reales o no se usan.'),
            ('Y el chequeo de portafolio: ',
             'con la lista en mano, quién envió el video y la mejora anotada de cada uno. En la Clase 1 el ritual solo se '
             'presenta; el primer chequeo público es en la Clase 2.'),
            ('Lo que queda pendiente se hereda: ',
             'lo que no cerró hoy entra en el reporte de la noche y coordinación lo devuelve dentro de la guia siguiente. '
             'El docente no reinventa la secuencia: la guia del día la trae resuelta.'),
        ],
        grabador='el docente',
        video_min='1 minuto',
        hora_inicio='8:00',
        hora_tarde='8:15',
        ingles=('desde el Bloque 2 de la Clase 1 el docente habla en inglés. En A1 la Clase 1 puede llevar más español '
                'que los otros niveles: el cronograma, la virtud, los rituales y la Carta se explican en español solo ese día. '
                'Después, inglés simple todo el tiempo, con gesto y modelado en vez de traducción.'),
        pase_reporte=False,
        sec5_titulo='5. EL PLAN DEL NIVEL (para que el docente lo tenga en la cabeza)',
        sec5=[
            ('Lo que el nivel entrega: ',
             'el verbo ser/estar, presentarse y presentar a otros, números, hora y precios, la rutina diaria, la familia, '
             'las profesiones, lugares de la ciudad y emociones. Presente simple, pasado simple con verbos regulares e '
             'irregulares, "hay", presente continuo y planes con going to. Cada clase termina hablando: simulación de una '
             'situación cotidiana.'),
            ('Los hitos, por número de clase: ',
             'Cl 6 mini-presentación · Cl 11 y Cl 12 MIDTERM (proyecto + examen) · Cl 17 mini-presentación · '
             'Cl 22 presentaciones finales MY WORLD, de 3 a 5 minutos · Cl 23 examen FINAL, aplicado por un evaluador '
             'externo (ese día el docente no dicta guia).'),
            ('Cómo llegan: ',
             'todos los hitos van DENTRO de la guia del día, sin día aparte ni marcador separado. En la Clase 1 el docente '
             'solo anuncia los números de clase del midterm y del final — nunca contenido, formato, notas ni resultados.'),
        ],
        due='antes de las 8:00 AM del día siguiente',
        sec7_extra=None,
    ),

    # ------------------------------------------------------------------ A1 2H
    dict(
        out='VERSION_2/A1_2H/SYLLABUS_A1_NOCTURNO_2H.docx',
        titulo='SYLLABUS — A1 NOCTURNO 2H',
        linea3=('Instrucciones para el docente del cohorte · 6:30 a 8:30 PM, lunes a viernes · '
                '45 clases, 90 horas · Fecha de inicio: lo define coordinación'),
        sec1_titulo='1. CÓMO FUNCIONA EL COHORTE',
        sec1_intro=('Es el mismo nivel A1 del cohorte de la mañana, repartido en 2 horas diarias de noche: 45 clases en vez '
                    'de 23. Una clase = un módulo (o media parte de un módulo largo, y la guia lo dice). El reparto de los '
                    'cuatro bloques es B1 20-25\' · B2 40-45\' · B3 35-40\' · B4 15-20\'.'),
        sec1_tabla=[
            ['Dato', 'Cómo es en este cohorte'],
            ['Formato y horario', '2 horas diarias, lunes a viernes, 6:30 a 8:30 PM. 45 clases, 90 horas.'],
            ['Docente', 'Un solo docente dicta todo el nivel. El docente asignado lo define coordinación.'],
            ['Contenido', 'Libro oficial A1, módulo por módulo en orden. Como el día es corto, un módulo largo se '
                          'parte en dos clases y la guia trae la caja "HOY SOLO / NO TOCAR AÚN" que marca el corte. El módulo '
                          'que no exista en el libro se salta: nunca se inventa contenido.'],
            ['Proyecto del nivel', 'MY WORLD. Se anuncia en la Clase 1 y se construye una pieza por clase — la pieza del día es '
                                   'el video del portafolio de ese día. Se presenta al cierre del nivel.'],
            ['Idioma', 'La Clase 1 admite español para el cronograma, la virtud, los rituales y la Carta. Desde el Bloque 2 de la '
                       'Clase 1 el docente habla en inglés, con el inglés muy simple que pide A1.'],
        ],
        sec1_anchos=[3.6, 13.4],
        sec1_cierre=None,
        sec2_titulo='2. LA CONTINUIDAD ENTRE CLASES (lo que hace que esto funcione)',
        sec2=[
            ('Al abrir cada clase, la recuperación espaciada: ',
             '3 a 5 disparadores de la Clase N-3 y de la Clase N-7, orales, DE PIE, en cadena, sin cuaderno. Los errores que se '
             'oigan van al tablero anónimos y se re-producen correctos en 1 minuto. No es explicación: es recordar hablando.'),
            ('Enseguida, el error paper del día anterior: ',
             '4 a 6 errores REALES del grupo, anónimos, en el tablero; el grupo diagnostica y reconstruye la forma correcta, y '
             'cada estudiante produce un ejemplo nuevo propio. Errores reales o no se usan.'),
            ('Y el chequeo de portafolio: ',
             'con la lista en mano, quién envió el video y la mejora anotada de cada uno. En la Clase 1 el ritual solo se '
             'presenta; el primer chequeo público es en la Clase 2.'),
            ('La frontera del día se respeta: ',
             'la caja "HOY SOLO / NO TOCAR AÚN" de la primera página de la guia no es una sugerencia. Adelantarse hoy rompe '
             'la clase de mañana, que ya está escrita.'),
        ],
        grabador='el docente',
        video_min='1 minuto',
        hora_inicio='6:30',
        hora_tarde='6:45',
        ingles=('desde el Bloque 2 de la Clase 1 el docente habla en inglés. En A1 la Clase 1 puede llevar más español que '
                'los otros niveles: el cronograma, la virtud, los rituales y la Carta se explican en español solo ese día. '
                'Después, inglés simple todo el tiempo, con gesto y modelado en vez de traducción.'),
        pase_reporte=False,
        sec5_titulo='5. EL PLAN DEL NIVEL (para que el docente lo tenga en la cabeza)',
        sec5=[
            ('Lo que el nivel entrega: ',
             'el verbo ser/estar, presentarse y presentar a otros, números, hora y precios, la rutina diaria, la familia, las '
             'profesiones, lugares de la ciudad y emociones. Presente simple, pasado simple con verbos regulares e irregulares, '
             '"hay", presente continuo y planes con going to. Cada clase termina hablando: simulación de una situación cotidiana.'),
            ('Los hitos, por número de clase: ',
             'Cl 11 sesión especial · Cl 22 y Cl 23 MIDTERM · Cl 34 sesión especial · Cl 44 y Cl 45 FINAL (proyecto '
             'MY WORLD + examen; el examen lo aplica un evaluador externo y ese día el docente no dicta guia). El reparto exacto '
             'de esos dos últimos días lo define coordinación.'),
            ('Cómo llegan: ',
             'todos los hitos van DENTRO de la guia del día, sin día aparte ni marcador separado. En la Clase 1 el docente solo '
             'anuncia los números de clase del midterm y del final — nunca contenido, formato, notas ni resultados.'),
        ],
        due='antes de las 6:30 PM del día siguiente',
        sec7_extra=None,
    ),

    # ------------------------------------------------------------------ A2 4H
    dict(
        out='VERSION_2/A2_4H/SYLLABUS_A2_INTENSIVO_4H.docx',
        titulo='SYLLABUS — A2 INTENSIVO 4H',
        linea3=('Instrucciones para el docente del cohorte · Jornada de la mañana del ARRANQUE A1+A2 · '
                '8:00 a 12:00 M, lunes a viernes · 28 clases, 110 horas · Arranca al terminar A1: la fecha la define coordinación'),
        sec1_titulo='1. CÓMO FUNCIONA EL COHORTE',
        sec1_intro=('Es el nivel A2 completo en jornada intensiva de la mañana: una sola clase diaria de 4 horas con un solo '
                    'docente, y es la segunda mitad del ARRANQUE A1+A2. Una clase de 4 horas son dos clases de 2 horas seguidas con '
                    'pausa — el reparto de los cuatro bloques es B1 30-35\' · B2 80-90\' · B3 80-90\' · B4 25-30\', y la '
                    'pausa va entre el Bloque 2 y el Bloque 3 sin contar en esos tiempos.'),
        sec1_tabla=[
            ['Dato', 'Cómo es en este cohorte'],
            ['Formato y horario', '4 horas diarias, lunes a viernes, 8:00 a 12:00 M. 28 clases, 110 horas.'],
            ['Docente', 'Un solo docente dicta la sesión completa. El docente asignado lo define coordinación.'],
            ['Contenido', 'Libro oficial A2 en Cl 1-20 y arco de repaso hacia B1 en Cl 21-28. El libro A2 tiene huecos '
                          '(M4, M9, M19, M25, M31, M35 y M40 no existen): se saltan, no se inventa nada para llenarlos.'],
            ['Proyecto del nivel', 'MY YEAR. Se anuncia en la Clase 1 y se construye una pieza por clase — la pieza del día '
                                   'es el video del portafolio de ese día. 19 piezas en Cl 1-20; en el arco solo se pulen y se '
                                   'ensamblan (no se agregan piezas nuevas). Presentación completa de 3 a 5 minutos en Cl 27.'],
            ['Módulo de Graduación', 'Al terminar A2 dentro del ARRANQUE, el estudiante elige su Módulo de Graduación '
                                              '(EMPRENDEDOR o PASAPORTE), incluido. El docente no lo explica ni lo ofrece: si preguntan, '
                                              'se responde "eso lo ve con coordinación".'],
        ],
        sec1_anchos=[3.8, 13.2],
        sec1_cierre=None,
        sec2_titulo='2. LA CONTINUIDAD ENTRE CLASES (lo que hace que esto funcione)',
        sec2=[
            ('Al abrir cada clase, la recuperación espaciada: ',
             '3 a 5 disparadores de la Clase N-3 y de la Clase N-7, orales, DE PIE, en cadena, sin cuaderno. Los errores que se oigan '
             'van al tablero anónimos y se re-producen correctos en 1 minuto. No es explicación: es recordar hablando.'),
            ('Enseguida, el error paper del día anterior: ',
             '4 a 6 errores REALES del grupo, anónimos, en el tablero; el grupo diagnostica y reconstruye la forma correcta, y cada '
             'estudiante produce un ejemplo nuevo propio. En el arco de repaso (Cl 21-28) este trabajo desde el error es la espina '
             'dorsal del Bloque 2.'),
            ('Y el chequeo de portafolio: ',
             'con la lista en mano, quién envió el video y la mejora anotada de cada uno, más una línea que le pone '
             'nombre a la pieza ("ese fue tu MY YEAR piece N"). En la Clase 1 el ritual solo se presenta; el primer chequeo público '
             'es en la Clase 2.'),
        ],
        grabador='el docente',
        video_min='2 minutos',
        hora_inicio='8:00',
        hora_tarde='8:15',
        ingles=('100% inglés desde el Bloque 2 de la Clase 1. El español solo para el cronograma, la virtud, los rituales y la '
                'Carta o la Cápsula en la primera clase.'),
        pase_reporte=False,
        sec5_titulo='5. EL PLAN DEL NIVEL (para que el docente lo tenga en la cabeza)',
        sec5=[
            ('Lo que el nivel entrega: ',
             'futuro (will, might, planes), fechas y calendario, condicionales, pasado simple y continuo, presente perfecto, voz '
             'pasiva, verbos con preposición, comparativos y superlativos, cantidades y precios, describir personas y ropa. '
             'Situaciones: entrevista de trabajo, agencia de viajes, hotel, tienda, restaurante, servicio al cliente, reunión de '
             'equipo y primer día en un empleo.'),
            ('Los hitos, por número de clase: ',
             'Cl 1-20 módulos del libro · Cl 14 MIDTERM ("MY YEAR so far", unos 5 minutos por estudiante) · Cl 21-28 arco de '
             'repaso hacia B1 · Cl 27 presentación final de MY YEAR completa (3 a 5 minutos) · Cl 28 examen FINAL en las '
             'últimas 2 horas, aplicado por un evaluador externo (para esas 2 horas no hay guia).'),
            ('Cómo llegan: ',
             'todos los hitos van DENTRO de la guia del día, sin día aparte ni marcador separado. En la Clase 1 el docente solo '
             'anuncia los números de clase del midterm y del final — nunca contenido, formato, notas ni resultados.'),
        ],
        due='antes de las 8:00 AM del día siguiente',
        sec7_extra=None,
    ),

    # ------------------------------------------------------------------ A2 2H
    dict(
        out='VERSION_2/A2_2H/SYLLABUS_A2_NOCTURNO_2H.docx',
        titulo='SYLLABUS — A2 NOCTURNO 2H',
        linea3=('Instrucciones para el docente del cohorte · 6:30 a 8:30 PM, lunes a viernes · '
                '55 clases, 110 horas · Fecha de inicio: lo define coordinación'),
        sec1_titulo='1. CÓMO FUNCIONA EL COHORTE',
        sec1_intro=('Es el mismo nivel A2 del cohorte de la mañana, repartido en 2 horas diarias de noche: 55 clases en vez de 28. '
                    'Una clase = un módulo del libro, y cuando el módulo es largo la guia lo parte y marca el corte. El reparto '
                    'de los cuatro bloques es B1 20-25\' · B2 40-45\' · B3 35-40\' · B4 15-20\'.'),
        sec1_tabla=[
            ['Dato', 'Cómo es en este cohorte'],
            ['Formato y horario', '2 horas diarias, lunes a viernes, 6:30 a 8:30 PM. 55 clases, 110 horas.'],
            ['Docente', 'Un solo docente dicta todo el nivel. El docente asignado lo define coordinación.'],
            ['Contenido', 'Libro oficial A2, módulo por módulo en orden, con la caja "HOY SOLO / NO TOCAR AÚN" cuando el '
                          'módulo se parte en dos clases. El libro A2 tiene huecos (M4, M9, M19, M25, M31, M35 y M40 no existen): '
                          'se saltan, no se inventa nada para llenarlos. Agotado el libro, el resto del nivel es repaso hacia B1.'],
            ['Proyecto del nivel', 'MY LIFE. Cada estudiante presenta su vida real en inglés, de 7 a 10 minutos más 2 o 3 '
                                   'preguntas del público, en Cl 53. Se construye una pieza por clase — la pieza del día es la '
                                   'ronda oral de cierre del Bloque 3 y el video del portafolio de ese día. El instructivo con los '
                                   'guiones exactos lo entrega coordinación con la guia; el docente no agrega actividades.'],
            ['Módulo de Graduación', 'Aplica a los cohortes del ARRANQUE A1+A2. Si este cohorte lo tiene o no, lo define '
                                              'coordinación; el docente no lo explica ni lo ofrece.'],
        ],
        sec1_anchos=[3.8, 13.2],
        sec1_cierre=None,
        sec2_titulo='2. LA CONTINUIDAD ENTRE CLASES (lo que hace que esto funcione)',
        sec2=[
            ('Al abrir cada clase, la recuperación espaciada: ',
             '3 a 5 disparadores de la Clase N-3 y de la Clase N-7, orales, DE PIE, en cadena, sin cuaderno. Los errores que se oigan '
             'van al tablero anónimos y se re-producen correctos en 1 minuto. No es explicación: es recordar hablando.'),
            ('Enseguida, el error paper del día anterior: ',
             '4 a 6 errores REALES del grupo, anónimos, en el tablero; el grupo diagnostica y reconstruye la forma correcta, y cada '
             'estudiante produce un ejemplo nuevo propio. Errores reales o no se usan.'),
            ('Y el chequeo de portafolio: ',
             'con la lista en mano, quién envió el video y la mejora anotada de cada uno, más la línea que le pone nombre '
             'a la pieza de MY LIFE. En la Clase 1 el ritual solo se presenta; el primer chequeo público es en la Clase 2.'),
            ('La frontera del día se respeta: ',
             'la caja "HOY SOLO / NO TOCAR AÚN" de la primera página no es una sugerencia. Adelantarse hoy rompe la clase de '
             'mañana, que ya está escrita.'),
        ],
        grabador='el docente',
        video_min='2 minutos',
        hora_inicio='6:30',
        hora_tarde='6:45',
        ingles=('100% inglés desde el Bloque 2 de la Clase 1. El español solo para el cronograma, la virtud, los rituales y la '
                'Carta o la Cápsula en la primera clase.'),
        pase_reporte=False,
        sec5_titulo='5. EL PLAN DEL NIVEL (para que el docente lo tenga en la cabeza)',
        sec5=[
            ('Lo que el nivel entrega: ',
             'futuro (will, might, planes), fechas y calendario, condicionales, pasado simple y continuo, presente perfecto, voz '
             'pasiva, verbos con preposición, comparativos y superlativos, cantidades y precios, describir personas y ropa. '
             'Situaciones: entrevista de trabajo, agencia de viajes, hotel, tienda, restaurante, servicio al cliente, reunión de '
             'equipo y primer día en un empleo.'),
            ('Los hitos, por número de clase: ',
             'Cl 26 MIDTERM · Cl 53 presentaciones finales MY LIFE (7 a 10 minutos + 2 o 3 preguntas del público) · Cl 55 '
             'examen FINAL en las últimas 2 horas, aplicado por un evaluador externo (para esas 2 horas no hay guia). El ensamble '
             'y el ensayo del proyecto caen en Cl 51-52.'),
            ('Cómo llegan: ',
             'todos los hitos van DENTRO de la guia del día, sin día aparte ni marcador separado. En la Clase 1 el docente solo '
             'anuncia los números de clase del midterm y del final — nunca contenido, formato, notas ni resultados.'),
        ],
        due='antes de las 6:30 PM del día siguiente',
        sec7_extra=None,
    ),

    # ------------------------------------------------------------------ B1 4H
    dict(
        out='VERSION_2/B1_4H/SYLLABUS_B1_MASTERY_4H.docx',
        titulo='SYLLABUS — B1 MASTERY 4H',
        linea3=('Instrucciones para los dos docentes · 8:00 a 12:00 M, lunes a viernes · '
                '44 clases, 175 horas · Fecha de inicio: lo define coordinación'),
        sec1_titulo='1. DOS PISTAS, DOS DOCENTES, EL MISMO DÍA',
        sec1_intro=('Cada día de B1 Mastery son DOS clases seguidas de 110 minutos, con dos docentes distintos y una pausa entre '
                    'ellas. Conversación va primero, Gramática va segundo, siempre en ese orden, y cada docente recibe '
                    'únicamente la guia de su pista.'),
        sec1_tabla=[
            ['Pista', 'Docente (lo asigna coordinación)', 'Cuándo', 'Qué hace'],
            ['CONVERSACIÓN', 'Docente de Conversación', 'PRIMERO: las 2 primeras horas',
             'Produce ORAL el módulo del día: historia, parejas, simulación profesional, avance del proyecto. No enseña la '
             'regla en papel.'],
            ['GRAMÁTICA', 'Docente de Gramática', 'SEGUNDO: las 2 últimas horas del mismo día',
             'Sella EN PAPEL lo que salió oral esa mañana: regla del libro citada en el tablero, drill, ejercicio escrito y una '
             'simulación DISTINTA. Bloques 1 a 3 DE PIE: piso 70%, validado en 86%.'],
        ],
        sec1_anchos=[2.6, 3.4, 3.4, 7.6],
        sec1_cierre=('La tarea también se reparte y no se negocia: la de Conversación es el VIDEO del portafolio, la ESCRITA es de '
                     'Gramática. Nunca se piden dos escritas el mismo día.'),
        sec2_titulo='2. EL PASE ENTRE LOS DOS (lo que hace que esto funcione)',
        sec2=[
            ('Conversación → Gramática, el mismo día: ',
             'al terminar su bloque, el docente de Conversación escribe el PASE en 3 líneas — lo que salió bien, los 3 errores '
             'más repetidos y qué quedó pendiente del módulo — y lo manda por el grupo antes de la pausa. Gramática lo lee '
             'antes de entrar y abre con eso: "esto salió de sus bocas esta mañana; ahora lo sellamos en papel".'),
            ('Gramática → Conversación, para el día siguiente: ',
             'al cerrar la jornada, Gramática devuelve el PASE — qué quedó sellado y qué sigue frágil — y con eso '
             'Conversación abre la mañana siguiente. Si el PASE va en una sola dirección, no está funcionando.'),
            ('Regla dura: ',
             'la simulación de Gramática NUNCA repite la de Conversación del mismo día. Mismo punto gramatical, escenario '
             'distinto. Si los estudiantes sienten que es "la misma clase otra vez", falló el PASE.'),
            ('Además, cada pista abre con continuidad: ',
             'recuperación espaciada de la Clase N-3 y N-7 (3 a 5 disparadores orales, DE PIE, en cadena, sin cuaderno) y el error '
             'paper del día anterior al tablero, anónimo.'),
        ],
        grabador='el docente de Conversación, que va primero',
        video_min='3 minutos',
        hora_inicio='8:00',
        hora_tarde='8:15',
        ingles=('100% inglés desde el Bloque 2 de la Clase 1, en las dos pistas. El español solo para el cronograma, los rituales '
                'y la Carta o la Cápsula en la primera clase.'),
        pase_reporte=True,
        sec5_titulo='5. EL PLAN DEL NIVEL (para que los dos lo tengan en la cabeza)',
        sec5=[
            ('Lo que el nivel entrega: ',
             'consolida toda la gramática en contexto profesional y agrega la del nivel — question tags, deducción, tercer '
             'condicional, "debí haber / pude haber", conectores de causa y contraste, preguntas indirectas, discurso indirecto y '
             'tiempos perfectos. Situaciones: briefings, entrevistas, onboarding, coordinación de horarios, planeación de '
             'proyectos, evaluaciones de desempeño, negociación con proveedores, recepción y reportes.'),
            ('Los hitos, por número de clase: ',
             'Cl 10 y Cl 18 entrevista simulada · Cl 22 MIDTERM "My Story, My Goals" (5 minutos por estudiante) · Cl 28 y Cl 35 '
             'negociación · Cl 31 y Cl 38 debate · Cl 40 a Cl 42 taller de pitch · Cl 43 presentaciones finales en formato '
             'panel tipo Shark Tank (3 minutos ante 3 compañeros que preguntan) · Cl 44 examen FINAL en el bloque de Gramática '
             '(últimas 2 horas), aplicado por un evaluador externo (para esas 2 horas no hay guia).'),
            ('Cómo llegan: ',
             'dentro de la guia del día de la pista que corresponda, sin día aparte ni marcador separado. En la Clase 1 solo se '
             'anuncian los números del midterm y del final — nunca contenido, formato, notas ni resultados. PLAN DE GERENCIA '
             '28/09/2026: la ubicación de entrevistas, negociación, debate, taller de pitch y el formato panel de Cl 43; el '
             'midterm de Cl 22 y el final de Cl 43-44 ya venían desde la guia de Clase 1.'),
        ],
        due='antes de las 8:00 AM del día siguiente',
        sec7_extra=('El bloque de Gramática se dicta DE PIE (piso 70%) y el movimiento siempre lleva contenido.'),
    ),

    # ------------------------------------------------------------------ B2 2H
    dict(
        out='VERSION_2/B2_2H/SYLLABUS_B2_NOCTURNO_2H.docx',
        titulo='SYLLABUS — B2 NOCTURNO 2H',
        linea3=('Instrucciones para el docente del cohorte · 6:30 a 8:30 PM, lunes a viernes · '
                '100 clases, 200 horas · Fecha de inicio: lo define coordinación'),
        sec1_titulo='1. CÓMO FUNCIONA EL COHORTE',
        sec1_intro=('B2 no tiene libro nuevo: las estructuras ya se aprendieron en B1 y aquí se vuelven reflejo. El nivel es '
                    'netamente conversacional — el docente modela, corrige al vuelo y exige en la simulación, y jamás explica '
                    'gramática en tablero como lección. El reparto de los cuatro bloques es B1 20-25\' · B2 40-45\' · '
                    'B3 35-40\' · B4 15-20\'.'),
        sec1_tabla=[
            ['Dato', 'Cómo es en este cohorte'],
            ['Formato y horario', '2 horas diarias, lunes a viernes, 6:30 a 8:30 PM. 100 clases, 200 horas.'],
            ['Docente', 'Un solo docente dicta todo el nivel. El docente asignado lo define coordinación.'],
            ['Contenido', 'Sin libro nuevo: el nivel avanza por CONTEXTOS de uso (la guia del día trae el contexto y las '
                          'expresiones). Cada noche, además: banco de vocabulario de 6 a 8 expresiones, siempre distintas a las de '
                          'las noches anteriores, y trabalenguas de vocalización.'],
            ['Escritura', 'Toda escritura evaluable se hace A MANO y EN EL AULA, nunca como tarea en casa. Es la regla anti-fraude '
                          'del nivel y no tiene excepciones.'],
            ['Proyecto del nivel', 'Arranca desde las primeras clases y se arma en Cl 81-97. Se presenta en Cl 98-99, de 7 a 10 '
                                   'minutos más preguntas.'],
        ],
        sec1_anchos=[3.6, 13.4],
        sec1_cierre=None,
        sec2_titulo='2. LA CONTINUIDAD ENTRE CLASES (lo que hace que esto funcione)',
        sec2=[
            ('Al abrir cada clase, la recuperación espaciada: ',
             '3 a 5 disparadores de la Clase N-3 y de la Clase N-7, orales, DE PIE, en cadena, sin cuaderno — en B2 son '
             'mini-situaciones, no preguntas de gramática. Los errores que se oigan van al tablero anónimos y se re-producen '
             'correctos en 1 minuto.'),
            ('Enseguida, el error paper de la noche anterior: ',
             '4 a 6 errores REALES del grupo, anónimos, en el tablero; el grupo diagnostica y reconstruye, y cada estudiante '
             'produce un ejemplo nuevo propio. Errores reales o no se usan.'),
            ('Y el chequeo de portafolio: ',
             'con la lista en mano, quién envió el video y la mejora anotada de cada uno. En la Clase 1 el ritual solo se '
             'presenta; el primer chequeo público es en la Clase 2.'),
            ('El registro acumulado: ',
             'el banco de vocabulario es acumulativo — el set de cada noche es distinto de todos los anteriores, y el set del '
             'día reaparece obligatorio en la simulación o en la tarea de esa misma noche.'),
        ],
        grabador='el docente',
        video_min='5 minutos',
        hora_inicio='6:30',
        hora_tarde='6:45',
        ingles=('100% inglés desde el Bloque 2 de la Clase 1 — en B2, en la práctica, desde el primer minuto. El español '
                'solo para el cronograma, los rituales y la Carta en la primera clase.'),
        pase_reporte=False,
        sec5_titulo='5. EL PLAN DEL NIVEL (para que el docente lo tenga en la cabeza)',
        sec5=[
            ('FASE 1 — Cl 1 a Cl 20, la vida real a toda velocidad: ',
             'quejas en un restaurante, direcciones, compras y devoluciones, médico, arriendo, llamadas, aeropuerto, banco, '
             'vecinos, problemas técnicos y desacuerdos.'),
            ('FASE 2 — desde Cl 21, el mundo profesional: ',
             'presentarse y hacer networking, el CV en 3 minutos, entrevistas (preguntas clásicas y difíciles), reuniones, '
             'presentar una idea en 3 minutos, dar buenas y malas noticias, cliente molesto, negociación (cotizar y cerrar '
             'acuerdo), decir que no, asumir un error, dar y recibir feedback, conflicto de equipo, pitch de 90 segundos, '
             'reunión remota y pedir un aumento.'),
            ('Los hitos, por número de clase: ',
             'Cl 50 MIDTERM (presentación de 5 minutos) · alrededor de Cl 60, ESCRITURA EN CLASE del perfil de LinkedIn en '
             'inglés, a mano y en el aula — PLAN DE GERENCIA 28/09/2026 · Cl 51-80 dominio bajo presión (debates, '
             'improvisación) · Cl 81-97 armado del proyecto final · Cl 98-99 presentaciones finales (7 a 10 minutos + '
             'preguntas) · Cl 100 examen FINAL, aplicado por un evaluador externo (ese día no hay guia). El nivel cierra con un '
             'simulacro integrador de una jornada de trabajo completa en inglés. Al terminar B2 con el programa completo entra el '
             'REFUERZO PRO.'),
            ('Cómo llegan: ',
             'todos los hitos van DENTRO de la guia del día, sin día aparte ni marcador separado. En la Clase 1 el docente solo '
             'anuncia los números de clase del midterm y del final — nunca contenido, formato, notas ni resultados.'),
        ],
        due='antes de las 6:30 PM del día siguiente',
        sec7_extra=('Banco de vocabulario y trabalenguas cada noche, siempre nuevos. Toda escritura evaluable, a mano y en el aula. '
                    'Las simulaciones son físicas y de pie, nunca roleplay sentado.'),
    ),
]


# ----------------------------------------------------------------------------- render
def build(cfg):
    d = Doc()
    d.titulo(cfg['titulo'], 'Cómo funciona este cohorte y qué hace cada docente', cfg['linea3'])

    # 1
    d.sec(cfg['sec1_titulo'])
    d.t(cfg['sec1_intro'])
    d.tabla(cfg['sec1_tabla'], cfg['sec1_anchos'])
    if cfg.get('sec1_cierre'):
        d.t(cfg['sec1_cierre'], bold=True, after=2)

    # 2
    d.sec(cfg['sec2_titulo'])
    for bold_txt, txt in cfg['sec2']:
        d.b(bold_txt, txt)

    # 3 (compartida, parametrizada)
    d.sec('3. LO NUEVO DESDE ESTE COHORTE')
    d.b('Grabación oral de entrada (solo Clase 1): ',
        '%s graba a cada estudiante 1 a 2 minutos hablando, mientras el resto trabaja. Es la foto de partida del nivel para la '
        'garantía. Esa misma noche se las envía a la auxiliar administrativa por WhatsApp, una por una con el nombre, y ella '
        'las guarda en el computador de la academia.' % cfg['grabador'])
    d.b('Portafolio = VIDEO diario, enviado: ',
        'cada estudiante graba un video de mínimo %s, hablado de corrido y sin leer, y lo envía el mismo día al grupo de '
        'WhatsApp del cohorte (donde están el docente y la auxiliar administrativa). El grupo ES el archivo del portafolio: los videos diarios no se descargan; solo se guardan en el computador de la academia la grabación de entrada, un video de hito cada 10 clases (Cl 10, 20, 30...: el docente reenvía a la auxiliar administrativa, con el nombre, el video de esa clase de cada estudiante) y la grabación de salida del nivel. Festivos: no hay clase, la siguiente clase se dicta el siguiente día hábil y las clases perdidas se recuperan al final del nivel hasta completar las horas. '
        'Ya no es audio y ya no se queda en el celular: audio solo por excepción, máximo 2 por semana. EL DOCENTE VE los '
        'videos antes de la clase y anota al menos UNA cosa por mejorar de cada uno — una frase, con el error real. En el '
        'chequeo de portafolio, con la lista en mano, marca quién ENVIÓ y le dice a cada uno su mejora en voz alta, en 5 '
        'segundos. Video recibido + mejora anotada van al reporte de la noche. Es la revisión más importante del día: el '
        'video es la clase particular de cada estudiante.' % cfg['video_min'])
    d.b('Puntualidad: ',
        'la clase empieza a las %s en punto. La llegada después de las %s se marca como LLEGADA TARDE en el reporte; cada 3 '
        'cuentan como una inasistencia para el contrato y la garantía. Se dice en la Clase 1 como parte de la formación: '
        'llegar a tiempo es lo que estamos entrenando, no un castigo.' % (cfg['hora_inicio'], cfg['hora_tarde']))
    d.b('Las condiciones de la garantía se dicen UNA vez, en Clase 1: ',
        'asistencia mínima 80%, 90% de tareas incluido el video diario, todas las evaluaciones. Después no se vuelven a '
        'explicar: se cumplen.')
    d.b('Inglés: ', cfg['ingles'])
    d.b('Feedback sí, notas no: ',
        'el docente da feedback TODOS los días y de frente: la mejora de cada video, el error paper, la corrección en la '
        'simulación, "esto te salió, esto te falta". Eso es lo que el estudiante más valora y es suyo. Lo único que el '
        'docente NO comunica son NOTAS y RESULTADOS de las evaluaciones (midterm, final, aprobó o no, garantía): eso lo '
        'comunica coordinación, para que nadie negocie una nota con su profesor. Si preguntan "¿cómo voy?", se responde con '
        'feedback concreto; si preguntan "¿qué nota saqué?", se responde "eso te lo dice coordinación".')

    # 4
    d.sec('4. EL REPORTE DE CADA CLASE (en la plataforma, al terminar la clase)')
    d.t('Se llena en la plataforma de reportes de la academia al salir de la clase, el mismo día, con estas piezas:')
    d.b('Asistencia ', 'con la columna de llegada tarde.')
    d.b('Videos recibidos ', 'del día anterior: quién envió, quién no, y la mejora anotada por cada video visto.')
    d.b('Error paper ', 'sin nombres (foto del papel) y el registro con nombres aparte, solo para coordinación.')
    d.b('Tickets de salida ', 'recogidos (foto, o entrega física al día siguiente).')
    if cfg['pase_reporte']:
        d.b('El PASE ', 'al otro docente, por el grupo.')

    # 5
    d.sec(cfg['sec5_titulo'])
    for bold_txt, txt in cfg['sec5']:
        d.b(bold_txt, txt)

    # 6
    d.sec('6. LAS VIRTUDES: POR QUÉ LAS HACEMOS Y CÓMO SE HACEN BIEN')
    d.t('Por qué, en tres frases que puedes repetir:', bold=True)
    d.b('Porque es lo que vendemos. ', 'Al estudiante no se le prometió inglés: se le prometió entrenamiento con garantía y un destino (un trabajo, irse, emprender). Lo que decide si llega a ese destino no es la gramática: es si aparece a tiempo, si sostiene el esfuerzo cuando ya no es novedad, si se atreve a hablar con miedo, si cumple lo que dijo. Eso es lo que un jefe, una familia de Au Pair o un cliente evalúan primero. Las virtudes son ese entrenamiento, con nombre.')
    d.b('Porque el inglés no se aprende sin ellas. ', 'Repetir mil veces lo mismo es templanza. Hablar frente a otros sabiendo que te vas a equivocar es fortaleza. Grabar el video el día que no quieres es prudencia y templanza juntas. Un estudiante que entiende que la virtud del bloque es lo que le va a permitir sostener el nivel, deja de ver el ritual como relleno.')
    d.b('Porque es lo que hace que se queden. ', 'El que abandona en la semana 3 no abandona por la gramática: abandona porque no tenía nombre para lo que le estaba pasando. Cuando el docente le dice "esto que sientes es la parte de fortaleza del nivel, y por eso la estamos entrenando", el estudiante se queda. La retención del grupo depende de esto más que de cualquier otra cosa que hagas.')
    d.t('Las cuatro, por calendario absoluto (bloques de 5 clases; Cl 1-5 Prudencia; la guía del día dice cuál sigue, y no se desplaza por festivos):', bold=True)
    d.b('PRUDENCIA: ', 'pensar antes de actuar, planear, decidir. En inglés: preparar lo que vas a decir antes de decirlo; elegir el tiempo verbal antes de abrir la boca.')
    d.b('FORTALEZA: ', 'coraje para hablar con miedo, iniciativa, no rendirse. En inglés: pedir la palabra, ser el guest en la simulación, grabar el video aunque salga mal.')
    d.b('TEMPLANZA: ', 'disciplina, manejo del tiempo, paciencia con la repetición. En inglés: el video diario, llegar a tiempo, hacer el drill completo sin atajos.')
    d.b('JUSTICIA: ', 'trabajo en equipo, liderazgo ético, empatía. En inglés: escuchar al compañero en la simulación, corregir sin humillar, ayudar al que va más lento.')
    d.t('Cómo se hace bien, en 5 a 7 minutos (el ritual VATS, al inicio de la clase):', bold=True)
    d.b('V, Virtud (1 min): ', 'el docente nombra la virtud del bloque y la conecta con lo de HOY en una frase: "Esta semana es fortaleza. Hoy la simulación es una entrevista: la fortaleza es contestar aunque no tengas la palabra perfecta."')
    d.b('A, Activar (2 min): ', 'una pregunta, en inglés, que junte la virtud con la gramática del día. Ejemplo con presente perfecto: "What is something you have done this year that took courage?" Cada uno piensa 30 segundos.')
    d.b('T, Hablar (2-3 min): ', 'en parejas o en cadena de pie, cada uno responde en una o dos frases. El docente escucha y anota errores para el error paper, no corrige aquí.')
    d.b('S, Compartir (1 min): ', 'dos o tres respuestas al grupo. El docente cierra con una sola frase que conecta: "That is why today you speak first and think second."')
    d.t('Lo que NO es: no es un sermón, no es una charla de motivación, no dura 15 minutos y no se salta cuando "no hay tiempo". Es una frase, una pregunta y las voces de ellos. Si el docente lo recorta, la clase pierde su hilo y el estudiante pierde la razón para volver mañana.')
    d.t('Cuando un estudiante pregunte "¿y esto qué tiene que ver con inglés?", la respuesta es esta:', bold=True)
    d.t('"Todo. Aquí no te estamos enseñando palabras: te estamos entrenando para el día que las necesites de verdad, en una entrevista, en un vuelo, frente a un cliente. Ese día no te va a fallar el vocabulario: te va a fallar el nervio, o la constancia, o la preparación. Eso es lo que entrenamos con las virtudes. Y es lo que hace que el que se gradúa aquí no solo hable inglés: se le nota."')

    # 7
    d.sec('7. LOS RITUALES Y POR QUÉ EXISTEN (lo que no cambia)')
    d.t('Ninguno de estos es un capricho ni una formalidad. Cada uno resuelve un problema concreto que ya nos costó estudiantes. El docente que entiende para qué sirve cada uno, lo hace bien; el que lo ve como regla, lo recorta.')
    d.b('La Frase del Día en el tablero, antes de que entren. ', 'QUÉ ES: una sola oración en inglés, escrita por la academia en la guía del día (el docente no la inventa), que junta la estructura gramatical de esa clase con la virtud de la semana. Ejemplo real, Clase 1 de este cohorte (módulo: pasado cerrado vs abierto; virtud: prudencia): "Prudence weighs the clock before it speaks: what I did last year is closed, and what I have achieved this year is still open." Ahí están el simple past, el present perfect y la prudencia en una frase que se puede decir en voz alta. CÓMO SE HACE, en orden: (1) el docente la escribe en el tablero ANTES de que entren los estudiantes, arriba y grande, y ahí se queda toda la clase; (2) en el Bloque 1 la lee dos veces, el grupo la repite en coro dos veces, y un estudiante la dice solo; (3) el docente la explica en una sola línea ("two pasts in one sentence: I did closes the door, I have done leaves it open"), sin clase de gramática; (4) durante la clase el docente la usa de forma natural al menos tres veces, en lo que dice; (5) al cierre, un estudiante la dice de memoria y otro la usa en una oración propia. Total: unos 4 minutos, repartidos. Por qué: una frase que se oye, se dice y se usa diez veces en contexto se queda; una lista de veinte palabras copiadas no. Es la forma más barata de repetición espaciada que existe, y es el ancla visible de toda la clase: el estudiante distraído levanta la vista y sabe de qué se trata hoy. Reemplazó a las listas de vocabulario en cuaderno, que nadie volvía a abrir. Cada clase estrena la suya; la de ayer va en el reporte solo como referencia.')
    d.b('El chequeo de portafolio, al abrir. ', 'Quién envió el video y una mejora dicha en voz alta a cada uno. Por qué: es el único momento del día en que cada estudiante recibe feedback personal, y es lo que hace que el video se grabe mañana también. Un portafolio que nadie ve muere en dos semanas.')
    d.b('La recuperación al abrir (lo de hace 3 y hace 7 clases). ', 'Dos o tres preguntas de pie sobre lo que se vio hace tres y siete clases, antes de lo nuevo. Por qué: lo que se recupera justo cuando se está olvidando se fija para siempre; lo que se vio una sola vez se pierde en diez días. Son tres minutos que valen una clase de repaso.')
    d.b('Cuatro bloques largos, no doce cortos. ', 'Por qué: hablar un idioma exige tiempo sostenido en una misma situación; con actividades de ocho minutos el estudiante nunca llega a la parte difícil, que es donde se aprende.')
    d.b('La simulación con un guest, observadores con tarea y el docente como coach (nunca como guest). ', 'Por qué: el estudiante que hace de guest vive la situación real (una entrevista, una queja, una negociación) y los que observan trabajan con una ficha, así nadie mira el techo. Si el docente hace de guest, la simulación se vuelve una conversación con el profesor, que es justo lo que el estudiante ya sabe hacer.')
    d.b('El error paper: anónimo en el tablero, con nombres solo para coordinación. ', 'Por qué: el error sin nombre se corrige entre todos y nadie se avergüenza, así que la próxima vez se atreven a hablar igual; el registro con nombres le permite a coordinación ver quién repite qué y actuar antes de que se vuelva un retiro.')
    d.b('El ticket de salida, en los últimos 5 minutos. ', 'Tres a cinco frases escritas por cada estudiante con la estructura de hoy, con nombre, sin calificar. Por qué: es la evidencia diaria de que cada uno aprendió lo de ese día, sin depender de la opinión de nadie. Es lo que sostiene la garantía y lo que le muestra a coordinación quién va y quién no. Se recogen todos: un ticket que falta es una señal.')
    d.b('La tarea con hora de entrega, sin excepciones. ', 'Por qué: la constancia no se enseña con discursos, se entrena con fechas que se cumplen. Y la hora fija (antes de la clase siguiente) evita el "te lo mando después", que es el principio del abandono.')
    d.b('Cero material impreso: todo en el tablero, en el papel del estudiante o dictado. ', 'Por qué: sin hoja, la atención está en el docente y en hablar; con hoja, el estudiante lee en vez de escuchar. Y el material de Heiiu es propiedad intelectual de la academia: la guía es solo para el docente y no se fotografía ni se comparte.')
    d.b('Sin nombres de estudiantes en las guías, sin nombres de metodologías frente a ellos, sin notas de boca del docente. ', 'Por qué: la guía es reutilizable y no lleva casos personales; los nombres de las técnicas son de la academia y no se enseñan; y las notas van por coordinación para que ningún estudiante negocie su resultado con su profesor.')

    if cfg.get('sec7_extra'):
        d.t(cfg['sec7_extra'], bold=True, after=2)

    d.pie()
    out = os.path.join(RAIZ, cfg['out'].replace('/', os.sep))
    d.save(out)
    return out


if __name__ == '__main__':
    for cfg in COHORTES:
        p = build(cfg)
        print('OK  %7d B  %s' % (os.path.getsize(p), p))
