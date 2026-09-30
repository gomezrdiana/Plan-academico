# -*- coding: utf-8 -*-
"""Verificador de las guias del B1 nocturno 2h (Conv + Grammar, Cl 1-12) contra la doctrina vigente.
Uso desde la raiz:  python generadores/verificar_b1_2h.py [N_MAX]
Criterios 1-17 (ver encabezado de cada chequeo). Los cualitativos son heuristicas por marcadores."""
import os, re, sys, io
from pypdf import PdfReader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, 'VERSION_2', 'B1_2H')
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12

VIRT = ['PRUDENCIA', 'TEMPLANZA', 'JUSTICIA', 'FORTALEZA']
VIRT_EN = {'PRUDENCIA': 'PRUDENCE', 'TEMPLANZA': 'TEMPERANCE', 'JUSTICIA': 'JUSTICE', 'FORTALEZA': 'FORTITUDE'}
WEEKDAYS = r'\b(lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bado|domingo|monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b'
MONTHS = r'\b\d{1,2} de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b'
METHODS = r'\b(TBLT|Dogme|TPRS|PBL|CLIL|Task[- ]Based|Suggestopedia|Silent Way|Audio-?lingual|Lexical Approach|Communicative Approach|Total Physical Response)\b'
ALLOWED_DAY_PHRASES = ['(viernes y lunes, o jueves y viernes)', '(jueves y viernes, o viernes y lunes)',
                       '(lunes, miercoles y viernes alternos)', '(martes, jueves y viernes alternos)']
STOP = {'THE', 'A', 'AN', 'OF', 'TO', 'AT', 'AND', 'AFTER', 'FOR', 'IN', 'ON', 'WHO', 'WHAT', 'IS', 'IT', 'DO', 'DOES'}


def path(track, n):
    if track == 'CONV':
        return os.path.join(BASE, 'CONVERSACION', 'B1_Clase%d_CONV_PRINT.md' % n)
    return os.path.join(BASE, 'GRAMATICA', 'B1_Clase%d_GRAMMAR_PRINT.md' % n)


def pdfs(track, n):
    d = 'CONVERSACION' if track == 'CONV' else 'GRAMATICA'
    return (os.path.join(BASE, d, 'GUIAS', 'B1_Clase%d_%s_GUIA.pdf' % (n, track)),
            os.path.join(BASE, d, 'REPORTES', 'B1_Clase%d_%s_REPORTE.pdf' % (n, track)))


def section(t, start_pat, end_pat):
    m = re.search(start_pat, t, re.M)
    if not m:
        return ''
    rest = t[m.end():]
    e = re.search(end_pat, rest, re.M)
    return rest[:e.start()] if e else rest


def body_before_nota(t):
    i = t.find('## NOTA INTERNA')
    return t if i < 0 else t[:i]


def b3_title(t):
    m = re.search(r"^## BLOQUE 3[^\n]*?(?:SIMULACION|HITO)[^:\n]*:\s*(.+?)\s*\(\d+'\)", t, re.M)
    if not m:
        return ''
    return m.group(1).strip()


def words(title):
    return {w for w in re.findall(r"[A-Z][A-Z'-]+", title.upper()) if w not in STOP}


def frase(t):
    m = re.search(r'\*\*Frase del D[ií]a:\*\*\s*\*"(.+?)"\*', t)
    return m.group(1).strip() if m else ''


def checks(track, n):
    t = io.open(path(track, n), encoding='utf-8').read()
    low = t.lower()
    lines = t.splitlines()
    body = body_before_nota(t)
    b1 = section(t, r'^## BLOQUE 1', r'^## BLOQUE 2')
    b2 = section(t, r'^## BLOQUE 2', r'^## BLOQUE 3')
    b3 = section(t, r'^## BLOQUE 3', r'^## BLOQUE 4')
    b4 = section(t, r'^## BLOQUE 4', r'^\[PAGEBREAK\]')
    nota = t[t.find('## NOTA INTERNA'):] if '## NOTA INTERNA' in t else ''
    conv = track == 'CONV'
    r = {}
    # 1 cabecera
    if conv:
        h1 = '# B1 MASTERY NOCTURNO 2H — Cl %d/44 CONVERSACION (lunes, miercoles y viernes alternos) — HOJA DE RUTA' % n
        h2 = r'^\*\*Conv %d/44 · 120 min · 6:30-8:30 PM · Bloques: [^\n]*= 120\*\*$' % n
    else:
        h1 = '# B1 MASTERY NOCTURNO 2H — Cl %d/44 GRAMATICA (martes, jueves y viernes alternos) — HOJA DE RUTA' % n
        h2 = r'^\*\*Grammar %d/44 · 120 min · 6:30-8:30 PM · Bloques: [^\n]*= 120\*\*$' % n
    r['01_cabecera'] = lines[0].strip() == h1 and bool(re.match(h2, lines[2])) and '/88' not in t \
        and not re.search(r'noche \d+ de (88|10)', t)
    # 2 virtud
    v = VIRT[((n - 1) // 5) % 4]
    k = (n - 1) % 5 + 1
    a = ((n - 1) // 5) * 5 + 1
    r['02_virtud'] = bool(re.search(r'^\*\*Virtud:\*\* %s — Cl %d de 5 de esta virtud \(Cl %d-%d de cada pista\)'
                                    % (v, k, a, a + 4), t, re.M))
    # 3 frase del dia
    fr = frase(t)
    r['03_frase'] = bool(fr) and 'ANTES de que entren' in b1 and '3+ veces' in t and 'de memoria' in t
    # 4 HOY SOLO pag 1
    head = '\n'.join(lines[:25])
    r['04_hoy_solo'] = 'HOY SOLO' in head and 'NO TOCAR' in head.upper()
    # 5 bloques
    mins = [int(x) for x in re.findall(r"^## BLOQUE \d[^\n]*?\((\d+)'\)", t, re.M)]
    heads = re.findall(r'^## BLOQUE (\d)', t, re.M)
    mh = re.search(r"B1 (\d+)' \+ B2 (\d+)' \+ B3 (\d+)' \+ B4 (\d+)'", lines[2])
    r['05_4bloques=120'] = heads == ['1', '2', '3', '4'] and len(mins) == 4 and sum(mins) == 120 \
        and bool(mh) and [int(x) for x in mh.groups()] == mins
    # 6 bloque 1
    ok6 = '6:30' in b1 and '6:45' in b1 and 'inasistencia' in b1
    if not (conv and n == 1):
        ok6 = ok6 and 'SENT' in b1 and 'mejora' in b1.lower() and '5 seg' in b1 \
            and 'That is coordination' in b1 and 'PASE' in b1
        if n >= 2:
            ok6 = ok6 and 'Si dictaste tu la clase anterior' in b1
    if n >= 8:
        ok6 = ok6 and ('Cl %d' % (n - 3)) in b1 and ('Cl %d' % (n - 7)) in b1
    elif n >= 4:
        ok6 = ok6 and ('Cl %d' % (n - 3)) in b1
    elif not (conv and n == 1):
        ok6 = ok6 and ('no existen' in b1 or 'Cl 1' in b1)
    mv = re.search(r"(VATS|\[VIRTUD\])[^\n]*?\((\d)(?:-(\d))?'", b1)
    vmin = int(mv.group(3) or mv.group(2)) if mv else 0
    ok_vats = 5 <= vmin <= 7 and (VIRT_EN[v] in b1.upper() or v in b1.upper()) \
        and ('por que' in b1.lower() or 'porque' in b1.lower())
    if n in (1, 6, 11):
        ok_vats = ok_vats and ('OPENING' in b1 or 'ABRE' in b1)
    r['06_bloque1'] = ok6
    r['06_vats5-7'] = ok_vats
    # 7 portafolio
    hw = section(t, r'^\*\*Tarea', r'^```\s*$\n(?!HOMEWORK)')
    hwb = re.search(r'```\n(HOMEWORK.*?)```', t, re.S)
    hwt = hwb.group(1) if hwb else ''
    hwl = ' '.join(hwt.lower().split())
    long_hw = [l for l in hwt.split('\n') if len(l) > 78]
    r['07_video'] = ('minimum 3 minutes' in hwl and 'straight' in hwl and 'no reading' in hwl
                     and 'whatsapp' in hwl and 'audio only by exception' in hwl
                     and not re.search(r'audio\s*(/|o|or)\s*video', low) and not long_hw)
    # 8 tarea
    ok8 = 'DUE: TODAY, and in any case BEFORE 6:30 PM tomorrow' in hwt and '7:00 PM' not in t \
        and '30-45 min (B1)' in hwt and 'not fragmented' in hwl
    if conv:
        ok8 = ok8 and 'ONE TASK ONLY: THE VIDEO' in hwt and '(1) WRITTEN' not in hwt
    else:
        ok8 = ok8 and '(1) WRITTEN' in hwt and '(2) DAILY PORTFOLIO VIDEO' in hwt
    r['08_tarea'] = ok8
    # 10 PASE
    if conv:
        pm = re.search(r'```\nPASE Conv Cl %d -> Grammar Cl %d.*?```' % (n, n), t, re.S)
        ttl = b3_title(t)
        r['10_pase'] = bool(pm) and bool(ttl) and ttl.split(' — ')[0].split(':')[0][:18] in ' '.join(pm.group(0).split())
    else:
        pm = re.search(r'```\nPASE Grammar Cl %d -> Conv Cl %d.*?```' % (n, n + 1), t, re.S)
        r['10_pase'] = bool(pm)
    # 11 de pie (grammar)
    if not conv:
        mp = re.search(r'DE PIE:[^\n]*?(\d{2})%', t)
        pct = int(mp.group(1)) if mp else 0
        bh = re.findall(r'^## BLOQUE \d[^\n]*', t, re.M)
        r['11_de_pie'] = 70 <= pct <= 90 and all(('DE PIE' in h or 'SENTADOS' in h) for h in bh)
    # 12 ticket + error paper
    r['12_ticket_errorpaper'] = 'Ticket de salida' in b4 and '3-5 frases' in b4 and 'TODOS' in b4 \
        and 'anonim' in b4.lower() and 'con nombre' in b4.lower()
    # 13 checklist
    cl = re.search(r'^\*\*Checklist de salida:\*\*[^\n]*', t, re.M)
    cls = cl.group(0).lower() if cl else ''
    ok13 = all(x in cls for x in ['llegada tarde', 'asistencia', 'error paper', 'tickets', 'engrapad', 'fotos', 'pase'])
    if not (conv and n == 1):
        ok13 = ok13 and 'videos recibidos' in cls and 'mejora' in cls
    if conv and n == 1:
        ok13 = ok13 and 'grabaciones de entrada' in cls and 'auxiliar administrativa' in cls \
            and 'primera clase a la que asista' in low
    if conv and n == 10:
        ok13 = ok13 and 'auxiliar administrativa' in cls and 'hito' in cls
    r['13_checklist'] = ok13
    # 14 simulacion
    b3l = b3.lower()
    r['14_guest_obs_coach'] = 'guest' in b3l and 'observer' in b3l and 'coach' in b3l and 'nunca' in b3l
    # 15 prohibidos
    bd = body
    for ph in ALLOWED_DAY_PHRASES:
        bd = bd.replace(ph, '')
    bd = re.sub(r'"[^"\n]*\bon Monday\b[^"\n]*"', '', bd)
    bd = re.sub(r'help last Saturday', '', bd)  # item f verbatim del libro (A2 M17, Exercises 1 p.165) y su clave
    r['15_sin_dias_fechas'] = not re.search(WEEKDAYS, bd, re.I) and not re.search(MONTHS, bd, re.I)
    r['15_sin_metodos'] = not re.search(METHODS, t, re.I)
    r['15_sin_escape_7pm_nativos'] = '\\_' not in t and '7:00 PM' not in t and not re.search(r'\bnativ|\bnative\b', low)
    r['15_sin_tecnologia'] = not re.search(r'\b(video ?beam|proyector|parlante|tablet|kahoot|quizlet|youtube)\b', body, re.I)
    # 16 pdf
    g, rp = pdfs(track, n)
    gp = len(PdfReader(g).pages) if os.path.exists(g) else 99
    rpp, rtxt = 99, ''
    if os.path.exists(rp):
        rd = PdfReader(rp)
        rpp = len(rd.pages)
        rtxt = ' '.join((p.extract_text() or '') for p in rd.pages)
    r['16_pdf<=5'] = gp <= 5
    r['16_reporte_1pag'] = rpp == 1 and 'BLOQUE 4' in rtxt and 'Modulo' in rtxt
    # 17 proyecto
    if conv:
        r['17_mystory'] = 'MY STORY' in b2 and ('piece' in b2.lower() or 'pieza' in b2.lower())
    else:
        r['17_mystory'] = bool(re.search(r'no hay (avance de )?pieza', nota, re.I))
    return r, gp, mins, fr, b3_title(t)


def main():
    allok = True
    tot = {}
    frases = {}
    titles = {}
    for n in range(1, NMAX + 1):
        for track in ('CONV', 'GRAMMAR'):
            r, gp, mins, fr, ttl = checks(track, n)
            frases[(track, n)] = fr
            titles[(track, n)] = ttl
            fails = [k for k, v in r.items() if not v]
            for k, v in r.items():
                tot.setdefault(k, [0, 0])
                tot[k][1] += 1
                tot[k][0] += int(bool(v))
            if fails:
                allok = False
            print('%-7s Cl %2d pags=%d bloques=%s %s' % (track, n, gp, mins, 'OK' if not fails else 'FALLA: ' + ', '.join(fails)))
    # 3 frases distintas
    vals = [v.lower() for v in frases.values()]
    dup_fr = len(set(vals)) != len(vals) or '' in vals
    tot['03_frases_distintas_24'] = [0 if dup_fr else 1, 1]
    # 9 anti-duplicado
    probs = []
    for n in range(1, NMAX + 1):
        c, g = titles[('CONV', n)], titles[('GRAMMAR', n)]
        if not c or not g:
            probs.append('Cl %d sin titulo B3' % n)
            continue
        wc, wg = words(c), words(g)
        j = len(wc & wg) / max(1, len(wc | wg))
        if c.upper() == g.upper() or j >= 0.34:
            probs.append('Cl %d Conv/Grammar parecidos (%.2f): %s | %s' % (n, j, c, g))
    keys = list(titles)
    for i in range(len(keys)):
        for j2 in range(i + 1, len(keys)):
            a, b = titles[keys[i]], titles[keys[j2]]
            wa, wb = words(a), words(b)
            jj = len(wa & wb) / max(1, len(wa | wb))
            if a.upper() == b.upper() or jj >= 0.34:
                probs.append('%s %d vs %s %d parecidos (%.2f): %s | %s' % (keys[i][0], keys[i][1], keys[j2][0], keys[j2][1], jj, a, b))
    # Familias de escenario (mismo tipo de situacion y mismos roles): no deben repetirse entre las 24,
    # salvo pares revisados a mano en REVISADOS (distinto proposito, roles o meta; ver reporte).
    FAMILIAS = {'HANDOVER': r'HANDOVER', 'INSPECCION/AUDITORIA': r'INSPECTION|AUDIT',
                'INCIDENTE': r'INCIDENT', 'LLAMADA': r'\bCALL\b', 'AGENDA': r'SCHEDUL'}
    REVISADOS = {('GRAMMAR', 2, 'CONV', 9),     # cambio de turno (pendientes con hora) vs inventario por vacaciones (duenos)
                 ('GRAMMAR', 1, 'GRAMMAR', 9),  # rendicion de cuentas ante RRHH vs reclamacion ante aseguradora
                 ('GRAMMAR', 4, 'GRAMMAR', 10), # cliente agenda visita tecnica vs RRHH verifica referencia de un tercero
                 ('CONV', 5, 'GRAMMAR', 4), ('CONV', 5, 'CONV', 8), ('GRAMMAR', 4, 'CONV', 8)}  # agenda: semana del equipo / cita tecnica / cadencia de reuniones
    for fam, rx in FAMILIAS.items():
        hits = [k for k in keys if re.search(rx, titles[k].upper())]
        for i in range(len(hits)):
            for j2 in range(i + 1, len(hits)):
                a, b = hits[i], hits[j2]
                if (a[0], a[1], b[0], b[1]) in REVISADOS or (b[0], b[1], a[0], a[1]) in REVISADOS:
                    continue
                probs.append('familia %s repetida: %s %d (%s) | %s %d (%s)' % (fam, a[0], a[1], titles[a], b[0], b[1], titles[b]))
    tot['09_b3_distintos'] = [0 if probs else 1, 1]
    print()
    for k in sorted(tot):
        a, b = tot[k]
        print('%-28s %d/%d' % (k, a, b))
    if dup_fr:
        print('\nFRASES DUPLICADAS O VACIAS')
    if probs:
        print('\nB3 A REVISAR:')
        for p in probs:
            print('  ' + p)
    print('\nESCENARIOS B3:')
    for k in keys:
        print('  %-7s Cl %2d  %s' % (k[0], k[1], titles[k]))
    ok = allok and not dup_fr and not probs
    print('\nTODO VERDE' if ok else '\nHAY FALLAS')


if __name__ == '__main__':
    main()
