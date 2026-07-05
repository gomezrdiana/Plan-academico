#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Reporte 1-hoja A2 nocturno NUEVO — Cl 2 modelo v4.1.
M2 Months and Years + preposición IN. PRUDENCIA v1 día 2."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


cl2_activities = [
    ('BLOQUE 1 — OPENER (frase + PRUDENCIA día 2 + mystery del Cl 1 + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT M2 Months + Years + preposición IN + pronunciación', '~50 min'),
    ('BLOQUE 3 — LIVE: BIRTHDAY & ANNIVERSARY EXCHANGE (pares forzando meses + IN + WILL)', '~45 min'),
    ('BLOQUE 4 — CIERRE (error recap + frase close + tarea + Cl 3 announce)', '~15 min'),
]

cl2_deliverables = [
    'Foto del board final con los 3-5 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal',
    'Confirmar: PRUDENCIA v1 día 2 de 5 marcado',
    'Confirmar: 4 inserciones de Frase del Día hechas',
    'Confirmar: anunciaste M3 Days of Month + Ordinal Numbers para Cl 3',
]

cl2_selfeval = [
    'Frase del Día en el board ANTES de empezar',
    'Escribí "PRUDENCIA" en el board grande + dije qué significa hoy',
    'Todo lo que dije a la clase fue en INGLÉS',
    'NO usé sobres, cards, grids impresos (solo board + cuaderno)',
    'ESCRIBÍ 3 columnas: MONTHS / YEARS / PREPOSITION IN',
    'Marqué que TODOS los meses van CAPITALIZADOS (regla anti-error)',
    'Enseñé las 2 formas de leer años: "twenty twenty-six" y "two thousand twenty-six"',
    'Cuando alguien dijo "on March" o "at June": dije "Prudence. Pick the right preposition."',
    'CORREGÍ en board cuando un error apareció 2 veces',
    'En Bloque 3 cada pareja produjo 5+ meses + 3+ años + 5+ preposiciones IN + 2+ WILL',
    'Hice puente con WILL + days de Cl 1 al menos 1 vez',
    'NO comuniqué notas / NO mencioné metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'A2', 'A2_Class2_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 2 de 55',
    'M2 Months and Years + preposición IN (pronunciación + capitalización + 2 formas de leer años) — PRUDENCIA v1 día 2 de 5',
    cl2_activities,
    cl2_deliverables,
    cl2_selfeval,
    S,
)

print('Reporte A2 Cl 2 generado.')
