# Reporte de clase v3 GENERICO: construye el REPORTE.pdf de cada PRINT.md vigente en VERSION_2.
# Cuerpo fijo (plantilla REPORTE_PROFE) + cabecera pre-llenada leida del propio PRINT
# (cohorte, Cl N, modulo, virtud, titulos reales de los 4 bloques).
# Uso desde la raiz:  python generadores/gen_reporte_v3.py            -> todos los cohortes
#                     python generadores/gen_reporte_v3.py A2_2H ...  -> solo esos
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
import io, re, glob, tempfile
from gen_a1_a2_clases_pdfs import md_to_pdf

ROOT = _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__)))
V2 = _hos.path.join(ROOT, 'VERSION_2')

COHORTE_LABEL = {
    'A1_4H': 'A1 (4h)', 'A1_2H': 'A1 (2h noche)',
    'A2_4H': 'A2 (4h)', 'A2_2H': 'A2 (2h PM)',
    'B1_4H': 'B1 Mastery (4h AM)', 'B1_2H': 'B1 (2h noche)',
    'B2_4H': 'B2 (4h)', 'B2_2H': 'B2 (2h noche)',
}

CUERPO = """
**Fecha:** ____________  **Profesor:** ____________

## Ejecucion de bloques (marque lo que ocurrio)

{bloques}

**Que salte o cambie y por que?** (2 lineas)

____________________________________________________________________

____________________________________________________________________

## 3 errores oidos hoy (cita textual, SIN nombres)

1. __________________________________________________________

2. __________________________________________________________

3. __________________________________________________________

## Asistencia y entregables

**Asistieron:** ______ de ______ estudiantes.  **Portafolio (quien hizo su audio/video?):** ______ de ______

- [ ] Tickets de salida recogidos (TODOS)   ·   [ ] Error papers recogidos   ·   [ ] Fotos/videos del dia

> El detalle con nombres (errores por estudiante, ausencias) va en su libreta privada para coordinacion, como siempre. Este reporte viaja fisico con los tickets y error papers.

**Firma del profesor:** ______________________________
"""


def parse_print(path):
    t = io.open(path, encoding='utf-8').read()
    m = re.search(r'\*\*Virtud:\*\*\s*([^\n]+)', t)
    virtud = m.group(1).split(' · ')[0].replace('**', '').strip() if m else None
    m = re.search(r'\*\*Modulos?:\*\*\s*([^\n]+)', t)
    modulo = m.group(1).replace('**', '').strip() if m else None
    if modulo and len(modulo) > 95:
        modulo = modulo[:92].rstrip() + '...'
    bloques = []
    for m in re.finditer(r'^##\s+(BLOQUE\s+\d[^\n]*)', t, re.M):
        titulo = m.group(1).replace('**', '').strip()
        bloques.append('- %s:  [ ] Completo   [ ] Parcial   [ ] No se hizo' % titulo)
    return virtud, modulo, bloques


def clase_de(nombre):
    m = re.search(r'Cla?s[se]{1,2}(\d+)', nombre)
    return m.group(1) if m else '?'


def track_de(nombre):
    for t in ('CONV', 'GRAMMAR'):
        if '_%s_' % t in nombre:
            return ' · ' + t
    return ''


def generar(cohorte):
    carpeta = _hos.path.join(V2, cohorte)
    prints = sorted(glob.glob(_hos.path.join(carpeta, '*_PRINT.md')))
    if not prints:
        return 0
    _hos.makedirs(_hos.path.join(carpeta, 'REPORTES'), exist_ok=True)
    n_ok = 0
    for p in prints:
        base = _hos.path.basename(p)
        virtud, modulo, bloques = parse_print(p)
        if len(bloques) < 4:
            print('SKIP (sin 4 bloques, es marcador?):', base)
            continue
        header = '# REPORTE DE CLASE — %s%s · Clase %s\n\n' % (
            COHORTE_LABEL.get(cohorte, cohorte), track_de(base), clase_de(base))
        linea2 = []
        if modulo:
            linea2.append('**Modulo:** %s' % modulo)
        if virtud:
            linea2.append('**Virtud:** %s' % virtud)
        if linea2:
            header += ' · '.join(linea2) + '\n'
        md = header + CUERPO.format(bloques='\n'.join(bloques))
        tmp = _hos.path.join(tempfile.gettempdir(), 'rep_v3_tmp.md')
        io.open(tmp, 'w', encoding='utf-8').write(md)
        out = _hos.path.join(carpeta, 'REPORTES', base.replace('_PRINT.md', '_REPORTE.pdf'))
        md_to_pdf(tmp, out)
        n_ok += 1
    return n_ok


if __name__ == '__main__':
    objetivos = _hsys.argv[1:] or sorted(COHORTE_LABEL)
    total = 0
    for c in objetivos:
        total += generar(c)
    print('Reportes v3 generados:', total)
