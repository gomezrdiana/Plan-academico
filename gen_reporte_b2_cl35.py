#!/usr/bin/env python3
"""Reporte 1-hoja B2 Cl 35 — última clase con profesor regular antes del Final coord."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))

build_report_v2(
    os.path.join(D, 'B2', 'B2_Clase35_REPORTE.pdf'),
    'B2 NIVEL 2H | Clase 35 de 36 — ÚLTIMA CLASE',
    'FULL DRY-RUN bajo condiciones del Final + Vocab Set #27 ENTERING WITH AUTHORITY + cohort retrospectiva (cierra bloque JUSTICIA) + despedida sobria — JUSTICIA día 5 de 5 CIERRA bloque',
    [
        ('BLOQUE 1 — OPENER (frase + JUSTICIA día 5 CIERRA + mystery del Cl 34 + bridge)', '~10 min'),
        ('BLOQUE 2 — CONTENT Set #27 + dry-run rules + first-word drilling', '~35 min'),
        ('BLOQUE 3 — LIVE: FULL DRY-RUN (5-7 min monologue de memoria + 2-3 min Q&A, sin coaching)', '~55 min'),
        ('BLOQUE 4 — CIERRE + RETROSPECTIVA + DESPEDIDA (Cl 36 = coord evaluador externo, NO yo)', '~20 min'),
    ],
    [
        'Notas del dry-run por estudiante: 1 win + 1 sharpen (en cuaderno personal)',
        'Foto del board con Set #27 + dry-run rules',
        'Error paper anónimo (físico, con la guía — NO fotografiado)',
        '3 errores literales con NOMBRES en tu cuaderno personal',
        'Confirmar: JUSTICIA día 5 CIERRA bloque marcado',
        'Confirmar: retrospectiva cohort 30 seg/cada uno SIN discusión ejecutada',
        'Confirmar: Cl 36 anunciado 3 veces como Final coord externo (NO tú)',
    ],
    [
        'Frase del Día en el board ANTES de empezar',
        'Escribí "JUSTICE" en el board grande + dije qué significa hoy (día 5 cierre)',
        'Todo lo que dije a la clase fue en INGLÉS',
        'NO usé cards, grids impresos (solo board + cuaderno)',
        'ESCRIBÍ Set #27 (6 palabras): OPEN / STEP IN / CLAIM / ASSERT / PROJECT / COMMAND',
        'Cronómetro AUDIBLE durante todo el dry-run',
        'NO coaché durante el monologue de los estudiantes (solo silencio + notas)',
        'Si alguien se trabó: NO rescaté — solo "Take a breath. Continue from where you remember."',
        'ANTI-FRAUDE: monologue FROM MEMORY — NO notas, NO papel, NO celular',
        'RETROSPECTIVA: 1 palabra + 30 seg/cada uno SIN discusión SIN excepción',
        'DESPEDIDA sobria — NO emotiva, NO terapéutica',
        'NO comuniqué notas / NO mencioné metodología por nombre',
    ],
    S,
)

print('Reporte B2 Cl 35 generado.')
