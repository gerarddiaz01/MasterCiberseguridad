# Informe Técnico: Validación de Entrada de Datos y Cross-Site Scripting (XSS)

**Documentos de Referencia:** "AWEB - Input Validation\_ XSS Scripting.pdf"

## 1. Resumen Ejecutivo

Este informe aborda la **Validación de Entrada de Datos (Input Validation)** como práctica esencial en la ciberseguridad web y su papel crucial en la prevención de ataques de inyección, específicamente el **Cross-Site Scripting (XSS)**. Se detalla la importancia de la validación a nivel de **cliente** y **servidor**, se explican las metodologías de seguridad como las **Listas Blancas (Allowlists)**, y se desglosan los tres tipos principales de XSS: **Reflejado**, **Almacenado** y **Basado en DOM**. Finalmente, se documentan procedimientos prácticos para la explotación y el *bypass* de filtros de seguridad en entornos de laboratorio (DVWA y PortSwigger).

---

## 2. Conceptos Fundamentales

### Validación de Entrada de Datos (Input Validation)
La validación de entrada de datos es una práctica fundamental cuyo objetivo es asegurar que solo los datos **esperados, correctos y seguros** sean procesados por una aplicación. Es el proceso de verificar que la información que recibe una aplicación web desde una fuente externa, como un usuario, cumple con las reglas y el formato esperado.

* **Importancia:** Es crucial para la **Protección contra ataques**, previniendo vulnerabilidades como la **Inyección SQL (SQL Injection)** y el **Cross-Site Scripting (XSS)**. También garantiza la **Integridad de los datos** y un **Funcionamiento correcto** de la aplicación, evitando fallos o comportamientos impredecibles.
* **Ubicación de la Validación:**
    * **Lado del Cliente (Navegador):** Se realiza con lenguajes como **JavaScript** antes de que los datos se envíen al servidor. Es rápida y mejora la experiencia de usuario, pero **no es segura**, ya que un atacante puede evadirla fácilmente con herramientas como un proxy web (ej. Burp Suite).
    * **Lado del Servidor:** Es la validación **más crítica y obligatoria** para la seguridad. Se lleva a cabo una vez que los datos han sido recibidos, asegurando que se realiza la verificación sin importar cómo se manipuló la petición en el cliente.

### Técnicas de Implementación de Validación
Existen varias técnicas recomendadas para una validación efectiva:

* **Validadores de Tipo de Datos:** Aseguran que el dato recibido corresponde al tipo esperado (ej. entero, cadena de texto, booleano).
* **Rango de Valores:** Comprueban que un valor numérico o de fecha se encuentra dentro de un rango permitido (ej. una cantidad entre 1 y 100).
* **Expresiones Regulares (Regular Expressions):** Herramienta potente para validar formatos específicos como **correos electrónicos** o **códigos postales**.
* **Listas Negras (Denylists) vs. Listas Blancas (Allowlists):**
    * **Listas Negras:** Definen caracteres o patrones **no permitidos** (ej. `script`, `alert`). **No son recomendables** porque son fáciles de evadir mediante variaciones o codificaciones.
    * **Listas Blancas:** Definen caracteres o formatos que **sí están permitidos** y se consideran seguros. Es la técnica **más segura y recomendada**, ya que rechaza automáticamente cualquier cosa que no esté explícitamente en la lista.
* **Normalización (Normalization):** Convierte los datos de entrada a un formato estándar o **"canónico"** para su posterior procesamiento. Esto asegura que el texto se trate solo como **texto plano**, neutralizando la inyección de código (ej. convierte `<script>` a `&lt;script&gt;`).

---

## 3. Cross-Site Scripting (XSS)

El XSS es una vulnerabilidad de tipo **inyección** que permite a un atacante inyectar **código malicioso (generalmente JavaScript)** en una página web que será ejecutado por el navegador de la víctima.

* **Objetivos del Ataque XSS:**
    * **Robo de cookies:** Para suplantar la identidad del usuario.
    * **Redirección a sitios maliciosos:** Para robar credenciales (phishing).
    * **Manipulación de la interfaz:** Para que el usuario envíe información sensible a un servidor del atacante.

### Tipos de Cross-Site Scripting

| Tipo de XSS | Mecanismo de Inyección | Persistencia | Riesgo |
| :--- | :--- | :--- | :--- |
| **Reflejado (Reflected)** | El *payload* se envía en la URL de una petición HTTP (GET) y el servidor lo "refleja" inmediatamente en la respuesta HTML sin validación. | No Persistente | Requiere **ingeniería social** para que la víctima haga clic en el enlace malicioso. |
| **Almacenado (Stored)** | El *payload* se almacena de forma **persistente** en el servidor (ej. base de datos). | Persistente | Es el **más peligroso**. Se ejecuta automáticamente para **todos los usuarios** que visitan la página vulnerable. |
| **Basado en DOM (DOM-based)** | La vulnerabilidad reside en el **código JavaScript del cliente**. El *payload* es procesado y ejecutado por el **DOM** del navegador sin llegar al servidor. | No Persistente | Requiere que la víctima haga clic en un enlace malicioso, similar al reflejado. |

### *Payloads* de Testeo Comunes

El *payload* más sencillo para confirmar la ejecución de código es `[script]alert("XSS")[/script]` (donde `[` y `]` representan `<` y `>`). Sin embargo, los filtros de seguridad a menudo lo bloquean, por lo que se utilizan alternativas:

* **Sin la etiqueta *script***: `[img src=x onerror=alert("XSS")]`. El evento `onerror` se dispara al fallar la carga de la imagen.
* **Con etiquetas de eventos**: `[svg onload=alert(1)]` o `[body onload=alert(1)]`. El evento `onload` ejecuta el código al cargar el elemento.

---

## 4. Procedimientos Prácticos

### 4.1. Explotación de XSS Reflejado (DVWA)

#### **Nivel de Seguridad: Medium**
El código fuente en este nivel utiliza la función `str_replace('<script>', '', $_GET['name'])` para buscar y eliminar la cadena `<script>` en minúsculas. Esta es una defensa débil de lista negra.

| Paso | Acción | Propósito / Resultado |
| :--- | :--- | :--- |
| 1. | Configurar DVWA a nivel **"medium"** y navegar a la sección XSS Reflejado. | Se confirma que la entrada se refleja en el mensaje (ej. "Hello test"). |
| 2. | Intentar el *payload* básico: `<script>alert(1)</script>`. | Falla, ya que la función `str_replace` elimina la cadena, dejando un mensaje como "Hello alert(1)". |
| 3. | **Bypass** del filtro (evasión de la lista negra): Usar el *payload*: `<SCRIPT>alert(1)</SCRIPT>`. | La función `str_replace` es sensible a mayúsculas y no detecta la cadena en mayúsculas. El navegador ejecuta el *script* y se muestra una ventana emergente de alerta, confirmando la vulnerabilidad. |

#### **Nivel de Seguridad: High**
El código fuente en este nivel utiliza una **Expresión Regular (Regex)** insensible a mayúsculas y minúsculas con la línea `preg_replace('/<(.*)s(.*)c(.*)r(.*)i(.*)p(.*)t/i', '', $_GET['name'])`. Este filtro robusto bloquea la palabra "script" en cualquier combinación de mayúsculas y minúsculas.

| Paso | Acción | Propósito / Resultado |
| :--- | :--- | :--- |
| 1. | Cambiar DVWA a nivel **"high"**. | Preparar el entorno para una defensa más robusta. |
| 2. | Intentar el *payload* anterior: `<SCRIPT>alert(1)</SCRIPT>`. | Falla, ya que el `preg_replace` con la bandera `i` detecta y reemplaza la cadena. |
| 3. | **Bypass** del filtro: Usar un *payload* que no contenga la palabra *script*. Por ejemplo: `[svg onload=alert(1)]`. | El servidor no tiene un filtro para la etiqueta `[svg]`. El atributo de evento `onload` se ejecuta al cargar la etiqueta, mostrando la alerta y explotando la vulnerabilidad. |

### 4.2. Explotación de XSS Almacenado (DVWA)

#### **Nivel de Seguridad: Medium (Análisis del Código)**
En este nivel, el campo **Name** es similar al XSS Reflejado de nivel medio (usa `str_replace` para `<script>`), haciéndolo vulnerable a *payloads* con mayúsculas. El campo **Message** es más seguro, ya que utiliza la función `htmlspecialchars()`.

* **Función `htmlspecialchars()`:** Es la medida más efectiva para prevenir XSS, ya que convierte caracteres especiales como `<` y `>` a sus entidades HTML (`&lt;` y `&gt;`). Esto asegura que el código inyectado se muestre como **texto plano** en el navegador y no se ejecute.

| Paso | Acción | Propósito / Resultado |
| :--- | :--- | :--- |
| 1. | Usar Burp Suite para **interceptar** la petición POST. | El campo **Name** tiene una restricción de longitud del lado del cliente que debe ser evadida. |
| 2. | En la petición interceptada, modificar el parámetro `txtName` para incluir un *payload* que evada la lista negra sensible a mayúsculas: `txtName=test<SCRIPT>alert(name+medium)</SCRIPT>...`. | El *payload* se inyecta en el campo **Name**, se almacena en la base de datos y se ejecuta al cargar la página. Se demuestra la persistencia de la vulnerabilidad almacenada. |

#### **Nivel de Seguridad: High**
Ambos campos (`Name` y `Message`) utilizan funciones de saneamiento más robustas (como `htmlspecialchars` o *regex* más complejas). Se requiere un *payload* creativo que no utilice las palabras clave filtradas.

| Paso | Acción | Propósito / Resultado |
| :--- | :--- | :--- |
| 1. | Interceptar la petición POST con Burp Suite. | Se requiere una inyección para evadir las restricciones de longitud y los filtros robustos. |
| 2. | Inyectar un *payload* alternativo sin *script* en el parámetro `txtName`. Por ejemplo: `txtName=test<body onload=alert(1)>...`. | El servidor no filtra esta etiqueta o evento. El *payload* se almacena y, al recargar la página, el navegador interpreta la etiqueta `[body]` con el evento `onload`, ejecutando la alerta. |

### 4.3. Explotación de XSS Basado en DOM (PortSwigger Lab)

La vulnerabilidad reside en la función de JavaScript `document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">')`, donde `query` es la entrada no saneada extraída de `location.search` (la URL). El *script* está inyectando directamente la entrada del usuario dentro del atributo `src` de una etiqueta `[img]`.

| Paso | Acción | Propósito / Resultado |
| :--- | :--- | :--- |
| 1. | Analizar el código para identificar el **punto de inyección**. | Se confirma que la entrada (`query`) se usa sin saneamiento dentro de un *string* de la etiqueta `[img src="..."]`. |
| 2. | **Bypass** del atributo `src`: Insertar el *payload* en el campo de búsqueda: `"><script>alert(1)</script>`. | La cadena `"` **cierra** el atributo `src` de la imagen. El `>` **cierra** la etiqueta `[img]`. El resto del *payload* (`<script>alert(1)</script>`) es interpretado como código HTML/JavaScript válido por el navegador y se ejecuta. |
| 3. | **Alternativa de Bypass:** Usar un *payload* de evento: `"><body onload=alert(1)>`. | Confirma que, una vez que se "escapa" del atributo `src` de la imagen, se puede inyectar cualquier código ejecutable. |

---

## 5. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La **Validación de Entrada de Datos** es el pilar fundamental de la seguridad web. Su correcta implementación previene ataques de inyección críticos como **SQL Injection** y **XSS**. Al validar las entradas de manera estricta, se detectan los intentos de ataque en las primeras etapas, protegiendo tanto la confidencialidad de la información (ej. robo de *cookies* de sesión) como la integridad de los datos y la reputación de la aplicación.

### Puntos de Aprendizaje Clave
* **La validación en el servidor es obligatoria y crítica:** La validación del lado del cliente debe usarse solo para la experiencia de usuario, pero nunca como medida de seguridad, ya que es trivial de evadir.
* **Listas Blancas vs. Listas Negras:** El enfoque de **Lista Negra** (`str_replace` o `strip_tags`) es débil y siempre será evadido por atacantes creativos (ej. mayúsculas/minúsculas o *payloads* alternativos). La estrategia más segura es la **Lista Blanca (Allowlists)**, que define explícitamente qué es aceptable.
* **El `alert` es solo una prueba de concepto (PoC):** Un *alert* demuestra la existencia de la vulnerabilidad, pero un ataque real puede robar *cookies* de sesión o redirigir al usuario.
* **La defensa ideal es la codificación de salida:** Funciones como `htmlspecialchars()` (codificación de salida) convierten el código ejecutable en texto inofensivo, asegurando que la entrada del usuario se muestre como texto plano.

### Relevancia Técnica
Los procedimientos aprendidos son de vital importancia en la auditoría de seguridad (*pentesting*) de aplicaciones web:
1.  **Identificación de la Fuente:** Es crucial determinar si la vulnerabilidad es **Reflejada** (petición HTTP), **Almacenada** (base de datos) o **Basada en DOM** (código JavaScript del cliente), ya que la mitigación y la explotación son distintas.
2.  **Análisis de Filtros:** La capacidad de revisar el código fuente (como en DVWA) o inspeccionar la respuesta (con herramientas como Burp Suite) permite a un profesional identificar la debilidad exacta (ej. un `str_replace` sensible a mayúsculas o un filtro `preg_replace` robusto) y diseñar un ***payload* de evasión** específico.
3.  **Evitar la Fragilidad del Cliente:** La explotación del **XSS Almacenado** a nivel medio demostró la necesidad de usar herramientas como Burp Suite para saltarse las validaciones de longitud del lado del cliente, confirmando que estas no son una barrera de seguridad efectiva.
4.  **Conciencia sobre Funciones Vulnerables:** Se subraya el peligro de inyectar datos de `location.search` sin saneamiento a través de métodos como `document.write()` o `innerHTML`, ya que estas funciones son *sinks* comunes para el **XSS Basado en DOM**.