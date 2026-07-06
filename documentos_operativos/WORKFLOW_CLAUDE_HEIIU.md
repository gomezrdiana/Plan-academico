# WORKFLOW CLAUDE × HEIIU — Insights y sistema de trabajo

> Resultado de la entrevista Diana × Claude del 05/07/2026. Referenciado desde CLAUDE.md.
> Propósito: que cada sesión de Claude Code sirva a las DOS metas que deciden la supervivencia:
> **(1) subir números (caja, matrículas)** y **(2) que la experiencia élite llegue de verdad al aula**.
> Toda tarea que no sirva a una de las dos, se pospone.

---

## 1. Contexto estratégico (por qué existe este documento)

- Heiiu está **a punto de quiebra**. No hay opción de fallar.
- La apuesta: academia **élite** — inglés + mentoría + habilidades para el futuro (virtudes, carácter) — para diferenciarse de ~20 academias de la ciudad, con presencialidad y virtualidad.
- Claude Code es la palanca de ambos frentes: producción pedagógica Y máquina comercial. Hasta hoy ha sido ~90% pedagógica; eso debe cambiar.

## 2. Qué hace Diana hoy con Claude (diagnóstico)

| Tarea | Estado | Problema detectado |
|---|---|---|
| Generar guías + reportes 5 cohortes (`/clases`) | Maduro (208 generadores) | Las guías crecieron de 4-5 a **12 hojas**; los profes **no las leen** ni terminan los bloques; Diana no alcanza a revisar nada; mucho papel |
| Procesar feedback profes (PDFs de FEEDBACK PROFES) | Manual, esporádico | Papel excesivo; sin formato fijo; no alimenta automáticamente guías ni auditoría |
| Auditoría profes (Sistema_Auditoria) | Manual | Depende de tiempo de Diana que no existe |
| Estrategia/comercial (Blueprint, precios 2026, bootcamps) | Material creado, **sin ejecutar** | La producción de guías se come el tiempo; el backlog del Blueprint no avanza |
| Casos de estudiantes (refuerzos, `/repaso-ausente`) | Funciona | — |
| Dashboard operativo | **Abandonado desde 04/05** | Diana no sabe qué número mirar; visibilidad financiera cero (los datos los tiene la auxiliar contable, no el sistema) |

## 3. Insights de la entrevista (los no-obvios primero)

1. **La guía larga era un seguro contra profes que transmiten errores — pero el seguro no paga.** Se hicieron guías de 12 hojas "super específicas" y los profes igual no las leen. Costo altísimo (tiempo Diana + tokens + papel), beneficio no verificable. → El detalle debe vivir donde sí se ejecuta: **1 hoja**.
2. **Las clases 1-a-1 virtuales son la palanca de caja más rápida y nadie las vende.** Ya existen, son rentables, no tienen riesgo de deserción grupal (1 alumno = 1 pago) y no requieren diseñar nada nuevo. Solo les falta marketing.
3. **Posible desalineación posicionamiento↔clientela:** el enfoque social atrae estudiantes de bajos recursos, mientras la estrategia declarada es élite/premium. No son excluyentes (becados como propósito, premium como negocio) pero hay que decidirlo explícitamente y dirigir el marketing al segmento que paga.
4. **La visibilidad financiera existe pero está desconectada:** contabilidad subcontratada + auxiliar contable con todos los registros. El dashboard no hay que inventarlo desde cero — hay que pedirle a la auxiliar **un corte semanal** y dárselo a Claude.
5. **El miedo a la copia es doble** (el sistema completo Y las guías sueltas) y ha frenado la digitalización del ciclo de reportes. Se resuelve con reglas, no con parálisis (ver §7).
6. **El virtual grupal premium está frenado por tres cosas a la vez:** no llegan interesados, miedo deserción-vs-nómina, y el producto no está diseñado. Las 1-a-1 son el laboratorio natural para destrabar las tres.
7. **Los profes reportan que a los estudiantes no les gustan las clases sobre-estructuradas** — dato de segunda mano (profes), pero consistente con la regla de 4 bloques largos del 18/06. La hoja de ruta refuerza esto: estructura mínima visible, riqueza en la ejecución.
8. Diana eligió **batch semanal + toques diarios** como rutina, y estandarizar en **Opus (einstein)** con Fable solo si es necesario.
9. **Los rituales mueren si Diana no los revisa a diario** — patrón confirmado por ella: "si yo no hago ese trabajo diario, profesores y alumnos dejan de hacerlo". Por eso todo ciclo nuevo (tickets, portafolio, reportes) debe sostenerse por **consecuencia visible semanal**, nunca por revisión diaria de Diana (§9).
10. **El compromiso es mutuo y el aula no alcanza:** 575 horas no producen inglés sin trabajo diario en casa. El estudiante debe tener **portafolio de audios/videos diarios** y mostrar su progreso en cada clase. Bonus estratégico: un estudiante que practica a diario detecta errores del profe — los profes A1-B1 no son nativos y cometen errores naturales; el portafolio + tickets son también control de calidad docente indirecto.
11. **Cero material físico comprado:** no hay liquidez para flashcards/sobres/impresiones extra. Toda actividad con objetos = tarea previa al estudiante con Plan B (regla existente, ahora con razón económica explícita).

## 4. Rutina semanal (el workflow)

**Sesión grande semanal** (1 vez, ej. sábado/domingo):
1. `/clases` para la semana completa de los 5 cohortes — en formato hoja de ruta (§5).
2. Procesar los reportes de profes de la semana anterior (§8) → ajustes a guías + auditoría si aplica.
3. Actualizar `DASHBOARD_SEMANAL.md` (§6) con el corte de la auxiliar contable.
4. **Bloque comercial obligatorio** (mínimo 1/3 de la sesión): avanzar la acción comercial de la semana (campaña, seguimiento leads, material). *Regla: lo comercial va en la agenda de la sesión, no "cuando sobre tiempo" — nunca sobra.*
5. Commit + push a GitHub (respaldo — el repo vive en Downloads de una sola máquina).

**Toques diarios** (minutos, no horas): imprevistos (festivo, ausente → `/repaso-ausente`, ajuste puntual por reporte de profe).

**Reparto de modelos (estandarizado, post-Fable):**
- **einstein (Opus)** = motor por defecto: guías, material comercial, investigación.
- **tesla (Sonnet)** = extraer del libro, leer reportes/PDFs de profes.
- **mark (Haiku)** = correr generadores, verificar PDFs en disco, git.
- **sidis (Fable)** = solo decisiones que cambian el negocio (diseño de producto nuevo, pricing, trade-offs mayores). Todo lo demás debe funcionar sin Fable.

## 5. Rediseño de guía: HOJA DE RUTA (decisión 05/07/2026)

Reemplaza el formato largo para todas las guías nuevas:

- **Página 1 = LA guía** (lo único que el profe necesita ejecutar al 100%): encabezado (nivel · Cl N · virtud · Frase del Día), **4 bloques** con duración e instrucción ejecutable exacta (qué escribir en tablero, qué simulación, quién de pie), tarea con due date, error paper, checkboxes de entregables.
- **Estructura fija de los bloques (garantiza el método por diseño, no por confianza):**
  - **Bloque 1 abre SIEMPRE con recuperación espaciada**: instrucción exacta de qué recuperar de Cl N-3 y Cl N-7 (oral, de pie, ~10 min), generada automáticamente porque Claude conoce el historial de módulos. Cuando hay tickets de la semana anterior, la recuperación se construye **con los errores reales de los tickets** — así los estudiantes ven que lo que escriben se lee.
  - **Bloque 1 incluye el chequeo público de portafolio** (~3 min): el profe pregunta quién hizo el audio/video diario — accountability pública, patrón ya validado en B2.
  - **Bloque 4 cierra SIEMPRE con el ticket de salida** (5 min): cada estudiante escribe 3-5 frases con la estructura del día; viaja físico a coordinación junto con el error paper.
- **Cero material físico del profe o de la academia** (sin liquidez para comprarlo): cualquier actividad con objetos = el profe se lo pide al estudiante con anticipación como tarea, siempre con Plan B en la hoja.
- **Anexo opcional (máx 3-4 págs)** solo cuando el módulo lo exige: reglas y ejemplos verbatim del libro, Plan B. Se imprime solo si el profe lo pide o el módulo es nuevo/difícil.
- **Tope duro: 5 páginas totales** (vs 12 actuales). Ahorro estimado de papel y tokens: >60%.
- Todos los no-negociables Heiiu siguen aplicando; el checklist de verificación se corre igual (mark lo audita post-generación y reporta solo excepciones).
- La skill `/clases` debe actualizarse a este formato (recordar: `.claude/` es solo local, no está en git — respaldarla aparte).

## 6. Dashboard semanal de supervivencia

Archivo único: `documentos_operativos/DASHBOARD_SEMANAL.md`, regenerado en cada sesión grande. Cuatro números, nada más:

1. **Caja confirmada del mes vs nómina+costos** (dato: corte semanal de la auxiliar contable — pedirlo es la primera acción admin).
2. **Leads y matrículas nuevas de la semana** (incluye 1-a-1 virtuales).
3. **Riesgo de deserción por cohorte** (asistencia + señales de los reportes de profes).
4. **% ejecución de guías por profe** (de los reportes — mide si el producto élite llega al aula).
5. **Señal de aprendizaje por cohorte** (de tickets de salida + error papers: % de estudiantes que dominan la estructura de la semana, errores comunes, cumplimiento del portafolio diario — ver §9).

Regla de rigor: si un dato no llegó, la celda dice "SIN DATO" — nunca se estima ni se inventa.

## 7. Protección IP (reglas para digitalizar sin miedo)

La joya es el sistema completo Y los paquetes de guías. Reglas:
1. Los profes reciben **solo la hoja del día** (o de la semana en curso), nunca paquetes de nivel ni el Blueprint. El Blueprint no sale de coordinación jamás.
2. Todo PDF entregado a profe lleva **marca de agua**: "Uso exclusivo {profe} — Heiiu — {fecha}" (agregarlo al motor de PDF es un cambio pequeño).
3. **Cláusula de confidencialidad/propiedad intelectual en el contrato de profesor ANTES de escalar la entrega digital.** (El contrato profesor aún no existe — la plantilla hora-cátedra v2 es la base; esto ya era pendiente conocido y ahora es bloqueante.)
4. Sin nombres de metodologías en nada que toque un profe (regla existente, se mantiene).

## 8. Ciclo de reporte de profes (digital, formato fijo)

- **1 hoja fija por clase** (mitad de página real): ☐ por bloque ejecutado/saltado, 3 errores oídos (citas), asistencia, 1 línea libre. Es la contraparte natural de la hoja de ruta — mismo esqueleto.
- Canal: digital (foto o formulario — pilotear con Tomás, el profe más confiable, antes de exigirlo a todos).
- Procesamiento: en la sesión semanal, tesla extrae → alimenta dashboard (§6), auditoría y ajustes de guías. El doble protocolo de error paper (anónimo en clase / con nombres a coordinación) se mantiene.
- El reporte del profe es 1 de las 3 patas de la **triangulación** del §9 — nunca se toma solo como verdad.

## 9. Auditoría del aprendizaje y del método (decisiones 06/07/2026)

El §8 audita lo que el profe *dice* que hizo; esta sección audita lo que el estudiante *realmente aprendió* y si el método Blueprint se ejecutó de verdad. Principio rector: **el ciclo se sostiene por consecuencia visible semanal, no por revisión diaria de Diana** (los rituales sin auditoría mueren — patrón confirmado).

**Las 3 señales por estudiante:**
1. **Ticket de salida** (todas las clases, todos los cohortes): 3-5 frases con la estructura del día, últimos 5 min del Bloque 4. Físico, viaja con el error paper. Es señal individual de aprendizaje imposible de falsear por el profe y no se siente como examen.
2. **Portafolio diario** (el "compromiso mutuo"): 1 audio o video corto (1-3 min) por día fuera del aula — repetir, escuchar, grabarse con el celular. Cero costo, cero material. El chequeo es **público en Bloque 1** (el profe pregunta, no revisa contenido — revisar contenido es de coordinación). El progreso acumulado se muestra en los hitos ya existentes (shadowing/mini-competencias, checkpoints, midterm/final).
3. **Error paper** (ya existe, doble protocolo) — se mantiene igual.

**Cómo se cierra el ciclo SIN trabajo diario de Diana:**
- Recolección: diaria y física (el profe solo recoge y entrega — no evalúa ni comunica evaluaciones).
- Procesamiento: **semanal, en la sesión batch** — tesla lee tickets + error papers + reportes y produce el mapa de la semana.
- **Consecuencia visible (esto es lo que mantiene vivo el ritual):** las hojas de ruta de la semana siguiente abren el Bloque 1 recuperando LOS ERRORES REALES de los tickets, con mención explícita ("coordinación leyó sus tickets — el error común fue X"). Estudiantes y profes comprueban cada semana que lo que producen se lee y tiene efecto. Ni Diana ni nadie revisa a diario.

**Triangulación (garantía de que el método se ejecutó):** cada semana se cruzan 3 fuentes independientes — (a) reporte firmado del profe, (b) tickets/producción de estudiantes, (c) error paper. Si el profe reporta "Bloque 1 ejecutado" pero los tickets no muestran rastro de la recuperación espaciada, hay divergencia → esa clase entra a Sistema_Auditoria. La auditoría formal pasa a ser **por excepción** (solo divergencias), no por muestreo ciego.

**Control de calidad docente indirecto (profes no nativos):** tesla marca en los tickets errores *sistemáticos* de todo el grupo en una misma estructura — patrón típico de error enseñado, no de error de estudiante. Va al mapa semanal como alerta discreta para coordinación; jamás se comunica vía estudiantes.

**Ficha viva por estudiante:** 1 archivo por estudiante (carpeta interna de coordinación, ej. `Estudiantes complejos/` o nueva `fichas/`) con: errores recurrentes (con nº de clase), cumplimiento de tarea y portafolio, síntesis de tickets, avance de proyecto, riesgo y próxima acción. Se actualiza SOLO en la sesión semanal; celda sin señal = "SIN DATO". Las fichas alimentan refuerzos y decisiones — pero **nunca meten nombres en guías reutilizables**. Es la mentoría élite hecha visible y es material vendible como reporte de progreso.

## 10. Frente comercial (secuencia recomendada)

**Recomendación de Claude (Diana delegó la prioridad #1):** *detener la hemorragia de tiempo (hoja de ruta) para financiar la máquina de ventas, empezando por el producto que ya existe y ya es rentable.*

**Semanas 1-2:**
1. Migrar a hoja de ruta (§5) — ya incluye ticket de salida, recuperación espaciada y chequeo de portafolio (§9) → libera el tiempo de Diana y arranca la auditoría de aprendizaje en el mismo movimiento.
2. **Campaña 1-a-1 virtual premium**: nombre, precio premium, pitch ("mentoría individual de inglés para gente sin tiempo"), material con lo comercial 2026 ya creado. Es caja rápida sin diseño nuevo y sin riesgo de deserción.
3. Pedir a la auxiliar contable el primer corte semanal → Dashboard v1.

**Día ~30:**
4. Ciclo de reporte digital de profes (§8) + marca de agua + cláusula IP en contrato.
5. Decisión explícita del posicionamiento: segmento premium como negocio, social como programa aparte (becas con cupo), y marketing dirigido al que paga.

**Día ~90:**
6. Diseñar el **grupo virtual pequeño premium** con lo aprendido en las 1-a-1: formato **cohorte corto prepagado** (tipo bootcamp de 8 semanas pagado completo) para neutralizar el miedo deserción-vs-nómina. sidis/Fable se usa aquí.
7. Triage del backlog del Blueprint: solo se ejecuta lo que vende o retiene; el resto queda en "si sobrevivimos".

## 11. Higiene del sistema (mantenimiento mínimo)

- **Push a GitHub en cada sesión grande** — el repo es el negocio y vive en una sola máquina (carpeta Downloads).
- Respaldar `.claude/` (skills `/clases` y `/repaso-ausente`, settings) fuera del repo — git las ignora.
- Los PDFs de niveles cerrados / versiones V1 pueden archivarse (backup_pre_clean ya existe como precedente) para que el repo no siga engordando.

## Preguntas abiertas

- ¿La auxiliar contable puede entregar el corte semanal en un formato fijo (Excel simple)? Definir con ella.
- Métrica de éxito de la campaña 1-a-1 (¿cuántas matrículas 1-a-1/mes hacen la diferencia en caja?): sale del primer corte de la auxiliar.
- Formato exacto del canal de reporte de profes (foto vs formulario) — decidir tras el piloto con Tomás.
- Precio y nombre del producto 1-a-1 premium — sesión comercial específica.
- ¿El contrato de estudiante (31 cláusulas) ya cubre el portafolio diario como obligación, o hay que agregarlo? Revisar antes de anunciarlo como compromiso formal.
- ¿Dónde entregan los estudiantes los audios/videos diarios sin que nadie deba revisarlos a diario? (propuesta inicial: grupo/canal por cohorte donde subir = evidencia; coordinación muestrea semanal).
