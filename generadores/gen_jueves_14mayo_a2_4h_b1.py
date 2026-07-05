#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera 3 guias + 3 reportes para clases del jueves 14/05/2026:
- A2 4hr AM Cl 17 (Tomas)   - M37 What Do You Look Like + M38 Order of Adjectives + Depuracion Lista 3 + Nuevo Shadowing
- B1 Mastery Cl 12 Grammar (Juan Diego) - A2 M14 While/During/Again + M15 Present Perfect Regular formal + Integration past
- B1 Mastery Cl 12 Conv (Danna)         - Bridge formal->casual con Present Perfect en Job Interview + Page 11 draft 1
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
B1_DIR = os.path.join(D, 'B1')
A2_REP = os.path.join(A2_DIR, 'reportes')
B1_REP = os.path.join(B1_DIR, 'reportes')
for r in (A2_REP, B1_REP):
    os.makedirs(r, exist_ok=True)

# ============================================================
# A2 4hr AM Cl 17 - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class17_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Class17_GUIA.pdf'),
)
print('OK: A2_4h_Class17_GUIA.pdf')

a2_4h_c17_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('VATS FORTALEZA dia 2 (v1)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 16)', '7 min'),
    ('Tarea Check Cl 16', '5 min'),
    ('DEPURACION GOLDLIST LISTA 3 (Modelo D)', '15 min'),
    ('VOCABULARY UPGRADE A2-tier M37 + M38', '15 min'),
    ('LIBRO M37 What Do You Look Like + Speed Drill', '20 min'),
    ('SIMULACION M37 - Police Composite Sketch (DE PIE)', '25 min'),
    ('LIBRO M38 Order of Adjectives (OSAS COMP)', '25 min'),
    ('Historia interactiva M37+M38 - The Mysterious Neighbor', '10 min'),
    ('SIMULACION INTEGRADA M37+M38 - Missing Person Report (DE PIE)', '30 min'),
    ('SHADOWING NUEVO CICLO Dia 1 (video nuevo)', '12 min'),
    ('Free production M37+M38 con 6 fotos (DE PIE)', '18 min'),
    ('Error Paper Live (peer relay)', '8 min'),
    ('Tarea + Cierre + anuncio M39 viernes', '16 min'),
]
a2_4h_c17_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto del tablero - M37 vocabulary + M38 OSAS COMP',
    'Foto de Lista 3 de TODOS los cuadernos con cruces',
    'Numero de tachadas por estudiante (comparar con Cl 16 Lista 2)',
    'Foto del cuaderno con seccion "D1 of List 3" iniciada',
    'Foto/video Police Composite Sketch (con dibujos hechos por estudiantes)',
    'Foto/video Missing Person Report (integracion M37+M38)',
    'Foto/video Free Production con las 6 fotos',
    'Foto/video Shadowing nuevo ciclo Dia 1',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 16',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Notas sobre como funciono la integracion M37+M38',
]
a2_4h_c17_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'NO permiti escritura Lista nueva hoy (Modelo D - solo depuracion Lista 3)',
    'Conduje DEPURACION Lista 3 con el mismo procedimiento de Cl 15-16',
    'Tome foto de TODAS las Listas 3 con cruces',
    'Conte tachadas por estudiante y compare con Cl 16 Lista 2',
    'ESCRIBI M37 vocabulary + M38 OSAS COMP en tablero ANTES de clase',
    'Cubri M37 What Do You Look Like DESDE EL LIBRO (no inventando)',
    'Cubri M38 Order of Adjectives DESDE EL LIBRO con OSAS COMP completo',
    'Conduje Police Composite Sketch con estudiantes dibujando',
    'Conduje Missing Person Report integrando M37+M38 con multiples adjetivos',
    'Conduje Shadowing NUEVO ciclo Dia 1 (no Dia 3 del ciclo anterior)',
    'Simulaciones fueron PROFESIONALES/realistas (no fantasiosas)',
    'NO acepte la excusa "no me da tiempo" para no hacer tarea',
    'Camine con papel de errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'Anuncie M39 para viernes Cl 18',
    'Anote feedback sobre integracion M37+M38 (que funciono / que no)',
]

build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class17_REPORTE.pdf'),
    'A2 INTENSIVO | Cl 17 de 28 | 4 HORAS | M37 + M38 + DEPURACION LISTA 3 + NUEVO SHADOWING',
    'M37 What Do You Look Like (physical description) + M38 Order of Adjectives (OSAS COMP) + Police Sketch + Missing Person Report + Depuracion Lista 3 + Shadowing Dia 1 nuevo ciclo + FORTALEZA dia 2 v1',
    a2_4h_c17_act, a2_4h_c17_deliv, a2_4h_c17_eval, S,
)
print('OK: A2_4h_Class17_REPORTE.pdf')

# ============================================================
# B1 Cl 12 Grammar - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase12_GRAMMAR_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase12_GRAMMAR_GUIA.pdf'),
)
print('OK: B1_Clase12_GRAMMAR_GUIA.pdf')

b1_c12_g_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '4 min'),
    ('EL POR QUE DE HOY', '3 min'),
    ('VATS JUSTICIA dia 2 (v1)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 11 VIP Hotel)', '7 min'),
    ('Tarea Check Cl 11', '5 min'),
    ('LIBRO M14 - While/During/Again + Speed Drill', '15 min'),
    ('LIBRO M15 - Present Perfect Regular formalizacion', '15 min'),
    ('INTEGRACION DEL PASADO COMPLETO (M12+M13+M14+M15)', '15 min'),
    ('SIMULACION PROFESIONAL - Yesterday Conference (DE PIE)', '15 min'),
    ('GoldList Lista 12 (20 frases M14+M15)', '10 min'),
    ('Error Paper Live', '7 min'),
    ('PASE ESCRITO a Danna + Tarea + Cierre', '9 min'),
]
b1_c12_g_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER usando errores VIP Hotel',
    'PASE escrito a Danna (foto antes de entregar)',
    'Foto del tablero - M14 + M15 + Integration template',
    'Foto/video Yesterday Conference simulation',
    'Papel errores fisico (anonimo)',
    '16 cuadernos GoldList Lista 12 (20 frases M14+M15)',
    'Lista quienes NO entregaron tarea Cl 11',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Notas sobre como manejaron la integracion 4 piezas del pasado',
]
b1_c12_g_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'Cubri M14 While/During/Again DESDE EL LIBRO (linea 8983)',
    'Cubri M15 Present Perfect Regular DESDE EL LIBRO (linea 9739) - formalizacion',
    'NO ensene Third Conditional ni Could/Should have (fuera de programa)',
    'Hice INTEGRACION explicita M12+M13+M14+M15 (4 piezas del pasado)',
    'Conduje Yesterday Conference simulation con narrativa real del VIP Hotel ayer',
    'Conduje GoldList Lista 12 con 20 frases (M14+M15)',
    'En libreta personal anote 3 errores con NOMBRE',
    'Camine con papel errores anonimo',
    'ESCRIBI el PASE a Danna con 3 errores literales + nota tecnica',
    'ENTREGARE FISICAMENTE el PASE a Danna ANTES de su Cl 12 Conv',
    'En Tarea explique pedagogicamente el por que (If you skip tonight...)',
    'NO acepte la excusa "no me da tiempo"',
    'Anote evidencia sobre como manejaron la integracion 4 piezas',
    'Anuncie M16 Present Perfect Irregular para Cl 13 viernes',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase12_GRAMMAR_REPORTE.pdf'),
    'B1 MASTERY | Cl 12 de 44 | BLOQUE 1: GRAMMAR (HOY VA PRIMERO)',
    'A2 Book M14 While/During/Again + M15 Present Perfect Regular (formalizacion) + Integracion 4 piezas del pasado (M12-M15) + Yesterday Conference simulation + PASE escrito a Danna',
    b1_c12_g_act, b1_c12_g_deliv, b1_c12_g_eval, S,
)
print('OK: B1_Clase12_GRAMMAR_REPORTE.pdf')

# ============================================================
# B1 Cl 12 Conv - GUIA + REPORTE
# ============================================================
md_to_pdf(
    os.path.join(B1_DIR, 'B1_Clase12_CONV_PRINT.md'),
    os.path.join(B1_DIR, 'B1_Clase12_CONV_GUIA.pdf'),
)
print('OK: B1_Clase12_CONV_GUIA.pdf')

b1_c12_c_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('VATS JUSTICIA dia 2 (v1)', '7 min'),
    ('PEER TEACHER SLOT (PASE de Juan Diego - Grammar M14+M15)', '7 min'),
    ('Reframe Por Que Grabamos + Bridge formal->casual intro', '2 min'),
    ('HOT TOPIC PROFUNDO - texto First-Time Experiences segunda lectura', '17 min'),
    ('SIMULACION PROFESIONAL - Job Interview Present Perfect (DE PIE)', '20 min'),
    ('SHADOWING', '15 min'),
    ('PROJECT WORKSHOP Page 11 - ESCRITURA borrador narrative (anti-fraude)', '18 min'),
    ('Mini-Pitch + Q&A en vivo', '10 min'),
    ('Error Paper Live + PASE a Juan Diego + Tarea + Cierre', '7 min'),
]
b1_c12_c_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER usando PASE',
    'PASE recibido de Juan Diego (archivado)',
    'PASE escrito a Juan Diego (foto antes de entregar)',
    'Foto/video del Hot Topic profundo (segunda lectura del texto)',
    'Foto/video Job Interview simulation (bridge formal->casual)',
    'Foto/video Shadowing',
    '16 Paginas 11 del proyecto NARRATIVE DRAFT 1 (foto - escritura en clase)',
    'Foto/video Mini-Pitch',
    'Papel errores fisico (anonimo)',
    'Libreta personal con 3 errores literales + NOMBRE por bloque',
    'Notas operativas sobre los 2 estudiantes en riesgo (Yuli y Vanessa) en Job Interview',
]
b1_c12_c_eval = [
    'Lei la guia COMPLETA al menos 1 hora antes',
    'HABLE 100% EN INGLES durante todo el bloque',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'PROYECTE seguridad',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'RECIBI el PASE escrito de Juan Diego ANTES de mi bloque',
    'ASIGNE estudiante de PEER TEACHER con errores del PASE',
    'LEI el REFRAME POR QUE GRABAMOS antes del primer bloque grabado',
    'EXPLIQUE el bridge formal->casual ANTES de Job Interview',
    'Conduje Hot Topic PROFUNDO (no repeti dinamica de Cl 11)',
    'Conduje Job Interview con preguntas Present Perfect-based del banco',
    'Cada estudiante uso Present Perfect en registro casual (no monologo)',
    'Conduje escritura Page 11 EN CLASE (anti-fraude IA)',
    'En libreta personal anote 3 errores con NOMBRE por estudiante',
    'Camine con papel errores anonimo',
    'ESCRIBI el PASE a Juan Diego con 3 errores literales + nota tecnica',
    'En Tarea explique pedagogicamente el por que',
    'NO acepte la excusa "no me da tiempo"',
    'Anote evidencia especifica de los 2 estudiantes en riesgo en Job Interview',
    'Estudiantes hablaron 80%+ del tiempo',
]

build_report_v2(
    os.path.join(B1_REP, 'B1_Clase12_CONV_REPORTE.pdf'),
    'B1 MASTERY | Cl 12 de 44 | BLOQUE 2: CONVERSACIONAL (HOY VA SEGUNDO)',
    'Bridge formal->casual Present Perfect + Job Interview simulation + Hot Topic profundo texto First-Time Experiences + Page 11 NARRATIVE DRAFT 1 (escritura en clase anti-fraude) + PASE de y para Juan Diego',
    b1_c12_c_act, b1_c12_c_deliv, b1_c12_c_eval, S,
)
print('OK: B1_Clase12_CONV_REPORTE.pdf')

print('\n6 PDFs generados:')
print('  - A2/A2_4h_Class17_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class17_REPORTE.pdf')
print('  - B1/B1_Clase12_GRAMMAR_GUIA.pdf')
print('  - B1/reportes/B1_Clase12_GRAMMAR_REPORTE.pdf')
print('  - B1/B1_Clase12_CONV_GUIA.pdf')
print('  - B1/reportes/B1_Clase12_CONV_REPORTE.pdf')
