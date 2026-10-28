# -*- coding: utf-8 -*-
"""Láminas PARA EL CLIENTE 'a cuotas con Heiiu' por ruta: A1 → B2, A2 → B2 y B1 → B2.
Sin matriz por perfil (es interna): cada jornada muestra el RANGO de cuota, del perfil Transformación al General
(Ejecutivo no se muestra: paga su empresa). Números = motor de cuotas del kit (beca de cuotas, inicial 20%,
cuota fija con el interés del crédito directo, máximo de cuotas por jornada).
Salida: recursos/comercial/INDUCCION_COMERCIAL/CUOTAS_2026_A1_B2.png, CUOTAS_2026_A2_B2.png, CUOTAS_2026_B1_B2.png, CUOTAS_2026_B2.png
Uso: python -X utf8 generadores/comercial/gen_pieza_financiado_cliente.py"""
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
# becas: (Transformación cuotas, General cuotas, General contado, Transformación contado)
RUTAS = {
    'A1_B2': dict(titulo='DE A1 A B2 · A CUOTAS CON HEIIU', nombre='Programa completo A1 → B2', incluidos=('A1', 'A2', 'B1', 'B2'),
                  horas=575, full=8696000, bq=(36, 25.6), bc=(32, 45), n2=11, n4=5, dur2='~14 meses', dur4='~7 meses'),
    'A2_B2': dict(titulo='DE A2 A B2 · A CUOTAS CON HEIIU', nombre='Programa A2 → B2', incluidos=('A2', 'B1', 'B2'),
                  horas=485, full=7100000, bq=(27, 19.2), bc=(25.6, 36), n2=11, n4=5, dur2='~12 meses', dur4='~6 meses'),
    'B1_B2': dict(titulo='DE B1 A B2 · A CUOTAS CON HEIIU', nombre='Programa B1 → B2', incluidos=('B1', 'B2'),
                  horas=375, full=5185000, bq=(15.8, 11.2), bc=(17.6, 24.8), n2=8, n4=3, dur2='~9 meses', dur4='~4 meses'),
    # Solo B2 = fila de la matriz del kit (no es nivel suelto): T 20,3/11,3 · G 14,4/8. Maximo 4 cuotas (2 h, ~5 meses); 4 h ~2,5 meses -> 2 cuotas.
    'B2': dict(titulo='NIVEL B2 · A CUOTAS CON HEIIU', nombre='Programa B2', incluidos=('B2',),
               horas=200, full=2343000, bq=(11.3, 8), bc=(14.4, 20.3), n2=4, n4=2, dur2='~5 meses', dur4='~2,5 meses',
               nota='Ultimo nivel de la ruta: aplica beca del Fondo.'),
    # Plan de liderazgo (joven que ya habla ingles, entra a B2): sin garantia, sin video diario, sin libros, sin Cajasan (Diana 28/10)
    'B2_LIDERAZGO': dict(titulo='PLAN DE LIDERAZGO B2 · A CUOTAS', nombre='Plan de liderazgo B2', incluidos=('B2',),
               horas=200, full=2343000, bq=(11.3, 8), bc=(14.4, 20.3), n2=4, n4=2, dur2='~5 meses', dur4='~2,5 meses',
               nota='Ultimo nivel de la ruta: aplica beca del Fondo.',
               sub='Plan de liderazgo en inglés · 200 horas presenciales en B2 · un rol en cada simulación',
               incluye=['Clases presenciales en grupo, en inglés', 'Rol en cada simulación: presentador,', 'mediador o coach', 'Video de hito cada 10 clases',
                        'Reporte de asistencia y avance', 'Proyecto final en vivo con preguntas', 'Certificado B2 con evaluador externo'],
               pie='Separa el cupo con $300.000 y congela el precio · Plan de liderazgo en inglés · 200 horas presenciales en Bucaramanga',
               outdir=os.path.join(BASE, 'recursos', 'personalizados', 'JOVEN_BILINGUE')),
}
INICIAL = 0.20; TASA = 0.019
def peso(x): return '$' + format(int(round(x)), ',').replace(',', '.')
def cuota(saldo, n): return saldo * TASA / (1 - (1 + TASA) ** -n)
def pct(p): return ('%g' % p).replace('.', ',') + '%'

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
    d.text((W // 2 + 40, 60), r['titulo'], font=font('calibrib.ttf', 50), fill=CAFE, anchor='mt')
    d.text((W // 2 + 40, 120), r.get('sub', '%s · %d horas presenciales · garantía por escrito' % (r['nombre'], r['horas'])),
           font=font('calibri.ttf', 24), fill=GRIS, anchor='mt')

    # escalera (más baja para dejar sitio al plan)
    x0, base_y, bw, gap, step = 150, 520, 215, 22, 48
    for i, (nv, hrs, pr, col) in enumerate(NIVELES):
        x = x0 + i * (bw + gap); top = base_y - 160 - i * step
        if nv in r['incluidos']:
            d.rounded_rectangle([x, top, x + bw, base_y], radius=14, fill=col)
            d.text((x + bw // 2, top + 14), nv, font=font('calibrib.ttf', 56), fill=BLANCO, anchor='mt')
            d.text((x + bw // 2, top + 82), hrs, font=font('calibri.ttf', 26), fill=(255, 240, 225), anchor='mt')
            d.text((x + bw // 2, base_y - 38), peso(pr), font=font('calibrib.ttf', 28), fill=BLANCO, anchor='mt')
        else:
            d.rounded_rectangle([x, top, x + bw, base_y], radius=14, fill=CREMA, outline=GRIS_CLARO, width=3)
            d.text((x + bw // 2, top + 14), nv, font=font('calibrib.ttf', 56), fill=GRIS_CLARO, anchor='mt')
            d.text((x + bw // 2, top + 82), hrs, font=font('calibri.ttf', 26), fill=GRIS_CLARO, anchor='mt')
            d.text((x + bw // 2, base_y - 40), 'YA LO TIENES', font=font('calibrib.ttf', 22), fill=GRIS, anchor='mt')
    d.line([(x0, base_y + 2), (x0 + 4 * bw + 3 * gap, base_y + 2)], fill=CAFE, width=3)
    d.text((x0, base_y + 12), r.get('nota', 'Nivel suelto: sin beca.').replace('Ultimo', 'Último'), font=font('calibri.ttf', 24), fill=GRIS)
    lab = r['nombre'] + ' de lista:  '; off = 280 if 'nota' not in r else 480
    d.text((x0 + off, base_y + 12), lab, font=font('calibri.ttf', 24), fill=GRIS)
    d.text((x0 + off + d.textlength(lab, font=font('calibri.ttf', 24)), base_y + 8), peso(r['full']), font=font('calibrib.ttf', 32), fill=CAFE)

    # plan a cuotas (rango Transformación → General)
    pT = r['full'] * (1 - r['bq'][0] / 100); pG = r['full'] * (1 - r['bq'][1] / 100)
    py = base_y + 70
    d.text((x0, py), 'TU PLAN A CUOTAS', font=font('calibrib.ttf', 26), fill=NAR)
    d.text((x0 + 250, py + 3), 'beca del Fondo a cuotas del %s al %s · inicial del 20%% · el resto mensual' % (pct(r['bq'][1]), pct(r['bq'][0])),
           font=font('calibri.ttf', 21), fill=GRIS)
    for j, (nombre, n, dur) in enumerate((('Intensivo 2 h · L-V 6:30 a 8:30 pm', r['n2'], r['dur2']), ('Súper intensivo 4 h · L-V 8:00 a 12:00', r['n4'], r['dur4']))):
        bx = x0 + j * 475; by = py + 40
        d.rounded_rectangle([bx, by, bx + 455, by + 120], radius=16, fill=BLANCO, outline=NAR, width=3)
        d.text((bx + 18, by + 12), nombre, font=font('calibrib.ttf', 22), fill=NAR)
        d.text((bx + 18, by + 42), '%s · hasta %d cuotas' % (dur, n), font=font('calibri.ttf', 20), fill=GRIS)
        cT = cuota(pT * (1 - INICIAL), n); cG = cuota(pG * (1 - INICIAL), n)
        d.text((bx + 18, by + 70), '%d cuotas de %s a %s' % (n, peso(cT), peso(cG)), font=font('calibrib.ttf', 26), fill=CAFE)
    d.text((x0, py + 176), 'Inicial del 20%%: de %s a %s · Separas hoy con $300.000 y se cruza con la inicial · Pagas antes de terminar el programa' % (peso(pT * INICIAL), peso(pG * INICIAL)),
           font=font('calibri.ttf', 20), fill=CAFE)
    d.text((x0, py + 204), 'Las cuotas incluyen el costo de financiación. Menos cuotas, menor valor total. Tu plan queda por escrito el día que firmas.',
           font=font('calibri.ttf', 20), fill=GRIS)

    # tarjeta contado
    cx, cy, cw, ch = 1150, 190, 380, 300
    d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=20, fill=NAR)
    d.text((cx + cw // 2, cy + 22), 'DE CONTADO, LA BECA SUBE', font=font('calibrib.ttf', 28), fill=AMAR, anchor='mt')
    d.text((cx + cw // 2, cy + 62), 'según el perfil del estudiante', font=font('calibri.ttf', 22), fill=BLANCO, anchor='mt')
    d.text((cx + cw // 2, cy + 104), 'del %s al %s' % (pct(r['bc'][0]), pct(r['bc'][1])), font=font('calibrib.ttf', 46), fill=BLANCO, anchor='mt')
    d.text((cx + cw // 2, cy + 168), r['nombre'] + ', de contado', font=font('calibri.ttf', 21), fill=(255, 230, 210), anchor='mt')
    d.text((cx + cw // 2, cy + 196), 'desde ' + peso(r['full'] * (1 - r['bc'][1] / 100)), font=font('calibrib.ttf', 34), fill=AMAR, anchor='mt')
    d.text((cx + cw // 2, cy + 246), 'Cesantías, crédito con tu banco o cooperativa', font=font('calibri.ttf', 18), fill=(255, 230, 210), anchor='mt')
    d.text((cx + cw // 2, cy + 270), 'y tarjeta de crédito cuentan como contado.', font=font('calibri.ttf', 18), fill=(255, 230, 210), anchor='mt')

    # tarjeta qué incluye
    cy2 = cy + ch + 24; ch2 = 236
    d.rounded_rectangle([cx, cy2, cx + cw, cy2 + ch2], radius=20, fill=BLANCO, outline=NAR, width=3)
    d.text((cx + 22, cy2 + 18), 'QUÉ INCLUYE', font=font('calibrib.ttf', 26), fill=NAR)
    incl = r.get('incluye', ['Garantía de aprendizaje por escrito', 'Clases presenciales en grupo', 'Video diario revisado por tu profesor',
                           'Reporte de asistencia y avance', 'Libros incluidos si separas hoy', 'Afiliados a Cajasan: condiciones', 'especiales con carné o certificado vigente'])
    for i, t in enumerate(incl):
        d.text((cx + 22, cy2 + 54 + i * 26), t, font=font('calibri.ttf', 20), fill=CAFE if ('incluye' in r or i < 5) else GRIS)

    d.text((x0, H - 46), r.get('pie', 'Separa tu cupo con $300.000 y congela el precio · Única academia presencial de Bucaramanga con garantía de aprendizaje por escrito'),
           font=font('calibri.ttf', 21), fill=GRIS)

    out = os.path.join(r.get('outdir', OUTDIR), 'CUOTAS_2026_%s.png' % clave)
    try: img.save(out, optimize=True); print('OK', out)
    except OSError: img.save(out.replace('.png', '_v2.png'), optimize=True); print('ABIERTA -> _v2', out)
    for n in (r['n2'], r['n4']):
        print('   %d cuotas: %s a %s | inicial %s a %s' % (n, peso(cuota(pT * 0.8, n)), peso(cuota(pG * 0.8, n)), peso(pT * 0.2), peso(pG * 0.2)))

if __name__ == '__main__':
    for k in RUTAS: pieza(k)
