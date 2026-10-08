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
E.append(P('Contrato laboral desde el día uno con el <b>básico mínimo legal</b>. Los tres primeros meses, si cumple los mínimos de actividad y resultado, recibe un <b>piso de $3.500.000</b>; si sus comisiones lo superan, recibe las comisiones. Desde el mes 4, básico más comisión, y el básico sube en el mes 7 y en el año 2 por resultados.'))
E.append(Spacer(1, 4))
E.append(tarjetas([('10%', 'del recaudo corporativo<br/>(plan empresa)'), ('6%', 'del recaudo de cada estudiante<br/>que llega por su alianza'), ('$3.5M', 'piso de arranque<br/>meses 1, 2 y 3'), ('Mínimo', 'legal si no llega<br/>al mínimo del mes')]))

E.append(P('Qué vende (las dos ofertas que ya existen)', 'h2'))
E.append(tabla([
 ['Oferta', 'Qué es', 'Qué le paga a ella'],
 ['A. Alianza sin costo (Heiiu Business Partner)', 'La empresa firma el convenio estándar: sus colaboradores entran con carta a la columna Transformación y la empresa entrega 3 Becas [Empresa] por trimestre. La empresa no paga nada.', '6% del recaudo de cada estudiante que se matricule por esa alianza, mes a mes mientras paga (su cartera). El cierre del estudiante lo hace la asesora; la cartera es de ella.'],
 ['B. Plan empresa', f'La empresa paga cupos de sus colaboradores a tarifa corporativa (${CUPO:,.0f} por cupo del programa completo). De 3 a 7 cupos lo cierra ella con la orden estándar; 8 o más, lo cierra gerencia.', f'10% del recaudo corporativo del primer año: ${CUPO*COM_B2B:,.0f} por cupo pagado de contado (si lo cierra gerencia por ser a la medida, 5%).'],
 ['Activación', 'Una alianza firmada no vale hasta que produce: charla de 20 minutos en la empresa, diagnóstico de inglés al equipo, Experience Class. Es parte de su trabajo.', 'No paga por sí misma; es lo que convierte la firma en matrículas.'],
], [3.6 * cm, 6.6 * cm, W - 10.2 * cm], bold_col=0))

E.append(KeepTogether([P('Cuánto gana según lo que produzca (de contado)', 'h2'),
 tabla([
 ['Produce en el mes', 'Recaudo', 'Comisión', 'Con básico (desde el mes 4)'],
 ['3 cupos de plan empresa', f'${3*CUPO:,.0f}', f'${3*CUPO*COM_B2B:,.0f}', f'${3*CUPO*COM_B2B + 1_750_000:,.0f}'],
 ['5 cupos', f'${5*CUPO:,.0f}', f'${5*CUPO*COM_B2B:,.0f}', f'${5*CUPO*COM_B2B + 1_750_000:,.0f}'],
 ['10 cupos (meta meses 4-6)', f'${10*CUPO:,.0f}', f'${10*CUPO*COM_B2B:,.0f}', f'${10*CUPO*COM_B2B + 1_750_000:,.0f}'],
 ['15 cupos (meta desde el mes 7)', f'${15*CUPO:,.0f}', f'${15*CUPO*COM_B2B:,.0f}', f'${15*CUPO*COM_B2B + 2_000_000:,.0f}'],
 ['+ 10 estudiantes por alianzas pagando cuotas de $450.000', '$4.500.000 al mes', '$270.000 al mes, se suma a lo anterior', 'cartera que crece cada mes'],
 ], [5.6 * cm, 3.6 * cm, 3.6 * cm, W - 12.8 * cm], bold_col=2, shade_rows=(3, 4)),
 P('Los cupos a cuotas pagan la comisión a medida que la empresa paga. Un plan de 5 cupos (~$24 millones) le deja $2.4 millones; dos planes así al mes ya la ponen por encima de $6 millones.', 'note')]))

E.append(KeepTogether([P('La escalera: mínimos, metas, fijo e ingreso suben con la antigüedad', 'h2'),
 P('Los mínimos de los meses 1-3 dan derecho al piso de $3.500.000; si no los cumple, recibe el mínimo legal más lo que haya comisionado. Todo se registra en el tracker B2B y se mide los viernes.'),
 tabla([
 ['Etapa', 'Fijo', 'Mínimo para el piso', 'Meta', 'Gana si cumple la meta'],
 ['Mes 1', 'Mínimo legal (dentro del piso)', '40 empresas contactadas con decisor (2 por día) · 12 reuniones · 3 activaciones · 2 firmas (convenio o plan)', '3 firmas', '$3.500.000 (piso)'],
 ['Mes 2', 'Mínimo legal (dentro del piso)', '4 firmas acumuladas · 5 cupos corporativos · 3 activaciones', '6 cupos', '$3.500.000 (piso; 6 cupos = $2.9M de comisión)'],
 ['Mes 3', 'Mínimo legal (dentro del piso)', '6 firmas acumuladas · 10 cupos acumulados', '10 cupos', '$4.780.000 (10 cupos superan el piso)'],
 ['Meses 4 a 6', 'Mínimo legal (~$1.750.000)', '—', '10 cupos o $48M de recaudo corporativo', '$6.530.000'],
 ['Meses 7 a 12', 'Básico $2.000.000', '—', '15 cupos o $72M', '$9.170.000'],
 ['Año 2', 'Básico $2.300.000', '—', '15 a 20 cupos', '$9.500.000 a $11.900.000'],
 ], [2.4 * cm, 3.6 * cm, 5.4 * cm, 3.0 * cm, W - 14.4 * cm], bold_col=4, shade_rows=(4, 5)),
 P('Básico mínimo legal: verificar el valor vigente antes de firmar. La cartera del 6% de las alianzas se suma a todo lo anterior.', 'note')]))

E.append(KeepTogether([P('Qué pasa si no cumple', 'h2'),
 tabla([
 ['Situación', 'Consecuencia'],
 ['No llega al mínimo del mes (meses 1-3)', 'No hay piso: recibe el mínimo legal más sus comisiones, y entra en carta de ampliación (una semana con meta escrita).'],
 ['Falla dos mínimos seguidos', 'Salida dentro del período de prueba.'],
 ['Falla el mínimo del mes 2', 'El piso del mes 3 no existe.'],
 ['Segundo viernes del mes 1', 'Alerta temprana: 20 empresas contactadas, 6 reuniones y 1 firma; si no, carta esa misma semana.'],
 ['Alianza firmada sin activar en 30 días', 'No cuenta como firma.'],
 ], [5.2 * cm, W - 5.2 * cm], bold_col=0),
 P('<b>El piso nunca se paga por no producir.</b>')]))

E.append(KeepTogether([P('Lo que arriesga la academia', 'h2'),
 tarjetas([('~$2.3M', 'al mes si no produce nada<br/>(mínimo legal cargado)'), ('$3.5M', 'por mes de piso, solo si<br/>cumplió los mínimos'), ('$0', 'de comisión que no venga<br/>de recaudo ya cobrado')]),
 Spacer(1, 6),
 P('A meta desde el mes 7 (15 cupos, $72 millones de recaudo corporativo): ella gana $9.2 millones y la academia se queda con más de $62 millones. La comisión alta no es generosidad: es el único costo que crece solo cuando la caja crece.', 'note')]))

E.append(KeepTogether([P('Fronteras, por escrito el día uno', 'h2'),
 tabla([
 ['Con quién', 'Regla'],
 ['Docente del piloto B2B', 'Él conserva las empresas registradas en su tracker; ella, las nuevas. Quien registra primero en el tracker es dueño de la empresa. Mismo tablero, dos filas.'],
 ['Asesoras (inbound)', 'Todo lo que llega por WhatsApp, anuncios y reactivación es de ellas. Los estudiantes que lleguen por una alianza de ella los cierran las asesoras (comisión de cierre para ellas) y ella cobra la cartera del 6%.'],
 ['Gerencia', 'Firma todo convenio y toda orden; cierra los planes de 8 cupos o más y cualquier condición fuera del formato. Ella no negocia precios ni condiciones.'],
 ], [3.6 * cm, W - 3.6 * cm], bold_col=0)]))

E.append(KeepTogether([P('Cómo decírselo (40 segundos)', 'h2'),
 P('"Tu trabajo es abrir empresas, no atender citas. Entras de planta desde el primer día con el mínimo legal, y los tres primeros meses te garantizo $3.500.000 si cumples unos mínimos de actividad y resultado. Comisionas el 10% de todo lo que una empresa pague por sus cupos, y el 6% de lo que pague cada estudiante que entre por una alianza tuya, mes a mes, durante todo su programa: esa es tu cartera. Tu meta es llegar a 10 cupos al mes en el cuarto mes y a 15 en el séptimo; con 15 cupos estás por encima de $9 millones, más la cartera de tus alianzas. Y el ritmo es de directora: dos empresas nuevas contactadas por día. Las dos ofertas, el convenio y la orden de plan empresa, ya están escritas; tú las llevas a la empresa y las cierras."', 'q'),
 P('Antes de firmar: entrevista con simulación de visita a una empresa (ella presenta las dos ofertas y cierra el convenio) · anexo del contrato con esta curva · básico mínimo legal vigente confirmado · fronteras firmadas con el docente del piloto y las asesoras · lista de empresas ya en conversación (excluidas).', 'note')]))

doc.build(E, onFirstPage=pie, onLaterPages=pie); print('OK', out)
