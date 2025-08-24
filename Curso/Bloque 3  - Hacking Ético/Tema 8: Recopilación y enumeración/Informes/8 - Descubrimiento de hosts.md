Documentos de Referencia: "RE - Descubimiento de hosts.pdf"

# Informe Técnico: Descubrimiento de Hosts y Protocolos de Red

## 1. Resumen Ejecutivo
Este informe técnico profundiza en el concepto de **descubrimiento de hosts**, una etapa crucial en la fase de reconocimiento de redes. Aborda los fundamentos de los protocolos de red esenciales como **ARP**, **DNS**, **ICMP**, **TCP** y **UDP** para sentar las bases de la comunicación. A través de ejemplos prácticos y la manipulación de herramientas como **Nmap**, **ARP-Scan**, **Netdiscover** y la creación de un script con **Python y Scapy**, se explican las diversas técnicas de identificación de máquinas activas. El informe concluye destacando la importancia de estos conocimientos para la auditoría y seguridad de redes, proporcionando una base sólida para profesionales del sector.

---

## 2. Conceptos Fundamentales

### 2.1. Conceptos Básicos de Redes
* **Red de computadoras:** Un conjunto de computadoras que comparten recursos. Se comunican utilizando protocolos comunes a través de interconexiones digitales.
* **Topologías de red:** Las redes pueden tener diferentes estructuras, como Anillo, Malla, Estrella, Conexión Total, Línea, Árbol y Bus. La topología de estrella es común en redes domésticas, donde el router actúa como un punto central.

### 2.2. Protocolos de Red Esenciales
* **ARP (Address Resolution Protocol):** Es un protocolo de comunicaciones de la capa de enlace de datos. Su función es encontrar la dirección de hardware (dirección MAC) que corresponde a una dirección IP específica en una red local. Una máquina envía un mensaje ARP a toda la red preguntando por la dirección MAC de una IP, y el host con esa IP responde con su MAC.
* **DNS (Domain Name System):** Un sistema de nombres jerárquico y distribuido que traduce nombres de dominio (como wikipedia.org) a direcciones IP. Funciona como una "agenda telefónica" para internet, eliminando la necesidad de memorizar direcciones IP numéricas. Los registros DNS de tipo A asocian dominios a IPv4, y los de tipo AAAA a IPv6.
* **ICMP (Internet Control Message Protocol):** Un protocolo de apoyo que compensa las deficiencias del protocolo IP al proporcionar un mecanismo para que los dispositivos de red comuniquen información vital, como la conectividad y el estado de la red. Los mensajes ICMP más comunes son el **Echo Request** y el **Echo Reply**, que se utilizan en el comando `ping`.
* **TCP (Transmission Control Protocol):** Un estándar de comunicación orientado a la conexión que garantiza la entrega exitosa y confiable de datos a través de una red. Antes de enviar datos, establece una conexión mediante un proceso de "handshake". Sus ventajas incluyen la confiabilidad, el control de flujo y la verificación de errores.
* **UDP (User Datagram Protocol):** Un protocolo de comunicación sin conexión y liviano. A diferencia de TCP, no garantiza la entrega ni el orden de los mensajes, lo que lo hace ideal para aplicaciones en tiempo real como streaming de video y juegos en línea. No tiene la sobrecarga de control de flujo o manejo de conexiones.

### 2.3. Host Discovery
* **Definición:** Es una de las primeras fases del reconocimiento de red. Su propósito es reducir un gran conjunto de direcciones IP a una lista más pequeña de hosts activos o de interés, para luego enfocar el escaneo de puertos en esos hosts.
* **Propósitos:**
    * **Identificación de dispositivos activos:** Permite saber qué máquinas están en línea en una red.
    * **Mapeo de la topología:** Ayuda a entender la disposición física y lógica de la red.
    * **Preparación para auditorías:** Es un paso preliminar para las etapas posteriores de una auditoría de seguridad.
* **Técnicas:** Existen varias técnicas para el descubrimiento de hosts, incluyendo **TCP SYN Ping**, **TCP ACK Ping**, **UDP Ping**, **ICMP Ping**, **IP Protocol Ping** y **ARP Scan**.

---

## 3. Procedimientos Prácticos

A continuación, se detallan los procedimientos para el descubrimiento de hosts utilizando herramientas de línea de comandos en un entorno de laboratorio con Kali Linux.

### 3.1. Práctica de ICMP Ping
Esta técnica utiliza Nmap para enviar paquetes ICMP Echo Request.

* **Comando:** `nmap -sn -PE 10.0.1.4`.
    * `nmap`: Herramienta de escaneo de red.
    * `-sn`: Opción para realizar un "ping scan" que descubre hosts sin escanear puertos.
    * `-PE`: Especifica el uso de un ping de eco ICMP (ICMP Echo Request).
    * `10.0.1.4`: La dirección IP del host objetivo.
* **Proceso y Resultado:** Nmap envía un Echo Request. Si el host está activo y no lo bloquea, responde con un Echo Reply. Como se observa en la captura de pantalla del terminal, el host `10.0.1.4` se reporta como "up" con una baja latencia, confirmando que está activo.

### 3.2. Práctica de TCP SYN Ping
Esta técnica envía un paquete TCP con el flag SYN activado a los hosts de la red.

* **Comando:** `nmap -sn -PS22 10.0.1.0/24`.
    * `-PS<port(s)>`: Indica a Nmap que use un ping TCP SYN, enviando un paquete TCP con el flag SYN.
    * `22`: El puerto al que se envía el paquete.
    * `10.0.1.0/24`: Rango de la red a escanear.
* **Proceso y Resultado:** El comando lanza peticiones a la red. Los hosts que responden con un `SYN/ACK` se consideran activos. Se aborta la conexión para no levantar sospechas. La captura de pantalla del terminal muestra varios hosts como "up", incluyendo `10.0.1.1`, `10.0.1.4`, `10.0.1.5` y `10.0.1.6`.

### 3.3. Práctica de TCP ACK Ping
Esta técnica envía un paquete TCP con el flag ACK activado. Requiere privilegios de root para funcionar correctamente.

* **Comando:** `sudo nmap -sn -PA22 --disable-arp-ping 10.0.1.0/24`.
    * `sudo`: Permisos de administrador.
    * `-PA<port(s)>`: Utiliza un ping TCP ACK, enviando un paquete con el flag ACK.
    * `--disable-arp-ping`: Deshabilita el escaneo ARP implícito para forzar a Nmap a usar el método `-PA`.
* **Proceso y Resultado:** Los hosts activos que reciben un paquete ACK y no saben por qué se envía responden con un `RST/ACK`, lo que indica a Nmap que están activos. Como se muestra en la captura de pantalla del terminal, Nmap identifica 6 hosts como "up" después de ejecutar el comando con `sudo`.

### 3.4. Práctica de UDP Ping
Esta técnica envía paquetes UDP. Al igual que el `TCP ACK Ping`, requiere privilegios de root.

* **Comando:** `sudo nmap -sn -PU22 --disable-arp-ping 10.0.1.0/24`.
    * `-PU<port(s)>`: Utiliza un ping UDP, enviando un paquete UDP sin datos.
    * `--data-length <number>`: Parámetro opcional para incluir un payload aleatorio, lo que puede ayudar a evadir firewalls que descartan paquetes UDP sin datos.
* **Proceso y Resultado:** Si un host está activo y el puerto está abierto, no se recibe respuesta. Si el puerto está cerrado, se recibe un error ICMP. Como se muestra en la captura de pantalla del terminal, Nmap identifica 5 hosts como "up". La captura de Wireshark muestra los paquetes UDP enviados con el payload especificado.

### 3.5. Práctica de ARP Scan
Esta es una técnica muy rápida y efectiva para redes locales, ya que opera en la capa 2 del modelo OSI.

* **Comando con ARP-Scan:** `sudo arp-scan -I`.
    * `-I`: Escanea la red local completa.
* **Proceso y Resultado:** El comando envía solicitudes ARP a todas las direcciones IP del rango de la red local. Los hosts activos responden con su dirección MAC. La captura de pantalla del terminal muestra la detección de 5 hosts, con sus respectivas direcciones MAC.
* **Comando con Nmap:** `sudo nmap -sn -PR 10.0.1.0/24`.
    * `-PR`: Le indica a Nmap que use el protocolo de resolución de direcciones (ARP) para el descubrimiento de hosts.
* **Proceso y Resultado:** Nmap envía solicitudes ARP y los hosts activos responden con sus direcciones MAC. Al igual que con `arp-scan`, la captura de pantalla del terminal muestra los 6 hosts activos con sus direcciones MAC y latencia.

### 3.6. Construcción de una Herramienta DIY (Python + Scapy)
El documento proporciona un script simple para crear un escáner ARP utilizando Python y la biblioteca Scapy.

* **Script:** Se define una función `scan(ip)` que construye un paquete ARP con una dirección MAC de destino de broadcast (`ff:ff:ff:ff:ff:ff`). Luego usa `srp` (send and receive packets) para enviar el paquete y capturar las respuestas. El script itera sobre las respuestas y imprime la dirección IP (`psrc`) y la dirección MAC (`hwsrc`) de cada host activo.
* **Ejecución:** Se ejecuta el script con `sudo python3 arp.py`. Los permisos de `sudo` son necesarios para manipular paquetes a bajo nivel.
* **Resultado:** El script produce una lista de direcciones IP y sus correspondientes direcciones MAC para los hosts activos en la red.

---

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad
El descubrimiento de hosts es una fase fundamental en una auditoría de seguridad, ya que permite reducir el alcance de la búsqueda a los dispositivos activos. Esto no solo ahorra tiempo, sino que también permite una evaluación más precisa de la postura de seguridad de la red. La comprensión de las diferentes técnicas de escaneo, como el ARP scan en redes locales y el ICMP/TCP/UDP ping para redes más amplias, es vital para evadir firewalls y obtener un inventario completo de los dispositivos. La posibilidad de construir herramientas personalizadas con Python y Scapy ofrece una flexibilidad y un control sin precedentes para escenarios de seguridad complejos.

### 4.2. Puntos de Aprendizaje Clave
* **Protocolos de red:** Se ha revisado el funcionamiento de ARP, DNS, ICMP, TCP y UDP, y se ha comprendido cómo cada uno puede ser manipulado para el descubrimiento de hosts.
* **Técnicas de escaneo:** Se han explorado y demostrado las técnicas de escaneo más comunes, identificando las fortalezas y debilidades de cada una (por ejemplo, la fiabilidad del ARP scan vs. la evasión de firewalls con UDP/IP Protocol Ping).
* **Herramientas:** Nmap, ARP-Scan y Netdiscover son herramientas poderosas para el reconocimiento de redes. La elección de la herramienta depende de los objetivos y el tipo de red (por ejemplo, Nmap es versátil, mientras que ARP-Scan es más rápido en LAN).
* **Desarrollo propio (DIY):** La creación de un script con Python y Scapy ilustra el proceso de bajo nivel de la comunicación de red, una habilidad invaluable para adaptar las herramientas a necesidades específicas de auditoría.

### 4.3. Relevancia Técnica
El conocimiento de las técnicas de descubrimiento de hosts es indispensable para cualquier profesional de la ciberseguridad. La capacidad de utilizar herramientas como Nmap, ARP-Scan y Netdiscover, así como de entender la generación de paquetes con bibliotecas como Scapy, permite realizar auditorías de red completas y eficaces. Esta habilidad no solo es útil para identificar hosts activos, sino también para evaluar la eficacia de las medidas de seguridad perimetrales como los firewalls, y para preparar las siguientes etapas de un pentesting. La práctica con estas herramientas proporciona una comprensión profunda y aplicable en un entorno profesional real.