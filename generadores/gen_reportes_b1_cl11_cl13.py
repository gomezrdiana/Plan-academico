#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Reportes 1-hoja B1 Mastery Cl 11-13 modelo v4.1. Bloque JUSTICIA v1 (Cl 11-15)."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ==================================================================
# Cl 11 — Past Simple Regular — JUSTICIA día 1 ABRE
# ==================================================================
for track, title_track, focus, sim, last_check in [
    ('CONV', 'CONV', 'oral (Yesterday\'s Workday Debrief)', 'YESTERDAY\'S WORKDAY DEBRIEF',
     'En Bloque 3 cada pareja produjo 5+ verbos regulares en pasado + time markers'),
    ('GRAMMAR', 'GRAMMAR', 'tabla formal + ED Pronunciation Relay', 'ED PRONUNCIATION RELAY',
     'ESCRIBÍ 3 columnas /t/ /d/ /ɪd/ + 20 verbos clasificados por sonido'),
]:
    build_report_v2(
        os.path.join(D, 'B1', f'B1_conversacional_V2' if track=='CONV' else f'B1_gramatica_V2',
                     f'B1_Clase11_{track}_REPORTE.pdf'),
        f'B1 MASTERY | Clase 11 de 44 — {title_track}',
        f'Past Simple REGULAR verbs ({focus}) — spelling rules + /t/-/d/-/ɪd/ — JUSTICIA v1 día 1 de 5 ABRE bloque',
        [
            (f'BLOQUE 1 — OPENER (frase + JUSTICIA día 1 ABRE + mystery + bridge)', '~10 min'),
            (f'BLOQUE 2 — CONTENT Past Simple regular (spelling + pronunciación + práctica pares)', '~50 min'),
            (f'BLOQUE 3 — LIVE: {sim} (rotaciones + observer)', '~45 min'),
            (f'BLOQUE 4 — CIERRE (error recap + frase close + PASE + tarea + Cl 12 announce)', '~15 min'),
        ],
        [
            'Foto del board final con los 3-5 errores típicos del día',
            'Error paper anónimo (físico, con la guía — NO fotografiado)',
            '3 errores literales con NOMBRES en tu cuaderno personal',
            f'PASE A {"GRAMMAR Cl 11" if track=="CONV" else "CONV Cl 12"} entregado (3 gaps observados)',
            'Confirmar: JUSTICIA v1 día 1 ABRE bloque marcado',
            'Confirmar: anunciaste Cl 12 = Past Simple IRREGULAR (top 25 + 4 patrones)',
        ],
        [
            'Frase del Día en el board ANTES de empezar',
            'Escribí "JUSTICE" en el board grande + dije qué significa hoy (apertura)',
            'Todo lo que dije a la clase fue en INGLÉS',
            'NO usé cards, grids impresos (solo board + cuaderno)',
            'ESCRIBÍ las 4 reglas de spelling: -ed / -d / -ied / doble consonante',
            'ESCRIBÍ las 3 reglas de pronunciación /t/ /d/ /ɪd/',
            'Cuando alguien dijo "workt" o "studyed": dije "Justice. Give the past its right ending."',
            'CORREGÍ en board cuando un error apareció 2 veces',
            last_check,
            'Hice puente con Cl 10 (object pronouns) al menos 1 vez',
            'NO comuniqué notas / NO mencioné metodología por nombre',
        ],
        S,
    )


# ==================================================================
# Cl 12 — Past Simple Irregular — JUSTICIA día 2
# ==================================================================
for track, title_track, focus, sim, last_check in [
    ('CONV', 'CONV', 'oral (Weekend Storytelling Swap)', 'WEEKEND STORYTELLING SWAP',
     'En Bloque 3 cada pareja contó 5+ acciones con MIN 4 irregulares cada una'),
    ('GRAMMAR', 'GRAMMAR', 'tabla 5 grupos + 25-verb dictation', 'IRREGULAR PAST SPRINT (25 verbs)',
     'ESCRIBÍ los 5 grupos en board: SAME / VOWEL CHANGE / -OUGHT / -ELT-ENT-EPT / TOTALLY DIFFERENT'),
]:
    build_report_v2(
        os.path.join(D, 'B1', f'B1_conversacional_V2' if track=='CONV' else f'B1_gramatica_V2',
                     f'B1_Clase12_{track}_REPORTE.pdf'),
        f'B1 MASTERY | Clase 12 de 44 — {title_track}',
        f'Past Simple IRREGULAR top 25 verbos en 5 grupos ({focus}) — JUSTICIA v1 día 2 de 5',
        [
            ('BLOQUE 1 — OPENER (frase + JUSTICIA día 2 + mystery del Cl 11 + bridge)', '~10 min'),
            ('BLOQUE 2 — CONTENT Past Simple irregular (5 grupos + práctica pares)', '~50 min'),
            (f'BLOQUE 3 — LIVE: {sim}', '~45 min'),
            ('BLOQUE 4 — CIERRE (error recap + frase close + PASE + tarea + Cl 13 announce)', '~15 min'),
        ],
        [
            'Foto del board final con los 5 grupos de irregulares + 3-5 errores típicos',
            'Error paper anónimo (físico, con la guía — NO fotografiado)',
            '3 errores literales con NOMBRES en tu cuaderno personal',
            f'PASE A {"GRAMMAR Cl 12" if track=="CONV" else "CONV Cl 13"} entregado (3 gaps observados)',
            'Confirmar: JUSTICIA v1 día 2 de 5 marcado',
            'Confirmar: anunciaste Cl 13 = Past Simple NEGATIVAS + PREGUNTAS (DID + bare)',
        ],
        [
            'Frase del Día en el board ANTES de empezar',
            'Escribí "JUSTICE" en el board grande + dije qué significa hoy',
            'Todo lo que dije a la clase fue en INGLÉS',
            'NO usé cards, grids impresos (solo board + cuaderno)',
            last_check,
            'Hice callback a Cl 11 (regulars worked/stopped/studied) al menos 1 vez',
            'Trabajé el "READ trap": /riːd/ → /rɛd/ (escrito igual, pronunciación cambia)',
            'Cuando alguien dijo "goed" o "thinked": dije "Justice. That verb has its own past form."',
            'CORREGÍ en board cuando un error apareció 2 veces',
            'En Bloque 4 anuncié Cl 13 = DID + bare verb (regla clave)',
            'NO comuniqué notas / NO mencioné metodología por nombre',
        ],
        S,
    )


# ==================================================================
# Cl 13 — Past Simple Negatives + Questions DID — JUSTICIA día 3
# ==================================================================
for track, title_track, focus, sim, last_check in [
    ('CONV', 'CONV', 'oral (Job Interview Past Experience)', 'JOB INTERVIEW PAST EXPERIENCE',
     'En Bloque 3 cada pareja produjo 8 preguntas + 2 negativas correctas con bare verb'),
    ('GRAMMAR', 'GRAMMAR', 'tabla 5 secciones + DID/DIDN\'T + WH-Q Sprint', 'DID/DIDN\'T DRILL + WH-QUESTION SPRINT',
     'ESCRIBÍ 5 secciones: Afirmativa / Negativa / Yes-No Q / Short answer / WH-Q + excepción subject Q'),
]:
    build_report_v2(
        os.path.join(D, 'B1', f'B1_conversacional_V2' if track=='CONV' else f'B1_gramatica_V2',
                     f'B1_Clase13_{track}_REPORTE.pdf'),
        f'B1 MASTERY | Clase 13 de 44 — {title_track}',
        f'Past Simple NEGATIVAS + PREGUNTAS (DID + bare verb) ({focus}) — JUSTICIA v1 día 3 de 5',
        [
            ('BLOQUE 1 — OPENER (frase + JUSTICIA día 3 + mystery del Cl 12 + bridge)', '~10 min'),
            ('BLOQUE 2 — CONTENT DID + bare (negativas + yes-no Q + WH-Q + short answers + subject Q)', '~50 min'),
            (f'BLOQUE 3 — LIVE: {sim}', '~45 min'),
            ('BLOQUE 4 — CIERRE (error recap + frase close + PASE + tarea + Cl 14 announce)', '~15 min'),
        ],
        [
            'Foto del board final con la regla BARE VERB después de DID + 3-5 errores típicos',
            'Error paper anónimo (físico, con la guía — NO fotografiado)',
            '3 errores literales con NOMBRES en tu cuaderno personal',
            f'PASE A {"GRAMMAR Cl 13" if track=="CONV" else "CONV Cl 14"} entregado (3 gaps observados)',
            'Confirmar: JUSTICIA v1 día 3 de 5 marcado',
            'Confirmar: anunciaste Cl 14',
        ],
        [
            'Frase del Día en el board ANTES de empezar',
            'Escribí "JUSTICE" en el board grande + dije qué significa hoy',
            'Todo lo que dije a la clase fue en INGLÉS',
            'NO usé cards, grids impresos (solo board + cuaderno)',
            last_check,
            'Hice callback a Cl 11+12: con DID, el verbo regresa a BARE (no -ed ni irregular)',
            'Marqué la EXCEPCIÓN subject questions: "WHO called?" sin DID',
            'Cuando alguien dijo "Did you worked?" o "She didn\'t went": dije "Justice. After DID, bare."',
            'CORREGÍ en board cuando un error apareció 2 veces',
            'En Bloque 3 los pares produjeron 8 preguntas + 2 negativas con bare verb cada uno',
            'NO comuniqué notas / NO mencioné metodología por nombre',
        ],
        S,
    )


print('\n6 reportes B1 Cl 11-13 (Conv + Gram) generados.')
