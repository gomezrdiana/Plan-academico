#!/usr/bin/env python3
"""Genera GUIA EVALUADORA editable (PDF con form fields) en ES y EN.
Combina: ladder A1->B2 + activador competitivo + reporte para asesor.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
import os
import re

DARK = HexColor('#1a1a2e')
GRAY = HexColor('#555555')
GREEN = HexColor('#28a745')
BLUE = HexColor('#007bff')
YELLOW = HexColor('#d4a017')
ORANGE = HexColor('#fd7e14')
RED = HexColor('#dc3545')
WARN = HexColor('#fff3cd')
LIGHTBOX = HexColor('#f0f0f0')
ACTIVATOR_BG = HexColor('#e8f4f8')
w, h = letter

D = os.path.dirname(os.path.abspath(__file__))
EVAL_DIR = os.path.join(D, 'recursos', 'evaluaciones')


# =========================================================================
# DATOS DEL TEST (mismas preguntas en ambos idiomas — preguntas siempre EN)
# =========================================================================

A1_QUESTIONS = [
    ("So, what do you do? Do you work or study?", "Present simple do/does"),
    ("Does your mom work too, or stay home?", "Does + 3rd person"),
    ("What time do you usually wake up?", "What time + present simple"),
    ("Where do you eat lunch?", "Where + present simple"),
    ("Do you play any sports?", "Do you + verb"),
    ("Can you cook?", "Can/can't + short answer"),
    ("What can you cook? Best dish?", "Can + vocab"),
    ("If you feel sick, should you go to work?", "Should"),
    ("What will you do this weekend?", "Will/won't"),
    ("How much does a coffee cost here?", "How much + numbers"),
    ("Tell me about your family. Brothers/sisters?", "Pronouns + verb-s"),
    ("Where should I go if I visit your city?", "Should (advice)"),
]

A2_QUESTIONS = [
    ("Plans for the weekend? What are you going to do?", "Going to"),
    ("Anything you might do but you're not sure?", "Might"),
    ("Concert at 8pm Saturday. How tell a friend?", "Present simple for schedules"),
    ("If you have free time tomorrow, what will you do?", "First conditional"),
    ("If you had a million dollars, what would you do?", "Second conditional"),
    ("Have you ever traveled to another country?", "Present perfect"),
    ("What were you doing yesterday at 3pm?", "Past continuous"),
    ("Were you doing something when someone interrupted?", "Past cont + when/while"),
    ("What do you think about English?", "'That' for opinions"),
    ("When's your birthday? Today's date?", "Ordinal numbers"),
    ("If it rains during your vacation, what will you do?", "During/while + 1st cond"),
]

B1_QUESTIONS = [
    ("Tell me about a trip. Where, what happened, would you go back?", "Storytelling, multi-tense"),
    ("Social media: good or bad?", "Opinions + reasons"),
    ("Describe your best friend - looks AND personality.", "Detailed description"),
    ("What had you planned before deciding to study English here?", "Past perfect"),
    ("If you could change one thing about your city, what + why?", "2nd cond + reasoning"),
    ("Your typical day - morning to night, full detail.", "Sustained 2 min + vocab"),
    ("Plans for the next 5 years?", "Varied future forms"),
    ("Explain how to make your favorite food. Step by step.", "Sequencing + vocab"),
    ("What have you been doing lately that you enjoy?", "Present perfect continuous"),
]

B2_QUESTIONS = [
    ("You like traveling, don't you?", "Question tags"),
    ("City or countryside? Or both?", "Either/neither/both"),
    ("If you hadn't studied English young, how different would life be?", "3rd/mixed conditional"),
    ("Tell me about a famous building. When built? Used for?", "Passive voice"),
    ("Recent conversation - what did the other person say?", "Reported speech"),
    ("Gotten anything done recently? Haircut, repair?", "Causative"),
    ("Tell me about someone who influenced you, whose advice you follow.", "Relative clauses"),
    ("Should everyone learn a 2nd language? Anywhere not necessary?", "Indefinite pronouns"),
    ("DEBATE: AI will replace teachers. Argue 3+ min.", "Sustained argumentation"),
    ("Something that went wrong but was a blessing in disguise.", "Complex narrative + vocab"),
]


# =========================================================================
# TEXTOS POR IDIOMA
# =========================================================================

TEXTS = {
    'es': {
        'title': 'GUIA EVALUADORA - Diagnostico + Activacion Competitiva',
        'subtitle': 'Documento unico: guion + reporte. Llenar durante y al cierre. Entregar al asesor.',
        'sec0': 'SECCION 0 - DATOS DE LA SESION',
        'prospect': 'Prospecto:', 'date': 'Fecha:', 'evaluator': 'Evaluadora:',
        'age': 'Edad:', 'profession': 'Profesion:',
        'start': 'Inicio:', 'end': 'Fin:',
        'modality': 'Modalidad:', 'inperson': 'Presencial', 'virtual': 'Virtual',
        'advisor': 'Asesor:',
        'sec1_title': 'SECCION 1 - FILOSOFIA DEL ROL (leer ANTES)',
        'philosophy': ("Tu trabajo NO es probar nivel. Es abrir la primera puerta de Heiiu. "
                       "Hoy haces 2 cosas: (1) DIAGNOSTICAR el nivel del prospecto, "
                       "(2) ACTIVAR su drive competitivo plantando frases en momentos clave. "
                       "Heiiu busca estudiantes competitivos consigo mismos, que ven el ingles "
                       "como herramienta para crecer. Tu sesion filtra y activa ese perfil."),
        'sec2_title': 'SECCION 2 - APERTURA (30 seg, script literal)',
        'opening': ('"Hola [nombre]. Esto NO es un examen - es una conversacion para ver donde '
                    'estas HOY con el ingles. En 3 a 6 meses te vas a reir de este momento. '
                    'Empezamos relajado y vamos subiendo. Listo?"'),
        'opening_en': ('EN alternative: "Hey [name], this isn\'t a test - it\'s a chat to see '
                       'where you are today. In 3-6 months you\'ll laugh at this moment. Cool?"'),
        'level_a1': 'NIVEL A1 (Min 0-5) - Presente simple, modales basicos',
        'level_a2': 'NIVEL A2 (Min 5-12) - Future forms, condicionales, perfect',
        'level_b1': 'NIVEL B1 (Min 12-20) - Sostiene conversacion, narrativa, detalle',
        'level_b2': 'NIVEL B2 (Min 20-28) - Gramatica avanzada, argumentacion',
        'q_col': 'Pregunta (en INGLES al prospecto)', 'struct_col': 'Estructura',
        'pass': 'PASA', 'fail': 'FALLA',
        'total_a1': 'Total A1 correctas: ___ / 12',
        'total_a2': 'Total A2 correctas: ___ / 11',
        'total_b1': 'Total B1 correctas: ___ / 9',
        'total_b2': 'Total B2 correctas: ___ / 10',
        'activator_a1_title': 'ACTIVADOR A1 (frases para plantar)',
        'activator_a1_pass': ('Pasa: "Acabas de pasar A1. Hay 3 niveles mas. La mayoria se queda en A2. Veamos."'),
        'activator_a1_fail': ('Falla: "Esa estructura es de las que se trabajan a cada rato aqui. '
                              'En 30 dias desaparece como error - ese es el GAP que cerramos."'),
        'activator_a1_strength': ('Fortaleza: "Lo que acabas de decir tiene base solida. Vamos."'),
        'activator_a2_title': 'ACTIVADOR A2',
        'activator_a2_pass': ('Pasa: "Estas en territorio B1. Pocos llegan aca sin escuela. De donde sacaste lo que sabes?"'),
        'activator_a2_fail': ('Falla B1-bridge: "Eso ya es B1. Tienes la base, te falta practica. '
                              'En 6-8 semanas aqui esa estructura saldria sin pensarlo."'),
        'activator_b1_title': 'ACTIVADOR B1',
        'activator_b1_pass': ('Pasa: "Vas a B2. Cuando llegues aca tienes opciones laborales, viajes, '
                              'decisiones de vida que no tendrias. Que te frena?"'),
        'activator_b2_title': 'ACTIVADOR B2',
        'activator_b2_pass': ('Pasa: "Estas cerca de C1. Estudios afuera, IELTS sin terror, '
                              'trabajos internacionales reales. Sabias que estabas tan cerca?"'),
        'decision_a1': 'DECISION A1: PASA (6+/12) -> sigue a A2  |  FALLA -> place A1, parar',
        'decision_a2': 'DECISION A2: PASA (7+/11) -> sigue a B1  |  FALLA -> place A2, parar',
        'decision_b1': 'DECISION B1: PASA (6+/9 + sostiene) -> sigue a B2  |  FALLA -> place B1, parar',
        'decision_b2': 'DECISION B2: B2+ (7+/10 fluido) o B2',
        'cierre_title': 'SECCION 4 - CIERRE ACTIVADOR (3 min al final - script literal)',
        'cierre_text': ('"Esto es lo que veo. Tu nivel HOY es [X]. La distancia hasta [siguiente] '
                        'son [Y estructuras]. Te voy a ser honesta: los estudiantes que cierran ese '
                        'gap son los que vienen con disciplina real, son competitivos consigo mismos, '
                        'no con otros. Hablan el mismo idioma del mundo porque lo trabajan diariamente. '
                        'Eres de esos?"  PAUSA. Escucha respuesta.'),
        'sec5_title': 'SECCION 5 - LECTURA DE COMPETITIVIDAD (tu marcas)',
        'comp_high': 'ALTA - se prendio con stakes, hizo preguntas sobre tiempo/metodo, ambicion visible',
        'comp_med': 'MEDIA - interesado pero sin impetu propio (asesor necesita empujar)',
        'comp_low': 'BAJA - apatico o resistente al frame de crecimiento',
        'hook_label': 'Hook que mas resono (frase que cambio su tono):',
        'sec6_title': 'SECCION 6 - DIAGNOSTICO FINAL',
        'final_level': 'Nivel oficial:',
        'certainty': 'Certeza:', 'cert_clear': '100% claro', 'cert_border': '80% borde',
        'cert_retest': '60% re-test 2 semanas',
        'program': 'Programa recomendado:',
        'sec7_title': 'SECCION 7 - DOS FORTALEZAS CONCRETAS (con cita textual)',
        'strength1': 'Fortaleza 1:', 'strength2': 'Fortaleza 2:',
        'quote': 'Cita:',
        'sec8_title': 'SECCION 8 - UN PUNTO DE TRABAJO ESPECIFICO',
        'work_point': 'Punto:', 'how_solved': 'Como lo resuelve el programa (1 linea):',
        'sec9_title': 'SECCION 9 - MOTIVACION PROFUNDA',
        'mot_work': 'Trabajo (ascenso/cambio)', 'mot_travel': 'Viaje',
        'mot_family': 'Familia', 'mot_personal': 'Personal',
        'mot_business': 'Negocio propio', 'mot_studies': 'Estudios',
        'mot_other': 'Otra:',
        'mot_detail': 'Detalle (que dijo el prospecto):',
        'sec10_title': 'SECCION 10 - LECTURA EMOCIONAL FINAL',
        'hot': 'CALIENTE - listo para cerrar, hizo preguntas sobre arrancar',
        'warm': 'TIBIO - interesado con duda especifica:',
        'doubt_cost': 'Costo', 'doubt_time': 'Tiempo', 'doubt_method': 'Metodo',
        'doubt_family': 'Decision familiar', 'doubt_other': 'Otra:',
        'cold': 'FRIO - desinflado, necesita 2do contacto',
        'why_emotional': 'Por que tu lectura emocional (1-2 frases):',
        'sec11_title': 'SECCION 11 - COMPROMISO TEMPORAL CON EL PROSPECTO',
        'commit_today': 'Asesor contacta HOY antes de:',
        'commit_hours': 'En las proximas ___ horas (antes de):',
        'commit_tomorrow': 'Manana antes de:',
        'commit_immediately': 'Asesor entra inmediatamente (presencial)',
        'channel': 'Canal:', 'wa': 'WhatsApp', 'call': 'Llamada',
        'inperson_appt': 'Cita presencial', 'video': 'Videollamada',
        'sec12_title': 'SECCION 12 - FRASES TEXTUALES (oro para el asesor)',
        'intent_label': 'Frase de INTENCION DE COMPRA (si la dijo):',
        'objection_label': 'Frase de OBJECION o DUDA (si la dijo):',
        'sec13_title': 'SECCION 13 - BRIEFING RAPIDO PARA EL ASESOR (2-3 lineas)',
        'sec14_title': 'SECCION 14 - ANCLAS PARA EL PITCH DEL ASESOR',
        'anchor1': 'Ancla 1 (profesion/contexto):',
        'anchor2': 'Ancla 2 (motivacion profunda):',
        'anchor3': 'Ancla 3 (fortaleza detectada):',
        'sec15_title': 'SECCION 15 - URGENCIA',
        'urg_immediate': 'INMEDIATO (<30 min) - caliente + competitividad alta',
        'urg_today': 'HOY (mismo dia) - interes real',
        'urg_24h': '24 HORAS - tibio',
        'urg_48h': '48 HORAS+ - frio, re-enganche',
        'urg_why': 'Si >24h, por que:',
        'sec16_title': 'SECCION 16 - NOTAS LIBRES',
        'errors_title': 'ERRORES QUE NO HACER (recordatorio)',
        'errors': ('No le digas el nivel exacto al prospecto (coordinacion lo hace) | '
                   'No hables de precios | No compares con otros estudiantes | '
                   'No prometas tiempos | No corrijas durante el test'),
        'closing': 'CIERRE',
        'time_finished': 'Hora terminada reporte:', 'time_sent': 'Hora enviado al asesor:',
        'signature': 'Firma evaluadora:',
    },
    'en': {
        'title': "EVALUATOR'S GUIDE - Diagnosis + Competitive Activation",
        'subtitle': 'Single document: script + report. Fill during + at close. Hand to advisor.',
        'sec0': 'SECTION 0 - SESSION DATA',
        'prospect': 'Prospect:', 'date': 'Date:', 'evaluator': 'Evaluator:',
        'age': 'Age:', 'profession': 'Profession:',
        'start': 'Start:', 'end': 'End:',
        'modality': 'Format:', 'inperson': 'In-person', 'virtual': 'Virtual',
        'advisor': 'Advisor:',
        'sec1_title': "SECTION 1 - THE ROLE'S PHILOSOPHY (read BEFORE)",
        'philosophy': ("Your job is NOT to test level. It's to open Heiiu's first door. "
                       "Today you do 2 things: (1) DIAGNOSE the prospect's level, "
                       "(2) ACTIVATE their competitive drive by planting phrases at key moments. "
                       "Heiiu seeks students competitive with themselves, who see English as a "
                       "tool to grow. Your session filters and activates that profile."),
        'sec2_title': 'SECTION 2 - OPENING (30 sec, literal script)',
        'opening': ('"Hey [name], this isn\'t a test - it\'s a chat to see where you are today. '
                    'In 3-6 months you\'ll laugh at this moment. We start relaxed and go up. Cool?"'),
        'opening_en': ('ES alternative: "Hola [nombre], esto NO es un examen - es una conversacion '
                       'para ver donde estas HOY. En 3-6 meses te vas a reir. Listo?"'),
        'level_a1': 'LEVEL A1 (Min 0-5) - Present simple, basic modals',
        'level_a2': 'LEVEL A2 (Min 5-12) - Future forms, conditionals, perfect',
        'level_b1': 'LEVEL B1 (Min 12-20) - Sustains conversation, narrative, detail',
        'level_b2': 'LEVEL B2 (Min 20-28) - Advanced grammar, argumentation',
        'q_col': 'Question (in ENGLISH to prospect)', 'struct_col': 'Structure',
        'pass': 'PASS', 'fail': 'FAIL',
        'total_a1': 'Total A1 correct: ___ / 12',
        'total_a2': 'Total A2 correct: ___ / 11',
        'total_b1': 'Total B1 correct: ___ / 9',
        'total_b2': 'Total B2 correct: ___ / 10',
        'activator_a1_title': 'A1 ACTIVATOR (phrases to plant)',
        'activator_a1_pass': ('Pass: "You just passed A1. There are 3 more levels. Most people stay at A2. Let\'s see."'),
        'activator_a1_fail': ('Fail: "That structure is one we work on a lot here. In 30 days '
                              'that error disappears - that\'s exactly the GAP we close."'),
        'activator_a1_strength': ('Strength: "What you just said has solid base. Let\'s go."'),
        'activator_a2_title': 'A2 ACTIVATOR',
        'activator_a2_pass': ('Pass: "You\'re at B1 territory. Few people get here without school. Where\'d you learn what you know?"'),
        'activator_a2_fail': ('Fail B1-bridge: "That\'s already B1. You have the base, you need '
                              'focused practice. In 6-8 weeks here that structure flows naturally."'),
        'activator_b1_title': 'B1 ACTIVATOR',
        'activator_b1_pass': ('Pass: "You\'re going to B2. When you get here you have job options, '
                              'travel, life decisions you wouldn\'t have. What\'s holding you back?"'),
        'activator_b2_title': 'B2 ACTIVATOR',
        'activator_b2_pass': ('Pass: "You\'re close to C1. Study abroad, IELTS without panic, '
                              'real international jobs. Did you know you were this close?"'),
        'decision_a1': 'A1 DECISION: PASS (6+/12) -> continue A2  |  FAIL -> place A1, stop',
        'decision_a2': 'A2 DECISION: PASS (7+/11) -> continue B1  |  FAIL -> place A2, stop',
        'decision_b1': 'B1 DECISION: PASS (6+/9 + sustains) -> continue B2  |  FAIL -> place B1, stop',
        'decision_b2': 'B2 DECISION: B2+ (7+/10 fluent) or B2',
        'cierre_title': 'SECTION 4 - ACTIVATOR CLOSING (3 min - literal script)',
        'cierre_text': ('"Here\'s what I see. Your level TODAY is [X]. The distance to [next level] '
                        'is [Y structures]. I\'ll be honest: students who close that gap are the ones '
                        'who come with real discipline, competitive with themselves not with others. '
                        'They speak the global language because they work it daily, not because they\'re gifted. '
                        'Are you one of those?"  PAUSE. Listen.'),
        'sec5_title': 'SECTION 5 - COMPETITIVENESS READING (you mark)',
        'comp_high': 'HIGH - fired up by stakes, asked about time/method, visible ambition',
        'comp_med': 'MEDIUM - interested but no self-driving impulse (advisor must push)',
        'comp_low': 'LOW - apathetic or resistant to growth frame',
        'hook_label': 'Hook that resonated most (phrase that shifted their tone):',
        'sec6_title': 'SECTION 6 - FINAL DIAGNOSIS',
        'final_level': 'Official level:',
        'certainty': 'Certainty:', 'cert_clear': '100% clear', 'cert_border': '80% borderline',
        'cert_retest': '60% re-test 2 weeks',
        'program': 'Recommended program:',
        'sec7_title': 'SECTION 7 - TWO CONCRETE STRENGTHS (with literal quote)',
        'strength1': 'Strength 1:', 'strength2': 'Strength 2:',
        'quote': 'Quote:',
        'sec8_title': 'SECTION 8 - ONE SPECIFIC WORK POINT',
        'work_point': 'Point:', 'how_solved': 'How program solves it (1 line):',
        'sec9_title': 'SECTION 9 - DEEP MOTIVATION',
        'mot_work': 'Work (promotion/change)', 'mot_travel': 'Travel',
        'mot_family': 'Family', 'mot_personal': 'Personal',
        'mot_business': 'Own business', 'mot_studies': 'Studies',
        'mot_other': 'Other:',
        'mot_detail': 'Detail (what the prospect said):',
        'sec10_title': 'SECTION 10 - FINAL EMOTIONAL READING',
        'hot': 'HOT - ready to close, asked about starting',
        'warm': 'WARM - interested with specific doubt:',
        'doubt_cost': 'Cost', 'doubt_time': 'Time', 'doubt_method': 'Method',
        'doubt_family': 'Family decision', 'doubt_other': 'Other:',
        'cold': 'COLD - deflated, needs 2nd contact',
        'why_emotional': 'Why your emotional reading (1-2 sentences):',
        'sec11_title': 'SECTION 11 - TIME COMMITMENT TO PROSPECT',
        'commit_today': 'Advisor contacts TODAY before:',
        'commit_hours': 'In ___ hours (before):',
        'commit_tomorrow': 'Tomorrow before:',
        'commit_immediately': 'Advisor enters immediately (in-person)',
        'channel': 'Channel:', 'wa': 'WhatsApp', 'call': 'Phone call',
        'inperson_appt': 'In-person appt', 'video': 'Video call',
        'sec12_title': 'SECTION 12 - VERBATIM QUOTES (gold for advisor)',
        'intent_label': 'PURCHASE INTENT quote (if said):',
        'objection_label': 'OBJECTION/DOUBT quote (if said):',
        'sec13_title': 'SECTION 13 - QUICK BRIEF FOR ADVISOR (2-3 lines)',
        'sec14_title': "SECTION 14 - ANCHORS FOR ADVISOR'S PITCH",
        'anchor1': 'Anchor 1 (profession/context):',
        'anchor2': 'Anchor 2 (deep motivation):',
        'anchor3': 'Anchor 3 (detected strength):',
        'sec15_title': 'SECTION 15 - URGENCY',
        'urg_immediate': 'IMMEDIATE (<30 min) - hot + high competitiveness',
        'urg_today': 'TODAY - real interest',
        'urg_24h': '24 HOURS - warm',
        'urg_48h': '48 HOURS+ - cold, re-engage',
        'urg_why': 'If >24h, why:',
        'sec16_title': 'SECTION 16 - FREE NOTES',
        'errors_title': 'ERRORS TO AVOID (reminder)',
        'errors': ('Do not tell prospect their exact level (coordination handles) | '
                   'Do not discuss prices | Do not compare with other students | '
                   'Do not promise timeframes | Do not correct during test'),
        'closing': 'CLOSING',
        'time_finished': 'Time finished report:', 'time_sent': 'Time sent to advisor:',
        'signature': 'Evaluator signature:',
    }
}


# =========================================================================
# HELPERS
# =========================================================================

def make_pdf(lang):
    t = TEXTS[lang]
    fn = os.path.join(EVAL_DIR, f'GUIA_EVALUADORA_{lang.upper()}_EDITABLE.pdf')
    c = canvas.Canvas(fn, pagesize=letter)

    margin = 36
    page_y = h - 30

    def new_page():
        c.showPage()
        return h - 30

    def section_header(y, text, color=DARK):
        if y < 80:
            y = new_page()
        c.setFillColor(color)
        c.rect(margin, y - 16, w - 2 * margin, 18, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont('Helvetica-Bold', 9.5)
        c.drawString(margin + 5, y - 12, text)
        return y - 24

    def small_box(y, text, color=ACTIVATOR_BG, height_lines=2):
        """Caja de texto informativo (no editable). Auto-wrap."""
        if y < 80:
            y = new_page()
        # Calculate height needed
        max_chars = 110
        lines = []
        words = text.split(' ')
        cur = ''
        for word in words:
            if len(cur) + len(word) + 1 > max_chars:
                lines.append(cur)
                cur = word
            else:
                cur = cur + ' ' + word if cur else word
        if cur:
            lines.append(cur)
        box_h = len(lines) * 9 + 6
        c.setFillColor(color)
        c.rect(margin, y - box_h, w - 2 * margin, box_h, fill=1, stroke=0)
        c.setFillColor(black)
        c.setFont('Helvetica', 7.5)
        for i, line in enumerate(lines):
            c.drawString(margin + 5, y - 9 - i * 9, line)
        return y - box_h - 4

    def text_field(name, x, y, width=200, height=12):
        c.acroForm.textfield(name=name, x=x, y=y, width=width, height=height,
                             fontSize=8, borderWidth=0.5, borderColor=GRAY)

    def checkbox(name, x, y, size=10):
        c.acroForm.checkbox(name=name, x=x, y=y, size=size, borderWidth=0.5)

    def label(text, x, y, font='Helvetica', size=8, color=black, bold=False):
        c.setFont('Helvetica-Bold' if bold else font, size)
        c.setFillColor(color)
        c.drawString(x, y, text)

    def question_row(y, num, q, struct, prefix):
        """Una pregunta del test con checkboxes pass/fail."""
        if y < 60:
            y = new_page()
        # Number
        c.setFont('Helvetica-Bold', 8)
        c.setFillColor(DARK)
        c.drawString(margin, y, f'{num}.')
        # Question
        c.setFont('Helvetica-Bold', 8)
        c.setFillColor(black)
        # truncate if needed
        q_display = q if len(q) <= 70 else q[:70] + '...'
        c.drawString(margin + 14, y, q_display)
        # Structure (gray italic)
        c.setFont('Helvetica-Oblique', 6.5)
        c.setFillColor(GRAY)
        c.drawString(margin + 14, y - 8, f'[{struct}]')
        # Pass/Fail checkboxes (right side)
        c.setFillColor(black)
        c.setFont('Helvetica', 7)
        checkbox(f'{prefix}_q{num}_pass', w - margin - 80, y - 4, size=9)
        c.drawString(w - margin - 67, y - 2, t['pass'])
        checkbox(f'{prefix}_q{num}_fail', w - margin - 38, y - 4, size=9)
        c.drawString(w - margin - 25, y - 2, t['fail'])
        return y - 18

    # ===== PAGE 1: HEADER + SEC 0 + SEC 1 + SEC 2 =====
    y = page_y
    # Title
    c.setFillColor(DARK)
    c.rect(0, y - 30, w, 40, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 14)
    c.drawString(margin, y - 12, t['title'])
    c.setFont('Helvetica', 8)
    c.drawString(margin, y - 24, t['subtitle'])
    y -= 42

    # SEC 0
    y = section_header(y, t['sec0'])
    c.setFillColor(black)
    label(t['prospect'], margin, y, bold=True)
    text_field('prospect_name', margin + 70, y - 3, width=180)
    label(t['age'], margin + 270, y, bold=True)
    text_field('age', margin + 300, y - 3, width=40)
    label(t['date'], margin + 360, y, bold=True)
    text_field('date', margin + 395, y - 3, width=80)
    y -= 18
    label(t['profession'], margin, y, bold=True)
    text_field('profession', margin + 70, y - 3, width=200)
    label(t['evaluator'], margin + 290, y, bold=True)
    text_field('evaluator_name', margin + 350, y - 3, width=130)
    y -= 18
    label(t['start'], margin, y, bold=True)
    text_field('start_time', margin + 35, y - 3, width=50)
    label(t['end'], margin + 100, y, bold=True)
    text_field('end_time', margin + 130, y - 3, width=50)
    label(t['modality'], margin + 200, y, bold=True)
    checkbox('mod_inperson', margin + 250, y - 3)
    label(t['inperson'], margin + 263, y)
    checkbox('mod_virtual', margin + 320, y - 3)
    label(t['virtual'], margin + 333, y)
    label(t['advisor'], margin + 390, y, bold=True)
    text_field('advisor_name', margin + 430, y - 3, width=110)
    y -= 22

    # SEC 1 - Filosofia
    y = section_header(y, t['sec1_title'], color=ORANGE)
    y = small_box(y, t['philosophy'], color=WARN)
    y -= 6

    # SEC 2 - Apertura
    y = section_header(y, t['sec2_title'])
    y = small_box(y, t['opening'])
    y = small_box(y, t['opening_en'], color=LIGHTBOX)
    y -= 6

    # ===== A1 =====
    y = section_header(y, t['level_a1'], color=GREEN)
    for i, (q, s) in enumerate(A1_QUESTIONS, 1):
        y = question_row(y, i, q, s, 'a1')
    # Total + Decision
    if y < 80:
        y = new_page()
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(black)
    c.drawString(margin, y, t['total_a1'])
    y -= 14
    y = small_box(y, t['activator_a1_pass'])
    y = small_box(y, t['activator_a1_fail'])
    y = small_box(y, t['activator_a1_strength'])
    y -= 4
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(DARK)
    c.drawString(margin, y, t['decision_a1'])
    y -= 14

    # ===== A2 =====
    y = section_header(y, t['level_a2'], color=BLUE)
    for i, (q, s) in enumerate(A2_QUESTIONS, 1):
        y = question_row(y, i, q, s, 'a2')
    if y < 80:
        y = new_page()
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(black)
    c.drawString(margin, y, t['total_a2'])
    y -= 14
    y = small_box(y, t['activator_a2_pass'])
    y = small_box(y, t['activator_a2_fail'])
    y -= 4
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(DARK)
    c.drawString(margin, y, t['decision_a2'])
    y -= 14

    # ===== B1 =====
    y = section_header(y, t['level_b1'], color=YELLOW)
    for i, (q, s) in enumerate(B1_QUESTIONS, 1):
        y = question_row(y, i, q, s, 'b1')
    if y < 80:
        y = new_page()
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(black)
    c.drawString(margin, y, t['total_b1'])
    y -= 14
    y = small_box(y, t['activator_b1_pass'])
    y -= 4
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(DARK)
    c.drawString(margin, y, t['decision_b1'])
    y -= 14

    # ===== B2 =====
    y = section_header(y, t['level_b2'], color=RED)
    for i, (q, s) in enumerate(B2_QUESTIONS, 1):
        y = question_row(y, i, q, s, 'b2')
    if y < 80:
        y = new_page()
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(black)
    c.drawString(margin, y, t['total_b2'])
    y -= 14
    y = small_box(y, t['activator_b2_pass'])
    y -= 4
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(DARK)
    c.drawString(margin, y, t['decision_b2'])
    y -= 14

    # ===== SEC 4 - CIERRE ACTIVADOR =====
    y = section_header(y, t['cierre_title'], color=ORANGE)
    y = small_box(y, t['cierre_text'], color=WARN, height_lines=4)
    y -= 4

    # ===== SEC 5 - LECTURA COMPETITIVIDAD =====
    y = section_header(y, t['sec5_title'])
    if y < 90:
        y = new_page()
    checkbox('comp_high', margin, y - 3)
    label(t['comp_high'], margin + 14, y)
    y -= 14
    checkbox('comp_med', margin, y - 3)
    label(t['comp_med'], margin + 14, y)
    y -= 14
    checkbox('comp_low', margin, y - 3)
    label(t['comp_low'], margin + 14, y)
    y -= 16
    label(t['hook_label'], margin, y, bold=True)
    y -= 14
    text_field('hook_resonated', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 22

    # ===== SEC 6 - DIAGNOSTICO FINAL =====
    y = section_header(y, t['sec6_title'])
    if y < 100:
        y = new_page()
    label(t['final_level'], margin, y, bold=True)
    for i, lvl in enumerate(['A1', 'A2', 'B1', 'B2', 'B2+']):
        checkbox(f'final_{lvl}', margin + 75 + i * 50, y - 3, size=12)
        label(lvl, margin + 92 + i * 50, y, bold=True)
    y -= 18
    label(t['certainty'], margin, y, bold=True)
    checkbox('cert_clear', margin + 60, y - 3)
    label(t['cert_clear'], margin + 75, y)
    checkbox('cert_border', margin + 165, y - 3)
    label(t['cert_border'], margin + 180, y)
    checkbox('cert_retest', margin + 270, y - 3)
    label(t['cert_retest'], margin + 285, y)
    y -= 18
    label(t['program'], margin, y, bold=True)
    text_field('program', margin + 130, y - 3, width=w - 2 * margin - 130)
    y -= 18

    # ===== SEC 7 - FORTALEZAS =====
    y = section_header(y, t['sec7_title'])
    if y < 100:
        y = new_page()
    label(t['strength1'], margin, y, bold=True)
    text_field('strength1', margin + 75, y - 3, width=w - 2 * margin - 75)
    y -= 14
    label(t['quote'], margin, y, bold=True)
    text_field('strength1_quote', margin + 50, y - 3, width=w - 2 * margin - 50)
    y -= 16
    label(t['strength2'], margin, y, bold=True)
    text_field('strength2', margin + 75, y - 3, width=w - 2 * margin - 75)
    y -= 14
    label(t['quote'], margin, y, bold=True)
    text_field('strength2_quote', margin + 50, y - 3, width=w - 2 * margin - 50)
    y -= 18

    # ===== SEC 8 - PUNTO DE TRABAJO =====
    y = section_header(y, t['sec8_title'])
    if y < 80:
        y = new_page()
    label(t['work_point'], margin, y, bold=True)
    y -= 12
    text_field('work_point', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 18
    label(t['how_solved'], margin, y, bold=True)
    y -= 12
    text_field('how_solved', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 20

    # ===== SEC 9 - MOTIVACION =====
    y = section_header(y, t['sec9_title'])
    if y < 100:
        y = new_page()
    motivations = [('mot_work', t['mot_work']), ('mot_travel', t['mot_travel']),
                   ('mot_family', t['mot_family']), ('mot_personal', t['mot_personal']),
                   ('mot_business', t['mot_business']), ('mot_studies', t['mot_studies'])]
    col_w = 250
    for i, (key, lbl) in enumerate(motivations):
        col = i % 2
        row = i // 2
        x_pos = margin + col * col_w
        y_pos = y - row * 12
        checkbox(key, x_pos, y_pos - 3)
        label(lbl, x_pos + 14, y_pos)
    y -= 38
    label(t['mot_other'], margin, y, bold=True)
    text_field('mot_other_text', margin + 50, y - 3, width=w - 2 * margin - 50)
    y -= 16
    label(t['mot_detail'], margin, y, bold=True)
    y -= 12
    text_field('mot_detail', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 20

    # ===== SEC 10 - LECTURA EMOCIONAL =====
    y = section_header(y, t['sec10_title'])
    if y < 100:
        y = new_page()
    checkbox('emo_hot', margin, y - 3)
    label(t['hot'], margin + 14, y, bold=True)
    y -= 14
    checkbox('emo_warm', margin, y - 3)
    label(t['warm'], margin + 14, y, bold=True)
    y -= 12
    doubts = [('doubt_cost', t['doubt_cost']), ('doubt_time', t['doubt_time']),
              ('doubt_method', t['doubt_method']), ('doubt_family', t['doubt_family'])]
    for i, (key, lbl) in enumerate(doubts):
        x_pos = margin + 30 + (i % 4) * 110
        checkbox(key, x_pos, y - 3)
        label(lbl, x_pos + 14, y)
    y -= 14
    label(t['doubt_other'], margin + 30, y)
    text_field('doubt_other_text', margin + 80, y - 3, width=200)
    y -= 14
    checkbox('emo_cold', margin, y - 3)
    label(t['cold'], margin + 14, y, bold=True)
    y -= 14
    label(t['why_emotional'], margin, y, bold=True)
    y -= 12
    text_field('why_emo', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 20

    # ===== SEC 11 - COMPROMISO TEMPORAL =====
    y = section_header(y, t['sec11_title'])
    if y < 100:
        y = new_page()
    checkbox('commit_today', margin, y - 3)
    label(t['commit_today'], margin + 14, y)
    text_field('commit_today_time', margin + 230, y - 3, width=70)
    y -= 14
    checkbox('commit_hours', margin, y - 3)
    label(t['commit_hours'], margin + 14, y)
    text_field('commit_hours_time', margin + 230, y - 3, width=70)
    y -= 14
    checkbox('commit_tomorrow', margin, y - 3)
    label(t['commit_tomorrow'], margin + 14, y)
    text_field('commit_tomorrow_time', margin + 230, y - 3, width=70)
    y -= 14
    checkbox('commit_immediate', margin, y - 3)
    label(t['commit_immediately'], margin + 14, y)
    y -= 16
    label(t['channel'], margin, y, bold=True)
    channels = [('ch_wa', t['wa']), ('ch_call', t['call']),
                ('ch_inperson', t['inperson_appt']), ('ch_video', t['video'])]
    for i, (key, lbl) in enumerate(channels):
        x_pos = margin + 60 + i * 110
        checkbox(key, x_pos, y - 3)
        label(lbl, x_pos + 14, y)
    y -= 20

    # ===== SEC 12 - FRASES TEXTUALES =====
    y = section_header(y, t['sec12_title'])
    if y < 90:
        y = new_page()
    label(t['intent_label'], margin, y, bold=True)
    y -= 12
    text_field('intent_quote', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 16
    label(t['objection_label'], margin, y, bold=True)
    y -= 12
    text_field('objection_quote', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 20

    # ===== SEC 13 - BRIEFING =====
    y = section_header(y, t['sec13_title'])
    if y < 80:
        y = new_page()
    text_field('briefing1', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 18
    text_field('briefing2', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 18
    text_field('briefing3', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 22

    # ===== SEC 14 - ANCLAS =====
    y = section_header(y, t['sec14_title'])
    if y < 100:
        y = new_page()
    for i, key in enumerate(['anchor1', 'anchor2', 'anchor3']):
        label(t[key], margin, y, bold=True)
        text_field(key, margin + 130, y - 3, width=w - 2 * margin - 130)
        y -= 16
    y -= 6

    # ===== SEC 15 - URGENCIA =====
    y = section_header(y, t['sec15_title'])
    if y < 100:
        y = new_page()
    urgs = [('urg_immediate', t['urg_immediate']), ('urg_today', t['urg_today']),
            ('urg_24h', t['urg_24h']), ('urg_48h', t['urg_48h'])]
    for key, lbl in urgs:
        checkbox(key, margin, y - 3)
        label(lbl, margin + 14, y)
        y -= 14
    label(t['urg_why'], margin, y, bold=True)
    y -= 12
    text_field('urg_why_text', margin, y - 3, width=w - 2 * margin, height=14)
    y -= 20

    # ===== SEC 16 - NOTAS LIBRES =====
    y = section_header(y, t['sec16_title'])
    if y < 80:
        y = new_page()
    for i in range(3):
        text_field(f'free_notes_{i}', margin, y - 3, width=w - 2 * margin, height=14)
        y -= 18
    y -= 4

    # ===== ERRORES + CIERRE =====
    y = section_header(y, t['errors_title'], color=RED)
    y = small_box(y, t['errors'], color=WARN)
    y -= 6

    if y < 60:
        y = new_page()
    label(t['time_finished'], margin, y, bold=True)
    text_field('time_finished', margin + 140, y - 3, width=80)
    label(t['time_sent'], margin + 250, y, bold=True)
    text_field('time_sent', margin + 380, y - 3, width=80)
    y -= 18
    label(t['signature'], margin, y, bold=True)
    text_field('signature', margin + 130, y - 3, width=300)

    c.save()
    with open(fn, 'rb') as f:
        pages = len(re.findall(rb'/Type\s*/Page[^s]', f.read()))
    print(f'OK: {fn} - {pages} pages, fully editable')


# =========================================================================
# MAIN
# =========================================================================
make_pdf('es')
make_pdf('en')
print('\nGUIA EVALUADORA editable generada (ES + EN). Form fields fully fillable.')
