# AUDITORÍA DE LEADS LAHAUS — 29/09 AL 28/10/2026

Interno de gerencia · para decidir el 2/11 (seguir, salida de mutuo acuerdo o Garantía de Funcionamiento) · fuente: export del panel `leads_20261028_152059.xlsx` (689 filas, corte 28/10 15:20). Cada caso se identifica por **fila del Excel**; no hay nombres, teléfonos ni correos. Lista completa de casos: `AUDITORIA_LEADS_2026-10-28_CASOS.csv` (fila · bloque · hallazgo). **Actualizada el 29/10** con el export del CRM anterior `heiiu-leads-funnelup-2026-10-19-al-27.csv` (67 leads; ver §8).

## 0. Dos advertencias de método (antes de leer los números)

1. **El export no trae hora por mensaje.** Solo trae fecha de creación del lead y fecha del último mensaje. Con este archivo **no se puede medir el tiempo de respuesta** del agente.
2. **La columna Origen no sirve para separar pauta de base vieja.** LaHaus sobrescribe el origen y la campaña con el último blast: 26 leads de pauta de la muestra (formularios del 6 al 9/10 y chats de los anuncios V1/V3 del 15 al 18/10) aparecen como "BLAST" porque después les llegó la reactivación de Halloween. Por eso los clasifiqué por el **primer mensaje de la conversación**: si abre con "Hace unas semanas nos escribiste" (blast del 6/10) o con la plantilla de Halloween, es **base vieja**; si abre con el lead escribiendo o con el saludo de formulario, es **pauta**. Resultado: 147 de pauta, 489 de la base del 6/10 y 53 de la base cargada el 27/10.

## 1. Embudo real (pauta)

| Semana (lun-dom) | Leads | De formulario | Sin ningún mensaje | Solo escribió el agente | Respondieron | Cita registrada | Asistida (COMPLETED) |
|---|---|---|---|---|---|---|---|
| 28/09-04/10 | 37 | 19 | 6 | 14 | 17 | 3 | 1 |
| 05/10-11/10 | 69 | 44 | 17 | 18 | 34 | 2 | 0 |
| 12/10-18/10 | 29 | 0 | 5 | 0 | 24 | 2 | 0 |
| 19/10-25/10 | 2 | 0 | 2 | 0 | 0 | 0 | 0 |
| 26/10-28/10 | 10 | 0 | 3 | 0 | 7 | 0 | 0 |
| **Total** | **147** | **63** | **33** | **32** | **82** | **7** | **1** |

- **Muestra auditada (pauta creada desde el 06/10): 103 leads.** 60 respondieron, 27 sin ningún mensaje, 16 solo con mensajes del agente. 4 citas registradas (filas 26, 489, 550, 555) y **0 marcadas como asistidas** (la fila 550 sí asistió según la conversación, pero la etapa no se actualizó).
- **Etapas de la muestra:** UNQUALIFIED 54 · SUCCESSFUL_CONTACT 21 · NEW 18 · UNCONTACTED 4 · STARTED_SCHEDULE 2 · SCHEDULED_VISIT 2 · CONFIRMED_VISIT 2 · COMPLETED_VISIT 0.
- **La caída de volumen:** leads de pauta por día: 6/10: 23 · 7/10: 22 · 8/10: 12 · 9/10: 5 · **10 al 15/10: cero** · 15-18/10: 29 (anuncios V1/V3) · **19 al 26/10: 2 (los dos sin conversación)** · 26-28/10: 10 (anuncios V7/V8).
  - El último lead de formulario entra el 9/10 a las 19:03. Según la carta del 13/10, el formulario "Curso Inglés" siguió activo hasta el 13/10: **4 días de formulario activo sin un solo lead en el panel.**
  - La campaña V5/V6 del 19/10 (la única activa según la respuesta del 19/10): **ningún chat con código V5 o V6 en todo el archivo.**
  - **ACTUALIZACIÓN 29/10 — el hueco del 19 al 27/10 está explicado y NO es de LaHaus.** Los chats de los anuncios de esa semana entraron al número de WhatsApp del CRM anterior (Funnel Up) y no al de LaHaus: 67 leads del 19 al 27/10 (19/10: 3 · 20/10: 6 · 21/10: 14 · 22/10: 8 · 23/10: 8 · 24/10: 6 · 25/10: 10 · 26/10: 10 · 27/10: 2), aunque el número de LaHaus estaba conectado. Es la configuración de Meta, que es de Heiiu; LaHaus no la toca. **Este punto se retira del reclamo** (ver §6, punto 1 y §8).

**Contexto, base vieja (no cuenta para la evaluación de la pauta):** base del 6/10: 489 leads, 77 respondieron, 3 citas, 1 asistida (fila 567). Base del 27/10: 53 leads, 12 respuestas, 0 citas. Blast de Halloween (22-26/10, incluye 43 leads de pauta): 395 envíos visibles, 23 respuestas, 2 citas (filas 62 y 26). Plantilla A ("perder la oportunidad"): 208 envíos, 14 respuestas, 2 citas. Plantilla B ("que no te dé miedo"): 187 envíos, 9 respuestas, 0 citas.

## 2. Bloque A — Respuesta oportuna

**Lo que no se puede medir:** el tiempo de respuesta (no hay hora por mensaje).

| Señal | Casos | Filas |
|---|---|---|
| Formulario sin ningún mensaje del agente (6-8/10) | 13 | 557, 560, 562, 565, 569, 570, 571, 575, 578, 585, 586, 588, 589 |
| Entrada por WhatsApp con transcripción vacía; 10 de ellos en etapa SUCCESSFUL_CONTACT, una contradicción | 13 | 477, 485, 505, 507, 508, 510, 511, 512, 513, 515, 546, 577, 644 |
| Retraso medible (el único): primer mensaje 34 min después de crear el lead (7/10, 23:51) | 1 | 566 |
| Último mensaje del lead sin respuesta | 1, no cuenta: eran códigos de Facebook, no un lead | 66 |
| Quejas por demora ("no me respondieron", "sigo esperando") | **0** | — |

Cita del único retraso medible (fila 566): el lead se crea a las 23:51 del 7/10 y el único mensaje, *"¿Prefieres que revisemos las opciones directamente por aquí o mediante una llamada breve?"*, es de las 00:25. El otro caso con un solo mensaje (fila 24) respondió en 12 segundos.

**Lectura honesta:** las 26 transcripciones vacías son el dato más grave del bloque, pero no prueban demora: pueden ser envíos que Meta rechazó. El informe de LaHaus del 9/10 (pág. 2) reconoce que solo al 80,4 % de los leads de pauta les llegó el primer mensaje. Heiiu pidió el 13/10 (punto 4 y punto 9) la causa y los códigos de error 131049/131026 por lead. Con este archivo no se ve que lo hayan entregado.

## 3. Bloque B — Seguimientos

**Lo pedido, con fecha.** El 07/10 (punto 4) Heiiu escribió: *"Los 5 toques en 24 horas para lead nuevo están bien"*, y que los reintentos repiten **la misma** pregunta pendiente. En el punto 6 pidió excluir de la reactivación a quien tuvo conversación en los últimos 30 días. El 13/10 (punto 7) pidió máximo un contacto al día (días 0, 1, 3 y 7) y apagar las llamadas de voz de la IA en frío. **Ojo:** la cadencia del 13/10 no está acordada. El 19/10 Heiiu la dejó como "nuestra propuesta" para la revisión del 30/10, así que no sirve como incumplimiento.

**Lo que muestra el archivo:** el agente **sí hace seguimiento**. Casi todas las conversaciones de pauta con respuesta tienen entre 4 y 8 mensajes del agente después del último mensaje del lead, y cierran con *"¿prefieres que dejemos tu solicitud en pausa por ahora?"*. En al menos 15 conversaciones hay más mensajes por iniciativa del agente que días transcurridos: si en algo falla, es en que insiste de más, no de menos.

| Desviación medible | Casos | Pedido que incumple |
|---|---|---|
| Lead que nunca respondió: 4 contactos o menos en total, ninguno llega a 5 (7 con 4, 7 con 3, 1 con 2, 1 con 1) | 16 de 16 | 5 toques en 24 h (07/10) |
| Lead callado a mitad del flujo con 0-1 seguimiento (572) o con despedida y cierre sin aviso visible (564 "Déjame ya te aviso"; 590 "Gracias") | 3 | 07/10 punto 5 |
| Reintentos que lanzan 2 o más preguntas nuevas en vez de repetir la pendiente | 25 de 60 conversaciones con respuesta | 07/10 punto 4 |
| Llamada de voz IA en frío en leads creados después del 13/10 | 14 leads (sin contar una prueba interna) | 13/10 punto 7a, **verificar si LaHaus lo aceptó en su informe del 17/10** |
| Leads de pauta de 8 a 11 días incluidos en el blast de Halloween del 26/10 | 10 (43 de pauta en total) | 07/10 punto 6 y 13/10, **verificar quién armó la lista** |

Ejemplo de reintento que avanza el flujo (fila 504): tras el mensaje del anuncio, el agente encadena *"¿el curso es para ti o para alguien más?"* → *"¿qué tanto inglés tienes?"* → *"¿Qué jornada te queda mejor?"* sin respuesta del lead entre una y otra.

## 4. Bloque C — Sincronización de citas (el bloque más fuerte)

| Fila | Fecha | Qué pasó (cita textual, sin datos personales) |
|---|---|---|
| **188** | 27/10 | Lead: "Jueves". Agente: *"Ya estoy procesando tu llamada para el jueves 29 de octubre a las 4:15 pm"* → *"Un asesor te va a contactar para confirmar tu agendamiento."* **Fecha de visita vacía**, etapa SUCCESSFUL_CONTACT. **29/10:** el lead **no tiene teléfono en el panel** (canal EXTERNAL, sin origen ni anuncio), el panel no lo encuentra por nombre ni por correo, no está en las bandejas de Instagram ni Facebook de Heiiu y **tampoco está en Funnel Up**. El agente le ofreció *"llamada de WhatsApp a este mismo número"* y agendó una llamada que nadie podía hacer. La conversación (51 mensajes) solo existe dentro de LaHaus: **LaHaus debe decir por qué canal entró** (pregunta enviada el 29/10). Mientras tanto la asesora le escribe al correo. Ver §8. |
| 685 | 02/10 | Agente: *"Ya le pasé tu solicitud al equipo para que te marquen hoy a las 4:00 pm"*. Sin cita registrada. Es anterior a la muestra, pero prueba que el problema se repite. |
| 574 | 07/10 | Lead: "12". Agente: *"Para la llamada de mañana a las 12:00 ya se nos ocupó el espacio"*, dos veces. Sin cita. (Reportado el 08/10, punto 16.) |
| 489 | 20/10 | Cita registrada para las 12:30 por llamada. Agente: *"¿lograste conversar con la asesora hoy a las 12:30?"* Lead: *"No"*. La etapa sigue SCHEDULED y el agente vuelve a perfilar en vez de reagendar. **Verificar con la asesora antes de alegarlo**: puede ser falla nuestra. |
| 550 | 09/10 | El lead confirma que atendió (*"Si" / "Muy bien"*); la etapa queda CONFIRMED_VISIT y no COMPLETED. |
| 594, 595, 635 (+ 567 y 587 de base) | 5-7/10 | La fecha de registro de la cita es **posterior** a la hora de la cita (hasta 23 h). Puede ser un registro tardío o solo la fecha de actualización: el export no lo distingue. |
| 62 (base) | 27/10 | *"Tu cita ya está lista para el Jueves, 29 de Octubre 2026 15:00"* sin que el lead eligiera hora. Verificar si la agendó la asesora. **También es mañana.** |

**Proporción:** de 9 citas acordadas en conversaciones de pauta (594, 635, 550, 555, 489, 26, 188, 685, 574), **3 no quedaron en el calendario (1 de cada 3)**, en tres semanas distintas (2/10, 7/10, 27/10). Y LaHaus lo reconoce por escrito en su informe del 9/10 (pág. 2, "Ajuste 2"): *"un intento de agendamiento que terminó en error técnico y por eso no cuenta como cita"*.

## 5. Bloque D — Calidad del agente (no cuenta para la garantía; sí para la decisión comercial)

Los TyC dicen que *"LaHaus no garantiza la exactitud de los mensajes de LaHaus AI"* (TyC v.27.08.25, cláusula anterior a la XI) y que las respuestas *"no garantizamos que sean completamente precisas"*. Todo este bloque queda fuera de la garantía.

| Hallazgo | Filas |
|---|---|
| Precios inexistentes $9.560.000 / $3.150.000 (reportado 07/10; la causa se prometió para el 21/10 y no aparece) | 590 |
| Promesas sobre Au Pair: "te dejamos lista… para que te ganes la plaza"; "pago semanal", "casa y comida cubiertas", "ahorros en dólares"; "puedes aplicar a otras opciones para viajar por trabajo" | 544, 516, 517, 444, 527, 555, 564, 572, 445 |
| Promesa de rapidez ("avanzas más rápido", "ganes confianza rápido") | 524, 527 |
| Saludo "Arranque de octubre" después del pedido urgente del 06/10 | 10 leads del 7 al 9/10 |
| Reglas de edad mal aplicadas: 16 años "entra sin problema" entre semana; 10 y 11 años perfilados y uno agendado (regla del 19/10: menores de 12 no se agenda) | 532, 494, 26 |
| Reinicia el saludo cuando el lead reenvía el mensaje del anuncio (regla del 22/10) | 493, 495, 498 |
| "Estamos abriendo grupo" en la tarde, 5 pares de franjas distintos, franjas en domingo | 526 (domingo también en 501, 524, 527) |
| "Ya actualizo tu correo" sin que el lead diera correo | 489 |

## 6. Lo que dirá LaHaus y qué responder

1. **"La caída de leads es de su pauta."** Es cierto, y con más razón desde el 29/10: Au Pair se pausó el 8/10, el formulario el 13/10, y del 19 al 27/10 los chats de los anuncios se fueron al número de Funnel Up por la configuración de Meta (67 leads que LaHaus nunca vio). Todo eso es de Heiiu y LaHaus lo va a decir con razón: ellos no tocan la configuración de Meta. **No alegar la caída de volumen ni la campaña V5/V6.** Queda una sola pregunta abierta, y es pregunta, no reclamo: los 4 días de formulario activo sin leads (10-13/10) y las 84 conversaciones de la campaña del 10/10 que Meta reporta contra 15 en el panel (abierta desde el 19/10). Antes de usarla, Brian confirma si esas conversaciones también cayeron en Funnel Up.
2. **"Las conversaciones vacías son envíos que Meta rechazó."** Es posible. Respuesta: el código de error por fila, pedido el 13/10 y no entregado.
3. **"Sí hacemos seguimiento."** Es cierto, y no conviene alegar que no lo hay. Respuesta: el reclamo no es la ausencia de seguimiento sino que no se cumple lo configurado (5 toques, repetir la misma pregunta, exclusión del blast, llamadas en frío).
4. **"Los errores del agente no están cubiertos."** Es cierto según los TyC: el Bloque D se usa en la conversación comercial, no en la notificación.
5. **"Heiiu cambió el flujo siete veces."** Es cierto (30/09, 06, 07, 08, 13, 19 y 22/10). Respuesta: una cita acordada que no llega al calendario (fila 188) no depende de ningún flujo; es la funcionalidad de sincronización, y ellos mismos reportaron un error técnico el 9/10.

## 7. Veredicto

| Bloque | ¿Base para "incumplimiento sustancial y reiterado"? | Por qué |
|---|---|---|
| A · Respuesta oportuna | **No, con este archivo** | Sin horas no hay medición. 26 transcripciones vacías y 1 retraso de 34 min; 0 quejas. |
| B · Seguimientos | **Parcial** | El seguimiento existe. Las desviaciones son medibles (16/16 leads silenciosos por debajo de 5 toques, 25 reintentos que avanzan el flujo, 14 leads con llamadas en frío tras pedir apagarlas), pero dependen de que la cadencia de 5 toques conste como configuración de LaHaus y de que las llamadas no estén subregistradas en la transcripción. |
| C · Sincronización de citas | **Parcial, el más defendible** | 3 de 9 citas acordadas sin registro, repetido el 2/10, el 7/10 y el 27/10, más el error técnico que LaHaus reconoce el 9/10 y 5 registros con fecha posterior a la cita. El volumen absoluto es bajo (3 casos). |

**Evidencia que falta del panel (capturas con hora):**

- **C:** calendario del 29/10 sin la cita de la fila 188 (captura hoy); registro de las filas 685 y 574; confirmación de la asesora sobre la fila 489. Son 4 casos. **Fila 188 además:** captura del panel buscándolo por nombre y por correo sin resultado, bandejas de Instagram y Facebook del 27/10 sin esa conversación, y la respuesta escrita de LaHaus sobre el canal por el que entró.
- **A:** para las 26 filas vacías y la fila 566, la hora de entrada del lead, la hora del primer envío y el código de error. Son 27 casos.
- **B:** configuración escrita de la cadencia vigente; registro de llamadas de 3 de los 16 leads silenciosos (filas 552, 566 y 551); confirmación de lo que LaHaus respondió el 17/10 sobre las llamadas en frío y la exclusión del blast.

**Recomendación para el 2/11:** notificar por escrito la Garantía de Funcionamiento **por el Bloque C**, con el B como agravante, apenas estén las 4 capturas de C. Es la única vía que habilita la terminación anticipada. En la misma carta, ofrecer la salida de mutuo acuerdo. No usar el Bloque D en la notificación.

`SUPUESTO DE PLANEACIÓN — verificar con el abogado`: la ventana de 60 días se cuenta desde la firma del 26/09 y vence alrededor del 25/11. Si se notifica el 3/11, los 10 días hábiles vencen alrededor del 18/11 (el 2/11 y el 16/11 son festivos). Los pagos no son reembolsables (Orden de Servicio, "Consideraciones"), así que conviene revisar con el abogado qué cuota se evita.

## 8. Actualización 29/10 — Funnel Up y los leads sin teléfono

**Fuente:** export del CRM anterior, `heiiu-leads-funnelup-2026-10-19-al-27.csv` (67 leads, columnas nombre · teléfono · fecha · hora). Cruzado contra el export de LaHaus por teléfono (10 últimos dígitos) y por nombre. Sin datos personales aquí.

**1. Qué pasó.** Del 19 al 27/10 los chats de los anuncios de Meta entraron al número de WhatsApp de Funnel Up, no al de LaHaus, aunque el de LaHaus estaba conectado. Leads por día en Funnel Up: 19/10: 3 · 20/10: 6 · 21/10: 14 · 22/10: 8 · 23/10: 8 · 24/10: 6 · 25/10: 10 · 26/10: 10 · 27/10: 2. Eso explica el hueco del panel de LaHaus (2 leads de pauta del 19 al 25/10, los dos sin conversación) y la campaña V5/V6 "sin un solo chat". **Es un error de configuración de Meta, es decir, de Heiiu.** LaHaus no administra Meta y lo va a decir; tiene razón. Consecuencia: la caída de volumen de esa semana se retira del reclamo (§6, punto 1) y el embudo de pauta de la tabla del §1 queda incompleto para esa semana por causa nuestra.

**2. Lo que sí cruza.** De los 67 leads de Funnel Up, 55 tienen teléfono y de esos la mayoría ya existe en el export de LaHaus (entraron a la base por el blast de Halloween o por carga). **12 de 67 llegaron a Funnel Up sin número** (casi 1 de cada 5): por WhatsApp eso no ocurre, así que esos leads entraron por otro canal del anuncio (Instagram o Messenger). Pregunta para Brian, no para LaHaus.

**3. La fila 188 no está en Funnel Up.** Funnel Up solo trae 2 leads el 27/10 (10:02 am y 11:39 am; el segundo es la fila 29 del export) y el lead de la fila 188 se creó a la 1:46 pm; ningún lead sin teléfono de Funnel Up coincide por nombre. En LaHaus hay 10 leads sin teléfono; 5 son conversaciones reales de anuncios (filas 188 del video V8 y 497, 499, 500, 504 del video V1, 16-18/10), todos canal EXTERNAL sin origen ni anuncio. A todos el agente les habló como si fueran de WhatsApp. **Lectura honesta:** hasta que LaHaus diga por qué canal entran esos chats, el caso 188 no se puede cargar a ninguno de los dos: si es un canal de LaHaus (su propio WhatsApp o su widget), agendaron una llamada sin número, y es bloque C; si es un canal de Meta que Heiiu conectó mal, es nuestro. La pregunta escrita se envió el 29/10; la respuesta, con hora, es la evidencia.

**4. Qué cambia en el veredicto.** Nada en el bloque C (los 3 casos sin registro siguen: 685, 574 y 188 por la fecha de visita vacía). Se pierde el argumento de volumen de la semana del 19/10. Se gana un hecho que hay que tener claro antes de la carta: **el 29/10 Heiiu ya tiene un error propio documentado (Meta → Funnel Up)**, y la carta no puede apoyarse en nada que dependa de la configuración de Meta.

**5. Pendientes de esta actualización.**
- Brian: desde qué fecha y hasta cuándo los anuncios apuntaron al número de Funnel Up; en qué ubicación estaba V8 el 27/10 (WhatsApp, Instagram, Messenger); por qué Funnel Up recibe leads sin número; si las 84 conversaciones del 10/10 también cayeron allá.
- LaHaus: por qué canal entró la fila 188 (y las filas 497, 499, 500 y 504) y cómo se contacta a un lead sin número en su panel.
- Asesora: correo enviado a la fila 188 el 29/10 antes de la hora de la llamada; resultado.
- Los 12 leads de Funnel Up sin número y los 55 con número se trabajan desde Funnel Up o se cargan a LaHaus; decisión de gerencia.
