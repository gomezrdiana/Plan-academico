# -*- coding: utf-8 -*-
"""Otrosi al contrato docente v3.1: piloto de alianzas empresariales (abre y presenta; gerencia cierra). Por rol, firmable.
Salida: contratos/ANEXO_PILOTO_ALIANZAS_EMPRESARIALES_DOCENTE_v1.docx"""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

GRIS = RGBColor(0x77, 0x77, 0x77)
d = Document()
for s in d.sections:
    s.top_margin = Cm(1.5); s.bottom_margin = Cm(1.3); s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10)

def t(txt, bold=False, after=4, size=10, align=None, color=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align: p.alignment = align
    r = p.add_run(txt); r.bold = bold; r.font.size = Pt(size)
    if color: r.font.color.rgb = color

def cl(n, tit, txt):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(5)
    r = p.add_run(f'{n}. {tit}. '); r.bold = True; r.font.size = Pt(10)
    r2 = p.add_run(txt); r2.font.size = Pt(10)

t('ANEXO AL CONTRATO DOCENTE — PILOTO DE ALIANZAS EMPRESARIALES', bold=True, size=12.5, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
t('Otrosí al Contrato de Prestación de Servicios Profesionales — Docente Hora Cátedra v3.1 · Hace parte integral del contrato · Versión 1 · octubre de 2026', size=9, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER, after=10)

t('Entre GLOBAL TEACHER S.A.S. (Heiiu English Academy), NIT 900.422.478-2, representada por DIANA MARCELA GÓMEZ RANGEL (EL CONTRATANTE), y ______________________________________, C.C. ____________________ (EL CONTRATISTA), en desarrollo del contrato docente vigente entre las partes y de su cláusula de propiedad intelectual, se acuerda el siguiente piloto:', after=8)

cl(1, 'OBJETO', 'EL CONTRATISTA, por iniciativa propia y de manera voluntaria, desarrollará durante el piloto actividades de apertura de alianzas con empresas y organizaciones bajo el programa Heiiu Business Partner (Oferta A: alianza sin costo, con acceso de los colaboradores de la empresa aliada a los beneficios del Fondo de Becas conforme a su Reglamento, artículo 3.5; Oferta B: plan empresa a tarifa corporativa, artículo 3.6, que negocia y cierra gerencia): identificar empresas, contactar a sus decisores, presentar la propuesta institucional y entregar el material aprobado. Esta actividad es independiente de su labor docente, no es exclusiva y no implica subordinación: EL CONTRATISTA define sus horarios y medios, siempre por fuera de sus horas de clase programadas.')

cl(2, 'ALCANCE Y LÍMITES', 'EL CONTRATISTA abre, presenta y puede obtener la firma de la empresa en los dos formatos ESTÁNDAR aprobados por gerencia, sin modificar ninguna de sus condiciones: el convenio de alianza (Oferta A) y la orden del Plan Empresa de tres a siete cupos a tarifa corporativa (Oferta B); ambos quedan perfeccionados con la firma del representante legal de la academia. EL CONTRATISTA NO negocia, NO cotiza ni promete condiciones distintas de los formatos. Toda empresa que pida ocho cupos o más, clases en sus instalaciones, horarios propios, otros plazos o cualquier condición distinta, se agenda con gerencia, que negocia y cierra. Las empresas que ya estén en conversación con la academia al inicio del piloto (listadas en el numeral 9) quedan excluidas del piloto.')

cl(3, 'REGISTRO', 'Para que una empresa cuente en el piloto, EL CONTRATISTA la registra en el tracker del piloto desde el primer contacto (empresa, decisor, fecha, canal, estado, próximo paso) y envía a gerencia el reporte diario y el reporte semanal acordados. Lo que no esté registrado no cuenta ni genera remuneración. En caso de concurrencia sobre una misma empresa, prevalece el registro más antiguo.')

cl(4, 'REMUNERACIÓN (siempre sobre recaudo efectivo a caja)', 'a) MATRÍCULAS POR ALIANZA: CINCO por ciento (5%) del recaudo de cada matrícula de estudiante nuevo que ingrese a la academia a través de un convenio de becas firmado con una empresa que EL CONTRATISTA registró y abrió, con independencia de quién conduzca la asesoría y el cierre. Aplica a las matrículas recibidas durante los doce (12) meses siguientes a la firma de cada convenio. b) PLAN EMPRESA: CINCO por ciento (5%) del recaudo del primer año cuando EL CONTRATISTA cierra el Plan Empresa estándar (tres a siete cupos) con el formato aprobado; TRES por ciento (3%) del recaudo del primer año cuando la empresa que EL CONTRATISTA registró y abrió contrata un plan a la medida cerrado por gerencia. c) Estas remuneraciones sustituyen, para las empresas del piloto, la de referido del contrato docente; no se acumulan entre sí ni con las del Anexo de Habilitación Comercial sobre el mismo recaudo.')

cl(5, 'CORTES Y PAGO', 'Las remuneraciones se liquidan mensualmente, con corte el último día de cada mes, contra el reporte de ingresos de la academia y el tracker, y se pagan contra cuenta de cobro dentro de los cinco (5) días hábiles siguientes, respecto de pagos cuyo término legal de retracto ya esté vencido. Los gastos de desplazamiento y comunicación de EL CONTRATISTA son por su cuenta.')

cl(6, 'DURACIÓN Y CORTES DEL PILOTO', 'El piloto dura sesenta (60) días calendario desde la firma. Metas de referencia acumuladas: al día 15, seis empresas contactadas y dos reuniones con decisor; al día 30, doce contactadas, cinco reuniones y un convenio firmado; al día 45, dos convenios y las primeras personas remitidas por una empresa aliada; al día 60, tres convenios firmados y tres matrículas por alianza. Las partes revisan los avances los días 15, 30 y 45; si al día 30 no hay un convenio firmado, cualquiera de las partes puede dar por terminado el piloto; al día 60 revisan los resultados y deciden por escrito si el piloto se cierra, se prorroga o se formaliza como un rol de desarrollo comercial con metas trimestrales. El cierre del piloto no afecta el contrato docente ni las remuneraciones ya causadas, que se siguen pagando conforme al numeral 4.a.')

cl(7, 'REGLAS DE REPRESENTACIÓN', 'EL CONTRATISTA se presenta como docente de la academia habilitado para presentar el programa de alianzas; no se presenta como representante legal ni como empleado. No recibe dinero de las empresas ni de los estudiantes: todo pago va a las cuentas de la academia. Se obliga a usar únicamente el lenguaje institucional aprobado: "beca", nunca "descuento", "patrocinio" ni "gratis"; no promete empleo, visas, facilidad ni resultados distintos del texto exacto de la garantía institucional. Toda pieza o mensaje nuevo que use la marca requiere aprobación escrita de gerencia.')

cl(8, 'PROPIEDAD DE LA INFORMACIÓN', 'El material entregado, el tracker, los contactos empresariales generados durante el piloto y los convenios resultantes son de propiedad de GLOBAL TEACHER S.A.S., conforme a la cláusula de propiedad intelectual y confidencialidad del contrato docente. Al cierre del piloto EL CONTRATISTA devuelve el material y entrega el tracker actualizado.')

cl(9, 'EMPRESAS EXCLUIDAS DEL PILOTO (ya en conversación con la academia)', '1. ______________________________  2. ______________________________  3. ______________________________  4. ______________________________')

cl(10, 'VIGENCIA', 'Este anexo rige desde su firma por el término del piloto y, para efectos del numeral 4, por los doce meses posteriores a cada convenio firmado. Cualquiera de las partes puede terminarlo por escrito en cualquier momento sin afectar el contrato docente ni las remuneraciones ya causadas.')

d.add_paragraph()
t('Para constancia se firma en Bucaramanga, el día ______ de ____________ de 2026.', after=12)
t('EL CONTRATANTE                                                        EL CONTRATISTA', after=16)
t('_____________________________                                _____________________________', after=2)
t('DIANA MARCELA GÓMEZ RANGEL                              Nombre: ________________________', after=2)
t('Representante Legal — GLOBAL TEACHER S.A.S.                 C.C. ______________________________', after=2)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\contratos\ANEXO_PILOTO_ALIANZAS_EMPRESARIALES_DOCENTE_v1.docx'
d.save(out); print('OK', out)
