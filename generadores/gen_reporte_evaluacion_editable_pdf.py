#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera REPORTE_EVALUACION_PROSPECTO_EDITABLE.pdf — PDF rellenable (AcroForm).
Mejoras v2:
- Eliminada opcion "necesita 2do test en 2 semanas"
- Sin simbolos < > (reemplazados por palabras "menos de" / "mas de")
- Layout corrido (sin tantos espacios en blanco)
- Referencias al Manual del Evaluador en cada seccion
- Mejor separacion entre labels y campos (no se solapan)
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas

DARK = HexColor('#1a1a2e')
GRAY = HexColor('#555555')
LIGHT = HexColor('#f0f0f0')
ACCENT = HexColor('#0066cc')
REF_COLOR = HexColor('#888888')

w, h = letter
M_L = 36
M_R = 36
W = w - M_L - M_R

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVAL_DIR = os.path.join(D, 'recursos', 'evaluaciones')
PDF_PATH = os.path.join(EVAL_DIR, 'REPORTE_EVALUACION_PROSPECTO_EDITABLE.pdf')

c = canvas.Canvas(PDF_PATH, pagesize=letter)
y = h - 30


def new_page():
    global y
    c.showPage()
    y = h - 30


def check_space(needed):
    global y
    if y - needed < 50:
        new_page()


def section_header(text, manual_ref=None):
    """Header de seccion + opcional referencia al Manual del Evaluador."""
    global y
    check_space(34 if manual_ref else 22)
    c.setFillColor(DARK)
    c.rect(M_L, y - 16, W, 20, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(M_L + 8, y - 11, text)
    y -= 22
    if manual_ref:
        c.setFillColor(REF_COLOR)
        c.setFont('Helvetica-Oblique', 7.5)
        c.drawString(M_L + 4, y, 'Ref: ' + manual_ref)
        y -= 10


def label(text, bold=True, size=9, gap=14):
    global y
    check_space(gap + 4)
    c.setFillColor(black)
    c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    c.drawString(M_L, y, text)
    y -= gap


def hint(text, gap=10):
    global y
    check_space(gap + 2)
    c.setFillColor(GRAY)
    c.setFont('Helvetica-Oblique', 7.5)
    c.drawString(M_L + 4, y, text)
    y -= gap


def textfield(name, width=None, height=14, multiline=False, gap_after=8):
    """Campo de texto editable. Se dibuja DEBAJO del cursor actual con gap suficiente
    para no solaparse con el label."""
    global y
    if width is None:
        width = W
    # Bajar 4px extra antes de dibujar para garantizar no solapamiento con texto previo
    y -= 4
    check_space(height + gap_after)
    c.acroForm.textfield(
        name=name,
        x=M_L, y=y - height,
        width=width, height=height,
        borderColor=GRAY,
        fillColor=LIGHT,
        textColor=black,
        forceBorder=True,
        fieldFlags='multiline' if multiline else None,
        fontSize=9,
    )
    y -= (height + gap_after)


def textfield_inline(name, label_text, label_w=160, field_w=None, height=14, gap_after=6):
    """Etiqueta + campo en mismo renglon."""
    global y
    if field_w is None:
        field_w = W - label_w - 4
    check_space(height + gap_after)
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 9)
    c.drawString(M_L, y - height + 4, label_text)
    c.acroForm.textfield(
        name=name,
        x=M_L + label_w, y=y - height,
        width=field_w, height=height,
        borderColor=GRAY,
        fillColor=LIGHT,
        textColor=black,
        forceBorder=True,
        fontSize=9,
    )
    y -= (height + gap_after)


def checkbox_line(name, text, indent=20, gap=13):
    global y
    check_space(gap)
    c.acroForm.checkbox(
        name=name,
        x=M_L + indent, y=y - 11,
        size=10,
        borderWidth=0.6,
        borderColor=GRAY,
        fillColor=white,
    )
    c.setFillColor(black)
    c.setFont('Helvetica', 9)
    c.drawString(M_L + indent + 16, y - 9, text)
    y -= gap


def big_quote_box(name, label_text, height=42):
    """Caja grande para frase textual del prospecto."""
    global y
    label(label_text, bold=True, size=9, gap=12)
    y -= 4  # extra padding para no solapar
    check_space(height + 8)
    c.acroForm.textfield(
        name=name,
        x=M_L + 8, y=y - height,
        width=W - 16, height=height,
        borderColor=ACCENT,
        fillColor=LIGHT,
        textColor=black,
        forceBorder=True,
        fieldFlags='multiline',
        fontSize=9,
    )
    y -= (height + 8)


def title_block(title, subtitle):
    global y
    c.setFillColor(DARK)
    c.setFont('Helvetica-Bold', 16)
    c.drawCentredString(w/2, y - 4, title)
    y -= 22
    c.setFillColor(GRAY)
    c.setFont('Helvetica-Oblique', 8.5)
    lines = []
    words = subtitle.split()
    line = ''
    for word in words:
        if len(line + ' ' + word) > 105:
            lines.append(line)
            line = word
        else:
            line = (line + ' ' + word).strip()
    if line:
        lines.append(line)
    for ln in lines:
        c.drawCentredString(w/2, y, ln)
        y -= 10
    y -= 8


# =====================================================================
# PÁGINA 1
# =====================================================================

title_block(
    'REPORTE DE EVALUACIÓN — PROSPECTO HEIIU',
    'Llenar inmediatamente al cerrar la evaluación. Tiempo: 3 a 5 min máximo. '
    'Entregable obligatorio para coordinación y asesor comercial. '
    'Sin este reporte, el asesor improvisa y el cliente se enfría.'
)

# SECCIÓN 1
section_header('1. DATOS BÁSICOS',
               manual_ref='Manual del Evaluador, Momento 1 (Preparación) — briefing recibido del asesor')

textfield_inline('nombre', 'Nombre completo:', label_w=110)
textfield_inline('edad', 'Edad aproximada:', label_w=110, field_w=80)
textfield_inline('profesion', 'Profesión / ocupación:', label_w=110)
textfield_inline('fecha', 'Fecha (DD/MM/YYYY):', label_w=110, field_w=120)
textfield_inline('hora', 'Hora inicio / fin:', label_w=110, field_w=180)

label('Modalidad:', bold=True, size=9, gap=12)
checkbox_line('mod_presencial', 'Presencial')
checkbox_line('mod_virtual', 'Virtual (Google Meet)')

textfield_inline('evaluadora', 'Evaluadora:', label_w=110)
textfield_inline('asesor', 'Asesor responsable:', label_w=110)

# SECCIÓN 2
section_header('2. DIAGNÓSTICO DE NIVEL',
               manual_ref='Manual del Evaluador, Momento 4 (Devolución) — paso VISIÓN')

label('Nivel diagnosticado (marcar UNO):', size=9, gap=12)
checkbox_line('nivel_a1', 'A1')
checkbox_line('nivel_a2', 'A2')
checkbox_line('nivel_b1', 'B1')
checkbox_line('nivel_b2', 'B2')

label('Certeza del diagnóstico:', size=9, gap=12)
checkbox_line('cert_100', '100% claro')
checkbox_line('cert_80', '80% — está al borde de subir/bajar')

label('Si está al borde, ¿hacia qué dirección?:', size=9, gap=12)
checkbox_line('borde_sube', 'Sube')
checkbox_line('borde_baja', 'Baja')

label('Programa recomendado:', size=9, gap=12)
checkbox_line('prog_a1n', 'A1 nocturno (2h)')
checkbox_line('prog_a2n', 'A2 nocturno (2h)')
checkbox_line('prog_a24h', 'A2 4h intensivo mañana')
checkbox_line('prog_b1', 'B1 (1h50m por 2 bloques)')
checkbox_line('prog_b2', 'B2 (4h)')
textfield_inline('prog_otro', 'Otro:', label_w=60)

# =====================================================================
# PÁGINA 2
# =====================================================================

new_page()

# SECCIÓN 3
section_header('3. DOS FORTALEZAS CONCRETAS',
               manual_ref='Manual del Evaluador, Momento 4 (Devolución) — paso VISIÓN')
hint('Específico, no genérico. Ej: "usa correctamente phrasal verbs como pick up y figure out".')

label('Fortaleza 1:', size=9, gap=12)
textfield('fort1_desc', height=22, multiline=True)
big_quote_box('fort1_cita', 'Cita textual o ejemplo escuchado (si lo hubo):', height=30)

label('Fortaleza 2:', size=9, gap=12)
textfield('fort2_desc', height=22, multiline=True)
big_quote_box('fort2_cita', 'Cita textual o ejemplo escuchado (si lo hubo):', height=30)

# SECCIÓN 4
section_header('4. UN PUNTO DE TRABAJO ESPECÍFICO',
               manual_ref='Manual del Evaluador, Momento 4 (Devolución) — paso VISIÓN')
hint('Lo que más se traba. Ej: "confunde Past Simple con Present Perfect".')

label('Punto de trabajo:', size=9, gap=12)
textfield('punto_trabajo', height=26, multiline=True)

label('¿Cómo lo va a resolver el programa? (1 línea):', size=9, gap=12)
textfield('punto_solucion', height=18, multiline=True)

# SECCIÓN 5
section_header('5. MOTIVACIÓN PROFUNDA DETECTADA',
               manual_ref='Manual del Evaluador, Momento 1 (Preparación) y Momento 3 (Conexión profesional)')

label('¿Qué es lo que MÁS quiere lograr con el inglés?', size=9, gap=12)
checkbox_line('mot_trabajo', 'Trabajo (ascenso / nuevo puesto / cambio de empresa)')
checkbox_line('mot_viaje', 'Viaje (vacaciones / migración / intercambio)')
checkbox_line('mot_familia', 'Familia (hijos / pareja extranjera / nietos)')
checkbox_line('mot_personal', 'Personal (autorrealización / superar trauma con el inglés)')
checkbox_line('mot_negocio', 'Negocio propio (clientes internacionales / marca personal)')
checkbox_line('mot_estudios', 'Estudios (maestría / certificación profesional)')
textfield_inline('mot_otra', 'Otra:', label_w=50)

big_quote_box('mot_detalle', 'Detalle específico (qué dijo el prospecto que dejó claro su motivación):', height=40)

# =====================================================================
# PÁGINA 3
# =====================================================================

new_page()

# SECCIÓN 6
section_header('6. LECTURA EMOCIONAL',
               manual_ref='Manual del Evaluador, Momento 4 (Devolución) — paso INVITACIÓN')

label('¿Cómo se siente el prospecto al cerrar la evaluación?', size=9, gap=12)
checkbox_line('le_caliente', 'CALIENTE — listo para cerrar. Mostró emoción y preguntas sobre cómo arrancar.')
checkbox_line('le_tibio', 'TIBIO — interesado pero con duda específica.')
checkbox_line('le_frio', 'FRÍO — desinflado o desconfiado. Necesita 2do contacto.')

label('Si TIBIO, ¿cuál es la duda específica?', size=9, gap=12)
checkbox_line('duda_costo', 'Costo / presupuesto')
checkbox_line('duda_tiempo', 'Tiempo / agenda')
checkbox_line('duda_metodo', 'Método / si va a funcionar')
checkbox_line('duda_familia', 'Decisión familiar (necesita consultar pareja/papás)')
textfield_inline('duda_otra', 'Otra:', label_w=50)

label('¿Por qué tu lectura emocional? (1-2 frases):', size=9, gap=12)
textfield('le_porque', height=26, multiline=True)

# SECCIÓN 7
section_header('7. COMPROMISO TEMPORAL HECHO AL PROSPECTO',
               manual_ref='Manual del Evaluador, Momento 4 (INVITACIÓN) y Momento 5 (Handoff)')
hint('Esta es la promesa que cerraste. Si el asesor no cumple, perdiste el cierre.')

label('Le dije al prospecto que:', size=9, gap=12)
checkbox_line('ct_hoy', 'El asesor lo contacta HOY antes de las (anotar hora abajo)')
checkbox_line('ct_horas', 'El asesor lo contacta en las próximas X horas (anotar abajo)')
checkbox_line('ct_mananah', 'El asesor lo contacta MAÑANA antes de las (anotar abajo)')
checkbox_line('ct_inmediato', '(Solo presencial) El asesor entró al salón inmediatamente')

textfield_inline('ct_hora', 'Hora exacta acordada:', label_w=140, field_w=200)

label('Canal de contacto acordado:', size=9, gap=12)
checkbox_line('canal_wsp', 'WhatsApp')
checkbox_line('canal_llamada', 'Llamada telefónica')
checkbox_line('canal_pres', 'Cita presencial')
checkbox_line('canal_video', 'Videollamada')

# =====================================================================
# PÁGINA 4
# =====================================================================

new_page()

# SECCIÓN 8
section_header('8. FRASES TEXTUALES (oro puro para el asesor)',
               manual_ref='Manual del Evaluador, Momento 3 (Durante la prueba) — anotar lo importante')

big_quote_box('frase_compra', 'Frase que indica INTENCIÓN DE COMPRA (si la dijo):', height=40)
hint('Ej: "necesito tener inglés en 6 meses", "estoy listo para invertir en mí".')

big_quote_box('frase_objecion', 'Frase que indica OBJECIÓN o DUDA (si la dijo):', height=40)
hint('Ej: "el próximo mes lo veo", "tengo que hablar con mi esposa", "me parece caro".')

# SECCIÓN 9
section_header('9. BRIEFING RÁPIDO PARA EL ASESOR (2-3 líneas)',
               manual_ref='Manual del Evaluador, Momento 5 (Handoff) — briefing al asesor')
hint('Resumen ejecutivo. Lo primero que el asesor lee antes de contactar.')

textfield('briefing', height=46, multiline=True)

# SECCIÓN 10
section_header('10. ANCLAS PARA EL PITCH DEL ASESOR',
               manual_ref='Manual del Evaluador, Momento 5 (Handoff) — info que usa el asesor para personalizar')
hint('2-3 conexiones específicas para personalizar el contacto. NO genérico.')

label('Ancla 1 (relacionada con su profesión / contexto):', size=9, gap=12)
textfield('ancla1', height=22, multiline=True)
hint('Ej: "Trabaja en marketing → mencionarle que B2 abre roles bilingües internacionales".')

label('Ancla 2 (relacionada con su motivación profunda):', size=9, gap=12)
textfield('ancla2', height=22, multiline=True)
hint('Ej: "Quiere ir a Canadá en 18 meses → mostrarle que B2 deja con nivel para IELTS".')

label('Ancla 3 (relacionada con sus fortalezas detectadas):', size=9, gap=12)
textfield('ancla3', height=22, multiline=True)
hint('Ej: "Tiene buena pronunciación → resaltar que destaca más rápido en producción oral".')

# =====================================================================
# PÁGINA 5
# =====================================================================

new_page()

# SECCIÓN 11
section_header('11. RECOMENDACIÓN URGENCIA',
               manual_ref='Manual del Evaluador, Momento 5 (Handoff) — qué tan rápido contactar')

label('¿Qué tan rápido debe contactar el asesor?', size=9, gap=12)
checkbox_line('urg_inmediato', 'INMEDIATO (menos de 30 min) — prospecto caliente, momentum alto')
checkbox_line('urg_hoy', 'HOY (mismo día) — interés real, pero no urgente')
checkbox_line('urg_24h', '24 HORAS (mañana) — tibio, dejar que procese')
checkbox_line('urg_48h', '48 HORAS o más — frío, necesita re-enganche con valor agregado')

label('Si recomendaste contacto en más de 24 horas, ¿por qué?', size=9, gap=12)
textfield('urg_porque', height=20, multiline=True)

# SECCIÓN 12
section_header('12. NOTAS LIBRES',
               manual_ref='—')
hint('Patrones detectados, alertas, contexto familiar/profesional importante, etc.')

textfield('notas', height=70, multiline=True)

# CIERRE
section_header('CIERRE DEL REPORTE',
               manual_ref='Llenar al final, antes de enviar al asesor por WhatsApp/email')

textfield_inline('hora_termino', 'Hora en que terminé este reporte:', label_w=200)
textfield_inline('hora_envio', 'Hora en que envié al asesor:', label_w=200)

hint('Meta: llenar y enviar en menos de 5 min. Más de 30 min = información se diluye.', gap=14)

textfield_inline('firma', 'Firma evaluadora:', label_w=110)

# =====================================================================
# PÁGINA 6 — Instrucciones (NO editable)
# =====================================================================

new_page()

section_header('INSTRUCCIONES PARA EL ASESOR (no editable, solo lectura)',
               manual_ref='Aplicar después de recibir este reporte de la evaluadora')

c.setFillColor(black)
c.setFont('Helvetica', 9)
asesor_inst = [
    '1. Léelo COMPLETO antes de contactar. No improvises.',
    '2. Usa las anclas (Sección 10) para personalizar tu primer mensaje. NO mensaje genérico.',
    '3. Cumple el compromiso temporal (Sección 7). Sin excusas.',
    '4. Si el prospecto es CALIENTE: llama, no escribas. Cierre se hace por voz, no por chat.',
    '5. Si es TIBIO con duda específica: trabaja esa duda directamente.',
    '6. Si es FRÍO: 2do contacto en 2-3 días con valor agregado (artículo, video, testimonio).',
]
for inst in asesor_inst:
    check_space(14)
    c.drawString(M_L + 4, y, inst)
    y -= 14

y -= 6
c.setFont('Helvetica-BoldOblique', 9)
c.setFillColor(DARK)
c.drawString(M_L, y, 'Cierres reales = compromiso del asesor cumplido + información específica usada + decisión hoy.')
y -= 24

section_header('INSTRUCCIONES PARA COORDINACIÓN (archivado)',
               manual_ref='Trazabilidad y revisión de conversion rate')

c.setFillColor(black)
c.setFont('Helvetica', 9)
coord_inst = [
    '• Archivar TODOS los reportes (físicos o digitales) por mes.',
    '• Cada lunes: revisar reportes de la semana anterior y verificar conversion rate.',
    '   (cuántos cerraron / cuántos se evaluaron)',
    '• Si conversion menor a 30 por ciento: revisar dónde se rompe (handoff tardío,',
    '   mensaje genérico, no se trabajó la objeción).',
    '• Si un asesor tiene conversion menor a 20 por ciento en 5 o más evaluaciones:',
    '   revisión 1-a-1 con la gerente comercial.',
]
for inst in coord_inst:
    check_space(14)
    c.drawString(M_L + 4, y, inst)
    y -= 14

# Footer
y = 30
c.setFillColor(GRAY)
c.setFont('Helvetica-Oblique', 7)
c.drawString(M_L, y, 'PROPIEDAD INTELECTUAL DE HEIIU — USO INTERNO. NO compartir fuera del equipo de evaluación y coordinación.')

c.save()
print(f'OK: {PDF_PATH}')
