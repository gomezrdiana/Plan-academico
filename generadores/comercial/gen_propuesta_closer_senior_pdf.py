# -*- coding: utf-8 -*-
"""Propuesta closer senior (modelo absorbible) en PDF presentable, colores de marca.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/PROPUESTA_CLOSER_SENIOR.pdf"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
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

def tabla(rows, widths, header=True, bold_col=None, shade_rows=()):
    data = []
    for i, r in enumerate(rows):
        if i == 0 and header: data.append([P(c, 'th') for c in r])
        else: data.append([P(c, 'tcb' if (bold_col is not None and j == bold_col) else 'tc') for j, c in enumerate(r)])
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [('GRID', (0, 0), (-1, -1), 0.5, LINEA), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    if header: style.append(('BACKGROUND', (0, 0), (-1, 0), NAR))
    for r in shade_rows: style.append(('BACKGROUND', (0, r), (-1, r), CREMA))
    t.setStyle(TableStyle(style)); return t

def tarjetas(items):
    cells = [[P(v, 'big'), P(l, 'bigl')] for v, l in items]
    data = [[Table([[c[0]], [c[1]]], colWidths=[4.0 * cm]) for c in cells]]
    t = Table(data, colWidths=[4.2 * cm] * len(items))
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), CREMA), ('BOX', (0, 0), (-1, -1), 0, CREMA), ('INNERGRID', (0, 0), (-1, -1), 6, colors.white), ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    return t

def pie(canvas, doc):
    canvas.saveState(); canvas.setFillColor(NAR); canvas.rect(0, letter[1] - 0.5 * cm, letter[0], 0.5 * cm, fill=1, stroke=0)
    canvas.setFillColor(AMAR); canvas.rect(0, letter[1] - 0.5 * cm, 4 * cm, 0.5 * cm, fill=1, stroke=0)
    canvas.setFont('Cal', 8.5); canvas.setFillColor(GRIS)
    canvas.drawString(2 * cm, 1.1 * cm, 'Heiiu English Academy · Propuesta de vinculación comercial · uso interno de gerencia · 08/10/2026')
    canvas.drawRightString(letter[0] - 2 * cm, 1.1 * cm, f'{doc.page}'); canvas.restoreState()

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\PROPUESTA_CLOSER_SENIOR.pdf'
doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.6 * cm, bottomMargin=1.8 * cm, title='Propuesta closer senior')
W = letter[0] - 4 * cm
E = []
E.append(P('Closer de planta · perfil senior', 'h1'))
E.append(P('Modelo de ingreso por comisión con piso de arranque. Qué gana, con qué condiciones y qué arriesga la academia.', 'sub'))

E.append(P('La idea en una frase', 'h2'))
E.append(P('Gana el <b>12% de todo lo que entre a la caja</b> por sus clientes, desde su primera venta. Los tres primeros meses son un piloto por prestación de servicios con un <b>piso de $3.500.000</b> si cumple los mínimos; desde el mes 4, si pasó las mediciones, <b>pasa a contrato laboral</b> con básico mínimo legal más comisión, y el básico sube dos veces por resultados. La meta y el ingreso suben con la antigüedad, como en seguros.'))
E.append(Spacer(1, 4))
E.append(tarjetas([('12%', 'de lo que entre<br/>hasta su meta'), ('15%', 'de lo que entre<br/>por encima de la meta'), ('$3.5M', 'piso de arranque<br/>meses 1, 2 y 3'), ('Mes 4', 'pasa a laboral:<br/>básico + comisión')]))

E.append(P('Cómo se arma su ingreso', 'h2'))
E.append(tabla([
 ['Pieza', 'Cuándo', 'Cómo funciona'],
 ['Comisión', 'Siempre, desde la primera venta', '12% de lo que entre en el mes por sus clientes. Lo que exceda su meta del mes paga el 15%. Una matrícula de $2.990.000 de contado le deja $358.800; por encima de la meta, $448.500.'],
 ['Piso de arranque', 'Solo meses 1, 2 y 3 (piloto por prestación de servicios)', '$3.500.000 si cumple el mínimo de contratos del mes y atiende 5 citas por semana. Si sus comisiones superan el piso, se le pagan las comisiones y el piso desaparece.'],
 ['Básico (laboral)', 'Desde el mes 4, si pasó las mediciones', 'Contrato laboral con básico mínimo legal (verificar vigente, ~$1.750.000) más la comisión. El básico sube a $2.000.000 en el mes 7 y a $2.300.000 en el año 2, siempre por resultados.'],
 ['Cartera', 'Desde el mes 2 en adelante', 'Los clientes pagan en cuotas: cada contrato le sigue pagando el 12% de cada cuota en los meses siguientes. Su comisión crece con el tiempo aunque un mes venda menos.'],
], [3.0 * cm, 4.0 * cm, W - 7.0 * cm], bold_col=0))
E.append(P('Tres pisos, como en seguros: si vende cero, el básico (desde el mes 4); si cumple mínimos, el piso; si supera, las comisiones. Forma: prestación de servicios los tres primeros meses y laboral desde el cuarto (revisar con el abogado).', 'note'))

E.append(P('Cuánto gana según lo que entre (esto es lo que ella mira)', 'h2'))
E.append(tabla([
 ['Entra a la academia en el mes', 'Ella gana', 'Nota'],
 ['$15.000.000', '$1.800.000', 'En meses 1-3, el piso la sube a $3.500.000 si cumplió el mínimo'],
 ['$20.000.000', '$2.400.000', 'Ídem'],
 ['$30.000.000', '$3.600.000', ''],
 ['$36.000.000', '$4.300.000', 'Equivale a 12 contratos de contado'],
 ['$42.000.000', '$5.000.000', 'Para ganar $5 millones: que entren $42 millones'],
 ['$50.000.000', '$6.000.000', ''],
 ['$58.000.000', '$7.000.000', 'Equivale a 18 contratos de contado'],
], [5.5 * cm, 3.5 * cm, W - 9.0 * cm], bold_col=1, shade_rows=(5,)))

E.append(KeepTogether([P('Por qué el mismo número de contratos puede dar ingresos distintos', 'h2'),
 tabla([
 ['18 contratos en un mes', 'Entra ese mes', 'Gana ese mes', 'Y después'],
 ['Todos de contado ($2.990.000 c/u)', '$53.800.000', '$7.000.000', 'Nada más'],
 ['Todos a cuotas (inicial $1.200.000)', '$21.600.000', '$2.600.000', '$970.000 al mes durante 4 meses mientras pagan'],
 ], [5.6 * cm, 3.2 * cm, 3.0 * cm, W - 11.8 * cm], bold_col=2),
 P('Al final cobra lo mismo por esos 18 contratos; a cuotas lo recibe repartido. Por eso existe el piso en los meses 1-3, y desde el mes 4 la cartera la sostiene.', 'note')]))

E.append(KeepTogether([P('La escalera: metas, fijo e ingreso suben con la antigüedad', 'h2'), P('Las metas se cuentan en <b>contratos firmados con la inicial pagada</b>. Además, todas las semanas: 5 citas atendidas. Se mide cada viernes en el tablero que ella misma llena.'),
 tabla([
 ['Etapa', 'Contrato y fijo', 'Mínimo / Meta (contratos)', 'Gana si cumple la meta (de contado)'],
 ['Mes 1', 'Prestación · piso $3.5M', 'mínimo 3 / meta 6', '$3.500.000 (piso)'],
 ['Mes 2', 'Prestación · piso $3.5M', 'mínimo 4 / meta 8', '$3.500.000 (piso; con 10 contratos, $3.770.000)'],
 ['Mes 3', 'Prestación · piso $3.5M', 'mínimo 6 / meta 8', '$3.500.000 (piso; con 10 contratos, $3.770.000)'],
 ['Meses 4 a 6', 'Laboral · básico mínimo legal (~$1.750.000)', 'meta 10', '$5.340.000'],
 ['Meses 7 a 12', 'Laboral · básico $2.000.000', 'meta 12', '$6.310.000'],
 ['Año 2', 'Laboral · básico $2.300.000', 'meta 12 a 14', '$6.600.000 a $7.500.000'],
 ], [2.6 * cm, 5.6 * cm, 3.8 * cm, W - 12.0 * cm], bold_col=3, shade_rows=(4, 5)),
 P('Por encima de la meta todo paga 15%: con 15 contratos en el mes 7, $7.650.000; con 18, $9.000.000. Básico mínimo legal: verificar el valor vigente antes de firmar.', 'note')]))

E.append(KeepTogether([P('Qué pasa si no cumple', 'h2'), tabla([
 ['Situación', 'Consecuencia'],
 ['No llega al mínimo del mes', 'No hay piso. Recibe solo su comisión (lo que recaudó × 12%) y entra en carta de ampliación: una semana más con meta escrita.'],
 ['Falla dos mínimos seguidos', 'Salida. El mes 3 no existe.'],
 ['Falla el mínimo del mes 2', 'El piso del mes 3 no existe: ese mes es comisión pura.'],
 ['Segundo viernes del mes 1', 'Alerta temprana: debe llevar al menos 1 contrato y 10 citas atendidas; si no, carta esa misma semana.'],
], [4.6 * cm, W - 4.6 * cm], bold_col=0), P('<b>El piso nunca se paga por no vender.</b> Para cobrar los tres pisos completos tiene que haber cerrado 13 contratos en 90 días.')]))

E.append(KeepTogether([P('Lo que arriesga la academia', 'h2'), tarjetas([('$3.5M', 'peor caso real: un mes de piso<br/>con el mínimo justo'), ('$10.5M', 'máximo absoluto: tres pisos,<br/>y solo si cerró 13 contratos'), ('~$2.3M', 'fijo desde el mes 4 (básico<br/>cargado), solo si ya demostró')]), Spacer(1, 6), tabla([
 ['Contratos al mes (de contado), desde el mes 7', 'Entra', 'Ella gana (básico $2.0M + comisión)', 'Queda para la academia'],
 ['8', '$23.900.000', '$4.870.000', '$19.000.000'],
 ['12 (la academia sana)', '$35.900.000', '$6.310.000', '$29.600.000'],
 ['15', '$44.900.000', '$7.650.000', '$37.300.000'],
 ['18', '$53.800.000', '$9.000.000', '$44.800.000'],
], [5.2 * cm, 3.4 * cm, 3.2 * cm, W - 11.8 * cm], bold_col=3, shade_rows=(2,)), P('El mes en que le pagas $9.000.000 es el mes en que la academia se quedó con $44.800.000. La comisión alta no es generosidad: es el único costo que crece solo cuando la caja crece.', 'note')]))

E.append(KeepTogether([P('Cómo cuenta cada tipo de venta', 'h2'), tabla([
 ['Venta', 'Cuenta para la meta', 'Comisión'],
 ['Programa completo o Arranque de contado', '1 contrato', '12% (15% sobre la meta), de una vez'],
 ['Programa a cuotas', '1 contrato cuando la inicial está pagada (mín. $1.000.000 o 30%)', '12% de la inicial y de cada cuota cuando entra'],
 ['Separación de $300.000 sola', '0 (lead en proceso)', '12% de los $300.000; el resto cuando pague la inicial'],
 ['Nivel suelto / sabatino', '½ contrato', '12%'],
 ['Cliente antiguo (continuidad, supletorio)', '½ contrato', '6%'],
 ['Plan empresa que ella abra', '1 contrato por cupo', '3% del recaudo corporativo del primer año'],
], [5.4 * cm, 5.2 * cm, W - 10.6 * cm]), P('La meta solo se llena con programas con inicial pagada; separaciones y niveles sueltos no.', 'note')]))

E.append(KeepTogether([P('Cómo decírselo (40 segundos)', 'h2'),
 P('"Comisionas desde el primer cierre: el 12% de todo lo que entre de tus clientes, y el 15% de lo que cierres por encima de tu meta. Los tres primeros meses te garantizo $3.500.000 mientras arrancas, con mínimos de 3, 4 y 6 contratos y 5 citas atendidas por semana. Si pasas esas tres mediciones, en el cuarto mes entras de planta con contrato laboral: básico más comisión, y el básico sube en el mes 7 y en el año 2 por resultados. Tu objetivo son 8 contratos al mes; desde el cuarto mes, 10; desde el séptimo, 12. Con 12 contratos estás por encima de $6 millones; con 15, en $7.6. Las citas te llegan agendadas; tu trabajo es cerrarlas."', 'q'),
 P('Antes de firmar: entrevista con prueba práctica de cierre · anexo del contrato con esta curva · forma del contrato revisada por el abogado · frontera por escrito con la asesora actual (la comisión es de quien atiende la cita y cierra).', 'note')]))

doc.build(E, onFirstPage=pie, onLaterPages=pie); print('OK', out)
