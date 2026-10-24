# -*- coding: utf-8 -*-
"""Cuatro volantes por segmento (bosquejo, misma base visual de la pieza de referidos):
  1 PROFESIONALES  medicos, profesionales y directivos: 100 horas personalizadas, horario flexible
  2 MEDICINA       estudiantes de medicina: entrevistas de admision a programas
  3 ATENCION       recepcion, salud, odontologia, hoteleria, turismo, restaurantes
  4 PADRES         padres de familia: programas para sus hijos con enfoque (viaje, intercambio, universidad)
Reglas: sin precio, sin "facil/rapido", sin empleo/visa/nativos, sin nombres de metodologias ni de competidores.
Contacto: linea de alianzas 316 768 8793. Sin modalidad (presencial/en linea) ni horarios: decision de gerencia 24/10/2026.
Salida: recursos/comercial/campanas/volantes/VOLANTE_{n}_{SEG}_BOSQUEJO.png  (1080x1620, 2:3, imprime en 10x15 o media carta)"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1620
NAR = (229, 76, 9); AMAR = (251, 201, 0); CREMA = (255, 248, 231); OSC = (48, 39, 28); GRIS = (110, 100, 88); BLANCO = (255, 255, 255)
F = 'C:/Windows/Fonts/'
ROOT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
LOGO = ROOT + r'\recursos\marca heiiu\logo_heiiu_sobre_naranja.png'
OUTDIR = ROOT + r'\recursos\comercial\campanas\volantes'
LINEA = '316 768 8793'   # linea de alianzas (el gerente de alianzas reparte los volantes); nunca la linea principal
def font(name, size): return ImageFont.truetype(F + name, size)

def wrap(d, txt, fnt, maxw):
    out, cur = [], ''
    for w in txt.split(' '):
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=fnt) <= maxw: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out

def parrafo(d, x, y, txt, fnt, fill, maxw, lh=None):
    lh = lh or int(fnt.size * 1.28)
    for ln in wrap(d, txt, fnt, maxw):
        d.text((x, y), ln, font=fnt, fill=fill); y += lh
    return y

VOLANTES = {
    '1_PROFESIONALES': dict(
        tag='PROGRAMA INDIVIDUAL · MÉDICOS, PROFESIONALES Y DIRECTIVOS',
        titular=['Su inglés,', 'en su agenda.'],
        bajada='100 horas personalizadas, uno a uno, con un horario que se acomoda a sus turnos, sus juntas y sus viajes.',
        panel=('100 HORAS', 'individuales · horario flexible · desde 3 horas por semana'),
        puntos=[('Sobre su trabajo', 'El contenido sale de su día: la junta, el congreso, el paciente o el cliente de afuera, el correo que hay que contestar hoy.'),
                ('Al ritmo que su agenda permita', 'Usted fija los días y las horas cada semana. Con tres horas semanales termina en unos ocho meses; con más, antes.'),
                ('Avance medido', 'Prueba de nivel al inicio y al final, reporte mensual y garantía de aprendizaje por escrito.')],
        cta='Agende una asesoría de 15 minutos', nota='Cupos individuales limitados por disponibilidad de profesor.'),
    '2_MEDICINA': dict(
        tag='PREPARACIÓN INDIVIDUAL · ESTUDIANTES E INTERNOS DE MEDICINA',
        titular=['La entrevista que decide', 'tu programa, en inglés.'],
        bajada='Preparación uno a uno para entrevistas de admisión a residencias, rotaciones y programas: tu historia, tus casos y las preguntas que te van a hacer.',
        panel=('POR HORAS', 'según la fecha de tu entrevista'),
        puntos=[('Simulacros grabados', 'Respondes las preguntas típicas una y otra vez, te grabas, y corregimos pronunciación, estructura y tiempo de respuesta.'),
                ('Presentar un caso', 'Vocabulario clínico y la forma de contar un caso, tu investigación o tu experiencia en orden y sin rodeos.'),
                ('Tu presentación personal', 'Quién eres, por qué ese programa y qué aportas, dicho en un minuto y con seguridad.')],
        cta='Escríbenos con la fecha de tu entrevista', nota='Garantía de aprendizaje por escrito. No prometemos admisión: entrenamos la entrevista.'),
    '3_ATENCION': dict(
        tag='INGLÉS PARA ATENCIÓN AL CLIENTE · RECEPCIÓN, SALUD, ODONTOLOGÍA, HOTELES, TURISMO Y RESTAURANTES',
        titular=['Atiende en inglés', 'al cliente que llega.'],
        bajada='Entrenamiento práctico con las situaciones reales de tu puesto: recibir, reservar, cobrar, explicar un procedimiento y resolver una queja.',
        panel=('GRUPOS O INDIVIDUAL', 'se habla desde la primera clase · grupos de máximo 16'),
        puntos=[('Las frases de tu trabajo', 'Cada clase es una situación de tu puesto: el huésped que llega, el paciente que llama, la mesa que pide la cuenta.'),
                ('Hablas desde el primer día', 'Con un profesor al lado que te corrige ahí mismo. Nada de llenar cuadernos sin abrir la boca.'),
                ('Para tu empresa', 'Becas con el nombre de la empresa para su equipo, sin costo para la empresa. Pregunta por el programa de alianzas.')],
        cta='Pregunta por el horario de tu turno', nota='Garantía de aprendizaje por escrito.'),
    '4_PADRES': dict(
        tag='PROGRAMAS PARA JÓVENES · PADRES DE FAMILIA',
        titular=['El inglés que su hijo', 'va a necesitar.'],
        bajada='Programas para jóvenes con un enfoque claro desde el primer día: el viaje, el intercambio, la universidad o la beca que viene.',
        panel=('ENFOQUE POR META', 'viaje · intercambio · admisión universitaria · beca'),
        puntos=[('Se habla, no solo se escribe', 'Clases donde su hijo habla desde la primera sesión, con simulaciones de lo que va a vivir: el aeropuerto, la entrevista, la clase afuera.'),
                ('Usted ve el avance', 'Reporte periódico a los padres con asistencia, puntualidad y progreso, y grabaciones de entrada y de salida del nivel.'),
                ('Hábitos que se quedan', 'Junto con el inglés se entrenan puntualidad, constancia y disciplina. Eso también se reporta.')],
        cta='Agende una asesoría para conocer la ruta de su hijo', nota='Garantía de aprendizaje por escrito.'),
}

def volante(key, c):
    img = Image.new('RGB', (W, H), CREMA); d = ImageDraw.Draw(img)
    logo = Image.open(LOGO).convert('RGB'); band_col = logo.getpixel((3, 3))
    BAND = 222
    d.rectangle([0, 0, W, BAND], fill=band_col)
    lh_ = 150; lw_ = int(logo.width * lh_ / logo.height); logo = logo.resize((lw_, lh_), Image.LANCZOS)
    img.paste(logo, (60, 26))
    ft = font('calibrib.ttf', 20)
    ty = 176
    for ln in wrap(d, c['tag'], ft, W - 120):
        d.text((60, ty), ln, font=ft, fill=CREMA); ty += 24

    y = BAND + 46
    d.rectangle([60, y, 170, y + 6], fill=NAR); y += 28
    f_t = font('calibrib.ttf', 70)
    for ln in c['titular']:
        d.text((60, y), ln, font=f_t, fill=OSC); y += 74
    y += 16
    y = parrafo(d, 60, y, c['bajada'], font('georgiai.ttf', 33), GRIS, W - 120, lh=44)

    # panel oscuro
    y += 26
    px0, py0, px1, py1 = 60, y, W - 60, y + 206
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle([px0 + 6, py0 + 14, px1 + 6, py1 + 14], radius=28, fill=(0, 0, 0, 70)); sh = sh.filter(ImageFilter.GaussianBlur(12))
    img = Image.alpha_composite(img.convert('RGBA'), sh).convert('RGB'); d = ImageDraw.Draw(img)
    d.rounded_rectangle([px0, py0, px1, py1], radius=28, fill=OSC)
    fsz = 72
    while d.textlength(c['panel'][0], font=font('georgiab.ttf', fsz)) > px1 - px0 - 96: fsz -= 2
    d.text((px0 + 48, py0 + 38 + (72 - fsz) // 2), c['panel'][0], font=font('georgiab.ttf', fsz), fill=AMAR)
    parrafo(d, px0 + 50, py0 + 130, c['panel'][1], font('calibri.ttf', 28), CREMA, px1 - px0 - 100, lh=34)
    y = py1 + 44

    # tres puntos
    for tit, sub in c['puntos']:
        d.ellipse([60, y + 6, 60 + 22, y + 28], fill=NAR)
        d.text((100, y), tit, font=font('calibrib.ttf', 33), fill=NAR); y += 44
        y = parrafo(d, 100, y, sub, font('calibri.ttf', 27), OSC, W - 160, lh=35); y += 26

    # CTA amarillo
    y = max(y + 10, H - 120 - 150)
    bx0, by0, bx1, by1 = 60, y, W - 60, y + 78
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=18, fill=AMAR)
    d.text(((bx0 + bx1) // 2, (by0 + by1) // 2), c['cta'] + '  →', font=font('calibrib.ttf', 30), fill=OSC, anchor='mm')
    parrafo(d, 60, by1 + 14, c['nota'], font('calibri.ttf', 20), GRIS, W - 120, lh=25)

    # pie
    fy = H - 120
    d.rectangle([0, fy, W, H], fill=NAR)
    d.text((60, fy + 26), 'Escríbenos: ' + LINEA, font=font('calibrib.ttf', 26), fill=CREMA)
    d.text((60, fy + 64), '@heiiu_english  ·  Bucaramanga', font=font('calibri.ttf', 24), fill=CREMA)
    d.text((W - 60, fy + 26), 'Garantía de aprendizaje', font=font('calibri.ttf', 22), fill=CREMA, anchor='ra')
    d.text((W - 60, fy + 58), 'por escrito, sin letra pequeña', font=font('calibrib.ttf', 24), fill=AMAR, anchor='ra')

    os.makedirs(OUTDIR, exist_ok=True)
    out = os.path.join(OUTDIR, 'VOLANTE_%s_BOSQUEJO.png' % key)
    try: img.save(out, optimize=True); print('OK', out)
    except OSError: out2 = out.replace('.png', '_v2.png'); img.save(out2, optimize=True); print('ABIERTA ->', out2)

for k, c in VOLANTES.items(): volante(k, c)
