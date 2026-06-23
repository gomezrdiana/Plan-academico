#!/usr/bin/env python3
"""
Restaurar bloque SELF-CHECK en B2 Class 12-17 que se perdió cuando
mi script de Portfolio reemplazó el bloque combinado SELF-CHECK + HOMEWORK + CLOSE
con solo el HOMEWORK.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
B2_DIR = ROOT / 'B2'

SELFCHECK_BLOCK = """### ☐ SELF-CHECK (5 min)

Hand out self-check sheet. Students fill ALL fields. COLLECT. CHECK EVERY ONE: blank field = hand it back, fill it NOW. No incomplete sheets accepted. Send to coordination TODAY.

"""


def fix_class(class_num):
    path = B2_DIR / f'B2_Class{class_num}_PRINT.md'
    if not path.exists():
        return f'  Class {class_num}: not found'

    text = path.read_text(encoding='utf-8')

    # Verificar si ya tiene Self-Check como bloque
    if re.search(r'^### .*SELF.?CHECK', text, re.MULTILINE | re.IGNORECASE):
        return f'  Class {class_num}: already has Self-Check'

    # Insertar Self-Check antes del bloque HOMEWORK
    pattern_hw = re.compile(r'^### .*HOMEWORK.*$', re.MULTILINE | re.IGNORECASE)
    matches = list(pattern_hw.finditer(text))
    if not matches:
        return f'  Class {class_num}: no HOMEWORK block found'

    # Tomar el ULTIMO match (el HOMEWORK + CLOSE al final, no el HOMEWORK REVIEW al inicio)
    last = matches[-1]
    pos = last.start()
    text = text[:pos] + SELFCHECK_BLOCK + text[pos:]
    path.write_text(text, encoding='utf-8')
    return f'  Class {class_num}: Self-Check inserted before final HOMEWORK'


def main():
    print('Restoring Self-Check in B2 classes...\n')
    for n in range(1, 23):
        print(fix_class(n))
    print('\nDone.')


if __name__ == '__main__':
    main()
