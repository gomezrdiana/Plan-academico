#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""
Actualiza el bloque ERROR PAPER REVIEW en todas las guias para incluir
una tabla con 10 lineas en blanco que coordinacion o el profesor llenan
antes de la clase.

Reemplaza el bloque actual con la version mejorada.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Nuevo bloque ES con tabla en blanco
NEW_BLOCK_ES = """### ☐ ERROR PAPER REVIEW — DÍA 6 (20 min)

**⚠️ Usa `ANEXO_ERROR_PAPER_REVIEW.pdf` para el protocolo completo.**

Hoy es **Día 6** — bloque que ocurre cada 5 clases para revisar los errores acumulados de las clases anteriores.

**Antes de la clase:** coordinación o el profesor llena la tabla de abajo con los **Top 10 errores recurrentes** de las últimas 5 clases (basados en los papeles de errores). Si no se llenó, el profesor lo hace de memoria al inicio del bloque.

**LOS 10 ERRORES DE HOY** (llenar antes / al inicio de la clase):

| # | ❌ Error que se escuchó | → | ✅ Versión correcta |
|---|------------------------|---|--------------------|
| 1 |                        | → |                    |
| 2 |                        | → |                    |
| 3 |                        | → |                    |
| 4 |                        | → |                    |
| 5 |                        | → |                    |
| 6 |                        | → |                    |
| 7 |                        | → |                    |
| 8 |                        | → |                    |
| 9 |                        | → |                    |
| 10|                        | → |                    |

**Setup (1 min):** Copia los 10 errores de la tabla al tablero del salón.

**Modelado en grupo (8 min):** Por cada error, di la versión INCORRECTA en voz alta sin tono de juicio. La clase identifica qué está mal. Tú modelas la versión correcta. La clase repite **2 veces**. Técnica No-Listen-Repeat. NO expliques la regla — solo modela.

**Drill en parejas (8 min):** "Pairs. Person A says the wrong version. Person B corrects with the right one. Then switch. Go through all 10 errors."

**Cierre + compromiso (3 min):** Cada estudiante escoge UN error que más quiere eliminar. Escribe en su cuaderno:
```
I will stop saying: ___________
I will say instead: ___________
```
"In 5 classes I'll ask you about this. If you eliminated it: 5 English Points."

> **Sin nombres. Sin vergüenza.** Estos son errores del idioma chocando con la boca, no errores de personas. Si tu papel de errores estuvo flojo: reporta a coordinación.

"""

# Nuevo bloque EN con tabla en blanco
NEW_BLOCK_EN = """### ☐ ERROR PAPER REVIEW — DAY 6 (20 min)

**⚠️ Use `ANEXO_ERROR_PAPER_REVIEW.pdf` for the full protocol.**

Today is **Day 6** — this block runs every 5 classes to review the accumulated errors from previous classes.

**Before class:** coordination or the teacher fills in the table below with the **Top 10 recurring errors** from the last 5 classes (based on error papers). If not filled in, the teacher does it from memory at the start of the block.

**TODAY'S 10 ERRORS** (fill in before / at the start of class):

| # | ❌ Error heard | → | ✅ Correct version |
|---|---------------|---|--------------------|
| 1 |               | → |                    |
| 2 |               | → |                    |
| 3 |               | → |                    |
| 4 |               | → |                    |
| 5 |               | → |                    |
| 6 |               | → |                    |
| 7 |               | → |                    |
| 8 |               | → |                    |
| 9 |               | → |                    |
| 10|               | → |                    |

**Setup (1 min):** Copy the 10 errors from the table onto the classroom board.

**Group modeling (8 min):** For each error, say the WRONG version aloud without judgment. The class identifies what's wrong. You model the correct version. The class repeats **2 times**. No-Listen-Repeat technique. Do NOT explain the grammar rule — only model.

**Pair drill (8 min):** "Pairs. Person A says the wrong version. Person B corrects with the right one. Then switch. Go through all 10 errors."

**Close + commitment (3 min):** Each student picks ONE error they most want to eliminate. They write in their notebook:
```
I will stop saying: ___________
I will say instead: ___________
```
"In 5 classes I'll ask you about this. If you eliminated it: 5 English Points."

> **No names. No shame.** These are errors of language meeting the mouth, not personal failures. If your error paper was weak this week: report to coordination.

"""


def update_file(path):
    text = path.read_text(encoding='utf-8')

    # Patron para detectar el bloque viejo (ES o EN) hasta el siguiente ###
    pattern = re.compile(
        r'### ☐ ERROR PAPER REVIEW — D[ÍI]A 6.*?(?=\n### |\n## |\Z)',
        re.DOTALL
    )
    matches = list(pattern.finditer(text))

    if not matches:
        # Tambien buscar version EN (DAY 6)
        pattern_en = re.compile(
            r'### ☐ ERROR PAPER REVIEW — DAY 6.*?(?=\n### |\n## |\Z)',
            re.DOTALL
        )
        matches = list(pattern_en.finditer(text))
        if not matches:
            return None  # no tiene el bloque

    # Determinar si es ES o EN
    is_en = 'DAY 6' in matches[0].group(0)
    new_block = NEW_BLOCK_EN if is_en else NEW_BLOCK_ES

    # Reemplazar
    new_text = text[:matches[0].start()] + new_block + text[matches[0].end():]
    path.write_text(new_text, encoding='utf-8')
    return 'updated EN' if is_en else 'updated ES'


def main():
    print('Actualizando bloque Error Paper Review con tabla en blanco...\n')
    n_updated = 0
    for sub in ['A1', 'A2', 'B1', 'B2']:
        d = ROOT / sub
        if not d.is_dir():
            continue
        for f in sorted(d.glob('*_PRINT.md')):
            result = update_file(f)
            if result:
                print(f'  {f.relative_to(ROOT)}: {result}')
                n_updated += 1

    # A2 4h Class 6 (insertado manualmente con formato distinto)
    a2_4h = ROOT / 'A2' / 'A2_4h_Class6_PRINT.md'
    if a2_4h.exists():
        text = a2_4h.read_text(encoding='utf-8')
        # buscar el bloque sin el ☐
        pattern_alt = re.compile(
            r'### ERROR PAPER REVIEW — D[ÍI]A 6.*?(?=\n### |\n## |\Z)',
            re.DOTALL
        )
        if pattern_alt.search(text):
            new_text = pattern_alt.sub(NEW_BLOCK_ES.rstrip(), text, count=1)
            a2_4h.write_text(new_text, encoding='utf-8')
            print(f'  A2/A2_4h_Class6_PRINT.md: updated ES (manual format)')
            n_updated += 1

    print(f'\nTotal updated: {n_updated} files')


if __name__ == '__main__':
    main()
