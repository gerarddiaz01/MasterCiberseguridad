Documentos de Referencia: "RE - Fingerprinting _ Nmap.pdf"

# Informe Técnico: Fingerprinting y Escaneo de Redes con Nmap

## 1. Resumen Ejecutivo

Este informe técnico se centra en el **fingerprinting**, una técnica fundamental en ciberseguridad para la evaluación de la infraestructura de red. Detalla las metodologías clave para el descubrimiento de hosts y la identificación de servicios, versiones y sistemas operativos. Se explora en profundidad el uso de la herramienta **Nmap**, abarcando diversos tipos de escaneo como SYN, TCP Connect, ACK, NULL, FIN y XMAS, y se complementa con el análisis de paquetes a nivel de red utilizando **Wireshark**. El objetivo es proporcionar una guía didáctica y técnica para comprender cómo se recopila información sobre una red y cómo se interpretan las respuestas para identificar posibles vulnerabilidades.

## 2. Conceptos Fundamentales

* **Fingerprinting:** Es la técnica de identificar y analizar las características técnicas específicas de un sistema o red. El objetivo principal es crear un perfil completo del objetivo, incluyendo información sobre los hosts, servicios y sus versiones. Esta información es crucial para comprender la infraestructura, identificar posibles puntos débiles y optimizar la gestión de la red.
* **Descubrimiento de Hosts (Host Discovery):** Es el proceso de identificar los hosts activos en una red para entender el alcance de la infraestructura objetivo. Los métodos comunes incluyen:
    * **Ping (ICMP):** Envío de mensajes ICMP para determinar la disponibilidad de los hosts. Este método puede ser menos efectivo si los hosts bloquean las respuestas ICMP.
    * **Descubrimiento ARP:** Identificación de hosts en la misma subred mediante mensajes ARP (Address Resolution Protocol), que asocian direcciones IP con direcciones MAC. Este método es discreto y menos propenso a ser detectado por sistemas de defensa.
    * **Escaneo de Subred:** Búsqueda de hosts escaneando rangos de direcciones IP.
* **Descubrimiento de Servicios y Versiones:** Es la identificación de servicios y sus versiones en un host para comprender su funcionalidad y detectar vulnerabilidades asociadas. Las técnicas incluyen:
    * **Protocol Identification:** Análisis de protocolos para determinar la funcionalidad y riesgos de los servicios.
    * **Banner Grabbing:** Obtención de información sobre un servicio y su versión a través de los banners de respuesta que envía al establecer una conexión.
    * **Active Fingerprinting:** Interacción directa con los servicios para obtener información más precisa sobre sus versiones y configuraciones.
* **Análisis de Vulnerabilidades (Vulnerability Analysis):** Su objetivo es identificar debilidades potenciales en los servicios y sistemas descubiertos durante el proceso de fingerprinting. Una técnica común es la **comparación de versiones**, que consiste en cotejar las versiones de los servicios con bases de datos de vulnerabilidades conocidas para determinar si son explotables.
* **Escaneos (Scanning):** Son procesos que exploran activamente una red para recopilar información sobre dispositivos, puertos y servicios disponibles. Funcionan enviando paquetes de datos y analizando las respuestas para identificar dispositivos activos, puertos abiertos y servicios en ejecución.

## 3. Procedimientos Prácticos

### 3.1. Uso de Nmap para el Escaneo de Redes

El material instruye sobre el uso de la herramienta de línea de comandos **Nmap (Network Mapper)**, que se encuentra preinstalada en el sistema operativo Kali Linux. La ayuda de Nmap es accesible a través del comando `nmap` sin argumentos, y su sintaxis general es `nmap [Scan Type(s)] [Options] {target specification}`.

---

#### 3.1.1. Descubrimiento de Hosts

Para identificar los hosts activos en una red, se puede utilizar el **Ping Scan** con la opción `-sn`. Este comando envía paquetes para determinar si un host está en línea sin realizar un escaneo de puertos completo.

* **Comando:** `sudo nmap -sn 192.168.1.0/24`
* **Explicación:**
    * `sudo`: Permisos de superusuario, necesarios para ciertos tipos de escaneo.
    * `nmap`: Llama a la herramienta Nmap.
    * `-sn`: Opción para realizar un Ping Scan, que deshabilita el escaneo de puertos.
    * `192.168.1.0/24`: El rango de direcciones IP a escanear, en este caso, una subred completa.
* **Resultado:** El comando devuelve una lista de los hosts que están activos en la red, junto con su dirección IP y la dirección MAC. La latencia de la respuesta también se muestra.

---

#### 3.1.2. Escaneo de Puertos y Análisis con Wireshark

El documento demuestra cómo realizar y analizar diversos tipos de escaneo de puertos utilizando Nmap en conjunto con **Wireshark**, una herramienta para la captura y análisis de tráfico de red.

* **Escaneo SYN (`-sS`):** También conocido como "Half-Open Scan". Es sigiloso porque no completa la conexión TCP.
    * **Comando:** `sudo nmap -sS 192.168.1.103`.
    * **Proceso:** Se envía un paquete SYN. Si el puerto está abierto, el objetivo responde con un paquete SYN/ACK. Si está cerrado, responde con un RST/ACK. La conexión se cierra inmediatamente después de la respuesta, de ahí su naturaleza "half-open". Si no hay respuesta, el puerto se considera filtrado.
    * **Análisis con Wireshark:** Se puede observar el intercambio de paquetes SYN y SYN/ACK que confirma un puerto abierto, o el paquete RST para un puerto cerrado, como se muestra en la captura de pantalla del flujo TCP Stream del puerto 21.

* **Escaneo TCP Connect (`-sT`):** Un método básico y detectable que establece una conexión TCP completa con el objetivo.
    * **Comando:** `nmap -sT 192.168.1.104`.
    * **Proceso:** El atacante envía un SYN, la víctima responde con un SYN/ACK, y el atacante completa la conexión con un ACK. Si el puerto está cerrado, la víctima responde con un RST.
    * **Análisis con Wireshark:** Se visualiza la secuencia completa de la conexión de tres vías (SYN, SYN/ACK, ACK).

* **Escaneo ACK (`-sA`):** Envía paquetes con el flag ACK activado para determinar si los puertos están filtrados por un firewall.
    * **Comando:** `sudo nmap -sA 192.168.1.103`.
    * **Proceso:** Si se recibe un paquete RST, el puerto está sin filtrar (unfiltered). Si no se recibe respuesta, el puerto está filtrado (filtered).
    * **Análisis con Wireshark:** Se puede observar la ausencia de respuestas para los puertos filtrados y las respuestas RST para los puertos no filtrados.

* **Escaneos NULL, FIN y XMAS:** Estos escaneos son sigilosos y buscan evadir firewalls. La interpretación de sus respuestas es la misma para los tres:
    * **No se recibe respuesta:** El puerto está abierto o filtrado.
    * **Se recibe un paquete RST:** El puerto está cerrado.
    * **Comandos:** `sudo nmap -sN 192.168.1.103` (NULL), `sudo nmap -sF 192.168.1.103` (FIN), y `sudo nmap -sX 192.168.1.103` (XMAS).
    * **Análisis con Wireshark:** Se examinan los encabezados de los paquetes. En el escaneo NULL, no hay flags activadas. En el FIN, solo el flag FIN está activado. En el XMAS, los flags FIN, PSH y URG están activados simultáneamente, creando el efecto de "luces de navidad" que le da su nombre.

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad

El **fingerprinting** es una fase crítica en cualquier evaluación de seguridad, ya que permite obtener un perfil completo de la infraestructura de red, identificar puntos débiles y planificar estrategias de ataque o defensa. Los escaneos son esenciales para comprender la topología de la red, identificar servicios y puertos abiertos, y evaluar la seguridad general. La elección del tipo de escaneo depende de factores como el nivel de sigilo requerido y las configuraciones de seguridad del objetivo.

### 4.2. Puntos de Aprendizaje Clave

* **Nmap** es una herramienta poderosa y versátil para el escaneo de redes y el descubrimiento de hosts y servicios, esencial para cualquier profesional de la ciberseguridad.
* La página oficial de Nmap ofrece una vasta cantidad de recursos, documentación y tutoriales para aprender sobre la herramienta y sus capacidades.
* **Wireshark** es una herramienta fundamental para analizar el tráfico a nivel de paquete, permitiendo visualizar y comprender cómo funcionan los escaneos en un nivel más profundo.
* La **correlación** entre los resultados de Nmap y los datos capturados en Wireshark permite validar la efectividad de las técnicas de escaneo y obtener una comprensión más completa de la actividad de la red.

### 4.3. Relevancia Técnica

Los procedimientos detallados en este informe son de gran utilidad en un entorno profesional. La capacidad de realizar escaneos de manera efectiva y de analizar las respuestas a nivel de paquete es una habilidad fundamental para las evaluaciones de seguridad, las pruebas de penetración y la administración de redes. El uso de Nmap y Wireshark en conjunto permite no solo identificar vulnerabilidades, sino también entender la lógica subyacente de las interacciones de red, lo cual es invaluable para detectar anomalías y reforzar las defensas de la infraestructura.