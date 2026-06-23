import fitz, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
doc = fitz.open('Libros/Full B1 Book - Rev. 1.pdf')
start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end = int(sys.argv[2]) if len(sys.argv) > 2 else 40
for i in range(start-1, min(end, doc.page_count)):
    print(f'--- PAGE {i+1} ---')
    print(doc[i].get_text())
