# -*- coding: utf-8 -*-
"""Brief de la PRUEBA PRÁCTICA pagada para candidatos a Community Manager (Kimberly, Sebastián).
La prueba = ejecutar un guion del paquete de grabación 09/10 (GUION 4 'Siete meses', V3_575H) con las mismas
reglas de entrega que el videógrafo. El texto del guion se copia verbatim de GUIONES_GRABACION_2026-10-09.docx.
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
guion = paras[i0:i1]

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
p('En Heiiu los anuncios se producen a partir de **guiones escritos por gerencia**: cada guion trae el gancho, el texto que se dice tal cual, lo que se ve, el texto en pantalla, el cierre y un **código** que identifica el anuncio en la pauta. El videógrafo recibe el guion, graba y entrega el video listo para subir a Meta, sin que gerencia intervenga. La prueba es exactamente eso: **tomas UN guion del paquete actual y entregas el anuncio terminado**, con las mismas reglas de entrega que usa el videógrafo. No es una pieza libre ni un video "creativo": se evalúa que el guion se ejecute como está escrito y que el archivo quede listo para pauta.')

h('2. El guion asignado: GUION 4 "Siete meses" (anuncio V3_575H)')
p('Necesitas a la profe y el tablero del salón vacío, unos 15 minutos antes de una clase. Gerencia coordina el día y la hora con la profe; tú llegas con tu equipo. La profe dice el texto; tú diriges el encuadre, el audio y las tomas (2 tomas mínimo).', after=6)
caja(guion)

h('3. Reglas de grabación y edición (las mismas del videógrafo)')
for t in [
 'Formato **9:16, 1080x1920, MP4**. Celular o cámara en vertical.',
 'Audio: micrófono de solapa o el celular a **menos de 1,5 m** de quien habla. Luz natural o del salón; **sin aro de luz** (se ve a anuncio).',
 '**Subtítulos grandes, palabra por palabra**, dentro de la zona segura de Reels: ni en el 14% superior ni en el 35% inferior de la pantalla.',
 'Textos en pantalla con los colores de marca: naranja #E54C09 y amarillo #FBC900 (el amarillo **nunca** como texto sobre blanco). Logo de Heiiu **solo en el último segundo**.',
 'Música baja o ninguna; nunca encima de la voz.',
 'El texto se dice **tal cual está en el guion**. Si la profe dice algo prohibido, se repite la toma.',
 '**Prohibido** (en voz, subtítulo o texto en pantalla): precio · nombres de programas ("Arranque", "A1 intensivo") · "fácil" · "gratis" · "descuento" · "rápido" sin el número · "garantizado en X meses" · "consigue trabajo" · "visa" · "profesores nativos" · días de la semana · nombres de estudiantes.',
 '**Prohibido** el gancho que le atribuye una carencia al que mira ("¿No sabes inglés?", "¿Crees que el inglés es aburrido?"): política de Meta y, además, ya no funcionó. El gancho es el que trae el guion.',
 'Cierre siempre a WhatsApp, con la frase de cierre del guion.',
]: li(t)

h('4. Qué entregas')
for t in [
 '**Dos archivos:** versión completa (20-30 s) y versión de 15 s (gancho + frase fuerte + cierre), cortada del mismo material.',
 'Nombre de archivo = código + letra B (porque es la segunda versión de este anuncio) + duración: **V3_575H_B_30s.mp4** y **V3_575H_B_15s.mp4**.',
 'Enviados al WhatsApp de gerencia **como DOCUMENTO**, no como video (para que WhatsApp no los comprima).',
 'Más el **material en bruto** completo en una carpeta de Drive compartida (sirve para cortar otros ganchos sin volver a grabar).',
 '**Plazo:** máximo 5 días calendario después de la grabación. Tú propones la fecha de entrega al confirmar.',
]: li(t)

h('5. Cómo se evalúa (pasa quien cumple los 7)')
t = d.add_table(rows=1, cols=2); t.style = 'Table Grid'
for j, v in enumerate(['Criterio', 'Qué se revisa']):
    r = t.rows[0].cells[j].paragraphs[0].add_run(v); r.bold = True; r.font.size = Pt(9.5)
for a, b in [
 ('1. Gancho', 'Los primeros 2 segundos son los del guion: imagen + texto grande. Nada prohibido.'),
 ('2. Texto', 'La profe dice el texto tal cual; "575 h", "7 meses" y "14 meses" quedan escritos en el tablero y legibles.'),
 ('3. Subtítulos', 'Grandes, palabra por palabra, dentro de la zona segura. Sin errores de ortografía.'),
 ('4. Formato y nombre', '9:16, 1080x1920, MP4, nombres exactos, enviados como documento, bruto en Drive.'),
 ('5. Audio e imagen', 'Voz limpia sin eco ni ruido; encuadre estable; sin aro de luz.'),
 ('6. Versión de 15 s', 'Respeta la estructura del guion (gancho → frase fuerte → cierre) y se entiende sola.'),
 ('7. Entrega', 'En la fecha que propusiste.'),
]:
    c = t.add_row().cells
    for j, v in enumerate([a, b]):
        r = c[j].paragraphs[0].add_run(v); r.font.size = Pt(9.5); r.bold = (j == 0)
d.add_paragraph()

h('6. Qué pasa después')
p('Si pasas la prueba, se firma el contrato de prestación de servicios en las condiciones conversadas. Dentro del trabajo mensual, además de las historias, piezas y testimonios, **producirás anuncios a partir de los guiones de gerencia con estas mismas reglas**: ese material se suma al del videógrafo y se entrega listo para la pauta. La prueba es una muestra real de esa parte del trabajo.')
p('Dudas sobre el guion o la logística: por WhatsApp a gerencia antes de grabar. Lo que no esté escrito en el guion no se inventa: se pregunta.', GRIS, 9.5)

try:
    d.save(OUT); print('OK', OUT)
except PermissionError:
    d.save(OUT.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
print('\n'.join(guion))
