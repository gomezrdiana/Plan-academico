# -*- coding: utf-8 -*-
"""Piezas editoriales de conciencia (reemplazan los volantes PIL de gen_volantes_segmentos.py, retirado el 24/10/2026).
Una pieza MANIFIESTO (por qué el inglés y los hábitos suben de valor cuando casi todo lo demás lo pierde) y cuatro piezas
por segmento con el mismo sistema visual: PROFESIONALES (médicos, profesionales, directivos), MEDICINA (entrevistas de
admisión), ATENCION (recepción, salud, hoteles, turismo, restaurantes) y PADRES.
Se escriben en HTML/CSS (Constantia + Segoe UI + Bahnschrift, fuentes del sistema) y se renderizan a PNG 1080x1620 con
Microsoft Edge sin ventana. Reglas: sin precio, sin modalidad ni horarios, sin "fácil/rápido", sin empleo/visa/nativos,
sin nombres de competidores, sin "únicos", garantía por escrito. Contacto: línea de alianzas 316 768 8793 (el gerente de
alianzas reparte las piezas), nunca la línea principal.
Salida (git): recursos/comercial/campanas/volantes/{publico}/PIEZA_*.png (digitales; una subcarpeta por publico: jovenes, padres, empresas,
hoteleria, recepcion, medicos, profesionales, ya_decidio, calle, manifiesto) + copia en la carpeta del gerente de alianzas / volantes.
La hoja de asesoras (GENERAL_ASESORAS_FRENTE + un RESPALDO por codigo, con QR) solo se imprime: va unicamente a volantes/{publico}/imprenta/ con sangrado de 3 mm.
ASESORAS_CORTA_QR = la corta de jovenes con QR, una por codigo, digital: la asesora la abre en su celular y el joven la escanea (sin imprenta).
Uso: python generadores/comercial/gen_piezas_conciencia.py"""
import os, shutil, subprocess, pathlib, tempfile
from urllib.parse import quote
from PIL import Image
import qrcode

ROOT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
LOGO_NAR = os.path.join(ROOT, r'recursos\marca heiiu\logo_heiiu_sobre_naranja.png')
LOGO_TR = os.path.join(ROOT, r'recursos\marca heiiu\logo_heiiu_transparente.png')
OUTDIR = os.path.join(ROOT, r'recursos\comercial\campanas\volantes')
COPIA = os.path.join(ROOT, r'recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza\volantes')
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
WORK = os.path.join(tempfile.gettempdir(), 'heiiu_piezas'); os.makedirs(WORK, exist_ok=True)
LINEA = '316 768 8793'; IG = '@heiiu_english'
QR_LINEA = '573167688793'; QR_MENSAJE = 'Hola, quiero información para estudiar inglés en Heiiu. Código de asesor: {codigo}'
CODIGOS_TXT = os.path.join(ROOT, r'recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza\plan referidos\codigos_asesoras.txt')


def codigos():
    if os.path.exists(CODIGOS_TXT): return [l.strip() for l in open(CODIGOS_TXT, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return ['C-%02d' % i for i in range(1, 11)]


def qr_png(codigo):
    enlace = 'https://wa.me/%s?text=%s' % (QR_LINEA, quote(QR_MENSAJE.format(codigo=codigo)))
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1); q.add_data(enlace); q.make(fit=True)
    out = os.path.join(WORK, 'qr_%s.png' % codigo); q.make_image(fill_color=(28, 23, 20), back_color='white').save(out); return out
W, H = 1080, 1620


def logo_transparente():
    """Quita el naranja del logo oficial (blanco + amarillo quedan) para usarlo sobre fondo oscuro."""
    if os.path.exists(LOGO_TR): return
    im = Image.open(LOGO_NAR).convert('RGB'); px = im.load(); out = Image.new('RGBA', im.size); po = out.load()
    orr, org, orb = px[3, 3]
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px[x, y]
            a = min(1.0, max(0.0, (g - org) / 127.0))          # naranja g=74 -> 0; amarillo g=201 -> 1; blanco -> 1
            if a <= 0.02: po[x, y] = (0, 0, 0, 0); continue
            rr = min(255, max(0, int((r - (1 - a) * orr) / a))); gg = min(255, max(0, int((g - (1 - a) * org) / a))); bb = min(255, max(0, int((b - (1 - a) * orb) / a)))
            po[x, y] = (rr, gg, bb, int(a * 255))
    out.save(LOGO_TR); print('logo transparente OK')


CSS = """
@page { margin: 0 }
* { box-sizing: border-box; margin: 0; padding: 0 }
html, body { width: %(W)dpx; height: %(H)dpx; overflow: hidden }
body { background: #1C1714; color: #FFF8E7; font-family: 'Segoe UI', Candara, sans-serif; -webkit-font-smoothing: antialiased }
.page { position: relative; width: %(W)dpx; height: %(H)dpx; overflow: hidden;
        background: radial-gradient(900px 700px at 100%% -10%%, rgba(229,76,9,.42), rgba(229,76,9,0) 60%%),
                    radial-gradient(700px 500px at -10%% 65%%, rgba(251,201,0,.10), rgba(251,201,0,0) 60%%), #1C1714 }
.top { height: calc(100%% - %(BAND)dpx); padding: 64px 72px 64px 72px; display: flex; flex-direction: column }
.label { font-family: Bahnschrift, 'Segoe UI', sans-serif; font-size: 20px; letter-spacing: .26em; color: #FBC900; font-weight: 600 }
.label span { color: rgba(255,248,231,.55); margin-left: 14px; letter-spacing: .2em }
h1 { font-family: Constantia, Georgia, serif; font-weight: 700; font-size: 86px; line-height: 1.04; letter-spacing: -.012em; margin-top: 34px; color: #FFF8E7 }
h1 em { font-style: italic; color: #FBC900; font-weight: 400 }
.rule { width: 96px; height: 5px; background: #E54C09; margin: 38px 0 36px 0 }
ol.st { list-style: none }
ol.st li { display: grid; grid-template-columns: 64px 1fr; gap: 0 18px; align-items: start; padding: 26px 0 24px 0; border-top: 1px solid rgba(255,248,231,.14) }
ol.st li:last-child { border-bottom: 1px solid rgba(255,248,231,.14) }
ol.st .n { font-family: Bahnschrift, sans-serif; font-size: 24px; color: #FBC900; letter-spacing: .08em; padding-top: 6px }
ol.st p { font-size: 30px; line-height: 1.34; color: rgba(255,248,231,.70); font-weight: 300 }
ol.st p b { color: #FFF8E7; font-weight: 600 }
.pivot { margin-top: auto; padding-top: 44px }
.pivot .lead { font-family: Georgia, Constantia, serif; font-style: italic; font-size: 40px; color: #FBC900; line-height: 1.2 }
.pivot .big { font-family: Constantia, Georgia, serif; font-weight: 700; font-size: 68px; line-height: 1.06; letter-spacing: -.01em; margin-top: 18px; color: #FFF8E7 }
.pivot .big2 { font-family: Constantia, Georgia, serif; font-size: 40px; line-height: 1.2; margin-top: 26px; color: rgba(255,248,231,.88) }
.why { margin-top: 46px }
.why h2 { font-family: Constantia, Georgia, serif; font-size: 44px; font-weight: 700; color: #FBC900; margin-bottom: 20px }
.why .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px }
.why .card { background: rgba(255,248,231,.055); border: 1px solid rgba(255,248,231,.16); border-radius: 18px; padding: 22px 24px 24px 24px }
.why .card.full { grid-column: 1 / span 2; background: rgba(251,201,0,.10); border-color: rgba(251,201,0,.45) }
.why .k { font-family: Bahnschrift, sans-serif; font-size: 19px; letter-spacing: .14em; color: #FBC900; font-weight: 600; margin-bottom: 8px }
.why p { font-size: 25px; line-height: 1.3; color: rgba(255,248,231,.86) }
.why p b { color: #FFF8E7; font-weight: 600 }
.intro { font-family: Constantia, Georgia, serif; font-size: 27px; line-height: 1.36; color: rgba(255,248,231,.88); margin: 0 0 22px 0 } .intro b { color: #FBC900 }
.intro.after { margin: 10px 0 0 0 }
blockquote { margin-top: 10px; padding: 22px 28px 22px 30px; border-left: 6px solid #FBC900; background: rgba(255,248,231,.06); border-radius: 0 16px 16px 0;
             font-family: Constantia, Georgia, serif; font-size: 27px; line-height: 1.36; color: #FFF8E7 }
blockquote b { font-weight: 700 } blockquote cite { display: block; font-style: normal; font-family: Bahnschrift, sans-serif; font-size: 18px; letter-spacing: .14em; color: #FBC900; margin-top: 12px }
.fn { margin-top: 22px; padding-top: 12px; border-top: 1px solid rgba(255,248,231,.14); font-size: 16px; line-height: 1.35; color: rgba(255,248,231,.5) }
.band { position: absolute; left: 0; right: 0; bottom: 0; height: %(BAND)dpx; background: #FF4A00; padding: 44px 72px 0 72px;
        display: grid; grid-template-columns: 1fr 215px; gap: 0 40px; align-items: start }
.band::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 8px; background: #FBC900 }
.band p { font-size: 25px; line-height: 1.34; color: #FFF8E7 }
.band p b { font-weight: 700 }
.band .logo { width: 215px; margin-top: -12px; justify-self: end }
.band .qrbox { position: absolute; right: 60px; top: 22px; width: 240px; background: #FFF8E7; border-radius: 14px; padding: 9px 9px 6px 9px; text-align: center }
.band .qrbox img { width: 206px; display: block; margin: 0 auto }
.band .qrbox span { font-family: Bahnschrift, sans-serif; font-weight: 700; font-size: 26px; color: #E54C09; display: block; margin-top: 2px; letter-spacing: .04em }
.band.tels .cta .tel { font-size: 28px; font-weight: 600; letter-spacing: 0 }
.band.qr .cta { right: 330px } .band.qr .cta .tel { font-size: 26px; font-weight: 400 }
.band .codigo { justify-self: end; width: 215px; border: 3px dashed rgba(255,248,231,.85); border-radius: 12px; padding: 10px 12px 8px 12px; text-align: center; margin-top: -8px }
.band .codigo .k { font-family: Bahnschrift, sans-serif; font-size: 15px; letter-spacing: .12em; color: #FFF8E7; display: block; margin-bottom: 4px }
.band .codigo .v { font-family: Bahnschrift, sans-serif; font-size: 34px; font-weight: 700; color: #FFF8E7; display: block; line-height: 1 }
.band .codigo .v span { display: inline-block; width: 92px; border-bottom: 3px solid #FBC900; height: 30px; vertical-align: bottom; margin-left: 6px }
.cta { position: absolute; left: 72px; right: 72px; bottom: 40px; display: flex; justify-content: space-between; align-items: baseline;
       border-top: 1px solid rgba(255,248,231,.45); padding-top: 22px }
.cta .tel { font-family: Bahnschrift, sans-serif; font-size: 40px; font-weight: 700; letter-spacing: .02em; color: #FFF8E7 }
.cta .tel small { font-family: 'Segoe UI', sans-serif; font-weight: 400; font-size: 22px; letter-spacing: 0; margin-right: 14px; color: rgba(255,248,231,.85) }
.cta .ig { font-size: 22px; color: #FFF8E7; letter-spacing: .04em }
.cta .ig b { color: #1C1714; background: #FBC900; padding: 6px 14px; border-radius: 6px; font-weight: 700; margin-left: 14px; font-size: 20px }
"""

PIEZAS = {
    'MANIFIESTO': dict(
        label='HEIIU ENGLISH ACADEMY', sub='BUCARAMANGA',
        h1='Casi todo pierde valor <em>más rápido</em> que antes.',
        st=[('La tecnología cambió la forma de aprender. Lo que hace cinco años se estudiaba en un salón, hoy está en una pantalla.'),
            ('Los títulos ya no dicen, por sí solos, lo que una empresa necesita saber de una persona.'),
            ('La inteligencia artificial avanza cada mes y hace cosas que antes pagábamos a especialistas.')],
        lead='Pero hay algo que sube de valor cada día:',
        big='poder hablar con cualquier persona del mundo.',
        big2='Y los hábitos que hacen que de verdad lo logres. Y una idea de negocio propia, pensada y contada en inglés.',
        band='En Heiiu entrenamos las dos cosas: <b>el inglés</b> y <b>los hábitos que lo sostienen</b>: puntualidad, constancia y disciplina. Con garantía de aprendizaje por escrito.',
        band_px=340),
    'GENERAL_ASESORAS_FRENTE': dict(   # hoja que la asesora de la entidad aliada entrega o reenvia; cara 1: conciencia con cifras verificadas (fuentes al pie)
        compact=True, label='HEIIU ENGLISH ACADEMY', sub='BUCARAMANGA',
        h1='¿Otro año sin plata y sin rumbo? <em>Aquí alguien cree en ti y empuja tu proyecto.</em>',
        st=[('<b>Ya ni la universidad asegura nada.</b> Hay carreras que cambian antes de terminarlas y títulos que las empresas ya no piden. <b>El que habla inglés abarca más</b>: más vacantes, más clientes, más países, y una idea de negocio propia que aquí te empujamos a pensar.'),
            ('<b>De cada 8 jóvenes que terminan el colegio en Colombia, solo 1 sale con un inglés que le sirva</b> para estudiar o trabajar. Los otros 7 lo tienen pendiente de adultos.¹'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más</b> que quien hace el mismo trabajo sin él.²'),
            ('<b>La inteligencia artificial traduce, pero no conversa por ti.</b> En la entrevista, con el cliente y en el aeropuerto, el que habla eres tú.')],
        lead='Y no es falta de ganas: es que nadie aprende un idioma solo.',
        big='De cada 100 personas que bajan una app de inglés, 88 la dejan antes del mes.³',
        big2='Un idioma se entrena en equipo, con gente que no busca excusas ni culpables: busca lograr el objetivo.',
        fn='¹ Pruebas Saber 11 de 2025, análisis del Observatorio de Realidades Educativas de la Universidad Icesi. ² DNP, Archivos de Economía, <i>Bilingüismo laboral en Colombia</i>. ³ Retención a 30 días de la app de idiomas más descargada, estadísticas públicas 2026.',
        band='Dale la vuelta a la hoja: así entrenamos en Heiiu, <b>la beca a la que aplicas con el código de tu asesora</b> y cómo escribirnos.',
        tel='Cómo escribirnos: <b>al respaldo</b>', band_px=250),
    'GENERAL_ASESORAS_RESPALDO': dict(   # cara 2: el Pacto con las palabras de gerencia (texto vigente 15/10/2026), por que Heiiu, beca y como escribir
        compact=True, theme='light', label='ASÍ ES HEIIU', sub='LEE ESTO ANTES DE DECIDIR',
        h1='Academias hay muchas. <em>Esta te firma el resultado.</em>',
        intro=('A muchas academias les sale el negocio cuando pagas y dejas de ir. Nadie te llama, nadie te extraña, y a los tres meses la matrícula se volvió culpa. '
               '<b>En Heiiu queremos la parte difícil: que vengas, que te sueltes a hablar y que no te rindas.</b> Por eso te lo decimos antes de que pagues:'),
        quote=('Nuestro objetivo es que salgas hablando inglés. Si no se logra, algo está mal: o tú dejaste de entrenar, o nosotros no estamos cumpliendo. '
               'Esto es un entrenamiento en equipo, como prepararse para una maratón: desde el primer día hablas, tu profesor ve dónde puedes mejorar y lo repetimos hasta que sale. '
               'Por eso grabas un video corto todos los días y tu profesor te lo devuelve con una mejora. A cambio, la garantía por escrito: '
               '<b>si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.</b> ¿Te le mides a ese ritmo?'),
        cite='GERENCIA · HEIIU ENGLISH ACADEMY',
        after='¿Suena duro? Míralo al revés: <b>la única forma de perder la plata es dejar de entrenar.</b> Si entrenas, sales hablando inglés. Y si entrenas y no avanzas, te la devolvemos.',
        st=[], lead='', big='', big2='',
        why=[('AQUÍ NADIE DESAPARECE', 'Faltaste y no avisaste: te llamamos ese mismo día. Si eres menor, en tu casa también se enteran. No es persecución: es la parte menos chévere del coach, <b>la que esperamos no tener que hacer</b>.', False),
             ('SE NOTA, Y SE PUEDE MOSTRAR', 'Te grabamos el primer día y el último del nivel. Pon los dos videos juntos y no vas a necesitar que nadie te diga que avanzaste. <b>En casa tampoco tendrán que creerte: lo oyen.</b>', False),
             ('PUERTAS AFUERA, PERO SEGURAS', 'Cuando veas a dónde te puede llevar tu inglés, te contactamos con operadores verificados de programas en el exterior: au pair, trabajo de temporada, campamentos. Solo puertas seguras.', False),
             ('LA CONTRASEÑA', 'Los médicos se reconocen por el amor a aprender. Aquí la contraseña es otra y con ella entra cualquiera: <b>el amor por salir adelante</b>. Sin excusas, con dolor y con la meta al frente. Así, estás entre los tuyos.', False)],
        band='Escanea el código de tu asesora: el mensaje ya sale listo con su código. <b>Con él aplicas a la beca; sin código no hay beca.</b>',
        por_codigo=True, band_px=290),
    # ---------------- INDUSTRIAS (frente oscuro + respaldo claro, 10x15 a doble cara; las reparte el gerente de alianzas) ----------------
    'HOTELERIA_FRENTE': dict(
        compact=True, label='INGLÉS PARA HOTELERÍA Y TURISMO', sub='HOTELES · RESTAURANTES · AGENCIAS · GUÍAS',
        h1='El turista habla inglés. <em>¿Lo recibes tú o llamas a otro?</em>',
        st=[('<b>En 2025 Colombia recibió más extranjeros que nunca:</b> 3,5 millones entre enero y septiembre, 4,5% más que el año anterior.¹'),
            ('<b>El visitante número uno viene de Estados Unidos:</b> 1 de cada 5 extranjeros.¹ Pide, reclama y agradece en inglés.'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más</b> que quien hace el mismo trabajo sin él.²'),
            ('<b>La inteligencia artificial traduce, pero no conversa por ti.</b> El huésped que llega a las once de la noche habla contigo, no con una app.')],
        lead='Y no es falta de ganas: es que nadie aprende un idioma solo.',
        big='De cada 100 personas que bajan una app de inglés, 88 la dejan antes del mes.³',
        big2='Un idioma se entrena en equipo, con gente que no busca excusas: busca atender bien. Y aquí te empujamos a pensar una idea de negocio propia y a contarla en inglés.',
        fn='¹ Ministerio de Comercio, Industria y Turismo y Migración Colombia, enero a septiembre de 2025. ² DNP, Archivos de Economía, <i>Bilingüismo laboral en Colombia</i>. ³ Retención a 30 días de la app de idiomas más descargada, estadísticas públicas 2026.',
        band='Dale la vuelta a la hoja: así entrenamos en Heiiu y <b>la beca con el nombre de tu hotel, restaurante o agencia</b>.',
        band_px=250),
    'HOTELERIA_RESPALDO': dict(
        compact=True, theme='light', label='ASÍ ES HEIIU', sub='INGLÉS PARA HOTELERÍA Y TURISMO',
        h1='Academias hay muchas. <em>Esta te firma el resultado.</em>',
        intro='A muchas academias les sale el negocio cuando pagas y dejas de ir. Nadie te llama, nadie te extraña, y a los tres meses la matrícula se volvió culpa. <b>En Heiiu queremos la parte difícil: que vengas, que te sueltes a hablar y que no te rindas.</b> Por eso te lo decimos antes de que pagues:', quote='Nuestro objetivo es que salgas hablando inglés. Si no se logra, algo está mal: o tú dejaste de entrenar, o nosotros no estamos cumpliendo. Esto es un entrenamiento en equipo, como prepararse para una maratón: desde el primer día hablas, tu profesor ve dónde puedes mejorar y lo repetimos hasta que sale. Por eso grabas un video corto todos los días y tu profesor te lo devuelve con una mejora. A cambio, la garantía por escrito: <b>si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.</b> ¿Te le mides a ese ritmo?', cite='GERENCIA · HEIIU ENGLISH ACADEMY', after='¿Suena duro? Míralo al revés: <b>la única forma de perder la plata es dejar de entrenar.</b> Si entrenas, sales hablando inglés. Y si entrenas y no avanzas, te la devolvemos.',
        st=[], lead='', big='', big2='',
        why=[('LAS ESCENAS DE TU PUESTO', 'Cada clase es una situación real: el check-in, la reserva por teléfono, la mesa que pide la cuenta, la queja por el aire acondicionado. Se repite hasta que sale sin pensar.', False),
             ('AQUÍ NADIE DESAPARECE', 'Faltaste y no avisaste: te llamamos ese mismo día. No es persecución: es la parte menos chévere del coach, <b>la que esperamos no tener que hacer</b>.', False),
             ('SE NOTA, Y SE PUEDE MOSTRAR', 'Te grabamos el primer día y el último del nivel. Pon los dos videos juntos y no vas a necesitar que nadie te diga que avanzaste. <b>Tu jefe tampoco tendrá que creerte: lo oye.</b>', False),
             ('PARA TU EMPRESA', 'Becas con el nombre del hotel, el restaurante o la agencia para su equipo, <b>sin costo para la empresa</b>. Pregunta por el programa de alianzas.', False)],
        band='Grupos para equipos o programa individual. <b>Escríbenos y agenda tu asesoría.</b>',
        band_px=290),

    'MEDICOS_DIRECTIVOS_FRENTE': dict(   # programa individual de 100 horas: sin garantia (decision de gerencia 24/10/2026), trato de usted
        compact=True, label='PROGRAMA INDIVIDUAL', sub='MÉDICOS · ESPECIALIZACIONES · ALTA DIRECCIÓN',
        h1='El paciente de afuera ya llegó. <em>¿Le paga la consulta a usted o al que sí habla inglés?</em>',
        st=[('<b>El 92% de los artículos de ciencias de la salud está en inglés.</b>¹ El congreso, el protocolo y la convocatoria llegan primero en ese idioma.'),
            ('<b>En 2025 llegaron a Colombia más extranjeros que nunca, y 1 de cada 5 viene de Estados Unidos.</b>² El paciente de afuera no trae intérprete: pregunta, entiende y decide en inglés.'),
            ('<b>Sin inglés no se pierde un título. Se pierden conversaciones:</b> el networking, los resultados que vale la pena contar, entender lo que otros quieren transmitir.'),
            ('<b>La inteligencia artificial traduce el documento, pero no conversa por usted.</b> En la entrevista de la especialización, en la junta y en el congreso, el que habla es usted.')],
        lead='En un puesto directivo o médico, eso es gran parte de la experiencia, del avance y de los resultados.',
        big='A este nivel nadie aprende con una app: se aprende con un plan a su medida.',
        big2='Y si tiene una idea de negocio, la trabajamos con usted y la presenta en inglés.',
        fn='¹ Elsevier, con datos de PubMed. ² Ministerio de Comercio, Industria y Turismo y Migración Colombia, enero a septiembre de 2025.',
        band='Dale la vuelta a la hoja: así es el programa individual y <b>cómo se arma sobre su agenda</b>.',
        band_px=250),
    'MEDICOS_DIRECTIVOS_RESPALDO': dict(
        compact=True, theme='light', label='ASÍ ES EL PROGRAMA INDIVIDUAL', sub='100 HORAS · UNO A UNO · CONVERSACIONES AVANZADAS EN SU ÁREA',
        h1='Su inglés, <em>en su agenda.</em>',
        intro=('<b>Entrenamos conversaciones avanzadas en su área laboral.</b> Armamos el plan a su medida, para que la clase se enfoque en los temas de los que usted ya estaría hablando si hablara inglés: la junta, el congreso, el paciente o el cliente de afuera, '
               'la entrevista de la especialización. Usted fija los días y las horas cada semana. Antes de hablar de precios, le decimos cómo es:'),
        quote=('Nuestro objetivo es que salga hablando inglés en lo suyo. Esto es un entrenamiento, como prepararse para una maratón: desde el primer día habla, su profesor ve dónde puede mejorar y lo repetimos hasta que sale. '
               'Entre una sesión y otra, un audio corto que su profesor le devuelve con una mejora; usted elige cuándo. Empezamos con una prueba de nivel; <b>el avance lo va a notar usted en la junta, no en un papel.</b> ¿Se le mide?'),
        cite='GERENCIA · HEIIU ENGLISH ACADEMY',
        after='¿Suena exigente? Lo es, a propósito. <b>Las 100 horas tienen 12 meses de vigencia desde la primera sesión; las que no use en ese plazo se pierden.</b> Dentro del plazo usted decide el ritmo, no el calendario de un grupo: con tres horas a la semana termina en unos ocho meses; con más, antes.',
        st=[], lead='', big='', big2='',
        why=[('SOBRE SU TRABAJO', 'El contenido sale de su día: el caso que presenta, la junta del jueves, el correo que hay que contestar hoy. Nada de diálogos de libro.', False),
             ('PARA LA ESPECIALIZACIÓN', 'Entrevista de admisión, presentación de un caso, su historia profesional en un minuto. Se graba, se corrige y se repite hasta que suene seguro. <b>No prometemos la admisión: entrenamos la entrevista.</b>', False),
             ('AVANCE QUE SE NOTA', 'Prueba de nivel al inicio para armar el plan, y cuenta clara de las horas usadas y las que le quedan. El avance lo nota usted donde importa: en la conversación.', False),
             ('LO QUE NO HACEMOS', 'No prometemos el ascenso ni la visa. No usamos diálogos de libro ni horarios fijos que no caben en un turno. <b>Cupos limitados por disponibilidad de profesor.</b>', False)],
        band='Programa individual para médicos, profesionales y directivos. <b>Agende una asesoría de 15 minutos.</b>',
        band_px=290),
    'PROFESIONALES_FRENTE': dict(   # programa individual, version general (decision de gerencia 27/10/2026): directivos, ejecutivos, ingenieros, abogados; misma estructura que medicos, sin el nicho
        compact=True, label='PROGRAMA INDIVIDUAL', sub='DIRECTIVOS · EJECUTIVOS · INGENIEROS · ABOGADOS',
        h1='El cliente de afuera ya llegó. <em>¿Le firma el contrato a usted o al que sí habla inglés?</em>',
        st=[('<b>Quien certifica su inglés gana cerca de un 26% más.</b>¹ Porque abarca más: más clientes, más proyectos, más mesas donde se decide.'),
            ('<b>En 2025 llegaron a Colombia más extranjeros que nunca, y 1 de cada 5 viene de Estados Unidos.</b>² El cliente, el socio o el inversionista de afuera no trae intérprete: pregunta, negocia y decide en inglés.'),
            ('<b>Sin inglés no se pierde el cargo. Se pierden conversaciones:</b> la negociación, el contacto que abre la puerta, el proyecto que se define en una llamada.'),
            ('<b>La inteligencia artificial traduce el contrato, pero no negocia por usted.</b> En la junta, en la reunión con el cliente y en la entrevista, el que habla es usted.')],
        lead='En un cargo directivo o profesional, eso es gran parte del avance y de los resultados.',
        big='A este nivel nadie aprende con una app: se aprende con un plan a su medida.',
        big2='Y si tiene una idea de negocio, la trabajamos con usted y la presenta en inglés.',
        fn='¹ DNP, <i>Bilingüismo laboral en Colombia</i>. ² MinCIT y Migración Colombia, enero a septiembre de 2025.',
        band='Dale la vuelta a la hoja: así es el programa individual y <b>cómo se arma sobre su agenda</b>.',
        band_px=250),
    'PROFESIONALES_RESPALDO': dict(
        compact=True, theme='light', label='ASÍ ES EL PROGRAMA INDIVIDUAL', sub='100 HORAS · UNO A UNO · CONVERSACIONES AVANZADAS EN SU ÁREA',
        h1='Su inglés, <em>en su agenda.</em>',
        intro=('<b>Entrenamos conversaciones avanzadas en su área laboral.</b> Armamos el plan a su medida, para que la clase se enfoque en los temas de los que usted ya estaría hablando si hablara inglés: la junta, la negociación, el cliente o el socio de afuera, '
               'la presentación de resultados, la entrevista. Usted fija los días y las horas cada semana. Antes de hablar de precios, le decimos cómo es:'),
        quote=('Nuestro objetivo es que salga hablando inglés en lo suyo. Esto es un entrenamiento, como prepararse para una maratón: desde el primer día habla, su profesor ve dónde puede mejorar y lo repetimos hasta que sale. '
               'Entre una sesión y otra, un audio corto que su profesor le devuelve con una mejora; usted elige cuándo. Empezamos con una prueba de nivel; <b>el avance lo va a notar usted en la reunión, no en un papel.</b> ¿Se le mide?'),
        cite='GERENCIA · HEIIU ENGLISH ACADEMY',
        after='¿Suena exigente? Lo es, a propósito. <b>Las 100 horas tienen 12 meses de vigencia desde la primera sesión; las que no use en ese plazo se pierden.</b> Dentro del plazo usted decide el ritmo, no el calendario de un grupo: con tres horas a la semana termina en unos ocho meses; con más, antes.',
        st=[], lead='', big='', big2='',
        why=[('SOBRE SU TRABAJO', 'El contenido sale de su día: el contrato que revisa, la junta del jueves, la propuesta que presenta, el correo que hay que contestar hoy. Nada de diálogos de libro.', False),
             ('PARA NEGOCIAR Y PRESENTARSE', 'Defender una cifra, presentar su propuesta, contar su historia profesional en un minuto. Se graba, se corrige y se repite hasta que suene seguro. <b>No prometemos el contrato ni el cargo: entrenamos la conversación.</b>', False),
             ('AVANCE QUE SE NOTA', 'Prueba de nivel al inicio para armar el plan, y cuenta clara de las horas usadas y las que le quedan. El avance lo nota usted donde importa: en la conversación.', False),
             ('LO QUE NO HACEMOS', 'No prometemos el ascenso ni la visa. No usamos diálogos de libro ni horarios fijos que no caben en una agenda llena. <b>Cupos limitados por disponibilidad de profesor.</b>', False)],
        band='Programa individual para directivos, ejecutivos y profesionales. <b>Agende una asesoría de 15 minutos.</b>',
        band_px=290),
    'DECIDIDO_FRENTE': dict(   # para el que YA decidio aprender ingles y esta escogiendo donde (decision de gerencia 27/10/2026); trato de tu
        compact=True, label='PARA EL QUE YA DECIDIÓ', sub='APRENDER INGLÉS ESTE AÑO',
        h1='Ya decidiste aprender inglés. <em>¿Vas a pagar donde te lo prometen o donde te lo garantizan?*</em>',
        st=[('<b>De cada 100 personas que bajan una app de inglés, 88 la dejan antes del mes.</b>¹ No es falta de ganas: es que nadie aprende un idioma solo.'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más.</b>² La diferencia no la hace empezar: la hace terminar con un nivel que se pueda demostrar.'),
            ('<b>Aquí hablas desde el primer día,</b> grabas un video corto cada día y tu profesor te lo devuelve con una mejora. Si faltas, te llamamos ese mismo día.'),
            ('<b>Prueba de entrada, prueba de salida y evaluador externo al cierre del nivel.</b> Lo que avanzas no es una sensación: queda por escrito.')],
        lead='Ya tomaste la decisión difícil. Para escoger dónde, basta una pregunta: ¿quién responde si no aprendes?',
        big='Garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.',
        big2='',
        fn='* Garantía por escrito, anexo al contrato de matrícula; aplican términos y condiciones. ¹ Retención a 30 días de la app de idiomas más descargada, estadísticas públicas 2026. ² DNP, <i>Bilingüismo laboral en Colombia</i>.',
        band='Dale la vuelta a la hoja: así entrenamos en Heiiu y <b>por qué podemos firmarlo</b>.',
        band_px=250),
    'DECIDIDO_RESPALDO': dict(
        compact=True, theme='light', label='ASÍ ES HEIIU', sub='LEE ESTO ANTES DE PAGAR EN CUALQUIER PARTE',
        h1='Academias hay muchas. <em>Esta te firma el resultado.</em>',
        intro=('A muchas academias les sale el negocio cuando pagas y dejas de ir. Nadie te llama, nadie te extraña, y a los tres meses la matrícula se volvió culpa. '
               '<b>En Heiiu queremos la parte difícil: que vengas, que te sueltes a hablar y que no te rindas.</b> Por eso te lo decimos antes de que pagues:'),
        quote=('Nuestro objetivo es que salgas hablando inglés. Si no se logra, algo está mal: o tú dejaste de entrenar, o nosotros no estamos cumpliendo. '
               'Esto es un entrenamiento en equipo, como prepararse para una maratón: desde el primer día hablas, tu profesor ve dónde puedes mejorar y lo repetimos hasta que sale. '
               'Por eso grabas un video corto todos los días y tu profesor te lo devuelve con una mejora. A cambio, la garantía por escrito: '
               '<b>si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.</b> ¿Te le mides a ese ritmo?'),
        cite='GERENCIA · HEIIU ENGLISH ACADEMY',
        after='¿Suena duro? Míralo al revés: <b>la única forma de perder la plata es dejar de entrenar.</b> Si entrenas, sales hablando inglés. Y si entrenas y no avanzas, te la devolvemos.',
        st=[], lead='', big='', big2='',
        why=[('TU META, COMO PROYECTO', 'Entras con lo que quieres lograr (una entrevista, un viaje, un negocio, el siguiente paso en tu trabajo) y desde el primer día lo trabajamos como un proyecto en inglés, con pasos y fecha.', False),
             ('AQUÍ NADIE DESAPARECE', 'Faltaste y no avisaste: te llamamos ese mismo día. No es persecución: es la parte menos chévere del coach, <b>la que esperamos no tener que hacer</b>.', False),
             ('SE NOTA, Y SE PUEDE MOSTRAR', 'Te grabamos el primer día y el último del nivel. Pon los dos videos juntos y no vas a necesitar que nadie te diga que avanzaste.', False),
             ('EL FINAL NO LO PONE TU PROFESOR', 'El examen de cierre del nivel lo aplica un evaluador externo. Grupos de máximo 16, en una academia con licencia desde 2012 y certificación ISO 9001.', False)],
        band='Escríbenos y agenda tu asesoría. <b>Te decimos cómo es antes de hablar de precios.</b>',
        band_px=290),

    'RECEPCION_FRENTE': dict(
        compact=True, label='INGLÉS PARA RECEPCIÓN', sub='CLÍNICAS · CONSULTORIOS · HOTELES · EMPRESAS',
        h1='La primera voz que oye el cliente eres tú. <em>¿También en inglés?</em>',
        st=[('<b>Cuando un extranjero llama o llega, no pregunta por el gerente: te pregunta a ti.</b> Y lo que pase en ese minuto decide si se queda.'),
            ('<b>En 2025 Colombia recibió más extranjeros que nunca, y 1 de cada 5 viene de Estados Unidos.</b>¹ Llegan a la clínica, al hotel y a la oficina con el mismo idioma.'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más</b> que quien hace el mismo trabajo sin él.² Las vacantes que dicen "recepcionista bilingüe" son para quien pueda demostrarlo.'),
            ('<b>La inteligencia artificial traduce, pero no contesta el teléfono por ti.</b>')],
        lead='Y no es falta de ganas: es que nadie aprende un idioma solo.',
        big='De cada 100 personas que bajan una app de inglés, 88 la dejan antes del mes.³',
        big2='Un idioma se entrena en equipo, con gente que no busca excusas: busca que la llamada salga bien. Y aquí te empujamos a pensar una idea de negocio propia y a contarla en inglés.',
        fn='¹ Ministerio de Comercio, Industria y Turismo y Migración Colombia, enero a septiembre de 2025. ² DNP, Archivos de Economía, <i>Bilingüismo laboral en Colombia</i>. ³ Retención a 30 días de la app de idiomas más descargada, estadísticas públicas 2026.',
        band='Dale la vuelta a la hoja: así entrenamos en Heiiu y <b>la beca con el nombre de tu empresa</b>.',
        band_px=250),
    'RECEPCION_RESPALDO': dict(
        compact=True, theme='light', label='ASÍ ES HEIIU', sub='INGLÉS PARA RECEPCIÓN',
        h1='Academias hay muchas. <em>Esta te firma el resultado.</em>',
        intro='A muchas academias les sale el negocio cuando pagas y dejas de ir. Nadie te llama, nadie te extraña, y a los tres meses la matrícula se volvió culpa. <b>En Heiiu queremos la parte difícil: que vengas, que te sueltes a hablar y que no te rindas.</b> Por eso te lo decimos antes de que pagues:', quote='Nuestro objetivo es que salgas hablando inglés. Si no se logra, algo está mal: o tú dejaste de entrenar, o nosotros no estamos cumpliendo. Esto es un entrenamiento en equipo, como prepararse para una maratón: desde el primer día hablas, tu profesor ve dónde puedes mejorar y lo repetimos hasta que sale. Por eso grabas un video corto todos los días y tu profesor te lo devuelve con una mejora. A cambio, la garantía por escrito: <b>si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.</b> ¿Te le mides a ese ritmo?', cite='GERENCIA · HEIIU ENGLISH ACADEMY', after='¿Suena duro? Míralo al revés: <b>la única forma de perder la plata es dejar de entrenar.</b> Si entrenas, sales hablando inglés. Y si entrenas y no avanzas, te la devolvemos.',
        st=[], lead='', big='', big2='',
        why=[('LAS FRASES DE TU PUESTO', 'Cada clase es una llamada o una llegada real: tomar los datos, dar una cita, explicar un procedimiento, pedir que espere sin que se moleste. Se repite hasta que sale sin pensar.', False),
             ('AQUÍ NADIE DESAPARECE', 'Faltaste y no avisaste: te llamamos ese mismo día. No es persecución: es la parte menos chévere del coach, <b>la que esperamos no tener que hacer</b>.', False),
             ('SE NOTA, Y SE PUEDE MOSTRAR', 'Te grabamos el primer día y el último del nivel. Pon los dos videos juntos y no vas a necesitar que nadie te diga que avanzaste. <b>Tu jefe tampoco tendrá que creerte: lo oye.</b>', False),
             ('PARA TU EMPRESA', 'Becas con el nombre de la clínica, el consultorio o la empresa para su equipo, <b>sin costo para la empresa</b>. Pregunta por el programa de alianzas.', False)],
        band='Grupos para equipos o programa individual. <b>Escríbenos y agenda tu asesoría.</b>',
        band_px=290),
    'EMPRESAS_FRENTE': dict(   # tesis del gerente de alianzas (25/10/2026): le devolvemos un mejor empleado, y se lo demostramos; de usted
        compact=True, label='PROGRAMA PARA EMPRESAS', sub='TALENTO HUMANO · GERENCIA',
        h1='¿Cuántos clientes de afuera ha perdido por el inglés? <em>No lo sabe: esos se van callados.</em>',
        st=[('<b>Presenta y sustenta.</b> Simulaciones de trabajo real, en inglés: un informe, una reunión, un cliente, una entrevista. Se graba y se corrige hasta que sale.'),
            ('<b>Cumple.</b> Tarea diaria con video enviado el mismo día. El porcentaje de entrega va en el reporte: usted ve quién cumple y quién no.'),
            ('<b>Llega a tiempo y no abandona.</b> Cada clase registra la hora de llegada; tres llegadas tarde cuentan como una falta. Asistencia mínima del 80%.'),
            ('<b>Va por una meta con fecha.</b> Prueba de entrada y de salida, y evaluador externo al cierre del nivel. Lo que avanza queda por escrito, no en una sensación.')],
        lead='Y con la beca para los hijos de sus empleados, su empresa le aporta a la región lo que más le falta: jóvenes estudiando. A cada uno lo empujamos a pensar como dueño: una idea de negocio, presentada en inglés.',
        big='Todo con garantía por escrito: si el estudiante cumple su parte y no avanza, le devolvemos el 100% del nivel.',
        big2='',
        band='Dale la vuelta a la hoja: por qué le conviene aunque su empresa no necesite inglés, y <b>las becas con su nombre, sin costo para la empresa</b>.',
        band_px=250),
    'EMPRESAS_RESPALDO': dict(   # por que le conviene aunque no necesite ingles: bienestar del empleado y su familia (datos con fuente), gratitud, el trato
        compact=True, theme='light', label='AUNQUE SU EMPRESA NO NECESITE INGLÉS', sub='BECAS CON SU NOMBRE · SIN COSTO PARA LA EMPRESA',
        h1='Puede que su empresa no necesite inglés. <em>Su gente sí.</em>',
        intro='Un trabajador agradece lo que la empresa hace por su desarrollo. Y lo que hace por su hijo no lo olvida: <b>la educación de los hijos está entre lo que más anhela.</b>⁴ El trato, en una frase:',
        quote=('El colaborador firma su contrato y asume sus condiciones, para él o para su hijo; la empresa no asume ninguna obligación económica. La empresa postula, recibe el reporte periódico y entrega los certificados de beca con su nombre. '
               'Y a cada estudiante le firmamos lo mismo que a todos: <b>si cumple su parte y no avanza, le devolvemos el 100% del nivel.</b>'),
        cite='GERENCIA · HEIIU ENGLISH ACADEMY',
        st=[('<b>La mitad de internet está en inglés: el 49,5% de los sitios web.</b>¹ En español, el 6%. El que lee inglés piensa con el doble de información.'),
            ('<b>1 de cada 5 jóvenes en Colombia ni estudia ni trabaja: 2,3 millones.</b>² Un hijo de su empleado en un programa que exige asistencia y video diario está ocupado en algo que lo saca adelante.'),
            ('<b>Un empleado preocupado por su casa no rinde.</b> El 34% de los trabajadores colombianos se ha ausentado por ansiedad o depresión.³')],
        lead='¿Y si un colaborador no cumple? Usted también se entera: el reporte lo dice. Y cuando busque gente, le referimos estudiantes con ese historial, con su autorización.',
        big='',
        big2='',
        fn='¹ W3Techs, octubre de 2026, sitios web por idioma principal. ² DANE, Gran Encuesta Integrada de Hogares, jóvenes de 15 a 28 años, septiembre a noviembre de 2025. ³ Estudio de Seguros Sura sobre salud mental laboral, 2025. ⁴ Encuesta Provokers y Apprecio a trabajadores de Colombia, México, Chile y Perú.',
        band='Becas con el nombre de su empresa para su gente y sus hijos, <b>sin costo para la empresa</b>. Agende una reunión de 20 minutos.',
        band_px=290),
    'EMPRESAS_CORTA': dict(   # version corta de una sola cara (decision de gerencia 25/10/2026): tesis del gerente de alianzas + competencias medibles + hijos/region + garantia + beca sin costo; de usted
        compact=True, label='PROGRAMA PARA EMPRESAS', sub='TALENTO HUMANO · GERENCIA',
        h1='¿Cuántos clientes de afuera ha perdido por el inglés? <em>No lo sabe: esos se van callados.</em>',
        st=[('<b>Presenta y sustenta.</b> Simulaciones de trabajo real, en inglés: un informe, una reunión, un cliente, una entrevista. Se graba y se corrige hasta que sale.'),
            ('<b>Cumple.</b> Tarea diaria con video enviado el mismo día. El porcentaje de entrega va en el reporte: usted ve quién cumple y quién no.'),
            ('<b>Llega a tiempo y no abandona.</b> Cada clase registra la hora de llegada; tres llegadas tarde cuentan como una falta. Asistencia mínima del 80%.'),
            ('<b>Va por una meta con fecha.</b> Prueba de entrada y de salida, y evaluador externo al cierre del nivel. Lo que avanza queda por escrito.')],
        lead='Un trabajador agradece lo que la empresa hace por él, y lo que hace por su hijo no lo olvida. Con la beca para los hijos de sus empleados, su empresa le aporta a la región jóvenes estudiando, empujados a pensar como dueños: una idea de negocio, presentada en inglés.',
        big='Todo con garantía por escrito: si cumple su parte y no avanza, le devolvemos el 100% del nivel.',
        big2='',
        band='Becas con el nombre de su empresa para su gente y sus hijos, <b>sin costo para la empresa</b>. La empresa postula y recibe el reporte de cada uno. Agende una reunión de 20 minutos.',
        band_px=290),
    # ---------------- VERSIONES CORTAS (una sola cara, digitales, para WhatsApp) ----------------
    'HOTELERIA_CORTA': dict(
        compact=True, label='INGLÉS PARA HOTELERÍA Y TURISMO', sub='HOTELES · RESTAURANTES · AGENCIAS · GUÍAS',
        h1='El turista habla inglés. <em>¿Lo recibes tú o llamas a otro?</em>',
        st=[('<b>En 2025 Colombia recibió más extranjeros que nunca,</b> y 1 de cada 5 viene de Estados Unidos.¹ Pide, reclama y agradece en inglés.'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más</b> que quien hace el mismo trabajo sin él.²'),
            ('<b>Las escenas de tu puesto, en inglés:</b> el check-in, la reserva por teléfono, la mesa que pide la cuenta, la queja por el aire. Se repite hasta que sale sin pensar.'),
            ('<b>Se nota, y se puede mostrar:</b> te grabamos el primer día y el último del nivel. Tu jefe no tendrá que creerte: lo oye.')],
        lead='Aprender inglés no es fácil ni siempre divertido. Pero aquí nadie desaparece: si faltas, te llamamos. Y aquí te empujamos a pensar una idea de negocio propia y a contarla en inglés.', big='Garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.', big2='', fn='¹ Ministerio de Comercio, Industria y Turismo y Migración Colombia, enero a septiembre de 2025. ² DNP, Archivos de Economía, <i>Bilingüismo laboral en Colombia</i>.',
        band='Grupos para equipos o programa individual. Becas con el nombre de tu hotel, restaurante o agencia, <b>sin costo para la empresa</b>. Escríbenos y agenda tu asesoría.',
        band_px=290),
    'MEDICOS_DIRECTIVOS_CORTA': dict(
        compact=True, label='PROGRAMA INDIVIDUAL', sub='MÉDICOS · ESPECIALIZACIONES · ALTA DIRECCIÓN',
        h1='El paciente de afuera ya llegó. <em>¿Le paga la consulta a usted o al que sí habla inglés?</em>',
        st=[('<b>El 92% de los artículos de ciencias de la salud está en inglés.</b>¹ El congreso, el protocolo y la convocatoria llegan primero en ese idioma.'),
            ('<b>En 2025 llegaron a Colombia más extranjeros que nunca, y 1 de cada 5 viene de Estados Unidos.</b>² El paciente de afuera no trae intérprete: pregunta, entiende y decide en inglés.'),
            ('<b>Entrenamos conversaciones avanzadas en su área laboral:</b> la junta, el congreso, el paciente o el cliente de afuera, la entrevista de la especialización. Plan a su medida y en su agenda, con audios entre sesiones que su profesor devuelve con una mejora.')],
        lead='Sin inglés no se pierde un título. Se pierden conversaciones: el networking, los resultados que vale la pena contar, entender lo que otros quieren transmitir.',
        big='100 horas, uno a uno. Entrenamos lo que importa: la conversación que abre pacientes, negocios y contactos.',
        big2='Y si tiene una idea de negocio, la trabajamos con usted y la presenta en inglés.', fn='¹ Elsevier, con datos de PubMed. ² Ministerio de Comercio, Industria y Turismo y Migración Colombia, enero a septiembre de 2025.',
        band='Programa individual para médicos, profesionales y directivos. <b>Cupos limitados por disponibilidad de profesor.</b> Agende una asesoría de 15 minutos.',
        band_px=290),
    'PROFESIONALES_CORTA': dict(
        compact=True, label='PROGRAMA INDIVIDUAL', sub='DIRECTIVOS · EJECUTIVOS · INGENIEROS · ABOGADOS',
        h1='El cliente de afuera ya llegó. <em>¿Le firma el contrato a usted o al que sí habla inglés?</em>',
        st=[('<b>Quien certifica su inglés gana cerca de un 26% más.</b>¹ Porque abarca más: más clientes, más proyectos, más mesas donde se decide.'),
            ('<b>En 2025 llegaron a Colombia más extranjeros que nunca, y 1 de cada 5 viene de Estados Unidos.</b>² El cliente, el socio o el inversionista de afuera no trae intérprete: pregunta, negocia y decide en inglés.'),
            ('<b>Entrenamos conversaciones avanzadas en su área laboral:</b> la junta, la negociación, el cliente o el socio de afuera, la entrevista. Plan a su medida y en su agenda, con audios entre sesiones que su profesor devuelve con una mejora.')],
        lead='Sin inglés no se pierde el cargo. Se pierden conversaciones: la negociación, el contacto que abre la puerta, el proyecto que se define en una llamada.',
        big='100 horas, uno a uno. Entrenamos lo que importa: la conversación que abre clientes, negocios y contactos.',
        big2='Y si tiene una idea de negocio, la trabajamos con usted y la presenta en inglés.', fn='¹ DNP, <i>Bilingüismo laboral en Colombia</i>. ² MinCIT y Migración Colombia, enero a septiembre de 2025.',
        band='Programa individual para directivos, ejecutivos y profesionales. <b>Cupos limitados por disponibilidad de profesor.</b> Agende una asesoría de 15 minutos.',
        band_px=290),
    'DECIDIDO_CORTA': dict(
        compact=True, label='PARA EL QUE YA DECIDIÓ', sub='APRENDER INGLÉS ESTE AÑO',
        h1='Ya decidiste aprender inglés. <em>¿Vas a pagar donde te lo prometen o donde te lo garantizan?*</em>',
        st=[('<b>De cada 100 personas que bajan una app de inglés, 88 la dejan antes del mes.</b>¹ No es falta de ganas: es que nadie aprende un idioma solo.'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más.</b>² La diferencia no la hace empezar: la hace terminar con un nivel que se pueda demostrar.'),
            ('<b>Aquí hablas desde el primer día,</b> grabas un video corto cada día y tu profesor te lo devuelve con una mejora. Si faltas, te llamamos. El final del nivel lo aplica un evaluador externo.')],
        lead='Ya tomaste la decisión difícil. Para escoger dónde, basta una pregunta: ¿quién responde si no aprendes?',
        big='Garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.',
        big2='', fn='* Garantía por escrito, anexo al contrato de matrícula; aplican términos y condiciones. ¹ Retención a 30 días de la app de idiomas más descargada, estadísticas públicas 2026. ² DNP, <i>Bilingüismo laboral en Colombia</i>.',
        band='Grupos de máximo 16. <b>Escríbenos y agenda tu asesoría:</b> te decimos cómo es antes de hablar de precios.',
        band_px=290),
    'RECEPCION_CORTA': dict(
        compact=True, label='INGLÉS PARA RECEPCIÓN', sub='CLÍNICAS · CONSULTORIOS · HOTELES · EMPRESAS',
        h1='La primera voz que oye el cliente eres tú. <em>¿También en inglés?</em>',
        st=[('<b>Cuando un extranjero llama o llega, no pregunta por el gerente: te pregunta a ti.</b> Y en 2025 llegaron más que nunca; 1 de cada 5, de Estados Unidos.¹'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más.</b>² Las vacantes que dicen "recepcionista bilingüe" son para quien pueda demostrarlo.'),
            ('<b>Las frases de tu puesto, en inglés:</b> tomar los datos, dar una cita, explicar un procedimiento, pedir que espere sin que se moleste. Se repite hasta que sale sin pensar.'),
            ('<b>Se nota, y se puede mostrar:</b> te grabamos el primer día y el último del nivel. Tu jefe no tendrá que creerte: lo oye.')],
        lead='Aprender inglés no es fácil ni siempre divertido. Pero aquí nadie desaparece: si faltas, te llamamos. Y aquí te empujamos a pensar una idea de negocio propia y a contarla en inglés.', big='Garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.', big2='', fn='¹ Ministerio de Comercio, Industria y Turismo y Migración Colombia, enero a septiembre de 2025. ² DNP, Archivos de Economía, <i>Bilingüismo laboral en Colombia</i>.',
        band='Grupos para equipos o programa individual. Becas con el nombre de tu clínica, consultorio o empresa, <b>sin costo para la empresa</b>. Escríbenos y agenda tu asesoría.',
        band_px=290),
    'ASESORAS_CORTA': dict(   # digital, la reenvia la asesora de la entidad aliada junto con SU enlace; por eso no lleva numero
        compact=True, label='HEIIU ENGLISH ACADEMY', sub='BUCARAMANGA',
        h1='¿Otro año sin plata y sin rumbo? <em>Aquí alguien cree en ti y empuja tu proyecto.</em>',
        st=[('<b>De cada 8 jóvenes que terminan el colegio en Colombia, solo 1 sale con un inglés que le sirva.</b>¹ Los otros 7 lo tienen pendiente de adultos.'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más.</b>² ¿Por qué? Porque abarca más: más vacantes a las que aplicar, más clientes a los que vender, más países a los que ir.'),
            ('<b>1 de cada 5 jóvenes en Colombia ni estudia ni trabaja.</b>³ No es falta de capacidad: con inglés y disciplina ese mismo joven puede trabajar remoto, vender afuera, estudiar becado o montar algo propio.'),
            ('<b>Hay muchas academias de inglés. Esta te firma el resultado por escrito.</b> Hablas desde el primer día, grabas un video corto cada día, y si faltas te llamamos.')],
        lead='Con el código de tu asesora puedes aplicar a una beca, y tu proyecto lo trabajamos contigo en inglés.',
        big='Garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.', big2='',
        fn='¹ Saber 11 de 2025, análisis de la Universidad Icesi. ² DNP, <i>Bilingüismo laboral en Colombia</i>. ³ DANE, GEIH 2025, 15 a 28 años.',
        band='Escríbenos desde el enlace que te mandó tu asesora: <b>tu código ya va en el mensaje. Sin código no hay beca.</b>',
        tel='Escríbenos por el enlace de tu asesora', tel_small=True, band_px=290),
    'ASESORAS_CORTA_QR': dict(   # digital con QR, una por codigo (decision de gerencia 27/10/2026): la asesora la abre en SU celular y el joven la escanea; reemplaza la hoja impresa mientras no haya imprenta
        compact=True, label='HEIIU ENGLISH ACADEMY', sub='BUCARAMANGA',
        h1='¿Otro año sin plata y sin rumbo? <em>Aquí alguien cree en ti y empuja tu proyecto.</em>',
        st=[('<b>De cada 8 jóvenes que terminan el colegio en Colombia, solo 1 sale con un inglés que le sirva.</b>¹ Los otros 7 lo tienen pendiente de adultos.'),
            ('<b>Quien certifica su inglés gana cerca de un 26% más.</b>² ¿Por qué? Porque abarca más: más vacantes a las que aplicar, más clientes a los que vender, más países a los que ir.'),
            ('<b>1 de cada 5 jóvenes en Colombia ni estudia ni trabaja.</b>³ No es falta de capacidad: con inglés y disciplina ese mismo joven puede trabajar remoto, vender afuera, estudiar becado o montar algo propio.'),
            ('<b>Hay muchas academias de inglés. Esta te firma el resultado por escrito.</b> Hablas desde el primer día, grabas un video corto cada día, y si faltas te llamamos.')],
        lead='Con el código de tu asesora puedes aplicar a una beca, y tu proyecto lo trabajamos contigo en inglés.',
        big='Garantía por escrito: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.', big2='',
        fn='¹ Saber 11 de 2025, análisis de la Universidad Icesi. ² DNP, <i>Bilingüismo laboral en Colombia</i>. ³ DANE, GEIH 2025, 15 a 28 años.',
        band='Escanea este código en el celular de tu asesora: el mensaje sale listo. <b>Con su código aplicas a la beca; sin código no hay beca.</b>',
        por_codigo=True, band_px=290),
    # ---------------- PADRES (la asesora de la entidad aliada le habla al papa del que sale del colegio o del que aun no arranca) ----------------
    'PADRES_FRENTE': dict(   # misma tesis que la de empresas, volteada al papa: le devolvemos un mejor hijo; solo imprenta (10x15), de usted
        compact=True, imprenta=True, label='PARA PADRES', sub='DEL QUE SALE DEL COLEGIO · DEL QUE AÚN NO ARRANCA',
        h1='¿Cinco años de matrícula en una carrera que su hijo no tiene clara? <em>Primero el inglés.</em>',
        st=[('<b>1 de cada 5 jóvenes en Colombia ni estudia ni trabaja.</b>¹ No es falta de capacidad: es falta de una meta con fecha y de alguien que le exija. Eso es lo que entrenamos.'),
            ('<b>Si acaba de salir del colegio, no se apresure a elegir universidad.</b> Hay carreras que cambian antes de terminarlas y títulos que las empresas ya no piden. Un año aprendiendo inglés con disciplina no se pierde: abre la beca, el intercambio y la carrera que sí es.'),
            ('<b>De cada 8 jóvenes que terminan el colegio, solo 1 sale con un inglés que le sirva.</b>² Los otros 7 llegan a la universidad y al primer empleo con eso pendiente.'),
            ('<b>Lo que medimos para que aprenda inglés es lo que usted quiere ver en casa:</b> llegar a tiempo, cumplir la tarea diaria, no rendirse, ir por una meta con fecha. Y usted recibe el reporte.')],
        lead='Y lo empujamos a pensar una idea de negocio propia y a contarla en inglés.',
        big='Garantía por escrito: si cumple su parte y no avanza, le devolvemos el 100% del nivel.',
        big2='', fn='¹ DANE, Gran Encuesta Integrada de Hogares, jóvenes de 15 a 28 años, septiembre a noviembre de 2025. ² Pruebas Saber 11 de 2025, análisis del Observatorio de Realidades Educativas de la Universidad Icesi.',
        band='Dele la vuelta a la hoja: cómo entrenamos y <b>la beca a la que su hijo aplica con el código de su asesora</b>.',
        tel='Cómo escribirnos: <b>al respaldo</b>', band_px=250),
    'PADRES_RESPALDO': dict(   # un respaldo por codigo de asesora, con su QR; solo imprenta
        compact=True, imprenta=True, theme='light', label='ASÍ ES HEIIU', sub='LEA ESTO ANTES DE DECIDIR',
        h1='Academias hay muchas. <em>Esta le firma el resultado.</em>',
        intro=('A muchas academias les sale el negocio cuando usted paga y su hijo deja de ir. Nadie lo llama, nadie lo extraña, y a los tres meses la matrícula se volvió una pelea en la casa. '
               '<b>En Heiiu queremos la parte difícil: que venga, que se suelte a hablar y que no se rinda.</b> Por eso se lo decimos antes de que pague:'),
        quote=('Nuestro objetivo es que su hijo salga hablando inglés. Si no se logra, algo está mal: o él dejó de entrenar, o nosotros no estamos cumpliendo. '
               'Esto es un entrenamiento en equipo, como prepararse para una maratón: desde el primer día habla, su profesor ve dónde puede mejorar y lo repetimos hasta que sale. '
               'Por eso graba un video corto todos los días y su profesor se lo devuelve con una mejora. A cambio, la garantía por escrito: '
               '<b>si cumple su parte y no avanza, le devolvemos el 100% del nivel.</b> ¿Se le mide él a ese ritmo?'),
        cite='GERENCIA · HEIIU ENGLISH ACADEMY',
        after='¿Suena duro? Mírelo al revés: <b>la única forma de perder la plata es que deje de entrenar.</b> Y usted se entera antes que nadie: el reporte llega a la casa.',
        st=[], lead='', big='', big2='',
        why=[('AQUÍ NADIE DESAPARECE', 'Faltó y no avisó: lo llamamos ese mismo día, y usted también se entera. No es persecución: es la parte menos chévere del coach, <b>la que esperamos no tener que hacer</b>.', False),
             ('SE NOTA, Y SE PUEDE MOSTRAR', 'Lo grabamos el primer día y el último del nivel. Ponga los dos videos juntos: <b>no va a necesitar que nadie le diga que avanzó.</b>', False),
             ('PUERTAS AFUERA, PERO SEGURAS', 'Cuando su inglés dé, lo conectamos con operadores verificados de programas en el exterior: au pair, campamentos, trabajo de temporada. Solo puertas seguras.', False),
             ('LA CONTRASEÑA', 'Aquí entra cualquiera que traiga una sola cosa: <b>el amor por salir adelante</b>. Sin excusas, con la meta al frente, rodeado de gente que quiere lo mismo.', False)],
        band='Escanee el código de su asesora: el mensaje sale listo con su código. <b>Con él su hijo aplica a la beca; sin código no hay beca.</b>',
        tel_qr='Escanee el código de su asesora: <b>%s</b>', por_codigo=True, band_px=290),
    'PADRES_CORTA': dict(   # digital, la reenvia la asesora con SU enlace; sin numero
        compact=True, label='PARA PADRES', sub='DEL QUE SALE DEL COLEGIO · DEL QUE AÚN NO ARRANCA',
        h1='¿Cinco años de matrícula en una carrera que su hijo no tiene clara? <em>Primero el inglés.</em>',
        st=[('<b>1 de cada 5 jóvenes en Colombia ni estudia ni trabaja.</b>¹ No es falta de capacidad: es falta de una meta con fecha y de alguien que le exija.'),
            ('<b>Si acaba de salir del colegio, no se apresure a elegir universidad.</b> Un año aprendiendo inglés con disciplina no se pierde: abre la beca, el intercambio y la carrera que sí es.'),
            ('<b>Lo que medimos es lo que usted quiere ver en casa:</b> llegar a tiempo, cumplir la tarea diaria, no rendirse, ir por una meta con fecha. Y usted recibe el reporte.'),
            ('<b>Si falta, lo llamamos ese mismo día</b> y usted también se entera. Lo grabamos el primer día y el último del nivel: el avance se oye.')],
        lead='Con el código de su asesora, su hijo puede aplicar a una beca. Y lo empujamos a pensar una idea de negocio propia y a contarla en inglés.',
        big='Garantía por escrito: si cumple su parte y no avanza, le devolvemos el 100% del nivel.',
        big2='', fn='¹ DANE, Gran Encuesta Integrada de Hogares, jóvenes de 15 a 28 años, septiembre a noviembre de 2025. ² Pruebas Saber 11 de 2025, análisis del Observatorio de Realidades Educativas de la Universidad Icesi.',
        band='Escríbanos desde el enlace que le mandó su asesora: <b>el código ya va en el mensaje. Sin código no hay beca.</b>',
        tel='Escríbanos por el enlace de su asesora', tel_small=True, band_px=290),
    # ---------------- CALLE (volanteo: una idea, tres lineas, el numero; sin datos ni precios) ----------------
    'CALLE_A': dict(
        calle=True, label='HEIIU ENGLISH ACADEMY', sub='BUCARAMANGA',
        h1='El que habla inglés abarca más: <em>más vacantes, más clientes, más países.</em>',
        st=[('Hablas inglés desde el primer día, con un profesor que te corrige ahí mismo.'),
            ('Un coach que no te deja rendirte. Aquí nadie entrena solo.'),
            ('Te empujamos a pensar una idea de negocio y a contarla en inglés.'),
            ('Y lo que no cabe aquí: becas, convenios, programas en el exterior. Y un enfoque de carácter y liderazgo: <b>te preparamos para la vida, no para un examen.</b> Escribe y pregunta.')],
        lead='Y lo firmamos: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.', big='', big2='',
        band='Grupos y programa individual, en Bucaramanga. <b>Escríbenos y agenda tu asesoría.</b>',
        band_px=300),
    'CALLE_B': dict(
        calle=True, label='HEIIU ENGLISH ACADEMY', sub='BUCARAMANGA',
        h1='¿Nadie sabe cuál es el camino? <em>Los mejores piden inglés.</em>',
        st=[('Hablas inglés desde el primer día, con un profesor que te corrige ahí mismo.'),
            ('Un coach que no te deja rendirte, y una idea de negocio propia contada en inglés.'),
            ('Becas, convenios, programas en el exterior. Carácter y liderazgo: <b>te preparamos para la vida, no para un examen.</b>')],
        lead='Y lo firmamos: si cumples tu parte y no avanzas, te devolvemos el 100% del nivel.', big='', big2='',
        band='Grupos y programa individual, en Bucaramanga. <b>Escríbenos y agenda tu asesoría.</b>',
        band_px=300),
}


LIGHT = """
body { background: #FFF8E7; color: #1C1714 }
.page { background: radial-gradient(900px 700px at 100% -10%, rgba(229,76,9,.16), rgba(229,76,9,0) 60%), #FFF8E7 }
.label { color: #E54C09 } .label span { color: rgba(28,23,20,.55) }
h1 { color: #1C1714 } h1 em { color: #E54C09 }
ol.st li { border-color: rgba(28,23,20,.14) } ol.st .n { color: #E54C09 } ol.st p { color: rgba(28,23,20,.78) } ol.st p b { color: #1C1714 }
.pivot .lead { color: #E54C09 } .pivot .big { color: #1C1714 } .pivot .big2 { color: rgba(28,23,20,.85) }
.why h2 { color: #E54C09 } .why .card { background: #FFFFFF; border-color: #E8DCC8 } .why .card.full { background: rgba(251,201,0,.22); border-color: #E6B800 }
.why .k { color: #E54C09 } .why p { color: rgba(28,23,20,.85) } .why p b { color: #1C1714 }
blockquote { border-left-color: #E54C09; background: rgba(229,76,9,.06); color: #1C1714 } blockquote cite { color: #E54C09 }
.intro { color: rgba(28,23,20,.88) } .intro b { color: #E54C09 }
.fn { color: rgba(28,23,20,.55); border-color: rgba(28,23,20,.14) }
"""

CALLE = """
h1 { font-size: 98px; line-height: 1.02; margin-top: 36px }
.rule { margin: 36px 0 22px 0 }
ol.st li { padding: 18px 0 16px 0; grid-template-columns: 70px 1fr }
ol.st .n { font-size: 28px; padding-top: 8px }
ol.st p { font-size: 36px; line-height: 1.22; color: #FFF8E7; font-weight: 400 }
.pivot { padding-top: 30px } .pivot .lead { font-size: 38px; line-height: 1.25 }
.band p { font-size: 30px; line-height: 1.3 }
.cta .tel { font-size: 56px } .cta .tel small { font-size: 26px }
"""

COMPACT = """
.top { padding-top: 56px; padding-bottom: 44px } h1 { font-size: 70px; margin-top: 26px } .rule { margin: 30px 0 26px 0 }
ol.st li { padding: 19px 0 17px 0 } ol.st p { font-size: 28px; line-height: 1.32 }
.pivot { padding-top: 26px } .pivot .lead { font-size: 33px } .pivot .big { font-size: 48px; margin-top: 10px } .pivot .big2 { font-size: 36px; margin-top: 18px } .fn { margin-top: 14px }
.why { margin-top: 18px } .why h2 { font-size: 38px; margin-bottom: 14px } .why .grid { gap: 12px }
.why .card { padding: 14px 19px 15px 19px; border-radius: 14px } .why .k { font-size: 17px; margin-bottom: 4px } .why p { font-size: 21.5px; line-height: 1.25 }
.intro { font-size: 25px; line-height: 1.33; margin-bottom: 18px } blockquote { font-size: 25px; line-height: 1.33; padding: 18px 24px 18px 26px } blockquote cite { margin-top: 8px }
"""


def html(c):
    st = ''.join('<li><span class="n">0%d</span><p>%s</p></li>' % (i + 1, t) for i, t in enumerate(c['st']))
    st = ('<ol class="st">%s</ol>' % st) if st else ''
    big2 = '<p class="big2">%s</p>' % c['big2'] if c['big2'] else ''
    logo = pathlib.Path(LOGO_NAR).as_uri()
    if c.get('qr'):
        derecha = '<div class="qrbox"><img src="%s"><span>%s</span></div>' % (pathlib.Path(qr_png(c['qr'])).as_uri(), c['qr'])
        tel = (c.get('tel_qr') or 'Escanea el código de tu asesora: <b>%s</b>') % c['qr']
    elif c.get('codigo'):
        derecha = '<div class="codigo"><span class="k">CÓDIGO DE TU ASESORA</span><span class="v">C-<span></span></span></div>'; tel = '<small>Escríbenos</small>' + LINEA
    else:
        derecha = '<img class="logo" src="%s">' % logo
        tel = c['tel'] if c.get('tel') else '<small>Escríbenos</small>' + LINEA
    why = ''
    quote = ('<blockquote>%s<cite>%s</cite></blockquote>' % (c['quote'], c.get('cite', ''))) if c.get('quote') else ''
    if c.get('intro'): quote = '<p class="intro">%s</p>' % c['intro'] + quote
    if c.get('after'): quote += '<p class="intro after">%s</p>' % c['after']
    fn = ('<div class="fn">%s</div>' % c['fn']) if c.get('fn') else ''
    if c.get('why'):
        cards = ''.join('<div class="card%s"><div class="k">%s</div><p>%s</p></div>' % (' full' if full else '', k, t) for k, t, full in c['why'])
        why = '<div class="why">%s<div class="grid">%s</div></div>' % (('<h2>%s</h2>' % c['why_h2']) if c.get('why_h2') else '', cards)
    return ('<!doctype html><html><head><meta charset="utf-8"><style>%s%s%s%s</style></head><body><div class="page">'
            '<div class="top"><div class="label">%s<span>%s</span></div><h1>%s</h1><div class="rule"></div>%s'
            '%s<div class="pivot"><p class="lead">%s</p><p class="big">%s</p>%s</div>%s%s</div>'
            '<div class="band%s"><p>%s</p>%s'
            '<div class="cta"><div class="tel">%s</div><div class="ig">%s<b>Bucaramanga</b></div></div></div>'
            '</div></body></html>') % (CSS % dict(W=W, H=c.get('H', H), BAND=c['band_px']), COMPACT if c.get('compact') else '', LIGHT if c.get('theme') == 'light' else '', CALLE if c.get('calle') else '', c['label'], c['sub'], c['h1'], quote, st, c['lead'], c['big'], big2, why, fn,
                                       (' qr' if c.get('qr') else '') + (' tels' if c.get('tel_small') else ''), c['band'], derecha, tel, IG)


CARPETAS = (('GENERAL_ASESORAS', 'jovenes'), ('ASESORAS', 'jovenes'), ('PADRES', 'padres'), ('EMPRESAS', 'empresas'), ('HOTELERIA', 'hoteleria'),
            ('RECEPCION', 'recepcion'), ('MEDICOS', 'medicos'), ('PROFESIONALES', 'profesionales'), ('DECIDIDO', 'ya_decidio'), ('CALLE', 'calle'), ('MANIFIESTO', 'manifiesto'))


def carpeta(nombre):
    """Subcarpeta por publico (decision de gerencia 27/10/2026): volantes/{jovenes,padres,empresas,...}/PIEZA_*.png, y su imprenta/ adentro."""
    for pref, c in CARPETAS:
        if nombre.startswith(pref): return c
    return 'otros'


def render(nombre, c):
    if c.get('por_codigo') and not c.get('qr'):
        for cod in codigos(): render('%s_%s' % (nombre, cod), dict(c, qr=cod, por_codigo=False))
        return
    hp = os.path.join(WORK, nombre + '.html'); png = os.path.join(WORK, nombre + '.png')
    open(hp, 'w', encoding='utf-8').write(html(c))
    if os.path.exists(png): os.remove(png)
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--force-device-scale-factor=1',
                    '--user-data-dir=' + os.path.join(WORK, 'profile'), '--window-size=%d,%d' % (W, c.get('H', H)),
                    '--screenshot=' + png, pathlib.Path(hp).as_uri()], capture_output=True, timeout=90)
    assert os.path.exists(png), 'Edge no generó ' + png
    if nombre.startswith('GENERAL_ASESORAS') or c.get('imprenta'):   # hojas que solo se imprimen: van unicamente a imprenta/, con sangrado
        sangrado(nombre, png); return
    out = os.path.join(OUTDIR, carpeta(nombre), 'PIEZA_%s.png' % nombre)
    os.makedirs(lp(os.path.dirname(out)), exist_ok=True); os.makedirs(lp(os.path.join(COPIA, carpeta(nombre))), exist_ok=True)
    for p in (out, os.path.join(COPIA, carpeta(nombre), os.path.basename(out))):
        try: shutil.copy(png, lp(p)); print('OK', p)
        except OSError: p2 = p.replace('.png', '_v2.png'); shutil.copy(png, lp(p2)); print('ABIERTA ->', p2)   # abierta en el visor: PermissionError o errno 22


def lp(path):
    """Ruta larga de Windows (la carpeta del gerente supera los 260 caracteres con las hojas de imprenta)."""
    path = os.path.abspath(path)
    pref = chr(92) * 2 + '?' + chr(92)
    return path if path.startswith(pref) else pref + path


def sangrado(nombre, src, mm=3, ppp=274):
    """Version para imprenta 10x15: extiende los bordes `mm` milimetros replicando el borde (sangrado para el corte).
    1080 px / 10 cm = 274 ppp -> 3 mm = 32 px por lado. Salida: volantes/{publico}/imprenta/PIEZA_{nombre}_10x15_s3mm.png (git + carpeta del gerente; nombre corto por el limite de ruta de Windows)."""
    im = Image.open(src).convert('RGB')
    b = round(mm / 25.4 * ppp); w, h = im.size
    out = Image.new('RGB', (w + 2 * b, h + 2 * b)); out.paste(im, (b, b))
    out.paste(im.crop((0, 0, w, 1)).resize((w, b)), (b, 0)); out.paste(im.crop((0, h - 1, w, h)).resize((w, b)), (b, h + b))
    out.paste(im.crop((0, 0, 1, h)).resize((b, h)), (0, b)); out.paste(im.crop((w - 1, 0, w, h)).resize((b, h)), (w + b, b))
    for (x, y, px, py) in ((0, 0, 0, 0), (w + b, 0, w - 1, 0), (0, h + b, 0, h - 1), (w + b, h + b, w - 1, h - 1)):
        out.paste(Image.new('RGB', (b, b), im.getpixel((px, py))), (x, y))
    for d in (os.path.join(OUTDIR, carpeta(nombre), 'imprenta'), os.path.join(COPIA, carpeta(nombre), 'imprenta')):
        os.makedirs(lp(d), exist_ok=True); p = os.path.join(d, 'PIEZA_%s_10x15_s3mm.png' % nombre); out.save(lp(p), dpi=(ppp, ppp)); print('IMPRENTA', p)


if __name__ == '__main__':
    import sys
    logo_transparente()
    for k in (sys.argv[1:] or PIEZAS): render(k, PIEZAS[k])
