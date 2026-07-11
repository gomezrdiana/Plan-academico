---
name: clases
description: Genera guías HOJA DE RUTA (1 pág ejecutable + anexo opcional, tope 5 págs) y reportes Heiiu de un día o un rango lunes-viernes, para los 5 cohortes (A2 4h AM, B1 Mastery Conv+Grammar, A1 noche, A2 PM noche, B2 PM Amina). Para cada cohorte lee la guía previa para continuidad, verifica el módulo siguiente en el libro (sigue libro, salta huecos, nunca inventa), calcula la virtud por número de clase, aplica todos los no-negociables Heiiu (Frase del Día / numeración consecutiva / sin nombres / sin metodologías / sin comunicar evals / simulación profesional / tarea estricta / error paper doble / recuperación espaciada N-3 y N-7 / chequeo portafolio / ticket de salida / cero material físico / B1 PASE / B2 vocab bank + trabalenguas + fase / A2 4h arco repaso / marcadores en clases de examen), genera PRINT.md + script generador + PDF guía + PDF reporte estático, lanza los cohortes del mismo día en paralelo (B1 = 1 agente con Conv+Grammar), verifica en disco (≤5 páginas) y reporta tabla resumen con módulo/virtud/Frase del Día/páginas/supuestos.
---

# clases — generador de guías Heiiu (formato HOJA DE RUTA)

Invocación: `/clases <fecha o rango> [filtro opcional]`. Ejemplos:
- `/clases lunes 25/05` → los 5 cohortes ese día
- `/clases 25-29/05` o `/clases semana del 25/05` → semana completa Lu-Vi (día por día secuencial; cohortes del día en paralelo)
- `/clases jueves 28/05 solo B1` → un cohorte específico

Si la fecha es ambigua, resuélvela con el contexto (`currentDate` del entorno + memoria del último día generado). No preguntes salvo que sea imposible inferir.

> **Formato vigente desde 06/07/2026: HOJA DE RUTA** (decisión Diana, spec en `documentos_operativos/WORKFLOW_CLAUDE_HEIIU.md` §5 y §9). Las guías previas al 06/07 son formato largo (hasta 12 págs): sirven SOLO para continuidad de contenido, **NO como plantilla de formato**.

## 1. Los 5 cohortes

| Cohorte | Profe(s) | Formato | Total nivel | Archivos |
|---|---|---|---|---|
| **A2 4h AM** intensivo | Tomás | 4h · 28 cl · A2 110h | 110h | `A2/A2_4h_Class{N}_PRINT.md` — **TERMINADO (Cl 28/28, final 29/05)** |
| **B1 Mastery 4h AM** | Danna Conv 8-10 + Juan Diego Grammar 10-12 | 4h = 2 bloques · 44 ses · B1 175h | 175h | `VERSION_2/B1_4H/B1_Clase{N}_CONV_PRINT.md` y `..._GRAMMAR_PRINT.md` → GUIA en `VERSION_2/B1_4H/GUIAS/` · REPORTE en `VERSION_2/B1_4H/REPORTES/` |
| **A1 noche** | Christian (cohorte de 6) | 2h · 45 cl | 90h | `A1/A1_Class{N}_PRINT.md` — **TERMINADO (Cl 45/45)** |
| **A1 4h AM** (nuevo desde 06/07/2026) | (por confirmar) | 4h · ~22-23 cl | 90h | `VERSION_2/A1_4H/A1_4h_Class{N}_PRINT.md` → GUIA en `VERSION_2/A1_4H/GUIAS/` · REPORTE en `VERSION_2/A1_4H/REPORTES/` · hitos: mini-pres Cl 6 · midterm Cl 11-12 · final Cl 22-23 · proyecto "MY WORLD" (supuesto por confirmar) |
| **A2 PM noche (cohorte nuevo desde ~15/06)** | Tomás | 2h · 55 cl | 110h | `VERSION_2/A2_2H/A2_Class{N}_PRINT.md` → GUIA en `VERSION_2/A2_2H/GUIAS/` · REPORTE en `VERSION_2/A2_2H/REPORTES/` (Cl 14-18 ya en hoja de ruta) |

**Estructura de carpetas (desde 10/07/2026):** todo lo vigente vive en `VERSION_2/{NIVEL}_{4H|2H}/` (PRINT.md en la raíz del cohorte, PDFs en `GUIAS/` y `REPORTES/`; las carpetas `_4H` cubren entre semana + taller sabatino, salvo B2 que no tiene sabatino). Todo lo viejo (cohortes terminados + formato pre-hoja-de-ruta, incluidas las clases pasadas de cohortes activos) está en `VERSION_1/` — **de ahí NO se imprime ni se regenera**, pero SÍ se lee para continuidad (guía previa, recuperación N-3/N-7, virtudes/frases ya usadas): las guías viejas del A2 PM están en `VERSION_1/A2/V2/`, las del B1 cohorte 2 en `VERSION_1/B1/B1_*_V2/`.
| **B2 PM Amina** | Amina | 2h · 36 ses | 72h con Amina | `B2/B2_PM_Amina_Clase{N}_PRINT.md` — **TERMINADO (Cl 35 + Final Cl 36 evaluador externo)** |

## 2. Formato HOJA DE RUTA (obligatorio para toda guía nueva)

**Página 1 = LA guía.** Todo lo que el profe debe ejecutar cabe en 1 página (2 como máximo absoluto en clases de 4h). Un profe que ejecute la hoja ejecuta el método completo sin leer nada más.

```
# {NIVEL} · Cl {N} · {TRACK si aplica} — HOJA DE RUTA
Virtud: {virtud} · Frase del Día: "{frase}"

## BLOQUE 1 ({min}') — Apertura
- Recuperación espaciada (10'): [instrucción EXACTA de qué recuperar de
  Cl N-3 y Cl N-7 — oral, de pie]
- Chequeo público de portafolio (3'): "Who did their daily audio/video?"
  (el profe pregunta y anota; NO revisa contenido)
- Warm-up del día + Frase del Día en tablero

## BLOQUE 2 ({min}') — {Módulo/contenido}
- [qué escribir en el tablero, verbatim del libro: regla + ejemplos + pág]
- [actividad de práctica con instrucción exacta]

## BLOQUE 3 ({min}') — {Simulación / producción}
- [simulación profesional realista: rol, escenario, quién de pie,
  patrón 1 guest + observers activos]

## BLOQUE 4 ({min}') — Cierre
- Ticket de salida (5'): cada estudiante escribe 3-5 frases con la
  estructura de hoy. Se recogen TODOS.
- Tarea: [qué] — DUE: Cl {N+1} antes de {hora}
- Error paper + anuncio próxima clase

□ Reporte firmado  □ Error papers  □ Tickets de salida  □ Fotos/videos
```

**Reglas fijas de la estructura:**
- **Bloque 1 abre SIEMPRE con recuperación espaciada** de Cl N-3 y Cl N-7 (si N<8, usa las que existan; N=1 solo warm-up). Con instrucción exacta — lo opcional no ocurre. Si el mapa semanal de tickets tiene errores reales procesados, construye la recuperación con ESOS errores y dilo en la hoja ("coordinación leyó sus tickets — error común: X"). **Si no hay tickets procesados, usa el contenido de los módulos de N-3/N-7 y NO menciones tickets** — nunca fabricar señal que no existe.
- **Bloque 1 incluye el chequeo público de portafolio** (~3 min). El profe solo pregunta y anota — el contenido lo revisa coordinación.
- **Bloque 4 cierra SIEMPRE con el ticket de salida** (5 min) antes de tarea y error paper.
- **4 bloques largos, NO 12-13 actividades cortas** (regla 18/06 — el modelo inmersivo).
- **Cero material físico del profe/academia** (sin liquidez): cualquier objeto (cartas, sobres, props) = el profe lo pide al estudiante con anticipación como tarea, con Plan B escrito en la hoja.

- **Bloques 2 y 3 SOLO se construyen con patrones del catálogo cerrado** de `documentos_operativos/ARQUITECTURA_ACADEMICA_HEIIU.md` (P1-P14), combinados según la tabla por cohorte y el selector por tipo de contenido (§2 de ese doc). PROHIBIDO inventar tipos de actividad o mutar la estructura de un patrón — se varía contenido (módulo, vocabulario, escenario), no estructura. La guía NUNCA menciona nombres de patrón (ni "P3") — solo instrucciones concretas. Si el módulo no encaja en ningún patrón: `SUPUESTO DE PLANEACIÓN — verificar`, no improvisar.

**Anexo opcional (máx 3-4 págs, tras `[PAGEBREAK]`):** SOLO cuando el módulo es nuevo/difícil y el verbatim del libro no cabe en la hoja: reglas y ejemplos completos citados del libro, Plan B extendido, NOTA INTERNA. Si la hoja se basta sola, NO generes anexo.

**Tope duro: 5 páginas totales por PDF.** Si sale más largo, recorta el anexo — jamás la hoja.

## 3. Procedimiento por (día, cohorte)

1. **Identifica la clase siguiente**: lista las guías existentes del cohorte, el último número + 1 es la clase a generar.
2. **Lee la guía previa SOLO para continuidad** (no para formato): módulo cubierto y dónde quedó, tarea asignada (el Bloque 1 nuevo la revisa), errores/temas anunciados, B2: sets de vocab y trabalenguas ya usados + cuenta regresiva, B1: contenido del PASE. El formato de salida es SIEMPRE la hoja de ruta de §2.
3. **Verifica el módulo siguiente** leyendo el libro del nivel:
   - A1: `recursos/docs_estrategia/A1 Book.md` — busca el siguiente `**Module N**` por encima del último cubierto.
   - A2 (4h y PM): `recursos/docs_estrategia/A2 Book.md` — íd.
   - B1: el módulo que la guía Grammar previa anuncia en su NOTA INTERNA; verifica el contenido en el A2 Book (B1 reúsa hardest A1+A2).
   - B2 Amina: lee `B2/B2_PM_Amina_ROADMAP_72h_PRINT.md` (autoritativo; el 90h está OBSOLETO) para el paso/fase del día.
   - **A2 4h después de Cl 20:** libro AGOTADO en M44. Sigue el **arco de repaso de errores** Cl 21-28 (mapa en memoria `project-a2-4h-arco-repaso-b1`).
4. **Regla del libro:** si un número de módulo NO existe (hueco), SALTA al siguiente que exista. NUNCA inventes, infieres ni rellenas contenido faltante. Cita literal del libro: título, página, reglas, vocabulario, ejemplos (lo esencial en la hoja; el resto al anexo si hace falta).
5. **Virtud por número de clase** — lee `recursos/calendarios/CALENDARIO_VIRTUDES_2026.md`, tabla del formato del cohorte:
   - A1 NOCTURNO 2H, A2 NOCTURNO 2H, A2 INTENSIVO 4H, B1 daytime (4h) — por número de clase.
   - **B2 Amina:** rotación estándar bloques de 5 (1-5 Prudencia · 6-10 Templanza · 11-15 Justicia · 16-20 Fortaleza · 21-25 Prudencia · 26-30 Templanza · 31-35 Justicia · Cl 36 SÍNTESIS/Final). Confirmado Diana 22/05 — aplicar directamente, **NO marcar como supuesto**.
6. **Frase del Día**: 1 frase que integra módulo + virtud + vocabulario foco. Cero copia/depuración. (GoldList ELIMINADO 14/05.)
7. **Recuperación espaciada**: identifica los módulos/estructuras de Cl N-3 y Cl N-7 (de las guías existentes) y escribe la instrucción exacta de recuperación en Bloque 1.
8. **Continuidad**: el Bloque 1 revisa la tarea previa; los errores de la clase previa alimentan la práctica; al cierre se anuncia la próxima.
9. **¿La clase es un marcador?** Si el número cae en un examen del mapa (ver §5), genera un **marcador corto** (1 pág, sin inventar resultados), no una guía de módulo.
10. **Escribe `<archivo>_PRINT.md`** en formato hoja de ruta (§2).
11. **Escribe el generador Python** en `generadores/gen_<dia>_<cohorte>_cl{N}.py` espejo del del día anterior (que también está en `generadores/`). Como vive en `generadores/`, debe (a) empezar con el shim `import os as _hos, sys as _hsys; _hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))` para que resuelvan los imports de motor, y (b) si calcula rutas con `__file__`, usar **doble** `os.path.dirname(...)` (o `Path(__file__).resolve().parent.parent`) para que la base sea la raíz del repo. Copiar el del día anterior ya trae ambos. Usa `from gen_a1_a2_clases_pdfs import md_to_pdf` para la guía. **REPORTE formato v3 (vigente desde 10/07/2026, reemplaza `build_report_v2`)**: NO escribas código de reporte en el generador de la clase — el reporte lo produce el script genérico `generadores/gen_reporte_v3.py`, que parsea el PRINT.md (virtud, módulo, títulos reales de los 4 bloques `## BLOQUE N ...`) y arma el cuerpo fijo de la plantilla (Completo/Parcial/No se hizo por bloque · "¿Qué salté o cambié?" · 3 errores textuales sin nombres · asistencia + portafolio · checklist entregables · firma; fecha y profesor en blanco). Al final del batch corre UNA vez: `python generadores/gen_reporte_v3.py` (o con los cohortes tocados como args, p. ej. `A2_2H B1_4H`). Requisito: el PRINT debe tener sus 4 encabezados `## BLOQUE N` y la línea `**Virtud:**` — si no, el script lo salta y lo reporta.
12. **Corre el generador desde la raíz** (`python generadores/gen_...py`, NO con `cd generadores/`) y verifica con `ls`/`stat` que ambos PDFs existen en su carpeta de nivel. Guía: >2KB y **≤5 páginas** (una hoja de ruta típica pesa mucho menos que las guías largas viejas — sospecha si supera ~15KB: probablemente salió formato largo). Reporte v3: **1 página**, ~2.5-3KB.

## 4. No-negociables Heiiu (aplicar a TODAS las guías)

- **Frase del Día** (GoldList eliminado 14/05/2026 — no presentarlo como ritual activo). 1 frase en tablero (módulo + virtud + vocab), cero copia, cero depuración, ~3-5 min, profe la usa 3+ veces naturalmente; al cierre 1 estudiante la dice + 1 la usa en oración nueva. Script si preguntan: *"The method evolved. We use Phrase of the Day now — simpler, more direct. Your old notebooks stay yours."*
- **Recuperación espaciada N-3/N-7 + chequeo portafolio en Bloque 1 · Ticket de salida en Bloque 4** — estructura fija de §2, sin excepciones (salvo marcadores de examen).
- **Numeración consecutiva** por sesión. Presentaciones / midterm / final term consumen su número con marcador PDF (`feedback-numeracion-clases-consecutiva`).
- **Sin nombres de estudiantes** en guías (reutilizables entre cohortes). Casos individuales → notas operativas aparte con fecha. Los errores de tickets se citan SIEMPRE anónimos ("error común").
- **Sin nombres de metodologías** (TBLT/Dogme/TPRS/PBL/etc.) — protección de IP.
- **Profesor NUNCA comunica evaluaciones / midterm / final / notas / resultados** — coordinación SOLO. El ticket de salida NO es examen y el profe no lo evalúa ni comenta: solo lo recoge y lo entrega.
- **No fabricar resultados** ni inventar lo que no se puede verificar (`feedback-no-fabricated-reports`). Incluye: no citar "tickets de la semana" si no hay mapa semanal procesado.
- **Simulación profesional realista** (oficina, cliente, tienda, aeropuerto, entrevista, equipo). NUNCA fantasía. NUNCA familia/trauma personal.
- **Tarea**: due date explícita (próxima clase antes de **7:00 PM** general; **B2 Amina = 6:00 PM** — norma del cohorte). Tiempo por nivel: A1 15-20min · A2 20-30 · B1 30-45 · B2 45-60 (4 componentes estrictos). NO fragmentada. Push-back NO se acepta. El **audio/video diario del portafolio** es componente permanente de la tarea en todos los niveles (1-3 min, celular, repetir/escuchar/grabarse).
- **Error Paper** doble protocolo: anónimo en clase + libreta privada con NOMBRES para el reporte de coordinación.
- **Cero material físico preparado por profe/academia** — objetos = tarea previa al estudiante + Plan B en la hoja.
- **B1 Grammar (Juan Diego)** ~70%+ del bloque DE PIE (ansiedad con guías estáticas). Las últimas guías corrieron en ~86% de pie — mantén ese piso.
- **B2 Amina específico**:
  - **Fase 2 (Cl 6-12):** ~94% oral, cero escritura en clase.
  - **Fase 3 (Cl 13-20):** escritura en clase **a mano**, anti-fraude documentado (texto traído de casa no cuenta, se reescribe a mano; AI/home-text sospechoso → alerta coordinación).
  - **B2 Vocab Bank** crece: cada clase un **Set #N de 6 palabras académicas nuevas**, distintas de los sets previos (leer la guía previa para listar las ya usadas). Total acumulado se reporta.
  - **3-4 trabalenguas nuevos** cada clase, distintos de los previos.
  - **Lectura nominal pública de no-entregas** al abrir; **2 strikes → notificar coordinación** al cierre.
  - **Bridge formal↔casual** (registros académico ↔ natural).
  - **Cuenta regresiva al Final** (Cl 36): derivar de la guía previa por días transcurridos. NO fabricar.
  - Todo lo anterior debe caber compacto dentro de los 4 bloques de la hoja (el vocab set y los trabalenguas son líneas, no secciones).
- **A2 4h después de Cl 20:** libro agotado. Sigue **arco de repaso** Cl 21-28 (clusters de error A2→B1): tiempos verbales / comparativos+gerundio-infinitivo / phrasal+pasiva / preguntas-negativos-orden / preposiciones-artículos / concordancia-there is-causativo / mastery integrado + check B1. Mapa actualizable en NOTA INTERNA (anexo).
- **Reportes estáticos** (no editables), se llenan a mano. Usar `build_report_v2`.

## 5. Mapa de exámenes vigente (consultar antes de generar — un marcador NO es módulo)

- **B1 Mastery:** Cl 22 = MIDTERM PRESENTATION (5 min c/u) · Cl 44 = FINAL (últimas 2h = bloque Grammar). Definido en la guía B1 Cl 1.
- **A2 PM noche:** Cl 25 PRESENTACIONES ✅ · Cl 26 MIDTERM ✅ (marcadores existentes) · Cl 55 FINAL.
- **B2 Amina:** Checkpoints C1 fin Cl 5 / C2 fin Cl 12 / C3 fin Cl 20 / C4 fin Cl 28 · Cl 36 FINAL (roadmap 72h).
- **A1 noche:** Cl 45 FINAL (regla últimas 2h). Midterm histórico ~Cl 22-23 SIN marcador (pendiente limpieza retroactiva — pedir confirmación a Diana antes de marcar).
- **A2 4h AM:** ½ Cl 28 (últimas 2h del nivel) = FINAL. Midterm/presentaciones SIN definir para este cohorte.

Si la clase a generar coincide con un marcador → genera **marcador** (formato como `A2_Class25_PRESENTACIONES_PRINT.md` / `A2_Class26_MIDTERM_PRINT.md`): 1 pág, número consecutivo, contenido especial, sin inventar resultados. El Final del nivel lo aplica evaluador externo — NO generar guía pedagógica ese día.

## 6. Reglas de horas (todo cabe)

A1 = 90h · A2 = 110h · B1 = 175h · B2 = 200h (cohorte Amina = 72h restantes). El examen Final ocupa las **últimas 2 horas** del nivel. Todo el contenido del nivel debe terminar ANTES de esas últimas 2h. Ver `feedback-final-examen-ultimas-2h`.

## 7. Paralelización

Para un día completo: lanza **un agente `general-purpose` por cohorte** en un mismo mensaje, en paralelo. **B1 es UN agente** que produce las 2 guías (Conv + Grammar) porque comparten día + PASE escrito entre bloques (Danna → Juan Diego mismo día; Juan Diego → Danna para el día siguiente).

Para un rango Lu-Vi: procesa **día por día secuencialmente** (cada día necesita las guías del previo para continuidad); dentro de cada día, todos los cohortes en paralelo.

Cada prompt de agente debe incluir: **la plantilla hoja de ruta de §2 con sus reglas fijas** (el agente NO debe copiar el formato largo de la guía previa), ruta de la guía previa solo para continuidad, ruta del libro (si aplica), regla de virtud + número de clase a calcular, los módulos de Cl N-3/N-7 para la recuperación espaciada, los no-negociables relevantes al cohorte, y un recordatorio explícito de NO inventar contenido ni señales de tickets inexistentes. Marcar cualquier supuesto SOLO en NOTA INTERNA (anexo) como `(SUPUESTO DE PLANEACIÓN — verificar)`.

## 8. Verificación + reporte final

Después de cada día (o al cierre del rango):
1. Verifica en disco que existan los PDFs esperados (guía + reporte por cohorte; B1 doble: Conv + Grammar). Guías **≤5 páginas** y >2KB (si una guía pesa como las viejas de 12 págs, se rehace); reportes v3 = 1 página ~2.5-3KB con cabecera de la clase (cohorte + Cl N + módulo + bloques reales).
1-bis. **Corre el CONTRATO DE VALIDACIÓN V1-V20** de `ARQUITECTURA_ACADEMICA_HEIIU.md` §3 sobre cada PRINT.md (lo puede correr mark leyendo el archivo). 1 falla = la hoja se corrige y regenera antes de reportar.
2. Reporta una tabla compacta:

| Cohorte | Clase | Módulo / contenido | Virtud | Frase del Día (resumida) | Recuperación (N-3/N-7) | Págs guía (≤5) | Supuestos |

3. Resume cualquier supuesto que algún agente flaqueara en NOTA INTERNA — Diana decide si auditar.
4. Lista próximas clases por cohorte (encadena al siguiente día/semana).

## 9. Fuentes canónicas

- **ARQUITECTURA ACADÉMICA (LEY para bloques 2-3):** `documentos_operativos/ARQUITECTURA_ACADEMICA_HEIIU.md` — catálogo P1-P14, gramática por cohorte (§2), matriz genérica nivel×formato para cohortes nuevos (§2-BIS), virtualidad grupal (§2-TER), selector, contrato V1-V20, plantillas. Opus ejecuta este diseño, no lo modifica. Si Diana pide un cohorte que no está en §1 de esta skill (nuevo nivel/formato/virtual), instancia desde §2-BIS/§2-TER y agrega la fila.
- **Master Blueprint:** `documentos_operativos/MASTER_BLUEPRINT_HEIIU.md` (norte operativo).
- **Workflow y formato hoja de ruta:** `documentos_operativos/WORKFLOW_CLAUDE_HEIIU.md` (§5 formato, §9 auditoría del aprendizaje).
- **Libros:** `recursos/docs_estrategia/A1 Book.md`, `recursos/docs_estrategia/A2 Book.md`.
- **Calendario virtudes:** `recursos/calendarios/CALENDARIO_VIRTUDES_2026.md`.
- **Roadmap B2 Amina (autoritativo):** `B2/B2_PM_Amina_ROADMAP_72h_PRINT.md`. El `ROADMAP_90h` está obsoleto.
- **Memorias clave** (consultar si surge duda):
  - Formato y aprendizaje: `feedback-guias-hoja-de-ruta`, `feedback-auditoria-aprendizaje`, `feedback-modelo-inmersivo-guias`, `feedback-profe-sin-material-preparado`.
  - Reglas universales: `feedback-numeracion-clases-consecutiva`, `feedback-modulos-libro-skip-no-inventar`, `feedback-final-examen-ultimas-2h`, `feedback-mapa-examenes-cohorte`, `feedback-goldlist-retired`, `feedback-no-fabricated-reports`, `feedback-no-eval-communication`, `feedback-guias-reutilizables`, `feedback-no-methodology-names`, `feedback-tarea-due-date-explicita`, `feedback-error-paper-doble-protocolo`, `feedback-simulaciones-realistas`, `feedback-blueprint-preflight-checklist`, `feedback-examen-final-otro-evaluador`.
  - Cohortes/arcos: `project-a2-4h-arco-repaso-b1`, `project-why-colombia-final-b2`, `project-b2-virtud-rotacion-estandar`, `project-a2-modulo19-inexistente`, `project-a1-module-map`.
  - Convenciones de profesor: `feedback-b1-grammar-movement`, `feedback-b2-amina-fase2-conversacional`, `feedback-b2-writing-in-class-only`, `feedback-b2-immersive-activities`, `feedback-historias-interactivas-estilo-clase1`, `feedback-simulacion-guest-observer-pattern`, `feedback-textos-heiiu-dos-versiones`, `feedback-fotos-videos-reframe`, `feedback-homework-grabo`.

## 10. Qué NO hacer

- NO copiar el formato largo de las guías previas al 06/07 — son solo fuente de continuidad.
- NO inventar tipos de actividad ni mutar patrones del catálogo (ARQUITECTURA §1) — combinar sí, crear no.
- NO generar anexo cuando la hoja se basta sola; NO pasar de 5 páginas totales.
- NO inventar módulos cuando el libro no los tiene (saltar al siguiente que existe).
- NO citar tickets/errores de la semana si no hay mapa semanal procesado — la recuperación usa entonces los módulos de N-3/N-7.
- NO comunicar resultados/notas al estudiante (regla del profesor; el ticket de salida no se evalúa en aula).
- NO usar nombres de estudiantes en la guía (van en notas aparte con fecha).
- NO usar nombres de metodologías.
- NO presentar GoldList como ritual activo.
- NO fabricar fechas, resultados, checkpoints o midterm que no estén en docs.
- NO requerir material físico comprado/preparado por el profe o la academia.
- NO saltar el pre-flight (apertura / estructura / carácter / memoria pasiva / producción / cierre / limpieza / tono).
- NO preguntar lo que se puede verificar leyendo un archivo. Sí preguntar cuando un dato real (qué pasó en clase, qué decidió Diana) cambia el output y no está en docs.

## 11. Cambios al patrón

Si Diana ajusta una regla durante una invocación (ej. cambia un cluster del arco A2 4h, mueve un marcador), aplica el cambio al día en curso y registra la decisión actualizando la memoria pertinente (`feedback-*` o `project-*`) + nota en `MEMORY.md`. El Blueprint y el WORKFLOW se actualizan cuando la regla es definitiva.
