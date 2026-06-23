#!/usr/bin/env python3
"""Genera PDF + reporte para A2 4h Cl 16 (miercoles 13/05/2026). M34 + M36 (saltando M35) + Depuracion Lista 2. Vuelta a 2 modulos por clase."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(D, 'A2')
A2_REPORTES = os.path.join(A2_DIR, 'reportes')

os.makedirs(A2_REPORTES, exist_ok=True)

# GUIA Cl 16
md_to_pdf(
    os.path.join(A2_DIR, 'A2_4h_Class16_PRINT.md'),
    os.path.join(A2_DIR, 'A2_4h_Class16_GUIA.pdf'),
)

# REPORTE Cl 16
a2_c16_act = [
    ('MYSTERY HOMEWORK CHECK (sobre cerrado)', '5 min'),
    ('EL POR QUE DE HOY (bloque explicativo)', '2 min'),
    ('VATS Fortaleza dia 1 (v1)', '5 min'),
    ('PEER TEACHER SLOT (errores M33 Cl 15)', '7 min'),
    ('Tarea Check Cl 15', '5 min'),
    ('DEPURACION GOLDLIST LISTA 2 (Modelo D limpio)', '15 min'),
    ('VOCABULARY UPGRADE A2-tier para M34 + M36', '15 min'),
    ('LIBRO M34 How Much Does It Cost + Speed Drill', '22 min'),
    ('SIMULACION PROFESIONAL M34 - preguntar precios (DE PIE)', '25 min'),
    ('LIBRO M36 What Are You Wearing + vocab clothing/colors', '25 min'),
    ('Historia interactiva M34+M36 - "La compra del traje"', '10 min'),
    ('SIMULACION INTEGRADA M34+M36 - comprar ropa (DE PIE)', '30 min'),
    ('SHADOWING DIA 3 - Presentacion mini-competencia grupal', '12 min'),
    ('Free production M34+M36 (parejas DE PIE)', '18 min'),
    ('Error Paper Live (peer relay)', '8 min'),
    ('Tarea + Cierre + anuncio M37 jueves', '16 min'),
]
a2_c16_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE del Mystery Homework Check',
    'Foto/video del PEER TEACHER en accion',
    'Foto de Lista 2 de TODOS los cuadernos con cruces',
    'Numero de tachadas por estudiante (comparar con Cl 15 Lista 1)',
    'Foto del cuaderno con seccion "D1 of List 2" iniciada',
    'Foto del tablero del WORD UPGRADE M34 + M36',
    'Foto/video de la Simulacion M34 (preguntar precios)',
    'Foto/video de la Simulacion INTEGRADA M34+M36 (compra de ropa, material redes)',
    'Foto/video de Shadowing Dia 3 mini-competencia',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 15',
    'Tu libreta personal con 3 errores literales + NOMBRE por bloque',
    'Notas de tu energia hoy - como funciono volver a 2 modulos',
]
a2_c16_eval = [
    'Lei el mensaje pedagogico al inicio ANTES de clase',
    'HABLE 100% EN INGLES durante todo el bloque',
    'LEI el bloque EL POR QUE DE HOY al inicio (2 min completos)',
    'EXPLIQUE EL OBJETIVO de cada actividad ANTES de empezarla',
    'APLIQUE consolidacion antes de complejidad',
    'PROYECTE seguridad (preparacion previa, ritmo)',
    'PREPARE el SOBRE del Mystery Homework Check ANTES de clase',
    'Conduje MYSTERY HOMEWORK CHECK llamando al azar',
    'ASIGNE estudiante de PEER TEACHER con anticipacion',
    'NO permiti escritura Lista nueva hoy (Modelo D limpio - solo depuracion Lista 2)',
    'Conduje DEPURACION Lista 2 con el mismo procedimiento de Cl 15',
    'Tome foto de TODAS las Listas 2 con cruces',
    'Conte tachadas por estudiante y compare con Cl 15 Lista 1',
    'ESCRIBI WORD UPGRADE M34 + M36 en 2 secciones del tablero ANTES de clase',
    'Cubri M34 How Much Does It Cost DESDE EL LIBRO (no inventando)',
    'Cubri M36 What Are You Wearing DESDE EL LIBRO (saltando M35)',
    'Hice INTEGRACION M34 + M36 en la SIMULACION DE COMPRA DE ROPA',
    'Conduje SIMULACION INTEGRADA moviendo sillas para crear 3 tiendas',
    'Conduje Shadowing Dia 3 como mini-competencia con voting',
    'Simulaciones fueron PROFESIONALES/realistas (no temas familiares)',
    'NO acepte la excusa "no me da tiempo" para no hacer tarea',
    'Camine con papel de errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'Anuncie M37 para jueves Cl 17 (verificar libro)',
    'Anote como funciono volver a 2 modulos vs 1 (feedback para coordinacion)',
]

build_report_v2(
    os.path.join(A2_REPORTES, 'A2_4h_Class16_REPORTE.pdf'),
    'A2 INTENSIVO | Clase 16 de 28 | 4 HORAS | M34 + M36 + DEPURACION LISTA 2 | VUELTA A 2 MODULOS',
    'M34 How Much Does It Cost (Prices) + M36 What Are You Wearing (Clothing) saltando M35 + Depuracion Lista 2 + Shadowing Dia 3 | Fortaleza dia 1 (v1)',
    a2_c16_act, a2_c16_deliv, a2_c16_eval, S,
)
print('OK: A2_4h_Class16_REPORTE.pdf')

print('\n2 PDFs generados:')
print('  - A2/A2_4h_Class16_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class16_REPORTE.pdf')
