# -*- coding: utf-8 -*-
"""TÉRMINOS Y CONDICIONES DEL PROGRAMA INDIVIDUAL (100 horas, uno a uno) — anexo al contrato de matrícula.
Decisiones de gerencia 27/10/2026: 100 horas con 12 meses de vigencia desde la primera sesión (las que no se usan se pierden);
prueba de nivel solo al inicio; sin reporte mensual; sin garantía de aprendizaje (24/10); audios entre sesiones voluntarios;
ritmo recomendado 1,5 h dos veces por semana. Las reglas de agenda, cancelación y puntualidad son propuesta para aprobación.
Por rol, sin nombres. Salida: recursos/comercial/productos/TERMINOS_PROGRAMA_INDIVIDUAL_HEIIU.docx (+ PDF por Word) y copia del PDF
en la carpeta del gerente de alianzas. Uso: python generadores/comercial/gen_terminos_programa_individual.py"""
import os, sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'recursos', 'comercial', 'productos', 'TERMINOS_PROGRAMA_INDIVIDUAL_HEIIU.docx')
NARANJA = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.4); s.bottom_margin = Cm(1.2); s.left_margin = Cm(1.8); s.right_margin = Cm(1.8)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(9.5)


def sec(txt):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2); p.paragraph_format.keep_with_next = True
    r = p.add_run(txt); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NARANJA


def t(txt, bold=False, size=9.5, color=None, after=3, align=None):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align: p.alignment = align
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color
    return p


def item(letra, titulo, txt):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2); p.paragraph_format.left_indent = Cm(0.4)
    r = p.add_run(letra + ') '); r.bold = True; r.font.size = Pt(9.5)
    r = p.add_run(titulo + ' '); r.bold = True; r.font.size = Pt(9.5)
    r = p.add_run(txt); r.font.size = Pt(9.5)


p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('ANEXO AL CONTRATO DE MATRÍCULA — TÉRMINOS Y CONDICIONES DEL PROGRAMA INDIVIDUAL'); r.bold = True; r.font.size = Pt(12.5); r.font.color.rgb = NARANJA
t('Versión 1.0 · octubre de 2026 · 100 horas · uno a uno · conversaciones avanzadas en su área', size=9, color=GRIS, after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
t('Anexo al Contrato para Programa de Cursos Heiiu-Global Teacher SAS suscrito el ____ / ____ / ______ · Estudiante: ______________________________ · Documento: ______________', bold=True, after=4)
t('Entre Heiiu Global Teacher SAS y el ESTUDIANTE se acuerda que el PROGRAMA INDIVIDUAL contratado se rige por las siguientes condiciones, que el estudiante declara conocer antes de pagar:', after=2)

sec('1. QUÉ INCLUYE EL PROGRAMA')
item('a', 'Cien (100) horas de sesión uno a uno', 'con un profesor asignado por la academia, sobre un plan a la medida del estudiante: su trabajo, su especialidad, sus reuniones, sus pacientes o clientes, su entrevista.')
item('b', 'Prueba de nivel al inicio', 'y entrevista de objetivos, de las cuales sale el plan. No hay examen final: el avance lo comprueba el estudiante en sus propias conversaciones.')
item('c', 'Revisión de audios entre sesiones.', 'El estudiante puede enviar audios cortos entre una sesión y otra; el profesor los devuelve con una mejora en la sesión siguiente o antes. Son voluntarios: no enviar audios no afecta las horas ni el programa.')
item('d', 'Constancia de horas cursadas', 'al cierre del programa, expedida por la academia.')
item('e', 'No incluye:', 'libro ni material de estudio (el contenido sale del trabajo real del estudiante), examen ni certificación de nivel, ni la Garantía Heiiu de Aprendizaje, que aplica únicamente a los programas grupales por nivel.')

sec('2. VIGENCIA DE LAS HORAS')
item('a', 'Doce (12) meses', 'contados desde la primera sesión. La primera sesión debe realizarse dentro de los treinta (30) días calendario siguientes al pago; si no se realiza, la vigencia empieza a contar el día 31.')
item('b', 'Las horas no usadas al vencer la vigencia se pierden.', 'No se reembolsan, no se transfieren a otra persona ni a otro programa, y no se extienden, salvo la pausa del literal c).')
item('c', 'Una (1) pausa', 'de hasta treinta (30) días calendario, solicitada por escrito antes de que empiece, extiende la vigencia por los mismos días. Solo se concede una vez durante el programa.')

sec('3. SESIONES Y RITMO')
item('a', 'Duración de cada sesión:', 'una (1), una y media (1,5) o dos (2) horas. Ritmo recomendado: una hora y media dos veces por semana, con el que las 100 horas se terminan en unos ocho meses. Para cubrir las 100 horas dentro de la vigencia se requiere un promedio de dos (2) horas semanales.')
item('b', 'Horario fijo semanal.', 'Al inicio, el estudiante y la coordinación acuerdan los días y horas de la semana, dentro de la disponibilidad del profesor. Ese horario queda reservado para el estudiante. Cambiarlo requiere una (1) semana de aviso y está sujeto a disponibilidad.')
item('c', 'Sesiones adicionales', 'al horario fijo se agendan con la coordinación con al menos cuarenta y ocho (48) horas de anticipación, según disponibilidad del profesor.')
item('d', 'Toda sesión se agenda y se confirma por escrito', 'por el canal de la academia. Lo acordado de palabra con el profesor no modifica la agenda.')

sec('4. CANCELACIONES, REPROGRAMACIONES Y PUNTUALIDAD')
item('a', 'Cancelación por el estudiante con al menos veinticuatro (24) horas de anticipación,', 'por escrito: la sesión se reprograma dentro de la vigencia y no se descuentan horas.')
item('b', 'Cancelación con menos de 24 horas, o inasistencia sin aviso:', 'se descuenta la sesión completa de las 100 horas. El estudiante que no llega ni avisa durante los primeros veinte (20) minutos se entiende inasistente.')
item('c', 'Llegada tarde del estudiante:', 'la sesión termina a la hora acordada; el tiempo perdido se descuenta y no se repone.')
item('d', 'Cancelación o retraso por parte de la academia o del profesor:', 'la academia avisa con la misma anticipación, repone la sesión completa dentro de los quince (15) días siguientes y no descuenta horas. El tiempo de retraso del profesor se repone al final de la sesión o en la siguiente.')
item('e', 'Revisión del horario.', 'Si en un mes el estudiante cancela más de la mitad de las sesiones programadas, la coordinación revisa con él el horario fijo, para que las horas no se pierdan al vencer la vigencia.')

sec('5. LUGAR, PROFESOR Y CONTENIDO')
item('a', 'Lugar:', 'las sesiones son presenciales en la sede de la academia. Sesiones a distancia solo por acuerdo previo y escrito con la coordinación, con las mismas reglas de horas, agenda y puntualidad.')
item('b', 'Profesor:', 'lo asigna la academia según disponibilidad; el inicio del programa se confirma cuando hay profesor asignado (cupos limitados). La academia puede cambiar el profesor garantizando la continuidad del plan. El estudiante puede solicitar un cambio de profesor una (1) vez, por escrito, y se atiende según disponibilidad.')
item('c', 'Contenido y confidencialidad:', 'el estudiante aporta material real de su trabajo (casos, correos, presentaciones, entrevistas) sin datos que identifiquen a pacientes, clientes o terceros. La academia y el profesor tratan ese material como confidencial y no lo usan fuera de las sesiones.')

sec('6. PAGO, RETRACTO Y LO QUE NO SE PROMETE')
item('a', 'Pago y activación:', 'el precio y la forma de pago son los del contrato de matrícula. Las horas se activan con el pago. Rige el derecho de retracto del contrato (cinco días hábiles, Ley 1480 de 2011) mientras no se haya realizado la primera sesión; después, no hay devolución por horas no usadas.')
item('b', 'Lo que no se promete:', 'el programa entrena la conversación profesional del estudiante. No garantiza la admisión a una especialización, un ascenso, una visa, ni un puntaje en examen internacional, ni un nivel determinado al terminar.')
item('c', 'Datos personales:', 'se tratan conforme a la cláusula de tratamiento de datos del contrato de matrícula.')

sec('7. PREVALENCIA')
t('En lo específico del programa individual (horas, vigencia, agenda, cancelaciones y alcance), este anexo prevalece sobre las cláusulas del contrato de matrícula escritas para los programas grupales por nivel. En todo lo demás, el contrato permanece sin modificaciones.', after=8)

t('Firma del ESTUDIANTE: ______________________________  C.C. ______________', bold=True, after=4)
t('Firma HEIIU GLOBAL TEACHER SAS: ______________________________  C.C. ______________', bold=True, after=4)
t('Fecha: ____ / ____ / ______', bold=True, after=0)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
try:
    doc.save(OUT); print('OK', OUT)
except OSError:
    OUT2 = OUT.replace('.docx', '_v2.docx'); doc.save(OUT2); print('ABIERTO ->', OUT2)
