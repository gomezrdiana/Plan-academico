# -*- coding: utf-8 -*-
"""TANDA CREMA — 15 piezas IG para @carlosedo.cfo (variante fondo claro del lote azul).

Fondo #F8F5F7 · texto principal #16335A / #0B203C · acentos y lineas champagne #B4A177
· footer @carlosedo.cfo en champagne. Misma composicion del lote azul, invertida.
1080x1350 (IG 4:5). Sin emojis en el arte.

Correr desde la RAIZ del repo:  python generadores/gen_carlos_tanda_crema.py
Salida: recursos/comercial/CFO/IG/_MAESTROS_NO_PUBLICAR/CREMA/*.png
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.pdfgen import canvas as rlcanvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz

# ---------------------------------------------------------------- PALETA
CREMA      = HexColor('#F8F5F7')   # fondo
NAVY       = HexColor('#16335A')   # texto principal
NAVY_D     = HexColor('#0B203C')   # titulos / sombras
NAVY_SUAVE = HexColor('#3D5983')   # texto pequeno (volumen)
ACERO      = HexColor('#506C96')   # secundarios
CHAMP_LINE = HexColor('#B4A177')   # acentos y lineas (palette oficial)
# Champagne para TEXTO sobre fondo claro: #B4A177 sobre crema queda con contraste ~2.4:1
# (ilegible en cuerpo grande). Se usa el champagne profundo, el mismo del lote claro previo.
# Si Diana quiere el #B4A177 literal en texto, cambiar esta sola linea.
CHAMP_TEXT = HexColor('#8E7A4E')

pdfmetrics.registerFont(TTFont('Georgia',  r'C:\Windows\Fonts\georgia.ttf'))
pdfmetrics.registerFont(TTFont('GeorgiaB', r'C:\Windows\Fonts\georgiab.ttf'))
pdfmetrics.registerFont(TTFont('GeorgiaI', r'C:\Windows\Fonts\georgiai.ttf'))
pdfmetrics.registerFont(TTFont('Segoe',    r'C:\Windows\Fonts\segoeui.ttf'))
pdfmetrics.registerFont(TTFont('SegoeB',   r'C:\Windows\Fonts\segoeuib.ttf'))

W, H = 1080, 1350
MX = 90                 # margen lateral (zona segura IG: >40)
MAXW = W - 2 * MX       # 900
BAND_TOP, BAND_BOT = 940, 268   # banda de contenido (dentro del cuadrado central)

OUT_DIR = os.path.join('recursos', 'comercial', 'CFO', 'IG',
                       '_MAESTROS_NO_PUBLICAR', 'CREMA')
FOTO = os.path.join('recursos', 'comercial', 'CFO', 'IG', 'foto_carlos.jpg')

CTA_TEST = 'Test de los 7 \u201cNO\u201d \u2192 link en bio'
CTA_POST = 'Postule su empresa \u2192 link en bio'

# ---------------------------------------------------------------- CONTENIDO
# elementos: ('quote', texto, size, color, space_before)
#            ('small', texto)               -> Segoe, texto de apoyo
#            ('rule',)                      -> filete champagne corto
#            ('label', texto)               -> etiqueta de serie, champagne, letterspaced
#            ('barblock', texto, color, size, space_before)
#            ('qmark',)                     -> comilla grande champagne

PIEZAS = [
 ('N01_Saldo_mentiroso', CTA_TEST, [
    ('quote', 'Tener plata en la cuenta no significa que su empresa est\u00e9 bien.', 62, NAVY_D, 0),
    ('rule',),
    ('small', 'Nadie quiebra de un d\u00eda para otro: se desangran durante meses '
              'mientras el saldo se ve sano.'),
 ]),
 ('N02_Desfinanciacion', CTA_POST, [
    ('quote', 'M\u00e1s deuda sin diagn\u00f3stico no es financiaci\u00f3n:', 58, NAVY_D, 0),
    ('quote', 'es desfinanciaci\u00f3n.', 58, CHAMP_TEXT, 24),
    ('rule',),
    ('small', 'Se siente como ox\u00edgeno el primer mes \u2014 y en seis, la cuota nueva '
              'es un hueco m\u00e1s grande que el que tap\u00f3.'),
 ]),
 ('N03_La_cuenta_10x', CTA_TEST, [
    ('quote', 'Para ganar $1.000 m\u00e1s de utilidad:', 52, NAVY_D, 0),
    ('barblock', 'vender $10.000 m\u00e1s\u2026', NAVY, 54, 48),
    ('barblock', 'o encontrar $1.000 que YA son suyos y se est\u00e1n yendo.',
                 CHAMP_TEXT, 54, 34),
 ]),
 ('N04_No_vende_encuentra', CTA_TEST, [
    ('qmark',),
    ('quote', 'La contrataci\u00f3n m\u00e1s rentable que puede hacer este a\u00f1o no vende:',
              58, NAVY_D, 6),
    ('quote', 'encuentra dinero perdido.', 58, CHAMP_TEXT, 24),
 ]),
 ('N05_Area_administrativa', CTA_TEST, [
    ('quote', '\u00bfQui\u00e9n est\u00e1 decidiendo las finanzas de su empresa?', 62, NAVY_D, 0),
    ('rule',),
    ('small', 'En la mayor\u00eda de las pymes: el \u00e1rea administrativa. Administrar la '
              'operaci\u00f3n no es decidir en finanzas \u2014 y cuando lo hace quien no es '
              'del oficio, la empresa lo paga sin que nadie lo note a tiempo.'),
 ]),
 ('N06_Gasto_como_costo', CTA_TEST, [
    ('quote', 'Un gasto registrado como costo le distorsiona el margen.', 62, NAVY_D, 0),
    ('rule',),
    ('small', 'Y cambia por completo lo que un banco ve de su empresa.'),
 ]),
 ('N07_No_es_gratis', CTA_POST, [
    ('quote', 'Mi radiograf\u00eda no es gratis:', 60, NAVY_D, 0),
    ('quote', 'se paga con su testimonio.', 60, CHAMP_TEXT, 24),
    ('rule',),
    ('small', 'Y no acepto a todas las empresas \u2014 5 al mes, elegidas por potencial '
              'de recuperaci\u00f3n.'),
 ]),
 ('N08_FL_TX_CO', CTA_TEST, [
    ('quote', 'He manejado los n\u00fameros de empresas en Florida, Texas y Colombia.',
              60, NAVY_D, 0),
    ('rule',),
    ('small', 'Le hablo al due\u00f1o en su idioma \u2014 y a su banco en el suyo.'),
 ]),
 ('N09_Ya_hizo_lo_dificil', CTA_TEST, [
    ('quote', 'Usted ya hizo lo dif\u00edcil.', 76, NAVY_D, 0),
    ('rule',),
    ('small', 'Construy\u00f3 el producto, encontr\u00f3 el mercado, sostuvo la empresa a\u00f1o '
              'tras a\u00f1o. Lo \u00fanico que falta es lo f\u00e1cil \u2014 y es justo lo que sigue evitando.'),
 ]),
 ('N10_El_banco_antes', CTA_POST, [
    ('quote', '\u00bfSu empresa calificar\u00eda hoy para un cr\u00e9dito \u2014 y en qu\u00e9 condiciones?',
              60, NAVY_D, 0),
    ('rule',),
    ('small', 'Saberlo ANTES de necesitarlo tambi\u00e9n es mi trabajo.'),
 ]),
 # ------------------------------------------------ SERIE: LO QUE NO HAGO
 ('S01_No_soy_consultor', CTA_TEST, [
    ('label', 'SERIE \u00b7 LO QUE NO HAGO \u00b7 1/5'),
    ('quote', 'No soy un consultor ni le vendo un curso:', 60, NAVY_D, 30),
    ('quote', 'soy el \u00e1rea financiera que su empresa no tiene.', 60, CHAMP_TEXT, 26),
 ]),
 ('S02_No_manejo_su_dinero', CTA_TEST, [
    ('label', 'SERIE \u00b7 LO QUE NO HAGO \u00b7 2/5'),
    ('quote', 'No manejo su dinero. Ni tengo sus claves, ni autorizo pagos.', 58, NAVY_D, 30),
    ('quote', 'Interpreto la informaci\u00f3n \u2014 usted decide.', 58, CHAMP_TEXT, 26),
 ]),
 ('S03_No_todo_esta_mal', CTA_TEST, [
    ('label', 'SERIE \u00b7 LO QUE NO HAGO \u00b7 3/5'),
    ('quote', 'No le voy a decir que todo est\u00e1 mal.', 62, NAVY_D, 30),
    ('quote', 'Si sus n\u00fameros est\u00e1n sanos, se lo digo \u2014 y esa certeza tambi\u00e9n vale.',
              52, CHAMP_TEXT, 26),
 ]),
 ('S04_No_acepto_a_todas', CTA_POST, [
    ('label', 'SERIE \u00b7 LO QUE NO HAGO \u00b7 4/5'),
    ('quote', 'No acepto a todas las empresas.', 62, NAVY_D, 30),
    ('quote', '5 al mes, por potencial de recuperaci\u00f3n.', 56, CHAMP_TEXT, 26),
    ('rule',),
    ('small', 'Postularse no garantiza el cupo.'),
 ]),
 ('S05_No_tecnicismos', CTA_TEST, [
    ('label', 'SERIE \u00b7 LO QUE NO HAGO \u00b7 5/5'),
    ('quote', 'No hablo en tecnicismos.', 66, NAVY_D, 30),
    ('quote', 'Su radiograf\u00eda son 3 p\u00e1ginas que se leen en 1 minuto.', 54, CHAMP_TEXT, 26),
 ]),
]


# ---------------------------------------------------------------- HELPERS
def wrap(c, text, font, size, max_w):
    """Parte un parrafo en lineas que caben en max_w."""
    out, cur = [], ''
    for w_ in text.split():
        t = (cur + ' ' + w_).strip()
        if c.stringWidth(t, font, size) <= max_w:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = w_
    if cur:
        out.append(cur)
    return out


def tracked(c, x, y, text, font, size, space):
    """drawString con letterspacing manual (reportlab 4 no expone setCharSpace)."""
    for ch in text:
        c.drawString(x, y, ch)
        x += c.stringWidth(ch, font, size) + space


def build(c, elementos, qscale):
    """Devuelve (items, alto_total). item = (tipo, payload, alto, espacio_antes)."""
    items = []
    for el in elementos:
        t = el[0]
        if t == 'label':
            items.append(('label', el[1], 30, 0))
        elif t == 'qmark':
            items.append(('qmark', None, 62, 0))
        elif t == 'rule':
            items.append(('rule', None, 4, 42))
        elif t == 'small':
            size = 33
            lines = wrap(c, el[1], 'Segoe', size, MAXW)
            items.append(('small', (lines, size), len(lines) * size * 1.42, 30))
        elif t == 'quote':
            size = el[2] * qscale
            lines = wrap(c, el[1], 'GeorgiaB', size, MAXW)
            items.append(('quote', (lines, size, el[3]),
                          len(lines) * size * 1.24, el[4]))
        elif t == 'barblock':
            size = el[3] * qscale
            lines = wrap(c, el[1], 'GeorgiaB', size, MAXW - 46)
            items.append(('barblock', (lines, size, el[2]),
                          len(lines) * size * 1.24, el[4]))
    total = sum(h + sb for _, _, h, sb in items)
    if items:
        total -= items[0][3]
    return items, total


def fondo(c):
    c.setFillColor(CREMA)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    # renglones de libro contable, muy tenues
    c.saveState()
    c.setStrokeColorRGB(0.086, 0.2, 0.353, alpha=0.06)
    c.setLineWidth(1)
    y = 0
    while y < H:
        c.line(0, y, W, y)
        y += 46
    c.restoreState()
    # filo superior champagne
    c.setFillColor(CHAMP_LINE)
    c.rect(0, H - 10, W, 10, stroke=0, fill=1)


def cabecera(c):
    cx, cy, r = 180, 1085, 100
    if os.path.exists(FOTO):
        IMG_W, IMG_H = 2316.0, 3088.0
        FX0, FY0, FLADO = 216.0, 388.0, 2200.0
        esc = (2 * r) / FLADO
        c.saveState()
        p = c.beginPath()
        p.circle(cx, cy, r)
        c.clipPath(p, stroke=0, fill=0)
        c.drawImage(FOTO, (cx - r) - FX0 * esc, (cy - r) - FY0 * esc,
                    IMG_W * esc, IMG_H * esc, mask='auto')
        c.restoreState()
    else:
        c.setFillColor(NAVY)
        c.circle(cx, cy, r, stroke=0, fill=1)
        c.setFillColor(CREMA)
        c.setFont('GeorgiaB', 52)
        c.drawCentredString(cx, cy - 18, 'CR')
    c.setStrokeColor(CHAMP_LINE)
    c.setLineWidth(3)
    c.circle(cx, cy, r, stroke=1, fill=0)

    x = cx + r + 32
    c.setFillColor(NAVY_D)
    c.setFont('SegoeB', 42)
    c.drawString(x, cy + 8, 'Carlos Remolina')
    c.setFillColor(ACERO)
    c.setFont('Segoe', 27)
    c.drawString(x, cy - 42, 'Director Financiero Externo \u00b7 FL \u00b7 TX \u00b7 CO')


def pie(c, cta):
    c.setStrokeColor(CHAMP_LINE)
    c.setLineWidth(2)
    c.line(MX, 228, W - MX, 228)
    c.setFillColor(CHAMP_TEXT)
    c.setFont('SegoeB', 32)
    c.drawString(MX, 172, '@carlosedo.cfo')
    c.setFillColor(NAVY_SUAVE)
    c.setFont('Segoe', 28)
    c.drawRightString(W - MX, 174, cta)


def dibujar(c, items, total):
    band_h = BAND_TOP - BAND_BOT
    y = BAND_TOP - max(0, (band_h - total)) / 2.0
    for tipo, payload, h, sb in items:
        y -= sb
        if tipo == 'label':
            c.setFillColor(CHAMP_TEXT)
            c.setFont('SegoeB', 24)
            tracked(c, MX, y - 24, payload, 'SegoeB', 24, 3.4)
        elif tipo == 'qmark':
            c.setFillColor(CHAMP_LINE)
            c.setFont('GeorgiaB', 110)
            c.drawString(MX - 6, y - 78, '\u201c')
        elif tipo == 'rule':
            c.setStrokeColor(CHAMP_LINE)
            c.setLineWidth(4)
            c.line(MX, y - 2, MX + 88, y - 2)
        elif tipo == 'small':
            lines, size = payload
            c.setFillColor(NAVY_SUAVE)
            c.setFont('Segoe', size)
            for i, ln in enumerate(lines):
                c.drawString(MX, y - size * 1.0 - i * size * 1.42, ln)
        elif tipo == 'quote':
            lines, size, color = payload
            c.setFillColor(color)
            c.setFont('GeorgiaB', size)
            for i, ln in enumerate(lines):
                c.drawString(MX, y - size * 0.95 - i * size * 1.24, ln)
        elif tipo == 'barblock':
            lines, size, color = payload
            c.setFillColor(color)
            c.rect(MX, y - h + size * 0.14, 8, h - size * 0.14, stroke=0, fill=1)
            c.setFont('GeorgiaB', size)
            for i, ln in enumerate(lines):
                c.drawString(MX + 34, y - size * 0.95 - i * size * 1.24, ln)
        y -= h


# ---------------------------------------------------------------- MAIN
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    pdf_path = os.path.join(OUT_DIR, '_master.pdf')
    c = rlcanvas.Canvas(pdf_path, pagesize=(W, H))
    band_h = BAND_TOP - BAND_BOT

    for nombre, cta, elementos in PIEZAS:
        qscale = 1.0
        items, total = build(c, elementos, qscale)
        while total > band_h and qscale > 0.55:
            qscale -= 0.03
            items, total = build(c, elementos, qscale)
        if qscale < 1.0:
            print('  ajuste de tamano en %s -> escala %.2f' % (nombre, qscale))
        fondo(c)
        cabecera(c)
        dibujar(c, items, total)
        pie(c, cta)
        c.showPage()
    c.save()

    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(1, 1))
        out = os.path.join(OUT_DIR, PIEZAS[i][0] + '.png')
        pix.save(out)
        print('OK: %s (%dx%d)' % (out, pix.width, pix.height))
    doc.close()
    os.remove(pdf_path)
    print('LISTO: %d piezas crema en %s' % (len(PIEZAS), OUT_DIR))


if __name__ == '__main__':
    main()
