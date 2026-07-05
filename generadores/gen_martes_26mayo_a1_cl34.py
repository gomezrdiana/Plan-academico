#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 34 (martes 26/05/2026):
- APERTURA DEL ARCO DE CONSOLIDACION POST-LIBRO (Cl 34-44 antes del Final Cl 45).
- M36 NO existe en el A1 Book (M35 fue el ultimo modulo gramatical; despues solo
  anexo A1 VOCABULARY pag 417+). Regla Heiiu: modulo inexistente se salta al
  siguiente; como NO hay siguiente, Cl 34-44 = consolidacion integrada.
- Inspiracion estructural: Cl 35 plan A1 Parte 4 (Practica Intensiva Speaking +
  Writing), adaptada a 2h reales, sin GoldList, con Frase del Dia.
- Foco hoy: Carta a un amigo extranjero (integracion de TODOS los tiempos A1 +
  going to obligatorio + min 3 verbos M35) + Peer Review con checklist + Lectura
  en voz alta + Q&A + Dictado Inverso + Frase del Dia + virtud JUSTICIA v2 dia 4.
- Continua despues de Cl 33 (M35 EXTENDED PV4 verbos adicionales); profesor
  Christian, cohorte de 6. SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1_DIR = os.path.join(D, 'A1')
A1_REP = os.path.join(A1_DIR, 'reportes')
os.makedirs(A1_REP, exist_ok=True)

md_to_pdf(os.path.join(A1_DIR, 'A1_Class34_PRINT.md'), os.path.join(A1_DIR, 'A1_Class34_GUIA.pdf'))
print('OK: A1_Class34_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 33 = 8 oraciones going to + 8 verbos)', '5 min'),
    ('EL POR QUE DE HOY + ANUNCIO ARCO DE CONSOLIDACION POST-LIBRO', '3 min'),
    ('FRASE DEL DIA - presentacion (3 tiempos en 1 oracion)', '4 min'),
    ('VATS (Justicia dia 4 + amistad en past/present/future)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 33 M35 PV4 verbos adicionales)', '7 min'),
    ('CHECKLIST de TIEMPOS A1 en tablero (mapa para la carta)', '4 min'),
    ('WRITING - Carta a un amigo extranjero (15+ oraciones, going to obligatorio, 3+ verbos M35)', '20 min'),
    ('PEER REVIEW con checklist (tenses + errores + 1 oracion faltante)', '20 min'),
    ('SPEAKING - Lectura en voz alta + Q&A del grupo (DE PIE)', '20 min'),
    ('DICTADO INVERSO - profesor "se equivoca" / grupo corrige (DE PIE)', '10 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + Tense Checklist A1',
    'Foto/video PEER TEACHER',
    'Cartas fisicas de los estudiantes (recogidas TODAS)',
    'Hojas de Peer Review (recogidas - evidencia de revision)',
    'Foto/video de la lectura en voz alta (al menos 1 estudiante)',
    'Foto/video Dictado Inverso (tablero con errores corregidos)',
    'Foto/video Shadowing',
    'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 33',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 33 going to + 8 verbos)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'ESCRIBI el TENSE CHECKLIST A1 en tablero ANTES del bloque de writing',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 hizo oracion con past+present+future',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 34 = JUSTICIA v2 dia 4 (por numero de clase)',
    'Hile JUSTICIA dia 4 en VATS con past+present+future sobre un amigo (lo que hice/hago/voy a hacer)',
    'ANUNCIE EXPLICITAMENTE el ARCO DE CONSOLIDACION (libro acabo en M35, Cl 34-44 pulir, Cl 45 Final)',
    'CONFIRME que M36 NO existe en el A1 Book (verificado en indice - solo anexo vocabulario despues)',
    'Cubri WRITING - Carta a amigo extranjero con minimo 15 oraciones',
    'Hice cumplir REGLA: going to OBLIGATORIO + minimo 3 verbos M35 (buy/drive/tell/call/finish/meet/travel/come/feel/visit/watch/go/eat/wake up)',
    'Camine durante writing ayudando con vocabulario pero NO con gramatica (eso lo ve peer review)',
    'Conduje PEER REVIEW con checklist (tenses usados + verbos M35 + 3 fuertes + 2 errores + 1 faltante)',
    'Forze el dialogo de feedback EN INGLES entre parejas (6 min final del bloque)',
    'Conduje SPEAKING - lectura en voz alta + 2 preguntas del grupo por estudiante DE PIE',
    'Forze preguntas si el grupo se quedo callado (sobre weekend / friend arrival / city)',
    'Conduje DICTADO INVERSO con errores deliberados (be missing, doble conjugacion, -s despues de going to, will + to)',
    'Conduje Shadowing del ciclo activo',
    'RECOGI las cartas fisicas Y las hojas de Peer Review (anti-fraude IA + evidencia)',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (miercoles 27/05 antes 7PM)',
    'Exigi reescritura con correcciones + 3 oraciones nuevas + grabo 90 seg + shadowing (NO se fragmenta)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 35 miercoles 27/05 (Jeopardy + Quiz consolidacion - JUSTICIA dia 5 cierre del bloque)',
    'Anuncie que Cl 36 abrira FORTALEZA v2 (transicion de virtud por numero de clase)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class34_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 34 de 45 | ARCO CONSOLIDACION POST-LIBRO Ses 1/11 - CARTA INTEGRADORA | JUSTICIA v2 dia 4 | FRASE DEL DIA (Goldlist retirado)',
    'Apertura ARCO DE CONSOLIDACION POST-LIBRO (M35 fue el ultimo modulo gramatical - M36 NO existe). Cl 34-44 = consolidacion integrada antes del Final Cl 45. Hoy: Carta a un amigo extranjero (15+ oraciones, TODOS los tiempos, going to obligatorio, minimo 3 verbos M35) + Peer Review con checklist + Lectura en voz alta + Q&A + Dictado Inverso + FRASE DEL DIA (past+present+future en 1 oracion)',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class34_REPORTE.pdf')

print('\n2 PDFs generados para martes 26/05 A1 Nocturno Cl 34:')
print('  - A1/A1_Class34_GUIA.pdf')
print('  - A1/reportes/A1_Class34_REPORTE.pdf')
