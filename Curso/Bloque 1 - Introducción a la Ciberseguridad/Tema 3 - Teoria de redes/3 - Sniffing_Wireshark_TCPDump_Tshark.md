# Análisis del Tráfico de Red: Sniffing y Herramientas Esenciales (Wireshark, TCPdump, Tshark)

El **sniffing de redes** es una técnica fundamental en ciberseguridad que implica la captura y el monitoreo del tráfico que viaja a través de una red. Aunque a menudo se asocia con actividades maliciosas como el espionaje, también es una herramienta indispensable para administradores de red y analistas de seguridad para diagnosticar problemas de red, verificar la configuración y detectar actividades maliciosas. Al realizar *sniffing*, se capturan los **paquetes de datos** que se transmiten en la red, incluyendo su **payload** (los datos en sí) y las múltiples **cabeceras** que indican el origen, destino y tipo de información.

## 1\. Entorno de Laboratorio

Para comprender y practicar el *sniffing*, utilizaremos el siguiente entorno de laboratorio:

  * **Máquina Kali Linux:**
      * Dirección IP: `10.0.1.12`
  * **Máquina Ubuntu Server 1:**
      * Dirección IP: `10.0.1.13`
  * **Máquina Ubuntu Server 2:**
      * Dirección IP: `10.0.1.14`

Todas estas máquinas se encuentran en la misma subred (`10.0.1.0/24`), lo que nos permitirá generar y capturar el tráfico que fluye entre ellas.

## 2\. Tipos de Sniffing

Existen dos categorías principales de *sniffing*, diferenciadas por la interacción del atacante o analista con la red:

  * **Passive Sniffing (Sniffing Pasivo):** El atacante simplemente "escucha" el tráfico sin interactuar activamente con la red o los sistemas. No genera ningún paquete adicional, simplemente observa el flujo de datos.
  * **Active Sniffing (Sniffing Activo):** En este tipo de captura, el usuario debe realizar ciertas interacciones o técnicas para forzar que el tráfico pase por su máquina y así poder capturarlo.

### 2.1. Técnicas de Sniffing Activo

Varias técnicas permiten el *Active Sniffing*:

  * **Modo Promiscuo (Promiscuous Mode):** Se refiere a la capacidad de una interfaz de red (NIC) para capturar **todos los paquetes de datos** que pasan a través de ella en un segmento de red compartido, independientemente de si esos paquetes están destinados o no a esa interfaz en particular. Esta capacidad es utilizada tanto en *Active Sniffing* como en *Passive Sniffing* (si el medio lo permite, como en redes *hub* o Wi-Fi).

  * **DNS Spoofing:** Consiste en confundir a un *host* objetivo para que, en lugar de enviar una petición DNS a su servidor legítimo, la envíe al atacante. El atacante manipula la respuesta DNS para redirigir el tráfico del objetivo hacia una ubicación maliciosa o a sí mismo, y luego, opcionalmente, lo reenvía al destino real para evitar levantar sospechas.

  * **ARP Spoofing/Poisoning:** El atacante envía **mensajes ARP falsificados** a la red, asociando su propia dirección MAC con la dirección IP de otro dispositivo (ej., la del *router* o de un servidor). De esta forma, todo el tráfico destinado a esa IP legítima se redirige hacia el atacante, quien puede inspeccionarlo y luego reenviarlo a su destino real.

  * **DHCP Sniffing:** El atacante monitorea el tráfico del protocolo DHCP en la red para obtener información sobre direcciones IP disponibles, direcciones MAC de dispositivos y la configuración de red. Esta información puede ser utilizada posteriormente para realizar otros ataques, como la creación de un servidor DHCP malicioso o la suplantación de IPs.

## 3\. Herramientas para Sniffing

Existen diversas herramientas para realizar *sniffing* y analizar el tráfico de red, tanto con interfaz gráfica como de línea de comandos.

### 3.1. Wireshark

**Wireshark** es un **sniffer de paquetes de red de código abierto** con una interfaz gráfica muy completa y potente.

#### **Características Clave:**

  * **Captura y Análisis Gráfico:** Permite capturar tráfico de red en vivo o analizar capturas previamente guardadas (ficheros **PCAP** y **PCAPNG**) de forma visual.
  * **Inspección de Paquetes:** Ofrece una vista detallada de cada paquete, mostrando las cabeceras de todas las capas (Ethernet, IP, TCP/UDP, HTTP, DNS, etc.) y el *payload*.
  * **Filtros Avanzados:** Permite aplicar filtros (de captura y de visualización) para ver únicamente el tráfico deseado, lo que es fundamental para aislar problemas o actividades maliciosas.
  * **Estadísticas de Red:** Genera estadísticas sobre el tráfico capturado, como protocolos utilizados, *endpoints*, conversaciones, etc.
  * **Exportación de Capturas:** Permite exportar las capturas en diversos formatos, siendo los más comunes PCAP y PCAPNG.

### 3.2. Tshark

**Tshark** es la **versión de línea de comandos de Wireshark**. Ofrece las mismas funcionalidades para capturar y analizar tráfico, pero a través de comandos de texto.

#### **Características Clave:**

  * **Análisis en Tiempo Real o de Archivos:** Permite realizar análisis de tráfico en vivo directamente desde la terminal o investigar capturas guardadas (PCAP/PCAPNG).
  * **Uso en Entornos sin GUI:** Ideal para servidores remotos o sistemas que no disponen de entorno gráfico.
  * **Scripting y Automatización:** Su naturaleza de línea de comandos lo hace perfecto para *scripts* o tareas automatizadas de monitoreo de red.
  * **Comandos Asociados:** Incluye otras utilidades como `rawshark`, `editcap` (para editar capturas), `mergecap` (para combinar capturas) y `text2pcap` (para convertir texto a formato PCAP).
  * **Instalación:** Se instala fácilmente con `sudo apt install tshark` en sistemas Debian/Ubuntu.

### 3.3. TCPdump

**TCPdump** es otra herramienta de línea de comandos para capturar tráfico de red en sistemas Unix-like (incluido Linux). Es **similar a Tshark** y una excelente opción para entornos sin interfaz gráfica.

#### **Características Clave:**

  * **Captura de Tráfico:** Permite capturar paquetes directamente de una interfaz de red.
  * **Filtros de Captura:** Soporta filtros complejos para capturar solo el tráfico relevante.
  * **Salida por Consola o Fichero:** Puede mostrar el tráfico directamente en la consola o guardarlo en un archivo PCAP para su posterior análisis con herramientas como Wireshark.
  * **Uso en Servidores:** Muy utilizada en servidores remotos para el monitoreo de tráfico o la detección de intrusiones.

## 4\. Laboratorio Práctico: Sniffing con Wireshark, TCPdump y Tshark

Este laboratorio se realizará desde la máquina Kali Linux, la cual tiene la IP `10.0.1.12`. Las máquinas Ubuntu Server 1 (`10.0.1.13`) y Ubuntu Server 2 (`10.0.1.14`) se utilizarán para generar tráfico de red.

### 4.1. Preparación: Generar Tráfico de Red

Antes de iniciar las capturas, es útil generar tráfico de red para tener algo que analizar. En la máquina Kali, se levantará un servidor HTTP simple:

1.  **Iniciar Servidor HTTP en Kali:**

    ```bash
    python3 -m http.server 80
    ```

      * **`python3 -m http.server`**: Ejecuta un módulo de Python que inicia un servidor web HTTP básico.
      * **`80`**: Especifica que el servidor debe escuchar en el puerto 80 (puerto estándar para HTTP).
      * **Objetivo**: Crear un servidor web accesible desde otras máquinas de la red, que permitirá generar tráfico HTTP (peticiones GET) para su posterior captura y análisis.

### 4.2. Sniffing con Wireshark

Wireshark viene instalado por defecto en Kali Linux.

1.  **Iniciar Wireshark:** Abrir la aplicación Wireshark desde el menú o la terminal.

2.  **Seleccionar Interfaz de Captura:** En la ventana principal de Wireshark, se deben seleccionar las interfaces de red por las que se desea capturar tráfico. Para este laboratorio, seleccionaremos la interfaz **`eth0`**. Clicar en ella para iniciar la captura.

      * **Objetivo**: Poner la interfaz de red en modo de captura para interceptar los paquetes que pasan a través de ella.

3.  **Generar Tráfico (Ping y HTTP):**

      * **Desde Ubuntu Server 1 (`10.0.1.13`):** Realizar un `ping` a la IP de Kali (`10.0.1.12`).
          * **`ping 10.0.1.12`**: Envía paquetes ICMP Echo Request.
          * **Objetivo**: Generar tráfico ICMP para ver cómo Wireshark los captura y los muestra.
      * **Desde el Navegador de Kali:** Abrir el navegador y navegar a una página web (ej., `example.com`).
          * **Objetivo**: Generar tráfico HTTP y DNS para observar las peticiones y respuestas en Wireshark.

4.  **Analizar Captura en Wireshark:**

      * **Tráfico ICMP y ARP:** Wireshark mostrará las peticiones **ICMP Echo Request** y las respuestas **ICMP Echo Reply**. También se podrán observar peticiones **ARP Request** (ej., cuando una máquina no conoce la MAC de `10.0.1.12`) y sus **ARP Reply**, resolviendo la dirección MAC.

      * **Tráfico HTTP y DNS:** Al navegar, se verán las peticiones **HTTP GET** (ej., `GET / HTTP/1.1` a `example.com`), las respuestas **HTTP/1.1 200 OK** (si la página carga correctamente), o incluso **HTTP/1.1 404 Not Found** (como para `favicon.ico`). Wireshark permite aplicar filtros (ej., escribir `http` en la barra de filtros) para ver solo el tráfico HTTP.

### 4.3. Sniffing con TCPdump

`tcpdump` es una herramienta de línea de comandos para la captura y análisis de paquetes, ideal para entornos sin GUI.

1.  **Verificar Permisos y Opciones de `tcpdump`:**

      * Intentar ejecutar `tcpdump` sin `sudo` resultará en un error de permiso. Esto es porque la captura de paquetes a bajo nivel requiere privilegios de *root*.
      * ```bash
          tcpdump
          # Output: tcpdump: eth0 You don't have permission to perform this capture on that device
        ```
      * Para ver las opciones disponibles:
        ```bash
        sudo tcpdump -h
        ```
          * **`sudo`**: Ejecuta el comando con privilegios de superusuario.
          * **`-h`**: Muestra la ayuda y las opciones disponibles del comando `tcpdump`.
          * **Objetivo**: Familiarizarse con las opciones para filtrar por interfaz (`-i`), guardar en archivo (`-w`), etc.

2.  **Iniciar Captura con `tcpdump`:**

    ```bash
    sudo tcpdump
    ```

      * **Explicación**: Lanza `tcpdump` con privilegios de *root*. Por defecto, `tcpdump` escucha en la primera interfaz de red disponible (generalmente `eth0`). Mostrará una salida *verbose* (detallada) del tráfico en tiempo real.
      * **Objetivo**: Capturar y mostrar el tráfico de red directamente en la terminal.

3.  **Generar Tráfico HTTP y Analizar Salida:**

      * **Acción:** Recargar la página web en el navegador de Kali (o realizar otra petición HTTP).
      * **Observación:** `tcpdump` mostrará las líneas de tráfico relacionadas con la petición HTTP (ej., peticiones DNS para `example.com`, conexiones TCP, y transacciones HTTP). Aunque menos visual que Wireshark, los detalles (`IP origen`, `IP destino`, `puertos`, `flags TCP`, `protocolos`) son visibles.
      * **Uso como Analista de Ciberseguridad:** La salida de `tcpdump` es crucial para *scripts* de monitoreo automatizados o para realizar análisis forenses en servidores donde no se puede instalar una GUI. Esta salida puede ser redirigida a un archivo (usando la opción `-w`) para su posterior análisis con Wireshark.

### 4.4. Sniffing con Tshark

`tshark` es la versión de línea de comandos de Wireshark y ofrece funcionalidades muy similares a `tcpdump`.

1.  **Verificar Instalación e Iniciar Captura con `tshark`:**

    ```bash
    tshark
    ```

      * **Explicación**: Similar a `tcpdump`, inicia la captura en la interfaz por defecto. Si `tshark` no estuviera instalado, se instalaría con `sudo apt install tshark`.
      * **Objetivo**: Capturar y mostrar tráfico con una salida estructurada similar a Wireshark pero en la consola.

2.  **Generar Tráfico (HTTP y ICMP) y Analizar Salida:**

      * **Acción:** Recargar la página web en el navegador de Kali para generar tráfico HTTP/DNS. Luego, desde Ubuntu Server 1 (`10.0.1.13`) y Ubuntu Server 2 (`10.0.1.14`), realizar `ping` a Kali (`10.0.1.12`).
      * **Observación:** `tshark` mostrará los paquetes capturados, incluyendo:
          * **Peticiones HTTP:** Se verán líneas como `HTTP GET / HTTP/1.1` o `HTTP/1.1 304 Not Modified`, indicando la actividad web.
          * **Peticiones ICMP:** Se mostrarán los **ICMP Echo request** y **Echo reply** de los *pings* entre las máquinas Ubuntu y Kali.
          * **Peticiones ARP:** Si una máquina Ubuntu no conocía la MAC de Kali, se verán las peticiones ARP (ej., "Who has 10.0.1.12? Tell 10.0.1.13") y las respuestas ("10.0.1.12 is at 08:00:27:16:db:d7"). Esto es fundamental para entender cómo las máquinas resuelven direcciones MAC en la red local.
      * **Uso como Analista de Ciberseguridad:** `tshark` es excelente para automatizar análisis de paquetes, aplicar filtros complejos sin la necesidad de una GUI, y para depurar problemas de red en servidores. Su salida puede ser fácilmente parseada por *scripts*.

Mediante estos ejemplos prácticos, se demuestra cómo Wireshark, `tcpdump` y `tshark` permiten a los profesionales de ciberseguridad capturar, visualizar y analizar el tráfico de red, lo cual es vital para el monitoreo, la detección de incidentes y la resolución de problemas en la red.

-----