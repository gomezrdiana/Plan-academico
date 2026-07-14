import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
import fitz
import io
import sys

# Redirige stdout a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pdf_path = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\Libros\Libro B1.pdf'
doc = fitz.open(pdf_path)

print(f'Total pages: {doc.page_count}')

# Extrae páginas 117 a 160 (índice base-0: 116 a 159)
start_page = 117  # base-1
end_page = 160    # base-1

out_path = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\generadores\_b1_book_p117_160.txt'

with open(out_path, 'w', encoding='utf-8') as f:
    for i in range(start_page - 1, min(end_page, doc.page_count)):
        page = doc.load_page(i)
        text = page.get_text()
        f.write(f'===== PAGE {i+1} =====\n')
        f.write(text)
        f.write('\n')

print(f'TEXT WRITTEN to {out_path}')

# Verifica tamaño
file_size = _hos.path.getsize(out_path)
print(f'File size: {file_size} bytes')
