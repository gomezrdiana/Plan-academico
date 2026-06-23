#!/usr/bin/env python3
"""Genera la guia + reporte del A1 Nocturno 2H Cl 41 (jueves 04/06/2026):
- Consolidacion Final 1: Repaso visual TOTAL M0-M35 (timeline en tablero) +
  Simulacro mini-examen formato Final + Resolucion de dudas + Speaking libre +
  Top 10 errores A1 poster + Frase del Dia + virtud SINTESIS dia 1.
- A1 Book termino en M35 (Cl 32-33). Cl 34-44 = consolidacion; Cl 45 = Final.
- TRANSICION DE VIRTUD: Cl 36-40 = FORTALEZA v2 -> Cl 41-45 = SINTESIS (las 4).
  Mencionar el cambio en bloques 3 y 4. Calendario absoluto: SINTESIS NO se desplaza.
- Continua despues de Cl 40 (ensayo miniproyecto + Time Capsule); profesor Christian, cohorte de 6.
- SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class41_PRINT.md'), os.path.join(A1_DIR, 'A1_Class41_GUIA.pdf'))
print('OK: A1_Class41_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 40 = miniproyecto + oral final practicado)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion + transicion FORTALEZA->SINTESIS', '4 min'),
    ('VATS (SINTESIS dia 1 - las 4 virtudes integradas en 1 oracion)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 40 ensayo miniproyecto)', '7 min'),
    ('REPASO VISUAL TOTAL - TIMELINE M0-M35 en tablero + 10 ejercicios rapidos', '25 min'),
    ('SIMULACRO MINI-EXAMEN formato Final (gramatica + voc + correccion + writing) + auto-correccion', '20 min'),
    ('RESOLUCION DE DUDAS del simulacro (ultimo chance grande) - DE PIE', '15 min'),
    ('SHADOWING (verificar dia del ciclo) + Speaking libre 5 min', '15 min'),
    ('Top 10 errores A1 POSTER + Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + TIMELINE M0-M35',
    'Foto del POSTER Top 10 errores A1',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacro (estudiantes trabajando, NO la hoja con respuestas)',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 40 (miniproyecto + oral final practicado)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Cuantas dudas reales resolviste en el bloque 8',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 40 miniproyecto + oral final)',
    'IMPRIMI hojas del simulacro mini-examen ANTES (1 por estudiante)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase (4 lineas, las 4 virtudes)',
    'PRESENTE Frase del Dia con coro 3x y EXPLIQUE el mapeo virtud->linea',
    'INSERTE Frase del Dia 2+ veces NATURALMENTE durante la clase',
    'AL CIERRE 1 estudiante la dijo + 1 uso SINTESIS en oracion propia',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 41 = SINTESIS dia 1 (calendario absoluto, linea 33 CALENDARIO_VIRTUDES_2026.md)',
    'MENCIONE EXPLICITAMENTE la transicion FORTALEZA v2 (Cl 36-40) -> SINTESIS (Cl 41-45)',
    'Hile SINTESIS en VATS forzando oracion con las 4 virtudes integradas',
    'CONFIRME que NO hay modulo nuevo (libro termino en M35) - hoy es consolidacion total',
    'Dibuje el TIMELINE M0-M35 completo en tablero (pasado/presente/futuro + modales + others)',
    'Estudiantes copiaron el TIMELINE en su cuaderno',
    'Conduje 10 ejercicios rapidos identificando tiempo verbal de cada frase',
    'Aplique SIMULACRO mini-examen formato Final (gramatica 8 + voc 5 + correccion 4 + writing 5)',
    'Auto-correccion guiada inmediata (yo lei respuestas, ellos marcaron)',
    'Dedique los 15 min completos de RESOLUCION DE DUDAS (1+ duda por estudiante minimo)',
    'Si nadie pregunto de un tema con errores, yo lo levante',
    'Conduje Speaking Libre 5 min sin corregir (anotando para Error Paper)',
    'Conduje Shadowing del ciclo activo',
    'LLENE el POSTER TOP 10 ERRORES A1 EN VIVO con el grupo (queda colgado para Cl 42-44)',
    'Camine con papel errores anonimo (3 errores live)',
    'En libreta personal anote 3 errores con NOMBRE',
    'NO comunique notas / fecha Final / resultado miniproyecto (si preguntaron: derive a coordinacion)',
    'En Tarea explique el por que + due date explicito (viernes 05/06 antes 7PM, 15-20 min, NO fragmentada)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 42 viernes 05/06 (consolidacion 2 + simulacro 2 + ensayo oral)',
    'Anuncie Cl 43 lunes 08/06 = MINIPROYECTOS (presentaciones)',
    'Anote asistencia real / 6 y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class41_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 41 de 45 | CONSOLIDACION FINAL 1 - REPASO VISUAL TOTAL + SIMULACRO MINI-EXAMEN + TOP 10 ERRORES | SINTESIS dia 1 (las 4 virtudes integradas) | FRASE DEL DIA (Goldlist retirado)',
    'Consolidacion Final 1 post-M35: Timeline M0-M35 en tablero + Simulacro formato Final (gramatica/voc/correccion/writing) + Resolucion de dudas + Top 10 errores poster + Frase del Dia SINTESIS dia 1 (transicion FORTALEZA v2 -> SINTESIS las 4 virtudes en 1 oracion). Anuncio Cl 43 lunes 08/06 MINIPROYECTOS.',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class41_REPORTE.pdf')

print('\n2 PDFs generados para jueves 04/06 A1 Nocturno Cl 41:')
print('  - A1/A1_Class41_GUIA.pdf')
print('  - A1/reportes/A1_Class41_REPORTE.pdf')
