# -*- coding: utf-8 -*-
"""Hoja interna del programa de referidos para asesores de entidades aliadas (bono recargable de $200.000 por
matricula pagada de contado, piloto hasta el 31/01/2027). Por rol, sin nombres. Documento interno del Gerente de
Alianzas: no se entrega a las asesoras (a ellas les llega la pieza). Salida (git):
recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PROGRAMA_REFERIDOS_ASESORES_ENTIDADES.docx (+PDF,
copia del PDF en la carpeta del gerente de alianzas / plan referidos)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PROGRAMA_REFERIDOS_ASESORES_ENTIDADES.docx'
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
d = Document()
for s in d.sections:
    s.top_margin = Cm(0.6); s.bottom_margin = Cm(0.4); s.left_margin = Cm(1.3); s.right_margin = Cm(1.3)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(1)
    x = p.add_run(t); x.bold = True; x.font.size = Pt(10.5); x.font.color.rgb = NAR
def t(txt, size=9, color=None, after=3, bold=False):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    x = p.add_run(txt); x.font.size = Pt(size); x.bold = bold
    if color: x.font.color.rgb = color
def tabla(hdr, filas, anchos, size=8):
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
    sp = d.add_paragraph(); sp.paragraph_format.space_after = Pt(0); sp.paragraph_format.line_spacing = Pt(6); sp.add_run(' ').font.size = Pt(4)
def caja(txt, size=8.5):
    tb = d.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0); x = c.paragraphs[0].add_run(txt); x.font.size = Pt(size)
    sp = d.add_paragraph(); sp.paragraph_format.space_after = Pt(0); sp.paragraph_format.line_spacing = Pt(6); sp.add_run(' ').font.size = Pt(4)

p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
x = p.add_run('PROGRAMA DE REFERIDOS · ASESORES DE ENTIDADES ALIADAS'); x.bold = True; x.font.size = Pt(13); x.font.color.rgb = NAR
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(4)
x = p.add_run('Hoja interna del Gerente de Alianzas · 23/10/2026 · piloto hasta el 31 de enero de 2027 · a las asesoras les llega la pieza, no esta hoja'); x.font.size = Pt(8.5); x.font.color.rgb = GRIS

t('Qué es: un bono para el asesor o asesora de una entidad aliada (caja, cooperativa, fondo) por cada afiliado que escriba a Heiiu con su código y se matricule pagando de contado. '
  'Qué no es: una comisión de venta. La asesora refiere; la cita y el cierre los hace nuestro equipo. Todo lo que se ofrece está en esta hoja; lo que no está aquí, no se ofrece.')

sec('1. El bono')
tabla(['Punto', 'Regla'], [
 ('Monto', '$200.000 por matrícula. Fijo, igual para todas las entidades y todas las asesoras.'),
 ('Medio', 'Tarjeta recargable a nombre de la asesora, comprada por Heiiu a un proveedor que factura. Nunca efectivo, nunca transferencia personal, nunca "detalles".'),
 ('Cuándo se causa', 'Matrícula con contrato firmado, pagada de contado (directo o con el crédito de la entidad), con los cinco días de retracto cumplidos y el pago recibido por Heiiu. En las entidades que pagan a 30 días, cuando pagan.'),
 ('Cuándo se recarga', 'En el cierre del mes en que entra el pago. La recarga la autoriza el financiero después de revisar el cierre contable del mes.'),
 ('No aplica', 'Matrículas financiadas por cuotas con Heiiu; afiliados con gestión humana de nuestro equipo en los 30 días previos a su mensaje; referidos sin código; retiros dentro del retracto.'),
 ('Financiación del piloto', 'De cada bono, $100.000 los pone Heiiu y $100.000 se descuentan de la comisión del gerente de alianzas por esa misma matrícula, con su autorización firmada. Se revisa al cierre del piloto; si cambia, se aumenta el bono o se deja igual.'),
], [3.2, 15.2])

sec('2. Código y QR de cada asesora (no hay formulario)')
t('Cada asesora tiene un código propio (por ejemplo C-07) y un QR con ese código, impreso y por WhatsApp. El QR abre WhatsApp en la línea de alianzas (316 768 8793) con el mensaje ya escrito: '
  '"Hola, quiero información para estudiar inglés en Heiiu. Código de asesor: C-07". El mismo enlace (uno por código, en el archivo ENLACES_CODIGOS.txt junto a los QR) se reenvía por WhatsApp. La asesora no digita datos de nadie.', after=2)
t('El primer mensaje lo manda el afiliado, no nosotros: escanea el QR o toca el enlace y pulsa enviar. Su número, el código y la hora quedan en la línea; ese es el registro. Heiiu no llama a nadie que no haya escrito. '
  'Coordinación lleva en una hoja de cálculo cada mensaje con código: fecha, código, celular, contactado, cita, matrícula pagada, bono recargado.', after=2)
tabla(['Regla', 'Para qué'], [
 ('Primer mensaje gana', 'Si un mismo celular llega con dos códigos, el bono es del código del primer mensaje. La hora de WhatsApp decide.'),
 ('Vale 30 días', 'Si la matrícula no se paga dentro de los 30 días siguientes al primer mensaje, no hay bono. La intención es que la asesora ayude a gestionar una matrícula rápida.'),
 ('Base previa', 'Que el celular ya esté en nuestra base (pauta, plataforma, reactivaciones) no quita el bono. Lo quita que en los 30 días previos al mensaje alguien del equipo lo haya llamado o gestionado; los mensajes automáticos del bot no cuentan como gestión. Coordinación lo verifica antes de marcar la matrícula como referida.'),
], [3.2, 15.2])

sec('3. Quién hace qué')
tabla(['Paso', 'Responsable', 'Qué hace'], [
 ('1', 'Asesora de la entidad', 'Le cuenta al afiliado y le muestra su QR o le reenvía su enlace.'),
 ('2', 'Afiliado', 'Escanea el QR o toca el enlace y envía el mensaje con el código a la línea de alianzas.'),
 ('3', 'Gerente de alianzas', 'Responde en menos de un día hábil, confirma el código contra la lista de códigos y agenda la cita. Cierra él o la pasa a la asesora comercial: durante el piloto él también vende.'),
 ('4', 'Quien cierre', 'Cita, cierre y matrícula. El código de la asesora de la entidad queda escrito en el contrato o en el formulario de matrícula.'),
 ('5', 'Coordinación', 'Anota en la hoja de cálculo cada mensaje con código y marca: contactado · cita · matrícula pagada · bono recargado, con fecha. Verifica base previa y los 30 días.'),
 ('6', 'Financiero', 'Revisa el cierre contable del mes, confirma pago recibido y retracto cumplido, y autoriza la recarga.'),
 ('7', 'Gerente de alianzas', 'Reporta el lunes en el tablero de alianzas: registros, citas, matrículas y bonos del piloto, por entidad y por asesora.'),
], [1.0, 3.6, 13.8])

sec('4. Premio único al cierre del piloto')
t('La asesora que más matrículas pagadas traiga hasta el 31 de enero de 2027 recibe un nivel de inglés en Heiiu para ella o para un familiar, en un grupo con cupo disponible. Un solo premio; en empate, gana quien llegó primero al número. No hay metas por mes ni por trimestre.')

sec('5. Lo que el gerente de alianzas no puede ofrecer ni hacer')
caja('• Efectivo, transferencias o cualquier pago fuera de la tarjeta.  • Más de $200.000 o cualquier escalera de montos.  • Metas por mes o por trimestre.  '
     '• Piezas con logos de las entidades, o piezas distintas a la aprobada por gerencia.  • Entrar a una oficina con el programa sin que la dirección de esa oficina lo sepa; si una entidad dice que sus asesoras no pueden recibirlo, en esa entidad el programa se cae y queda solo el premio.  '
     '• Contactar a un afiliado antes de que escriba.  • Aportar él mismo dinero, bonos o regalos a una asesora.')

sec('6. Antes de arrancar (sin esto no se entrega la primera tarjeta)')
tabla(['Pendiente', 'Responsable'], [
 ('Dos cotizaciones del proveedor de tarjeta: emisión, comisión por recarga, compra mínima, y su carta de condiciones.', 'Gerente de alianzas'),
 ('Concepto de la contadora: registro del gasto, retención si aplica, soporte de cada recarga.', 'Gerencia'),
 ('Autorización firmada del descuento de $100.000 por bono en la comisión del gerente de alianzas.', 'Gerente de alianzas y gerencia'),
 ('Lista de códigos por asesora (sin nombres en la lista que circula) y un QR por código, impreso y por WhatsApp.', 'Gerente de alianzas la lista; gerencia los QR'),
 ('Aval de la dirección de cada oficina donde se presente el programa, antes de la primera asesora.', 'Gerente de alianzas'),
], [13.6, 4.8])

last = d.paragraphs[-1]  # Word exige un parrafo tras la ultima tabla: se deja de 1 pt para que no salte a pagina 2
last.paragraph_format.space_after = Pt(0); last.paragraph_format.space_before = Pt(0); last.paragraph_format.line_spacing = Pt(1)
last.add_run(' ').font.size = Pt(1)
try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
