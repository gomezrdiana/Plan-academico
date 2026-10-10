# -*- coding: utf-8 -*-
"""Borrador para el abogado: ANEXO DE COMPENSACIÓN Y METAS al contrato laboral del Ejecutivo(a) de Alianzas Empresariales.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/ANEXO_COMPENSACION_EJECUTIVO_ALIANZAS_BORRADOR.docx"""
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(64); s.top_margin = s.bottom_margin = Pt(54)

def p(t, b=False, size=10.5, color=None, align=None, after=5, italic=False):
    x = d.add_paragraph(); x.paragraph_format.space_after = Pt(after)
    if align: x.alignment = align
    r = x.add_run(t); r.bold = b; r.italic = italic; r.font.size = Pt(size)
    if color: r.font.color.rgb = color
    return x
def cl(n, titulo, texto):
    x = d.add_paragraph(); x.paragraph_format.space_after = Pt(6); x.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = x.add_run(f'CLÁUSULA {n}. {titulo}. '); r.bold = True
    x.add_run(texto)
def tabla(rows):
    t = d.add_table(rows=1, cols=len(rows[0])); t.style = 'Table Grid'
    for j, h in enumerate(rows[0]):
        r = t.rows[0].cells[j].paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9)
    for f in rows[1:]:
        c = t.add_row().cells
        for j, v in enumerate(f):
            r = c[j].paragraphs[0].add_run(v); r.font.size = Pt(9)
    d.add_paragraph().paragraph_format.space_after = Pt(2)

# ---------- Nota para el abogado ----------
p('NOTA PARA EL ABOGADO (retirar antes de firmar)', True, 12, NAR)
p('Borrador del anexo de compensación y metas para el cargo de Ejecutivo(a) de Alianzas Empresariales, que se firmaría junto con el contrato laboral (término a definir). Agradecemos revisar en especial:', after=3)
for t in ['1. Naturaleza salarial: básico, comisiones, acelerador y garantía de ingreso mínimo se tratan como salario (art. 127 CST). Confirmar la redacción y la base de liquidación de prestaciones y seguridad social.',
          '2. Metas crecientes pactadas desde la firma (cláusulas 5 y 6): validar que la tabla trimestral y el aumento automático desde el mes 25 queden bien pactados y no se interpreten como modificación unilateral (SL1183-2018).',
          '3. Comisión de cartera decreciente (6% en los 12 meses siguientes a la firma de la matrícula del estudiante, 3% del mes 13 al 24, 0% después): validar redacción.',
          '4. Terminación (cláusula 10): decisión de gerencia: a la terminación solo se pagan comisiones sobre lo recaudado hasta esa fecha; nada sobre recaudos posteriores ni cartera. Validar que la redacción sea suficiente y no se entienda como renuncia a derechos causados.',
          '5. Incumplimiento de indicadores (cláusula 9): si se quiere que el incumplimiento reiterado pueda ser justa causa (SL520-2025), indicar si debe incluirse también en el Reglamento Interno de Trabajo.',
          '6. Período de prueba y tipo de contrato: indicar lo recomendable para este cargo.',
          '7. Confidencialidad y no captación de empresas aliadas y estudiantes tras la terminación: indicar alcance válido.']:
    p(t, after=2)
p('', after=6)

# ---------- Anexo ----------
p('ANEXO No. 1 AL CONTRATO DE TRABAJO', True, 13, NAR, WD_ALIGN_PARAGRAPH.CENTER, after=2)
p('ESQUEMA DE COMPENSACIÓN, METAS E INDICADORES — EJECUTIVO(A) DE ALIANZAS EMPRESARIALES', True, 11, None, WD_ALIGN_PARAGRAPH.CENTER, after=8)
p('Entre GLOBAL TEACHER S.A.S. (Heiiu English Academy), NIT __________, representada legalmente por __________________, en adelante EL EMPLEADOR, y __________________, identificado(a) con C.C. __________, en adelante EL TRABAJADOR, se acuerda el presente anexo, que hace parte integral del contrato de trabajo suscrito el ____ / ____ / ______.', after=8)

cl(1, 'OBJETO DEL CARGO', 'EL TRABAJADOR desarrollará el canal corporativo e institucional de la academia: prospección y relacionamiento con empresas, áreas de bienestar y fundaciones; presentación de la propuesta de valor; negociación y cierre de convenios de alianza (Heiiu Business Partner) y de órdenes de plan empresa; cierre de programas personalizados para ejecutivos; activación de las alianzas firmadas; y propuesta de nuevas oportunidades de programas y mercados. La atención de prospectos individuales que llegan por publicidad y canales digitales corresponde al equipo de asesoría comercial.')
cl(2, 'SALARIO BÁSICO', 'EL TRABAJADOR devengará un salario básico mensual equivalente al salario mínimo legal mensual vigente, más el auxilio de transporte legal cuando haya lugar ($1.750.905 + $249.095 en 2026, Decretos 1469 y 1470 de 2025). El básico se ajusta cada año según el decreto del Gobierno Nacional. El básico aumentará por escalones de resultado según la cláusula 7.')
cl(3, 'COMISIONES', 'Sobre los valores efectivamente recaudados por EL EMPLEADOR, EL TRABAJADOR devengará: (a) plan empresa y programas personalizados cerrados por EL TRABAJADOR: diez por ciento (10%) del recaudo del primer año de cada contrato; (b) cartera de alianzas: por cada estudiante que se matricule con carta de postulación de una empresa aliada registrada a nombre de EL TRABAJADOR, seis por ciento (6%) de los pagos que ese estudiante realice durante los doce (12) meses siguientes a la fecha de firma de su contrato de matrícula, y tres por ciento (3%) de los que realice entre los meses trece (13) y veinticuatro (24) contados desde esa misma fecha; a partir del mes veinticinco (25) no se causa comisión de cartera. Las comisiones se liquidan mensualmente sobre lo recaudado en el mes anterior, no tienen tope y constituyen salario.')
cl(4, 'INGRESO MÍNIMO GARANTIZADO (MESES 1 A 3)', 'Durante los tres (3) primeros meses de vigencia del contrato, en cada mes en que EL TRABAJADOR cumpla los indicadores de gestión del mes (cláusula 8), EL EMPLEADOR garantiza un ingreso total de TRES MILLONES QUINIENTOS MIL PESOS ($3.500.000), que incluye el básico y las comisiones del mes; si estos no alcanzan dicho valor, EL EMPLEADOR pagará la diferencia. Si las comisiones superan ese valor, se paga el total causado. En el mes en que no se cumplan los indicadores, no aplica la garantía y se paga el básico más las comisiones causadas.')
cl(5, 'METAS DE VENTAS', 'Se entiende por "ventas firmadas" el valor total de los contratos de plan empresa, cupos corporativos y programas personalizados cerrados por EL TRABAJADOR, firmados por EL EMPLEADOR y con el pago inicial recibido, sean de contado o a cuotas. La cartera de alianzas no cuenta para la meta. Las metas se evalúan por trimestre de vigencia del contrato, aumentan según el calendario de la tabla siguiente, conocido y aceptado por EL TRABAJADOR desde la firma, y no se fijan según los resultados de periodos anteriores:')
tabla([['Trimestre', 'Meses de contrato', 'Meta de ventas firmadas', 'Básico mensual'],
       ['T1', '1 a 3', '$90.000.000 en el trimestre ($30M/mes) + indicadores de gestión', 'SMMLV + auxilio'],
       ['T2', '4 a 6', '$144.000.000 en el trimestre ($48M/mes)', 'SMMLV + auxilio'],
       ['T3', '7 a 9', '$198.000.000 ($66M/mes)', 'SMMLV + $550.000 + auxilio (si cumple cl. 7)'],
       ['T4', '10 a 12', '$234.000.000 ($78M/mes)', 'SMMLV + $550.000 + auxilio (si cumple cl. 7)'],
       ['T5', '13 a 15', '$252.000.000 ($84M/mes)', 'SMMLV + $850.000 + auxilio (si cumple cl. 7)'],
       ['T6', '16 a 18', '$276.000.000 ($92M/mes)', 'SMMLV + $850.000 + auxilio (si cumple cl. 7)'],
       ['T7', '19 a 21', '$300.000.000 ($100M/mes)', 'SMMLV + $850.000 + auxilio (si cumple cl. 7)'],
       ['T8', '22 a 24', '$324.000.000 ($108M/mes)', 'SMMLV + $850.000 + auxilio (si cumple cl. 7)']])
cl(6, 'METAS DESDE EL MES 25', 'A partir del mes veinticinco (25), la meta de cada trimestre será la del trimestre inmediatamente anterior aumentada en dos punto cinco por ciento (2,5%), salvo que las partes firmen un otrosí con una tasa distinta, que podrá revisarse cada mes de diciembre con base en la capacidad operativa y el potencial del mercado.')
cl(7, 'ASCENSO DE BÁSICO', 'EL TRABAJADOR pasa al escalón de básico indicado en la tabla de la cláusula 5 cuando haya cumplido el 100% de la meta en al menos dos (2) de los tres (3) últimos trimestres evaluados. Una vez alcanzado un escalón, el básico no disminuye.')
cl(8, 'ACELERADOR', 'En los trimestres en que EL TRABAJADOR firme al menos dos (2) empresas nuevas con pago inicial recibido, la comisión del literal (a) de la cláusula 3 se liquidará así sobre el recaudo de los contratos que componen cada tramo, ordenados por fecha de firma: hasta el 100% de la meta trimestral, 10%; entre el 100% y el 130%, 15%; por encima del 130%, 20%. Sin tope.')
cl(9, 'INDICADORES DE GESTIÓN', 'Cada mes EL TRABAJADOR deberá registrar en el tablero de alianzas de la academia, el mismo día, con su soporte: cuarenta (40) empresas contactadas con persona que toma la decisión, doce (12) reuniones de presentación de veinte (20) minutos o más con dicha persona y, en los meses 1 a 3, tres (3) activaciones de alianzas; desde el mes 4, al menos una activación por trimestre por cada alianza activa. Resultados mínimos del primer trimestre: mes 1, dos (2) firmas y ventas firmadas por treinta millones de pesos ($30.000.000); mes 2, cuatro (4) firmas y ventas firmadas acumuladas por sesenta millones de pesos ($60.000.000); mes 3, seis (6) firmas y ventas firmadas acumuladas por noventa millones de pesos ($90.000.000). Únicamente para el primer mes, los contratos firmados con pago inicial recibido dentro de los cinco (5) días calendario siguientes a su cierre se contabilizan como del mes 1. Una alianza que no registre activación en treinta (30) días desde su firma no cuenta como firma. Cuando no se alcancen los indicadores, las partes acordarán por escrito un plan de ajuste de una (1) semana con metas concretas. [PENDIENTE ABOGADO: consecuencias del incumplimiento reiterado.]')
cl(10, 'ATRIBUCIÓN Y TERMINACIÓN', 'Una empresa queda a nombre de EL TRABAJADOR cuando la registra primero en el tablero con fecha y soporte. Un estudiante se atribuye a una alianza cuando presenta la carta de postulación de la empresa aliada y no figuraba como prospecto de la academia antes de la fecha de firma del convenio. Los contratos firmados con pago inicial recibido cuentan para la meta aunque el grupo inicie en fecha posterior por capacidad de la academia. A la terminación del contrato, por cualquier causa, EL TRABAJADOR tendrá derecho únicamente a las comisiones causadas sobre los valores recaudados hasta la fecha de terminación; los recaudos posteriores, incluida la cartera de alianzas, no generan comisión.')
cl(11, 'CONDICIONES COMERCIALES', 'EL TRABAJADOR cierra con las tarifas y documentos estándar vigentes de la academia (convenio de alianza, orden de plan empresa y tabla de precios: de 3 a 7 cupos $4.782.800, de 8 a 15 $4.350.000, de 16 a 30 $3.950.000 por cupo del programa completo, sobre un precio de lista de $8.696.000). No está facultado para otorgar descuentos adicionales. Todo convenio y orden los firma el representante legal. Más de treinta (30) cupos se cotizan con gerencia.')
cl(12, 'SEGUIMIENTO', 'EL TRABAJADOR organiza su agenda y sus visitas. Las partes sostendrán una reunión diaria de seguimiento de quince (15) minutos a hora fija (resultados del día anterior frente al plan y plan del día) y una reunión semanal de planeación de treinta (30) minutos los lunes. EL TRABAJADOR mantendrá el tablero de alianzas actualizado el mismo día.')
cl(13, 'MODIFICACIONES', 'Ninguna meta, tasa de comisión, garantía o condición de este anexo podrá modificarse sin acuerdo escrito firmado por ambas partes (otrosí).')
p('', after=10)
p('Para constancia se firma en Bucaramanga, el ____ de __________ de ______.', after=24)
p('_______________________________                    _______________________________', after=0)
p('EL EMPLEADOR                                                         EL TRABAJADOR', after=0)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\ANEXO_COMPENSACION_EJECUTIVO_ALIANZAS_BORRADOR.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
