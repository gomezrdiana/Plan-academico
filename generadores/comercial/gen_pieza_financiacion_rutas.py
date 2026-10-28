# -*- coding: utf-8 -*-
"""Piezas 'Financiado con Heiiu' por ruta (A2 → B2 y B1 → B2), mismo marco que las láminas de precios 2026.
Fuente de números: matriz del kit (gen_kit_bonito.py) = beca de CUOTAS por perfil, inicial 20%, interés del crédito
directo 1,9% mensual sobre saldo (cuota fija), máximo de cuotas por jornada (gen_aclaracion_becas_cuotas.py).
Salida: recursos/comercial/INDUCCION_COMERCIAL/FINANCIADO_2026_A2_B2.png y FINANCIADO_2026_B1_B2.png
Uso: python -X utf8 generadores/comercial/gen_pieza_financiacion_rutas.py"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
CREMA = (255, 248, 231); NAR = (229, 76, 9); AMAR = (251, 201, 0); CAFE = (48, 39, 28); GRIS = (120, 110, 100); BLANCO = (255, 255, 255)
F = 'C:/Windows/Fonts/'
def font(n, s): return ImageFont.truetype(F + n, s)
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTDIR = os.path.join(BASE, 'recursos', 'comercial', 'INDUCCION_COMERCIAL')

RUTAS = {
    'A2_B2': dict(titulo='A2 → B2 FINANCIADO CON HEIIU', nombre='Programa A2 → B2', horas=485, full=7100000,
                  becas=[('TRANSFORMACIÓN', 'estrato 1-2 con soporte o afiliado a Cajasan', 27, 36),
                         ('GENERAL', 'todos los demás', 19.2, 25.6),
                         ('EJECUTIVO', 'paga su empresa', 9, 12)],
                  n2=11, n4=5, dur2='~12 meses', dur4='~6 meses'),
    'B1_B2': dict(titulo='B1 → B2 FINANCIADO CON HEIIU', nombre='Programa B1 → B2', horas=375, full=5185000,
                  becas=[('TRANSFORMACIÓN', 'estrato 1-2 con soporte o afiliado a Cajasan', 15.8, 24.8),
                         ('GENERAL', 'todos los demás', 11.2, 17.6),
                         ('EJECUTIVO', 'paga su empresa', 5.3, 8.3)],
                  n2=8, n4=3, dur2='~9 meses', dur4='~4 meses'),
}
INICIAL = 0.20; TASA = 0.019
def peso(x): return '$' + format(int(round(x)), ',').replace(',', '.')
def cuota(saldo, n): return saldo * TASA / (1 - (1 + TASA) ** -n)
def pct(p): return ('%g' % p).replace('.', ',') + '%'

def marco(titulo, sub):
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
    d.text((W // 2 + 60, 60), titulo, font=font('calibrib.ttf', 50), fill=CAFE, anchor='mt')
    d.text((W // 2 + 60, 120), sub, font=font('calibri.ttf', 24), fill=GRIS, anchor='mt')
    return img, d

def pieza(clave):
    r = RUTAS[clave]
    img, d = marco(r['titulo'], '%s · %d horas presenciales · garantía por escrito · plan de pagos firmado' % (r['nombre'], r['horas']))

    # tabla principal
    x0, y0 = 150, 185; colw = [330, 300, 300]; tw = sum(colw) + 20
    rowh = 118; headh = 70
    d.rounded_rectangle([x0, y0, x0 + tw, y0 + headh + rowh * 3 + 16], radius=18, fill=BLANCO, outline=NAR, width=3)
    # cabecera
    cx = x0 + 20
    d.text((cx, y0 + 16), 'PERFIL', font=font('calibrib.ttf', 24), fill=NAR)
    d.text((cx, y0 + 44), 'precio de lista ' + peso(r['full']), font=font('calibri.ttf', 19), fill=GRIS)
    cx += colw[0]
    d.text((cx + colw[1] // 2, y0 + 14), 'INTENSIVO 2 h', font=font('calibrib.ttf', 24), fill=NAR, anchor='mt')
    d.text((cx + colw[1] // 2, y0 + 44), 'hasta %d cuotas · %s' % (r['n2'], r['dur2']), font=font('calibri.ttf', 19), fill=GRIS, anchor='mt')
    cx += colw[1]
    d.text((cx + colw[2] // 2, y0 + 14), 'SÚPER INTENSIVO 4 h', font=font('calibrib.ttf', 24), fill=NAR, anchor='mt')
    d.text((cx + colw[2] // 2, y0 + 44), 'hasta %d cuotas · %s' % (r['n4'], r['dur4']), font=font('calibri.ttf', 19), fill=GRIS, anchor='mt')
    d.line([(x0 + 14, y0 + headh), (x0 + tw - 14, y0 + headh)], fill=NAR, width=2)
    for i, (perfil, quien, bq, bc) in enumerate(r['becas']):
        y = y0 + headh + i * rowh + 10
        if i: d.line([(x0 + 14, y - 8), (x0 + tw - 14, y - 8)], fill=(235, 225, 210), width=2)
        precio = r['full'] * (1 - bq / 100); ini = precio * INICIAL; saldo = precio - ini
        cx = x0 + 20
        d.text((cx, y + 4), perfil, font=font('calibrib.ttf', 24), fill=CAFE)
        d.text((cx, y + 34), quien, font=font('calibri.ttf', 18), fill=GRIS)
        d.text((cx, y + 58), 'beca a cuotas ' + pct(bq) + ' → ' + peso(precio), font=font('calibrib.ttf', 20), fill=NAR)
        d.text((cx, y + 84), 'inicial 20%: ' + peso(ini), font=font('calibri.ttf', 19), fill=CAFE)
        for j, n in enumerate((r['n2'], r['n4'])):
            ccx = x0 + 20 + colw[0] + j * colw[1] + colw[1] // 2
            d.text((ccx, y + 10), '%d cuotas de' % n, font=font('calibri.ttf', 22), fill=GRIS, anchor='mt')
            d.text((ccx, y + 38), peso(cuota(saldo, n)), font=font('calibrib.ttf', 34), fill=CAFE, anchor='mt')
            d.text((ccx, y + 84), 'o menos cuotas, más bajas en total', font=font('calibri.ttf', 16), fill=GRIS, anchor='mt')

    # tarjeta: cómo funciona
    cx, cy, cw = 1130, 185, 400
    d.rounded_rectangle([cx, cy, cx + cw, cy + 330], radius=20, fill=NAR)
    d.text((cx + cw // 2, cy + 20), 'CÓMO FUNCIONA', font=font('calibrib.ttf', 28), fill=AMAR, anchor='mt')
    lineas = ['1. Separas tu cupo con $300.000 hoy:', '    se cruza con la inicial.', '2. Inicial del 20% a los 3 días.',
              '3. Cuotas mensuales desde el día 30.', '4. Terminas de pagar antes de', '    terminar el programa.',
              '5. Pagaré y plan de pagos firmados.', '6. Las cuotas incluyen el costo', '    de financiación de Heiiu.']
    for i, t in enumerate(lineas):
        d.text((cx + 22, cy + 64 + i * 28), t, font=font('calibri.ttf', 21), fill=BLANCO)

    # tarjeta: contado
    cy2 = cy + 330 + 22
    d.rounded_rectangle([cx, cy2, cx + cw, cy2 + 196], radius=20, fill=BLANCO, outline=NAR, width=3)
    d.text((cx + 22, cy2 + 16), 'SI PAGAS DE CONTADO, LA BECA SUBE', font=font('calibrib.ttf', 22), fill=NAR)
    d.text((cx + 22, cy2 + 50), 'Cesantías, crédito con tu banco o', font=font('calibri.ttf', 20), fill=CAFE)
    d.text((cx + 22, cy2 + 76), 'cooperativa, o tarjeta de crédito', font=font('calibri.ttf', 20), fill=CAFE)
    d.text((cx + 22, cy2 + 102), 'cuentan como contado.', font=font('calibri.ttf', 20), fill=CAFE)
    bc_min = r['becas'][1][3]; bc_max = r['becas'][0][3]
    d.text((cx + 22, cy2 + 132), 'Beca del %s al %s' % (pct(bc_min), pct(bc_max)), font=font('calibrib.ttf', 21), fill=CAFE)
    d.text((cx + 22, cy2 + 158), 'de contado desde ' + peso(r['full'] * (1 - bc_max / 100)), font=font('calibrib.ttf', 21), fill=NAR)

    # sello de uso interno (la matriz por perfil no se muestra al cliente: se le dice su celda)
    d.rounded_rectangle([150, 700, 150 + 560, 740], radius=10, fill=AMAR)
    d.text((150 + 280, 720), 'USO INTERNO DE LA ASESORA · NO SE ENVÍA NI SE MUESTRA AL CLIENTE', font=font('calibrib.ttf', 17), fill=CAFE, anchor='mm')
    d.text((150, 750), 'Al cliente se le da SU plan por escrito: inicial + número de cuotas + valor de cada cuota. Nunca la tabla completa.', font=font('calibri.ttf', 20), fill=GRIS)

    # pie
    d.text((150, H - 112), 'Las becas del Fondo se evalúan con soportes en la asesoría. El plan exacto (inicial, número de cuotas y valor) lo entrega la asesora por escrito.',
           font=font('calibri.ttf', 21), fill=GRIS)
    d.text((150, H - 80), 'Nivel suelto y sabatino: sin beca del Fondo. Afiliados a Cajasan: condiciones especiales (se confirman en la asesoría).',
           font=font('calibri.ttf', 21), fill=GRIS)
    d.text((150, H - 46), 'Única academia presencial de Bucaramanga con garantía de aprendizaje por escrito.',
           font=font('calibri.ttf', 21), fill=GRIS)

    out = os.path.join(OUTDIR, 'FINANCIADO_2026_%s.png' % clave)
    try: img.save(out, optimize=True); print('OK', out)
    except OSError: img.save(out.replace('.png', '_v2.png'), optimize=True); print('ABIERTA -> _v2', out)
    for perfil, quien, bq, bc in r['becas']:
        precio = r['full'] * (1 - bq / 100); saldo = precio * (1 - INICIAL)
        print('  %-14s precio %s inicial %s | %d cuotas %s | %d cuotas %s' % (perfil, peso(precio), peso(precio * INICIAL),
              r['n2'], peso(cuota(saldo, r['n2'])), r['n4'], peso(cuota(saldo, r['n4']))))

if __name__ == '__main__':
    for k in RUTAS: pieza(k)
