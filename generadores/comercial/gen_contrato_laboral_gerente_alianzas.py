# -*- coding: utf-8 -*-
"""Contrato individual de trabajo a término INDEFINIDO con período de prueba de 2 meses para el Gerente de Alianzas
Empresariales. Cláusulas estándar del CST; la compensación vive en el ANEXO No. 1. BORRADOR para firma, pendiente de
revisión del abogado (no cambia lo pactado). Salida (fuera de git): Candidatos/John Hinestroza/CONTRATO_LABORAL_JOHN_BORRADOR.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

GRIS = RGBColor(0x66, 0x66, 0x66)
OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza\CONTRATO_LABORAL_JOHN_BORRADOR.docx'
TRABAJADOR = 'JOHN HINESTROZA'
d = Document()
for s in d.sections:
    s.top_margin = Cm(1.5); s.bottom_margin = Cm(1.3); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10)

def p(txt, bold=False, size=10, align=None, after=5, color=None):
    x = d.add_paragraph(); x.paragraph_format.space_after = Pt(after)
    if align is not None: x.alignment = align
    r = x.add_run(txt); r.bold = bold; r.font.size = Pt(size)
    if color is not None: r.font.color.rgb = color
    return x
def cl(nombre, cuerpo):
    x = d.add_paragraph(); x.paragraph_format.space_after = Pt(5); x.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = x.add_run(nombre + ' '); r.bold = True; r.font.size = Pt(10)
    r = x.add_run(cuerpo); r.font.size = Pt(10)

p('CONTRATO INDIVIDUAL DE TRABAJO A TÉRMINO INDEFINIDO', True, 13, WD_ALIGN_PARAGRAPH.CENTER, 2)
p('Borrador para firma · pendiente de revisión del abogado (la revisión no modifica lo pactado) · 19/10/2026', False, 9, WD_ALIGN_PARAGRAPH.CENTER, 8, GRIS)

tb = d.add_table(rows=0, cols=2); tb.style = 'Table Grid'
for a, b in [
 ('EMPLEADOR', 'GLOBAL TEACHER S.A.S. (Heiiu English Academy), NIT 900.422.478-2, domicilio Bucaramanga, representada legalmente por DIANA MARCELA GÓMEZ RANGEL, C.C. 63.552.709 de Bucaramanga.'),
 ('TRABAJADOR', TRABAJADOR + ', identificado con C.C. No. ____________________ de ____________________, domiciliado en ______________________________, teléfono ______________, correo ______________________________.'),
 ('CARGO', 'Gerente de Alianzas Empresariales.'),
 ('SALARIO BÁSICO', 'Salario mínimo legal mensual vigente ($1.750.905 en 2026) más auxilio de transporte legal ($249.095 en 2026), más las comisiones, garantías y acelerador del ANEXO No. 1, que constituyen salario.'),
 ('FECHA DE INICIO', 'Martes 20 de octubre de 2026.'),
 ('PERÍODO DE PRUEBA', 'Dos (2) meses: del 20 de octubre al 19 de diciembre de 2026.'),
 ('LUGAR DE TRABAJO', 'Bucaramanga y su área metropolitana: sede de la academia (Carrera 27 # 48-49, Sotomayor) y trabajo de campo en empresas.'),
]:
    c = tb.add_row().cells
    r = c[0].paragraphs[0].add_run(a); r.bold = True; r.font.size = Pt(9.5)
    r = c[1].paragraphs[0].add_run(b); r.font.size = Pt(9.5)
for row in tb.rows:
    row.cells[0].width = Cm(3.6); row.cells[1].width = Cm(13.4)
d.add_paragraph().paragraph_format.space_after = Pt(2)

p('Entre las partes identificadas arriba, en adelante EL EMPLEADOR y EL TRABAJADOR, se celebra el presente contrato individual de trabajo, regido por el Código Sustantivo del Trabajo y por las siguientes cláusulas:', after=6)

cl('PRIMERA. OBJETO Y CARGO.', 'EL EMPLEADOR contrata a EL TRABAJADOR para desempeñar el cargo de Gerente de Alianzas Empresariales: desarrollar el canal corporativo e institucional de la academia (empresas, fundaciones, cajas de compensación y organizaciones), presentar la propuesta de valor, negociar y cerrar convenios de alianza y órdenes de plan empresa, activar las alianzas firmadas, cerrar programas personalizados y gestionar los contactos de la base de la academia que gerencia le asigne, conforme a las funciones, indicadores y condiciones del ANEXO No. 1, que hace parte integral de este contrato. EL TRABAJADOR no tiene personal a cargo. El cargo es de confianza y manejo en los términos del artículo 162 del CST.')
cl('SEGUNDA. DURACIÓN.', 'El contrato es a término indefinido y rige desde el 20 de octubre de 2026.')
cl('TERCERA. PERÍODO DE PRUEBA.', 'Conforme a los artículos 76 a 80 del CST, las partes pactan un período de prueba de DOS (2) MESES, contados desde la fecha de inicio. Durante este período cualquiera de las partes podrá dar por terminado el contrato sin previo aviso y sin indemnización. La evaluación del período de prueba toma como criterio los resultados y los indicadores del ANEXO No. 1 (cláusula 9), registrados en el tablero de alianzas y en las actas de seguimiento, con cortes al día treinta (30) y al día cuarenta y cinco (45).')
cl('CUARTA. SALARIO Y FORMA DE PAGO.', 'EL TRABAJADOR devengará el salario básico indicado en el encabezado, más las comisiones, el ingreso mínimo garantizado de los meses 1 a 3 y el acelerador pactados en el ANEXO No. 1, que tienen naturaleza salarial y se liquidan mensualmente sobre lo efectivamente recaudado en el mes anterior. El pago se hace por transferencia a la cuenta que EL TRABAJADOR abra en la entidad bancaria indicada por EL EMPLEADOR, con los períodos de pago de nómina de la academia. De la cartera de alianzas y de la terminación aplica lo previsto en el ANEXO No. 1.')
cl('QUINTA. JORNADA Y SEGUIMIENTO.', 'EL TRABAJADOR organiza su agenda y sus visitas dentro de la jornada máxima legal. Son de obligatorio cumplimiento: el seguimiento diario con gerencia a hora fija (lunes presencial de planeación, martes a jueves virtual, viernes presencial de cierre de semana), que EL TRABAJADOR prepara y presenta y del que queda registro escrito; y el tablero de alianzas actualizado el mismo día. Las sesiones presenciales pueden realizarse con gerencia o con quien gerencia designe.')
cl('SEXTA. OBLIGACIONES ESPECIALES DE EL TRABAJADOR.', '(a) Registrar en el tablero, el mismo día y con soporte, cada contacto, reunión, activación, firma y venta. (b) Cerrar únicamente con las tarifas, becas y documentos estándar vigentes de la academia; no está facultado para otorgar descuentos ni condiciones distintas, ni para firmar convenios u órdenes en nombre de EL EMPLEADOR, que firma el representante legal. (c) No recibir dinero de clientes ni estudiantes: todo pago ingresa a las cuentas de EL EMPLEADOR; el efectivo que reciba por excepción se entrega en la sede el mismo día contra recibo. (d) Tratar los datos personales de prospectos, clientes y estudiantes conforme a la Ley 1581 de 2012 y a las políticas de EL EMPLEADOR, usándolos solo para este contrato. (e) Cumplir las reglas comerciales de la academia: no prometer resultados, empleo ni visas; no ofrecer clase de prueba ni modalidades que no existan; no nombrar competidores. (f) Usar su propio teléfono y medio de transporte, cuyo costo no asume EL EMPLEADOR salvo acuerdo escrito.')
cl('SÉPTIMA. EXCLUSIVIDAD Y NO CONFLICTO.', 'Durante la vigencia del contrato EL TRABAJADOR no comercializará, directa ni indirectamente, programas de idiomas ni servicios educativos de terceros, ni usará el nombre, la marca o la información de EL EMPLEADOR para fines distintos de este contrato.')
cl('OCTAVA. CONFIDENCIALIDAD Y PROPIEDAD INTELECTUAL.', 'La información comercial, los precios, las bases de datos, el tablero, los guiones, los documentos de alianza y el material pedagógico de EL EMPLEADOR son confidenciales y de su propiedad exclusiva. EL TRABAJADOR se obliga a no divulgarlos, copiarlos ni usarlos fuera de este contrato, durante su vigencia y hasta dos (2) años después de su terminación, y a devolver todo material y acceso al terminar. Las empresas, contactos y alianzas registrados pertenecen a EL EMPLEADOR.')
cl('NOVENA. FALTAS GRAVES.', 'Además de las previstas en la ley y en el reglamento interno de trabajo, se consideran faltas graves que justifican la terminación con justa causa: recibir dinero de clientes sin entregarlo el mismo día; otorgar descuentos o condiciones no autorizadas; alterar u omitir registros del tablero; usar o divulgar información confidencial; comercializar servicios de terceros; y el incumplimiento grave o reiterado de las obligaciones e indicadores del ANEXO No. 1, previo requerimiento escrito.')
cl('DÉCIMA. TERMINACIÓN.', 'El contrato termina por las causas legales (artículos 61 y 62 del CST), por decisión de cualquiera de las partes durante el período de prueba, o por renuncia de EL TRABAJADOR con preaviso de quince (15) días. A la terminación se liquidan las prestaciones de ley y las comisiones causadas sobre lo efectivamente recaudado hasta la fecha de retiro, en los términos del ANEXO No. 1.')
cl('DÉCIMA PRIMERA. ANEXO Y MODIFICACIONES.', 'El ANEXO No. 1 (esquema de compensación, metas e indicadores) hace parte integral de este contrato. El esquema se revisa cada año en diciembre según rendimiento y condiciones del negocio; ninguna meta, tasa, garantía o condición se modifica sin otrosí firmado por ambas partes, salvo los aumentos de meta ya pactados en el anexo.')
cl('DÉCIMA SEGUNDA. AFILIACIONES Y DOCUMENTOS.', 'EL EMPLEADOR afilia a EL TRABAJADOR al sistema de seguridad social (salud, pensión, riesgos laborales) y a la caja de compensación familiar desde la fecha de inicio. EL TRABAJADOR entrega a coordinación, a más tardar el miércoles 21 de octubre de 2026, los documentos requeridos para la afiliación y la nómina (RUT, certificados de EPS y fondo de pensiones, hoja de vida, certificados laborales) y el resultado del examen médico de ingreso.')
cl('DÉCIMA TERCERA. DOMICILIO.', 'Para todos los efectos las partes fijan como domicilio contractual la ciudad de Bucaramanga. Este contrato reemplaza cualquier acuerdo verbal o escrito anterior sobre el cargo.')
p('', after=8)
p('Para constancia se firma en Bucaramanga, el ____ de octubre de 2026, en dos ejemplares del mismo tenor.', after=28)
p('_______________________________                                   _______________________________', after=0)
p('EL EMPLEADOR                                                                        EL TRABAJADOR', after=0)
p('Diana Marcela Gómez Rangel · Representante legal                        ' + TRABAJADOR, after=0, size=9.5)
p('Global Teacher S.A.S. · NIT 900.422.478-2                                        C.C. ____________________', after=0, size=9.5)

try: d.save(OUT); print('OK', OUT)
except PermissionError: d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
