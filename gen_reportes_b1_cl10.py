#!/usr/bin/env python3
"""Reportes 1-hoja B1 Mastery Cl 10 — Conv + Grammar, modelo v4.1.
Object pronouns + indirect objects. TEMPLANZA v1 día 5 CIERRA bloque."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# B1 CL 10 CONV — Object pronouns oral — TEMPLANZA día 5 CIERRA
# ============================================================

conv_activities = [
    ('BLOQUE 1 — OPENER (frase + TEMPLANZA día 5 CIERRA + mystery del pase Cl 9 + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT object pronouns + indirect objects + TELL/ASK exception', '~50 min'),
    ('BLOQUE 3 — LIVE: DELEGATION CALL (trios con observer + 3 rotaciones)', '~45 min'),
    ('BLOQUE 4 — CIERRE (error recap + frase close + virtud cierre + retrospective + PASE A GRAMMAR + tarea)', '~15 min'),
]

conv_deliverables = [
    'Foto del board final con los 3-5 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal',
    'PASE A GRAMMAR Cl 10 entregado (3 gaps observados oralmente)',
    'Confirmar: TEMPLANZA v1 día 5 de 5 CIERRA bloque marcado',
    'Confirmar: anunciaste Cl 11 = JUSTICIA v1 día 1 ABRE',
]

conv_selfeval = [
    'Frase del Día en el board ANTES de empezar',
    'Escribí "TEMPERANCE" en el board grande + dije qué significa hoy (día 5 cierre)',
    'Todo lo que dije a la clase fue en INGLÉS',
    'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
    'En Bloque 2 los pares hablaron más que yo',
    'En Bloque 3 yo coachée — NO jugué ni manager ni colega del trio',
    'Cuando alguien dijo orden mal: dije "Measure. Where does the pronoun belong?"',
    'CORREGÍ en board cuando un error apareció 2 veces',
    'Hice el callback a Cl 9 al menos 1 vez (HIS report vs I helped HIM)',
    'Retrospective 30 seg cada uno SIN discusión',
    'PASE A GRAMMAR Cl 10 con 3 gaps orales escritos',
    'NO comuniqué notas / NO mencioné metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'B1', 'B1_Clase10_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 10 de 44 — CONV',
    'OBJECT PRONOUNS + INDIRECT OBJECTS oral (me/you/him/her/it/us/them + Order A/B + TELL/ASK exception) — TEMPLANZA v1 día 5 de 5 CIERRA bloque',
    conv_activities,
    conv_deliverables,
    conv_selfeval,
    S,
)


# ============================================================
# B1 CL 10 GRAMMAR — Object pronouns tabla — TEMPLANZA día 5 CIERRA
# ============================================================

gram_activities = [
    ('BLOQUE 1 — OPENER (frase + TEMPLANZA día 5 CIERRA + mystery del pase Conv mismo día + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT object pronouns tabla formal + 2 órdenes + TELL/ASK exception + callback Cl 9', '~50 min'),
    ('BLOQUE 3 — LIVE: PRONOUN POSITION DRILL (pares + 8 intercambios + 3 rondas)', '~45 min'),
    ('BLOQUE 4 — CIERRE (error recap + frase close + virtud cierre + retrospective + PASE A CONV Cl 11 + tarea)', '~15 min'),
]

gram_deliverables = [
    'Foto del board final con los 3-5 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal',
    'PASE A CONV Cl 11 entregado (3 gaps gramaticales observados)',
    'Confirmar: TEMPLANZA v1 día 5 CIERRA bloque marcado',
    'Confirmar: anunciaste Cl 11 = JUSTICIA v1 día 1 ABRE',
]

gram_selfeval = [
    'Frase del Día en el board ANTES de empezar',
    'Recibí el PASE del Conv mismo día + lo trabajé en mystery',
    'ESCRIBÍ tabla object pronouns en board (me/you/him/her/it/us/them)',
    'Mostré los 2 órdenes: verb+IO+DO vs verb+DO+TO+IO',
    'Marqué la excepción TELL/ASK (no toman TO)',
    'Hice el callback Cl 9: HIS report (possessive) vs I helped HIM (object)',
    'Todo lo dicho a la clase en INGLÉS',
    'NO usé cards preparadas (todo se generó en board)',
    'CORREGÍ en board cuando un error apareció 2 veces',
    'En Bloque 3 los pares trabajaron 8 intercambios + 3 rondas',
    'Retrospective 30 seg cada uno SIN discusión',
    'PASE A CONV Cl 11 con 3 gaps gramaticales escritos',
    'NO comuniqué notas / NO mencioné metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'B1', 'B1_Clase10_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 10 de 44 — GRAMMAR',
    'OBJECT PRONOUNS tabla + 2 órdenes + TELL/ASK exception + callback Cl 9 possessives — TEMPLANZA v1 día 5 de 5 CIERRA bloque',
    gram_activities,
    gram_deliverables,
    gram_selfeval,
    S,
)

print('\nReportes B1 Cl 10 (Conv + Grammar) generados.')
