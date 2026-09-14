# -*- coding: utf-8 -*-
"""Propuesta para cerradora high ticket — 1 pagina para compartir pantalla."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NARANJA = RGBColor(0xE5, 0x4C, 0x09)
GRIS = RGBColor(0x77, 0x77, 0x77)
CREMA = 'FFF8E7'
NARANJA_HEX = 'E54C09'

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.3); s.bottom_margin = Cm(1.1); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(10.5)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    el = OxmlElement('w:shd'); el.set(qn('w:val'), 'clear'); el.set(qn('w:fill'), color)
    tcPr.append(el)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('HEIIU ENGLISH ACADEMY — PROPUESTA COMERCIAL · CERRADORA HIGH TICKET'); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = NARANJA
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Septiembre 2026 · Confidencial'); r.font.size = Pt(9.5); r.font.color.rgb = GRIS

def sec(txt):
    p = doc.add_paragraph(); r = p.add_run(txt); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = NARANJA
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)

def t(txt, bold=False):
    p = doc.add_paragraph(); r = p.add_run(txt); r.font.size = Pt(10.5); r.bold = bold
    p.paragraph_format.space_after = Pt(2)

def frase(txt):
    tab = doc.add_table(rows=1, cols=1); tab.style = 'Table Grid'
    c = tab.rows[0].cells[0]; shd(c, CREMA)
    p = c.paragraphs[0]; r = p.add_run(txt); r.font.size = Pt(10.5); r.bold = True
    esp = doc.add_paragraph(); esp_r = esp.add_run(''); esp_r.font.size = Pt(3)
    esp.paragraph_format.space_after = Pt(0)

sec('EL PRODUCTO')
t('ARRANQUE A1+A2: los dos primeros niveles de inglés COMPLETOS — 200 horas presenciales, libros y certificado oficial por nivel — $2.990.000, precio de lanzamiento. Cohorte inicia el 5 DE OCTUBRE.', bold=True)
t('Y el high ticket detrás: el PROGRAMA COMPLETO (A1 a B2, 575 horas) con beca del Fondo según el perfil del cliente — caso típico (perfil General, de contado): $5.913.280. Perfiles de menores ingresos pueden acceder a becas mayores, con soportes y cupos. El cierre doble ofrece los dos caminos: las dos respuestas son sí.')

sec('POR QUÉ CIERRA (los diferenciales)')
t('· GARANTÍA DE APRENDIZAJE POR ESCRITO en el contrato — única en la ciudad. Mata la objeción #1 ("¿y si no aprendo?").')
t('· MÓDULO DE GRADUACIÓN al terminar A2, a elección: el estudiante sale con su PÁGINA WEB publicada y su primer mensaje de venta en inglés — o con su aplicación lista para irse a trabajar afuera (video + entrevista ensayada).')
t('· Institución con licencia desde 2012, programas registrados, certificación ICONTEC.')
t('· Precio de lanzamiento + contador de cupos REAL: la urgencia no es teatro.')
frase('No vendemos inglés. Vendemos a dónde te lleva — con garantía firmada.')

sec('LA META')
t('20 CUPOS ANTES DEL 5 DE OCTUBRE: 10 en la jornada de la MAÑANA (8:00-12:00, super intensivo) + 10 en la NOCHE (6:30-8:30).', bold=True)

sec('EL TRATO')
t('· Comisión: 8% del recaudo por TODA venta de tu canal (tu contenido, tu red, y la pauta financiada). Pago contra plata efectiva en caja.', bold=True)
t('· ACELERADOR: si completas los 20 cupos antes del 5 de octubre, toda la serie se reliquida al 10% — retroactivo.', bold=True)
t('· PAUTA FINANCIADA POR HEIIU sobre tus piezas, en tus canales: apruebas pieza + presupuesto con gerencia antes de publicar; tope inicial $1.000.000/mes, revisable por resultados; factura de la plataforma como soporte del gasto.')
t('· Sin exclusividad, sin horarios, sin básico. Leads que la casa te entregue: 5%.')

sec('LA REGLA DEL CUPO 21 (automática, sin permisos)')
t('El contador de cupos es compartido y gerencia lo actualiza a diario. Con el contador en 20, cambia el guion — no se pide permiso: toda venta siguiente se cierra como COHORTE SIGUIENTE con el precio de lanzamiento CONGELADO — el cliente paga los $2.990.000 de hoy aunque esa cohorte salga después a precio normal — y comisiona igual. Lo único prohibido: prometer cupo del 5 de octubre cuando ya van 20.')

sec('REGLAS DE LA CASA (innegociables)')
t('Sin descuentos inventados (la única flexibilidad es la escrita) · sin promesas de empleo, visa o "bilingüe en X meses" · la palabra "patrocinio" no existe: es beca del Fondo · toda venta se registra en la planilla comercial para comisionar.')

sec('EL PROCESO')
t('1. Contrato de prestación de servicios con confidencialidad — esta semana. 2. Firmado = manual de venta completo + planilla + piezas, el mismo día. 3. Primera venta: esta misma semana.', bold=True)

doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Heiiu English Academy · Carrera 27 # 48-49, Bucaramanga · Gerencia'); r.font.size = Pt(9); r.font.color.rgb = GRIS

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\PROPUESTA_CERRADORA_HIGH_TICKET.docx'
doc.save(out); print('OK', out)
