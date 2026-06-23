#!/usr/bin/env python3
"""
Fix B2 Class 12-22:
1. Remove the Portfolio Build block that was incorrectly inserted at the start.
2. Re-insert it at the correct position (before Self-Check / Homework block at the end).
3. Update the homework block with the new daily-investment language.

The bug in apply_b2_portfolio_build.py: regex didn't accept `--` as separator (Class 12+ uses double-dash).
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
B2_DIR = ROOT / 'B2'

# Importar las funciones de portfolio del script anterior
import sys
sys.path.insert(0, str(ROOT))
from apply_b2_portfolio_build import (
    portfolio_block_for_day, cycle_day_for_class, updated_homework_block
)


def fix_class(class_num):
    if class_num < 12 or class_num > 22:
        return f'  Class {class_num}: skip'

    path = B2_DIR / f'B2_Class{class_num}_PRINT.md'
    if not path.exists():
        return f'  Class {class_num}: not found'

    text = path.read_text(encoding='utf-8')

    # 1. Encontrar y eliminar el bloque Portfolio Build mal posicionado
    pattern_pb = re.compile(
        r'### ☐ PORTFOLIO BUILD.*?(?=\n### |\n## )',
        re.DOTALL
    )
    matches = list(pattern_pb.finditer(text))
    if not matches:
        return f'  Class {class_num}: no Portfolio Build block found'
    if len(matches) > 1:
        return f'  Class {class_num}: WARNING — found {len(matches)} portfolio blocks'

    # Eliminar el primer (y unico) match
    text = pattern_pb.sub('', text, count=1)

    # 2. Insertar el bloque Portfolio en la posicion correcta (antes de Self-Check al final)
    day = cycle_day_for_class(class_num)
    cycle_num = ((class_num - 2) // 5) + 1
    pb_block = portfolio_block_for_day(day, cycle_num)

    # Patron flexible: SELF-CHECK con `--` o `–` o ` - `
    pattern_selfcheck = re.compile(
        r'^(### [☐]?\s*\d+:\d+[-–—]+\d+:\d+\s*\|\s*SELF.?CHECK.*)$',
        re.MULTILINE | re.IGNORECASE
    )
    match_sc = pattern_selfcheck.search(text)
    if match_sc:
        pos = match_sc.start()
        text = text[:pos] + pb_block + text[pos:]
        sc_status = 'before SELF-CHECK'
    else:
        # fallback: HOMEWORK al final (no Homework Review al inicio)
        # Buscar el ULTIMO match de un bloque que diga homework
        all_hw = list(re.finditer(r'^### .*HOMEWORK.*', text, re.MULTILINE | re.IGNORECASE))
        if all_hw:
            pos = all_hw[-1].start()  # el ULTIMO
            text = text[:pos] + pb_block + text[pos:]
            sc_status = 'before LAST homework block'
        else:
            return f'  Class {class_num}: no Self-Check or Homework found'

    # 3. Actualizar bloque HOMEWORK al final con el nuevo texto
    pattern_hw_block = re.compile(
        r'### [☐]?\s*\d+:\d+[-–—]+\d+:\d+\s*\|\s*([A-Z\s+]*?)?HOMEWORK[^\n]*?$.*?(?=\n### |\n## |\nNotes:|\Z)',
        re.MULTILINE | re.DOTALL | re.IGNORECASE
    )
    new_text, n_replaced = pattern_hw_block.subn(updated_homework_block(), text, count=1)
    if n_replaced == 0:
        # fallback con regex mas simple
        pattern_hw_simple = re.compile(
            r'### [^\n]*HOMEWORK[^\n]*\n.*?(?=\n### |\n## |\nNotes:|\Z)',
            re.DOTALL | re.IGNORECASE
        )
        # Reemplazar SOLO el ultimo
        all_matches = list(pattern_hw_simple.finditer(new_text))
        if all_matches:
            last = all_matches[-1]
            new_text = new_text[:last.start()] + updated_homework_block() + new_text[last.end():]
            n_replaced = 1
    text = new_text

    path.write_text(text, encoding='utf-8')
    return f'  Class {class_num}: PB Day {day} (Cycle {cycle_num}) inserted {sc_status}, HW replaced {n_replaced}'


def main():
    print('Fixing B2 Class 12-22...\n')
    for n in range(12, 23):
        print(fix_class(n))
    print('\nDone. Run regen_all_pdfs.py.')


if __name__ == '__main__':
    main()
