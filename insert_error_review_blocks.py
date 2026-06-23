#!/usr/bin/env python3
"""
Inserta el bloque ERROR PAPER REVIEW (20 min) en las clases marcadas como "Dia 6".

Aplica a:
- A1: Class 6, 11, 16, 21, 26, 31, 36, 41
- A2 nocturno: Class 6, 11, 16, 21, 26, 31, 36, 41, 46, 51
- A2 4h: Class 6, 11
- B1: ninguna por ahora (solo existen Clase 1, 2)
- B2: Class 6, 11, 16, 21, 26, 31, 36, 41, 46

Solo procesa archivos que ya existan.

Posicion: justo despues del bloque VATS, antes del siguiente bloque.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

ERROR_REVIEW_BLOCK_ES = """### ☐ ERROR PAPER REVIEW — DÍA 6 (20 min)

**⚠️ Usa `ANEXO_ERROR_PAPER_REVIEW.pdf` para el protocolo completo.**

Hoy es **Día 6** — bloque que ocurre cada 5 clases para revisar los errores acumulados de las clases anteriores.

**Antes de la clase:** coordinación te entregó la lista consolidada de **Top 10 errores recurrentes** de las últimas 5 clases (basados en tus papeles de errores). Si no la recibiste a tiempo, usa los 7-10 errores más frecuentes de tu propio papel de errores.

**Setup (1 min):** Escribe los 7-10 errores en el tablero en formato:
```
1. ❌ ___________  →  ✅ ___________
2. ❌ ___________  →  ✅ ___________
...
```

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


ERROR_REVIEW_BLOCK_EN = """### ☐ ERROR PAPER REVIEW — DAY 6 (20 min)

**⚠️ Use `ANEXO_ERROR_PAPER_REVIEW.pdf` for the full protocol.**

Today is **Day 6** — this block runs every 5 classes to review the accumulated errors from previous classes.

**Before class:** coordination delivered the consolidated list of **Top 10 recurring errors** from the last 5 classes (based on your error papers). If you didn't receive it in time, use the 7-10 most frequent errors from your own error paper.

**Setup (1 min):** Write the 7-10 errors on the board in this format:
```
1. ❌ ___________  →  ✅ ___________
2. ❌ ___________  →  ✅ ___________
...
```

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


# Lista de archivos donde insertar (segun nivel)
def files_to_process():
    files = []
    a1_classes = [6, 11, 16]  # solo hasta Class 16 que existe
    for n in a1_classes:
        path = ROOT / 'A1' / f'A1_Class{n}_PRINT.md'
        if path.exists():
            files.append((path, 'es'))

    a2_classes = [6, 11]  # solo hasta Class 15 existe (15 -> next ER es Class 16, no existe aun)
    for n in a2_classes:
        path = ROOT / 'A2' / f'A2_Class{n}_PRINT.md'
        if path.exists():
            files.append((path, 'es'))

    a2_4h_classes = [6]  # solo hasta Class 10 existe
    for n in a2_4h_classes:
        path = ROOT / 'A2' / f'A2_4h_Class{n}_PRINT.md'
        if path.exists():
            files.append((path, 'es'))

    b2_classes = [6, 11, 16, 21]
    for n in b2_classes:
        path = ROOT / 'B2' / f'B2_Class{n}_PRINT.md'
        if path.exists():
            files.append((path, 'en'))

    return files


def insert_block(path, lang):
    text = path.read_text(encoding='utf-8')

    # Verificar si ya existe el bloque
    if 'ERROR PAPER REVIEW — DÍA 6' in text or 'ERROR PAPER REVIEW — DAY 6' in text:
        return f'  {path.relative_to(ROOT)}: already has Error Review block'

    # Buscar el bloque VATS y meter el bloque despues
    # Patron: "### ☐ 00:00-00:05 | VATS..." y luego encontrar el siguiente "###"
    pattern_vats = re.compile(
        r'(### [☐]?\s*\d+:\d+[-–—]+\d+:\d+\s*\|\s*VATS[^\n]*\n.*?)(\n### )',
        re.DOTALL | re.IGNORECASE
    )
    block = ERROR_REVIEW_BLOCK_EN if lang == 'en' else ERROR_REVIEW_BLOCK_ES

    new_text, n = pattern_vats.subn(r'\1\n' + block + r'\2', text, count=1)
    if n == 0:
        return f'  {path.relative_to(ROOT)}: VATS block not found, skipped'

    path.write_text(new_text, encoding='utf-8')
    return f'  {path.relative_to(ROOT)}: Error Review block inserted after VATS'


def main():
    print('Insertando bloque Error Paper Review...\n')
    for path, lang in files_to_process():
        print(insert_block(path, lang))
    print('\nDone. Run regen_all_pdfs.py to generate PDFs.')


if __name__ == '__main__':
    main()
