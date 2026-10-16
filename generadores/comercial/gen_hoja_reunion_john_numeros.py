# -*- coding: utf-8 -*-
"""Hoja de la SEGUNDA reunión de gerencia con John: él viene "a resolver dudas" después de hablar con el socio financiero,
pero el socio no hizo las preguntas de números. Esta reunión las hace gerencia (15 min), fija los términos una sola vez
y NO cierra: la oferta formal va por escrito después de la referencia. 1-2 págs.
Salida (fuera de git): Candidatos/HOJA_REUNION_JOHN_NUMEROS.docx (+ PDF vía Word COM)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos'
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0); s.left_margin = Cm(1.7); s.right_margin = Cm(1.7)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)
def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(7); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAR
def t(txt, size=10, color=None, after=3, bold=False, indent=0):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after); p.paragraph_format.left_indent = Cm(indent)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
def caja(txt, size=10.5):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    c.paragraphs[0].paragraph_format.space_after = Pt(0)
    r = c.paragraphs[0].add_run(txt); r.font.size = Pt(size); r.italic = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
def anota(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2); p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run('Anota: '); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = GRIS
    r = p.add_run(txt); r.font.size = Pt(9.5); r.font.color.rgb = GRIS

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('JOHN — REUNIÓN DE NÚMEROS (él cree que viene a resolver dudas)'); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('Presencial · 40 min · Uso interno de gerencia · Llevas: esta hoja, su ficha del 14/10, su tarea y un esfero'); r.font.size = Pt(9); r.font.color.rgb = GRIS

t('Carlos habló con él y le gustó, pero no le hizo las preguntas de números. Entonces las haces tú hoy, 15 minutos, antes de hablar de términos. Regla de la reunión: sales con CUATRO números de él escritos en esta hoja, los términos dichos una sola vez, y SIN oferta firmada. La oferta va por escrito después de la llamada a Elkin.', after=4)
caja('Si todavía no has llamado a Elkin (Welli), no se promete fecha de inicio hoy. Se dice: "la oferta formal te llega por escrito esta semana".', size=10)

sec('1. Sus dudas primero (5 min)')
caja('"Cuéntame qué dudas trajiste. Las anoto todas y te las respondo en orden."')
t('Anotas y respondes corto. Cualquier duda de plata se responde en el bloque 3, no aquí: "eso te lo dejo clarísimo en un momento, con números".', size=10, color=GRIS)

sec('2. Los números de él (15 min) — las tres que Carlos no hizo')
t('A. Welli, de memoria:', bold=True, after=1)
caja('"En un mes normal en Welli: ¿a cuántos gerentes contactabas, cuántos te recibían, cuántos firmaban y cuánto facturaban esos convenios? Cuatro números."')
anota('contactos ______  reuniones ______  firmas ______  facturación $__________ al mes.   Mala señal: porcentajes vagos ("casi todos") o no da los cuatro.')
t('B. Heiiu, en vivo:', bold=True, after=1)
caja('"Con cupos de $4.782.800 y la meta de $30 millones al mes que tú mismo pusiste en tu plan: ¿cuántos cupos son, en cuántas empresas, cuántas reuniones necesitas y a cuántos decisores tienes que contactar? ¿Y qué cuenta para ti como decisor?"')
anota('cupos ______  empresas ______  reuniones ______  contactos ______  decisor = ______________.   Referencia: 6-7 cupos · 2-3 empresas · 12 reuniones · 40 contactos. Si los números están en su tarea pero hoy no se los sabe, la tarea se la hicieron.')
t('C. La primera semana, con nombres:', bold=True, after=1)
caja('"Día uno: ¿a quién llamas? Dame cinco nombres con empresa y cargo."')
anota('1 __________ 2 __________ 3 __________ 4 __________ 5 __________.   Compara con su tarea (Marval, Freskaleche, Foscal, Extrucol, Kikes) y las clínicas que nombró (Evoca, Pinar, Clinident). Mala señal: empresas sin persona, o solo odontólogos sin puente a empresas de 40+ empleados.')

sec('3. Los términos, dichos una vez y sin negociar (10 min)')
t('Aquí corriges dos cosas que se dijeron el 14/10 y que la oferta escrita NO va a tener: no es "sin ir a la oficina" y no tiene equipo a cargo. Se dice hoy, de frente, para que no sea sorpresa en el contrato.', size=10, color=GRIS)
for x in [
 'Contrato laboral desde el día uno. Básico $2.000.000 más prestaciones.',
 'Ingreso mínimo de $3.500.000 los meses 1 a 3, en cada mes en que cumpla los indicadores: mes 1 = 40 empresas contactadas con quien decide, 12 reuniones, 2 firmas; mes 2 = 4 firmas acumuladas y 2 activaciones; mes 3 = 6 firmas acumuladas y 3 activaciones.',
 'Comisión del 10% sobre lo que entra a caja, no sobre lo firmado; se liquida mes vencido. Acelerador del 15% y 20% sobre la meta trimestral, sin tope. Más 6% de los pagos de cada estudiante de sus alianzas durante 12 meses.',
 'Meta $30 millones al mes en el primer trimestre, medida en ventas firmadas con inicial pagada.',
 'Martes y jueves en la sede, con planilla. Los otros días en campo. Seguimiento diario de 15 minutos a hora fija y planeación los lunes de 30 minutos, las dos las presenta él.',
 'Sin equipo a cargo. El equipo de asesoría apoya activaciones y matricula a los interesados que él genere, pero no le reporta.']:
    p = doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(1); r = p.add_run(x); r.font.size = Pt(10)
t('D. La plata, su cálculo:', bold=True, after=1)
caja('"Con eso: ¿en qué mes calculas que tu comisión pasa el piso de $3,5 millones? Y si en el mes 4 no lo ha hecho, ¿qué haces?"')
anota('mes ______  respuesta al mes 4: ______________________.   Lo que sirve: un número y una razón ("mes 3, con dos empresas de 5 cupos ya son $4,8M"). Mala señal: "no hay problema" sin cálculo, o volver a pedir $3M fijos.')
caja('Si pide más fijo: "El esquema es este para todo el mundo. Lo que sube aquí es la comisión, y sube sin tope." No se abre la carta guardada hoy. Solo después de Elkin, por escrito, y solo si aceptó todo lo demás y esa es su única objeción.', size=10)

sec('4. Cierre (5 min)')
caja('"Gracias. La oferta formal te llega por escrito esta semana, después de hablar con tu referencia de Welli. Ahí va la fecha de inicio. Tú la lees con calma y me dices."')
t('No se dice "estás contratado", "cuenta con eso" ni "bienvenido". Un candidato bueno espera una semana; uno que presiona para firmar hoy te está diciendo algo.', size=10, color=GRIS)

sec('Después de la reunión: 5 líneas a Carlos')
t('1) Welli: sus cuatro números y si cuadran con "7 a 180 aliados".  2) Heiiu: su embudo en vivo coincide con su tarea: sí / no.  3) Primera semana: cuántos nombres reales con cargo.  4) Plata: mes en que dice que pasa el piso y qué hace si no.  5) Tu veto: sí / no, y por qué en una frase.', size=10)
t('La oferta se redacta cuando estén las 5 líneas y la llamada a Elkin. No antes.', size=10, bold=True, after=0)

out = BASE + r'\HOJA_REUNION_JOHN_NUMEROS.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
