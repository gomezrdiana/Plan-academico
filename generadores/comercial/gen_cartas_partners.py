# -*- coding: utf-8 -*-
"""Cartas Business/Student Partner corregidas + hoja de condiciones Go Above and Beyond."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NARANJA = RGBColor(0xE5, 0x4C, 0x09)
GRIS = RGBColor(0x77, 0x77, 0x77)
CREMA = 'FFF8E7'
NARANJA_HEX = 'E54C09'
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\B2B'


def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd'); el.set(qn('w:val'), 'clear'); el.set(qn('w:fill'), color)
    tcPr.append(el)


def nuevo():
    doc = Document()
    for s in doc.sections:
        s.top_margin = Cm(2.0); s.bottom_margin = Cm(1.8); s.left_margin = Cm(2.3); s.right_margin = Cm(2.3)
    doc.styles['Normal'].font.name = 'Calibri'
    doc.styles['Normal'].font.size = Pt(11.5)
    return doc


def cabecera(doc):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run('heiiu'); r.bold = True; r.font.size = Pt(26); r.font.color.rgb = NARANJA
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run('· english academy ·'); r.font.size = Pt(10); r.font.color.rgb = GRIS
    doc.add_paragraph()


def pie(doc):
    doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run('Heiiu English Academy · heiiu.com · Carrera 27 # 48-49, segundo piso, Bucaramanga')
    r.font.size = Pt(9.5); r.font.color.rgb = GRIS


def parrafo(doc, txt, bold=False):
    p = doc.add_paragraph(); r = p.add_run(txt); r.font.size = Pt(11.5); r.bold = bold
    p.paragraph_format.space_after = Pt(10)
    return p


# ============ CARTA 1: BUSINESS PARTNER ============
doc = nuevo(); cabecera(doc)
parrafo(doc, 'Bucaramanga, ____ de septiembre de 2026')
parrafo(doc, 'Señor(a):\nGerente de Recursos Humanos — [Nombre de la empresa]')
parrafo(doc, 'Asunto: Alianza estratégica con Heiiu English Academy — Heiiu Business Partner', bold=True)
parrafo(doc, 'En Heiiu English Academy formamos estudiantes que buscan convertirse en la mejor versión de sí mismos aprendiendo inglés. Convencidos del potencial bilingüe de los equipos de trabajo de nuestra región, queremos invitar a [Nombre de la empresa] a convertirse en Heiiu Business Partner dentro de nuestra iniciativa Go Above and Beyond, que reconoce e incentiva el esfuerzo de los miembros destacados de nuestras empresas aliadas a través de becas de formación en inglés del Fondo de Becas institucional Heiiu.')
parrafo(doc, 'Como empresa aliada, [Nombre de la empresa] podrá usar estas becas como herramienta de reconocimiento para su equipo: sus colaboradores con ingresos de hasta 1.5 SMMLV podrán acceder, con carta de su empresa, al nivel más alto de beca del Fondo, y todo su equipo recibirá condiciones preferenciales de pago. La alianza no tiene ningún costo para la empresa: es una iniciativa de bienestar que usted entrega, y nosotros la respaldamos con licencia de funcionamiento desde 2012, programas registrados, certificación de calidad ICONTEC y una garantía de aprendizaje por escrito, única en la ciudad.')
parrafo(doc, 'Estamos atentos para agendar una reunión y presentarle las condiciones exactas del programa. Esperando una respuesta afirmativa, quedamos atentos durante los próximos días.')
parrafo(doc, 'Cordialmente,')
parrafo(doc, 'Gerencia — Heiiu English Academy', bold=True)
pie(doc)
doc.save(BASE + r'\CARTA_BUSINESS_PARTNER_v3.docx'); print('OK business')

# ============ CARTA 2: STUDENT PARTNER ============
doc = nuevo(); cabecera(doc)
parrafo(doc, 'Bucaramanga, ____ de septiembre de 2026')
parrafo(doc, 'Señor(a):\nGerente de Recursos Humanos — [Nombre de la empresa]')
parrafo(doc, 'Asunto: Alianza estratégica con Heiiu English Academy — Heiiu Student Partner', bold=True)
parrafo(doc, 'En Heiiu English Academy formamos estudiantes que buscan convertirse en la mejor versión de sí mismos aprendiendo inglés. Queremos invitar a [Nombre de la empresa] a convertirse en Heiiu Student Partner dentro de nuestra iniciativa Go Above and Beyond, que conecta a nuestros egresados destacados con empresas del sector real de la economía.')
parrafo(doc, 'Nuestros egresados destacados terminan su programa con nivel certificado por evaluador externo, un portafolio real de su progreso y un proyecto de graduación tangible. Como Heiiu Student Partner, su empresa tendrá acceso preferente a esa vitrina de talento: cuando abra vacantes que requieran inglés, le presentamos los perfiles destacados — con su video de presentación en inglés incluido — sin costo, sin exclusividad y sin ninguna obligación de contratación. La decisión siempre es suya; nosotros solo le acercamos talento verificado y le ahorramos la parte más lenta del reclutamiento bilingüe.')
parrafo(doc, 'Estamos atentos para agendar una reunión y presentarle el funcionamiento de la vitrina de egresados y los criterios con los que seleccionamos a los destacados. Esperando una respuesta afirmativa, quedamos atentos durante los próximos días.')
parrafo(doc, 'Cordialmente,')
parrafo(doc, 'Gerencia — Heiiu English Academy', bold=True)
pie(doc)
doc.save(BASE + r'\CARTA_STUDENT_PARTNER_v3.docx'); print('OK student')

# ============ CARTA 3: SCHOOL PARTNER ============
doc = nuevo(); cabecera(doc)
parrafo(doc, 'Bucaramanga, ____ de septiembre de 2026')
parrafo(doc, 'Señor(a):' + chr(10) + 'Rector(a) / Coordinador(a) Académico(a) — [Nombre del colegio]')
parrafo(doc, 'Asunto: Alianza Heiiu School Partner — el plan bilingüe para sus estudiantes de 8° a 11°', bold=True)
parrafo(doc, 'En Heiiu English Academy formamos estudiantes que buscan convertirse en la mejor versión de sí mismos aprendiendo inglés. Queremos invitar a [Nombre del colegio] a convertirse en Heiiu School Partner dentro de nuestra iniciativa Go Above and Beyond — una alianza sin ningún costo para el colegio, diseñada para sus estudiantes de 8° a 11°: desde la ruta bilingüe de los sábados (que no toca la jornada escolar) hasta la decisión más importante del grado 11 — qué sigue después del grado.')
parrafo(doc, 'La alianza incluye: (1) la HEIIU EXPERIENCE CLASS — no una charla: una clase real de inglés inmersivo de 45 minutos para su grado 11, en su colegio o en nuestra sede, donde sus estudiantes viven una simulación profesional hablando de pie desde el primer minuto; (2) el PREMIO HEIIU — una beca anual que su colegio entrega en su ceremonia de grado al estudiante más destacado en inglés, como reconocimiento del colegio a la excelencia; (3) el TALLER PARA PADRES de 8° a 11° — "el semestre que no se pierde": cómo convertir los meses entre el grado y la universidad en un nivel de inglés certificado, con garantía de aprendizaje por escrito; y (4) la ruta sabatina para 8°-10° (un nivel por año, los sábados, sin tocar la jornada escolar — el estudiante llega a grado 11 con nivel B1); y (5) condiciones preferenciales de pago para sus estudiantes y egresados.')
parrafo(doc, 'Nos respalda una licencia de funcionamiento desde 2012, programas registrados, certificación de calidad ICONTEC y la única garantía de aprendizaje por escrito de la ciudad. Estamos atentos para agendar una reunión de 20 minutos y coordinar la primera Experience Class de su grado 11.')
parrafo(doc, 'Cordialmente,')
parrafo(doc, 'Gerencia — Heiiu English Academy', bold=True)
pie(doc)
doc.save(BASE + chr(92) + 'CARTA_SCHOOL_PARTNER_v1.docx'); print('OK school')

# ============ DOC 3: CONDICIONES (uso interno / para la reunion) ============
doc = nuevo()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('GO ABOVE AND BEYOND — CONDICIONES DE LOS PROGRAMAS'); r.bold = True; r.font.size = Pt(16); r.font.color.rgb = NARANJA
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Uso interno — es lo que se presenta EN la reunión con la empresa · v1 14/09/2026 · Convenios: los firma gerencia'); r.font.size = Pt(10); r.font.color.rgb = GRIS
doc.add_paragraph()

def sec(txt):
    p = doc.add_paragraph(); r = p.add_run(txt); r.bold = True; r.font.size = Pt(13.5); r.font.color.rgb = NARANJA
    p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(4)

def item(txt, bold=False):
    p = doc.add_paragraph(); r = p.add_run(txt); r.font.size = Pt(11); r.bold = bold
    p.paragraph_format.space_after = Pt(4)

sec('1. HEIIU BUSINESS PARTNER (becas para su equipo)')
item('· Colaborador con ingresos hasta 1.5 SMMLV + carta de la empresa + desprendible de nómina = soporte válido para la BECA TRANSFORMACIÓN (techo 45%), dentro de los cupos trimestrales del Fondo.')
item('· Los demás colaboradores de la empresa aliada reciben el BENEFICIO DE CONVENIO: pagan a cuotas con el porcentaje de contado de su perfil.')
item('· REGLA DEL MEJOR BENEFICIO: los beneficios nunca se acumulan — si el colaborador califica a una beca superior del Fondo por su propio perfil, se le aplica la mejor.', bold=True)
item('· Todo pasa por el Reglamento del Fondo de Becas (administrado y auditado por contaduría externa): la empresa no paga nada; el colaborador paga su programa con su beca aplicada.')
item('· Compromisos de la empresa: designar un contacto de RRHH, emitir las cartas de postulación y difundir el beneficio internamente.')

sec('2. HEIIU STUDENT PARTNER (vitrina de egresados)')
item('· Qué es DESTACADO: nivel aprobado con evaluador externo + portafolio completo del programa (incluido su video de presentación en inglés) + concepto académico favorable.')
item('· Cuando la empresa abra vacantes que requieran inglés, Heiiu le presenta los perfiles destacados con su video — la empresa evalúa y decide.')
item('· Sin costo, sin exclusividad y SIN obligación de contratación. Heiiu conecta talento verificado; no actúa como bolsa de empleo ni intermediario laboral.', bold=True)
item('· A los estudiantes JAMÁS se les promete empleo: la vitrina se comunica como una puerta que se abre al que se destaca — nunca como garantía.')
item('· EXCLUSIÓN EXPRESA: el programa NO gestiona prácticas, pasantías ni contratos de aprendizaje — presenta EGRESADOS para vacantes ordinarias. Las figuras de práctica/aprendizaje tienen cargas legales propias (afiliaciones, cuota de aprendices, reforma laboral) y NO hacen parte de este programa. La palabra practicante no se usa en ninguna reunión.', bold=True)

sec('3. HEIIU SCHOOL PARTNER (colegios — grado 11)')
item('· HEIIU EXPERIENCE CLASS sin costo: una clase Heiiu REAL de 45 min para grado 11 (en el colegio o en la sede) — se vive, no se presenta. Nunca un stand en feria.')
item('· PREMIO HEIIU: beca anual al estudiante más destacado en inglés, entregada EN la ceremonia de grado del colegio — Heiiu presente en el escenario frente a los padres de familia. [Definir nivel de la beca: sugerido techo Transformación sobre el Arranque.]')
item('· Charla para padres de grado 11 (escuela de padres): "el semestre que no se pierde" — el gap entre el grado y la universidad convertido en A1+A2 completos con garantía escrita y Módulo de Graduación.')
item('· Convenio egresados: los graduados del colegio aliado reciben el beneficio de convenio (cuotas al porcentaje de contado) + prioridad de cupo en la cohorte de enero.')
item('· RUTA SABATINA 8°-10°: A1 en 8°, A2 en 9°, B1 en 10° (4h/sábado, por nivel individual, sin tocar la jornada escolar) — llega a grado 11 con B1 y su gap semestre es el B2 + Módulo de Graduación. Reglas de siempre del sabatino: por nivel suelto, sin beca, con descuento por forma de pago. Un estudiante de 8° capturado = 3-4 años de ruta.', bold=True)
item('· TIMING: este canal construye la cohorte de ENERO (grado 11 se gradúa en noviembre) — se siembra en septiembre-octubre. Piloto: 2-3 colegios con relación previa, nunca en frío los primeros.', bold=True)

sec('3. CANDADOS OPERATIVOS (internos — no se muestran a la empresa)')
item('· Las cartas y los convenios los firma GERENCIA. La búsqueda, presentación y gestión de empresas y colegios la ejecuta la ASESORA COMERCIAL — sin facultad de firmar convenios ni pactar condiciones fuera de las escritas.', bold=True)
item('· Todo convenio lo firma gerencia. El beneficio Transformación por empresa requiere el artículo 3.5 del Reglamento del Fondo (pendiente VoBo contaduría + abogado, en el mismo paquete del contrato de 30 cláusulas).')
item('· Los empleados becados que lleguen a matricularse los atiende la asesora comercial como leads calientes (kit, módulo 8).')
pie(doc)
doc.save(BASE + r'\CONDICIONES_GO_ABOVE_AND_BEYOND.docx'); print('OK condiciones')
