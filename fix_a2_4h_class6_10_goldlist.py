#!/usr/bin/env python3
"""
Fix A2 4h Class 6-10:
1. Consolidar las 10 frases existentes (5 del bloque #1 + 5 del bloque #2) +
   10 frases nuevas alineadas a modulo y virtud = 20 frases en UN bloque (manana).
2. Reemplazar el bloque #2 (5 FRASES MAS) con FREE PRODUCTION del modulo de la tarde.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
A2_DIR = ROOT / 'A2'

# Frases extra (11-20) para cada clase, alineadas a modulo + virtud
EXTRA_PHRASES = {
    6: [  # M13 Already/Still/Until + M14 While/During/Again - Templanza/Fortaleza
        ('11. *I haven\'t seen her in years.*', 'No la he visto en años.'),
        ('12. *We haven\'t visited that place yet.*', 'Todavia no hemos visitado ese lugar.'),
        ('13. *He still hasn\'t told the truth.*', 'El todavia no ha dicho la verdad.'),
        ('14. *I worked while you were sleeping.*', 'Trabaje mientras dormias.'),
        ('15. *Try this exercise again.*', 'Intenta este ejercicio otra vez.'),
        ('16. *During the meeting, nobody spoke.*', 'Durante la reunion, nadie hablo.'),
        ('17. *We waited until the rain stopped.*', 'Esperamos hasta que paro la lluvia.'),
        ('18. *She still loves him after all these years.*', 'Ella todavia lo ama despues de todos estos años.'),
        ('19. *I already paid the bill.*', 'Ya pague la cuenta.'),
        ('20. *Don\'t open the door again.*', 'No abras la puerta otra vez.'),
    ],
    7: [  # M15 PP Regular + M16 PP Irregular - Prudencia
        ('11. *I have known her for 10 years.*', 'La he conocido por 10 años.'),
        ('12. *We have planned everything carefully.*', 'Hemos planeado todo cuidadosamente.'),
        ('13. *Have you ever traveled alone?*', 'Alguna vez has viajado solo?'),
        ('14. *She has just finished her homework.*', 'Ella acaba de terminar su tarea.'),
        ('15. *They have already eaten.*', 'Ya han comido.'),
        ('16. *I have never been so happy.*', 'Nunca he sido tan feliz.'),
        ('17. *He has worked here since 2018.*', 'Ha trabajado aqui desde 2018.'),
        ('18. *We haven\'t decided yet.*', 'Todavia no hemos decidido.'),
        ('19. *Have they arrived?*', 'Han llegado?'),
        ('20. *I have spoken to her about it.*', 'He hablado con ella al respecto.'),
    ],
    8: [  # M17 Past vs PP + M18 Passive - Prudencia
        ('11. *Yesterday I worked late.*', 'Ayer trabaje hasta tarde.'),
        ('12. *I have worked late many times.*', 'He trabajado hasta tarde muchas veces.'),
        ('13. *She visited Paris in 2019.*', 'Ella visito Paris en 2019.'),
        ('14. *She has visited Paris twice.*', 'Ella ha visitado Paris dos veces.'),
        ('15. *The car was repaired by my brother.*', 'El carro fue reparado por mi hermano.'),
        ('16. *Many books are read every year.*', 'Muchos libros se leen cada año.'),
        ('17. *English is spoken everywhere.*', 'El ingles se habla en todas partes.'),
        ('18. *Last week we cooked together.*', 'La semana pasada cocinamos juntos.'),
        ('19. *The decision was made yesterday.*', 'La decision se tomo ayer.'),
        ('20. *I have made my choice.*', 'He tomado mi decision.'),
    ],
    9: [  # M20 Gerunds Subjects + M21 Gerunds after Preps - Templanza
        ('11. *Reading helps me relax.*', 'Leer me ayuda a relajarme.'),
        ('12. *Listening is harder than speaking.*', 'Escuchar es mas dificil que hablar.'),
        ('13. *I am tired of waiting.*', 'Estoy cansado de esperar.'),
        ('14. *She is good at cooking.*', 'Ella es buena cocinando.'),
        ('15. *Thank you for coming.*', 'Gracias por venir.'),
        ('16. *He is afraid of flying.*', 'El le tiene miedo a volar.'),
        ('17. *We talked about traveling.*', 'Hablamos sobre viajar.'),
        ('18. *I am interested in learning.*', 'Estoy interesado en aprender.'),
        ('19. *Walking every day is healthy.*', 'Caminar cada dia es saludable.'),
        ('20. *Saving money is important.*', 'Ahorrar dinero es importante.'),
    ],
    10: [  # M22 Gerunds Double Verbs + M23 Phrasal Verbs - Templanza
        ('11. *I look forward to seeing you.*', 'Espero con ansia verte.'),
        ('12. *She enjoys reading and writing.*', 'Ella disfruta leyendo y escribiendo.'),
        ('13. *We need to work on speaking faster.*', 'Necesitamos trabajar en hablar mas rapido.'),
        ('14. *Don\'t give up on learning.*', 'No te rindas en aprender.'),
        ('15. *I keep trying to improve.*', 'Sigo intentando mejorar.'),
        ('16. *Please look after my dog.*', 'Por favor cuida a mi perro.'),
        ('17. *He decided to start exercising.*', 'Decidio empezar a ejercitarse.'),
        ('18. *We agreed on meeting at 5 PM.*', 'Acordamos reunirnos a las 5 PM.'),
        ('19. *She finished writing her essay.*', 'Ella termino de escribir su ensayo.'),
        ('20. *They asked for more practice.*', 'Pidieron mas practica.'),
    ],
}


def get_modulo_tarde(text):
    """Detecta el numero del segundo modulo (despues del descanso)."""
    matches = re.findall(r'M[oó]dulo (\d+)', text)
    if matches:
        nums = sorted(set(int(m) for m in matches if m.isdigit()))
        if len(nums) >= 2:
            return nums[1]
        if nums:
            return nums[0]
    return '?'


def get_first_block_info(text):
    """Extrae info del bloque GOLDLIST manana (#1 o solo)."""
    m = re.search(r'### (\d+)\. (\d+:\d+-\d+:\d+) \| GOLDLIST -- 5 FRASES \((\d+) min\)', text)
    if m:
        return m.group(1), m.group(2), m.group(3)
    return None, None, None


def get_second_block_info(text):
    """Extrae info del bloque GOLDLIST tarde (#2 o '5 FRASES MAS')."""
    m = re.search(r'### (\d+)\. (\d+:\d+-\d+:\d+) \| GOLDLIST -- 5 FRASES MAS \((\d+) min\)', text)
    if m:
        return m.group(1), m.group(2), m.group(3)
    return None, None, None


# Patrones para extraer el bloque entero (header + body) hasta el siguiente ###
PATTERN_BLOCK1 = re.compile(
    r'### \d+\. \d+:\d+-\d+:\d+ \| GOLDLIST -- 5 FRASES \(\d+ min\).*?(?=\n### \d+\. )',
    re.DOTALL
)
PATTERN_BLOCK2 = re.compile(
    r'### \d+\. \d+:\d+-\d+:\d+ \| GOLDLIST -- 5 FRASES MAS \(\d+ min\).*?(?=\n### \d+\. )',
    re.DOTALL
)


def consolidated_goldlist_block(class_num, block_num, time_range, frases_existentes_5, frases_existentes_5_mas, extras_10):
    """Construye el bloque consolidado de 20 frases."""
    return f"""### {block_num}. {time_range} | GOLDLIST -- 20 FRASES (10 min)

**PREPARACION DEL TABLERO:** ANTES de que lleguen los estudiantes, escribe estas 20 frases en el tablero -- AMBOS IDIOMAS. Copia de esta guia. No traduzcas de memoria.

**EL CUADERNO DE GOLDLIST SE QUEDA EN LA ACADEMIA.** Los estudiantes NO se lo llevan a casa. Recoge todos los cuadernos al final de la clase.

Di: "Tomen su cuaderno de GoldList. Escriban la fecha de hoy. Copien las 20 frases del tablero: ingles a la izquierda, espanol a la derecha. No se apuren -- escribanlas con calma y con buena letra. NO memorizar. Solo escribir."

Los estudiantes copian del tablero (8 min):

{frases_existentes_5}

{frases_existentes_5_mas}

{extras_10}

Cuando terminen de copiar (1 min): Di: "Lean la lista UNA vez en voz alta conmigo." Lee cada frase en ingles, la clase repite. UNA sola vez. No corregir pronunciacion -- momento relajado.

Di: "Listo. Cierren el cuaderno. NO estudien estas frases. Su cerebro las absorbera solo. En 14 dias depuramos la lista del Dia 1."

**RECOGE TODOS LOS CUADERNOS DE GOLDLIST.** Guardalos en el salon.

"""


def free_production_block(block_num, time_range, modulo_tarde):
    return f"""### {block_num}. {time_range} | FREE PRODUCTION -- CONVERSACION DEL MODULO {modulo_tarde} (10 min)

**Que es:** Conversacion libre en parejas sobre el tema del Modulo {modulo_tarde} de la tarde. Los estudiantes USAN la gramatica recien aprendida en contexto real antes de cerrar el dia.

**Setup (1 min):** Escribe en el tablero el TEMA conversacional del modulo de la tarde. La pregunta debe forzar el uso de la gramatica nueva minimo 3 veces por persona.

**Reglas (escribelas):**
- ENGLISH ONLY. Si no saben una palabra, la describen.
- USAR la gramatica del modulo de la tarde minimo 3 veces.
- Cada estudiante habla 4 minutos (no menos).
- Cambian de pareja a la mitad.

**Round 1 (4 min):** Pairs face each other. Person A talks 2 min, Person B talks 2 min. **STANDING.**

**Cambio de pareja (10 seg):** Una fila rota una posicion.

**Round 2 (4 min):** Nueva pareja. 2 min cada uno. Tema sigue igual, pero responden a alguien nuevo.

**Cierre (1 min):** Pregunta a 2 estudiantes: "What's the most interesting thing your partners told you?" 1 frase cada uno.

**Tu trabajo durante el bloque:**
- Camina con papel de errores fisico.
- Anota errores de la gramatica del modulo (NO los de pronunciacion general).
- NO corrijas en caliente. Solo anota.
- Si una pareja cae al espanol: "English. Try."

> **Por que este bloque cierra el dia y no es Goldlist #2:** El Goldlist ya se hizo en la manana (20 frases). Aqui los estudiantes USAN la gramatica de la tarde. La gramatica entra al cuerpo. Si saltas este bloque, salen con teoria sin practica.

"""


def fix_class(class_num):
    path = A2_DIR / f'A2_4h_Class{class_num}_PRINT.md'
    if not path.exists():
        return f'  Class {class_num}: not found'

    text = path.read_text(encoding='utf-8')

    # Buscar info de los 2 bloques
    b1_num, b1_time, _ = get_first_block_info(text)
    b2_num, b2_time, _ = get_second_block_info(text)

    if not b1_num or not b2_num:
        return f'  Class {class_num}: no GOLDLIST blocks (1 or 2) found'

    # Extraer las 5 frases del bloque #1 y del #2
    block1_match = PATTERN_BLOCK1.search(text)
    block2_match = PATTERN_BLOCK2.search(text)
    if not block1_match or not block2_match:
        return f'  Class {class_num}: regex match failed'

    # Extraer las frases del bloque 1 (lineas que empiezan con "1." a "5.")
    body1 = block1_match.group(0)
    body2 = block2_match.group(0)

    # Lineas que empiezan con num. *
    frases_5_b1 = '\n'.join(re.findall(r'^\d+\. \*[^\n]*', body1, re.MULTILINE)[:5])
    frases_5_b2 = '\n'.join(re.findall(r'^\d+\. \*[^\n]*', body2, re.MULTILINE)[:5])

    # Frases extras 11-20
    extras_10_text = '\n'.join(f'{eng} -- {esp}' for eng, esp in EXTRA_PHRASES[class_num])

    # Construir bloque consolidado
    new_block_1 = consolidated_goldlist_block(
        class_num, b1_num, b1_time,
        frases_5_b1, frases_5_b2, extras_10_text
    )

    # Construir Free Production para el bloque #2
    modulo_tarde = get_modulo_tarde(text)
    new_block_2 = free_production_block(b2_num, b2_time, modulo_tarde)

    # Reemplazar
    text = PATTERN_BLOCK1.sub(new_block_1, text, count=1)
    text = PATTERN_BLOCK2.sub(new_block_2, text, count=1)

    path.write_text(text, encoding='utf-8')
    return f'  Class {class_num}: Goldlist consolidado a 20 frases (block {b1_num} {b1_time}); Free Production en {b2_time} (Modulo {modulo_tarde})'


def main():
    print('Fixing A2 4h Class 6-10: Goldlist 20 frases consolidado + Free Production...\n')
    for n in range(6, 11):
        print(fix_class(n))
    print('\nDone. Run regen_all_pdfs.py.')


if __name__ == '__main__':
    main()
