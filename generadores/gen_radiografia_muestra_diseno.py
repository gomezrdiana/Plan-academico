# Radiografía de MUESTRA con diseño de marca (navy/gold) para compartir pantalla.
# Datos ILUSTRATIVOS (restaurante ficticio) — marcado como ejemplo en cada página.
# Correr desde la raíz del repo.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

NAVY = HexColor('#152A4A')
NAVY_LT = HexColor('#3D5A80')
GOLD = HexColor('#C9A227')
CREAM = HexColor('#F5F0E6')
INK = HexColor('#2E2E2E')
MUTED = HexColor('#6B7280')
GOOD = HexColor('#2E7D32')
WARN = HexColor('#B26A00')
BAD = HexColor('#C62828')

W, H = letter
OUT = os.path.join('recursos', 'comercial', 'CFO', 'RADIOGRAFIA_MUESTRA_DISENO.pdf')
c = canvas.Canvas(OUT, pagesize=letter)


def header(title, subtitle):
    c.setFillColor(NAVY); c.rect(0, H - 88, W, 88, stroke=0, fill=1)
    c.setFillColor(GOLD); c.rect(0, H - 91, W, 3, stroke=0, fill=1)
    c.setFillColor(GOLD); c.setFont('Helvetica-Bold', 8.5)
    c.drawString(20 * mm, H - 24, 'CARLOS EDO REMOLINA  ·  DIRECTOR FINANCIERO EXTERNO')
    c.setFillColor(white); c.setFont('Helvetica-Bold', 19)
    c.drawString(20 * mm, H - 48, title)
    c.setFillColor(HexColor('#C8D0DC')); c.setFont('Helvetica', 10)
    c.drawString(20 * mm, H - 66, subtitle)
    # Badge MUESTRA
    c.setFillColor(GOLD); c.roundRect(W - 72 * mm, H - 58, 54 * mm, 16, 8, stroke=0, fill=1)
    c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 7.5)
    c.drawCentredString(W - 45 * mm, H - 53, 'MUESTRA · DATOS ILUSTRATIVOS')


def footer(page):
    c.setFillColor(GOLD); c.rect(0, 16, W, 2, stroke=0, fill=1)
    c.setFillColor(NAVY); c.rect(0, 0, W, 16, stroke=0, fill=1)
    c.setFillColor(HexColor('#C8D0DC')); c.setFont('Helvetica', 7.5)
    c.drawCentredString(W / 2, 5, f'Radiografía Financiera de MUESTRA — ejemplo ilustrativo, no corresponde a ninguna empresa real · p.{page}')


def status_chip(x, y, kind):
    col, icon, word = {'good': (GOOD, '✓', 'SANO'), 'warn': (WARN, '!', 'ALERTA'), 'bad': (BAD, '×', 'CRÍTICO')}[kind]
    c.setFillColor(col); c.roundRect(x, y, 58, 13, 6.5, stroke=0, fill=1)
    c.setFillColor(white); c.setFont('Helvetica-Bold', 7.5)
    c.drawCentredString(x + 29, y + 3.5, f'{icon} {word}')


def tile(x, y, w, h, label, value, kind, note=''):
    c.setFillColor(CREAM); c.roundRect(x, y, w, h, 6, stroke=0, fill=1)
    c.setFillColor(GOLD); c.rect(x, y, 3, h, stroke=0, fill=1)
    c.setFillColor(MUTED); c.setFont('Helvetica-Bold', 7.5)
    c.drawString(x + 10, y + h - 14, label.upper())
    c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 15)
    c.drawString(x + 10, y + h - 34, value)
    if note:
        c.setFillColor(MUTED); c.setFont('Helvetica', 7.5)
        c.drawString(x + 10, y + h - 46, note)
    status_chip(x + w - 66, y + 8, kind)


# ---------------- PÁGINA 1 — LOS 5 NÚMEROS + VEREDICTO ----------------
header('RADIOGRAFÍA FINANCIERA', 'Restaurante familiar · 14 empleados · Periodo analizado: últimos 12 meses')

c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 12)
c.drawString(20 * mm, H - 116, 'EL NEGOCIO EN 5 NÚMEROS')
c.setStrokeColor(GOLD); c.setLineWidth(1.2); c.line(20 * mm, H - 121, W - 20 * mm, H - 121)

tw = (W - 40 * mm - 16) / 2
tiles = [
    ('Ventas', '$65.000 / mes', 'good', '$780.000 al año — el negocio SÍ vende'),
    ('Costo de comida', '36% de ventas', 'bad', 'Sano: 28-31% — cada punto son $650/mes'),
    ('Nómina', '34% de ventas', 'bad', 'Sano: 28-30% — horas extra sin control'),
    ('Lo que queda LIBRE', '$2.100 / mes (3,2%)', 'bad', 'Sano: $7.800-10.400 (12-16%)'),
]
y0 = H - 190
for i, (lab, val, kind, note) in enumerate(tiles):
    x = 20 * mm + (i % 2) * (tw + 16)
    y = y0 - (i // 2) * 64
    tile(x, y, tw, 56, lab, val, kind, note)

tile(20 * mm, y0 - 128 - 8, W - 40 * mm, 56, 'Caja disponible', 'No se sabe', 'bad',
     'Cuenta personal y del negocio mezcladas — el punto ciego que tapa todos los demás')

# Veredicto
vy = y0 - 128 - 8 - 96
c.setFillColor(NAVY); c.roundRect(20 * mm, vy, W - 40 * mm, 78, 8, stroke=0, fill=1)
c.setFillColor(GOLD); c.setFont('Helvetica-Bold', 11)
c.drawString(26 * mm, vy + 60, 'EL VEREDICTO')
c.setFillColor(white); c.setFont('Helvetica', 10)
c.drawString(26 * mm, vy + 44, 'Este negocio NO tiene un problema de ventas. Tiene un problema de números que nadie mira:')
c.drawString(26 * mm, vy + 30, 'de cada $100 que vende, $97 se van — y nadie sabe exactamente por dónde.')
c.setFont('Helvetica-Bold', 12); c.setFillColor(GOLD)
c.drawString(26 * mm, vy + 10, 'Fugas identificadas: $96.700 al año — un sueldo ejecutivo completo, regalado.')
footer(1); c.showPage()

# ---------------- PÁGINA 2 — LAS 3 FUGAS (BARRAS) + SUELDO DE DUEÑO ----------------
header('LAS 3 FUGAS DE DINERO', 'Cuantificadas — qué son, cuánto valen y qué se hace con cada una')

c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 12)
c.drawString(20 * mm, H - 116, 'CUÁNTO VALE CADA FUGA (al año)')
c.setStrokeColor(GOLD); c.setLineWidth(1.2); c.line(20 * mm, H - 121, W - 20 * mm, H - 121)

fugas = [('Costo de comida (36% vs 30%)', 46800), ('Nómina — horas extra y turnos', 31200), ('Apps de delivery sin repricing', 18700)]
bx, bw_max, bh, gap = 20 * mm, 118 * mm, 24, 14
by = H - 160
for i, (lab, val) in enumerate(fugas):
    y = by - i * (bh + gap + 12)
    c.setFillColor(INK); c.setFont('Helvetica-Bold', 9.5)
    c.drawString(bx, y + bh + 3, lab)
    w = bw_max * (val / fugas[0][1])
    c.setFillColor(NAVY)
    c.rect(bx, y, max(w - 4, 1), bh, stroke=0, fill=1)
    c.roundRect(bx + w - 8, y, 8, bh, 4, stroke=0, fill=1)
    c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 12)
    c.drawString(bx + w + 8, y + 7, f'${val:,}'.replace(',', '.'))

ty = by - 3 * (bh + gap + 12) - 6
c.setFillColor(CREAM); c.roundRect(20 * mm, ty - 40, W - 40 * mm, 40, 6, stroke=0, fill=1)
c.setFillColor(GOLD); c.rect(20 * mm, ty - 40, 3, 40, stroke=0, fill=1)
c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 11)
c.drawString(26 * mm, ty - 16, 'TOTAL RECUPERABLE:  $96.700 / año   ·   ~$8.000 / mes')
c.setFillColor(MUTED); c.setFont('Helvetica', 8.5)
c.drawString(26 * mm, ty - 30, 'Sin vender un plato más y sin despedir a nadie — solo mirando los números todos los meses.')

# Sueldo de dueño — número héroe
hy = ty - 60
c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 12)
c.drawString(20 * mm, hy - 8, 'Y EL NÚMERO MÁS IMPORTANTE PARA USTED:')
c.setStrokeColor(GOLD); c.line(20 * mm, hy - 13, W - 20 * mm, hy - 13)
c.setFillColor(NAVY); c.roundRect(20 * mm, hy - 92, W - 40 * mm, 70, 8, stroke=0, fill=1)
c.setFillColor(GOLD); c.setFont('Helvetica-Bold', 10)
c.drawString(26 * mm, hy - 40, 'SU SUELDO DE DUEÑO')
c.setFillColor(white); c.setFont('Helvetica-Bold', 24)
c.drawString(26 * mm, hy - 66, '$4.500 / mes — fijo, desde el mes 2')
c.setFillColor(HexColor('#C8D0DC')); c.setFont('Helvetica', 9)
c.drawString(26 * mm, hy - 82, 'Se acabó "sacar cuando hay": usted se paga primero, sin culpa y sin ahogar el negocio.')
footer(2); c.showPage()

# ---------------- PÁGINA 3 — PLAN 90 DÍAS + TABLERO ----------------
header('EL PLAN DE 90 DÍAS', 'De la radiografía a la recuperación — y el tablero que usted recibe cada mes')

rows = [
    ('Días 1-30', 'Separar cuentas · sueldo de dueño · fichas de porción · registro de merma · cotizar proveedores', 'El negocio se ve completo por primera vez'),
    ('Días 31-60', 'Renegociar 2 proveedores · reajustar 2 turnos · precios de app diferenciados · flujo de caja proyectado', '$4.000-5.500/mes recuperándose'),
    ('Días 61-90', 'Flujo de 13 semanas rodando · metas por indicador · decisiones grandes CON números', '$6.000-7.000/mes de mejora sostenida'),
]
yy = H - 120
for fase, acc, res in rows:
    c.setFillColor(CREAM); c.roundRect(20 * mm, yy - 52, W - 40 * mm, 52, 6, stroke=0, fill=1)
    c.setFillColor(GOLD); c.rect(20 * mm, yy - 52, 3, 52, stroke=0, fill=1)
    c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 10.5); c.drawString(26 * mm, yy - 16, fase)
    c.setFillColor(INK); c.setFont('Helvetica', 8.5); c.drawString(26 * mm, yy - 30, acc)
    c.setFillColor(GOOD); c.setFont('Helvetica-Bold', 9); c.drawString(26 * mm, yy - 44, '→ ' + res)
    yy -= 62

c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 12)
c.drawString(20 * mm, yy - 10, 'EL TABLERO QUE USTED RECIBE CADA MES (1 página)')
c.setStrokeColor(GOLD); c.line(20 * mm, yy - 15, W - 20 * mm, yy - 15)

tab = [
    ('Indicador', 'Este mes', 'Mes pasado', 'Meta', 'Estado'),
    ('Ventas', '$67.200', '$65.000', '$65.000', 'good'),
    ('Costo de comida', '33,1%', '36,0%', '31%', 'warn'),
    ('Nómina', '31,5%', '34,0%', '30%', 'warn'),
    ('Libre del mes', '$5.900', '$2.100', '$8.400', 'warn'),
    ('Caja fin de mes', '$18.300', '$11.700', '$40.000', 'bad'),
]
col_x = [20 * mm, 70 * mm, 100 * mm, 130 * mm, 158 * mm]
ty2 = yy - 34
c.setFillColor(NAVY); c.rect(20 * mm, ty2 - 4, W - 40 * mm, 18, stroke=0, fill=1)
c.setFillColor(white); c.setFont('Helvetica-Bold', 8.5)
for j, htxt in enumerate(tab[0]):
    c.drawString(col_x[j] + 4, ty2, htxt)
for i, row in enumerate(tab[1:]):
    ry = ty2 - 20 - i * 20
    if i % 2 == 0:
        c.setFillColor(HexColor('#F7F7F5')); c.rect(20 * mm, ry - 5, W - 40 * mm, 20, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont('Helvetica', 9)
    for j in range(4):
        c.drawString(col_x[j] + 4, ry, row[j])
    status_chip(col_x[4], ry - 3, row[4])

gy = ty2 - 20 - 5 * 20 - 16
c.setFillColor(CREAM); c.roundRect(20 * mm, gy - 34, W - 40 * mm, 38, 6, stroke=0, fill=1)
c.setFillColor(GOLD); c.rect(20 * mm, gy - 34, 3, 38, stroke=0, fill=1)
c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 9.5)
c.drawString(26 * mm, gy - 12, 'MI GARANTÍA: si no le encuentro hallazgos que valgan más de lo que pagó, no me paga.')
c.setFillColor(MUTED); c.setFont('Helvetica', 8.5)
c.drawString(26 * mm, gy - 26, 'La suya se construye con SUS números: solo lectura de su contabilidad, 3 extractos y 45 minutos suyos.')
footer(3); c.save()
print('OK:', OUT)
