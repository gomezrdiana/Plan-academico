# -*- coding: utf-8 -*-
"""Hoja de arranque del docente recolector-cerrador de referidos (Juan Diego), 15/10/2026. Dos páginas, en USTED.
Flujo directo (decisión de gerencia 14/10): el estudiante o egresado entrega nombre y número del amigo con su OK previo;
el docente escribe primero y luego llama. Deriva de PROGRAMA_REFERIDOS_PROPUESTA_2026-10 (versión final).
Salida: recursos/comercial/HOJA_ARRANQUE_REFERIDOS_DOCENTE.docx (+ PDF por Word)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
m = lambda v: f'${v:,.0f}'.replace(',', '.')
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.3); s.bottom_margin = Cm(1.1); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(7); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR
def t(txt, bold=False, size=10, color=None, after=3):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def item(txt, prefix=None):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1.5); p.paragraph_format.left_indent = Cm(0.4)
    if prefix:
        r = p.add_run(prefix + ' '); r.bold = True; r.font.size = Pt(10)
    r = p.add_run(txt); r.font.size = Pt(10)
def caja(lines):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run('\n'.join(lines)); r.font.size = Pt(9.5); r.italic = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
def tabla(filas, anchos, fs=9.5):
    tb = doc.add_table(rows=len(filas), cols=len(filas[0])); tb.style = 'Table Grid'
    for i, fila in enumerate(filas):
        for j, v in enumerate(fila):
            c = tb.cell(i, j); c.width = Cm(anchos[j]); c.paragraphs[0].paragraph_format.space_after = Pt(0)
            r = c.paragraphs[0].add_run(v); r.font.size = Pt(fs)
            if i == 0: r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); shd(c, 'E54C09')
            elif j == 0: r.bold = True; shd(c, 'FFF8E7')
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('REFERIDOS — HOJA DE ARRANQUE'); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Para Juan Diego · Heiiu English Academy · del 15 al 30 de octubre de 2026 · Uso interno'); r.font.size = Pt(9); r.font.color.rgb = GRIS

sec('1. QUÉ VA A HACER')
t('Traer estudiantes nuevos por recomendación de los que ya están y de los que ya terminaron, y cerrarlos usted mismo. Quince días, con metas claras. No dicta clases durante el piloto: su tiempo es para esto.')
item('Pasar por TODOS los grupos activos entre el miércoles 15 y el viernes 17: 30 segundos al cierre de cada clase, con el profe titular presente (guion abajo). Sale de cada grupo con nombres y números.', '1.')
item('Llamar a TODOS los egresados entre el 15 y el 22 (guion abajo). Si no contestan, un mensaje y se reintenta al día siguiente.', '2.')
item('Contactar a cada referido el MISMO día que recibe el número, perfilarlo, llevarlo a una clase de prueba y a la asesoría, y cerrar la matrícula.', '3.')
item('Mensaje de 3 líneas todos los días a las 6:00 p.m. a gerencia: a quién le pidió hoy, cuántos referidos nuevos, citas agendadas. Y 5 líneas los lunes.', '4.')

sec('2. QUÉ GANA')
tabla([
 ['Si…', 'Programa completo de contado (' + m(4_782_800) + ')', 'A cuotas (' + m(5_648_000) + ')', 'Arranque A1+A2 (' + m(2_990_000) + ')'],
 ['Usted cierra la matrícula', '5% = ' + m(239_140), '5% de cada pago que entre (' + m(282_400) + ' al final)', '5% = ' + m(149_500)],
 ['La cierra la asesora (solo si venció su plazo)', '2% = ' + m(95_656), '2% de cada pago', '2% = ' + m(59_800)],
], [4.6, 4.4, 4.4, 3.8])
item('Siempre sobre la plata que entra a caja. Se liquida a fin de mes contra la planilla, con el retracto vencido. Si hay devolución, se descuenta.', 'Cómo se paga:')
item('Las primeras 2 matrículas las cierra con la asesora al lado: usted conduce y cobra su 5% completo. Desde la tercera, solo.', 'Arranque acompañado:')
item('Usted no cobra bono de estudiante. El bono es para quien refiere: ' + m(150_000) + ' (completo), ' + m(75_000) + ' (Arranque); en cuotas, mitad con la inicial y mitad con la cuota 3. Lo elige en plata, abono a su cuota o 2 horas 1-a-1. Se paga cuando el referido pagó la inicial y llegó a su clase 5.', 'El bono del que refiere:')

sec('3. CÓMO FUNCIONA')
t('El estudiante o el egresado le da el nombre y el número de su amigo, después de avisarle que Heiiu le va a escribir de su parte. Usted escribe primero (nunca llama en frío) y en ese mensaje le da la salida: si dice que no, se borra el número y no se insiste. Esa es la única regla que no se salta.', bold=True)
tabla([
 ['Paso', 'Qué pasa'],
 ['1', 'Ronda en el grupo o llamada al egresado. Sale con nombre y número de UNA persona por estudiante, y el estudiante le avisa a su amigo ese mismo día.'],
 ['2', 'Registra al referido en la planilla ANTES de escribirle: nombre, número, quién lo refiere, fecha.'],
 ['3', 'Le escribe ese mismo día desde la línea de referidos de Heiiu, con el mensaje de abajo: "[nombre] nos dio su número… ¿puedo llamarle 5 minutos?".'],
 ['4', 'Si responde SÍ o contesta la llamada, sigue. Si responde NO, lo borra y lo marca en la planilla. Si no responde en 24 horas, una llamada en horario legal; si tampoco, un último mensaje al tercer día y se cierra.'],
 ['5', 'Perfila: para qué necesita el inglés · desde cero o ya estudió (y qué pasó) · presencial y jornada · El Pacto ("¿se le mide a ese ritmo?") · contado o inicial del 20% y cuotas.'],
 ['6', 'Agenda la clase de prueba (con quien lo refirió, el día que diga coordinación) y la asesoría por llamada de WhatsApp. Presencial solo si él lo pide.'],
 ['7', 'Cierra con el tarifario oficial. El pago entra SOLO a la cuenta de Heiiu; contrato y recibo los hace coordinación en la sede.'],
], [1.2, 16.0])

sec('4. LAS REGLAS')
item('Solo desde la línea de referidos de Heiiu, nunca desde su celular. Las listas de estudiantes, egresados y referidos no salen de la planilla.', 'Canal:')
item('Precios, becas y planes oficiales, sin descuentos ni promesas (fácil, rápido, empleo, visa). Se dice lo duro antes de firmar: video diario, asistencia. Nunca recibe dinero. No firma nada en nombre de Heiiu.', 'Tarifario cerrado:')
item('Cita en 7 días y cierre en 14 desde el registro del referido. Si no, pasa a la asesora y usted queda con el 2%.', 'Plazos:')
item('Cero venta dentro del tiempo de clase. Lunes a viernes 7:00 a.m. a 7:00 p.m., sábados 8:00 a.m. a 3:00 p.m.; un contacto al día por persona; nunca domingos ni festivos. Si el referido escribe, se responde a cualquier hora.', 'Tiempo y horario:')
item('Cuenta el referido registrado en la planilla antes del primer contacto y que no estaba en la base en los últimos 30 días. No cuentan personal de Heiiu ni sus familiares. El bono no se usa como argumento ante el referido.', 'Qué cuenta:')

sec('5. LOS 15 DÍAS')
tabla([
 ['Cuándo', 'Qué', 'Meta al 30/10'],
 ['15 al 17/10', 'Ronda en todos los grupos', '15 referidos registrados y contactados (1 por día hábil)'],
 ['15 al 22/10', 'Todos los egresados, por llamada', '5 citas'],
 ['Todos los días', 'Contactar, perfilar, clase de prueba, cerrar · reporte 6:00 p.m.', '2 matrículas con inicial pagada'],
 ['30/10', 'Corte con gerencia: qué funcionó, qué sigue', 'Si no hay ni 5 referidos registrados, se corrige el guion y se repite'],
], [2.6, 8.2, 6.4])

sec('6. GUIONES')
t('Ronda de 30 segundos (al cierre de la clase):', bold=True, after=1)
caja(['"Treinta segundos antes de que se vayan. Ustedes saben lo que cuesta este proceso y saben que funciona.',
      'Piensen en UNA persona que necesite inglés de verdad: para el trabajo, para irse, para su hijo. ¿Ya la tienen?',
      'Hoy mismo me dan su nombre y su número, y le avisan que Heiiu le va a escribir de parte de ustedes.',
      'Si se matricula y llega a su clase 5, ustedes reciben $150.000, un abono a su cuota o 2 horas 1-a-1. Ustedes eligen.',
      'Y su amigo puede venir a una clase con ustedes antes de decidir. ¿Quién ya pensó en alguien? Me lo dicen ahora."'])
t('Llamada al egresado (2 minutos, en horario legal; si no contesta, el mensaje de abajo):', bold=True, after=1)
caja(['"Buenos días, [nombre], le habla Juan Diego, profesor de Heiiu. Usted terminó [nivel] con nosotros en [mes]. ¿Cómo le ha ido con el inglés?',
      'Le llamo por una sola cosa: abrimos un programa de referidos para egresados. Si usted conoce a alguien que necesite inglés de verdad',
      'y se matricula, usted recibe $150.000 o 2 horas de clase 1-a-1, y su amigo tiene una clase de prueba antes de decidir.',
      '¿En quién piensa? Deme su nombre y su número, y avísele hoy que le vamos a escribir de su parte."'])
t('Mensaje al egresado que no contestó:', bold=True, after=1)
caja(['Buenos días, [nombre], le habla Juan Diego, profesor de Heiiu. Usted terminó [nivel] con nosotros en [mes]. Abrimos un programa de',
      'referidos para egresados: si conoce a alguien que necesite inglés de verdad y se matricula, usted recibe $150.000 (o 2 horas de clase',
      '1-a-1), y su amigo tiene una clase de prueba antes de decidir. ¿Puedo llamarle 2 minutos hoy o mañana para contarle cómo funciona?'])
t('Primer mensaje al referido (desde la línea de Heiiu, el mismo día que recibe el número):', bold=True, after=1)
caja(['Buenos días, [nombre]. Le escribe Juan Diego, profesor de Heiiu English Academy, en Bucaramanga. [Nombre de quien refiere] nos dio su',
      'número y nos dijo que usted necesita el inglés para [motivo, si lo sabe]. ¿Puedo llamarle 5 minutos hoy para contarle cómo trabajamos?',
      'Si prefiere que no le escribamos, respóndame NO y borro su número de inmediato.'])
t('Con el SÍ o en la llamada: usaremos su nombre y su número solo para darle información de nuestros programas; puede pedir que lo borremos cuando quiera. Queda anotado en la planilla.', size=9.5, color=GRIS)

sec('7. PARA ARRANCAR MAÑANA')
for c in ['Contrato docente v3.1 y Anexo de Habilitación Comercial firmados (hoy).', 'Inducción con el Kit de Venta y el anexo del Pacto (hoy, 1 hora con gerencia).',
          'Celular con la línea de referidos de Heiiu y acceso a la planilla.', 'Lista de grupos activos con horarios y lista de egresados con teléfono (coordinación).', 'Días y grupos con cupo para la clase de prueba (coordinación).']:
    item(c, '☐')
doc.add_paragraph()
t('Leído y acordado, Bucaramanga, 15 de octubre de 2026.          Gerencia: ____________________          Docente: ____________________', size=9.5)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\HOJA_ARRANQUE_REFERIDOS_DOCENTE.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
