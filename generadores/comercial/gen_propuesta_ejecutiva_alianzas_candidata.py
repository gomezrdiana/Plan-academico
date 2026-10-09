# -*- coding: utf-8 -*-
"""Propuesta de vinculación para la CANDIDATA (Ejecutiva de Alianzas Empresariales).
Versión externa de PROPUESTA_HUNTER_B2B: en segunda persona, sin márgenes de la academia, sin guion ni notas internas.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PROPUESTA_EJECUTIVA_ALIANZAS.pdf"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

F = 'C:/Windows/Fonts/'
pdfmetrics.registerFont(TTFont('Cal', F + 'calibri.ttf')); pdfmetrics.registerFont(TTFont('CalB', F + 'calibrib.ttf')); pdfmetrics.registerFont(TTFont('Geo', F + 'georgiai.ttf'))
NAR = colors.HexColor('#E54C09'); AMAR = colors.HexColor('#FBC900'); CREMA = colors.HexColor('#FFF8E7'); CAFE = colors.HexColor('#30271C'); GRIS = colors.HexColor('#6B6B6B'); LINEA = colors.HexColor('#E6DCCB')
st = {
 'kicker': ParagraphStyle('kicker', fontName='CalB', fontSize=10, textColor=GRIS, leading=13, spaceAfter=2),
 'h1': ParagraphStyle('h1', fontName='CalB', fontSize=24, textColor=NAR, leading=28, spaceAfter=6),
 'sub': ParagraphStyle('sub', fontName='Cal', fontSize=11.5, textColor=CAFE, leading=15, spaceAfter=10),
 'h2': ParagraphStyle('h2', fontName='CalB', fontSize=14, textColor=NAR, leading=17, spaceBefore=6, spaceAfter=4),
 'p': ParagraphStyle('p', fontName='Cal', fontSize=10, textColor=CAFE, leading=13.5, spaceAfter=5),
 'big': ParagraphStyle('big', fontName='CalB', fontSize=22, textColor=NAR, leading=26, alignment=1),
 'bigl': ParagraphStyle('bigl', fontName='Cal', fontSize=9.5, textColor=GRIS, leading=12, alignment=1),
 'q': ParagraphStyle('q', fontName='Geo', fontSize=11.5, textColor=CAFE, leading=16, leftIndent=10, rightIndent=10, spaceAfter=6),
 'tc': ParagraphStyle('tc', fontName='Cal', fontSize=9.5, textColor=CAFE, leading=12.5),
 'tcb': ParagraphStyle('tcb', fontName='CalB', fontSize=9.5, textColor=CAFE, leading=12.5),
 'th': ParagraphStyle('th', fontName='CalB', fontSize=9.5, textColor=colors.white, leading=12),
 'note': ParagraphStyle('note', fontName='Cal', fontSize=9, textColor=GRIS, leading=12, spaceAfter=6),
 'li': ParagraphStyle('li', fontName='Cal', fontSize=10, textColor=CAFE, leading=13.5, leftIndent=12, bulletIndent=0, spaceAfter=2),
}
P = lambda t, s='p': Paragraph(t, st[s])
LI = lambda t: Paragraph(t, st['li'], bulletText='•')

def tabla(rows, widths, bold_col=None, shade_rows=()):
    data = [[P(c, 'th') for c in rows[0]]] + [[P(c, 'tcb' if (bold_col is not None and j == bold_col) else 'tc') for j, c in enumerate(r)] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [('GRID', (0, 0), (-1, -1), 0.5, LINEA), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('BACKGROUND', (0, 0), (-1, 0), NAR)]
    for r in shade_rows: style.append(('BACKGROUND', (0, r), (-1, r), CREMA))
    t.setStyle(TableStyle(style)); return t

def tarjetas(items, w=4.0):
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
    canvas.drawString(2 * cm, 1.1 * cm, 'Heiiu English Academy · Propuesta de vinculación · Ejecutivo(a) de Alianzas Empresariales · confidencial · octubre 2026')
    canvas.drawRightString(letter[0] - 2 * cm, 1.1 * cm, f'{doc.page}'); canvas.restoreState()

CUPO = 4_782_800; COM = 0.10
m = lambda v: f'${v:,.0f}'.replace(',', '.')
out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PROPUESTA_EJECUTIVA_ALIANZAS.pdf'
doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.6 * cm, bottomMargin=1.8 * cm, title='Propuesta de vinculación · Ejecutivo(a) de Alianzas Empresariales')
W = letter[0] - 4 * cm
E = []

# ---------- 1. Apertura ----------
E.append(P('HEIIU ENGLISH ACADEMY · PROPUESTA DE VINCULACIÓN', 'kicker'))
E.append(P('Ejecutivo(a) de Alianzas Empresariales', 'h1'))
E.append(P('Canal corporativo e institucional · Bucaramanga y área metropolitana', 'sub'))
E.append(caja([P('Las empresas de Bucaramanga necesitan gente que hable inglés, y no solo dentro de su equipo. Con sus programas de bienestar, con beneficios para las familias de sus colaboradores o a través de sus fundaciones, pueden aportar a la educación de su comunidad: formar personas en inglés para abrirles oportunidades. Heiiu tiene el programa, la licencia y una garantía de aprendizaje por escrito. <b>Buscamos a la persona que construya este canal y lo haga suyo.</b>'),
              P('El cargo requiere experiencia en alianzas estratégicas, convenios y dirección comercial: llevar las ofertas de Heiiu a las empresas y convertirlas en estudiantes.')]))
E.append(Spacer(1, 6))
E.append(tarjetas([('10%', 'de lo que paga cada empresa<br/>por los cupos de su gente'), ('6%', 'mes a mes, de cada estudiante<br/>que entra por la alianza'), ('$3.5M', 'ingreso mínimo garantizado los<br/>3 primeros meses (con indicadores)')], w=5.6))

# ---------- 2. El rol ----------
E.append(P('El rol', 'h2'))
E.append(P('Liderar el desarrollo del canal corporativo e institucional de Heiiu: identificar, abrir y consolidar alianzas con empresas, áreas de bienestar y fundaciones de Bucaramanga y su área metropolitana. Es un rol de campo y de relacionamiento con la alta dirección; la atención de prospectos individuales y el proceso de matrícula están a cargo del equipo de asesoría comercial.'))
for t in ['<b>Prospección y relacionamiento:</b> identificar empresas y fundaciones con potencial y establecer contacto con quienes toman la decisión (gerencia, talento humano, bienestar, responsabilidad social).',
          '<b>Presentación de la propuesta de valor:</b> exponer las dos modalidades de vinculación (alianza sin costo y plan empresa) en reuniones ejecutivas.',
          '<b>Negociación y cierre:</b> formalizar convenios y órdenes de plan empresa dentro de las condiciones comerciales establecidas, con firma de gerencia.',
          '<b>Activación de alianzas:</b> coordinar charlas, diagnósticos de nivel y clases de muestra que conviertan cada convenio en estudiantes matriculados.',
          '<b>Desarrollo de nuevas oportunidades:</b> a partir de lo que se escucha en el mercado, proponer a gerencia nuevos programas, formatos y líneas de expansión (sectores, ciudades, convocatorias públicas o de cooperación).']:
    E.append(LI(t))

E.append(KeepTogether([P('Autonomía y seguimiento', 'h2'),
 P('El cargo tiene autonomía para organizar su agenda, sus visitas y su forma de trabajar. Lo que no se suelta es el seguimiento: este canal es estratégico para Heiiu y queremos potenciarlo al máximo en este momento, así que es crucial no dejar pasar ninguna oportunidad. Por eso lo acompañamos de cerca.'),
 LI('<b>Tablero de alianzas:</b> se lleva al día con empresas, reuniones, firmas, cupos y próximos pasos. Es la herramienta del cargo: deja registrada cada empresa que se abre, protege la cartera y es la base de las reuniones.'),
 LI('<b>Dos reuniones fijas por semana, de 30 minutos, con gerencia:</b> el lunes se definen las empresas y reuniones de la semana; el jueves se revisan resultados contra la meta del mes y se ajusta.')]))

# ---------- 3. Las ofertas ----------
E.append(PageBreak())
E.extend(([P('Lo que se lleva a las empresas', 'h2'),
 tabla([
 ['Oferta', 'Qué recibe la empresa', 'Comisión del cargo'],
 ['A. Alianza sin costo', 'Firma un convenio estándar. Sus colaboradores entran con beca del Fondo (columna Transformación): el programa completo, que vale ' + m(8_696_000) + ', les queda desde ' + m(4_782_800) + '. Además, la empresa entrega 3 becas con su nombre por trimestre. A la empresa no le cuesta nada: es un beneficio para su gente.', '<b>6% de lo que pague cada estudiante</b> que entre por esa alianza, mes a mes, durante todo su programa. Es la cartera del cargo: crece con cada alianza activa.'],
 ['B. Plan empresa', 'La empresa paga los cupos de su gente con tarifa corporativa por volumen, sobre un precio de lista de ' + m(8_696_000) + ' por persona: de 3 a 7 cupos, ' + m(4_782_800) + ' cada uno; de 8 a 15, ' + m(4_350_000) + '; de 16 a 30, ' + m(3_950_000) + ' con grupo cerrado en la sede o en la empresa.', '<b>10% de lo que pague la empresa</b> el primer año. Un plan de 5 cupos deja ' + m(5 * CUPO * COM) + '; un grupo cerrado de 16, ' + m(16 * 3_950_000 * COM) + '.'],
 ], [3.4 * cm, 7.2 * cm, W - 10.6 * cm], bold_col=0),
 P('Todos estos valores ya traen el descuento sobre el precio de lista (' + m(8_696_000) + ' el programa completo, 575 horas, de cero a B2): por eso no hay descuentos adicionales que negociar. El convenio y la orden de plan empresa están escritos y son estándar. Más de 30 cupos se cotizan con gerencia.', 'note')]))

# ---------- 4. Compensación ----------
E.append(KeepTogether([P('Esquema de compensación', 'h2'),
 P('La vinculación es mediante <b>contrato laboral desde el primer día</b>: salario mínimo legal vigente más auxilio de transporte (' + m(2_000_000) + ' mensuales en 2026; se ajusta cada enero según el decreto del Gobierno), con prestaciones sociales y seguridad social. A este básico se suma una <b>comisión variable desde el primer cierre</b>, que también constituye salario.'),
 P('Durante los tres primeros meses, mientras se construye la cartera, la academia garantiza un <b>ingreso mínimo de ' + m(3_500_000) + '</b> en cada mes en que se cumplan los indicadores de gestión. Cuando las comisiones superan ese valor, se liquida el total generado, sin tope.'),
 tabla([
 ['En el mes', 'Compensación'],
 ['Se cumplen los indicadores y la comisión es inferior a ' + m(3_500_000), 'Se garantiza el ingreso mínimo de ' + m(3_500_000) + '.'],
 ['Se cumplen los indicadores y la comisión supera ese valor', 'Básico + la comisión total generada, sin tope.'],
 ['No se alcanzan los indicadores', 'Básico + la comisión generada, y un plan de ajuste de una semana con metas concretas.'],
 ], [8.2 * cm, W - 8.2 * cm], bold_col=0)]))

# ---------- 5. Proyección ----------
E.append(KeepTogether([P('Proyección comisional (pagos de contado)', 'h2'),
 tabla([
 ['Cierre en el mes', 'La empresa paga', 'Comisión', 'Ingreso ese mes'],
 ['3 cupos de plan empresa', m(3 * CUPO), m(3 * CUPO * COM), m(3_500_000) + ' (meses 1-3) · ' + m(3 * CUPO * COM + 2_000_000) + ' después'],
 ['5 cupos', m(5 * CUPO), m(5 * CUPO * COM), m(5 * CUPO * COM + 2_000_000)],
 ['10 cupos', m(10 * CUPO), m(10 * CUPO * COM), m(10 * CUPO * COM + 2_000_000)],
 ['15 cupos (desde el mes 7)', m(15 * CUPO), m(15 * CUPO * COM), m(15 * CUPO * COM + 2_549_095)],
 ['Un grupo cerrado de 15 (' + m(4_350_000) + ' c/u)', m(15 * 4_350_000), m(15 * 4_350_000 * COM), m(15 * 4_350_000 * COM + 2_000_000)],
 ], [5.6 * cm, 3.6 * cm, 3.2 * cm, W - 12.4 * cm], bold_col=3, shade_rows=(4,)),
 P('<b>La cartera se suma a todo esto:</b> 10 estudiantes de las alianzas pagando cuotas de ' + m(450_000) + ' generan ' + m(270_000) + ' de comisión cada mes, y 30 estudiantes, ' + m(810_000) + ' cada mes, mientras estudian. Cada alianza activa sigue generando comisión. Si la empresa paga a cuotas, la comisión se liquida a medida que paga.', 'note')]))

# ---------- 6. Plan de crecimiento ----------
E.append(KeepTogether([P('Plan de crecimiento', 'h2'),
 tabla([
 ['Etapa', 'Básico', 'Meta del mes', 'Ingreso con la meta'],
 ['Meses 1 a 3', 'Mínimo legal vigente + auxilio (' + m(2_000_000) + ' en 2026)', 'Construir la base (ver indicadores)', 'Desde ' + m(3_500_000) + ' garantizado'],
 ['Meses 4 a 6', 'Mínimo legal vigente + auxilio', '10 cupos', m(6_780_000)],
 ['Meses 7 a 12', 'Mínimo vigente + ' + m(550_000) + ' + auxilio (' + m(2_550_000) + ' en 2026)', '15 cupos', m(9_720_000)],
 ['Año 2', 'Mínimo vigente + ' + m(850_000) + ' + auxilio (' + m(2_850_000) + ' en 2026)', '15 a 20 cupos', m(10_000_000) + ' a ' + m(12_400_000)],
 ], [2.8 * cm, 4.8 * cm, 4.2 * cm, W - 11.8 * cm], bold_col=3, shade_rows=(3, 4)),
 P('Valores calculados con el salario mínimo y el auxilio de transporte de 2026. Cada enero se ajustan al decreto del Gobierno: el básico de cada etapa nunca queda por debajo del mínimo legal vigente más el auxilio, y los ingresos de la tabla suben en la misma proporción. Los aumentos de etapa son por resultados, no por calendario: se pasa a la siguiente etapa cuando se cumplió la meta en al menos 2 de los 3 meses anteriores. No incluyen la cartera de alianzas.', 'note')]))

# ---------- 7. Lo que buscamos ----------
E.append(KeepTogether([P('Lo que buscamos en la persona que se una al equipo', 'h2'),
 P('Un ritmo de dirección comercial: dos empresas nuevas con quien decide, cada día. En los tres primeros meses, estos son los indicadores de gestión que respaldan el ingreso mínimo de ' + m(3_500_000) + ':'),
 tabla([
 ['Mes', 'Gestión (cada mes)', 'Resultados'],
 ['Mes 1', '40 empresas contactadas con quien decide · 12 reuniones · 3 activaciones', '2 firmas (convenio o plan)'],
 ['Mes 2', '40 empresas · 12 reuniones · 3 activaciones', '4 firmas acumuladas · 5 cupos corporativos'],
 ['Mes 3', '40 empresas · 12 reuniones · 3 activaciones', '6 firmas acumuladas · 10 cupos acumulados'],
 ], [2.0 * cm, 8.6 * cm, W - 10.6 * cm], bold_col=0),
 P('Desde el mes 4 se mantienen como indicador de cada mes las 40 empresas y las 12 reuniones, junto con la meta de cupos; y cada alianza activa debe tener al menos una activación por trimestre (la alianza que pasa un trimestre sin actividad deja de contar). Cada contacto, reunión, activación, firma y cupo se registra con su prueba en el tablero el mismo día; las definiciones exactas se entregan en la inducción. Una alianza que no se activa en 30 días no cuenta como firma.', 'note')]))

# ---------- 8. Reglas ----------
E.append(KeepTogether([P('Reglas de atribución y cartera', 'h2'),
 LI('<b>Empresas registradas:</b> la empresa que el cargo registra primero en el tablero queda a su nombre.'),
 LI('<b>Cartera propia:</b> el estudiante que llega con la carta de postulación de una empresa aliada genera el 6% mes a mes para el cargo, aunque la matrícula la haga una asesora.'),
 LI('<b>Canales separados:</b> lo que llega por anuncios y WhatsApp es del equipo de asesoría; lo que se abre en campo es del cargo.'),
 LI('<b>Firma de gerencia:</b> cada convenio y cada orden los firma gerencia; el cargo cierra y la academia respalda.')]))

# ---------- 9. Herramientas ----------
E.append(KeepTogether([P('Herramientas desde el primer día', 'h2'),
 LI('El convenio de alianza, la orden de plan empresa y la tabla de precios, listos para firmar.'),
 LI('Un producto que se puede mostrar: academia presencial con licencia de la Secretaría de Educación desde 2012 y garantía de aprendizaje por escrito, la única academia presencial de Bucaramanga que la firma.'),
 LI('Clases de muestra y diagnósticos de inglés para activar a las empresas, dictados por el equipo académico.')]))

doc.build(E, onFirstPage=pie, onLaterPages=pie); print('OK', out)
