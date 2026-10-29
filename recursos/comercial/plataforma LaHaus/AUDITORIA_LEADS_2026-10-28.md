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
| Reintentos que lanzan 2 o más preguntas nuevas en vez de repetir la pendiente | 25 de 60 conversaciones con respuesta | 07/10 punto 4. **NO SE ALEGA (29/10):** LaHaus respondió el 9/10 que es configuración fija (punto 4) y Heiiu lo aceptó por escrito el 13/10 ("ok en tres cosas: agrupar mensajes, validar el nombre y variar los reintentos"). |
| Llamada de voz IA en frío en leads creados después del 13/10 | 14 leads (sin contar una prueba interna) | 13/10 punto 7a. **NO SE ALEGA (29/10):** LaHaus respondió el 17/10 (sección 12) que apagarlas aplica a todos los leads y Heiiu nunca confirmó que las apagaran (la carta del 19/10 no lo dice). Queda como decisión pendiente para la reunión del 30/10. |
| Leads de pauta de 8 a 11 días incluidos en el blast de Halloween del 26/10 | 10 (43 de pauta en total) | 07/10 punto 6 y 13/10, **verificar quién armó la lista** |

Ejemplo de reintento que avanza el flujo (fila 504): tras el mensaje del anuncio, el agente encadena *"¿el curso es para ti o para alguien más?"* → *"¿qué tanto inglés tienes?"* → *"¿Qué jornada te queda mejor?"* sin respuesta del lead entre una y otra.

## 4. Bloque C — Sincronización de citas (el bloque más fuerte)

| Fila | Fecha | Qué pasó (cita textual, sin datos personales) |
|---|---|---|
| **188** | 27/10 | Lead: "Jueves". Agente: *"Ya estoy procesando tu llamada para el jueves 29 de octubre a las 4:15 pm"* → *"Un asesor te va a contactar para confirmar tu agendamiento."* **Fecha de visita vacía**, etapa SUCCESSFUL_CONTACT. **29/10:** el lead **no tiene teléfono en el panel** (canal EXTERNAL, sin origen ni anuncio), el panel no lo encuentra por nombre ni por correo, no está en las bandejas de Instagram ni Facebook de Heiiu y **tampoco está en Funnel Up**. El agente le ofreció *"llamada de WhatsApp a este mismo número"* y agendó una llamada que nadie podía hacer. La conversación (51 mensajes) solo existe dentro de LaHaus: **LaHaus debe decir por qué canal entró** (pregunta enviada el 29/10). Mientras tanto la asesora le escribe al correo. Ver §8. |
| 685 | 02/10 | Agente: *"Ya le pasé tu solicitud al equipo para que te marquen hoy a las 4:00 pm"*. Sin cita registrada. Es anterior a la muestra, pero prueba que el problema se repite. |
| 574 | 07/10 | Lead: "12". Agente: *"Para la llamada de mañana a las 12:00 ya se nos ocupó el espacio"*, dos veces. Sin cita. (Reportado el 08/10, punto 16.) **NO SE ALEGA (29/10):** LaHaus lo explicó el 9/10 (informe de feedback, punto 16): el lead respondió cuando faltaban menos de 24 h y la regla de anticipación mínima de 24 h **configurada en Heiiu** retiró la franja. Heiiu pidió bajarla a 4 h el 19/10 (punto 7). |
| 489 | 20/10 | Cita registrada para las 12:30 por llamada. Agente: *"¿lograste conversar con la asesora hoy a las 12:30?"* Lead: *"No"*. La etapa sigue SCHEDULED y el agente vuelve a perfilar en vez de reagendar. **Verificar con la asesora antes de alegarlo**: puede ser falla nuestra. |
| 550 | 09/10 | El lead confirma que atendió (*"Si" / "Muy bien"*); la etapa queda CONFIRMED_VISIT y no COMPLETED. |
| 594, 595, 635 (+ 567 y 587 de base) | 5-7/10 | La fecha de registro de la cita es **posterior** a la hora de la cita (hasta 23 h). Puede ser un registro tardío o solo la fecha de actualización: el export no lo distingue. |
| 62 (base) | 27/10 | *"Tu cita ya está lista para el Jueves, 29 de Octubre 2026 15:00"* sin que el lead eligiera hora. Verificar si la agendó la asesora. **También es mañana.** |

**Proporción (corregida el 29/10):** de 9 citas acordadas en conversaciones de pauta (594, 635, 550, 555, 489, 26, 188, 685, 574), **2 no quedaron en el calendario (685 el 2/10 y 188 el 27/10)**; la 574 quedó explicada por una regla nuestra. A eso se suma el caso que LaHaus reconoce por escrito en su informe del 9/10 (pág. 2, "Ajuste 2"): *"un intento de agendamiento que terminó en error técnico y por eso no cuenta como cita"* (no dice cuál lead es; pedir el dato). Y la 188 tiene un agravante propio: el 17/10 (sección 01, paso 7) LaHaus escribió que el agente *"nunca cierra con 'un asesor te contactará'"*, y el 27/10 cerró exactamente así.

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
| B · Seguimientos | **Débil (corregido el 29/10)** | El seguimiento existe. Queda una sola desviación alegable: 16/16 leads silenciosos por debajo de los 5 toques en 24 h que LaHaus describió como su propia cadencia (Jaider, 6/10; Heiiu la aceptó el 7/10). Los reintentos variables los aceptó Heiiu el 13/10 y las llamadas en frío nunca se mandaron apagar. Depende de que la cadencia de 5 toques conste por escrito como configuración de LaHaus. |
| C · Sincronización de citas | **Parcial, el más defendible (corregido el 29/10)** | 2 de 9 citas acordadas sin registro (2/10 y 27/10), más el error técnico que LaHaus reconoce el 9/10, la cita de la fila 62 puesta sin que el lead eligiera hora, la 489 pendiente de la asesora y 5 registros con fecha posterior a la cita. El volumen absoluto es bajo (2-3 casos firmes). |

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

**3. La fila 188 no está en Funnel Up.** Funnel Up solo trae 2 leads el 27/10 (10:02 am y 11:39 am; el segundo es la fila 29 del export) y el lead de la fila 188 se creó a la 1:46 pm; ningún lead sin teléfono de Funnel Up coincide por nombre. En LaHaus hay 10 leads sin teléfono; 5 son conversaciones reales de anuncios (filas 188 del video V8 y 497, 499, 500, 504 del video V1, 16-18/10), todos canal EXTERNAL sin origen ni anuncio. A todos el agente les habló como si fueran de WhatsApp. **Lectura honesta:** hasta que LaHaus diga por qué canal entran esos chats, el caso 188 no se puede cargar a ninguno de los dos: si es un canal de LaHaus (su propio WhatsApp o su widget), agendaron una llamada sin número, y es bloque C; si es un canal de Meta que Heiiu conectó mal, es nuestro. La pregunta escrita se envió el 29/10; la respuesta, con hora, es la evidencia. **Ojo (29/10, tarde):** el propio informe de LaHaus del 17/10 (sección 08) ya explica el mecanismo: *"si no aparece el número de teléfono, es porque el usuario activó la función de nombre de usuario de WhatsApp, que oculta el número y lo reemplaza por un apodo; basta con buscar el apodo en WhatsApp"*. Es decir, el lead sí está en el WhatsApp de LaHaus, con nombre de usuario en vez de número. Para ubicarlo hoy: pestaña Conversaciones del panel, por fecha (27/10, 1:46 pm), no el buscador de leads; desde ahí la asesora toma la conversación y le pide el número. Y el agente lo sabía (el informe lo dice) y aun así ofreció *"llamada de WhatsApp a este mismo número"* y cerró con *"un asesor te va a contactar"*, la frase que el 17/10 dijeron que nunca usa.

**4. Qué cambia en el veredicto.** Poco en el bloque C (quedan 685 y 188 sin registro, la 574 se cae por la regla de 24 h nuestra, y la 188 gana peso por el cierre prohibido y el número oculto). Se pierde el argumento de volumen de la semana del 19/10. Se gana un hecho que hay que tener claro antes de la carta: **el 29/10 Heiiu ya tiene un error propio documentado (Meta → Funnel Up)**, y la carta no puede apoyarse en nada que dependa de la configuración de Meta.

**4-bis. El reproche de acompañamiento ("ocho días sin un lead y LaHaus no avisó").** Es cierto que lo sabían: la carta del 19/10 les dijo que la única campaña activa era la del 19/10, clic a WhatsApp, con los códigos V5 y V6, y el 22/10 hubo reunión con su Customer Success. Del 19 al 27/10 no entró un solo chat V5/V6 a su panel y nadie de LaHaus lo señaló. **Pero no sirve para la Garantía de Funcionamiento:** la Orden de Servicio solo garantiza tres funcionalidades (respuesta oportuna, seguimientos y sincronización de citas) y la única obligación de aviso que firma LaHaus es cuando los leads lleguen a 1.000 al mes. No hay cláusula de monitoreo ni de alerta. Y LaHaus va a responder tres cosas, las tres ciertas: la configuración de Meta es de Heiiu; Heiiu tenía el panel y SAMI y tampoco lo vio hasta el export del 28/10; en la reunión del 22/10 no se planteó. **Uso correcto:** en la conversación comercial, como falla de acompañamiento que justifica la salida de mutuo acuerdo ("un Customer Success que no nota ocho días en cero no es el servicio que compramos"), nunca en la notificación de garantía.

**5. Pendientes de esta actualización.**
- Brian: desde qué fecha y hasta cuándo los anuncios apuntaron al número de Funnel Up; en qué ubicación estaba V8 el 27/10 (WhatsApp, Instagram, Messenger); por qué Funnel Up recibe leads sin número; si las 84 conversaciones del 10/10 también cayeron allá.
- LaHaus: por qué canal entró la fila 188 (y las filas 497, 499, 500 y 504) y cómo se contacta a un lead sin número en su panel.
- Asesora: correo enviado a la fila 188 el 29/10 antes de la hora de la llamada; resultado.
- Los 12 leads de Funnel Up sin número y los 55 con número se trabajan desde Funnel Up o se cargan a LaHaus; decisión de gerencia.

## 9. Salidas posibles al 29/10 (tras leer la Orden de Servicio, los TyC v.27.08.25, los correos de cierre del 16 y 21/09, las cartas del 13 y 19/10 y los informes de LaHaus del 9 y 17/10)

**Lo firmado, en cuatro líneas.** Licencia de 90 días desde el 28/09 (JP confirmó por correo que corre desde la activación, ~30/09; verificar el correo exacto); $1.200.000 al mes, pagados por anticipado y **no reembolsables**; *"la cancelación no otorga reembolsos ni créditos y surte efecto al término del periodo contratado"*; renovación solo con aprobación previa de Heiiu (ajuste iii); descarga de base e historial antes de desactivar (ajuste ii). TyC: el software se entrega *"tal como está"*; LaHaus no responde por la exactitud de los mensajes del agente (cláusula X.vi); responsabilidad total limitada a lo pagado en los 3 meses anteriores (X.iii); no pagar genera mora y **suspensión sin declaración judicial** (IV); impago reiterado es causal para que LaHaus termine por culpa de Heiiu, sin devoluciones (XII); controversias: arreglo directo 10 días hábiles y luego arbitraje en Medellín con costos por mitades (XV). La única puerta de salida anticipada que existe en el papel es la **Garantía de Funcionamiento** de la Orden: incumplimiento *"sustancial y reiterado"* de respuesta oportuna, seguimientos o sincronización de citas, dentro de los primeros 60 días, notificado por escrito, **y no subsanado en 10 días hábiles**. No hay cláusula de monitoreo, de informes ni de acompañamiento. No existe en la carpeta un acuerdo de confidencialidad firmado aparte (la Orden trae la cláusula de confidencialidad y no reutilización, así que no es un incumplimiento útil).

| Camino | Qué implica | Costo | Probabilidad / riesgo |
|---|---|---|---|
| **1. Garantía de Funcionamiento** (carta formal) | Notificar por escrito los casos del bloque C (188, 685, 62, el error técnico del 9/10, 489 si la asesora lo confirma) y el B (16/16 bajo 5 toques). LaHaus tiene 10 días hábiles para corregir. | Si prospera, se termina sin pagar el mes 3 (el mes 2 ya está causado desde el 28/10). | **Baja como salida, útil como palanca.** Son 2-3 casos firmes; LaHaus solo tiene que "subsanar" (arreglar la sincronización) en 10 días y la terminación se cae. Y van a alegar que la cadencia de 24 h, Meta y Funnel Up son de Heiiu. |
| **2. Salida de mutuo acuerdo al cierre del mes 2** (recomendado) | Una sola carta a JP, no a Jaider: (a) notifica la garantía con los casos del bloque C, (b) recuerda el correo del 16/09 donde JP aceptó *"permanencia de 2 meses si la plataforma incumple su operación"*, (c) lista lo prometido y no entregado (resultado de los casos prometido para el 21/10 y no entregado al 22/10; informe semanal por fuente y toque "en curso" desde el 9/10 y nunca entregado, reemplazado por SAMI que no tiene acceso a las conversaciones; el cierre "un asesor te contactará" que el 17/10 dijeron que no existe; 8 días sin un lead de la campaña avisada y nadie lo señaló), (d) propone terminar el 27-29/11 pagando el mes 2 y nada más, con descarga de base e historial y sin penalidades, (e) deja escrito que si no aceptan, Heiiu ejerce la terminación anticipada al vencer los 10 días hábiles. | Mes 2 ($1.200.000). Se ahorra el mes 3. | **Media-alta.** Para LaHaus es más barato aceptar que pelear por $1,2M en Medellín, y la carta les quita el caso de éxito (la confidencialidad exige autorización de Heiiu para usar la marca). |
| **3. Cumplir los 90 días y no renovar** | Pagar meses 2 y 3; enviar aviso de no renovación a suscripciones@lahaus.com al menos 5 días hábiles antes del vencimiento (antes del 18/12). | $2.400.000. | **Segura.** Es el piso: sin pelea, sin riesgo. |
| **4. Dejar de pagar sin carta** | TyC IV: mora y suspensión inmediata. XII: impago reiterado = terminación por culpa de Heiiu, sin devoluciones y con derecho de LaHaus a cobrar perjuicios. Se pierde el acceso a la base y al historial (el derecho de descarga es "previo a la desactivación"). | Aparentemente $0; en realidad exposición a $2.400.000 + mora, y la base en riesgo. | **No.** Nunca cortar sin carta; antes de cualquier corte, descargar base e historial y que Brian cambie el destino de los anuncios. |

**Recomendación:** camino 2, con el camino 1 adentro de la misma carta. Secuencia: (1) 30/10 reunión de cadencia ya agendada: se pregunta por la fila 188, por el resultado de los casos del 21/10 y por el informe semanal, sin anunciar nada; (2) 30-31/10 se pide el corte del primer mes por fuente (ellos mismos lo pusieron como hito del 31/10); (3) **2/11: carta a JP con copia a Jaider** (camino 2) y, el mismo día, el pago del mes 2, para que el impago no se convierta en el argumento de ellos; (4) si al 18/11 no hay respuesta o no aceptan, carta de terminación anticipada por la garantía (los 10 días hábiles desde el 3/11 vencen alrededor del 18/11; el 60.º día cae alrededor del 27-29/11 según la fecha de activación: **verificar con el abogado y con el correo de JP**). Lo que NO va en la carta: la caída de volumen, la campaña V5/V6, Funnel Up, los errores de contenido del agente (bloque D) y los nombres de los leads.

**Lo que dice el hilo de correo con JP (revisado en Gmail el 29/10; un solo hilo, "Propuesta LaHaus AI - Plan PRO", 8 mensajes del 16 al 21/09):**

- **Permanencia de 2 meses, textual.** Diana (16/09, 4:45 pm): *"si en los primeros 60 días la plataforma incumple su propia operación (respuesta inmediata a los leads, seguimientos ejecutados, citas sincronizadas al calendario), ¿podemos terminar anticipadamente sin cumplir la permanencia de 3 meses?"*. JP (16/09, 6:18 pm): *"Podemos tener un acuerdo de permanencia mínima por dos meses si no cumple con los requerimientos que mencionas, y si cumple de 3 meses como lo mencionamos."* Diana (16/09, 7:00 pm): *"Que la permanencia mínima de 2 meses por incumplimiento operativo quede en el contrato u orden de servicio."* JP (16/09, 7:09 pm): *"De acuerdo, lo incluimos."* Eso es lo que la Orden tradujo como Garantía de Funcionamiento. Las tres funciones de la garantía son las que Diana escribió; la frase de JP es más amplia ("los requerimientos que mencionas") y sirve en la carta.
- **Fecha desde la que corre el término: NO está confirmada por correo.** JP (16/09, 6:18 pm) escribió: *"El pago mensual es adelantado, pero ese mes empieza a contar una vez se logre la implementación y esté activo el asistente AI. Ese día se fija la fecha de corte."* Diana lo pidió como ajuste 2 de la Orden el 21/09 y **ese correo no tiene respuesta en el hilo**; la Orden v2 firmada dice 28/09. Si hubo confirmación, fue por WhatsApp (buscarla). **Para los plazos se asume lo conservador: inicio 28/09, día 60 = 27/11.** Notificar antes del 3/11 deja margen de sobra.
- **Acuerdo de confidencialidad aparte:** JP (16/09, 7:09 pm): *"de acuerdo lo diligenciamos en el transcurso de la próxima semana, antes de salir al aire."* No hay ningún documento firmado en la carpeta ni en el correo. La Orden trae la cláusula, así que no es un incumplimiento útil, pero es una promesa más sin cumplir para la lista de la carta.
- **La propuesta del 16/09 (correo de JP, 11:42 am) incluye en el Plan PRO** *"Auditorías de Campañas Meta: auditorías ilimitadas para identificar oportunidades de mejora y eficiencia en la pauta que administra tu equipo"* y *"Notificaciones en tiempo real: alertas inmediatas ante cada nuevo lead y actividad relevante de tus campañas"*. Nunca se hizo una auditoría de campañas. No convierte el error de Meta en culpa de LaHaus (la configuración es de Heiiu), pero sí responde al "ustedes no tocan Meta": vendieron auditorías de la pauta y ocho días en cero no les llamaron la atención. Va en la conversación, no en la notificación.
- **Base y landing al terminar** (JP, 16/09, 3:06 pm): *"La base de datos ustedes la pueden descargar y solicitarla una vez terminen el servicio, antes de inactivar la cuenta"*; la landing *"queda por un tiempo limitado (6 meses) si cancelan el servicio"*.
- No hay en Gmail factura del mes 2, ni correo de suscripciones@lahaus.com, ni copia de la Orden firmada por Adobe Sign (solo los recordatorios de firma del 23 al 30/09). Si existe, está en otro correo o en el WhatsApp.

**Fila 188, respuesta de LaHaus (29/10, 2:07 pm, Jaider por WhatsApp):** la cita no se creo porque el lead tiene el numero oculto con nombre de usuario de WhatsApp y el agente lo derivo a contacto humano. Confirmado con la transcripcion: el lead NUNCA pidio un humano; el agente ofrecio franjas, el lead eligio "jueves", el agente escribio "en un momento te confirmo" y derivo solo. Nadie confirmo en dos dias. **Lo que decide la culpa: a quien le llego la notificacion de contacto humano del 27/10 a las 2:26 pm** (pendiente: respuesta de la asesora). Si le llego y no se atendio, es de Heiiu y se corrige con los barridos de 12:00 y 6:00 pm; si no le llego a nadie, el agente deriva a un humano inexistente y es bloque B/C. En cualquier caso queda una limitacion de plataforma no informada: el agente no puede agendar leads con nombre de usuario, y el informe del 17/10 (seccion 08) explico el apodo sin decir eso. Pregunta para el 30/10: cuantos leads con nombre de usuario han entrado desde el 29/09 y que paso con cada uno.

**Para cerrar esta sección falta:** la respuesta de LaHaus sobre la fila 188, la confirmación de la asesora sobre la 489, el dato de qué lead fue el "error técnico" del 9/10, y buscar en el WhatsApp con JP si confirmó la fecha de activación como inicio del término.
