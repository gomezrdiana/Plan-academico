---
name: repaso-ausente
description: Genera una guía de repaso autónoma para un estudiante que se ausentó, cubriendo los temas de las clases que perdió. Bilingüe (instrucciones en español, contenido en inglés), fácil para ~13 años, para hacer solo/a en casa, con respuestas para autocorrección. Úsala cuando Diana pida ponerse al día a un estudiante ausente.
---

Genera una **guía de repaso autónoma** para un estudiante ausente. Argumentos esperados en `$ARGUMENTS`: nivel + clases perdidas (rango o fechas) + nombre del estudiante. Ej: `B1 Cl 27-33 para María Angélica`.

## Paso 1 — Identificar qué se perdió
Si te dan fechas, mapéalas a números de clase (el grupo avanza una clase por sesión; usa el calendario/última guía para anclar). Confirma el rango de clases con Diana si hay ambigüedad.

## Paso 2 — Extraer el contenido REAL (nunca inventar)
Para cada clase perdida, saca el tema del **libro oficial** (`Libros/`) y de las guías del grupo (`*_PRINT.md` de ese cohorte). Extrae, verbatim: la **regla**, 5–8 **ejemplos**, los **errores típicos** (mal→bien) y los **bancos de palabras**. Cita módulo y página. Si un dato no está en la fuente, dilo — no lo rellenes. (Puedes delegar la extracción a **tesla**.)

## Paso 3 — Escribir UNA guía autocontenida (PRINT.md)
Bilingüe: instrucciones en **español**, contenido en **inglés**, lenguaje simple para ~13 años, para hacer **sola/o**. Estructura:
- Portada: `Para: <NOMBRE>` + nivel + rango de clases + cómo usarla (un tema por día, revisar respuestas al final, sin hacer trampa).
- **Un mini-tema por clase perdida**, cada uno con: `[1] LA IDEA` (explicación fácil en español) → `[2] LA REGLA` (fórmula + ejemplos, en bloque de código) → `[3] CUIDADO` (errores mal→bien) → `[4] PRACTICA` (5 ejercicios para escribir).
- **SPEAKING LAB**: 2–3 misiones de grabarse (1 min c/u) usando la gramática.
- **LISTENING LAB**: 2–3 misiones de YouTube con qué anotar.
- **CHECKLIST** de progreso.
- **RESPUESTAS** al final (clave de todos los ejercicios) para autocorrección — imprescindible para trabajo autónomo.

Sin emojis (el PDF en Helvetica no los renderiza); usa `X` para lo incorrecto y `->`/`OK:` para lo correcto, como en las guías del repo.

## Paso 4 — Nombre de archivo y ubicación
Guarda en `<NIVEL>/<NIVEL>_repaso_autonomo/<NIVEL>_Repaso_Autonomo_ClNN-MM_PRINT.md`. El **nombre del archivo va genérico** (sin nombre de estudiante, para reutilizar entre cohortes); el nombre solo aparece en la portada.

## Paso 5 — Generar el PDF y verificar
Renderiza con `md_to_pdf(md_path, pdf_path)` de `gen_a1_a2_clases_pdfs.py` (`python -c "from gen_a1_a2_clases_pdfs import md_to_pdf; md_to_pdf(...)"`). Verifica el PDF en disco y reporta páginas/tamaño. El `.md` fuente queda al lado por si Diana quiere editar.
