# -*- coding: utf-8 -*-
"""KIT DE VENTA HEIIU — manual bonito para asesoras: letra grande, colores de marca, lenguaje llano."""
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

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.8); s.bottom_margin = Cm(1.6); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(12)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd'); el.set(qn('w:val'), 'clear'); el.set(qn('w:fill'), color)
    tcPr.append(el)

def portada(txt_arriba, titulo, txt_abajo):
    for _ in range(6): doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(txt_arriba); r.font.size = Pt(14); r.font.color.rgb = GRIS
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(titulo); r.bold = True; r.font.size = Pt(34); r.font.color.rgb = NARANJA
    for linea in txt_abajo.split('|'):
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(linea.strip()); r.font.size = Pt(13); r.font.color.rgb = NEGRO
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

def seccion(num, txt):
    p = doc.add_paragraph()
    r = p.add_run(num + '  ' + txt); r.bold = True; r.font.size = Pt(20); r.font.color.rgb = NARANJA
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(8)

def sub(txt):
    p = doc.add_paragraph()
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(13.5); r.font.color.rgb = NEGRO
    p.paragraph_format.space_before = Pt(7); p.paragraph_format.space_after = Pt(3)

def texto(txt, size=12, bold=False):
    p = doc.add_paragraph(); r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    p.paragraph_format.space_after = Pt(3)
    return p

def frase(txt):
    tab = doc.add_table(rows=1, cols=1); tab.style = 'Table Grid'
    c = tab.rows[0].cells[0]; shd(c, CREMA)
    p = c.paragraphs[0]; r = p.add_run(txt); r.italic = True; r.font.size = Pt(12.5)
    esp = doc.add_paragraph(); esp.paragraph_format.space_after = Pt(0)
    esp.paragraph_format.space_before = Pt(0)
    for rr in esp.runs: pass
    esp_r = esp.add_run(''); esp_r.font.size = Pt(4)

def tabla(filas, anchos=None, header=True, fs=11.5):
    tab = doc.add_table(rows=len(filas), cols=len(filas[0])); tab.style = 'Table Grid'
    for i, fila in enumerate(filas):
        for j, val in enumerate(fila):
            c = tab.rows[i].cells[j]
            for k, ln in enumerate(str(val).split('\n')):
                p = c.paragraphs[0] if k == 0 else c.add_paragraph()
                r = p.add_run(ln)
                r.font.size = Pt(fs)
                if header and i == 0:
                    r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            if header and i == 0:
                shd(c, NARANJA_HEX)
    esp = doc.add_paragraph(); esp.paragraph_format.space_after = Pt(0)
    esp_r = esp.add_run(''); esp_r.font.size = Pt(4)

def salto():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

def link(p, url, txt):
    rid = p.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
    r = OxmlElement('w:r'); rPr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '0563C1'); rPr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rPr.append(u)
    b = OxmlElement('w:b'); rPr.append(b)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '26'); rPr.append(sz)
    r.append(rPr)
    t_el = OxmlElement('w:t'); t_el.text = txt; r.append(t_el)
    h.append(r); p._p.append(h)

# ============ PORTADA ============
portada('HEIIU ENGLISH ACADEMY · USO INTERNO', 'KIT DE VENTA', 'Manual de la Asesora Comercial · v2 consolidada, septiembre 2026 | Todo lo que necesitas para una cita completa está en este documento, incluidas las dudas resueltas del equipo.')

# ============ 1. LA CITA ============
seccion('1.', 'LA CITA: CÓMO SE CIERRA')

sub('La regla de oro')
texto('Una cita solo puede terminar de TRES maneras:', bold=True)
texto('1. Matriculado (o cupo separado con abono).')
texto('2. En lista de espera, con fecha.')
texto('3. Un NO claro — con el motivo anotado para rescate.')
texto('OJO: lista de espera exige un obstáculo REAL con FECHA ("me pagan la prima en diciembre", "mi grupo abre en enero") + recontacto agendado. El test: ¿puedo escribir una fecha al lado de este nombre? Sí = lista de espera. No = es un "lo voy a pensar" → se trabaja la objeción, y si no cierra, es la salida 3.', bold=True)
frase('"Lo voy a pensar" NO es una salida. El que sale a pensarlo, casi nunca vuelve.')

sub('La primera pregunta (siempre)')
frase('"¿Has estudiado inglés antes? ¿Puedes tener una conversación básica?"')
tabla([
 ['Si responde…', 'Entonces…'],
 ['"No, empiezo de cero" (la mayoría)', 'Cierre directo: ofrécele el ARRANQUE. Sin prueba en la cita — su evaluación de ingreso se agenda al matricular.'],
 ['"Ya sé algo" o pide la prueba', 'Se agenda la SESIÓN DE UBICACIÓN (ver sección 2) — ideal el mismo día — y se cierra con el nivel exacto en la mano. Cupo congelado con abono.'],
])

sub('Los dos productos (solo muestras DOS números por cliente)')
tabla([
 ['ARRANQUE A1+A2', 'PROGRAMA COMPLETO (A1 a B2)'],
 ['$2.990.000 — precio de lanzamiento, 20 cupos. Precio único: sin becas, sin estratos, sin preguntas.', 'Precio según su beca del Fondo (usa tu TARJETA DE BECAS, sección 3).'],
 ['Incluye: 2 niveles completos (200 horas), libros, certificado por nivel, garantía escrita y Módulo de Graduación al terminar A2 — a ELECCIÓN (ver abajo).', 'Incluye todo lo del Arranque + niveles B1 y B2 + al final: REFUERZO PRO (pitch avanzado, negociación real en inglés, video del antes y después).'],
])

sub('El Módulo de Graduación (incluido — se elige UNO al terminar A2, nunca ambos)')
frase('La pregunta que abre la elección: "¿Tu meta es montar algo tuyo, o irte a trabajar afuera? Tenemos módulo de graduación para cada una — tú eliges al terminar tu A2."')
tabla([
 ['MÓDULO EMPRENDEDOR', 'MÓDULO PASAPORTE'],
 ['Para el que quiere facturar: página web publicada con dominio propio · pitch en inglés · perfil para vender afuera · cuenta de pagos internacional · primer mensaje de venta enviado a un cliente real.', 'Para el que quiere irse (Au Pair, Work & Travel, H2B): video de presentación en inglés · hoja de vida + carta de aplicación · entrevista simulada con familia/empleador (grabada, antes y después) · certificado internacional EF SET · kit de llegada (aeropuerto, inmigración, primer día).'],
])
texto('Reglas: el precio es el MISMO elija el que elija — va incluido, no se cobra ni se descuenta. La elección es al terminar A2, no en la cita (en la cita solo se muestran los dos caminos). JAMÁS prometer visa, cupo en programa externo o empleo — el módulo entrega preparación y puertas verificadas. El interesado en irse se registra también para el carril de alianzas.', bold=True)

sub('Jornadas del ARRANQUE (cohorte del 5 de octubre · desde 17 años)')
texto('· Mañana 8:00 AM-12:00 PM (super intensivo) o Noche 6:30-8:30 PM. 20 cupos en TOTAL.')
texto('· La jornada NO se empuja: la definen el horario del cliente y su bolsillo — la mañana es super intensivo (máx 2 cuotas), la noche es intensivo (hasta 4 cuotas). La asesora solo INFORMA cómo van: "el grupo de la mañana ya va en [N]".', bold=True)
texto('· PREGUNTA OBLIGADA al registrar preferencia (suena a servicio, no a alarma): "¿Tu horario es fijo o tienes flexibilidad entre mañana y noche?" — se anota FLEXIBLE o SOLO MAÑANA / SOLO NOCHE. JAMÁS se le dice al cliente que su grupo "podría no abrir".')
texto('· Al de horario fijo se le vende SEGURIDAD, no riesgo (al firmar): "Tu cupo queda asegurado en TU jornada. Y tu plata está protegida siempre: si algo cambiara en la programación, tu precio queda congelado o te devolvemos tu abono completo — jamás te movemos de horario sin tu sí."')
texto('· Cada jornada abre con grupo mínimo (6) — ese dato es INTERNO: la consolidación la decide gerencia al cierre de cupos, viendo el tablero de flexibles. La asesora nunca gestiona eso en la cita.')
texto('· Y para ti: tu comisión se causa cuando el grupo ABRE y la plata entra — grupo que no abre = comisiones que no llegan. Tu juego es completar UN grupo rápido; el contador es tu cierre: "a la noche le faltan 2 para abrir — tu abono de hoy es el que la abre".', bold=True)

sub('El cierre doble (tu mejor jugada — las dos respuestas son SÍ)')
texto('SIEMPRE se presenta PRIMERO el programa completo (el ancla alta) y el Arranque de segundo (la red). El cierre doble ES la escalera: son los escalones 1 y 2 ofrecidos juntos — la escalera sigue aplicando si hay un NO a ambos.', bold=True)
frase('"Tienes dos caminos: te comprometes hoy con el programa completo — con tu beca queda en [tarjeta], sales con B2 y te ahorras más de un millón — o arrancas con A1+A2 por $2.990.000 y decides después. ¿Cuál te hago?"')
frase('"El Arranque monta tu negocio; el programa completo te enseña a DEFENDERLO en inglés."')

sub('La escalera de cierre — nadie sale sin que se le ofrezca el escalón siguiente')
texto('SIEMPRE se empieza ARRIBA. Solo se baja un escalón con un NO real YA TRABAJADO (objeción respondida y aun así no). Bajar sin ese no = regalar plata. Saltar escalones = perder ventas.', bold=True)
tabla([
 ['Escalón', 'Qué se ofrece', 'Se baja cuando…'],
 ['1', 'PROGRAMA COMPLETO con su beca del Fondo (número exacto: tabla en pesos, sección 3)', 'No real, ya respondido con plan de pagos y Fondo'],
 ['2', 'ARRANQUE A1+A2 — $2.990.000 (si empieza de cero) o el paquete menor hacia B2 (si ya tiene nivel)', 'No real trabajado'],
 ['3', 'NIVEL SUELTO (ej. solo A1: $1.596.000). Aquí — y SOLO aquí — tu única carta: hasta 20% de descuento por pago de contado, SOLO en cita presencial, JAMÁS por teléfono o WhatsApp', 'No real trabajado'],
 ['4', 'SABATINO — la entrada más económica (4h/semana, por nivel, sin beca)', 'No real trabajado'],
 ['5', 'NO es una venta, es una SIEMBRA: motivo REAL del no + teléfono, a la base de rescate — la tanda de rescate llama con el motivo en la mano', '—'],
], fs=10.5)
texto('Las dos trampas: (1) jamás ARRANCAR abajo — quien abre ofreciendo sabatino nunca vende un completo; (2) jamás bajar rápido — le enseñas al cliente que esperando consigue menos precio.', bold=True)

sub('Las 4 anclas (úsalas en TODA cita)')
texto('1. GARANTÍA: "Si cumples — asistencia, tareas, evaluaciones — y no muestras avance, te devolvemos el 100% del nivel. POR ESCRITO, en tu contrato."', 12)
texto('2. PRUEBA: "Tu avance no es una promesa: queda medido desde el día uno. Tú lo VES."', 12)
texto('3. CERTIFICACIÓN: "Institución con licencia desde 2012, programas registrados hasta 2032 y certificación de calidad ICONTEC."', 12)
texto('4. FORMACIÓN: "Aquí no solo aprendes inglés: cada clase abre trabajando una virtud — disciplina, prudencia, constancia — aterrizada en conductas concretas del aula." · Al papá: "le devolvemos un hijo más responsable — en inglés." · Al adulto: "la garantía existe porque el programa entrena los hábitos que te hacen cumplir."', 12)

sub('Al matricular: la frase del expediente (se dice SIEMPRE, antes de firmar)')
frase('"Tu garantía funciona con tu evidencia: desde el día uno grabas un audio de práctica de 1 a 3 minutos diarios, en tu celular — nadie de tu clase lo escucha. Ese portafolio es tu póliza: es lo que respalda tu garantía, y es donde TÚ mismo vas a oír tu cambio mes a mes. La garantía y el audio diario vienen juntos — se firman juntos."')
texto('Así el audio diario nace como parte del trato ANTES de firmar. El que firma la garantía firma su evidencia — nunca es sorpresa del profesor en la semana 2.', bold=True)

sub('Para cerrar (elige UNA frase y guarda silencio)')
texto('· "¿Arrancamos? Hoy quedas matriculado."')
texto('· "¿Te sirve más el grupo de la mañana o el de la noche?"')
texto('· "No estás arriesgando nada — la garantía está por escrito. ¿Qué te detiene?"')
texto('· "El precio de lanzamiento es por 20 cupos. ¿Cerramos?"')
frase('Después de la frase de cierre: SILENCIO. El primero que habla, concede.')

sub('Respuestas a objeciones')
tabla([
 ['Si dice…', 'Tú respondes…'],
 ['"Lo voy a pensar"', '"Claro. ¿Qué es exactamente lo que quieres pensar — el precio, el horario o el momento? Miremos ese punto ahora."'],
 ['"Debo consultarlo"', '"Perfecto. Separemos tu cupo hoy con el abono y confirmas mañana — así no pierdes el lanzamiento."'],
 ['"No tengo todo el dinero"', 'Plan de pagos con fechas exactas — o si aspira al programa completo, el Fondo de Becas.'],
 ['"¿Y si no aprendo?"', 'LA GARANTÍA, por escrito. (Es la mejor pregunta que te pueden hacer.)'],
 ['"En otra academia me dan el 65%"', '"¿Descuento sobre qué precio? Pregunta el precio FINAL: con matrícula, con libros, con todo. El nuestro es uno solo y está completo — y con garantía firmada."'],
 ['"Es muy caro" / "En Smart es más barato"', '"Hagamos la cuenta real: el programa completo son 575 horas presenciales — te sale a poco más de $10.000 la hora de clase real, con libros, certificado y garantía firmada incluidos. Pídele a cualquier otra academia el precio FINAL y divídelo por las horas que de verdad te dan. Ahí comparamos." (Solo si el cliente saca el precio — nunca abrir con esto.)'],
 ['"¿Tienen profes nativos?"', '"Nuestros profes son certificados y expertos en hispanohablantes: entienden exactamente tus errores. Y tu avance queda medido y garantizado por escrito — no depende de la nacionalidad de nadie."'],
 ['"Me quiero ir de Au Pair / niñera — no me interesa la página web"', '"¡Perfecto! Para irte el requisito #1 ES el inglés conversacional — este programa es tu pasaporte, y trabajamos solo con operadores VERIFICADOS de Au Pair. El módulo emprendedor viene incluido, no cuesta aparte y no es requisito: la mayoría vuelve al año con dólares ahorrados, y ahí ese módulo vale oro. Lo tienes ganado para cuando quieras." (El precio JAMÁS baja por no usar un componente — paquete no separable.)'],
])

sub('Lo que JAMÁS se hace')
texto('· La palabra "patrocinio" no existe: se dice BECA DEL FONDO.')
texto('· La tarjeta de becas no se muestra al cliente — se le dice SU resultado.')
texto('· No se promete: empleo, visa, "bilingüe en X meses", ni nada que no esté por escrito.')
texto('· No se dice "gratis" ni "descuento".')
texto('· Toda matrícula sale con el kit completo firmado, con huellas, y copia para el estudiante.')

salto()
# ============ 2. LA PRUEBA ============
seccion('2.', 'LA PRUEBA DE UBICACIÓN')
frase('Se le dice así: "Esta prueba NO se aprueba ni se pierde — solo nos dice tu punto de partida, para que no pagues ni una clase de más ni de menos."')

texto('Regla nueva: el que "ya sabe algo" tiene su resultado COMPLETO antes de matricularse o decidir — así el contrato nace con el nivel exacto y nunca hay devoluciones ni cobros sorpresa.', bold=True)

sub('LA SESIÓN DE UBICACIÓN (~1 hora, por videollamada, ANTES de decidir)')
texto('Se agenda desde la cita, lo antes posible — ideal el mismo día: "¿Tienes 50 minutos ahora saliendo de aquí, o esta tarde?". Para congelar el cupo y el precio de lanzamiento mientras tanto: abono de separación (ej. $300.000, se cruza con la matrícula).')
p = texto('1. El prospecto hace el examen internacional EF SET de 50 minutos (gratis y ADAPTATIVO: ajusta la dificultad al nivel — no maltrata a nadie), desde su casa. Enlace: ')
link(p, 'https://efset.org/ef-set-50/', 'efset.org/ef-set-50')
texto('2. TODO el examen en videollamada supervisada: CÁMARA PRENDIDA y PANTALLA COMPARTIDA. (Varios prospectos pueden hacerlo a la vez en una misma videollamada, cámaras prendidas, micrófonos apagados.)')
texto('3. Reglas de pantalla (la página está en inglés): el botón grande siempre avanza; al inicio hay prueba de sonido ("Continue" = continuar); y AVISA ANTES de arrancar: "al final te pide nombre, teléfono, correo y año de nacimiento — llénalos de una, sin pausa, o se cierra la sesión".')
texto('4. COORDINA CON EL PROFE DESDE ANTES: apenas termina el test, el profe entra a la MISMA videollamada y hace la mini-oral de 5 minutos (abajo). Todo queda resuelto en una sola sesión.')
texto('5. Con los dos resultados, la asesora llama a cerrar EL MISMO DÍA: "ya tienes tu nivel exacto — tu programa queda en $X. ¿Firmamos?".')

sub('La mini-oral de 5 minutos (la aplica UN PROFE, apenas termina el test)')
texto('El profe pregunta en orden y se detiene cuando el cliente ya no responde con soltura:')
tabla([
 ['Nivel', 'Pregunta del profe', 'Qué se espera oír'],
 ['A1', 'What is your name? Where do you live?', 'Frases simples completas'],
 ['A2', 'What did you do yesterday?', 'Usa el pasado sin trabarse'],
 ['B1', 'Tell me about a difficult situation and how you solved it.', 'Narra y se defiende, aunque con errores'],
 ['B2', 'If you could change one thing about your city, what would it be?', 'Opina y fluye con naturalidad'],
])
frase('REGLA CLAVE: entre el test de 50 minutos y la oral, MANDA LA MENOR. El que lee bien pero habla A2, se ubica por lo que HABLA: "vamos a asegurar tu base — subir de grupo siempre se puede, y la reubicación no te cuesta nada".')

texto('El EF SET de la sesión queda guardado en la carpeta del prospecto: cuando se matricula, ese MISMO resultado es la línea base FIRMADA de su garantía — no se repite. Si el prospecto no tiene equipo en casa: se le agenda el computador de la sede.', bold=True)

sub('¿Y el que empieza de cero?')
texto('Cierre directo en la cita, sin ninguna prueba antes (no hay riesgo de paquete equivocado: arranca en A1). Su EF SET de 50 minutos lo hace AL MATRICULAR, antes de la primera clase, con el mismo protocolo de videollamada supervisada — esa es su línea base de la garantía. También sirve la sesión grupal.')

sub('Con la ubicación, qué se ofrece')
tabla([
 ['Su ubicación', 'Le ofreces'],
 ['Cero / A1', 'ARRANQUE A1+A2 ($2.990.000) — cierre directo'],
 ['A2', 'Paquete B1 a B2 con Fondo de Becas (tarjeta)'],
 ['B1', 'Solo B2 con Fondo — SIEMPRE con la sesión de ubicación completa antes de firmar'],
 ['B2 confirmado', 'Clases personalizadas / conversación avanzada — se agenda cita con gerencia. JAMÁS venderle un nivel que ya tiene'],
])

salto()
# ============ 3. LAS BECAS ============
seccion('3.', 'LA TARJETA DE BECAS DEL FONDO')
frase('Esta tabla es INTERNA: nunca se muestra ni se fotografía. Al cliente se le dice SU resultado.')

sub('Las 2 preguntas (en este orden)')
texto('1. ¿QUIÉN es? — define su columna:', bold=True)
texto('· Estrato 1-2 o SISBÉN (con soporte): TRANSFORMACIÓN — cupos limitados por trimestre.')
texto('· Todos los demás: GENERAL.')
texto('· Ejecutivo / paga su empresa: EJECUTIVO.')
texto('2. ¿QUÉ compra y CÓMO paga? — define su fila.', bold=True)

sub('La matriz (beca sobre el precio del paquete — solo buscar, no calcular)')
tabla([
 ['Compra', 'TRANSFORMACIÓN (contado/cuotas)', 'GENERAL (contado/cuotas)', 'EJECUTIVO (contado/cuotas)'],
 ['A1 a B2 completo', '45% / 36%', '32% / 25,6%', '15% / 12%'],
 ['A2 a B2', '36% / 27%', '25,6% / 19,2%', '12% / 9%'],
 ['B1 a B2', '24,8% / 15,8%', '17,6% / 11,2%', '8,3% / 5,3%'],
 ['Solo B2', '20,3% / 11,3%', '14,4% / 8%', '6,8% / 3,8%'],
 ['Nivel suelto / sabatino', 'SIN BECA', 'SIN BECA', 'SIN BECA'],
])
texto('Ejemplo: estrato 3 quiere A2→B2 en cuotas → columna GENERAL, fila A2→B2, cuotas → 19,2%.')
texto('Niveles sueltos: SIN beca del Fondo — aplican descuento por forma de pago (contado 20% · cuotas 10% + interés · Cajasan 30%). El sabatino solo se vende por nivel suelto.')

# ---- tablas calculadas (matriz hibrida en pesos) ----
FULL = {'A1 a B2 completo': 8696000, 'A2 a B2': 7100000, 'B1 a B2': 5185000, 'Solo B2': 2343000}
PCT = {
 'A1 a B2 completo': {'T': (45, 36), 'G': (32, 25.6), 'E': (15, 12)},
 'A2 a B2':          {'T': (36, 27), 'G': (25.6, 19.2), 'E': (12, 9)},
 'B1 a B2':          {'T': (24.8, 15.8), 'G': (17.6, 11.2), 'E': (8.3, 5.3)},
 'Solo B2':          {'T': (20.3, 11.3), 'G': (14.4, 8), 'E': (6.8, 3.8)},
}
NMAX = {'A1 a B2 completo': 11, 'A2 a B2': 11, 'B1 a B2': 8, 'Solo B2': 4}
def peso(x): return '$' + format(int(round(x)), ',').replace(',', '.')
def cuota_m(saldo, n): return saldo * 0.019 / (1 - 1.019 ** -n)

salto()
sub('La tabla en PESOS (buscar la celda y decir el número — NO calcular)')
filas = [['Compra (precio full)', 'TRANSFORMACIÓN', 'GENERAL', 'EJECUTIVO']]
for paq in FULL:
    fila = [paq + '\nfull ' + peso(FULL[paq])]
    for per in ('T', 'G', 'E'):
        c, q = PCT[paq][per]
        fila.append('Contado ' + peso(FULL[paq]*(1-c/100)) + '\nCuotas ' + peso(FULL[paq]*(1-q/100)))
    filas.append(fila)
tabla(filas)
texto('El precio full NUNCA cambia — la beca lo baja según la celda. "Cuotas" es el precio BASE si paga a cuotas; los intereses del crédito directo van aparte (abajo).')

sub('CAJASAN: se pregunta SIEMPRE, se registra SIEMPRE')
texto('En TODA cita: "¿Eres afiliado a Cajasan?" — y se anota en su ficha, pague de contado o a cuotas: el reporte de afiliados atendidos es lo que mantiene viva la alianza (única academia de inglés con este convenio).', bold=True)
texto('BENEFICIO DEL CONVENIO: el afiliado que paga a cuotas recibe la beca de CONTADO de su perfil (empleado formal = menos riesgo, el Fondo le sostiene el % pleno). Se verifica con carné o certificado de afiliación.')
texto('JAMÁS se le envía a pedir crédito o libranza a Cajasan: tienen su propio programa de inglés — no les hacemos publicidad.', bold=True)

sub('Cómo se paga (ofrecer EN ESTE ORDEN — Heiiu evita financiar directo)')
texto('1. CONTADO (la mejor beca): transferencia, tarjeta débito, o efectivo ÚNICAMENTE en la sede con recibo.')
texto('2. CESANTÍAS: el cheque de cesantías cuenta como pago de CONTADO (aplica la beca de contado). Abono de separación de $300.000 hoy congela cupo y precio; el cheque debe entregarse dentro de los 10 días hábiles siguientes y siempre antes del inicio de clases.')
texto('3. CRÉDITO DE UN TERCERO (Comultrasan, banco, financiera): también cuenta como CONTADO — a la academia le entra el 100% y el cliente le debe a la entidad. Misma regla: abono de $300.000 hoy, desembolso completo en máximo 10 días hábiles. Si el crédito es negado o no llega a tiempo, el cliente paga por otro medio a la tarifa que corresponda, o su abono queda como saldo a favor (nunca devolución en efectivo).')
texto('4. TARJETA DE CRÉDITO del cliente: cuenta como pago de contado y él difiere con su banco, PERO el valor a pagar aumenta 5% por el costo del uso de la tarjeta. Se dice antes de pasarla, siempre: "por tarjeta de crédito el valor sube un 5% por el costo de la transacción — por transferencia o débito no tiene ese recargo."', bold=True)
texto('5. CRÉDITO DIRECTO HEIIU — ÚLTIMO recurso, solo si nada de lo anterior aplica: beca de cuotas (o de contado si es afiliado Cajasan) + interés del 1,9% mensual sobre saldo. Separación de cupo $300.000 (se cruza con la inicial) → cuota inicial (mínimo 20%) máximo a 3 días → cuotas mensuales desde el día 30. SIEMPRE con pagaré + carta de instrucciones + anexo plan de pagos firmados — sin firmas no hay crédito.', bold=True)

sub('Si toca crédito directo: la cuota tipo (inicial 20% + el máximo de cuotas)')
filas = [['Compra', 'TRANSFORMACIÓN', 'GENERAL', 'EJECUTIVO']]
for paq in FULL:
    n = NMAX[paq]
    fila = [paq + '\n(' + str(n) + ' cuotas máx)']
    for per in ('T', 'G', 'E'):
        base = FULL[paq]*(1-PCT[paq][per][1]/100)
        fila.append('Inicial ' + peso(base*0.20) + '\n+ ' + str(n) + ' de ' + peso(cuota_m(base*0.80, n)))
    filas.append(fila)
tabla(filas)
texto('REGLA DEL CRÉDITO: el estudiante termina de PAGAR antes de terminar el programa — por eso el máximo de cuotas depende de la modalidad.', bold=True)
texto('· La tabla de arriba usa los máximos del INTENSIVO (10h/semana): completo ~14 meses, A2→B2 ~12, B1→B2 ~9, Solo B2 ~5.')
texto('· En SUPER INTENSIVO (20h/semana) el programa dura la mitad y las cuotas bajan: completo y A2→B2 máximo 5 cuotas · B1→B2 máximo 3 · Solo B2 prácticamente de contado.')
texto('Para otra cuota inicial u otro número de cuotas: MOTOR_CUOTAS_FONDO_2026.xlsx (interno) — nunca calcular a mano frente al cliente.')

sub('¿Y el ARRANQUE ($2.990.000)? Sin becas — pero misma escalera de pago')
texto('Contado o tarjeta: igual que arriba. Si toca crédito directo (1,9% mensual, separación $300.000 → inicial mín 20% a 3 días → cuotas desde día 30), el tope de cuotas sale de la duración (200 horas):')
tabla([
 ['Modalidad', 'Dura', 'Máx cuotas', 'Cuota tipo (inicial 20% = $598.000)'],
 ['Super intensivo 20h/sem', '~2,5 meses', '2', '2 cuotas de $1.230.193'],
 ['Intensivo 10h/sem', '~5 meses', '4', '4 cuotas de $626.672'],
])
texto('Con inicial del 50% ($1.495.000) el intensivo baja a 4 cuotas de $391.670. Otros escenarios: hoja ARRANQUE del motor de cuotas.')

sub('Vigencia de la oferta (el "voy a buscar la plata")')
texto('· Toda beca aprobada sale POR ESCRITO (WhatsApp) con vencimiento: 72 HORAS. "Tu beca quedó aprobada por el Fondo hasta el [día] a las 6 PM."')
texto('· Con abono de separación ($300.000): cupo + precio CONGELADOS 7 días calendario. El abono es lo que compra tiempo.')
texto('· Sin abono, a las 72 horas la beca VENCE y vuelve al Fondo. Se puede volver a presentar la solicitud, pero sin garantizar el mismo porcentaje ni el cupo.')
texto('· Seguimiento pautado (no esperar a ver si vuelve): mismo día resumen escrito con número y vencimiento → +24h mensaje → +48h llamada → día 3: "vence hoy".')
texto('LA FECHA SE CUMPLE. Si venció, venció: la re-presentación de la solicitud es real, no teatro. Una sola excepción conocida y el Fondo pierde toda su fuerza — el cliente se da cuenta.', bold=True)
frase('El escudo de la asesora: "Yo no puedo extenderla — el Fondo audita las fechas."')

sub('El guion del Fondo (tal cual)')
frase('"Heiiu tiene un Fondo de Becas institucional, administrado por contaduría. Yo no decido las becas — yo presento tu solicitud y el Fondo la evalúa."')
frase('Si regatea: "No puedo tocar el porcentaje — el Fondo se audita y una excepción lo tumba para todas las familias. Lo que sí puedo hacer es presentar bien tu caso."')
texto('Al aprobar una beca: SIEMPRE se entrega carta impresa + reglamento.', bold=True)
frase('La lógica, por si preguntan: "Entre más necesitas, más alto tu techo. Entre más te comprometes, más del techo te ganas."')

salto()
# ============ 4. CHECKLIST ============
seccion('4.', 'LO QUE SE DICE SIEMPRE — CHECKLIST DE TODA CITA')
texto('Estas 10 cosas son OBLIGATORIAS en toda cita, en este orden natural. Al terminar cada cita, repásalas: si faltó una, se dice en el seguimiento del mismo día.', bold=True)
texto('□ 1. LA PREGUNTA DE NIVEL: "¿Has estudiado inglés antes? ¿Puedes tener una conversación básica?" — define todo el camino.')
texto('□ 2. LA PREGUNTA CAJASAN: "¿Eres afiliado a Cajasan?" — se pregunta y se ANOTA siempre, pague como pague.')
texto('□ 3. LAS 4 ANCLAS: garantía por escrito · avance medido · institución con licencia e ICONTEC · formación del carácter.')
texto('□ 4. LA PREGUNTA DE LA META: "¿Tu meta es montar algo tuyo, o irte a trabajar afuera?" — presenta los dos módulos de graduación.')
texto('□ 5. EL CIERRE DOBLE: los dos caminos (Arranque $2.990.000 o completo con beca) — las dos respuestas son SÍ.')
texto('□ 6. SI "YA SABE ALGO": sesión de ubicación agendada con FECHA Y HORA antes de que se vaya — jamás se va sin agenda.')
texto('□ 7. SI ES ARRANQUE: las dos jornadas + la regla del grupo mínimo, ANTES de firmar — nunca de sorpresa.')
texto('□ 8. LA FRASE DEL EXPEDIENTE (antes de firmar): la garantía y el audio diario vienen juntos — se firman juntos.')
texto('□ 9. UNA frase de cierre + SILENCIO. El primero que habla, concede.')
texto('□ 10. SI NO CIERRA HOY: la oferta POR ESCRITO con vencimiento (72 horas) + el abono de separación ofrecido + el motivo real anotado para rescate.')
frase('Cita perfecta = las 10 marcadas. Cita sin cierre pero con las 10 = trabajo bien hecho, el seguimiento la remata. Cita con cierre pero sin la 2, la 7 o la 8 = problema futuro: complétalas en la firma.')

salto()
# ============ 5. DUDAS RESUELTAS ============
seccion('5.', 'DUDAS RESUELTAS — DOCTRINA OFICIAL')
texto('Estas son las dudas que ya preguntó el equipo y su respuesta oficial. Si tu duda no está aquí, se pregunta a gerencia y la respuesta entra a este kit.', bold=True)

sub('1. ¿Cuándo es GENERAL y cuándo EJECUTIVO?')
texto('El test es uno solo: ¿QUIÉN PAGA LA FACTURA? Paga una empresa, o pide factura a nombre de empresa o reembolso corporativo → EJECUTIVO (techo 15%). Persona natural que paga de su bolsillo → GENERAL (techo 32%), sin importar su cargo, su ropa o su carro. Estrato 1-2 o SISBÉN con soporte → TRANSFORMACIÓN (techo 45%).')
texto('Nunca se clasifica por pinta ni por cargo: se clasifica por la factura. Y al Ejecutivo no se le vende beca — se le vende conveniencia: certificación, garantía firmada, factura para su empresa, avance medido. Su 15% es un gesto, no el argumento.', bold=True)

sub('2. Empleado de empresa aliada (Go Above and Beyond): ¿qué beca le aplica?')
texto('Mismo test, más un dato: ¿cuánto gana? · La empresa paga la factura → EJECUTIVO 15%. · El empleado paga de su bolsillo Y gana hasta 1.5 SMMLV → con carta de su empresa aliada + desprendible de nómina → TRANSFORMACIÓN 45%, dentro de los cupos del Fondo. · Gana más de 1.5 SMMLV y paga de su bolsillo → GENERAL 32% + beneficio de convenio (paga a cuotas con el porcentaje de contado).')
texto('El ARRANQUE no tiene becas: precio único $2.990.000 para todos, aliados incluidos. Los beneficios nunca se acumulan: se aplica el mejor.', bold=True)

sub('3. ¿La comisión aplica a ventas corporativas?')
texto('Sí. La venta es la venta, venga de donde venga: mismo esquema para una matrícula individual, un Arranque, un becado de empresa aliada o un contrato corporativo. Sin recaudo no hay comisión — cobrar también es vender.')

sub('4. ¿Qué se dice del contador cuando no se ha vendido nada?')
texto('Jamás "quedan 20 de 20": eso anuncia que nadie ha comprado. El contador tiene tres etapas y las tres son verdad: · 0 vendidos → "Acaban de abrirse los 20 cupos del lanzamiento." · 1 a 4 → "Los cupos ya se están asignando." · 5 o más → el número real: "Vamos 8 de 20."')
texto('La regla que no cambia: jamás inventar el número.', bold=True)

sub('5. EL PACTO: la verdad que se dice ANTES de firmar')
texto('Para TODOS: jamás prometer fácil, rápido ni divertido. Se promete el método, el respaldo y la garantía — a cambio del trabajo del estudiante.', bold=True)
texto('La charla completa es solo para el cliente QUEMADO, el que ya intentó y fracasó (se detecta con "¿has estudiado inglés antes? ¿cómo te fue?"). Al que llega limpio no se le receta un trauma que no tiene.')
frase('"Te voy a ser honesta: esto NO es fácil. Vas a tener días de no querer venir, tareas que fastidian, audios que te van a dar pena grabar. El inglés no se aprende suave: se entrena, como un deporte. Y si llevas años intentándolo y no has podido, el problema nunca fuiste tú — fue el método. Aquí es al revés: de pie, hablando desde el día uno. Por eso somos los únicos que firmamos garantía: si TÚ pones el trabajo, y no avanzas, te devolvemos la plata. Ese es el trato."')
texto('Por qué así: el que firma advertido no deserta en la semana 3 ni pide devolución; la dureza honesta hace creíble la garantía; y filtra al comprador correcto.')

sub('6. ¿El afiliado a Cajasan recibe el 45%?')
texto('No por ser de Cajasan. El 45% lo da el PERFIL (Transformación, con soporte). Cajasan mejora la FORMA DE PAGO: el afiliado que paga a cuotas recibe el porcentaje de contado de su propio perfil.')
frase('"Cajasan no cambia quién eres — cambia cómo pagas: siempre al precio de contado de tu perfil."')

sub('7. "Te doy un abono, pero necesito el crédito de la cooperativa"')
texto('El crédito de un tercero y el cheque de cesantías cuentan como contado (sección 3, escalera de pago): abono de $300.000 hoy congela cupo y precio, desembolso completo en máximo 10 días hábiles y siempre antes del inicio de clases. Si no llega a tiempo o es negado: paga por otro medio a la tarifa que corresponda, o su abono queda como saldo a favor para cualquier programa. Nunca devolución en efectivo.')

sub('8. ¿Se puede matricular a alguien sin que venga a la sede?')
texto('La matrícula tiene DOS momentos, y solo el primero es digital:')
texto('· SEPARACIÓN (100% digital): abono a las cuentas de la academia + el cliente acepta por escrito el recibo de separación ("ACEPTO las condiciones del recibo No. X", con foto de su cédula) + se agenda en el mismo acto su sesión de ubicación. Eso congela cupo y precio, y tiene plena validez legal.')
texto('· FORMALIZACIÓN (siempre en la sede): contrato de matrícula firmado en físico, a más tardar el día de la sesión de ubicación. El efectivo solo se recibe en la sede, con recibo.')
frase('El chat asegura el cupo; la sede firma el contrato.')

sub('9. La planilla: si no aparecen las listas desplegables')
texto('La flecha solo aparece al hacer clic EN la celda. Y si el archivo llegó por WhatsApp o descarga, Excel lo abre en "Vista protegida": hay que darle a "Habilitar edición" para que las listas funcionen.')

doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Heiiu English Academy · Kit de Venta · Se aprende, se practica en voz alta, se ejecuta.'); r.font.size = Pt(10); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\KIT_DE_VENTA_ASESORAS.docx'
doc.save(out); print('OK', out)
