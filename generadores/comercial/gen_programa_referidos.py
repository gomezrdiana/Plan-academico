# -*- coding: utf-8 -*-
"""Propuesta PARA ANÁLISIS del programa de referidos (12/10/2026): bono al estudiante que refiere + pago al profe
embajador que los pide y registra + regla para no pagar tres veces. Documento por ROLES (sin nombres).
Salida: recursos/comercial/PROGRAMA_REFERIDOS_PROPUESTA_2026-10.docx"""
import re
from docx import Document
from docx.shared import Pt, RGBColor

NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)
m = lambda v: f'${v:,.0f}'.replace(',', '.')
CONTADO = 4_782_800; CUOTAS = 5_648_000; ARRANQUE = 2_990_000
LEAD = 10_800; CONV = 0.15; META_X_MATRICULA = round(LEAD / CONV)   # ~$72.000 de pauta por matrícula (dato interno 08/10)

d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(54); s.top_margin = s.bottom_margin = Pt(46)
def h(t, size=13):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(9); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAR
def p(t, color=None, size=10.5, after=4):
    x = d.add_paragraph(); x.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        r = x.add_run(part[2:-2] if part.startswith('**') else part); r.bold = part.startswith('**'); r.font.size = Pt(size)
        if color: r.font.color.rgb = color
def li(t): p('•  ' + t, after=2)
def tabla(rows, bold_first=True, shade=None):
    t = d.add_table(rows=1, cols=len(rows[0])); t.style = 'Table Grid'
    for j, v in enumerate(rows[0]):
        r = t.rows[0].cells[j].paragraphs[0].add_run(v); r.bold = True; r.font.size = Pt(9.5)
    for i, row in enumerate(rows[1:]):
        c = t.add_row().cells
        for j, v in enumerate(row):
            r = c[j].paragraphs[0].add_run(v); r.font.size = Pt(9.5); r.bold = (bold_first and j == 0) or (shade is not None and i == shade)
    d.add_paragraph()

p('HEIIU · COMERCIAL · DOCUMENTO INTERNO PARA ANÁLISIS', GRIS, 10)
p('PROGRAMA DE REFERIDOS — PROPUESTA (12/10/2026)', NAR, 15)
p('Qué se decide aquí: (1) cuánto recibe el estudiante que refiere, (2) cuánto recibe el profe embajador que pide y registra los referidos, (3) cómo cambia según contado o cuotas, y (4) la regla para no pagar tres veces por la misma matrícula. Todo por roles: estudiante que refiere · profe embajador · asesora comercial · coordinación.', GRIS, 9.5)

h('1. Por qué un programa y no "pedir el favor"')
p('Referidos es el único canal probado junto con la pauta (Estrategia de Ventas 2026, §7), y hoy funciona sin programa: nadie lo pide de forma fija ni se registra quién trajo a quién. Un referido es un lead que ya viene con confianza: no cuesta pauta, responde más y se retira menos. El programa fija tres cosas: **cuánto se paga, cuándo se pide y dónde se registra.**')

h('2. Lo que cuesta hoy una matrícula por pauta (para comparar)')
tabla([
 ['Concepto', 'Valor por matrícula', 'Fuente'],
 ['Pauta Meta', m(META_X_MATRICULA), f'{m(LEAD)} por lead de formulario ÷ {int(CONV*100)}% de conversión (datos internos 08/10)'],
 ['Plataforma del agente (LaHaus)', 'SUPUESTO — verificar', 'Cobra por lead facturable; falta el valor por lead del contrato'],
 ['Comisión de la asesora que cierra', m(round(CONTADO*0.05)) + ' (contado)', '5% del recaudo (esquema vigente)'],
 ['TOTAL aproximado', '≈ ' + m(META_X_MATRICULA + round(CONTADO*0.05)) + ' + plataforma', '≈ 6,5% del programa de contado, sin contar la plataforma'],
])
p('Conclusión: el programa de referidos no debe costar mucho más de **7-8% del valor de la matrícula** para que sea tan rentable como la pauta, y lo que lo justifica además es que no exige caja por adelantado (se paga solo cuando el referido ya pagó).', after=6)

h('3. Las dos opciones')
p('**Opción A — generosa:** bono alto al estudiante y pago fijo al embajador, con la asesora al 5% normal. Total ≈ ' + m(200_000 + 100_000 + round(CONTADO*0.05)) + ' por matrícula de contado (≈ 11%). Más cara que la pauta: solo se justifica si se mide que los referidos se retiran menos y pagan mejor.')
p('**Opción B — equilibrada (recomendada):** bono medio al estudiante, pago fijo al embajador y asesora al 3% en referidos (el lead llega pre-vendido y la cita la agenda el embajador, no el bot). Total ≈ ' + m(150_000 + 80_000 + round(CONTADO*0.03)) + ' por matrícula de contado (≈ 7,8%): igual de rentable que la pauta y sin caja por adelantado.', after=6)
tabla([
 ['Quién recibe', 'Programa completo DE CONTADO (' + m(CONTADO) + ')', 'Programa completo A CUOTAS (' + m(CUOTAS) + ')', 'Arranque A1+A2 (' + m(ARRANQUE) + ')'],
 ['Estudiante que refiere — Opción A', m(200_000) + ' al pagar la inicial', m(100_000) + ' con la inicial + ' + m(100_000) + ' con la cuota 3', m(100_000)],
 ['Estudiante que refiere — Opción B', m(150_000) + ' al pagar la inicial', m(75_000) + ' con la inicial + ' + m(75_000) + ' con la cuota 3', m(75_000)],
 ['Profe embajador — Opción A', m(100_000), m(60_000) + ' con la inicial + ' + m(40_000) + ' con la cuota 3', m(50_000)],
 ['Profe embajador — Opción B', m(80_000), m(50_000) + ' con la inicial + ' + m(30_000) + ' con la cuota 3', m(40_000)],
 ['Asesora que cierra', '5% (A) · 3% (B) del recaudo', 'igual, a medida que entra cada cuota', 'igual'],
], bold_first=True)
p('Cómo se paga el bono del estudiante: él elige **transferencia** o **abono a su propia cuota** (si está financiado). Para el estudiante que ya terminó de pagar, transferencia. Sin tope de referidos: quien trae 3 matrículas cobra 3 bonos.', after=6)

h('4. Reglas (las que evitan pagar de más o pagar mal)')
for t in [
 '**Registro antes del primer contacto.** El referido se registra en la planilla (nombre, teléfono, quién lo refiere, fecha) ANTES de que la asesora o el bot le escriban. Si ya estaba en el sistema (bot, formulario o base) en los últimos 30 días, no es referido: es un lead de pauta y no genera bono.',
 '**El bono se paga cuando el referido pagó la inicial y asistió a su clase 5.** Así no se paga por matrículas que se retiran en la primera semana. El segundo pago (cuotas) se liquida cuando entra la cuota 3.',
 '**No se paga tres veces.** El embajador cobra por REGISTRAR y AGENDAR; la asesora, por CERRAR. Si el embajador cierra solo (sin asesora en la venta), recibe el 5% del recaudo en vez del fijo, como cualquier vendedor; nunca las dos cosas.',
 '**Nunca descuentos al referido como gancho.** El referido entra con la misma tarifa y la misma beca que cualquier estudiante; el beneficio es para quien refiere. Esto protege la escalera de precios y evita que el referido "negocie" con el bono del otro.',
 '**Sin plata al profe por estudiantes de su propio grupo que ya estaban matriculados.** El embajador cobra por referidos nuevos que él registró, de cualquier grupo.',
 '**Nada de esto se comunica como "comisión" a los estudiantes.** A ellos se les dice "bono de referidos". Lo del embajador es un acuerdo interno por escrito (otrosí a su contrato) antes del primer pago.',
]: li(t)

h('5. Cómo opera (piloto de 60 días)')
for t in [
 '**El profe embajador** (sin grupo a cargo durante el piloto) pasa por TODOS los grupos en la primera semana: 10 minutos al cierre de clase, con el guion: "¿Conoces a alguien que necesite inglés de verdad — para el trabajo, para irse, para su hijo? Dame su nombre y su número; nosotros lo llamamos y, si se matricula, tú recibes un bono." Lo registra ese mismo día.',
 '**Momentos fijos de pedir**, además de la ronda: al cerrar una matrícula (la asesora), al grabar un testimonio, tras una presentación de midterm o final, y al graduar (cada graduado sale con 2 referidos pedidos).',
 '**Coordinación** lleva la planilla única (referido · quién refiere · embajador · fecha · estado: contactado / cita / matriculado / Cl 5 / bono pagado) y liquida los bonos a fin de mes contra esa planilla.',
 '**Meta del piloto:** 30 referidos registrados en 60 días → 10 citas → 4 matrículas. Con eso se mide el costo real por matrícula y se decide si sigue, sube o cambia.',
 '**Seguimiento:** reporte semanal de 5 líneas (registrados, contactados, citas, matrículas, bonos) en la reunión fija de los lunes.',
]: li(t)

h('6. Lo que falta decidir (Diana)')
for t in ['Opción A o B (recomendada: B).',
          'Si el embajador cobra también cuando el referido entra a un programa personalizado o a una alianza empresarial (propuesta: sí, con los mismos fijos).',
          'Valor por lead de la plataforma del agente, para cerrar la comparación de la sección 2.',
          'Si el bono del estudiante puede ser, en vez de plata, 2 horas 1-a-1 (costo para la academia ≈ ' + m(60_000) + ', valor percibido ≈ ' + m(100_000) + '): sirve como alternativa, no como única opción.']: li(t)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\PROGRAMA_REFERIDOS_PROPUESTA_2026-10.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
