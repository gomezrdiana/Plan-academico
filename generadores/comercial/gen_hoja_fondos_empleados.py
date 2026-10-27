# -*- coding: utf-8 -*-
"""HOJA que se deja al final de la presentación a un FONDO DE EMPLEADOS (una hoja carta, dos caras):
todo el detalle que se sacó de las diapositivas: quiénes somos, horarios, intensidad, docentes, evaluación, certificación,
garantía textual, tabla de valor económico, beneficios con fuentes, qué firma y contacto. Se entrega AL FINAL, nunca al inicio.
Salida: recursos/comercial/B2B/HOJA_FONDOS_EMPLEADOS_HEIIU.docx (+PDF por Word COM)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66); BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
R = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
OUT = R + r'\recursos\comercial\B2B\HOJA_FONDOS_EMPLEADOS_HEIIU.docx'
LOGO = R + r'\recursos\marca heiiu\logo_heiiu_transparente.png'
d = Document()
for s in d.sections:
    s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0); s.left_margin = Cm(1.6); s.right_margin = Cm(1.6)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9.5)


def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)


def sec(t):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAR


def t(txt, size=9.5, color=None, after=3, bold=False, align=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align is not None: p.alignment = align
    for part in txt.split('**'):
        pass
    parts = txt.split('**')
    for i, part in enumerate(parts):
        r = p.add_run(part); r.font.size = Pt(size); r.bold = bold or (i % 2 == 1)
        if color: r.font.color.rgb = color
    return p


def bullets(items, size=9.5):
    for x in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(1)
        parts = x.split('**')
        for i, part in enumerate(parts):
            r = p.add_run(part); r.font.size = Pt(size); r.bold = (i % 2 == 1)


def tabla(hdr, filas, anchos, size=9, bold_first=True):
    tb = d.add_table(rows=1, cols=len(hdr)); tb.style = 'Table Grid'
    for i, h in enumerate(hdr):
        c = tb.rows[0].cells[i]; shd(c, 'E54C09'); c.paragraphs[0].paragraph_format.space_after = Pt(0)
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = BLANCO
    for f in filas:
        row = tb.add_row().cells
        for i, txt in enumerate(f):
            row[i].paragraphs[0].paragraph_format.space_after = Pt(0)
            parts = txt.split('**')
            for k, part in enumerate(parts):
                r = row[i].paragraphs[0].add_run(part); r.font.size = Pt(size); r.bold = (bold_first and i == 0) or (k % 2 == 1)
    for row in tb.rows:
        for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    d.add_paragraph().paragraph_format.space_after = Pt(0)


# ---------------------------------------------------------------- CARA 1
d.add_picture(LOGO, height=Cm(1.6))
p = d.add_paragraph(); p.paragraph_format.space_after = Pt(0)
r = p.add_run('PROGRAMA DE INGLÉS PARA FONDOS DE EMPLEADOS — HOJA DE DETALLE'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
t('Beca del 45% para afiliados y sus familias, sin costo para el fondo · Garantía de aprendizaje por escrito · Heiiu English Academy — Global Teacher S.A.S., NIT 900.422.478-2', size=8.5, color=GRIS, after=4)

sec('1. Quiénes somos')
t('Academia presencial de Bucaramanga, **con licencia de la Secretaría de Educación desde 2012** (educación para el trabajo y el desarrollo humano) y **certificación de calidad ISO 9001 e ICONTEC**. Sede propia en Sotomayor, Carrera 27 # 48-49. Un solo programa, completo: **de A1 a B2 en 575 horas presenciales certificadas**, en grupos de máximo 16. B2 es el nivel que piden las vacantes, las universidades y los programas en el exterior. Convenios vigentes con entidades y empresas de la región, con becas a nombre de cada una.', after=2)
t('Vender inglés es fácil. Lo difícil es que la gente aprenda. En Heiiu queremos la parte difícil: que venga, que se suelte a hablar y que no se rinda. Por eso cada clase tiene una simulación real con un profesor que corrige ahí mismo; por eso hay un video corto en inglés todos los días desde la casa; y por eso, si un estudiante falta y no avisa, lo llamamos ese mismo día.', size=9, color=GRIS, after=2)

sec('2. El programa')
tabla(['Horarios', 'Intensidad', 'Docentes'], [
    ('Mañana: lunes a viernes, 8:00 a 12:00.\nNoche: lunes a viernes, 6:30 a 8:30 p. m.\nSábados: 8:00 a 12:00 (taller).\nCon 8 o más afiliados en un grupo, el horario lo define el fondo.',
     'Súper intensivo: 20 h por semana, programa completo en unos 7 meses.\nIntensivo: 10 h por semana, en unos 14 meses.\nMás un video corto en inglés todos los días, devuelto con una mejora.',
     'Profesores bilingües colombianos, uno por grupo de máximo 16. Trabajan como coach: dirigen la simulación, corrigen en el momento y revisan el video de cada día. Coordinación académica sigue asistencia, tareas y evaluaciones.'),
], [6.0, 6.0, 6.0], size=8.5, bold_first=False)
tabla(['Evaluación', 'Certificación', 'Garantía (texto del contrato)'], [
    ('Prueba de entrada el primer día. Evaluaciones durante el nivel y evaluación final con evaluador externo al cierre de cada nivel. Reporte al fondo: asistencia y cumplimiento de cada becado. Nunca notas: esas son del estudiante.',
     'Certificado Heiiu por cada nivel terminado (A1, A2, B1, B2) y por el programa completo, según los estándares de la Secretaría de Educación. Certificado de beca a nombre del fondo para cada becado.',
     '**Si el estudiante cumple su parte (asistencia del 80%, 90% de las tareas con video diario, todas las evaluaciones) y no avanza, le devolvemos el 100% del nivel.** No prometemos que sea fácil ni rápido. Prometemos que funciona si hace su parte, y lo firmamos.'),
], [6.0, 6.0, 6.0], size=8.5, bold_first=False)
t('Cada estudiante entra con una meta propia (una entrevista, un viaje, un negocio propio, el siguiente paso en su trabajo) y desde el primer día la trabajamos como un proyecto en inglés, con pasos y fecha. Próximo grupo: **martes 3 de noviembre de 2026**; no para en diciembre, solo descansa los festivos.', size=9, after=2)

sec('3. Valor económico para el afiliado con carta del fondo')
tabla(['Programa completo A1 a B2 (575 h)', 'Valor de lista', 'Con carta del fondo'], [
    ('De contado: transferencia, tarjeta, cesantías o crédito del fondo o de una cooperativa', '$8.696.000', '**$4.782.800 · beca del 45%**'),
    ('A cuotas, con crédito directo de la academia', '$8.696.000', '**$5.565.440 · beca del 36%**'),
    ('Ejemplo a cuotas: inicial del 20% y 11 cuotas', '', '**$1.113.088 hoy y 11 cuotas de $452.348**'),
], [9.6, 3.4, 5.0], size=8.5)
t('Es beca del Fondo de Becas Heiiu, no un descuento: la misma tarifa y la misma garantía para todos los que entran con carta del fondo. El crédito del fondo cuenta como pago de contado. Aplica también al cónyuge y a los hijos desde los 12 años (menor de edad con acudiente). **Beca con el nombre del fondo:** hasta 3 afiliados por trimestre, elegidos por el fondo, reciben el 45% aunque paguen a cuotas, más los libros y prioridad de cupo; si todos cumplen, suben a 5. **Si el fondo prefiere pagar los cupos (Plan Empresa):** $4.782.800 por cupo de 3 a 7, $4.350.000 de 8 a 15, $3.950.000 de 16 a 30; de contado o con inicial y 3 cuotas. Valores vigentes 30 días desde la presentación. Todo pago entra directamente a la academia; el fondo no recibe ni gestiona pagos.', size=8.5, after=0)

# ---------------------------------------------------------------- CARA 2
d.add_page_break()
sec('4. Qué gana el fondo')
bullets([
    '**Un beneficio nuevo para sus afiliados, sin costo para el fondo.** El fondo postula con una carta de una página; no paga ni cobra nada.',
    '**Becas y certificados con el nombre del fondo**, entregados en su propio evento o en la sede.',
    '**Reporte periódico** de asistencia y cumplimiento de cada becado: el fondo ve quién cumple.',
    '**Diagnóstico de nivel de inglés** para hasta 10 afiliados, sin costo, la semana siguiente a la firma.',
    '**Un afiliado que avanza se lo agradece al fondo.** Y lo que el fondo hace por su hijo, no lo olvida: la educación de los hijos está entre lo que más anhela un trabajador.⁴',
])
sec('5. Qué gana el afiliado y su familia')
bullets([
    '**Paga la mitad por ser afiliado:** beca del 45% sobre el programa completo, para él, su cónyuge y sus hijos desde los 12 años.',
    '**Quien certifica su inglés gana cerca de un 26% más** que quien hace el mismo trabajo sin él, y tiene más empleo formal.¹',
    '**Garantía por escrito:** si cumple su parte y no avanza, recibe el 100% del nivel de vuelta.',
    '**No entrena solo:** un profesor que corrige ahí mismo, un coach que no lo deja rendirse y una llamada el mismo día si falta.',
    '**Sale con algo que mostrar:** el video del primer día junto al del último, y una idea de negocio propia contada en inglés.',
    '**Para sus hijos que salen del colegio:** solo 1 de cada 8 termina el colegio con un inglés que le sirva;² y 1 de cada 5 jóvenes del país ni estudia ni trabaja.³ Un año de inglés con disciplina abre la beca, el intercambio y la carrera que sí es.',
])
t('¹ DNP, Archivos de Economía, Bilingüismo laboral en Colombia. ² Pruebas Saber 11 de 2025, análisis del Observatorio de Realidades Educativas de la Universidad Icesi. ³ DANE, Gran Encuesta Integrada de Hogares, jóvenes de 15 a 28 años, septiembre a noviembre de 2025. ⁴ Encuesta Provokers y Apprecio a trabajadores de Colombia, México, Chile y Perú.', size=7.5, color=GRIS, after=4)

sec('6. Qué firma el fondo y qué pasa después')
tabla(['Paso', 'Qué es', 'Cuándo'], [
    ('1. Convenio', 'Una hoja, sin costo ni obligaciones económicas. 12 meses. Cualquiera de las partes lo termina con aviso escrito de 30 días, sin afectar a los ya matriculados. El fondo designa un contacto y emite las cartas de postulación.', 'Hoy, o en la próxima junta'),
    ('2. Charla de 20 minutos', 'Con los afiliados, en el fondo o en la empresa. Les contamos el programa y el Pacto antes de que decidan; se registran los interesados.', 'Esta semana'),
    ('3. Diagnóstico de nivel', 'Hasta 10 afiliados, sin costo.', 'La semana siguiente a la firma'),
    ('4. Matrícula', 'Cada afiliado firma su contrato con la academia, con su carta de postulación. Separa cupo y paga la inicial; entra al grupo del 3 de noviembre.', 'Antes del 3 de noviembre'),
    ('5. Reporte', 'Asistencia y cumplimiento de los becados, al contacto del fondo.', 'Cada trimestre'),
], [3.4, 11.0, 3.6], size=8.5)
t('Lo que este convenio no incluye: exclusividad, intermediación laboral, promesas de empleo, visa o resultados. La academia trata los datos de los afiliados según la Ley 1581 de 2012, solo para los fines del convenio.', size=8.5, color=GRIS, after=6)

p = d.add_paragraph(); p.paragraph_format.space_after = Pt(0)
r = p.add_run('Contacto: Gerente de Alianzas · Línea de alianzas 316 768 8793 · Carrera 27 # 48-49, Sotomayor, Bucaramanga · Instagram @Heiiu_english'); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = NAR

try:
    d.save(OUT); print('OK', OUT)
except PermissionError:
    d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
