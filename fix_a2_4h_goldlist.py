#!/usr/bin/env python3
"""
Fix A2 4h Class 1-10:
1. Renombrar 'GOLDLIST #1' a solo 'GOLDLIST' (es el unico)
2. Reemplazar 'GOLDLIST #2' con 'FREE PRODUCTION' del modulo de la tarde
3. Cambiar referencias internas

El bloque Free Production es generico — el profesor adapta al modulo del dia.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
A2_DIR = ROOT / 'A2'

FREE_PRODUCTION_BLOCK_TEMPLATE = """### {block_num}. {time_range} | FREE PRODUCTION — CONVERSACION DEL MODULO {modulo_num} (10 min)

**Que es:** Conversacion libre en parejas sobre el tema del Modulo {modulo_num} de la tarde. Los estudiantes USAN la gramatica recien aprendida en contexto real antes de cerrar el dia.

**Setup (1 min):** Escribe en el tablero el TEMA conversacional del modulo de la tarde. Ejemplo: si el modulo fue Past Continuous, escribe "Tell your partner about a moment from your weekend you'll never forget. Use Past Continuous." Si el modulo fue Conditionals, "If you could change one thing about your week, what would it be? Why?"

**Reglas (escribelas):**
- ENGLISH ONLY. Si no saben una palabra, la describen.
- USAR la gramatica del modulo de la tarde minimo 3 veces.
- Cada estudiante habla 4 minutos (no menos).
- Cambian de pareja a la mitad.

**Round 1 (4 min):** Pairs face each other. Person A talks 2 min, Person B talks 2 min. **STANDING.**

**Cambio de pareja (10 seg):** Una fila rota una posicion.

**Round 2 (4 min):** Nueva pareja. 2 min cada uno. Tema sigue siendo el mismo, pero responden a alguien nuevo — la respuesta cambia.

**Cierre (1 min):** Pregunta a 2 estudiantes: "What's the most interesting thing your partners told you?" 1 frase cada uno.

**Tu trabajo durante el bloque:**
- Camina con papel de errores fisico.
- Anota errores de la gramatica del modulo (NO los de pronunciacion general — ese momento ya paso).
- NO corrijas en caliente. Solo anota.
- Si una pareja cae al espanol: "English. Try."

> **Por que este bloque cierra el dia y no es Goldlist #2:** El Goldlist ya se hizo en la manana. Aqui los estudiantes NO copian frases — las USAN. Es el momento donde la gramatica de la tarde entra al cuerpo. Si saltas este bloque, los estudiantes salen con teoria y sin practica de la segunda mitad del dia.

"""

# Patron del bloque GOLDLIST #2 a eliminar
PATTERN_GOLDLIST_2 = re.compile(
    r'### \d+\. \d+:\d+-\d+:\d+ \| GOLDLIST #2.*?(?=\n### \d+\. |\n## |\Z)',
    re.DOTALL
)

# Patron del bloque GOLDLIST #1 a renombrar (solo el header)
PATTERN_GOLDLIST_1_HEADER = re.compile(
    r'^(### \d+\. \d+:\d+-\d+:\d+ \| )GOLDLIST #1 -- ',
    re.MULTILINE
)


def get_modulo_for_class(class_num, text):
    """Detecta el numero del modulo de la tarde. Por defecto: ver MODULO 2 / MODULO 4 / etc."""
    # Buscar referencias a "MODULO N" en la segunda mitad
    matches = re.findall(r'MODULO (\d+)', text.upper())
    if matches:
        # El segundo modulo del dia (despues del descanso)
        nums = sorted(set(int(m) for m in matches))
        if len(nums) >= 2:
            return nums[1]  # el segundo
        return nums[0]
    return '?'


def get_time_range_from_old_block(text):
    """Extrae el rango de tiempo del bloque GOLDLIST #2 original."""
    m = re.search(r'### \d+\. (\d+:\d+-\d+:\d+) \| GOLDLIST #2', text)
    if m:
        return m.group(1)
    return '11:20-11:30'  # default


def get_block_num_from_old_block(text):
    """Extrae el numero del bloque GOLDLIST #2 original."""
    m = re.search(r'### (\d+)\. \d+:\d+-\d+:\d+ \| GOLDLIST #2', text)
    if m:
        return m.group(1)
    return '17'


def fix_class(class_num):
    path = A2_DIR / f'A2_4h_Class{class_num}_PRINT.md'
    if not path.exists():
        return f'  Class {class_num}: not found'

    text = path.read_text(encoding='utf-8')

    # 1. Detectar el bloque GoldList #2 antes de eliminarlo
    if 'GOLDLIST #2' not in text:
        return f'  Class {class_num}: no GOLDLIST #2 found, skipped'

    time_range = get_time_range_from_old_block(text)
    block_num = get_block_num_from_old_block(text)
    modulo = get_modulo_for_class(class_num, text)

    # 2. Reemplazar GoldList #2 con Free Production
    new_block = FREE_PRODUCTION_BLOCK_TEMPLATE.format(
        block_num=block_num,
        time_range=time_range,
        modulo_num=modulo,
    )
    text, n_replaced = PATTERN_GOLDLIST_2.subn(new_block, text, count=1)
    if n_replaced == 0:
        return f'  Class {class_num}: regex did not match GOLDLIST #2'

    # 3. Renombrar GOLDLIST #1 a solo GOLDLIST
    text, n_renamed = PATTERN_GOLDLIST_1_HEADER.subn(r'\1GOLDLIST -- ', text)

    # 4. Limpiar referencias residuales a "GoldList #1" en otros lugares del texto
    text = text.replace('GoldList #1', 'GoldList')
    text = text.replace('GOLDLIST #1', 'GOLDLIST')

    # 5. Limpiar la nota del descanso que dice "BORRA el tablero. Escribe las 20 frases del GoldList #2"
    text = re.sub(
        r'Durante el descanso: BORRA el tablero\.\s*Escribe las 20 frases del GoldList[^\n]*\.[^\n]*\n?',
        'Durante el descanso: prepara el material del Modulo 2.\n',
        text
    )
    text = re.sub(
        r'\d+\.\s*Escribe las 20 frases del GoldList \(?\#?2\)?[^\n]*\n?',
        '',
        text
    )

    path.write_text(text, encoding='utf-8')
    return f'  Class {class_num}: GoldList #2 -> Free Production (Modulo {modulo}, time {time_range}, block {block_num})'


def main():
    print('Fixing A2 4h Class 1-10: GoldList #2 -> Free Production...\n')
    for n in range(1, 11):
        print(fix_class(n))
    print('\nDone. Run regen_all_pdfs.py to generate PDFs.')


if __name__ == '__main__':
    main()
