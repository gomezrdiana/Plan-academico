# -*- coding: utf-8 -*-
"""Propuesta HUNTER B2B (perfil senior de convenios) — modelo absorbible con tres escalones, metas en empresas/cupos.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PROPUESTA_HUNTER_B2B.pdf"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

F = 'C:/Windows/Fonts/'
pdfmetrics.registerFont(TTFont('Cal', F + 'calibri.ttf')); pdfmetrics.registerFont(TTFont('CalB', F + 'calibrib.ttf')); pdfmetrics.registerFont(TTFont('Geo', F + 'georgiai.ttf'))
NAR = colors.HexColor('#E54C09'); AMAR = colors.HexColor('#FBC900'); CREMA = colors.HexColor('#FFF8E7'); CAFE = colors.HexColor('#30271C'); GRIS = colors.HexColor('#6B6B6B'); LINEA = colors.HexColor('#E6DCCB')
st = {
 'h1': ParagraphStyle('h1', fontName='CalB', fontSize=20, textColor=NAR, leading=24, spaceAfter=4),
 'sub': ParagraphStyle('sub', fontName='Cal', fontSize=10, textColor=GRIS, leading=13, spaceAfter=10),
 'h2': ParagraphStyle('h2', fontName='CalB', fontSize=13, textColor=NAR, leading=16, spaceBefore=10, spaceAfter=5),
 'p': ParagraphStyle('p', fontName='Cal', fontSize=10.5, textColor=CAFE, leading=14, spaceAfter=5),
 'big': ParagraphStyle('big', fontName='CalB', fontSize=22, textColor=NAR, leading=26, alignment=1),
 'bigl': ParagraphStyle('bigl', fontName='Cal', fontSize=9.5, textColor=GRIS, leading=12, alignment=1),
 'q': ParagraphStyle('q', fontName='Geo', fontSize=11, textColor=CAFE, leading=15, leftIndent=8, spaceAfter=4),
 'tc': ParagraphStyle('tc', fontName='Cal', fontSize=9.5, textColor=CAFE, leading=12),
 'tcb': ParagraphStyle('tcb', fontName='CalB', fontSize=9.5, textColor=CAFE, leading=12),
 'th': ParagraphStyle('th', fontName='CalB', fontSize=9.5, textColor=colors.white, leading=12),
 'note': ParagraphStyle('note', fontName='Cal', fontSize=9, textColor=GRIS, leading=12, spaceAfter=6),
}
P = lambda t, s='p': Paragraph(t, st[s])

def tabla(rows, widths, bold_col=None, shade_rows=()):
    data = [[P(c, 'th') for c in rows[0]]] + [[P(c, 'tcb' if (bold_col is not None and j == bold_col) else 'tc') for j, c in enumerate(r)] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [('GRID', (0, 0), (-1, -1), 0.5, LINEA), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('BACKGROUND', (0, 0), (-1, 0), NAR)]
    for r in shade_rows: style.append(('BACKGROUND', (0, r), (-1, r), CREMA))
    t.setStyle(TableStyle(style)); return t

def tarjetas(items):
    data = [[Table([[P(v, 'big')], [P(l, 'bigl')]], colWidths=[4.0 * cm]) for v, l in items]]
    t = Table(data, colWidths=[4.2 * cm] * len(items))
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), CREMA), ('INNERGRID', (0, 0), (-1, -1), 6, colors.white), ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    return t

def pie(canvas, doc):
    canvas.saveState(); canvas.setFillColor(NAR); canvas.rect(0, letter[1] - 0.5 * cm, letter[0], 0.5 * cm, fill=1, stroke=0)
    canvas.setFillColor(AMAR); canvas.rect(0, letter[1] - 0.5 * cm, 4 * cm, 0.5 * cm, fill=1, stroke=0)
    canvas.setFont('Cal', 8.5); canvas.setFillColor(GRIS)
    canvas.drawString(2 * cm, 1.1 * cm, 'Heiiu English Academy · Propuesta de vinculación comercial B2B · uso interno de gerencia · 08/10/2026')
    canvas.drawRightString(letter[0] - 2 * cm, 1.1 * cm, f'{doc.page}'); canvas.restoreState()

CUPO = 4_782_800; COM_B2B = 0.10; COM_ALI = 0.06
out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PROPUESTA_HUNTER_B2B.pdf'
doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.6 * cm, bottomMargin=1.8 * cm, title='Propuesta Hunter B2B')
W = letter[0] - 4 * cm
E = []
E.append(P('Hunter B2B · perfil senior de convenios', 'h1'))
E.append(P('Abre y activa alianzas y planes empresa. No atiende citas de WhatsApp (eso lo hacen las asesoras). Modelo de ingreso por comisión con tres escalones, como en seguros.', 'sub'))

E.append(P('La idea en una frase', 'h2'))
E.append(P('Contrato laboral desde el día uno con el <b>mínimo legal: $2.000.000</b> (salario $1.750.905 + auxilio de transporte $249.095, decretos 1469 y 1470 de 2025). Comisiona desde la primera venta. Durante los tres primeros meses, <b>en cada mes que cumpla los mínimos</b> de actividad y resultado, le garantizamos un ingreso total de <b>$3.500.000</b>: si su básico más comisiones no llega, se le completa; si lo supera, recibe lo que produjo. <b>Si en un mes no cumple los mínimos, no hay $3.500.000</b>: recibe el mínimo legal más sus comisiones y entra en carta de ampliación. El básico sube en el mes 7 y en el año 2 por resultados.'))
E.append(Spacer(1, 4))
E.append(tarjetas([('10%', 'del recaudo corporativo<br/>(plan empresa)'), ('6%→3%', 'del recaudo de cada estudiante<br/>que llega por su alianza'), ('$3.5M', 'piso de arranque<br/>meses 1, 2 y 3'), ('$2.0M', 'mínimo legal siempre<br/>(salario + auxilio)')]))

E.append(P('Qué vende (las dos ofertas que ya existen)', 'h2'))
E.append(tabla([
 ['Oferta', 'Qué es', 'Qué le paga a ella'],
 ['A. Alianza sin costo (Heiiu Business Partner)', 'La empresa firma el convenio estándar: sus colaboradores entran con carta a la columna Transformación y la empresa entrega 3 Becas [Empresa] por trimestre. La empresa no paga nada.', '6% del recaudo de cada estudiante que se matricule por esa alianza: 6% en los 12 meses siguientes a la firma de su matrícula y 3% del mes 13 al 24 (su cartera). El cierre del estudiante lo hace la asesora; la cartera es de ella.'],
 ['B. Plan empresa', 'La empresa paga cupos de sus colaboradores a tarifa corporativa por volumen, escrita: de 3 a 7 cupos $4.782.800 cada uno; de 8 a 15, $4.350.000 (grupo cerrado en la sede desde 12); de 16 a 30, $3.950.000 (grupo cerrado en la sede o en la empresa). Ella cierra los tres tramos con la orden estándar y gerencia firma; más de 30 cupos lo cotiza gerencia con ella.', f'10% del recaudo corporativo del primer año en todos los tramos: ${CUPO*COM_B2B:,.0f} por cupo del tramo 1 de contado; un grupo cerrado de 16 cupos (${16*3_950_000:,.0f}) le deja ${16*3_950_000*COM_B2B:,.0f}.'],
 ['Activación', 'Una alianza firmada no vale hasta que produce: charla de 20 minutos en la empresa, diagnóstico de inglés al equipo, Experience Class. Es parte de su trabajo.', 'No paga por sí misma; es lo que convierte la firma en matrículas.'],
], [3.6 * cm, 6.6 * cm, W - 10.2 * cm], bold_col=0))

E.append(KeepTogether([P('Cuánto gana según lo que produzca (de contado)', 'h2'),
 tabla([
 ['Produce en el mes', 'Recaudo', 'Comisión', 'Comisión + básico ($2.0M)'],
 ['3 cupos de plan empresa', f'${3*CUPO:,.0f}', f'${3*CUPO*COM_B2B:,.0f}', f'${3*CUPO*COM_B2B + 2_000_000:,.0f} (meses 1-3: piso $3.500.000)'],
 ['5 cupos', f'${5*CUPO:,.0f}', f'${5*CUPO*COM_B2B:,.0f}', f'${5*CUPO*COM_B2B + 2_000_000:,.0f}'],
 ['10 cupos (meta meses 4-6)', f'${10*CUPO:,.0f}', f'${10*CUPO*COM_B2B:,.0f}', f'${10*CUPO*COM_B2B + 2_000_000:,.0f}'],
 ['15 cupos (meta desde el mes 7)', f'${15*CUPO:,.0f}', f'${15*CUPO*COM_B2B:,.0f}', f'${15*CUPO*COM_B2B + 2_549_095:,.0f} (básico ya en $2.3M + auxilio)'],
 ['Un grupo cerrado de 15 (tramo 2, $4.350.000 c/u)', f'${15*4_350_000:,.0f}', f'${15*4_350_000*COM_B2B:,.0f}', f'${15*4_350_000*COM_B2B + 2_000_000:,.0f} ese mes si es de contado'],
 ['+ 10 estudiantes por alianzas pagando cuotas de $450.000', '$4.500.000 al mes', '$270.000 al mes, se suma a lo anterior', 'cartera que crece cada mes'],
 ], [5.6 * cm, 3.6 * cm, 3.6 * cm, W - 12.8 * cm], bold_col=2, shade_rows=(3, 4)),
 P('Los cupos a cuotas pagan la comisión a medida que la empresa paga (40% inicial + 3 cuotas en los tramos 2 y 3). Un plan de 5 cupos (~$24 millones) le deja $2.4 millones; dos planes así al mes ya la ponen por encima de $6 millones con el básico.', 'note')]))

E.append(KeepTogether([P('La escalera: metas trimestrales crecientes, fijo e ingreso', 'h2'),
 P('Los mínimos de los meses 1-3 dan derecho al piso de $3.500.000; si no los cumple, recibe el mínimo legal más lo que haya comisionado. Todo se registra a diario en el tablero de alianzas (cinco minutos al cierre del día) y gerencia lo revisa todos los días. Seguimiento diario de 15 minutos a hora fija (ayer frente al plan y lo de hoy) y planeación semanal los lunes de 30 minutos. No se cancelan: si una se mueve, se repone ese mismo día.'),
 tabla([
 ['Etapa', 'Fijo', 'Mínimo para el piso', 'Meta', 'Gana si cumple la meta'],
 ['Mes 1', '$2.000.000 (mínimo legal)', '40 empresas contactadas con decisor (2 por día) · 12 reuniones · 3 activaciones · 2 firmas (convenio o plan)', '3 firmas', '$3.500.000 (piso)'],
 ['Mes 2', '$2.000.000', '40 empresas · 12 reuniones · 3 activaciones + 4 firmas acumuladas · 5 cupos corporativos', '6 cupos', '$3.500.000 (piso; 6 cupos = $2.9M de comisión)'],
 ['Mes 3', '$2.000.000', '40 empresas · 12 reuniones · 3 activaciones + 6 firmas acumuladas · 10 cupos acumulados (≈$48M de ventas en el T1)', '10 cupos', '$6.780.000 (básico + 10 cupos)'],
 ['T2 (meses 4-6)', 'Mínimo vigente + auxilio', 'Gestión base cada mes (40 empresas · 12 reuniones · 1 activación por alianza por trimestre); sin piso', '$48M de ventas al mes', '$6.800.000'],
 ['T3 (7-9) · T4 (10-12)', 'Mínimo + $550.000 + auxilio ($2.550.000 en 2026)', 'Gestión base cada mes', '$66M · $78M', '$9.150.000 · $10.350.000'],
 ['T5 a T8 (meses 13-24)', 'Mínimo + $850.000 + auxilio ($2.850.000 en 2026)', 'Gestión base cada mes', '$84M · $92M · $100M · $108M', '$11.250.000 a $13.650.000'],
 ['Desde T9 (mes 25)', 'Se revisa cada año', 'Gestión base cada mes', 'Trimestre anterior + 2,5% (~10% al año), salvo otrosí', '—'],
 ], [2.4 * cm, 3.6 * cm, 5.4 * cm, 3.0 * cm, W - 14.4 * cm], bold_col=4, shade_rows=(4, 5)),
 P('Meta en ventas firmadas (contratos con inicial pagada: plan empresa, cupos, personalizados; contado o cuotas), evaluada por TRIMESTRE y creciente por calendario pactado (nunca según lo vendido antes: castiga al que rinde, Misra & Nair 2011). Sube de básico si cumple la meta en 2 de los 3 últimos trimestres. ACELERADOR sin tope: 10% hasta la meta, 15% del 100 al 130%, 20% sobre 130%, solo en trimestres con al menos 2 empresas nuevas firmadas. CARTERA decreciente por estudiante: 6% los 12 meses siguientes a la firma de la matrícula, 3% del mes 13 al 24, 0% después; no cuenta para la meta. Contratos firmados que no se puedan iniciar por capacidad cuentan para la meta (se alquilan salones). Todo pactado en el anexo desde la firma: cambiarlo después exige otrosí (SL1183-2018). Comisiones y básico pagan prestaciones y seguridad social; el mínimo y el auxilio se ajustan cada enero por decreto.', 'note')]))

E.append(KeepTogether([P('Qué cuenta y qué no (definiciones del tablero)', 'h2'),
 P('Cada término se registra en el tracker el mismo día, con su prueba; lo que no está en el tracker no existe. Una alianza que no activa en 30 días deja de contar como firma para los mínimos.'),
 tabla([
 ['Término', 'Cuenta cuando…', 'NO cuenta', 'Prueba en el tracker'],
 ['Empresa contactada con decisor', 'Habló (llamada, reunión o chat con respuesta) con quien puede firmar o autorizar: gerente, dueño, talento humano o bienestar. Una vez por empresa.', 'Recepción, asistente, correo sin respuesta, "le paso el mensaje". Volver a hablar con la misma empresa.', 'Empresa, nombre y cargo del decisor, fecha, canal.'],
 ['Reunión', 'Presentación de la alianza o del plan empresa al decisor, agendada y realizada (presencial o videollamada), de 20 minutos o más.', 'Llamadas de prospección, visitas sin decisor, reuniones canceladas.', 'Fecha, asistentes, resultado (interesa / no / pide propuesta).'],
 ['Activación', 'Una alianza firmada hace algo que produce leads: charla en la empresa, mensaje en el canal interno con la postulación, feria o evento. Cada actividad es una activación.', 'Firmar el convenio (eso es firma). Una charla sin lista de asistentes.', 'Fecha, tipo, asistentes o postulaciones recibidas.'],
 ['Firma (convenio o plan)', 'Convenio Business Partner firmado por el representante legal, o plan empresa con la orden firmada y la inicial pagada.', 'Carta de intención, "nos interesa", orden sin pago.', 'Documento firmado + comprobante del pago inicial (plan).'],
 ['Cupo corporativo', 'Cada colaborador de un plan empresa con orden firmada e inicial pagada. 15 cupos en una orden = 15.', 'Becados de alianza (son estudiantes de la asesora; a ella le paga la cartera del 6%). Cupos de órdenes sin pago.', 'Orden + comprobante; la comisión se liquida sobre recaudo real.'],
 ], [3.2 * cm, 5.6 * cm, 4.4 * cm, W - 13.2 * cm])]))

E.append(KeepTogether([P('Qué pasa si no cumple', 'h2'),
 tabla([
 ['Situación', 'Consecuencia'],
 ['No llega al mínimo del mes (meses 1-3)', 'No hay piso: recibe $2.000.000 más sus comisiones, y entra en carta de ampliación (una semana con meta escrita).'],
 ['Falla dos mínimos seguidos', 'Salida dentro del período de prueba.'],
 ['Falla el mínimo del mes 2', 'El piso del mes 3 no existe.'],
 ['Segundo viernes del mes 1', 'Alerta temprana: 20 empresas contactadas, 6 reuniones y 1 firma; si no, carta esa misma semana.'],
 ['Alianza firmada sin activar en 30 días', 'No cuenta como firma.'],
 ], [5.2 * cm, W - 5.2 * cm], bold_col=0),
 P('<b>El piso nunca se paga por no producir.</b>')]))

E.append(KeepTogether([P('Lo que arriesga la academia', 'h2'),
 tarjetas([('~$2.7M', 'al mes si no produce nada<br/>(mínimo legal cargado)'), ('$3.5M', 'por mes de piso, solo si<br/>cumplió los mínimos'), ('$0', 'de comisión que no venga<br/>de recaudo ya cobrado')]),
 Spacer(1, 6),
 P('Por cupo, después de su comisión con prestaciones, el profe y los libros, la academia se queda con el 65-68% ($2.7M a $3.2M según el tramo). Su fijo cargado (~$2.7M) se paga con el margen de un solo cupo. A meta desde el mes 7 (15 cupos, $72 millones): ella gana $9.7 millones y la academia se queda con más de $57 millones.', 'note')]))

E.append(KeepTogether([P('Fronteras, por escrito el día uno', 'h2'),
 tabla([
 ['Con quién', 'Regla'],
 ['Docente con habilitación comercial', 'Si un docente trae una empresa por su cuenta, la registra en el tracker; quien registra primero es dueño. El canal empresas es de ella.'],
 ['Asesoras (inbound)', 'Todo lo que llega por WhatsApp, anuncios y reactivación es de ellas. Los estudiantes que lleguen por una alianza de ella los cierran las asesoras (comisión de cierre para ellas) y ella cobra la cartera del 6%.'],
 ['Gerencia', 'Firma todo convenio y toda orden. Ella cierra hasta 30 cupos con la tabla de volumen escrita, sin negociar precios ni condiciones; más de 30 cupos o cualquier condición fuera de la orden lo cotiza gerencia con ella. Nada se vende por debajo de $3.500.000 el cupo.'],
 ['Atribución de un estudiante a su alianza', 'Cuatro condiciones: (1) la empresa está registrada a su nombre en el tracker, con fecha de firma, antes de que el estudiante escriba; (2) el estudiante trae la carta de postulación de la empresa (sin carta no hay beca ni atribución); (3) si el estudiante ya estaba en LaHaus antes de la fecha del convenio, es inbound; (4) el agente pregunta "¿vienes por una empresa aliada?", la asesora lo confirma con la carta y lo anota en la planilla de matrícula. La atribución la decide un papel y una fecha, no una discusión.'],
 ], [3.6 * cm, W - 3.6 * cm], bold_col=0)]))

E.append(KeepTogether([P('Cómo decírselo (40 segundos)', 'h2'),
 P('"Tu trabajo es abrir empresas, no atender citas. Entras de planta desde el primer día, contrato laboral, con el mínimo legal, y los tres primeros meses te garantizo $3.500.000 si cumples unos mínimos de actividad y resultado. Comisionas el 10% de todo lo que una empresa pague por sus cupos, y el 6% de lo que pague cada estudiante que entre por una alianza tuya, mes a mes, durante todo su programa: esa es tu cartera. Tu meta es llegar a 10 cupos al mes en el cuarto mes y a 15 en el séptimo; con 15 cupos estás por encima de $9.5 millones, más la cartera de tus alianzas. Y el ritmo es de directora: dos empresas nuevas contactadas por día. Las dos ofertas, el convenio y la orden de plan empresa, ya están escritas; tú las llevas a la empresa y las cierras."', 'q'),
 P('Antes de firmar: entrevista con simulación de visita a una empresa (ella presenta las dos ofertas y cierra el convenio) · anexo del contrato con esta curva y la tabla de volumen · carga prestacional confirmada con contaduría · fronteras firmadas con las asesoras · lista de empresas ya en conversación (excluidas).', 'note')]))

doc.build(E, onFirstPage=pie, onLaterPages=pie); print('OK', out)
