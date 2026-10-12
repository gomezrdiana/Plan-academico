# -*- coding: utf-8 -*-
"""Brief de la PRUEBA PRÁCTICA pagada para candidatos a Community Manager (Kimberly, Sebastián).
La prueba = ejecutar desde casa (sin ir a la academia) un guion del paquete de grabación 09/10 (GUION 4 'Siete meses',
V3_575H) con las mismas reglas de entrega que el videógrafo; mide si sigue instrucciones y cómo maneja sus opiniones. El texto del guion se copia verbatim de GUIONES_GRABACION_2026-10-09.docx.
Salida: recursos/comercial/contratacion/COMMUNITY_MANAGER/BRIEF_PRUEBA_PRACTICA_CM.docx"""
import os, re
from docx import Document
from docx.shared import Pt, RGBColor

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu'
SRC = os.path.join(BASE, r'recursos\comercial\campañas\GUIONES_GRABACION_2026-10-09.docx')
OUT = os.path.join(BASE, r'recursos\comercial\contratacion\COMMUNITY_MANAGER\BRIEF_PRUEBA_PRACTICA_CM.docx')
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)

# --- guion 3 verbatim del paquete ---
paras = [p.text for p in Document(SRC).paragraphs if p.text.strip()]
i0 = next(i for i, t in enumerate(paras) if t.startswith('GUION') and 'SIETE MESES' in t.upper())
i1 = next(i for i, t in enumerate(paras) if t.startswith('GUION') and i > i0)
guion = [t for t in paras[i0:i1] if not t.startswith('Mensaje prellenado')]  # el prellenado lo configura el trafficker en Meta, no va en el video

d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10.5)
for s in d.sections: s.left_margin = s.right_margin = Pt(54); s.top_margin = s.bottom_margin = Pt(48)

def h(t, size=13):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(t); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAR
def p(t, color=None, size=10.5, after=4):
    x = d.add_paragraph(); x.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', t):
        if not part: continue
        r = x.add_run(part[2:-2] if part.startswith('**') else part); r.bold = part.startswith('**'); r.font.size = Pt(size)
        if color: r.font.color.rgb = color
def li(t): p('•  ' + t, after=2)
def caja(lines):
    t = d.add_table(rows=1, cols=1); t.style = 'Table Grid'; c = t.rows[0].cells[0]
    first = True
    for ln in lines:
        x = c.paragraphs[0] if first else c.add_paragraph(); first = False
        r = x.add_run(ln); r.font.size = Pt(10); x.paragraph_format.space_after = Pt(3)
        if ln.startswith('GUION'): r.bold = True; r.font.color.rgb = NAR
    d.add_paragraph()

p('HEIIU ENGLISH ACADEMY · COMMUNITY MANAGER', GRIS, 10)
p('PRUEBA PRÁCTICA PAGADA — PRODUCIR UN ANUNCIO DESDE UN GUION', NAR, 15)
p('Pago: $100.000 contra entrega. Se paga igual si pasas o no la prueba. El material entregado queda para uso de la academia.', GRIS, 9.5)

h('1. Qué es la prueba')
p('En Heiiu los anuncios de pauta paga se producen a partir de **guiones escritos por gerencia**: cada guion trae los primeros segundos que detienen a la persona, el texto que se dice tal cual, lo que se ve, las letras que van en pantalla, el cierre y un **código** que identifica el anuncio. El CM recibe el guion, graba, edita y entrega el video a gerencia para aprobación; gerencia se lo pasa al trafficker, que lo sube a Meta. La prueba es exactamente eso: **te enviamos UN guion y entregas el video terminado**, con las reglas de las secciones 3 y 4. Estos videos no son libres ni creativos, a diferencia de los orgánicos, porque son los que llevan el presupuesto de pauta: buscamos que el guion se ejecute como está escrito y que el archivo quede listo para pauta.')

h('2. El guion asignado: GUION 4 "Siete meses" (anuncio V3_575H) — se graba desde casa')
p('**No tienes que venir a la academia.** Te grabas tú, o alguien que te haga el favor, en tu casa o donde quieras. Quien sale a cámara habla como presentador(a). El guion es el mismo que se graba en la academia con la profe; abajo está adaptado para casa. Todo lo demás se ejecuta tal cual. **Si algo no queda claro, escríbenos antes de grabar:** preferimos la comunicación abierta y resolver dudas a tiempo; intentamos dártelo muy detallado, pero cualquier pregunta es bienvenida.', after=6)
rod = d.add_table(rows=1, cols=4); rod.style = 'Table Grid'
for j, v in enumerate(['Segundos', 'Qué se ve', 'Qué dice la persona (hablado + subtítulos, tal cual)', 'Letras grandes en pantalla (texto sobre el video)']):
    r = rod.rows[0].cells[j].paragraphs[0].add_run(v); r.bold = True; r.font.size = Pt(9.5)
for row in [
 ('0-2', 'Primer plano de la hoja: escribe "5 AÑOS" grande y lo tacha con una raya.', '(no habla todavía)', '"Lo que tarda el inglés a 2 horas por semana."'),
 ('2-8', 'La persona a cámara, plano medio, la hoja a un lado.', '"El Marco Común Europeo calcula entre quinientas y seiscientas horas de clase para llegar a B2."', '"B2 = 500-600 h (Marco Común Europeo)"'),
 ('8-18', 'Mientras habla, escribe en la hoja frente a la cámara (no llevarlo escrito de antes): "575 h", "7 meses", "14 meses", con letra grande para que se lea.', '"Si estudias dos horas por semana, son cinco años. En Heiiu: cuatro horas al día, siete meses. O si trabajas, dos horas cada noche: catorce."', '"2 h/semana = 5 años" · luego "En Heiiu: 7 meses · noche: 14"'),
 ('18-22', 'Vuelve a cámara, seria, sin sonrisa de comercial.', '"No es fácil. Es rápido porque es intenso."', '(ninguna)'),
 ('22-25', 'Cierre a cámara. En el último segundo aparece el logo de Heiiu.', '"Pregúntanos qué fecha te queda. Escríbenos."', '"Garantía por escrito"'),
]:
    c = rod.add_row().cells
    for j, v in enumerate(row):
        r = c[j].paragraphs[0].add_run(v); r.font.size = Pt(9.5); r.bold = (j == 0)
d.add_paragraph()
p('**Versión de 15 segundos** (se corta del mismo material; no se graba aparte):', after=3)
r15 = d.add_table(rows=1, cols=3); r15.style = 'Table Grid'
for j, v in enumerate(['Segundos', 'Qué se ve', 'Qué dice (tal cual)']):
    r = r15.rows[0].cells[j].paragraphs[0].add_run(v); r.bold = True; r.font.size = Pt(9.5)
for row in [('0-3', 'Tacha "5 AÑOS" en la hoja.', '(no habla)'),
            ('3-11', 'A cámara; escribe "7 meses".', '"Si estudias dos horas por semana, son cinco años. En Heiiu: cuatro horas al día, siete meses."'),
            ('11-15', 'Cierre a cámara + logo en el último segundo.', '"No es fácil. Es intenso. Pregúntanos qué fecha te queda."')]:
    c = r15.add_row().cells
    for j, v in enumerate(row):
        r = c[j].paragraphs[0].add_run(v); r.font.size = Pt(9.5); r.bold = (j == 0)
d.add_paragraph()
p('**Qué vende este anuncio y qué no:** la velocidad con un número real. El Marco Común Europeo estima 500-600 horas guiadas para llegar a B2; Heiiu son 575 horas en 7 meses (4 h/día) o 14 meses (2 h/noche). "7 meses" se dice como descripción del programa; **jamás** "garantizado que hablas en 7 meses". Sin precio. Las dos jornadas van en la misma pieza para no dejar por fuera al nocturno.', after=6)
p('**Adaptaciones para grabar en casa (solo estas):**', after=2)
for t in ['En vez de tablero se usa una hoja, cartulina o pizarra pequeña (ya está así en la tabla).',
          'La persona habla a cámara, plano medio, fondo limpio (una pared), sin logos de otras marcas ni ropa con marcas.',
          'Si no tienes a nadie que te ayude, te grabas tú misma: cuenta igual.']: li(t)
p('**Si ves algo que mejoraría el guion** (una palabra, el orden, el inicio), nos encanta escucharlo: entrega el video como está escrito y mándanos tus ideas aparte, por WhatsApp, con el porqué. Así conocemos las dos cosas que nos importan: cómo ejecutas y cómo piensas.', after=6)

h('3. Reglas de grabación y edición (las mismas de todos nuestros anuncios)')
for t in [
 'Formato **9:16, 1080x1920, MP4**. Celular o cámara en vertical.',
 'Audio: micrófono de solapa o el celular a **menos de 1,5 m** de quien habla. Luz natural o del salón; **sin aro de luz** (se ve a anuncio).',
 '**Subtítulos grandes, palabra por palabra**, dentro de la zona segura de Reels: ni en el 14% superior ni en el 35% inferior de la pantalla.',
 'Textos en pantalla con los colores de marca: naranja #E54C09 y amarillo #FBC900 (el amarillo **nunca** como texto sobre blanco). Logo de Heiiu **solo en el último segundo**.',
 'Música baja o ninguna; nunca encima de la voz.',
 'El texto se dice **tal cual está en el guion**. Si a quien habla se le sale algo prohibido, se repite la toma.',
 '**Prohibido** (en voz, subtítulo o texto en pantalla): precio · nombres de programas ("Arranque", "A1 intensivo") · "fácil" · "gratis" · "descuento" · "rápido" sin el número · "garantizado en X meses" · "consigue trabajo" · "visa" · "profesores nativos" · días de la semana · nombres de estudiantes.',
 '**Prohibido** el gancho que le atribuye una carencia al que mira ("¿No sabes inglés?", "¿Crees que el inglés es aburrido?"): política de Meta y, además, ya no funcionó. El gancho es el que trae el guion.',
 'Cierre siempre a WhatsApp, con la frase de cierre del guion.',
]: li(t)

h('4. Qué entregas')
for t in [
 '**Dos archivos:** versión completa (20-30 s) y versión de 15 s (gancho + frase fuerte + cierre), cortada del mismo material.',
 'Nombre de archivo = código + letra B (porque es la segunda versión de este anuncio) + duración: **V3_575H_B_30s.mp4** y **V3_575H_B_15s.mp4**. El código identifica el guion para el trafficker, que es quien sube los anuncios a Meta y configura el botón de WhatsApp. **Tú no subes nada a Meta** ni configuras mensajes.',
 'Enviados al WhatsApp de gerencia **como DOCUMENTO**, no como video (para que WhatsApp no los comprima).',
 'Más el **material en bruto** en una carpeta de Drive compartida (sirve para cortar otros ganchos sin volver a grabar).',
 '**Plazo:** máximo 5 días calendario desde que recibes este brief. Tú propones la fecha de entrega al confirmar.',
]: li(t)

h('5. Cómo se evalúa (pasa quien cumple los 7)')
t = d.add_table(rows=1, cols=2); t.style = 'Table Grid'
for j, v in enumerate(['Criterio', 'Qué se revisa']):
    r = t.rows[0].cells[j].paragraphs[0].add_run(v); r.bold = True; r.font.size = Pt(9.5)
for a, b in [
 ('1. Gancho', 'Los primeros 2 segundos son los del guion: imagen + texto grande. Nada prohibido.'),
 ('2. Texto', 'La persona dice el texto tal cual; "575 h", "7 meses" y "14 meses" quedan escritos en la hoja y legibles.'),
 ('3. Subtítulos', 'Grandes, palabra por palabra, dentro de la zona segura. Sin errores de ortografía.'),
 ('4. Formato y nombre', '9:16, 1080x1920, MP4, nombres exactos, enviados como documento, bruto en Drive.'),
 ('5. Audio e imagen', 'Voz limpia sin eco ni ruido; encuadre estable; sin aro de luz; la hoja con las cifras se lee.'),
 ('6. Versión de 15 s', 'Respeta la estructura del guion (gancho → frase fuerte → cierre) y se entiende sola.'),
 ('7. Entrega y sugerencias', 'En la fecha que propusiste. El video va como está escrito; las sugerencias, si las hay, aparte y con su porqué.'),
]:
    c = t.add_row().cells
    for j, v in enumerate([a, b]):
        r = c[j].paragraphs[0].add_run(v); r.font.size = Pt(9.5); r.bold = (j == 0)
d.add_paragraph()

h('6. Qué pasa después')
p('Si pasas la prueba, se firma el contrato de prestación de servicios en las condiciones conversadas. El trabajo mensual tiene **dos partes**: (1) **los anuncios para pauta**: recibes el guion escrito por gerencia, grabas en la academia con los profes y los estudiantes, editas y entregas el video listo con su código, con estas mismas reglas (esta prueba mide esa parte, desde casa, antes de grabar en la academia); y (2) **el contenido orgánico**: testimonios, ejercicios en clase, historias y el día a día de la academia, guiado por tu creatividad y por las ideas que te demos, respetando las reglas de mensaje de Heiiu (la lista de prohibidos de la sección 3).')
p('Cualquier duda sobre el guion o la logística: por WhatsApp a gerencia, antes de grabar. Lo que no esté escrito en el guion, se pregunta.', GRIS, 9.5)

try:
    d.save(OUT); print('OK', OUT)
except PermissionError:
    d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
print('\n'.join(guion))
