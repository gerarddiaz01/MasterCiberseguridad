# Packet Sniffing con TCPDump y TShark: Análisis de Tráfico de Red

El **packet sniffing** o interceptación de paquetes es una técnica esencial en ciberseguridad que implica capturar y analizar el tráfico de datos que fluye a través de una red. Permite a los administradores de red examinar el contenido de los paquetes, incluyendo direcciones IP, protocolos y datos transmitidos, para depurar redes o monitorizar el tráfico. Sin embargo, también puede ser utilizado por agentes maliciosos para interceptar información confidencial como contraseñas. Comprender y utilizar herramientas de packet sniffing es fundamental para fortificar las redes y sistemas, y es relevante en la ciberseguridad para defenderse de agentes maliciosos.

Para que el packet sniffing sea efectivo, es crucial que la tarjeta de red opere en **modo promiscuo**. Este modo permite que la tarjeta capture todos los paquetes de datos que pasan por el segmento de red al que está conectada, sin importar si están destinados a ella o no. Sin el modo promiscuo, la tarjeta de red solo capturaría los paquetes dirigidos específicamente a ella, limitando significativamente la capacidad de monitoreo y análisis. Por lo tanto, el modo promiscuo es esencial para obtener una visión completa y precisa de la actividad de la red, lo que es vital para la seguridad y el rendimiento óptimo de la infraestructura.

## Componentes del Packet Sniffing

El proceso de packet sniffing involucra varios componentes clave:

  * **Traffic Mirroring (Duplicación de Tráfico):** Es la técnica de hacer una copia exacta de los paquetes de datos que se envían, dirigiendo esta copia a un segundo dispositivo. Esto es útil tanto para la administración de redes como para el análisis forense.
  * **Packet Sniffer:** Es un software o dispositivo que captura los paquetes de datos que atraviesan la red. Pueden ser utilizados por administradores para diagnosticar problemas de red o por atacantes para recopilar información sensible.
  * **Malicious Eavesdropping (Escucha Maliciosa):** Es la acción de interceptar secretamente el tráfico de la red con intenciones maliciosas. Este tráfico, que ha sido duplicado mediante la técnica de mirroring, se dirige al PC del atacante donde el sniffer de paquetes está activo.

Es vital entender la estructura de las tramas de red o los paquetes, como el **TCP Header (cabecera TCP)**, para interpretar correctamente la información capturada. La cabecera TCP incluye componentes como el puerto de origen (`source port`), puerto de destino (`destination port`), número de secuencia, y `flags` como `CWR`, `ECE`, `URG`, `ACK`, `PSH`, `RST`, `SYN` y `FIN`. Estos `flags` son cruciales para configurar detecciones o entender el estado de una conexión. El campo `checksum` certifica que no ha habido errores durante la transmisión.

## Herramientas para Packet Sniffing: TCPDump y TShark

**Wireshark** es una herramienta de análisis de red de código abierto y gratuita, ampliamente utilizada para la captura y el análisis detallado de tráfico. Permite inspeccionar datos de red a nivel de paquete, desglosándolos para una fácil visualización y diagnóstico de problemas. Soporta cientos de protocolos, ofrece filtros potentes y la capacidad de inspeccionar y visualizar la jerarquía de paquetes y sesiones. Además, cuenta con una interfaz gráfica que facilita el trabajo con archivos de captura.

**TCPDump** y **TShark** son dos herramientas de análisis de paquetes sencillas y potentes que operan desde la línea de comandos.

  * **TCPDump:** Es un analizador de paquetes muy utilizado en sistemas operativos tipo Unix. Se usa para depurar tráfico y monitorizar la seguridad de la red, permitiendo guardar los paquetes capturados en un archivo para su análisis posterior.
  * **TShark:** Es la versión de línea de comandos de Wireshark. Ofrece muchas de las mismas características para capturar y analizar paquetes de red, pero sin la interfaz gráfica. Esto lo hace ideal para tareas automatizadas o entornos sin interfaz gráfica, como servidores remotos.

## Pruebas Prácticas de Packet Sniffing con TCPDump y TShark

Para demostrar el funcionamiento del packet sniffing, se utilizaron dos máquinas virtuales: una máquina emisora (IP: 10.211.55.5) y una máquina receptora/interceptora (IP: 10.211.55.17).

### 1\. Instalación de TCPDump y TShark

En ambas máquinas virtuales, se instalan las herramientas necesarias:

1.  **Actualizar la lista de paquetes (opcional, pero buena práctica):**

    ```bash
    sudo apt update
    ```

    Este comando actualiza el índice de paquetes disponibles en los repositorios.

2.  **Instalar TCPDump:**

    ```bash
    sudo apt install tcpdump
    ```

    Descarga e instala la herramienta TCPDump.

3.  **Instalar TShark:**

    ```bash
    sudo apt install tshark
    ```

    Descarga e instala la herramienta TShark.

### 2\. Generación de Tráfico de Red

Para poder capturar y analizar paquetes, primero se debe generar tráfico entre las dos máquinas.

1.  **Verificar conectividad con `ping` (desde la máquina emisora):**

    ```bash
    ping 10.211.55.17
    ```

    Este comando envía paquetes ICMP a la máquina receptora para asegurar que hay comunicación bidireccional.

2.  **Capturar tráfico con `tcpdump` (en la máquina receptora/interceptora):**

    ```bash
    sudo tcpdump -i any host 10.211.55.5 and host 10.211.55.17 -w captura.pcap
    ```

    Este comando inicia la captura de paquetes:

      * `sudo`: Ejecuta el comando con privilegios de superusuario.
      * `tcpdump`: Invoca la herramienta TCPDump.
      * `-i any`: Captura tráfico en cualquier interfaz de red disponible.
      * `host 10.211.55.5 and host 10.211.55.17`: Filtra el tráfico para incluir solo los paquetes que involucran a ambas direcciones IP.
      * `-w captura.pcap`: Guarda los paquetes capturados en un archivo llamado `captura.pcap`. Este es un formato típico para capturas de packet sniffing.
        La terminal mostrará un mensaje indicando que `tcpdump` está escuchando.

3.  **Generar tráfico ICMP con `ping` (desde la máquina emisora):**
    Mientras `tcpdump` está escuchando, se envía nuevamente un `ping` continuo para generar tráfico ICMP que será capturado.

4.  **Transferir un archivo con `netcat` (entre ambas máquinas):**
    Para generar tráfico adicional y observar la transferencia de datos, se utiliza `netcat` para enviar un archivo sin cifrar.

      * **En la máquina receptora/interceptora (en una nueva terminal):**
        ```bash
        nc -l 12345 > archivo_recibido.txt
        ```
        Este comando pone a `netcat` en modo de escucha (`-l`) en el puerto `12345`, redirigiendo cualquier dato recibido al archivo `archivo_recibido.txt`.
      * **En la máquina emisora:**
        ```bash
        nc 10.211.55.17 12345 planets.csv
        ```
        Este comando envía el archivo `planets.csv` a la IP `10.211.55.17` en el puerto `12345`.
        Una vez finalizada la transferencia, se verifica que el archivo ha sido recibido correctamente en la máquina interceptora. Es importante señalar que `netcat` no cifra el tráfico, lo que permite observar el contenido de los paquetes.

### 3\. Análisis del Tráfico Interceptado con TShark

Una vez capturado el tráfico, se utiliza `tshark` para analizar el archivo `.pcap`.

1.  **Detener la captura de `tcpdump`:**
    Se interrumpe la ejecución de `tcpdump` en la máquina receptora/interceptora (normalmente con `Ctrl+C`).

2.  **Visualizar los paquetes capturados con `tshark`:**

    ```bash
    tshark -r captura.pcap "ip.addr == 10.211.55.5 and ip.addr == 10.211.55.17"
    ```

    Este comando lee el archivo de captura y muestra los paquetes filtrados:

      * `tshark`: Invoca la herramienta TShark.
      * `-r captura.pcap`: Indica a TShark que lea los datos del archivo `captura.pcap`.
      * `"ip.addr == 10.211.55.5 and ip.addr == 10.211.55.17"`: Es un filtro de visualización que muestra solo los paquetes que involucran a ambas direcciones IP, ya sean de origen o destino.

    El resultado muestra una lista de paquetes capturados. Se pueden identificar:

      * **Paquetes ICMP del `ping` (por ejemplo, del 1 al 14):** Se observa la dirección IP de origen y destino, y el tipo de mensaje ICMP (`Echo request/reply`). También se muestra el **TTL (Time To Live)**, que indica cuántos saltos puede hacer un paquete antes de ser descartado.
      * **Inicio y transferencia de datos de `netcat` (por ejemplo, del 17 al 18, y 20 al 27 y 42 al 47):**
          * **Inicio de sesión TCP:** Se observa un paquete `SYN` (inicio de conexión) seguido de un `SYN, ACK` (reconocimiento de conexión).
          * **Three-way Handshake completado:** Un paquete `ACK` indica la finalización del proceso de `three-way handshake` TCP.
          * **Transmisión de datos:** Los paquetes que contienen datos tienen las banderas `PSH` (Push) y `ACK` activadas. Se observan números de secuencia y acuses de recibo (`ACK`) que confirman el orden y la recepción de los datos.
          * **Finalización de la sesión TCP (por ejemplo, del 32 al 34):** Se observa un intercambio de paquetes `FIN, ACK` y un `ACK` final, indicando el cierre de la conexión.

3.  **Visualizar el contenido de los datos transferidos (en formato ASCII):**
    Para ver el contenido real del archivo transferido (en este caso, `planets.csv`), se puede usar un filtro más específico y redirigir la salida a `xxd` para convertir el contenido hexadecimal a ASCII.

    ```bash
    tshark -r captura.pcap -Y "tcp.port == 12345" -T fields -e data | xxd -r -p
    ```

      * `-Y "tcp.port == 12345"`: Filtra los paquetes por el puerto TCP `12345`.
      * `-T fields -e data`: Extrae solo el campo de datos del paquete.
      * `| xxd -r -p`: Redirige la salida a `xxd` para convertir el código hexadecimal a ASCII.
        Este comando permite observar el contenido textual del archivo transferido.

## Importancia del Packet Sniffing en Ciberseguridad

TCPDump y TShark, combinados, son herramientas muy potentes para el packet sniffing, especialmente útiles en entornos de línea de comandos como servidores remotos. El packet sniffing es fundamental para la seguridad de la red porque proporciona a los administradores y equipos de seguridad una visibilidad profunda sobre el tráfico de datos. Permite detectar actividades maliciosas, identificar vulnerabilidades de seguridad y realizar análisis forenses en tiempo real. Al capturar y analizar paquetes de datos, el packet sniffing ayuda a las empresas a prevenir intrusiones, mitigar amenazas y responder eficazmente a incidentes de seguridad. En resumen, es una técnica esencial para fortalecer la seguridad de la red y mantener un entorno de TI protegido contra las crecientes amenazas en Internet.