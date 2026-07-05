#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 43 (lunes 08/06/2026):
- ARCO DE REPASO DE ERRORES COMUNES - CLUSTER 2: COMPARATIVOS/SUPERLATIVOS + GERUNDIO vs INFINITIVO
  (-er+than / more+adj+than / as...as / the + -est / the most + adj /
   enjoy+avoid+finish + -ing / want+need+decide + to + base)
- El A2 Book termino en M44 (pag 352); Cl 41 cerro el libro; Cl 42 abrio el arco (tiempos).
  Cl 43 = segundo cluster del arco de repaso A2->B1.
- FRASE DEL DIA + virtud PRUDENCIA v3 dia 3 (Cl 41-45 = PRUDENCIA v3, calendario absoluto).
- Error Paper EXPANDIDO (6 errores, 2 por sub-cluster A/B/C).
- Tarea 20-30 min, due martes 09/06 antes 7:00 PM, NO fragmentada.
- Anuncio Cl 44 (mar 09/06): arco clase 3 = phrasal verbs + voz pasiva + PRUDENCIA v3 dia 4.
- SIN GoldList. Sin nombres. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class43_PRINT.md'), os.path.join(A2_DIR, 'A2_Class43_GUIA.pdf'))
print('OK: A2_Class43_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 42 - control de tiempos)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v3 dia 3 + comparar con criterio)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de comparativos/superlativos)', '7 min'),
    ('CORRECCION SISTEMATICA A - COMPARATIVOS (-er+than / more+adj+than / as...as + irregulares)', '13 min'),
    ('CORRECCION SISTEMATICA B - SUPERLATIVOS (the + -est / the most + adj + irregulares)', '10 min'),
    ('CORRECCION SISTEMATICA C - GERUNDIO vs INFINITIVO (enjoy/avoid/finish + -ing; want/need/decide + to)', '14 min'),
    ('SPEED DRILL - los 3 sub-clusters en velocidad (15 items + parejas)', '13 min'),
    ('SIMULACION PROFESIONAL - The Performance Review (DE PIE, comparar + decidir)', '17 min'),
    ('SHADOWING (verificar dia del ciclo)', '8 min'),
    ('Error Paper EXPANDIDO (6 errores) + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 44', '4 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Comparativos + Superlativos + Gerundio/Infinitivo + Errores',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Performance Review',
    'Foto/video Shadowing',
    'Papel errores fisico (anonimo, 6 errores EXPANDIDO) - entregado fisicamente con la guia',
    'Lista quienes NO entregaron tarea Cl 42 (las 3 partes: 10 oraciones + audio daily report + listening 5 frases)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 42)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion (comparativo + decision)',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 43 = PRUDENCIA v3 (dia 3, por numero de clase, Cl 41-45)',
    'Hile PRUDENCIA en VATS con comparar + decidir (UNA forma, no dos)',
    'ENTENDI que HOY es la SEGUNDA clase del ARCO DE REPASO (Cl 43 = arco clase 2)',
    'NO inventé contenido: el A2 Book termino en M44; hoy = CORRECCION sistematica de errores tipicos',
    'CORRECCION A: comparativos (-er+than corto / more+adj+than largo / as...as igualdad / irregulares better-worse)',
    'CORRECCION B: superlativos (the + -est corto / the most + adj largo / irregulares the best-worst / SIEMPRE con THE)',
    'CORRECCION C: gerundio vs infinitivo (enjoy/avoid/finish+-ing; want/need/decide+to+base)',
    'Conduje Speed Drill 15 items mezclando los 3 sub-clusters en coro rapido',
    'Conduje Simulacion The Performance Review forzando comparativos + superlativos + decisiones',
    'Simulacion fue PROFESIONAL (tienda u oficina, comparar 3 colaboradores + recomendar acciones)',
    'Conduje Shadowing del ciclo activo',
    'ERROR PAPER EXPANDIDO (6 errores, 2 por sub-cluster A/B/C) - anonimo en clase / libreta con nombres',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (martes 09/06 antes 7:00 PM)',
    'Tarea 20-30 min (A2), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 44 = arco clase 3 (phrasal verbs + voz pasiva + PRUDENCIA v3 dia 4)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class43_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 43 de 55 | ARCO REPASO Cl 2 - COMPARATIVOS/SUPERLATIVOS + GERUNDIO vs INFINITIVO | PRUDENCIA v3 dia 3 | FRASE DEL DIA (Goldlist retirado)',
    'ARCO DE REPASO A2->B1 - CLUSTER 2: COMPARATIVOS/SUPERLATIVOS + GERUNDIO vs INFINITIVO (-er+than / more+adj+than / as...as / the + -est / the most + adj / enjoy+avoid+finish + -ing / want+need+decide + to + base) + Speed Drill 3 sub-clusters + The Performance Review + Error Paper EXPANDIDO 6 errores + FRASE DEL DIA. El A2 Book termino en M44 (Cl 41 cerro); Cl 42 abrio el arco con tiempos; hoy Cl 43 = segundo cluster (comparar con criterio + decidir con la forma correcta). Anuncio Cl 44 = arco clase 3 (phrasal verbs + voz pasiva).',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class43_REPORTE.pdf')

print('\n2 PDFs generados para lunes 08/06 A2 PM Cl 43:')
print('  - A2/A2_Class43_GUIA.pdf')
print('  - A2/reportes/A2_Class43_REPORTE.pdf')
