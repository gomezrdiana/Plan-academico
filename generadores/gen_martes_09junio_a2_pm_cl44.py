#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 44 (martes 09/06/2026):
- ARCO DE REPASO DE ERRORES COMUNES - CLUSTER 3: PHRASAL VERBS + VOZ PASIVA
  (separables vs inseparables / posicion del pronombre objeto /
   be + past participle en 4 tiempos: presente, pasado, presente perfecto, futuro)
- El A2 Book termino en M44 (pag 352); Cl 41 cerro el libro; Cl 42 abrio el arco (tiempos);
  Cl 43 corrigio comparativos/superlativos + gerundio vs infinitivo.
  Cl 44 = tercer cluster del arco de repaso A2->B1.
- FRASE DEL DIA + virtud PRUDENCIA v3 dia 4 (Cl 41-45 = PRUDENCIA v3, calendario absoluto).
- Error Paper EXPANDIDO (6 errores: 3 phrasal verbs + 3 voz pasiva).
- Tarea 20-30 min, due miercoles 10/06 antes 7:00 PM, NO fragmentada.
- Anuncio Cl 45 (mie 10/06): arco clase 4 = preguntas/negativos/auxiliares + orden palabras
  + PRUDENCIA v3 dia 5 (ultimo dia del bloque).
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

md_to_pdf(os.path.join(A2_DIR, 'A2_Class44_PRINT.md'), os.path.join(A2_DIR, 'A2_Class44_GUIA.pdf'))
print('OK: A2_Class44_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 43 - cluster 2: comparativos/superlativos + gerundio/infinitivo)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v3 dia 4 + quien hace que / donde va cada pieza)', '5 min'),
    ('PEER TEACHER SLOT (error tipico de phrasal verb separable con pronombre)', '7 min'),
    ('CORRECCION SISTEMATICA A - PHRASAL VERBS (10 mas comunes + separables vs inseparables + posicion pronombre)', '15 min'),
    ('CORRECCION SISTEMATICA B - VOZ PASIVA (be + past participle en 4 tiempos: presente/pasado/presente perfecto/futuro)', '17 min'),
    ('SPEED DRILL - phrasal verbs + voz pasiva en velocidad (15 items + parejas)', '13 min'),
    ('SIMULACION PROFESIONAL - The Handover Briefing (DE PIE, entregar turno con phrasal verbs + voz pasiva)', '20 min'),
    ('SHADOWING (verificar dia del ciclo)', '10 min'),
    ('Error Paper EXPANDIDO (6 errores: 3 phrasal + 3 voz pasiva) + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 45', '4 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Phrasal Verbs + Voz Pasiva + Errores',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Handover Briefing',
    'Foto/video Shadowing',
    'Papel errores fisico (anonimo, 6 errores EXPANDIDO: 3 phrasal + 3 voz pasiva) - entregado fisicamente con la guia',
    'Lista quienes NO entregaron tarea Cl 43 (las 3 partes: 10 oraciones comparar+decidir + audio compare-recommend 2 min + listening 10 frases)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 43)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion (pasiva + phrasal verb con pronombre)',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 44 = PRUDENCIA v3 (dia 4, por numero de clase, Cl 41-45)',
    'Hile PRUDENCIA en VATS con quien hace que (pasiva) + donde va el pronombre (phrasal verb)',
    'ENTENDI que HOY es la TERCERA clase del ARCO DE REPASO (Cl 44 = arco clase 3)',
    'NO inventé contenido: el A2 Book termino en M44; hoy = CORRECCION sistematica de errores tipicos',
    'CORRECCION A: phrasal verbs (10 mas comunes / separables = pronombre en medio / inseparables = no se rompen)',
    'CORRECCION B: voz pasiva (be + past participle en 4 tiempos / con BEEN en presente perfecto / con BE en futuro)',
    'Conduje Speed Drill 15 items mezclando phrasal verbs (separables/inseparables) + pasiva en 4 tiempos',
    'Conduje Simulacion The Handover Briefing forzando phrasal verbs + pasiva (past + pres. perf. + future)',
    'Simulacion fue PROFESIONAL (tienda u oficina, entregar turno + colega hace 2 preguntas que fuerzan formas)',
    'Conduje Shadowing del ciclo activo',
    'ERROR PAPER EXPANDIDO (6 errores: 3 phrasal verbs + 3 voz pasiva) - anonimo en clase / libreta con nombres',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (miercoles 10/06 antes 7:00 PM)',
    'Tarea 20-30 min (A2), NO fragmentada',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 45 = arco clase 4 (preguntas/negativos/auxiliares + orden palabras + PRUDENCIA v3 dia 5)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class44_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 44 de 55 | ARCO REPASO Cl 3 - PHRASAL VERBS + VOZ PASIVA | PRUDENCIA v3 dia 4 | FRASE DEL DIA (Goldlist retirado)',
    'ARCO DE REPASO A2->B1 - CLUSTER 3: PHRASAL VERBS + VOZ PASIVA (10 phrasal verbs mas comunes / separables vs inseparables / posicion del pronombre objeto / be + past participle en 4 tiempos: presente, pasado, presente perfecto, futuro) + Speed Drill 2 sub-clusters + The Handover Briefing + Error Paper EXPANDIDO 6 errores (3+3) + FRASE DEL DIA. El A2 Book termino en M44 (Cl 41 cerro); Cl 42 abrio el arco con tiempos; Cl 43 corrigio comparar+decidir; hoy Cl 44 = tercer cluster (entregar informacion profesional con la voz correcta y el phrasal verb bien armado). Anuncio Cl 45 = arco clase 4 (preguntas/negativos/auxiliares + orden palabras).',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class44_REPORTE.pdf')

print('\n2 PDFs generados para martes 09/06 A2 PM Cl 44:')
print('  - A2/A2_Class44_GUIA.pdf')
print('  - A2/reportes/A2_Class44_REPORTE.pdf')
