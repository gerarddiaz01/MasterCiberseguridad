# Herramientas Fundamentales de Red en Linux para Ciberseguridad

Como analistas de ciberseguridad, dominar las herramientas de red desde la terminal de Linux es esencial para la configuración, diagnóstico, monitoreo y análisis de seguridad de la red. Estas herramientas nos permiten obtener información crucial sobre interfaces de red, rutas, conexiones activas, puertos abiertos y la conectividad general del sistema, lo cual es vital tanto en la fase de reconocimiento como en la respuesta a incidentes.

En esta sesión, exploraremos las principales herramientas de red disponibles en sistemas Unix y Linux: `ifconfig`, `ip`, `route`, `ping`, `fping`, `netstat` y `hping3`.

## 1\. Gestión de Interfaces de Red: `ifconfig` e `ip`

Estas herramientas son fundamentales para visualizar y configurar las interfaces de red de un sistema.

### 1.1. `ifconfig`

El comando `ifconfig` (interface configurator) es una utilidad tradicional utilizada en sistemas Unix y Linux para configurar y visualizar la configuración de interfaces de red. Aunque ha sido parcialmente reemplazado por el comando `ip` en sistemas más modernos, sigue siendo ampliamente utilizado y reconocido.

#### **Funcionalidades Clave:**

  * **Ver y modificar la configuración de red:** Permite configurar direcciones IP, máscaras de red (`netmask`), direcciones de *broadcast*.
  * **Listar interfaces activas:** Muestra las interfaces de red presentes en el sistema, como `eth0` (Ethernet), `wlan0` (Wi-Fi) o `lo` (loopback).
  * **Deshabilitar/Habilitar interfaces:** Permite activar o desactivar interfaces de red.
  * **Mostrar estadísticas de transmisión:** Proporciona datos sobre paquetes enviados (`TX packets`), recibidos (`RX packets`), errores, paquetes caídos, etc.
  * **Ver direcciones MAC:** Muestra la dirección física o **MAC address** de la interfaz.

#### **Sintaxis y Uso:**

  * **Mostrar todas las interfaces:**

    ```bash
    ifconfig
    ```

    Este comando, ejecutado sin argumentos, lista todas las interfaces de red configuradas en el sistema, junto con sus detalles.

    **Ejemplo de Salida (`ifconfig`):**

    ```
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 172.17.249.136  netmask 255.255.240.0  broadcast 172.17.255.255
            inet6 fe80::8561:40f6:6741:200c  prefixlen 64  scopeid 0x20<link>
            ether 00:15:50:00:36:36  txqueuelen 1000  (Ethernet)
            RX packets 44  bytes 16075 (15.6 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 22  bytes 2942 (2.8 KiB)
            TX errors 0  dropped 0  overruns 0  carrier 0  collisions 0

    eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 10.0.0.100  netmask 255.0.0.0  broadcast 10.255.255.255
            ether 00:15:50:00:36:37  txqueuelen 1000  (Ethernet)
            RX packets 1108  bytes 213985 (208.9 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 1336  bytes 69100 (67.4 KiB)
            TX errors 0  dropped 0  overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 8466  bytes 361216 (352.7 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 8466  bytes 361216 (352.7 KiB)
            TX errors 0  dropped 0  overruns 0  carrier 0  collisions 0
    ```

    En este ejemplo, vemos tres interfaces: `eth0`, `eth1` y `lo` (loopback). Se muestra su dirección IP (`inet`), máscara de red (`netmask`), dirección MAC (`ether`), y estadísticas de paquetes.

  * **Configurar una dirección IP manualmente (requiere `sudo`):**

    ```bash
    sudo ifconfig eth1 10.0.0.12 netmask 255.255.255.0
    # O utilizando notación CIDR:
    sudo ifconfig eth1 10.0.0.12/24
    ```

    Esto asigna la IP `10.0.0.12` con una máscara de `255.255.255.0` (o `/24`) a la interfaz `eth1`.

### 1.2. `ip`

El comando `ip` es una utilidad de línea de comandos más moderna y potente en sistemas Unix y Linux, diseñada para reemplazar a `ifconfig` y otras herramientas de red antiguas. `ip` engloba diversas funcionalidades en un solo comando.

#### **Funcionalidades Clave:**

  * **Mostrar y configurar interfaces de red:** Permite gestionar direcciones IP, interfaces (activar/desactivar).
  * **Ver y manipular rutas de red:** Gestión de la tabla de enrutamiento del kernel.
  * **Administrar tablas ARP:** Muestra y modifica la caché ARP.
  * **Configurar reglas de *firewall*:** En algunos contextos, puede interactuar con reglas de Netfilter.

#### **Sintaxis y Uso:**

El comando `ip` utiliza una estructura de objeto-acción. Los objetos comunes incluyen `address` (o `addr` o `a`), `link` (o `l`), `route` (o `r`).

  * **Mostrar direcciones IP y configuraciones de interfaces:**

    ```bash
    ip a
    # o
    ip address show
    ```

    Esta es la alternativa moderna a `ifconfig`. Muestra detalles completos de las interfaces, incluyendo IPs, direcciones MAC, estado (UP, DOWN), etc.

    **Ejemplo de Salida (`ip a`):**

    ```
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host noprefixroute
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether 00:15:50:00:36:36 brd ff:ff:ff:ff:ff:ff
        inet 172.17.249.136/20 brd 172.17.255.255 scope global dynamic noprefixroute eth0
           valid_lft 83477sec preferred_lft 83477sec
        inet6 fe80::8561:40f6:6741:200c/64 scope link noprefixroute
           valid_lft forever preferred_lft forever
    3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether 00:15:50:00:36:37 brd ff:ff:ff:ff:ff:ff
        inet 10.9.3.1/8 brd 10.255.255.255 scope global eth1
           valid_lft forever preferred_lft forever
        inet 10.9.8.1/24 scope global eth1
           valid_lft forever preferred_lft forever
        inet 10.9.9.1/24 scope global secondary eth1
           valid_lft forever preferred_lft forever
        inet 10.0.0.1/24 scope global secondary eth1
           valid_lft forever preferred_lft forever
        inet 10.0.0.12/24 scope global secondary eth1
           valid_lft forever preferred_lft forever
    ```

  * **Añadir una dirección IP a una interfaz (requiere `sudo`):**

    ```bash
    sudo ip address add 10.0.0.30/24 dev eth1
    ```

    Esto añade una dirección IP secundaria a la interfaz `eth1`. Es útil para configuraciones de host virtual o cuando una interfaz necesita comunicarse en múltiples subredes.

  * **Eliminar una dirección IP de una interfaz (requiere `sudo`):**

    ```bash
    sudo ip address del 10.0.0.30/24 dev eth1
    ```

## 2\. Gestión de Rutas de Red: `route` e `ip route`

La tabla de enrutamiento del kernel es esencial para que un sistema sepa por dónde enviar el tráfico hacia diferentes redes.

### 2.1. `route`

El comando `route` se utiliza para mostrar y manipular la tabla de enrutamiento IP del kernel.

#### **Funcionalidades Clave:**

  * **Ver rutas configuradas:** Muestra la tabla de enrutamiento actual del sistema.
  * **Añadir, eliminar o modificar rutas:** Permite especificar por qué *gateway* o interfaz debe pasar el tráfico para alcanzar una red o host específico.

#### **Sintaxis y Uso:**

  * **Mostrar la tabla de enrutamiento:**

    ```bash
    route -n
    ```

    La opción `-n` es crucial para mostrar las direcciones IP numéricamente, en lugar de intentar resolver nombres de host, lo que acelera la visualización y es más directo para un análisis de red.

    **Ejemplo de Salida (`route -n`):**

    ```
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         172.17.240.1    0.0.0.0         UG    100    0        0 eth0
    10.0.0.0        0.0.0.0         255.0.0.0       U     0      0        0 eth1
    172.17.240.0    0.0.0.0         255.255.240.0   U     100    0        0 eth0
    ```

      * **Destination:** La red o host de destino. `0.0.0.0` con `Genmask 0.0.0.0` indica la **ruta por defecto** (todo el tráfico que no coincide con otras rutas).
      * **Gateway:** La IP del *gateway* o router por el que debe salir el tráfico. `0.0.0.0` indica que el destino está directamente conectado a la interfaz.
      * **Genmask:** La máscara de red.
      * **Flags:** Indicadores como `U` (Up - ruta activa) y `G` (Gateway - la ruta utiliza un *gateway*).
      * **Iface:** La interfaz de red que se utilizará para esta ruta.

  * **Añadir una ruta a una red específica:**

    ```bash
    sudo route add -net 11.0.0.0 netmask 255.255.255.0 gw 10.0.0.1
    # O utilizando notación CIDR con ip route:
    sudo ip route add 11.0.0.0/24 via 10.0.0.1
    ```

    Esto le dice al sistema que, para alcanzar cualquier dirección en la red `11.0.0.0/24`, debe enviar el tráfico a `10.0.0.1` (que se asume es un *gateway* o router).

  * **Eliminar una ruta:**

    ```bash
    sudo route del -net 11.0.0.0 netmask 255.255.255.0 gw 10.0.0.1
    # O utilizando ip route:
    sudo ip route del 11.0.0.0/24
    ```

  * **Añadir o eliminar la ruta por defecto:**
    La **ruta por defecto** (`default gateway`) es crucial porque define por dónde se envía todo el tráfico que no coincide con ninguna otra ruta más específica en la tabla.

    ```bash
    sudo route add default gw 10.0.0.1
    sudo route del default gw 172.17.240.1
    ```

### 2.2. `ip route`

Como parte del comando `ip`, la subcomando `route` también gestiona la tabla de enrutamiento y es la forma preferida en sistemas modernos.

#### **Sintaxis y Uso:**

  * **Mostrar la tabla de enrutamiento:**

    ```bash
    ip route show
    ```

    Esta es la alternativa moderna y más potente a `route -n`.

    **Ejemplo de Salida (`ip route show`):**

    ```
    default via 172.17.240.1 dev eth0 proto dhcp src 172.17.249.136 metric 100
    10.0.0.0/8 dev eth1 proto kernel scope link src 10.9.3.1
    172.17.240.0/20 dev eth0 proto kernel scope link src 172.17.249.136 metric 100
    ```

  * **Añadir una ruta:**

    ```bash
    sudo ip route add 11.0.0.0/24 via 10.0.0.1
    ```

  * **Eliminar una ruta:**

    ```bash
    sudo ip route del 11.0.0.0/24
    ```

## 3\. Verificación de Conectividad: `ping` y `fping`

Estas herramientas se utilizan para verificar la conectividad de red entre dispositivos.

### 3.1. `ping`

El comando `ping` es una herramienta fundamental para verificar la conectividad de red entre dos dispositivos. Funciona enviando paquetes **ICMP Echo Request** y esperando respuestas **ICMP Echo Reply**.

#### **Funcionalidades Clave:**

  * **Comprobar accesibilidad de un host remoto:** Determina si una máquina está "viva" y es accesible en la red.
  * **Calcular tiempo de ida y vuelta (RTT):** Mide el tiempo que tarda un paquete en viajar al destino y regresar.
  * **Determinar número de saltos (TTL):** El valor **TTL** (Time To Live) en el encabezado IP puede dar una indicación del número de routers (saltos) entre el origen y el destino.

#### **Sintaxis y Uso:**

  * **Ping básico a un host:**

    ```bash
    ping 10.0.0.100
    ```

    Este comando enviará continuamente paquetes **ICMP** hasta que se detenga manualmente (Ctrl+C).

    **Ejemplo de Salida (`ping 10.0.0.100`):**

    ```
    PING 10.0.0.100 (10.0.0.100) 56(84) bytes of data.
    64 bytes from 10.0.0.100: icmp_seq=1 ttl=64 time=0.033 ms
    64 bytes from 10.0.0.100: icmp_seq=2 ttl=64 time=0.023 ms
    64 bytes from 10.0.0.100: icmp_seq=3 ttl=64 time=0.027 ms

    --- 10.0.0.100 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2032ms
    rtt min/avg/max/mdev = 0.023/0.027/0.033/0.004 ms
    ```

    La salida muestra que se enviaron 3 paquetes, los 3 fueron recibidos sin pérdida, y proporciona las estadísticas de tiempo. Un `TTL` de 64 o 128 es común para sistemas Linux y Windows, respectivamente, y decrece con cada salto de router.

  * **Enviar un número específico de paquetes:**

    ```bash
    ping -c 2 10.0.0.20
    ```

    La opción `-c` (count) especifica el número de paquetes a enviar. Es útil para pruebas rápidas sin inundar la red.

    **Ejemplo de Salida (`ping -c 2 10.0.0.20`):**

    ```
    PING 10.0.0.20 (10.0.0.20) 56(84) bytes of data.
    64 bytes from 10.0.0.20: icmp_seq=1 ttl=64 time=0.561 ms
    64 bytes from 10.0.0.20: icmp_seq=2 ttl=64 time=0.986 ms

    --- 10.0.0.20 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1021ms
    rtt min/avg/max/mdev = 0.561/0.773/0.986/0.212 ms
    ```

### 3.2. `fping`

`fping` es una herramienta avanzada similar a `ping`, pero con la capacidad de enviar múltiples paquetes **ICMP Echo Request** a múltiples hosts de forma simultánea. Es extremadamente útil para escanear rangos de direcciones IP y determinar qué hosts están activos.

#### **Funcionalidades Clave:**

  * **Ping a múltiples hosts:** Permite especificar una lista de IPs o un rango de red.
  * **Escaneo de rangos IP:** Puede escanear automáticamente un rango de direcciones para identificar hosts activos.
  * **Informes concisos:** Puede configurarse para mostrar solo los hosts que responden o los que están inactivos.
  * **Detección de hosts activos:** Muy útil en la fase de reconocimiento de un pentesting o análisis de red.

#### **Sintaxis y Uso:**

  * **Ping a una lista de hosts:**

    ```bash
    fping 10.0.0.1 10.0.0.20 10.0.0.100
    ```

    **Ejemplo de Salida (`fping 10.0.0.1 10.0.0.20 10.0.0.100`):**

    ```
    10.0.0.20 is alive
    10.0.0.100 is alive
    ICMP Host Unreachable from 10.0.0.100 for ICMP Echo sent to 10.0.0.1
    ICMP Host Unreachable from 10.0.0.100 for ICMP Echo sent to 10.0.0.1
    ICMP Host Unreachable from 10.0.0.100 for ICMP Echo sent to 10.0.0.1
    ICMP Host Unreachable from 10.0.0.100 for ICMP Echo sent to 10.0.0.1
    10.0.0.1 is unreachable
    ```

    En este caso, `10.0.0.20` y `10.0.0.100` están activos, mientras que `10.0.0.1` no es alcanzable.

  * **Enviar solo 1 paquete a cada host y mostrar un resumen:**

    ```bash
    fping -c 1 10.0.0.1 10.0.0.100
    ```

    **Ejemplo de Salida (`fping -c 1 10.0.0.1 10.0.0.100`):**

    ```
    10.0.0.100: [0], 64 bytes, 0.033 ms (0.033 avg, 0% loss)
    10.0.0.1 : [0], timed out (NaN avg, 100% loss)

    10.0.0.1   : xmt/rcv/%loss = 1/0/100%
    10.0.0.100 : xmt/rcv/%loss = 1/1/0%, min/avg/max = 0.033/0.033/0.033
    ```

  * **Escaneo de un rango de direcciones IP (usando `-g` para generar rangos):**

    ```bash
    fping -g 10.0.0.1 10.0.0.20
    ```

    Esto escaneará todas las IPs desde `10.0.0.1` hasta `10.0.0.20`.
    **Ejemplo de Salida (`fping -g 10.0.0.1 10.0.0.20`):**

    ```
    10.0.0.12 is alive
    10.0.0.20 is alive
    # ... (y el resto indicarán 'unreachable')
    ```

    Los mensajes "ICMP Host Unreachable" o "is unreachable" indican que el host no respondió a la solicitud ICMP. Esto podría deberse a que la máquina está apagada, no existe, o un *firewall* está bloqueando el tráfico ICMP.

## 4\. Análisis de Conexiones y Puertos: `netstat`

El comando `netstat` (network statistics) es una herramienta versátil para mostrar información detallada sobre las conexiones de red, tablas de enrutamiento, estadísticas de interfaz y otros datos relacionados con la red en un sistema. Es una herramienta clave para la auditoría de seguridad y la detección de actividad sospechosa.

#### **Funcionalidades Clave:**

  * **Conexiones activas:** Muestra las conexiones TCP y UDP activas.
  * **Puertos abiertos/escucha:** Identifica qué puertos están abiertos y a la espera de conexiones (`LISTEN`).
  * **Establecimiento de conexiones:** Muestra las conexiones establecidas (`ESTABLISHED`).
  * **Procesos asociados:** Permite ver qué procesos (`PID/Program name`) están utilizando qué puertos o conexiones.
  * **Estadísticas de interfaz:** Ofrece estadísticas de tráfico para cada interfaz de red.

#### **Sintaxis y Uso:**

`netstat` se utiliza con varias opciones para filtrar y formatear la salida:

  * **Mostrar todas las conexiones activas y puertos en escucha (numérico, TCP, UDP, con procesos):**

    ```bash
    netstat -tulpn
    ```

      * `-t`: Muestra conexiones **TCP**.
      * `-u`: Muestra conexiones **UDP**.
      * `-l`: Muestra sockets en estado de **LISTEN** (puertos a la escucha).
      * `-p`: Muestra el **PID** (Process ID) y el nombre del programa asociado al socket. (Requiere privilegios de root para ver todos los procesos).
      * `-n`: Muestra las direcciones y números de puerto **numéricamente**, sin intentar resolver nombres de host o nombres de servicio. Esto es vital para un análisis rápido y para evitar ralentizaciones por DNS o búsquedas de servicios.

    **Ejemplo de Salida (`netstat -tulpn`):**

    ```
    (Not all processes could be identified, non-owned process info
    will not be shown, you would have to be root to see it all.)
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 0.0.0.0:22              0.0.0.0:* LISTEN      -
    tcp6       0      0 :::22                   :::* LISTEN      -
    tcp6       0      0 ::1:3350                :::* LISTEN      -
    ```

    En este ejemplo, vemos que el puerto `22` (SSH) está a la escucha tanto en **IPv4** (`0.0.0.0:22`) como en **IPv6** (`:::22`). También hay un proceso a la escucha en el puerto `3350` en `::1` (localhost IPv6). Como analista, esta es una de las primeras verificaciones para identificar servicios expuestos.

  * **Mostrar solo conexiones TCP en escucha con PID y nombres de servicio:**

    ```bash
    sudo netstat -ltp
    ```

    Esta combinación es muy útil para ver rápidamente qué servicios TCP están activos y escuchando conexiones en el sistema.

  * **Mostrar solo conexiones UDP en escucha:**

    ```bash
    sudo netstat -lup
    ```

  * **Mostrar estadísticas de interfaces:**

    ```bash
    netstat -i
    ```

    Muestra estadísticas por interfaz, incluyendo paquetes recibidos/enviados y errores.

  * **Mostrar tabla de enrutamiento:**

    ```bash
    netstat -r
    ```

    Esta es otra forma de ver la tabla de enrutamiento, similar a `route -n` o `ip route show`.

## 5\. Escaneo de Puertos Avanzado y Creación de Paquetes: `hping3`

`hping3` es una utilidad de red avanzada que permite a los usuarios construir y enviar paquetes **TCP/IP** personalizados, lo que la convierte en una herramienta invaluable para pruebas de penetración, *firewall testing* y análisis de red. Es mucho más potente que `ping` o `fping`, ya que permite un control granular sobre los paquetes.

#### **Funcionalidades Clave:**

  * **Envío de paquetes ICMP, TCP y UDP:** Permite especificar el tipo de paquete.
  * **Configuración avanzada de paquetes:** Control total sobre puertos de origen/destino, tamaños de paquete, banderas **TCP** (SYN, ACK, PSH, URG, FIN, RST), y campos de cabecera personalizados.
  * **Escaneo de puertos:** Muy eficiente para identificar puertos abiertos, cerrados o filtrados.
  * **Pruebas de *firewall*:** Permite probar las reglas de filtrado de un *firewall*.
  * **Simulación de ataques:** Puede simular ataques **DDoS** (Distributed Denial of Service) o ataques de **inundación SYN**.
  * **Detección de *host* activo (fingerprinting):** Analizando las respuestas, puede ayudar a identificar el sistema operativo del host remoto.

#### **Sintaxis y Uso:**

`hping3` es una herramienta muy versátil con numerosas opciones. Requiere `sudo` para la mayoría de sus funciones.

  * **Escaneo de puertos TCP SYN para un rango específico:**

    ```bash
    sudo hping3 -c 1 -faster -S -scan 20-500 10.0.0.20
    ```

      * `sudo`: Se requiere para ejecutar `hping3` con la capacidad de crear paquetes *raw*.
      * `-c 1`: Envía 1 paquete a cada puerto.
      * `-faster`: Aumenta la velocidad de envío de paquetes (más rápido que el modo por defecto, pero menos que `-fastest`).
      * `-S`: Envía paquetes con la bandera **SYN** activa (típico para escaneos de puertos SYN).
      * `-scan 20-500`: Especifica el rango de puertos a escanear, del 20 al 500.
      * `10.0.0.20`: La dirección IP del objetivo.

    **Ejemplo de Salida (`sudo hping3 -c 1 -faster -S -scan 20-500 10.0.0.20`):**

    ```
    Scanning 10.0.0.20 (10.0.0.20), port 20-500
    481 ports to scan, use -V to see all the replies

    PORT  SERV NAME  FLAGS  TTL  ID  WIN  LEN
    22    ssh        .S..A...  64   0   29200  44
    80    http       .S..A...  64   0   29200  44

    All replies received. Done.
    Not responding ports:
    ```

    La salida muestra que los puertos `22` (**SSH**) y `80` (**HTTP**) están abiertos en `10.0.0.20`, ya que se recibió una respuesta SYN-ACK (indicada por las banderas `SA`). Los puertos que no responden no están listados aquí, a menos que se use la opción `-V`. Esto es invaluable para la **enumeración de servicios** y la identificación de puntos de entrada potenciales en un objetivo.

  * **Otras opciones comunes de `hping3` (para analistas de ciberseguridad):**

      * `-p <puerto>`: Especifica el puerto de destino.
      * `-s <puerto_origen>`: Especifica el puerto de origen.
      * `--flood`: Envía paquetes tan rápido como sea posible, sin mostrar respuestas. Útil para pruebas de **DDoS** (siempre con autorización).
      * `-V`: Muestra todas las respuestas, incluyendo las de puertos cerrados (RST).
      * `--rand-source`: Utiliza una dirección IP de origen aleatoria (para ofuscación).
      * `-d <tamaño_datos>`: Establece el tamaño de los datos del paquete.
      * `-rand-dest`: Genera direcciones IP de destino aleatorias.
      * `--traceroute`: Realiza un *traceroute* con paquetes TCP o UDP.

`hping3` es una verdadera "navaja suiza" para la red, permitiendo a los analistas ir más allá de las simples comprobaciones de conectividad y realizar pruebas más sofisticadas que son críticas en entornos de ciberseguridad.

## Conclusiones

El dominio de estas herramientas de línea de comandos en Linux es fundamental para cualquier profesional de la ciberseguridad. Permiten:

  * **Reconocimiento:** Identificar hosts activos, puertos abiertos y servicios en ejecución en una red objetivo.
  * **Diagnóstico:** Solucionar problemas de conectividad y configuración de red.
  * **Monitoreo:** Observar el tráfico de red, las conexiones activas y el estado de las interfaces.
  * **Pruebas de Seguridad:** Evaluar la robustez de los *firewalls*, detectar vulnerabilidades y simular diferentes tipos de ataques.

Siempre recuerda utilizar estas herramientas en entornos controlados y con la debida autorización para evitar consecuencias no deseadas. Practicar con ellas en un laboratorio personal es la mejor manera de asentar estos conocimientos.