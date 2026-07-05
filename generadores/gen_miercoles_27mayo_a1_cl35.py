#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 35 (miercoles 27/05/2026):
- CONSOLIDACION GAMIFICADA: Jeopardy A1 completo (6 categorias x 5 preguntas) +
  Round Robin 6 estaciones + Quiz Mega 4 equipos 20 preguntas.
- Sin modulo nuevo (A1 Book termino en M35 pag 416; arco Cl 34-44 = consolidacion
  integrada antes del Final Cl 45 por decision Diana).
- VIRTUD: JUSTICIA v2 dia 5 (ULTIMO del bloque Cl 31-35). Manana Cl 36 = FORTALEZA
  v2 dia 1 — anunciar transicion en cierre.
- Frase del Dia: "Today we compete fairly — that's what makes the win count."
- Continuidad: Cl 34 (martes 26/05) cubrio Carta amigo extranjero integrando todos
  los tiempos (Speaking + Writing). Mystery hoy chequea esa carta.
- Profesor Christian, cohorte de 6, asistencia 50-67%.
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

md_to_pdf(os.path.join(A1_DIR, 'A1_Class35_PRINT.md'), os.path.join(A1_DIR, 'A1_Class35_GUIA.pdf'))
print('OK: A1_Class35_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 34 = Carta amigo extranjero)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia v2 dia 5 - ULTIMO del bloque + competicion justa)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 34 mezcla de tiempos)', '7 min'),
    ('JEOPARDY A1 COMPLETO - 6 categorias x 5 preguntas (CAN/Present/Past/Future/Vocab/Emotions)', '25 min'),
    ('ROUND ROBIN 6 ESTACIONES (Familia/Rutina/Ayer/Planes/Comida/Emociones)', '20 min'),
    ('QUIZ MEGA - 4 equipos, 20 preguntas mixtas (gramatica/vocab/correccion/produccion)', '20 min'),
    ('SHADOWING (verificar dia del ciclo)', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Anuncio Cl 36 (FORTALEZA v2 dia 1)', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + JEOPARDY board con puntajes finales',
    'Foto/video PEER TEACHER',
    'Foto/video JEOPARDY en accion (equipos compitiendo)',
    'Foto/video Round Robin (rotacion entre estaciones)',
    'Foto/video Quiz Mega (papers up)',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 34 (Carta amigo extranjero)',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 34 = Carta amigo extranjero)',
    'PREPARE 30 tarjetas Jeopardy ANTES (6 categorias x 5 preguntas)',
    'PREPARE 6 tarjetas Round Robin ANTES (Familia/Rutina/Ayer/Planes/Comida/Emociones)',
    'PREPARE banco 20 preguntas Quiz Mega ANTES (5 gramatica + 5 vocab + 5 correccion + 5 produccion)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE (cada vez que un equipo gana limpio)',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en oracion nueva',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 35 = JUSTICIA v2 dia 5 (ULTIMO del bloque por numero de clase)',
    'Hile JUSTICIA dia 5 en VATS con cierre del bloque (mismas reglas, igual oportunidad)',
    'ANUNCIE en cierre la transicion a FORTALEZA v2 dia 1 manana Cl 36',
    'CONFIRME que A1 Book termino en M35 (no hay modulo nuevo - consolidacion integrada)',
    'Forme 4 equipos balanceados (ajuste al vuelo segun asistencia)',
    'JEOPARDY: roto a TODOS los estudiantes del equipo (cada uno respondio al menos 1 vez)',
    'JEOPARDY: las preguntas fueron REALES sobre vida cotidiana (no fantasiosas)',
    'ROUND ROBIN: 3 min por estacion + palmada para rotar + TODOS hablaron en cada estacion',
    'QUIZ MEGA: cronometro 30 seg + papers up + bonus por error extra detectado',
    'En libreta personal anote 3 errores con NOMBRE (cosechados de Jeopardy/Quiz/Round Robin)',
    'Camine con papel errores anonimo en cierre',
    'En Tarea explique pedagogicamente el por que + due date explicito (jueves 28/05 antes 7PM)',
    'Tarea NO fragmentada (15-20 min completos, no por partes)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 36 jueves 28/05 (consolidacion + Mi Ciudad Ideal + CAMBIO virtud a FORTALEZA v2 dia 1)',
    'Conduje Shadowing del ciclo activo',
    'NO comunique notas/midterm/final (eso es coordinacion)',
    'Anote asistencia real / 6 y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class35_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 35 de 45 | CONSOLIDACION GAMIFICADA - JEOPARDY + ROUND ROBIN + QUIZ MEGA | JUSTICIA v2 dia 5 (ULTIMO bloque) | FRASE DEL DIA',
    'Consolidacion A1 gamificada (sin modulo nuevo - A1 Book termino en M35): Jeopardy A1 completo 6 categorias x 5 preguntas (CAN/Present/Past/Future/Vocab/Emotions) + Round Robin 6 estaciones (Familia/Rutina/Ayer/Planes/Comida/Emociones) + Quiz Mega 4 equipos 20 preguntas mixtas + FRASE DEL DIA "Today we compete fairly — that\'s what makes the win count" + ANUNCIO transicion a FORTALEZA v2 dia 1 manana Cl 36',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class35_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 27/05 A1 Nocturno Cl 35:')
print('  - A1/A1_Class35_GUIA.pdf')
print('  - A1/reportes/A1_Class35_REPORTE.pdf')
