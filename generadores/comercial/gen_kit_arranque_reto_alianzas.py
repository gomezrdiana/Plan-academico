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
r = p.add_run('Heiiu English Academy · Para el ejecutivo de alianzas · Del lunes 20 de octubre al martes 3 de noviembre de 2026 · Léelo el domingo; llévalo el lunes')
r.font.size = Pt(9.5); r.font.color.rgb = GRIS
caja(['**Tu meta única:** 10 personas inscritas con la inicial pagada en la cuenta de Heiiu al martes 3 de noviembre a las 6:00 p. m., llegadas a través de empresas. Al menos 5 de una misma empresa.',
      '**Tu trabajo:** contactas al dueño o gerente, te reúnes con quien decide, das una charla de 20 minutos a sus empleados, presentas y **cierras tú mismo**, en la charla o en el seguimiento. No hay asesora ni cita con asesora. El pago entra a Heiiu; coordinación recibe el pago y firma contrato y pagaré con cada estudiante en la sede, a donde tú lo llevas o lo envías.',
      '**Tu rutina fija:** 15 minutos con gerencia todos los días a las 8:00 a. m. (el lunes 20 en la sede, después por llamada): qué hiciste ayer y qué empresas tienes hoy. La planilla FORMATO_15_EMPRESAS_RETO.xlsx siempre al día.'], size=9.5)

# ---------------------------------------------------------------- 1
sec('1. Heiiu en 10 líneas')
bullets([
 'Academia de inglés **presencial** en Bucaramanga (Carrera 27 # 48-49, barrio Sotomayor, segundo piso). La marca es Heiiu; "Global Teacher S.A.S." solo en documentos legales.',
 'Institución de educación para el trabajo y el desarrollo humano **con licencia desde 2012**; programas registrados ante la Secretaría de Educación (Resoluciones 1581-1131 y 2253-2025).',
 '**Triple certificación de calidad ICONTEC** (NTC 5555, NTC 5580 e ISO 9001). Es una certificación, no una exclusividad.',
 '**Garantía de aprendizaje por escrito**, texto único: "Si cumples — asistencia, tareas, evaluaciones — y no avanzas, te devolvemos el 100% del nivel. Por escrito, en el contrato." Es lo único que se dice como "la única academia PRESENCIAL de Bucaramanga".',
 '**Niveles:** A1 (90 h) · A2 (110 h) · B1 (175 h) · B2 (200 h). Programa completo A1 a B2 = **575 horas** presenciales. Certificado oficial por cada nivel aprobado y factura al matricularse.',
 '**Próximo grupo (confirmado por gerencia):** abre el martes 3 de noviembre o el lunes 9 de noviembre. Jornada de mañana, tarde o noche, de 2 o de 4 horas diarias: el horario lo definen los primeros que se matriculen; una empresa con 8 cupos o más define su propio horario. Para entrar el 3 de noviembre, la inicial tiene que estar pagada antes de esa fecha. Sábados de 8:00 a 12:00, un nivel a la vez.',
 '**Cómo son las clases:** en grupo pequeño, habladas en inglés desde la primera clase, con una simulación real en cada clase (entrevista, llamada, reunión) y el profesor como coach; video corto diario en inglés que el profesor revisa; una virtud por bloque.',
 '**Convenio con Cajasan** (no exclusivo): el afiliado entra a la columna más alta del Fondo de Becas. Nunca "los únicos con Cajasan".',
 'Al terminar A2, **Módulo de Graduación** a elección: Emprendedor (página web y primer mensaje de venta en inglés) o Pasaporte (video de presentación, hoja de vida, entrevista ensayada). Con el completo, Refuerzo PRO al final de B2. Se describen, nunca se promete un resultado.',
 '**Nuestra causa** (para la reunión): educativa, formar a jóvenes y trabajadores de Santander a través del inglés con valores y disciplina; empresarial, las empresas locales pueden ganar con calidad, resultados que se pueden mostrar y garantía por escrito.'])

# ---------------------------------------------------------------- 2
sec('2. El Pacto y la proyección por motivo')
t('No vendemos inglés fácil ni rápido. Vendemos **entrenamiento + destino**, y el cliente firma advertido. Se dice a todos, antes de dar precios:', after=1)
caja('"Antes de contarte precios, te cuento cómo es esto, para que decidas con todo claro. Nuestro objetivo es que salgas hablando inglés; si no se logra, algo está mal: o tú dejaste de entrenar, o nosotros no estamos cumpliendo. Esto es un entrenamiento en equipo, como un gimnasio o aprender a nadar: desde el primer día hablas, tu profesor identifica dónde puedes mejorar y lo repetimos hasta que sale. Por eso grabas un video corto todos los días, y tu profesor te lo devuelve con una mejora. A cambio, la garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel. ¿Te le mides a ese ritmo?"', size=9.5, italic=True)
t('Si dice "busco algo más suave": "Te agradezco la sinceridad. Este programa es exigente a propósito, y prefiero decírtelo ahora a que lo descubras en la segunda semana." Fin, sin reintentos. Jamás: fácil, rápido, divertido, "en tres meses hablas", nativos, empleo, visa.', size=9, color=GRIS)
tabla(['Motivo', 'Proyección (2 o 3 frases; emocionar no es prometer)'], [
 ('Trabajo / ascenso', '"La vacante que hoy pasas de largo porque pide inglés, y que ahora sí aplicas; la reunión donde entra alguien de afuera y tú eres quien responde. El inglés no te da el puesto: te quita la excusa que hoy te lo cierra." Se vende preparación, jamás empleo.'),
 ('Viaje', '"Para un viaje entrenamos justo lo que vas a vivir: resolver cosas tú mismo, entender lo que te dicen y responder sin traductor." Vacaciones: el Arranque sirve.'),
 ('Estudio o trabajo afuera', '"El módulo Pasaporte te deja el video de presentación, la hoja de vida y la entrevista ensayada." Va al programa completo. Traslado definitivo durante el nivel: no se vende.'),
 ('Su hijo o hija', '"Imagínate a tu hijo a los 18 con el inglés resuelto: la universidad o la beca sin ese requisito pendiente, o su primer trabajo cobrando más. Y lo que los papás más nos agradecen: aquí se entrena disciplina y constancia." Desde 12 años en cualquier jornada; el acudiente va a la cita y firma.'),
], [3.2, 14.8])

# ---------------------------------------------------------------- 3
sec('3. Mensaje de contacto al dueño o gerente')
t('Un solo pedido: **15 minutos de reunión y una charla de 20 minutos con su gente.** Nada de precios en el mensaje. Empresas de 40 a 150 empleados donde el dueño o el gerente decide; registra la empresa en la planilla antes de escribir.', size=9.5)
tabla(['Versión', 'Texto (cambia lo que está entre corchetes)'], [
 ('WhatsApp en frío', '"Buenos días, [nombre]. Soy [tu nombre], ejecutivo de alianzas de Heiiu English Academy, en Bucaramanga: licencia desde 2012 y certificación ICONTEC. Estamos abriendo alianzas con empresas de la ciudad: sin costo para la empresa, sus colaboradores acceden a la beca más alta de nuestro Fondo para formarse en inglés presencial, con garantía de aprendizaje por escrito. Le pido 15 minutos para mostrárselo y, si le sirve, una charla de 20 minutos con su equipo. ¿Le queda mejor el [día] a las [hora] o el [día] a las [hora]?"'),
 ('LinkedIn', '"[Nombre], le escribo de Heiiu English Academy, academia presencial de Bucaramanga con licencia desde 2012. Abrimos alianzas con empresas que quieren premiar y formar a su gente en inglés sin tocar la nómina: la empresa no paga nada y sus colaboradores entran con la beca más alta de nuestro Fondo, con garantía de aprendizaje por escrito. ¿Me regala 15 minutos esta semana para contarle cómo funciona? Si le sirve, le propongo una charla de 20 minutos con su equipo."'),
 ('Referido por un conocido', '"Buenos días, [nombre]. [Nombre de quien lo refiere] me sugirió escribirle. Soy [tu nombre], de Heiiu English Academy. Estamos abriendo alianzas con empresas de Bucaramanga para que sus colaboradores se formen en inglés con la beca más alta de nuestro Fondo, sin costo para la empresa y con garantía por escrito. Le pido 15 minutos para mostrárselo y, si le parece, una charla de 20 minutos con su gente. ¿El [día] a las [hora] o el [día] a las [hora]?"'),
], [3.2, 14.8], size=8.5)
t('Horario de contacto por iniciativa tuya: lunes a viernes de 7:00 a. m. a 7:00 p. m. y sábados de 8:00 a. m. a 3:00 p. m.; nunca domingos ni festivos; máximo un contacto al día por persona.', size=9, color=GRIS)

# ---------------------------------------------------------------- 4
sec('4. Reunión con el decisor: 10 minutos, 6 pasos')
tabla(['Paso', 'Qué dices', 'Sales con'], [
 ('1. La causa (1 min)', '"Heiiu es una academia santandereana e independiente. Nuestra causa es doble: formar a la gente de Santander a través del inglés, con valores y disciplina, y demostrar que las empresas locales ganan con calidad y resultados que se pueden mostrar."', 'Su atención'),
 ('2. Qué gana su empresa (2 min)', 'Un beneficio de bienestar para su gente **sin costo de nómina**; Becas con el nombre de su empresa (3 por trimestre, suben a 5 si todos sus becados cumplen) con certificado a su nombre; reporte periódico de asistencia y cumplimiento de sus becados (nunca notas); diagnóstico de nivel de inglés hasta 10 personas, sin costo.', 'Qué le importa más: premiar o formar'),
 ('3. Modelo A o modelo B (3 min)', '"Si su empresa quiere premiar a su gente sin tocar presupuesto, firmamos la alianza hoy. Si quiere formar a su equipo, le presento el plan empresa." **A, alianza sin costo:** cada colaborador con carta de la empresa paga su programa completo a $4.782.800 de contado (lista: $8.696.000). **B, plan empresa:** la empresa paga los cupos: $4.782.800 por cupo de 3 a 7, $4.350.000 de 8 a 15, $3.950.000 de 16 a 30.', 'A, B o los dos'),
 ('4. Qué firma (1 min)', '**A:** el Convenio Heiiu Business Partner: 12 meses, sin costo ni obligaciones económicas; la empresa designa un contacto de talento humano, emite las cartas de postulación y difunde el beneficio; no recibe ni gestiona pagos. **B:** la Orden Plan Empresa: elige tramo y forma de pago, designa a los colaboradores antes del inicio; queda en firme con la firma del representante legal de Heiiu y el pago inicial; precios vigentes 30 días. Tú no firmas por Heiiu: firma gerencia.', 'Documento que va a firmar'),
 ('5. La charla (2 min)', '"Para que su gente lo conozca, le pido 20 minutos con ellos, en su sede, en el horario que menos le afecte la operación. Yo la doy; los interesados se inscriben directo con nosotros."', 'Autorización de la charla'),
 ('6. Cierre con fecha (1 min)', '"¿La hacemos el [día] a las [hora] o el [día] a las [hora]?" Y silencio. Toda reunión termina con algo: fecha de charla, convenio u orden firmados, o un referido concreto.', 'Fecha de charla en la planilla'),
], [3.0, 11.6, 3.4], size=8.5)
caja(['**Qué NO se promete en la reunión:** empleo, visa, ascensos ni "su equipo saldrá bilingüe en X meses" · profesores nativos · clases virtuales en grupo · reporte de notas (solo asistencia y cumplimiento; las notas las comunica coordinación al estudiante) · exclusividad · descuentos adicionales (los valores ya traen la beca) · horarios, plazos o precios fuera del convenio y de la orden · fechas de inicio sin confirmar con gerencia.',
      '**Lo que pasa a gerencia (se agenda, no se cotiza):** más de 30 cupos, grupo cerrado en la empresa con horario especial, copago con valores distintos, plazos distintos o cualquier condición que no esté escrita en la orden.'], size=9)

# ---------------------------------------------------------------- 5
sec('5. La charla de 20 minutos a los empleados')
tabla(['Minuto', 'Bloque', 'Qué haces'], [
 ('0-3', 'El destino', 'Pregunta a la sala: "¿Quién aquí necesita el inglés para el trabajo, para un viaje, para estudiar o por sus hijos?" Toma dos respuestas y usa la proyección de esa persona (sección 2).'),
 ('3-6', 'El Pacto', 'El texto de la sección 2, completo, en voz alta. "Esto no es para todos, y está bien: es mejor saberlo hoy que en la clase 5."'),
 ('6-9', 'Cómo son las clases', 'Presenciales, grupo pequeño, inglés desde la primera clase, una simulación real por clase, video diario, una virtud por bloque. El grupo abre el 3 o el 9 de noviembre; mañana, tarde o noche, de 2 o 4 horas diarias, y el horario lo definen los primeros que se matriculan. La garantía, con su texto exacto.'),
 ('9-13', 'Precios: las 3 opciones', 'La tabla de la sección 6, en este orden: lo que paga tu empresa (si firmó plan empresa), el completo con la beca de la alianza, y el Arranque solo para quien el completo no le alcance. "No manejamos descuentos: el precio es el precio."'),
 ('13-16', 'Cómo inscribirse hoy', 'Cierras ahí mismo con los que estén listos: "Hoy te doy tu número exacto, pagas la inicial (transferencia a la cuenta de Heiiu o tarjeta) y firmas en la sede con coordinación. Los primeros que se matriculan definen el horario del grupo."'),
 ('Si la empresa ya compró los cupos (Plan Empresa)', 'La charla cambia', 'No es de venta: son 10 minutos con los colaboradores designados para El Pacto, el horario del grupo y la fecha de inicio, para que nadie llegue sin saber a qué se comprometió. Al resto del personal se les ofrece la beca de la alianza (opción 2): un cupo pagado por la empresa abre la puerta para vender más.'),
 ('16-20', 'Preguntas y registro', 'Pasas la hoja de interesados (hoja INTERESADOS del formato, impresa): nombre, celular, motivo, jornada. Respondes con la sección 8. Con los que no cerraron hoy, dejas en el acto día y hora de tu llamada de seguimiento.'),
], [1.4, 3.2, 13.4], size=8.5)
t('El mismo día pasas los interesados a la planilla y guardas la hoja física para coordinación. No tomas fotos de la hoja, no creas grupos de WhatsApp con empleados y no compartes los datos con la empresa.', size=9, color=GRIS)

# ---------------------------------------------------------------- 6
sec('6. Hoja de precios de la charla')
tabla(['Opción', 'Para quién', 'Valor', 'Cómo se paga'], [
 ('1. Tu empresa paga tu cupo (Plan Empresa)', 'Solo si la empresa firmó la Orden Plan Empresa', 'Programa completo A1 a B2 por cupo: $4.782.800 (3 a 7 cupos) · $4.350.000 (8 a 15) · $3.950.000 (16 a 30)', 'Lo paga la empresa contra factura: de contado, o inicial (30% en el tramo de 3 a 7; 40% de 8 en adelante) y 3 cuotas mensuales. Copago posible. La empresa escoge a quién le da cada cupo y puede cambiar a la persona antes de la primera clase, siempre que no cambie de horario; después de iniciar, no.'),
 ('2. Pagas tú, con la beca de la alianza', 'Todo colaborador con carta de su empresa aliada', 'Completo A1 a B2 (lista $8.696.000): **$4.782.800 de contado** · **$5.565.440 a cuotas**', 'Contado: transferencia a la cuenta de Heiiu o tarjeta; crédito de banco o cooperativa y cesantías también cuentan como contado. Cuotas: inicial mínima del 20% ($1.113.088) y cuotas mensuales al 1,9%; firmas pagaré. La cuota exacta la da coordinación con el motor de cuotas, nunca de memoria.'),
 ('3. Arranque A1+A2', 'Solo si el completo no le alcanza', '$2.990.000, precio único, sin beca. 200 horas, dos niveles certificados y Módulo de Graduación', 'Contado. Arranque a cuotas: ' + SUP + '.'),
], [3.4, 3.2, 4.9, 6.5], size=8.5)
bullets([
 '**Becas con el nombre de la empresa** (las 3 que la empresa elige por trimestre): pagan $4.782.800 aunque vayan a cuotas, con libros y prioridad de cupo. Nunca se suman dos becas: se aplica la mejor.',
 '**Ya sabe algo de inglés:** el valor de los paquetes parciales (A2 a B2, B1 a B2, solo B2) para aliados: ' + SUP + '. El nivel lo define la academia en la sesión de ubicación.',
 '**Todo entra a Heiiu:** transferencia a la cuenta de Heiiu o tarjeta. Si el estudiante paga en efectivo, el efectivo llega a la sede ese mismo día y coordinación expide el recibo. Tú nunca te quedas con dinero.',
 '**Número de la cuenta de Heiiu** para dar en la charla: ' + SUP + ' el lunes 20 (no lo escribas de memoria).'], size=9)

# ---------------------------------------------------------------- 7
sec('7. Proceso de inscripción paso a paso')
tabla(['Paso', 'Qué pasa', 'Quién'], [
 ('1. Interesado', 'Queda en la hoja de la charla y ese mismo día en la planilla (hoja INTERESADOS).', 'Ejecutivo'),
 ('2. Cierre', 'Lo haces tú, en la charla o en el seguimiento (llamada o en la sede), en unos 20 minutos. Orden: motivo, para quién y quién decide, nivel, jornada, El Pacto, forma de pago; solo entonces el número exacto. "Ya sé algo": sesión de ubicación; quién la hace y cuándo: ' + SUP + '.', 'Ejecutivo'),
 ('3. Inicial pagada', 'Transferencia a la cuenta de Heiiu o tarjeta, con pantallazo del comprobante (la cédula se presenta en la sede, no se envía por chat); efectivo, a la sede el mismo día con recibo de coordinación. Para entrar el 3 de noviembre, pagada antes de esa fecha. Coordinación recibe y verifica el pago.', 'Estudiante · coordinación'),
 ('4. Contrato y pagaré', 'Tú llevas o envías al estudiante a la sede. Allí, en físico: contrato de matrícula, anexo de garantía y pagaré si va a cuotas (si requiere codeudor se define ahí). Menor de 18: firma el acudiente.', 'Coordinación'),
 ('5. Cupo', 'Grupo del 3 o del 9 de noviembre; el horario lo definen los primeros matriculados (empresa con 8 o más: su propio horario). Plan Empresa: la orden la firma gerencia y la empresa designa a sus colaboradores; puede cambiar a la persona antes de la primera clase sin cambiar de horario.', 'Coordinación · gerencia'),
], [3.0, 12.0, 3.0], size=8.5)
caja(['**Qué cuenta como "inscrito pagado" para el reto:** la inicial (o el pago de contado) **en la cuenta de Heiiu, verificada por coordinación,** a más tardar el martes 3 de noviembre a las 6:00 p. m. En Plan Empresa, cada cupo cuenta cuando entra el pago inicial de la empresa por ese cupo.',
      '**No cuenta:** una promesa de pago, un pantallazo sin verificar, dinero que alguien te entregue a ti. Si el abono de separación de $300.000 cuenta como inicial para el reto: ' + SUP + '.'], size=9)

# ---------------------------------------------------------------- 8
sec('8. Objeciones frecuentes: la respuesta corta')
tabla(['Te dicen', 'Respondes'], [
 ('"Está muy caro"', '"Te entiendo. Por eso existe la alianza: el programa completo vale $8.696.000 y por tu empresa lo pagas a $4.782.800 de contado, o a cuotas con una inicial del 20%. No manejamos descuentos: el precio de contado es el precio." Y si de verdad no le alcanza: el Arranque.'),
 ('"No tengo tiempo"', '"El grupo puede ser de mañana, tarde o noche, de 2 o de 4 horas diarias, y el horario lo definen los primeros que se matriculan: si te inscribes ya, ayudas a definirlo. ¿Tu horario es fijo?" Turnos rotativos: "Te lo digo de frente: el programa es de horario fijo y la asistencia es parte de la garantía; no te voy a vender algo que no te va a funcionar."'),
 ('"Ya sé inglés"', '"Perfecto: el nivel lo define la academia en una sesión de ubicación corta, y entras en el nivel que te corresponde." Coordinación la agenda; si quiere, hace antes la prueba EF SET gratuita en línea.'),
 ('"¿Es virtual?"', '"En grupo somos presenciales; virtual tenemos las clases personalizadas por videollamada, desde 30 horas, a tu horario, y las cotiza la dirección académica."'),
 ('"Lo pienso"', '"¿Qué es lo que más te hace dudar: el precio, el horario o si de verdad vas a aprender?" Se responde eso y se deja la cita agendada. Nunca "aquí estaré cuando decidas".'),
 ('"Mi empresa no paga"', '"No tiene que pagar: la alianza no le cuesta nada a tu empresa. Con la carta de tu empresa entras a la beca más alta del Fondo, y el programa es tuyo, con tu contrato y tu garantía."'),
 ('"¿Y si no aprendo?"', 'La garantía, con su texto exacto. "Por escrito, en el contrato."'),
 ('"¿Clase de prueba?"', '"No manejamos clase de prueba: una clase suelta no te muestra si vas a aprender; lo que te lo garantiza es el contrato."'),
 ('Nombra otra academia', 'No repites su nombre ni hablas mal: "Allá se compra acceso, aquí se compra resultado." Lo anotas en la planilla.'),
], [3.4, 14.6], size=8.5)

# ---------------------------------------------------------------- 9
sec('9. Reglas innegociables')
bullets([
 'Solo los precios de este kit. Ningún descuento, beca, promoción, cupo, fecha ni condición distinta: lo que no está aquí, se agenda con gerencia.',
 'No hay clase de prueba. No hay clases virtuales en grupo. No se habla de profesores nativos ni del equipo docente: se vende método, respaldo y garantía.',
 'Nunca "fácil", "rápido", "gratis", "patrocinio", "descuento", "bilingüe en X meses"; nunca se promete empleo, visa ni resultado. Se dice "beca del Fondo" y "sin costo para la empresa".',
 'No se nombran otras academias. No se nombran métodos: se dice "clases inmersivas, activas y prácticas".',
 'Solo dos fechas de inicio: martes 3 o lunes 9 de noviembre. No se promete horario: lo definen los primeros matriculados.',
 'Todo pago entra a Heiiu: transferencia o tarjeta; el efectivo llega a la sede el mismo día y coordinación expide el recibo. Nunca te quedas con dinero. Tú no firmas por Heiiu.',
 'Los datos personales de interesados y decisores van solo en la planilla y en la hoja física de la charla; no se comparten con nadie, tampoco con la empresa.',
 'Toda empresa queda registrada en el formato antes de la primera reunión.',
 '15 minutos con gerencia todos los días a las 8:00 a. m., sin cancelar. La planilla al día, todos los días, antes de esa llamada.'], size=9.5)

# ---------------------------------------------------------------- 10
sec('10. Ritmo del reto día a día')
tabla(['Fecha', 'Qué tiene que estar hecho'], [
 ('Lun 20/10', '8:00 a 10:00 a. m., inducción en la sede; 10:00, a la calle. Mensajes de contacto a tu lista; primeras reuniones agendadas.'),
 ('Mar 21/10', 'Corte de los días 1 y 2: **15 empresas contactadas con el decisor**, con nombre y cargo en la planilla.'),
 ('Mié 22 a vie 24/10', 'Reuniones. Corte de la semana 1: **8 reuniones con decisor y 3 charlas autorizadas** para la semana 2, con fecha.'),
 ('Lun 27 a vie 31/10', 'Charlas, cierres e inscripciones. Recomendación: charlas hechas a más tardar el jueves 30, para que los pagos alcancen a entrar antes del corte y los inscritos puedan abrir grupo el 3 de noviembre.'),
 ('Lun 2/11', 'Festivo: no se contacta a nadie por iniciativa tuya.'),
 ('Mar 3/11', '**Corte a las 6:00 p. m.:** inscritos con inicial pagada y verificada por coordinación. Planilla cerrada y cuenta de cobro. Ese mismo día abre el grupo del 3 de noviembre (el siguiente, el lunes 9).'),
], [3.4, 14.6], size=8.5)
sub('Qué llevas en la maleta')
tabla(['Archivo (en recursos/comercial/B2B/)', 'Para qué', 'Ojo'], [
 ('CONVENIO_HEIIU_BUSINESS_PARTNER_v1.pdf', 'Lo firma la empresa en el modelo A', 'Firma por Heiiu el representante legal (gerencia).'),
 ('ORDEN_PLAN_EMPRESA_v1.pdf', 'Lo firma la empresa en el modelo B', 'Queda en firme con firma de gerencia y pago inicial. El cambio de persona vale hasta antes de la primera clase (gerencia), aunque el numeral 3 diga otra cosa.'),
 ('COMPARATIVO_BENEFICIO_ALIANZA.pdf', 'Tu referencia de las dos ofertas en pesos', 'Es para ti: no se entrega (trae columnas internas).'),
 ('CARTA_BUSINESS_PARTNER_v3.pdf', 'Carta de invitación a la empresa', 'Trae fecha de septiembre y una regla vieja de beca: no se entrega hasta que gerencia la actualice.'),
 ('PROPUESTA_B2B_EMPRESAS.pdf', 'Propuesta de julio', 'Trae menú, profesor nativo y modalidad virtual que ya no aplican: no se entrega ni se lee hasta que gerencia la actualice.'),
], [6.2, 5.4, 6.4], size=8.5)
t('Además: este kit, la planilla en el celular, 10 hojas INTERESADOS impresas y la carta de postulación de la empresa para cada colaborador (modelo: ' + SUP + '). Transporte y celular son tuyos.', size=9)

out = BASE + r'\KIT_ARRANQUE_RETO_15_DIAS_ALIANZAS.docx'
try:
    doc.save(out); print('OK', out)
except PermissionError:
    doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
