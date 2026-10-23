# -*- coding: utf-8 -*-
"""Un QR por codigo de asesora para el programa de referidos de entidades aliadas.
Cada QR abre WhatsApp en la linea de alianzas con el mensaje ya escrito y el codigo de la asesora.
Lee los codigos de codigos_asesoras.txt (uno por linea, sin nombres; lineas con # se ignoran) en la carpeta
del gerente de alianzas / plan referidos (fuera de git). Si el archivo no existe, genera solo el de ejemplo C-07.
Salida: plan referidos/QR/QR_{codigo}.png (tarjeta 600x780 con el QR, el codigo y la instruccion). Uso:
    python generadores/comercial/gen_qr_asesoras.py"""
import os
from urllib.parse import quote
import qrcode
from PIL import Image, ImageDraw, ImageFont

LINEA = '573167688793'   # linea de alianzas (316 768 8793), nunca la linea principal
MENSAJE = 'Hola, quiero información para estudiar inglés en Heiiu. Código de asesor: {codigo}'
ROOT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
CARPETA = ROOT + r'\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza\plan referidos'
LISTA = os.path.join(CARPETA, 'codigos_asesoras.txt')
OUTDIR = os.path.join(CARPETA, 'QR')
NAR = (229, 76, 9); OSC = (48, 39, 28); GRIS = (110, 100, 88); CREMA = (255, 248, 231)
def font(n, s): return ImageFont.truetype('C:/Windows/Fonts/' + n, s)

def enlace(codigo): return 'https://wa.me/%s?text=%s' % (LINEA, quote(MENSAJE.format(codigo=codigo)))

def tarjeta(codigo):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=2)
    qr.add_data(enlace(codigo)); qr.make(fit=True)
    q = qr.make_image(fill_color=OSC, back_color='white').convert('RGB').resize((480, 480), Image.NEAREST)
    W, H = 600, 780
    img = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 90], fill=NAR)
    d.text((W // 2, 45), 'HEIIU · PROGRAMA DE REFERIDOS', font=font('calibrib.ttf', 30), fill=CREMA, anchor='mm')
    img.paste(q, ((W - 480) // 2, 110))
    d.text((W // 2, 630), 'Código de asesor', font=font('calibri.ttf', 26), fill=GRIS, anchor='mm')
    d.text((W // 2, 680), codigo, font=font('calibrib.ttf', 54), fill=NAR, anchor='mm')
    d.text((W // 2, 740), 'Escanea y envía el mensaje: ya lleva tu código.', font=font('calibri.ttf', 24), fill=OSC, anchor='mm')
    return img

if os.path.exists(LISTA):
    codigos = [l.strip() for l in open(LISTA, encoding='utf-8') if l.strip() and not l.startswith('#')]
else:
    codigos = ['C-07']; print('No existe', LISTA, '-> solo el ejemplo C-07')
os.makedirs(OUTDIR, exist_ok=True)
lineas = []
for c in codigos:
    out = os.path.join(OUTDIR, 'QR_%s.png' % c)
    tarjeta(c).save(out); print('OK', c); lineas.append('%s	%s' % (c, enlace(c)))
with open(os.path.join(OUTDIR, 'ENLACES_CODIGOS.txt'), 'w', encoding='utf-8') as f:
    f.write('Enlace de WhatsApp por codigo (es el mismo que abre el QR). La asesora lo reenvia al afiliado tal cual.

' + '
'.join(lineas) + '
')
print('ENLACES_CODIGOS.txt ok')
