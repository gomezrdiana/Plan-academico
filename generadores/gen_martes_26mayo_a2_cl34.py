#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 PM Nocturno Cl 34 (martes 26/05/2026):
- M36 What Are You Wearing? (Describing Clothing) + Frase del Dia + virtud JUSTICIA v2 (dia 4)
- Pasa de preguntar el PRECIO (M34) a DESCRIBIR ropa + colores + orden de adjetivos (M36)
- SIN GoldList. Reporte estatico (se llena a mano).
- NOTA INTERNA: M35 NO EXISTE en el libro - salto auditado de M34 (pag 293-300) a M36 (pag 301-306).
  Regla Heiiu: se salta al siguiente modulo existente, NUNCA se inventa. No se anuncia en clase.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_Class34_PRINT.md'), os.path.join(A2_DIR, 'A2_Class34_GUIA.pdf'))
print('OK: A2_Class34_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 33 = M34)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia + M36)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 33)', '7 min'),
    ('LIBRO M36 - What Are You Wearing? (pag 301-306)', '15 min'),
    ('SPEED DRILL - wearing + color + adj order', '15 min'),
    ('SIMULACION PROFESIONAL - Lost & Found Desk: Describe the Owner (DE PIE)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '9 min'),
    ('Tarea + Cierre + anuncio Cl 35 (M37)', '8 min'),
]
a2_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M36 ropa + colores + orden de adjetivos',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion Lost & Found Desk',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 33',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 33 M34)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'NO comente notas ni resultados del midterm (exclusivo coordinacion)',
    'Verifique virtud CL 34 = JUSTICIA v2 (dia 4, por numero de clase)',
    'Hile JUSTICIA en VATS con el patron I am wearing (lo que uno viste hacia el otro)',
    'Cubri M36 What Are You Wearing DESDE EL LIBRO (pag 301-306)',
    'Ensene Vocabulario 1 Ropa (22 prendas literales del libro pag 302)',
    'Ensene Vocabulario 2 Colores (13 colores + dark/light del libro pag 303)',
    'Ensene "I HAVE a shirt" (posesion) vs "I AM WEARING a shirt" (puesta ahora)',
    'Ensene adjetivo ANTES del sustantivo y SIN cambio de forma (red shoes, no reds shoes)',
    'Ensene modificador PRIMERO (dark blue / light blue, no blue dark)',
    'Conduje Speed Drill 15 items wearing + color + adj order en coro rapido',
    'Conduje Simulacion Lost & Found Desk: Describe the Owner con descripciones reales',
    'Simulacion fue PROFESIONAL (no familiar ni fantasiosa)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (miercoles 27/05 antes 7:00 PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 35 = M37 What Do You Look Like (cierre Justicia v2 dia 5)',
    'NO comente en clase que M35 fue saltado (nota interna - regla Heiiu se salta al siguiente existente)',
]
build_report_v2(os.path.join(A2_REP, 'A2_Class34_REPORTE.pdf'),
    'A2 NOCTURNO | Clase 34 de 55 | M36 WHAT ARE YOU WEARING | JUSTICIA v2 dia 4 | FRASE DEL DIA (Goldlist retirado) | M35 inexistente - salto auditado',
    'M36 What Are You Wearing? (Vocab Ropa 22 prendas + Vocab Colores 13 + dark/light; "I have a shirt" posesion vs "I am wearing a shirt" puesta ahora; adjetivo ANTES del sustantivo y SIN cambio de forma; modificador PRIMERO dark/light + color) + paso de preguntar el PRECIO (M34) a DESCRIBIR ropa con orden correcto de adjetivos + Lost & Found Desk Describe the Owner + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_Class34_REPORTE.pdf')

print('\n2 PDFs generados para martes 26/05 A2 PM Cl 34:')
print('  - A2/A2_Class34_GUIA.pdf')
print('  - A2/reportes/A2_Class34_REPORTE.pdf')
