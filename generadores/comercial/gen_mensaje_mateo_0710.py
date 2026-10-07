# -*- coding: utf-8 -*-
"""Mensaje a Mateo (arrendador) con la propuesta de pago, 07/10/2026. Salida en la carpeta EFORSALUD - MATEO MONROY."""
import re
from docx import Document
from docx.shared import Pt, RGBColor

d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(11)
GRIS = RGBColor(0x66, 0x66, 0x66)
def para(txt, after=8):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    for part in re.split(r'(\*\*[^*]+\*\*)', txt):
        if not part: continue
        r = p.add_run(part[2:-2] if part.startswith('**') else part); r.bold = part.startswith('**')

p = d.add_paragraph(); r = p.add_run('MENSAJE PARA MATEO — 07/10/2026 (copiar y pegar en WhatsApp)'); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = GRIS
para('Mateo, buenos días, y disculpa la demora: necesitaba tener los números claros antes de proponerte algo que pueda cumplir.')
para('**1 y 2. La fecha y lo mensual.** Te propongo vencimiento único de los dos pagarés el 31 de mayo de 2027, y mientras tanto un pago mensual por transferencia, en escalera: octubre y noviembre $4.000.000; diciembre y enero $4.500.000; febrero $5.000.000; desde marzo el canon completo. Cada mes se paga antes del 10 del mes siguiente: el de octubre, antes del 10 de noviembre. Los $3.000.000 de Eforsalud van completos todos los meses, y la diferencia del canon de Astra en esos cinco meses se suma al saldo de mayo. El 28 de febrero hacemos un corte: si no estoy al día con lo mensual, puedes dar por vencido todo desde ahí; y si fallo dos meses seguidos en cualquier momento, igual. Febrero es mi fecha de decisión, como te dije: si en febrero me toca vender, estoy dispuesta a hacerlo para quedar al día contigo y no quedarles mal, pero cualquier venta me requiere tiempo. Por eso el 31 de mayo tienes el pago completo.')
para('**3. El canon de Astra.** Tu cuadro dice IPC 5,1%, y $3.000.000 con 5,1% son $3.153.000, no $3.306.000. Te pido por favor que quede en $3.153.000 + IVA a partir de octubre. Y el pagaré de 2026 en los $29.754.000 tal como están en tu cuadro, para un total de $86.754.000 entre los dos pagarés.')
para('**4. El contrato** a dos años, hasta enero de 2028. Mi licencia está atada a esta dirección y necesito esa seguridad para seguir invirtiendo aquí.')
para('**5. Garantías.** Codeudor no tengo. Te doy mi firma, los pagos puntuales, el corte de febrero y la aceleración si fallo. Los $2.700.000 de tu papá te los llevo en efectivo cuando vayamos a la notaría y saldamos esa cuenta.')
para('Voy a darla toda para vender más y no cerrar. Créeme que aprecio mucho que tú y tu familia me sigan apoyando en este camino que llevo sola y con mucho esfuerzo, pero reitero que nunca va a ser mi intención que ustedes paguen por mi decisión: para mayo puedes contar con el pago total. Ahora me voy a dedicar a meterle todo y a ser muy exigente con las ventas, y espero poder pagarte más rápido ahora que mi atención va a estar ahí. Lo que te pido es un último salto de fe; gracias a ustedes he podido construir esto de a poquitos y lo valoro inmensamente.')
para('Revísalo y me cuentas. Gracias por la paciencia, Mateo.')

d.add_paragraph()
p = d.add_paragraph(); r = p.add_run('NOTAS PARA DIANA (no van en el mensaje): lo que debe quedar en el papel antes de firmar'); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = GRIS
for t in [
 '• Acuerdo de pago: "la diferencia entre el canon y el valor mensual acordado se acumula al saldo exigible el 31/05/2027, sin intereses, y su pago parcial no constituye mora ni causal de terminación mientras el acuerdo se cumpla". Abonos anticipados bajan el saldo sin penalidad.',
 '• Corte del 28/02: revisa los pagos de octubre a enero (el de febrero vence el 10 de marzo).',
 '• Contrato nuevo: cláusula 4 con pago "antes del 10 del mes siguiente"; parágrafo: los cánones ene-sep 2026 quedan solo en el pagaré 02 y no causan intereses ni terminación mientras se cumpla el acuerdo; 30 días para ponerse al día antes de que un atraso del canon corriente sea causal; duración hasta enero 2028 (o prórroga automática blindada).',
 '• Pagaré 02: $29.754.000 cerrado (sin "más IVA"); si el documento dice "más IVA" son $5.653.260 adicionales. Eforsalud: Diana quitó ese punto del mensaje (07/10); si él sube los $3.000.000, se pide en la notaría que quede congelado mientras dure el acuerdo. Pagaré 03: con concepto "saldo de servicios 2024-2025 y enero a septiembre de 2026" y acreedor con NIT. Ningún espacio en blanco; carta de instrucciones leída completa.',
 '• Línea de aval en blanco (sin codeudor). Nada de inmueble.',
 '• $2.700.000 en efectivo en la notaría contra recibo firmado por Mateo: "paz y salvo de la obligación con Fabricio Monroy".',
 '• Saldo estimado al 31/05/2027: $86.754.000 + ~$13.4M de diferencias de la escalera ≈ $100M. Si en febrero se decide vender, la venta debe estar en marcha ese mismo mes.',
]: para(t, after=4)

out = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\EFORSALUD - MATEO MONROY\MENSAJE_PROPUESTA_MATEO_2026-10-07.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
