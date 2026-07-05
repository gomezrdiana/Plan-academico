#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Reportes 1-hoja A2 nocturno NUEVO — Cl 3, Cl 4, Cl 5 modelo v4.1.
PRUDENCIA v1 bloque (Cl 1-5). Cl 5 cierra bloque, Cl 6 abre TEMPLANZA."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ============================================================
# A2 CL 3 — M3 Days of Month + Ordinals — PRUDENCIA día 3
# ============================================================

cl3_activities = [
    ('BLOQUE 1 — OPENER (frase + PRUDENCIA día 3 + mystery del Cl 2 + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT M3 ordinales 1st-31st + fechas (AM vs BR) + lectura aloud', '~50 min'),
    ('BLOQUE 3 — LIVE: SCHEDULING THE NEXT MONTH (pares + rotaciones)', '~45 min'),
    ('BLOQUE 4 — CIERRE (error recap + frase close + tarea + Cl 4 announce)', '~15 min'),
]

cl3_deliverables = [
    'Foto del board final con los 3-5 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal',
    'Confirmar: PRUDENCIA v1 día 3 de 5 marcado',
    'Confirmar: 4 inserciones de Frase del Día hechas',
    'Confirmar: anunciaste M5 Future Triplicate para Cl 4',
]

cl3_selfeval = [
    'Frase del Día en el board ANTES de empezar',
    'Escribí "PRUDENCIA" en el board grande + dije qué significa hoy',
    'Todo lo que dije a la clase fue en INGLÉS',
    'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
    'ESCRIBÍ 3 columnas: ORDINALS / DATES PATTERN / READING DATES',
    'Marqué los 5 irregulares: 1st / 2nd / 3rd / 9th / 12th',
    'Diferencia American (May 5th) vs British (the 5th of May) explicada',
    'Cuando alguien dudó: dije "Prudence. Pick the ordinal before the date."',
    'CORREGÍ en board cuando un error apareció 2 veces',
    'En Bloque 3 los pares produjeron 5+ fechas habladas y 3+ escritas',
    'Hice puente con WILL + days de Cl 1 al menos 1 vez',
    'NO comuniqué notas / NO mencioné metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'A2', 'A2_Class3_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 3 de 55',
    'M3 Days of Month + Ordinal Numbers (1st-31st + American/British format + reading aloud) — PRUDENCIA v1 día 3 de 5',
    cl3_activities,
    cl3_deliverables,
    cl3_selfeval,
    S,
)


# ============================================================
# A2 CL 4 — M5 Future Triplicate — PRUDENCIA día 4
# ============================================================

cl4_activities = [
    ('BLOQUE 1 — OPENER (frase + PRUDENCIA día 4 + mystery del Cl 3 + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT M5 Future Triplicate (WILL / GOING TO / Present Cont) + triggers + práctica', '~50 min'),
    ('BLOQUE 3 — LIVE: NEXT QUARTER WORKPLACE PLAN (pares forzando los 3 futuros)', '~45 min'),
    ('BLOQUE 4 — CIERRE (error recap + frase close + tarea + Cl 5 cierre announce)', '~15 min'),
]

cl4_deliverables = [
    'Foto del board final con los 3-5 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal',
    'Confirmar: PRUDENCIA v1 día 4 de 5 marcado',
    'Confirmar: 4 inserciones de Frase del Día hechas',
    'Confirmar: anunciaste Cl 5 = M6 Right on Time + cierre bloque PRUDENCIA',
]

cl4_selfeval = [
    'Frase del Día en el board ANTES de empezar',
    'Escribí "PRUDENCIA" en el board grande + dije qué significa hoy',
    'Todo lo que dije a la clase fue en INGLÉS',
    'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
    'ESCRIBÍ 3 columnas: WILL / GOING TO / PRESENT CONTINUOUS',
    'Trigger de cada futuro explicado claro (spontáneo / pre-decidido / arreglo fijo)',
    'Cuando alguien usó futuro equivocado: dije "Prudence. Which future fits?"',
    'CORREGÍ en board cuando un error apareció 2 veces',
    'En Bloque 3 cada pareja produjo MIN 3 sentencias con cada uno de los 3 futuros',
    'Hice puente con WILL de Cl 1 al menos 1 vez (no es el único futuro)',
    'NOTAS INTERNAS mencionan M4 SALTADO (regla libro: nunca inventar)',
    'NO comuniqué notas / NO mencioné metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'A2', 'A2_Class4_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 4 de 55',
    'M5 The Future in Triplicate (WILL spontáneo + GOING TO pre-decidido + PRESENT CONTINUOUS arreglo fijo) — M4 SALTADO — PRUDENCIA v1 día 4 de 5',
    cl4_activities,
    cl4_deliverables,
    cl4_selfeval,
    S,
)


# ============================================================
# A2 CL 5 — M6 Schedules — PRUDENCIA día 5 CIERRA + retro
# ============================================================

cl5_activities = [
    ('BLOQUE 1 — OPENER (frase + PRUDENCIA día 5 CIERRA + mystery del Cl 4 + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT M6 Schedules (Present Simple para timetables vs Present Cont personal)', '~50 min'),
    ('BLOQUE 3 — LIVE: TRAVEL & SCHEDULE INFO CALL (pares + rotaciones reducidas)', '~38 min'),
    ('BLOQUE 4 — CIERRE + CARTA AL YO DEL FUTURO (error + frase + virtud + Carta 12 min + tarea + Cl 6 announce)', '~22 min'),
]

cl5_deliverables = [
    'CUENTA: sobres Carta al Yo del Futuro sellados = estudiantes presentes',
    'ENTREGA los sobres a coordinación HOY (no se llevan a casa)',
    'Foto del board final con los 3-5 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal',
    'Confirmar: PRUDENCIA v1 día 5 CIERRA bloque marcado',
    'Confirmar: anunciaste Cl 6 = TEMPLANZA v1 día 1 ABRE + M7 Might',
]

cl5_selfeval = [
    'Frase del Día en el board ANTES de empezar',
    'Escribí "PRUDENCIA" en el board grande + dije qué significa hoy (día 5 cierre)',
    'Todo lo que dije a la clase fue en INGLÉS',
    'NO usé sobres, cards, grids impresos (incluido sobres de la Carta — se doblan en clase)',
    'ESCRIBÍ 2 columnas: SCHEDULES (Present Simple) vs PERSONAL PLANS (Present Cont)',
    'Cuando alguien usó forma mal: dije "Prudence. Whose time is this — yours or the schedule\'s?"',
    'CORREGÍ en board cuando un error apareció 2 veces',
    'Hice puente con Cl 4 (contraste schedules vs arrangements)',
    'CARTA AL YO DEL FUTURO: DEMOSTRÉ el doblez en mi hoja primero (~30 seg)',
    'CARTA: 8 min de escritura en silencio, NO leí su contenido',
    'CARTA: RECOGÍ todos los sobres + CONTÉ contra estudiantes presentes',
    'CARTA: ENTREGÉ los sobres a coordinación al final del día (no se llevan a casa)',
    'NO comuniqué notas / NO mencioné metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'A2', 'A2_Class5_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 5 de 55',
    'M6 Right on Time! / Scheduled Events (Present Simple para timetables vs Present Continuous personal) — PRUDENCIA v1 día 5 de 5 CIERRA bloque',
    cl5_activities,
    cl5_deliverables,
    cl5_selfeval,
    S,
)

print('\nReportes A2 Cl 3, Cl 4, Cl 5 generados.')
