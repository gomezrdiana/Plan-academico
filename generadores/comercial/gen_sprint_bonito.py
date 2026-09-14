# -*- coding: utf-8 -*-
"""Sprint 20 Cupos + Mensajes del Sprint en formato de marca (mismo estilo de los kits)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NARANJA = RGBColor(0xE5, 0x4C, 0x09)
NEGRO = RGBColor(0x22, 0x22, 0x22)
GRIS = RGBColor(0x77, 0x77, 0x77)
CREMA = 'FFF8E7'
NARANJA_HEX = 'E54C09'
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL'


def nuevo_doc():
    doc = Document()
    for s in doc.sections:
        s.top_margin = Cm(1.6); s.bottom_margin = Cm(1.4); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
    doc.styles['Normal'].font.name = 'Calibri'
    doc.styles['Normal'].font.size = Pt(11.5)
    return doc


def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd'); el.set(qn('w:val'), 'clear'); el.set(qn('w:fill'), color)
    tcPr.append(el)


def make_helpers(doc):
    def titulo(txt, sub1=None, sub2=None):
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(txt); r.bold = True; r.font.size = Pt(20); r.font.color.rgb = NARANJA
        for s in (sub1, sub2):
            if s:
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(s); r.font.size = Pt(11); r.font.color.rgb = GRIS
        doc.add_paragraph()

    def seccion(txt):
        p = doc.add_paragraph()
        r = p.add_run(txt); r.bold = True; r.font.size = Pt(14.5); r.font.color.rgb = NARANJA
        p.paragraph_format.space_before = Pt(9); p.paragraph_format.space_after = Pt(4)

    def texto(txt, size=11.5, bold=False):
        p = doc.add_paragraph(); r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
        p.paragraph_format.space_after = Pt(4)
        return p

    def frase(txt, size=11.5):
        tab = doc.add_table(rows=1, cols=1); tab.style = 'Table Grid'
        c = tab.rows[0].cells[0]; shd(c, CREMA)
        for k, ln in enumerate(txt.split('\n')):
            p = c.paragraphs[0] if k == 0 else c.add_paragraph()
            r = p.add_run(ln); r.font.size = Pt(size)
        esp = doc.add_paragraph(); esp_r = esp.add_run(''); esp_r.font.size = Pt(4)
        esp.paragraph_format.space_after = Pt(0)

    def tabla(filas, fs=10.5):
        tab = doc.add_table(rows=len(filas), cols=len(filas[0])); tab.style = 'Table Grid'
        for i, fila in enumerate(filas):
            for j, val in enumerate(fila):
                c = tab.rows[i].cells[j]
                for k, ln in enumerate(str(val).split('\n')):
                    p = c.paragraphs[0] if k == 0 else c.add_paragraph()
                    r = p.add_run(ln); r.font.size = Pt(fs)
                    if i == 0:
                        r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                if i == 0:
                    shd(c, NARANJA_HEX)
        esp = doc.add_paragraph(); esp_r = esp.add_run(''); esp_r.font.size = Pt(4)
        esp.paragraph_format.space_after = Pt(0)

    return titulo, seccion, texto, frase, tabla


# ================== DOC 1: SPRINT ==================
doc = nuevo_doc()
titulo, seccion, texto, frase, tabla = make_helpers(doc)

titulo('SPRINT 20 CUPOS — 14 SEP → 5 OCT',
       'Plan de la asesora comercial · Acuerdo de ENTREGABLES',
       'Comisión: 20 Arranques ≈ $3.000.000')

seccion('LA MATEMÁTICA')
frase('40+ contactos salientes/día  →  5-6 citas agendadas  →  2-3 asistidas  →  1 matrícula/día hábil')
texto('Los leads NUEVOS que Meta trae cada día (el flujo) no alcanzan para eso. La mina es el STOCK: los cientos de conversaciones dormidas acumuladas en el bot durante meses + las listas de la academia. El sprint es minería de stock.')

seccion('LOS ENTREGABLES DE CADA DÍA HÁBIL (en el orden y horario que tú manejes)')
texto('1. 40 CONTACTOS SALIENTES del barrido, con comentario en el bot por cada uno: resultado + próximo paso. Todo contacto se registra con NOMBRE Y APELLIDO — hay muchos Andreas y Juanes.', bold=True)
texto('REGLA DE REGISTRO: lo que nace en el bot se comenta EN el bot; todo lo demás (colegios, empresas, grupos, LinkedIn, referidos) vive en la PLANILLA_SPRINT (hoja FUERA DEL BOT). El reporte de las 6 PM sale de las dos fuentes.')
texto('2. Leads nuevos: el bot los atiende al instante. La asesora revisa la bandeja del bot mínimo 3 VECES AL DÍA (mañana, mediodía y tarde) y toma manualmente toda conversación donde el lead preguntó algo que el bot no resolvió, pidió hablar con una persona, o quedó en silencio tras mostrar interés. Todas atendidas el mismo día hábil, antes del reporte.')
texto('3. Toda cita del día atendida + las de mañana confirmadas.')
texto('4. Reporte de las 6:00 PM por WhatsApp — se copia esta plantilla y se llenan los números:')
frase('REPORTE [día]\nContacté hoy a: [nombres Y APELLIDOS]\nTotal contactados: __\nCitas agendadas: __\nCitas asistidas: __\nCierres o abonos: __\nPlata que entró hoy: $ __')
texto('Así se ve lleno un día real:', bold=True)
frase('REPORTE lunes 14\nContacté hoy a: Andrea Gómez, Braulio Pérez, Carla Ruiz, Diego Mantilla, Estefanía León… (y sigue la lista)\nTotal contactados: 42\nCitas agendadas: 5\nCitas asistidas: 2\nCierres o abonos: 1 (abono de $300.000 — cupo separado)\nPlata que entró hoy: $300.000')

doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
seccion('EL BARRIDO (cómo se trabaja el stock sin filtros ni CRM)')
texto('El bot no tiene notas viejas ni segmentación — no importa. Regla única: de la conversación MÁS RECIENTE hacia atrás, Mensaje 1 a todo el mundo (está redactado para servir sin conocer la historia). La respuesta re-segmenta sola:')
texto('· Contesta interesado → cita con día y hora.')
texto('· Contesta que no → motivo real, comentario en el bot.')
texto('· No contesta → llamada a las +24h → último mensaje a las +48h → comentario y se sigue.')
texto('NO se filtra nada antes del barrido — se dispara a todos. Si el contactado resulta ser estudiante actual, pivote inmediato a referido: "¡Verdad que tú ya estás con nosotros! Entonces te tomo la palabra para otra cosa: ¿quién de tu círculo lleva años diciendo necesito el inglés? Mándame su nombre y número y lo atiendo de tu parte." Cada tope con un matriculado es un intento de referido gratis.', bold=True)

seccion('LOS OTROS CANALES (a medida que gerencia entrega cada lista)')
tabla([
 ['Canal', 'Cómo se trabaja'],
 ['EXALUMNOS A1/A2 que no siguieron\n(lista de recepción)', 'Mensaje variante hacia B2 con Fondo — NUNCA Arranque. Es la lista más valiosa: se trabaja apenas llegue.'],
 ['REFERIDOS — estudiantes y acudientes\n(lista de recepción)', 'Mensaje 2 a todos, una sola tanda. "Solicitud pre-presentada" = tú radicas la solicitud del referido ANTES de su cita. Es velocidad de proceso — NO cambia porcentajes de beca.'],
 ['OPERADORES Au Pair / W&T', 'Canal de GERENCIA — las alianzas las trabaja gerencia directamente. A ti te llegan las candidatas remitidas como leads normales: las atiendes con prioridad (vienen calientes y con meta clara — el Módulo Pasaporte es su cierre).'],
 ['EMPRESAS ALIADAS\n(Go Above and Beyond)', 'Canal de GERENCIA y el líder de alianzas (Business/Student Partner). A ti te llegan los empleados BECADOS de empresas aliadas como leads calientes — regla del mejor beneficio: si el becado califica a una beca superior del Fondo, se le aplica la mejor, nunca ambas.'],
 ['COLEGIOS\n(School Partner)', 'Las alianzas con colegios las abre GERENCIA. Tu rol: en cada TALLER DE PADRES capturas los datos en sala (nombre del padre, hijo, grado, teléfono) y AGENDAS CITAS ahí mismo a la salida. Después del taller: mensaje de gracias el mismo día + llamada a las 24h a los que no agendaron. Los registrados del taller son leads tuyos — entran a tu reporte como todo lo demás. Productos: 11° = Arranque de enero · 8°-10° = ruta sabatina (nivel individual, sin beca, descuento por forma de pago).'],
 ['REDES LOCALES\n(miércoles y sábado)', '4-5 publicaciones por tanda en grupos de Facebook de Bucaramanga (empleo, emprendedores, viajes, mamás) + 1 Marketplace + estado de WhatsApp diario. SIEMPRE con la pieza de video o imagen de pauta (las entrega gerencia) + el Mensaje 4.'],
 ['LINKEDIN\n(1 sesión semanal de 45 min)', 'Carril EJECUTIVO/B2B: 10 contactos por sesión a perfiles ejecutivos o de RRHH de empresas de Bucaramanga, con el Mensaje 5. LA VENTA ES TUYA de principio a fin (y tu comisión): tú agendas, tú presentas, tú cierras. Gerencia te acompaña en la primera reunión corporativa si la pides, y firma los convenios y precios B2B fuera de tabla.\n\nTU ESCALERA B2B (nunca abrir regalando): 1) La VENTA — formación pagada para ejecutivos/equipos, con factura. 2) Si no hay presupuesto pero hay interés → la ALIANZA sin costo (Business/Student Partner): ofrécela y entrega el contacto a gerencia — las cartas las envía el rol de alianzas, no tú. 3) No total → base con motivo. Ningún contacto se pierde: venta, alianza o motivo.'],
], fs=10)

seccion('VENCIMIENTOS (rutina desde el día 3)')
texto('Toda oferta que no cierra sale POR ESCRITO con vencimiento de 72 horas y se registra EL MISMO DÍA en la PLANILLA_SPRINT (hoja OFERTAS Y VENCIMIENTOS). Rutina diaria: filtrar la columna VENCE por HOY y llamarlas: "tu beca vence hoy a las 6 PM". Estado de cada una: VIGENTE, CERRÓ, VENCIÓ o RE-PRESENTADA — la fecha SE CUMPLE.')

seccion('METAS DE LA SEMANA (revisión cada viernes con gerencia)')
tabla([
 ['Métrica', 'Meta'],
 ['Contactos salientes (por nombre)', '200'],
 ['Citas agendadas', '25'],
 ['Citas asistidas', '12'],
 ['Matrículas o cupos separados con abono', '4-5'],
], fs=11)
texto('Termómetro: el contador de cupos (vendidos/20) se actualiza a diario en el tablero de la sede y el chat interno.', bold=True)

seccion('LAS 5 REGLAS DEL SPRINT')
texto('1. Toda conversación termina en cita con día y hora, o en NO con motivo anotado. Nada queda "en veremos".')
texto('2. Cierre doble SIEMPRE: completo primero (ancla), Arranque de red.')
texto('3. Precio de lanzamiento + contador de cupos en cada conversación — la urgencia es real.')
texto('4. Ningún descuento inventado: la única flexibilidad es la escrita (Fondo, 72h, abono $300.000).')
texto('5. Día sin reporte = día sin actividad verificable.')

doc.save(BASE + r'\SPRINT_20_CUPOS.docx')
print('OK sprint docx')

# ================== DOC 2: MENSAJES ==================
doc = nuevo_doc()
titulo, seccion, texto, frase, tabla = make_helpers(doc)

titulo('MENSAJES DEL SPRINT',
       'Copiar, personalizar nombre, enviar · Todo mensaje termina pidiendo la cita con DOS opciones de día/hora')

seccion('MENSAJE 1 — BASE MUERTA (el barrido del bot)')
frase('Hola [nombre] 👋 Soy [asesora] de Heiiu. Hace un tiempo hablamos de tu inglés y hoy te escribo con algo puntual: abrimos cohorte nueva el 5 DE OCTUBRE con precio de lanzamiento — los DOS primeros niveles completos (200 horas presenciales, libros y certificados incluidos) por $2.990.000, con garantía de aprendizaje POR ESCRITO. Son solo 20 cupos y ya se están asignando.\n\n¿Retomamos con una cita de 20 minutos? Tengo [día] a las [hora] o [día] a las [hora] — presencial o virtual.')

seccion('MENSAJE 1-B — EXALUMNOS de A1/A2 que no continuaron (a ellos NUNCA Arranque)')
frase('Hola [nombre] 👋 Soy [asesora] de Heiiu. Tu A1/A2 quedó ahí guardado — y el inglés que no se usa se oxida. Te escribo porque el Fondo de Becas tiene apertura para paquetes hacia B2 y tu caso aplica a evaluación: retomas donde quedaste y sales con tu B2 completo. ¿Te cuento los números de tu caso en una cita de 20 min? Tengo [día/hora] o [día/hora].')

seccion('MENSAJE 2 — REFERIDOS (estudiantes y acudientes actuales)')
frase('Hola [nombre] 👋 Te escribo de Heiiu con una buena para tu gente: abrimos cohorte nueva el 5 DE OCTUBRE — 20 cupos de lanzamiento, los dos primeros niveles completos por $2.990.000 con garantía por escrito.\n\n¿Quién de tu círculo lleva años diciendo "necesito el inglés" — un hermano, un amigo, alguien del trabajo? Mándame su nombre y número: entra con solicitud pre-presentada al Fondo de Becas y yo lo atiendo personalmente de tu parte. Los cupos son pocos y tu gente merece el empujón. 💪')
texto('NOTA INTERNA: "pre-presentada" = tú radicas la solicitud del referido antes de su cita, para que llegue con la evaluación iniciada. Es velocidad de proceso — NO cambia los porcentajes de beca. Jamás prometer % extra por ser referido.', 10.5, bold=True)

seccion('MENSAJE 3 — OPERADORES AU PAIR / W&T / H2B (este lo envía GERENCIA — no la asesora)')
frase('Buen día [nombre], le escribo de Heiiu English Academy — la academia aliada en Bucaramanga. Le cuento algo que les sirve a sus candidatas frenadas por el nivel de inglés: abrimos cohorte el 5 DE OCTUBRE (20 cupos), y nuestro programa termina con el MÓDULO PASAPORTE: la candidata sale con su video de presentación en inglés, su aplicación lista (hoja de vida + carta) y su entrevista con familia ENSAYADA y grabada, además del certificado internacional.\n\nEs decir: ustedes reciben candidatas listas para presentar, no candidatas a medio camino. ¿Hablamos 15 minutos esta semana para armar el flujo de remisión? ¿[día/hora] o [día/hora]?')

seccion('MENSAJE 4 — PUBLICACIÓN EN GRUPOS DE FACEBOOK / MARKETPLACE (miércoles y sábado)')
frase('🎯 BUCARAMANGA: ¿llevas años diciendo "necesito el inglés"? Abrimos cohorte el 5 DE OCTUBRE — los DOS primeros niveles COMPLETOS (200 horas presenciales, libros y certificado incluidos) por $2.990.000, con GARANTÍA DE APRENDIZAJE POR ESCRITO en tu contrato. Solo 20 cupos de lanzamiento y ya se están asignando. Al terminar sales con tu propia página web publicada o con tu aplicación lista para irte a trabajar afuera. Escríbeme al [número] y te cuento en 5 minutos. 🇺🇸')
texto('Se publica SIEMPRE con la pieza de video o la imagen de pauta (las entrega gerencia). Nunca texto solo.', 10.5, bold=True)

seccion('MENSAJE 5 — LINKEDIN (carril ejecutivo/B2B · la venta es tuya; convenios y precios B2B los firma gerencia)')
frase('Hola [nombre], vi tu perfil en [empresa]. Dirijo el área comercial de Heiiu English Academy en Bucaramanga — trabajamos inglés para perfiles ejecutivos y equipos: programas con certificación, avance medido con examen internacional y garantía de aprendizaje por escrito (única en la ciudad), con factura para la empresa. ¿Te interesaría una llamada de 15 minutos para ver si aplica para ti o tu equipo?')

seccion('LAS 4 REGLAS DE ENVÍO')
texto('1. Personalizar SIEMPRE el nombre — y si hay motivo anotado, abrir con él: "me contaste que en diciembre...".')
texto('2. Nunca más de un mensaje sin respuesta por día al mismo contacto. Ritmo: mensaje → +24h llamada → +48h último mensaje → comentario con motivo.')
texto('3. Palabras prohibidas de siempre: gratis, descuento, patrocinio, promesas de visa/empleo.')
texto('4. El que responde cualquier cosa recibe respuesta a SU pregunta primero, y luego las dos opciones de cita — igual que el bot.')

doc.save(BASE + r'\MENSAJES_SPRINT.docx')
print('OK mensajes docx')
