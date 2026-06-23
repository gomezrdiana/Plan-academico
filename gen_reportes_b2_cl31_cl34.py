#!/usr/bin/env python3
"""Reportes 1-hoja B2 Cl 31-34 modelo v4.1 — bloque JUSTICIA (Cl 31-35) — Fase 5 pre-Final."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))


# ==================================================================
# Cl 31 — Phase 5 opening — JUSTICIA día 1 ABRE
# ==================================================================
build_report_v2(
    os.path.join(D, 'B2', 'B2_Clase31_REPORTE.pdf'),
    'B2 NIVEL 2H | Clase 31 de 36',
    'Phase 5 opening — framework + recap Sets #21-23 + 30-sec HOOK round — JUSTICIA día 1 de 5 ABRE bloque',
    [
        ('BLOQUE 1 — OPENER (frase + JUSTICIA día 1 ABRE + welcome Phase 5 + bridge)', '~10 min'),
        ('BLOQUE 2 — CONTENT FRAMEWORK (Phase 5 system + recap Sets #21-23 + monologue structure + 3-sec rule)', '~50 min'),
        ('BLOQUE 3 — LIVE: 30-SEC HOOK ROUND (cada estudiante × 2 + peer feedback)', '~45 min'),
        ('BLOQUE 4 — CIERRE (recap + frase close + virtud + tarea + Cl 32 announce)', '~15 min'),
    ],
    [
        'Foto del board con Phase 5 system + monologue structure',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: JUSTICIA día 1 ABRE bloque (Cl 31-35) marcado',
        'Confirmar: 4 inserciones de Frase del Día hechas',
        'Confirmar: anunciaste Cl 32 = REFRAME + Q&A intensive + Set #24',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "JUSTICE" en el board grande + dije qué significa hoy (apertura)',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé cards, grids impresos (solo board + cuaderno)',
        'ESCRIBÍ Phase 5 system: 5 clases + monologue structure + Q&A 3-sec rule',
        'Recapitulé Sets #21-23 con ejemplos profesionales',
        'Cada estudiante nombró su PROYECTO en voz alta + 1 frase del porqué',
        'En Bloque 3 cada estudiante entregó su HOOK 2 veces (30 seg cada vez)',
        'Peer feedback estructurado: 1 win + 1 sharpen (con vocab de Sets)',
        'Cuando un hook se pasó de 30 seg: dije "Tighten — cut adjectives"',
        'Cl 36 mencionado solo como evaluador externo de coordinación',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)


# ==================================================================
# Cl 32 — REFRAME + Q&A intensive + Set #24 — JUSTICIA día 2
# ==================================================================
build_report_v2(
    os.path.join(D, 'B2', 'B2_Clase32_REPORTE.pdf'),
    'B2 NIVEL 2H | Clase 32 de 36',
    'REFRAME the speaker role + Q&A INTENSIVE (3 rondas × 3 preguntas) + Vocab Set #24 TAKING THE FLOOR — JUSTICIA día 2 de 5',
    [
        ('BLOQUE 1 — OPENER (frase + JUSTICIA día 2 + mystery del Cl 31 hook + bridge)', '~10 min'),
        ('BLOQUE 2 — CONTENT REFRAME + 3-sec rule + Set #24 + mini-drills', '~50 min'),
        ('BLOQUE 3 — LIVE: Q&A INTENSIVE 3 RONDAS × 3 PREGUNTAS (B1 audience / skeptic / honest gap)', '~45 min'),
        ('BLOQUE 4 — CIERRE (recap + frase close + virtud + tarea + Cl 33 announce)', '~15 min'),
    ],
    [
        'Foto del board con REFRAME + 3-sec rule + Set #24',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: JUSTICIA día 2 de 5 marcado',
        'Confirmar: 4 inserciones de Frase del Día hechas',
        'Confirmar: anunciaste Cl 33 = Monologue refinement + Set #25',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "JUSTICE" en el board grande + dije qué significa hoy',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé cards, grids impresos (solo board + cuaderno)',
        'ESCRIBÍ el REFRAME: "You are the model. The room learns by hearing you first."',
        'Articulé la 3-SECOND RULE explícitamente en board',
        'ESCRIBÍ Set #24 (6 palabras): JUMP IN / BUILD ON / OFFER / CHIME IN / STEP UP / WEIGH IN',
        'En Bloque 3 las 3 rondas se completaron: B1 audience / skeptic / honest gap',
        'Cada estudiante respondió 9 preguntas en total (3 por ronda)',
        'Cuando alguien dudó 5+ seg: dije "3 seconds. Use Set #24 even half-formed."',
        'Vocab Set #24 se aplicó LIVE en Bloque 3 (no solo en Bloque 2)',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)


# ==================================================================
# Cl 33 — Monologue refinement + Set #25 + Q&A harder — JUSTICIA día 3
# ==================================================================
build_report_v2(
    os.path.join(D, 'B2', 'B2_Clase33_REPORTE.pdf'),
    'B2 NIVEL 2H | Clase 33 de 36',
    'Phase 5 monologue refinement + Q&A INTENSIVE HARDER + Vocab Set #25 HOLDING THE TURN WITH PRECISION — JUSTICIA día 3 de 5',
    [
        ('BLOQUE 1 — OPENER (frase + JUSTICIA día 3 + mystery del Cl 32 + bridge)', '~10 min'),
        ('BLOQUE 2 — CONTENT REFINEMENT (cada uno sharpens su 60-sec weakest + Set #25)', '~50 min'),
        ('BLOQUE 3 — LIVE: Q&A INTENSIVE HARDER (3 rondas: skeptic post-hook / counter / panel)', '~45 min'),
        ('BLOQUE 4 — CIERRE (recap + frase close + virtud + tarea + Cl 34 announce)', '~15 min'),
    ],
    [
        'Foto del board con Set #25 + 60-sec weakest spots identificados',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: JUSTICIA día 3 de 5 marcado',
        'Confirmar: 4-5 inserciones de Frase del Día hechas',
        'Confirmar: anunciaste Cl 34 = FULL monologue from memory + Set #26',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "JUSTICE" en el board grande + dije qué significa hoy',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé cards, grids impresos (solo board + cuaderno)',
        'ESCRIBÍ Set #25 (6 palabras): ELABORATE / CLARIFY / QUALIFY / NUANCE / SPECIFY / CONTEXTUALIZE',
        'Cada estudiante identificó SU 60-sec weakest spot del monologue',
        'Coaching individual en whispers (NO en frente del grupo)',
        'Pair rehearsal del segmento sharpened',
        'Q&A HARDER que Cl 32: skeptic post-hook + counter a sí mismo + panel del cohorte',
        'Cuando alguien dio respuesta vaga: dije "Specify. WHO benefits? HOW?"',
        'Vocab Set #25 se aplicó LIVE en respuestas Q&A (no solo en Bloque 2)',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)


# ==================================================================
# Cl 34 — FULL monologue from memory + Set #26 — JUSTICIA día 4
# ==================================================================
build_report_v2(
    os.path.join(D, 'B2', 'B2_Clase34_REPORTE.pdf'),
    'B2 NIVEL 2H | Clase 34 de 36',
    'FULL 5-7 min monologue FROM MEMORY + LIVE peer Q&A + teacher critical audience + Vocab Set #26 CLOSING THE TURN CLEANLY — JUSTICIA día 4 de 5',
    [
        ('BLOQUE 1 — OPENER (frase + JUSTICIA día 4 + mystery del Cl 33 + bridge)', '~10 min'),
        ('BLOQUE 2 — CONTENT Set #26 + close craft (rewrite final 15-sec)', '~50 min'),
        ('BLOQUE 3 — LIVE: FULL MONOLOGUE FROM MEMORY (cada uno 5-7 min + peer + critical Q&A)', '~45 min'),
        ('BLOQUE 4 — CIERRE (recap + frase close + virtud + tarea + Cl 35 announce)', '~15 min'),
    ],
    [
        'Foto del board con Set #26 + finales rewritten',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: JUSTICIA día 4 de 5 marcado (1 día por cerrar)',
        'Confirmar: 4 inserciones de Frase del Día hechas',
        'Confirmar: anunciaste Cl 35 = FULL DRY-RUN + Set #27 + cierre bloque JUSTICIA + Cl 36 Final coord',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "JUSTICE" en el board grande + dije qué significa hoy',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé cards, grids impresos (solo board + cuaderno)',
        'ESCRIBÍ Set #26 (6 palabras): LAND / WRAP / SEAL / HAND OFF / YIELD / PUNCTUATE',
        'Cada estudiante reescribió los ÚLTIMOS 15 SEG de su monologue usando Set #26',
        'Pair rehearsal del close 3 veces',
        'ANTI-FRAUDE: monologue FROM MEMORY — NO notas, NO papel, NO celular',
        'Cada estudiante recibió 1 pregunta crítica del teacher (audience role)',
        'Cuando alguien hizo fade al final ("...so yeah"): dije "Set #26. LAND it. Punctuate."',
        'Si el cohorte es 5+, ajusté: 2-3 hicieron full delivery + resto 60-sec preview',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)


print('\n4 reportes B2 Cl 31-34 generados.')
