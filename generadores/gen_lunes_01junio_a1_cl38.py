#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 38 (lunes 01/06/2026):
- Post-M35 (A1 Book termino en M35; Cl 34-44 = consolidacion integrada hacia
  Oral Final Cl 45). Cl 38 = Practica intensiva miniproyecto en parejas con
  feedback estructurado + Time Capsule (carta al yo del futuro a mano en
  clase, anti-fraude IA, sellada en sobre con nombre, se abre al terminar A2).
- Virtud FORTALEZA v2 dia 3 (Cl 36-40). Frase del Dia hilada con FORTALEZA dia 3
  + practica miniproyecto + Time Capsule.
- Continua despues de Cl 37 (Speed Dating + Portafolio + anuncio 5 temas Oral
  Final); profesor Christian, cohorte de 6 estudiantes, asistencia 50-67%.
- Modelo Cl 39-40 del plan estructural adaptado a 2h y a cohorte de 6 (no 16).
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class38_PRINT.md'), os.path.join(A1_DIR, 'A1_Class38_GUIA.pdf'))
print('OK: A1_Class38_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 37 = polish miniproyecto + grabo oral final + listening)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Fortaleza dia 3 + practica + Time Capsule)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 37 Speed Dating)', '7 min'),
    ('REPASO 8 ESTRUCTURAS A1 obligatorias miniproyecto', '8 min'),
    ('PRACTICA INTENSIVA MINIPROYECTO EN PAREJAS - 3 rondas feedback estructurado (DE PIE)', '30 min'),
    ('TIME CAPSULE - Carta al Yo del Futuro a mano en clase (anti-fraude IA, sellada)', '18 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Verificacion Sellado Time Capsule + Tarea + Cierre', '16 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Structure Checklist 8 items',
    'Foto/video PEER TEACHER',
    'Foto/video Practica Miniproyecto (al menos 1 ronda)',
    'Foto del bloque de sobres SELLADOS Time Capsule (etiqueta visible "Open at end of A2")',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 37',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cantidad de sobres Time Capsule sellados (debe = asistencia)',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 37 polish miniproyecto + oral final + listening)',
    'PREPARE 6 sobres blancos con nombre + 6 hojas A4 + lapicero para Time Capsule ANTES de clase',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'ESCRIBI el Structure Checklist 8 items en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en oracion sobre practica miniproyecto',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 38 = FORTALEZA v2 dia 3 (por numero de clase)',
    'Hile FORTALEZA dia 3 en VATS con practica repetida + carta honesta al yo del futuro',
    'Confirme que A1 Book termino en M35 (Cl 34-44 = consolidacion integrada hacia Oral Final Cl 45)',
    'Repase las 8 estructuras A1 obligatorias del miniproyecto (PRES SIMPLE/CONT/PAST/GOING TO/CAN/SHOULD/THERE IS-ARE/SOME-ANY/PREPS)',
    'Modele 1 miniproyecto con las 8 estructuras antes de la practica en parejas',
    'Conduje 3 RONDAS de Practica Miniproyecto en parejas con rotacion de companeros',
    'Feedback estructurado del compañero en 3 lineas (entendi/no entendi - mas sobre - estructura faltante)',
    'Round 2 cada presentador incorporo 1 mejora del feedback de Round 1',
    'Cronometre 3-4 min por presentacion (NO leer texto entero - solo tarjeta 5 palabras)',
    'Conduje Time Capsule A MANO EN CLASE (anti-fraude IA: no celulares, no copia, no IA)',
    'Verifique visualmente que la carta es la letra del estudiante',
    'Selle cada sobre frente al estudiante con cinta + nombre visible',
    'Guarde los sobres en carpeta etiquetada "A1 Time Capsule - open at end of A2"',
    'Cantidad de sobres sellados = asistencia real (verificado al cierre)',
    'NO corregi gramatica durante el Time Capsule (es documento personal)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo durante la practica miniproyecto',
    'En libreta personal anote 3 errores con NOMBRE',
    'NO comunique notas/criterios miniproyecto/rubrica Oral Final ("Coordination handles that")',
    'En Tarea explique pedagogicamente el por que + due date explicito (martes 02/06 antes 7PM)',
    'Tarea NO se fragmento (15-20 min) - practica miniproyecto 3 veces + grabo oral final',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 39 martes 02/06 (mas ensayo miniproyecto + resumen visual completo M0-M35)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class38_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 38 de 45 | PRACTICA INTENSIVA MINIPROYECTO + TIME CAPSULE | FORTALEZA v2 dia 3 | FRASE DEL DIA (Goldlist retirado)',
    'Practica intensiva miniproyecto en parejas - 3 rondas con feedback estructurado + Time Capsule (carta al yo del futuro a mano en clase, anti-fraude IA, sellada en sobre con nombre, se abre al terminar A2) + Repaso 8 estructuras A1 obligatorias + FRASE DEL DIA (A1 Book termino en M35; Cl 34-44 = consolidacion integrada hacia Oral Final Cl 45)',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class38_REPORTE.pdf')

print('\n2 PDFs generados para lunes 01/06 A1 Nocturno Cl 38:')
print('  - A1/A1_Class38_GUIA.pdf')
print('  - A1/reportes/A1_Class38_REPORTE.pdf')
