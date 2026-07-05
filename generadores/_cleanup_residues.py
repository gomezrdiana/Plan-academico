#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Escanea residuos en el repo Heiiu (excluye .git, backup_pre_clean, B2/reportes)."""
import os, re, sys

PATTERNS = [
    (r'.*_PRINT\.pdf$', 'PDF directo del print (convención vieja)'),
    (r'.*\.tmp\.pdf$', 'PDF temporal de iteración bloqueada por viewer'),
    (r'.*_GUIA_v[0-9_]+\.pdf$', 'GUIA con timestamp/versión'),
    (r'.*\.bak$', 'Backup inline'),
    (r'.*_pre_[a-z0-9]+\.md$', 'MD pre-modificación'),
    (r'.*_OLD\..*$', 'Marcado OLD'),
    (r'.*~$', 'Backup de editor'),
]

EXCLUDE = ('.git', 'backup_pre_clean', '__pycache__', '.claude', os.path.join('B2', 'reportes'))

residues = []
for root, dirs, files in os.walk('.'):
    norm = os.path.normpath(root)
    if any(ex in norm.split(os.sep) for ex in EXCLUDE):
        continue
    for f in files:
        full = os.path.join(root, f)
        for pat, desc in PATTERNS:
            if re.match(pat, f, re.IGNORECASE):
                size_kb = os.path.getsize(full) // 1024
                residues.append((full, desc, size_kb))
                break

if not residues:
    print('Sin residuos detectados.')
    sys.exit(0)

print(f'Encontrados {len(residues)} residuos:\n')
for path, desc, size in residues:
    print(f'  [{size:>5} KB] {path}   ({desc})')
print(f'\nTotal: {sum(r[2] for r in residues)} KB')
