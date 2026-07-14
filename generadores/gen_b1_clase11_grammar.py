#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera PDF guia + REPORTE editable para B1 Cl 11 GRAMMAR (miercoles 13/05/2026). Juan Diego: A2 Book M12 + M13 + VIP HOTEL ACTIVITY 60min con 2 guests (invitado B2/C1 + Juan Diego en rol dual) y switch entre 2 grupos."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1_DIR = os.path.join(D, 'B1')
B1_REPORTES = os.path.join(B1_DIR, 'reportes')
os.makedirs(B1_REPORTES, exist_ok=True)

# ============================================================
# 1. PDF GUIA Cl 11 GRAMMAR (incluye ANEXO A escenarios + ANEXO B role cards)
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'GRAMATICA', 'B1_Clase11_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase11_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase11_GRAMMAR_GUIA.pdf')

# ============================================================
# 2. REPORTE Cl 11 GRAMMAR (para Juan Diego)
# ============================================================
b1_c11_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '4 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS (virtud del dia)', '5 min'),
    ('PEER TEACHER SLOT (errores del PASE de Danna)', '6 min'),
    ('LIBRO A2 M12 - Past Simple vs Past Continuous + Speed Drill', '8 min'),
    ('LIBRO A2 M13 - Already / Still / Until + Speed Drill', '8 min'),
    ('Reframe POR QUE GRABAMOS (30s) + setup VIP HOTEL', '2 min'),
    ('VIP HOTEL ACTIVITY - 2 grupos x 2 rounds + switch (CENTRAL)', '60 min'),
    ('Debrief + Grammar Pin + Error Paper Live', '7 min'),
    ('GoldList Lista 11 + Tarea + Cierre + PASE escrito a Danna', '8 min'),
]
b1_c11_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER usando errores del PASE de Danna',
    'PASE recibido de Danna (archivado)',
    'PASE escrito a Danna (foto antes de entregar - queda copia)',
    'Foto/video de VIP HOTEL ACTIVITY Round 1 (ambos grupos)',
    'Foto/video del SWITCH de guests entre grupos',
    'Foto/video de VIP HOTEL ACTIVITY Round 2 (ambos grupos)',
    'Firma o nota del invitado especial con su impresion B2/C1',
    'Papel errores fisico (anonimo)',
    '16 cuadernos GoldList Lista 11 (20 frases M12+M13+vocab hotel)',
    'Lista quienes NO entregaron las 12 oraciones de tarea Cl 10',
    'Libreta personal con 4+ errores literales + NOMBRE por grupo',
    'Nota sobre los 2 estudiantes en riesgo: produjeron M12/M13 bajo presion?',
]
b1_c11_g_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'Lei el ANEXO A escenarios + ANEXO B role cards al menos 30 min antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'RECIBI el PASE escrito de Danna ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'LEI el REFRAME POR QUE GRABAMOS antes del primer bloque grabado',
    'Cubri M12 Past Simple vs Past Continuous DESDE EL LIBRO (no inventando)',
    'Cubri M13 Already/Still/Until DESDE EL LIBRO (no inventando)',
    'NO ensene Third Conditional ni Would have/Could have (fuera de programa)',
    'Imprimi 16 role cards y las entregue a cada estudiante',
    'Conduje la VIP HOTEL ACTIVITY con 2 grupos en paralelo',
    'Hice el SWITCH de guests entre grupos a los 25 min',
    'Anote 4+ errores con NOMBRE en libreta personal durante la actividad',
    'Camine entre los 2 grupos sin interrumpir',
    'Conduje Grammar Pin con 3 preguntas orales post-actividad',
    'Camine con papel errores anonimo en Error Paper Live',
    'Conduje GoldList Lista 11 con 20 frases en tablero (M12+M13+vocab hotel)',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'ENTREGARE FISICAMENTE el PASE a Danna manana antes de su Cl 12 Conv',
    'En Tarea LEI la justificacion pedagogica (If you skip tonight...)',
    'NO acepte la excusa "no me da tiempo"',
    'Anote evidencia especifica de los 2 estudiantes en riesgo bajo presion',
]

build_report_v2(
    os.path.join(B1_REPORTES, 'B1_Clase11_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Clase 11 de 44 | BLOQUE 2: GRAMMAR & WRITING (HOY VA SEGUNDO)',
    'A2 Book M12 Past Simple vs Past Continuous + M13 Already/Still/Until + VIP HOTEL ACTIVITY 60min con 2 guests B2/C1 (invitado especial + Juan Diego rol dual profesor/guest) + switch entre 2 grupos + PASE escrito a Danna',
    b1_c11_g_act, b1_c11_g_deliv, b1_c11_g_eval, S,
)
print('OK: B1_Clase11_GRAMMAR_REPORTE.pdf')

print('\n2 PDFs generados:')
print('  - B1/B1_Clase11_GRAMMAR_GUIA.pdf  (guia + ANEXO A escenarios + ANEXO B role cards)')
print('  - B1/reportes/B1_Clase11_GRAMMAR_REPORTE.pdf  (estatico para Juan Diego)')
