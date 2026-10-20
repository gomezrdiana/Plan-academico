# -*- coding: utf-8 -*-
"""KIT DE ARRANQUE del GERENTE DE ALIANZAS EMPRESARIALES (cargo indefinido). Deriva del kit del reto
(gen_kit_arranque_reto_alianzas.py, única fuente del contenido): misma oferta, precios, documentos, reunión, charla,
objeciones y reglas; sin meta del reto, sin secciones 12-13, con tablero en vez de planilla y seguimiento 8:45.
Salida (fuera de git): Candidatos/John Hinestroza/KIT_ARRANQUE_GERENTE_ALIANZAS.docx (+PDF).
Correr desde la raíz: python generadores/comercial/gen_kit_arranque_gerente_alianzas.py"""
import os, re
SRC = os.path.join(os.path.dirname(__file__), 'gen_kit_arranque_reto_alianzas.py')
s = open(SRC, encoding='utf-8').read()
R = [
 ('Kit de arranque · Reto de 15 días · Ejecutivo de alianzas', 'Kit de arranque · Gerente de Alianzas Empresariales'),
 ('KIT DE ARRANQUE — RETO DE 15 DÍAS · ALIANZAS EMPRESARIALES', 'KIT DE ARRANQUE · GERENTE DE ALIANZAS EMPRESARIALES'),
 ('Heiiu English Academy · Para el ejecutivo de alianzas · Del miércoles 21 de octubre al martes 3 de noviembre de 2026 · Léelo completo antes de responder al reto', 'Heiiu English Academy · Para el Gerente de Alianzas Empresariales · Léelo completo antes de la primera reunión con una empresa'),
 ("'**Tu meta:** 10 personas inscritas y pagadas, **o $30.000.000 en caja** de Heiiu, lo que llegue primero, al martes 3 de noviembre a las 6:00 p. m., traídas por ti: empresas, referidos o conocidos, de cualquier programa (completo, parcial, Arranque, plan empresa o inglés para empresarios). Cada persona queda registrada en tu planilla antes de pagar. Inscrito pagado = pagó de contado, o pagó la inicial de su plan de pagos y firmó el contrato con coordinación. Caja = dinero verificado en la cuenta de Heiiu. Lo ideal es de contado: 7 completos de contado ya son la meta.'",
  "'**Tus metas y tus cortes** están en tu anexo de compensación; aquí no se repiten. Toda empresa y toda persona queda registrada en el tablero de alianzas antes de la primera reunión o del pago. Inscrito pagado = pagó de contado, o pagó la inicial de su plan de pagos y firmó el contrato con coordinación. Caja = dinero verificado en la cuenta de Heiiu. Lo ideal es de contado.'"),
 ("'**Tu rutina fija:** 15 minutos con gerencia todos los días a las **8:30 a. m.** (el miércoles 21 en la sede, después por llamada): rutina del día, dudas, sugerencias, recomendaciones e indicadores si los hay. La planilla FORMATO_15_EMPRESAS_RETO.xlsx siempre al día antes de esa llamada.'",
  "'**Tu rutina fija:** seguimiento con gerencia todos los días a las **8:45 a. m.**: lunes presencial de planeación de la semana (30 min); martes a jueves por llamada (15 min: avance, dudas, ayuda); viernes presencial de cierre de semana con el tablero (30 min). Lo preparas y lo presentas tú. El tablero de alianzas (TABLERO_ALIANZAS.xlsx) siempre al día antes de esa hora.'"),
 ('El foco del reto es la gente que empieza de cero: es lo más fácil de cerrar y lo que abre el grupo del 3 de noviembre.', 'El foco es la gente que empieza de cero: es lo más fácil de cerrar y lo que abre cada grupo nuevo.'),
 ('te lo entrega gerencia en la inducción del miércoles 21.', 'te lo entrega gerencia en la inducción.'),
 ('Registra la empresa en la planilla antes de escribir.', 'Registra la empresa en el tablero antes de escribir: la empresa es de quien la registra primero, por 60 días.'),
 ('Fecha en la planilla', 'Fecha en el tablero'),
 ('pasas los interesados a la planilla', 'pasas los interesados al tablero'),
 ('Lo anotas en la planilla.', 'Lo anotas en el tablero.'),
 ('ese mismo día en la planilla (hoja INTERESADOS).', 'ese mismo día en el tablero de alianzas.'),
 ('Para entrar el 3 de noviembre, pagado antes de esa fecha.', 'Para entrar a un grupo, pagado antes de su fecha de inicio.'),
 ('Grupo del 3 de noviembre; el horario', 'Próximo grupo (martes 3 de noviembre); el horario'),
 ('verificado por coordinación,** a más tardar el martes 3 de noviembre a las 6:00 p. m.', 'verificado por coordinación,** dentro de la fecha de cada corte.'),
 ('**Los que ya venían avanzados** y que la academia te entregue para cerrar: te pagan comisión, pero no cuentan para los 10.', '**Los contactos de la base de la academia** que gerencia te asigne se trabajan como cualquier cliente: cuentan completos para los cortes del periodo de prueba y al 50% para la meta trimestral, como dice tu anexo.'),
 ('Una sola fecha de inicio: martes 3 de noviembre.', 'Una sola fecha de inicio por grupo: la que fija gerencia (el próximo abre el martes 3 de noviembre).'),
 ('van solo en la planilla y en la hoja física', 'van solo en el tablero y en la hoja física'),
 ('Toda empresa queda registrada en el formato antes de la primera reunión.', 'Toda empresa queda registrada en el tablero antes de la primera reunión; la empresa es de quien la registra primero, por 60 días.'),
 ('15 minutos con gerencia todos los días a las 8:30 a. m., sin cancelar. La planilla al día, todos los días, antes de esa llamada.', 'Seguimiento con gerencia todos los días a las 8:45 a. m., sin cancelar. El tablero al día, todos los días, antes de esa hora.'),
]
for a, b in R:
    assert a in s, 'NO ENCONTRADO: ' + a[:60]
    s = s.replace(a, b)
i = s.index('# ---------------------------------------------------------------- 12'); j = s.index('out = BASE')
s = s[:i] + s[j:]
s = s.replace(r"out = BASE + r'\KIT_ARRANQUE_RETO_15_DIAS_ALIANZAS.docx'",
              r"out = BASE + r'\LINKEDIN DIANA GOMEZ\Candidatos\John Hinestroza\KIT_ARRANQUE_GERENTE_ALIANZAS.docx'")
exec(compile(s, SRC, 'exec'))
