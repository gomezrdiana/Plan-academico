# VERSION_2 — Contenido Vigente (Formato Hoja de Ruta)

Esta carpeta contiene solo el material de **cohortes activos** en formato de hoja de ruta ejecutable (1 página + anexos opcionales).

## Estructura por cohorte

Cada cohorte sigue la regla:
- **PRINT.md** (fuente markdown) → raíz de la carpeta del cohorte
- **GUIAS/** → archivos `_GUIA.pdf` (generados desde PRINT.md)
- **REPORTES/** → archivos `_REPORTE.pdf` (checklist editable por clase)

### Cohortes activos (2026-07-10)

| Cohorte | Clases | Descripción | Estado |
|---------|--------|-------------|--------|
| **A1_4H** | 1–5 | A1 entre semana + taller sabatino, todos a su ritmo | Activo |
| **A2_2H** | 14–18 | A2 nocturno PM (2h/clase) | Activo (Cl 14-18) |
| **B1_4H** | 21–25 | B1 Mastery, tracks CONV+GRAMMAR, entre semana | Activo (Cl 21-25) |
| **B2_4H** | — | B2 entre semana (no activo en esta versión) | Pendiente |

### Carpetas vacías (reservadas)

- **A1_2H**, **A2_4H**, **B1_2H**, **B2_2H** → cohortes sin abrir aún en esta estructura. Se poblarán al activarse.

## Notas operativas

- Los generadores Python (`generadores/gen_*.py`) escriben directamente en estas rutas.
- **NUNCA** imprimir o editar PDFs de aquí de forma manual — todo regenera desde el PRINT.md.
- Los reportes (`_REPORTE.pdf`) son editables en clase para checklist; no versionar cambios manuales.
- No existe GoldList (retirado 14/05/2026). La "Frase del Día" va en tablero, anotada durante la sesión.
- La virtud VATS sigue calendario absoluto (no se desplaza por festivos).

## Cambios respecto a VERSION_1

- **Formato:** línea 1 página (ejecutable) + anexos opcionales = máx 5 págs.
- **Organización:** por cohorte (no por nivel global).
- **Reportes:** centralizados en subcarpeta REPORTES/ (antes esparcidos).
- **PRINT.md:** en raíz del cohorte (no en subcarpeta nivel/).
