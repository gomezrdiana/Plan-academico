# -*- coding: utf-8 -*-
"""Versión CORTA de la entrevista de números de Carlos a John: 5 preguntas, 1 página, 20 minutos.
Reemplaza en uso a ENTREVISTA_CARLOS_JOHN_NUMEROS (2 págs, que Carlos no aplicó).
Salida (fuera de git): Candidatos/ENTREVISTA_CARLOS_JOHN_5PREGUNTAS.docx (+ PDF vía Word COM)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\LINKEDIN DIANA GOMEZ\Candidatos'

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.1); s.bottom_margin = Cm(0.9); s.left_margin = Cm(1.7); s.right_margin = Cm(1.7)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)

def shd(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear'); el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), color); tcPr.append(el)
def t(txt, bold=False, size=10, color=None, after=3, indent=0):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after); p.paragraph_format.left_indent = Cm(indent)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
    return p

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('JOHN HINESTROZA — 5 PREGUNTAS DE NÚMEROS'); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = NAR
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(6)
r = p.add_run('La hace Carlos · virtual · 20 minutos · se hacen las 5, en este orden, y se anota el número que diga en cada una'); r.font.size = Pt(9); r.font.color.rgb = GRIS

t('Lo que él ya declaró, para contrastar: en Welli pasó de 7 a 180 aliados; cumplimiento 85-110%; "20 gerentes en 2 semanas"; aspira a $3M fijo / $7M total. En su tarea propuso 40 decisores en 2 semanas, meta $30M y 5 indicadores. Nuestro cupo vale $4.782.800. La comisión se paga sobre lo que entra a caja, no sobre lo firmado.', size=9.5, color=GRIS, after=6)

def pregunta(n, titulo, pregunta_txt, anota, alerta):
    tb = doc.add_table(rows=1, cols=1); tb.style = 'Table Grid'; c = tb.cell(0, 0); shd(c, 'FFF8E7')
    par = c.paragraphs[0]; par.paragraph_format.space_after = Pt(1)
    r = par.add_run(f'{n}. {titulo}'); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAR
    par = c.add_paragraph(); par.paragraph_format.space_after = Pt(2)
    r = par.add_run(pregunta_txt); r.font.size = Pt(10.5); r.italic = True
    par = c.add_paragraph(); par.paragraph_format.space_after = Pt(1)
    r = par.add_run('Anota: '); r.bold = True; r.font.size = Pt(9.5)
    r = par.add_run(anota); r.font.size = Pt(9.5)
    par = c.add_paragraph(); par.paragraph_format.space_after = Pt(0)
    r = par.add_run('Mala señal: '); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = GRIS
    r = par.add_run(alerta); r.font.size = Pt(9.5); r.font.color.rgb = GRIS
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

pregunta(1, 'Su embudo en Welli, de memoria',
 '"En un mes normal en Welli: ¿a cuántos gerentes contactabas, cuántos te recibían, cuántos firmaban y cuánto facturaban esos convenios? Cuatro números."',
 'contactos ____  reuniones ____  firmas ____  facturación $________ al mes.',
 'no da los cuatro números o los da en porcentajes vagos ("casi todos", "la mayoría"). Quien vendió de verdad se sabe su embudo.')

pregunta(2, 'Cómo lo reportaba',
 '"¿Cómo le reportabas eso a tu jefe: en qué formato, cada cuánto y con qué columnas?"',
 'formato ________  frecuencia ________  columnas: ________________________.',
 'no describe un tablero con columnas concretas. Aquí el cargo presenta cifras cada día, 15 minutos; si nunca lo hizo, no lo va a hacer.')

pregunta(3, 'El embudo de Heiiu, en vivo',
 '"Con cupos de $4.782.800 y tu propia meta de $30 millones al mes: ¿cuántos cupos son, en cuántas empresas, cuántas reuniones necesitas y a cuántos decisores tienes que contactar? Y dime qué cuenta para ti como decisor."',
 'cupos ____  empresas ____  reuniones ____  contactos ____  decisor = ________________.',
 'no llega a algo cercano a 6-7 cupos, 2-3 empresas, 12 reuniones, 40 contactos (es la matemática de su propia tarea), o "decisor" es cualquiera que le conteste. Si los números le salen de la tarea pero no se los sabe, la tarea se la hicieron.')

pregunta(4, 'La primera semana, con nombres',
 '"Lunes 27 de octubre, día uno: ¿a quién llamas? Dame cinco nombres con empresa y cargo."',
 'nombres y cargos: 1 ________ 2 ________ 3 ________ 4 ________ 5 ________. Compara con su tarea (Marval, Freskaleche, Foscal, Extrucol, Kikes) y con las clínicas que nombró (Evoca, Pinar, Clinident).',
 'repite las empresas de la tarea sin nombre de persona, o los contactos son de Welli (odontología) sin puente a empresas de 40+ empleados. En Welli lo recibían por la marca; aquí nadie conoce la academia.')

pregunta(5, 'La plata',
 '"Básico de $2 millones, piso de $3,5 millones los meses 1 a 3 si cumples indicadores, y comisión sobre lo que entra a caja, mes vencido. ¿En qué mes calculas que tu comisión pasa el piso, y si en el mes 4 no lo ha hecho, qué haces?"',
 'mes en que pasa el piso ____  respuesta al mes 4: ________________________.',
 '"no hay problema" sin cálculo, o vuelve a pedir el fijo de $3M. Lo que sirve es un número y una razón ("mes 3, porque con 2 empresas de 5 cupos ya son $4,8M").')

t('Reglas', bold=True, size=11, color=NAR, after=1)
t('No se negocia nada en la llamada: si pide más fijo, "eso lo define Diana con los resultados de este proceso". No se menciona ningún otro candidato. No se le dice qué respuesta esperábamos.', size=9.5, after=2)
t('Al terminar, 3 líneas a Diana por WhatsApp:', bold=True, size=10, after=1)
t('1) Sus números de Welli y de Heiiu cuadran entre sí: sí / no.   2) Sabe reportar con tablero: sí / no.   3) Lo contrato: sí / no, y por qué en una frase.', size=9.5, after=0, indent=0.4)

out = BASE + r'\ENTREVISTA_CARLOS_JOHN_5PREGUNTAS.docx'
try: doc.save(out); print('OK', out)
except PermissionError: doc.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
