# ARP Spoofing: Ataque, Realización y Mitigación

El **ARP Spoofing**, también conocido como **ARP Poisoning** o envenenamiento de ARP, es una técnica de **hacking** que explota el protocolo ARP (Address Resolution Protocol) en redes locales (**LAN**). Su objetivo es enviar mensajes ARP falsificados a la red para engañar a los dispositivos, haciendo que asocien la dirección IP de un host legítimo con la dirección MAC de un atacante. De esta manera, el atacante puede interceptar, modificar o bloquear el tráfico destinado al host legítimo, ya que los dispositivos de la red enviarán el tráfico al atacante, pensando que es el destino correcto.

Este ataque es un tipo de ataque de **Man-in-the-Middle (MitM)**, ya que el atacante se sitúa en medio de la comunicación entre dos dispositivos. El protocolo ARP es vulnerable a este tipo de ataques porque, por defecto, no incluye mecanismos de autenticación para verificar la legitimidad de los mensajes ARP.

## Protocolo ARP y su Vulnerabilidad

El protocolo ARP es esencial para las comunicaciones en una LAN, ya que se encarga de mapear direcciones IP (capa 3 del modelo OSI) a direcciones MAC (capa 2). Cada dispositivo en la red mantiene una **tabla ARP** que almacena estas asociaciones. Cuando un dispositivo necesita enviar un paquete a una dirección IP en la misma red, primero busca la dirección MAC correspondiente en su tabla ARP. Si no la encuentra, envía una solicitud ARP de difusión para obtener la dirección MAC. El dispositivo con la dirección IP solicitada responde con su dirección MAC, y la tabla ARP se actualiza.

La vulnerabilidad reside en que los dispositivos confían en las respuestas ARP que reciben, sin verificar si provienen de la fuente legítima. Un atacante puede aprovechar esto para enviar respuestas ARP falsificadas, asociando su propia dirección MAC con la dirección IP del router (gateway) o de otro host, lo que le permite desviar el tráfico de la víctima hacia su máquina.

## Realización de un Ataque de ARP Spoofing

A continuación, se detalla un ataque de ARP Spoofing utilizando dos máquinas virtuales Ubuntu: una como víctima/servidor y otra como atacante.

### Preparación del Entorno

1.  **Identificar las direcciones IP:**
    En ambas máquinas, se utiliza el comando `ip addr` para obtener las direcciones IP.

      * Máquina víctima: `10.211.55.5`
      * Máquina atacante: `10.211.55.17`

2.  **Verificar la conectividad:**
    Desde la máquina atacante, se realiza un `ping` a la máquina víctima para confirmar que hay comunicación entre ambas.

3.  **Identificar la dirección MAC del gateway:**
    En la máquina atacante, se utiliza el comando `arp -a` para mostrar la tabla ARP y encontrar la dirección MAC asociada al gateway de la red. Si el comando no está disponible, se puede instalar con `sudo apt install net-tools`.

4.  **Habilitar el IP forwarding en la máquina atacante:**
    Para que los paquetes fluyan correctamente entre la víctima y el gateway real mientras el atacante intercepta el tráfico, es necesario habilitar el reenvío de paquetes IP.

    ```bash
    echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
    ```

      * `echo 1`: Genera el valor `1` para habilitar el reenvío.
      * `|`: Redirige la salida del comando anterior como entrada del siguiente.
      * `sudo tee /proc/sys/net/ipv4/ip_forward`: Utiliza `sudo` y `tee` para escribir el valor `1` en el archivo del sistema `ip_forward`, lo que habilita el reenvío de paquetes.

### Ejecución del Ataque con Arpspoof

Una vez que el entorno está preparado, se utiliza la herramienta `arpspoof` para ejecutar el ataque.

1.  **Lanzar el ataque desde la máquina atacante:**

    ```bash
    sudo arpspoof -i eth0 -t 10.211.55.5 10.211.55.1
    ```

      * `sudo`: Ejecuta el comando con privilegios de superusuario.
      * `arpspoof`: Invoca la herramienta para enviar respuestas ARP falsificadas.
      * `-i eth0`: Especifica la interfaz de red (`eth0`) que se utilizará para el ataque.
      * `-t 10.211.55.5`: Define la dirección IP de la víctima (el `target`).
      * `10.211.55.1`: Especifica la dirección IP del gateway.
        Este comando comienza a enviar paquetes ARP falsificados, asociando la dirección MAC del atacante con la IP del gateway en la tabla ARP de la víctima.

2.  **Verificar el éxito del ataque en la máquina víctima:**
    En la máquina víctima, se ejecuta `arp -a` para comprobar si la dirección MAC del gateway ha cambiado. Se observa que la dirección IP del gateway (`10.211.55.1`) ahora está asociada con la dirección MAC de la máquina atacante. A partir de este momento, todo el tráfico de la víctima destinado al exterior será redirigido a la máquina del atacante.

3.  **Capturar el tráfico en la máquina atacante:**
    Mientras el ataque de `arpspoof` sigue en curso en una terminal, en otra se levanta `tcpdump` para capturar el tráfico.

    ```bash
    sudo tcpdump -i eth0 arp or ip
    ```

      * `-i eth0`: Escucha en la interfaz de red `eth0`.
      * `arp or ip`: Captura el tráfico de los protocolos ARP e IP.
        A partir de aquí, el atacante puede monitorear todo el tráfico que la víctima envía, incluyendo datos no cifrados. Si bien el tráfico HTTPS está cifrado y su contenido no es legible, aún se pueden ver los metadatos de la conexión.

## Consecuencias del ARP Spoofing

Las consecuencias de un ataque de ARP Spoofing exitoso pueden ser muy graves y comprometer la confidencialidad, integridad y disponibilidad de los datos. El atacante puede:

  * **Robo de información confidencial:** Capturar contraseñas, datos bancarios o cualquier otra información sensible que se transmita sin cifrado.
  * **Suplantación de identidad:** Utilizar la información interceptada para suplantar la identidad de la víctima en la red.
  * **Interrupción de servicios:** Bloquear o modificar el tráfico de red, lo que puede causar una interrupción de los servicios de red.

## Mitigación de Ataques de ARP Spoofing

Para mitigar el riesgo de ARP Spoofing, es fundamental implementar medidas de seguridad robustas:

  * **Seguridad de red basada en autenticación:** Implementar soluciones de autenticación, como el estándar **IEEE 802.1X**, para verificar la identidad de los dispositivos y usuarios antes de permitirles el acceso a la red. Esto asegura que solo los dispositivos autorizados puedan conectarse.
  * **Monitorización y detección de ARP anómalos:** Utilizar herramientas de monitorización de red que puedan detectar y alertar sobre cambios inusuales o anómalos en las tablas ARP. Esto ayuda a identificar posibles intentos de ARP Spoofing.
  * **Filtrado de tráfico ARP sospechoso:** Configurar reglas en los dispositivos de red para bloquear o filtrar el tráfico ARP que parezca sospechoso. Un ejemplo de comportamiento sospechoso es recibir respuestas ARP de múltiples direcciones MAC para una misma dirección IP.
  * **Implementación de VLANs:** Utilizar **VLANs (Virtual LANs)** para segmentar la red. La segmentación reduce la superficie de ataque y limita la propagación de paquetes ARP maliciosos, ya que restringe el alcance del ataque a un segmento de red más pequeño.

En resumen, aunque el ARP Spoofing es una técnica de ataque que explota una vulnerabilidad inherente al protocolo ARP, se puede mitigar implementando medidas de seguridad proactivas y robustas para proteger la infraestructura de red.