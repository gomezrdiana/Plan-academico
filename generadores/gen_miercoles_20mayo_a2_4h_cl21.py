#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Genera la guia + reporte del A2 INTENSIVO 4h AM Cl 21 (miercoles 20/05/2026):
- CONSOLIDACION M43 "How Do You Do?" (Adverbs of Manner) + M44 "I Want You to
  Go" (The Active Causative). EL A2 BOOK TERMINO EN M44 (pag 352): NO hay
  Modulo 45, NO se inventa contenido. Hoy = profundizar/integrar M43+M44 con
  los ejercicios reales del libro (pags 343-346 y 349-351).
- Shadowing Dia 2 (mismo video de Cl 20, sin video, de memoria) + Frase del
  Dia + virtud PRUDENCIA v2 (por numero de clase: Cl 21-25).
- Sigue a Cl 20 (M43+M44). SIN GoldList. Reporte estatico (se llena a mano).
"""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf
from generate_pdfs import get_styles, build_report_v2

S = get_styles()
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A2_DIR = os.path.join(D, 'A2')
A2_REP = os.path.join(A2_DIR, 'reportes')
os.makedirs(A2_REP, exist_ok=True)

md_to_pdf(os.path.join(A2_DIR, 'A2_4h_Class21_PRINT.md'),
          os.path.join(A2_DIR, 'A2_4h_Class21_GUIA.pdf'))
print('OK: A2_4h_Class21_GUIA.pdf')

a2_act = [
    ('MYSTERY HOMEWORK CHECK (tarea Cl 20 = M43 adverbio + M44 causativo)', '5 min'),
    ('EL POR QUE DE HOY', '2 min'),
    ('FRASE DEL DIA - presentacion', '4 min'),
    ('VATS (Prudencia v2 + M43/M44)', '5 min'),
    ('PEER TEACHER SLOT (errores Cl 20)', '7 min'),
    ('Tarea Check Cl 20', '5 min'),
    ('REPASO VIVO M43 - adverbios de manera (concepto + vocab desde el libro)', '22 min'),
    ('SPEED DRILL M43 - adjetivo -> adverbio + ubicacion', '15 min'),
    ('REPASO VIVO M44 - el causativo activo "I want you to..." (desde el libro)', '20 min'),
    ('HISTORIA INTERACTIVA M43+M44 - "The careful planning day" (DE PIE)', '12 min'),
    ('SIMULACION PROFESIONAL - "Planning Meeting" (DE PIE)', '25 min'),
    ('SIMULACION INTEGRADA M43+M44 - "Who does what, and how?" (DE PIE)', '23 min'),
    ('SHADOWING - DIA 2: SIN VIDEO, DE MEMORIA (DE PIE)', '18 min'),
    ('Free production M43+M44 (parejas DE PIE)', '14 min'),
    ('Error Paper Live + Frase del Dia CIERRE', '8 min'),
    ('Tarea + Cierre + anuncio Cl 22 (jueves)', '10 min'),
]
a2_deliv = [
    'Reporte impreso lleno',
    'Foto del SOBRE Mystery (chequea Cl 20 M43 adverbio + M44 causativo)',
    'Foto del tablero - Frase del Dia + M43 adverbios + M44 patron causativo',
    'Foto/video PEER TEACHER',
    'Foto/video Simulacion "Planning Meeting"',
    'Foto/video Simulacion integrada "Who Does What, And How?"',
    'Foto/video Shadowing Dia 2 (sin video, de memoria)',
    'Foto/video Free Production',
    'Papel errores fisico (ANONIMO)',
    'Lista quienes NO entregaron tarea Cl 20',
    'Libreta personal con 3 errores literales + NOMBRE',
    'Cuantas veces lograste insertar la Frase del Dia naturalmente',
]
a2_eval = [
    'Lei el mensaje pedagogico ANTES de clase',
    'Entendi que HOY es CONSOLIDACION: el A2 Book termino en M44, NO hay modulo nuevo',
    'NO invente contenido (no existe Modulo 45)',
    'HABLE 100% EN INGLES',
    'EXPLIQUE OBJETIVO de cada actividad ANTES',
    'PREPARE el SOBRE del Mystery ANTES (chequea tarea Cl 20 M43+M44)',
    'ESCRIBI la FRASE DEL DIA en tablero ANTES de clase',
    'PRESENTE Frase del Dia con coro 3x',
    'INSERTE Frase del Dia 3+ veces NATURALMENTE',
    'AL CIERRE 1 estudiante la dijo de memoria + 1 la uso en nueva oracion',
    'NO use GoldList ni mencione listas/depuracion (ritual cerrado)',
    'NO repeti el discurso de cierre GoldList (ya se hizo Cl 18)',
    'NO comente notas ni resultados de evaluacion (exclusivo coordinacion)',
    'Verifique virtud CL 21 = PRUDENCIA v2 (por numero de clase, Cl 21-25)',
    'Hile PRUDENCIA en VATS con adverbio de manera + causativo',
    'Repase M43 How Do You Do DESDE EL LIBRO (pag 340-346)',
    'Reforce adjetivo + -ly + irregulares (good->well, fast, hard)',
    'Reforce ubicacion del adverbio + manera vs frecuencia',
    'Repase M44 I Want You to Go DESDE EL LIBRO (pag 347-351)',
    'Contraste "I want to go" vs "I want YOU to go" (cambio de sujeto)',
    'Marque el error de calco "I want that you go" como INCORRECTO',
    'Lleve la combinacion M43+M44 a fluidez ("I want you to do it carefully")',
    'Conduje Speed Drill adjetivo->adverbio + ubicacion (velocidad/automatico)',
    'Conduje Historia Interactiva (dia de planeacion absurdo cotidiano, NO fantasia)',
    'Conduje Simulacion "Planning Meeting" PROFESIONAL (no familiar)',
    'Conduje Simulacion integrada M43+M44 "Who Does What, And How?"',
    'Verifique link + que HOY = Shadowing DIA 2 (mismo video Cl 20, sin video)',
    'Corri Shadowing Dia 2: de memoria, sin video, por bloques',
    'Camine con papel errores ANONIMO (protocolo doble)',
    'En libreta personal anote 3 errores con NOMBRE + cita literal',
    'En Tarea explique el por que + due date explicito (jueves 21/05 7PM)',
    'Tarea NO fragmentada + tiempo dentro del rango A2 (20-30 min)',
    'NO acepte la excusa "no me da tiempo"',
    'Anuncie Cl 22 (jueves) = continuacion CONSOLIDACION + Shadowing Dia 3 mini-competencia',
]
build_report_v2(
    os.path.join(A2_REP, 'A2_4h_Class21_REPORTE.pdf'),
    'A2 INTENSIVO 4H | Clase 21 de 28 | CONSOLIDACION M43 ADVERBS OF MANNER + M44 ACTIVE CAUSATIVE (fin del A2 Book) | SHADOWING DIA 2 | PRUDENCIA v2 | FRASE DEL DIA (GoldList retirado)',
    'CONSOLIDACION M43 How Do You Do? (Adverbs of Manner) + M44 I Want You to Go (Active Causative) - el A2 Book termino en M44, NO hay modulo nuevo. Planning Meeting + Who Does What And How + Shadowing Dia 2 (sin video, memoria) + FRASE DEL DIA',
    a2_act, a2_deliv, a2_eval, S)
print('OK: A2_4h_Class21_REPORTE.pdf')

print('\n2 PDFs generados para miercoles 20/05 A2 INTENSIVO 4h AM Cl 21:')
print('  - A2/A2_4h_Class21_GUIA.pdf')
print('  - A2/reportes/A2_4h_Class21_REPORTE.pdf')
