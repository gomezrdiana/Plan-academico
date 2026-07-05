#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""
Regenera TODOS los PDFs de guias B&W desde PRINT.md.
Uso: python regen_all_pdfs.py
"""
import os, sys

# Importar md_to_pdf desde el script existente
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_a1_a2_clases_pdfs import md_to_pdf

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a1_dir = os.path.join(base, 'A1')
a2_dir = os.path.join(base, 'A2')
b1_dir = os.path.join(base, 'B1')
b2_dir = os.path.join(base, 'B2')

# Mapping: PRINT.md filename -> output PDF filename
def get_pdf_name(print_md_name):
    """A1_Class15_PRINT.md -> A1_Clase15_GUIA.pdf
       B1_Clase1_CONV_PRINT.md -> B1_Clase1_CONV_GUIA.pdf"""
    name = print_md_name.replace('_PRINT.md', '_GUIA.pdf')
    name = name.replace('Class', 'Clase')
    return name

# Regenerar A1
for f in sorted(os.listdir(a1_dir)):
    if f.startswith('A1_Class') and f.endswith('_PRINT.md'):
        in_path = os.path.join(a1_dir, f)
        out_path = os.path.join(a1_dir, get_pdf_name(f))
        try:
            md_to_pdf(in_path, out_path)
        except PermissionError as e:
            print(f'PERM ERR (cierra el PDF): {out_path}')
        except Exception as e:
            print(f'ERR {f}: {e}')

# Regenerar A2 (nocturno)
for f in sorted(os.listdir(a2_dir)):
    if f.startswith('A2_Class') and f.endswith('_PRINT.md'):
        in_path = os.path.join(a2_dir, f)
        out_path = os.path.join(a2_dir, get_pdf_name(f))
        try:
            md_to_pdf(in_path, out_path)
        except PermissionError as e:
            print(f'PERM ERR (cierra el PDF): {out_path}')
        except Exception as e:
            print(f'ERR {f}: {e}')

# Regenerar A2 4h
for f in sorted(os.listdir(a2_dir)):
    if f.startswith('A2_4h_Class') and f.endswith('_PRINT.md'):
        in_path = os.path.join(a2_dir, f)
        out_path = os.path.join(a2_dir, get_pdf_name(f))
        try:
            md_to_pdf(in_path, out_path)
        except PermissionError as e:
            print(f'PERM ERR (cierra el PDF): {out_path}')
        except Exception as e:
            print(f'ERR {f}: {e}')

# Regenerar B1
if os.path.isdir(b1_dir):
    for f in sorted(os.listdir(b1_dir)):
        if f.endswith('_PRINT.md'):
            in_path = os.path.join(b1_dir, f)
            out_path = os.path.join(b1_dir, get_pdf_name(f))
            try:
                md_to_pdf(in_path, out_path)
            except PermissionError as e:
                print(f'PERM ERR (cierra el PDF): {out_path}')
            except Exception as e:
                print(f'ERR {f}: {e}')

# Regenerar B2
if os.path.isdir(b2_dir):
    for f in sorted(os.listdir(b2_dir)):
        if f.endswith('_PRINT.md'):
            in_path = os.path.join(b2_dir, f)
            out_path = os.path.join(b2_dir, get_pdf_name(f))
            try:
                md_to_pdf(in_path, out_path)
            except PermissionError as e:
                print(f'PERM ERR (cierra el PDF): {out_path}')
            except Exception as e:
                print(f'ERR {f}: {e}')

# Regenerar CALENDARIO_VIRTUDES (en recursos/calendarios/)
calendarios_dir = os.path.join(base, 'recursos', 'calendarios')
if os.path.isdir(calendarios_dir):
    md_to_pdf(os.path.join(calendarios_dir, 'CALENDARIO_VIRTUDES_2026.md'),
              os.path.join(calendarios_dir, 'CALENDARIO_VIRTUDES_2026.pdf'))

print('\nRegeneracion completa.')
