import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
import os
base = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\B1'
for n in (34, 35, 36, 37, 38):
    md = os.path.join(base, f'B1_Clase{n}_CONV_PRINT.md')
    pdf = os.path.join(base, f'B1_Clase{n}_CONV_GUIA.pdf')
    with open(md, 'r', encoding='utf-8') as f:
        lines = sum(1 for _ in f)
    pdf_kb = os.path.getsize(pdf) // 1024
    print(f'Cl {n}: {lines} lines | PDF {pdf_kb} KB')
