#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""
Limpia los PRINT.md de las guias.

Reglas:
1. Hace backup en backup_pre_clean/ antes de tocar nada.
2. Elimina lineas/bloques de boilerplate generico (que ya viven en MANUAL_PROFESOR_REGLAS_GENERALES).
3. Elimina secciones nombradas:
   - "## 🚨 REPORTES DE LA CLASE ANTERIOR ..."
   - "## 🎚️ LAS 3 TECNICAS DE CONTROL 80-20 ..."
   - "## 🎯 TUS 5 RESPUESTAS ..."
4. Despues del header, limpia los `---` consecutivos resultantes.

NO toca:
- El header (titulo, modulo, profesor/fecha/presentes).
- Bloques pedagogicos del modulo (incluyendo "PUENTE M_X -> M_Y" si existe).
- Bloques que arrancan con `### ☐` o similares.

Uso:
    python clean_guides.py [--dry-run] [archivo1 archivo2 ...]
    python clean_guides.py --all       # limpia TODOS los PRINT.md
"""
import os, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKUP_DIR = ROOT / 'backup_pre_clean'

# === LINEAS DE BOILERPLATE A ELIMINAR ===
# Cualquier linea cuyo texto (limpiando markdown) empieza con uno de estos prefijos.
BOILERPLATE_LINE_PREFIXES = [
    '⚠️ EL MÓDULO DEL LIBRO Y LOS EJERCICIOS NO DEBEN EXCEDER',
    '⏱️ CRONOMETRA CADA ACTIVIDAD',
    '⏱️ SI UNA ACTIVIDAD SE PASA DEL TIEMPO',
    '📹 Puedes grabar cualquier actividad',
    '📹 You may record any activity',
    'REGLAS: Celular BOCA ABAJO',
    'RULES: Phone FACE-DOWN',
    'TÉCNICA DE CORRECCIÓN:',
    '📝 PAPEL DE ERRORES ES OBLIGATORIO',
    '📝 ERROR PAPER IS MANDATORY',
    '🚫 NO NEGOCIABLE:',
    '🚫 NO comuniques información',
    '🚫 SIGUE LA GUÍA AL PIE DE LA LETRA',
    '⏱️ TIME EVERY ACTIVITY',
]

# === SECCIONES H2 A ELIMINAR (titulo + cuerpo hasta el siguiente ## o ###) ===
# Match si la linea ## empieza con uno de estos textos (despues del ##).
SECTION_TITLES_TO_REMOVE = [
    '🚨 REPORTES DE LA CLASE ANTERIOR',
    '🎚️ LAS 3 TÉCNICAS DE CONTROL 80-20',
    '🎚️ LAS 3 TECNICAS DE CONTROL 80-20',
    '🎯 TUS 5 RESPUESTAS',
]

# === SECCIONES H3 A ELIMINAR (titulo + cuerpo hasta el siguiente ## o ###) ===
# Estas son refuerzos basados en errores reportados que NO deben vivir en la guia base.
H3_TITLES_TO_REMOVE = [
    '🚨 REFUERZO CRÍTICO',
    '🚨 REFUERZO CRITICO',
]

# === LINEAS DE BLOCKQUOTE A ELIMINAR (referencias a tecnicas que viven en el manual) ===
# Si una linea empieza con > y contiene cualquiera de estos textos, se elimina.
BLOCKQUOTE_FRAGMENTS_TO_REMOVE = [
    'TIEMPO PROFESOR',
    '30 fichas',
    'Time Watchers',
    'Cuenta las fichas',
    'cuenta tus fichas',
    'Cuenta tus fichas',
]

# === LINEAS DENTRO DE BLOQUES QUE TAMBIEN SE ELIMINAN ===
# Si una linea contiene cualquiera de estos textos, se elimina (excepto si es header).
INLINE_FRAGMENTS_TO_REMOVE = [
    'META MEDIBLE HOY',
    'Las 30 fichas del profesor',
    'fichas en el bolsillo',
]


def strip_md_emphasis(line):
    """Quita ** y * para comparar prefijos sin formato."""
    return line.replace('**', '').replace('*', '').strip()


def line_is_boilerplate(line):
    clean = strip_md_emphasis(line)
    return any(clean.startswith(p) for p in BOILERPLATE_LINE_PREFIXES)


def line_is_blockquote_to_remove(line):
    s = line.lstrip()
    if not s.startswith('>'):
        return False
    return any(frag in line for frag in BLOCKQUOTE_FRAGMENTS_TO_REMOVE)


def line_is_inline_fragment_to_remove(line):
    return any(frag in line for frag in INLINE_FRAGMENTS_TO_REMOVE)


def clean_text(text):
    lines = text.split('\n')
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        clean = strip_md_emphasis(line)

        # 1. Si es un H2 que empieza con uno de los titulos a eliminar, brincar todo
        # hasta el siguiente H2 o H3 (o EOF).
        if line.lstrip().startswith('##') and not line.lstrip().startswith('###'):
            stripped_after_hashes = line.lstrip().lstrip('#').strip()
            if any(stripped_after_hashes.startswith(t) for t in SECTION_TITLES_TO_REMOVE):
                i += 1
                while i < n:
                    nxt = lines[i].lstrip()
                    if nxt.startswith('##') or nxt.startswith('###'):
                        break
                    i += 1
                continue

        # 1b. Si es un H3 que empieza con titulo a eliminar (e.g. REFUERZO CRITICO),
        # brincar hasta el siguiente ### o ## (o EOF).
        if line.lstrip().startswith('###'):
            stripped_after_hashes = line.lstrip().lstrip('#').strip()
            # Quitar checkbox si lo tiene: "☐ 00:13... | 🚨 REFUERZO ..."
            if any(t in stripped_after_hashes for t in H3_TITLES_TO_REMOVE):
                i += 1
                while i < n:
                    nxt = lines[i].lstrip()
                    if nxt.startswith('##') or nxt.startswith('###'):
                        break
                    i += 1
                continue

        # 2. Si la linea es boilerplate, brincarla.
        if line_is_boilerplate(line):
            i += 1
            continue

        # 3. Si la linea es blockquote con fragmentos a eliminar, brincarla.
        if line_is_blockquote_to_remove(line):
            i += 1
            continue

        # 4. Si la linea contiene fragmentos inline a eliminar (META MEDIBLE), brincarla.
        if line_is_inline_fragment_to_remove(line):
            i += 1
            continue

        out.append(line)
        i += 1

    # 3. Colapsar secuencias de --- y lineas en blanco repetidas (mas de 2 seguidas)
    collapsed = []
    blank_run = 0
    for line in out:
        if line.strip() == '':
            blank_run += 1
            if blank_run <= 2:
                collapsed.append(line)
        else:
            blank_run = 0
            collapsed.append(line)

    # 4. Colapsar `---` consecutivos (con blancos entre ellos): si encuentra 2+ en seguida, deja solo 1
    final = []
    j = 0
    m = len(collapsed)
    while j < m:
        line = collapsed[j]
        if line.strip() == '---':
            final.append(line)
            # Saltar otros --- consecutivos (con blancos entre ellos)
            k = j + 1
            while k < m and (collapsed[k].strip() == '' or collapsed[k].strip() == '---'):
                if collapsed[k].strip() == '---':
                    # esta es otro separador, brincamos el anterior y todo en medio
                    j = k
                k += 1
            j += 1
        else:
            final.append(line)
            j += 1

    return '\n'.join(final)


def process_file(path, dry_run=False):
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding='utf-8')
    cleaned = clean_text(text)

    if cleaned == text:
        return 'unchanged', 0

    delta = len(text) - len(cleaned)
    pct = round(100 * delta / len(text), 1) if len(text) else 0

    if dry_run:
        return f'would-clean (-{delta} chars, -{pct}%)', delta

    # Backup
    backup_path = BACKUP_DIR / rel
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, backup_path)

    path.write_text(cleaned, encoding='utf-8')
    return f'cleaned (-{delta} chars, -{pct}%)', delta


def find_all_print_files():
    found = []
    for sub in ['A1', 'A2', 'B1', 'B2']:
        d = ROOT / sub
        if d.is_dir():
            found.extend(sorted(d.glob('*_PRINT.md')))
    return found


def main():
    args = sys.argv[1:]
    dry_run = '--dry-run' in args
    args = [a for a in args if a != '--dry-run']

    if not args or args == ['--all']:
        files = find_all_print_files()
    else:
        files = [Path(a) if Path(a).is_absolute() else ROOT / a for a in args]

    print(f'{"DRY RUN" if dry_run else "APPLYING"} on {len(files)} files...\n')
    total_delta = 0
    n_changed = 0
    for f in files:
        if not f.exists():
            print(f'  SKIP (missing): {f}')
            continue
        status, delta = process_file(f, dry_run=dry_run)
        total_delta += delta
        if 'unchanged' not in status:
            n_changed += 1
        print(f'  {status:35s}  {f.relative_to(ROOT)}')

    print(f'\nTotal: {n_changed} files affected, -{total_delta} chars total.')
    if not dry_run and n_changed:
        print(f'Backups in: {BACKUP_DIR}')


if __name__ == '__main__':
    main()
