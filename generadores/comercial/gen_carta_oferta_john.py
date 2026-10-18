# -*- coding: utf-8 -*-
"""Carta de oferta laboral para el candidato 1 de alianzas (John). Se envía SOLO después de la referencia de Welli
y de las 5 líneas del socio. 1 página. Términos = propuesta que él recibió + lo dicho en reunión (2 días en sede,
sin personal a cargo, territorio salud, contrato indefinido con prueba de 2 meses, revisión a los 45 días).
Salida (fuera de git): Candidatos/John Hinestroza/CARTA_OFERTA_JOHN_2026-10.docx (+PDF)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza'
d = Document()
for s in d.sections:
    s.top_margin = Cm(1.3); s.bottom_margin = Cm(1.0); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(9.5)
def t(txt, size=9.5, bold=False, color=None, after=3, align=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align: p.alignment = align
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def sec(txt):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NAR
def bullets(items, size=9.5):
    for x in items:
        p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(0); r = p.add_run(x); r.font.size = Pt(size)

t('Heiiu English Academy · Global Teacher S.A.S.', size=9, color=GRIS, after=0)
t('Bucaramanga, ____ de octubre de 2026', size=9.5, after=6)
t('OFERTA LABORAL — EJECUTIVO SENIOR DE ALIANZAS EMPRESARIALES', bold=True, size=12.5, color=NAR, after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
t('Señor John Hinestroza', after=4)
t('Después de nuestras conversaciones y de la verificación de su referencia, le presentamos por escrito la oferta para incorporarse a la academia. Estos son los términos; el contrato y su anexo de compensación recogen exactamente lo mismo.', after=4)

sec('1. Cargo, contrato y fecha de inicio')
bullets([
 'Cargo: Ejecutivo Senior de Alianzas Empresariales. Reporta a gerencia.',
 'Contrato de trabajo a término indefinido, con periodo de prueba de dos (2) meses.',
 'Inicio: lunes 27 de octubre de 2026. Inducción el lunes 27 (jornada completa) y el martes 28 en la mañana; trabajo de campo desde el martes 28 en la tarde.'])

sec('2. Compensación (detalle en el anexo de compensación)')
bullets([
 'Básico: salario mínimo legal más auxilio de transporte ($2.000.000 en 2026), más prestaciones sociales y seguridad social de ley.',
 'Comisión del 10% sobre el recaudo del primer año de los contratos de plan empresa y programas personalizados que usted cierre; se liquida mes vencido sobre lo efectivamente recaudado, sin tope. Acelerador: 15% entre el 100% y el 130% de la meta trimestral y 20% por encima, cuando firme al menos dos empresas nuevas en el trimestre.',
 'Cartera de alianzas: 6% de los pagos de cada estudiante que se matricule con carta de una empresa aliada registrada a su nombre, durante los 12 meses siguientes a su matrícula, y 3% del mes 13 al 24.',
 'Ingreso mínimo garantizado de $3.500.000 en cada uno de los meses 1 a 3 en que cumpla los indicadores de gestión y de firmas (mes 1: 40 empresas contactadas con quien decide, 12 reuniones y 2 firmas; mes 2: 4 firmas acumuladas y 2 activaciones; mes 3: 6 firmas acumuladas y 3 activaciones). La meta de ventas de $30.000.000 mensuales del primer trimestre no es condición de esta garantía. Si en un mes no se cumplen los indicadores, se paga el básico más las comisiones causadas y se acuerda un plan de ajuste de una semana.',
 'Metas trimestrales crecientes y escalones de básico según la tabla del anexo, conocida desde la firma.'])

sec('3. Forma de trabajo')
bullets([
 'Dos días fijos por semana en la sede (martes y jueves), con registro de asistencia, para tablero, activaciones con el equipo de asesoría y cierres con empresas. Los demás días en campo, con autonomía para organizar su agenda y sus visitas.',
 'Seguimiento diario de 15 minutos con gerencia a las 8:45 a. m., que usted presenta: resultados del día anterior frente al plan y empresas del día. Planeación semanal los lunes, 30 minutos, que usted lidera. Tablero de alianzas al día, el mismo día.',
 'Sin personal a cargo. El equipo de asesoría comercial apoya las activaciones y matricula a los interesados que usted genere, pero no le reporta.',
 'Territorio inicial asignado por gerencia: salud (clínicas, odontología, IPS), fundaciones, cajas de compensación y organizaciones grandes. Una empresa queda a su nombre cuando la registra primero en el tablero. Gerencia puede ajustar el territorio por escrito.',
 'Cierra con las tarifas y los documentos estándar de la academia; no está facultado para otorgar descuentos. Convenios y órdenes los firma el representante legal.'])

sec('4. Revisión de resultados')
t('El jueves 11 de diciembre de 2026, dentro del periodo de prueba, se revisan los resultados del cargo: inscritos con pago recibido, firmas activadas y cumplimiento de los indicadores de gestión. La continuidad del cargo depende de esa revisión.', after=2)

sec('5. Aceptación y firma')
bullets([
 'Acepte esta oferta respondiendo por escrito antes del jueves 22 de octubre de 2026 a las 6:00 p. m.',
 'Firma del contrato y del anexo de compensación: viernes 23 de octubre de 2026 en la sede. Traer: cédula, RUT, certificación bancaria, certificados de afiliación a EPS y fondo de pensiones, hoja de vida y certificados laborales.',
 'Esta oferta reemplaza cualquier conversación anterior sobre los términos del cargo y pierde vigencia si no se acepta en el plazo indicado.'])
t('', after=10)
t('_________________________________', after=0)
t('Diana Marcela Gómez Rangel', bold=True, after=0)
t('Gerente · Heiiu English Academy · Global Teacher S.A.S.', size=9, color=GRIS, after=8)
t('Acepto los términos de esta oferta:  _________________________________   Fecha: ____ / ____ / 2026', size=9.5)

out = BASE + r'\CARTA_OFERTA_JOHN_2026-10.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
