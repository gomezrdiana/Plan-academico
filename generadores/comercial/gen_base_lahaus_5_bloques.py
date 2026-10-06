# -*- coding: utf-8 -*-
"""Base del asistente (INFO_ACADEMIA_PARA_ASISTENTE.md) convertida a texto plano y partida en 5 bloques
para pegar en las 5 cargas manuales de la plataforma LaHaus. Salida: BASE_LAHAUS_5_BLOQUES_<fecha>.docx"""
import re, io, datetime
from docx import Document
from docx.shared import Pt, RGBColor

BASE = r'C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu\recursos\comercial\plataforma LaHaus'
SRC = BASE + r'\INFO_ACADEMIA_PARA_ASISTENTE.md'
fecha = datetime.date.today().strftime('%Y-%m-%d')
NAR = RGBColor(0xE5, 0x4C, 0x09); GRIS = RGBColor(0x66, 0x66, 0x66)

md = io.open(SRC, encoding='utf-8').read()

def plain(line):
    l = line.rstrip()
    if l.startswith('#'):
        return l.lstrip('#').strip().upper()
    l = re.sub(r'\*\*([^*]+)\*\*', r'\1', l)
    l = re.sub(r'\*([^*]+)\*', r'\1', l)
    l = re.sub(r'^\s*[-•]\s+', '• ', l)
    l = l.replace('`', '')
    return l

# secciones de primer nivel (## )
parts = re.split(r'\n(?=## )', md)
sections = []
for p in parts:
    lines = [plain(x) for x in p.split('\n')]
    txt = '\n'.join(x for x in lines if x is not None)
    txt = re.sub(r'\n{3,}', '\n\n', txt).strip()
    if txt: sections.append(txt)

# partir por parrafos (lineas en blanco) para equilibrar; un encabezado de seccion nunca queda al final de un bloque
SEP = chr(10)
paras = []
for sec in sections:
    for chunk in sec.split(SEP):
        if chunk.strip(): paras.append(chunk.rstrip())
    paras.append('')  # linea en blanco entre secciones
total = sum(len(x) + 1 for x in paras)
target = total / 5
blocks, cur, acc = [], [], 0
for i, x in enumerate(paras):
    last_is_header = bool(cur) and cur[-1].isupper() and len(cur[-1]) < 120
    if cur and acc + len(x) > target * 1.05 and len(blocks) < 4 and not last_is_header:
        blocks.append(SEP.join(cur)); cur, acc = [], 0
    cur.append(x); acc += len(x) + 1
if cur: blocks.append(SEP.join(cur))
while len(blocks) > 5:
    blocks[-2] = blocks[-2] + SEP + blocks[-1]; blocks.pop()

d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(10)
for sct in d.sections: sct.left_margin = sct.right_margin = Pt(56); sct.top_margin = sct.bottom_margin = Pt(48)
p = d.add_paragraph(); r = p.add_run(f'BASE DEL ASISTENTE v{fecha} — 5 BLOQUES PARA PEGAR EN LAHAUS'); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = NAR
p = d.add_paragraph(); r = p.add_run('Cada bloque reemplaza COMPLETO el bloque del mismo número que hoy está cargado (las 5 cargas manuales). Se pega tal cual, en orden. Al terminar: borrar cualquier texto viejo que haya quedado fuera de estos cinco.'); r.italic = True; r.font.size = Pt(9.5); r.font.color.rgb = GRIS
for i, b in enumerate(blocks, 1):
    d.add_page_break()
    p = d.add_paragraph(); r = p.add_run(f'BLOQUE {i} DE {len(blocks)}  ·  {len(b):,} caracteres  ·  pegar en la carga manual #{i} (reemplaza todo)'); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = NAR
    for line in b.split('\n'):
        q = d.add_paragraph(); q.paragraph_format.space_after = Pt(2)
        rr = q.add_run(line); rr.font.size = Pt(10)
        if line.isupper() and len(line) < 120: rr.bold = True
out = BASE + rf'\BASE_LAHAUS_5_BLOQUES_{fecha}.docx'
try: d.save(out); print('OK', out)
except PermissionError: d.save(out.replace('.docx', '_v2.docx')); print('ABIERTO -> _v2')
print('bloques:', [len(b) for b in blocks], 'total', total)
