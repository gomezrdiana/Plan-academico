#!/usr/bin/env python3
"""B1 Mastery — EDICION UNICA (4 h y 2 h): regenera las 87 GUIAS (Conv 1-44, Grammar 1-43)
desde los PRINT.md genericos de VERSION_2/B1_4H, mas la HOJA_LECTURA_POR_JORNADA.
Solo renderiza (md_to_pdf); no reescribe ningun PRINT.md.
Uso desde la raiz:  python generadores/gen_b1_4h_edicion_unica.py
Reportes despues:   python generadores/gen_reporte_v3.py B1_4H/CONVERSACION B1_4H/GRAMATICA"""
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
import os, re, glob
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1 = os.path.join(D, 'VERSION_2', 'B1_4H')


def paginas(pdf):
    return len(re.findall(rb'/Type\s*/Page[^s]', open(pdf, 'rb').read()))


filas = []
for pista in ('CONVERSACION', 'GRAMATICA'):
    carpeta = os.path.join(B1, pista)
    os.makedirs(os.path.join(carpeta, 'GUIAS'), exist_ok=True)
    for md in sorted(glob.glob(os.path.join(carpeta, 'B1_Clase*_PRINT.md')),
                     key=lambda p: int(re.search(r'Clase(\d+)_', p).group(1))):
        pdf = os.path.join(carpeta, 'GUIAS', os.path.basename(md).replace('_PRINT.md', '_GUIA.pdf'))
        md_to_pdf(md, pdf)
        filas.append((os.path.basename(pdf), os.path.getsize(pdf) // 1024, paginas(pdf)))

hoja = os.path.join(B1, 'HOJA_LECTURA_POR_JORNADA.md')
hoja_pdf = hoja.replace('.md', '.pdf')
md_to_pdf(hoja, hoja_pdf)
filas.append((os.path.basename(hoja_pdf), os.path.getsize(hoja_pdf) // 1024, paginas(hoja_pdf)))

for n, kb, p in filas:
    print('%-36s %4d KB  %d pag' % (n, kb, p))
print('TOTAL PDFs:', len(filas))
