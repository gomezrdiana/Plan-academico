# -*- coding: utf-8 -*-
"""Hoja de una pagina para el Gerente de Alianzas Empresariales: por que el primer contacto a empresas se escribe
como dice MENSAJES_PRIMER_CONTACTO_EMPRESAS, con la evidencia detras de cada regla, en tono de aprendizaje
compartido. Por rol, sin nombres. Fuente: INVESTIGACION_CONTACTO_FRIO_EMPRESAS_2026-10-21.md. Salida (git):
recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/POR_QUE_ESCRIBIMOS_ASI_EMPRESAS.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\POR_QUE_ESCRIBIMOS_ASI_EMPRESAS.docx'
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
d = Document()
for s in d.sections:
    s.top_margin = Cm(0.9); s.bottom_margin = Cm(0.7); s.left_margin = Cm(1.3); s.right_margin = Cm(1.3)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9.5)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(1)
    x = p.add_run(t); x.bold = True; x.font.size = Pt(10.5); x.font.color.rgb = NAR
def t(txt, size=9.5, color=None, after=3, bold=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    x = p.add_run(txt); x.font.size = Pt(size); x.bold = bold
    if color: x.font.color.rgb = color
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
def caja(txt, size=9.5):
    tb = d.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0); x = c.paragraphs[0].add_run(txt); x.font.size = Pt(size)
    d.add_paragraph().paragraph_format.space_after = Pt(0)

p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
x = p.add_run('POR QUÉ ESCRIBIMOS ASÍ A LAS EMPRESAS'); x.bold = True; x.font.size = Pt(13); x.font.color.rgb = NAR
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(4)
x = p.add_run('Acompaña a la hoja MENSAJES_PRIMER_CONTACTO_EMPRESAS · 21/10/2026 · lo que encontramos, para que la regla se entienda y se pueda discutir con datos'); x.font.size = Pt(8.5); x.font.color.rgb = GRIS

t('Jhon primero que todo super el primer borrador del correo que se escribió para las empresas realmente me parece que est bien redactado y respetuoso, pero sobretodo que tiene la idea muy clara y es que vendemos mas que el ingles que todos venden. Pero como me pediste comentarios y sugerencias, yo me puse a hacer una investigación profunda para darte una guía de lo que se consideran buenas practicas a la hora de enviar correos a altos directivos porque por lo general lo que tiene a fallar cuando se hacen envíos en frio es que lo que a nosotros nos parece bien y completo, al gerente le parece largo y no lo termina leyendo. Lo cual no nos sirve por que perdemos el primer intento. Entonces aquí van las sugerencias y lo que encontré y ya con eso decides tambien tu como lo terminas de organizar.')

sec('Lo que cambia y por qué')
tabla(['Cómo lo hacemos', 'Qué encontramos'], [
 ('Menos de 90 palabras. El borrador tenía 270.',
  'Un gerente decide en menos de 3 segundos si abre el correo y lo lee en 9 segundos o menos. Pasadas las 100 palabras, las respuestas caen (Gong, 2026, más de un millón de ciclos de venta). Con 270 palabras, lo mejor del mensaje queda en la parte que nadie lee.'),
 ('Asunto corto con el nombre de la empresa, y el correo con el nombre y cargo de quien decide. Nunca "Estimado responsable".',
  'Poner el nombre en el asunto subió la apertura 20% y los contactos de venta 31% en experimentos con grupos de control (Sahni, Wheeler y Chintagunta, Marketing Science, 2018). Un correo sin nombre se lee como masivo y se borra.'),
 ('La primera línea habla de su empresa; la segunda, de lo que gana: becas con el nombre de su empresa, sin costo para la empresa, con las que puede premiar y retener a su gente.',
  'Lo centrado en el producto baja la respuesta (Gong, 2026). Y en Colombia el 75% de las empresas no da ningún beneficio extrasalarial y la mitad no mide los que da (ACRIP 2024; elempleo). Lo que abre la puerta no es el inglés: es un beneficio que no cuesta y que se puede mostrar.'),
 ('Las virtudes y los hábitos van en una frase, no en lista.',
  'Sí somos distintos por eso, y sí se dice: junto con el inglés se entrenan puntualidad, constancia y disciplina, y eso se le puede reportar a la empresa. Lo que no va en el primer correo es la lista de once competencias y cuatro virtudes: en 9 segundos de lectura se vuelve catálogo y se lee como promesa. En la reunión va en una frase ("y usted ve en el reporte su asistencia, puntualidad y cumplimiento") y la lista completa se cuenta con la causa, en un minuto. Cuando esos hábitos estén en indicadores, el reporte a la empresa los incluye.'),
 ('Un solo pedido: 15 minutos. En el primer correo se pregunta "¿le interesa?"; el día y la hora van en el segundo o cuando respondan.',
  'En 304.174 correos, en frío ganó la pregunta de interés; con la conversación ya abierta ganó proponer día y hora. "¿Podríamos agendar una breve conversación?" no ganó en ninguna etapa (Gong Labs, 2020). Por eso el kit se ajusta: dos fechas, sí, pero desde el segundo toque. Si le interesa y no contesta, lo recogen los seguimientos: el segundo correo trae las dos fechas y el tercero es la llamada; por eso la secuencia no para hasta el cuarto toque.'),
 ('Cuatro toques: correo, correo en el mismo hilo, llamada o LinkedIn, cierre. Cada uno trae algo nuevo.',
  'Entre el 42% y el 59% de las respuestas llega en los seguimientos (Instantly y Belkins, 2026). Un seguimiento sube las respuestas 66% (Backlinko). Más de cuatro toques solo suben las quejas.'),
 ('Sin adjuntos ni enlaces en el primer correo, y desde el correo de la academia.',
  'El dominio propio responde el doble que un correo gratuito (Hunter, 2025, 31 millones de correos). Los adjuntos afectan la entrega. Por eso el cargo escribe desde la cuenta institucional ger.alianzas@heiiu.com, que coordinación entrega mañana con su clave.'),
 ('WhatsApp solo cuando la persona dio su número o un referido lo autorizó.',
  'La política de WhatsApp (Meta, septiembre de 2026) exige número y permiso; sin eso se arriesga la línea. Además, el celular personal de un gerente es dato personal (Ley 1581). Si ya hubo contacto y la persona dio su número (en una reunión, con su tarjeta o escribiendo primero), sí se le puede escribir por WhatsApp.'),
 ('Correo en horario laboral; llamadas y WhatsApp con horario y un contacto al día; la línea de salida solo en el cierre.',
  'Para el correo basta con enviarlo en horario laboral: el gerente lo abre cuando quiere. Las normas de horario y frecuencia (Ley 2300) y el Registro de Números Excluidos pesan en la llamada y en el WhatsApp: horario de oficina, un contacto al día y el registro solo para celulares personales. Llamar al teléfono publicado de la empresa sí se puede.'),
], [6.4, 11.4])

sec('Lo que no sabemos todavía, y lo vamos a saber con el tablero')
t('Cuántas empresas de Bucaramanga responden a un correo así, cuántas a una llamada al teléfono publicado de la empresa y cuántas a una visita. La meta de arranque es entre 5% y 10% de respuesta y una reunión por cada 8 a 12 empresas que completen los cuatro toques; es un supuesto, y en cuatro semanas el tablero dice si es verdad. Por eso cada toque se anota el mismo día: sin registro no hay forma de aprender.')
caja('Si en la calle algo contradice esta hoja (una empresa que respondió a la llamada y no al correo, una que pidió la propuesta por WhatsApp), se anota en el tablero y se trae al seguimiento. Las reglas salieron de datos; con datos nuestros se cambian.')
t('Fuente completa: INVESTIGACION_CONTACTO_FRIO_EMPRESAS_2026-10-21 (en gerencia).', size=8.5, color=GRIS, after=0)

try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
