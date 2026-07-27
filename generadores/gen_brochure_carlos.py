# Brochure de primer contacto de Carlos (CFO fraccional) con el diseño de su Propuesta v1:
# banda navy + acentos dorados + recuadros crema. Correr desde la raíz del repo.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, HRFlowable)

NAVY = HexColor('#152A4A')
GOLD = HexColor('#C9A227')
CREAM = HexColor('#F5F0E6')
BODY = HexColor('#2E2E2E')
GRAYL = HexColor('#C8D0DC')

W, H = letter
HEADER_H = 118

OUT = os.path.join('recursos', 'comercial', 'CFO', 'CARLOS_CFO_BROCHURE_DISENO.pdf')


def draw_page(canv, doc):
    canv.saveState()
    # Banda superior navy
    canv.setFillColor(NAVY)
    canv.rect(0, H - HEADER_H, W, HEADER_H, stroke=0, fill=1)
    canv.setFillColor(GOLD)
    canv.rect(0, H - HEADER_H - 3, W, 3, stroke=0, fill=1)
    # Contenido del header
    canv.setFillColor(GOLD)
    canv.setFont('Helvetica-Bold', 8.5)
    canv.drawString(22 * mm, H - 26, 'CARLOS [APELLIDO]  ·  CFO FRACCIONAL')
    canv.setFillColor(white)
    canv.setFont('Helvetica-Bold', 20)
    canv.drawString(22 * mm, H - 52, '¿Cuánta plata le quedó LIBRE')
    canv.drawString(22 * mm, H - 74, 'el mes pasado?')
    canv.setFillColor(GRAYL)
    canv.setFont('Helvetica', 10.5)
    canv.drawString(22 * mm, H - 92, 'No cuánto vendió — cuánto le quedó. Si tiene que buscar la respuesta, esta página es para usted.')
    canv.setFont('Helvetica', 8.5)
    canv.drawString(22 * mm, H - 107, '[email]   ·   [teléfono]   ·   [link de agenda]   ·   Asesoría en español, 100% remota')
    # Footer navy
    canv.setFillColor(GOLD)
    canv.rect(0, 16, W, 2, stroke=0, fill=1)
    canv.setFillColor(NAVY)
    canv.rect(0, 0, W, 16, stroke=0, fill=1)
    canv.setFillColor(GRAYL)
    canv.setFont('Helvetica', 7.5)
    canv.drawCentredString(W / 2, 5, 'Carlos [Apellido] · CFO Fraccional · Dirección financiera en español para empresarios en USA')
    canv.restoreState()


S_SEC = ParagraphStyle('sec', fontName='Helvetica-Bold', fontSize=11.5, leading=14,
                       textColor=NAVY, spaceBefore=10, spaceAfter=2)
S_BODY = ParagraphStyle('body', fontName='Helvetica', fontSize=9.6, leading=13, textColor=BODY)
S_Q = ParagraphStyle('q', fontName='Helvetica', fontSize=9.8, leading=13.6, textColor=BODY,
                     leftIndent=14, firstLineIndent=-14, spaceBefore=2.5)
S_CALL = ParagraphStyle('call', fontName='Helvetica', fontSize=9.6, leading=13.2, textColor=NAVY)
S_CTA_T = ParagraphStyle('ctat', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=NAVY)


def gold_rule():
    return HRFlowable(width='100%', thickness=1.2, color=GOLD, spaceBefore=0, spaceAfter=6)


def callout(flow_paragraphs, pad=8):
    t = Table([[flow_paragraphs]], colWidths=[W - 44 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CREAM),
        ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), pad), ('BOTTOMPADDING', (0, 0), (-1, -1), pad),
        ('LINEBEFORE', (0, 0), (0, -1), 2.5, GOLD),
    ]))
    return t


story = []
story.append(Paragraph('HÁGASE ESTAS 5 PREGUNTAS <font size=8.5 color="#666666">(30 segundos — nadie lo está mirando)</font>', S_SEC))
story.append(gold_rule())
qs = [
    '¿Sabe cuánto vendió el mes pasado… y cuánto le quedó <b>libre de verdad</b>?',
    '¿Sabe cuál de sus productos o servicios le <b>deja</b> plata — y cuál se la está <b>quitando</b>?',
    'Si mañana pide un préstamo para crecer, ¿tiene los números <b>listos para mostrárselos al banco</b>?',
    'Si algún día quisiera vender su negocio o retirarse, ¿alguien podría ver en papel <b>cuánto vale</b>?',
    'Las decisiones grandes (contratar, comprar, abrir, invertir) — ¿las toma <b>con números o con estómago</b>?',
]
for i, q in enumerate(qs, 1):
    story.append(Paragraph(f'<b><font color="#C9A227">{i}.</font></b>  {q}', S_Q))
story.append(Spacer(1, 8))
story.append(callout([Paragraph(
    '<b>Si dudó en 2 o más, no tiene un problema de negocio: tiene un punto ciego de números.</b> '
    'Y los puntos ciegos cuestan plata todos los meses — se vean o no. Después de años de trabajo, la pregunta ya no es '
    'si su negocio le da para vivir: <b>es si le está construyendo patrimonio, o solo lo mantiene ocupado.</b>', S_CALL)]))

story.append(Paragraph('QUÉ HAGO YO', S_SEC))
story.append(gold_rule())
for b in [
    '<b>En 30 días le entrego las 3 fugas de plata más grandes de su negocio, con su cifra.</b> No un informe: tres números suyos que no conocía y qué hacer con cada uno.',
    '<b>Cada mes, en una página:</b> cuánto entró, cuánto salió, por dónde se fue y cuánto quedó — más alertas cuando un número se sale de rango.',
    '<b>Entregables fijos, sin contratos largos:</b> usted sabe exactamente qué recibe. Si un mes no le sirve, lo hablamos.',
]:
    story.append(Paragraph(f'<font color="#C9A227"><b>—</b></font>  {b}', S_Q))
story.append(Spacer(1, 6))
story.append(Paragraph(
    '<b>No soy su contador — soy su director financiero.</b> Su contador mira el pasado (registros, impuestos). '
    'Yo miro lo que viene: la caja, los márgenes y las decisiones. Y una regla mía, de entrada: '
    '<b>yo nunca toco su plata</b> — solo leo los números; las claves y las firmas siempre son suyas.', S_BODY))

story.append(Paragraph('QUIÉN SOY', S_SEC))
story.append(gold_rule())
story.append(Paragraph(
    '<b>Carlos [Apellido], CFO.</b> Dirijo las finanzas de una red de <b>12 unidades de negocio en Estados Unidos</b>: '
    'caja, márgenes, nómina y decisiones de crecimiento, de forma remota. [X años de trayectoria en (sectores)]. '
    'Atiendo un grupo pequeño de empresas para mantener este nivel de dedicación.', S_BODY))
story.append(Spacer(1, 10))
story.append(callout([
    Paragraph('EL SIGUIENTE PASO — sin costo y sin compromiso', S_CTA_T),
    Spacer(1, 3),
    Paragraph('<b>20 minutos por videollamada: le digo qué miraría primero en SU negocio y por qué.</b> '
              'Si en esa llamada no ve algo que valga la pena, ahí queda — y quedamos bien.', S_CALL),
    Spacer(1, 3),
    Paragraph('<b>WhatsApp:</b> [teléfono]   ·   <b>Correo:</b> [email]   ·   <b>Agende directo:</b> [link]', S_CALL),
], pad=10))

doc = BaseDocTemplate(OUT, pagesize=letter, leftMargin=22 * mm, rightMargin=22 * mm,
                      topMargin=HEADER_H + 14, bottomMargin=30)
frame = Frame(22 * mm, 26, W - 44 * mm, H - HEADER_H - 14 - 30, id='main')
doc.addPageTemplates([PageTemplate(id='p', frames=[frame], onPage=draw_page)])
doc.build(story)
print(f'OK: {OUT}')
