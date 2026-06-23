#!/usr/bin/env python3
"""Genera REPORTES 1-hoja para A2 Cl 1 (M1 WILL + days, PRUDENCIA día 1 ABRE)
y A2 Cl 46 (Cluster 5: Prepositions + Articles + Quantifiers, TEMPLANZA v3 día 1 ABRE).

Ambos adaptados al MODELO INMERSIVO v4.1: 4 bloques largos + virtud integrada + Frase del Día
+ sin material preparado + sin GoldList + sin Shadowing como bloque + sin nombre profe."""
import os
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))


# =============================================================
# A2 CL 1 — M1 I Will Play on Monday — PRUDENCIA v1 día 1 ABRE
# =============================================================

cl1_activities = [
    ('BLOQUE 1 — OPENER + BIG REVEAL (frase + virtud + speed round)', '~10-15 min'),
    ('BLOQUE 2 — CONTENT M1 WILL + DAYS (fórmula + pares + derivación libre)', '~50 min'),
    ('BLOQUE 3 — LIVE: MY PERFECT WEEK (simulación pares 3 rotaciones)', '~35 min'),
    ('BLOQUE 4 — CIERRE + CARTA AL YO DEL FUTURO + tarea', '~20 min'),
]

cl1_deliverables = [
    'Sobres (Carta al Yo del Futuro) sellados y entregados a coordinación = estudiantes presentes',
    'Foto del board final con los 3 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal (para coordinación)',
    'Confirmar: PRUDENCIA v1 día 1 ABRE bloque (marcado en NOTAS INTERNAS)',
    'Confirmar: 4 inserciones de Frase del Día hechas',
]

cl1_selfeval = [
    'Big reveal Cl 1 en español NO se extendió más de 8 min',
    'A partir del Bloque 2 todo lo que dije a la clase fue en INGLÉS',
    'Escribí "PRUDENCIA" en el board grande + dije qué significa hoy',
    'Frase del Día en el board ANTES de empezar (no a mitad de clase)',
    'NO usé sobres, cards, grids impresos (solo board + cuaderno estudiante)',
    'En Bloque 2 los pares hablaron MÁS que yo',
    'En Bloque 3 yo coachée — NO jugué de pareja del estudiante',
    'Avancé por SEÑALES del grupo (no por reloj interno)',
    'Si alguien titubeó: dije "Piensa 2 segundos antes de hablar. Eso es prudencia."',
    'Cierre: 1 estudiante dijo la Frase del Día de memoria',
    'NO comuniqué ninguna nota (coordinación maneja resultados)',
    'NO mencioné ninguna metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'A2', 'A2_Class1_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 1 de 55',
    'M1 — I Will Play on Monday (Future WILL + Days of Week) — PRUDENCIA v1 día 1 ABRE — OPENING DAY del cohorte',
    cl1_activities,
    cl1_deliverables,
    cl1_selfeval,
    S,
)

# Adicional: anotación específica del Cl 1 al final del PDF NO es posible sin modificar build_report_v2.
# La info clave (Carta al Yo del Futuro, big reveal en español como excepción) queda capturada en
# los deliverables + selfeval arriba.


# =============================================================
# A2 CL 46 — CLUSTER 5 (Prep + Art + Quant) — TEMPLANZA v3 día 1 ABRE
# =============================================================

cl46_activities = [
    ('BLOQUE 1 — OPENER (frase + TEMPLANZA abre + 60-sec mystery Cl 45 + bridge)', '~10 min'),
    ('BLOQUE 2 — CONTENT CLUSTER 5 (3 sub-clusters: Prepositions + Articles + Quantifiers)', '~50 min'),
    ('BLOQUE 3 — LIVE: SCHEDULING & INVENTORY CALL (pares + 3 rotaciones)', '~45 min'),
    ('BLOQUE 4 — CIERRE (error recap + frase close + tarea + Cl 47 announce)', '~15 min'),
]

cl46_deliverables = [
    'Foto del board final con los 3 errores típicos del día',
    'Error paper anónimo (físico, con la guía — NO fotografiado)',
    '3 errores literales con NOMBRES en tu cuaderno personal (para coordinación)',
    'Confirmar: TEMPLANZA v3 día 1 ABRE bloque (Cl 46-50)',
    'Confirmar: 4 inserciones de Frase del Día hechas',
    'Confirmar: 3 rotaciones de simulación completas + 1 demo en frente del grupo',
]

cl46_selfeval = [
    'Frase del Día en el board ANTES de empezar (no a mitad)',
    'Escribí "TEMPERANCE" en el board grande + dije qué significa hoy',
    'Todo lo que dije a la clase fue en INGLÉS (verbos operativos en español solo para mí)',
    'NO usé sobres, cards, grids impresos (solo board + cuaderno estudiante)',
    'En Bloque 2 escribí las 3 columnas (Prepositions / Articles / Quantifiers) en board',
    'CORREGÍ en board cuando un error apareció 2 veces (no a la primera)',
    'Cuando alguien dudó: dije "Measure. Pick the right small word. That is temperance."',
    'En Bloque 3 yo coachée — NO jugué coordinator ni supplier',
    'Avancé por SEÑALES del grupo (no por reloj interno)',
    'Apliqué Plan B si algo se trabó (alertas marcadas en la guía)',
    'Cierre: 1 estudiante dijo la Frase del Día de memoria + parafraseó',
    'NO comuniqué ninguna nota (coordinación maneja resultados)',
    'NO mencioné ninguna metodología por nombre',
]

build_report_v2(
    os.path.join(D, 'A2', 'A2_Class46_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 46 de 55',
    'Cluster 5 de 9 — Prepositions (IN/ON/AT) + Articles (A/AN/THE/zero) + Quantifiers (much/many/a lot of/some/any) — TEMPLANZA v3 día 1 ABRE',
    cl46_activities,
    cl46_deliverables,
    cl46_selfeval,
    S,
)

print('\nAmbos reportes generados.')
