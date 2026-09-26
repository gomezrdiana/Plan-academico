# -*- coding: utf-8 -*-
"""Adenda de una hoja al contrato de matricula de 24 clausulas (el que se firma mientras se agotan los impresos):
incorpora los anexos vigentes y crea las obligaciones del portafolio; no toca ninguna clausula del contrato."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

GRIS = RGBColor(0x77, 0x77, 0x77)
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.5); s.bottom_margin = Cm(1.3); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(10)

def t(txt, bold=False, after=4, size=10):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold

def num(n, titulo, txt):
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(f'{n}. {titulo} '); r.bold = True; r.font.size = Pt(10)
    r2 = p.add_run(txt); r2.font.size = Pt(10)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('ADENDA AL CONTRATO PARA PROGRAMA DE CURSOS HEIIU — GLOBAL TEACHER S.A.S.'); r.bold = True; r.font.size = Pt(12.5)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Anexos vigentes y compromisos del programa · Hace parte integral del contrato de matrícula No. __________ suscrito el ____ / ____ / ______'); r.font.size = Pt(9); r.font.color.rgb = GRIS
doc.add_paragraph()

t('Entre GLOBAL TEACHER S.A.S. (Heiiu English Academy), NIT 900.422.478-2, y el SUSCRIPTOR / ESTUDIANTE ______________________________________, identificado(a) con C.C. ________________, se acuerda adicionar al contrato de matrícula lo siguiente:')

num(1, 'ANEXOS QUE HACEN PARTE DEL CONTRATO.',
    'Hacen parte integral del contrato, con el mismo valor que sus cláusulas, los siguientes documentos que el SUSCRIPTOR declara recibir y aceptar en este acto: (a) el ANEXO DE GARANTÍA HEIIU DE APRENDIZAJE; (b) el RECIBO DE SEPARACIÓN DE CUPO, cuando lo haya; (c) el ANEXO DE PLAN DE PAGOS, cuando el pago sea a cuotas; (d) el pagaré y su carta de instrucciones, cuando el pago sea a cuotas; (e) la autorización de consulta y reporte a centrales de riesgo, en el formato de la central; y (f) la autorización de uso de imagen. En el supuesto específico de devolución por garantía, el ANEXO DE GARANTÍA prevalece sobre las cláusulas del contrato que limiten devoluciones; en todo lo demás, el contrato permanece sin modificación.')

num(2, 'COMPROMISOS DEL ESTUDIANTE QUE ESTA ADENDA CREA EXPRESAMENTE.',
    'Para efectos del programa y de la garantía, el ESTUDIANTE se obliga a: (a) presentar la evaluación de entrada del nivel, que incluye una grabación oral en su primera clase; (b) grabar y ENVIAR a la academia, todos los días de clase, un video corto de práctica en inglés, hablado de corrido y sin leer, con la duración mínima del nivel (A1: 1 minuto · A2: 2 · B1: 3 · B2: 5), que constituye su portafolio académico; (c) asistir al menos al 80% de las clases del nivel, entregar al menos el 90% de las tareas y presentar todas las evaluaciones. Cada tres (3) llegadas tarde de más de quince (15) minutos se contabilizan como una (1) inasistencia. La academia conserva las grabaciones y videos únicamente como evidencia académica del avance del ESTUDIANTE, conforme a la Ley 1581 de 2012.')

num(3, 'ABONO DE SEPARACIÓN, RETRACTO Y SALDO A FAVOR.',
    'Dentro de los cinco (5) días hábiles siguientes al pago, el SUSCRIPTOR puede retractarse y se le devuelve la totalidad de lo pagado (Ley 1480 de 2011). Vencido ese término, el abono de separación no se devuelve en dinero: queda como SALDO A FAVOR aplicable a cualquier programa de la academia durante doce (12) meses. El abono congela el cupo y el precio por siete (7) días calendario. El cheque de cesantías y el crédito de terceros cuentan como pago de contado si el desembolso se recibe dentro de los diez (10) días hábiles siguientes y antes del inicio de clases.')

num(4, 'SI EL GRUPO NO ABRE.',
    'Si la jornada elegida no alcanza el número mínimo de estudiantes, el ESTUDIANTE elige entre: pasarse a otra jornada disponible, conservar su precio congelado para la siguiente cohorte, o la devolución total de su abono. La academia no lo cambia de jornada sin su aceptación.')

num(5, 'LO DEMÁS NO CAMBIA.',
    'Todas las demás cláusulas del contrato de matrícula continúan vigentes. En caso de contradicción entre esta adenda y el contrato en las materias aquí reguladas, prevalece esta adenda.')

doc.add_paragraph()
t('Firmada en Bucaramanga el ____ / ____ / ______', after=10)
t('SUSCRIPTOR / ESTUDIANTE                                                   GLOBAL TEACHER S.A.S.', after=14)
t('_____________________________                                _____________________________', after=2)
t('Nombre: ________________________                              DIANA MARCELA GÓMEZ RANGEL', after=2)
t('C.C. ______________________________                              Representante Legal', after=2)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\documentos_operativos\plantillas\ADENDA_CONTRATO_24_ANEXOS.docx'
doc.save(out); print('OK', out)
