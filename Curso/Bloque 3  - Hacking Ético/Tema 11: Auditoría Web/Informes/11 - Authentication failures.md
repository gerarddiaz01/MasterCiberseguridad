Documentos de Referencia: "AWEB - Authentication Failures.pdf"

# Informe Técnico: Fallos en la Autenticación y Ataques de Fuerza Bruta

### 1. Resumen Ejecutivo
Este informe detalla las vulnerabilidades y las pruebas de seguridad relacionadas con los fallos de autenticación en aplicaciones web. Se centra en dos tipos de ataques principales: la fuerza bruta y el _password spraying_. Se explican las herramientas, procedimientos y metodologías para llevar a cabo estas pruebas de manera controlada en entornos de laboratorio, como la aplicación DVWA. Además, se abordan las estrategias de mitigación para estas vulnerabilidades y la importancia de implementar políticas de contraseñas robustas como una medida de seguridad fundamental.

---

### 2. Conceptos Fundamentales
* **Ataque de Fuerza Bruta (_Brute Force Attack_):** Consiste en la ejecución de múltiples intentos de autenticación contra una única cuenta de usuario, utilizando un diccionario de contraseñas. El objetivo es adivinar la contraseña correcta de un usuario conocido. La herramienta más utilizada para esta tarea es **Burp Suite** con su funcionalidad **Intruder**. La mitigación principal para este tipo de ataque es el bloqueo de la cuenta del usuario tras un número limitado de intentos fallidos, generalmente entre 3 y 5.

* **Ataque de _Password Spraying_:** A diferencia de la fuerza bruta, este ataque ejecuta múltiples intentos de autenticación utilizando una única contraseña conocida contra una lista de usuarios diferentes. Este método es eficaz cuando se sospecha que los usuarios pueden estar utilizando contraseñas comunes o por defecto. Al igual que con el ataque de fuerza bruta, la herramienta más conocida para realizarlo es **Burp Suite Intruder**. La mitigación en este caso se centra en el bloqueo de la dirección IP de origen, ya que las peticiones provienen de una única fuente.

* **Política de Contraseñas (_Password Policy_):** Es un conjunto de reglas que una contraseña debe cumplir para ser aceptada en una aplicación. Su propósito es evitar el uso de credenciales débiles o predecibles. Estas políticas son una medida de seguridad interna y suelen incluir reglas sobre la **longitud mínima**, la **complejidad** (combinación de mayúsculas, minúsculas, números y caracteres especiales), la **caducidad periódica** y la **prohibición de reuso** de contraseñas anteriores.

---

### 3. Procedimientos Prácticos
Para demostrar los ataques de fuerza bruta y _password spraying_, se utiliza un entorno de laboratorio con **DVWA (Damn Vulnerable Web Application)** como máquina víctima y **Kali Linux** como máquina de ataque. Se emplea **Burp Suite** para interceptar el tráfico y configurar los ataques.

#### **Ataque de Fuerza Bruta**

1.  **Configuración Inicial:** Se intercepta la petición de inicio de sesión de DVWA utilizando Burp Suite. Para este ejemplo, se intenta iniciar sesión con el usuario conocido **admin** y una contraseña incorrecta.
2.  **Envío a Intruder:** La petición interceptada se envía a la funcionalidad **Intruder** de Burp Suite.
3.  **Configuración de Posiciones (_Positions_):** En la pestaña **Positions**, se limpia la configuración por defecto y se selecciona únicamente el valor del parámetro **password** para que sea el campo a variar en los intentos. Esto se logra seleccionando el valor y haciendo clic en "Add".
4.  **Configuración de Payloads:** En la pestaña **Payloads**, se añaden manualmente las contraseñas a probar, como `root`, `toor`, `admin1`, `admin2`, `admin3`, y `password`.
5.  **Configuración de Redirecciones:** En la pestaña **Settings**, se ajustan las opciones de **Redirections** para que Burp Suite siga las redirecciones en las respuestas del servidor. Esto es crucial, ya que las aplicaciones a menudo redirigen a una página de éxito (_index.php_) cuando la autenticación es correcta y a una página de fallo (_login.php_) en caso contrario. La configuración se establece en "Always" y se activa la opción "Process cookies in redirections".
6.  **Ejecución del Ataque:** Se inicia el ataque y se observa la lista de peticiones y respuestas en la pestaña **Results**. Se analiza la longitud de las respuestas, ya que un cambio significativo en la longitud suele indicar una respuesta diferente del servidor, como una redirección exitosa. Se verifica que la contraseña `password` tiene una longitud de respuesta diferente y redirige a _index.php_, confirmando que es la credencial correcta.

#### **Ataque de _Password Spraying_**

1.  **Configuración Inicial:** Se intercepta una petición de inicio de sesión. En este caso, se asume que la contraseña **password** es la que se va a probar contra múltiples usuarios.
2.  **Envío a Intruder:** La petición se envía a **Intruder**.
3.  **Configuración de Posiciones:** En la pestaña **Positions**, se selecciona y se marca el campo del **nombre de usuario** para que sea el valor a variar.
4.  **Configuración de Payloads:** En la pestaña **Payloads**, se añaden los nombres de usuario a probar, como `root`, `administrator`, `administrador`, `test`, `guest` y `admin`.
5.  **Configuración de Redirecciones:** Al igual que en el ataque de fuerza bruta, se configuran las redirecciones para que Burp Suite siga las respuestas del servidor.
6.  **Ejecución del Ataque:** Se inicia el ataque. Al analizar los resultados, se busca una longitud de respuesta diferente. Se descubre que la longitud de la respuesta para el usuario **admin** es significativamente distinta, lo que indica que se ha logrado la autenticación, ya que el servidor redirige a _index.php_.

---

### 4. Conclusiones y Puntos Clave
* **Limitación de Intentos de Autenticación:** Es crucial limitar los intentos de inicio de sesión a un máximo de 3 a 5 por usuario. Si un usuario falla en el inicio de sesión varias veces, debe ser bloqueado temporalmente.
* **Mitigación de _Password Spraying_:** Para mitigar este tipo de ataque, se debe evitar la exposición de los nombres de usuario registrados en una aplicación sin que el atacante se autentique. Además, el bloqueo de la dirección IP de origen es una medida efectiva para detener múltiples intentos provenientes del mismo atacante.
* **Importancia de las Políticas de Contraseñas:** La implementación de políticas de contraseñas robustas es una de las medidas de seguridad más importantes. Estas políticas evitan el uso de contraseñas débiles o por defecto, dificultando significativamente los ataques de fuerza bruta y _password spraying_ y protegiendo la confidencialidad de los usuarios.
* **Relevancia Técnica:** Este ejercicio demuestra cómo herramientas como **Burp Suite Intruder** permiten a un auditor de seguridad simular ataques para identificar vulnerabilidades en los mecanismos de autenticación. La capacidad de analizar las respuestas del servidor, como los códigos de estado y la longitud de las respuestas, es una habilidad fundamental para determinar la efectividad de las pruebas y la robustez de una aplicación.

---

Documentos de Referencia: AWEB - Authentication Failures.pdf

# Informe Técnico: Autorización, Roles y Vulnerabilidad de Directory Traversal

### 1. Resumen Ejecutivo
Este informe aborda las vulnerabilidades relacionadas con la autorización y el acceso indebido a recursos en servidores web, centrándose en el concepto de roles de usuario y la vulnerabilidad de **Directory Traversal**. Se describen los principios de seguridad clave, como el **Principio de Menor Privilegio (PoLP)** y las **Listas de Control de Acceso (ACL)**. Además, se detalla la vulnerabilidad de Directory Traversal, sus objetivos y su impacto, y se presentan ejemplos de explotación y las estrategias de mitigación necesarias para proteger los sistemas contra este tipo de ataques.

---

### 2. Conceptos Fundamentales
* **Roles de Usuario:** Diferentes roles de usuario deben tener diferentes niveles de acceso a los recursos internos de una organización, ya sea a nivel de infraestructura digital o física. Un rol define el tipo de trabajo y las tareas que un usuario realiza. Los accesos de usuarios no autenticados, autenticados y con privilegios deben ser distintos para garantizar la seguridad.

* **Listas de Control de Acceso (ACL):** Son un mecanismo para implementar la diferenciación de roles. Una ACL identifica qué usuarios están autorizados para acceder a determinados recursos. Estas listas limitan el acceso y pueden ser más o menos permisivas según la sensibilidad del recurso.

* **Principio de Menor Privilegio (PoLP):** Este principio de seguridad establece que a un usuario se le debe conceder el nivel mínimo de privilegios o permisos necesarios para que pueda realizar sus funciones laborales.

* **Directory Traversal:** Es una vulnerabilidad que se produce por una gestión incorrecta de los accesos a recursos internos de un servidor. El objetivo de esta vulnerabilidad es acceder a ficheros y directorios restringidos, que se encuentran fuera de la estructura de la aplicación web, e incluso ejecutar comandos. La ejecución de comandos se realiza con los privilegios del usuario asociado al sitio web (por ejemplo, el usuario `ww-data` en Linux).

---

### 3. Procedimientos Prácticos
La vulnerabilidad de Directory Traversal se puede explotar a través de diversas técnicas. A continuación, se describen los ejemplos de explotación, cada uno ilustrando una forma diferente de manipular las peticiones para acceder a archivos o directorios restringidos.

1.  **Retroceso de Directorios (_Dot-Dot-Slash_):**
    * **Ejemplo:** `Website.tld/resource?view=../../../../Windows/system.in`.
    * **Descripción:** Esta técnica utiliza la secuencia `../` para retroceder en la estructura de directorios del servidor hasta alcanzar la raíz del sistema o un directorio de interés. En este caso, se retrocede desde la ubicación de la aplicación hasta el directorio de Windows para acceder al archivo `system.in`.

2.  **Codificación URL:**
    * **Ejemplo:** `Website.tld/resource?view=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd`.
    * **Descripción:** Esta técnica utiliza la codificación de caracteres en la URL para evadir filtros de seguridad que buscan la secuencia `../`. El carácter `%2e` simboliza un punto (`.`), y `%2f` representa la barra (`/`). El navegador decodifica esta secuencia, permitiendo el retroceso de directorios hasta el archivo `/etc/passwd`, que en sistemas Unix/Linux contiene información sobre los usuarios.

3.  **Acceso Directo a Archivos de Copia de Seguridad:**
    * **Ejemplo:** `Website.tld/resource?view=backup.db`.
    * **Descripción:** A veces, las aplicaciones exponen copias de seguridad de archivos sensibles en directorios accesibles. En este caso, el atacante asume que existe un archivo llamado `backup.db` y lo solicita directamente, lo que puede exponer datos sensibles de la base de datos si el archivo no está protegido adecuadamente.

4.  **Ejecución de Comandos del Sistema:**
    * **Ejemplo:** `Website.tld/scripts/..%5c../opt/bin/bash+pwd`.
    * **Descripción:** Esta técnica combina el retroceso de directorios con la ejecución de comandos. El carácter `%5c` es la codificación URL para la barra invertida (`\`), utilizada en sistemas Windows. Se retrocede en la jerarquía hasta la ruta `/opt/bin/bash` (una consola de comandos en sistemas Linux) para ejecutar el comando `pwd` (imprimir el directorio de trabajo actual). La ejecución de comandos depende de los privilegios del usuario de la aplicación web.

5.  **Null Byte (_%00_)**
    * **Ejemplo:** `Website.tld?filename=../../../../etc/passwd%00.png`.
    * **Descripción:** El **null byte** (`%00`) se utiliza para terminar prematuramente una cadena de caracteres. En este caso, el servidor procesa el nombre del archivo solo hasta el null byte, ignorando la extensión `.png`. Esto permite al atacante acceder a archivos como `/etc/passwd`, eludiendo las validaciones del servidor basadas en la extensión del archivo.

---

### 4. Conclusiones y Puntos Clave
* **Importancia y Beneficios de Seguridad:** Es fundamental identificar, asociar y diferenciar correctamente los roles de los usuarios en una aplicación y en la infraestructura. Esto evita que usuarios con bajos privilegios accedan a información sensible o a recursos que no les corresponden, lo que podría llevar a una mayor vulnerabilidad del sistema. La implementación de **ACLs** y el **Principio de Menor Privilegio** son esenciales para la correcta distribución de recursos y para limitar los daños en caso de un compromiso de cuenta.

* **Mitigaciones Clave para Directory Traversal:** Las dos mitigaciones más importantes para esta vulnerabilidad son:
    1.  **Parametrizar los datos de entrada:** Los datos enviados al servidor deben ser tratados como cadenas de texto, y no como comandos o rutas de archivos. Esto evita que caracteres especiales como `../` o `%00` sean interpretados como comandos.
    2.  **Implementar ACLs:** Las listas de control de acceso deben restringir el acceso a archivos y directorios fuera del alcance de la aplicación web, evitando que cualquier usuario pueda acceder a ficheros del sistema operativo.

* **Relevancia Técnica:** Comprender el **Directory Traversal** y la correcta implementación de roles es crucial en un entorno profesional. Demuestra la importancia de validar y sanear los datos de entrada del usuario, así como de configurar adecuadamente los permisos de acceso en el servidor. Un fallo en la autorización puede llevar a una brecha de seguridad grave, permitiendo al atacante acceder a información crítica y comprometer todo el sistema.

---

Documentos de Referencia: AWEB - Authentication Failures.pdf

# Informe Técnico: Fallos de Autenticación, IDOR y Escalada de Privilegios

### 1. Resumen Ejecutivo
Este informe explora dos vulnerabilidades de seguridad críticas relacionadas con la autorización en aplicaciones web: **Insecure Direct Object References (IDOR)** y la **escalada de privilegios**. Analiza sus definiciones, métodos de explotación, y las herramientas utilizadas, como **Burp Suite Intruder**. Además, detalla las estrategias de mitigación clave para proteger los sistemas y discute los diferentes vectores de ataque que pueden conducir a la escalada de privilegios, como fallos de software, ingeniería social y credenciales débiles.

---

### 2. Conceptos Fundamentales
* **IDOR (_Insecure Direct Object References_):** Una vulnerabilidad que permite a los usuarios acceder directamente a recursos u objetos a los que no deberían tener acceso. Esto sucede porque los recursos a menudo tienen identificadores predecibles o fáciles de adivinar, como números consecutivos o nombres predeterminados. Los recursos afectados carecen de restricciones de acceso o visibilidad, lo que permite a un usuario no autorizado acceder a información o archivos de otros usuarios, incluso si tienen un nivel de privilegio diferente. Para identificar y explotar esta vulnerabilidad, se pueden usar ataques de **fuerza bruta** o **fuzzing**.

* **Escalada de Privilegios:** Se refiere al proceso de obtener acceso no autorizado a un sistema, llevando a cabo acciones o accediendo a recursos que están restringidos para el nivel de usuario actual del atacante. Esto podría incluir la ejecución de comandos o el acceso a archivos y directorios que el usuario no debería poder ver. Para lograr una escalada de privilegios, es fundamental tener un conocimiento profundo del sistema o la aplicación vulnerable y de su infraestructura interna.

---

### 3. Procedimientos Prácticos
Los ataques de **IDOR** y **escalada de privilegios** se pueden llevar a cabo de varias maneras, utilizando diferentes técnicas para explotar las debilidades en los sistemas de autorización.

#### Explotación de IDOR
La vulnerabilidad IDOR se explota al manipular los identificadores de recursos en las URL. La herramienta principal para esto es **Burp Suite Intruder**, que permite a los atacantes usar diccionarios o rangos de números para automatizar la búsqueda de recursos vulnerables. A continuación, se detallan ejemplos comunes de explotación:
* **Identificador Numérico:** Un atacante puede modificar un parámetro como `author=1` para intentar acceder a la información de otros autores cambiando el valor numérico.
* **Identificador por Nombre:** Un atacante puede cambiar un identificador como `user=guest` por otros nombres de usuario por defecto o predecibles para identificar otras cuentas existentes.
* **Números de Documentos:** En un sistema de facturación o documentos, un atacante puede cambiar un número de factura predecible (`invoice=123456`) o un número de documento confidencial (`signedDocument=872631`) para acceder a información de otros usuarios.

#### Vectores de Ataque para la Escalada de Privilegios
La escalada de privilegios puede lograrse a través de varias vías:
* **Compromiso de Cuentas:** Cuando las credenciales son débiles o no están protegidas por políticas de contraseñas robustas o un segundo factor de autenticación, un atacante puede adivinarlas o robarlas para suplantar la identidad del usuario y obtener sus privilegios en el sistema.
* **Vulnerabilidades en el Software:** Los fallos de configuración en las aplicaciones o el uso de versiones obsoletas con vulnerabilidades conocidas pueden ser explotados para elevar los privilegios del atacante.
* **Software Malicioso (_Malware_):** Los programas maliciosos pueden ser enviados, descargados o instalados en los equipos para ejecutar tareas sin el consentimiento del usuario legítimo.
* **Ingeniería Social:** Esta técnica se basa en persuadir a una persona para que realice una acción que no debería. Se utiliza para engañar a los usuarios y que revelen información sensible o instalen _malware_. Los métodos incluyen:
    * **Phishing:** Uso de correos electrónicos para engañar a las víctimas.
    * **Smishing:** Uso de mensajes de texto (SMS) para el mismo propósito.
    * **Llamadas telefónicas:** Haciéndose pasar por una persona de confianza, como un jefe o un banco.

---

### 4. Conclusiones y Puntos Clave
* **Mitigación de IDOR:** La principal medida para mitigar ataques IDOR es asegurarse de que los identificadores de los recursos no sean predecibles o fáciles de adivinar. Además, es crucial establecer reglas de acceso rigurosas para los recursos, garantizando que solo los usuarios a los que les corresponden puedan verlos. Bloquear las direcciones IP que realizan un gran número de peticiones también es una buena práctica para detener estos ataques.

* **Puntos de Aprendizaje Clave:** La escalada de privilegios puede tener una gran variedad de orígenes, desde fallos en las tecnologías de una aplicación hasta la configuración de los permisos de los usuarios en los servidores. Es fundamental implementar **políticas de contraseñas robustas** y **controles de acceso** para proteger la información y los recursos del sistema.

* **Relevancia Técnica:** Comprender las vulnerabilidades IDOR y la escalada de privilegios es esencial en un entorno profesional. Demuestra la importancia de una **validación de entrada exhaustiva**, la **gestión adecuada de los permisos** de los usuarios y el uso de **identificadores de recursos seguros**. Los auditores de seguridad deben ser capaces de identificar estas vulnerabilidades para prevenir brechas de seguridad y proteger los datos sensibles de una organización.