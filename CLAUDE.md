# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

Sistema de generación de material pedagógico de **Heiiu** (escuela de inglés). NO es software tradicional: scripts de Python renderizan **guías de clase (GUIA.pdf)** y **reportes (REPORTE.pdf)** a partir de archivos markdown (**PRINT.md**). El markdown es la fuente de verdad; los PDF se generan, nunca se editan a mano.

## Documento norte — leer SIEMPRE antes de generar una guía

`documentos_operativos/MASTER_BLUEPRINT_HEIIU.md` consolida estrategia, niveles, sistema de virtudes y los no-negociables. Consúltalo antes de crear cualquier guía nueva. Es el archivo que no se puede perder.

**Ojo — hay DOS "Blueprints":** el MASTER (pedagógico, arriba) y `recursos/docs_estrategia/Heiiu_Blueprint_DEFINITIVO_2026.md` (estratégico/comercial: precios 15.3-BIS, becas 15.2, funnel 13.8, roles 15.6). Para TODO lo comercial la fuente es el DEFINITIVO + `documentos_operativos/ESTRATEGIA_VENTAS_2026.md`.

## Arquitectura académica — LEY para generar guías

`documentos_operativos/ARQUITECTURA_ACADEMICA_HEIIU.md` define el **catálogo cerrado de patrones P1-P14** (las metodologías codificadas, sin nombre), la gramática de bloques por cohorte, el selector de patrón por tipo de contenido y el **contrato de validación V1-V20**. Los Bloques 2-3 de toda hoja de ruta SOLO usan patrones del catálogo; se varía contenido, nunca estructura; patrones nuevos solo los diseña Diana. Documento interno — jamás se entrega a profesores.

## Workflow de trabajo con Claude

`documentos_operativos/WORKFLOW_CLAUDE_HEIIU.md` (entrevista 05/07/2026) define el sistema de trabajo: rutina de batch semanal + toques diarios, formato **hoja de ruta 1 página** para guías nuevas (tope 5 págs con anexo), dashboard semanal de supervivencia, reglas de protección IP para material entregado a profes, ciclo de reporte de profes, **auditoría del aprendizaje** (ticket de salida diario + portafolio de audios/videos + recuperación espaciada N-3/N-7 + ficha viva por estudiante + triangulación profe↔estudiante↔error paper), y prioridades comerciales. Las sesiones deben servir a dos metas: subir números (caja/matrículas) y que la experiencia élite llegue al aula.

## Regla de oro del contenido

El contenido pedagógico sale del **libro oficial** (carpeta `Libros/`) tal cual: se sigue la secuencia, se **salta** el módulo que no exista, y **NUNCA se inventa** ni se infiere. Se cita verbatim (título, página, reglas, vocabulario, ejemplos). Marca lo que asumas como `SUPUESTO DE PLANEACIÓN — verificar`.

## Flujo de generación de PDFs

Dependencia: **reportlab** (no hay `requirements.txt`; asúmelo instalado). Entorno **Windows**.

**Estructura:** los 2 motores (`gen_a1_a2_clases_pdfs.py` y `generate_pdfs.py`) viven en la **raíz**; todos los generadores por clase están en **`generadores/`**. Siempre se corren **desde la raíz**: `python generadores/gen_xxx.py` (cada generador mete la raíz en `sys.path` y escribe sus PDFs en las carpetas de nivel `A1/ A2/ B1/ B2/`). NO ejecutar con `cd generadores/`.

- `md_to_pdf(md_path, pdf_path, max_lines_per_section=None, compact=False)` — de `gen_a1_a2_clases_pdfs.py`. Renderiza un PRINT.md a GUIA.pdf B&N. Soporta `#`/`##`/`###`, bloques de código ` ``` ` (para mapas y frases), listas `-`, `**negrita**`, tablas, blockquote `>`, y el marcador `[PAGEBREAK]`. Bloques de código muy largos (>~60 líneas) se parten solos.
- `get_styles()` + `build_report_v2(filename, title, subtitle, activities_checklist, deliverables, selfeval, styles)` — de `generate_pdfs.py`. Genera el REPORTE.pdf de 1 página (checklist editable).
- **Generador por clase** = un `gen_*.py` en `generadores/` que importa ambas y las llama. Copia uno reciente (p. ej. `generadores/gen_b1_cl20.py`) como plantilla y guárdalo también en `generadores/`. **B1 Mastery = 2 tracks** (CONV + GRAMMAR) → 4 PDFs por clase.
- Tras generar, **verifica en disco**: guías ~20–25 KB, reportes ~6 KB.

## Convenciones de nombres

- Fuente: `{NIVEL}_Clase{N}_{TRACK}_PRINT.md` (o `Class{N}` en A1/A2). Salida: `_GUIA.pdf` y `_REPORTE.pdf`.
- Generadores: `gen_{nivel}_cl{N}.py`, todos dentro de `generadores/`.
- B1 va dividido en `B1_conversacional_*` y `B1_gramatica_*`, con versiones `_V1` / `_V2` (V2 = vigente).

## Numeración y virtudes

Número de clase **absoluto** por nivel (A1 1–45, A2 1–55, B1 1–44). La **virtud** se asigna por número de clase en bloques de 5, en **calendario absoluto** — no se desplaza por festivos ni clases canceladas.

## No-negociables Heiiu (detalle en el Blueprint)

Frase del Día en el tablero (NO existe GoldList) · numeración consecutiva · **sin nombres de estudiantes** en guías reutilizables · **sin nombres de metodologías** · los profes **no comunican** evaluaciones (eso es coordinación) · modelo inmersivo de 4 bloques largos · sin material impreso preparado (todo en tablero o tarea, con Plan B) · tarea estricta (due date explícita, no fragmentada) · error paper físico anónimo + reporte con nombres para coordinación · simulaciones profesionales realistas · **B1**: PASE bidireccional Conv↔Grammar, Grammar ~70–86% de pie · **B2 (Amina)**: banco de vocabulario + trabalenguas + fase · Final del nivel lo aplica evaluador externo (no generar guía ese día).

## Agentes especializados (globales, uno por modelo)

Para delegar y ahorrar tokens: **sidis** (Fable, estrategia pura — cara, usar poco), **einstein** (Opus, redactar guías + investigación profunda), **tesla** (Sonnet, leer/extraer del libro), **mark** (Haiku, correr scripts / generar PDFs / verificar). También existe la skill `/clases` para generar el material diario de los 5 cohortes.

## Nota

El `.gitignore` ignora `.claude/` (skills, hooks y settings quedan **solo locales**, no se suben) y `B2/reportes/` (fotos/PDF personales de estudiantes).

**Respaldo de skills:** `documentos_operativos/skills_backup/` versiona copias de los `SKILL.md` de `.claude/skills/`. Cada vez que se modifique una skill, copiar el `SKILL.md` actualizado a esa carpeta en la misma sesión (y actualizar la fecha en su README).
