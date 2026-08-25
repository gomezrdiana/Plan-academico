import sys, os
ROOT = r"C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu"
sys.path.insert(0, ROOT)
from gen_a1_a2_clases_pdfs import md_to_pdf

BASE = os.path.join(ROOT, "VERSION_2", "B1_4H", "GRAMATICA")
for n in range(15, 20):
    md  = os.path.join(BASE, f"B1_Clase{n}_GRAMMAR_PRINT.md")
    pdf = os.path.join(BASE, "GUIAS", f"B1_Clase{n}_GRAMMAR_GUIA.pdf")
    md_to_pdf(md, pdf)
    print(n, os.path.getsize(pdf), "bytes")
