---
name: semanal
description: Ejecuta la SESIÓN BATCH SEMANAL completa de Heiiu (diseñada con Fable, ejecutable 100% con Opus). Parte académica (guías de la semana con /clases, procesar reportes de profes + tickets desde la carpeta de intercambio, mapa semanal de señales, fichas de estudiantes, divergencias→auditoría) + parte comercial obligatoria (dashboard con datos de Brian/María Eugenia/auxiliar — SIN DATO si no llegó —, tanda nueva de contenido F1 desde errores reales, lote Capa 1, ganchos/captions TikTok+IG por pieza, análisis de métricas orgánicas, rescate de leads, 1 avance B2B) + cierre (commit/push, respaldo skills, memoria). Úsala cuando Diana diga "sesión semanal", "arqueo semanal", "hagamos la semana" o similar.
---

# semanal — sesión batch semanal Heiiu (playbook para Opus)

Invocación: `/semanal` (opcional: `solo académico` / `solo comercial` / `solo contenido`).
**Metas gemelas de toda sesión** (WORKFLOW_CLAUDE_HEIIU.md): que la experiencia élite llegue al aula Y que suban los números. Meta de caja vigente: **$20-22M/mes cobrados** (ANALISIS_PRELIMINAR finanzas).
Modelos: tú (Opus/einstein) rediges todo; **tesla** extrae de PDFs/fotos; **mark** corre generadores, verifica PDFs y git. **Nada requiere Fable** — si detectas una decisión de DISEÑO nueva (patrón nuevo, producto nuevo, trade-off mayor), NO la tomes: anótala para sesión de diseño con Diana.

## PARTE A — ACADÉMICA

**A1. Ingerir señales de la semana anterior.**
- Fuente: carpeta de intercambio (Diana/auxiliar suben fotos de: reportes firmados de profes, tickets de salida, error papers con nombres). Si no hay nada: TODO el mapa = "SIN DATO" y se le recuerda a Diana el circuito (profes entregan físico → admin sube — los profes JAMÁS acceden a carpetas).
- tesla extrae → **MAPA SEMANAL DE SEÑALES** (plantilla en ARQUITECTURA_ACADEMICA §4.3): por cohorte, top 3-5 errores comunes (anónimos), % dominio de la estructura, cumplimiento de portafolio, divergencias reporte-profe↔tickets, alerta de error sistemático (posible error enseñado — profes no nativos). Guardar en `documentos_operativos/mapas_semanales/MAPA_SEMANAL_{fecha}.md`.
- Divergencia confirmada → registrar para Sistema_Auditoria (auditoría POR EXCEPCIÓN). Nunca abrir auditoría sin divergencia documentada.

**A2. Actualizar fichas de estudiantes** (plantilla ARQUITECTURA §4.2, carpeta de fichas interna): solo con señales reales; sin señal = "SIN DATO"; nombres JAMÁS pasan a guías.

**A3. Generar la semana de guías** → invocar la skill `/clases` para el rango Lu-Vi siguiente (ella contiene todo: hoja de ruta, P1-P14, V1-V20, cohortes activos). La recuperación espaciada de la semana nueva SE CONSTRUYE con los errores del mapa de A1 (y solo si el mapa existe — anti-fabricación V18).
- Sabatino (cuando Diana entregue el roster): actualizar REGISTRO SABATINO por nivel + generar hoja de taller (ARQUITECTURA §2-QUATER) — solo cambian Frase del Día, virtud, escenario B3 y registro adjunto.

## PARTE B — COMERCIAL (obligatoria, mínimo 1/3 de la sesión — nunca "si sobra tiempo")

**B1. Dashboard** (`documentos_operativos/DASHBOARD_SEMANAL.md`): actualizar con lo que haya llegado de: Brian (gasto, leads, costo/lead, citas agendadas, desglose por campaña), María Eugenia (citas asistidas, cierres, motivo de no-cierre), auxiliar (caja, % cuotas de estudiantes al día, cartera). Los datos llegan por los bloques WhatsApp de `documentos_operativos/FORMATOS_REPORTE_SEMANAL.md` (Diana los reenvía cada viernes); las respuestas las pega Diana en sesión o quedan en `recursos/comercial/datos/`. Si un bloque no volvió: SIN DATO + recordarle a Diana reenviarlo. **Regla de hierro: celda sin dato = "SIN DATO" — jamás estimar ni arrastrar el valor anterior como si fuera nuevo.** Diagnóstico del embudo según ESTRATEGIA_VENTAS §8 (dónde se rompe: lead→cita = bot; cita→cierre = guion/oferta; costo/lead subiendo = fatiga creativa).

**B2. Tanda de contenido semanal** (entregar como UN archivo `recursos/comercial/campanas/TANDA_{fecha}.md` + PDF con md_to_pdf):
1. **Tanda F1 nueva** (guiones de errores para Breagh): SOLO errores reales del mapa semanal (o de reportes/documentos del repo, citando fuente). Formato de GUIONES_BREAGH_F1_TANDA1.md: GANCHO → ERROR → POR QUÉ (trampa del español) → CORRECCIÓN → REMATE+CTA rotado.
2. **Lote Capa 1** (posts sin cara): tarjetas de error ("❌ X → ✅ Y") + Frases del Día REALES de las guías de la semana + 2-3 encuestas para historias.
3. **2 ganchos + 2 captions por pieza publicable: uno TikTok (crudo, directo), uno IG/Reels** (regla TikTok-first).
4. **Análisis de métricas orgánicas**: con los pantallazos/exports que Breagh haya enviado — qué retuvo, guardados/compartidos, mensajes a WhatsApp originados; recomendar qué repetir/matar. Sin datos = "SIN DATO" + recordatorio.
- **LÍNEA ROJA en todo contenido** (BRIEF_BREAGH v4): se publican FRUTOS del sistema, jamás el sistema (nada de virtudes/patrones/rituales/secuencias/páginas de guías). Prueba del ácido: "¿enseña CÓMO operamos o muestra QUE funcionamos?".

**B2-TER. Semáforo de contenido (desde 22/07/2026 — evita el apagón de julio):** cada sesión se registra en el dashboard: **"contenido programado hasta: ___ (semanas restantes: N)"** — el dato lo da Breagh (pantallazo de TikTok Studio/Meta Suite) o es "SIN DATO" + recordatorio. Reglas: (1) **N < 4 semanas = alerta**: esa misma sesión se genera la tanda siguiente y se agenda con Breagh la sesión de programación (remota, 2-3h); (2) **regla del día 25**: antes del 25 de cada mes, el paquete del mes siguiente (lote Capa 1 + calendario de publicación + guiones nuevos si hay visita) debe estar ENTREGADO a Breagh; (3) **entregado = confirmado recibido por WhatsApp** — commiteado en el repo NO cuenta como entregado (lección julio: los guiones existían desde el 07/07 y nadie publicó nada). El banco grabado en julio (~40 crudos a 3-4 reels/sem) cubre ago-oct; grabación nueva solo en visitas de Breagh — el semáforo vigila PROGRAMACIÓN, no grabación.

**B2-BIS. Cobranza (desde 12/07/2026 — palanca de caja #1 según datos reales):** si hay informe nuevo de Jacqueline (`recursos/finanzas/INFORME*.xlsx`), correr `python "recursos/finanzas/analizar_cartera.py"` (NO calcular a mano — el script saca totales, % cuotas al día, vencidos y por-vencer). Con la salida: (1) actualizar dashboard (% cuotas al día — base junio ~23%, meta 70%; leer % solo a fin de mes, a inicio de mes sale inflado); (2) lista de llamadas de la semana para la auxiliar según `documentos_operativos/PROTOCOLO_COBRANZA.md` (vencidos → D+2 con guion; próximos 7 días → D-3); (3) chequear gatillo #7 del `PREMORTEM_2026.md`; (4) pendientes con Jacqueline en `recursos/finanzas/PENDIENTES_JACQUELINE.md`; (5) **medidor anti-recarga**: preguntar/registrar en dashboard "deuda personal de Diana usada para la empresa este mes: $___" — meta $0 SIEMPRE; si no es $0 → gatillo #2 del PREMORTEM (bajar pauta, sin debate). Contexto completo: `recursos/finanzas/ANALISIS_CARTERA_2026-07-12.md` (hallazgo clave: cuotas pactadas $13.8M/mes vs recaudo real $2-3M — el hueco de caja es de COBRO, no de ventas).

**B3. Rescate y B2B**: lista de leads no cerrados → 1 tanda de mensajes de rescate para María Eugenia (plantillas cortas, sin promesas prohibidas). Redactar/avanzar 1 pieza B2B (propuesta personalizada sobre PITCH_B2B_HEIIU.md si Diana dio empresa/contacto).

**B4. Guardarraíles comerciales** (ESTRATEGIA §11 + decisiones vigentes): narrativa = **Fondo de Becas** (patrocinador PROHIBIDO) · sin promesas de plazos/empleo/visa/pronunciación nativa · sabatino desc. máx 20% (única excepción a tabla) · abono inicial mínimo 30-40% en paquetes (si Diana lo confirmó) · no subir pauta sin diagnóstico del embudo · B2B sin becas.

## PARTE C — CIERRE

1. Verificación en disco de todo lo generado (mark): PDFs válidos, V1-V20 en guías.
2. `git add` de lo trabajado + commit descriptivo + **push** (el repo es el negocio).
3. Si se modificó alguna skill: copiar a `documentos_operativos/skills_backup/` + actualizar su README.
4. Si Diana tomó decisiones nuevas: memoria (`feedback-*`/`project-*`) + línea en MEMORY.md.
5. Reporte final a Diana: tabla de guías generadas · dashboard resumido (4-5 números) · qué quedó SIN DATO y a quién pedírselo · tanda de contenido entregada · pendientes de decisión.

## Qué NO hacer
- NO inventar datos, métricas, errores de estudiantes ni resultados — nunca.
- NO tomar decisiones de diseño (patrones, productos, precios, narrativas nuevas) — se anotan para Diana.
- NO mencionar patrocinador en ningún material nuevo.
- NO saltarse la parte comercial por falta de tiempo — es la mitad obligatoria.
- NO publicar/crear contenido que cruce la línea roja del sistema.
