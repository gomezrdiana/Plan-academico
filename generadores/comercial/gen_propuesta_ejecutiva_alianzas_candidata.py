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
E.append(caja([P('Las empresas de Bucaramanga necesitan gente que hable inglés, y no solo dentro de su equipo. Con sus programas de bienestar, con beneficios para las familias de sus colaboradores o a través de sus fundaciones, pueden aportar a la educación de su comunidad: formar personas en inglés para abrirles oportunidades. Heiiu tiene el programa, la licencia y una garantía de aprendizaje por escrito.'),
              P('Pero en Heiiu no formamos solo en inglés: formamos personas. Cada clase entrena virtudes (prudencia, fortaleza, templanza y justicia) y hábitos de constancia y cumplimiento, porque el inglés abre la puerta y el carácter es el que sostiene lo que viene después. Y cada estudiante termina con resultados que puede mostrar, no solo con un certificado: la creación de su propia página web, el pitch para un proyecto de venta o un video presentándose para ser considerado en una vacante. Esa es nuestra apuesta por un mejor santandereano: más preparado para emprender, para trabajar con el mundo y para competir en una economía que ya funciona con inteligencia artificial. <b>Buscamos a la persona que lleve esta propuesta a las empresas, construya este canal y lo haga suyo.</b>'),
              P('El cargo requiere experiencia en alianzas estratégicas, convenios y dirección comercial: llevar las ofertas de Heiiu a las empresas y convertirlas en estudiantes.')]))
E.append(Spacer(1, 6))
E.append(tarjetas([('10%', 'de lo que paga cada empresa<br/>por los cupos de su gente'), ('6%', 'de los pagos de cada estudiante<br/>de la alianza (12 meses)'), ('$3.5M', 'ingreso mínimo garantizado los<br/>3 primeros meses (con indicadores)')], w=5.6))

# ---------- 2. El rol ----------
E.append(P('El rol', 'h2'))
E.append(P('Liderar el desarrollo del canal corporativo e institucional de Heiiu: identificar, abrir y consolidar alianzas con empresas, áreas de bienestar, fundaciones y colegios de Bucaramanga y su área metropolitana. Es un rol de campo y de relacionamiento con la alta dirección; la atención de prospectos individuales y el proceso de matrícula están a cargo del equipo de asesoría comercial.'))
for t in ['<b>Colegios y ferias:</b> relacionamiento con colegios (rectoría, coordinación académica, asociaciones de padres) y participación en ferias escolares, universitarias y empresariales para presentar los programas y captar interesados.',
          '<b>Prospección y relacionamiento:</b> identificar empresas y fundaciones con potencial y establecer contacto con quienes toman la decisión (gerencia, talento humano, bienestar, responsabilidad social).',
          '<b>Presentación de la propuesta de valor:</b> exponer las dos modalidades de vinculación (alianza sin costo y plan empresa) en reuniones ejecutivas.',
          '<b>Negociación y cierre:</b> formalizar convenios y órdenes de plan empresa dentro de las condiciones comerciales establecidas, con firma de gerencia.',
          '<b>Activación de alianzas:</b> coordinar charlas, diagnósticos de nivel y clases de muestra que conviertan cada convenio en estudiantes matriculados.',
          '<b>Desarrollo de nuevas oportunidades:</b> a partir de lo que se escucha en el mercado, proponer a gerencia nuevos programas (por ejemplo, inglés para emprendedores o inglés para trabajar con inteligencia artificial), formatos y líneas de expansión (sectores, ciudades, convocatorias públicas o de cooperación).']:
    E.append(LI(t))

E.append(KeepTogether([P('Autonomía y seguimiento', 'h2'),
 P('El cargo tiene autonomía para organizar su agenda, sus visitas y su forma de trabajar. Lo que no se suelta es el seguimiento: este canal es estratégico para Heiiu y queremos potenciarlo al máximo en este momento, así que es crucial no dejar pasar ninguna oportunidad. Por eso el seguimiento es diario.'),
 LI('<b>Tablero de alianzas:</b> se lleva al día con empresas, reuniones, firmas, cupos y próximos pasos. Es la herramienta del cargo: deja registrada cada empresa que se abre, protege la cartera y es la base de las reuniones.'),
 LI('<b>Seguimiento diario con gerencia, 15 minutos a hora fija:</b> qué se logró el día anterior frente al plan y qué empresas y reuniones siguen hoy.'),
 LI('<b>Planeación semanal, los lunes, 30 minutos:</b> empresas objetivo y reuniones de la semana, y avance frente a la meta del trimestre.')]))

# ---------- 3. Las ofertas ----------
E.extend(([P('Lo que se lleva a las empresas', 'h2'),
 tabla([
 ['Oferta', 'Qué recibe la empresa', 'Comisión del cargo'],
 ['A. Alianza sin costo', 'Firma un convenio estándar. Sus colaboradores entran con beca del Fondo (columna Transformación): el programa completo, que vale ' + m(8_696_000) + ', les queda desde ' + m(4_782_800) + '. Además, la empresa entrega 3 becas con su nombre por trimestre. A la empresa no le cuesta nada: es un beneficio para su gente.', '<b>6% de lo que pague cada estudiante</b> que entre por esa alianza durante los 12 meses siguientes a la firma de su matrícula, y 3% del mes 13 al 24. Es la cartera del cargo: crece con cada alianza activa.'],
 ['B. Plan empresa', 'La empresa paga los cupos de su gente con tarifa corporativa por volumen, sobre un precio de lista de ' + m(8_696_000) + ' por persona: de 3 a 7 cupos, ' + m(4_782_800) + ' cada uno; de 8 a 15, ' + m(4_350_000) + '; de 16 a 30, ' + m(3_950_000) + ' con grupo cerrado en la sede o en la empresa.', '<b>10% de lo que pague la empresa</b> el primer año. Un plan de 5 cupos deja ' + m(5 * CUPO * COM) + '; un grupo cerrado de 16, ' + m(16 * 3_950_000 * COM) + '.'],
 ], [3.4 * cm, 7.2 * cm, W - 10.6 * cm], bold_col=0),
 P('Todos estos valores ya traen el descuento sobre el precio de lista (' + m(8_696_000) + ' el programa completo, 575 horas, de cero a B2): por eso no hay descuentos adicionales que negociar. El convenio y la orden de plan empresa están escritos y son estándar. Más de 30 cupos se cotizan con gerencia.', 'note')]))

E.append(KeepTogether([P('Lo que cada estudiante se lleva (además del certificado por nivel)', 'h2'),
 LI('<b>Módulo de Graduación al cerrar A2, a elección:</b> <i>Emprendedor</i> (página web publicada con dominio propio, pitch de negocio en inglés, perfil para vender en el exterior, cuenta de pagos internacional y primer mensaje de venta a un cliente real) o <i>Pasaporte</i> (video de presentación, hoja de vida y entrevista en inglés para trabajar o estudiar afuera).'),
 LI('<b>Portafolio profesional en B2:</b> hoja de vida y perfil de LinkedIn en inglés, video pitch de 60 segundos, banco de respuestas para entrevistas y proyecto final.'),
 LI('<b>Garantía de aprendizaje por escrito</b> y formación en virtudes y hábitos en cada clase.'),
 P('Para una empresa o una fundación, esto es lo que hace distinta la propuesta: no financia horas de clase, financia personas que salen con un resultado concreto.', 'note')]))

# ---------- 4. Compensación ----------
E.append(KeepTogether([P('Esquema de compensación', 'h2'),
 P('La vinculación es mediante <b>contrato laboral desde el primer día</b>: salario mínimo legal vigente más auxilio de transporte (' + m(2_000_000) + ' mensuales en 2026; se ajusta cada enero según el decreto del Gobierno), con prestaciones sociales y seguridad social. A este básico se suma una <b>comisión variable desde el primer cierre</b>, que también constituye salario.'),
 P('<b>La meta se mide en ventas firmadas; la comisión se paga sobre lo que efectivamente entra a caja.</b> Cada mes se liquida la comisión sobre lo recaudado en el mes anterior. Ejemplo: si en un periodo se firman ' + m(300_000_000) + ' en matrículas y planes, y en ese periodo entran ' + m(100_000_000) + ', la comisión se paga sobre los ' + m(100_000_000) + '; el resto se va pagando en los meses en que la empresa o el estudiante paguen sus cuotas.'),
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
 P('<b>La cartera se suma a todo esto:</b> 10 estudiantes de las alianzas pagando cuotas de ' + m(450_000) + ' generan ' + m(270_000) + ' de comisión cada mes, y 30 estudiantes, ' + m(810_000) + ' cada mes, mientras estudian. Cada estudiante genera 6% en los 12 meses siguientes a la firma de su matrícula y 3% del mes 13 al 24; por eso el ingreso grande depende de seguir abriendo alianzas. Si la empresa paga a cuotas, la comisión se liquida a medida que paga.', 'note')]))

# ---------- 6. Plan de crecimiento ----------
E.append(KeepTogether([P('Plan de crecimiento: metas trimestrales', 'h2'),
 P('La meta se mide en <b>ventas firmadas</b> (valor total de los contratos con la inicial pagada: plan empresa, cupos y programas personalizados, de contado o a cuotas) y se evalúa <b>por trimestre</b>. Sube cada trimestre según este calendario, pactado desde la firma; nunca según lo vendido en el periodo anterior.'),
 tabla([
 ['Trim.', 'Meses', 'Meta del trimestre (≈ al mes)', 'Programas completos en el trimestre**', 'Básico', 'Ingreso mensual con la meta*'],
 ['T1', '1-3', m(90_000_000) + ' (≈' + m(30_000_000) + '/mes)', '≈ 18 + 3 Arranque (6 + 1 al mes)', 'Mínimo vigente + auxilio', m(5_000_000) + ' (mínimo ' + m(3_500_000) + ' garantizado)'],
 ['T2', '4-6', m(144_000_000) + ' (≈' + m(48_000_000) + '/mes)', '≈ 30', 'Mínimo vigente + auxilio', m(6_800_000)],
 ['T3', '7-9', m(198_000_000) + ' (≈' + m(66_000_000) + '/mes)', '≈ 41', 'Mínimo + ' + m(550_000) + ' + auxilio', m(9_150_000)],
 ['T4', '10-12', m(234_000_000) + ' (≈' + m(78_000_000) + '/mes)', '≈ 49', 'Mínimo + ' + m(550_000) + ' + auxilio', m(10_350_000)],
 ['T5', '13-15', m(252_000_000) + ' (≈' + m(84_000_000) + '/mes)', '≈ 53', 'Mínimo + ' + m(850_000) + ' + auxilio', m(11_250_000)],
 ['T6', '16-18', m(276_000_000) + ' (≈' + m(92_000_000) + '/mes)', '≈ 58', 'Mínimo + ' + m(850_000) + ' + auxilio', m(12_050_000)],
 ['T7', '19-21', m(300_000_000) + ' (≈' + m(100_000_000) + '/mes)', '≈ 63', 'Mínimo + ' + m(850_000) + ' + auxilio', m(12_850_000)],
 ['T8', '22-24', m(324_000_000) + ' (≈' + m(108_000_000) + '/mes)', '≈ 68', 'Mínimo + ' + m(850_000) + ' + auxilio', m(13_650_000)],
 ['Desde T9', '25+', 'La del trimestre anterior + 2,5%', '—', 'Se revisa cada año', '—'],
 ], [1.7 * cm, 1.4 * cm, 4.0 * cm, 2.6 * cm, 4.0 * cm, W - 13.7 * cm], bold_col=5, shade_rows=(5, 6, 7, 8)),
 P('**Programa completo de cero a B2 a tarifa corporativa (' + m(4_782_800) + ', equivalente a 45% de beca sobre el precio de lista de ' + m(8_696_000) + '); el Arranque A1+A2 vale ' + m(2_990_000) + '. Cualquier combinación de contado, cuotas, cupos o personalizados cuenta por su valor. A medida que la marca se posicione en el canal corporativo y se vendan programas con menos beca o de mayor valor (personalizados), cada venta vale más: la meta se alcanza con menos programas y la comisión por venta sube. *Básico más 10% de comisión sobre la meta, con pagos de contado y valores de 2026; no incluye acelerador ni cartera. El mínimo y el auxilio se ajustan cada enero según el decreto del Gobierno. El básico sube de escalón cuando se cumple la meta en al menos 2 de los 3 últimos trimestres. Los contratos firmados con inicial pagada cuentan para la meta aunque el grupo inicie después: la capacidad (salones, profesores, horarios) es responsabilidad de la academia.', 'note')]))

E.append(KeepTogether([P('Acelerador por sobrecumplimiento (sin tope)', 'h2'),
 tabla([
 ['Ventas del trimestre frente a la meta', 'Comisión sobre lo que entra en ese tramo'],
 ['Hasta el 100%', '10%'],
 ['Del 100% al 130%', '15%'],
 ['Más del 130%', '20%'],
 ], [8.2 * cm, W - 8.2 * cm], bold_col=0),
 P('El acelerador aplica en los trimestres con al menos 2 empresas nuevas firmadas con inicial pagada: premia abrir mercado, no solo crecer cuentas existentes. Ejemplo con meta trimestral de ' + m(252_000_000) + ': si se firman ' + m(360_000_000) + ', la comisión pasa de ' + m(36_000_000) + ' a ' + m(43_000_000) + ' en el trimestre.', 'note')]))

E.append(KeepTogether([P('Proyección del cargo', 'h2'),
 P('Con resultados sostenidos, el cargo puede crecer hacia la coordinación de un equipo comercial corporativo o liderar la apertura de nuevas sedes y mercados, de acuerdo con la evolución del canal y las decisiones de gerencia.')]))

# ---------- 7. Lo que buscamos ----------
E.append(KeepTogether([P('Lo que buscamos en la persona que se una al equipo', 'h2'),
 P('Esperamos un ritmo constante: hablar cada día con quien decide en al menos dos empresas nuevas (40 al mes). En los tres primeros meses, cumplir esa gestión y las firmas del mes asegura el ingreso mínimo de ' + m(3_500_000) + '; la meta de ventas es de ' + m(30_000_000) + ' al mes:'),
 tabla([
 ['Mes', 'Gestión y firmas (respaldan el ingreso mínimo)', 'Meta de ventas'],
 ['Mes 1', '40 empresas contactadas con quien decide · 12 reuniones · 2 firmas', m(30_000_000) + ' (≈ 6 programas completos + 1 Arranque)'],
 ['Mes 2', '40 empresas · 12 reuniones · 4 firmas acumuladas · 2 activaciones', m(30_000_000) + ' en el mes'],
 ['Mes 3', '40 empresas · 12 reuniones · 6 firmas acumuladas · 3 activaciones', m(30_000_000) + ' en el mes'],
 ], [2.0 * cm, 8.6 * cm, W - 10.6 * cm], bold_col=0),
 P('Desde el mes 4 se mantienen como indicador de cada mes las 40 empresas y las 12 reuniones, junto con la meta de cupos; y cada alianza activa debe tener al menos una activación por trimestre (la alianza que pasa un trimestre sin actividad deja de contar). Cada contacto, reunión, activación, firma y cupo se registra con su prueba en el tablero el mismo día; las definiciones exactas se entregan en la inducción. Una alianza que no se activa en 30 días no cuenta como firma. Solo para el primer mes: lo firmado con inicial pagada hasta 5 días calendario después del cierre del mes 1 cuenta para el mes 1.', 'note')]))

# ---------- 8. Reglas ----------
E.append(KeepTogether([P('Reglas de atribución y cartera', 'h2'),
 LI('<b>Empresas registradas:</b> la empresa que el cargo registra primero en el tablero queda a su nombre.'),
 LI('<b>Cartera propia:</b> el estudiante que llega con la carta de postulación de una empresa aliada genera para el cargo el 6% de sus pagos durante los 12 meses siguientes a la firma de su matrícula y el 3% del mes 13 al 24, aunque la matrícula la haga una asesora. La cartera no cuenta para la meta.'),
 LI('<b>Canales claros, trabajo en equipo:</b> lo que llega por anuncios y WhatsApp es del equipo de asesoría; lo que se abre en campo es del cargo. Las asesoras apoyan las activaciones y la matrícula de los interesados del canal, y cada una cobra su parte.'),
 LI('<b>Bases de datos propias:</b> los contactos que el cargo genere en ferias, colegios, charlas y empresas se registran en el sistema de la academia dentro de las 24 horas siguientes. El cargo es responsable de que el equipo de asesoría los gestione, con o sin su presencia, y hace seguimiento hasta el cierre. Las matrículas que salgan de esas bases, registradas a su nombre antes del primer contacto de la asesora, generan su comisión de cartera (6% y 3%).'),
 LI('<b>Cierre de apoyo:</b> cuando una asesora no pueda atender a un cliente y gerencia o coordinación se lo asigne, el cargo puede cerrar esa matrícula y recibe la misma comisión de cierre que habría recibido la asesora. Esas ventas no cuentan para la meta trimestral del cargo.'),
 LI('<b>Firma de gerencia:</b> cada convenio y cada orden los firma gerencia; el cargo cierra y la academia respalda.')]))

# ---------- 9. Herramientas ----------
E.append(KeepTogether([P('Herramientas y equipo desde el primer día', 'h2'),
 LI('<b>Un equipo que trabaja contigo:</b> el equipo de asesoría comercial apoya las activaciones (charlas, ferias, jornadas de inscripción en empresas y colegios), atiende y matricula a los interesados que genera el canal, y coordinación académica dicta las clases de muestra y los diagnósticos. El cargo lidera el canal; no lo hace solo.'),
 LI('El convenio de alianza, la orden de plan empresa y la tabla de precios, listos para firmar.'),
 LI('Un producto que se puede mostrar: academia presencial con licencia de la Secretaría de Educación desde 2012 y garantía de aprendizaje por escrito, la única academia presencial de Bucaramanga que la firma.'),
 LI('Clases de muestra y diagnósticos de inglés para activar a las empresas, dictados por el equipo académico.')]))

doc.build(E, onFirstPage=pie, onLaterPages=pie); print('OK', out)
