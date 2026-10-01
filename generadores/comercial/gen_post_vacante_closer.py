# -*- coding: utf-8 -*-
"""Vacante CLOSER de planta (version 01/10/2026): post LinkedIn + pieza grafica + instrucciones Brian + portales + mensaje directo.
Salida: recursos/comercial/INDUCCION_COMERCIAL/contratacion comercial/POST_LINKEDIN_VACANTE_CLOSER.xlsx"""
import openpyxl
from openpyxl.styles import Alignment, Font

OUT = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\INDUCCION_COMERCIAL\contratacion comercial\POST_LINKEDIN_VACANTE_CLOSER.xlsx'
wb = openpyxl.Workbook(); wb.remove(wb.active)

def hoja(nombre, lineas):
    ws = wb.create_sheet(nombre)
    for l in lineas: ws.append([l])
    ws.column_dimensions['A'].width = 120
    for c in ws['A']: c.alignment = Alignment(wrap_text=True, vertical='top')
    ws['A1'].font = Font(bold=True)

hoja('POST LINKEDIN', [
    'Busco a la persona que cierra. Las citas te las ponemos nosotros: tú las conviertes en matrículas.',
    'En Heiiu English Academy (Bucaramanga) abrimos UNA vacante: Ejecutivo(a) Comercial de Cierre, de planta.',
    'Te lo digo de frente, como le hablamos a nuestros estudiantes: este cargo no es de esperar. Cada día te llegan personas que ya preguntaron, ya conocen el precio y ya agendaron una asesoría. Tu trabajo es atenderlas en la sede o por videollamada, resolver sus dudas, manejar la objeción y cerrar la matrícula en esa cita o en las 48 horas siguientes. Si lo tuyo es "déjame pensarlo y te llamo la otra semana", esta vacante no es para ti. Si lo tuyo es cerrar, sigue leyendo.',
    'QUÉ VAS A VENDER',
    'No vendemos clases de inglés. Vendemos entrenamiento con garantía de aprendizaje por escrito, avance medido y el respaldo de una institución con licencia desde 2012 y certificación ICONTEC. Un producto con diferenciales reales, un sistema de citas que funciona y material de venta listo para usar.',
    'QUÉ OFRECEMOS',
    '✔ Contrato laboral a término fijo de un año, con todas las prestaciones de ley.',
    '✔ Básico de $2.000.000 + comisiones sin techo sobre lo que cierras.',
    '✔ Dos aumentos de básico en tu primer año, atados a tus resultados (mes 4 y mes 7).',
    '✔ Las citas llegan agendadas: tú no prospectas en frío, tú cierras.',
    '✔ Metas claras y medición transparente desde el día uno.',
    'QUÉ BUSCAMOS',
    '• Mínimo 2 años cerrando intangibles en cita: educación, seguros, servicios financieros, planes o membresías.',
    '• Experiencia cerrando ventas de $3 millones en adelante, con tasa de cierre que puedas demostrar con números.',
    '• Capacidad de decidir en la cita: manejo de objeciones de precio, de tiempo y de "lo consulto con mi esposo".',
    '• Disciplina de registro: cada cita queda registrada con su resultado el mismo día. Lo que no está en el sistema, no existe.',
    '• Trabajo presencial en Bucaramanga (sector Sotomayor), con disponibilidad en la tarde y noche entre semana.',
    'CÓMO APLICAR',
    'Envía tu hoja de vida a auxiliaradministrativo@heiiu.com con el asunto "Closer Heiiu" y, esto es lo importante, un audio o video de 1 minuto contándonos la venta más difícil que has cerrado y cómo la cerraste. Sin el audio no revisamos la hoja de vida. En la entrevista harás un cierre simulado.',
    'Si conoces a alguien así, etiquétalo(a). La persona correcta llega a un cargo donde su esfuerzo se nota en su bolsillo.',
    '#Bucaramanga #EmpleoBucaramanga #Ventas #Closer #AsesorComercial',
])

hoja('PIEZA GRAFICA', [
    'TEXTO PARA LA PIEZA GRÁFICA (imagen del post)',
    'Titular: BUSCAMOS CLOSER COMERCIAL DE PLANTA',
    'Subtítulo: Las citas te las ponemos nosotros. Tú cierras.',
    '· Contrato laboral a un año + prestaciones',
    '· Básico $2.000.000 + comisiones sin techo',
    '· 2 aumentos de básico en tu primer año por resultados',
    '· Bucaramanga · presencial · tardes y noches',
    'Cierre: Aplica con tu hoja de vida + un audio de 1 minuto. Detalles en el post.',
    'Marca: logo Heiiu, naranja #E54C09 sobre crema #FFF8E7. El amarillo #FBC900 nunca como texto sobre blanco.',
])

hoja('PARA BRIAN', [
    'PARA BRIAN — SOLO LINKEDIN Y REDES',
    '1. PIEZA PRINCIPAL: crear la vacante gratuita en LinkedIn Empleos desde la página de empresa de Heiiu, con el texto del post (título: Ejecutivo(a) Comercial de Cierre · ubicación: Bucaramanga · presencial · tiempo completo). Aparece por búsqueda, no depende de seguidores.',
    '2. Publicar el post en la página de Heiiu con la pieza gráfica, y compartirlo desde su perfil como apoyo, siempre enlazando a la vacante oficial de Heiiu.',
    '3. Replicar la pieza gráfica en Instagram y Facebook de la academia.',
    '4. Si se le pone pauta: segmentar Bucaramanga y área metropolitana, cargos actuales tipo asesor comercial, ejecutivo de ventas, closer o ejecutivo de cuenta, sectores seguros, educación, telecomunicaciones, servicios financieros y planes de salud o exequiales.',
    '5. Las hojas de vida llegan a auxiliaradministrativo@heiiu.com con el asunto "Closer Heiiu".',
])

hoja('PORTALES (ACADEMIA)', [
    'PORTALES DE EMPLEO GRATUITOS — LOS PUBLICA LA ACADEMIA, NO BRIAN',
    'Dónde: Computrabajo · Magneto · elempleo · Servicio Público de Empleo (Agencia de Cajasan o Comfenalco) · grupos de empleo de Bucaramanga en Facebook.',
    'Datos para llenar los formularios:',
    '· Cargo: Ejecutivo(a) Comercial de Cierre, de planta',
    '· Empresa: Heiiu English Academy (Global Teacher S.A.S.)',
    '· Ciudad: Bucaramanga · presencial · tiempo completo · disponibilidad tardes y noches',
    '· Contrato: término fijo a un año',
    '· Salario: $2.000.000 + comisiones + prestaciones de ley',
    '· Experiencia: mínimo 2 años cerrando intangibles en cita',
    '· Descripción: copiar el texto de la hoja POST LINKEDIN, sin los hashtags.',
    '· Contacto: auxiliaradministrativo@heiiu.com, asunto "Closer Heiiu".',
    'Filtro al recibir: quien no mande el audio o video de 1 minuto queda descartado sin revisar. A los que sí lo manden se les aplica la guía de entrevista (GUIA_ENTREVISTA_COMERCIAL_v3) más el cierre simulado.',
])

hoja('MENSAJE DIRECTO', [
    'MENSAJE DIRECTO PARA VENDEDORES QUE YA ESTÁN TRABAJANDO (búsqueda activa en LinkedIn)',
    'Hola [NOMBRE], vi tu perfil y tu experiencia en ventas en [EMPRESA / SECTOR]. En Heiiu English Academy, en Bucaramanga, estamos buscando UNA persona de cierre, de planta: contrato laboral a un año, básico de $2.000.000 más comisiones sin techo, y dos aumentos de básico en el primer año atados a resultados. Las citas llegan agendadas; el trabajo es cerrarlas.',
    'Si te interesa conocer los detalles, o conoces a alguien con ese perfil, cuéntame y te comparto la información completa.',
    'A quién buscar: personas en Bucaramanga con cargos de asesor comercial, closer, ejecutivo de ventas o ejecutivo de cuenta en seguros, planes exequiales o de salud, telecomunicaciones, servicios financieros o educación. Meta: 20 mensajes directos en la primera semana.',
])

hoja('NOTA INTERNA (no publicar)', [
    'NOTA INTERNA — no se publica ni se envía a Brian',
    'Cuándo se publica: el 15/10/2026 si se cumple cualquiera de estas tres: más de 25 citas agendadas en el mes · franjas sin atender · cierre de la asesora por debajo de 1 de cada 3 citas atendidas. Antes no.',
    'Frontera con la asesora actual (comisión pura, leads digitales por contrato): se define por escrito antes de la primera cita de la closer. Propuesta: la asesora conserva sus canales propios y los leads que ya trabaja; la closer de planta toma las citas que agenda el asistente para atención en sede y las franjas que la asesora no cubre. La comisión es de quien atiende la cita y cierra.',
    'Regla de cierre que aplica a todas: la cita termina con separación, con segunda conversación con fecha dentro de 48 horas, o con "no por ahora" y su razón. Lo que pasa de 48 horas vuelve al sistema.',
    'Reglamento y entrevista: REGLAMENTO_MEDICION_COMERCIAL (término fijo 1 año + 2 meses de prueba, metas de actividad y resultado) y GUIA_ENTREVISTA_COMERCIAL_v3 con el cierre simulado como prueba práctica. Costo cargado estimado: ~$2.4M/mes; se paga con 1 matrícula.',
])

wb.save(OUT); print('OK', OUT)
