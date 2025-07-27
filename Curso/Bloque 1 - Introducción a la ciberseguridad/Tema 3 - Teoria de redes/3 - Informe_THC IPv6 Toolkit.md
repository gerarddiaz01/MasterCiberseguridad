# THC IPv6 Attack Toolkit: Obtención y Uso de Herramientas Clave en Kali Linux

Este informe introduce el **THC IPv6 Attack Toolkit**, una suite de herramientas de código abierto esencial para la evaluación de seguridad en redes IPv6. Se detallará cómo obtener e instalar este *toolkit* y se explicará el uso de tres comandos principales: `atk6-address6`, `atk6-alive6` y `atk6-parasite6`, junto con su sintaxis, objetivo y un ejemplo práctico.

## 1\. Introducción al THC IPv6 Attack Toolkit

El **THC IPv6 Attack Toolkit** (también conocido como el kit de herramientas de ataques IPv6 de THC o "The Hacker's Choice") es un conjunto de herramientas de código abierto diseñado específicamente para realizar **ataques y pruebas de pentesting** en redes IPv6. Desarrollado por el equipo de **The Hacker's Choice (THC)**, es ampliamente utilizado por profesionales de la seguridad para evaluar la robustez de las implementaciones IPv6 y detectar posibles vulnerabilidades.

Este *toolkit* ofrece una amplia gama de ataques, desde el **Neighbor Spoofing** hasta el envío de paquetes de enrutamiento maliciosos.

## 2\. Obtención e Instalación del THC IPv6 Attack Toolkit

Aunque Kali Linux suele incluir el THC IPv6 Toolkit preinstalado, es útil conocer cómo obtenerlo y sus dependencias en caso de necesitar una instalación manual o en otra distribución basada en Debian/Ubuntu.

El proyecto principal se encuentra en GitHub. Es importante notar que, según la información proporcionada, el repositorio principal ha tenido poco desarrollo en los últimos años, aunque sigue siendo funcional.

### 2.1. Dependencias Requeridas

Para compilar las herramientas del *toolkit* desde el código fuente, se necesitan las siguientes librerías:

  * **`lib pcap`**: Librería para captura de paquetes.
  * **`lib ssl`**: Librería para operaciones SSL/TLS.
  * **`libnetfilter_queue`**: Librería para interactuar con la cola de paquetes de Netfilter.

### 2.2. Instalación de Dependencias (Kali, Debian, Ubuntu)

Para instalar las dependencias en sistemas como Kali, Debian o Ubuntu, utiliza el gestor de paquetes `apt`:

```bash
sudo apt install libpcap-dev libssl-dev libnetfilter-queue-dev
```

  * **`sudo`**: Permite ejecutar el comando con privilegios de superusuario, necesario para instalar paquetes.
  * **`apt install`**: Es el comando del gestor de paquetes APT para instalar nuevos paquetes.
  * **`libpcap-dev`**: Paquete de desarrollo de la librería `libpcap`.
  * **`libssl-dev`**: Paquete de desarrollo de la librería `libssl`.
  * **`libnetfilter-queue-dev`**: Paquete de desarrollo de la librería `libnetfilter_queue`.

**Objetivo**: Instalar las librerías de desarrollo necesarias para la compilación de las herramientas del THC IPv6 Toolkit.

### 2.3. Compilación e Instalación desde el Código Fuente

Una vez instaladas las dependencias, si obtuvieras el código fuente (por ejemplo, clonando el repositorio de GitHub), los pasos para compilar e instalar serían:

1.  **Compilación**: Navega al directorio del código fuente y ejecuta:

    ```bash
    make
    ```

      * **`make`**: Es una utilidad que automatiza la compilación de programas a partir de código fuente, siguiendo las instrucciones de un archivo `Makefile`.

2.  **Instalación**: Una vez compilado, para instalar las herramientas en el sistema:

    ```bash
    sudo make install
    ```

      * **`sudo make install`**: Copia los ejecutables y otros archivos necesarios a los directorios del sistema para que puedan ser ejecutados desde cualquier ubicación.

### 2.4. Instalación del Toolkit Completo (Paquete Precompilado)

En distribuciones como Kali Linux, es más sencillo instalar el *toolkit* completo utilizando el paquete precompilado `thc-ipv6`:

```bash
sudo apt install thc-ipv6
```

  * **`sudo apt install thc-ipv6`**: Este comando descarga e instala todas las herramientas precompiladas del THC IPv6 Toolkit, haciéndolas directamente utilizables en la terminal sin necesidad de compilación manual.

**Objetivo**: Instalar rápidamente el conjunto completo de herramientas THC IPv6 en el sistema.

## 3\. Comandos Principales del THC IPv6 Toolkit

Las herramientas del THC IPv6 Toolkit no se ejecutan directamente con `thc`, sino con prefijos como `atk6-`. Podemos explorar las herramientas disponibles buscando `atk6` y luego el nombre específico (ej. `atk6-parasite6`).

A continuación, exploraremos el uso de tres comandos clave del *toolkit*.

### 3.1. `atk6-address6`: Conversión de Direcciones IPv6 y MAC

La herramienta `atk6-address6` permite convertir entre direcciones IPv6 y direcciones MAC, especialmente para direcciones *link-local* de IPv6 que se derivan en gran parte de la dirección MAC.

#### Sintaxis y Uso

```bash
atk6-address6 <IPv6_Address_or_MAC_Address>
```

  * **`atk6-address6`**: Nombre del comando para la conversión de direcciones.
  * **`<IPv6_Address_or_MAC_Address>`**: El argumento puede ser una dirección IPv6 (para obtener la MAC equivalente) o una dirección MAC (para obtener la dirección *link-local* IPv6 equivalente).

**Objetivo**: Obtener la dirección MAC a partir de una dirección IPv6 (especialmente *link-local*) o viceversa.

#### Ejemplo Práctico

1.  **Obtener MAC desde IPv6**:
    Supongamos una dirección IPv6 *link-local* como `fe80::76d3:59ff:fef2:1328`.

    ```bash
    atk6-address6 fe80::76d3:59ff:fef2:1328
    ```

    **Explicación**: El comando procesará la dirección IPv6 proporcionada.
    **Resultado Esperado**: La herramienta mostrará la dirección MAC correspondiente. Notarás que partes de la dirección MAC se corresponden directamente con segmentos de la dirección IPv6 (por ejemplo, `76:d3:59:f2:13:28`). El `ff:fe` en medio de la dirección IPv6 es parte del formato EUI-64 que se usa para derivar direcciones IPv6 de direcciones MAC.

2.  **Obtener IPv6 desde MAC**:
    Si tenemos una dirección MAC, por ejemplo, `de:c3:59:f2:13:28`.

    ```bash
    atk6-address6 de:c3:59:f2:13:28
    ```

    **Explicación**: El comando tomará la dirección MAC y aplicará las reglas de derivación de EUI-64 para generar la dirección IPv6 *link-local* correspondiente.
    **Resultado Esperado**: Mostrará la dirección IPv6 *link-local* generada (ej. `fe80::dec3:59ff:fef2:1328`).

### 3.2. `atk6-alive6`: Descubrimiento de Hosts Vivos

La herramienta `atk6-alive6` se utiliza para descubrir *hosts* que están activos o "vivos" en una red IPv6, enviando paquetes ICMPv6 Echo Request (ping) y esperando respuestas.

#### Sintaxis y Uso

```bash
sudo atk6-alive6 <interface>
```

  * **`sudo`**: Este comando requiere privilegios de superusuario (`root`) para poder interactuar directamente con la interfaz de red y enviar/recibir paquetes RAW. Sin `sudo`, el comando fallará con un error de permisos.
  * **`atk6-alive6`**: Nombre del comando para el escaneo de hosts vivos.
  * **`<interface>`**: La interfaz de red a través de la cual se realizará el escaneo (ej., `eth0` para Ethernet cableada o `wlan0` para Wi-Fi).

**Objetivo**: Identificar los *hosts* IPv6 activos en la red local.

#### Ejemplo Práctico

1.  **Ejecutar el comando**:

    ```bash
    sudo atk6-alive6 eth0
    ```

    **Explicación**: El comando enviará paquetes ICMPv6 Echo Request a direcciones *multicast* o *unicast* en el segmento de red `eth0` y listará los *hosts* que respondan.

2.  **Análisis con Wireshark**: Para comprender mejor cómo funciona `atk6-alive6` a bajo nivel, se puede capturar el tráfico con **Wireshark** simultáneamente.

      * **Abrir Wireshark**: Inicia Wireshark en tu sistema Kali.
      * **Filtrar por IPv6**: En la barra de filtros de visualización, escribe `ipv6` y aplica el filtro para ver solo el tráfico IPv6.
      * **Seleccionar Interfaz**: Elige la interfaz de red `eth0` (o la que estés utilizando) y comienza la captura.

      * **Relanzar `atk6-alive6`**: Vuelve a ejecutar `sudo atk6-alive6 eth0` en la terminal.
      * **Observar en Wireshark**: En Wireshark, verás una serie de paquetes ICMPv6:
          * **Echo Request (Tipo 128)**: Enviados por tu máquina, a menudo a direcciones *multicast* (como `ff02::1` que representa "todos los nodos en el enlace local") para descubrir *routers* y *hosts*.

              * **Tipo**: 128
              * **Fuente**: Tu dirección IPv6 *link-local*.
              * **Destino**: Dirección *multicast* o *unicast*.

          * **Echo Reply (Tipo 129)**: Respuestas de otros *hosts* vivos en la red.

              * **Tipo**: 129
              * **Fuente**: Dirección IPv6 del host que responde.
              * **Destino**: Tu dirección IPv6 *link-local*.

          * También podrás observar mensajes **Neighbor Solicitation (NS)** (Tipo 135) y **Neighbor Advertisement (NA)** (Tipo 136) como parte del proceso de descubrimiento de vecinos del protocolo NDP.

            En un paquete NS, se puede ver la dirección MAC de origen y la dirección IPv6 objetivo. En un paquete NA, se puede ver la dirección MAC del host que responde y la dirección IPv6 del host.

### 3.3. `atk6-parasite6`: Suplantación de Vecinos (Neighbor Spoofing)

La herramienta `atk6-parasite6` es una utilidad para realizar **Neighbor Spoofing** o envenenamiento de vecinos en redes IPv6. Es el equivalente a un **ARP Spoofer** en redes IPv4. Este ataque redirige todo el tráfico local a tu sistema (o a la "nada" si la dirección MAC falsa no existe) respondiendo falsamente a las solicitudes de vecinos (`Neighbor Solicitation`).

#### Sintaxis y Uso

```bash
sudo atk6-parasite6 [-1R] <interface> [<fake-mac>]
```

  * **`sudo`**: Requiere privilegios de superusuario para manipular la red a bajo nivel.
  * **`atk6-parasite6`**: Nombre del comando para realizar el *Neighbor Spoofing*.
  * **`<interface>`**: La interfaz de red por la que se realizará el ataque (ej., `eth0`).
  * **`<fake-mac>` (opcional)**: Una dirección MAC falsa a la que se redirigirá el tráfico. Si no se especifica, se usará la MAC del atacante.

**Opciones Importantes**:

  * **`-1`**: Envía los paquetes por objetivo cada 5 segundos.
  * **`-R`**: Intenta inyectar la información de destino de la solicitud.
  * **`-F`**: Realiza el ataque utilizando paquetes fragmentados para evadir ciertos mecanismos de seguridad (NS security bypass).
  * **`-H`**: Utiliza una cabecera Hop-by-Hop para evadir seguridad.
  * **`-D`**: Utiliza una cabecera de destino grande para evadir seguridad.

**Objetivo**: Interceptar o desviar el tráfico de red IPv6 suplantando la identidad de un vecino legítimo en la red local.

#### Ejemplo Práctico (Concepto)

Aunque el texto no muestra una ejecución explícita de `atk6-parasite6`, describe su propósito y su relación con el *Neighbor Spoofing*.

```bash
sudo atk6-parasite6 eth0
```

**Explicación**: Este comando iniciaría un ataque de *Neighbor Spoofing* en la interfaz `eth0`. El sistema del atacante comenzaría a responder a las solicitudes de vecinos (NS) en nombre de otras máquinas o del *router*, redirigiendo el tráfico destinado a esas direcciones a la máquina del atacante.

**Advertencia**: El `atk6-parasite6` es una herramienta de ataque que puede interrumpir la conectividad de la red y puede ser ilegal si se usa sin autorización. Utilizarla con precaución y solo en entornos controlados y autorizados.

## 4\. Conclusión

El THC IPv6 Attack Toolkit es una colección exhaustiva de herramientas diseñadas para realizar evaluaciones de seguridad en redes IPv6. Proporciona a los investigadores de seguridad un medio para medir la robustez de las implementaciones de IPv6 y la seguridad de las redes que utilizan este protocolo. El *toolkit* ofrece una amplia gama de ataques, desde el *Neighbor Spoofing* hasta el envío de paquetes de enrutamiento maliciosos, permitiendo evaluar la seguridad y mejorar las defensas de las redes IPv6. Es fundamental comprender tanto la funcionalidad como las implicaciones de seguridad de estas herramientas antes de utilizarlas.

-----