#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A1 Nocturno 2H Cl 33 (lunes 25/05/2026):
- M35 EXTENDED - Practica Verbal 4 "Going to" Verbos Adicionales (libro pag 415-416)
  + Frase del Dia + virtud JUSTICIA v2 (dia 3)
- M36 NO existe en el A1 Book (M35 es el ultimo modulo gramatical; despues solo anexo
  A1 VOCABULARY). Regla Heiiu: modulo inexistente se salta al siguiente; como no hay
  siguiente, se completa M35 con Practica Verbal 4 (pendiente desde Cl 32 que solo
  cubrio Practica Verbal 1/2/3 pag 409-413).
- Verbos nuevos del libro pag 415-416: buy, drive, tell, call, finish, meet, travel,
  come, feel, visit, watch, go, wake up, eat.
- Continua despues de M35 "Going to / Gonna" (Cl 32); profesor Christian, cohorte de 6.
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

md_to_pdf(os.path.join(A1_DIR, 'A1_Class33_PRINT.md'), os.path.join(A1_DIR, 'A1_Class33_GUIA.pdf'))
print('OK: A1_Class33_GUIA.pdf')

a1_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 32 = M35 going to weekend)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Justicia dia 3 + M35 extended verbos)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 32 going to)', '7 min'),
    ('LIBRO M35 PRACTICA VERBAL 4 - verbos adicionales (pag 415-416)', '20 min'),
    ('VERB SWAP DRILL - going to con cualquier verbo (DE PIE)', '15 min'),
    ('SIMULACION - The Just Schedule (DE PIE, planear semana, repartir justo)', '25 min'),
    ('SHADOWING (verificar dia del ciclo)', '15 min'),
    ('Error Paper Live + Frase del Dia CIERRE + Tarea + Cierre', '12 min'),
]
a1_deliv = [
    'Reporte impreso lleno', 'Foto del SOBRE Mystery',
    'Foto del tablero - Frase del Dia + M35 verbos adicionales',
    'Foto/video PEER TEACHER', 'Foto/video Simulacion The Just Schedule',
    'Foto/video Shadowing', 'Papel errores fisico (anonimo)',
    'Lista quienes NO entregaron tarea Cl 32',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Asistencia real / 6',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a1_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'HABLE 100% EN INGLES', 'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES de clase (chequea tarea Cl 32 M35 going to)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x', 'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo + 1 la uso en nueva oracion con verbo distinto',
    'NO use GoldList ni mencione listas (ritual cerrado)',
    'Verifique virtud CL 33 = JUSTICIA v2 dia 3 (por numero de clase)',
    'Hile JUSTICIA dia 3 en VATS con going to + verbos diversos (call/finish/visit lo que se debe)',
    'CONFIRME que M36 NO existe en el A1 Book (M35 es el ultimo modulo gramatical) - verificado en indice',
    'Cubri M35 PRACTICA VERBAL 4 - VERBOS ADICIONALES DESDE EL LIBRO (pag 415-416 con Respuestas)',
    'Ensene be + going to + verbo BASE con verbos nuevos (buy/drive/tell/call/finish/meet/travel/come/feel/visit)',
    'Reforce: verbo despues de going to SIEMPRE en BASE (no -ing, no -s, no pasado)',
    'Hice Verb Swap Drill DE PIE con 10-12 verbos distintos (no solo "play")',
    'Conduje Simulacion The Just Schedule con going to + verbos diversos + reparto justo',
    'Simulacion fue COTIDIANA/PROFESIONAL (no familiar fantasiosa)',
    'En Round 2 prohibi repetir verbo de Round 1',
    'Conduje Shadowing del ciclo activo',
    'Camine con papel errores anonimo',
    'En libreta personal anote 3 errores con NOMBRE',
    'En Tarea explique pedagogicamente el por que + due date explicito (martes 26/05 antes 7PM)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 34 martes 26/05 (consolidacion oral - el libro ya no tiene modulos gramaticales nuevos)',
    'Anote asistencia real y como va la Frase del Dia',
]
build_report_v2(os.path.join(A1_REP, 'A1_Class33_REPORTE.pdf'),
    'A1 NOCTURNO | Clase 33 de 45 | M35 EXTENDED - PRACTICA VERBAL 4 VERBOS ADICIONALES | JUSTICIA v2 dia 3 | FRASE DEL DIA (Goldlist retirado)',
    'M35 EXTENDED - "Going to" Practica Verbal 4 Verbos Adicionales (libro pag 415-416: buy, drive, tell, call, finish, meet, travel, come, feel, visit, watch, go) + Simulacion The Just Schedule + FRASE DEL DIA (M36 NO existe en libro - se completa M35 con PV4 pendiente desde Cl 32)',
    a1_act, a1_deliv, a1_eval, S)
print('OK: A1_Class33_REPORTE.pdf')

print('\n2 PDFs generados para lunes 25/05 A1 Nocturno Cl 33:')
print('  - A1/A1_Class33_GUIA.pdf')
print('  - A1/reportes/A1_Class33_REPORTE.pdf')
