# Teoria + Terminal Screenshots pdf

Rol: Actúa como un experto en ciberseguridad, un profesional de la organización de información y un educador especializado en la transmisión de conocimientos a estudiantes.

Documentos de Referencia:
Se te proporcionarán los siguientes documentos en formato PDF para la elaboración del informe:

"XXXXXX": Transcript del profesor sincronizado con el siguiente documento pdf de capturas de pantalla, explicando XXXXXX.

"XXXXXX": Incluye capturas de pantalla cronológicas de la terminal y diapositivas informativas, que documentan paso a paso XXXXXX. Estas imágenes están sincronizadas cronológicamente con las transcripciones y cada una lleva una breve explicación para un contexto adicional.

Tarea Principal:
Genera un informe detallado en formato Markdown y en castellano, utilizando la información clave de los documentos de referencia. El informe debe centrarse en XXXXXX.

Redacta un informe muy extenso y detallado estructurando y organizando toda la información relevante presente en los documentos que te he proporcionado sobre XXXXX, centrándote en los siguientes aspectos y expandiendo cada uno de ellos en profundidad utilizando los documentos proporcionados: 

-
-
-

Explica paso a paso todas las pruebas realizadas y los comandos ejecutados.

Detalla los conceptos aprendidos.

Todo lo anterior debe ser explicado utilizando toda la información de los documentos proporcionados, ambos transcripts y el pdf con los screenshots de la terminal.

Directrices de Estilo y Formato:

Identificación de Fuentes al Inicio: El informe **DEBE** comenzar con una sección clara que liste los nombres **exactos** de todos los documentos PDF utilizados como referencia. Esta sección debe ser la **primera línea visible** del informe. Éste listado de los documentos utilizados para hacer el informe tiene que ser la única referencia a documentos externos, no me incluyas ninguna otra fuente. Formato: `Documentos de Referencia: "NombreDoc1.pdf", "NombreDoc2.pdf"`

Jerarquía de Títulos: Utiliza títulos y subtítulos (#, ##, ###, etc.) para crear una estructura lógica, clara y fácil de seguir.

Listas: Emplea listas con viñetas para desglosar conceptos y ejemplos.

Tablas Markdown: Utiliza tablas si consideras que la información se beneficia de una presentación tabular para mayor claridad y comparación.

Negrita: Usa negritas para destacar términos clave y conceptos importantes.

Explicación de Comandos: Para cada comando de terminal, explica de forma clara y exhaustiva su sintaxis, cada uno de sus elementos o parámetros (obligatorios y opcionales), el porqué de la acción, el cómo se realiza y su objetivo. Es crucial no incluir el usuario de la terminal (ej., user@singular1). La explicación debe conectar el comando directamente con el contexto del ejercicio o paso específico que se está demostrando en los screenshots.

Riqueza y Profundidad Informativa: El informe debe ser **exhaustivo y altamente técnico**, integrando la información del transcript con los detalles visuales y las explicaciones de los screenshots. Cada concepto debe ser desarrollado con la máxima profundidad, utilizando todos los detalles, resultados y ejemplos disponibles en ambos documentos.

Vocabulario Técnico Consistente: Mantén el vocabulario técnico de ciberseguridad original, conservando los términos en inglés de la jerga (ej., Bug Bounty, Exploit, 0-day, DevSecOps, SSDLC, Data Leaks, Ransomware, Phishing, Insider, APT, DDoS, Malware, etc.), incluso si el texto principal está en español.

Agrupación Lógica: Agrupa la información relacionada para evitar redundancias y mejorar la claridad y el flujo del documento.

Comprensibilidad: El informe debe ser fácil de entender, permitiendo repasar el contenido de la clase sin necesidad de volver a ver el vídeo original.

Ampliación (Opcional): Puedes desarrollar o ampliar ligeramente algunos temas o conceptos utilizando la información ya presente en los documentos de referencia si eso ayuda a la comprensión general, siempre que sea relevante y no genere repetición innecesaria.

PROHIBICIÓN ESTRICTA DE CITAS Y ENLACES EXTERNOS: El informe **NO DEBE INCLUIR BAJO NINGÚN CONCEPTO** citas textuales, referencias numéricas a fuentes (), hipervínulos, URLs, nombres de sitios web, software de transcripción (ej. 'Minutes AI'), o cualquier otro tipo de referencia o enlace a fuentes externas, ni dentro del texto ni al final, con la excepción de la Identificación de Fuentes al Inicio, listando los nombres **exactos** de todos los documentos PDF utilizados como referencia. Toda la información debe ser parafraseada y presentada como parte del contenido original generado, basándose **exclusivamente** en los documentos proporcionados.

Formato de Salida: El resultado debe ser texto Markdown directamente, sin ningún tipo de contenedor (canvas, documento inmersivo, etc.).

Revisión Final: Antes de generar la respuesta, verifica que **no haya ninguna forma de citación o enlace externo** presente en el informe (excepto la Identificación de Fuentes al Inicio, listando los nombres **exactos** de todos los documentos PDF utilizados como referencia).

----------------------------------------------------------------------------------------------------------------------------------------------------

# Prompt Maestro para el Análisis de PDF

### Rol y Tarea Principal

Actúa como un experto en ciberseguridad, un profesional en la organización de información y un educador especializado. Tu tarea es doble: primero, analizar y extraer todos los detalles relevantes del documento que te proporcionaré, y segundo, redactar un informe exhaustivo, técnico y didáctico, reestructurando toda la información extraída según las directrices que te daré a continuación. El informe no debe ser un resumen, sino una reestructuración completa y detallada de todo el contenido, incluyendo descripciones de imágenes y pasos a seguir.

---

### Fases de Ejecución

1.  **Fase de Análisis y Extracción:** Lee con atención todo el contenido del documento, incluyendo el texto y las capturas de pantalla. Extrae los siguientes elementos para su uso en el informe:
    * **"NombreExactoDelDocumento":** El nombre del archivo.
    * **"TemaPrincipal":** El tema central de la clase.
    * **"ConceptosClave":** Identifica y extrae las definiciones y principios fundamentales del tema.
    * **"ProcedimientosPracticos":** Localiza y desglosa cada procedimiento paso a paso, prestando especial atención a las acciones, los menús, las ventanas de configuración y las capturas de pantalla que los ilustran.
    * **"ConclusionesDetalladas":** Analiza la información para identificar las conclusiones clave, los beneficios de seguridad y los puntos importantes de aprendizaje mencionados al final del material.

2.  **Fase de Generación del Informe:** Usando la información extraída, redacta el informe siguiendo este esqueleto y las directrices de estilo. Cada sección debe ser extremadamente detallada, sin escatimar en explicaciones para asegurar la máxima comprensión.

---

### Esqueleto y Directrices del Informe

* **Identificación de Fuentes al Inicio:** El informe **DEBE** comenzar con una sección clara que liste el nombre exacto del documento utilizado. Formato: `Documentos de Referencia: "NombreExactoDelDocumento"`
* **Título Principal:** Usa un título descriptivo y conciso (ej., `# Informe Técnico: [TemaPrincipal]`).

### 1. Resumen Ejecutivo
Redacta un resumen breve y preciso que introduzca el tema y los puntos clave que se abordarán en el informe.

### 2. Conceptos Fundamentales
Explica los "ConceptosClave" que extrajiste. Para cada concepto, proporciona una definición clara y el contexto en el que se usa, sin simplificar en exceso. Utiliza listas con viñetas para una mejor organización.

### 3. Procedimientos Prácticos
Detalla los "ProcedimientosPracticos" de forma exhaustiva. Explica cada paso en profundidad, describiendo la acción, el porqué de la misma, y el resultado esperado. Incluye la referencia a la existencia de capturas de pantalla para guiar la acción, como "tal como se muestra en la captura de pantalla".
    * **Explicación de Comandos:** Para cualquier comando de terminal, explica su sintaxis, sus elementos y su propósito en detalle. **NO** incluyas el usuario de la terminal.

### 4. Conclusiones y Puntos Clave
Esta sección debe ser completa y reflexiva. No te limites a un simple resumen. Utiliza los "ConclusionesDetalladas" extraídas para desglosar los siguientes puntos:
    * **Importancia y Beneficios de Seguridad:** Explica la importancia del tema en la ciberseguridad y las ventajas que aporta.
    * **Puntos de Aprendizaje Clave:** Enumera los conceptos más importantes que se aprendieron en la clase.
    * **Relevancia Técnica:** Describe la relevancia de los procedimientos aprendidos en un entorno profesional.

---

### Directrices de Formato Adicionales

* **Jerarquía de Títulos:** Utiliza títulos y subtítulos (`#`, `##`, `###`) para una estructura lógica.
* **Listas y Tablas:** Emplea listas con viñetas y tablas Markdown cuando la información se beneficie de una presentación organizada.
* **Negrita:** Usa negritas para destacar términos clave y conceptos.
* **Vocabulario Técnico Consistente:** Mantén el vocabulario técnico de ciberseguridad original en inglés (ej., `Active Directory`, `DNS Server`).
* **Agrupación Lógica:** Agrupa la información relacionada para mejorar la claridad y el flujo.
* **Prohibición Estricta de Referencias Externas:** El informe NO DEBE INCLUIR citas textuales, referencias numéricas, hipervínculos, URLs o nombres de sitios web, con la única excepción de la "Identificación de Fuentes" al inicio.
* **Formato de Salida:** El resultado debe ser texto Markdown.


----------------------------------------------------------------------------------------------------------------------------------------------------


En referencia al XXXXXX, está genial, me encanta, pero hay una cosa que puedes hacer sin modificar el contenido: deja la primera frase del documento de referencia, pero quita el resto de citas y referencias a los documentos fuente pero sin modificar nada más, dame el documento exactamente igual que antes excepto las citas. ej., ([cite: 139], [cite_start]).

----------------------------------------------------------------------------------------------------------------------------------------------------


En relación con el informe que me acabas de dar sobre XXXXXXX, quiero que seas más preciso y me des mas información, utiliza los documentos que te he dado para que el informe sea mucho más rico en información.