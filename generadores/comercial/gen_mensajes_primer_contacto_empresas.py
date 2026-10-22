# -*- coding: utf-8 -*-
"""Hoja por rol para el Gerente de Alianzas Empresariales: primer contacto en frío a empresas y secuencia de 4 toques
(correo, respuesta en el hilo, llamada o LinkedIn, cierre), WhatsApp solo con permiso, reglas y errores. Derivada de
INVESTIGACION_CONTACTO_FRIO_EMPRESAS_2026-10-21.md y del kit del cargo. Salida (git):
recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/MENSAJES_PRIMER_CONTACTO_EMPRESAS.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\MENSAJES_PRIMER_CONTACTO_EMPRESAS.docx'
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
d = Document()
for s in d.sections:
    s.top_margin = Cm(0.9); s.bottom_margin = Cm(0.7); s.left_margin = Cm(1.3); s.right_margin = Cm(1.3)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(1)
    x = p.add_run(t); x.bold = True; x.font.size = Pt(10.5); x.font.color.rgb = NAR
def t(txt, size=9, color=None, after=1, bold=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    x = p.add_run(txt); x.font.size = Pt(size); x.bold = bold
    if color: x.font.color.rgb = color
def bullets(items, size=9):
    for it in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); x = p.add_run(it); x.font.size = Pt(size)
def caja(lineas, size=9, titulo=None):
    tb = d.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    first = True
    if titulo:
        c.paragraphs[0].paragraph_format.space_after = Pt(2); x = c.paragraphs[0].add_run(titulo); x.bold = True; x.font.size = Pt(size); x.font.color.rgb = NAR; first = False
    for ln in lineas:
        p = c.paragraphs[0] if first else c.add_paragraph(); first = False
        p.paragraph_format.space_after = Pt(2); x = p.add_run(ln); x.font.size = Pt(size)
    d.add_paragraph().paragraph_format.space_after = Pt(0)
def tabla(hdr, filas, anchos, size=8.5):
    tb = d.add_table(rows=1, cols=len(hdr)); tb.style = 'Table Grid'
    for i, h in enumerate(hdr):
        c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
        x = c.paragraphs[0].add_run(h); x.bold = True; x.font.size = Pt(size); x.font.color.rgb = BLANCO
    for f in filas:
        row = tb.add_row().cells
        for i, txt in enumerate(f):
            row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
            x = row[i].paragraphs[0].add_run(txt); x.font.size = Pt(size); x.bold = (i == 0)
    for row in tb.rows:
        for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    d.add_paragraph().paragraph_format.space_after = Pt(0)

p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
x = p.add_run('PRIMER CONTACTO CON EMPRESAS — MENSAJES Y SECUENCIA'); x.bold = True; x.font.size = Pt(13); x.font.color.rgb = NAR
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(4)
x = p.add_run('Gerente de Alianzas Empresariales · uso interno · 21/10/2026 · Objetivo de todo mensaje: 15 minutos con quien decide. La charla a los empleados se pide en esa reunión, no por correo.'); x.font.size = Pt(8.5); x.font.color.rgb = GRIS

sec('1. Antes de escribir (si falta una, no se escribe)')
bullets([
 'Nombre y cargo de quien decide, verificados en la página de la empresa, LinkedIn o el RUES. Nunca "Estimado responsable". Máximo dos personas por empresa: gerencia general y gestión humana.',
 'Un dato concreto de esa empresa para la primera línea (atiende clientes del exterior, abrió vacantes que piden inglés, exporta, tiene turnos fijos).',
 'Si está afiliada a Cajasan (se pregunta en la llamada o lo dice la empresa; no se supone).',
 'La empresa registrada en la pestaña EMPRESAS del tablero antes del primer toque. Cada toque se anota el mismo día.',
 'Se envía desde el correo de la academia, de martes a jueves entre 7:00 y 9:00 a. m., sin adjuntos ni enlaces. Nunca desde un correo personal ni con copia oculta a varias empresas.'])

sec('2. Toque 1 · día 0 (miércoles) · correo al decisor · de 60 a 90 palabras')
caja([
 'Asunto: Becas para [Empresa]',
 'Buenos días, [cargo y apellido]:',
 'Vi que [dato concreto: atienden clientes del exterior / abrieron vacantes que piden inglés].',
 'En Heiiu English Academy abrimos becas con el nombre de [Empresa] para sus colaboradores, sin costo para la empresa, y usted recibe un reporte de la asistencia y el cumplimiento de sus becados. Cada uno estudia con garantía de aprendizaje por escrito.',
 '¿Le interesa que le cuente en 15 minutos cómo funciona?',
 '[Nombre] · Gerente de Alianzas Empresariales · Heiiu English Academy · [celular de la línea de alianzas]',
 'Si no es para ustedes, me lo dice y no vuelvo a escribirle.'])
t('Otros asuntos que sirven: "[Nombre], beneficio para su equipo" · "Afiliados Cajasan en [Empresa]" (solo si está afiliada; nunca que parezca que Cajasan envía el mensaje). En el primer correo se pregunta por el interés; el día y la hora van en el segundo o apenas respondan.', size=8.5, color=GRIS)

sec('3. Toque 2 · día 2 (viernes) · respuesta en el mismo hilo · de 40 a 60 palabras · aquí van las dos franjas')
caja([
 'Buenos días, [cargo y apellido]. Le sumo un solo dato:',
 'Si está afiliada: "sus colaboradores afiliados a Cajasan ya acceden a la beca más alta de nuestro Fondo; la alianza les suma las becas con el nombre de [Empresa] y el reporte de asistencia."',
 'Si no: "cada becado estudia con garantía de aprendizaje por escrito: si cumple y no avanza, la academia le devuelve el nivel."',
 '¿Le queda bien el martes a las 7:30 a. m. o el jueves a las 2:00 p. m.? Son 15 minutos, por llamada o en su oficina.'])

sec('4. Toque 3 · día 5 (lunes) · se cambia de canal: llamada al conmutador; si no hay teléfono, LinkedIn')
caja([
 'Llamada: "Buenos días, soy [Nombre], Gerente de Alianzas de Heiiu English Academy. Le escribí al [cargo] el miércoles sobre unas becas para los colaboradores de [Empresa], sin costo para la empresa. ¿Es [él / ella] quien decide los beneficios para el personal, o con quién lo veo?"',
 'Si pasa el decisor: "Le propongo algo concreto: un diagnóstico de nivel de inglés para hasta 10 personas de su equipo, sin costo, y 15 minutos para explicarle las becas. ¿Martes a las 7:30 o jueves a las 2?" Y silencio.',
 'Si contesta la asistente: nombre y correo de quien decide, y a qué hora suele estar. Se agradece y se anota. No se deja "recado".',
 'LinkedIn (menos de 300 caracteres): "Buenos días, [nombre]. Soy Gerente de Alianzas de Heiiu English Academy, en Bucaramanga. Le escribí por correo sobre becas con el nombre de [Empresa] para su equipo, sin costo para la empresa. ¿Le interesa que se lo cuente en 15 minutos?"'])
t('Celular personal del decisor: solo si él lo dio, lo publicó para contacto profesional o un referido lo autorizó; antes de llamar se consulta el Registro de Números Excluidos. Un contacto al día y un solo canal por semana con la misma persona.', size=8.5, color=GRIS)

sec('5. Toque 4 · día 10 (viernes) · cierre en el hilo original · de 30 a 40 palabras')
caja([
 '[Cargo y apellido], cierro el tema por ahora para no insistir. Si más adelante quieren el diagnóstico de nivel para su equipo o las becas con el nombre de [Empresa], me escribe a este correo y lo retomamos. Gracias por su tiempo.'])
t('Se marca en el tablero como "sin respuesta" y se vuelve a intentar a los 90 días con un motivo nuevo. Respondió "no": se agradece y se cierra; no se discute. Respondió "sí" en cualquier toque: se para la secuencia y se agenda.', size=8.5, color=GRIS)

sec('6. WhatsApp: solo con permiso')
t('La política de WhatsApp exige que la persona haya dado su número y aceptado recibir mensajes. Sin eso no se escribe, y nunca desde la línea principal de la academia. Sirve cuando hay tarjeta entregada, referido que autorizó o línea de atención publicada por la empresa.', size=9)
caja([
 '"Buenos días, [nombre]. Soy [Nombre], de Heiiu English Academy; [referido] me dio su número y me dijo que usted lleva el bienestar en [Empresa]. ¿Le puedo escribir por aquí sobre unas becas para su equipo, sin costo para la empresa?"',
 '"Buenos días. Soy [Nombre], Gerente de Alianzas de Heiiu English Academy. ¿Con quién hablo sobre beneficios de formación para los colaboradores de [Empresa]? Es una alianza sin costo para la empresa; con 15 minutos basta."'])

sec('7. Diez reglas')
tabla(['Regla', 'Por qué'], [
 ('Correo de 50 a 90 palabras; LinkedIn menos de 300 caracteres; WhatsApp 3 o 4 líneas', 'Un gerente decide en 3 segundos si abre y lee en 9; pasadas las 100 palabras las respuestas caen.'),
 ('Asunto de 3 a 6 palabras con el nombre de la empresa o de la persona', 'El nombre en el asunto subió la apertura 20% y los contactos de venta 31% en experimentos controlados.'),
 ('La primera línea habla de su empresa, no de la academia', 'Lo centrado en el producto y las listas de métodos o virtudes bajan la respuesta.'),
 ('Un solo pedido: 15 minutos', 'Dos pedidos en 9 segundos de lectura son ninguno.'),
 ('Toque 1 pregunta por el interés; las dos franjas van en el toque 2 o cuando respondan', 'En frío ganó "¿le interesa?"; con la conversación abierta ganó proponer día y hora.'),
 ('Una sola frase de respaldo, verificable', 'Licencia desde 2012, ICONTEC o garantía por escrito. Una, no las tres.'),
 ('Cada seguimiento trae algo nuevo; al tercer toque se cambia de canal', 'Entre el 42% y el 59% de las respuestas llega en los seguimientos; "¿vio mi correo?" no trae nada.'),
 ('Sin adjuntos ni enlaces en el primer contacto; desde el correo de la academia', 'Los adjuntos y enlaces afectan la entrega; el dominio propio responde el doble que un correo gratuito.'),
 ('Palabras que no se escriben: gratis, descuento, fácil, rápido, nómina, patrocinio', 'Se dice "sin costo para la empresa" y "beca del Fondo". No se nombran otras academias ni se promete empleo o resultado.'),
 ('Horario legal, un contacto al día, un canal por semana, salida en cada mensaje', 'Lunes a viernes 7 a. m. a 7 p. m., sábados 8 a. m. a 3 p. m.; nunca domingos ni festivos.'),
], [7.6, 10.2])

sec('8. Lo que hace que no respondan (y que el correo se borre)')
bullets([
 '"Estimado responsable de Recursos Humanos" sin nombre: se lee como correo masivo.',
 'Hablar de "nuestro programa", "queremos presentarle", y listas de competencias o virtudes: eso es pedagogía interna, no es lo que gana el gerente.',
 'Hablar de "la inversión de la organización" antes de que sepa que hay opción sin costo para la empresa.',
 '"¿Podríamos agendar una breve conversación?": pregunta abierta sin interés ni fecha. No ganó en ninguna etapa.',
 'Más de 100 palabras, párrafos largos, adjuntos, varias peticiones, cargo o firma incompletos, sin celular de contacto.'], size=9)
t('Lo que no está en esta hoja (clase de prueba, cupos sin costo, precios especiales) no se ofrece: se agenda con gerencia. Fuente completa: INVESTIGACION_CONTACTO_FRIO_EMPRESAS_2026-10-21.', size=8.5, color=GRIS, after=0)

try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
