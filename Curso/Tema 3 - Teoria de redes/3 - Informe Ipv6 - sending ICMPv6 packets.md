# Informe del Ejercicio Práctico: Comunicación IPv6 (ICMPv6) y Análisis de Cabeceras

### Diferencias entre Direcciones IPv6 y Direcciones IPv6 Link Local

El Protocolo de Internet versión 6 (IPv6) introduce un espacio de direcciones mucho más amplio y una gestión de direcciones más flexible que IPv4. Dentro de IPv6, existen varios tipos de direcciones, cada una con un propósito y un ámbito específicos. Las direcciones **Link Local** son un tipo particular y muy importante de dirección IPv6, distinta de las direcciones IPv6 "globales" o enrutables.

#### 1. Direcciones IPv6 (Generales / Enrutables)

Las direcciones IPv6 generales, comúnmente llamadas **direcciones unicast globales** o **direcciones de única-local (ULA)**, están diseñadas para la comunicación a través de redes más grandes y a menudo a través de Internet.

* **Propósito:** Proporcionar conectividad universal a través de la red (Internet) o dentro de una organización grande (intranet).
* **Ámbito (Scope):**
    * **Global:** Únicas a nivel mundial, enrutables a través de Internet (similar a las direcciones IP públicas de IPv4). Comienzan típicamente con `2000::/3`.
    * **Única-Local (ULA):** Diseñadas para uso dentro de una única organización o sitio. No son enrutables a través de Internet, pero son enrutables dentro de la intranet (similar a las direcciones IP privadas de IPv4). Comienzan con `fc00::/7` o `fd00::/8`.
* **Asignación:** Pueden ser asignadas manualmente, mediante SLAAC (Stateless Address Autoconfiguration, que usa el prefijo de la red y el identificador de interfaz), o por DHCPv6.
* **Ejemplos:**
    * Global: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
    * Única-Local: `fd00:db8::1`

#### 2. Direcciones IPv6 Link Local (`fe80::/10`)

Las direcciones Link Local son un tipo especial de dirección IPv6 que tiene un ámbito muy restringido.

* **Propósito:** Permitir la comunicación **solo entre nodos que están conectados directamente en el mismo segmento de red (o "enlace")**. Esto incluye dispositivos en la misma LAN, o VMs que comparten el mismo switch virtual. Son esenciales para la detección de vecinos (Neighbor Discovery Protocol - NDP) y la autoconfiguración inicial.
* **Ámbito (Scope):** Estrictamente limitado al segmento de red local. **No son enrutables por los routers**; un router no reenviará tráfico con una dirección Link Local como origen o destino.
* **Prefijo:** Siempre comienzan con `fe80::/10`. Esto significa que los primeros 10 bits son `1111 1110 10`, y el resto del prefijo es cero.
* **Asignación:** Son **obligatorias** para cada interfaz habilitada para IPv6. Se configuran automáticamente tan pronto como una interfaz se habilita para IPv6, sin necesidad de un servidor DHCP o configuración manual. A menudo se derivan de la dirección MAC del adaptador (utilizando el formato EUI-64) o se generan de forma pseudoaleatoria.
* **Casos de Uso:**
    * **Neighbor Discovery Protocol (NDP):** Utilizado para resolución de direcciones MAC a IP, detección de routers, autoconfiguración de direcciones, y detección de inaccesibilidad de vecinos.
    * **Autoconfiguración:** Los dispositivos usan direcciones Link Local para comunicarse con el router y obtener un prefijo de red para construir sus direcciones globales.
    * **Servicios Locales:** Descubrimiento y comunicación con servicios que solo operan en el enlace local.
* **Especificación de Interfaz para Pings:** Cuando se hace ping a una dirección Link Local, es **esencial** especificar la interfaz de red local por la que se debe enviar y recibir el paquete (ej., `%eth0` en Linux o `%14` en Windows). Esto es porque la misma dirección Link Local (`fe80::`) puede existir en múltiples interfaces de un mismo host, pero cada una pertenece a un enlace diferente.

#### Resumen de Diferencias Clave:

| Característica   | Dirección IPv6 (General / Global / ULA)    | Dirección IPv6 Link Local (`fe80::/10`)    |
| :--------------- | :----------------------------------------- | :------------------------------------------ |
| **Prefijo** | Variado (ej. `2000::/3`, `fc00::/7`)       | Siempre `fe80::/10`                        |
| **Ámbito** | Global o dentro de una organización/sitio | **Solo el segmento de red local** |
| **Enrutabilidad**| **Enrutable** | **NO Enrutable** |
| **Obligatoriedad**| Opcional, según la necesidad de conexión   | **Obligatoria** para cada interfaz IPv6     |
| **Propósito** | Conectividad de extremo a extremo (WAN/LAN) | Operaciones de enlace local (NDP, autoconfiguración) |
| **Configuración**| Manual, SLAAC, DHCPv6                      | Automática (autoconfiguración automática)   |
| **Uso en Pings** | `ping -6 <dirección_global>`              | `ping -6 <dirección_link_local>%<interfaz>`|

## Contexto y Objetivo del Ejercicio

Este ejercicio práctico se centra en la implementación y verificación de la comunicación a través del protocolo **IPv6**, específicamente utilizando mensajes **ICMPv6**. El objetivo principal es establecer y confirmar la conectividad IPv6 entre dos máquinas, capturar el tráfico resultante con Wireshark, y analizar en detalle la estructura de las cabeceras IPv6 e ICMPv6 para comprender los fundamentos de este protocolo de nueva generación.

Para la realización de este ejercicio, se utilizó un entorno de laboratorio virtual compuesto por dos máquinas virtuales (VMs) principales:

  * **Kali Linux VM:**

      * **Dirección IPv6 (Link Local):** `fe80::a00:27ff:fe2e:c1a9` (en la interfaz `eth0`).
      * **Rol:** Máquina desde la cual se iniciaron las pruebas de conectividad (ping) y donde se ejecutó Wireshark para la captura y el análisis del tráfico de red.

  * **Windows 10 VM:**

      * **Dirección IPv6 (Link Local):** `fe80::224:1539:2bc:c94d%14` (en su adaptador de red).
      * **Rol:** Máquina objetivo de las pruebas de conectividad, configurada para responder a las solicitudes ICMPv6.

Las directrices del ejercicio fueron las siguientes:

  * Asegurar que ambas máquinas estuvieran configuradas con IPv6 y pudieran comunicarse.
  * Explorar el comando `ping -6` para enviar un paquete ICMPv6 de una máquina a otra.
  * Utilizar una herramienta de captura como Wireshark para interceptar el paquete ICMPv6.
  * Analizar en profundidad la cabecera IPv6 de dicho paquete.
  * El objetivo final era familiarizarse con estas herramientas de análisis de redes y adquirir la habilidad de leer e interpretar la información obtenida, lo cual es fundamental para un analista de ciberseguridad.

## Fase 1: Establecimiento y Verificación de la Conectividad IPv6

La comunicación utilizando direcciones **Link Local (`fe80::`)** es clave en IPv6 para la conectividad dentro de un mismo segmento de red local. Estas direcciones no son enrutables, lo que significa que el tráfico que las utiliza no puede salir del segmento de red inmediato. Para que dos máquinas se comuniquen a través de sus direcciones Link Local, deben estar en el mismo "dominio de difusión" o "segmento de cable virtual". EN mi caso no sé si estaban en el mismo segmento pero usando las direcciones IPv6 de ambas máquinas me ha funcionado el ping.

### 1.1. Verificación y Configuración de la Conectividad IPv6 Link Local:

La primera fase del ejercicio se centró en asegurar que la Kali Linux VM y la Windows 10 VM pudieran comunicarse a través de sus direcciones IPv6 Link Local. Las configuraciones iniciales de red mostraron que las VMs no se comunicaban correctamente a pesar de tener direcciones IPv6. La causa principal de esto en entornos virtualizados a menudo reside en cómo los adaptadores de red virtual están enlazados a la red física o entre sí.

  * **Ajuste de la Configuración de Red en VirtualBox para Ambas VMs:**
    Para garantizar que Kali Linux VM y Windows 10 VM compartieran el mismo segmento de red virtual y permitieran la comunicación Link Local de manera fiable, se configuró el **Adaptador de Red 1** de **ambas máquinas virtuales** para utilizar el modo **"Red solo-anfitrión" (Host-only Adapter)**.
      * **Pasos de Configuración en VirtualBox Manager (para cada VM):**
        1.  La VM fue **apagada** (estado "Powered Off").
        2.  Se accedió a `Configuración (Settings)` \> `Red (Network)`.
        3.  En la pestaña `Adaptador 1`:
              * **"Habilitar adaptador de red"**: Se aseguró que estuviera marcado.
              * **"Conectado a:"**: Se seleccionó **"Red solo-anfitrión (Host-only Adapter)"**.
              * **"Nombre:"**: Se seleccionó la **misma "Red solo-anfitrión"** (ej., `vboxnet0`) para ambas VMs. Esto es crucial, ya que asegura que compartan el mismo conmutador virtual aislado.
              * **"Modo promiscuo:"**: Se estableció en **"Permitir todo (Allow All)"**. Esto permite que el adaptador virtual capture todo el tráfico que pasa por el conmutador virtual, esencial para Wireshark y algunas operaciones de red.
        4.  Se confirmó la configuración haciendo clic en `OK`.

### 1.2. Verificación de Direcciones IPv6 Link Local en las VMs:

Después de configurar los adaptadores solo-anfitrión, se iniciaron ambas VMs y se verificaron sus direcciones Link Local.

  * **En Kali Linux VM (terminal):**

    ```bash
    ip -6 address show eth0
    ```

      * **Sintaxis `ip -6 address show <interfaz>`:** Muestra las direcciones IPv6 configuradas para la interfaz especificada (en este caso, `eth0`, la interfaz principal de Kali en la red solo-anfitrión).
      * **Resultado:** Se identificó la dirección Link Local de Kali: `fe80::a00:27ff:fe2e:c1a9` para la interfaz `eth0`.

  * **En Windows 10 VM (Símbolo del sistema o PowerShell):**

    ```cmd
    ipconfig /all
    ```

      * **Sintaxis `ipconfig /all`:** Muestra una configuración detallada de todos los adaptadores de red en Windows.
      * **Resultado:** Se identificó la "Dirección IPv6 de vínculo local" de Windows 10: `fe80::224:1539:2bc:c94d%14` (el `%14` es el ID de ámbito o de interfaz de Windows, necesario al hacer ping a direcciones Link Local desde Windows).

### 1.3. Prueba de Conectividad con `ping -6`:

Con ambas VMs configuradas en la misma "Red solo-anfitrión" y sus direcciones Link Local identificadas, se procedió a verificar la conectividad.

  * **Comando de Ping ICMPv6 desde Kali a Windows 10:**
    ```bash
    ping -6 fe80::224:1539:2bc:c94d%eth0
    ```
      * **Sintaxis `ping -6`:** Indica que se utilice el protocolo IPv6 para el ping.
      * `fe80::224:1539:2bc:c94d`: Es la dirección IPv6 Link Local de destino (la de la Windows 10 VM).
      * `%eth0`: **Este componente es crucial para las direcciones Link Local.** Le indica al sistema Kali por qué interfaz de red *local* (`eth0`) debe intentar enviar el paquete para alcanzar esa dirección `fe80::`. Las direcciones Link Local tienen un ámbito restringido a la interfaz.
      * **Resultado:** El ping fue **exitoso**, recibiendo respuestas desde la Windows 10 VM, lo que confirmó que la conectividad IPv6 Link Local entre ambas máquinas estaba establecida. No recibí el mensaje "Address unreachable" o nad aparecido, simplemente estaba comunicando (aunque en la terminal no lo veía, en wireshark se veía).

## Fase 2: Captura y Análisis de Tráfico ICMPv6 con Wireshark

Una vez confirmada la conectividad, se procedió a capturar un paquete ICMPv6 con Wireshark y analizar su cabecera IPv6 en detalle.

### 2.1. Captura del Paquete ICMPv6:

1.  **Inicio de Captura en Wireshark:** En la Kali Linux VM, se abrió Wireshark y se seleccionó la interfaz `eth0` (la misma utilizada para el ping) para iniciar la captura de paquetes.
2.  **Generación de un Solo Ping ICMPv6:** Para obtener una captura limpia y fácil de analizar, se envió un único paquete ping desde la terminal de Kali:
    ```bash
    ping -6 -c 1 fe80::224:1539:2bc:c94d%eth0
    ```
      * `-c 1`: Limita el comando a enviar solo un paquete ICMPv6 Echo Request.

    Podríamos haber hecho directamente diciendo desde que interfaz quiero que se haga así:
    ```bash
    ping -I eth0 fe80::224:1539:2bc:c94d
    ```

    También, si sólo tenemos una maquina para ver dicho tráfico podemos usar nuestra propia maquina con Loopback. Pero para capturarla en Wireshark hay que cambiar la interfaz, ya no será eth0 sino será Loopback
    ```bash
    ping ::1
    ```
3.  **Detención de la Captura:** Se detuvo la captura en Wireshark tras el envío del paquete.

### 2.2. Análisis del Paquete ICMPv6 en Wireshark:

1.  **Filtro de Visualización:** Para aislar los paquetes de interés en la captura, se aplicó un filtro:

    ```
    icmpv6
    ```

      * **Sintaxis del Filtro:** `icmpv6` filtra la lista de paquetes para mostrar únicamente aquellos que pertenecen al protocolo ICMPv6.
      * **Resultado:** La lista mostró los paquetes `Echo (ping) request` y `Echo (ping) reply`.

2.  **Selección y Análisis de la Cabecera IPv6 (Paquete Echo Request):**
    Se seleccionó el paquete ICMPv6 Echo Request (el que va de Kali a Windows 10, generalmente el primer paquete de la pareja ping/respuesta). En el "Panel de Detalles del Paquete", se expandió la sección **"Internet Protocol Version 6"** para examinar sus campos.

      * **`Version: 6`**: Indica claramente que este paquete utiliza la versión 6 del Protocolo de Internet. Este campo es fijo y de 4 bits.
      * **`Traffic Class: 0x00`**: Este campo de 8 bits se utiliza para la clasificación de paquetes en IPv6, similar al campo DSCP (Differentiated Services Code Point) en IPv4. Permite priorizar ciertos tipos de tráfico (Quality of Service - QoS). Un valor de `0x00` indica prioridad o clase de tráfico por defecto.
      * **`Flow Label: 0x0b86e`**: Este campo de 20 bits se utiliza para que un host de origen etiquete secuencias de paquetes para las que solicita un manejo especial por parte de los routers IPv6 (como un flujo de tráfico que requiere un determinado QoS o que debe seguir una ruta específica). Para pings simples, a menudo es 0 o un valor generado automáticamente.
      * **`Payload Length: 84 bytes`**: Este campo de 16 bits indica la longitud de la parte de datos del paquete IPv6 (la parte que sigue al encabezado IPv6 base). En este caso, incluye la cabecera ICMPv6 y cualquier dato ICMP.
      * **`Next Header: ICMPv6 (58)`**: Este campo de 8 bits identifica el protocolo de la cabecera inmediatamente siguiente a la cabecera IPv6 base. Un valor de `58` indica que el siguiente protocolo es ICMPv6. Si fuera TCP sería `6`, UDP `17`.
      * **`Hop Limit: 64`**: Este campo de 8 bits especifica el número máximo de "saltos" (routers) que el paquete puede atravesar. Se decrementa en uno en cada router. Si llega a cero, el paquete se descarta. Un valor de `64` es un valor inicial común.
      * **`Source Address: fe80::a00:27ff:fe2e:c1a9`**: La dirección IPv6 de origen del paquete, que es la dirección Link Local de la Kali Linux VM.
      * **`Destination Address: fe80::224:1539:2bc:c94d`**: La dirección IPv6 de destino del paquete, que es la dirección Link Local de la Windows 10 VM.

    Se expandió la sección **"Internet Control Message Protocol v6"**:

      * **`Type: Echo (ping) request (128)`**: Confirma que el paquete es una solicitud de ping ICMPv6.
      * **`Code: 0`**: El código asociado al tipo de mensaje Echo Request.
      * Otros campos como `Identifier` y `Sequence` (utilizados para emparejar solicitudes con respuestas de ping).

## Importancia para un Analista de Ciberseguridad

Para un analista de ciberseguridad, comprender estos conceptos y herramientas es fundamental:

1.  **Fundamentos de Redes:** Un conocimiento profundo de cómo los paquetes se construyen y viajan a través de la red (Layer 3 - IPv6, Layer 4 - ICMPv6, TCP, UDP) es la base para cualquier análisis de seguridad. Entender los campos de la cabecera no es solo teoría, es saber "leer el lenguaje" de la red.
2.  **Diagnóstico de Problemas:** Ser capaz de interpretar un `Hop Limit` bajo, un `Flow Label` inusual, o un `Next Header` inesperado puede ser la clave para diagnosticar problemas de conectividad, enrutamiento o incluso problemas de rendimiento.
3.  **Análisis de Seguridad y Forensia:**
      * **Detección de Anomalías:** Identificar valores inusuales en campos como `Traffic Class`, `Flow Label`, o `Hop Limit` (si un paquete llega con un `Hop Limit` muy bajo de forma inesperada) puede indicar manipulaciones o ataques.
      * **Identificación de Ataques:** Muchos ataques de red (escaneos, DoS, explotación de vulnerabilidades) dejan huellas en los encabezados de los paquetes. Comprender la estructura normal de un `ping` IPv6 permite detectar variaciones maliciosas.
      * **Investigación Forense:** En un incidente de seguridad, un archivo PCAP es una "caja negra" de lo que ocurrió. La capacidad de un analista para desglosar y entender cada campo de la cabecera IPv6 (y otras cabeceras) es crucial para reconstruir líneas de tiempo de ataques, identificar los métodos del atacante y determinar el alcance de un compromiso.
      * **Conocimiento de IPv6 Específico:** Dada la creciente adopción de IPv6, es imperativo que los analistas de ciberseguridad comprendan sus particularidades, como las direcciones Link Local, la eliminación del campo de suma de verificación del encabezado base (aumentando la eficiencia pero trasladando la responsabilidad a las capas superiores), y la expansión de los encabezados de extensión (que pueden ser usados por atacantes).
4.  **Dominio de Herramientas:** `Wireshark` es la herramienta de facto para el análisis de tráfico de red. Su dominio permite una visibilidad profunda en la red que ninguna otra herramienta puede ofrecer de forma tan granular.
5.  **Desarrollo y Pruebas de Defensa:** Al entender cómo se construyen los paquetes, un analista puede probar la efectividad de sus propias defensas (firewalls, IDS/IPS) contra diferentes tipos de tráfico y ataques.

En resumen, la capacidad de un analista de ciberseguridad para leer y entender la información detallada en los encabezados de paquetes IPv6 y ICMPv6 con herramientas como Wireshark no es solo una habilidad técnica, sino una **capacidad fundamental para la detección, el análisis y la defensa efectiva en las redes modernas**.