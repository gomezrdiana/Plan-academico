# -*- coding: utf-8 -*-
"""Piezas editoriales de conciencia (reemplazan los volantes PIL de gen_volantes_segmentos.py, retirado el 24/10/2026).
Una pieza MANIFIESTO (por qué el inglés y los hábitos suben de valor cuando casi todo lo demás lo pierde) y cuatro piezas
por segmento con el mismo sistema visual: PROFESIONALES (médicos, profesionales, directivos), MEDICINA (entrevistas de
admisión), ATENCION (recepción, salud, hoteles, turismo, restaurantes) y PADRES.
Se escriben en HTML/CSS (Constantia + Segoe UI + Bahnschrift, fuentes del sistema) y se renderizan a PNG 1080x1620 con
Microsoft Edge sin ventana. Reglas: sin precio, sin modalidad ni horarios, sin "fácil/rápido", sin empleo/visa/nativos,
sin nombres de competidores, sin "únicos", garantía por escrito. Contacto: línea de alianzas 316 768 8793 (el gerente de
alianzas reparte las piezas), nunca la línea principal.
Salida (git): recursos/comercial/campanas/volantes/PIEZA_*.png + copia en la carpeta del gerente de alianzas / volantes.
Uso: python generadores/comercial/gen_piezas_conciencia.py"""
import os, shutil, subprocess, pathlib, tempfile
from PIL import Image

ROOT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
LOGO_NAR = os.path.join(ROOT, r'recursos\marca heiiu\logo_heiiu_sobre_naranja.png')
LOGO_TR = os.path.join(ROOT, r'recursos\marca heiiu\logo_heiiu_transparente.png')
OUTDIR = os.path.join(ROOT, r'recursos\comercial\campanas\volantes')
COPIA = os.path.join(ROOT, r'recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza\volantes')
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
WORK = os.path.join(tempfile.gettempdir(), 'heiiu_piezas'); os.makedirs(WORK, exist_ok=True)
LINEA = '316 768 8793'; IG = '@heiiu_english'
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
.band { position: absolute; left: 0; right: 0; bottom: 0; height: %(BAND)dpx; background: #FF4A00; padding: 44px 72px 0 72px;
        display: grid; grid-template-columns: 1fr 300px; gap: 0 40px; align-items: start }
.band::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 8px; background: #FBC900 }
.band p { font-size: 26px; line-height: 1.34; color: #FFF8E7 }
.band p b { font-weight: 700 }
.band .logo { width: 300px; margin-top: -8px; justify-self: end }
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
        big2='Y los hábitos que hacen que de verdad lo logres.',
        band='En Heiiu entrenamos las dos cosas: <b>el inglés</b> y <b>los hábitos que lo sostienen</b>: puntualidad, constancia y disciplina. Con garantía de aprendizaje por escrito.',
        band_px=340),
    'GENERAL_ASESORAS': dict(   # la muestra o reenvia la asesora de la entidad aliada; 1080x1920 (pantalla completa de WhatsApp)
        H=1920, compact=True, label='HEIIU ENGLISH ACADEMY', sub='BUCARAMANGA',
        h1='¿Por qué inglés, <em>y por qué ahora?</em>',
        st=[('La tecnología cambió la forma de aprender. Lo que vale ya no es el certificado, sino lo que puedes hacer con lo que sabes.'),
            ('La inteligencia artificial traduce, pero no conversa por ti. En la entrevista, en la reunión y en el viaje, hablas tú.'),
            ('Hoy, desde Bucaramanga, puedes estudiar, trabajar o vender con gente de todo el mundo. El idioma en común es el inglés.')],
        lead='Poder comunicarte con cualquier persona del mundo sube de valor cada día.',
        big='Y no se aprende con suerte: se aprende en equipo, con alguien que cree en ti y sabe que eres capaz.',
        big2='',
        why=[('HABLAS DESDE EL PRIMER DÍA', 'Un profesor al lado que te corrige ahí mismo. Nada de llenar cuadernos sin abrir la boca.', False),
             ('EL PRIMER PASO HACIA LO QUE QUIERES', 'Hoy nadie busca solo un cargo: busca una vida que le guste. El viaje, el ascenso, el trabajo afuera o tu emprendimiento. Te ayudamos a dar el <b>primer paso</b> hacia eso que te haría feliz.', False),
             ('UN COACH QUE NO TE SUELTA', 'Aprender inglés no es fácil ni siempre divertido, digan lo que digan las redes. Por eso tienes un coach: si faltas, te atrasas o te desanimas, <b>aquí no te dejamos rendirte</b>.', False),
             ('VES TU AVANCE O TE DEVOLVEMOS EL DINERO', 'Si asistes, haces tus tareas y presentas tus evaluaciones, y aun así no avanzas, te devolvemos el <b>100% del nivel</b>. Está firmado en tu contrato.', False),
             ('BECA POR TU ENTIDAD ALIADA', 'Si llegas por una entidad aliada, tienes una <b>beca</b> con su nombre. Pregúntale a tu asesora y escríbenos desde su enlace o su QR: <b>tu código ya va en el mensaje</b>.', True)],
        band='Una academia que firma lo que promete y no te deja solo en el camino. <b>Escríbenos y agenda tu asesoría.</b>',
        band_px=300),
    '1_PROFESIONALES': dict(
        label='PROGRAMA INDIVIDUAL', sub='MÉDICOS · PROFESIONALES · DIRECTIVOS',
        h1='Su inglés, <em>en su agenda.</em>',
        st=[('<b>100 horas uno a uno.</b> Usted fija los días y las horas cada semana; el programa se acomoda a sus turnos, sus juntas y sus viajes.'),
            ('<b>Sobre su trabajo.</b> Armamos el plan a su medida, para que la clase se enfoque en los temas de los que usted ya estaría hablando si hablara inglés.'),
            ('<b>Avance medido.</b> Prueba de nivel al inicio y al final, y reporte mensual de su progreso.')],
        lead='Sin inglés no se pierde un título. Se pierden conversaciones:',
        big='el networking, los resultados que vale la pena contar, entender lo que otros quieren transmitir.',
        big2='En un puesto directivo o médico, eso es gran parte de la experiencia, del avance y de los resultados.',
        band='Programa individual para médicos, profesionales y directivos. <b>Cupos limitados por disponibilidad de profesor.</b> Agende una asesoría de 15 minutos.',
        band_px=320),
    '2_MEDICINA': dict(
        label='PREPARACIÓN INDIVIDUAL', sub='ESTUDIANTES E INTERNOS DE MEDICINA',
        h1='La entrevista que decide tu programa, <em>en inglés.</em>',
        st=[('<b>Simulacros grabados.</b> Respondes las preguntas típicas una y otra vez, te grabas, y corregimos pronunciación, estructura y tiempo de respuesta.'),
            ('<b>Presentar un caso.</b> Vocabulario clínico y la forma de contar un caso, tu investigación o tu experiencia en orden y sin rodeos.'),
            ('<b>Tu presentación personal.</b> Quién eres, por qué ese programa y qué aportas, dicho en un minuto y con seguridad.')],
        lead='No prometemos la admisión.',
        big='Entrenamos la entrevista.',
        big2='Por horas, según la fecha de tu entrevista. Garantía de aprendizaje por escrito.',
        band='Preparación uno a uno para entrevistas de admisión a residencias, rotaciones y programas. <b>Escríbenos con la fecha de tu entrevista.</b>',
        band_px=320),
    '3_ATENCION': dict(
        label='INGLÉS PARA ATENCIÓN AL CLIENTE', sub='RECEPCIÓN · SALUD · HOTELES · TURISMO · RESTAURANTES',
        h1='Atiende en inglés <em>al cliente que llega.</em>',
        st=[('<b>Las frases de tu trabajo.</b> Cada clase es una situación de tu puesto: el huésped que llega, el paciente que llama, la mesa que pide la cuenta.'),
            ('<b>Hablas desde el primer día.</b> Con un profesor al lado que te corrige ahí mismo. Nada de llenar cuadernos sin abrir la boca.'),
            ('<b>Para tu empresa.</b> Becas con el nombre de la empresa para su equipo, sin costo para la empresa. Pregunta por el programa de alianzas.')],
        lead='El cliente que llega no espera a que termines el curso.',
        big='Por eso se habla desde la primera clase.',
        big2='',
        band='Grupos de máximo 16 personas o programa individual. <b>Garantía de aprendizaje por escrito.</b> Escríbenos y agenda tu asesoría.',
        band_px=320),
    '4_PADRES': dict(
        label='PROGRAMAS PARA JÓVENES', sub='PADRES DE FAMILIA',
        h1='El inglés que su hijo <em>va a necesitar.</em>',
        st=[('<b>Se habla, no solo se escribe.</b> Su hijo habla desde la primera sesión, con simulaciones de lo que va a vivir: el aeropuerto, la entrevista, la clase afuera.'),
            ('<b>Usted ve el avance.</b> Reporte periódico a los padres con asistencia, puntualidad y progreso, y grabaciones de entrada y de salida del nivel.'),
            ('<b>Hábitos que se quedan.</b> Junto con el inglés se entrenan puntualidad, constancia y disciplina. Eso también se reporta.')],
        lead='Un enfoque claro desde el primer día:',
        big='el viaje, el intercambio, la universidad o la beca que viene.',
        big2='',
        band='Programas para jóvenes con meta definida y <b>garantía de aprendizaje por escrito</b>. Agende una asesoría para conocer la ruta de su hijo.',
        band_px=320),
}


COMPACT = """
.top { padding-top: 56px; padding-bottom: 44px } h1 { font-size: 76px; margin-top: 28px } .rule { margin: 30px 0 26px 0 }
ol.st li { padding: 19px 0 17px 0 } ol.st p { font-size: 28px; line-height: 1.32 }
.pivot { padding-top: 30px } .pivot .lead { font-size: 34px } .pivot .big { font-size: 52px; margin-top: 12px }
.why { margin-top: 28px } .why h2 { font-size: 38px; margin-bottom: 14px } .why .grid { gap: 14px }
.why .card { padding: 16px 20px 18px 20px; border-radius: 14px } .why .k { font-size: 17px; margin-bottom: 6px } .why p { font-size: 22px; line-height: 1.28 }
"""


def html(c):
    st = ''.join('<li><span class="n">0%d</span><p>%s</p></li>' % (i + 1, t) for i, t in enumerate(c['st']))
    big2 = '<p class="big2">%s</p>' % c['big2'] if c['big2'] else ''
    logo = pathlib.Path(LOGO_NAR).as_uri()
    why = ''
    if c.get('why'):
        cards = ''.join('<div class="card%s"><div class="k">%s</div><p>%s</p></div>' % (' full' if full else '', k, t) for k, t, full in c['why'])
        why = '<div class="why"><h2>%s</h2><div class="grid">%s</div></div>' % (c.get('why_h2', '¿Por qué con Heiiu?'), cards)
    return ('<!doctype html><html><head><meta charset="utf-8"><style>%s%s</style></head><body><div class="page">'
            '<div class="top"><div class="label">%s<span>%s</span></div><h1>%s</h1><div class="rule"></div>'
            '<ol class="st">%s</ol><div class="pivot"><p class="lead">%s</p><p class="big">%s</p>%s</div>%s</div>'
            '<div class="band"><p>%s</p><img class="logo" src="%s">'
            '<div class="cta"><div class="tel"><small>Escríbenos</small>%s</div><div class="ig">%s<b>Bucaramanga</b></div></div></div>'
            '</div></body></html>') % (CSS % dict(W=W, H=c.get('H', H), BAND=c['band_px']), COMPACT if c.get('compact') else '', c['label'], c['sub'], c['h1'], st, c['lead'], c['big'], big2, why,
                                       c['band'], logo, LINEA, IG)


def render(nombre, c):
    hp = os.path.join(WORK, nombre + '.html'); png = os.path.join(WORK, nombre + '.png')
    open(hp, 'w', encoding='utf-8').write(html(c))
    if os.path.exists(png): os.remove(png)
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--force-device-scale-factor=1',
                    '--user-data-dir=' + os.path.join(WORK, 'profile'), '--window-size=%d,%d' % (W, c.get('H', H)),
                    '--screenshot=' + png, pathlib.Path(hp).as_uri()], capture_output=True, timeout=90)
    assert os.path.exists(png), 'Edge no generó ' + png
    out = os.path.join(OUTDIR, 'PIEZA_%s.png' % nombre)
    os.makedirs(OUTDIR, exist_ok=True); os.makedirs(COPIA, exist_ok=True)
    for p in (out, os.path.join(COPIA, os.path.basename(out))):
        try: shutil.copy(png, p); print('OK', p)
        except PermissionError: p2 = p.replace('.png', '_v2.png'); shutil.copy(png, p2); print('ABIERTA ->', p2)


if __name__ == '__main__':
    import sys
    logo_transparente()
    for k in (sys.argv[1:] or PIEZAS): render(k, PIEZAS[k])
