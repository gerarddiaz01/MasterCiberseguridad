# Informe del Ejercicio Práctico: Generación y Análisis de Tráfico de Red con hping3 y Wireshark

## Contexto y Objetivo del Ejercicio

Este ejercicio práctico se centra en la manipulación y el análisis del tráfico de red a un nivel fundamental (capas 2, 3 y 4 del modelo OSI/TCP-IP). El objetivo principal es comprender cómo se construyen y transmiten los paquetes de red, y cómo herramientas especializadas permiten su generación, captura y análisis detallado para fines de ciberseguridad.

Para llevar a cabo este ejercicio, se utilizó un entorno de laboratorio compuesto por dos máquinas virtuales activas:

  * **Kali Linux VM:** Una máquina con la dirección IP `192.168.1.240`. Esta VM actuó como el **generador de tráfico** (utilizando `hping3`) y la **estación de análisis** (utilizando `Wireshark`).
  * **Ubuntu Server VM:** Una máquina con la dirección IP `192.168.1.241`. Esta VM sirvió como el **objetivo** para el tráfico generado, simulando un servidor en una red.

Ambas máquinas virtuales se configuraron para estar en la misma subred, lo que permitió una comunicación directa y la observación de sus interacciones de red. El objetivo del ejercicio fue generar diferentes tipos de tráfico de red (TCP, UDP, ICMP), capturarlo con Wireshark, y posteriormente analizar los detalles de los paquetes para responder a una serie de preguntas específicas.

## Configuración y Preparación del Entorno

Antes de iniciar la generación de tráfico, fue crucial establecer una conectividad de red adecuada entre ambas máquinas virtuales, asegurando que pudieran comunicarse directamente.

### Generación de Archivo PCAP y Análisis de Paquetes

Un **archivo PCAP** (Packet Capture) es un formato de archivo que almacena datos de paquetes de red capturados. Sirve como una "grabación" del tráfico que pasa por una interfaz de red, permitiendo un análisis forense, diagnóstico de red y estudio de protocolos en diferido. Para este ejercicio, se generó un archivo PCAP mediante una captura en vivo, ya que no se proporcionó uno. El archivo PCAP resultante de esta captura se nombró `PCAP exercise 1.pcap`.

**Proceso de Generación del Archivo PCAP y Comandos Utilizados:**

1.  **Inicio de la Captura en Wireshark:** En la Kali Linux VM, se abrió `Wireshark` y se inició una captura en la interfaz `eth0` para grabar todo el tráfico.
2.  **Generación de Tráfico (en la terminal de Kali, según el `Mousepad` del pantallazo):**
      * **Tráfico ICMP (Ping):** Envío de **mensajes** ICMP Echo Request para probar la conectividad básica.
        ```bash
        ping -c 5 192.168.1.241
        ```
          * `ping`: Envía mensajes ICMP Echo Request.
          * `-c 5`: Limita a 5 mensajes.
      * **Tráfico TCP (Escaneo de Puertos SYN):** Envío de **segmentos** TCP (unidades de datos de TCP) con la bandera SYN activa, simulando intentos de conexión.
        ```bash
        sudo hping3 -S -p 22 -p 80 -p 443 -p 8080 192.168.1.241 -c 10
        ```
          * `hping3`: Genera segmentos TCP.
          * `-S`: Establece la bandera SYN.
          * `-p 22 -p 80 -p 443 -p 8080`: indican los puertos por los cuales se puede pasar, podríamos haber usado un rango `-p 22-8080` si los incluye. Para el análisis, se consideró que generó tráfico a esos puertos.
          * `-c 10`: Envía 10 segmentos.
      * **Tráfico UDP (con hping3):** Envío de **datagramas** UDP (unidades de datos de UDP), que son transmisiones sin conexión.
        ```bash
        sudo hping3 --udp --baseport 123 192.168.1.241 -c 5
        ```
          * `hping3`: Genera datagramas UDP.
          * `--udp`: Equivalente a `-2`, indica generación de datagramas UDP.
          * `--baseport 123`: En este contexto, indica que se apunte al puerto 123.
          * `-c 5`: Envía 5 datagramas.
      * **Nota sobre IP aleatoria:** Aunque no se usó en el ejercicio visible, `hping3` puede generar paquetes con IP de origen aleatoria utilizando la opción `--rand-source`.
3.  **Finalización y Guardado:** Se detuvo la captura en Wireshark y se guardó el resultado en el archivo `PCAP exercise 1.pcap`.

### Análisis del Archivo PCAP y Respuestas a las Preguntas del Ejercicio

El archivo `PCAP exercise 1.pcap` fue abierto en Wireshark para su análisis detallado, respondiendo a cada pregunta del ejercicio basándonos en los datos capturados y el comportamiento observado.

#### Pregunta 1: ¿Qué dominios ha visitado la IP 192.168.1.241 (Ubuntu Server VM)? ¿Y qué subdominios?

Para responder a esta pregunta, se buscaron solicitudes DNS originadas desde la IP del Ubuntu Server VM.

  * **Filtro Wireshark:** `dns and ip.src == 192.168.1.241` o podemos usar si teníamos logs de http `http && ip.src == 192.168.1.241`
  * **Sintaxis del Filtro:** El filtro `dns` muestra paquetes del protocolo DNS. `ip.src == 192.168.1.241` filtra por la dirección IP de origen del Ubuntu Server VM. `and` combina ambas condiciones.
  * **Análisis de Datos:** Al aplicar el filtro y examinar las "Standard query" DNS, se identificó que la IP `192.168.1.241` realizó consultas para los siguientes dominios/subdominios:
      * `ntp.ubuntu.com`
      * `ntp.ubuntu.com.home`
      Si hubiesemos aplicado el filtro http y obtenido logs de http válidos, hubiesemos podido acceder a `Hypertext Transfer Protocol`, ver el host visitado (dominio o subdominio) y ver si es GET o POST.

#### Pregunta 2: ¿Qué protocolos se utilizan en la captura?

Para obtener una lista exhaustiva de los protocolos presentes en la captura, se utilizó la funcionalidad de estadísticas de Wireshark.

  * **Método:** Se accedió a `Statistics > Protocol Hierarchy` en Wireshark para obtener un desglose jerárquico de los protocolos.
  * **Análisis de Datos:** La jerarquía de protocolos mostró la presencia de:
      * Ethernet (todos los protocolos del PCAP file forman parte de Ethernet)
        * Link Layer Topology Discovery (LLTD)
        * HomePlug AV protocol
        * Address Resolution Protocol (ARP)
        * Internet Protocol Version 6 (IPv6)
        * Internet Protocol Version 4 (IPv4)
        * User Datagram Protocol (UDP)
            * Multicast Domain Name System (mDNS)
            * Domain Name System (DNS)
            * Dynamic Host Configuration Protocol (DHCPv6)
        * Transmission Control Protocol (TCP)
            * Transport Layer Security (TLS)
            * SSH Protocol
            * Hypertext Transfer Protocol (HTTP)
        * Internet Control Message Protocol (ICMP)
        * Internet Group Management Protocol (IGMPv2)

#### Pregunta 3: ¿Qué direcciones IP y puertos TCP/UDP se utilizan en cada flujo de datos?

Para identificar los flujos de datos principales, se utilizaron las estadísticas de conversaciones de Wireshark.

  * **Método:** Se accedió a `Statistics > Conversations` y se revisaron las pestañas "IPv4", "TCP" y "UDP".
  * **Análisis de Datos:** Se identificaron los siguientes flujos significativos con sus direcciones IP y puertos:
      * **Conversaciones IPv4 (pares de IPs):**
          * `192.168.1.240` (Kali) \<-\> `192.168.1.241` (Ubuntu Server): Flujos directos entre las VMs (generados por hping3).
          * `192.168.1.241` (Ubuntu Server) \<-\> `8.8.8.4` y `8.8.8.8` (Servidores DNS de Google): Flujos DNS.
          * `192.168.1.1` (Router/Gateway) \<-\> IPs locales (`192.168.1.240`, `192.168.1.241`, `192.168.1.255` broadcast).
      * **Conversaciones TCP (pares de IP:Puerto):**
          * `192.168.1.240` (puertos aleatorios, ej., `5422`) \<-\> `192.168.1.241` (puerto `80`): Múltiples flujos SYN de Kali a Ubuntu Server.
          * `192.168.1.57` (puertos altos) \<-\> IPs externas (puerto `443`): Flujos HTTPS.
      * **Conversaciones UDP (pares de IP:Puerto):**
          * `192.168.1.240` (puertos aleatorios, ej., `2349`) \<-\> `192.168.1.241` (puerto `123`): Flujos UDP de Kali a Ubuntu Server (NTP).
          * `192.168.1.241` (puertos aleatorios) \<-\> `8.8.8.8` (puerto `53`): Flujos DNS (UDP).
          * Flujos DHCP (puertos `67`/`68`) entre el router y la dirección de broadcast.

También podemos filtrar por UDP y TCP y ver el `src port` y `dst port` de cada log para ver los puertos de origen y destino. En los detalles se ven las direcciones ip también, sino en el log mismo se ven las direcciones ip de origen y destino.

#### Pregunta 4: ¿Qué métodos HTTP se utilizan en la captura? (GET, POST, PUT, etc.)

  * **Análisis:** En el archivo `PCAP exercise 1.pcap` no se observaron solicitudes HTTP (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `PATCH`, `OPTIONS`) debido a la falta de conexión a Internet de la Kali VM durante la captura. Si los tuviesemos se podría ver si es GET o POST en la info del log mismo. Sin embargo, estos métodos son parte integral del protocolo HTTP (Hypertext Transfer Protocol), fundamental para la comunicación en la web.
      * **Método GET:** Se utiliza para **solicitar datos** de un recurso (ej., para cargar una página web). Los datos se envían en la URL (cadena de consulta), son visibles y cacheables. Es **idempotente** (repetir no cambia el estado del servidor).
      * **Método POST:** Se utiliza para **enviar datos** al servidor para su procesamiento (ej., enviar un formulario o subir un archivo). Los datos se envían en el cuerpo de la solicitud HTTP, no en la URL. No es idempotente y no suele ser cacheable.
      * **Otros Métodos Principales:**
          * **HEAD:** Solicita solo los encabezados de la respuesta, sin el cuerpo del recurso.
          * **PUT:** Se usa para reemplazar un recurso completamente.
          * **DELETE:** Se usa para eliminar un recurso.
          * **PATCH:** Aplica modificaciones parciales a un recurso.
          * **OPTIONS:** Describe las opciones de comunicación disponibles para un recurso.

#### Pregunta 5: Enumera las diferentes direcciones MAC que aparecen en la captura junto con su dirección IP.

Para identificar los pares de direcciones MAC e IP, se analizaron los paquetes ARP (Address Resolution Protocol) y los encabezados Ethernet/IP/IPv6.

  * **Método:** Se filtró por `arp` y se examinaron los campos "Sender MAC address" e "Sender IP address", así como los encabezados "Ethernet II" e "Internet Protocol Version 4/6" de otros paquetes.
  * **Análisis de Datos:** Se identificaron los siguientes pares MAC-IP:
      * **`08:00:27:2e:c1:a9`**: Asociada a la IP `192.168.1.240` (Kali Linux VM).
      * **`08:00:27:a8:ff:c0`**: Asociada a la IP `192.168.1.241` (Ubuntu Server VM).
      * **`08:00:27:96:40`**: Asociada a la IP `192.168.1.1` (Router/Gateway de la red local).
      * **`08:00:27:a0:ff:c0`**: Asociada a la dirección IPv6 `2a01:cb1d:8b1e:5100:daa:ed:d536:8389:b7c`.
      * **`00:00:27:2e:c1:a9`**: Asociada a la dirección IPv6 `2a01:cb1d:8b1e:5100:2a50:1450:4007:80d::200e`.

Se puede ir también a Statistics, IPv4 Statistics, All Adresses, y podemos ver todas las direcciones ip que se han utilizado a lo largo de ésta captura. Podemos copiar una dirección ip de allí e utilziarle en el filtro `ip.addr == 192.168.1.240` para ver las interacciones de ésa dirección ip. Luego vamos a los detales, en Ethernet II y en Destination y Source vemos las direcciones MAC, en mi caso `08:00:27:2e:c1:a9` y `08:00:27:a8:ff:c0`. haciendo un `ifconfig lo podemos confirmar`.

#### Pregunta 6: ¿Desde qué puerto se lanza la solicitud (Request) para el primer paquete TCP SYN desde Kali a puerto 80 del Ubuntu Server? ¿Y a qué puerto se dirige?

  * **Filtro Wireshark:** `tcp.flags.syn == 1 and ip.src == 192.168.1.240`
  * **Sintaxis del Filtro:** `tcp.flags.syn == 1` busca paquetes TCP con la bandera SYN activada. `ip.src == 192.168.1.240` filtra por la IP de origen de la Kali VM. `and` combina las condiciones.
  * **Análisis de Datos:** Al examinar el paquete TCP SYN (ej. paquete No. 38 en la captura), se observó en los detalles del "Transmission Control Protocol":
      * La solicitud se lanzó **desde el puerto de origen `5422`**.
      * La solicitud se dirigió **al puerto de destino `80`**.

Si nos piden de encontrar un GET de http con una imagen.svg podemos encontrar el log filtrando por `http.request.uri contains "image.svg"` porque normalmente se solicita en el uri de la petición http. Y en los detalles podemos encontrar el puerto de origen y destino de dicho log. A parte podemos obtener la imagen.svg si hacemos botón derecho en el log, follow, TCP Stream, copiamos el string, abrimos una terminal y un archivo kali.svg con nano, guardamos el string del svg completo y podemos acceder a éste archivo para abrir la imagen.

#### Pregunta 7: ¿Se observa algún tipo de ataque o actividad maliciosa en la captura?

  * **Análisis:** El archivo `PCAP exercise 1.pcap` generado en este ejercicio no contenía ataques explícitos de terceros. Sin embargo, sí contenía **actividades que, en un contexto no autorizado, se considerarían maliciosas o preparatorias para un ataque**.
      * **Reconocimiento Activo (Escaneo de Puertos):** Los paquetes TCP SYN enviados a múltiples puertos (`22, 80, 443, 8080`) del Ubuntu Server VM desde Kali Linux (`hping3 -S`) constituyen un escaneo de puertos. Esta es una fase inicial crucial en los ataques, donde se intenta descubrir qué servicios están activos en un objetivo.
      * **IP Spoofing (Falsificación de IP de Origen):** Aunque no se realizó explícitamente en el ejercicio documentado, la capacidad de `hping3` para generar paquetes con IP de origen aleatoria utilizando la opción `--rand-source` es una técnica de falsificación. La falsificación de IP es una técnica maliciosa utilizada para ocultar la identidad del atacante, evadir filtros o facilitar ataques de denegación de servicio.

**Teoría: Detección y Prevención de Actividades Maliciosas**

El análisis de PCAP y logs es esencial en ciberseguridad para la detección de amenazas. Se busca identificar patrones anómalos o comportamientos que se desvíen de la norma.

  * **Formas de Encontrar Actividades Maliciosas (Patrones Comunes):**

      * **Reconocimiento:** Escaneos de puertos (múltiples conexiones a puertos de un objetivo), escaneos de red (ARP/ICMP a rangos de IP), o consultas DNS inusuales (a dominios sospechosos o servidores DNS no estándar).
      * **Acceso No Autorizado/Explotación:** Tráfico a puertos no estándar, patrones de paquetes que coinciden con exploits conocidos, o tráfico cifrado a destinos anusuales (Comando y Control).
      * **Persistencia/Comando y Control (C2):** Comunicación regular y periódica con IPs o dominios conocidos de C2, a menudo camuflada en protocolos comunes.
      * **Movimiento Lateral:** Intentos de autenticación fallidos múltiples o escaneos internos después de un compromiso.
      * **IP Spoofing:** Detectable por la asimetría en la comunicación (la respuesta no llega al emisor falsificado), anomalías en valores de TTL/ID, o IPs de origen que no pertenecen a la red de donde provienen los paquetes.

  * **Resolución y Prevención:**

      * **Mitigación Directa:** Bloquear IPs/puertos maliciosos en firewalls, aislar hosts comprometidos, aplicar parches de seguridad.
      * **Prevención y Detección Continua:**
          * **Filtrado de Entrada/Salida (BCP38):** Crucial en routers perimetrales para evitar que paquetes con IPs de origen falsas salgan o entren de la red.
          * **Sistemas de Detección/Prevención de Intrusiones (IDS/IPS):** Analizan el tráfico en tiempo real y alertan sobre patrones de ataque.
          * **Monitorización de Logs (SIEM/SOC):** Centralizan y correlacionan eventos de seguridad para detectar patrones.
          * **Firewalls de Aplicación Web (WAF):** Protegen contra ataques a nivel de aplicación.
          * **Segmentación de Red:** Divide la red para limitar la propagación.
          * **Autenticación Fuerte y Actualizaciones:** Mantener sistemas seguros y credenciales protegidas.

En el PCAP file de la corrección podemos apreciar muchísimas ARP requests de `Who has IPX? Tell IPX`, muy sospechoso y podemos pensar que ha habido un escáner de tipo ARP para todos los hosts de ésta máquina con el objetivo de hacer un ARP spoofing o identificar que máquinas están activas. Podríamos decir que dicha actividad es maliciosa.

## Conclusión

Este ejercicio ha proporcionado una comprensión práctica invaluable en la generación y el análisis de tráfico de red, pilares fundamentales de la ciberseguridad. Hemos utilizado `hping3` para construir paquetes a medida (segmentos TCP, datagramas UDP, mensajes ICMP) y `Wireshark` para su disección, lo que nos ha permitido verificar la composición de los paquetes, identificar los protocolos en uso, correlacionar direcciones MAC e IP, y comprender cómo se manifiestan las actividades de reconocimiento y el IP spoofing a nivel de red. El dominio de estas herramientas y conceptos es esencial para cualquier profesional que busque diagnosticar problemas, auditar la seguridad o responder a incidentes en un entorno de red.