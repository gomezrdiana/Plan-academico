# -*- coding: utf-8 -*-
"""Respuesta a las 4 dudas de Paula (24/09/2026): cita modelo, motor de cuotas, separacion de cupo, comision por pagos parciales."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NARANJA = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.6); s.bottom_margin = Cm(1.4); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10.5)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)

def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = NARANJA

def t(txt, bold=False, italic=False):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(txt); r.font.size = Pt(10.5); r.bold = bold; r.italic = italic

def num(n, txt):
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.6); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(f'{n}. '); r.bold = True; p.add_run(txt)

def tabla(filas, anchos):
    tb = doc.add_table(rows=len(filas), cols=len(filas[0])); tb.style = 'Table Grid'
    for i, fila in enumerate(filas):
        for j, v in enumerate(fila):
            c = tb.cell(i, j); c.width = Cm(anchos[j]); c.paragraphs[0].paragraph_format.space_after = Pt(0)
            r = c.paragraphs[0].add_run(v); r.font.size = Pt(9.5)
            if i == 0: r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); shd(c, 'E54C09')
            elif j == 0: r.bold = True; shd(c, 'FFF8E7')

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('RESPUESTA A TUS CUATRO PREGUNTAS'); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = NARANJA
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(8)
r = p.add_run('Para Paula · Heiiu English Academy · 24 de septiembre de 2026'); r.font.size = Pt(9); r.font.color.rgb = GRIS

t('Paula, buenas preguntas: son exactamente las que hay que hacer antes de la primera cita. Te las respondo en orden.')

sec('1. LA CITA MODELO: CÓMO EMPEZAR, QUÉ PREGUNTAR, CÓMO CERRAR')
t('Te propongo algo mejor que verme a mí: hacemos una SIMULACIÓN por videollamada esta semana. Yo hago de cliente y tú conduces la cita completa con el Guion de Cierre en Cita en la mano. Hacemos dos rondas con dos perfiles distintos — el que ya intentó y fracasó, y el que compara precios — y al final te digo qué se sintió desde el lado del cliente. Así ves el estilo en acción y lo adaptas a tu forma de hablar desde el primer día.')
t('El estilo Heiiu en una frase: preguntar más que hablar. La cita se gana con las preguntas de diagnóstico (qué ha intentado, para qué lo necesita, quién decide), no con la presentación. El programa y el precio llegan después, cuando ya sabes qué le duele.')
t('Lo que es INDISPENSABLE en toda cita (no se negocia):', bold=True)
num(1, 'La pregunta de nivel: "¿Has estudiado inglés antes? ¿Cómo te fue?" — define el camino y detecta al cliente quemado.')
num(2, 'La pregunta de Cajasan: se pregunta y se anota siempre. El afiliado (con carné o certificado vigente) entra a la columna Transformación en todos los paquetes, sin importar su estrato: 45% de contado o 36% a cuotas en el completo. Es la alianza registrada con Cajasan.')
num(3, 'Las 4 anclas: garantía por escrito · avance medido · institución con licencia e ICONTEC · formación del carácter.')
num(4, 'La pregunta de la meta: "¿Tu meta es montar algo tuyo, o irte a trabajar afuera?" — abre los módulos de graduación.')
num(5, 'El cierre doble: Arranque $2.990.000 o programa completo con beca. Las dos respuestas son SÍ.')
num(6, 'Si "ya sabe algo": sesión de ubicación agendada con fecha y hora antes de despedirse.')
num(7, 'Si es Arranque: las dos jornadas y la regla del grupo mínimo, ANTES de firmar. La regla: cada jornada abre con mínimo 6 estudiantes, pero ese número es interno y la consolidación la decide gerencia al cierre de cupos. Tú solo haces la pregunta obligada — "¿tu horario es fijo o tienes flexibilidad entre mañana y noche?" — y lo anotas. Jamás se dice que un grupo "podría no abrir"; al de horario fijo se le da seguridad: "tu cupo queda en tu jornada y tu plata está protegida: si algo cambiara, precio congelado o abono devuelto, jamás te movemos sin tu sí".')
num(8, 'La frase del expediente: la garantía y el video diario se firman juntos. El estudiante graba un video corto todos los días y lo envía a la academia: en A1 basta un minuto (A2 2, B1 3, B2 5), de corrido y sin leer. Es su evidencia para la garantía y donde él mismo ve su cambio.')
num(9, 'Una frase de cierre y silencio. El primero que habla, concede.')
num(10, 'Si no cierra hoy: oferta por escrito con vencimiento a 72 horas + abono de separación ofrecido + motivo real anotado.')
t('Y tres reglas de lenguaje: se dice "beca del Fondo", nunca "descuento"; la garantía se cita solo con su texto exacto; y jamás se promete fácil, rápido ni divertido — se promete método, respaldo y garantía a cambio de trabajo.', bold=True)
t('Lo que es TUYO (libertad total): el orden en que lo dices, tus palabras, tus historias, el tono, el ritmo, cómo generas confianza. Nadie te va a pedir que repitas un guion. El guion es la lista de lo que no puede faltar; la conversación es tuya.')

sec('2. EL MOTOR DE CUOTAS')
t('Sí, lo tienes: es el archivo MOTOR_CUOTAS_FONDO_2026.xlsx que va en tu kit. Se usa así:')
num(1, 'Eliges el paquete (Arranque, completo A1→B2, A2→B2, B1→B2 o solo B2).')
num(2, 'Eliges el perfil del cliente (Transformación, General o Ejecutivo) — eso define la beca.')
num(3, 'Pones la cuota inicial (mínimo 20%) y el número de cuotas que el cliente quiere, sin pasar el máximo de su modalidad.')
num(4, 'El motor te da la cuota mensual, ya con el 1,9% de interés incluido.')
t('Regla de oro: nunca calcules de memoria ni "más o menos". Y al cliente siempre le das el plan completo — inicial + número de cuotas + valor de cada cuota — nunca solo la cuota. Si pide menos cuotas que el máximo, siempre se puede y paga menos interés. Más que el máximo, nunca.', bold=True)
t('Recuerda: cesantías, crédito de un tercero (Comultrasan, banco) y tarjeta de crédito cuentan como CONTADO para nosotros — beca de contado y sin interés nuestro. Las condiciones del pago con tarjeta se tratan en la cita, nunca por escrito.')

sec('3. LA SEPARACIÓN DE CUPO, PASO A PASO')
tabla([
    ['Paso', 'Quién', 'Qué hace'],
    ['1. Abono', 'Cliente', 'Transfiere $300.000 a las cuentas oficiales de la academia (te paso los datos con el kit) y te envía el pantallazo del comprobante. Nunca efectivo por fuera de la sede, nunca a cuentas personales.'],
    ['2. Recibo', 'Tú', 'Llenas el Recibo de Separación de Cupo (la plantilla Word que va en tu kit: 12 datos), lo guardas como PDF y se lo envías. Numeración: cada persona que separa cupos usa sus iniciales (primer nombre y apellido) y su propio consecutivo sin saltos: los tuyos van PS-001, PS-002, PS-003…; los de la academia van GT-001, GT-002…; quien entre después usa las suyas. Nadie comparte prefijo, así nunca chocan.'],
    ['3. Aceptación', 'Cliente', 'Responde por escrito "ACEPTO las condiciones del recibo No. X", con la foto de su cédula. Junto con el pantallazo del comprobante, ese mensaje tiene validez legal.'],
    ['4. Confirmación del pago', 'Academia', 'La auxiliar administrativa verifica que el dinero entró y te confirma. Solo con esa confirmación el cupo queda separado.'],
    ['5. Cita de ubicación', 'Tú', 'En el mismo acto agendas su sesión de ubicación, con fecha y hora. Ninguna separación queda sin cita.'],
    ['6. Planilla', 'Tú', 'Registras todo en el Registro Maestro: fecha del abono, estado ABONO, cita agendada.'],
    ['7. Formalización', 'Academia', 'El contrato de matrícula se firma en físico en la sede, a más tardar el primer día de clases. "El chat asegura el cupo; la sede firma el contrato."'],
], [3.0, 2.2, 11.6])
t('Lo que el abono garantiza: cupo y precio congelados por 7 días calendario. Si el cliente se retracta dentro de los 5 días hábiles de ley, se le devuelve completo; después queda como saldo a favor para cualquier programa durante 12 meses. Nunca devolución en efectivo por fuera de ese plazo.')

sec('4. TU COMISIÓN CUANDO EL CLIENTE PAGA EN VARIOS MOMENTOS')
t('La regla es una: LA COMISIÓN SIGUE A LA PLATA. Ganas tu porcentaje sobre cada peso que entra a caja, en el momento en que entra, no sobre el precio de la venta.', bold=True)
t('Ejemplo con tu 8%, un cliente del Arranque a cuotas:')
tabla([
    ['Fecha', 'Lo que paga el cliente', 'Tu comisión (8%)', 'Cuándo se te paga'],
    ['25 sep', 'Abono $300.000', '$24.000', 'El retracto (5 días hábiles) vence el 2 oct: no alcanza el corte del 30 sep, se paga en el corte del 5 oct'],
    ['3 oct', 'Inicial $598.000 (cruza el abono: paga $298.000)', '$23.840', 'El retracto vence el 10 oct: se paga en el corte del 31 oct'],
    ['5 nov', 'Cuota 1 $626.672', '$50.134', 'Corte de noviembre'],
    ['5 dic', 'Cuota 2 $626.672', '$50.134', 'Corte de diciembre'],
], [2.0, 5.2, 3.2, 6.4])
t('Cómo funciona en la práctica:')
num(1, 'Cortes: 30 de septiembre, 5 de octubre y después el último día de cada mes. Se te paga contra cuenta de cobro dentro de los 5 días hábiles siguientes al corte.')
num(2, 'Solo se liquidan pagos cuyo retracto legal (5 días hábiles) ya venció. Un pago que entra dos días antes del corte se te paga en el corte siguiente.')
num(3, 'Si un pago se devuelve por retracto o devolución, la comisión de ese pago se descuenta de tu siguiente liquidación.')
num(4, 'Si alcanzas la puerta del 10% (12 matrículas en tus primeros 12 días de campaña, o 20 cupos antes del 5 de octubre), la diferencia del 2% sobre todo lo ya comisionado se te paga en el corte en que la alcances, y de ahí en adelante todo va al 10%.')
num(5, 'Cobrar también es vender: si el cliente deja de pagar sus cuotas, deja de haber comisión sobre lo que no entró. Por eso conviene que las cuotas queden cortas y claras desde la cita.')

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(10)
r = p.add_run('Cualquier duda que salga en la primera semana, me la escribes y entra a este mismo documento.'); r.font.size = Pt(9.5); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\RESPUESTA_PAULA_DUDAS_24SEP.docx'
doc.save(out); print('OK', out)
