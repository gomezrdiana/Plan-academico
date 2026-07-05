#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""
Auditoria de las guias contra el Blueprint Heiiu.

Para cada *_PRINT.md verifica la presencia de los componentes core:
- VATS (apertura)
- GoldList
- Autochequeo / autoevaluacion / exit ticket
- Tarea / homework / inversion diaria
- Papel de errores / error paper
- Shadowing (donde aplica)
- Errores + Peer Correction
- Reporte / entregables

Reporta una matriz por archivo + resumen al final.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Patrones (regex con flag IGNORECASE).
COMPONENTS = {
    'VATS':       [r'\bVATS\b'],
    'GoldList':   [r'\bGoldList\b', r'\bGold\s*List\b'],
    'Autocheck':  [r'autochequeo', r'autoevaluaci[oó]n', r'self.?check', r'exit ticket', r'autoeval'],
    'Tarea':      [r'\bTAREA\b', r'\bTarea\b', r'\bhomework\b', r'inversi[oó]n diaria'],
    'ErrorPaper': [r'papel de errores', r'error paper'],
    'Shadowing':  [r'\bShadowing\b', r'\bshadow\b'],
    'PeerCorr':   [r'peer correction', r'errores.*peer', r'peer.*correction'],
    'Reporte':    [r'\bREPORTE\b', r'\bReporte\b', r'\bentregables\b', r'\bENTREGABLES\b'],
}

# Componentes que son OPCIONALES por nivel/tipo (no contar como "missing" si no estan)
OPTIONAL_BY_FILE = {
    # B1 conversacional: solo speaking, no necesariamente GoldList o Shadowing
    'B1_Clase1_CONV_PRINT.md': ['GoldList', 'Shadowing'],
    'B1_Clase2_CONV_PRINT.md': ['GoldList', 'Shadowing'],
    # Los refuerzos individuales no necesariamente tienen toda la estructura
    'REFUERZO_Yeison_Sesion1_PRINT.md': ['VATS', 'GoldList', 'Shadowing', 'PeerCorr'],
    'REFUERZO_Yeison_Sesion2_PRINT.md': ['VATS', 'GoldList', 'Shadowing', 'PeerCorr'],
}


def check_file(path):
    text = path.read_text(encoding='utf-8')
    results = {}
    for comp, patterns in COMPONENTS.items():
        found = any(re.search(p, text, re.IGNORECASE) for p in patterns)
        results[comp] = found
    return results


def find_all_files():
    found = []
    for sub in ['A1', 'A2', 'B1', 'B2']:
        d = ROOT / sub
        if d.is_dir():
            found.extend(sorted(d.glob('*_PRINT.md')))
    return found


def main():
    files = find_all_files()
    print(f'Auditoria Blueprint sobre {len(files)} archivos\n')

    # Header
    cols = list(COMPONENTS.keys())
    name_w = max(len(f.parent.name + '/' + f.name) for f in files) + 2
    print(f'{"Archivo":<{name_w}}', end='')
    for c in cols:
        print(f'{c:<11}', end='')
    print()
    print('-' * (name_w + 11 * len(cols)))

    # Files
    n_complete = 0
    issues_by_file = {}
    for f in files:
        rel = f'{f.parent.name}/{f.name}'
        results = check_file(f)
        optionals = OPTIONAL_BY_FILE.get(f.name, [])

        missing = [c for c, ok in results.items() if not ok and c not in optionals]
        if not missing:
            n_complete += 1
        else:
            issues_by_file[rel] = missing

        print(f'{rel:<{name_w}}', end='')
        for c in cols:
            ok = results[c]
            opt = c in optionals
            mark = 'OK' if ok else ('--' if opt else 'XX')
            print(f'{mark:<11}', end='')
        print()

    # Summary
    print()
    print('=' * 70)
    print(f'COMPLETOS: {n_complete}/{len(files)}')
    print(f'CON FALTANTES: {len(issues_by_file)}')

    if issues_by_file:
        print('\nDetalle de faltantes:')
        for rel, miss in issues_by_file.items():
            print(f'  {rel}:')
            print(f'    falta: {", ".join(miss)}')

    print('\nLeyenda: OK presente | XX falta | -- opcional segun tipo')


if __name__ == '__main__':
    main()
