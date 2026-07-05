#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Reportes 1-hoja A2 Cl 47-50 modelo v4.1. Arco repaso post-M44, bloque TEMPLANZA v3 (Cl 46-50)."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ============================================================
# A2 CL 47 — Cluster 6 — TEMPLANZA día 2
# ============================================================
build_report_v2(
    os.path.join(D, 'A2', 'A2_Class47_REPORTE.pdf'),
    'A2 NIVEL 2H | Clase 47 de 55',
    'Cluster 6 de 9 — 3rd person -s + There is/are + Causative — TEMPLANZA v3 día 2 de 5',
    [
        ('BLOQUE 1 — OPENER (frase + TEMPLANZA día 2 + mystery del Cl 46 + bridge)', '~10 min'),
        ('BLOQUE 2 — CONTENT CLUSTER 6 (3 sub-clusters + práctica pares)', '~50 min'),
        ('BLOQUE 3 — LIVE: SERVICE COORDINATION CALL (pares + rotaciones)', '~45 min'),
        ('BLOQUE 4 — CIERRE (error recap + frase close + tarea + Cl 48 announce)', '~15 min'),
    ],
    [
        'Foto del board final con los 3-5 errores típicos del día',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: TEMPLANZA v3 día 2 de 5 marcado',
        'Confirmar: 4 inserciones de Frase del Día hechas',
        'Confirmar: anunciaste Cl 48 = Cluster 7 (Reported Speech + Connectors)',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "TEMPERANCE" en el board grande + dije qué significa hoy',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
        'ESCRIBÍ 3 columnas: 3RD PERSON -S / THERE IS-ARE / CAUSATIVE',
        'Cuando alguien dijo "He go" o "I had my car fix": dije "Measure. Match the ending."',
        'CORREGÍ en board cuando un error apareció 2 veces',
        'En Bloque 3 cada pareja produjo los 3 sub-clusters en simulación',
        'Hice puente con Cl 46 (preposiciones/articulos/cuantificadores) al menos 1 vez',
        'Error paper doble protocolo (anónimo + cuaderno con nombres)',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)


# ============================================================
# A2 CL 48 — Cluster 7 — TEMPLANZA día 3
# ============================================================
build_report_v2(
    os.path.join(D, 'A2', 'A2_Class48_REPORTE.pdf'),
    'A2 NIVEL 2H | Clase 48 de 55',
    'Cluster 7 de 9 — Reported Speech (said vs told + back-shift) + Connectors (because/so/and/but/although/however/even though) — TEMPLANZA v3 día 3 de 5',
    [
        ('BLOQUE 1 — OPENER (frase + TEMPLANZA día 3 + mystery del Cl 47 + bridge)', '~10 min'),
        ('BLOQUE 2 — CONTENT CLUSTER 7 (3 sub-clusters + práctica pares)', '~50 min'),
        ('BLOQUE 3 — LIVE: WORKPLACE STATUS UPDATE CALL (triads + 3 rondas)', '~45 min'),
        ('BLOQUE 4 — CIERRE (error recap + frase close + tarea + Cl 49 announce)', '~15 min'),
    ],
    [
        'Foto del board final con los 3-5 errores típicos del día',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: TEMPLANZA v3 día 3 de 5 marcado',
        'Confirmar: 4 inserciones de Frase del Día hechas',
        'Confirmar: anunciaste Cl 49 = Cluster 8 (Conditionals + Modals)',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "TEMPERANCE" en el board grande + dije qué significa hoy',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
        'ESCRIBÍ tabla back-shift: present→past, past→past perfect, will→would',
        'Diferencia said (no objeto) vs told (con objeto) reforzada al menos 2 veces',
        'Cuando alguien dijo "He said me" o "because so": dije "Measure. One verb, one connector."',
        'CORREGÍ en board cuando un error apareció 2 veces',
        'En Bloque 3 las triads reportaron 3+ frases + 2 reasons + 1 contrast',
        'Observer contó back-shifts en cada ronda',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)


# ============================================================
# A2 CL 49 — Cluster 8 — TEMPLANZA día 4
# ============================================================
build_report_v2(
    os.path.join(D, 'A2', 'A2_Class49_REPORTE.pdf'),
    'A2 NIVEL 2H | Clase 49 de 55',
    'Cluster 8 de 9 — Conditionals 0/1/2 + Modals (can/could/should/must/might + bare verb) — TEMPLANZA v3 día 4 de 5',
    [
        ('BLOQUE 1 — OPENER (frase + TEMPLANZA día 4 + mystery del Cl 48 + bridge)', '~10 min'),
        ('BLOQUE 2 — CONTENT CLUSTER 8 (4 sub-clusters + práctica pares)', '~50 min'),
        ('BLOQUE 3 — LIVE: WORKPLACE DECISION MEETING (pares + 3 escenarios)', '~45 min'),
        ('BLOQUE 4 — CIERRE (error recap + frase close + tarea + Cl 50 announce)', '~15 min'),
    ],
    [
        'Foto del board final con los 3-5 errores típicos del día',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: TEMPLANZA v3 día 4 de 5 marcado (un día por cerrar)',
        'Confirmar: 4 inserciones de Frase del Día hechas',
        'Confirmar: anunciaste Cl 50 = Cluster 9 MASTERY INTEGRATED + cierre bloque',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "TEMPERANCE" en el board grande + dije qué significa hoy',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
        'ESCRIBÍ 4 columnas: COND 0 / COND 1 / COND 2 / MODALS',
        'Regla bare verb después de modal reforzada al menos 2 veces',
        'Cuando alguien dijo "If I will" o "I can to go": dije "Measure. Pair the IF. Pair the modal."',
        'CORREGÍ en board cuando un error apareció 2 veces',
        'En Bloque 3 cada pareja produjo 3 conditionals + 3 modales distintos',
        'Observer contó pairs correctos por ronda',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)


# ============================================================
# A2 CL 50 — MASTERY + cierre TEMPLANZA — día 5 CIERRA
# ============================================================
build_report_v2(
    os.path.join(D, 'A2', 'A2_Class50_REPORTE.pdf'),
    'A2 NIVEL 2H | Clase 50 de 55',
    'Cluster 9 de 9 — MASTERY INTEGRATED (mix de los 9 clusters Cl 42-49) — TEMPLANZA v3 día 5 de 5 CIERRA bloque',
    [
        ('BLOQUE 1 — OPENER (frase + TEMPLANZA día 5 CIERRA + mystery Cl 49 + bridge)', '~10 min'),
        ('BLOQUE 2 — MASTERY DRILLS (5 mini-rondas mezclando los 9 clusters)', '~45 min'),
        ('BLOQUE 3 — LIVE: FULL WORKPLACE DAY (1 simulación continua con 4 micro-escenas)', '~45 min'),
        ('BLOQUE 4 — CIERRE + RETROSPECTIVA (error + frase + virtud + cohort retrospective + tarea + Cl 51 announce)', '~20 min'),
    ],
    [
        'Foto del board final con los 5 errores cross-cluster del día',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: TEMPLANZA v3 día 5 CIERRA bloque marcado',
        'Confirmar: retrospectiva cohort 30 seg/cada uno SIN discusión ejecutada',
        'Confirmar: anunciaste Cl 51 = JUSTICIA v3 día 1 ABRE + prep presentaciones 1 de 2',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "TEMPERANCE" en el board grande + dije qué significa hoy (día 5 cierre)',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
        'Las 5 mini-rondas (Block 2) mezclaron clusters distintos — NO contenido nuevo',
        'Bloque 3 fue UNA simulación CONTINUA — coordinador maneja 4 escenas back-to-back sin cambio de formato',
        'Cuando un estudiante recuperó automático un patrón: dije "That is temperance in action."',
        'CORREGÍ en board cuando un error cross-cluster apareció',
        'RETROSPECTIVA: 1 palabra + 30 seg/cada uno SIN discusión SIN excepción',
        'Anuncié Cl 51 = JUSTICIA día 1 + prep presentaciones',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)


print('\nReportes A2 Cl 47, 48, 49, 50 generados.')
