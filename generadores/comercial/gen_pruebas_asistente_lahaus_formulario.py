# -*- coding: utf-8 -*-
"""Formulario de pruebas del asistente LaHaus: texto para copiar + espacio para pegar la respuesta.
Salida: recursos/comercial/plataforma LaHaus/PRUEBAS_ASISTENTE_RONDA2_FORMULARIO.docx"""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.5); s.bottom_margin = Cm(1.3); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10.5)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)

def h(txt, size=13, color=NAR, after=4, before=8):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(before)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = color

def t(txt, bold=False, after=3, size=10.5, color=None, italic=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold; r.italic = italic
    if color: r.font.color.rgb = color

def prueba(n, escribe, debe, respondio=''):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f'{n}. ESCRIBE (copiar y pegar):'); r.bold = True; r.font.size = Pt(10); r.font.color.rgb = NAR
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'
    c = tb.rows[0].cells[0]; shd(c, 'FFF8E7')
    pp = c.paragraphs[0]; pp.paragraph_format.space_after = Pt(0)
    rr = pp.add_run(escribe); rr.font.size = Pt(11); rr.bold = True
    t('Debe: ' + debe, size=9, color=GRIS, after=2)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
    r = p.add_run('RESPONDIÓ:'); r.bold = True; r.font.size = Pt(10)
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'
    c = tb.rows[0].cells[0]
    pp = c.paragraphs[0]; pp.paragraph_format.space_after = Pt(0)
    rr = pp.add_run(respondio if respondio else '\n\n'); rr.font.size = Pt(10.5)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(0)
    r = p.add_run('☐ Pasó   ☐ Falló   Nota: ________________________________________________'); r.font.size = Pt(9); r.font.color.rgb = GRIS

h('PRUEBAS DEL ASISTENTE HEIIU EN LAHAUS — RONDA 2 (formulario)', 14, before=0)
t('Copia el texto naranja, pégalo en el chat de prueba, y pega la respuesta del asistente en el cuadro de abajo. Al terminar, comparte este archivo con gerencia. Interno: no se envía a LaHaus.', color=GRIS, after=6)

R1 = ('Hola. Bienvenido al lugar donde el inglés se convierte en tus nuevas oportunidades. En Global Teacher tenemos el método ideal '
      'para que hables con fluidez desde el primer día. 🌍 ¿Quieres evaluar tu nivel sin costo o ver nuestros planes de estudio?')

h('CONVERSACIÓN 1 — la cliente ideal (una sola conversación, seguida, en este orden)', 11.5)
t('Personaje: ingeniera industrial, 32 años, quiere presentar proyectos en inglés en su empresa, no sabe nada de inglés, trabaja de oficina 8 a 5.', color=GRIS, italic=True)
B = [
    ('Hola, vi el anuncio, quiero información', 'saluda como Heiiu, UNA pregunta (motivo o nombre), sin precios.', R1),
    ('Quiero trabajar', 'profundiza en el destino (¿trabajar en qué, dónde, cuándo?), no salta a nivel ni cita.'),
    ('Soy ingeniera industrial, quiero presentar proyectos en inglés en mi empresa. No sé nada de inglés', 'desde cero = sin prueba de ubicación; propone el PROGRAMA COMPLETO, no el Arranque; una pregunta.'),
    ('¿Y eso cuánto vale?', 'precio del completo en contexto; contado primero, cuotas después; Cajasan como respaldo; sin "descuento".'),
    ('Uy, muy caro', 'no baja el precio ni se disculpa; reencuadra valor; solo ahora ofrece el Arranque.'),
    ('Es que en Smart me dan 3 años para terminar y más barato', 'no nombra a Smart ni la desprestigia; contrasta con garantía y tiempo.'),
    ('¿Puedo tomar una clase de prueba gratis?', 'no hay clase de cortesía; explica en una frase; ofrece asesoría o visita.'),
    ('¿Qué experiencia tienen enseñando inglés?', 'una sola fecha: 2012, con licencia.'),
    ('¿Y cómo son las clases?', 'entrenamiento: bloques largos, simulaciones, video diario, virtudes; sin "de pie", sin metodologías, corto.'),
    ('¿Qué se ve en A1?', 'temas reales del nivel; no inventa.'),
    ('Vi que tienen malos reviews', 'sin defensiva; garantía firmada como prueba; invita a la sede.'),
    ('Bueno, gracias, lo voy a pensar', 'no suelta: pregunta qué le falta, propone fecha; sin presión burda.'),
    ('Tengo que hablarlo con mi esposo', 'invita al esposo a la cita; pregunta cuándo pueden los dos.'),
    ('Listo, agéndame', 'solo franjas del calendario de la asesora; pide nombre, no celular; confirma día, hora y sede.'),
    ('¿Los libros van incluidos?', 'solo con condición: incluidos si separa el cupo el mismo día de la cita.'),
]
n = 1
for item in B:
    prueba(n, item[0], item[1], item[2] if len(item) > 2 else ''); n += 1

h('PRUEBAS SUELTAS — cada una en una conversación nueva', 11.5)
S = [
    ('Trabajo por turnos rotativos, una semana de día y otra de noche', 'honesto: hoy no le sirve; no lo vende; deja la puerta abierta.'),
    ('Solo puedo virtual', 'no hay virtual; claro y corto; no promete "pronto".'),
    ('Es que estoy pensando en viajar en unos meses', 'pregunta cuándo y cuánto; 80% de asistencia y sin aplazamientos; no promete congelar.'),
    ('Es para mi hijo de 15 años', 'el acudiente viene a la cita y firma; pregunta jornada del colegio.'),
    ('Quiero irme de Au Pair el otro año', 'proyección: "el inglés es el pasaporte", la entrevista con la familia, el nivel que pide; no solo precio.'),
    ('¿Puedo pagar con tarjeta de crédito?', 'sí, como contado; "las condiciones se tratan en la cita"; NADA sobre recargo.'),
    ('¿Si llego tarde pierdo la garantía?', 'más de 15 min = tarde; 3 = 1 falta; 80% asistencia, 90% tareas con video, todas las evaluaciones; como formación.'),
    ('¿Y si no me gusta el profesor?', 'feedback diario y coordinación; no promete cambio de profesor a voluntad.'),
    ('¿Y si la clase me parece aburrida?', 'no vende "divertido"; entrenamiento con destino; qué hace la academia si algo no funciona.'),
    ('¿Puedo congelar el programa si me sale algo?', 'no hay aplazamientos; explica qué sí hay.'),
    ('¿Y si el grupo no abre?', 'otra jornada, precio congelado para la siguiente cohorte, o devolución total del abono.'),
    ('¿Dan descuento si pago de contado?', 'nunca "descuento"; el contado es el precio; la beca es Cajasan / Transformación.'),
    ('Para qué tanto video, es mucha repetición', 'una analogía (nadador, tablas de multiplicar) y el porqué del video diario; corto.'),
    ('¿Tienen profesores nativos?', 'no promete nativos; docentes certificados y el entrenamiento.'),
    ('¿Me das el número de la academia para llamar?', 'da el número oficial o remite a la asesora; nunca "este mismo número".'),
    ('Soy estudiante de B1, quiero cambiar de horario', 'no vende; remite a Experiencia al Cliente (una persona).'),
    ('Necesito la factura de mi pago', 'remite al canal correcto; aquí sí puede decir Global Teacher S.A.S.'),
    ('Ustedes son unos estafadores, me robaron la plata', 'calma, no discute, no promete devolución; pasa a una persona.'),
    ('¿Es Global Teacher o Heiiu? Me confundí', 'Heiiu es la academia; Global Teacher S.A.S. la razón social del contrato y la factura.'),
]
for esc, deb in S:
    prueba(n, esc, deb); n += 1

h('EN TODOS LOS MENSAJES, marca si pasó:', 11.5)
for txt in ['☐ Una sola pregunta por mensaje', '☐ Habla como Heiiu (Global Teacher solo por factura o razón social)', '☐ No ofrece cita antes de vender (motivo → nivel → programa → cita)',
            '☐ No repite el método en cada respuesta; nunca "de pie" ni nombres de metodologías', '☐ Máximo un emoji, y no en cada mensaje', '☐ Nunca "descuento", nunca "recargo", nunca nativos, nunca virtual', '☐ Nunca pide el celular; solo horarios del calendario de la asesora']:
    t(txt, after=1)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus\PRUEBAS_ASISTENTE_RONDA2_FORMULARIO.docx'
doc.save(out); print('OK', out)
