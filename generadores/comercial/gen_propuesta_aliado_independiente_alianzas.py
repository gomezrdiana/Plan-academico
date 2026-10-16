# -*- coding: utf-8 -*-
"""Propuesta de vinculación INDEPENDIENTE (sin fijo, solo comisión) para un candidato de alianzas que no entra al cargo
de planta. Derivada de gen_propuesta_ejecutiva_alianzas_candidata.py (mismo estilo), pero: sin salario, sin mínimo
garantizado, sin horario ni sede, sin ferias ni reactivaciones, solo empresas abiertas por relación directa con gerencia.
Se envía SOLO después de que el candidato entregue la tarea de 48 h y la referencia dé bien.
Salida (fuera de git): .../LINKEDIN DIANA GOMEZ/Candidatos/Reinaldo Joya/PROPUESTA_ALIADO_INDEPENDIENTE_ALIANZAS.pdf"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

F = 'C:/Windows/Fonts/'
pdfmetrics.registerFont(TTFont('Cal', F + 'calibri.ttf')); pdfmetrics.registerFont(TTFont('CalB', F + 'calibrib.ttf')); pdfmetrics.registerFont(TTFont('Geo', F + 'georgiai.ttf')); pdfmetrics.registerFont(TTFont('CalI', F + 'calibrii.ttf'))
pdfmetrics.registerFontFamily('Cal', normal='Cal', bold='CalB', italic='CalI', boldItalic='CalB')
NAR = colors.HexColor('#E54C09'); AMAR = colors.HexColor('#FBC900'); CREMA = colors.HexColor('#FFF8E7'); CAFE = colors.HexColor('#30271C'); GRIS = colors.HexColor('#6B6B6B'); LINEA = colors.HexColor('#E6DCCB')
st = {
 'kicker': ParagraphStyle('kicker', fontName='CalB', fontSize=10, textColor=GRIS, leading=13, spaceAfter=2),
 'h1': ParagraphStyle('h1', fontName='CalB', fontSize=22, textColor=NAR, leading=26, spaceAfter=4),
 'sub': ParagraphStyle('sub', fontName='Cal', fontSize=11, textColor=CAFE, leading=14, spaceAfter=8),
 'h2': ParagraphStyle('h2', fontName='CalB', fontSize=13, textColor=NAR, leading=16, spaceBefore=6, spaceAfter=3),
 'p': ParagraphStyle('p', fontName='Cal', fontSize=10, textColor=CAFE, leading=13, spaceAfter=4),
 'big': ParagraphStyle('big', fontName='CalB', fontSize=20, textColor=NAR, leading=24, alignment=1),
 'bigl': ParagraphStyle('bigl', fontName='Cal', fontSize=9, textColor=GRIS, leading=11.5, alignment=1),
 'tc': ParagraphStyle('tc', fontName='Cal', fontSize=9.5, textColor=CAFE, leading=12.5),
 'tcb': ParagraphStyle('tcb', fontName='CalB', fontSize=9.5, textColor=CAFE, leading=12.5),
 'th': ParagraphStyle('th', fontName='CalB', fontSize=9.5, textColor=colors.white, leading=12),
 'note': ParagraphStyle('note', fontName='Cal', fontSize=8.8, textColor=GRIS, leading=11, spaceAfter=3),
 'li': ParagraphStyle('li', fontName='Cal', fontSize=10, textColor=CAFE, leading=13, leftIndent=12, bulletIndent=0, spaceAfter=1.5),
}
P = lambda t, s='p': Paragraph(t, st[s])
LI = lambda t: Paragraph(t, st['li'], bulletText='•')
W = letter[0] - 4 * cm

def tabla(rows, widths, shade_rows=()):
    data = [[P(c, 'th') for c in rows[0]]] + [[P(c, 'tc') for c in r] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [('GRID', (0, 0), (-1, -1), 0.5, LINEA), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('BACKGROUND', (0, 0), (-1, 0), NAR)]
    for r in shade_rows: style.append(('BACKGROUND', (0, r), (-1, r), CREMA))
    t.setStyle(TableStyle(style)); return t

def tarjetas(items, w=5.6):
    data = [[Table([[P(v, 'big')], [P(l, 'bigl')]], colWidths=[w * cm]) for v, l in items]]
    t = Table(data, colWidths=[(w + 0.2) * cm] * len(items))
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), CREMA), ('INNERGRID', (0, 0), (-1, -1), 6, colors.white), ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    return t

def caja(flows):
    t = Table([[flows]], colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), CREMA), ('LINEBEFORE', (0, 0), (0, -1), 4, NAR), ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    return t

def pie(canvas, doc):
    canvas.saveState(); canvas.setFillColor(NAR); canvas.rect(0, letter[1] - 0.5 * cm, letter[0], 0.5 * cm, fill=1, stroke=0)
    canvas.setFillColor(AMAR); canvas.rect(0, letter[1] - 0.5 * cm, 4 * cm, 0.5 * cm, fill=1, stroke=0)
    canvas.setFont('Cal', 8.5); canvas.setFillColor(GRIS)
    canvas.drawString(2 * cm, 1.1 * cm, 'Heiiu English Academy · Propuesta de vinculación independiente · Aliado Comercial de Alianzas Empresariales · confidencial · octubre 2026')
    canvas.drawRightString(letter[0] - 2 * cm, 1.1 * cm, f'{doc.page}'); canvas.restoreState()

LISTA = 8_696_000; CUPO = 4_782_800; CUPO8 = 4_350_000; CUPO16 = 3_950_000
COM_EMP = 0.15   # sobre lo que paga la empresa (plan empresa), primer año
COM_EST = 0.08   # sobre los pagos de cada estudiante de alianza sin costo, 12 meses
m = lambda v: f'${v:,.0f}'.replace(',', '.')

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\Reinaldo Joya'
os.makedirs(BASE, exist_ok=True)
out = os.path.join(BASE, 'PROPUESTA_ALIADO_INDEPENDIENTE_ALIANZAS.pdf')
doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.6 * cm, bottomMargin=1.8 * cm, title='Propuesta de vinculación independiente · Aliado Comercial de Alianzas Empresariales')
E = []

E.append(P('HEIIU ENGLISH ACADEMY · PROPUESTA DE VINCULACIÓN INDEPENDIENTE', 'kicker'))
E.append(P('Aliado Comercial de Alianzas Empresariales', 'h1'))
E.append(P('Figura independiente, por resultados · Bucaramanga y área metropolitana · Preparada para Reinaldo Joya Suárez · octubre de 2026', 'sub'))

E.append(caja([P('Esta propuesta parte de lo que usted construyó: una red de gerentes y empresas abierta durante años en el sector financiero. Heiiu le propone poner esa red al servicio de un producto concreto, el inglés como entrenamiento de carrera para los equipos de esas empresas, con una figura <b>independiente, sin horario, sin sede y sin exclusividad</b>, que le paga sobre cada cierre.'),
              P('Es una figura honesta por las dos puntas: <b>no tiene ingreso fijo</b> y usted lo sabe desde hoy. A cambio, la comisión es más alta que la del cargo de planta y usted decide a quién visita, cuándo y cómo. La academia pone el producto, los documentos, la firma y la matrícula; usted pone la puerta.')]))
E.append(Spacer(1, 6))
E.append(tarjetas([('15%', 'de lo que paga cada empresa<br/>por los cupos de su gente (primer año)'), ('8%', 'de los pagos de cada estudiante<br/>que entra por su alianza (12 meses)'), ('$0', 'de costo para usted: sin cuota,<br/>sin meta mínima, sin horario')]))
E.append(Spacer(1, 6))

E.append(P('Qué hace el aliado (y qué no)', 'h2'))
for t in ['<b>Abre empresas por relación directa.</b> Usted contacta a gerentes y decisores que conoce o a los que llega por referencia, presenta a Heiiu y consigue la reunión. Esa es la parte que nadie puede hacer por usted.',
          '<b>Registra cada empresa antes de la primera reunión</b> en el tablero de alianzas de la academia (nombre, decisor, fecha). La empresa registrada queda a su nombre durante 6 meses; si en 60 días no hay reunión, se libera.',
          '<b>Presenta y cierra con el respaldo de gerencia.</b> Si usted lo pide, gerencia lo acompaña a la reunión de cierre. El convenio y la orden de plan empresa están escritos y los firma gerencia: usted cierra, la academia respalda.',
          '<b>No hace:</b> ferias, charlas masivas, reactivación de bases de datos ni atención de interesados que llegan por anuncios o redes. Eso es del equipo de la academia. Usted no cobra por eso ni se le exige.']:
    E.append(LI(t))

E.append(P('Lo que se lleva a las empresas', 'h2'))
E.append(tabla([
 ['Oferta', 'Qué recibe la empresa', 'Comisión del aliado'],
 ['A. Alianza sin costo', 'Firma un convenio estándar. Sus colaboradores y familias entran con beca: el programa completo, que vale ' + m(LISTA) + ', les queda desde ' + m(CUPO) + '. La empresa no paga nada.', '<b>8% de lo que pague cada estudiante</b> que llegue con la carta de la empresa, durante 12 meses desde su matrícula.'],
 ['B. Plan empresa', 'La empresa paga los cupos de su gente con tarifa por volumen sobre el precio de lista de ' + m(LISTA) + ': de 3 a 7 cupos, ' + m(CUPO) + ' cada uno; de 8 a 15, ' + m(CUPO8) + '; de 16 a 30, ' + m(CUPO16) + ' con grupo cerrado en la sede o en la empresa.', '<b>15% de lo que pague la empresa</b> durante el primer año del contrato.'],
], [3.2 * cm, 9.2 * cm, 5.1 * cm]))
E.append(P('Los valores ya traen el descuento sobre el precio de lista; por eso no hay descuentos adicionales que negociar. Cada estudiante sale con certificado por nivel, garantía de aprendizaje por escrito, módulo de graduación al cerrar A2 y portafolio profesional en B2. Lo que se vende es entrenamiento con resultado, nunca "fácil" ni "rápido": ese es el compromiso de la academia con cada empresa y es el mismo que le pedimos a usted.', 'note'))

E.append(KeepTogether([P('Cómo y cuándo se paga', 'h2'),
 LI('<b>Sobre lo que entra a caja.</b> La comisión se causa cuando la empresa o el estudiante paga, no cuando firma. Se liquida cada mes sobre lo recaudado el mes anterior y se paga dentro de los 5 días hábiles siguientes, contra cuenta de cobro, una vez vencido el plazo legal de retracto.'),
 LI('<b>Pagos a cuotas.</b> Si la empresa o el estudiante paga a cuotas, la comisión se paga cuota a cuota, en el mismo porcentaje.'),
 LI('<b>Figura legal.</b> Contrato de corretaje comercial entre independientes. Sin subordinación, sin horario, sin exclusividad: usted puede tener otras actividades mientras no represente otra academia de idiomas.')]))

E.append(KeepTogether([P('Lo que puede dejar en números', 'h2'),
 tabla([
  ['Cierre', 'La empresa o los estudiantes pagan', 'Comisión del aliado'],
  ['Plan empresa de 5 cupos (de contado)', m(5 * CUPO), m(5 * CUPO * COM_EMP)],
  ['Plan empresa de 10 cupos (de contado)', m(10 * CUPO8), m(10 * CUPO8 * COM_EMP)],
  ['Grupo cerrado de 16 en la empresa', m(16 * CUPO16), m(16 * CUPO16 * COM_EMP)],
  ['Alianza sin costo con 10 estudiantes pagando cuotas de ' + m(450_000), m(10 * 450_000) + ' al mes', m(10 * 450_000 * COM_EST) + ' cada mes, durante 12 meses'],
 ], [6.4 * cm, 5.3 * cm, 5.8 * cm]),
 P('Valores de 2026 con pagos de contado donde se indica. Un plan empresa de 10 cupos deja en un solo cierre lo que el cargo de planta deja en un mes con la meta cumplida. La diferencia es que aquí no hay piso: el mes sin cierre es un mes sin ingreso.', 'note')]))

E.append(KeepTogether([P('Seguimiento y piloto de 90 días', 'h2'),
 LI('<b>Una reunión semanal de 30 minutos con gerencia, el mismo día y a la misma hora</b>, presencial o virtual, liderada por usted: empresas registradas, reuniones hechas, próximos pasos. Es la única exigencia de agenda, y no se cancela.'),
 LI('<b>Piloto de 90 días.</b> Al día 90 se revisa junto con usted: si hay al menos un convenio o plan empresa firmado con el primer pago hecho, la figura continúa por 12 meses renovables. Si no lo hay, se cierra sin costo ni deuda para ninguna de las partes y las comisiones causadas se pagan igual.'),
 LI('<b>Inducción corta.</b> Dos sesiones de 2 horas en la sede con gerencia: el producto, los documentos, la forma de presentar la academia y la tabla de precios. Después, su primera reunión de cierre va acompañada.')]))

E.append(KeepTogether([P('Siguiente paso', 'h2'),
 P('Si esta figura le interesa, respóndanos por escrito con las tres primeras empresas que registraría y la fecha en que puede hacer la inducción. Con eso se firma el contrato de corretaje y se abre el tablero a su nombre.'),
 P('Esta es una propuesta de vinculación. Las condiciones definitivas quedan en el contrato de corretaje comercial y su anexo de comisiones, que se firman antes de la primera reunión con una empresa.', 'note')]))

doc.build(E, onFirstPage=pie, onLaterPages=pie); print('OK', out)
