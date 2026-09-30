import os, re, sys
from pypdf import PdfReader

ROOT = r"C:\Users\pedro\Downloads\diana gt\heiiu\estrategia global Heiiu"
D = os.path.join(ROOT, 'VERSION_2', 'A1_2H')
VIRT = {}
for n in range(1, 46):
    VIRT[n] = ['PRUDENCIA', 'TEMPLANZA', 'JUSTICIA', 'FORTALEZA'][((n - 1) // 5) % 4] if n <= 40 else 'SINTESIS'

WEEKDAYS = r'\b(lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bado|domingo|monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b'
METHODS = r'\b(TBLT|Dogme|TPRS|PBL|CLIL|Task[- ]Based|Suggestopedia|Silent Way|Audio-?lingual|Lexical Approach|Communicative Approach|Total Physical Response)\b'

def body_before_nota(t):
    i = t.find('NOTA INTERNA')
    return t if i < 0 else t[:i]

def section(t, start_pat, end_pat):
    m = re.search(start_pat, t, re.M)
    if not m: return ''
    rest = t[m.end():]
    e = re.search(end_pat, rest, re.M)
    return rest[:e.start()] if e else rest

def checks(n):
    p = os.path.join(D, 'A1_2h_Class%d_PRINT.md' % n)
    t = open(p, encoding='utf-8').read()
    low = t.lower()
    body = body_before_nota(t)
    b1 = section(t, r'^## BLOQUE 1', r'^## BLOQUE 2')
    r = {}
    r['cabecera'] = bool(re.search(r'^# A1 2h · Cl %d — HOJA DE RUTA\s*$' % n, t, re.M))
    mv = re.search(r'\*\*Virtud:\*\*\s*([^\n]*)', t)
    exp = VIRT[n]
    r['virtud'] = bool(mv) and (exp in mv.group(1).upper().replace('Í', 'I') or (exp == 'SINTESIS' and 'SÍNTESIS' in mv.group(1).upper()))
    r['frase'] = bool(re.search(r'\*\*Frase del D[ií]a:\*\*', t))
    r['hoy_solo'] = 'HOY SOLO' in t and ('NO TOCAR' in t.upper())
    mins = [int(x) for x in re.findall(r"^## BLOQUE \d \((\d+)'\)", t, re.M)]
    r['4bloques=120'] = len(mins) == 4 and sum(mins) == 120
    r['6:45'] = '6:45' in b1
    r['mejora'] = 'mejora' in b1.lower() and 'that is coordination, not me' in b1.lower()
    vname = exp if exp != 'SINTESIS' else 'SINTESIS'
    r['vats_b1'] = (vname in b1.upper()) and ('VATS' in b1 or 'virtud' in b1.lower())
    if n >= 8:
        r['N-3/N-7'] = ('Cl %d' % (n - 3)) in b1 and ('Cl %d' % (n - 7)) in b1
    elif n >= 2:
        r['N-3/N-7'] = ('Cl %d' % max(1, n - 3)) in b1 or 'Cl 1' in b1
    else:
        r['N-3/N-7'] = True
    r['frase_b1'] = bool(re.search(r'Frase del D[ií]a', b1))
    r['BEFORE 6:30 PM'] = 'BEFORE 6:30 PM' in t and ('(Cl %d)' % (n + 1)) in t
    mt = re.search(r'TIME: (\d+)(?:-(\d+))? min', t)
    r['15-20 min'] = bool(mt) and 15 <= int(mt.group(1)) and int(mt.group(2) or mt.group(1)) <= 20 and 'NOT fragmented' in t
    hw = ' '.join(t[t.find('HOMEWORK'):].split())
    r['video_diario'] = ('in one take' in hw and 'WITHOUT reading' in hw and 'WhatsApp' in hw and ('Audio only by exception' in hw or 'Audio does NOT count' in hw))
    r['ticket'] = bool(re.search(r'Ticket de salida', t))
    r['error_paper_doble'] = 'anonimo' in low.replace('ó', 'o') and 'libreta' in low
    chk = ['llegada tarde', 'videos recibidos', 'error paper', 'tickets', 'fotos']
    r['checklist_v3'] = all(k in low for k in chk) and '□' in t
    r['guest/observer/coach'] = all(k in low for k in ['guest', 'observer', 'coach']) if n not in (11, 22, 23, 44) else True
    r['no_7:00PM'] = '7:00 PM' not in t and '7:00 pm' not in low
    r['no_audio/video'] = not re.search(r'audio\s*(/|o)\s*video', low)
    r['no_\\_'] = '\\_' not in t
    r['no_dias_semana'] = not re.search(WEEKDAYS, body, re.I)
    r['no_metodologias'] = not re.search(METHODS, t, re.I)
    if n in (10, 20, 30, 40):
        r['hito'] = 'hito' in low and 'auxiliar administrativa' in low
    if n == 1:
        r['grab_entrada'] = 'grabacion de entrada' in low.replace('ó', 'o') and 'auxiliar administrativa' in low
    if n == 44:
        r['grab_salida_vs_Cl1'] = 'salida' in low and 'Cl 1' in t and 'entrada' in low
    g = os.path.join(D, 'GUIAS', 'A1_2h_Class%d_GUIA.pdf' % n)
    rp = os.path.join(D, 'REPORTES', 'A1_2h_Class%d_REPORTE.pdf' % n)
    gp = len(PdfReader(g).pages) if os.path.exists(g) else 99
    rpp = len(PdfReader(rp).pages) if os.path.exists(rp) else 99
    r['pdf<=5'] = gp <= 5
    r['reporte=1'] = rpp == 1
    return r, gp, mins

allok = True
crit_tot = {}
for n in range(1, 45):
    r, gp, mins = checks(n)
    fails = [k for k, v in r.items() if not v]
    for k, v in r.items():
        crit_tot.setdefault(k, [0, 0])
        crit_tot[k][1] += 1
        crit_tot[k][0] += int(bool(v))
    if fails: allok = False
    print('Cl %2d pags=%d bloques=%s %s' % (n, gp, mins, 'OK' if not fails else 'FALLA: ' + ', '.join(fails)))
print()
for k, (a, b) in crit_tot.items():
    print('%-22s %d/%d' % (k, a, b))
print('\nTODO VERDE' if allok else '\nHAY FALLAS')
