#!/usr/bin/env python3
"""Genera la guia + reporte del A1 Nocturno 2H Cl 36 (jueves 28/05/2026):
- Consolidacion Integrada (post-M35): SIMULACIONES MAS LIBRES + PRODUCCION
  INDEPENDIENTE (Conversacion libre + Guia Turistica Bucaramanga + Mi Ciudad
  Ideal + Peer Teaching).
- A1 Book cerro en M35 pag 416. NO hay modulo gramatical nuevo. Se USA todo
  lo guardado M1-M35 (presente/continuous/past/going to/can/should/there is-are/
  preposiciones/frecuencia/numeros/vocab familia-rutina-comida-emociones).
- Virtud: FORTALEZA v2 dia 1 (CAMBIO DE BLOQUE - Cl 31-35 fueron JUSTICIA v2;
  Cl 36-40 = FORTALEZA v2, verificado en CALENDARIO_VIRTUDES_2026.md).
  Transicion JUSTICIA -> FORTALEZA se menciona VISIBLEMENTE en VATS.
- Continua despues de Cl 35 (Jeopardy + Quiz Equipos + Round Robin); profesor
  Christian, cohorte de 6, asistencia 50-67%.
- SIN GoldList. Reporte estatico (se llena a mano).
- Anuncia al cierre Cl 37 = Pre-miniproyecto + anuncio 5 temas oral final
  (eligen 1) + FORTALEZA v2 dia 2.
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class36_PRINT.md'), os.path.join(A1_DIR, 'A1_Class36_GUIA.pdf'))
print('OK: A1_Class36_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 35 = review quiz/jeopardy)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (FORTALEZA v2 dia 1 - CAMBIO DE BLOQUE - transicion JUSTICIA->FORTALEZA visible)', '5 min'),
    ('PEER TEACHER SLOT (errores frescos Cl 35: do/does, -s 3ra persona, past vs continuous, irregulares)', '7 min'),
    ('CONVERSACION LIBRE - cohorte elige tema (3 rondas, palmada rotacion)', '15 min'),
    ('SIMULACION - Bucaramanga Tour Guide (DE PIE, equipos, there is/are + can + should + going to + precios)', '20 min'),
    ('PRODUCCION - Mi Ciudad Ideal (individual mapa + descripcion + presentacion parejas)', '15 min'),
    ('PEER TEACHING - cada uno enseña 2 temas A1 al companero (8 opciones)', '10 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Anuncio Cl 37 (pre-miniproyecto + 5 temas oral final) + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Temas posibles + Errores',
    'Foto/video PEER TEACHER', 'Foto/video Conversacion Libre',
    'Foto/video Simulacion Bucaramanga Tour Guide',
    'Foto de 2-3 mapas Mi Ciudad Ideal',
    'Foto/video Peer Teaching', 'Foto/video Shadowing',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 35',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
    'Observacion: como reacciono el cohorte al cambio JUSTICIA -> FORTALEZA',
    'Observacion: quien todavia depende del guion y quien ya produce solo',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 35 review quiz)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 conto un momento de "arrancar antes de estar listo"',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 36 = FORTALEZA v2 dia 1 (CAMBIO DE BLOQUE - calendario absoluto)',
    'MENCIONE VISIBLEMENTE en VATS la transicion JUSTICIA -> FORTALEZA (cierre de bloque)',
    'Hile FORTALEZA dia 1 en VATS con produccion libre (arrancar antes de estar listo)',
    'CONFIRME que el A1 Book cerro en M35 pag 416 (no hay modulo nuevo) - estamos en consolidacion',
    'NO presente gramatica nueva - se USA todo lo guardado M1-M35',
    'Conduje Conversacion Libre dejando que el cohorte elija tema (conte hasta 7 antes de intervenir)',
    'Conduje Simulacion Bucaramanga Tour Guide con there is/are + preposiciones + can + should + going to + precios',
    'Simulacion fue COTIDIANA/PROFESIONAL realista (turista canadiense), NO fantasiosa',
    'Conduje Mi Ciudad Ideal individual con mapa + 6-8 oraciones + presentacion en parejas',
    'Conduje Peer Teaching con 8 opciones de temas A1 (cada uno elige 2)',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo (sin corregir durante conversacion libre)',
    'En libreta personal anote 3 errores con NOMBRE para coordinacion',
    'En Tarea explique pedagogicamente el por que + due date explicito (viernes 29/05 antes 7PM, 15-20 min, NO fragmentada)',
    'NO acepte la excusa "no me da tiempo"',
    'NO comunique nada sobre evaluaciones / midterm / final (solo coordinacion)',
    'Anuncie Cl 37 = Pre-miniproyecto + anuncio de 5 temas oral final (eligen 1) + FORTALEZA v2 dia 2',
    'Anote asistencia real y observacion de quien produce solo vs quien depende del guion',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class36_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 36 de 45 | CONSOLIDACION INTEGRADA - SIMULACIONES LIBRES + PRODUCCION INDEPENDIENTE | FORTALEZA v2 dia 1 (CAMBIO DE BLOQUE) | FRASE DEL DIA',
    'Consolidacion Integrada post-M35 (libro A1 cerro pag 416): Conversacion Libre + Bucaramanga Tour Guide (equipos) + Mi Ciudad Ideal (individual + presentacion) + Peer Teaching (8 temas A1, cada uno elige 2) + FRASE DEL DIA hilada a FORTALEZA dia 1. CAMBIO DE BLOQUE de virtud (JUSTICIA -> FORTALEZA) mencionado visiblemente. Anuncia Cl 37 = Pre-miniproyecto + 5 temas oral final.',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class36_REPORTE.pdf')

print('\n2 PDFs generados para jueves 28/05 A1 Nocturno Cl 36:')
print('  - A1/A1_Class36_GUIA.pdf')
print('  - A1/reportes/A1_Class36_REPORTE.pdf')
