import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
import fitz
import sys

pdf_path = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\Libros\Full B1 Book - Rev. 1.pdf'
doc = fitz.open(pdf_path)
print('PAGES:', doc.page_count)
toc = doc.get_toc()
print('--- TOC ---')
for e in toc[:120]:
    print(e)
print('--- END TOC ---')
# Save full text to a temp file
out_path = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\_b1_book_text.md'
with open(out_path, 'w', encoding='utf-8') as f:
    for i in range(min(doc.page_count, 120)):
        page = doc.load_page(i)
        text = page.get_text()
        f.write(f'\n\n===== PAGE {i+1} =====\n')
        f.write(text)
print('TEXT WRITTEN to', out_path)
