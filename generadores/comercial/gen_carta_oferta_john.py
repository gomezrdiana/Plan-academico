# -*- coding: utf-8 -*-
"""Carta de oferta laboral para el candidato 1 de alianzas (John). Referencia de Welli verificada el 17-18/10.
Versión 18/10 tarde con las correcciones de gerencia: cargo Gerente de Alianzas, inicio martes 20/10, acelerador explicado,
cartera se queda en la empresa, mínimo $30M antes del cierre de la prueba, reuniones diarias (2 presenciales), sin personal
a cargo pero responsable de la gestión, regla de atribución frente a otros comerciales, base de la academia para trabajarla,
y nota de realidad de la empresa. 1 página.
Salida (fuera de git): Candidatos/John Hinestroza/CARTA_OFERTA_JOHN_2026-10.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza'
d = Document()
for s in d.sections:
    s.top_margin = Cm(0.8); s.bottom_margin = Cm(0.6); s.left_margin = Cm(1.5); s.right_margin = Cm(1.5)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(8)
def t(txt, size=8, bold=False, color=None, after=1, align=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align: p.alignment = align
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def sec(txt):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = NAR
def bullets(items, size=8):
    for x in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); r = p.add_run(x); r.font.size = Pt(size)

t('Heiiu English Academy · Global Teacher S.A.S.', size=8.5, color=GRIS, after=0)
t('Bucaramanga, 18 de octubre de 2026', after=4)
t('OFERTA LABORAL — GERENTE DE ALIANZAS EMPRESARIALES', bold=True, size=12, color=NAR, after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
t('Para: John Hinestroza', after=3)
t('Después de las conversaciones sostenidas y de la verificación de referencias, Heiiu English Academy presenta por escrito la oferta para el cargo. Estos son los términos; el contrato y su anexo de compensación recogen exactamente lo mismo. La oferta está sujeta a los exámenes médicos de ingreso.', after=3)

sec('1. Cargo, contrato y fecha de inicio')
bullets([
 'Cargo: Gerente de Alianzas Empresariales. Reporta a gerencia general.',
 'Contrato de trabajo a término indefinido, con periodo de prueba de dos (2) meses.',
 'Inicio: martes 20 de octubre de 2026, con la firma del contrato ese mismo día en la sede. Inducción el martes 20 (jornada completa) y el miércoles 21 en la mañana; trabajo de campo desde el miércoles en la tarde.'])

sec('2. Compensación (detalle en el anexo de compensación)')
bullets([
 'Básico: salario mínimo legal más auxilio de transporte ($2.000.000 en 2026), más prestaciones sociales y seguridad social de ley.',
 'Comisión del 10% sobre el recaudo del primer año de los contratos de plan empresa y programas personalizados cerrados por el Gerente de Alianzas; se liquida mes vencido sobre lo efectivamente recaudado, sin tope.',
 'Acelerador: aplica solo sobre lo que venda por encima de la meta del trimestre ($90.000.000 en el primero). Ese excedente comisiona al 15% hasta el 130% de la meta y al 20% de ahí en adelante, siempre que en ese trimestre haya firmado al menos dos empresas nuevas con pago recibido.',
 'Cartera de alianzas: 6% de los pagos de cada estudiante que se matricule con carta de una empresa aliada registrada a su nombre, durante los 12 meses siguientes a su matrícula, y 3% del mes 13 al 24. Si el contrato termina, se pagan las comisiones causadas sobre lo recaudado hasta la fecha de retiro; la cartera y las alianzas quedan en la empresa.',
 'Ingreso mínimo garantizado de $3.500.000 en cada uno de los meses 1 a 3 en que cumpla los indicadores de gestión y de firmas (mes 1: 40 empresas contactadas con quien decide, 12 reuniones y 2 firmas; mes 2: 4 firmas acumuladas y 2 activaciones; mes 3: 6 firmas acumuladas y 3 activaciones). La meta de ventas de $30.000.000 mensuales no es condición de esta garantía. Si en un mes no se cumplen los indicadores, se paga el básico más las comisiones causadas.',
 'Metas trimestrales crecientes y escalones de básico según la tabla del anexo, que cubre los primeros 24 meses y se conoce desde la firma. El esquema de comisiones y metas se revisa cada año según rendimiento, de común acuerdo y por escrito.'])

sec('3. Periodo de prueba y revisión de resultados')
t('El periodo de prueba se evalúa con ventas, no solo con gestión, en dos cortes. Día 30, miércoles 18 de noviembre de 2026: debe haber al menos una venta con pago recibido o una alianza activada. Día 45, jueves 3 de diciembre de 2026: debe haber como mínimo $30.000.000 en ventas con pago recibido, por cualquier canal (plan empresa, alianzas, programas personalizados o base de la academia). La continuidad del cargo después de cada corte depende de ese resultado. La garantía de ingreso de los meses 1 a 3 no modifica esta condición.', after=1)

sec('4. Forma de trabajo')
bullets([
 'Reunión diaria de seguimiento con gerencia de 15 a 30 minutos, de lunes a viernes a las 8:45 a. m., presentada por el Gerente de Alianzas: resultados del día anterior frente al plan y empresas del día. Es virtual, salvo dos días a la semana que son presenciales en la sede, con gerencia o con quien gerencia designe (socio financiero o asesor externo). Planeación semanal los lunes, 30 minutos, presencial. Tablero de alianzas al día, el mismo día. Fuera de eso, autonomía para organizar la agenda y las visitas.',
 'Sin personal a cargo. El equipo de asesoría comercial apoya las activaciones y matricula a los interesados que el Gerente de Alianzas genere, pero no le reporta: el Gerente de Alianzas es responsable de que esa gestión ocurra, le hace seguimiento y escala a gerencia lo que no avance.',
 'Territorio inicial: salud (clínicas, odontología, IPS), fundaciones, cajas de compensación y organizaciones grandes. Puede haber otros comerciales B2B en otros sectores. Regla única de atribución: una empresa es de quien la registra primero en el tablero, con 60 días para la primera reunión con el decisor; vencido ese plazo sin reunión, se libera. Los conflictos los resuelve gerencia por escrito.',
 'Cuando gerencia asigne contactos de la base de la academia, son para trabajarlos como a cualquier cliente, con la comisión de cierre vigente de las asesoras; esas ventas cuentan al 50% para la meta del cargo.',
 'Cierra con las tarifas y los documentos estándar de la academia; no está facultado para otorgar descuentos. Convenios y órdenes los firma el representante legal.'])

sec('5. La realidad de la empresa')
t('El cargo se acepta conociendo la realidad de la academia: una empresa pequeña, en crecimiento, donde los resultados se necesitan rápido y no hay tiempos de empresa grande. Por eso la inducción es de un día y medio y no de una semana: el producto se aprende con el kit de trabajo, en las primeras reuniones y en el seguimiento diario. Entender el producto y salir a la calle lo antes posible es parte del cargo desde el primer día.', after=1)

sec('6. Aceptación y firma')
bullets([
 'La oferta se acepta respondiendo por escrito a más tardar el lunes 19 de octubre de 2026 a las 12:00 del día.',
 'Exámenes médicos de ingreso el lunes 19, por cuenta de la empresa (la orden se envía con la aceptación). Firma del contrato y del anexo de compensación el martes 20 a las 8:00 a. m. en la sede. Documentos para la firma: cédula, RUT, certificación bancaria, certificados de afiliación a EPS y fondo de pensiones, hoja de vida y certificados laborales.',
 'Esta oferta reemplaza cualquier conversación anterior sobre los términos del cargo y pierde vigencia si no se acepta en el plazo indicado.'])
t('', after=3)
t('_________________________________', after=0)
t('Diana Marcela Gómez Rangel', bold=True, after=0)
t('Gerente · Heiiu English Academy · Global Teacher S.A.S.', size=8, color=GRIS, after=4)
t('Acepto los términos de esta oferta:  _________________________________   Fecha: ____ / ____ / 2026', size=8.5)

out = BASE + r'\CARTA_OFERTA_JOHN_2026-10.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
