# -*- coding: utf-8 -*-
"""MOTOR DE CUOTAS 2026 en PDF (uso interno del asesor). Misma matriz y misma formula que
gen_motor_cuotas.py (Excel). Una pagina por paquete, letra grande, sin tasa impresa:
al cliente se le dicta SU plan (inicial + numero de cuotas + valor), nunca la tabla."""
import os, sys
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'INDUCCION_COMERCIAL', 'MOTOR_CUOTAS_FONDO_2026_ASESOR.pdf')

FULL = {'A1-B2 completo': 8696000, 'A2-B2': 7100000, 'B1-B2': 5185000, 'Solo B2': 2343000}
PCT = {
 'A1-B2 completo': {'TRANSFORMACION': (45, 36), 'GENERAL': (32, 25.6), 'EJECUTIVO': (15, 12)},
 'A2-B2':          {'TRANSFORMACION': (36, 27), 'GENERAL': (25.6, 19.2), 'EJECUTIVO': (12, 9)},
 'B1-B2':          {'TRANSFORMACION': (24.8, 15.8), 'GENERAL': (17.6, 11.2), 'EJECUTIVO': (8.3, 5.3)},
 'Solo B2':        {'TRANSFORMACION': (20.3, 11.3), 'GENERAL': (14.4, 8), 'EJECUTIVO': (6.8, 3.8)},
}
MODALIDADES = {
 'A1-B2 completo': [('Súper intensivo 20 h/sem · ~7 meses · máximo 5 cuotas', [3, 4, 5]),
                    ('Intensivo 10 h/sem · ~14 meses · máximo 11 cuotas', [4, 6, 8, 10, 11])],
 'A2-B2':          [('Súper intensivo 20 h/sem · ~6 meses · máximo 5 cuotas', [3, 4, 5]),
                    ('Intensivo 10 h/sem · ~12 meses · máximo 11 cuotas', [4, 6, 8, 10, 11])],
 'B1-B2':          [('Súper intensivo 20 h/sem · ~4,5 meses · máximo 3 cuotas', [2, 3]),
                    ('Intensivo 10 h/sem · ~9 meses · máximo 8 cuotas', [4, 6, 8])],
 'Solo B2':        [('Intensivo 10 h/sem · ~5 meses · máximo 4 cuotas (en súper intensivo dura ~2,5 meses: prácticamente contado)', [2, 3, 4])],
}
PERFIL_TXT = {
 'TRANSFORMACION': 'TRANSFORMACIÓN · estrato 1 o 2 con soporte, afiliado a Cajasan con carné vigente, o carta de empresa aliada',
 'GENERAL': 'GENERAL · todos los demás',
 'EJECUTIVO': 'EJECUTIVO · ruta ejecutiva / empresa paga',
}
INICIALES = [0.20, 0.30, 0.40, 0.50]
r = 0.019

def cuota(saldo, n):
    return round(saldo * r / (1 - (1 + r) ** -n))

def pesos(v):
    return '$' + format(int(round(v)), ',').replace(',', '.')

NAR = colors.HexColor('#E54C09'); CREMA = colors.HexColor('#FFF8E7'); GRIS = colors.HexColor('#EEEEEE')
H1 = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=16, leading=19, textColor=NAR, spaceAfter=4)
H2 = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, spaceAfter=2)
TXT = ParagraphStyle('t', fontName='Helvetica', fontSize=8.5, leading=11)
AVISO = ParagraphStyle('a', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=NAR)
CEL = ParagraphStyle('c', fontName='Helvetica', fontSize=9.5, leading=11)
CELB = ParagraphStyle('cb', fontName='Helvetica-Bold', fontSize=9.5, leading=11)

REGLAS = ('<b>Reglas que no se negocian:</b> separación de cupo $300.000 hoy (se cruza con la inicial) · inicial mínima 20 % '
          'máximo 3 días después · cuotas desde el día 30 · el estudiante termina de pagar ANTES de terminar el programa, por eso '
          'cada modalidad tiene su máximo de cuotas · menos cuotas siempre se puede, más que el máximo nunca · las cuotas ya '
          'incluyen el costo del crédito directo de la academia · nunca se suman dos becas: se aplica la mejor · '
          'el plan (pagaré, carta y plan de pagos) se firma en la sede con coordinación.')
AL_CLIENTE = ('<b>AL CLIENTE SE LE DICTA SU PLAN, NO SE LE MUESTRA ESTA HOJA:</b> "Tu inicial es X, y son N cuotas de Y". '
              'Siempre el plan completo (inicial + número de cuotas + valor), nunca solo la cuota. No se dice "financiación '
              'sin interés" ni "descuento": se dice "beca del Fondo" y "crédito directo de la academia". Una combinación que no '
              'esté aquí la calcula coordinación, nunca de memoria.')

def tabla_modalidad(nombre, ncols, base_q, ancho_total):
    """Compatibilidad: una sola modalidad."""
    return tabla_perfil([(nombre, ncols)], base_q, ancho_total)

def tabla_perfil(mods, base_q, ancho_total):
    """Una tabla por perfil: las modalidades van lado a lado (fila 1 = nombre de la modalidad sobre sus columnas)."""
    todas = [n for _, ncols in mods for n in ncols]
    fila_mod = [Paragraph('<b>Modalidad</b>', CELB)]
    spans = []
    c0 = 1
    for nombre, ncols in mods:
        fila_mod.append(Paragraph('<b>' + nombre + '</b>', CELB))
        fila_mod.extend([''] * (len(ncols) - 1))
        spans.append(('SPAN', (c0, 0), (c0 + len(ncols) - 1, 0)))
        c0 += len(ncols)
    data = [fila_mod,
            [Paragraph('<b>Inicial</b>', CELB)] + [Paragraph('<b>%d cuotas</b>' % n, CELB) for n in todas]]
    for frac in INICIALES:
        ini = round(base_q * frac)
        saldo = base_q - ini
        data.append([Paragraph('%d %% = <b>%s</b>' % (int(frac * 100), pesos(ini)), CEL)] +
                    [Paragraph(pesos(cuota(saldo, n)), CEL) for n in todas])
    w0 = 4.6 * cm
    wc = (ancho_total - w0) / len(todas)
    t = Table(data, colWidths=[w0] + [wc] * len(todas))
    estilo = [('BACKGROUND', (0, 0), (-1, 0), GRIS), ('BACKGROUND', (0, 1), (-1, 1), CREMA),
              ('GRID', (0, 0), (-1, -1), 0.5, colors.grey), ('BOX', (0, 0), (-1, -1), 0.8, colors.black),
              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('TOPPADDING', (0, 0), (-1, -1), 2.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5)]
    # linea gruesa entre modalidades
    c0 = 1
    for _, ncols in mods[:-1]:
        c0 += len(ncols)
        estilo.append(('LINEBEFORE', (c0, 0), (c0, -1), 1.5, colors.black))
    t.setStyle(TableStyle(estilo + spans))
    return t

def pagina_paquete(story, paq, full, ancho):
    story.append(Paragraph('MOTOR DE CUOTAS 2026 · ' + paq + ' · precio de lista ' + pesos(full), H1))
    story.append(Paragraph('USO INTERNO DEL ASESOR · jamás se muestra ni se envía al cliente', AVISO))
    story.append(Paragraph(REGLAS, TXT)); story.append(Spacer(1, 4))
    for perfil, (pc_c, pc_q) in PCT[paq].items():
        base_c = round(full * (1 - pc_c / 100)); base_q = round(full * (1 - pc_q / 100))
        cab = Table([[Paragraph('<font color="white"><b>' + PERFIL_TXT[perfil] + '</b></font>', CELB),
                      Paragraph('<font color="white"><b>Contado: ' + pesos(base_c) + '</b></font>', CELB),
                      Paragraph('<font color="white"><b>Base a cuotas: ' + pesos(base_q) + '</b></font>', CELB)]],
                    colWidths=[ancho * 0.56, ancho * 0.20, ancho * 0.24])
        cab.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), NAR), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                 ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
        story.append(cab)
        story.append(tabla_perfil(MODALIDADES[paq], base_q, ancho))
        story.append(Spacer(1, 5))
    story.append(Paragraph(AL_CLIENTE, TXT))
    story.append(PageBreak())

def pagina_arranque(story, ancho):
    base = 2990000
    story.append(Paragraph('MOTOR DE CUOTAS 2026 · ARRANQUE A1+A2 · precio único ' + pesos(base) + ' (200 horas, sin becas)', H1))
    story.append(Paragraph('USO INTERNO DEL ASESOR · jamás se muestra ni se envía al cliente', AVISO))
    story.append(Paragraph(REGLAS.replace('nunca se suman dos becas: se aplica la mejor · ', ''), TXT)); story.append(Spacer(1, 4))
    cab = Table([[Paragraph('<font color="white"><b>Precio contado o a cuotas: ' + pesos(base) + ' · súper intensivo 20 h/sem ~2,5 meses: máximo 2 cuotas · intensivo 10 h/sem ~5 meses: máximo 4 cuotas</b></font>', CELB)]], colWidths=[ancho])
    cab.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), NAR), ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
    story.append(cab)
    story.append(tabla_modalidad('Arranque A1+A2 (la columna de 2 cuotas sirve para súper intensivo; 3 y 4 solo intensivo)', [2, 3, 4], base, ancho))
    story.append(Spacer(1, 5)); story.append(Paragraph(AL_CLIENTE, TXT))

def main():
    doc = SimpleDocTemplate(OUT, pagesize=landscape(letter), leftMargin=1.2 * cm, rightMargin=1.2 * cm, topMargin=1.0 * cm, bottomMargin=0.9 * cm,
                            title='Motor de cuotas 2026 · uso interno')
    ancho = landscape(letter)[0] - 2.4 * cm
    story = []
    for paq, full in FULL.items():
        pagina_paquete(story, paq, full, ancho)
    pagina_arranque(story, ancho)
    doc.build(story)
    print('OK', OUT, os.path.getsize(OUT), 'bytes')

if __name__ == '__main__':
    main()
