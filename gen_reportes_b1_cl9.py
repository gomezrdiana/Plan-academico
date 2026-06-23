#!/usr/bin/env python3
"""Reportes 1-hoja B1 Mastery Cl 9 — Conv + Grammar, modelo v4.1."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# B1 CL 9 CONV — POSSESSIVES oral — TEMPLANZA v1 día 4
# ============================================================

conv_activities = [
    ('BLOQUE 1 — OPENER (frase + TEMPLANZA día 4 + mystery del Cl 8 + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT POSSESSIVES oral (adj + \'s + of + whose) en pares', '~50 min'),
    ('BLOQUE 3 — LIVE: OFFICE OBJECT OWNERSHIP DISPUTE (pares + 3 rotaciones)', '~45 min'),
    ('BLOQUE 4 — CIERRE (error recap + frase close + PASE A GRAMMAR + tarea)', '~15 min'),
]

conv_deliverables = [
    'Foto del board final con los 3-5 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal',
    'PASE A GRAMMAR Cl 9 entregado (3 gaps observados oralmente)',
    'Confirmar: TEMPLANZA v1 día 4 de 5 marcado',
    'Confirmar: 4 inserciones de Frase del Día hechas',
]

conv_selfeval = [
    'Frase del Día en el board ANTES de empezar',
    'Escribí "TEMPERANCE" en el board grande + dije qué significa hoy',
    'Todo lo que dije a la clase fue en INGLÉS (operativos en español solo para mí)',
    'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
    'En Bloque 2 los pares hablaron más que yo',
    'En Bloque 3 yo coachée — NO jugué de pareja del estudiante',
    'Cuando alguien dudó: dije "Measure. Whose is it? Pick the right form."',
    'CORREGÍ en board cuando un error apareció 2 veces (no a la primera)',
    'Avancé por SEÑALES del grupo (no por reloj interno)',
    'PASE A GRAMMAR Cl 9 con 3 gaps orales escritos',
    'Cierre: 1 estudiante dijo la Frase del Día de memoria',
    'NO comuniqué notas / NO mencioné metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'B1', 'B1_Clase9_CONV_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 de 44 — CONV',
    'POSSESSIVES oral (adj + \'s + of + whose) — TEMPLANZA v1 día 4 de 5 — Block stays open',
    conv_activities,
    conv_deliverables,
    conv_selfeval,
    S,
)


# ============================================================
# B1 CL 9 GRAMMAR — POSSESSIVES tabla formal — TEMPLANZA día 4
# ============================================================

gram_activities = [
    ('BLOQUE 1 — OPENER (frase + TEMPLANZA día 4 + mystery del pase Conv + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT POSSESSIVES tabla formal (4 formas + spelling rules)', '~50 min'),
    ('BLOQUE 3 — LIVE: POSSESSIVES INTERROGATIVE drill (pares + 8 intercambios)', '~45 min'),
    ('BLOQUE 4 — CIERRE (error recap + frase close + PASE A CONV Cl 10 + tarea)', '~15 min'),
]

gram_deliverables = [
    'Foto del board final con los 3-5 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal',
    'PASE A CONV Cl 10 entregado (3 gaps observados gramaticales)',
    'Confirmar: TEMPLANZA v1 día 4 de 5 marcado',
    'Confirmar: 4 inserciones de Frase del Día hechas',
]

gram_selfeval = [
    'Frase del Día en el board ANTES de empezar',
    'Recibí el PASE del Conv mismo día + lo trabajé en mystery',
    'ESCRIBÍ las 4 formas de posesivo en board grande (my/his/her/etc + \'s + of + whose)',
    'Spelling rules explicados (boss\'s / bosses\' / children\'s)',
    'Todo lo dicho a la clase en INGLÉS',
    'NO usé cards preparadas (todo se generó en board)',
    'CORREGÍ en board cuando un error apareció 2 veces',
    'Diferencia "who\'s" vs "whose" reforzada al menos 2 veces',
    'En Bloque 3 los pares trabajaron 8 intercambios sin que yo interrumpiera',
    'Cuando alguien dudó: dije "Measure. Pick the right form. That is temperance."',
    'PASE A CONV Cl 10 con 3 gaps gramaticales escritos',
    'NO comuniqué notas / NO mencioné metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'B1', 'B1_Clase9_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 9 de 44 — GRAMMAR',
    'POSSESSIVES tabla formal (adj + \'s + of + whose + spelling rules) — TEMPLANZA v1 día 4 de 5',
    gram_activities,
    gram_deliverables,
    gram_selfeval,
    S,
)

print('\nReportes B1 Cl 9 (Conv + Grammar) generados.')
