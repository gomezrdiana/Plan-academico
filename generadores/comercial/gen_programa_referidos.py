# -*- coding: utf-8 -*-
"""Programa de referidos — VERSIÓN FINAL (14/10/2026). Reemplaza la propuesta para análisis del 12/10.
Decisiones de gerencia 14/10: Opción B ajustada con la investigación (INVESTIGACION_REFERIDOS_2026-10-14.md);
docente recolector-cerrador (sin grupo a cargo); base = estudiantes activos (~60) + egresados; clase de prueba sí;
tratamiento tributario del bono = pregunta al contador. Documento por ROLES (sin nombres).
Encaja con lo ya firmado/redactado: contrato docente v3.1 cl. 2(b) (referido 2% si cierra el equipo comercial),
ANEXO_HABILITACION_COMERCIAL_DOCENTE_v1 (lead de la casa cerrado por el docente 5%) y contrato de la asesora (5%).
Salida: recursos/comercial/PROGRAMA_REFERIDOS_PROPUESTA_2026-10.docx"""
import re
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_BREAK

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
m = lambda v: f'${v:,.0f}'.replace(',', '.')
pct = lambda v, base: f'{v / base * 100:.1f}%'.replace('.', ',')
CONTADO = 4_782_800; CUOTAS = 5_648_000; ARRANQUE = 2_990_000
LEAD = 10_800; CONV = 0.15; META_X_MATRICULA = round(LEAD / CONV)   # ≈ $72.000 de pauta por matrícula (dato interno 08/10)
BONO = {'c': 150_000, 'q': (75_000, 75_000), 'a': 75_000}
ACOMP = 50_000   # fijo a la asesora por cada cierre acompañado (máx. 3)

d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(54); s.top_margin = s.bottom_margin = Pt(46)
def h(t, size=13):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(9); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAR
def p(t, color=None, size=10.5, after=4):
    x = d.add_paragraph(); x.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        r = x.add_run(part[2:-2] if part.startswith('**') else part); r.bold = part.startswith('**'); r.font.size = Pt(size)
        if color: r.font.color.rgb = color
def li(t): p('•  ' + t, after=2)
def caja(lines):
    for l in lines:
        x = d.add_paragraph(); x.paragraph_format.space_after = Pt(0); x.paragraph_format.left_indent = Pt(18)
        r = x.add_run(l); r.font.name = 'Consolas'; r.font.size = Pt(9.5)
    d.add_paragraph().paragraph_format.space_after = Pt(2)
def tabla(rows, bold_rows=()):
    t = d.add_table(rows=1, cols=len(rows[0])); t.style = 'Table Grid'
    for j, v in enumerate(rows[0]):
        r = t.rows[0].cells[j].paragraphs[0].add_run(v); r.bold = True; r.font.size = Pt(9.5)
    for i, row in enumerate(rows[1:]):
        c = t.add_row().cells
        for j, v in enumerate(row):
            r = c[j].paragraphs[0].add_run(v); r.font.size = Pt(9.5); r.bold = (j == 0) or (i in bold_rows)
    d.add_paragraph().paragraph_format.space_after = Pt(2)
def salto(): d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

p('HEIIU · COMERCIAL · DOCUMENTO INTERNO', GRIS, 10)
p('PROGRAMA DE REFERIDOS — VERSIÓN FINAL (14/10/2026)', NAR, 15)
p('Roles: estudiante o egresado que refiere · docente recolector-cerrador (sin grupo a cargo durante el piloto de 15 días) · asesora comercial · coordinación · gerencia. Reemplaza la propuesta del 12/10. Base: investigación del 14/10 (evidencia y fuentes en INVESTIGACION_REFERIDOS_2026-10-14.md).', GRIS, 9.5)

h('0. Decisiones tomadas (gerencia, 14/10)')
for t in [
 '**Opción B**, con los ajustes de la investigación. La Opción A ($200.000 + fijo) se descarta: cae en el rango donde el bono alto trae referidos menos rentables.',
 '**El docente recolecta Y cierra** sus referidos. Recolecta en todos los grupos activos y llama a los egresados. Cobra por comisión, con los papeles firmados antes del primer mensaje (sección 6).',
 '**Piloto de 15 días: del 15 al 30 de octubre.** No hay ventas en octubre; esto arranca ya. El 30 se mide y se decide si sigue igual, cambia o para.',
 '**Base:** unos 60 estudiantes activos más los egresados (cantidad SIN DATO: coordinación entrega la lista).',
 '**El referido recibe una clase de prueba** junto a quien lo refiere (o solo, si quien lo refiere es egresado). Nunca descuento.',
 '**Contador:** antes del primer pago del bono se le hacen las preguntas de la sección 8.',
]: li(t)

h('1. Qué recibe cada quien')
p('Todo sobre recaudo efectivo a caja. Los porcentajes del docente son los que ya dicen su contrato v3.1 (cláusula 2b: referido cerrado por el equipo comercial, 2%) y el Anexo de Habilitación Comercial (lead de la casa cerrado por el docente, 5%). **Los referidos del programa son leads de la casa**, no canal propio: salen de la base de Heiiu, no de la red personal del docente. No hay fijo al docente: el fijo de $80.000 de la propuesta anterior lo reemplaza el 2% de su contrato, que ya está firmado.')
tabla([
 ['Quién recibe', 'Completo DE CONTADO (' + m(CONTADO) + ')', 'Completo A CUOTAS (' + m(CUOTAS) + ')', 'Arranque A1+A2 (' + m(ARRANQUE) + ')'],
 ['Estudiante o egresado que refiere (bono)', m(BONO['c']) + ' (' + pct(BONO['c'], CONTADO) + ')', m(BONO['q'][0]) + ' con la inicial + ' + m(BONO['q'][1]) + ' con la cuota 3', m(BONO['a']) + ' (' + pct(BONO['a'], ARRANQUE) + ')'],
 ['Docente, si ÉL cierra (5%, anexo de habilitación)', m(round(CONTADO * .05)), '5% de cada pago (' + m(round(CUOTAS * .05)) + ' al final)', m(round(ARRANQUE * .05))],
 ['Docente, si cierra la asesora (2%, contrato)', m(round(CONTADO * .02)), '2% de cada pago (' + m(round(CUOTAS * .02)) + ')', m(round(ARRANQUE * .02))],
 ['Asesora, si cierra un lead del docente (5%, su contrato)', m(round(CONTADO * .05)), '5% de cada pago (' + m(round(CUOTAS * .05)) + ')', m(round(ARRANQUE * .05))],
 ['TOTAL si cierra el docente', m(BONO['c'] + round(CONTADO * .05)) + ' (' + pct(BONO['c'] + CONTADO * .05, CONTADO) + ')', m(sum(BONO['q']) + round(CUOTAS * .05)) + ' (' + pct(sum(BONO['q']) + CUOTAS * .05, CUOTAS) + ')', m(BONO['a'] + round(ARRANQUE * .05)) + ' (' + pct(BONO['a'] + ARRANQUE * .05, ARRANQUE) + ')'],
 ['TOTAL si cierra la asesora (excepción)', m(BONO['c'] + round(CONTADO * .07)) + ' (' + pct(BONO['c'] + CONTADO * .07, CONTADO) + ')', m(sum(BONO['q']) + round(CUOTAS * .07)) + ' (' + pct(sum(BONO['q']) + CUOTAS * .07, CUOTAS) + ')', m(BONO['a'] + round(ARRANQUE * .07)) + ' (' + pct(BONO['a'] + ARRANQUE * .07, ARRANQUE) + ')'],
 ['Comparación: matrícula por pauta', m(META_X_MATRICULA + round(CONTADO * .05)) + ' (' + pct(META_X_MATRICULA + CONTADO * .05, CONTADO) + ') + plataforma', m(META_X_MATRICULA + round(CUOTAS * .05)) + ' + plataforma', m(META_X_MATRICULA + round(ARRANQUE * .05)) + ' + plataforma'],
], bold_rows=(4, 5))
for t in [
 '**La regla es que cierre el docente.** El caso "cierra la asesora" solo ocurre cuando él no llevó al referido a cita en 7 días o no cerró en 14 (sección 5): el lead pasa a ella y él se queda con su 2%. La propuesta del 12/10 ponía a la asesora al 3% en referidos; su contrato dice 5% para toda venta que gestione y no se toca por un caso que será la excepción.',
 '**Las primeras 2 matrículas el docente las cierra acompañado** por la asesora: él conduce y cobra su 5%; ella recibe ' + m(ACOMP) + ' fijos por acompañamiento (lo paga gerencia, máximo 2 veces; no modifica ningún contrato). Desde la 3ª cierra solo.',
 '**Una sola comisión por matrícula.** Nunca cobran los dos el 5% por el mismo recaudo. En la planilla queda quién condujo la asesoría hasta el abono.',
 '**Bono de quien refiere:** el estudiante activo elige **transferencia**, **abono a su propia cuota** o **2 horas 1-a-1**. El egresado elige transferencia o 2 horas 1-a-1. Sin tope: 3 matrículas, 3 bonos (más de 3 en un mes pasa a revisión, sección 4).',
 '**Beneficio del referido:** una **clase de prueba** en el grupo de quien lo refiere, antes de decidir (si quien refiere es egresado, en el grupo que coordinación indique). Entra con la misma tarifa y la misma beca que cualquiera. Coordinación define en qué grupos y qué días caben visitantes; el docente agenda la clase de prueba con coordinación, nunca por su cuenta.',
]: li(t)

h('2. Cuándo se paga')
for t in [
 '**Bono de quien refiere:** cuando el referido **pagó la inicial y asistió a su clase 5**. En cuotas, la segunda mitad cuando entra la cuota 3. Así no se paga por matrículas que se retiran en la primera semana.',
 '**Comisiones del docente y de la asesora:** liquidación mensual contra la planilla, sobre pagos con el retracto vencido, como dicen sus contratos. Devolución o retracto se descuenta de la siguiente liquidación.',
 '**Quién liquida:** coordinación arma la planilla a fin de mes; gerencia aprueba y paga. Lo que no está en la planilla no existe ni se paga.',
]: li(t)

h('3. Cómo se recogen los referidos (y por qué nadie pide el número del amigo)')
p('La SIC ha sancionado programas de referidos por usar datos del amigo sin su autorización (resoluciones de 2019, 2022 y 2023; Ley 1581). Por eso **el estudiante no entrega nombre ni número: reenvía un mensaje y el amigo le escribe a Heiiu primero.** Ese primer mensaje del amigo es la conducta que valida la autorización (Decreto 1377, art. 7) y Heiiu guarda la prueba (el chat).')
tabla([
 ['Paso', 'Quién', 'Qué pasa'],
 ['1', 'Docente', 'Ronda de 30 segundos al cierre de la clase (guion en el Anexo B), con el profe titular presente, fuera del tiempo de clase. A los egresados: mensaje primero y llamada de 2 minutos después (sección 7).'],
 ['2', 'Heiiu', 'Ese mismo día manda al grupo del curso (o al egresado) el mensaje reenviable (Anexo B-a).'],
 ['3', 'Estudiante / egresado', 'Se lo reenvía a UNA persona concreta. No da datos de nadie.'],
 ['4', 'Referido', 'Escribe a la línea de referidos de Heiiu: "Vengo de parte de [nombre]".'],
 ['5', 'Docente', 'Responde desde la línea de Heiiu con el aviso de privacidad y pide el SÍ (Anexo B-b). Sin SÍ no se escribe más. Registra en la planilla (Anexo C) antes de cualquier otra cosa.'],
 ['6', 'Docente', 'Perfila con las mismas preguntas del flujo del agente: para qué, nivel, presencial y jornada, El Pacto, forma de pago. Nunca ingresos ni centrales.'],
 ['7', 'Docente + coordinación', 'Agenda la clase de prueba (con quien lo refirió) y la asesoría por llamada de WhatsApp; presencial solo si el referido lo pide. La firma es presencial.'],
 ['8', 'Docente', 'Cierra con el tarifario oficial: contado, inicial del 20% y cuotas, o Arranque. Recibe el pago SOLO la cuenta de Heiiu; contrato y recibo los registra coordinación.'],
])
p('**Línea de referidos (decisión de gerencia).** La línea principal de WhatsApp la opera el agente de la plataforma: si el referido escribe ahí, el agente lo perfila y alerta a la asesora, no al docente. Recomendación: **un número nuevo de Heiiu** (SIM a nombre de la empresa, WhatsApp Business con el nombre Heiiu, en un celular que usa el docente; copia de seguridad y acceso de gerencia; al terminar el piloto el número vuelve a la oficina). Costo: el plan de la SIM. Alternativa: usar la línea principal y pedirle a la plataforma una regla "vengo de parte de" que derive al docente; eso implica otro cambio con la plataforma y se queda para la revisión de noviembre.')

h('4. Reglas anti-abuso')
for t in [
 'Cuenta como referido solo quien **escribe primero** con "vengo de parte de" y **no estaba** en la base, el bot ni un formulario en los últimos 30 días. Si ya estaba, es lead de pauta: sin bono y sin 5% del docente (aplica el flujo normal).',
 'Quien refiere debe estar **al día en pagos** (activo) o haber terminado su programa sin saldo (egresado).',
 'Más de **3 bonos en un mes** para la misma persona pasan a revisión de coordinación antes de pagarse.',
 'No se paga bono por **personal de Heiiu** ni por **familiares del docente recolector**; el docente no cobra bono de estudiante, solo su comisión.',
 'El bono **no se usa como argumento** ante el referido. Si pregunta, se le dice la verdad: "sí, a quien te refirió le damos un bono; a ti te damos la clase de prueba y la misma beca que a cualquiera".',
 '**Nunca descuento al referido.** Misma tarifa, misma beca, misma escalera. Esto protege los precios y evita que el referido negocie con el bono del otro.',
 'Los términos del bono van en la **hoja de términos** (Anexo A) con vigencia escrita, como exige la Ley 1480 (art. 33). Si cambia algo, se avisa por el mismo medio por el que se anunció.',
]: li(t)

h('5. Plazos y qué pasa si se vence')
tabla([
 ['Hito', 'Plazo desde el primer mensaje del referido', 'Si no se cumple'],
 ['Cita agendada (clase de prueba o asesoría)', '7 días', 'El lead pasa a la asesora. El docente queda con el 2% si ella cierra.'],
 ['Cierre (inicial pagada)', '14 días', 'Igual: pasa a la asesora, docente 2%.'],
 ['Lead que dice "no por ahora"', 'Un solo mensaje de despedida, sin reintentos', 'Marcado "frío" en la planilla; solo se retoma si él escribe.'],
])
p('Horario para mensajes y llamadas por iniciativa de Heiiu: lunes a viernes 7:00 a.m. a 7:00 p.m., sábados 8:00 a.m. a 3:00 p.m., nunca domingos ni festivos; máximo un contacto al día por lead (Ley 2300 de 2023). Lo que el referido escriba se responde a cualquier hora.', size=9.5, color=GRIS)

h('6. Los 4 candados del docente recolector-cerrador')
for t in [
 '**Papeles antes del primer mensaje:** (1) contrato docente v3.1 firmado (gerencia lo verifica hoy; si falta, se firma hoy); (2) **Anexo de Habilitación Comercial** firmado, que exige inducción previa con el Kit de Venta (precios, becas, escalera, El Pacto, garantía); (3) este programa como hoja de arranque firmada por los dos (metas, plazos, cierres acompañados, línea y planilla). El contrato ya cubre propiedad intelectual, confidencialidad, datos (Ley 1581) y la prohibición de usar bases o contactos de Heiiu fuera de Heiiu. No se pacta no competencia amplia: en Colombia no se sostiene (abogado).',
 '**Tarifario cerrado y cero autoridad.** Solo precios, becas y planes oficiales. Sin descuentos, sin promesas de facilidad, rapidez, empleo o visas, sin plazos de resultado distintos del texto de la garantía. Dice las condiciones duras antes de firmar (El Pacto: video diario, asistencia, puntualidad). **Nunca recibe dinero.** No firma nada en nombre de Heiiu.',
 '**Canal y datos de Heiiu.** Trabaja solo desde la línea de referidos de Heiiu; nunca desde su celular personal. El referido escribe primero y su SÍ queda en el chat. Planilla única (Anexo C). Las listas de estudiantes y egresados son Material Protegido: se consultan en la planilla y no salen de ahí.',
 '**Piloto de 15 días con metas, plazos y clase protegida.** Cero venta en tiempo de clase. Metas en la sección 7. Sus horas de ronda y de llamadas no se pagan aparte: su ingreso es la comisión (así lo dice el anexo: actividad facultativa, sin subordinación). Si gerencia decide pagarlas, entran al costo por matrícula.',
]: li(t)

h('7. Operación del piloto (15 días: del 15 al 30 de octubre)')
for t in [
 '**Días 1-3 (15 al 17/10) — grupos activos:** una ronda de 30 segundos en cada grupo, todos los grupos en tres días (coordinación entrega hoy la lista de grupos y horarios). Una sola petición en clase por grupo; después, los momentos fijos: al cerrar una matrícula (la asesora), al grabar un testimonio, tras un midterm o presentación, y al graduar (cada graduado sale con 2 referidos pedidos).',
 '**Días 1-7 (15 al 22/10) — egresados, todos:** coordinación arma hoy la lista (nombre, nivel terminado, fecha, teléfono) en la planilla. El docente escribe primero por la línea de Heiiu (Anexo B-c): se presenta, pide permiso para llamar 2 minutos y ofrece la salida ("si prefieres que no te escribamos, dímelo"). Quien dice que no, se marca y no se vuelve a contactar. Llamada en horario legal. SUPUESTO: la autorización de datos de la matrícula cubre esta comunicación de la academia; el abogado lo confirma. Por eso el mensaje va primero y nunca una llamada en frío.',
 '**Metas del piloto (al 30/10):** 15 referidos que escriben → 5 citas → 2 matrículas con inicial pagada. Si la lista de egresados contactables pasa de 60 personas, la meta sube a 20 → 7 → 3. (Con 60 activos y una participación típica cercana al 19%, solo los activos darían unos 11 referidos; los egresados completan la cifra.) Ritmo diario: 1 referido nuevo que escribe por día hábil.',
 '**Reporte:** mensaje de 3 líneas TODOS los días a las 6:00 p.m. (a quién pidió hoy, cuántos escribieron, citas agendadas) y 5 líneas los lunes en la reunión fija (registrados, contactados, citas, matrículas, bonos por pagar). Lo que no está en la planilla no cuenta.',
 '**Corte del 30/10:** referidos que escribieron, citas, asistencia, matrículas con inicial, días de primer mensaje a cita, y costo por matrícula referida (bonos + comisiones) contra pauta ($72.000 + 5% + plataforma). Sigue si llegó a la meta o si el costo por matrícula referida es ≤ 1,2 veces el de la pauta. Si no llegó ni a 5 referidos que escriben, el problema es la ronda o el mensaje, no el bono: se corrige el guion y se repite 15 días más. La retención (cuota 3 y asistencia ≥80% a 90 días) se mide después, al cierre del cohorte.',
]: li(t)

h('8. Para el contador (antes del primer pago de bono)')
for t in [
 'El bono en efectivo a un estudiante o egresado (persona natural, no empleado ni contratista): ¿se soporta como gasto de promoción? ¿Qué documento lo soporta (documento soporte DIAN con no obligado a facturar, o cuenta de cobro)? ¿Lleva retención en la fuente y a qué tarifa?',
 'El bono como abono a la cuota del estudiante: ¿se registra como descuento comercial (nota crédito) o como gasto? ¿Afecta el valor del contrato y del pagaré?',
 'El bono en especie (2 horas 1-a-1): ¿basta con registrarlo como costo docente?',
 'Las comisiones del docente y de la asesora ya se liquidan contra cuenta de cobro con retención, como hoy. ¿Algo cambia por ser referidos?',
]: li(t)

h('9. Lo que falta para arrancar (checklist)')
for t in ['Contrato docente v3.1 firmado (verificar hoy).', 'Inducción con el Kit de Venta y firma del Anexo de Habilitación Comercial.', 'Hoja de arranque del docente firmada (este documento, secciones 1, 5, 6 y 7).',
          'Número de la línea de referidos (SIM + WhatsApp Business) o decisión de usar la principal.', 'Lista de egresados con teléfono (coordinación) y lista de grupos activos con horarios.', 'Grupos y días con cupo para clase de prueba (coordinación).',
          'Hoja de términos del bono (Anexo A) firmada por gerencia y enviada a los grupos.', 'Respuesta del contador (sección 8).', 'Costo por lead de la plataforma, para cerrar la comparación con la pauta.']:
    li('☐  ' + t)

salto()
p('ANEXO A — HOJA DE TÉRMINOS DEL BONO DE REFERIDOS (para estudiantes y egresados)', NAR, 13)
p('Vigencia: del 15 de octubre al 31 de diciembre de 2026. Heiiu puede prorrogar o modificar estos términos avisando por el mismo medio por el que los comunicó (Ley 1480 de 2011, art. 33).', GRIS, 9.5)
for t in [
 '**Quién puede referir:** estudiantes activos al día en sus pagos y egresados de Heiiu sin saldo pendiente.',
 '**Cómo se refiere:** reenvías a tu amigo el mensaje que te manda Heiiu. Tu amigo le escribe a Heiiu diciendo "Vengo de parte de [tu nombre]". No nos des su número: él decide si escribe.',
 '**Qué recibe tu amigo:** una clase de prueba contigo (o en el grupo que le indiquemos) antes de decidir, y las mismas condiciones y becas de cualquier estudiante.',
 '**Qué recibes tú:** ' + m(BONO['c']) + ' si tu amigo se matricula en un programa completo; ' + m(BONO['a']) + ' si entra al Arranque A1+A2. Si paga a cuotas, el bono se divide en dos: la mitad con su inicial y la otra mitad con su cuota 3. Eliges cómo recibirlo: transferencia, abono a tu propia cuota o 2 horas de clase 1-a-1.',
 '**Cuándo se paga:** cuando tu amigo pagó su inicial y asistió a su clase 5. Heiiu liquida los bonos a fin de mes.',
 '**Condiciones:** tu amigo no debe haber tenido contacto con Heiiu (chat, formulario o asesoría) en los últimos 30 días. No aplica para personal de Heiiu ni sus familiares. No hay tope de referidos; más de 3 en un mes pasan por una revisión antes del pago. Si tu amigo se retira y pide devolución antes de la clase 5, el bono no se causa.',
 '**Datos:** solo tratamos los datos de tu amigo cuando él nos escribe y nos autoriza. Tus datos se tratan según la política de datos de Heiiu.',
]: li(t)
p('Gerencia — Heiiu · Bucaramanga, 15 de octubre de 2026 · Firma: ____________________', after=10)

p('ANEXO B — GUIONES Y MENSAJES', NAR, 13)
p('**Guion de 30 segundos en clase** (al cierre, con el profe titular presente):', after=2)
caja(['"Treinta segundos antes de que se vayan.', 'Ustedes saben lo que cuesta este proceso y saben que funciona.', 'Piensen en UNA persona que necesite inglés de verdad:', 'para el trabajo, para irse, para su hijo. ¿Ya la tienen?', 'No me den su número. Hoy les llega al grupo un mensaje:', 'reenvíenselo a esa persona. Si escribe, se matricula', 'y llega a su clase 5, ustedes reciben $150.000,', 'un abono a su cuota o 2 horas 1-a-1. Ustedes eligen.', 'Y su amigo puede venir a una clase con ustedes antes de decidir.', '¿Quién ya pensó en alguien? Escríbanle hoy."'])
p('**(a) Mensaje que Heiiu manda al grupo (o al egresado) y el estudiante reenvía a su amigo:**', after=2)
caja(['Hola [nombre]. Estoy estudiando inglés en Heiiu (presencial, Bucaramanga)', 'y me está funcionando. No es fácil: es entrenamiento todos los días.', 'Si te interesa, escríbeles a este número [línea de referidos] con:', '"Vengo de parte de [mi nombre]". Te cuentan cómo es y puedes', 'venir a una clase conmigo antes de decidir.'])
p('Versión para egresados: cambia "Estoy estudiando" por "Estudié inglés en Heiiu y salí hablando" y "una clase conmigo" por "una clase antes de decidir".', size=9.5, color=GRIS)
p('**(b) Primera respuesta de Heiiu al referido** (desde la línea de referidos, nunca desde un celular personal):', after=2)
caja(['Hola [nombre], gracias por escribir. Soy [nombre], profesor de Heiiu.', 'Antes de seguir: usaremos tu nombre y número solo para darte información', 'de nuestros programas, según nuestra política de datos [enlace].', '¿Nos autorizas? Responde SÍ. (Puedes pedir que te borremos cuando quieras.)'])
p('Después del SÍ: para qué necesitas el inglés · desde cero o ya estudiaste (y qué pasó) · presencial y jornada · El Pacto (video diario, garantía por escrito: "¿te le mides a ese ritmo?") · contado o inicial y cuotas · clase de prueba y asesoría por llamada: "¿[franja 1] o [franja 2]?". El referido escribe el día y la hora para que quede firme.', size=9.5, color=GRIS)
p('**(c) Primer mensaje a un egresado** (antes de llamar):', after=2)
caja(['Hola [nombre], soy [nombre], profesor de Heiiu. Terminaste [nivel] con nosotros', 'en [mes]. Te escribo por una sola cosa: ¿tienes 2 minutos para que te llame', 'hoy o mañana? Es sobre una persona que tú conozcas que necesite inglés.', 'Si prefieres que no te escribamos más, dímelo y listo.'])
p('**Guion de la llamada al egresado (2 minutos):** cómo te fue después del curso (una pregunta, para la planilla de testimonios) → "piensa en UNA persona que necesite inglés de verdad: trabajo, irse, un hijo" → "no me des su número: te mando un mensaje y se lo reenvías; si escribe y se matricula, recibes $150.000 o 2 horas 1-a-1" → "¿a quién se lo vas a mandar hoy?" → mensaje (a) versión egresado enviado al colgar.', size=9.5, color=GRIS)

p('ANEXO C — PLANILLA ÚNICA DE REFERIDOS (columnas)', NAR, 13)
tabla([
 ['Columna', 'Qué va'],
 ['Fecha del primer mensaje', 'Día y hora en que el referido escribió "vengo de parte de"'],
 ['Referido', 'Nombre y teléfono (solo después del SÍ)'],
 ['Autorización', 'SÍ con fecha (captura del chat guardada)'],
 ['Quién refiere', 'Nombre · activo (grupo) o egresado (nivel, fecha) · al día: sí/no'],
 ['Recolectado por', 'Docente / asesora / otro'],
 ['Verificación 30 días', 'No estaba en base, bot ni formulario: sí/no (lo revisa coordinación)'],
 ['Estado', 'Contactado → clase de prueba (fecha) → cita (fecha) → inicial pagada → clase 5 → bono pagado'],
 ['Quién condujo la asesoría', 'Docente / asesora / acompañado (nº 1-2)'],
 ['Programa y forma de pago', 'Completo contado / cuotas / Arranque'],
 ['Bono', 'Valor · forma elegida (transferencia, abono, 2 h) · fecha de pago'],
 ['Comisión', 'A quién (5% o 2%) · mes de liquidación'],
 ['Plazos', 'Día 7 (cita) · día 14 (cierre) · pasó a asesora: sí/no'],
])

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\PROGRAMA_REFERIDOS_PROPUESTA_2026-10.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
