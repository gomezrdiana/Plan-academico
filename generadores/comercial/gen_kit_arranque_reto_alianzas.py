# -*- coding: utf-8 -*-
"""KIT DE ARRANQUE del RETO DE 15 DÍAS (20/10 al 3/11/2026) para el ejecutivo de alianzas.
Lo lee el domingo y lo lleva el lunes. Redactado POR ROL (ejecutivo de alianzas / coordinación / gerencia), en tú,
sin nombres de personal ni de candidatos. Máximo 6 páginas.
Fuentes: INFO_ACADEMIA_PARA_ASISTENTE.md (§1-§7), ANEXO_KIT_PACTO_Y_PERFILACION.docx, B2B/ (PITCH, PROPUESTA,
ESTRATEGIA_PRO, ANTES_DE_SALIR, COMPARATIVO, CARTA v3, CONVENIO v1, ORDEN v1), gen_propuesta_ejecutiva_alianzas_candidata.py,
GUION_CIERRE_EN_CITA.md, DUDAS_Y_ACLARACIONES.md. Lo que no está en las fuentes va marcado SUPUESTO — verificar con gerencia.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/KIT_ARRANQUE_RETO_15_DIAS_ALIANZAS.docx (+ PDF vía Word COM).
Correr desde la raíz: python generadores/comercial/gen_kit_arranque_reto_alianzas.py"""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial'
SUP = 'SUPUESTO — verificar con gerencia'

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.5); s.bottom_margin = Cm(1.5); s.left_margin = Cm(1.5); s.right_margin = Cm(1.5)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)
doc.styles['Normal'].element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
doc.styles['Normal'].paragraph_format.space_after = Pt(2)

# pie de página
fp = doc.sections[0].footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = fp.add_run('Heiiu English Academy · Kit de arranque · Reto de 15 días · Ejecutivo de alianzas · Uso interno y confidencial: no se entrega a empresas ni a clientes')
fr.font.size = Pt(7.5); fr.font.color.rgb = GRIS


def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)


def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(7); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(12.5); r.font.color.rgb = NAR


def sub(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NAR


def rich(p, txt, size):
    """**negrita** en línea."""
    partes = txt.split('**')
    for i, x in enumerate(partes):
        if x:
            r = p.add_run(x); r.font.size = Pt(size); r.bold = (i % 2 == 1)
    return p


def t(txt, size=10, color=None, after=2, italic=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    rich(p, txt, size)
    for r in p.runs:
        if color: r.font.color.rgb = color
        r.italic = italic
    return p


def caja(lines, size=9.5, italic=False):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    if isinstance(lines, str): lines = [lines]
    for i, x in enumerate(lines):
        p = c.paragraphs[0] if i == 0 else c.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        rich(p, x, size)
        if italic:
            for r in p.runs: r.italic = True
    gap()


def gap(pts=1):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(''); r.font.size = Pt(pts)
    p.paragraph_format.line_spacing = Pt(pts + 2)


def bullets(items, size=9.5):
    for x in items:
        p = doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0)
        rich(p, x, size)


def tabla(hdr, filas, anchos, size=8.5, first_bold=True):
    tb = doc.add_table(rows=1, cols=len(hdr)); tb.style = 'Table Grid'
    for i, h in enumerate(hdr):
        c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = BLANCO
    for fila in filas:
        row = tb.add_row().cells
        for i, txt in enumerate(fila):
            row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
            rich(row[i].paragraphs[0], txt, size)
            if first_bold and i == 0:
                for r in row[i].paragraphs[0].runs: r.bold = True
    for row in tb.rows:
        for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    gap()
    return tb


# ---------------------------------------------------------------- PORTADA
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('KIT DE ARRANQUE — RETO DE 15 DÍAS · ALIANZAS EMPRESARIALES'); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(5)
r = p.add_run('Heiiu English Academy · Para el ejecutivo de alianzas · Del lunes 19 de octubre al martes 3 de noviembre de 2026 · Léelo completo antes de responder al reto')
r.font.size = Pt(9.5); r.font.color.rgb = GRIS
caja(['**Tu meta:** 10 personas inscritas y pagadas, **o $30.000.000 en caja** de Heiiu, lo que llegue primero, al martes 3 de noviembre a las 6:00 p. m., traídas por ti: empresas, referidos o conocidos, de cualquier programa (completo, parcial, Arranque, plan empresa o inglés para empresarios). Cada persona queda registrada en tu planilla antes de pagar. Inscrito pagado = pagó de contado, o pagó la inicial de su plan de pagos y firmó el contrato con coordinación. Caja = dinero verificado en la cuenta de Heiiu. Lo ideal es de contado: 7 completos de contado ya son la meta.',
      '**Tu trabajo:** contactas al dueño o gerente, te reúnes con quien decide, y cierras tú mismo: lo preferido es que la empresa invierta (plan empresa); si no, la charla de 20 minutos a sus empleados y la inscripción de cada uno con la beca de alianza. El pago entra a Heiiu, de contado idealmente. El estudiante firma el contrato con coordinación en la sede, y pagaré solo si va a cuotas.',
      '**Tu rutina fija:** 15 minutos con gerencia todos los días a las **8:30 a. m.** (el lunes 19 en la sede, después por llamada): rutina del día, dudas, sugerencias, recomendaciones e indicadores si los hay. La planilla FORMATO_15_EMPRESAS_RETO.xlsx siempre al día antes de esa llamada.',
      '**Este kit es la base.** Los guiones de reunión y de charla son nuestra sugerencia: tú tienes la experiencia y los adaptas. Lo que no cambia: qué se ofrece, los precios, lo que no se promete y las reglas.'], size=9.5)

# ---------------------------------------------------------------- 1
sec('1. Heiiu en 10 líneas')
bullets([
 'Academia de inglés **presencial** en Bucaramanga (Carrera 27 # 48-49, barrio Sotomayor, segundo piso). La marca es Heiiu; "Global Teacher S.A.S." solo en documentos legales.',
 'Institución de educación para el trabajo y el desarrollo humano **con licencia desde 2012**; programas registrados ante la Secretaría de Educación (Resoluciones 1581-1131 y 2253-2025).',
 '**Triple certificación de calidad ICONTEC** (NTC 5555, NTC 5580 e ISO 9001). Es una certificación, no una exclusividad.',
 '**Niveles:** A1 (90 h) · A2 (110 h) · B1 (175 h) · B2 (200 h). Programa completo A1 a B2 = **575 horas** presenciales. Certificado oficial por cada nivel aprobado y factura al matricularse.',
 '**Próximo grupo (confirmado por gerencia):** abre el martes 3 de noviembre. Jornada de mañana, tarde o noche, de 2 o de 4 horas diarias: el horario lo definen los primeros que se matriculen; una empresa con 8 cupos o más define su propio horario. Para entrar el 3 de noviembre, el pago tiene que estar hecho antes de esa fecha. Sábados de 8:00 a 12:00, un nivel a la vez.',
 '**Cómo son las clases:** presenciales, en grupos de máximo 16, con método activo y práctico; video corto diario en inglés que el profesor revisa; una virtud por bloque (sección 2).',
 '**El programa exige trabajo fuera de clase:** el video diario, escuchar podcasts en inglés y tareas cortas. Se dice antes de que firme.',
 '**Edades:** no vendemos a menores de 12 años. De 12 a 17, por lo general solo el sabatino; entre semana solo si el joven y el acudiente se comprometen al trabajo diario fuera de clase. El acudiente firma.',
 '**Convenio con Cajasan** (no exclusivo): el afiliado entra a la columna más alta del Fondo de Becas. Nunca "los únicos con Cajasan".',
 '**Nuestra causa** (para la reunión con el dueño o gerente): educativa, formar a jóvenes y trabajadores de Santander a través del inglés con valores y disciplina; empresarial, las empresas locales pueden ganar con calidad, resultados que se pueden mostrar y garantía por escrito.'], size=9)

# ---------------------------------------------------------------- 2
sec('2. Lo que nos diferencia (esto es lo que vendes)')
tabla(['Diferencia', 'Qué es y cómo se dice'], [
 ('Garantía de aprendizaje por escrito', 'Texto único: "Si cumples — asistencia, tareas, evaluaciones — y no avanzas, te devolvemos el 100% del nivel. Por escrito, en el contrato." Es lo único que se dice como "la única academia PRESENCIAL de Bucaramanga". Condiciones que el estudiante firma: asistencia (hasta 20% de faltas por nivel; con incapacidad médica no cuentan), tareas al 90% y todas las evaluaciones. Si falta, recupera hasta dos clases al mes en el taller de los sábados. Tres llegadas tarde de más de 15 minutos suman una falta. Retracto: 5 días hábiles por ley; después no hay devolución por retiro, solo por garantía.'),
 ('Mentor, entrenamiento y grupo selectivo', 'Aquí el profesor no dicta: entrena. Es tu mentor: te corrige, te pide cuentas y no te suelta; revisa tu video diario y te lo devuelve con una mejora. Y el grupo es selectivo por El Pacto (sección 3): entra quien acepta entrenar así. Por eso el resultado se puede garantizar.'),
 ('Módulo de Graduación', 'Al terminar A2 (incluido en el Arranque y en el completo), a elección. **Emprendedor:** sale con su página web publicada en inglés, su pitch y su primer mensaje de venta a un cliente real. **Pasaporte:** sale con el video de presentación, la hoja de vida en inglés, la entrevista ensayada y la postulación al exterior lista. Con el completo, además, Refuerzo PRO al final de B2. Se describen, nunca se promete un resultado. Dilo en toda charla: es lo que diferencia el programa de un curso.'),
 ('Virtudes', 'Cada bloque de clases trabaja una de cuatro virtudes: prudencia (pensar y planear), fortaleza (iniciativa, hablar en público, asertividad), templanza (disciplina, manejo del tiempo, paciencia) y justicia (trabajo en equipo, liderazgo, empatía). Se practica con un ritual corto al inicio de cada clase, en inglés. Cómo decirlo: "Aquí no solo sale hablando inglés: sale con más disciplina y más seguridad para hablar en público. Las empresas lo notan."'),
], [3.6, 14.4], size=8.5)

# ---------------------------------------------------------------- 3
doc.add_page_break()
sec('3. El Pacto y la proyección por motivo')
t('No vendemos inglés fácil ni rápido. Vendemos **entrenamiento + destino**, y el cliente firma advertido. Se dice a todos, antes de dar precios:', after=1)
caja('"Antes de contarte precios, te cuento cómo es esto, para que decidas con todo claro. Nuestro objetivo es que salgas hablando inglés; si no se logra, algo está mal: o tú dejaste de entrenar, o nosotros no estamos cumpliendo. Esto es un entrenamiento en equipo, como un gimnasio o aprender a nadar: desde el primer día practicas, tu profesor identifica dónde puedes mejorar y lo repetimos hasta que sale. Por eso grabas un video corto todos los días, escuchas podcasts en inglés y haces tareas cortas, y tu profesor te devuelve el video con una mejora. A cambio, la garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel. ¿Te le mides a ese ritmo?"', italic=True)
t('Si dice "busco algo más suave": "Te agradezco la sinceridad. Este programa es exigente a propósito, y prefiero decírtelo ahora a que lo descubras en la segunda semana." Fin, sin reintentos. Jamás: fácil, rápido, divertido, "en tres meses hablas", nativos, empleo, visa.', size=9)
tabla(['Motivo', 'Proyección (2 o 3 frases; emocionar no es prometer)'], [
 ('Trabajo / ascenso', '"La vacante que hoy pasas de largo porque pide inglés, y que ahora sí aplicas; la reunión donde entra alguien de afuera y tú eres quien responde. El inglés no te da el puesto: te quita la excusa que hoy te lo cierra." Se vende preparación, jamás empleo.'),
 ('Viaje', '"Para un viaje entrenamos justo lo que vas a vivir: resolver cosas tú mismo, entender lo que te dicen y responder sin traductor." Vacaciones: el Arranque sirve.'),
 ('Estudio o trabajo afuera', '"El módulo Pasaporte te deja el video de presentación, la hoja de vida y la entrevista ensayada." Va al programa completo. Traslado definitivo durante el nivel: no se vende.'),
 ('Montar un negocio', '"Tu negocio con una página en inglés publicada y un cliente de afuera que te escribe y le respondes sin traductor. Con eso sales del módulo Emprendedor."'),
 ('Su hijo o hija (12 a 17)', '"Imagínate a tu hijo a los 18 con el inglés resuelto: la universidad o la beca sin ese requisito pendiente, o su primer trabajo cobrando más. Y lo que los papás más nos agradecen: aquí se entrena disciplina y constancia." Por lo general el sabatino; entre semana solo con compromiso de trabajo diario. Menores de 12: no.'),
], [3.2, 14.8])

# ---------------------------------------------------------------- 4
sec('4. Qué se ve en cada nivel y los dos caminos')
tabla(['Nivel', 'En lenguaje de la vida real'], [
 ('A1 (90 h)', 'Presentarse, números, hora, rutina, familia, profesiones, ciudad; presente, pasado simple, planes. Cierra con la presentación "MY WORLD".'),
 ('A2 (110 h)', 'Futuro, condicionales, pasados, presente perfecto; entrevista de trabajo, viajes, hotel, servicio al cliente. Cierra con la presentación "MY LIFE" y el Módulo de Graduación.'),
 ('B1 (175 h)', 'Gramática en contexto profesional: briefings, entrevistas, onboarding, planeación, negociación. Hitos: "MY STORY, MY GOALS" y presentaciones finales.'),
 ('B2 (200 h)', 'Conversacional y profesional: vida real (quejas, médico, banco) y mundo laboral (networking, entrevistas, presentar una idea, negociación, pedir un aumento). Cierra con un simulacro de jornada de trabajo. Con el programa completo: Refuerzo PRO.'),
], [2.6, 15.4], size=8.5)
t('**Los dos caminos** (flyer "Dos caminos", en tu carpeta): el Arranque (A1+A2, 200 horas, con Módulo de Graduación) para quien empieza y quiere defenderse; el programa completo (575 horas, garantía y Refuerzo PRO) para quien tiene una meta profesional. Se muestra el flyer, se explica en un minuto y se pregunta: "¿cuál es tu meta?".', size=9)

# ---------------------------------------------------------------- 5
sec('5. El mensaje al dueño o gerente: lo escribes tú')
t('Tú sabes cómo se le escribe a un gerente; el texto es tuyo. Antes de mandarlo, léelo como si fueras el gerente: si tú no le contestarías, no lo mandes. Lo que sí tiene que cumplir:', after=1)
bullets([
 '**Un solo pedido:** 15 minutos con él. La charla con su gente se pide en la reunión, no en el mensaje.',
 '**No abre con "academia de inglés" ni con que alguien paga.** Abre con lo que gana él: un beneficio de formación para su gente, con garantía por escrito, y becas con el nombre de su empresa. Lo del inglés se entiende; lo de la plata se explica en la reunión.',
 '**Nada de precios, descuentos ni "gratis".** Si menciona el costo para la empresa, la frase es "sin costo para la empresa", nunca "sin costo de nómina".',
 '**Una frase de respaldo:** licencia desde 2012, certificación ICONTEC, garantía por escrito. Una, no las tres seguidas.',
 '**Cierra con dos opciones de día y hora.** No con "¿cuándo le queda bien?".',
 '**Empresas:** de 40 a 150 empleados donde el dueño o el gerente decide. Registra la empresa en la planilla antes de escribir.'], size=9)
t('Horario de contacto por iniciativa tuya: lunes a viernes de 7:00 a. m. a 7:00 p. m. y sábados de 8:00 a. m. a 3:00 p. m.; nunca domingos ni festivos; máximo un contacto al día por persona.', size=8.5, color=GRIS)

# ---------------------------------------------------------------- 6
sec('6. Reunión con el decisor: nuestra sugerencia (10 minutos)')
t('Tú tienes la experiencia y decides cómo llevarla. Lo que no cambia: el orden de preferencia (primero que la empresa invierta, después la alianza sin costo), qué firma cada modelo y qué no se promete.', size=9, after=1)
tabla(['Paso', 'Qué dices', 'Sales con'], [
 ('1. La causa (1 min)', '"Heiiu es una academia santandereana e independiente. Nuestra causa es doble: formar a la gente de Santander a través del inglés, con valores y disciplina, y demostrar que las empresas locales ganan con calidad y resultados que se pueden mostrar."', 'Su atención'),
 ('2. Qué gana su empresa (2 min)', 'Un beneficio de formación para su gente **sin costo para la empresa** (o con inversión, si quiere formar a su equipo); Becas con el nombre de su empresa (3 por trimestre, suben a 5 si todos sus becados cumplen) con certificado a su nombre; reporte periódico de asistencia y cumplimiento de sus becados (nunca notas); diagnóstico de nivel de inglés hasta 10 personas, sin costo.', 'Qué le importa más: formar o premiar'),
 ('3. Primero, plan empresa (2 min)', '"Si quiere formar a su equipo, la empresa paga los cupos: $4.782.800 por cupo de 3 a 7, $4.350.000 de 8 a 15, $3.950.000 de 16 a 30, de contado o con inicial y 3 cuotas. Usted escoge a quién y, con 8 o más, el horario es suyo." Es lo preferido: una decisión, una firma, un grupo.', 'Sí / no al plan empresa'),
 ('4. Si no, alianza sin costo (2 min)', '"Si prefiere no tocar presupuesto, firmamos la alianza: a la empresa no le cuesta nada y cada colaborador con su carta entra al programa completo a $4.782.800 de contado (lista $8.696.000) o $5.565.440 en cuotas." Y de una: "Para que sirva, le pido 20 minutos con su gente esta semana. ¿Martes o jueves?" Un convenio sin charla no produce nada: la charla se agenda en la misma reunión, y si talento humano no la mueve, la haces tú esa semana.', 'Fecha de la charla'),
 ('5. Qué firma (1 min)', '**Plan empresa:** la Orden Plan Empresa: elige tramo y forma de pago, designa a los colaboradores antes del inicio; queda en firme con la firma de gerencia y el pago inicial; precios vigentes 30 días. **Alianza:** el Convenio Heiiu Business Partner: 12 meses, sin costo ni obligaciones económicas; la empresa designa un contacto, emite las cartas de postulación y difunde el beneficio; no recibe ni gestiona pagos. Tú no firmas por Heiiu: firma gerencia.', 'Documento que va a firmar'),
 ('6. Cierre con fecha (1 min)', '"¿La hacemos el [día] a las [hora] o el [día] a las [hora]?" Y silencio. Toda reunión termina con algo: orden firmada, convenio firmado con fecha de charla, o un referido concreto.', 'Fecha en la planilla'),
], [3.0, 11.6, 3.4], size=8.5)
caja(['**Qué NO se promete en la reunión:** empleo, visa, ascensos ni "su equipo saldrá bilingüe en X meses" · profesores nativos · clases virtuales en grupo · reporte de notas (solo asistencia y cumplimiento; las notas las comunica coordinación al estudiante) · exclusividad · descuentos adicionales (los valores ya traen la beca) · horarios, plazos o precios fuera del convenio y de la orden · fechas de inicio sin confirmar con gerencia.',
      '**Lo que pasa a gerencia (se agenda, no se cotiza):** más de 30 cupos, grupo cerrado en la empresa con horario especial, copago con valores distintos, plazos distintos o cualquier condición que no esté escrita en la orden.',
      '**Si el dueño o gerente quiere inglés para él:** inglés para empresarios, personalizado, virtual, a su medida: $70.000 la hora, mínimo 30 horas ($2.100.000). Lo agendas con gerencia, que arma el plan con él.'], size=9)

# ---------------------------------------------------------------- 7
sec('7. La charla de 20 minutos a los empleados: nuestra sugerencia')
t('Es el camino cuando la empresa no invierte. Tú la adaptas; lo que no cambia es El Pacto antes de los precios, las opciones y el registro de interesados.', size=9, after=1)
tabla(['Minuto', 'Bloque', 'Qué haces'], [
 ('0-3', 'El destino', 'Pregunta a la sala: "¿Quién aquí necesita el inglés para el trabajo, para un viaje, para estudiar o para montar algo?" Toma dos respuestas y usa la proyección de esa persona (sección 3).'),
 ('3-6', 'El Pacto', 'El texto de la sección 3, completo, en voz alta. "Esto no es para todos, y está bien: es mejor saberlo hoy que en la clase 5."'),
 ('6-10', 'Lo que nos diferencia', 'Garantía con su texto exacto y sus condiciones; el profesor como mentor; el Módulo de Graduación en una frase (Emprendedor o Pasaporte); las virtudes en una frase. Cómo son las clases: presenciales, grupos de máximo 16, video diario, trabajo fuera de clase. El grupo abre el 3 de noviembre; mañana, tarde o noche, de 2 o 4 horas, y el horario lo definen los primeros que se matriculan.'),
 ('10-13', 'Precios: las opciones', 'La tabla de la sección 8, en este orden: lo que paga tu empresa (si firmó plan empresa), el completo con la beca de la alianza, y el Arranque solo para quien el completo no le alcance. "No manejamos descuentos: el precio es el precio."'),
 ('13-16', 'Cómo inscribirse hoy', 'Cierras ahí mismo con los que estén listos: "Hoy te doy tu número exacto, pagas (transferencia a la cuenta de Heiiu o tarjeta) y firmas en la sede con coordinación. Los primeros que se matriculan definen el horario del grupo."'),
 ('16-20', 'Preguntas y registro', 'Pasas la hoja de interesados (hoja INTERESADOS del formato, impresa): nombre, celular, motivo, jornada. Respondes con la sección 10. Con los que no cerraron hoy, dejas en el acto día y hora de tu llamada de seguimiento.'),
 ('Si la empresa ya compró los cupos', 'La charla cambia', 'No es de venta: son 10 minutos con los colaboradores designados para El Pacto, el horario del grupo y la fecha de inicio, para que nadie llegue sin saber a qué se comprometió. Al resto del personal se les ofrece la beca de la alianza: un cupo pagado por la empresa abre la puerta para vender más.'),
], [1.6, 3.2, 13.2], size=8.5)
t('El mismo día pasas los interesados a la planilla y guardas la hoja física para coordinación. No tomas fotos de la hoja, no creas grupos de WhatsApp con empleados y no compartes los datos con la empresa.', size=8.5, color=GRIS)

# ---------------------------------------------------------------- 8
sec('8. Hoja de precios')
tabla(['Opción', 'Para quién', 'Valor', 'Cómo se paga'], [
 ('1. Tu empresa paga tu cupo (Plan Empresa)', 'Solo si la empresa firmó la Orden Plan Empresa (existe desde 3 cupos; con menos, cada persona se matricula con la beca de alianza, y la empresa le paga si quiere)', 'Programa completo A1 a B2 por cupo: $4.782.800 (3 a 7 cupos) · $4.350.000 (8 a 15) · $3.950.000 (16 a 30)', 'Lo paga la empresa contra factura: de contado, o inicial (30% en el tramo de 3 a 7; 40% de 8 en adelante) y 3 cuotas mensuales. La empresa escoge a quién le da cada cupo y puede cambiar a la persona antes del inicio, sin cambiar de horario; iniciado el nivel, no.'),
 ('2. Pagas tú, con la beca de la alianza', 'Todo colaborador con carta de su empresa aliada', 'Completo A1 a B2 (lista $8.696.000): **$4.782.800 de contado** · **$5.565.440 a cuotas**', 'Contado: transferencia a la cuenta de Heiiu o tarjeta; crédito de banco o cooperativa y cesantías también cuentan como contado. Cuotas: inicial mínima del 20% ($1.113.088) y cuotas mensuales al 1,9%; firma pagaré. La cuota exacta la da coordinación con el motor de cuotas, nunca de memoria.'),
 ('3. Arranque A1+A2', 'Solo si el completo no le alcanza', '$2.990.000, precio único, sin beca. 200 horas, dos niveles certificados y Módulo de Graduación', 'Contado o máximo dos pagos: la mitad al inscribirse y la otra mitad antes de la primera clase; no hay más cuotas.'),
 ('4. Inglés para empresarios', 'El dueño o gerente que lo quiere para él', 'Personalizado, virtual, a su medida: **$70.000 la hora, mínimo 30 horas** ($2.100.000)', 'De contado. Tú lo agendas con gerencia, que arma el plan con él. Cuenta para tu comisión y para la caja de la meta.'),
], [3.4, 3.4, 4.6, 6.6], size=8.5)
bullets([
 '**Por qué "beca" y no "descuento":** el programa vale $8.696.000. Las becas las otorga el Fondo de Becas de la academia, según el perfil del estudiante y con soportes; la alianza con su empresa le da la columna más alta. Un descuento para todo el mundo no es descuento: es el precio, y así lo entiende la ley. Por eso nunca se dice "descuento" ni se suman dos becas: se aplica la mejor.',
 '**Becas con el nombre de la empresa** (las 3 que la empresa elige por trimestre): pagan $4.782.800 aunque vayan a cuotas, con libros y prioridad de cupo.',
 '**Ya sabe algo de inglés:** puede entrar a un grupo que ya va andando, pero eso lo define y lo cotiza gerencia, caso por caso; tú lo agendas, no lo cierras. La sesión de ubicación se coordina para el día siguiente, sin excepción. El foco del reto es la gente que empieza de cero: es lo más fácil de cerrar y lo que abre el grupo del 3 de noviembre.',
 '**Todo entra a Heiiu:** transferencia a la cuenta de Heiiu o tarjeta. Si el estudiante paga en efectivo, el efectivo llega a la sede ese mismo día y coordinación expide el recibo. Tú nunca te quedas con dinero.',
 '**Número de la cuenta de Heiiu** para dar en la charla: te lo entrega gerencia en la inducción del lunes 19. No lo escribas de memoria.'], size=9)

# ---------------------------------------------------------------- 9
sec('9. Proceso de inscripción paso a paso (cuando toca activación)')
t('Es el camino menos preferido: lo mejor es que la empresa invierta con el plan empresa. Cuando no, cada persona se inscribe así:', size=9, after=1)
tabla(['Paso', 'Qué pasa', 'Quién'], [
 ('1. Interesado', 'Queda en la hoja de la charla y ese mismo día en la planilla (hoja INTERESADOS).', 'Ejecutivo'),
 ('2. Cierre', 'Lo haces tú, en la charla o en el seguimiento (llamada o en la sede), en unos 20 minutos. Orden: motivo, para quién y quién decide, nivel, jornada, El Pacto, forma de pago; solo entonces el número exacto. "Ya sé algo": sesión de ubicación al día siguiente, sin excepción; gerencia define en qué grupo entra.', 'Ejecutivo'),
 ('3. Pago', 'De contado idealmente. Transferencia a la cuenta de Heiiu o tarjeta, con pantallazo del comprobante (la cédula se presenta en la sede, no se envía por chat); efectivo, a la sede el mismo día con recibo de coordinación. Para entrar el 3 de noviembre, pagado antes de esa fecha. Coordinación recibe y verifica el pago.', 'Estudiante · coordinación'),
 ('4. Contrato', 'El estudiante va a la sede. Allí, en físico: contrato de matrícula, anexo de garantía y, solo si va a cuotas, el pagaré (si requiere codeudor se define ahí). Menor de 18: firma el acudiente.', 'Coordinación'),
 ('5. Cupo', 'Grupo del 3 de noviembre; el horario lo definen los primeros matriculados (empresa con 8 o más: su propio horario). Plan Empresa: la orden la firma gerencia y la empresa designa a sus colaboradores; puede cambiar a la persona antes del inicio sin cambiar de horario.', 'Coordinación · gerencia'),
], [3.0, 12.0, 3.0], size=8.5)
caja(['**Qué cuenta para la meta:** inscrito pagado = pagó de contado, o pagó la inicial de su plan de pagos y firmó el contrato con coordinación; caja = todo lo que entre a la cuenta de Heiiu por tus ventas, de cualquier programa, **verificado por coordinación,** a más tardar el martes 3 de noviembre a las 6:00 p. m. En Plan Empresa, cada cupo cuenta cuando entra el pago inicial de la empresa por ese cupo.',
      '**No cuenta:** una promesa de pago, un pantallazo sin verificar, dinero que alguien te entregue a ti, ni el abono de separación de $300.000 solo. **Los que ya venían avanzados** y que la academia te entregue para cerrar: te pagan comisión, pero no cuentan para los 10.'], size=9)

# ---------------------------------------------------------------- 10
sec('10. Objeciones frecuentes: la respuesta corta')
tabla(['Te dicen', 'Respondes'], [
 ('"Está muy caro"', '"Te entiendo. Por eso existe la alianza: el programa completo vale $8.696.000 y por tu empresa lo pagas a $4.782.800 de contado, o a cuotas con una inicial del 20%. No manejamos descuentos: el precio de contado es el precio." Y si de verdad no le alcanza: el Arranque.'),
 ('"No tengo tiempo"', '"El grupo puede ser de mañana, tarde o noche, de 2 o de 4 horas diarias, y el horario lo definen los primeros que se matriculan: si te inscribes ya, ayudas a definirlo. ¿Tu horario es fijo?" Turnos rotativos: "Te lo digo de frente: el programa es de horario fijo y la asistencia es parte de la garantía; no te voy a vender algo que no te va a funcionar."'),
 ('"Ya sé inglés"', '"Perfecto: el nivel lo define la academia en una sesión de ubicación corta, mañana mismo, y entras en el nivel que te corresponde."'),
 ('"¿Es virtual?"', '"En grupo somos presenciales; virtual tenemos las clases personalizadas por videollamada, desde 30 horas, a tu horario, y las arma gerencia contigo."'),
 ('"Lo pienso"', '"¿Qué es lo que más te hace dudar: el precio, el horario o si de verdad vas a aprender?" Se responde eso y se deja la cita agendada. Nunca "aquí estaré cuando decidas".'),
 ('"Mi empresa no paga"', '"No tiene que pagar: la alianza no le cuesta nada a tu empresa. Con la carta de tu empresa entras a la beca más alta del Fondo, y el programa es tuyo, con tu contrato y tu garantía."'),
 ('"¿Y si no aprendo?"', 'La garantía, con su texto exacto. "Por escrito, en el contrato."'),
 ('"¿Clase de prueba?"', '"No manejamos clase de prueba: una clase suelta no te muestra si vas a aprender; lo que te lo garantiza es el contrato."'),
 ('"Es para mi hijo de 9"', '"Todavía no: empezamos desde los 12 años. Cuando los cumpla, el sabatino es el camino."'),
 ('Nombra otra academia', 'No repites su nombre ni hablas mal: "Allá se compra acceso, aquí se compra resultado." Lo anotas en la planilla.'),
], [3.4, 14.6], size=8.5)

# ---------------------------------------------------------------- 11
sec('11. Reglas innegociables')
bullets([
 'Solo los precios de este kit. Ningún descuento, beca, promoción, cupo, fecha ni condición distinta: lo que no está aquí, se agenda con gerencia.',
 'No hay clase de prueba. No hay clases virtuales en grupo. No se habla de profesores nativos ni del equipo docente: se vende método, mentor, respaldo y garantía.',
 'Nunca "fácil", "rápido", "gratis", "patrocinio", "descuento", "bilingüe en X meses"; nunca se promete empleo, visa ni resultado. Se dice "beca del Fondo" y "sin costo para la empresa".',
 'No se nombran otras academias. No se nombran métodos: se dice "clases inmersivas, activas y prácticas".',
 'Una sola fecha de inicio: martes 3 de noviembre. No se promete horario: lo definen los primeros matriculados. Menores de 12: no.',
 'Todo pago entra a Heiiu: transferencia o tarjeta; el efectivo llega a la sede el mismo día y coordinación expide el recibo. Nunca te quedas con dinero. Tú no firmas por Heiiu.',
 'Los datos personales de interesados y decisores van solo en la planilla y en la hoja física de la charla; no se comparten con nadie, tampoco con la empresa.',
 'Toda empresa queda registrada en el formato antes de la primera reunión.',
 '15 minutos con gerencia todos los días a las 8:30 a. m., sin cancelar. La planilla al día, todos los días, antes de esa llamada.'], size=9)

# ---------------------------------------------------------------- 12
sec('12. Ritmo del reto día a día')
tabla(['Fecha', 'Qué tiene que estar hecho'], [
 ('Lun 19/10', '8:00 a 10:00 a. m., inducción en la sede; 10:00, a la calle. Mensajes de contacto a tu lista; primeras reuniones agendadas.'),
 ('Mar 20/10', 'Corte de los días 1 y 2: **15 empresas contactadas con el decisor**, con nombre y cargo en la planilla.'),
 ('Mié 21 a vie 23/10', 'Reuniones. Corte de la semana 1: **8 reuniones con decisor y 3 charlas autorizadas** (o planes empresa en firma) para la semana 2, con fecha.'),
 ('Lun 26 a vie 30/10', 'Charlas, cierres e inscripciones. Recomendación: charlas hechas a más tardar el jueves 29, para que los pagos alcancen a entrar antes del corte y los inscritos puedan abrir grupo el 3 de noviembre.'),
 ('Lun 2/11', 'Festivo: no se contacta a nadie por iniciativa tuya.'),
 ('Mar 3/11', '**Corte a las 6:00 p. m.:** inscritos pagados y caja, verificados por coordinación. Planilla cerrada y cuenta de cobro. Ese mismo día abre el grupo del 3 de noviembre.'),
], [3.4, 14.6], size=8.5)
sub('Qué llevas en la maleta (todo está en tu carpeta)')
tabla(['Archivo', 'Para qué', 'Ojo'], [
 ('ORDEN_PLAN_EMPRESA_v1.pdf', 'Lo firma la empresa cuando paga los cupos', 'Queda en firme con firma de gerencia y pago inicial. La empresa puede cambiar a la persona solo antes del inicio y sin cambiar de horario.'),
 ('CONVENIO_HEIIU_BUSINESS_PARTNER_v1.pdf', 'Lo firma la empresa en la alianza sin costo', 'Firma por Heiiu el representante legal (gerencia). Se firma con fecha de charla.'),
 ('CARTA_POSTULACION_EMPRESA_ALIADA.pdf', 'Una por colaborador de empresa aliada', 'La emite la empresa; se entrega en la sede con el contrato. Sin carta no aplica la beca de alianza.'),
 ('Flyer dos caminos.pdf', 'Para mostrar en la charla y en el cierre', 'Arranque o completo: se explica en un minuto.'),
 ('FORMATO_15_EMPRESAS_RETO.xlsx', 'Tu planilla: empresas, reporte diario, interesados', 'Al día antes de las 8:30 de cada día.'),
], [6.2, 5.0, 6.8], size=8.5)
t('Además: este kit, 10 hojas INTERESADOS impresas y el número de cuenta que te entrega gerencia el lunes. Transporte y celular son tuyos. Para la cuenta de cobro del 3 de noviembre: RUT y documento de identidad vigente; coordinación te los pide el lunes.', size=9)

# ---------------------------------------------------------------- 13
sec('13. Tu compensación en el reto')
tabla(['Concepto', 'Cuánto', 'Cuándo y cómo'], [
 ('Honorarios del reto', '$1.000.000', 'Contra cuenta de cobro el 3 de noviembre. Se pagan pase lo que pase con la meta.'),
 ('Comisión', '10% de lo que entre a caja hasta el 3 de noviembre por tus inscritos', 'Se paga aunque no llegues a la meta. Si un inscrito paga inicial y cuotas, el 3 de noviembre se liquida el 10% de la inicial y el 10% de cada cuota cuando entra.'),
 ('Bono', '$1.000.000 de contado', 'Solo si llegas a la meta al 3 de noviembre a las 6:00 p. m.: 10 inscritos pagados o $30.000.000 en caja, lo que llegue primero.'),
 ('Los que ya venían avanzados', '10% de lo que entre', 'Si la academia te entrega a alguien ya avanzado para que lo cierres, te pagan comisión, pero no cuenta para los 10.'),
 ('Después del 3 de noviembre', 'Se define con el resultado', 'El 4 de noviembre, con los números del reto, gerencia y tú hablan de cómo seguir. El reto no obliga a nada más que lo escrito aquí.'),
], [3.6, 5.0, 9.4], size=8.5)
caja('Ejemplos con la meta cumplida: 7 completos de contado ($4.782.800 c/u) = $33.479.600 de caja = $5.347.960 para ti · 10 cupos pagados por la empresa ($4.350.000 c/u) = $6.350.000 para ti · 10 completos pagados por empleados ($4.782.800 c/u) = $6.782.800 · 10 Arranques ($2.990.000 c/u) = $4.990.000. Siempre: honorarios + bono + comisión.', size=9.5)

out = BASE + r'\KIT_ARRANQUE_RETO_15_DIAS_ALIANZAS.docx'
try:
    doc.save(out); print('OK', out)
except PermissionError:
    doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
