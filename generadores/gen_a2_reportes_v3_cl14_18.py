# Reportes de clase v3 (cuerpo nuevo + cabecera por clase) — A2 PM Cl 14-18
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
import tempfile
from gen_a1_a2_clases_pdfs import md_to_pdf

CLASES = [
    (14, "JUSTICIA (dia 4/5)", "M16 Present Perfect (Irregular)",
     "M16: Present perfect con verbos IRREGULARES", "Simulacion: TRAVEL AGENCY"),
    (15, "JUSTICIA (dia 5/5)", "M17 Present Perfect vs Simple Past",
     "M17: Past simple o Present perfect?", "Drill fisico: PAST SIDE / PERFECT SIDE"),
    (16, "FORTALEZA (dia 1/5)", "M18 Passive Voice (participios regulares)",
     "M18: La voz pasiva (participios regulares)", "Simulacion: NEW EMPLOYEE ORIENTATION"),
    (17, "FORTALEZA (dia 2/5)", "M20 Gerunds as Subjects",
     "M20: El gerundio como SUJETO", "Simulacion: TEAM MEETING - THE TRAINING PLAN"),
    (18, "FORTALEZA (dia 3/5)", "M21 Gerunds after Prepositions",
     "M21: El gerundio despues de PREPOSICION", "Simulacion: SAFETY BRIEFING - FIRST DAY RULES"),
]

PLANTILLA = """# REPORTE DE CLASE — A2 (2h PM) · Clase {n}

**Modulo:** {modulo} · **Virtud:** {virtud}

**Fecha:** ____________  **Profesor:** ____________

## Ejecucion de bloques (marque lo que ocurrio)

- BLOQUE 1 — Apertura (recuperacion + portafolio + Frase del Dia):  [ ] Completo   [ ] Parcial   [ ] No se hizo
- BLOQUE 2 — {b2}:  [ ] Completo   [ ] Parcial   [ ] No se hizo
- BLOQUE 3 — {b3}:  [ ] Completo   [ ] Parcial   [ ] No se hizo
- BLOQUE 4 — Cierre (ticket de salida + tarea + error paper):  [ ] Completo   [ ] Parcial   [ ] No se hizo

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

if __name__ == "__main__":
    root = _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__)))
    for n, virtud, modulo, b2, b3 in CLASES:
        md = PLANTILLA.format(n=n, virtud=virtud, modulo=modulo, b2=b2, b3=b3)
        tmp = _hos.path.join(tempfile.gettempdir(), f"rep_a2_cl{n}.md")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(md)
        out = _hos.path.join(root, "A2", "V2", f"A2_Class{n}_REPORTE.pdf")
        md_to_pdf(tmp, out)
        _hos.remove(tmp)
