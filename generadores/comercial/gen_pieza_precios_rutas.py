# -*- coding: utf-8 -*-
"""Piezas 'Precios 2026' por RUTA parcial (mismo diseño que PRECIOS_2026_HEIIU.png): A2 → B2 y B1 → B2.
Precios full y becas = matriz del kit (gen_kit_bonito.py / MOTOR_CUOTAS_FONDO_2026.xlsx). Los niveles que el
estudiante ya tiene se dibujan en contorno gris ("YA LO TIENES"), así la lámina conserva las 4 barras.
Salida: recursos/comercial/INDUCCION_COMERCIAL/PRECIOS_2026_A2_B2.png y PRECIOS_2026_B1_B2.png
Uso: python -X utf8 generadores/comercial/gen_pieza_precios_rutas.py"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
CREMA = (255, 248, 231); NAR = (229, 76, 9); AMAR = (251, 201, 0); CAFE = (48, 39, 28); GRIS = (120, 110, 100); BLANCO = (255, 255, 255)
GRIS_CLARO = (205, 198, 188)
F = 'C:/Windows/Fonts/'
def font(n, s): return ImageFont.truetype(F + n, s)
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTDIR = os.path.join(BASE, 'recursos', 'comercial', 'INDUCCION_COMERCIAL')

NIVELES = [('A1', '90 h', 1596000, (160, 150, 140)), ('A2', '110 h', 1915000, (200, 110, 70)),
           ('B1', '175 h', 2842000, (236, 110, 40)), ('B2', '200 h', 2343000, NAR)]

# rutas: niveles incluidos, horas, precio full, beca mínima (General contado) y máxima (Transformación contado), duraciones
RUTAS = {
    'A2_B2': dict(titulo='DE A2 A B2', incluidos=('A2', 'B1', 'B2'), horas=485, full=7100000, beca_min='25,6%', beca_max=36,
                  dur4='~6 meses', dur2='~12 meses', nombre='Programa A2 → B2'),
    'B1_B2': dict(titulo='DE B1 A B2', incluidos=('B1', 'B2'), horas=375, full=5185000, beca_min='17,6%', beca_max=24.8,
                  dur4='~4 meses', dur2='~9 meses', nombre='Programa B1 → B2'),
}
def peso(x): return '$' + format(int(round(x)), ',').replace(',', '.')

def pieza(clave):
    r = RUTAS[clave]
    img = Image.new('RGB', (W, H), CREMA)
    acc = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ad = ImageDraw.Draw(acc)
    ad.polygon([(0, 0), (140, 0), (0, 420)], fill=NAR + (255,))
    ad.polygon([(0, 0), (60, 0), (0, 200)], fill=AMAR + (255,))
    ad.polygon([(W, H), (W - 120, H), (W, H - 330)], fill=AMAR + (255,))
    ad.polygon([(W, H), (W - 50, H), (W, H - 150)], fill=NAR + (255,))
    img = Image.alpha_composite(img.convert('RGBA'), acc).convert('RGB'); d = ImageDraw.Draw(img)

    try:
        logo = Image.open(os.path.join(BASE, 'recursos', 'marca heiiu', 'logo_heiiu_sobre_naranja.png')).convert('RGBA')
        lh = 96; lw = int(logo.width * lh / logo.height); logo = logo.resize((lw, lh))
        pad = Image.new('RGBA', (lw + 36, lh + 24), NAR + (255,)); pad.paste(logo, (18, 12), logo)
        img.paste(pad, (150, 40), pad)
    except Exception:
        d.text((150, 50), 'heiiu', font=font('calibrib.ttf', 60), fill=NAR)

    d.text((W // 2, 60), 'PRECIOS 2026 · ' + r['titulo'], font=font('calibrib.ttf', 54), fill=CAFE, anchor='mt')
    d.text((W // 2 + 40, 122), '%s · %d horas presenciales · garantía por escrito' % (r['nombre'], r['horas']),
           font=font('calibri.ttf', 24), fill=GRIS, anchor='mt')

    x0, base_y, bw, gap = 150, 640, 225, 24
    step = 62
    for i, (nv, hrs, pr, col) in enumerate(NIVELES):
        x = x0 + i * (bw + gap); top = base_y - 210 - i * step
        if nv in r['incluidos']:
            d.rounded_rectangle([x, top, x + bw, base_y], radius=14, fill=col)
            d.text((x + bw // 2, top + 18), nv, font=font('calibrib.ttf', 64), fill=BLANCO, anchor='mt')
            d.text((x + bw // 2, top + 96), hrs, font=font('calibri.ttf', 28), fill=(255, 240, 225), anchor='mt')
            d.text((x + bw // 2, base_y - 40), peso(pr), font=font('calibrib.ttf', 30), fill=BLANCO, anchor='mt')
        else:
            d.rounded_rectangle([x, top, x + bw, base_y], radius=14, fill=CREMA, outline=GRIS_CLARO, width=3)
            d.text((x + bw // 2, top + 18), nv, font=font('calibrib.ttf', 64), fill=GRIS_CLARO, anchor='mt')
            d.text((x + bw // 2, top + 96), hrs, font=font('calibri.ttf', 28), fill=GRIS_CLARO, anchor='mt')
            d.text((x + bw // 2, base_y - 44), 'YA LO TIENES', font=font('calibrib.ttf', 24), fill=GRIS, anchor='mt')
    d.line([(x0, base_y + 2), (x0 + 4 * bw + 3 * gap, base_y + 2)], fill=CAFE, width=3)
    d.text((x0, base_y + 14), 'Nivel suelto: sin beca.', font=font('calibri.ttf', 26), fill=GRIS)
    d.text((x0 + 300, base_y + 14), r['nombre'] + ' de lista:', font=font('calibri.ttf', 26), fill=GRIS)
    d.text((x0 + 300 + d.textlength(r['nombre'] + ' de lista:  ', font=font('calibri.ttf', 26)), base_y + 9),
           peso(r['full']), font=font('calibrib.ttf', 34), fill=CAFE)

    cx, cy, cw, ch = 1150, 190, 380, 300
    d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=20, fill=NAR)
    d.text((cx + cw // 2, cy + 22), 'BECAS DEL FONDO', font=font('calibrib.ttf', 30), fill=AMAR, anchor='mt')
    d.text((cx + cw // 2, cy + 62), 'según el perfil del estudiante', font=font('calibri.ttf', 22), fill=BLANCO, anchor='mt')
    bmax = ('%g' % r['beca_max']).replace('.', ',') + '%'
    d.text((cx + cw // 2, cy + 104), 'del %s al %s' % (r['beca_min'], bmax), font=font('calibrib.ttf', 46), fill=BLANCO, anchor='mt')
    d.text((cx + cw // 2, cy + 168), r['nombre'] + ', de contado', font=font('calibri.ttf', 21), fill=(255, 230, 210), anchor='mt')
    d.text((cx + cw // 2, cy + 196), 'desde ' + peso(r['full'] * (1 - r['beca_max'] / 100)), font=font('calibrib.ttf', 34), fill=AMAR, anchor='mt')
    d.text((cx + cw // 2, cy + 246), 'Se evalúa con soportes en la asesoría.', font=font('calibri.ttf', 19), fill=(255, 230, 210), anchor='mt')
    d.text((cx + cw // 2, cy + 270), 'Libros incluidos si separas el mismo día.', font=font('calibri.ttf', 19), fill=(255, 230, 210), anchor='mt')

    cy2 = cy + ch + 24; ch2 = 204
    d.rounded_rectangle([cx, cy2, cx + cw, cy2 + ch2], radius=20, fill=BLANCO, outline=NAR, width=3)
    d.text((cx + 22, cy2 + 18), 'FINANCIACIÓN', font=font('calibrib.ttf', 26), fill=NAR)
    d.text((cx + 22, cy2 + 54), 'Cuotas con inicial y mensualidades', font=font('calibri.ttf', 22), fill=CAFE)
    d.text((cx + 22, cy2 + 84), 'Cesantías · crédito con tu banco', font=font('calibri.ttf', 20), fill=GRIS)
    d.text((cx + 22, cy2 + 110), 'o cooperativa', font=font('calibri.ttf', 20), fill=GRIS)
    d.text((cx + 22, cy2 + 140), 'Afiliados a Cajasan: condiciones', font=font('calibri.ttf', 20), fill=GRIS)
    d.text((cx + 22, cy2 + 166), 'especiales (se confirman en la asesoría)', font=font('calibri.ttf', 20), fill=GRIS)

    py = 712
    d.text((x0, py), 'PROGRAMAS', font=font('calibrib.ttf', 26), fill=NAR)
    progs = ['Súper intensivo 4 h · L-V 8:00 a 12:00 · ' + r['dur4'], 'Intensivo 2 h · L-V 6:30 a 8:30 pm · ' + r['dur2'],
             'Tarde entre semana · en apertura', 'Sabatino 4 h · 8:00 a 12:00 · un nivel a la vez', 'Clases personalizadas · desde 30 h']
    for i, t in enumerate(progs):
        cxp = x0 + (i % 2) * 560; cyp = py + 38 + (i // 2) * 32
        d.ellipse([cxp, cyp + 9, cxp + 10, cyp + 19], fill=AMAR, outline=NAR)
        d.text((cxp + 20, cyp), t, font=font('calibri.ttf', 22), fill=CAFE)

    d.text((x0, H - 46), 'Separa tu cupo con $300.000 y congela el precio · Única academia presencial de Bucaramanga con garantía de aprendizaje por escrito',
           font=font('calibri.ttf', 21), fill=GRIS)

    out = os.path.join(OUTDIR, 'PRECIOS_2026_%s.png' % clave)
    try: img.save(out, optimize=True); print('OK', out)
    except OSError: img.save(out.replace('.png', '_v2.png'), optimize=True); print('ABIERTA -> _v2', out)

if __name__ == '__main__':
    for k in RUTAS: pieza(k)
