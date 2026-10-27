# -*- coding: utf-8 -*-
"""Carta-propuesta de convenio para un FONDO DE EMPLEADOS (2 páginas, PDF). Versión corregida de la propuesta que el
gerente de alianzas envió el 26/10/2026: cifras cerradas (nada "por definir"), beca y no descuento, un solo beneficio,
financiación sin nombrar entidades ni prometer aprobación o tasa de terceros, modalidades del convenio (sin sabatino ni
personalizado), reporte de asistencia y cumplimiento (nunca notas), inicio 3 de noviembre, cargo Gerente de Alianzas.
Uso: python generadores/comercial/gen_propuesta_fondo_empleados.py [NOMBRE DEL FONDO]   (por defecto: Fecolsa)
Salida: recursos/comercial/B2B/PROPUESTA_CONVENIO_<FONDO>.docx (+PDF por Word COM)."""
import sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONDO = sys.argv[1] if len(sys.argv) > 1 else 'Fecolsa'
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
R = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
OUT = R + r'\recursos\comercial\B2B\PROPUESTA_CONVENIO_' + FONDO.upper().replace(' ', '_') + '.docx'
LOGO = R + r'\recursos\marca heiiu\logo_heiiu_transparente.png'
d = Document()
for s in d.sections:
    s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9.5)


def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)


def runs(p, txt, size, color=None, bold=False):
    for i, part in enumerate(txt.split('**')):
        r = p.add_run(part); r.font.size = Pt(size); r.bold = bold or (i % 2 == 1)
        if color: r.font.color.rgb = color


def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(7); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR


def t(txt, size=9.5, color=None, after=4, bold=False, align=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align is not None: p.alignment = align
    runs(p, txt, size, color, bold); return p


def bullets(items, size=9.5):
    for x in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(1); runs(p, x, size)


def tabla(hdr, filas, anchos, size=9.5):
    tb = d.add_table(rows=1, cols=len(hdr)); tb.style = 'Table Grid'
    for i, h in enumerate(hdr):
        c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = BLANCO
    for f in filas:
        row = tb.add_row().cells
        for i, txt in enumerate(f):
            row[i].paragraphs[0].paragraph_format.space_after = Pt(0); runs(row[i].paragraphs[0], txt, size)
    for row in tb.rows:
        for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    d.add_paragraph().paragraph_format.space_after = Pt(0)


# ---------------------------------------------------------------- PÁGINA 1
tb = d.add_table(rows=1, cols=2); c0, c1 = tb.rows[0].cells
shd(c0, 'E54C09'); c0.width = Cm(4.2); c1.width = Cm(13.2)
c0.paragraphs[0].add_run().add_picture(LOGO, height=Cm(1.5)); c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
c0.paragraphs[0].paragraph_format.space_after = Pt(0)
p = c1.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
r = p.add_run('PROPUESTA DE CONVENIO · PROGRAMA DE INGLÉS PARA LOS AFILIADOS DE ' + FONDO.upper()); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = NAR
p2 = c1.add_paragraph(); p2.paragraph_format.space_after = Pt(0)
runs(p2, 'Beca del 45% para afiliados y sus familias, sin costo para el fondo · Garantía de aprendizaje por escrito', 9, GRIS)
p3 = c1.add_paragraph(); p3.paragraph_format.space_after = Pt(0)
runs(p3, 'Heiiu English Academy — Global Teacher S.A.S., NIT 900.422.478-2 · Bucaramanga, 27 de octubre de 2026', 9, GRIS)
d.add_paragraph().paragraph_format.space_after = Pt(2)

t('Señores **' + FONDO + '**', after=6)
t('Cordial saludo. Les proponemos un convenio para que sus afiliados y sus familias accedan a nuestro programa completo de inglés con beca del 45%, con el nombre de ' + FONDO + ' y sin costo ni obligaciones económicas para el fondo. Nuestro propósito lo decimos desde el primer día: **que el estudiante salga hablando inglés**. Y lo respaldamos por escrito: si cumple su parte y no avanza, le devolvemos el 100% del nivel.', after=4)

sec('1. Quiénes somos')
bullets(['Academia presencial de Bucaramanga, **con licencia de la Secretaría de Educación desde 2012** y certificación de calidad ISO 9001 e ICONTEC. Sede en Sotomayor, Carrera 27 # 48-49.',
         'Un solo programa, completo: **de A1 a B2 en 575 horas presenciales certificadas**, en grupos de máximo 16.',
         'Entrenamiento en equipo: el estudiante habla desde el primer día, con un profesor que corrige en el momento y un video corto diario desde la casa.'])

sec('2. El programa y su valor')
tabla(['Nivel', 'Horas', 'Valor de lista por nivel'], [
    ('A1 · Básico', '90', '$1.597.000'), ('A2 · Básico-intermedio', '110', '$1.915.000'),
    ('B1 · Intermedio', '175', '$2.842.000'), ('B2 · Avanzado', '200', '$2.344.000'),
    ('**Programa completo A1 a B2**', '**575**', '**$8.696.000 de lista · $4.782.800 con carta de ' + FONDO + '**')], [6.0, 2.0, 9.4])
t('**Modalidades del convenio:** mañana (lunes a viernes, 8:00 a 12:00; 20 h por semana, unos 7 meses) o noche (lunes a viernes, 6:30 a 8:30 p. m.; 10 h por semana, unos 14 meses). Con 8 o más afiliados en un mismo grupo, el horario lo define el fondo. Prueba de entrada, evaluaciones por nivel y evaluador externo al cierre de cada nivel. Certificado Heiiu por nivel y por programa completo.', after=3)

sec('3. Lo que nos diferencia: seguimiento y garantía')
bullets(['**Garantía por escrito:** si el estudiante cumple su parte (asistencia del 80%, 90% de las tareas con video diario, todas las evaluaciones) y no avanza, le devolvemos el 100% del valor del nivel.',
         '**Práctica diaria con retroalimentación:** un video corto cada día, devuelto por su profesor con una mejora concreta.',
         '**Aquí nadie desaparece:** si falta sin avisar, lo llamamos ese mismo día; cada clase registra la hora de llegada.',
         '**Progreso demostrable:** lo grabamos el primer día y el último del nivel, y el reporte de avance llega a la familia.',
         '**Una meta propia, con fecha:** cada estudiante entra con lo que quiere lograr (una entrevista, un viaje, un negocio propio, el siguiente paso en su trabajo) y lo acompañamos para contarlo y sostenerlo en inglés.'])

sec('4. Beneficios para los afiliados de ' + FONDO)
bullets(['**Beca del 45% con carta de postulación del fondo:** $4.782.800 de contado por el programa completo (lista $8.696.000). A cuotas con crédito directo de la academia: $5.565.440 (beca del 36%; por ejemplo, inicial de $1.113.088 y 11 cuotas de $452.348). Es beca del Fondo de Becas Heiiu, no un descuento: misma tarifa y misma garantía para todos los que entran con carta.',
         '**Beca con el nombre de ' + FONDO + ':** hasta tres afiliados por trimestre, elegidos por el fondo, reciben el 45% aunque paguen a cuotas, más los libros del programa y prioridad de cupo. Si todos cumplen, el cupo sube a cinco el trimestre siguiente.',
         '**Familia:** el beneficio cubre al afiliado, a su cónyuge y a sus hijos desde los 12 años (menor de edad con acudiente), con la misma carta.',
         '**Prueba de nivel sin costo** para hasta diez afiliados, y un contacto asignado al convenio en la academia.'])
t('**Formas de pago.** Cualquier crédito externo cuenta como pago de contado y da la beca mayor: crédito del fondo, cesantías, banco, cooperativa o caja de compensación. Quien prefiera no usar crédito externo tiene las cuotas con crédito directo de la academia. Todo pago se hace directamente a la academia; el fondo no recibe ni gestiona pagos.', after=0)

# ---------------------------------------------------------------- PÁGINA 2 (fluye sola)
sec('5. Compromisos de cada parte')
tabla(['Heiiu', FONDO], [
    ('Charla de 20 minutos con los afiliados, en el fondo o en la empresa, antes de que decidan. Material y piezas digitales para difundir el convenio. Prueba de nivel sin costo (hasta diez). Certificados de beca a nombre de ' + FONDO + '. Reporte periódico de asistencia y cumplimiento de los becados (nunca calificaciones), con autorización del estudiante y conforme a la Ley 1581 de 2012.',
     'Designar un contacto. Emitir la carta de postulación de cada afiliado o familiar que elija (modelo incluido). Difundir el beneficio por sus canales y facilitar el espacio para la charla. El fondo no asume ninguna obligación económica: cada afiliado contrata y paga directamente con la academia.')],
    [8.7, 8.7])

sec('6. Plan de implementación')
tabla(['Cuándo', 'Qué'], [
    ('Esta semana', 'Firma del convenio y fecha de la charla con los afiliados.'),
    ('Semana siguiente a la firma', 'Charla de 20 minutos y pruebas de nivel.'),
    ('Martes 3 de noviembre de 2026', 'Inicio del próximo grupo. No para en diciembre: sigue hasta terminar el nivel, solo descansa los festivos. Los afiliados que no entren esperan al siguiente grupo.'),
    ('Cada trimestre', 'Reporte de asistencia y cumplimiento al contacto del fondo; entrega de las becas con el nombre de ' + FONDO + '.')], [4.6, 12.8])

sec('7. Por qué le conviene a ' + FONDO)
bullets(['Un beneficio educativo nuevo para sus afiliados y sus familias, con el nombre del fondo, **sin inversión ni presupuesto**.',
         'Riesgo cubierto para el afiliado: **garantía de devolución del 100% del nivel** si cumple y no avanza.',
         'Se puede medir: el fondo recibe asistencia y cumplimiento de cada becado.',
         'Cero carga operativa: el fondo postula con una carta de una página; la academia hace el resto.'])

sec('8. Condiciones')
bullets(['Vigencia de esta propuesta: 30 días desde su envío. Vigencia del convenio: 12 meses, renovables por acuerdo escrito; cualquiera de las partes puede terminarlo con aviso escrito de 30 días, sin afectar a los ya matriculados.',
         'El convenio no otorga exclusividad, no constituye intermediación laboral ni promete empleo, visa ni resultados. Los valores corresponden a las tarifas vigentes y se ajustan anualmente.',
         'La garantía aplica cuando el estudiante cumple los compromisos de asistencia, práctica diaria y evaluaciones de su contrato de matrícula.'])

sec('9. Siguiente paso')
t('Proponemos una reunión de 20 minutos esta semana para firmar el convenio (una página, adjunta) y fijar la fecha de la charla con los afiliados, de modo que quienes decidan entren al grupo del 3 de noviembre. Quedamos atentos.', after=10)
t('Cordialmente,', after=22)
t('**John Jairo Hinestroza**\nGerente de Alianzas · Heiiu English Academy\nLínea de alianzas 316 768 8793 · @heiiu_english · Carrera 27 # 48-49, Sotomayor, Bucaramanga', size=10, after=6)
t('Adjuntos: Convenio Heiiu Business Partner para entidades (1 página) · Modelo de carta de postulación · Hoja de detalle del programa.', size=8.5, color=GRIS, after=0)

try:
    d.save(OUT); print('OK', OUT)
except PermissionError:
    d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
