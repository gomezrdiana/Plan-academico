#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
import re

DARK=HexColor('#1a1a2e'); GRAY=HexColor('#555555'); WARN=HexColor('#fff3cd')
RED=HexColor('#dc3545'); REDBG=HexColor('#f8d7da')
w,h=letter
fn='B2/ENTREVISTA_ESTUDIANTES_B2_EDITABLE.pdf'
c=canvas.Canvas(fn,pagesize=letter)

def np():
    c.showPage(); return h-35

def draw_q(y, num, pregunta, tip, fname, critical=False):
    if y < 105:
        y = np()
    if critical:
        c.setFillColor(REDBG); c.rect(40, y-4, w-80, 13, fill=1, stroke=0)
    c.setFont('Helvetica-Bold', 9); c.setFillColor(RED if critical else DARK)
    c.drawString(42, y, f'{num}.')
    c.setFont('Helvetica-Bold', 8.5); c.setFillColor(black)
    words = pregunta.split(); lines=[]; line=''
    for word in words:
        test = line+' '+word if line else word
        if c.stringWidth(test,'Helvetica-Bold',8.5)<470: line=test
        else: lines.append(line); line=word
    if line: lines.append(line)
    for ln in lines:
        c.drawString(58, y, ln); y-=11
    c.setFont('Helvetica-Oblique',7); c.setFillColor(GRAY)
    tw = tip.split(); tlines=[]; tl=''
    for t in tw:
        test=tl+' '+t if tl else t
        if c.stringWidth(test,'Helvetica-Oblique',7)<470: tl=test
        else: tlines.append(tl); tl=t
    if tl: tlines.append(tl)
    for tln in tlines:
        c.drawString(58, y, tln); y-=9
    y-=2
    c.acroForm.textfield(name=fname, x=45, y=y-30, width=w-95, height=32, fontSize=8, borderWidth=0.5)
    y-=40
    return y

def section_header(y, text, color):
    if y < 130: y = np()
    c.setFillColor(color); c.rect(40,y-2,w-80,16,fill=1,stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold',9); c.drawString(48,y+1,text)
    return y-24

# PAGE 1
y=h-35
c.setFont('Helvetica-Bold',16); c.setFillColor(DARK)
c.drawString(40,y,'HEIIU B2 - Entrevista Individual')
y-=15; c.setFont('Helvetica',8); c.setFillColor(GRAY)
c.drawString(40,y,'20-25 min por estudiante | Lee las preguntas, anota respuestas | Confidencial')
y-=20

c.setFont('Helvetica-Bold',9); c.setFillColor(black)
c.drawString(40,y,'Estudiante:'); c.acroForm.textfield(name='est',x=110,y=y-3,width=140,height=14,fontSize=9,borderWidth=0.5)
c.drawString(270,y,'Fecha:'); c.acroForm.textfield(name='fecha',x=310,y=y-3,width=80,height=14,fontSize=9,borderWidth=0.5)
c.drawString(410,y,'Entrevistador:'); c.acroForm.textfield(name='entrev',x=490,y=y-3,width=80,height=14,fontSize=9,borderWidth=0.5)
y-=22

c.setFillColor(WARN); c.rect(40,y-18,w-80,20,fill=1,stroke=0)
c.setFillColor(black); c.setFont('Helvetica-Oblique',7)
c.drawString(48,y-5,'Di: "Hola [nombre]. Gracias por tomarte este tiempo. Esto es privado. No hay respuestas buenas ni malas. Quiero entender como te sientes."')
y-=28

# PARTE 1
y = section_header(y, 'PARTE 1 - EXPECTATIVAS vs REALIDAD', HexColor('#28a745'))
y = draw_q(y,1,'"Por que decidiste estudiar ingles en Heiiu? Que te atrajo?"',
    'Escucha: vino por el nativo? El metodo? Recomendacion? Precio? Que prometio la venta.','p1')
y = draw_q(y,2,'"Cuando empezaste, que esperabas lograr al terminar este nivel?"',
    'Hablar fluido? Pasar examen? Seguridad en entrevistas? Viajar?','p2')
y = draw_q(y,3,'"Sientes que lo estas logrando? Se honesto/a conmigo."',
    'CLAVE. No defiendas. Si dice "no": "Cuentame mas. Que sientes que te falta?"','p3')

# PARTE 2 - VERIFICACION FISICA (NEW)
y = section_header(y, 'PARTE 2 - VERIFICACION FISICA (CRITICO)', RED)
y = draw_q(y,4,'"Muestrame tu cuaderno. Cuantas paginas has escrito TU mismo/a en B2?"',
    'VERIFICAR VISUALMENTE. Cuaderno vacio = Project Workshop no pasa. Texto sin tachones/perfecto = sospecha IA. Anota # paginas.','p4',critical=True)
y = draw_q(y,5,'"La presentacion del Midterm la escribiste tu sola/o? Usaste ChatGPT o traductor?"',
    'Dejar silencio. Si dice "me ayudaron" preguntar "quien". Si dice "si yo" pedir que la repita de memoria 2 oraciones.','p5',critical=True)
y = draw_q(y,6,'"Callan ha leido tu escritura y te ha corregido en clase? Cuantas veces?"',
    'Project Workshop debe pasar 20-25 min en Clases 13-18 (6 clases). Si dice "nunca" o "1 vez" = no esta pasando.','p6',critical=True)

# PARTE 3 - CLASE Y PROFESOR
y = section_header(y, 'PARTE 3 - CLASE Y PROFESOR', HexColor('#007bff'))
y = draw_q(y,7,'"Describeme una clase tipica con Callan. Que hacen normalmente?"',
    'Compara con la guia. Anota diferencias. Esto te dice si Callan sigue la guia.','p7')
y = draw_q(y,8,'"Callan te corrige cuando HABLAS? Con que frecuencia?"',
    'Si dice "no mucho" o "casi nunca" = problema. Formato correcto: "No. Listen. [forma correcta]."','p8')
y = draw_q(y,9,'"En las ultimas 6 clases, cuantas veces han visto un video corto en YouTube y lo han repetido por partes?"',
    'ESTO ES SHADOWING. Debe pasar en Clases 12, 13, 14, 15, 16, 17 (6 veces). Si dice 1-2 = Callan lo salta.','p9',critical=True)
y = draw_q(y,10,'"Que actividades sientes que te ayudan mas? Y cuales NO aportan?"',
    'Si dice "Correct the Teacher no sirve" preguntar por que. Puede ser que Callan lo hace sin energia.','p10')

# PARTE 4 - FORMATO Y ACTIVIDADES (NEW)
y = section_header(y, 'PARTE 4 - FORMATO DE ACTIVIDADES', HexColor('#fd7e14'))
y = draw_q(y,11,'"Cuando hacen debate o roleplay, estan sentados en la silla o se paran y se mueven?"',
    'Si todo es sentado = falta kinestesia. Debates/roleplays deberian ser de pie, moviendose.','p11')
y = draw_q(y,12,'"Que preferirias: un roleplay sentados en pareja, o simular ir a una tienda de verdad, moverse y comprar?"',
    'Confirmar si quieren simulaciones inmersivas (tienda, aeropuerto, restaurante). Anota ideas textuales.','p12')
y = draw_q(y,13,'"Se sienten como adultos/jovenes o se sienten como ninos en el colegio?"',
    'B2 son jovenes-adultos. Si dicen "nino sentado" = aburrido, falta autonomia y movimiento.','p13')

# PARTE 5 - QUE QUIEREN
y = section_header(y, 'PARTE 5 - QUE QUIEREN', HexColor('#ffc107'))
y = draw_q(y,14,'"Si pudieras disenar la clase perfecta para ti, como seria?"',
    'Si dicen "solo conversar": "Sobre que?" Si dicen "mas gramatica": "Cual?" Anota textualmente.','p14')
y = draw_q(y,15,'"Necesitas el ingles para algo especifico? Trabajo? Viaje? Examen?"',
    'Personalizar las ultimas semanas a sus necesidades reales.','p15')
y = draw_q(y,16,'"Si pudieras cambiar UNA sola cosa de la clase, que seria?"',
    'La respuesta es ORO. Anota textualmente.','p16')

# PARTE 6 - CIERRE
y = section_header(y, 'PARTE 6 - CIERRE Y RETENCION', HexColor('#dc3545'))
y = draw_q(y,17,'"Volverias a estudiar con nosotros? Se honesto/a."',
    'Si "no": "Que tendria que cambiar?" Si "si": "Que nivel? Cuando?"','p17')
y = draw_q(y,18,'"Recomendarias Heiiu a un amigo? Por que si o por que no?"',
    'Net Promoter Score verbal. La respuesta te dice todo.','p18')

# Compensation
if y < 80: y = np()
c.setFillColor(HexColor('#d4edda')); c.rect(40,y-25,w-80,28,fill=1,stroke=0)
c.setFillColor(black); c.setFont('Helvetica-Oblique',7.5)
c.drawString(48,y-5,'Oferta si aplica: "Se que hubo cosas que pudimos hacer mejor. Te ofrezco [clase extra / descuento / sesion con Greg]"')
c.setFont('Helvetica',7.5); c.drawString(48,y-17,'Compensacion:')
c.acroForm.checkbox(name='comp_si',x=120,y=y-19,size=10,borderWidth=0.5); c.drawString(133,y-17,'Si')
c.acroForm.checkbox(name='comp_no',x=155,y=y-19,size=10,borderWidth=0.5); c.drawString(168,y-17,'No')
c.drawString(195,y-17,'Cual:'); c.acroForm.textfield(name='comp_cual',x=220,y=y-20,width=w-270,height=12,fontSize=7,borderWidth=0.5)
y-=38

# RESUMEN DIAGNOSTICO (EXPANDIDO)
if y < 210: y = np()
c.setFillColor(DARK); c.rect(40,y-2,w-80,18,fill=1,stroke=0)
c.setFillColor(white); c.setFont('Helvetica-Bold',10); c.drawString(48,y+1,'RESUMEN DIAGNOSTICO')
y-=26

# Checkboxes para hallazgos criticos
c.setFillColor(black); c.setFont('Helvetica-Bold',8)
c.drawString(45,y,'HALLAZGOS CRITICOS (marca lo que aplique):')
y-=14
for label, fname in [
    ('Cuaderno VACIO o con pocas paginas escritas por el estudiante','cb_cuad'),
    ('Uso ChatGPT/traductor para la presentacion del Midterm','cb_gpt'),
    ('Project Workshop NO esta pasando (0-1 correcciones de escritura)','cb_pw'),
    ('Shadowing solo ha ocurrido 1-2 veces (debe ser 6)','cb_sh'),
    ('Todas las actividades son sentadas, sin movimiento','cb_sent'),
    ('Callan NO corrige al hablar en tiempo real','cb_corr'),
]:
    if y<40: y=np()
    c.acroForm.checkbox(name=fname,x=50,y=y-2,size=10,borderWidth=0.5)
    c.setFont('Helvetica',8); c.drawString(65,y,label)
    y-=13

y-=6
for label, fname in [('Vino de (Heiiu / externo):','de_donde'),('Frustracion principal:','frustracion'),
    ('Que quiere el estudiante:','quiere'),('Se va o se queda:','va_queda'),('Accion a tomar:','accion')]:
    if y<50: y=np()
    c.setFillColor(black); c.setFont('Helvetica-Bold',8); c.drawString(45,y,label)
    c.acroForm.textfield(name=fname,x=230,y=y-3,width=w-280,height=13,fontSize=8,borderWidth=0.5)
    y-=19

y-=8; c.setFont('Helvetica',8)
c.drawString(40,y,'Firma coordinacion: _________________________')
c.drawString(320,y,'Fecha: ___/___/___')

c.save()
with open(fn,'rb') as f: pages=len(re.findall(rb'/Type\s*/Page[^s]',f.read()))
print(f'OK: {fn} - {pages} pag, editable con preguntas + tips + campos')
