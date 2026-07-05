#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 35 (miercoles 27/05/2026):
- M37 What Do You Look Like? (Describing People) + Frase del Dia + virtud JUSTICIA v2 (dia 5, ULTIMO dia del bloque)
- Pasa de describir ROPA (M36) a describir como ES / como SE VE una persona (M37: have + be + amplificadores very/somewhat + 4 usos de "like")
- SIN GoldList. Reporte estatico (se llena a mano).
- ANUNCIO CL 36 = cambio de virtud: JUSTICIA v2 -> FORTALEZA v2 dia 1.
- M37 verificado en A2 Book.md (pag 307-312: vocab partes del cuerpo + adjetivos personales + Guia 1 What Are You Like? + Ejemplos Describiendo a la Gente).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class35_PRINT.md'), os.path.join(A2_DIR, 'A2_Class35_GUIA.pdf'))
print('OK: A2_Class35_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 34 = M36)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia dia 5 + M37)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 34)', '7 min'),
    ('LIBRO M37 - look like + have/be (pag 307-312)', '15 min'),
    ('SPEED DRILL - describir personas (have / be + very/somewhat)', '15 min'),
    ('SIMULACION PROFESIONAL - The Reception Desk ID Check (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio Cl 36 (CAMBIO de virtud JUSTICIA -> FORTALEZA)', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M37 look like + have/be + adjetivos',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Reception Desk ID Check',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 34',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Confirmacion: anuncio de cambio de virtud (Justicia -> Fortaleza) hecho al cierre',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 34 M36)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 35 = JUSTICIA v2 dia 5 (ULTIMO dia del bloque 31-35)',
    'Hile JUSTICIA dia 5 en VATS con el patron what do you look like (equidad sin dos caras)',
    'Cubri M37 What Do You Look Like DESDE EL LIBRO (pag 307-312)',
    'Ensene los 4 usos de "like" (gustar / como / personalidad / apariencia + How are you = mood SIN like)',
    'Ensene "to have" para pelo, barba y partes del cuerpo (She has long hair)',
    'Ensene "to be" para adjetivos fisicos (She is tall / slender / strong)',
    'Ensene amplificadores "very" y "somewhat" - uno solo, nunca los dos juntos',
    'Conduje Speed Drill 15 items describir personas have/be en coro rapido',
    'Conduje Simulacion The Reception Desk ID Check con look like + have/be reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (jueves 28/05 antes 7:00 PM)',
    'NO acepte la excusa "no me da tiempo"',
    'AL CIERRE anuncie cambio de virtud: manana Cl 36 = FORTALEZA v2 dia 1 (cierre simbolico del bloque JUSTICIA)',
    'Anuncie Cl 36 = siguiente modulo del libro (auditado antes; en clase NO se promete M38 hasta confirmacion)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class35_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 35 de 55 | M37 WHAT DO YOU LOOK LIKE | JUSTICIA v2 dia 5 ULTIMO | CIERRE bloque - manana FORTALEZA v2 dia 1 | FRASE DEL DIA (Goldlist retirado)',
    'M37 What Do You Look Like? (4 usos de "like" / to have para pelo + partes del cuerpo + barba / to be para adjetivos fisicos / amplificadores very-somewhat nunca juntos) + paso de describir ROPA (M36) a describir como ES y SE VE la persona + The Reception Desk ID Check + FRASE DEL DIA + ANUNCIO cambio virtud JUSTICIA -> FORTALEZA al cierre',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class35_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 27/05 A2 PM Cl 35:')
print('  - A2/A2_Class35_GUIA.pdf')
print('  - A2/reportes/A2_Class35_REPORTE.pdf')
